---
directory: tests/functional/z_cluster/
squad: brown_squad
test_files: 56
test_functions: 102
tiers: {tier1: 3, tier2: 15, tier4: 21, tier4a: 6, tier4b: 11, tier4c: 5}
---

# Z Cluster

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| nodes/ | 18 | 45 |
| cluster_expansion/ | 10 | 19 |
| test_ceph_default_values_check.py/ | 1 | 5 |
| test_storagecluster_ceph_full_thresholds_params.py/ | 1 | 3 |
| test_multiple_mds.py/ | 1 | 2 |
| test_performance_profile_validation.py/ | 1 | 2 |
| test_scc.py/ | 1 | 2 |
| upgrade/ | 1 | 2 |
| test_add_mds_to_cluster.py/ | 1 | 1 |
| test_ceph_pg_log_dups_trim.py/ | 1 | 1 |
| test_coredump_check_for_ceph_daemon_crash.py/ | 1 | 1 |
| test_delete_local_volume_sym_link.py/ | 1 | 1 |
| test_delete_osd_deployment.py/ | 1 | 1 |
| test_delete_rook_ceph_mon_pod.py/ | 1 | 1 |
| test_hugepages.py/ | 1 | 1 |
| test_mon_data_avail_warn.py/ | 1 | 1 |
| test_mon_log_trimming.py/ | 1 | 1 |
| test_ms_pod_disruptions.py/ | 1 | 1 |
| test_must_gather.py/ | 1 | 1 |
| test_must_gather_minimal_crds.py/ | 1 | 1 |
| test_must_gather_modular.py/ | 1 | 1 |
| test_no_liveness_probe.py/ | 1 | 1 |
| test_noobaa_xss_vulnerability.py/ | 1 | 1 |
| test_osd_heap_profile.py/ | 1 | 1 |
| test_remove_mon_from_cluster.py/ | 1 | 1 |
| test_restart_mgr_while_two_mons_down.py/ | 1 | 1 |
| test_rook_ceph_log_rotate.py/ | 1 | 1 |
| test_rook_ceph_operator_log_type.py/ | 1 | 1 |
| test_rook_ceph_osd_flapping.py/ | 1 | 1 |
| test_rook_operator_restart_during_mon_failover.py/ | 1 | 1 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_nodes_restart_hci.py | 9 | brown_squad |
| test_resize_osd.py | 6 | brown_squad |
| test_nodes_maintenance.py | 6 | brown_squad |
| test_add_capacity.py | 5 | brown_squad |
| test_nodes_restart.py | 5 | brown_squad |
| test_ceph_default_values_check.py | 5 | brown_squad |
| test_disk_failures.py | 4 | brown_squad |
| test_non_ocs_taint_and_toleration.py | 4 | brown_squad |
| test_node_replacement_proactive.py | 3 | brown_squad |
| test_storagecluster_ceph_full_thresholds_params.py | 3 | brown_squad |

## Related
- [[brown_squad]]
