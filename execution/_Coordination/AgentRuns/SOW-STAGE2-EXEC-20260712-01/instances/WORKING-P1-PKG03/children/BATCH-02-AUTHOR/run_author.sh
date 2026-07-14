#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
TEMPLATE="$REPO_ROOT/execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/instances/WORKING-EXP-PKG02/children/BATCH-AUTHOR-PKG02/run_author.sh"
# Load only the accepted PKG-02 harness functions, substituting the package ID.
eval "$(sed -n '1,207p' "$TEMPLATE" | sed 's/--package-id PKG-02/--package-id PKG-03/g')"

RUN_REL="execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
RUN="$REPO_ROOT/$RUN_REL"
CHILD_REL="$RUN_REL/instances/WORKING-P1-PKG03/children/BATCH-02-AUTHOR"
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
progress 1 DEL-03-06 precheck "$(utc)" "$(utc)" PASS 0 YES "members/DEL-03-06/FROZEN_ROW.tsv;members/DEL-03-06/SOURCE_HASHES.tsv"

process_member DEL-03-06 1 \
  "projects/chirality-piping/execution/PKG-03_Piping Components, Materials, and Library Data Model/1_Working/DEL-03-06_Expansion joint component model" \
  "SOW-010" "OBJ-004" \
  "An expansion-joint component-model contract covering supplied stiffnesses, effective area, movement limits, hardware fields, units, provenance, completeness, and diagnostics is produced for the declared scope and objective." \
  "The contract preserves accepted expansion-joint requirements and boundaries, including supplied-data-only values, explicit units and provenance, protected-content controls, missing-value diagnostics, unresolved taxonomy and solver mappings, and no invented defaults or professional approval." \
  "Validate the contract and review source parity, field and fixture coverage, dimensional and provenance boundaries, missing-data diagnostics, protected-content controls, downstream solver limits, and unresolved human-review items."

process_member DEL-03-07 2 \
  "projects/chirality-piping/execution/PKG-03_Piping Components, Materials, and Library Data Model/1_Working/DEL-03-07_Public-private library import provenance checker" \
  "SOW-019,SOW-044" "OBJ-002,OBJ-004" \
  "A public/private library import-provenance checker contract covering source, license, redistribution, contributor and review metadata, privacy posture, unit preservation, quarantine, and diagnostics is produced for the declared scope and objectives." \
  "The contract preserves accepted public/private data boundaries, conservative missing-provenance handling, protected-content quarantine, unit and diagnostic requirements, and unresolved rights, vocabulary, source-catalog, and legal-acceptance decisions without creating legal conclusions or public defaults." \
  "Validate the contract and review source parity, metadata and diagnostic coverage, public/private separation, unit preservation, protected-content quarantine, invented-fixture boundaries, and unresolved human or legal review items."

process_member DEL-03-08 3 \
  "projects/chirality-piping/execution/PKG-03_Piping Components, Materials, and Library Data Model/1_Working/DEL-03-08_Pipe section property and mass-property calculator" \
  "SOW-051,SOW-018" "OBJ-004,OBJ-012" \
  "A pipe section-property and mass-property calculator contract covering explicit dimensional and material inputs, units, provenance, section and mass outputs, diagnostics, protected-data boundaries, and solver handoff limits is produced for the declared scope and objectives." \
  "The contract preserves accepted calculator requirements and boundaries, including user-entered or lawfully imported inputs, dimensional checks, no silent defaults, invented fixtures, unresolved conversion, schema, contributor, dependency, and human-review decisions, and no code-compliance or professional-approval claim." \
  "Validate the contract and review source parity, section and mass-property coverage, dimensional consistency, missing-input behavior, provenance, protected-content controls, calculator and solver separation, bounded witness evidence, and unresolved human-review items."

event 0 BATCH batch finish 1 NONE
