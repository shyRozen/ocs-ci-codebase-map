---
component: odf-console
squad: black_squad
test_areas: [UI Functional, UI Cross-Functional, MCG UI]
---

# ODF Console

ODF Console plugin for OpenShift. Dashboard views, capacity breakdown, health overview, storage topology, pool management, bucket management UI.

## Test Coverage
- [[tests-functional-ui]] — 28 tests, functional UI validation
- [[tests-cross_functional-ui]] — 11 tests, cross-functional UI (topology, validation)
- [[tests-functional-object-mcg]] — 21 UI tests (bucket policy, versioning, lifecycle, namespace store)

## Framework Classes
- `ocs_ci/ocs/ui/` — UI page objects (Selenium-based)
  - Page Object Model for ODF console pages
  - Navigation helpers, element locators
  - Screenshot and validation utilities
- `tests/libtest/test_ui_pom.py` — UI POM unit tests

## Related
- [[black_squad]]
- [[monitoring]] (dashboard alerts/metrics)
