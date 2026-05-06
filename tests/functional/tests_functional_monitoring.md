---
directory: tests/functional/monitoring/
squad: blue_squad
test_files: 26
test_functions: 44
tiers: {tier1: 11, tier2: 11, tier3: 4, tier4: 27}
---

# Monitoring

Prometheus alerts/metrics, PagerDuty integration, SendGrid alerts, monitoring workloads, operator probe resilience.

## Subdirectories
| Dir | Files | Tests | Focus |
|-----|-------|-------|-------|
| prometheus/alerts/ | 12 | ~20 | Ceph, capacity, RGW, NooBaa, HPA, encryption alerts |
| prometheus/metrics/ | 6 | ~12 | RBD usage, OCS utilization, MCG HPA, defaults |
| pagerduty/alerts/ | 2 | 0 | PagerDuty alert integration |
| sendgrid/alerts/ | 1 | 0 | SendGrid capacity alerts |
| libtest/ | 2 | 7 | Workload examples/fixtures |
| workload/ | 1 | 3 | Workload with disruptions |

## Key Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| prometheus/alerts/test_ceph.py | ~5 | Ceph health alerts |
| prometheus/alerts/test_capacity.py | ~3 | Capacity warning/critical |
| prometheus/metrics/test_ocs_utilization.py | ~3 | OCS utilization metrics |
| test_monitoring_tool.py | ~2 | Monitoring tool validation |
| test_operator_probe_resilience.py | ~2 | Operator probe tests |

## Marks Used
`@blue_squad`, `@tier1`, `@tier2`, `@tier3`, `@tier4`, `@polarion_id`

## Related
- [[blue_squad]]
- [[monitoring]]
- [[rook-ceph]]
