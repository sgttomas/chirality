#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
TEMPLATE="$REPO_ROOT/execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/instances/WORKING-EXP-PKG02/children/BATCH-AUTHOR-PKG02/run_author.sh"
eval "$(sed -n '1,207p' "$TEMPLATE" | sed 's/--package-id PKG-02/--package-id PKG-05/g' | sed '/git branch --show-current/d')"

RUN_REL="execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
RUN="$REPO_ROOT/$RUN_REL"
CHILD_REL="$RUN_REL/instances/WORKING-P2-PKG05/children/AUTHOR-B1"
CHILD="$REPO_ROOT/$CHILD_REL"
CAND_REL="$RUN_REL/candidates/W_P2/PIP-PKG05"
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
progress 1 DEL-05-01 precheck "$(utc)" "$(utc)" PASS 0 YES "members/DEL-05-01/FROZEN_ROW.tsv;members/DEL-05-01/SOURCE_HASHES.tsv"

process_member DEL-05-01 1 \
  "projects/chirality-piping/execution/PKG-05_Loads, Load Cases, and Stress Recovery/1_Working/DEL-05-01_Primitive load case engine" \
  "SOW-013" "OBJ-003" \
  "A primitive-load-case contract covering explicit weight, pressure, thermal, imposed-displacement, hydrotest, wind, seismic, and occasional mechanics categories, unit-aware preparation, load-case records, diagnostics, and deterministic solver-boundary contributions is produced for the declared scope and objective." \
  "The contract preserves the accepted primitive-load mechanics, unit, provenance, diagnostic, and rule-separation boundaries, including explicit missing-input findings, caller-supplied equivalent-static bases, and unresolved production policies without inventing code factors, combinations, allowables, defaults, or professional approval." \
  "Validate the contract and review source parity, category and record coverage, unit/provenance metadata, preparation and solver-vector interfaces, deterministic findings, protected-content and professional boundaries, and every surviving governed residual."

process_member DEL-05-02 2 \
  "projects/chirality-piping/execution/PKG-05_Loads, Load Cases, and Stress Recovery/1_Working/DEL-05-02_Load-case algebra engine" \
  "SOW-014" "OBJ-003,OBJ-005" \
  "A load-case-algebra contract covering unit-aware user-defined combinations, deterministic expression evaluation, result-state addition, subtraction, scaling, envelopes and ranges, diagnostics, provenance, and mechanics-only outputs is produced for the declared scope and objectives." \
  "The contract preserves the accepted bounded algebra surface, explicit units and operand compatibility, user-supplied expressions and factors, deterministic ordering and findings, and unresolved grammar and integration policies without embedding proprietary code combinations, allowables, silent conversions, or compliance meaning." \
  "Validate the contract and review source parity, algebra and result-state operations, dimensional compatibility, expression/provenance boundaries, deterministic diagnostics and tests, rule-pack separation, protected-content controls, and all unresolved governed items."

process_member DEL-05-03 3 \
  "projects/chirality-piping/execution/PKG-05_Loads, Load Cases, and Stress Recovery/1_Working/DEL-05-03_Fundamental stress recovery module" \
  "SOW-015" "OBJ-003" \
  "A fundamental stress-recovery contract covering mechanics-only recovery from element end and station resultants, axial, bending, torsional and shear components, section-property and modulus inputs, deterministic sweeps, units, findings, and result hooks is produced for the declared scope and objective." \
  "The contract preserves the accepted code-neutral mechanics boundary, explicit property and unit provenance, sign and station handling, deterministic recovery evidence, and unresolved envelope, tolerance, labeling, and validation policies without creating code stress categories, allowables, compliance conclusions, or professional approval." \
  "Validate the contract and review source parity, resultant-to-component recovery, stations and sweeps, section/modulus interfaces, units and sign conventions, diagnostics, deterministic witnesses, protected-content boundaries, and surviving integration residuals."

process_member DEL-05-04 4 \
  "projects/chirality-piping/execution/PKG-05_Loads, Load Cases, and Stress Recovery/1_Working/DEL-05-04_Analysis status semantics" \
  "SOW-047" "OBJ-005,OBJ-011" \
  "An analysis-status-semantics contract defining explicit model-incomplete, mechanics-solved, rule-inputs-incomplete, user-rule checked or failed, human-review-required, and externally recorded human-approval states with schema-first result interfaces is produced for the declared scope and objectives." \
  "The contract preserves the accepted separation of numerical computation, user-rule evaluation, missing data, professional review, and human-owned project acceptance, including hash-bound external acceptance residuals, without automatic certification, sealing, compliance, approval, or stale-record reuse." \
  "Validate the contract and review source parity, status vocabulary and transitions, automatic-versus-human authority boundaries, result and diagnostic interfaces, missing-input behavior, stale-hash obligations, tests, and professional-reliance controls."

process_member DEL-05-05 5 \
  "projects/chirality-piping/execution/PKG-05_Loads, Load Cases, and Stress Recovery/1_Working/DEL-05-05_Concentrated and distributed user load application" \
  "SOW-052,SOW-013" "OBJ-003,OBJ-012" \
  "A user-load-application contract covering concentrated forces and moments, full and partial-span distributed loads, oriented straight-pipe equivalent nodal recovery, unit-aware boundary records, deterministic findings, axial-effect bridges, and downstream result hooks is produced for the declared scope and objectives." \
  "The contract preserves the accepted general mechanics-load boundary, explicit units and provenance, deterministic ordering and invalid-input findings, and unresolved result-envelope, persistence, tolerance, and release policies without inventing magnitudes, factors, code combinations, allowables, protected content, or professional claims." \
  "Validate the contract and review source parity, concentrated and distributed application, partial spans and orientation, equivalent nodal recovery, axial-effect bridge ownership, unit/provenance metadata, result hooks, deterministic tests, and surviving governed residuals."

event 0 BATCH batch finish 1 NONE
