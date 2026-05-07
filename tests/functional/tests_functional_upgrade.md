---
directory: tests/functional/upgrade/
squad: brown_squad
test_files: 9
test_functions: 22
tiers: {tier2: 1}
---

# Upgrade

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| test_noobaa.py/ | 1 | 5 |
| test_resources.py/ | 1 | 4 |
| test_upgrade.py/ | 1 | 4 |
| test_configuration.py/ | 1 | 2 |
| test_monitoring_after_ocp_upgrade.py/ | 1 | 2 |
| test_upgrade_sc_allowexpansion_false.py/ | 1 | 2 |
| test_logging_upgrade.py/ | 1 | 1 |
| test_storagecluster_upgrade_params.py/ | 1 | 1 |
| test_upgrade_ocp.py/ | 1 | 1 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_noobaa.py | 5 | red_squad |
| test_resources.py | 4 | brown_squad |
| test_upgrade.py | 4 | purple_squad |
| test_configuration.py | 2 | brown_squad |
| test_monitoring_after_ocp_upgrade.py | 2 | magenta_squad |
| test_upgrade_sc_allowexpansion_false.py | 2 | green_squad |
| test_logging_upgrade.py | 1 | magenta_squad |
| test_storagecluster_upgrade_params.py | 1 | brown_squad |
| test_upgrade_ocp.py | 1 | purple_squad |

## Related
- [[brown_squad]]
