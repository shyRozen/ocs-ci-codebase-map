---
path: ocs_ci/utility/
modules: 87
total_lines: 38770
---

# Framework Utility

General utilities, cloud provider helpers, KMS, Prometheus, SSL, versioning, storage cluster setup.

## Key Modules (by size)
| File | Lines | Purpose |
|------|-------|---------|
| utils.py | 6957 | General utilities (huge: exec, wait, resource mgmt) |
| aws.py | 3403 | AWS operations (EC2, EBS, S3, Route53) |
| kms.py | 2727 | KMS integration (Vault, KMIP, Azure KMS) |
| vsphere.py | 1974 | vSphere/VMware utilities |
| ibmcloud.py | 1855 | IBM Cloud utilities |
| rosa.py | 1420 | ROSA utilities |
| azure_utils.py | 1266 | Azure utilities |
| iscsi_config.py | 935 | iSCSI configuration |
| prometheus.py | 847 | Prometheus query/validation |
| ssl_certs.py | 796 | SSL certificate management |
| storage_cluster_setup.py | 753 | Storage cluster setup helpers |
| operators.py | 728 | Operator installation/management |
| deployment_openshift_logging.py | 713 | OpenShift logging deployment |
| nfs_utils.py | 690 | NFS utilities |
| version.py | 598 | OCS/ODF version management |

## Key Functions (utils.py)
- `run_cmd()` — Execute shell commands
- `wait_for_resource_state()` — Wait for resource state
- `TimeoutSampler` — Polling with timeout
- `create_resource()` — Create K8s resources
- `get_pod_node()` — Get node for pod

## Related
- [[framework-core]]
- [[framework-ocs]]
- [[framework-helpers]]
