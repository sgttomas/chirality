#!/bin/bash
# I100: the three CLI authorities (checked JSON, binary64 JSON, units) for pytest and the harness, built from WT/b1-p
# (these crates are not changed by this round) into I100's own target, one cargo job at a time through the T3 wrapper.
set -u
WT=WT
S=$WT/scratch/i100_b1_i4p_py
P=$WT/b1-p/projects/chirality-piping
TG=$WT/targets/i100-b1-i4p-py
J=$S/tools/job.sh
$J cargo build_checked_json $P/core/serialization/canonical_json $TG/checked-json build --locked --offline --release --features checked-cli --bin openpipestress_jcs_ijson; echo "checked-json rc=$?"
$J cargo build_binary64_json $P/core/serialization/canonical_json $TG/checked-json build --locked --offline --release --features checked-cli --bin openpipestress_jcs_binary64; echo "binary64-json rc=$?"
$J cargo build_units $P/core/units $TG/units-authority build --locked --offline --release --features cli --bin openpipestress_units; echo "units rc=$?"
echo done
