#!/bin/bash
# RV113: two extra metadata probes (a measure and a gate with an extra member) on RS's control and N64/N65, after the TS chain.
WT=WT
S=$WT/scratch/rv113_rvr_01/rsr2
D=$WT/targets/rv113-rs2mut/debug/deps; B=$D/$(ls $D | grep -E '^rv113_census-[0-9a-f]+$' | head -1)
RE=$WT/rv113/rs2-mut/projects/chirality-piping/core/reporting/result_export
cd $RE || exit 90
for id in NONE N64 N65; do
  mut=$([ "$id" = NONE ] || echo "$id")
  "$WT/tools/t3_slot.sh" /usr/bin/env RV113_MUT="$mut" TMPDIR="$S/tmp/mut_$id" RV113_PROBES="$S/probes/probes_r2x.json" RV113_PROBES_OUT="$S/mutants/runs/$id/probes_r2x.jsonl" RUST_TEST_THREADS=2 "$B" rv113_probes --exact > "$S/mutants/runs/$id/harness_r2x.log" 2>&1
  echo "$id rc=$?"
done
echo extra-done
