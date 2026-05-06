---
directory: tests/cross_functional/longevity/
squad: magenta_squad
test_files: 6
test_functions: 6
tiers: {tier1: 0, tier2: 0, tier3: 0, tier4: 0}
---

# Longevity

Multi-stage longevity testing: 5 stages (stage0-stage4) plus an all-stages orchestrator. Sustained workload over extended periods.

## Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_all_stages.py | 1 | Run all longevity stages |
| test_stage0.py | 1 | Stage 0 — initial setup |
| test_stage1.py | 1 | Stage 1 — workload ramp |
| test_stage2.py | 1 | Stage 2 — sustained load |
| test_stage3.py | 1 | Stage 3 — stress + disruption |
| test_stage4.py | 1 | Stage 4 — cleanup + validation |

## Marks Used
`@magenta_squad`, `@polarion_id`

## Related
- [[magenta_squad]]
- [[rook-ceph]]
- [[framework-ocs]] (Longevity class in ocs_ci/ocs/longevity.py)
