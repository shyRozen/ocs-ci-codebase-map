# OCS-CI Codebase Map (release-4.21)

> Auto-generated map for ODF 4.21.

---

## Quick Stats

| Metric | Value |
|--------|-------|
| Test files | 528 |
| Test functions | 1049 |
| Squads | 11 |
| Test areas | 28 |

---

## Squads

| Squad | Tests |
|-------|-------|
| [[red_squad]] | 230 |
| [[green_squad]] | 175 |
| [[brown_squad]] | 157 |
| [[magenta_squad]] | 101 |
| [[black_squad]] | 45 |
| [[turquoise_squad]] | 44 |
| [[blue_squad]] | 44 |
| [[orange_squad]] | 43 |
| [[purple_squad]] | 43 |
| [[grey_squad]] | 33 |
| [[yellow_squad]] | 28 |

## Functional Tests

| Area | Tests | Files | Squad | Link |
|------|-------|-------|-------|------|
| object | 242 | 85 | red | [[tests_functional_object]] |
| z_cluster | 115 | 60 | brown | [[tests_functional_z_cluster]] |
| pv | 113 | 82 | green | [[tests_functional_pv]] |
| workloads | 71 | 45 | magenta | [[tests_functional_workloads]] |
| disaster_recovery | 45 | 38 | turquoise | [[tests_functional_disaster_recovery]] |
| monitoring | 44 | 22 | blue | [[tests_functional_monitoring]] |
| upgrade | 39 | 10 | brown | [[tests_functional_upgrade]] |
| ui | 38 | 15 | black | [[tests_functional_ui]] |
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
| krkn_chaos | 19 | 5 | green | [[tests_cross_functional_krkn_chaos]] |
| kcs | 8 | 7 | magenta | [[tests_cross_functional_kcs]] |
| longevity | 6 | 6 | magenta | [[tests_cross_functional_longevity]] |
| flowtest | 5 | 3 | magenta | [[tests_cross_functional_flowtest]] |
| resilience | 4 | 3 | green | [[tests_cross_functional_resilience]] |
| stress | 4 | 4 | magenta | [[tests_cross_functional_stress]] |

## Library Tests

| Area | Tests | Files | Link |
|------|-------|-------|------|
| Libtest | 110 | 39 | [[tests_libtest]] |

## Framework

| Module | Files | Lines | Link |
|--------|-------|-------|------|
| core | 8 | 1238 | [[framework-core]] |
| ocs | 68 | 49908 | [[framework-ocs]] |
| deployment | 37 | 29345 | [[framework-deployment]] |
| utility | 66 | 35710 | [[framework-utility]] |
| helpers | 29 | 23185 | [[framework-helpers]] |
