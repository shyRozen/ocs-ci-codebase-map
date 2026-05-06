---
path: ocs_ci/ocs/
modules: 173
total_lines: 98645
---

# Framework OCS

Resource classes, cluster management, workload operators, Ceph operations, platform node management.

## Top-Level Modules (by size)
| File | Lines | Purpose |
|------|-------|---------|
| cluster.py | 4160 | CephCluster, CephHealthMonitor, LVM |
| platform_nodes.py | 3876 | Platform-specific node ops (AWS, VMware, BM, etc.) |
| constants.py | 3871 | All constants (see [[framework-constants]]) |
| node.py | 3709 | Node operations, drain, restart, scheduling |
| bucket_utils.py | 3594 | Bucket operations, S3 utils, multipart |
| ocp.py | 2249 | OCP resource management (generic OCP class) |
| utils.py | 2241 | General OCS utilities |
| scale_lib.py | 1964 | Scale test libraries |
| longevity.py | 1511 | Longevity test orchestration |
| machine.py | 1362 | Machine/MachineSet operations |
| ocs_upgrade.py | 1293 | OCS upgrade procedures |
| perftests.py | 1073 | Performance test base class |
| amq.py | 1049 | AMQ workload operator |
| external_ceph.py | 1001 | External Ceph cluster support |
| exceptions.py | 844 | OCS exception classes |

## resources/ Subpackage (key modules)
| File | Lines | Purpose |
|------|-------|---------|
| pod.py | 4702 | Pod class, exec, volume mounts |
| storage_cluster.py | 3608 | StorageCluster CR management |
| mcg.py | 1359 | MCG/NooBaa resource management |
| storageconsumer.py | 1303 | Storage consumer management |
| pvc.py | 948 | PVC class, creation, deletion |
| cloud_manager.py | 758 | Cloud provider clients (AWS, Azure, GCP) |
| stretchcluster.py | 745 | Stretch cluster resource |
| objectbucket.py | 736 | OBC/OB resources |
| pv.py | 409 | PV operations |

## Other Subdirectories
| Dir | Purpose |
|-----|---------|
| acm/ | ACM integration |
| bdi/ | BDI workload |
| cnv/ | CNV integration |
| dr/ | DR operations (Ramen) |
| must_gather/ | Must-gather collection |
| ui/ | UI page objects, Selenium |
| tests/ | OCS module self-tests |

## Key Classes
- **CephCluster** — Ceph cluster operations, health, status
- **CephHealthMonitor** — Background health monitoring thread
- **OCP** — Generic OpenShift resource management
- **Pod** — Pod lifecycle, exec, IO
- **PVC** — PVC operations
- **StorageCluster** — StorageCluster CR management
- **MCG** — NooBaa resource management
- **Longevity** — Longevity test orchestration
- **BenchmarkOperator** — Base for perf workloads

## Related
- [[framework-core]]
- [[framework-helpers]]
- [[framework-constants]]
