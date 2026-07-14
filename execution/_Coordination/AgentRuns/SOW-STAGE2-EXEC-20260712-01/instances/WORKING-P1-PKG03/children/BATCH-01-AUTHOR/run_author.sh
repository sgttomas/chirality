#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
TEMPLATE="$REPO_ROOT/execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/instances/WORKING-EXP-PKG02/children/BATCH-AUTHOR-PKG02/run_author.sh"
# Load only the accepted PKG-02 harness functions, substituting the package ID.
eval "$(sed -n '1,207p' "$TEMPLATE" | sed 's/--package-id PKG-02/--package-id PKG-03/g')"

RUN_REL="execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
RUN="$REPO_ROOT/$RUN_REL"
CHILD_REL="$RUN_REL/instances/WORKING-P1-PKG03/children/BATCH-01-AUTHOR"
CHILD="$REPO_ROOT/$CHILD_REL"
CAND_REL="$RUN_REL/candidates/W_P1/PIP-PKG03"
CAND="$REPO_ROOT/$CAND_REL"
FROZEN="$RUN/snapshots/W_P1/preflight-r1/P1_MANIFEST.tsv"
AUTH="D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
BASIS="projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@69ac259a7113d5a838fb22aa2e84df0e0f109713"
HEAD_EXPECTED="5f124ad80fe84357f6dc33072dc4fbdbeb05d545"
FILES=(Datasheet.md Specification.md Guidance.md Procedure.md _STATUS.md _CONTEXT.md _REFERENCES.md _DEPENDENCIES.md Dependencies.csv)
HASH_FIELDS=(10 11 12 13 14 15 16 17 18)

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
  expected_rows="$(printf '%s\n' "$row" | cut -f19)"
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
progress 1 DEL-03-01 precheck "$(utc)" "$(utc)" PASS 0 YES "members/DEL-03-01/FROZEN_ROW.tsv;members/DEL-03-01/SOURCE_HASHES.tsv"

process_member DEL-03-01 1 \
  "projects/chirality-piping/execution/PKG-03_Piping Components, Materials, and Library Data Model/1_Working/DEL-03-01_Material library schema with provenance" \
  "SOW-017" "OBJ-004" \
  "A material-library schema contract covering temperature-dependent properties, allowable slots, provenance, redistribution status, privacy, completeness, and explicit diagnostics is produced for the declared scope and objective." \
  "The contract preserves accepted material-data requirements and boundaries, including unit awareness, protected-content and redistribution controls, explicit missing-value findings, and unresolved policy decisions without supplying engineering values or professional approval." \
  "Validate the contract and review source parity, schema and fixture coverage, unit and provenance boundaries, missing-value diagnostics, protected-content controls, deterministic persistence compatibility, and unresolved human-review items."

process_member DEL-03-02 2 \
  "projects/chirality-piping/execution/PKG-03_Piping Components, Materials, and Library Data Model/1_Working/DEL-03-02_Pipe section and component library schema" \
  "SOW-018" "OBJ-004" \
  "A pipe-section and component-library schema contract covering section geometry and properties, component identity, units, provenance, library governance, and explicit completeness diagnostics is produced for the declared scope and objective." \
  "The contract preserves accepted source requirements for unit-aware, provenance-bearing pipe and component records, rights-safe public fixtures, private data boundaries, explicit unknowns, and no silent engineering defaults." \
  "Validate the contract and review source parity, pipe-section and component record coverage, units and provenance, public/private data controls, missing-value diagnostics, deterministic persistence compatibility, and unresolved policy decisions."

process_member DEL-03-03 3 \
  "projects/chirality-piping/execution/PKG-03_Piping Components, Materials, and Library Data Model/1_Working/DEL-03-03_Bend and elbow component model fields" \
  "SOW-007" "OBJ-004" \
  "A bend-and-elbow component-model contract defining geometry, section, flexibility, stiffness, mass, unit, provenance, and completeness fields is produced for the declared scope and objective." \
  "The contract preserves accepted bend and elbow modeling requirements, explicit units and provenance, protected-data boundaries, diagnostic treatment of missing inputs, and unresolved engineering-policy choices without inventing defaults." \
  "Validate the contract and review source parity, bend and elbow field coverage, dimensional consistency, provenance and protected-content boundaries, missing-input diagnostics, mechanics handoff limits, and unresolved decisions."

process_member DEL-03-04 4 \
  "projects/chirality-piping/execution/PKG-03_Piping Components, Materials, and Library Data Model/1_Working/DEL-03-04_Branch connection component model fields" \
  "SOW-008" "OBJ-004" \
  "A branch-connection component-model contract defining geometry, run and branch identities, section and stiffness inputs, units, provenance, completeness, and diagnostics is produced for the declared scope and objective." \
  "The contract preserves accepted branch-connection requirements and limits, including explicit dimensional and provenance data, rights-safe fixtures, missing-value findings, and unresolved engineering choices without inferred values or compliance claims." \
  "Validate the contract and review source parity, branch geometry and identity coverage, dimensional consistency, provenance and protected-content controls, missing-input diagnostics, mechanics handoff limits, and unresolved decisions."

process_member DEL-03-05 5 \
  "projects/chirality-piping/execution/PKG-03_Piping Components, Materials, and Library Data Model/1_Working/DEL-03-05_Rigid component models for valves, flanges, reducers, and specialty items" \
  "SOW-009" "OBJ-004" \
  "A rigid and semi-rigid component-model contract covering valves, flanges, reducers, rigid placeholders, and specialty items, including geometry, mass, center-of-gravity, stiffness, units, provenance, and completeness fields, is produced for the declared scope and objective." \
  "The contract preserves accepted rigid-component requirements, public/private and protected-data boundaries, explicit missing-value diagnostics, provenance and unit discipline, resolved historical findings, and unresolved coordinate and solver-treatment decisions without inventing component values." \
  "Validate the contract and review source parity, component-family and field coverage, split stiffness dimensions, provenance and protected-content controls, explicit missing values, coordinate-convention gaps, mechanics handoff limits, and unresolved decisions."

event 0 BATCH batch finish 1 NONE
