---
component: mcg-noobaa
squad: red_squad
test_areas: [MCG, RGW, Scale NooBaa, Performance MCG]
---

# MCG / NooBaa

Multi-Cloud Gateway (NooBaa). S3-compatible object storage, bucket management, namespace stores, replication, NSFS, lifecycle policies.

## Test Coverage
- [[tests-functional-object-mcg]] — 228 tests, core MCG operations
- [[tests-functional-object-rgw]] — 16 tests, RGW integration
- [[tests-cross_functional-scale]] — 36 tests (12 NooBaa scale files)
- [[tests-cross_functional-performance]] — 34 tests (1 MCG CosBench file)
- [[tests-cross_functional-kcs]] — 8 tests (NooBaa rebuild, DB backup, password reset)
- [[tests-cross_functional-system_test]] — 23 tests (MCG recovery, replication, NSFS)

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
