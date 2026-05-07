---
directory: tests/functional/pv/
squad: green_squad
test_files: 77
test_functions: 113
tiers: {tier1: 12, tier2: 26, tier3: 3, tier4: 11, tier4b: 3, tier4c: 8}
---

# Pv

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| pv_services/ | 42 | 59 |
| pvc_snapshot/ | 10 | 11 |
| pv_encryption/ | 9 | 10 |
| pvc_clone/ | 6 | 10 |
| space_reclaim/ | 4 | 9 |
| add_metadata_feature/ | 1 | 8 |
| pvc_resize/ | 5 | 6 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_metadata.py | 8 | green_squad |
| test_cr_resources_validation.py | 5 | green_squad |
| test_rwop_pvc.py | 5 | green_squad |
| test_pvc_to_pvc_clone.py | 4 | green_squad |
| test_rwo_pvc_fencing_unfencing.py | 3 | green_squad |
| test_auto_reclaim_space_cronjob.py | 3 | green_squad |
| test_rbd_space_reclaim.py | 3 | green_squad |
| test_encrypted_rbd_volume_expansion.py | 2 | green_squad |
| test_del_mon_service_and_create_pvc.py | 2 | green_squad |
| test_dynamic_pvc_accessmodes_with_reclaim_policies.py | 2 | green_squad |

## Related
- [[green_squad]]
