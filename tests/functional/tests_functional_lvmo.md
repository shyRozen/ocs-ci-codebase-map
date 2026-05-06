---
directory: tests/functional/lvmo/
squad: aqua_squad
test_files: 9
test_cases: 24
tiers: {tier1: 0, tier2: 0, tier3: 0, tier4: 0}
---

# LVMO (Logical Volume Manager Operator)

LVM-based storage tests using parametrized test cases. Covers cloning, snapshots, PVC resize, alerts, manual disk paths.

## Test Files
| File | Test Cases | Key Tests |
|------|------------|-----------|
| test_lvm_clone_base.py | ~4 | Clone from PVC (FS/Block, WFFC/Immediate) |
| test_lvm_snapshot_base.py | ~4 | Snapshot operations |
| test_lvm_clone_bigger_than_disk.py | ~2 | Clone exceeding disk |
| test_lvm_snapshot_bigger_than_disk.py | ~2 | Snapshot exceeding disk |
| test_lvm_multi_clone.py | ~3 | Multiple clones |
| test_lvm_multi_snapshot.py | ~3 | Multiple snapshots |
| test_lvm_alerts.py | ~2 | LVM capacity alerts |
| test_lvmo_pvc_resize.py | ~2 | PVC resize on LVM |
| test_lvm_manual_diskpath.py | ~2 | Manual disk path config |

Note: Tests use `@pytest.mark.parametrize` with class-based `ManageTest` structure. Functions named `deprecated_test_*` pattern.

## Marks Used
`@aqua_squad`, `@skipif_lvm_not_installed`, `@polarion_id`, `@acceptance`

## Related
- [[aqua_squad]]
- [[lvmo]]
