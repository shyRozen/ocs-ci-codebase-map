---
directory: tests/functional/z_cluster/
squad: brown_squad
test_files: 62
test_functions: 115
tiers: {tier1: 12, tier2: 31, tier3: 1, tier4: 59}
---

# Z-Cluster (Cluster Operations)

Cluster health, OSD/MON management, capacity, node operations, cluster expansion/reduction, device replacement, Ceph daemon operations, SCC, log rotation.

## Subdirectories
| Dir | Files | Tests | Focus |
|-----|-------|-------|-------|
| (root) | 32 | 40 | Cluster health checks, Ceph defaults, MON ops, log trim |
| nodes/ | 18 | 44 | Node drain, restart, failure, recovery |
| cluster_expansion/ | 11 | 29 | Add capacity, resize OSD, device classes (@black_squad) |
| upgrade/ | 1 | 2 | Upgrade-related cluster checks |

## Key Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| cluster_expansion/test_add_capacity.py | ~5 | Add capacity (@black_squad) |
| nodes/test_node_*.py | ~44 | Node operations |
| test_ceph_default_values_check.py | ~3 | Ceph default validation |
| test_remove_mon_from_cluster.py | ~2 | MON removal |
| test_storagesystem.py | ~2 | Storage system validation |
| test_must_gather_modular.py | ~2 | Must-gather |

## Marks Used
`@brown_squad`, `@black_squad` (expansion), `@yellow_squad`, `@tier1`, `@tier2`, `@tier3`, `@tier4`, `@polarion_id`

## Related
- [[brown_squad]]
- [[black_squad]] (cluster expansion)
- [[rook-ceph]]
- [[ocs-operator]]
