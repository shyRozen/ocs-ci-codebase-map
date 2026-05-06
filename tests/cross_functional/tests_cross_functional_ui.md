---
directory: tests/cross_functional/ui/
squad: black_squad
test_files: 5
test_functions: 11
tiers: {tier1: 3, tier2: 3, tier3: 5, tier4: 1}
---

# UI (Cross-Functional)

Cross-functional UI tests: ODF topology, validation UI, add capacity UI, block pool creation, SC/RBD pool creation.

## Test Files
| File | Squad | Tests | Key Tests |
|------|-------|-------|-----------|
| test_validation_ui.py | black | ~3 | UI validation checks |
| test_odf_topology.py | black | ~2 | ODF topology view |
| test_add_capacity_ui.py | brown | ~2 | Add capacity from UI |
| test_create_pool_block_pool.py | green | ~2 | Block pool creation UI |
| test_creation_and_deletion_of_sc_and_rbdpool.py | green | ~2 | SC + RBD pool UI |

## Marks Used
`@black_squad`, `@green_squad`, `@brown_squad`, `@tier1`, `@tier2`, `@tier3`, `@tier4`, `@polarion_id`, `@ui`

## Related
- [[black_squad]]
- [[odf-console]]
- [[tests_functional_ui]]
