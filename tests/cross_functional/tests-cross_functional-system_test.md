---
directory: tests/cross_functional/system_test/
squad: magenta_squad
test_files: 14
test_functions: 23
tiers: {tier1: 1, tier2: 3, tier3: 0, tier4: 0}
---

# System Test

End-to-end system tests: cluster full recovery, graceful shutdown, MCG recovery/replication, clone deletion, object expiration, cluster-wide key rotation.

## Subdirectories
| Dir | Files | Tests | Focus |
|-----|-------|-------|-------|
| (root) | 10 | ~17 | Core system tests (@magenta_squad) |
| multicluster/ | 3 | ~5 | Multicluster acceptance (@yellow_squad) |
| mon/ | 1 | ~1 | MON quorum restore |

## Key Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_full_cluster_health.py | ~2 | Full cluster health system test |
| test_cluster_full_and_recovery.py | ~2 | Cluster full + recovery |
| test_graceful_nodes_shutdown.py | ~1 | Graceful node shutdown |
| test_mcg_recovery.py | ~2 | MCG recovery scenarios |
| test_mcg_replication_with_disruptions.py | ~2 | Replication under disruption |
| test_nsfs_system.py | ~2 | NSFS system test |
| multicluster/test_acceptance.py | ~2 | Multicluster acceptance |

## Marks Used
`@magenta_squad`, `@yellow_squad` (multicluster), `@tier1`, `@tier2`, `@system_test`, `@polarion_id`

## Related
- [[magenta_squad]]
- [[yellow_squad]] (multicluster)
- [[rook-ceph]]
