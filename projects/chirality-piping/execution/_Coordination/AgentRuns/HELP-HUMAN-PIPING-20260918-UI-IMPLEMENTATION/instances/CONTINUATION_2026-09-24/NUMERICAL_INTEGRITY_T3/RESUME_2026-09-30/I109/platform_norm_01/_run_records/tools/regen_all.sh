#!/bin/bash
# I109: the value entry's envelope (rendered as s11g's t13 renders it) for every committed request
# or model fixture under P/fixtures/product_preview and result_export's request fixtures, in both
# modes, from one scratch tree patched by regen_patch.py. Cargo through WT/tools/t3_cargo.sh.
# Usage: I109_WT=<WT> regen_all.sh <tree holding projects/chirality-piping> <out dir> <target dir>
set -u
T=${I109_WT:?set I109_WT to WT}; TREE=$1; OUT=$2; TGT=$3
P=$TREE/projects/chirality-piping; mkdir -p "$OUT"; : > "$OUT/runs.txt"
export TMPDIR=$T/scratch/i109_norm/tmp CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8
( cd "$P/core/product_physics" && "$T/tools/t3_cargo.sh" build --locked --offline --example i109_regen --target-dir "$TGT" ) > "$OUT/build.log" 2>&1 || { echo BUILD-FAIL; exit 1; }
BIN=$TGT/debug/examples/i109_regen
cd "$P" || exit 1
"$T/venv/bin/python" - > "$OUT/inputs.txt" <<'PY'
import glob, json
paths = sorted(glob.glob('fixtures/product_preview/**/*.json', recursive=True)) + sorted(glob.glob('core/reporting/result_export/tests/fixtures/*.request.json'))
for p in paths:
    try:
        d = json.load(open(p))
    except Exception:
        continue
    if isinstance(d, dict) and isinstance(d.get('model'), dict):
        print('request', p)
    elif isinstance(d, dict) and 'nodes' in d and 'pipe_segments' in d:
        print('model', p)
PY
while read -r kind path; do
  name=$(echo "$path" | tr '/' '_'); in=$path
  if [ "$kind" = model ]; then
    in=$OUT/wrapped_$name
    "$T/venv/bin/python" -c "import json,sys; print(json.dumps({'model': json.load(open(sys.argv[1])), 'materials': []}))" "$path" > "$in"
  fi
  for mode in sparse_interactive dense_scrutiny; do
    "$BIN" "$mode" "$in" > "$OUT/$name.$mode.json" 2> "$OUT/$name.$mode.err"; echo "$? $mode $path" >> "$OUT/runs.txt"
  done
done < "$OUT/inputs.txt"
echo REGEN-DONE
