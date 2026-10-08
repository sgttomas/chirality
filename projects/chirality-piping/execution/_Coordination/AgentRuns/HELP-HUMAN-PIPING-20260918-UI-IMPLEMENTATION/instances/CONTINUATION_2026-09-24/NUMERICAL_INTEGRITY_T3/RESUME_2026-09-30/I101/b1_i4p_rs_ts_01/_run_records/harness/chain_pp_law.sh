#!/bin/bash
# I101: PP's two source-text guards that read RE (retained_memory's law tests on the reviewed inputs and the reader
# layouts), against RS at b1-r's head (copy rss), as one cargo job. No solve: the two tests read sources and statics.
WT=WT
S=$WT/scratch/i101_b1_i4p_rs_ts
J=$S/harness/job.sh
P=$S/copies/rss/projects/chirality-piping
RUST_TEST_THREADS=2 $J cargo head_pp_law "$P/core/product_physics" "$WT/targets/i101-b1-i4p-rs-ts/head-pp" \
  test --locked --offline --lib -- --exact \
  retained_memory::law_tests::reviewed_inputs_bind_the_lock_and_the_reader_statics \
  retained_memory::law_tests::bindings_need_witnesses_inputs_and_reader_layouts
echo "pp law rc=$?"
