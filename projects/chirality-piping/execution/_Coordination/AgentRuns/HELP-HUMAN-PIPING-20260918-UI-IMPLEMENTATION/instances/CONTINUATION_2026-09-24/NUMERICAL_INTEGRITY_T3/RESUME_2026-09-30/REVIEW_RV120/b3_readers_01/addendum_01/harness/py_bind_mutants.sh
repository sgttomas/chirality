#!/bin/bash
# RV120 B3 repair 01: I100's PY note, checked on my forgeries with my own spellings of its R2-R5 (PY head 6d3d4cdca6,
# copy py2m): R2 drops step 4's E bits in both material-basis loops; R3 the G-hat bits; R4 = R2 plus the attempts loop's
# old-E binding; R5 = R3 plus the old-G binding. Raw PY readings of the four forgeries per mutant.
WT=WT
S=$WT/scratch/rv120_rvr
B3=$S/b3
export RV120_LOGDIR=$B3/logs
J=$S/tools/rv120_job.sh
B=$WT/targets/rv120b3-pybins/release
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1"
P=$WT/rv120b3/py2m/projects/chirality-piping; F=$P/core/analysis_runs/retained_precision.py
rm -rf $WT/rv120b3/py2m; mkdir -p $WT/rv120b3/py2m; cp -R $WT/rv120b3/py2/projects $WT/rv120b3/py2m/
cp $F $B3/tmp/rp_orig.py
for m in R2 R3 R4 R5; do
  cp $B3/tmp/rp_orig.py $F
  python3 - "$F" "$m" <<'PY'
import sys
p, m = sys.argv[1:3]; s = open(p).read()
both = '[m["elastic_modulus"],m["shear_modulus"]] == [bits(v) for v in pair]'
old = 'old[:2] == [bits(v) for v in pair]'
assert s.count(both) == 2 and s.count(old) == 1
s = s.replace(both, 'm["shear_modulus"] == bits(pair[1])' if m in ("R2", "R4") else 'm["elastic_modulus"] == bits(pair[0])')
if m == "R4": s = s.replace(old, 'old[1] == bits(pair[1])')
if m == "R5": s = s.replace(old, 'old[0] == bits(pair[0])')
open(p, "w").write(s); print(m, "applied")
PY
  $J slot py2m_$m $P /usr/bin/env $ENV $WT/venv/bin/python $S/tools/b3/rv120_b3_py_raw.py $P $B3/inputs/forge_eg.jsonl $B3/probes/r1forge_py_$m.jsonl; echo "py2m_$m rc=$?"
done
cp $B3/tmp/rp_orig.py $F; cmp $F $WT/rv120b3/py2/projects/chirality-piping/core/analysis_runs/retained_precision.py && echo reverted
