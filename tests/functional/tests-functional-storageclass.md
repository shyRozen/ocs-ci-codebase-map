---
directory: tests/functional/storageclass/
squad: green_squad
test_files: 23
test_functions: 29
tiers: {tier1: 8, tier2: 9, tier3: 6, tier4: 0}
---

# StorageClass

StorageClass creation, validation, RBD pools, CephFS, replica configurations, reclaim policies, encryption options.

## Test Files
| File | Tests | Tier | Key Tests |
|------|-------|------|-----------|
| test_cephfilesystem_creation.py | 1 | tier1 | CephFS filesystem creation |
| test_create_2sc_at_once_with_io.py | 1 | tier2 | Concurrent SC creation with IO |
| test_create_2_sc_with_1_pool_comp_rep2.py | 1 | tier2 | Pool sharing |
| test_create_multiple_sc_with_different_pool_name.py | 1 | tier2 | Multiple pools |
| test_create_multiple_sc_with_same_pool_name.py | 1 | tier2 | Same pool name |
| test_cross_sc_clone_snap_restore.py | 1 | tier3 | Cross-SC clone/snapshot |
| test_replica1.py | 1 | tier1 | Replica-1 SC (@brown_squad) |
| test_storageclassclaim.py | 1 | tier1 | SC claim (@yellow_squad) |
| test_storageclass_encryption_option.py | 1 | tier1 | Encryption option |
| test_storageclass_invalid.py | 1 | tier1 | Invalid SC handling |
| test_storageclass_reclaim_space.py | 1 | tier2 | Space reclaim SC |
| test_rbd_default_storageclass.py | 1 | tier1 | Default RBD SC |
| test_new_sc_rbd_replica2_3.py | 1 | tier2 | Replica 2/3 |

## Marks Used
`@green_squad`, `@brown_squad`, `@yellow_squad`, `@tier1`, `@tier2`, `@tier3`, `@polarion_id`

## Related
- [[green_squad]]
- [[ceph-csi]]
- [[tests-functional-pv]]
