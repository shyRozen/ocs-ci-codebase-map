---
directory: tests/functional/disaster_recovery/
squad: turquoise_squad
test_files: 20
test_functions: 25
tiers: {tier1: 10, tier2: 1, tier3: 3, tier4: 4, tier4a: 2, tier4b: 2}
---

# Disaster Recovery

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| regional-dr/ | 10 | 12 |
| sc_arbiter/ | 6 | 9 |
| metro-dr/ | 4 | 4 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_mon_osd_failures.py | 3 | turquoise_squad |
| test_managed_cluster_node_failure.py | 2 | turquoise_squad |
| test_negative_failover_relocate_ui.py | 2 | turquoise_squad |
| test_zone_shutdown_and_crash.py | 2 | turquoise_squad |
| test_active_hub_down_and_restore.py | 1 | turquoise_squad |
| test_app_failover_and_relocate.py | 1 | turquoise_squad |
| test_cnv_app_failover_relocate.py | 1 | turquoise_squad |
| test_no_data_loss_and_corruption_on_failures.py | 1 | turquoise_squad |
| test_cnv_app_failover_and_relocate.py | 1 | turquoise_squad |
| test_failover.py | 1 | turquoise_squad |

## Related
- [[turquoise_squad]]
