#!/usr/bin/env python3
"""Generate per-version test indexes from ocs-ci release branches.

Scans each release-X.Y branch in the ocs-ci repo using AST parsing and
produces test-index-X.Y.json files for the codebase map.

Usage:
    python scripts/update_map.py --ocs-ci-path ~/codcod/new-ocs-ci/ocs-ci --all
    python scripts/update_map.py --ocs-ci-path ~/codcod/new-ocs-ci/ocs-ci --version 4.20
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# AST scanner (adapted from odf-zstream-agents/tools/ocs_ci_scanner.py)
# ---------------------------------------------------------------------------


def scan_all_tests(ocs_ci_root: Path) -> list[dict]:
    tests_dir = ocs_ci_root / "tests"
    if not tests_dir.exists():
        print(f"  WARNING: tests/ not found in {ocs_ci_root}")
        return []

    test_files = sorted(tests_dir.rglob("test_*.py"))
    results = []
    for test_file in test_files:
        try:
            file_info = _parse_test_file(test_file, ocs_ci_root)
            if file_info and file_info.get("test_functions"):
                results.append(file_info)
        except Exception as e:
            pass  # skip unparseable files silently
    return results


def _parse_test_file(file_path: Path, ocs_ci_root: Path) -> dict | None:
    try:
        source = file_path.read_text(errors="ignore")
        tree = ast.parse(source, filename=str(file_path))
    except SyntaxError:
        return None

    rel_path = str(file_path.relative_to(ocs_ci_root))
    file_marks = []
    file_squad = ""
    test_functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_marks = _extract_decorators(node)
            class_squad = _find_squad(class_marks)
            if class_squad:
                file_squad = class_squad
            file_marks.extend(class_marks)

            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if item.name.startswith("test_"):
                        func_info = _extract_function_info(item, node.name, class_marks)
                        test_functions.append(func_info)

        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name.startswith("test_") and node.col_offset == 0:
                func_marks = _extract_decorators(node)
                func_squad = _find_squad(func_marks)
                if func_squad and not file_squad:
                    file_squad = func_squad
                file_marks.extend(func_marks)
                func_info = _extract_function_info(node, None, [])
                test_functions.append(func_info)

    if not test_functions:
        return None

    keywords = set()
    for func in test_functions:
        for word in func["name"].replace("test_", "").split("_"):
            if len(word) > 2:
                keywords.add(word.lower())
        for word in func.get("docstring", "").lower().split():
            if len(word) > 3:
                keywords.add(word)

    parts = rel_path.split("/")
    category = parts[1] if len(parts) > 2 else "root"
    subcategory = parts[2] if len(parts) > 3 else ""
    all_marks = list(set(file_marks))

    return {
        "file_path": rel_path,
        "category": category,
        "subcategory": subcategory,
        "squad": file_squad,
        "test_count": len(test_functions),
        "test_functions": test_functions,
        "marks": all_marks,
        "tiers": _extract_tiers(all_marks),
        "polarion_ids": _extract_polarion_ids(all_marks),
        "skip_conditions": _extract_skip_conditions(all_marks),
        "keywords": sorted(keywords)[:30],
        "description": _file_description(test_functions, rel_path),
    }


def _extract_function_info(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
    class_name: str | None,
    class_marks: list[str],
) -> dict:
    marks = _extract_decorators(node)
    all_marks = list(set(marks + class_marks))
    docstring = ast.get_docstring(node) or ""
    if len(docstring) > 200:
        docstring = docstring[:200] + "..."
    node_id = f"{class_name}::{node.name}" if class_name else node.name
    return {
        "name": node.name,
        "node_id": node_id,
        "marks": all_marks,
        "docstring": docstring,
        "line": node.lineno,
    }


def _extract_decorators(node: ast.AST) -> list[str]:
    marks = []
    for dec in getattr(node, "decorator_list", []):
        mark_str = _decorator_to_string(dec)
        if mark_str:
            marks.append(mark_str)
    return marks


def _decorator_to_string(dec: ast.AST) -> str:
    if isinstance(dec, ast.Name):
        return dec.id
    elif isinstance(dec, ast.Attribute):
        parts = []
        current = dec
        while isinstance(current, ast.Attribute):
            parts.append(current.attr)
            current = current.value
        if isinstance(current, ast.Name):
            parts.append(current.id)
        return ".".join(reversed(parts))
    elif isinstance(dec, ast.Call):
        func_str = _decorator_to_string(dec.func)
        args = []
        for arg in dec.args:
            if isinstance(arg, ast.Constant):
                args.append(repr(arg.value))
            elif isinstance(arg, ast.Name):
                args.append(arg.id)
        if args:
            return f"{func_str}({', '.join(args)})"
        return func_str
    return ""


def _find_squad(marks: list[str]) -> str:
    for mark in marks:
        if "_squad" in mark and not mark.startswith("pytest.mark."):
            return mark
        if "pytest.mark." in mark and "_squad" in mark:
            return mark.split("pytest.mark.")[-1].split("(")[0]
    return ""


def _extract_tiers(marks: list[str]) -> list[str]:
    tiers = []
    for mark in marks:
        for tier in ["tier0", "tier1", "tier2", "tier3", "tier4", "tier4a", "tier4b", "tier4c"]:
            if tier in mark.lower():
                tiers.append(tier)
    return sorted(set(tiers))


def _extract_polarion_ids(marks: list[str]) -> list[str]:
    ids = []
    for mark in marks:
        match = re.findall(r"OCS-\d+", mark)
        ids.extend(match)
    return ids


def _extract_skip_conditions(marks: list[str]) -> list[str]:
    conditions = []
    for mark in marks:
        if "skipif" in mark.lower() or "skip_" in mark.lower():
            conditions.append(mark)
    return conditions


def _file_description(test_functions: list[dict], rel_path: str) -> str:
    if not test_functions:
        return ""
    for func in test_functions:
        ds = func.get("docstring", "")
        if ds and len(ds) > 10:
            first_line = ds.split("\n")[0].strip()
            if len(first_line) > 10:
                return first_line[:150]
    func_names = [f["name"].replace("test_", "") for f in test_functions[:5]]
    return ", ".join(func_names)[:150]


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------


def get_current_ref(repo_path: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo_path, capture_output=True, text=True, timeout=10,
    )
    return result.stdout.strip()


def is_dirty(repo_path: Path) -> bool:
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=repo_path, capture_output=True, text=True, timeout=10,
    )
    return bool(result.stdout.strip())


def stash_changes(repo_path: Path) -> bool:
    result = subprocess.run(
        ["git", "stash", "push", "-m", "update_map.py auto-stash"],
        cwd=repo_path, capture_output=True, text=True, timeout=30,
    )
    return "Saved working directory" in result.stdout


def stash_pop(repo_path: Path):
    subprocess.run(
        ["git", "stash", "pop"],
        cwd=repo_path, capture_output=True, text=True, timeout=30,
    )


def checkout_branch(repo_path: Path, version: str) -> bool:
    branch = f"upstream/release-{version}"
    subprocess.run(
        ["git", "fetch", "upstream", f"release-{version}"],
        cwd=repo_path, capture_output=True, text=True, timeout=120,
    )
    result = subprocess.run(
        ["git", "checkout", branch],
        cwd=repo_path, capture_output=True, text=True, timeout=30,
    )
    return result.returncode == 0


def restore_ref(repo_path: Path, ref: str):
    subprocess.run(
        ["git", "checkout", ref],
        cwd=repo_path, capture_output=True, text=True, timeout=30,
    )


# ---------------------------------------------------------------------------
# Index generation
# ---------------------------------------------------------------------------


def build_index_json(
    results: list[dict], ocs_ci_root: Path, version: str,
) -> dict:
    return {
        "source": "https://github.com/red-hat-storage/ocs-ci",
        "branch": f"release-{version}",
        "scanned_at": datetime.now(timezone.utc).isoformat(),
        "total_files": len(results),
        "total_tests": sum(r["test_count"] for r in results),
        "files": results,
    }


def generate_version_summary(indexes: dict[str, dict]) -> dict:
    versions = sorted(
        indexes.keys(), key=lambda v: tuple(int(x) for x in v.split(".")),
    )

    per_version = []
    for v in versions:
        idx = indexes[v]
        per_version.append({
            "version": v,
            "branch": f"release-{v}",
            "total_files": idx["total_files"],
            "total_tests": idx["total_tests"],
            "scanned_at": idx["scanned_at"],
        })

    diffs = []
    for i in range(1, len(versions)):
        prev_v, curr_v = versions[i - 1], versions[i]
        prev_files = {f["file_path"] for f in indexes[prev_v]["files"]}
        curr_files = {f["file_path"] for f in indexes[curr_v]["files"]}
        diffs.append({
            "from_version": prev_v,
            "to_version": curr_v,
            "added_files": sorted(curr_files - prev_files),
            "removed_files": sorted(prev_files - curr_files),
            "added_count": len(curr_files - prev_files),
            "removed_count": len(prev_files - curr_files),
        })

    return {"versions": per_version, "diffs": diffs}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate per-version test indexes from ocs-ci release branches.",
    )
    p.add_argument(
        "--ocs-ci-path", type=Path, required=True,
        help="Path to local ocs-ci git repo",
    )

    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--version", type=str,
        help="Scan a single release branch (e.g., 4.20)",
    )
    group.add_argument(
        "--all", action="store_true",
        help="Scan all release branches",
    )

    p.add_argument("--min-version", type=str, default="4.10")
    p.add_argument("--max-version", type=str, default="4.21")
    p.add_argument(
        "--output-dir", type=Path, default=None,
        help="Output directory (default: map repo root)",
    )
    return p.parse_args()


def version_range(min_v: str, max_v: str) -> list[str]:
    min_major, min_minor = (int(x) for x in min_v.split("."))
    max_major, max_minor = (int(x) for x in max_v.split("."))
    versions = []
    for minor in range(min_minor, max_minor + 1):
        versions.append(f"{min_major}.{minor}")
    return versions


def main():
    args = parse_args()
    ocs_ci_path = args.ocs_ci_path.expanduser().resolve()

    if not (ocs_ci_path / ".git").exists():
        print(f"ERROR: {ocs_ci_path} is not a git repository")
        sys.exit(1)

    did_stash = False
    if is_dirty(ocs_ci_path):
        print("Stashing uncommitted changes in ocs-ci repo...")
        did_stash = stash_changes(ocs_ci_path)
        if not did_stash:
            print("ERROR: Failed to stash changes. Commit or stash manually first.")
            sys.exit(1)

    output_dir = args.output_dir or Path(__file__).resolve().parent.parent
    original_ref = get_current_ref(ocs_ci_path)

    if args.version:
        versions = [args.version]
    else:
        versions = version_range(args.min_version, args.max_version)

    print(f"ocs-ci repo: {ocs_ci_path}")
    print(f"Output dir:  {output_dir}")
    print(f"Versions:    {', '.join(versions)}")
    print()

    indexes: dict[str, dict] = {}

    try:
        for version in versions:
            print(f"[{version}] Checking out upstream/release-{version}...")
            if not checkout_branch(ocs_ci_path, version):
                print(f"[{version}] WARNING: branch not found, skipping")
                continue

            print(f"[{version}] Scanning test files...")
            results = scan_all_tests(ocs_ci_path)
            index_data = build_index_json(results, ocs_ci_path, version)
            indexes[version] = index_data

            out_file = output_dir / f"test-index-{version}.json"
            with open(out_file, "w") as f:
                json.dump(index_data, f, indent=2)

            print(
                f"[{version}] -> {out_file.name} "
                f"({index_data['total_files']} files, "
                f"{index_data['total_tests']} tests)"
            )

        if not indexes:
            print("\nNo indexes generated.")
            return

        # Update default test-index.json with the latest version
        latest = max(
            indexes.keys(),
            key=lambda v: tuple(int(x) for x in v.split(".")),
        )
        default_index = output_dir / "test-index.json"
        shutil.copy2(
            output_dir / f"test-index-{latest}.json", default_index,
        )
        print(f"\ntest-index.json updated to release-{latest}")

        # Generate version summary
        if len(indexes) > 1:
            summary = generate_version_summary(indexes)
            summary_file = output_dir / "version-summary.json"
            with open(summary_file, "w") as f:
                json.dump(summary, f, indent=2)
            print(f"version-summary.json written ({len(summary['diffs'])} diffs)")

            # Print diff highlights
            print("\nVersion diffs:")
            for d in summary["diffs"]:
                added = d["added_count"]
                removed = d["removed_count"]
                if added or removed:
                    print(
                        f"  {d['from_version']} -> {d['to_version']}: "
                        f"+{added} -{removed} files"
                    )

    finally:
        print(f"\nRestoring original ref {original_ref[:12]}...")
        restore_ref(ocs_ci_path, original_ref)
        if did_stash:
            print("Restoring stashed changes...")
            stash_pop(ocs_ci_path)

    print("Done.")


if __name__ == "__main__":
    main()
