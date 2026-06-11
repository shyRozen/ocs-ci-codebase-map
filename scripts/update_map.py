#!/usr/bin/env python3
"""Generate per-version map branches from ocs-ci release branches.

For each ocs-ci release branch, creates a matching branch in the map repo
with test-index.json + full Obsidian notes (dashboard, squads, components,
test areas, framework).

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
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# AST scanner
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
            info = _parse_test_file(test_file, ocs_ci_root)
            if info and info.get("test_functions"):
                results.append(info)
        except Exception:
            pass
    return results


def scan_markers(ocs_ci_root: Path) -> dict:
    """Parse pytest.ini and marks.py to extract marker info."""
    result = {
        "ini_markers": [],
        "marks_py_markers": [],
        "squad_marks": [],
        "skip_marks": [],
    }
    ini_path = ocs_ci_root / "pytest.ini"
    if ini_path.exists():
        in_markers = False
        for line in ini_path.read_text(errors="ignore").splitlines():
            if line.strip().startswith("markers"):
                in_markers = True
                continue
            if in_markers:
                stripped = line.strip()
                if not stripped or (
                    not line.startswith(" ") and not line.startswith("\t")
                ):
                    in_markers = False
                    continue
                parts = stripped.split(":", 1)
                name = parts[0].strip()
                desc = parts[1].strip() if len(parts) > 1 else ""
                result["ini_markers"].append(
                    {"name": name, "description": desc}
                )
    marks_path = (
        ocs_ci_root
        / "ocs_ci"
        / "framework"
        / "pytest_customization"
        / "marks.py"
    )
    if marks_path.exists():
        for line in marks_path.read_text(errors="ignore").splitlines():
            stripped = line.strip()
            if (
                "pytest.mark." in stripped
                and "=" in stripped
                and not stripped.startswith("#")
            ):
                name = stripped.split("=")[0].strip()
                if name and name.isidentifier():
                    if "_squad" in name:
                        result["squad_marks"].append(name)
                    elif "skipif" in name or "skip_" in name:
                        result["skip_marks"].append(name)
                    else:
                        result["marks_py_markers"].append(name)
    return result


def scan_framework(ocs_ci_root: Path) -> list[dict]:
    fw_dirs = {
        "core": ocs_ci_root / "ocs_ci" / "framework",
        "ocs": ocs_ci_root / "ocs_ci" / "ocs",
        "deployment": ocs_ci_root / "ocs_ci" / "deployment",
        "utility": ocs_ci_root / "ocs_ci" / "utility",
        "helpers": ocs_ci_root / "ocs_ci" / "helpers",
    }
    results = []
    for name, fdir in fw_dirs.items():
        if not fdir.exists():
            continue
        modules = []
        total_lines = 0
        for pf in sorted(fdir.glob("*.py")):
            try:
                lines = len(pf.read_text(errors="ignore").splitlines())
                total_lines += lines
                modules.append({"file": pf.name, "lines": lines})
            except Exception:
                pass
        subdirs = sorted(
            d.name
            for d in fdir.iterdir()
            if d.is_dir() and not d.name.startswith("__")
        )
        results.append(
            {
                "name": name,
                "path": str(fdir.relative_to(ocs_ci_root)),
                "module_count": len(modules),
                "total_lines": total_lines,
                "modules": sorted(modules, key=lambda m: -m["lines"])[:15],
                "subdirs": subdirs,
            }
        )
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
                        test_functions.append(
                            _extract_function_info(item, node.name, class_marks)
                        )
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name.startswith("test_") and node.col_offset == 0:
                func_marks = _extract_decorators(node)
                func_squad = _find_squad(func_marks)
                if func_squad and not file_squad:
                    file_squad = func_squad
                file_marks.extend(func_marks)
                test_functions.append(_extract_function_info(node, None, []))

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

    sorted_keywords = sorted(keywords)[:30]
    component = _classify_component(
        rel_path, sorted_keywords, file_path.name,
    )

    return {
        "file_path": rel_path,
        "category": category,
        "subcategory": subcategory,
        "squad": file_squad,
        "component": component,
        "test_count": len(test_functions),
        "test_functions": test_functions,
        "marks": all_marks,
        "tiers": _extract_tiers(all_marks),
        "polarion_ids": _extract_polarion_ids(all_marks),
        "skip_conditions": _extract_skip_conditions(all_marks),
        "keywords": sorted_keywords,
        "description": _file_description(test_functions, rel_path),
    }


def _extract_function_info(node, class_name, class_marks):
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


def _extract_decorators(node):
    marks = []
    for dec in getattr(node, "decorator_list", []):
        s = _decorator_to_string(dec)
        if s:
            marks.append(s)
    return marks


def _decorator_to_string(dec):
    if isinstance(dec, ast.Name):
        return dec.id
    if isinstance(dec, ast.Attribute):
        parts = []
        cur = dec
        while isinstance(cur, ast.Attribute):
            parts.append(cur.attr)
            cur = cur.value
        if isinstance(cur, ast.Name):
            parts.append(cur.id)
        return ".".join(reversed(parts))
    if isinstance(dec, ast.Call):
        func_str = _decorator_to_string(dec.func)
        args = []
        for a in dec.args:
            if isinstance(a, ast.Constant):
                args.append(repr(a.value))
            elif isinstance(a, ast.Name):
                args.append(a.id)
        if args:
            return f"{func_str}({', '.join(args)})"
        return func_str
    return ""


def _find_squad(marks):
    for m in marks:
        if "_squad" in m and not m.startswith("pytest.mark."):
            return m
        if "pytest.mark." in m and "_squad" in m:
            return m.split("pytest.mark.")[-1].split("(")[0]
    return ""


def _extract_tiers(marks):
    tiers = set()
    for m in marks:
        for t in (
            "tier0",
            "tier1",
            "tier2",
            "tier3",
            "tier4",
            "tier4a",
            "tier4b",
            "tier4c",
        ):
            if t in m.lower():
                tiers.add(t)
    return sorted(tiers)


def _extract_polarion_ids(marks):
    ids = []
    for m in marks:
        ids.extend(re.findall(r"OCS-\d+", m))
    return ids


def _extract_skip_conditions(marks):
    return [m for m in marks if "skipif" in m.lower() or "skip_" in m.lower()]


def _file_description(test_functions, rel_path):
    for func in test_functions:
        ds = func.get("docstring", "")
        if ds and len(ds) > 10:
            first_line = ds.split("\n")[0].strip()
            if len(first_line) > 10:
                return first_line[:150]
    names = [f["name"].replace("test_", "") for f in test_functions[:5]]
    return ", ".join(names)[:150]


# ---------------------------------------------------------------------------
# Component classification
# ---------------------------------------------------------------------------

# Directory → component (most specific first)
_DIR_COMPONENT_MAP = {
    "tests/functional/object/mcg/": "mcg",
    "tests/functional/object/rgw/": "rgw",
    "tests/functional/pv/": "ceph-csi",
    "tests/functional/storageclass/": "ceph-csi",
    "tests/functional/monitoring/": "monitoring",
    "tests/functional/encryption/": "encryption",
    "tests/functional/lvmo/": "lvmo",
    "tests/functional/disaster-recovery/": "disaster-recovery",
    "tests/functional/nfs_feature/": "nfs",
    "tests/functional/ui/": "odf-console",
    "tests/cross_functional/ui/": "odf-console",
    "tests/functional/odf-cli/": "odf-cli",
    "tests/functional/upgrade/": "upgrade",
    "tests/functional/deployment/": "ocs-operator",
    "tests/functional/pod_and_daemons/": "rook",
}

# Keyword signals for catch-all directories (z_cluster, etc.)
_KEYWORD_COMPONENT_RULES = [
    ({"noobaa", "mcg", "bucket", "obc"}, "mcg"),
    ({"must-gather", "must_gather", "gather"}, "must-gather"),
    ({"hugepages", "scc", "performance_profile", "liveness", "disruption"}, "odf-operator"),
    ({"storagecluster", "storagesystem"}, "ocs-operator"),
    ({"osd", "mon", "mds", "rook", "rbd", "cephfs", "ceph", "mgr"}, "rook"),
]

# Filename patterns
_FILENAME_COMPONENT_RULES = [
    ("must_gather", "must-gather"),
    ("noobaa", "mcg"),
    ("hugepages", "odf-operator"),
    ("performance_profile", "odf-operator"),
    ("liveness_probe", "odf-operator"),
    ("ms_pod_disruptions", "odf-operator"),
    ("scc", "odf-operator"),
    ("rook_ceph", "rook"),
    ("ceph_default", "rook"),
    ("ceph_pg", "rook"),
    ("osd_heap", "rook"),
    ("mon_log", "rook"),
    ("mon_data", "rook"),
    ("mds", "rook"),
    ("storagecluster", "ocs-operator"),
    ("add_capacity", "ocs-operator"),
    ("node_expansion", "ocs-operator"),
    ("resize_osd", "ocs-operator"),
    ("nodes_restart", "ocs-operator"),
    ("nodes_maintenance", "ocs-operator"),
    ("node_replacement", "ocs-operator"),
    ("disk_failure", "ocs-operator"),
    ("toleration", "ocs-operator"),
    ("taint", "ocs-operator"),
    ("az_failure", "ocs-operator"),
    ("rolling_shutdown", "ocs-operator"),
    ("rolling_terminate", "ocs-operator"),
    ("kernel_crash", "ocs-operator"),
    ("deployment", "ocs-operator"),
    ("acm", "ocs-operator"),
]


def _classify_component(rel_path: str, keywords: list[str], filename: str) -> str:
    """Determine the ODF component a test file belongs to."""
    # 1. Specific directory match
    for dir_prefix, comp in _DIR_COMPONENT_MAP.items():
        if rel_path.startswith(dir_prefix):
            return comp

    # 2. Filename patterns (strongest signal for catch-all dirs)
    fname_lower = filename.lower()
    for pattern, comp in _FILENAME_COMPONENT_RULES:
        if pattern in fname_lower:
            return comp

    # 3. Keyword signals
    kw_set = set(k.lower() for k in keywords)
    for signal_words, comp in _KEYWORD_COMPONENT_RULES:
        if kw_set & signal_words:
            return comp

    # 4. Default by parent directory
    if "z_cluster" in rel_path:
        return "ocs-operator"
    if "cross_functional" in rel_path:
        return "ocs-operator"

    return ""


# ---------------------------------------------------------------------------
# Obsidian note generation
# ---------------------------------------------------------------------------

COMPONENT_SQUAD_MAP = {
    "ceph-csi": {
        "squad": "green_squad",
        "areas": ["PV", "StorageClass", "Encryption"],
    },
    "rook-ceph": {"squad": "green_squad", "areas": ["PV", "Pod & Daemons"]},
    "mcg-noobaa": {"squad": "red_squad", "areas": ["MCG", "RGW"]},
    "disaster-recovery": {
        "squad": "turquoise_squad",
        "areas": ["Disaster Recovery"],
    },
    "lvmo": {"squad": "aqua_squad", "areas": ["LVMO"]},
    "odf-console": {"squad": "black_squad", "areas": ["UI"]},
    "monitoring": {"squad": "blue_squad", "areas": ["Monitoring"]},
    "ocs-operator": {
        "squad": "brown_squad",
        "areas": ["Deployment", "Upgrade", "Z-Cluster"],
    },
}


def _safe_area_key(subcategory):
    return subcategory.replace("-", "_").replace("/", "_")


def generate_notes(
    output_dir, test_results, framework_results, version,
    markers_data=None,
):
    areas = _aggregate_areas(test_results)
    squads = _aggregate_squads(test_results, areas)
    total_files = len(test_results)
    total_tests = sum(r["test_count"] for r in test_results)

    for d in (
        "squads",
        "components",
        "tests/functional",
        "tests/cross_functional",
        "tests/libtest",
        "framework",
    ):
        (output_dir / d).mkdir(parents=True, exist_ok=True)

    _gen_dashboard(
        output_dir, areas, squads, framework_results,
        total_files, total_tests, version,
    )
    _gen_readme(output_dir, areas, squads, total_files, total_tests, version)

    for sq_name, sq_data in squads.items():
        _gen_squad_note(
            output_dir / "squads" / f"{sq_name}.md", sq_name, sq_data
        )

    for comp_name, comp_info in COMPONENT_SQUAD_MAP.items():
        _gen_component_note(
            output_dir / "components" / f"{comp_name}.md",
            comp_name, comp_info, areas,
        )

    for area_key, data in areas.items():
        cat = data["category"]
        if cat == "libtest":
            path = output_dir / "tests" / "libtest" / f"tests_{area_key}.md"
        elif cat in ("functional", "cross_functional"):
            path = output_dir / "tests" / cat / f"tests_{cat}_{area_key}.md"
        else:
            continue
        _gen_test_area_note(path, area_key, data)

    for fw in framework_results:
        _gen_framework_note(
            output_dir / "framework" / f"framework-{fw['name']}.md", fw
        )

    if markers_data:
        _gen_markers_note(
            output_dir / "markers.md", markers_data, version
        )


def _aggregate_areas(test_results):
    areas = defaultdict(
        lambda: {
            "category": "",
            "files": [],
            "test_count": 0,
            "file_count": 0,
            "squads": defaultdict(int),
            "tiers": defaultdict(int),
            "subdirs": defaultdict(lambda: {"files": 0, "tests": 0}),
        }
    )
    for r in test_results:
        cat = r["category"]
        sub = r["subcategory"] or r["category"]
        key = _safe_area_key(sub) if cat != "libtest" else "libtest"
        a = areas[key]
        a["category"] = cat
        a["files"].append(r)
        a["file_count"] += 1
        a["test_count"] += r["test_count"]
        if r["squad"]:
            a["squads"][r["squad"]] += r["test_count"]
        for t in r["tiers"]:
            a["tiers"][t] += 1
        fp = r["file_path"].split("/")
        if len(fp) > 3:
            sd = fp[3] if cat != "libtest" else fp[2]
            a["subdirs"][sd]["files"] += 1
            a["subdirs"][sd]["tests"] += r["test_count"]
    return dict(areas)


def _aggregate_squads(test_results, areas):
    squads = defaultdict(
        lambda: {"test_count": 0, "file_count": 0, "areas": defaultdict(int)}
    )
    for r in test_results:
        sq = r["squad"]
        if not sq:
            continue
        s = squads[sq]
        s["file_count"] += 1
        s["test_count"] += r["test_count"]
        cat = r["category"]
        sub = r["subcategory"] or r["category"]
        key = _safe_area_key(sub) if cat != "libtest" else "libtest"
        if cat == "libtest":
            note = "tests_libtest"
        elif cat in ("functional", "cross_functional"):
            note = f"tests_{cat}_{key}"
        else:
            note = key
        s["areas"][note] += r["test_count"]
    return dict(squads)


def _gen_dashboard(
    out_dir, areas, squads, fw_results, total_files, total_tests, version
):
    lines = [
        f"# OCS-CI Codebase Map (release-{version})",
        "",
        f"> Auto-generated map for ODF {version}.",
        "",
        "---",
        "",
        "## Quick Stats",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Test files | {total_files} |",
        f"| Test functions | {total_tests} |",
        f"| Squads | {len(squads)} |",
        f"| Test areas | {len(areas)} |",
        "",
        "---",
        "",
        "## Squads",
        "",
        "| Squad | Tests |",
        "|-------|-------|",
    ]
    for sq in sorted(squads, key=lambda s: -squads[s]["test_count"]):
        lines.append(f"| [[{sq}]] | {squads[sq]['test_count']} |")

    for section, cat_name in [
        ("Functional Tests", "functional"),
        ("Cross-Functional Tests", "cross_functional"),
    ]:
        lines.extend(
            [
                "",
                f"## {section}",
                "",
                "| Area | Tests | Files | Squad | Link |",
                "|------|-------|-------|-------|------|",
            ]
        )
        for key, data in sorted(
            areas.items(), key=lambda x: -x[1]["test_count"]
        ):
            if data["category"] != cat_name:
                continue
            top_sq = "mixed"
            if data["squads"]:
                top_sq = max(
                    data["squads"], key=data["squads"].get
                ).replace("_squad", "")
            lines.append(
                f"| {key} | {data['test_count']} | {data['file_count']} "
                f"| {top_sq} | [[tests_{cat_name}_{key}]] |"
            )

    if "libtest" in areas:
        d = areas["libtest"]
        lines.extend(
            [
                "",
                "## Library Tests",
                "",
                "| Area | Tests | Files | Link |",
                "|------|-------|-------|------|",
                f"| Libtest | {d['test_count']} | {d['file_count']}"
                f" | [[tests_libtest]] |",
            ]
        )

    if fw_results:
        lines.extend(
            [
                "",
                "## Framework",
                "",
                "| Module | Files | Lines | Link |",
                "|--------|-------|-------|------|",
            ]
        )
        for fw in fw_results:
            lines.append(
                f"| {fw['name']} | {fw['module_count']} | "
                f"{fw['total_lines']} | [[framework-{fw['name']}]] |"
            )

    (out_dir / "_dashboard.md").write_text("\n".join(lines) + "\n")


def _gen_readme(out_dir, areas, squads, total_files, total_tests, version):
    lines = [
        f"# OCS-CI Codebase Map (release-{version})",
        "",
        "Structured knowledge base of the "
        "[ocs-ci](https://github.com/red-hat-storage/ocs-ci) "
        f"test framework for ODF {version}.",
        "",
        "| Section | Count |",
        "|---------|-------|",
        f"| Squads | {len(squads)} |",
        f"| Test Areas | {len(areas)} |",
        f"| Test Files | {total_files} |",
        f"| Test Functions | {total_tests} |",
        f"| Components | {len(COMPONENT_SQUAD_MAP)} |",
        "",
        "Start at `_dashboard.md` for navigation.",
        "",
        "## Usage",
        "",
        "- **Obsidian**: Clone, open as vault, Ctrl+G for graph view",
        "- **GitHub**: Browse markdown directly",
        "- **AI agents**: Consumed by "
        "[odf-zstream-agents]"
        "(https://github.com/shyRozen/odf-zstream-agents)",
        "",
        f"Branch `release-{version}` maps ocs-ci `release-{version}`.",
        "",
        "Source: [red-hat-storage/ocs-ci]"
        "(https://github.com/red-hat-storage/ocs-ci)"
        f" `release-{version}`",
    ]
    (out_dir / "README.md").write_text("\n".join(lines) + "\n")


def _gen_squad_note(path, name, data):
    lines = [
        "---",
        f"squad: {name}",
        f"test_count: {data['test_count']}",
        f"file_count: {data['file_count']}",
        "---",
        "",
        f"# {name.replace('_', ' ').title()}",
        "",
        "## Test Areas",
    ]
    for note, count in sorted(data["areas"].items(), key=lambda x: -x[1]):
        lines.append(f"- [[{note}]] -- {count} tests")
    lines.extend(
        [
            "",
            "## Key Marks",
            f"`@{name}`, `@tier1`..`@tier4`, `@polarion_id`",
        ]
    )
    path.write_text("\n".join(lines) + "\n")


def _gen_component_note(path, comp_name, comp_info, areas):
    lines = [
        "---",
        f"component: {comp_name}",
        f"squad: {comp_info['squad']}",
        f"test_areas: {comp_info['areas']}",
        "---",
        "",
        f"# {comp_name}",
        "",
        "## Test Coverage",
    ]
    for area_name in comp_info["areas"]:
        area_lower = (
            area_name.lower()
            .replace("/", "_")
            .replace("-", "_")
            .replace(" ", "_")
        )
        for key, data in areas.items():
            if area_lower in key.lower() or key.lower() in area_lower:
                cat = data["category"]
                if cat == "libtest":
                    note = "tests_libtest"
                else:
                    note = f"tests_{cat}_{key}"
                lines.append(f"- [[{note}]] -- {data['test_count']} tests")
                break
    lines.extend(["", "## Related", f"- [[{comp_info['squad']}]]"])
    path.write_text("\n".join(lines) + "\n")


def _gen_test_area_note(path, area_key, data):
    cat = data["category"]
    top_sq = "mixed"
    if data["squads"]:
        top_sq = max(data["squads"], key=data["squads"].get)
    tier_str = ", ".join(
        f"{t}: {c}" for t, c in sorted(data["tiers"].items())
    )
    if cat == "libtest":
        directory = f"tests/{area_key}/"
    else:
        directory = f"tests/{cat}/{area_key}/"
    lines = [
        "---",
        f"directory: {directory}",
        f"squad: {top_sq}",
        f"test_files: {data['file_count']}",
        f"test_functions: {data['test_count']}",
        f"tiers: {{{tier_str}}}" if tier_str else "tiers: {}",
        "---",
        "",
        f"# {area_key.replace('_', ' ').title()}",
        "",
    ]
    if data["subdirs"]:
        lines.extend(
            [
                "## Subdirectories",
                "",
                "| Dir | Files | Tests |",
                "|-----|-------|-------|",
            ]
        )
        for sd, info in sorted(
            data["subdirs"].items(), key=lambda x: -x[1]["tests"]
        ):
            lines.append(f"| {sd}/ | {info['files']} | {info['tests']} |")
        lines.append("")
    top_files = sorted(data["files"], key=lambda f: -f["test_count"])[:10]
    if top_files:
        lines.extend(
            [
                "## Key Test Files",
                "",
                "| File | Tests | Squad |",
                "|------|-------|-------|",
            ]
        )
        for f in top_files:
            fname = f["file_path"].split("/")[-1]
            lines.append(
                f"| {fname} | {f['test_count']}"
                f" | {f['squad'] or 'mixed'} |"
            )
        lines.append("")
    lines.extend(["## Related", f"- [[{top_sq}]]"])
    path.write_text("\n".join(lines) + "\n")


def _gen_framework_note(path, fw):
    lines = [
        "---",
        f"path: {fw['path']}",
        f"modules: {fw['module_count']}",
        f"total_lines: {fw['total_lines']}",
        "---",
        "",
        f"# Framework: {fw['name'].title()}",
        "",
        "## Key Modules",
        "",
        "| File | Lines |",
        "|------|-------|",
    ]
    for m in fw["modules"][:15]:
        lines.append(f"| {m['file']} | {m['lines']} |")
    if fw["subdirs"]:
        lines.extend(["", "## Subdirectories"])
        for sd in fw["subdirs"]:
            lines.append(f"- {sd}/")
    path.write_text("\n".join(lines) + "\n")


def _gen_markers_note(path, markers_data, version):
    ini = markers_data.get("ini_markers", [])
    marks_py = markers_data.get("marks_py_markers", [])
    squad_marks = markers_data.get("squad_marks", [])

    lines = [
        "---",
        f"version: {version}",
        f"total_markers: {len(ini)}",
        f"marks_py_count: {len(marks_py)}",
        f"squad_marks: {len(squad_marks)}",
        "---",
        "",
        f"# Pytest Markers (release-{version})",
        "",
        "Markers are registered in two places:",
        "",
        "1. **`pytest.ini`** -- the `markers =` list. Required for "
        "`--strict-markers` to accept the marker at collection time.",
        "2. **`ocs_ci/framework/pytest_customization/marks.py`** -- "
        "Python variables (e.g. `tier1 = pytest.mark.tier1(value=1)`) "
        "that tests import and use as decorators.",
        "",
        "To add a new marker, register it in **both** files.",
        "",
        "## How to add a z-stream marker",
        "",
        "The z-stream pipeline adds a temporary marker for test "
        "selection:",
        "",
        "1. Append to `pytest.ini` markers list: "
        "`zstream_4_16_13: z-stream 4.16.13 test enablement`",
        "2. Add `@pytest.mark.zstream_4_16_13` to each selected "
        "test file",
        "3. Run with `pytest -m zstream_4_16_13`",
        "",
        "No `marks.py` entry needed -- z-stream markers are used "
        "directly as `@pytest.mark.name`, not imported as Python "
        "variables.",
        "",
    ]

    if squad_marks:
        lines.extend(
            [
                "## Squad Marks",
                "",
                "| Marker | Usage |",
                "|--------|-------|",
            ]
        )
        for m in sorted(squad_marks):
            lines.append(
                f"| `@{m}` | `from ocs_ci.framework."
                f"pytest_customization.marks import {m}` |"
            )
        lines.append("")

    tier_marks = [m for m in marks_py if m.startswith("tier")]
    component_marks = [
        m
        for m in marks_py
        if m not in tier_marks
        and not m.startswith("skipif")
        and not m.startswith("order_")
        and not m.startswith("pre_")
        and not m.startswith("post_")
    ]

    if tier_marks:
        lines.extend(
            [
                "## Tier Marks",
                "",
                ", ".join(f"`@{m}`" for m in sorted(tier_marks)),
                "",
            ]
        )

    if component_marks:
        lines.extend(
            [
                "## Component & Category Marks",
                "",
                ", ".join(
                    f"`@{m}`" for m in sorted(component_marks)
                ),
                "",
            ]
        )

    if ini:
        lines.extend(
            [
                "## All Registered Markers (pytest.ini)",
                "",
                "| Marker | Description |",
                "|--------|-------------|",
            ]
        )
        for m in ini:
            lines.append(
                f"| `{m['name']}` | {m['description']} |"
            )
        lines.append("")

    lines.extend(["## Related", "- [[framework-core]]"])
    path.write_text("\n".join(lines) + "\n")


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------


def _run(cmd, cwd, timeout=30):
    return subprocess.run(
        cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout
    )


def get_current_ref(repo_path):
    return _run(["git", "rev-parse", "HEAD"], repo_path, 10).stdout.strip()


def get_current_branch(repo_path):
    return _run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"], repo_path, 10
    ).stdout.strip()


def is_dirty(repo_path):
    return bool(
        _run(["git", "status", "--porcelain"], repo_path, 10).stdout.strip()
    )


def stash_changes(repo_path):
    r = _run(
        ["git", "stash", "push", "--include-untracked", "-m", "update_map.py auto-stash"],
        repo_path,
    )
    return "Saved working directory" in r.stdout


def stash_pop(repo_path):
    _run(["git", "stash", "pop"], repo_path)


def ocs_ci_checkout(repo_path, version):
    _run(
        ["git", "fetch", "upstream", f"release-{version}"],
        repo_path,
        120,
    )
    return _run(
        ["git", "checkout", f"upstream/release-{version}"], repo_path
    ).returncode == 0


def restore_ref(repo_path, ref):
    _run(["git", "checkout", ref], repo_path)


def map_create_branch(map_dir, branch_name):
    r = _run(["git", "branch", "--list", branch_name], map_dir, 10)
    if r.stdout.strip():
        _run(["git", "checkout", branch_name], map_dir)
    else:
        _run(["git", "checkout", "-b", branch_name, "main"], map_dir)


def map_commit_and_push(map_dir, version, push=True):
    _run(["git", "add", "-A"], map_dir)
    status = _run(
        ["git", "status", "--porcelain"], map_dir, 10
    ).stdout.strip()
    if not status:
        print(f"  [map] No changes for release-{version}")
        return
    _run(
        ["git", "commit", "-m", f"Update map for release-{version}"],
        map_dir,
    )
    if push:
        _run(
            ["git", "push", "-u", "origin", f"release-{version}"],
            map_dir,
            60,
        )


# ---------------------------------------------------------------------------
# Clean generated content (keep .git, scripts/)
# ---------------------------------------------------------------------------


def clean_generated(out_dir):
    for item in out_dir.iterdir():
        if item.name in (".git", ".gitignore", "scripts"):
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


# ---------------------------------------------------------------------------
# CLI + main
# ---------------------------------------------------------------------------


def build_index_json(results, version):
    return {
        "source": "https://github.com/red-hat-storage/ocs-ci",
        "branch": f"release-{version}",
        "scanned_at": datetime.now(timezone.utc).isoformat(),
        "total_files": len(results),
        "total_tests": sum(r["test_count"] for r in results),
        "files": results,
    }


def parse_args():
    p = argparse.ArgumentParser(
        description=(
            "Generate per-version map branches from "
            "ocs-ci release branches."
        ),
    )
    p.add_argument(
        "--ocs-ci-path",
        type=Path,
        required=True,
        help="Path to local ocs-ci git repo",
    )
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument(
        "--version",
        type=str,
        help="Scan a single release branch (e.g., 4.20)",
    )
    g.add_argument(
        "--all",
        action="store_true",
        help="Scan all release branches",
    )
    p.add_argument("--min-version", type=str, default="4.10")
    p.add_argument("--max-version", type=str, default="4.21")
    p.add_argument(
        "--no-push",
        action="store_true",
        help="Don't push branches to origin",
    )
    return p.parse_args()


def version_range(min_v, max_v):
    _, lo = (int(x) for x in min_v.split("."))
    hi_major, hi = (int(x) for x in max_v.split("."))
    return [f"{hi_major}.{m}" for m in range(lo, hi + 1)]


def main():
    args = parse_args()
    ocs_ci_path = args.ocs_ci_path.expanduser().resolve()
    map_dir = Path(__file__).resolve().parent.parent

    if not (ocs_ci_path / ".git").exists():
        print(f"ERROR: {ocs_ci_path} is not a git repo")
        sys.exit(1)
    if not (map_dir / ".git").exists():
        print(f"ERROR: {map_dir} is not a git repo")
        sys.exit(1)

    ocs_ci_stashed = False
    if is_dirty(ocs_ci_path):
        print("Stashing ocs-ci changes...")
        ocs_ci_stashed = stash_changes(ocs_ci_path)
        if not ocs_ci_stashed:
            print("ERROR: Failed to stash.")
            sys.exit(1)

    ocs_ci_ref = get_current_ref(ocs_ci_path)
    map_branch = get_current_branch(map_dir)
    versions = (
        [args.version]
        if args.version
        else version_range(args.min_version, args.max_version)
    )

    print(f"ocs-ci: {ocs_ci_path}")
    print(f"map:    {map_dir}")
    print(f"versions: {', '.join(versions)}\n")

    try:
        for version in versions:
            print(
                f"[{version}] Checking out ocs-ci "
                f"upstream/release-{version}..."
            )
            if not ocs_ci_checkout(ocs_ci_path, version):
                print(f"[{version}] WARNING: branch not found, skipping")
                continue

            print(f"[{version}] Scanning...")
            test_results = scan_all_tests(ocs_ci_path)
            fw_results = scan_framework(ocs_ci_path)
            markers_data = scan_markers(ocs_ci_path)
            index = build_index_json(test_results, version)

            print(f"[{version}] Creating map branch release-{version}...")
            map_create_branch(map_dir, f"release-{version}")
            clean_generated(map_dir)

            with open(map_dir / "test-index.json", "w") as f:
                json.dump(index, f, indent=2)

            generate_notes(
                map_dir, test_results, fw_results, version,
                markers_data=markers_data,
            )
            print(
                f"[{version}] {index['total_files']} files, "
                f"{index['total_tests']} tests"
            )

            map_commit_and_push(
                map_dir, version, push=not args.no_push
            )

    finally:
        print(f"\nRestoring ocs-ci {ocs_ci_ref[:12]}...")
        restore_ref(ocs_ci_path, ocs_ci_ref)
        if ocs_ci_stashed:
            print("Restoring stashed ocs-ci changes...")
            stash_pop(ocs_ci_path)
        print(f"Restoring map to {map_branch}...")
        _run(["git", "checkout", map_branch], map_dir)

    print("Done.")


if __name__ == "__main__":
    main()
