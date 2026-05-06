---
directory: tests/cross_functional/kcs/
squad: magenta_squad
test_files: 8
test_functions: 8
tiers: {tier1: 1, tier2: 2, tier3: 4, tier4: 0}
---

# KCS (Knowledge-Centered Service)

Reproducing known customer scenarios: NooBaa rebuild, DB backup/recovery, MON crash recovery, password reset, SELinux relabel, maintenance pod, MCG external service disable.

## Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_noobaa_rebuild.py | 1 | NooBaa rebuild procedure |
| test_noobaa_db_backup_and_recovery.py | 1 | NooBaa DB backup/restore |
| test_monitor_recovery.py | 1 | MON recovery from crash |
| test_mon_crash_recovery_scenario.py | 1 | MON crash recovery |
| test_noobaadb_pw_reset.py | 1 | NooBaa DB password reset |
| test_selinux_relabel_solution.py | 1 | SELinux relabel fix |
| test_maintenance_pod.py | 1 | Maintenance pod usage |
| test_disable_mcg_external_service.py | 1 | Disable MCG external service |

## Marks Used
`@magenta_squad`, `@tier1`, `@tier2`, `@tier3`, `@polarion_id`

## Related
- [[magenta_squad]]
- [[mcg-noobaa]]
- [[rook-ceph]]
