---
directory: tests/cross_functional/stress/
squad: magenta_squad
test_files: 5
test_functions: 5
tiers: {tier1: 1, tier2: 0, tier3: 0, tier4: 0}
---

# Stress

CephFS stress tests, MCG stress tests, memory stress with CSI addon.

## Test Files
| File | Squad | Tests | Key Tests |
|------|-------|-------|-----------|
| cephfs/test_*.py | magenta | ~3 | CephFS stress operations |
| mcg/test_*.py | magenta | ~1 | MCG stress operations |
| test_memory_stress_with_csiaddon.py | green | ~1 | Memory stress on CSI addon |

## Marks Used
`@magenta_squad`, `@green_squad`, `@tier1`, `@polarion_id`

## Related
- [[magenta_squad]]
- [[green_squad]]
- [[ceph-csi]]
