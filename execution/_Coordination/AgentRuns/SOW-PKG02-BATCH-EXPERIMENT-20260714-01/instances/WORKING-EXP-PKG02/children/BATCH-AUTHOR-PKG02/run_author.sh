#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
RUN_REL="execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"
RUN="$REPO_ROOT/$RUN_REL"
CHILD_REL="$RUN_REL/instances/WORKING-EXP-PKG02/children/BATCH-AUTHOR-PKG02"
CHILD="$REPO_ROOT/$CHILD_REL"
CAND_REL="$RUN_REL/candidates/PIP-PKG02"
CAND="$REPO_ROOT/$CAND_REL"
FROZEN="$RUN/instances/WORKING-EXP-PKG02/FROZEN_INPUTS.tsv"
AUTH="D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
BASIS="projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@69ac259a7113d5a838fb22aa2e84df0e0f109713"
HEAD_EXPECTED="3efa950aa981f9d3491bab2ab3b3319a5a2c6d5c"
FILES=(Datasheet.md Specification.md Guidance.md Procedure.md _STATUS.md _CONTEXT.md _REFERENCES.md _DEPENDENCIES.md Dependencies.csv)
HASH_FIELDS=(9 10 11 12 13 14 15 16 17)

utc() { date -u +%Y-%m-%dT%H:%M:%SZ; }
sha() { shasum -a 256 "$1" | awk '{print $1}'; }
event() {
  printf '{"timestamp_utc":"%s","sequence":%s,"deliverable_id":"%s","stage":"%s","event":"%s","attempt":%s,"reason_code":"%s"}\n' \
    "$(utc)" "$1" "$2" "$3" "$4" "$5" "$6" >> "$CHILD/RUNTIME_EVENTS.jsonl"
}
progress() {
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\tPASS\tNONE\tNONE\t%s\t%s\n' \
    "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8" "$9" >> "$CHILD/PROGRESS.tsv"
}
expect_fail() {
  local prefix="$1"
  shift
  rm -f "${prefix}.stdout" "${prefix}.stderr" "${prefix}.exit"
  set +e
  "$@" >"${prefix}.stdout" 2>"${prefix}.stderr"
  local rc=$?
  set -e
  printf '%s\n' "$rc" > "${prefix}.exit"
  if [ "$rc" -eq 0 ]; then
    printf 'expected failure but command passed\n' >&2
    return 1
  fi
}
check_frozen() {
  local did="$1" live="$2" mdir="$3"
  local row
  row="$(awk -F '\t' -v d="$did" '$1==d {print; exit}' "$FROZEN")"
  [ -n "$row" ]
  printf '%s\n' "$row" > "$mdir/FROZEN_ROW.tsv"
  local idx actual expected i
  printf 'file\tsha256\tphase\tverdict\n' > "$mdir/SOURCE_HASHES.tsv"
  for i in "${!FILES[@]}"; do
    idx="${HASH_FIELDS[$i]}"
    expected="$(printf '%s\n' "$row" | cut -f "$idx")"
    actual="$(sha "$live/${FILES[$i]}")"
    [ "$actual" = "$expected" ]
    printf '%s\t%s\tbefore\tPASS\n' "${FILES[$i]}" "$actual" >> "$mdir/SOURCE_HASHES.tsv"
  done
  [ ! -e "$live/ScopeOfWork.md" ]
  grep -q 'IN_PROGRESS' "$live/_STATUS.md"
}
post_frozen() {
  local did="$1" live="$2" mdir="$3"
  local row idx actual expected i
  row="$(awk -F '\t' -v d="$did" '$1==d {print; exit}' "$FROZEN")"
  for i in "${!FILES[@]}"; do
    idx="${HASH_FIELDS[$i]}"
    expected="$(printf '%s\n' "$row" | cut -f "$idx")"
    actual="$(sha "$live/${FILES[$i]}")"
    [ "$actual" = "$expected" ]
    printf '%s\t%s\tafter\tPASS\n' "${FILES[$i]}" "$actual" >> "$mdir/SOURCE_HASHES.tsv"
  done
  [ ! -e "$live/ScopeOfWork.md" ]
}

