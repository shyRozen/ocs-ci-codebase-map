---
version: 4.15
total_markers: 74
marks_py_count: 86
squad_marks: 12
---

# Pytest Markers (release-4.15)

Markers are registered in two places:

1. **`pytest.ini`** -- the `markers =` list. Required for `--strict-markers` to accept the marker at collection time.
2. **`ocs_ci/framework/pytest_customization/marks.py`** -- Python variables (e.g. `tier1 = pytest.mark.tier1(value=1)`) that tests import and use as decorators.

To add a new marker, register it in **both** files.

## How to add a z-stream marker

The z-stream pipeline adds a temporary marker for test selection:

1. Append to `pytest.ini` markers list: `zstream_4_16_13: z-stream 4.16.13 test enablement`
2. Add `@pytest.mark.zstream_4_16_13` to each selected test file
3. Run with `pytest -m zstream_4_16_13`

No `marks.py` entry needed -- z-stream markers are used directly as `@pytest.mark.name`, not imported as Python variables.

## Squad Marks

| Marker | Usage |
|--------|-------|
| `@aqua_squad` | `from ocs_ci.framework.pytest_customization.marks import aqua_squad` |
| `@black_squad` | `from ocs_ci.framework.pytest_customization.marks import black_squad` |
| `@blue_squad` | `from ocs_ci.framework.pytest_customization.marks import blue_squad` |
| `@brown_squad` | `from ocs_ci.framework.pytest_customization.marks import brown_squad` |
| `@green_squad` | `from ocs_ci.framework.pytest_customization.marks import green_squad` |
| `@grey_squad` | `from ocs_ci.framework.pytest_customization.marks import grey_squad` |
| `@magenta_squad` | `from ocs_ci.framework.pytest_customization.marks import magenta_squad` |
| `@orange_squad` | `from ocs_ci.framework.pytest_customization.marks import orange_squad` |
| `@purple_squad` | `from ocs_ci.framework.pytest_customization.marks import purple_squad` |
| `@red_squad` | `from ocs_ci.framework.pytest_customization.marks import red_squad` |
| `@turquoise_squad` | `from ocs_ci.framework.pytest_customization.marks import turquoise_squad` |
| `@yellow_squad` | `from ocs_ci.framework.pytest_customization.marks import yellow_squad` |

## Tier Marks

`@tier1`, `@tier2`, `@tier3`, `@tier4`, `@tier4a`, `@tier4b`, `@tier4c`, `@tier_after_upgrade`

## Component & Category Marks

`@acceptance`, `@acm_import`, `@aws_based_platform_required`, `@aws_platform_required`, `@azure_platform_required`, `@bugzilla`, `@cloud_platform_required`, `@csi`, `@deployment`, `@e2e`, `@ecosystem`, `@external_mode_required`, `@filter_insecure_request_warning`, `@fips_required`, `@flowtests`, `@gather_metrics_on_fail`, `@gcp_platform_required`, `@google_api_required`, `@hci_client_required`, `@hci_provider_and_client_required`, `@hci_provider_required`, `@ibmcloud_platform_required`, `@ignore_leftover_label`, `@ignore_leftovers`, `@ignore_owner`, `@ipi_deployment_required`, `@jira`, `@kms_config_required`, `@libtest`, `@manage`, `@managed_service_required`, `@mcg`, `@metrics_for_external_mode_required`, `@monitoring`, `@ms_consumer_required`, `@ms_provider_and_consumer_required`, `@ms_provider_required`, `@ocp`, `@ocp_upgrade`, `@ocs_upgrade`, `@on_prem_platform_required`, `@pc_or_ms_consumer_required`, `@pc_or_ms_provider_required`, `@performance`, `@performance_a`, `@performance_b`, `@performance_c`, `@performance_extended`, `@polarion_id`, `@provider_client_ms_platform_required`, `@provider_client_platform_required`, `@rdr_ui_failover_config_required`, `@rdr_ui_relocate_config_required`, `@rgw`, `@rh_internal_lab_required`, `@rhv_platform_required`, `@rook`, `@run_this`, `@runs_on_provider`, `@scale`, `@scale_changed_layout`, `@scale_long_run`, `@system_test`, `@ui`, `@vsphere_platform_required`, `@workloads`

## All Registered Markers (pytest.ini)

