---
directory: tests/cross_functional/stress/
squad: magenta_squad
test_files: 4
test_functions: 4
tiers: {}
---

# Stress

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| cephfs/ | 2 | 2 |
| mcg/ | 1 | 1 |
| test_memory_stress_with_csiaddon.py/ | 1 | 1 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_cephfs_breakpoint.py | 1 | magenta_squad |
| test_cephfs_incremental_bulk_ops_cleanup.py | 1 | magenta_squad |
| test_noobaa_under_stress.py | 1 | magenta_squad |
| test_memory_stress_with_csiaddon.py | 1 | green_squad |

## Related
- [[magenta_squad]]
