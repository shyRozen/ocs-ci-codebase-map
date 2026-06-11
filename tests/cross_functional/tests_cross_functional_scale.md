---
directory: tests/cross_functional/scale/
squad: orange_squad
test_files: 24
test_functions: 35
tiers: {}
---

# Scale

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| noobaa/ | 10 | 14 |
| upgrade/ | 3 | 6 |
| test_scale_12_OCS_worker_nodes_and_6000_PVCs.py/ | 1 | 4 |
| test_pvc_creation_deletion_scale.py/ | 1 | 2 |
| test_cephfs_many_files.py/ | 1 | 1 |
| test_osd_node_balancing.py/ | 1 | 1 |
| test_pods_are_not_oomkilled_while_running_ios.py/ | 1 | 1 |
| test_pv_scale_and_respin_ceph_pods.py/ | 1 | 1 |
| test_pv_scale_ocs_create_delete_pvcs.py/ | 1 | 1 |
| test_scale_3_OCS_worker_nodes_and_1500_PVCs.py/ | 1 | 1 |
| test_scale_amq.py/ | 1 | 1 |
| test_scale_pvc_expand.py/ | 1 | 1 |
| test_scale_small_file_workload.py/ | 1 | 1 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_scale_12_OCS_worker_nodes_and_6000_PVCs.py | 4 | orange_squad |
| test_hsbench.py | 2 | orange_squad |
| test_list_objects.py | 2 | orange_squad |
| test_scale_bucket_replication.py | 2 | orange_squad |
| test_scale_namespace_rpc.py | 2 | orange_squad |
| test_pvc_creation_deletion_scale.py | 2 | orange_squad |
| test_upgrade_with_scaled_obc.py | 2 | orange_squad |
| test_upgrade_with_scaled_pvcs_pods.py | 2 | orange_squad |
| test_upgrade_with_scaled_rgw_obc.py | 2 | orange_squad |
| test_delete_objects.py | 1 | orange_squad |

## Related
- [[orange_squad]]
