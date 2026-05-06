# OCS-CI Codebase Map

A structured knowledge base of the [ocs-ci](https://github.com/red-hat-storage/ocs-ci) test framework for OpenShift Data Foundation (ODF). Built as an Obsidian vault with cross-linked notes — browse it locally in [Obsidian](https://obsidian.md) or read the markdown files directly on GitHub.

## What's Inside

| Section | Notes | What It Covers |
|---------|-------|---------------|
| [Squads](squads/) | 12 | Team ownership — which squad owns which tests and components |
| [Tests](tests/) | 30 | Every test area with file counts, test functions, tiers, marks, and subdirectory breakdowns |
| [Components](components/) | 8 | ODF components (ceph-csi, MCG, rook-ceph, etc.) with test coverage and framework classes |
| [Framework](framework/) | 6 | Framework internals — pytest plugins, resource classes, deployment logic, utilities |
| [Dashboard](_dashboard.md) | 1 | Entry point with summary tables and links to everything |

**Total: 57 notes** mapping 485 test files, 913 test functions, 215+ framework modules, and ~215,000 lines of code.

## Quick Navigation

Start with **[_dashboard.md](_dashboard.md)** — it has summary tables for squads, test areas, and framework modules with links to detailed notes.

### By Squad

| Squad | Areas | Tests |
|-------|-------|-------|
| [green_squad](squads/green_squad.md) | PV, StorageClass, Encryption, Krkn Chaos | ~130 |
| [red_squad](squads/red_squad.md) | MCG, RGW, Object Storage | ~100 |
| [brown_squad](squads/brown_squad.md) | Z-Cluster, NFS, Upgrade, ODF-CLI | ~100 |
| [blue_squad](squads/blue_squad.md) | Monitoring, Prometheus, Alerts | ~53 |
| [magenta_squad](squads/magenta_squad.md) | Workloads, System Test, Longevity | ~50 |
| [turquoise_squad](squads/turquoise_squad.md) | Disaster Recovery | ~37 |
| [orange_squad](squads/orange_squad.md) | Scale | ~33 |
| [black_squad](squads/black_squad.md) | UI | ~25 |
| [purple_squad](squads/purple_squad.md) | Deployment, Upgrade | ~17 |
| [grey_squad](squads/grey_squad.md) | Performance | ~15 |
| [yellow_squad](squads/yellow_squad.md) | Provider Mode, Data Replication | ~12 |
| [aqua_squad](squads/aqua_squad.md) | LVMO | ~9 |

### By Component

| Component | Squad | Key Test Areas |
|-----------|-------|---------------|
| [ceph-csi](components/ceph-csi.md) | green | PV, StorageClass, Encryption |
| [MCG/NooBaa](components/mcg-noobaa.md) | red | Object/MCG, Buckets, S3 |
| [rook-ceph](components/rook-ceph.md) | green/brown | Z-Cluster, Pods, Ceph operations |
| [OCS Operator](components/ocs-operator.md) | brown/purple | Deployment, Upgrade, Cluster mgmt |
| [ODF Console](components/odf-console.md) | black | UI functional + cross-functional |
| [Disaster Recovery](components/disaster-recovery.md) | turquoise | Metro DR, Regional DR, Arbiter |
| [Monitoring](components/monitoring.md) | blue | Prometheus, Alerts, PagerDuty |
| [LVMO](components/lvmo.md) | aqua | LVM Operator |

## Structure

```
ocs-ci-map/
├── _dashboard.md              ← Start here
├── squads/                    ← 12 squad ownership notes
│   ├── green_squad.md
│   ├── red_squad.md
│   └── ...
├── components/                ← 8 ODF component notes
│   ├── ceph-csi.md
│   ├── mcg-noobaa.md
│   └── ...
├── tests/
│   ├── functional/            ← 19 functional test area notes
│   │   ├── tests_functional_pv.md
│   │   ├── tests_functional_object_mcg.md
│   │   └── ...
│   ├── cross_functional/      ← 10 cross-functional test area notes
│   │   ├── tests_cross_functional_scale.md
│   │   ├── tests_cross_functional_performance.md
│   │   └── ...
│   └── libtest/               ← 1 library test note
│       └── tests_libtest.md
└── framework/                 ← 6 framework module notes
    ├── framework-core.md
    ├── framework-ocs.md
    ├── framework-deployment.md
    ├── framework-utility.md
    ├── framework-helpers.md
    └── framework-constants.md
```

## How to Use

### In Obsidian (recommended)
1. Clone this repo
2. Open the folder as an Obsidian vault (File → Open Vault → Open folder as vault)
3. Navigate to `_dashboard.md`
4. Press `Ctrl+G` for the graph view — see all connections between squads, tests, components, and framework
5. Use `Ctrl+O` to quick-search any note

### On GitHub
All notes are standard markdown — browse them directly. `[[wikilinks]]` won't be clickable on GitHub, but the content is fully readable.

### For AI Agents
This vault is designed to be consumed by the [odf-zstream-agents](https://github.com/shyRozen/odf-zstream-agents) pipeline. Agents download the map and use it for test selection instead of re-scanning the ocs-ci codebase each run.

## Source

Mapped from [ocs-ci](https://github.com/red-hat-storage/ocs-ci) at `~/codcod/new-ocs-ci/ocs-ci/`. All file counts, test function counts, and mark distributions were extracted from the actual codebase using AST parsing and grep.

## Related

- [odf-zstream-agents](https://github.com/shyRozen/odf-zstream-agents) — AI-powered z-stream test automation pipeline that uses this map
