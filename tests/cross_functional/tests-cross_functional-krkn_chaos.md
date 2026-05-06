---
directory: tests/cross_functional/krkn_chaos/
squad: green_squad
test_files: 6
test_functions: 24
tiers: {tier1: 0, tier2: 0, tier3: 0, tier4: 0}
---

# Krkn Chaos

Chaos engineering using Krkn framework: application outage, node scenarios, network chaos, hog scenarios, container chaos, random chaos.

## Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_krkn_application_outage_scenarios.py | ~4 | Application outage injection |
| test_krkn_node_scenarios.py | ~5 | Node failure scenarios |
| test_krkn_network_chaos_scenarios.py | ~4 | Network chaos/partition |
| test_krkn_hog_scenarios.py | ~4 | Resource hog (CPU/memory/IO) |
| test_krkn_container_chaos.py | ~4 | Container kill/restart chaos |
| test_random_chaos.py | ~3 | Random chaos selection |

## Marks Used
`@green_squad`, `@polarion_id`

## Related
- [[green_squad]]
- [[rook-ceph]]
- [[ceph-csi]]
