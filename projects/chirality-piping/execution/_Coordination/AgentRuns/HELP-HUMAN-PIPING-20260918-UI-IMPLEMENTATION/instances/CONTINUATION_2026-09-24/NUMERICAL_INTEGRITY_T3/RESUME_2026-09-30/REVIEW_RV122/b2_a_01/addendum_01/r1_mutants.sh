#!/bin/bash
# RV122 addendum 01: each repair mutant on a cp -R copy of the repair head (fresh mtimes), fresh target.
set -u
WT=WT; S=$WT/scratch/rv122_rvq2; PY=$WT/venv/bin/python
A=$S/arch_r1mut/projects/chirality-piping; SRC=$S/arch_r1/projects/chirality-piping/core/product_physics/src
O=$S/runs/r1_mutants; mkdir -p "$O"
export TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4
unset RUSTFLAGS CARGO_ENCODED_RUSTFLAGS
cd "$A" || exit 9
for id in "$@"; do
  $PY -I - "$S/scripts/r1_mutants_def.py" "$SRC" "$A/core/product_physics/src" "$id" <<'PYX' > "$O/$id.check" || { echo "$id APPLY_FAILED" >> "$O/meta.txt"; continue; }
import sys, pathlib, importlib.util, shutil
spec = importlib.util.spec_from_file_location("d", sys.argv[1]); d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
src, dst, mid = pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4]
for f in ("lib.rs", "retained_memory.rs"): shutil.copyfile(src / f, dst / f)
for (i, f, check, old, new) in d.M:
    if i == mid:
        t = (src / f).read_text(); n = t.count(old)
        if n != 1: raise SystemExit(f"{i}: {n} occurrences")
        (dst / f).write_text(t.replace(old, new)); print(i, f, check); break
else: raise SystemExit("unknown")
PYX
  $WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast --manifest-path core/product_physics/Cargo.toml \
    --target-dir "$WT/targets/rv122-r1mut-pp" --lib > "$O/$id.log" 2>&1
  echo "$id rc=$? $(date -u +%FT%TZ)" >> "$O/meta.txt"
done
cp "$SRC/lib.rs" "$SRC/retained_memory.rs" "$A/core/product_physics/src/"
