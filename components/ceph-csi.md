---
component: ceph-csi
squad: green_squad
test_areas: [PV, StorageClass, Encryption, Performance]
---

# ceph-csi

CSI driver for Ceph (RBD + CephFS). Handles PVC provisioning, snapshots, clones, resize, encryption, space reclaim.

## Test Coverage
- [[tests-functional-pv]] — 113 tests, core PV operations
- [[tests-functional-storageclass]] — 29 tests, StorageClass management
- [[tests-functional-encryption]] — 11 tests, in-transit encryption
- [[tests-cross_functional-performance]] — 34 tests, CSI perf benchmarks
- [[tests-cross_functional-scale]] — 36 tests, PVC scaling
- [[tests-cross_functional-krkn_chaos]] — 24 tests, chaos under CSI
- [[tests-cross_functional-stress]] — 5 tests, memory stress CSI addon

## Framework Classes
- `ocs_ci/ocs/resources/pvc.py` (948 lines) — PVC class
- `ocs_ci/ocs/resources/pv.py` (409 lines) — PV operations
- `ocs_ci/ocs/resources/pod.py` (4702 lines) — Pod with volume mounts
- `ocs_ci/ocs/resources/storage_cluster.py` (3608 lines) — StorageCluster CR

## Related
- [[green_squad]]
- [[grey_squad]] (performance)
- [[rook-ceph]]
