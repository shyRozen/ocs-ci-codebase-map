---
directory: tests/functional/upgrade/
squad: purple_squad
test_files: 10
test_functions: 39
tiers: {tier1: 0, tier2: 2, tier3: 0, tier4: 0}
---

# Upgrade

OCS/ODF upgrade tests, OCP upgrade, managed service upgrade, resource validation post-upgrade, configuration checks, Ceph health pre-checks.

## Test Files
| File | Squad | Tests | Key Tests |
|------|-------|-------|-----------|
| test_upgrade.py | purple/yellow | ~10 | OCS upgrade flow |
| test_upgrade_ocp.py | purple | ~5 | OCP upgrade |
| test_resources.py | purple/brown | ~8 | Post-upgrade resource validation |
| test_configuration.py | brown | ~4 | Configuration checks |
| test_storagecluster_upgrade_params.py | brown | ~3 | StorageCluster params |
| test_upgrade_precheck_ceph_health.py | brown | ~3 | Ceph health pre-check |
| test_ms_upgrade.py | yellow | ~3 | Managed service upgrade |

## Multi-Squad Ownership
- **purple_squad**: test_upgrade, test_upgrade_ocp, test_resources
- **brown_squad**: test_configuration, test_storagecluster_upgrade_params, test_resources, test_upgrade_precheck_ceph_health
- **yellow_squad**: test_ms_upgrade, test_upgrade
- **red_squad**: test_upgrade (NooBaa parts)
- **magenta_squad**: test_upgrade (workload parts)

## Marks Used
`@purple_squad`, `@brown_squad`, `@yellow_squad`, `@red_squad`, `@magenta_squad`, `@tier2`, `@polarion_id`, `@pre_upgrade`, `@post_upgrade`

## Related
- [[purple_squad]]
- [[brown_squad]]
- [[ocs-operator]]
