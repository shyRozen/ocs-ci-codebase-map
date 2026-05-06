---
directory: tests/functional/external_mode/
squad: brown_squad
test_files: 1
test_functions: 1
tiers: {tier1: 1, tier2: 0, tier3: 0, tier4: 0}
---

# External Mode

Tests for ODF connected to external Ceph cluster.

## Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_*.py | 1 | External mode validation |

## Marks Used
`@brown_squad`, `@tier1`, `@polarion_id`

## Related
- [[brown_squad]]
- [[rook-ceph]]
- [[ocs-operator]]
