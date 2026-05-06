---
squad: green_squad
test_count: 199
file_count: 126
primary_areas: [PV, StorageClass, Encryption, Krkn Chaos]
---

# Green Squad

## Test Areas
- [[tests_functional_pv]] — 113 tests, PV operations (clone, snapshot, resize, encryption, space reclaim)
- [[tests_functional_storageclass]] — 29 tests, StorageClass creation and management
- [[tests_functional_encryption]] — 11 tests, in-transit encryption, key rotation
- [[tests_cross_functional_krkn_chaos]] — 24 tests, chaos engineering (6 files)
- [[tests_cross_functional_resilience]] — 5 tests, storage component failure scenarios (3 files)
- [[tests_cross_functional_stress]] — 5 tests, memory stress with CSI addon (1 file)
- [[tests_functional_pod_and_daemons]] — 20 tests (3 files green)
- [[tests_functional_ui]] — 28 tests (2 files green)
- [[tests_functional_odf_cli]] — 7 tests (1 file green)
- [[tests_cross_functional_ui]] — 11 tests (2 files green)

## ODF Components
- [[ceph-csi]] — CSI driver for RBD + CephFS
- [[rook-ceph]] — PersistentVolumes, StorageClass
- [[monitoring]] — Encryption/KMS integration

## Key Marks
`@green_squad`, `@tier1`..`@tier4`, `@polarion_id`, `@skipif_ocs_version`
