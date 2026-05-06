---
directory: tests/functional/object/mcg/
squad: red_squad
test_files: 76
test_functions: 228
tiers: {tier1: 45, tier2: 102, tier3: 18, tier4: 17}
---

# Object Storage - MCG (Multi-Cloud Gateway / NooBaa)

Bucket operations, replication, namespace stores, NSFS, S3 routes, lifecycle, versioning, admission control, OBC, multipart upload, MCG CLI, custom credentials.

## Subdirectories
| Dir | Files | Tests | Focus |
|-----|-------|-------|-------|
| (root) | 63 | 196 | Core MCG tests |
| ui/ | 7 | 21 | MCG UI tests (@black_squad) |
| lifecycle/ | 4 | 9 | Lifecycle policies |
| flowtest/ | 2 | 2 | MCG flow tests |

## Key Test Files
| File | Tests | Key Tests |
|------|-------|-----------|
| test_bucket_policy.py | 19 | Bucket policy CRUD, anonymous access |
| test_namespace_rpc.py | 15 | Namespace RPC operations |
| test_namespace_crd.py | 15 | Namespace CRD operations |
| test_cors_config_elements.py | 8 | CORS configuration |
| test_write_to_bucket.py | 7 | Write operations, cloud targets |
| test_pv_pool.py | 7 | PV-backed pools |
| test_noobaa_secret.py | 6 | NooBaa secret management |
| test_lifecycle_configuration.py | 6 | Lifecycle rules |
| test_admission_control.py | 6 | Admission webhook |
| test_nsfs.py | 5 | NFS-backed object storage |

## Marks Used
`@red_squad`, `@black_squad` (UI), `@tier1`, `@tier2`, `@tier3`, `@tier4`, `@polarion_id`, `@runs_on_provider`

## Related
- [[red_squad]]
- [[black_squad]] (UI tests)
- [[mcg-noobaa]]
- [[tests_functional_object_rgw]]
