---
directory: tests/functional/disaster_recovery/
squad: turquoise_squad
test_files: 15
test_functions: 18
tiers: {tier1: 8, tier2: 1, tier3: 3, tier4: 3, tier4a: 1, tier4b: 2}
---

# Disaster Recovery

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| regional-dr/ | 8 | 10 |
| sc_arbiter/ | 4 | 5 |
| metro-dr/ | 3 | 3 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_managed_cluster_node_failure.py | 2 | turquoise_squad |
| test_negative_failover_relocate_ui.py | 2 | turquoise_squad |
| test_zone_shutdown_and_crash.py | 2 | turquoise_squad |
| test_active_hub_down_and_restore.py | 1 | turquoise_squad |
| test_app_failover_and_relocate.py | 1 | turquoise_squad |
| test_cnv_app_failover_relocate.py | 1 | turquoise_squad |
| test_failover.py | 1 | turquoise_squad |
| test_failover_and_relocate.py | 1 | turquoise_squad |
| test_node_operations_during_failover_relocate.py | 1 | turquoise_squad |
| test_relocate.py | 1 | turquoise_squad |

## Related
- [[turquoise_squad]]
