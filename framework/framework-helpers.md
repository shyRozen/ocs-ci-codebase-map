---
path: ocs_ci/helpers/
modules: 29
total_lines: 23525
---

# Framework Helpers

Test helpers for common operations: DR, performance, key rotation, disruptions, sanity checks, CNV, ODF CLI.

## Key Modules (by size)
| File | Lines | Purpose |
|------|-------|---------|
| helpers.py | 7456 | General test helpers (PVC/Pod creation, IO, validation) |
| dr_helpers.py | 2922 | DR failover/relocate helpers |
| performance_lib.py | 1059 | Performance test library |
| keyrotation_helper.py | 1018 | Key rotation (NooBaa, OSD, PV) |
| cephfs_stress_helpers.py | 1000 | CephFS stress test manager |
| managed_services.py | 982 | Managed service helpers |
| dr_helpers_ui.py | 975 | DR UI helpers |
| disruption_helpers.py | 901 | Pod/daemon disruption helpers |
| longevity_helpers.py | 771 | Longevity test helpers |
| cnv_helpers.py | 716 | CNV/VM helpers |
| vdbench_helpers.py | 711 | VDBench workload helpers |
| mcg_stress_helper.py | 665 | MCG stress helpers |
| sanity_helpers.py | 586 | Sanity check classes |
| osd_resize.py | 505 | OSD resize operations |
| e2e_helpers.py | 468 | E2E test helpers |
| stretchcluster_helper.py | 418 | Stretch cluster helpers |
| odf_cli.py | 407 | ODF CLI retriever/runner |

## Key Classes
- **Sanity / SanityExternalCluster / SanityManagedService / SanityProviderMode** — Sanity check variants
- **Disruptions / FIOIntegrityChecker** — Disruption and integrity
- **KeyRotation / NoobaaKeyrotation / OSDKeyrotation / PVKeyrotation** — Key rotation
- **ODFCLIRetriever / ODFCliRunner** — ODF CLI tool
- **ClusterFiller / BackgroundOps** — Cluster expansion helpers
- **CephFSStressTestManager** — CephFS stress orchestration

## Related
- [[framework-ocs]]
- [[framework-utility]]
- [[tests-functional-disaster-recovery]]
