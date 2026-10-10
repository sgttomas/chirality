"""Proposed dormant-record batch: dry-run by default; apply after scope review."""
from pathlib import Path
import argparse
import subprocess

BASELINE = '4510d8dc4265195a0cd99732870ba25ea9c2a047'
TAG = 'archive/pre-dormant-records-2026-10-09'
PREFIXES = (
    'projects/chirality-runtime/execution/_Coordination/SCA005_SCHEDULE_BASIS/',
    'projects/chirality-runtime/execution/_Estimates/SCA005_SUCCESSOR/',
    'projects/pec/execution/_Coordination/CLOSEOUT_POST_SCA005_2026-09-27/',
    'projects/pec/execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/',
    'projects/pec/execution/_Coordination/D-PEC-70_PEC_HOLD_RELEASE_2026-07-28/',
    'projects/pec/execution/_Coordination/D-PEC-71_OD8_RATIFICATION_2026-07-28/',
    'projects/pec/execution/_Coordination/D-PEC-72_P1_ENTRY_FOUNDATION_2026-08-01/',
    'projects/pec/execution/_Coordination/D-PEC-74_FIRST_P1_SOURCE_SLICE_2026-08-01/',
    'projects/pec/execution/_Coordination/D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/',
    'projects/pec/execution/_Coordination/D-PEC-77_DEL-01-05_ENFORCEMENT_2026-08-02/',
    'projects/pec/execution/_Coordination/D-PEC-78_OI-003_LOOP_REGISTRY_HOME_2026-08-02/',
    'projects/pec/execution/_Coordination/D1_PREMISE_AMEND_2026-09-27/',
    'projects/pec/execution/_Coordination/D83_D84_ACTIVATION_2026-09-07/',
    'projects/pec/execution/_Coordination/D83_D84_EXECUTION_2026-09-07/',
    'projects/pec/execution/_Coordination/D84_CHECKING_ROUTE_PREP_2026-09-07/',
    'projects/pec/execution/_Coordination/D84_L_REVERSAL_EXECUTION_2026-09-07/',
    'projects/pec/execution/_Coordination/D85_EXECUTION_2026-09-08/',
    'projects/pec/execution/_Coordination/D85_PRODUCTION_CLOSEOUT_2026-09-08/',
    'projects/pec/execution/_Coordination/DEL-01-06_RF002_REVISION_ACCEPTANCE_SESSION_PREP_2026-08-03/',
    'projects/pec/execution/_Coordination/FOLLOWON_D-PEC-66/',
    'projects/pec/execution/_Coordination/OD7-G3_APPLICATIONS/',
    'projects/pec/execution/_Coordination/P1_PRODUCTION_PREP_2026-09-07/',
    'projects/pec/execution/_Coordination/PEC_CURRENCY_D95_PREP_2026-09-25/',
    'projects/pec/execution/_Coordination/PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/',
    'projects/pec/execution/_Coordination/PEC_D1_PREMISE_PREP_2026-09-26/',
    'projects/pec/execution/_Coordination/PEC_FIRST_SOWS_D98_PREP_2026-09-26/',
    'projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/',
    'projects/pec/execution/_Coordination/PEC_REGISTRY_D96_PREP_2026-09-25/',
    'projects/pec/execution/_Coordination/PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/',
    'projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S1_PREP_2026-09-26/',
    'projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S4_PREP_2026-09-26/',
    'projects/pec/execution/_Coordination/PEC_SOW_REBUILD_S2_PREP_2026-09-26/',
    'projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/',
    'projects/pec/execution/_Coordination/PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/',
    'projects/pec/execution/_Coordination/PROJECT_SETUP_REFERENCE_PARITY_2026-07-28/',
    'projects/pec/execution/_Coordination/PROJECT_SETUP_SCA004_METADATA_ALIGNMENT_2026-08-03/',
    'projects/pec/execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/',
    'projects/pec/execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_PREP_2026-09-25/',
    'projects/pec/execution/_Coordination/REMAINING_RETIREMENT_D-PEC-99_2026-09-26/',
    'projects/pec/execution/_Coordination/REPAIR_D-PEC-65/',
    'projects/pec/execution/_Coordination/REV16_CURRENCY_SETUP_D101_2026-09-26/',
    'projects/pec/execution/_Coordination/RV1_ACCEPTANCE_RECORD_2026-09-27/',
    'projects/pec/execution/_Coordination/RV1_D1_REVIEW_2026-09-27/',
    'projects/pec/execution/_Coordination/SCA-005_PREP_2026-09-23/',
    'projects/pec/execution/_Coordination/SEED_D-PEC-62/',
    'projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27/',
    'projects/pec/execution/_Coordination/SOW_CURRENCY_S4_2026-09-26/',
    'projects/pec/execution/_Coordination/SOW_INIT_D98_2026-09-26/',
    'projects/pec/execution/_Coordination/SOW_INIT_K2_2026-09-26/',
    'projects/pec/execution/_Coordination/SOW_REBUILD_S2_2026-09-26/',
    'projects/pec/execution/_Coordination/TASK_MANAGEMENT_DPEC_REQUESTS_2026-08-02/',
    'projects/pec/execution/_Coordination/TM-PEC-013_CURRENCY_REPAIR_2026-08-09/',
    'projects/pec/execution/_Coordination/TM-PEC-014_SPEC_CURRENCY_2026-08-09/',
    'projects/pec/execution/_Coordination/TM-PEC-023_SCOPE_CHANGE_MAPPING_SESSION_PREP_2026-08-03/',
    'projects/pec/execution/_Coordination/WAVE_D-PEC-63/',
    'projects/pec/execution/_Coordination/WORKING_ITEMS_SCA004_CURRENCY_SWEEP_2026-08-03/',
    'projects/pec/execution/_Coordination/WorkGraphs/',
    'projects/pec/execution/_Coordination/X1_FIXTURES_2026-09-27/',
)

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--apply', action='store_true')
parser.add_argument('--list', action='store_true')
args = parser.parse_args()
paths = subprocess.check_output(['git', 'ls-files', '-z']).decode().split('\0')
selected = [p for p in paths if p.startswith(PREFIXES)]
print(f'{len(selected)} tracked historical files selected')
if args.list:
    print('\n'.join(selected))
if args.apply:
    actual = subprocess.check_output(['git', 'rev-parse', TAG+'^{commit}'], text=True).strip()
    if actual != BASELINE:
        raise SystemExit('Recovery tag mismatch')
    changed = set(subprocess.check_output(['git', 'diff', '--name-only', BASELINE], text=True).splitlines())
    if set(selected) & changed:
        raise SystemExit('Candidate changed since recovery baseline; review before deletion')
    for path in selected:
        Path(path).unlink()
