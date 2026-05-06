---
path: ocs_ci/deployment/
modules: 52
total_lines: 34955
---

# Framework Deployment

Platform deployers, OCS/ODF installation, multicluster deployment, ACM, CNV, MetalLB, Fusion.

## Key Modules (by size)
| File | Lines | Purpose |
|------|-------|---------|
| hub_spoke.py | 8236 | Hub-spoke multicluster deployment |
| deployment.py | 4483 | Base Deployment class, DR deploy ops |
| vmware.py | 3478 | VMware/vSphere deployer |
| baremetal.py | 1838 | Bare metal deployer |
| ibmcloud.py | 1483 | IBM Cloud deployer |
| aws.py | 957 | AWS IPI/UPI/Flexy deployers |
| cnv.py | 955 | CNV installer |
| metallb.py | 882 | MetalLB installer |
| mce.py | 791 | MCE (Multi-Cluster Engine) |
| flexy.py | 662 | Flexy deployment |
| disconnected.py | 571 | Disconnected environment |
| assisted_installer.py | 571 | Assisted installer |
| fusion_data_foundation.py | 523 | Fusion Data Foundation |
| rosa.py | 474 | ROSA (Red Hat OpenShift on AWS) |
| acm.py | 469 | ACM + Submariner |

## Key Classes
- **Deployment** — Base deployment class
- **DeploymentFactory** — Factory for platform-specific deployers
- **CloudDeploymentBase** — Cloud platform base
- **AWSIPI / AWSUPI / AWSUPIFlexy** — AWS deployers
- **AZUREBase / AZUREIPI** — Azure deployers
- **GCPBase / GCPIPI** — GCP deployers
- **IBMDeployment** — IBM deployer
- **CNVInstaller** — CNV deployment
- **Submariner** — Submariner for multicluster
- **RBDDRDeployOps** — RBD DR deployment
- **MultiClusterDROperatorsDeploy** — DR operators

## Platform Coverage
AWS, Azure, GCP, IBM Cloud, VMware, Bare Metal, ROSA, Flexy, Assisted Installer, Disconnected, RHV, Fusion, Fusion-as-a-Service

## Related
- [[framework-core]]
- [[framework-ocs]]
- [[tests_functional_deployment]]
