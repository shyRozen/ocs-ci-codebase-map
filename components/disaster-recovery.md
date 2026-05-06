---
component: disaster-recovery
squad: turquoise_squad
test_areas: [Regional DR, Metro DR, SC Arbiter]
---

# Disaster Recovery

DR orchestration (Ramen/ODF-DR). Regional DR (failover/relocate across sites), Metro DR (active-active metro distance), SC Arbiter (stretch cluster with arbiter).

## Test Coverage
- [[tests-functional-disaster-recovery]] — 45 tests across 39 files
  - Regional DR: failover, relocate, sequential, CNV, discovered apps, CG config
  - Metro DR: app failover/relocate, zone down, hub down
  - SC Arbiter: stretch cluster operations, MON/OSD failures, device replacement

## Framework Classes
- `ocs_ci/helpers/dr_helpers.py` (2922 lines) — DR failover/relocate helpers
- `ocs_ci/helpers/dr_helpers_ui.py` (975 lines) — DR UI helpers
- `ocs_ci/ocs/dr/` — DR operations subpackage
- `ocs_ci/ocs/resources/drpc.py` — DR PlacementControl
- `ocs_ci/ocs/resources/stretchcluster.py` (745 lines) — Stretch cluster
- `ocs_ci/ocs/dr_upgrade.py` (400 lines) — DR upgrade support
- `ocs_ci/helpers/stretchcluster_helper.py` (418 lines) — Stretch cluster helpers
- `ocs_ci/deployment/deployment.py` — RBDDRDeployOps, MultiClusterDROperatorsDeploy

## Related
- [[turquoise_squad]]
- [[rook-ceph]]
- [[ocs-operator]]