process_member() {
  local did="$1" seq="$2" live_rel="$3" scopes="$4" objectives="$5" out="$6" ac="$7" ver="$8"
  local live="$REPO_ROOT/$live_rel" mdir="$CHILD/members/$did" cand="$CAND/$did"
  local started ended conv_start conv_end final_start final_end check_start check_end
  local w1="$mdir/workspace-a" w2="$mdir/workspace-b"
  local p1="$mdir/final-a/ScopeOfWork.md" p2="$mdir/final-b/ScopeOfWork.md"
  local r1="$mdir/final-a/report.json" r2="$mdir/final-b/report.json"
  local cand_e="$cand/evidence/ScopeOfWork.md" cand_p="$cand/production/ScopeOfWork.md" cand_r="$cand/finalization.json"
  local -a cmd
  local ref

  mkdir -p "$mdir" "$cand/evidence" "$cand/production"
  started="$(utc)"
  event "$seq" "$did" precheck start 1 NONE
  [ "$(git rev-parse HEAD)" = "$HEAD_EXPECTED" ]
  [ "$(git rev-parse origin/main)" = "$HEAD_EXPECTED" ]
  [ "$(git branch --show-current)" = main ]
  check_frozen "$did" "$live" "$mdir"
  ended="$(utc)"
  if [ "$seq" -gt 1 ]; then
    progress "$seq" "$did" precheck "$started" "$ended" PASS 0 YES "members/$did/FROZEN_ROW.tsv;members/$did/SOURCE_HASHES.tsv"
  fi
  event "$seq" "$did" precheck finish 1 NONE

  conv_start="$(utc)"
  event "$seq" "$did" conversion start 1 NONE
  mkdir -p "$w1" "$w2"
  cp -a "$live/." "$w1/"
  cp -a "$live/." "$w2/"
  cmd=(python3 tools/scope_of_work/convert_four_documents_to_scope_of_work.py
    --deliverable "$w1" --deliverable-id "$did" --package-id PKG-02
    --decomposition-basis "$BASIS" --output-description "$out"
    --acceptance-criterion "$ac" --verification-method "$ver"
    --isolated-migration --migration-authority "$AUTH")
  IFS=',' read -ra scope_array <<< "$scopes"
  for ref in "${scope_array[@]}"; do cmd+=(--project-scope-ref "$ref"); done
  IFS=',' read -ra objective_array <<< "$objectives"
  for ref in "${objective_array[@]}"; do cmd+=(--package-objective-ref "$ref"); done
  "${cmd[@]}" > "$mdir/conversion-a.stdout" 2> "$mdir/conversion-a.stderr"
  cmd=(python3 tools/scope_of_work/convert_four_documents_to_scope_of_work.py
    --deliverable "$w2" --deliverable-id "$did" --package-id PKG-02
    --decomposition-basis "$BASIS" --output-description "$out"
    --acceptance-criterion "$ac" --verification-method "$ver"
    --isolated-migration --migration-authority "$AUTH")
  for ref in "${scope_array[@]}"; do cmd+=(--project-scope-ref "$ref"); done
  for ref in "${objective_array[@]}"; do cmd+=(--package-objective-ref "$ref"); done
  "${cmd[@]}" > "$mdir/conversion-b.stdout" 2> "$mdir/conversion-b.stderr"
  cmp -s "$w1/ScopeOfWork.md" "$w2/ScopeOfWork.md"
  cp "$w1/ScopeOfWork.md" "$cand_e"
  printf 'artifact\tsha256_a\tsha256_b\tbyte_identical\n' > "$mdir/DETERMINISM.tsv"
  printf 'evidence_conversion\t%s\t%s\ttrue\n' "$(sha "$w1/ScopeOfWork.md")" "$(sha "$w2/ScopeOfWork.md")" >> "$mdir/DETERMINISM.tsv"
  conv_end="$(utc)"
  progress "$seq" "$did" conversion "$conv_start" "$conv_end" PASS 0 NO "members/$did/DETERMINISM.tsv"
  event "$seq" "$did" conversion finish 1 NONE

  final_start="$(utc)"
  event "$seq" "$did" finalization start 1 NONE
  mkdir -p "$mdir/final-a" "$mdir/final-b"
  python3 tools/scope_of_work/finalize_scope_of_work.py --evidence-candidate "$w1/ScopeOfWork.md" --output "$p1" --report "$r1" > "$mdir/finalization-a.stdout" 2> "$mdir/finalization-a.stderr"
  python3 tools/scope_of_work/finalize_scope_of_work.py --evidence-candidate "$w2/ScopeOfWork.md" --output "$p2" --report "$r2" > "$mdir/finalization-b.stdout" 2> "$mdir/finalization-b.stderr"
  cmp -s "$p1" "$p2"
  cmp -s "$r1" "$r2"
  cp "$p1" "$cand_p"
  cp "$r1" "$cand_r"
  cmp -s "$p1" "$cand_p"
  cmp -s "$r1" "$cand_r"
  printf 'clean_finalization\t%s\t%s\ttrue\n' "$(sha "$p1")" "$(sha "$p2")" >> "$mdir/DETERMINISM.tsv"
  printf 'finalization_report\t%s\t%s\ttrue\n' "$(sha "$r1")" "$(sha "$r2")" >> "$mdir/DETERMINISM.tsv"
  final_end="$(utc)"
  progress "$seq" "$did" finalization "$final_start" "$final_end" PASS 0 NO "members/$did/final-a/report.json;members/$did/DETERMINISM.tsv"
  event "$seq" "$did" finalization finish 1 NONE

  check_start="$(utc)"
  event "$seq" "$did" validation_mapping_qa start 1 NONE
  python3 tools/scope_of_work/validate_scope_of_work.py "$w1" --isolated-migration --migration-authority "$AUTH" --json > "$mdir/validation-authorized-dual.json" 2> "$mdir/validation-authorized-dual.stderr"
  python3 tools/scope_of_work/validate_scope_of_work.py "$cand_p" --json > "$mdir/validation-sow-v1.json" 2> "$mdir/validation-sow-v1.stderr"
  set +e
  rg -ni 'sow-source-begin|sow-source-end|migration-authority:|pilot-variance:|issued-preparation-|migration candidate' "$cand_p" > "$mdir/clean-residue.scan"
  local residue_rc=$?
  set -e
  [ "$residue_rc" -eq 1 ]
  [ "$(grep -c '^>' "$cand_p")" -gt 0 ]

  python3 tools/scope_of_work/map_scope_of_work_claims.py --scope-of-work "$w1/ScopeOfWork.md" --production-scope-of-work "$cand_p" --source-dir "$w1" --output-csv "$mdir/claim-map-a.csv" > "$mdir/claim-map-a.stdout" 2> "$mdir/claim-map-a.stderr"
  python3 tools/scope_of_work/map_scope_of_work_claims.py --scope-of-work "$w2/ScopeOfWork.md" --production-scope-of-work "$cand_p" --source-dir "$w2" --output-csv "$mdir/claim-map-b.csv" > "$mdir/claim-map-b.stdout" 2> "$mdir/claim-map-b.stderr"
  cmp -s "$mdir/claim-map-a.csv" "$mdir/claim-map-b.csv"
  python3 tools/scope_of_work/report_scope_of_work_parity.py --scope-of-work "$w1/ScopeOfWork.md" --production-scope-of-work "$cand_p" --source-dir "$w1" --output-json "$mdir/parity-a.json" --output-md "$mdir/parity-a.md" --isolated-migration --migration-authority "$AUTH" > "$mdir/parity-a.stdout" 2> "$mdir/parity-a.stderr"
  python3 tools/scope_of_work/report_scope_of_work_parity.py --scope-of-work "$w2/ScopeOfWork.md" --production-scope-of-work "$cand_p" --source-dir "$w2" --output-json "$mdir/parity-b.json" --output-md "$mdir/parity-b.md" --isolated-migration --migration-authority "$AUTH" > "$mdir/parity-b.stdout" 2> "$mdir/parity-b.stderr"
  cmp -s "$mdir/parity-a.json" "$mdir/parity-b.json"
  cmp -s "$mdir/parity-a.md" "$mdir/parity-b.md"

  python3 tools/scope_of_work/derive_review_checklist.py "$cand_p" --output "$mdir/checklist-a.json" > "$mdir/checklist-a.stdout" 2> "$mdir/checklist-a.stderr"
  python3 tools/scope_of_work/derive_review_checklist.py "$cand_p" --output "$mdir/checklist-b.json" > "$mdir/checklist-b.stdout" 2> "$mdir/checklist-b.stderr"
  cmp -s "$mdir/checklist-a.json" "$mdir/checklist-b.json"
  python3 tools/scope_of_work/render_scope_of_work.py "$cand_p" --output "$mdir/render-a.html" > "$mdir/render-a.stdout" 2> "$mdir/render-a.stderr"
  python3 tools/scope_of_work/render_scope_of_work.py "$cand_p" --output "$mdir/render-b.html" > "$mdir/render-b.stdout" 2> "$mdir/render-b.stderr"
  cmp -s "$mdir/render-a.html" "$mdir/render-b.html"
  ! rg -ni '<script|<form|https?://|src=//' "$mdir/render-a.html" > "$mdir/render-forbidden.scan"

  mkdir -p "$mdir/mutated-production"
  cp "$cand_p" "$mdir/mutated-production/ScopeOfWork.md"
  perl -0pi -e 's/^> /> MUTATED /m' "$mdir/mutated-production/ScopeOfWork.md"
  expect_fail "$mdir/negative-mutated-map" python3 tools/scope_of_work/map_scope_of_work_claims.py --scope-of-work "$w1/ScopeOfWork.md" --production-scope-of-work "$mdir/mutated-production/ScopeOfWork.md" --source-dir "$w1" --output-csv "$mdir/negative-mutated-map.csv"
  [ ! -e "$mdir/negative-mutated-map.csv" ]
  expect_fail "$mdir/negative-mutated-parity" python3 tools/scope_of_work/report_scope_of_work_parity.py --scope-of-work "$w1/ScopeOfWork.md" --production-scope-of-work "$mdir/mutated-production/ScopeOfWork.md" --source-dir "$w1" --output-json "$mdir/negative-mutated-parity.json" --isolated-migration --migration-authority "$AUTH"

  mkdir -p "$mdir/negative-partial"
  cp "$live/Datasheet.md" "$mdir/negative-partial/Datasheet.md"
  cp "$live/_STATUS.md" "$mdir/negative-partial/_STATUS.md"
  expect_fail "$mdir/negative-partial-validation" python3 tools/scope_of_work/validate_scope_of_work.py "$mdir/negative-partial" --json
  expect_fail "$mdir/negative-unauthorized-dual" python3 tools/scope_of_work/validate_scope_of_work.py "$w1" --json
  rm -f "$mdir/negative-ambiguous-checklist.json"
  expect_fail "$mdir/negative-ambiguous-checklist" python3 tools/scope_of_work/derive_review_checklist.py "$w1" --output "$mdir/negative-ambiguous-checklist.json"
  [ ! -e "$mdir/negative-ambiguous-checklist.json" ]
  rm -f "$mdir/negative-unauthorized-checklist.json"
  expect_fail "$mdir/negative-unauthorized-checklist" python3 tools/scope_of_work/derive_review_checklist.py "$w1" --isolated-migration --migration-authority UNAUTHORIZED --output "$mdir/negative-unauthorized-checklist.json"
  [ ! -e "$mdir/negative-unauthorized-checklist.json" ]
  rm -f "$mdir/negative-evidence-render.html"
  expect_fail "$mdir/negative-evidence-render" python3 tools/scope_of_work/render_scope_of_work.py "$w1/ScopeOfWork.md" --output "$mdir/negative-evidence-render.html"
  [ ! -e "$mdir/negative-evidence-render.html" ]

  printf 'artifact\tsha256_a\tsha256_b\tbyte_identical\n' > "$mdir/DERIVATIVE_DETERMINISM.tsv"
  printf 'claim_map\t%s\t%s\ttrue\n' "$(sha "$mdir/claim-map-a.csv")" "$(sha "$mdir/claim-map-b.csv")" >> "$mdir/DERIVATIVE_DETERMINISM.tsv"
  printf 'parity_json\t%s\t%s\ttrue\n' "$(sha "$mdir/parity-a.json")" "$(sha "$mdir/parity-b.json")" >> "$mdir/DERIVATIVE_DETERMINISM.tsv"
  printf 'checklist\t%s\t%s\ttrue\n' "$(sha "$mdir/checklist-a.json")" "$(sha "$mdir/checklist-b.json")" >> "$mdir/DERIVATIVE_DETERMINISM.tsv"
  printf 'render_html\t%s\t%s\ttrue\n' "$(sha "$mdir/render-a.html")" "$(sha "$mdir/render-b.html")" >> "$mdir/DERIVATIVE_DETERMINISM.tsv"
  post_frozen "$did" "$live" "$mdir"
  check_end="$(utc)"
  progress "$seq" "$did" validation_mapping_qa "$check_start" "$check_end" PASS 0 NO "members/$did/validation-sow-v1.json;members/$did/parity-a.json;members/$did/checklist-a.json;members/$did/negative-*.exit"
  progress "$seq" "$did" postcheck_terminal "$check_end" "$(utc)" PASS 0 YES "members/$did/SOURCE_HASHES.tsv"
  event "$seq" "$did" validation_mapping_qa finish 1 NONE
}

