---
directory: tests/functional/data_replication_separation/
squad: yellow_squad
test_files: 2
test_functions: 4
tiers: {tier1: 2, tier2: 0, tier3: 0, tier4: 2}
---

# Data Replication Separation

Host network configuration and resiliency for data replication separation setups.

## Test Files
| File | Tests | Tier | Key Tests |
|------|-------|------|-----------|
| test_host_network.py | ~2 | tier1 | Host network validation |
| test_resiliency.py | ~2 | tier4 | Resiliency under separation |

## Marks Used
`@yellow_squad`, `@tier1`, `@tier4`, `@polarion_id`

## Related
- [[yellow_squad]]
- [[rook-ceph]]
