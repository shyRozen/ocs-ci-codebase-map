---
path: ocs_ci/ocs/constants.py
lines: 3871
---

# Framework Constants

Central constants file for the entire ocs-ci framework. Defines platform constants, squad mappings, resource names, image references, Ceph parameters.

## Key Constant Categories

### Squad Mapping
Squad decorators mapped to test areas for CI routing.

### Platform Constants
- `AWS_PLATFORM`, `VSPHERE_PLATFORM`, `AZURE_PLATFORM`, `GCP_PLATFORM`, `IBM_PLATFORM`, `BAREMETAL_PLATFORM`
- `ROSA_PLATFORM`, `FUSIONAAS_PLATFORM`

### Storage Constants
- `CEPHBLOCKPOOL`, `CEPHFILESYSTEM`, `CEPH_RGW`
- `DEFAULT_STORAGECLASS_CEPHFS`, `DEFAULT_STORAGECLASS_RBD`
- `VOLUME_MODE_FILESYSTEM`, `VOLUME_MODE_BLOCK`
- `IMMEDIATE_VOLUMEBINDINGMODE`, `WFFC_VOLUMEBINDINGMODE`

### Resource Names
- Pod names, deployment names, DaemonSet names
- Operator names, CSV patterns
- Namespace constants

### Image References
- Ceph images, CSI images, NooBaa images

### Status Constants
- `STATUS_RUNNING`, `STATUS_BOUND`, `STATUS_AVAILABLE`
- Health states, phase constants

### Timeouts
- Various timeout values for operations

## Related
- [[framework-core]]
- [[framework-ocs]]
