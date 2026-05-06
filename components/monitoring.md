---
component: monitoring
squad: blue_squad
test_areas: [Monitoring, Prometheus, PagerDuty, Alerts]
---

# Monitoring

Prometheus metrics/alerts, PagerDuty integration, SendGrid alerts, ODF health monitoring, capacity alerts.

## Test Coverage
- [[tests_functional_monitoring]] — 44 tests across 26 files
  - Prometheus alerts: Ceph health, capacity, RGW, NooBaa, HPA, encryption, deployment
  - Prometheus metrics: RBD usage, OCS utilization, MCG HPA, monitoring defaults
  - PagerDuty alerts: Ceph, deployment status
  - SendGrid alerts: capacity
  - Workload monitoring: disruption scenarios

## Framework Classes
- `ocs_ci/ocs/monitoring.py` (469 lines) — Monitoring utilities
- `ocs_ci/utility/prometheus.py` (847 lines) — Prometheus query/validation
- `ocs_ci/utility/pagerduty.py` (420 lines) — PagerDuty integration
- `ocs_ci/ocs/metrics.py` — Metrics collection

## Related
- [[blue_squad]]
- [[rook-ceph]]
- [[odf-console]] (dashboard metrics)
