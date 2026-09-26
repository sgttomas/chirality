#!/bin/bash
# usage: post_checks.sh <repo root>
# D-PEC-96 finite verification rows that need no Git: selection, mutation
# evidence, byte identity, basis citations, non-ASCII scan and the
# vocabulary scan. Read-only against the product tree; outputs go to checks/.
set -u
R=$1
RR="$R/projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2"
C="$RR/checks"
export PYTHONDONTWRITEBYTECODE=1
PY=/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
echo "# phase post-extra; PY=$PY ($($PY --version 2>&1)); PYTHONDONTWRITEBYTECODE=1; $(date)" >> "$C/COMMANDS.txt"
log(){ printf '%s\tcwd=%s\t%s\t> checks/%s\n' "$1" "$2" "$3" "$4" >> "$C/COMMANDS.txt"; echo "$1 $4"; }
PATHS="v2/config/loops.json v2/config/loops.schema.json v2/src/pec_v2/core/ports/loop_registry.py v2/src/pec_v2/core/ports/__init__.py v2/src/pec_v2/core/__init__.py v2/src/pec_v2/adapters/config/loop_registry.py v2/tests/config/test_json_loop_registry.py v2/tests/config/test_loop_registry_contract.py v2/tests/config/fixtures/duplicate_loop_id.json v2/tests/config/fixtures/missing_loop_id.json v2/tests/config/fixtures/schema_version_1.json"

# Selection (paths are project-relative: the profile's path rules are
# relative to projects/pec; corrected after the first run, see COMMANDS.txt)
(cd "$R" && "$PY" tools/software_workflow/select_affected_checks.py projects/pec/software-workflow.json $PATHS > "$C/selection.out" 2>&1); log $? . "python3 tools/software_workflow/select_affected_checks.py projects/pec/software-workflow.json <the 11 paths, project-relative>" selection.out

# Mutation evidence (run-root copy of the bound runner)
(cd "$R" && "$PY" "$RR/mutate_d96.py" projects/pec > "$C/mutate_d96.out" 2>&1); log $? . "python3 <run root>/mutate_d96.py projects/pec" mutate_d96.out

# Byte identity against the grant table (proposal postimage column)
cat > "$C/grant_postimages.txt" <<'EOT'
fd342b4f29edf3bece24a8d785b4a03d1a60158e62227753e4e1fa03529f53d7  v2/config/loops.json
104ed64820b7a1fa6f24249cb6817653b8a624f43c52ea181ae4fd5d510cb143  v2/config/loops.schema.json
a509bfb74920172a86ac21aff6a67245cd3248c5d73ef4e7427966069099c8a9  v2/src/pec_v2/core/ports/loop_registry.py
e44bf7f00c8ef2cfa5f8006ef2834feb020063df63a3b4b8d8cbd8f359174ff7  v2/src/pec_v2/core/ports/__init__.py
0e699a54d6bc202ff7a90c25fdb355da5ed2db185709c3a399870c1b0309c42d  v2/src/pec_v2/core/__init__.py
620a173d19d881ef396ebb339e4097f5ee4e3a0b6ada231718ca700926832f07  v2/src/pec_v2/adapters/config/loop_registry.py
8b45495fdc78eb77c12a4ebefdb064d34d40d5602fde573be4b4e817ddbe0c9b  v2/tests/config/test_json_loop_registry.py
b05ed8719c59258998b1c483456b66bd8d4a4d3bc4f68cdd6fb5c02541db7106  v2/tests/config/test_loop_registry_contract.py
6875f50023f1ad34a45c1af4b0a65316260c45aa05562ce45bb2d9bd8fd13c7e  v2/tests/config/fixtures/duplicate_loop_id.json
f4255b2483a014b542fb7f25c4314ff75dabb5cebbcfe751a2ad3df425f29598  v2/tests/config/fixtures/missing_loop_id.json
4ce07ad061abd222acabb2afe0f619fdc840b4cc11d31e49f1dff8fcc299d32e  v2/tests/config/fixtures/schema_version_1.json
EOT
(cd "$R/projects/pec" && shasum -a 256 -c "$C/grant_postimages.txt" > "$C/byte_identity.out" 2>&1
 echo "--- prep postimages/optionA_v2 comparison" >> "$C/byte_identity.out"
 for p in $PATHS; do q=${p#v2/}; if cmp -s "$p" "execution/_Coordination/PEC_REGISTRY_D96_PREP_2026-09-25/postimages/optionA_v2/$q"; then echo "IDENTICAL $p" ; else echo "DIFFERS $p"; fi; done >> "$C/byte_identity.out"
 echo "--- path-list sha256 (11 paths sorted, newline-terminated; expected b5db12e59bec0188b1798e8ccf7a3c09300c44e5dbcdf31c16a64aff5e84c73c)" >> "$C/byte_identity.out"
 printf '%s\n' $PATHS | LC_ALL=C sort | shasum -a 256 >> "$C/byte_identity.out"
 echo "--- must-remain" >> "$C/byte_identity.out"
 shasum -a 256 v2/tests/config/fixtures/malformed.json v2/src/pec_v2/adapters/config/__init__.py v2/src/pec_v2/adapters/__init__.py v2/src/pec_v2/__init__.py software-workflow.json v2/config/service_core_posture.json >> "$C/byte_identity.out")
log $? projects/pec "shasum -a 256 -c grant_postimages.txt; cmp against prep postimages; path-list hash; must-remain hashes" byte_identity.out

# Basis citations
(cd "$R" && "$PY" - > "$C/basis_citations.out" 2>&1 <<'EOT'
import json, os
d = json.load(open("projects/pec/v2/config/loops.json"))
bad = 0
for row in d["loops"]:
    for p in [row["loop_init_path"]] + [e["basis"] for e in row["feed_profiles"]]:
        ok = os.path.isfile(p)
        bad += not ok
        print(("PRESENT" if ok else "MISSING"), p)
print("schema_version", d["schema_version"], "rows", len(d["loops"]))
for e in d["loops"][0]["feed_profiles"]:
    print("ROW", e["profile"], "v%d" % e["version"], e["state"], e["basis"])
raise SystemExit(1 if bad else 0)
EOT
); log $? . "test -f on each basis and loop_init_path in v2/config/loops.json" basis_citations.out

# Non-ASCII scan of the 11 postimages and vocabulary scan
(cd "$R/projects/pec" && for p in $PATHS; do n=$(LC_ALL=C tr -d '\000-\177' < "$p" | wc -c | tr -d ' '); echo "$n $p"; done > "$C/non_ascii.out"); log $? projects/pec "count non-ASCII bytes in each of the 11 postimages" non_ascii.out
(cd "$R/projects/pec" && grep -rniE 'remaining' v2/ > "$C/grep_remaining.out" 2>&1); log $? projects/pec "grep -rniE remaining v2/ (expected exit 1, no match)" grep_remaining.out
