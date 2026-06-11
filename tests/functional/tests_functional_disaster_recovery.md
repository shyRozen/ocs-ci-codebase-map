---
directory: tests/functional/disaster_recovery/
squad: turquoise_squad
test_files: 29
test_functions: 35
tiers: {tier1: 16, tier2: 3, tier3: 2, tier4: 8, tier4a: 6, tier4b: 2}
---

# Disaster Recovery

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| regional-dr/ | 16 | 19 |
| sc_arbiter/ | 6 | 9 |
| metro-dr/ | 7 | 7 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_mon_osd_failures.py | 3 | turquoise_squad |
| test_managed_cluster_node_failure.py | 2 | turquoise_squad |
| test_negative_failover_relocate_ui.py | 2 | turquoise_squad |
| test_warning_and_alerting.py | 2 | turquoise_squad |
| test_zone_shutdown_and_crash.py | 2 | turquoise_squad |
| test_active_hub_down_and_restore.py | 1 | turquoise_squad |
| test_app_failover_and_relocate.py | 1 | turquoise_squad |
| test_app_failover_and_relocate_when_entire_one_zone_down.py | 1 | turquoise_squad |
| test_cnv_app_failover_relocate.py | 1 | turquoise_squad |
| test_multiple_apps_failover_and_relocate.py | 1 | turquoise_squad |

## Related
- [[turquoise_squad]]