process_member DEL-02-01 1 \
  "projects/chirality-piping/execution/PKG-02_Domain Model, Units, and Core Schemas/1_Working/DEL-02-01_Canonical domain model schema" \
  "SOW-041,SOW-065" "OBJ-001,OBJ-012,OBJ-014" \
  "A canonical domain-model schema contract covering project, physical and analytical models, materials, components, loads, results, reports, assumptions, traceability, and source-of-truth references is produced for the declared scope and objectives." \
  "The contract preserves the accepted source requirements and boundaries for the canonical model schema, including unit, provenance, diagnostic, professional-reliance, and protected-content constraints, with unresolved decisions retained as stated." \
  "Validate the contract and review source parity, object-family coverage, unit and provenance boundaries, deterministic persistence compatibility, and absence of protected content or compliance claims."

process_member DEL-02-02 2 \
  "projects/chirality-piping/execution/PKG-02_Domain Model, Units, and Core Schemas/1_Working/DEL-02-02_Unit system and dimensional-analysis core contract" \
  "SOW-025" "OBJ-001,OBJ-012" \
  "A unit-system and dimensional-analysis core contract specifying dimensions, conversion rules, storage conventions, and unit-test obligations is produced for the declared scope and objectives." \
  "The contract preserves the accepted source requirements for explicit dimensions, compatible conversion and storage behavior, deterministic checks, and fail-closed treatment of missing or incompatible units." \
  "Validate the contract and review source parity, dimensional consistency, conversion and storage rules, deterministic unit checks, explicit findings, and professional-reliance boundaries."

