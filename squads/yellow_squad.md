---
squad: yellow_squad
test_count: 39
file_count: 12
primary_areas: [Provider Mode, Managed Service, Multicluster, Data Replication]
---

# Yellow Squad

## Test Areas
- [[tests_functional_provider_mode]] — 1 test (ceph_csi_image_versions)
- [[tests_functional_data_replication_separation]] — 4 tests (host_network, resiliency)
- [[tests_functional_storageclass]] — 29 tests (1 file: storageclassclaim)
- [[tests_functional_upgrade]] — 39 tests (2 files: test_ms_upgrade, test_upgrade)
- [[tests_functional_z_cluster]] — 115 tests (1 file: ms_pod_disruptions)
- [[tests_cross_functional_system_test]] — 23 tests (3 multicluster files)
- [[tests_libtest]] — 111 tests (2 files: sanity_provider_mode, hci_pc_markers)

## ODF Components
- [[ocs-operator]] — Provider/client mode, managed service
- [[rook-ceph]] — Multicluster, data replication

## Key Marks
`@yellow_squad`, `@polarion_id`, `@managed_service`, `@provider_client`
