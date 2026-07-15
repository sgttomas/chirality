#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
TEMPLATE="$REPO_ROOT/execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/instances/WORKING-EXP-PKG02/children/BATCH-AUTHOR-PKG02/run_author.sh"
eval "$(sed -n '1,207p' "$TEMPLATE" | sed 's/--package-id PKG-02/--package-id PKG-06/g' | sed '/git branch --show-current/d')"

RUN_REL="execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
RUN="$REPO_ROOT/$RUN_REL"
CHILD_REL="$RUN_REL/instances/WORKING-P2-PKG06/children/AUTHOR-B1"
CHILD="$REPO_ROOT/$CHILD_REL"
CAND_REL="$RUN_REL/candidates/W_P2/PIP-PKG06"
CAND="$REPO_ROOT/$CAND_REL"
FROZEN="$RUN/snapshots/W_P2/preflight/P2_MANIFEST.tsv"
AUTH="D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
BASIS="projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@eaad463c0d481f6f1654e6adb5ee718f566176e9"
HEAD_EXPECTED="eaad463c0d481f6f1654e6adb5ee718f566176e9"
FILES=(Datasheet.md Specification.md Guidance.md Procedure.md _STATUS.md _CONTEXT.md _REFERENCES.md _DEPENDENCIES.md Dependencies.csv)
HASH_FIELDS=(10 12 14 16 19 20 21 22 23)

check_frozen() {
  local did="$1" live="$2" mdir="$3" row idx actual expected i dep_rows expected_rows
  row="$(awk -F '\t' -v d="$did" '$4==d {print; exit}' "$FROZEN")"
  [ -n "$row" ]
  printf '%s\n' "$row" > "$mdir/FROZEN_ROW.tsv"
  [ "$(printf '%s\n' "$row" | cut -f6)" = IN_PROGRESS ]
  [ "$(printf '%s\n' "$row" | cut -f9)" = LEGACY_FOUR_DOC ]
  printf 'file\tsha256\tphase\tverdict\n' > "$mdir/SOURCE_HASHES.tsv"
  for i in "${!FILES[@]}"; do
    idx="${HASH_FIELDS[$i]}"
    expected="$(printf '%s\n' "$row" | cut -f "$idx")"
    actual="$(sha "$live/${FILES[$i]}")"
    [ "$actual" = "$expected" ]
    printf '%s\t%s\tbefore\tPASS\n' "${FILES[$i]}" "$actual" >> "$mdir/SOURCE_HASHES.tsv"
  done
  dep_rows="$(( $(wc -l < "$live/Dependencies.csv") - 1 ))"
  expected_rows="$(printf '%s\n' "$row" | cut -f24)"
  [ "$dep_rows" = "$expected_rows" ]
  [ ! -e "$live/ScopeOfWork.md" ]
  grep -q 'IN_PROGRESS' "$live/_STATUS.md"
}

post_frozen() {
  local did="$1" live="$2" mdir="$3" row idx actual expected i
  row="$(awk -F '\t' -v d="$did" '$4==d {print; exit}' "$FROZEN")"
  for i in "${!FILES[@]}"; do
    idx="${HASH_FIELDS[$i]}"
    expected="$(printf '%s\n' "$row" | cut -f "$idx")"
    actual="$(sha "$live/${FILES[$i]}")"
    [ "$actual" = "$expected" ]
    printf '%s\t%s\tafter\tPASS\n' "${FILES[$i]}" "$actual" >> "$mdir/SOURCE_HASHES.tsv"
  done
  [ ! -e "$live/ScopeOfWork.md" ]
}

mkdir -p "$CHILD/members" "$CAND"
printf 'sequence\tdeliverable_id\tstage\tstarted_utc\tfinished_utc\tresult\tretries\tremediation\tblocker\twaiver\tevidence\tterminal\n' > "$CHILD/PROGRESS.tsv"
: > "$CHILD/RUNTIME_EVENTS.jsonl"
progress 1 DEL-06-01 precheck "$(utc)" "$(utc)" PASS 0 YES "members/DEL-06-01/FROZEN_ROW.tsv;members/DEL-06-01/SOURCE_HASHES.tsv"

