---
directory: tests/functional/ui/
squad: black_squad
test_files: 10
test_functions: 28
tiers: {tier1: 4, tier2: 12, tier3: 2, tier4: 0}
---

# UI (Functional)

ODF console UI tests: PV encryption, capacity breakdown, health overview, alerts, quickstarts, storage consumption trend, scale, error improvements, non-admin user.

## Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_pv_encryption_ui.py | ~4 | PV encryption UI validation |
| test_capacity_breakdown_ui.py | ~3 | Capacity breakdown dashboard |
| test_health_overview.py | ~3 | Health overview page |
| test_alert_text.py | ~3 | Alert text validation |
| test_quickstarts.py | ~3 | Quickstart guides |
| test_odf_storage_consumption_trend.py | ~2 | Storage trend charts |
| test_scale.py | ~2 | UI scale tests |
| test_error_improvements.py | ~2 | Error message UI |
| test_non_admin_user.py | ~2 | Non-admin access |

## Marks Used
`@black_squad`, `@green_squad` (2 files), `@tier1`, `@tier2`, `@tier3`, `@polarion_id`, `@ui`

## Related
- [[black_squad]]
- [[odf-console]]
- [[tests-cross_functional-ui]]
