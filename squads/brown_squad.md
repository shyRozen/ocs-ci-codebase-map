---
squad: brown_squad
test_count: 164
file_count: 82
primary_areas: [Cluster Operations, z_cluster, Nodes, Upgrade, Pod/Daemons]
---

# Brown Squad

## Test Areas
- [[tests-functional-z_cluster]] — 115 tests, cluster health/operations (31 z_cluster + 18 nodes + 11 expansion files)
- [[tests-functional-pod_and_daemons]] — 20 tests (6 files brown)
- [[tests-functional-upgrade]] — 39 tests (4 files brown)
- [[tests-functional-odf-cli]] — 7 tests (3 files brown)
- [[tests-functional-nfs_feature]] — 14 tests (1 file brown)
- [[tests-functional-storageclass]] — 29 tests (1 file: replica1)
- [[tests-functional-deployment]] — 4 tests (1 file brown)
- [[tests-functional-external_mode]] — 1 test
- [[tests-cross_functional-ui]] — 11 tests (1 file: add_capacity_ui)
- [[tests-libtest]] — 111 tests (3 files brown)

## ODF Components
- [[rook-ceph]] — Rook operator, Ceph daemons, OSD/MON management
- [[ocs-operator]] — Cluster operations, capacity management

## Key Marks
`@brown_squad`, `@tier1`..`@tier4`, `@polarion_id`
