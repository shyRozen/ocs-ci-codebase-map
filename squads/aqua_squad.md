---
squad: aqua_squad
test_count: 24
file_count: 9
primary_areas: [LVMO, LVM Operator]
---

# Aqua Squad

## Test Areas
- [[tests_functional_lvmo]] — 9 files, ~24 parametrized test cases
  - LVM clone base, snapshot base
  - LVM clone/snapshot bigger than disk
  - LVM multi-clone, multi-snapshot
  - LVM alerts, PVC resize
  - LVM manual disk path

## ODF Components
- [[lvmo]] — Logical Volume Manager Operator

## Key Marks
`@aqua_squad`, `@skipif_lvm_not_installed`, `@polarion_id`
