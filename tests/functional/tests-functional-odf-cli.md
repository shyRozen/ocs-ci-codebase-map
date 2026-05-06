---
directory: tests/functional/odf-cli/
squad: brown_squad
test_files: 4
test_functions: 7
tiers: {tier1: 2, tier2: 3, tier3: 1, tier4: 0}
---

# ODF CLI

ODF CLI tool testing: command validation, output verification, diagnostics.

## Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_*.py | 7 | ODF CLI commands, diagnostics |

## Multi-Squad Ownership
- **brown_squad**: 3 files
- **green_squad**: 1 file

## Marks Used
`@brown_squad`, `@green_squad`, `@tier1`, `@tier2`, `@tier3`, `@polarion_id`

## Related
- [[brown_squad]]
- [[ocs-operator]]
