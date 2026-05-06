---
component: ceph-csi
squad: green_squad
test_areas: [PV, StorageClass, Encryption, Performance]
---

# ceph-csi

CSI driver for Ceph (RBD + CephFS). Handles PVC provisioning, snapshots, clones, resize, encryption, space reclaim.

## Test Coverage
- [[tests_functional_pv]] — 113 tests, core PV operations
- [[tests_functional_storageclass]] — 29 tests, StorageClass management
- [[tests_functional_encryption]] — 11 tests, in-transit encryption
- [[tests_cross_functional_performance]] — 34 tests, CSI perf benchmarks
- [[tests_cross_functional_scale]] — 36 tests, PVC scaling
- [[tests_cross_functional_krkn_chaos]] — 24 tests, chaos under CSI
- [[tests_cross_functional_stress]] — 5 tests, memory stress CSI addon

## Framework Classes
- `ocs_ci/ocs/resources/pvc.py` (948 lines) — PVC class
- `ocs_ci/ocs/resources/pv.py` (409 lines) — PV operations
- `ocs_ci/ocs/resources/pod.py` (4702 lines) — Pod with volume mounts
- `ocs_ci/ocs/resources/storage_cluster.py` (3608 lines) — StorageCluster CR

## Related
- [[green_squad]]
- [[grey_squad]] (performance)
- [[rook-ceph]]
