---
directory: tests/functional/pv/
squad: green_squad
test_files: 79
test_functions: 113
tiers: {tier1: 13, tier2: 28, tier3: 3, tier4: 11, tier4b: 3, tier4c: 8}
---

# Pv

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| pv_services/ | 39 | 52 |
| pv_encryption/ | 12 | 15 |
| pvc_snapshot/ | 11 | 12 |
| pvc_clone/ | 6 | 10 |
| space_reclaim/ | 5 | 10 |
| add_metadata_feature/ | 1 | 8 |
| pvc_resize/ | 5 | 6 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_metadata.py | 8 | green_squad |
| test_cr_resources_validation.py | 5 | green_squad |
| test_rwop_pvc.py | 5 | green_squad |
| test_pvc_to_pvc_clone.py | 4 | green_squad |
| test_auto_reclaim_space_cronjob.py | 3 | green_squad |
| test_rbd_space_reclaim.py | 3 | green_squad |
| test_disable_pv_keyrotation.py | 2 | green_squad |
| test_encrypted_rbd_volume_expansion.py | 2 | green_squad |
| test_secrets_on_pods.py | 2 | mixed |
| test_del_mon_service_and_create_pvc.py | 2 | green_squad |

## Related
- [[green_squad]]
