---
component: ocs-operator
squad: purple_squad
test_areas: [Deployment, Upgrade, Provider Mode, External Mode]
---

# OCS Operator

OCS/ODF operator. Manages StorageCluster CR, operator lifecycle, upgrades, provider/client mode, external mode.

## Test Coverage
- [[tests-functional-deployment]] — 4 tests, operator deployment
- [[tests-functional-upgrade]] — 39 tests, OCS/ODF/OCP upgrade
- [[tests-functional-provider_mode]] — 1 test, provider mode
- [[tests-functional-external_mode]] — 1 test, external mode
- [[tests-functional-z_cluster]] — 115 tests (cluster expansion/operations)

## Framework Classes
- `ocs_ci/ocs/resources/storage_cluster.py` (3608 lines) — StorageCluster CR
- `ocs_ci/ocs/resources/storageconsumer.py` (1303 lines) — Storage consumer
- `ocs_ci/ocs/resources/storage_client.py` (572 lines) — Storage client
- `ocs_ci/ocs/resources/csv.py` — ClusterServiceVersion
- `ocs_ci/ocs/resources/packagemanifest.py` (309 lines) — PackageManifest
- `ocs_ci/ocs/ocs_upgrade.py` (1293 lines) — OCS upgrade procedures
- `ocs_ci/ocs/managedservice.py` (456 lines) — Managed service support

## Related
- [[purple_squad]]
- [[brown_squad]] (cluster operations)
- [[yellow_squad]] (provider/managed service)
- [[rook-ceph]]
