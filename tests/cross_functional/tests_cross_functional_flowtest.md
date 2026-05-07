---
directory: tests/cross_functional/flowtest/
squad: magenta_squad
test_files: 3
test_functions: 5
tiers: {}
---

# Flowtest

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| pvc_snapshot_and_clone/ | 2 | 4 |
| test_base_operation_node_drain.py/ | 1 | 1 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_pgsql_pvc_snapshot_and_clone.py | 2 | magenta_squad |
| test_pgsql_pvc_snapshot_and_clone_with_base_operation.py | 2 | magenta_squad |
| test_base_operation_node_drain.py | 1 | mixed |

## Related
- [[magenta_squad]]
