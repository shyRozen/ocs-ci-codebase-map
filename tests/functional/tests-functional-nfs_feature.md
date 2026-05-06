---
directory: tests/functional/nfs_feature/
squad: brown_squad
test_files: 1
test_functions: 14
tiers: {tier1: 7, tier2: 4, tier3: 0, tier4: 3}
---

# NFS Feature

NFS feature enablement for ODF clusters. Single test file covering NFS provisioning, access, and feature toggle.

## Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_nfs_feature_enable_for_ODF_clusters.py | 14 | NFS enable, provisioning, access modes |

## Marks Used
`@brown_squad`, `@tier1`, `@tier2`, `@tier4`, `@polarion_id`

## Related
- [[brown_squad]]
- [[rook-ceph]]
- [[ceph-csi]]
