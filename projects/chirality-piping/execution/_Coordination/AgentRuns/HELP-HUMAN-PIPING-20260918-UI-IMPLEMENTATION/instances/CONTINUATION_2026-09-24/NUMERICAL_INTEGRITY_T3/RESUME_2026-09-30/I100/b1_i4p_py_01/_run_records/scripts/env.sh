WT=WT
S=$WT/scratch/i100_b1_i4p_py
VENV=$WT/venv
TG=$WT/targets/i100-b1-i4p-py
export OPENPIPESTRESS_CHECKED_JSON_BIN=$TG/checked-json/release/openpipestress_jcs_ijson
export OPENPIPESTRESS_BINARY64_JSON_BIN=$TG/checked-json/release/openpipestress_jcs_binary64
export OPENPIPESTRESS_UNITS_BIN=$TG/units-authority/release/openpipestress_units
export PYTHONDONTWRITEBYTECODE=1
