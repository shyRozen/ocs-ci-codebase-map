---
directory: tests/functional/deployment/
squad: purple_squad
test_files: 3
test_functions: 4
tiers: {tier1: 1, tier2: 1, tier3: 0, tier4: 0}
---

# Deployment

OCS operator deployment validation, ACM (Advanced Cluster Management) deployment tests.

## Test Files
| File | Squad | Tests | Key Tests |
|------|-------|-------|-----------|
| test_deployment.py | purple | ~2 | OCS deployment validation |
| test_acm.py | purple | ~1 | ACM deployment |
| test_operator.py | brown | ~1 | Operator validation |

## Marks Used
`@purple_squad`, `@brown_squad`, `@tier1`, `@tier2`, `@polarion_id`

## Related
- [[purple_squad]]
- [[brown_squad]]
- [[ocs-operator]]
- [[framework-deployment]]
