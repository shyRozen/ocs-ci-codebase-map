---
squad: black_squad
test_count: 66
file_count: 19
primary_areas: [UI, Console, Cluster Expansion]
---

# Black Squad

## Test Areas
- [[tests_functional_ui]] — 28 tests (9 files: PV encryption UI, capacity breakdown, health overview, alerts, quickstarts)
- [[tests_functional_object_mcg]] — 228 tests (5 MCG UI files: bucket policy, versioning, lifecycle, namespace store)
- [[tests_functional_z_cluster]] — 115 tests (3 files: add_capacity, resize_osd, multiple_device_classes)
- [[tests_cross_functional_ui]] — 11 tests (2 files: validation_ui, odf_topology)

## ODF Components
- [[odf-console]] — ODF Console plugin, UI testing
- [[rook-ceph]] — Cluster expansion operations

## Key Marks
`@black_squad`, `@tier1`..`@tier4`, `@polarion_id`, `@ui`
