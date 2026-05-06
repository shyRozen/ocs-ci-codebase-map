---
squad: orange_squad
test_count: 43
file_count: 29
primary_areas: [Scale, PVC Scale, NooBaa Scale]
---

# Orange Squad

## Test Areas
- [[tests-cross_functional-scale]] — 36 tests across 28 files
  - Ceph/PVC scale: 13 files (PVC creation/deletion, OSD balancing, CephFS many files)
  - NooBaa scale: 12 files (OBC creation, bucket replication, namespace CRD/RPC)
  - Scale upgrade: 3 files (upgrade with scaled PVCs/OBCs)
- [[tests-functional-workloads]] — 71 tests (1 file: create_scale_pods_and_pvcs)

## ODF Components
- [[ceph-csi]] — CSI performance at scale
- [[mcg-noobaa]] — NooBaa endpoint scaling
- [[rook-ceph]] — OSD scaling

## Key Marks
`@orange_squad`, `@scale`, `@polarion_id`
