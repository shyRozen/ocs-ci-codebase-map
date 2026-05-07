---
directory: tests/functional/pod_and_daemons/
squad: brown_squad
test_files: 6
test_functions: 10
tiers: {tier1: 1, tier2: 3, tier4: 1, tier4a: 1}
---

# Pod And Daemons

## Subdirectories

| Dir | Files | Tests |
|-----|-------|-------|
| test_cephtoolbox_pod_nodeaffinity.py/ | 1 | 3 |
| test_mgr_pods.py/ | 1 | 3 |
| test_csi_logs_rotation.py/ | 1 | 1 |
| test_csiaddon_pod_security.py/ | 1 | 1 |
| test_ephemeral_pod.py/ | 1 | 1 |
| test_mgr_enable_rook_backend_module.py/ | 1 | 1 |

## Key Test Files

| File | Tests | Squad |
|------|-------|-------|
| test_cephtoolbox_pod_nodeaffinity.py | 3 | brown_squad |
| test_mgr_pods.py | 3 | mixed |
| test_csi_logs_rotation.py | 1 | brown_squad |
| test_csiaddon_pod_security.py | 1 | green_squad |
| test_ephemeral_pod.py | 1 | brown_squad |
| test_mgr_enable_rook_backend_module.py | 1 | brown_squad |

## Related
- [[brown_squad]]
