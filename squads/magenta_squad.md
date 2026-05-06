---
squad: magenta_squad
test_count: 113
file_count: 83
primary_areas: [Workloads, System Tests, Longevity, KCS, FlowTests]
---

# Magenta Squad

## Test Areas
- [[tests-functional-workloads]] — 71 tests (CNV 12, OCP registry 7, AMQ 5, PGSQL 4, Jenkins 4, Couchbase 4 files)
- [[tests-cross_functional-system_test]] — 23 tests (10 files)
- [[tests-cross_functional-kcs]] — 8 tests (8 files)
- [[tests-cross_functional-longevity]] — 6 tests, 5-stage longevity (6 files)
- [[tests-cross_functional-stress]] — 5 tests, CephFS/MCG stress (4 files)
- [[tests-cross_functional-flowtest]] — 5 tests, node drain + snapshot/clone flows (3 files)
- [[tests-cross_functional-resilience]] — 5 tests (1 file: ocs_monkey)

## ODF Components
- [[rook-ceph]] — Cluster health under workloads
- [[mcg-noobaa]] — NooBaa recovery, bucket notification
- [[ceph-csi]] — PVC snapshot/clone under load

## Key Marks
`@magenta_squad`, `@tier1`..`@tier4`, `@polarion_id`, `@system_test`
