---
squad: green_squad
test_count: 199
file_count: 126
primary_areas: [PV, StorageClass, Encryption, Krkn Chaos]
---

# Green Squad

## Test Areas
- [[tests-functional-pv]] — 113 tests, PV operations (clone, snapshot, resize, encryption, space reclaim)
- [[tests-functional-storageclass]] — 29 tests, StorageClass creation and management
- [[tests-functional-encryption]] — 11 tests, in-transit encryption, key rotation
- [[tests-cross_functional-krkn_chaos]] — 24 tests, chaos engineering (6 files)
- [[tests-cross_functional-resilience]] — 5 tests, storage component failure scenarios (3 files)
- [[tests-cross_functional-stress]] — 5 tests, memory stress with CSI addon (1 file)
- [[tests-functional-pod_and_daemons]] — 20 tests (3 files green)
- [[tests-functional-ui]] — 28 tests (2 files green)
- [[tests-functional-odf-cli]] — 7 tests (1 file green)
- [[tests-cross_functional-ui]] — 11 tests (2 files green)

## ODF Components
- [[ceph-csi]] — CSI driver for RBD + CephFS
- [[rook-ceph]] — PersistentVolumes, StorageClass
- [[monitoring]] — Encryption/KMS integration

## Key Marks
`@green_squad`, `@tier1`..`@tier4`, `@polarion_id`, `@skipif_ocs_version`
