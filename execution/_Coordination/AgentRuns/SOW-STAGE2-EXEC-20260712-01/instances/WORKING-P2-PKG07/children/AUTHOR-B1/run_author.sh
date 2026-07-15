#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
TEMPLATE="$REPO_ROOT/execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/instances/WORKING-EXP-PKG02/children/BATCH-AUTHOR-PKG02/run_author.sh"
eval "$(sed -n '1,207p' "$TEMPLATE" | sed 's/--package-id PKG-02/--package-id PKG-07/g' | sed '/git branch --show-current/d')"

RUN_REL="execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
RUN="$REPO_ROOT/$RUN_REL"
CHILD_REL="$RUN_REL/instances/WORKING-P2-PKG07/children/AUTHOR-B1"
CHILD="$REPO_ROOT/$CHILD_REL"
CAND_REL="$RUN_REL/candidates/W_P2/PIP-PKG07"
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
progress 1 DEL-07-01 precheck "$(utc)" "$(utc)" PASS 0 YES "members/DEL-07-01/FROZEN_ROW.tsv;members/DEL-07-01/SOURCE_HASHES.tsv"

process_member DEL-07-01 1 \
  "projects/chirality-piping/execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-01_3D viewport and centerline editor" \
  "SOW-020" "OBJ-006" \
  "A 3D viewport and centerline-editor contract covering unit-aware nodes, pipe runs, bends, simple component symbols, stable selection identity, command-routed edits, explicit diagnostics, and bounded interaction evidence is produced for the declared scope and objective." \
  "The contract preserves the current implemented viewport slice and named residuals, separates durable model state from transient interaction state, keeps missing or protected engineering data explicit, and invents no component dimensions, code values, defaults, compliance status, or professional approval." \
  "Validate the contract and review source parity, centerline and symbol boundaries, command/service mutation routing, stable identity, units, diagnostics, current implementation declarations and residuals, protected-data controls, and every retained governed TBD."

process_member DEL-07-02 2 \
  "projects/chirality-piping/execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-02_Model tree and property inspector" \
  "SOW-020,SOW-021" "OBJ-006" \
  "A model-tree and property-inspector contract covering stable entity hierarchy and selection, unit-aware editable properties, provenance and validation feedback, command-routed mutations, and viewport coordination is produced for the declared scope and objective." \
  "The contract preserves the current implemented inspection/editing boundary, explicit read-only and missing-data states, durable-versus-transient state separation, and protected/private data constraints without inventing engineering defaults, component data, authority, or hidden mutations." \
  "Validate the contract and review source parity, tree/selection identity, property categories and edit routing, unit and provenance handling, viewport synchronization, diagnostics and blocked states, current residuals, and professional-boundary language."

process_member DEL-07-03 3 \
  "projects/chirality-piping/execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-03_Material, component, and rule-pack editors" \
  "SOW-021" "OBJ-006" \
  "A material, component, and rule-pack editor contract covering schema-governed records, units, provenance and redistribution state, checksum/version identity, validated application-service commands, diagnostics, and explicit private/protected-content boundaries is produced for the declared scope and objective." \
  "The contract preserves the current editor slice and unresolved implementation decisions, keeps public and private data distinct, prevents silent defaults and direct persistence bypass, and invents no proprietary tables, formulas, allowables, component dimensions, code content, or professional acceptance." \
  "Validate the contract and review source parity, material/component/rule-pack field boundaries, units and provenance, checksum/version handling, command and persistence boundaries, private/protected data, diagnostics, current residuals, and every retained TBD or conflict."

process_member DEL-07-04 4 \
  "projects/chirality-piping/execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-04_Missing-data warning and blocking UX" \
  "SOW-022" "OBJ-006,OBJ-011" \
  "A missing-data warning and blocking-UX contract covering typed findings, solve-blocking and rule-check-blocking separation, affected-object navigation, provenance and unit diagnostics, remediation guidance, and visible professional-boundary status is produced for the declared scope and objectives." \
  "The contract preserves explicit fail-closed behavior, the distinction between mechanics input completeness and user-rule input completeness, and current warning UX evidence without inventing values, suppressing findings, treating absence as success, or implying code compliance or approval." \
  "Validate the contract and review source parity, diagnostic classes and severity, blocking-state separation, navigation and remediation surfaces, missing/incompatible/unprovenanced data handling, current implementation declarations and residuals, and no-silent-default behavior."

process_member DEL-07-05 5 \
  "projects/chirality-piping/execution/PKG-07_Graphical User Interface and Engineering Workflow/1_Working/DEL-07-05_Results viewer" \
  "SOW-023" "OBJ-006,OBJ-007" \
  "A results-viewer contract covering unit-aware mechanics and user-rule result categories, tabular and graphical review, warnings and assumptions, result-envelope traceability, ratio availability, and report/export handoff signals is produced for the declared scope and objectives." \
  "The contract preserves the implemented result surface and translational overlay, retains rotational visualization as an explicit residual, separates mechanics, user-rule checks, and human review, and invents no thresholds, formulas, allowables, code categories, compliance status, or professional approval." \
  "Validate the contract and review source parity, result categories and unit labels, diagnostics and provenance, status separation, ratio blocked/unavailable behavior, translational versus rotational visualization boundary, report/export traceability, and every retained governed residual."

event 0 BATCH batch finish 1 NONE