process_member DEL-02-03 3 \
  "projects/chirality-piping/execution/PKG-02_Domain Model, Units, and Core Schemas/1_Working/DEL-02-03_Code-neutral analysis boundary model" \
  "SOW-002" "OBJ-001,OBJ-011" \
  "A code-neutral analysis-boundary model defining states and interfaces that separate mechanics solving, user-rule checking, and human professional approval is produced for the declared scope and objectives." \
  "The contract preserves the accepted source distinctions among software-computed mechanics, user-supplied rule evaluation, and authorized human approval without creating automatic compliance or professional-reliance meaning." \
  "Validate the contract and review source parity, allowed state and interface distinctions, authority labels, diagnostics, and absence of automatic code-compliance or approval claims."

process_member DEL-02-04 4 \
  "projects/chirality-piping/execution/PKG-02_Domain Model, Units, and Core Schemas/1_Working/DEL-02-04_Plugin and extension domain contracts" \
  "SOW-038" "OBJ-009" \
  "Plugin and extension domain contracts defining governed extension points, adapter boundaries, permissions, and schema-first application-service access are produced for the declared scope and objective." \
  "The contracts preserve the accepted source constraints on validation, units, provenance, diagnostics, private data, canonical hashing, storage access, and professional responsibility without granting direct SQL or protected-content access." \
  "Validate the contracts and review source parity, extension-point and permission boundaries, no-bypass behavior, structured diagnostics, private-data controls, and absence of protected content or authority expansion."

process_member DEL-02-05 5 \
  "projects/chirality-piping/execution/PKG-02_Domain Model, Units, and Core Schemas/1_Working/DEL-02-05_Project persistence and round-trip serialization" \
  "SOW-050,SOW-041" "OBJ-001,OBJ-012" \
  "A project-persistence and round-trip serialization contract covering create, open, save, versioned persistence, units, loads, rule-pack references, provenance, and reproducibility metadata is produced for the declared scope and objectives." \
  "The contract preserves the accepted source requirements for schema-governed local persistence, deterministic round trips, explicit units and provenance, validated service boundaries, and unresolved physical-container or migration decisions." \
  "Validate the contract and review source parity, round-trip semantic preservation, canonical serialization and hash behavior, version diagnostics, private-data and protected-content boundaries, and absence of professional-approval claims."

event 0 BATCH batch finish 1 NONE
