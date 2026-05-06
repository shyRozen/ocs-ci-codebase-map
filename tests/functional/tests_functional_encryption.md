---
directory: tests/functional/encryption/
squad: green_squad
test_files: 5
test_functions: 11
tiers: {tier1: 7, tier2: 2, tier3: 0, tier4: 1}
---

# Encryption

In-transit encryption sanity, encryption configuration dashboard, key rotation, MON failure during in-transit encryption, data integrity.

## Test Files
| File | Tests | Tier | Key Tests |
|------|-------|------|-----------|
| test_intransit_encryption_sanity.py | ~3 | tier1 | In-transit encryption basic validation |
| test_encryption_configuration_dashboard.py | ~2 | tier1 | Dashboard encryption config |
| test_encryption_keyrotation.py | ~2 | tier1 | Key rotation operations |
| test_mon_failure_in_intransit_encryption.py | ~2 | tier2 | MON failure during encryption |
| test_intransit_encryption_data_integrity.py | ~2 | tier4 | Data integrity with encryption |

## Marks Used
`@green_squad`, `@tier1`, `@tier2`, `@tier4`, `@polarion_id`

## Related
- [[green_squad]]
- [[ceph-csi]]
- [[tests_functional_pv]]
