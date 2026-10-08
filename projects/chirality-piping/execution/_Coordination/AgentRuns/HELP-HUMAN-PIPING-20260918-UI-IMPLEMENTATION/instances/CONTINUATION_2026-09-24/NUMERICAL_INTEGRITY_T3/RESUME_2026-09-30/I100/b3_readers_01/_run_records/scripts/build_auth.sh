#!/bin/bash
# I100 B3: build the three CLI authorities from the base archive (e67c364680) into fresh targets, one cargo job at a time.
source WT/scratch/i100_b3r/tools/env.sh
$S/tools/job.sh cargo auth_cj $BASE/core/serialization/canonical_json $TG/checked-json build --locked --offline --release --features checked-cli --bin openpipestress_jcs_ijson --bin openpipestress_jcs_binary64; echo "cj rc=$?"
$S/tools/job.sh cargo auth_units $BASE/core/units $TG/units-authority build --locked --offline --release --features cli --bin openpipestress_units; echo "units rc=$?"
ls -la $OPENPIPESTRESS_CHECKED_JSON_BIN $OPENPIPESTRESS_BINARY64_JSON_BIN $OPENPIPESTRESS_UNITS_BIN