process_member DEL-06-01 1 \
  "projects/chirality-piping/execution/PKG-06_Rule Packs and User-Supplied Code Check Engine/1_Working/DEL-06-01_Rule-pack schema" \
  "SOW-016,SOW-042" "OBJ-005" \
  "A rule-pack-schema contract covering identity and versioning, provenance and redistribution status, canonical payload checksums, required inputs, declarative formula and allowable slots, check criteria, diagnostics, units, and professional-boundary metadata is produced for the declared scope and objective." \
  "The contract preserves the accepted public/private and protected-content boundaries, declarative sandbox-compatible posture, explicit missing-data behavior, canonical JSON/JCS-compatible hash basis, and retained grammar, storage, encryption, and packaging TBDs without inventing protected formulas, allowables, code content, defaults, or professional approval." \
  "Validate the contract and review source parity, schema record groups, identity/version/checksum/provenance fields, required-input and unit handling, evaluator and redistribution boundaries, diagnostics, invented-example constraints, and every retained governed residual."

process_member DEL-06-02 2 \
  "projects/chirality-piping/execution/PKG-06_Rule Packs and User-Supplied Code Check Engine/1_Working/DEL-06-02_Sandboxed unit-aware expression evaluator" \
  "SOW-045" "OBJ-005" \
  "A sandboxed unit-aware expression-evaluator contract covering a declarative allowlisted grammar, typed variables and functions, dimensional checks, bounded evaluation, deterministic diagnostics, canonical rule-pack version binding, and schema-first result envelopes is produced for the declared scope and objective." \
  "The contract preserves the accepted no-arbitrary-code, no-side-effect, unit/provenance, protected-content, private-data, and professional-authority boundaries together with retained grammar/library and integration TBDs, without embedding proprietary rules, formulas, allowables, silent conversions, or compliance meaning." \
  "Validate the contract and review source parity, grammar and sandbox boundaries, dimensional compatibility, persistence/version binding, deterministic evaluation and diagnostics, resource constraints, protected-content controls, and every unresolved governed item."

process_member DEL-06-03 3 \
  "projects/chirality-piping/execution/PKG-06_Rule Packs and User-Supplied Code Check Engine/1_Working/DEL-06-03_Required-input completeness checker" \
  "SOW-004" "OBJ-002,OBJ-005" \
  "A required-input-completeness contract connecting declarative rule-pack requirements to project, model, and user-supplied data, with explicit missing, unit-incompatible, unprovenanced, and rule-check-blocking findings, is produced for the declared scope and objectives." \
  "The contract preserves the accepted separation between solve-blocking physical inputs and rule-check-required data, explicit no-default behavior, private user-data and protected-content boundaries, and professional responsibility, while retaining the expression grammar/library decision as TBD and inventing no engineering values." \
  "Validate the contract and review source parity, declarative input binding, completeness and provenance classes, unit compatibility, RULE_INPUTS_INCOMPLETE and RULE_CHECK_BLOCKING behavior, schema/status dependencies, protected-content escalation, and surviving governed conflicts."

process_member DEL-06-04 4 \
  "projects/chirality-piping/execution/PKG-06_Rule Packs and User-Supplied Code Check Engine/1_Working/DEL-06-04_Private rule-pack lifecycle and checksum handling" \
  "SOW-042" "OBJ-002,OBJ-005" \
  "A private rule-pack lifecycle and checksum contract covering stable identity and version, source/provenance notice, redistribution and quarantine status, canonical JSON/JCS-compatible payload hashing, non-JSON manifest hashes, diagnostics, and report/audit references is produced for the declared scope and objectives." \
  "The contract preserves the accepted local-first privacy, explicit payload-bound checksum, stale-hash, protected-content, unit, and professional-authority boundaries while deferring storage, encryption, access policy, permission persistence, and final redistribution enums to their governed owners." \
  "Validate the contract and review source parity, lifecycle metadata, checksum payload boundaries, private/public and quarantine handling, diagnostics, audit hooks, no-bypass constraints, deferred security ownership, and all surviving source conflicts."

process_member DEL-06-05 5 \
  "projects/chirality-piping/execution/PKG-06_Rule Packs and User-Supplied Code Check Engine/1_Working/DEL-06-05_Invented non-code example rule pack" \
  "SOW-016" "OBJ-005,OBJ-011" \
  "An invented non-code example-rule-pack contract covering demonstration-only schema shape, original artificial values, provenance and redistribution fields, required-input and check placeholders, explicit notices, and safe verification expectations is produced for the declared scope and objectives." \
  "The contract preserves the accepted invented-only public posture, declarative non-executable boundary, no-silent-default behavior, protected-content exclusions, and professional non-reliance notice while retaining schema, grammar, evaluator, and checksum details as TBD until their owning deliverables resolve them." \
  "Validate the contract and review source parity, invented-value and notice requirements, provenance and redistribution fields, protected-content exclusions, professional boundaries, schema/evaluator ownership, example-path limits, and every surviving governed residual."

event 0 BATCH batch finish 1 NONE
