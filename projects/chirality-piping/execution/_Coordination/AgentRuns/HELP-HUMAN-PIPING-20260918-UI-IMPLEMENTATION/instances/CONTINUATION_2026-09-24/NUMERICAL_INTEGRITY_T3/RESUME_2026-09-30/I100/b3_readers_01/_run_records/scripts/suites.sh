#!/bin/bash
# I100 B3: I83's Python set plus the physics-source contract (S-C) and, with EXTRA, added files (I69's set plus the retained files; the 27 files I91 ran), on one P tree, as one T3 slot
# job, with I100's own builds of the CLI authorities. Usage: suites.sh <label> <P root>
set -u
source WT/scratch/i100_b3r/tools/env.sh
LABEL=$1; PROOT=$2; O=$S/suites/$LABEL; mkdir -p $O
SWEEP="tests/test_adapter_framework_contract.py tests/test_analysis_run_schema.py tests/test_analysis_run_records.py tests/test_analysis_status_schema.py tests/test_analysis_run_compatibility.py tests/test_comparison_contracts.py tests/test_handoff_package_schema.py tests/test_handoff_export_workflow.py tests/test_load_reference_headless_artifacts.py tests/test_invented_example_models.py tests/test_load_reference_schema.py tests/test_load_reference_source_schema.py tests/test_persistence_schema.py tests/test_physics_consumer_contract.py tests/test_preview_physics_consumer_contract.py tests/test_precision_consumer_contract.py tests/test_project_persistence_service.py tests/test_result_export_v0_2.py tests/test_stress_neutral_physics_source.py tests/test_results_schema.py tests/test_source_block_schema_contract.py tests/test_stress_neutral_precision.py tests/test_stress_neutral_export_package.py tests/test_retained_precision_contract.py tests/test_retained_precision_schema.py tests/test_retained_precision_carriers.py tests/test_results_dispatcher_v0_3.py tests/test_physics_source_contract.py${EXTRA:+ $EXTRA}"
$S/tools/job.sh slot suites_$LABEL $PROOT /bin/bash -c "$VENV/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/suites_$LABEL/basetemp -q -rs -rf -v --junitxml=$O/py.xml $SWEEP > $O/py.log 2>&1"
echo "suites $LABEL rc=$?"
