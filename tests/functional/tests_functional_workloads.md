---
directory: tests/functional/workloads/
squad: magenta_squad
test_files: 47
test_functions: 71
tiers: {tier1: 8, tier2: 9, tier3: 0, tier4: 0}
---

# Workloads

Application workloads on ODF storage: CNV (virtual machines), OCP (registry, monitoring, logging), AMQ, PGSQL, Jenkins, Couchbase, CosBench, Quay, BDI.

## Subdirectories
| Dir | Files | Tests | Focus |
|-----|-------|-------|-------|
| cnv/ | 12 | 16 | CNV VM workloads |
| ocp/ | 9 | 18 | OCP registry, monitoring, logging |
| app/amq/ | 5 | ~5 | AMQ messaging workloads |
| app/pgsql/ | 4 | ~4 | PostgreSQL workloads |
| app/jenkins/ | 4 | ~4 | Jenkins CI workloads |
| app/couchbase/ | 4 | ~4 | Couchbase workloads |
| pvc_snapshot_and_clone/ | 2 | 3 | PVC snapshot/clone with workloads |
| app/ (other) | ~3 | ~3 | CosBench, Quay, BDI |

## Key Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_create_scale_pods_and_pvcs_using_kube_job.py | ~3 | Scale pod/PVC creation (@orange_squad) |
| test_data_consistency.py | ~2 | Data consistency validation |
| test_new_sc_rbd_e2e_workloads.py | ~2 | E2E RBD workloads |

## Marks Used
`@magenta_squad`, `@orange_squad` (scale), `@tier1`, `@tier2`, `@polarion_id`

## Related
- [[magenta_squad]]
- [[ceph-csi]]
- [[rook-ceph]]
