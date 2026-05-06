---
directory: tests/functional/pod_and_daemons/
squad: brown_squad
test_files: 9
test_functions: 20
tiers: {tier1: 4, tier2: 4, tier3: 0, tier4: 3}
---

# Pod and Daemons

Ceph daemon management, pod disruptions, OSD/MON/MDS pod operations, daemon kill/restart tests.

## Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_*.py | 20 | Daemon kill, restart, pod disruptions |

## Multi-Squad Ownership
- **brown_squad**: 6 files — daemon operations, pod management
- **green_squad**: 3 files — CSI plugin pod operations

## Marks Used
`@brown_squad`, `@green_squad`, `@tier1`, `@tier2`, `@tier4`, `@polarion_id`

## Related
- [[brown_squad]]
- [[green_squad]]
- [[rook-ceph]]
