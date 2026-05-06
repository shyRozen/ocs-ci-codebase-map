---
squad: grey_squad
test_count: 33
file_count: 15
primary_areas: [Performance, CSI Performance, IO Workload]
---

# Grey Squad

## Test Areas
- [[tests-cross_functional-performance]] — 34 tests across 16 files
  - CSI tests: 11 files, 26 tests (PVC creation/deletion, clone, snapshot, pod attach/reattach)
  - IO workload: 4 files, 7 tests (FIO, small file, PGSQL, IO perf)

## ODF Components
- [[ceph-csi]] — CSI driver performance benchmarking
- [[rook-ceph]] — Ceph IO performance

## Key Marks
`@grey_squad`, `@performance`, `@polarion_id`