| Marker | Description |
|--------|-------------|
| `run_this` | testing marker for run this test, useful for development |
| `acceptance` | marker for acceptance tests |
| `tier0` | marker for tier0 tests |
| `tier1` | marker for tier1 tests |
| `tier2` | marker for tier2 tests |
| `tier3` | marker for tier3 tests |
| `tier4` | marker for tier4 tests |
| `tier4a` | marker for tier4 tests suite a |
| `tier4b` | marker for tier4 tests suite b |
| `tier4c` | marker for tier4 tests suite c |
| `tier_after_upgrade` | marker for test which will be executed after upgrade |
| `manage` | manage team marker |
| `ecosystem` | ecosystem team marker |
| `e2e` | e2e team marker |
| `ocp` | ocp related tests |
| `rook` | rook related tests |
| `ui` | UI related tests |
| `csi` | CSI related tests |
| `monitoring` | monitoring related tests |
| `workloads` | workloads related tests |
| `flowtests` | flowbased related tests |
| `system_test` | Tests related to system level scenarios where the test scenarios exercise multiple features together |
| `performance` | performance related tests |
| `performance_a` | performance related tests - first group |
| `performance_b` | performance related tests - second group |
| `performance_c` | performance related tests - third group |
| `performance_extended` | non regression performance tests |
| `scale` | scale related tests |
| `scale_long_run` | scale tests which has execution time in days |
| `scale_changed_layout` | scale capacity/node tests without teardown |
| `deployment` | deployment related tests |
| `acm_import` | acm_import related tests |
| `ocs_upgrade` | marker for OCS upgrade test |
| `pre_ocs_upgrade` | marker for pre OCS upgrade tests |
| `post_ocs_upgrade` | marker for post OCS upgrade tests |
| `ocp_upgrade` | marker for OCP upgrade test |
| `pre_ocp_upgrade` | marker for pre OCP upgrade tests |
| `post_ocp_upgrade` | marker for post OCP upgrade tests |
| `pre_upgrade` | upgrade related tests triggered before upgrade |
| `post_upgrade` | upgrade related tests triggered after upgrade |
| `post_deployment` | tests executed right after deployment |
| `polarion_id` | ID of test case used for reporting to Polarion |
| `libtest` | marker for library tests which requires a running cluster |
| `gather_metrics_on_fail` | collect metrics specified in parameter when error |
| `first` | for tests to be executed with priority, from pytest-ordering plugin |
| `skipif_ocs_version` | to skip tests based on ocs version applicable |
| `skipif_upgraded_from` | to skip tests if OCS cluster is upgraded from a particular version |
| `skipif_no_kms` | to skip tests if OCS cluster has not configured KMS integration |
| `last` | for tests to be executed with priority, from pytest-ordering plugin. test case executes at last |
| `second_to_last` | for tests to be executed with priority, from pytest-ordering plugin. test case executes at second to last |
| `post_ocp_upgrade` | marker for post ocp upgrade tests |
| `aqua_squad` | marker for aqua squad |
| `brown_squad` | marker for brown squad |
| `green_squad` | marker for green squad |
| `blue_squad` | marker for blue squad |
| `red_squad` | marker for red squad |
| `purple_squad` | marker for purple squad |
| `magenta_squad` | marker for magenta squad |
| `grey_squad` | marker for grey squad |
| `orange_squad` | marker for orange squad |
| `black_squad` | marker for black squad |
| `yellow_squad` | marker for yellow squad |
| `turquoise_squad` | marker for turquoise squad |
| `ignore_owner` | marker to ignore test during squad decorator check in pytest collection |
| `mcg` | marker for MCG related tests |
| `rgw` | marker for RGW related tests |
| `skipif_ocp_version` | marker we use for skipping tests on particular OCP version |
| `skipif_ui_not_support` | skip test if it's not supported for UI testing |
| `skipif_lvm_not_installed` | skip test if the lvm is not installed |
| `runs_on_provider` | skip test |
| `ignore_leftovers` | marker for the ignoring leftovers for specific test |
| `ignore_leftover_label` | marker for ignoring lefotover of resources having specific label |
| `ignore_resource_not_found_error_label` | ignore resource_not_found error such as when deleting a resource that was already deleted |
| `stretchcluster_required` | maker to select stretch ceph cluster related tests |

## Related
- [[framework-core]]
