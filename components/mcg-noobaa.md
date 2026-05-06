---
component: mcg-noobaa
squad: red_squad
test_areas: [MCG, RGW, Scale NooBaa, Performance MCG]
---

# MCG / NooBaa

Multi-Cloud Gateway (NooBaa). S3-compatible object storage, bucket management, namespace stores, replication, NSFS, lifecycle policies.

## Test Coverage
- [[tests_functional_object_mcg]] — 228 tests, core MCG operations
- [[tests_functional_object_rgw]] — 16 tests, RGW integration
- [[tests_cross_functional_scale]] — 36 tests (12 NooBaa scale files)
- [[tests_cross_functional_performance]] — 34 tests (1 MCG CosBench file)
- [[tests_cross_functional_kcs]] — 8 tests (NooBaa rebuild, DB backup, password reset)
- [[tests_cross_functional_system_test]] — 23 tests (MCG recovery, replication, NSFS)

## Framework Classes
- `ocs_ci/ocs/resources/mcg.py` (1359 lines) — MCG resource management
- `ocs_ci/ocs/resources/objectbucket.py` (736 lines) — OBC/OB resources
- `ocs_ci/ocs/resources/backingstore.py` (532 lines) — BackingStore
- `ocs_ci/ocs/resources/namespacestore.py` (497 lines) — NamespaceStore
- `ocs_ci/ocs/resources/bucketclass.py` — BucketClass
- `ocs_ci/ocs/bucket_utils.py` (3594 lines) — Bucket operations
- `ocs_ci/ocs/scale_noobaa_lib.py` (573 lines) — NooBaa scale library

## Related
- [[red_squad]]
- [[black_squad]] (MCG UI)
- [[orange_squad]] (NooBaa scale)
