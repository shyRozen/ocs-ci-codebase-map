# OCS-CI Codebase Map

> Auto-generated map of the ocs-ci test framework.
> Source: `~/codcod/new-ocs-ci/ocs-ci/`

---

## Quick Stats

| Metric | Value |
|--------|-------|
| Total test files | 485 |
| Total test functions | 913 |
| Framework modules | 215+ |
| Framework LOC | ~215,000 |
| Squads | 12 |
| Tiers | 4 (tier1–tier4) |
| Deployment platforms | 10+ |

---

## Squads

| Squad | Primary Areas | Test Count |
|-------|--------------|------------|
| [[green_squad]] | PV, StorageClass, Encryption, Krkn Chaos | ~130 |
| [[red_squad]] | MCG, RGW, Object Storage | ~100 |
| [[brown_squad]] | Z-Cluster, NFS, Upgrade, ODF-CLI, Pods | ~100 |
| [[blue_squad]] | Monitoring, Prometheus, Alerts | ~53 |
| [[magenta_squad]] | Workloads, System Test, Longevity, KCS, Stress | ~50 |
| [[turquoise_squad]] | Disaster Recovery (Metro/Regional DR) | ~37 |
| [[orange_squad]] | Scale | ~33 |
| [[black_squad]] | UI (Functional + Cross-Functional) | ~25 |
| [[purple_squad]] | Deployment, Upgrade, Libtest | ~17 |
| [[yellow_squad]] | Provider Mode, Data Replication, Managed Service | ~12 |
| [[grey_squad]] | Performance | ~15 |
| [[aqua_squad]] | LVMO | ~9 |

---

## Test Areas

### Functional Tests
| Area | Tests | Files | Squad | Link |
|------|-------|-------|-------|------|
| PV | 113 | 84 | green | [[tests_functional_pv]] |
| Object/MCG | 228 | 76 | red | [[tests_functional_object_mcg]] |
| Z-Cluster | 115 | 62 | brown | [[tests_functional_z_cluster]] |
| Monitoring | 44 | 26 | blue | [[tests_functional_monitoring]] |
| Upgrade | 39 | 10 | mixed | [[tests_functional_upgrade]] |
| StorageClass | 29 | 23 | green | [[tests_functional_storageclass]] |
| UI | 28 | 10 | black | [[tests_functional_ui]] |
| Workloads | 71 | 47 | magenta | [[tests_functional_workloads]] |
| Disaster Recovery | 45 | 39 | turquoise | [[tests_functional_disaster_recovery]] |
| Pod & Daemons | 20 | 9 | brown | [[tests_functional_pod_and_daemons]] |
| Object/RGW | 16 | 12 | red | [[tests_functional_object_rgw]] |
| NFS | 14 | 1 | brown | [[tests_functional_nfs_feature]] |
| Encryption | 11 | 5 | green | [[tests_functional_encryption]] |
| ODF-CLI | 7 | 4 | brown | [[tests_functional_odf_cli]] |
| Deployment | 4 | 3 | purple | [[tests_functional_deployment]] |
| Data Replication | 4 | 2 | yellow | [[tests_functional_data_replication_separation]] |
| External Mode | 1 | 1 | brown | [[tests_functional_external_mode]] |
| Provider Mode | 1 | 1 | yellow | [[tests_functional_provider_mode]] |

### Cross-Functional Tests
| Area | Tests | Files | Squad | Link |
|------|-------|-------|-------|------|
| Scale | 36 | 28 | orange | [[tests_cross_functional_scale]] |
| Performance | 34 | 16 | grey | [[tests_cross_functional_performance]] |
| Krkn Chaos | 24 | 6 | green | [[tests_cross_functional_krkn_chaos]] |
| System Test | 23 | 14 | magenta | [[tests_cross_functional_system_test]] |
| UI | 11 | 5 | black | [[tests_cross_functional_ui]] |
| KCS | 8 | 8 | magenta | [[tests_cross_functional_kcs]] |
| Longevity | 6 | 6 | magenta | [[tests_cross_functional_longevity]] |
| Resilience | 5 | 4 | green | [[tests_cross_functional_resilience]] |
| Stress | 5 | 5 | magenta | [[tests_cross_functional_stress]] |
| FlowTest | 5 | 3 | magenta | [[tests_cross_functional_flowtest]] |

### Library Tests
| Area | Tests | Files | Link |
|------|-------|-------|------|
| Libtest | 111 | 41 | [[tests_libtest]] |

---

## Framework

| Module | Purpose | Link |
|--------|---------|------|
| ocs_ci/framework/ | Pytest plugins, config, entry points | [[framework-core]] |
| ocs_ci/ocs/ | OCS/Ceph resource management | [[framework-ocs]] |
| ocs_ci/deployment/ | Platform deployment logic | [[framework-deployment]] |
| ocs_ci/utility/ | Utilities, cloud providers, versioning | [[framework-utility]] |
| ocs_ci/helpers/ | Test helper functions | [[framework-helpers]] |
| ocs_ci/ocs/constants.py | Master constants, squad mapping | [[framework-constants]] |

---

## Related
- [[ODF-ZStream-Multi-Agent-Plan-v2]] — Multi-agent pipeline plan
- [[ODF-ZStream-Jenkins-Reference]] — Jenkins integration
