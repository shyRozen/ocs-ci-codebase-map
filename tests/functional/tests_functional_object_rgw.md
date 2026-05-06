---
directory: tests/functional/object/rgw/
squad: red_squad
test_files: 12
test_functions: 16
tiers: {tier1: 6, tier2: 1, tier3: 1, tier4: 1}
---

# Object Storage - RGW (RADOS Gateway)

Ceph RADOS Gateway operations, S3 operations via RGW, RGW bucket management, multisite.

## Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_rgw_*.py | 16 | RGW bucket ops, S3 compliance, multisite |

## Marks Used
`@red_squad`, `@tier1`, `@tier2`, `@tier3`, `@tier4`, `@polarion_id`

## Related
- [[red_squad]]
- [[rook-ceph]]
- [[tests_functional_object_mcg]]
