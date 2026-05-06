---
directory: tests/functional/provider_mode/
squad: yellow_squad
test_files: 1
test_functions: 1
tiers: {tier1: 1, tier2: 0, tier3: 0, tier4: 0}
---

# Provider Mode

Tests for ODF in provider/client mode (managed service architecture).

## Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_ceph_csi_image_versions.py | 1 | CSI image version validation in provider mode |

## Marks Used
`@yellow_squad`, `@tier1`, `@polarion_id`

## Related
- [[yellow_squad]]
- [[ocs-operator]]
- [[ceph-csi]]
