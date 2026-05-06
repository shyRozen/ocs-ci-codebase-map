---
directory: tests/cross_functional/scale/
squad: orange_squad
test_files: 28
test_functions: 36
tiers: {tier1: 0, tier2: 0, tier3: 0, tier4: 0}
---

# Scale

PVC/Pod scaling, OSD node balancing, CephFS large file tests, NooBaa OBC scaling, scale upgrade validation.

## Subdirectories
| Dir | Files | Tests | Focus |
|-----|-------|-------|-------|
| (root) | 13 | 14 | Ceph/PVC scale tests |
| noobaa/ | 12 | 16 | NooBaa OBC/bucket scale |
| upgrade/ | 3 | 6 | Upgrade with scaled resources |

## Key Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_pvc_creation_deletion_scale.py | ~2 | PVC creation at scale |
| test_pv_scale_and_respin_ceph_pods.py | ~2 | PV scale + pod respin |
| test_scale_pgsql.py | ~1 | PGSQL at scale |
| test_scale_amq.py | ~1 | AMQ at scale |
| test_cephfs_many_files.py | ~1 | CephFS many-files stress |
| noobaa/test_scale_obc_creation.py | ~2 | OBC creation at scale |
| noobaa/test_scale_bucket_replication.py | ~2 | Bucket replication at scale |
| upgrade/test_upgrade_with_scaled_pvcs_pods.py | ~2 | Upgrade with scaled PVCs |

## Marks Used
`@orange_squad`, `@scale`, `@polarion_id`

## Related
- [[orange_squad]]
- [[ceph-csi]]
- [[mcg-noobaa]]
