---
directory: tests/functional/odf_cli/
squad: brown_squad
test_files: 4
test_functions: 7
tiers: {tier1: 1, tier2: 1, tier3: 1}
---

# Odf Cli

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| test_pvc_stale_volume_cleanup_cli.py/ | 1 | 3 |
| test_get_commands.py/ | 1 | 2 |
| test_debug_verbocity_of_ceph_component.py/ | 1 | 1 |
| test_operator_restart.py/ | 1 | 1 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_pvc_stale_volume_cleanup_cli.py | 3 | green_squad |
| test_get_commands.py | 2 | brown_squad |
| test_debug_verbocity_of_ceph_component.py | 1 | brown_squad |
| test_operator_restart.py | 1 | brown_squad |

## Related
- [[brown_squad]]
