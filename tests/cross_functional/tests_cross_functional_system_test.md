---
directory: tests/cross_functional/system_test/
squad: yellow_squad
test_files: 12
test_functions: 20
tiers: {}
---

# System Test

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| multicluster/ | 3 | 9 |
| test_mcg_replication_with_disruptions.py/ | 1 | 2 |
| test_object_expiration_system.py/ | 1 | 2 |
| mon/ | 1 | 1 |
| test_clone_deletion_after_max_cluster_space_utilization.py/ | 1 | 1 |
| test_cluster_full_and_recovery.py/ | 1 | 1 |
| test_full_cluster_health.py/ | 1 | 1 |
| test_graceful_nodes_shutdown.py/ | 1 | 1 |
| test_mcg_recovery.py/ | 1 | 1 |
| test_nsfs_system.py/ | 1 | 1 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_post_installation_state.py | 5 | yellow_squad |
| test_switch_to_correct_index_at_setup.py | 3 | yellow_squad |
| test_mcg_replication_with_disruptions.py | 2 | magenta_squad |
| test_object_expiration_system.py | 2 | mixed |
| test_restore_ceph_mon_quorum.py | 1 | magenta_squad |
| test_acceptance.py | 1 | yellow_squad |
| test_clone_deletion_after_max_cluster_space_utilization.py | 1 | mixed |
| test_cluster_full_and_recovery.py | 1 | magenta_squad |
| test_full_cluster_health.py | 1 | magenta_squad |
| test_graceful_nodes_shutdown.py | 1 | mixed |

## Related
- [[yellow_squad]]
