---
directory: tests/functional/workloads/
squad: magenta_squad
test_files: 37
test_functions: 60
tiers: {tier1: 3, tier2: 4}
---

# Workloads

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| app/ | 21 | 27 |
| ocp/ | 9 | 19 |
| test_create_scale_pods_and_pvcs_using_kube_job.py/ | 1 | 7 |
| pvc_snapshot_and_clone/ | 2 | 3 |
| cnv/ | 2 | 2 |
| test_data_consistency.py/ | 1 | 1 |
| test_new_sc_rbd_e2e_workloads.py/ | 1 | 1 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_monitoring_on_negative_scenarios.py | 10 | magenta_squad |
| test_create_scale_pods_and_pvcs_using_kube_job.py | 7 | magenta_squad |
| test_amq_node_reboot_and_shutdown.py | 2 | magenta_squad |
| test_amq_streamer_creation.py | 2 | magenta_squad |
| test_amq_streams.py | 2 | magenta_squad |
| test_rgw_kafka_notifications.py | 2 | magenta_squad |
| test_cosbench.py | 2 | magenta_squad |
| test_quay_operator.py | 2 | magenta_squad |
| test_registry_reboot_node.py | 2 | magenta_squad |
| test_compressed_sc_and_support_snap_clone.py | 2 | magenta_squad |

## Related
- [[magenta_squad]]
