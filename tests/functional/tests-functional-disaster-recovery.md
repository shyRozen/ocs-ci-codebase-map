---
directory: tests/functional/disaster-recovery/
squad: turquoise_squad
test_files: 39
test_functions: 45
tiers: {tier1: 21, tier2: 5, tier3: 3, tier4: 12}
---

# Disaster Recovery

Regional DR (failover, relocate, discovered apps, CNV), Metro DR (app failover, zone down, hub down), SC Arbiter (stretch cluster, node drain, device replacement).

## Subdirectories
| Dir | Files | Tests | Focus |
|-----|-------|-------|-------|
| regional-dr/ | 22 | 26 | Failover, relocate, sequential, CNV, CG config |
| sc_arbiter/ | 10 | 12 | Stretch cluster, MON/OSD failures, add capacity |
| metro-dr/ | 7 | 7 | Metro failover/relocate, zone down, hub down |

## Key Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| regional-dr/test_failover_and_relocate.py | ~2 | Basic failover + relocate |
| regional-dr/test_failover.py | ~1 | Standalone failover |
| regional-dr/test_relocate.py | ~1 | Standalone relocate |
| regional-dr/test_cnv_app_failover_and_relocate.py | ~1 | CNV DR |
| metro-dr/test_app_failover_and_relocate.py | ~1 | Metro DR basic |
| sc_arbiter/test_mon_osd_failures.py | ~2 | MON/OSD failure in stretch |
| sc_arbiter/test_noobaa_in_stretch.py | ~1 | NooBaa in stretch (@red_squad) |

## Marks Used
`@turquoise_squad`, `@red_squad` (NooBaa/RGW in stretch), `@tier1`, `@tier2`, `@tier3`, `@tier4`, `@polarion_id`

## Related
- [[turquoise_squad]]
- [[disaster-recovery]]
- [[rook-ceph]]
