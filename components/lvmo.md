---
component: lvmo
squad: aqua_squad
test_areas: [LVMO]
---

# LVMO (Logical Volume Manager Operator)

LVM-based local storage provisioning. Thin provisioning, snapshots, clones, PVC resize, capacity alerts, manual disk path configuration.

## Test Coverage
- [[tests_functional_lvmo]] — 9 files, ~24 parametrized test cases
  - Clone operations (base, multi-clone, bigger-than-disk)
  - Snapshot operations (base, multi-snapshot, bigger-than-disk)
  - PVC resize
  - Capacity alerts
  - Manual disk path

## Framework Classes
- `ocs_ci/ocs/cluster.py` — LVM class (within cluster.py)
- `ocs_ci/framework/pytest_customization/marks.py` — `@skipif_lvm_not_installed`

## Related
- [[aqua_squad]]
