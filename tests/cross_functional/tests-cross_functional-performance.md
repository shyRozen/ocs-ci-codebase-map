---
directory: tests/cross_functional/performance/
squad: grey_squad
test_files: 16
test_functions: 34
tiers: {tier1: 0, tier2: 0, tier3: 0, tier4: 0}
---

# Performance

CSI driver performance benchmarking, IO workload performance, MCG CosBench.

## Subdirectories
| Dir | Files | Tests | Focus |
|-----|-------|-------|-------|
| csi_tests/ | 11 | 26 | PVC creation/deletion, clone, snapshot, pod attach perf |
| io_workload/ | 4 | 7 | FIO, small file, PGSQL, IO perf |
| mcg/ | 1 | 1 | MCG CosBench (@red_squad) |

## Key Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| csi_tests/test_pvc_creation_deletion_performance.py | ~3 | PVC create/delete perf |
| csi_tests/test_pvc_bulk_creation_deletion_performance.py | ~3 | Bulk PVC perf |
| csi_tests/test_pvc_snapshot_performance.py | ~2 | Snapshot perf |
| csi_tests/test_pvc_clone_performance.py | ~2 | Clone perf |
| csi_tests/test_pod_attachtime.py | ~2 | Pod attach time |
| csi_tests/test_pod_reattachtime.py | ~2 | Pod reattach time |
| io_workload/test_fio_benchmark.py | ~2 | FIO benchmark |
| io_workload/test_small_file_workload.py | ~2 | Small file workload |

## Marks Used
`@grey_squad`, `@red_squad` (MCG), `@performance`, `@polarion_id`

## Related
- [[grey_squad]]
- [[ceph-csi]]
