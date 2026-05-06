---
path: ocs_ci/framework/
modules: 24
total_lines: 5083
---

# Framework Core

Pytest plugins, configuration management, test base classes, custom marks, reporting, logging.

## Key Modules
| File | Lines | Purpose |
|------|-------|---------|
| __init__.py | 755 | Config, MultiClusterConfig, GlobalVariables |
| pytest_customization/ocscilib.py | 1228 | Pytest hooks, CLI params, collection, setup/teardown |
| pytest_customization/marks.py | 904 | Squad marks, tier marks, platform marks, skip conditions |
| pytest_customization/reports.py | 176 | Test reporting |
| custom_logger.py | 187 | Custom logging setup |
| logger_helper.py | 108 | Log helper utilities |
| testlib.py | 55 | BaseTest, E2ETest, ManageTest, MCGTest |
| main.py | 30 | Entry point, init_ocsci_conf() |
| deploy.py | 30 | Deploy helpers |
| logger_factory.py | 29 | Logger factory |
| exceptions.py | 44 | Framework exceptions |

## Subdirectories
| Dir | Purpose |
|-----|---------|
| conf/ | YAML config files (89 files), OCP/OCS/FDF/Fusion version configs |
| pytest_customization/ | Pytest plugin, marks, reports |
| fusion/ | Fusion integration config |
| fusion_data_foundation/ | FDF integration config |
| tests/ | Framework self-tests |

## Key Classes
- **Config** — main configuration management, cluster config
- **MultiClusterConfig** — multicluster config support
- **ConfigSafeThread** — thread-safe config access
- **GlobalVariables** — shared global state
- **BaseTest** — test base class
- **E2ETest** — end-to-end test base
- **ManageTest** — management test base
- **MCGTest** — MCG-specific test base

## Key Marks (from marks.py)
`@tier1`..`@tier4`, `@acceptance`, `@manage`, `@ecosystem`, `@polarion_id`, `@green_squad`..`@aqua_squad`, `@scale`, `@performance`, `@system_test`

## Related
- [[framework-ocs]]
- [[framework-constants]]
