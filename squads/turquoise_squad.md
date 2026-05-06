---
squad: turquoise_squad
test_count: 44
file_count: 37
primary_areas: [Disaster Recovery, Regional DR, Metro DR, SC Arbiter]
---

# Turquoise Squad

## Test Areas
- [[tests_functional_disaster_recovery]] — 45 tests across 39 files
  - Regional DR: 22 files, 26 tests (failover, relocate, CNV, discovered apps)
  - SC Arbiter: 10 files, 12 tests (add capacity, node drain, device replacement)
  - Metro DR: 7 files, 7 tests (app failover/relocate, zone down, hub down)

## ODF Components
- [[disaster-recovery]] — DR orchestration (Ramen, ODF-DR)
- [[rook-ceph]] — Stretch clusters, zone-aware storage
- [[ocs-operator]] — StorageCluster DR config

## Key Marks
`@turquoise_squad`, `@tier1`..`@tier4`, `@polarion_id`
