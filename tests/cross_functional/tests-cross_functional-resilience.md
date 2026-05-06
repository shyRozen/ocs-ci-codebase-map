---
directory: tests/cross_functional/resilience/
squad: green_squad
test_files: 4
test_functions: 5
tiers: {tier1: 0, tier2: 0, tier3: 0, tier4: 0}
---

# Resilience

Storage component failure scenarios, platform failure scenarios, app scale on storage failure, OCS monkey chaos testing.

## Test Files
| File | Squad | Tests | Key Tests |
|------|-------|-------|-----------|
| test_storage_component_failure_scenarios.py | green | ~2 | Storage component failures |
| test_platfrom_failures_scenarios.py | green | ~1 | Platform-level failures |
| test_app_scale_on_storage_component_failure.py | green | ~1 | App scaling during failures |
| test_ocs_monkey.py | magenta | ~1 | OCS monkey chaos |

## Marks Used
`@green_squad`, `@magenta_squad`, `@polarion_id`

## Related
- [[green_squad]]
- [[magenta_squad]]
- [[rook-ceph]]
