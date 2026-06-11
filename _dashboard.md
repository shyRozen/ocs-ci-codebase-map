# OCS-CI Codebase Map (release-4.20)

> Auto-generated map for ODF 4.20.

---

## Quick Stats

| Metric | Value |
|--------|-------|
| Test files | 507 |
| Test functions | 1002 |
| Squads | 11 |
| Test areas | 28 |

---

## Squads

| Squad | Tests |
|-------|-------|
| [[red_squad]] | 223 |
| [[green_squad]] | 167 |
| [[brown_squad]] | 150 |
| [[magenta_squad]] | 99 |
| [[orange_squad]] | 43 |
| [[turquoise_squad]] | 42 |
| [[blue_squad]] | 42 |
| [[black_squad]] | 40 |
| [[purple_squad]] | 38 |
| [[grey_squad]] | 33 |
| [[yellow_squad]] | 28 |

## Functional Tests

| Area | Tests | Files | Squad | Link |
|------|-------|-------|-------|------|
| object | 234 | 80 | red | [[tests_functional_object]] |
| pv | 112 | 81 | green | [[tests_functional_pv]] |
| z_cluster | 108 | 58 | brown | [[tests_functional_z_cluster]] |
| workloads | 70 | 44 | magenta | [[tests_functional_workloads]] |
| disaster_recovery | 43 | 36 | turquoise | [[tests_functional_disaster_recovery]] |
| monitoring | 42 | 20 | blue | [[tests_functional_monitoring]] |
| upgrade | 36 | 9 | purple | [[tests_functional_upgrade]] |
| ui | 31 | 13 | black | [[tests_functional_ui]] |
| storageclass | 29 | 23 | green | [[tests_functional_storageclass]] |
| pod_and_daemons | 20 | 9 | brown | [[tests_functional_pod_and_daemons]] |
| nfs_feature | 14 | 1 | brown | [[tests_functional_nfs_feature]] |
| encryption | 11 | 5 | green | [[tests_functional_encryption]] |
| odf_cli | 7 | 4 | brown | [[tests_functional_odf_cli]] |
| data_replication_separation | 4 | 2 | yellow | [[tests_functional_data_replication_separation]] |
| deployment | 4 | 3 | purple | [[tests_functional_deployment]] |
| external_mode | 1 | 1 | brown | [[tests_functional_external_mode]] |
| provider_mode | 1 | 1 | yellow | [[tests_functional_provider_mode]] |

## Cross-Functional Tests

| Area | Tests | Files | Squad | Link |
|------|-------|-------|-------|------|
| scale | 36 | 24 | orange | [[tests_cross_functional_scale]] |
| performance | 34 | 16 | grey | [[tests_cross_functional_performance]] |
| system_test | 23 | 14 | magenta | [[tests_cross_functional_system_test]] |
| krkn_chaos | 13 | 4 | green | [[tests_cross_functional_krkn_chaos]] |
| kcs | 8 | 7 | magenta | [[tests_cross_functional_kcs]] |
| longevity | 6 | 6 | magenta | [[tests_cross_functional_longevity]] |
| flowtest | 5 | 3 | magenta | [[tests_cross_functional_flowtest]] |
| resilience | 4 | 3 | green | [[tests_cross_functional_resilience]] |
| stress | 2 | 2 | magenta | [[tests_cross_functional_stress]] |

## Library Tests

| Area | Tests | Files | Link |
|------|-------|-------|------|
| Libtest | 102 | 37 | [[tests_libtest]] |

## Framework

| Module | Files | Lines | Link |
|--------|-------|-------|------|
| core | 8 | 1202 | [[framework-core]] |
| ocs | 67 | 48565 | [[framework-ocs]] |
| deployment | 37 | 23162 | [[framework-deployment]] |
| utility | 65 | 32935 | [[framework-utility]] |
| helpers | 28 | 21045 | [[framework-helpers]] |
