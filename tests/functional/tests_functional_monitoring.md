---
directory: tests/functional/monitoring/
squad: blue_squad
test_files: 24
test_functions: 55
tiers: {tier1: 4, tier2: 8, tier3: 1, tier4: 10, tier4a: 4, tier4b: 1, tier4c: 6}
---

# Monitoring

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| prometheus/ | 17 | 37 |
| libtest/ | 2 | 7 |
| pagerduty/ | 2 | 6 |
| workload/ | 1 | 3 |
| sendgrid/ | 1 | 1 |
| test_monitoring_tool.py/ | 1 | 1 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_alert_mds_cache_high_usage.py | 6 | blue_squad |
| test_monitoring_defaults.py | 6 | blue_squad |
| test_workload_fixture.py | 5 | blue_squad |
| test_deployment_status.py | 5 | blue_squad |
| test_deployment_status.py | 4 | blue_squad |
| test_ceph.py | 3 | blue_squad |
| test_monitoring_negative.py | 3 | blue_squad |
| test_workload_with_distruptions.py | 3 | blue_squad |
| test_workload_example.py | 2 | blue_squad |
| test_alerting_works.py | 2 | blue_squad |

## Related
- [[blue_squad]]
