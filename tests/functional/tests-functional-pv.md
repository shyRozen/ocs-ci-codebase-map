---
directory: tests/functional/pv/
squad: green_squad
test_files: 84
test_functions: 113
tiers: {tier1: 30, tier2: 46, tier3: 3, tier4: 17}
---

# PV (Persistent Volumes)

Persistent volume operations, cloning, resizing, snapshots, encryption, space reclaim, metadata features.

## Subdirectories
| Dir | Files | Tests | Focus |
|-----|-------|-------|-------|
| pv_services/ | 43 | 55 | Core PVC/PV lifecycle, creation, deletion, IO |
| pv_encryption/ | 12 | 15 | RBD encryption (Vault, KMIP, Azure KMS) |
| pvc_snapshot/ | 11 | 12 | PVC snapshot create/restore |
| pvc_clone/ | 6 | 10 | PVC-to-PVC cloning |
| pvc_resize/ | 6 | 7 | PVC expansion |
| space_reclaim/ | 5 | 10 | RBD/CephFS space reclamation |
| add_metadata_feature/ | 1 | 4 | PV metadata annotations |

## Key Test Files
| File | Tests | Tier | Key Tests |
|------|-------|------|-----------|
| pv_services/test_cr_resources_validation.py | 5 | tier1 | Resource validation |
| pvc_clone/test_pvc_to_pvc_clone.py | 4 | tier1 | PVC clone operations |
| space_reclaim/test_rbd_space_reclaim.py | 3 | tier2 | RBD space reclaim |
| pv_services/test_dynamic_pvc_accessmodes_with_reclaim_policies.py | 2 | tier1 | Access modes |
| pvc_resize/test_pvc_expansion.py | 2 | tier2 | PVC expansion |
| pv_encryption/test_rbd_pv_encryption.py | 1 | tier1 | RBD PV encryption |

## Marks Used
`@green_squad`, `@tier1`, `@tier2`, `@tier3`, `@tier4`, `@polarion_id`, `@skipif_ocs_version`

## Related
- [[green_squad]]
- [[ceph-csi]]
- [[tests-functional-storageclass]]
- [[tests-functional-encryption]]
