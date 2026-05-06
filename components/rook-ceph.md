---
component: rook-ceph
squad: brown_squad
test_areas: [z_cluster, Pod/Daemons, Nodes, Cluster Expansion]
---

# Rook-Ceph

Rook operator for Ceph. Manages Ceph daemons (OSD, MON, MDS, MGR), cluster health, node operations, capacity management.

## Test Coverage
- [[tests-functional-z_cluster]] — 115 tests, cluster ops, daemons, health
- [[tests-functional-pod_and_daemons]] — 20 tests, daemon management
- [[tests-functional-nfs_feature]] — 14 tests, NFS on Ceph
- [[tests-functional-disaster-recovery]] — 45 tests, stretch cluster, DR
- [[tests-cross_functional-krkn_chaos]] — 24 tests, chaos on Ceph
- [[tests-cross_functional-resilience]] — 5 tests, failure scenarios
- [[tests-cross_functional-longevity]] — 6 tests, sustained operations

## Framework Classes
- `ocs_ci/ocs/cluster.py` (4160 lines) — CephCluster, CephHealthMonitor
- `ocs_ci/ocs/node.py` (3709 lines) — Node operations
- `ocs_ci/ocs/platform_nodes.py` (3876 lines) — Platform-specific node ops
- `ocs_ci/ocs/resources/pod.py` (4702 lines) — Pod management
- `ocs_ci/ocs/resources/storage_cluster.py` (3608 lines) — StorageCluster
- `ocs_ci/ocs/rados_utils.py` (631 lines) — RADOS utilities
- `ocs_ci/ocs/ceph_debug.py` — Ceph debug tools

## Related
- [[brown_squad]]
- [[green_squad]] (CSI driver on top of Ceph)
- [[ocs-operator]]
