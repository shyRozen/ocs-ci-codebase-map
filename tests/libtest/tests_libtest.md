---
directory: tests/libtest/
squad: mixed
test_files: 41
test_functions: 111
tiers: {tier1: 0, tier2: 0, tier3: 0, tier4: 0}
---

# LibTest

Unit tests and integration tests for framework libraries. Validates helpers, utilities, cloud providers, markers, workload operators, and internal APIs.

## Key Test Files
| File | Tests | Focus |
|------|-------|-------|
| test_api_client.py | ~5 | API client validation |
| test_benchmark_operator.py | ~3 | Benchmark operator |
| test_cluster_utils.py | ~4 | Cluster utility functions |
| test_fio_workload.py | ~3 | FIO workload helpers |
| test_requirements.py | ~3 | Requirement validation |
| test_awscli_leftovers.py | ~2 | AWS CLI cleanup |
| test_azure.py | ~2 | Azure cloud helpers |
| test_gcp.py | ~2 | GCP cloud helpers |
| test_ibmcloud.py | ~2 | IBM Cloud helpers |
| test_multicluster.py | ~3 | Multicluster support |
| test_metallb.py | ~2 | MetalLB (@purple_squad) |
| test_ui_pom.py | ~3 | UI Page Object Model |
| test_data_replication_separation.py | ~2 | Data replication |
| test_hci_pc_markers.py | ~2 | HCI/PC markers (@yellow_squad) |
| test_sanity_provider_mode.py | ~2 | Provider mode sanity (@yellow_squad) |

## Squad Markers
- **brown_squad**: 3 files (disk cleanup, bluestore label, Ceph rebalance)
- **yellow_squad**: 2 files (provider mode sanity, HCI markers)
- **purple_squad**: 2 files (MetalLB, provider hosted cluster)
- Most files: no squad marker (framework-level)

## Marks Used
`@brown_squad`, `@yellow_squad`, `@purple_squad`, `@polarion_id`

## Related
- [[framework-core]]
- [[framework-ocs]]
- [[framework-utility]]
