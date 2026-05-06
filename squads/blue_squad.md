---
squad: blue_squad
test_count: 44
file_count: 26
primary_areas: [Monitoring, Prometheus, PagerDuty, Alerts]
---

# Blue Squad

## Test Areas
- [[tests_functional_monitoring]] — 44 tests across 26 files
  - Prometheus alerts/metrics (18 files, 32 tests)
  - PagerDuty alerts (2 files)
  - SendGrid alerts (1 file)
  - Monitoring workloads (1 file, 3 tests)
  - Libtest monitoring (2 files, 7 tests)

## ODF Components
- [[monitoring]] — Prometheus, alerting, metrics
- [[rook-ceph]] — Ceph health alerts
- [[mcg-noobaa]] — NooBaa alerts

## Key Marks
`@blue_squad`, `@tier1`..`@tier4`, `@polarion_id`
