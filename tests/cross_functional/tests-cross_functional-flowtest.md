---
directory: tests/cross_functional/flowtest/
squad: magenta_squad
test_files: 3
test_functions: 5
tiers: {tier1: 0, tier2: 0, tier3: 0, tier4: 0}
---

# FlowTest

End-to-end flow tests: node drain with base operations, PVC snapshot and clone flows with PGSQL workloads.

## Subdirectories
| Dir | Files | Tests | Focus |
|-----|-------|-------|-------|
| (root) | 1 | ~1 | Node drain flow |
| pvc_snapshot_and_clone/ | 2 | ~4 | PGSQL snapshot/clone flows |

## Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_base_operation_node_drain.py | ~1 | Node drain with ongoing operations |
| pvc_snapshot_and_clone/test_pgsql_pvc_snapshot_and_clone.py | ~2 | PGSQL PVC snapshot/clone |
| pvc_snapshot_and_clone/test_pgsql_pvc_snapshot_and_clone_with_base_operation.py | ~2 | PGSQL snapshot/clone + base ops |

## Marks Used
`@magenta_squad`, `@polarion_id`

## Related
- [[magenta_squad]]
- [[ceph-csi]]
- [[rook-ceph]]
