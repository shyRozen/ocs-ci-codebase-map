---
directory: tests/functional/storageclass/
squad: green_squad
test_files: 24
test_functions: 32
tiers: {tier1: 5, tier2: 7, tier3: 4}
---

# Storageclass

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| test_create_storage_class_pvc.py/ | 1 | 4 |
| test_create_storageclass_with_same_name.py/ | 1 | 2 |
| test_cross_sc_clone_snap_restore.py/ | 1 | 2 |
| test_custom_storageclass_names.py/ | 1 | 2 |
| test_delete_rbd_pool_attached_to_sc.py/ | 1 | 2 |
| test_replica1.py/ | 1 | 2 |
| test_cephfilesystem_creation.py/ | 1 | 1 |
| test_create_2_sc_with_1_pool_comp_rep2.py/ | 1 | 1 |
| test_create_2sc_at_once_with_io.py/ | 1 | 1 |
| test_create_multiple_sc_with_different_pool_name.py/ | 1 | 1 |
| test_create_multiple_sc_with_same_pool_name.py/ | 1 | 1 |
| test_create_sc_and_make_it_as_a_default.py/ | 1 | 1 |
| test_create_sc_reclaim_policy_rep2_comp.py/ | 1 | 1 |
| test_create_storageclass_with_wrong_provisioner.py/ | 1 | 1 |
| test_csi_subvolume_group_property.py/ | 1 | 1 |
| test_multiple_sc_comp_rep_data_delete.py/ | 1 | 1 |
| test_new_sc_rbd_replica2_3.py/ | 1 | 1 |
| test_rbd_csi_default_sc.py/ | 1 | 1 |
| test_rbd_default_storageclass.py/ | 1 | 1 |
| test_storageclass_encryption_option.py/ | 1 | 1 |
| test_storageclass_invalid.py/ | 1 | 1 |
| test_storageclass_reclaim_space.py/ | 1 | 1 |
| test_storageclassclaim.py/ | 1 | 1 |
| test_verify_all_fields_in_sc_yaml_with_oc_describe_sc.py/ | 1 | 1 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_create_storage_class_pvc.py | 4 | green_squad |
| test_create_storageclass_with_same_name.py | 2 | green_squad |
| test_cross_sc_clone_snap_restore.py | 2 | green_squad |
| test_custom_storageclass_names.py | 2 | green_squad |
| test_delete_rbd_pool_attached_to_sc.py | 2 | green_squad |
| test_replica1.py | 2 | brown_squad |
| test_cephfilesystem_creation.py | 1 | mixed |
| test_create_2_sc_with_1_pool_comp_rep2.py | 1 | green_squad |
| test_create_2sc_at_once_with_io.py | 1 | green_squad |
| test_create_multiple_sc_with_different_pool_name.py | 1 | green_squad |

## Related
- [[green_squad]]
