#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
TEMPLATE="$REPO_ROOT/execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/instances/WORKING-EXP-PKG02/children/BATCH-AUTHOR-PKG02/run_author.sh"
# Load only the accepted PKG-02 harness functions, substituting the package ID.
eval "$(sed -n '1,207p' "$TEMPLATE" | sed 's/--package-id PKG-02/--package-id PKG-04/g')"

RUN_REL="execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
RUN="$REPO_ROOT/$RUN_REL"
CHILD_REL="$RUN_REL/instances/WORKING-P1-PKG04/children/BATCH-01-AUTHOR"
CHILD="$REPO_ROOT/$CHILD_REL"
CAND_REL="$RUN_REL/candidates/W_P1/PIP-PKG04"
CAND="$REPO_ROOT/$CAND_REL"
FROZEN="$RUN/snapshots/W_P1/preflight-r1/P1_MANIFEST.tsv"
AUTH="D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
BASIS="projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@69ac259a7113d5a838fb22aa2e84df0e0f109713"
HEAD_EXPECTED="2a5e3825d8d2fc4943742a53ccad3b89c4c81902"
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
progress 1 DEL-04-01 precheck "$(utc)" "$(utc)" PASS 0 YES "members/DEL-04-01/FROZEN_ROW.tsv;members/DEL-04-01/SOURCE_HASHES.tsv"

process_member DEL-04-01 1 \
  "projects/chirality-piping/execution/PKG-04_Solver Core and Numerical Methods/1_Working/DEL-04-01_3D frame stiffness kernel" \
  "SOW-005,SOW-035" "OBJ-003" \
  "A 3D frame-stiffness-kernel contract covering six-degree-of-freedom node mapping, global assembly, coordinate transforms, boundary conditions, sparse-solve interfaces, mechanics-only result envelopes, and deterministic verification is produced for the declared scope and objective." \
  "The contract preserves the accepted frame-kernel requirements and current declarations, including unit and provenance boundaries, explicit missing-input and solver findings, rights-cleared verification data, and unresolved formulation, tolerance, sparse-policy, arc-pressure-thrust, and mechanics-assessment items without inventing engineering values or approval." \
  "Validate the contract and review source parity, frame/DOF and assembly coverage, coordinate and boundary interfaces, sparse/reproducibility obligations, units and diagnostics, protected-content and professional boundaries, and every unresolved governed item."

process_member DEL-04-02 2 \
  "projects/chirality-piping/execution/PKG-04_Solver Core and Numerical Methods/1_Working/DEL-04-02_Straight pipe element" \
  "SOW-006" "OBJ-003" \
  "A straight-pipe-element contract covering local stiffness, explicit section-property integration, weight hooks, boundary metadata, spanned loads and axial effects, unit-aware end/station resultant recovery, and deterministic solver verification is produced for the declared scope and objective." \
  "The contract preserves the accepted straight-pipe mechanics and interface boundaries, including explicit units and lawful input provenance, no hidden load or engineering defaults, rights-cleared fixtures, mechanics-only outputs, and the unresolved governed solver-to-result-envelope integration." \
  "Validate the contract and review source parity, straight-pipe behavior and frame-kernel boundaries, section and weight interfaces, spanned-load and resultant coverage, dimensional checks, explicit findings, protected-content controls, and result-envelope residuals."

process_member DEL-04-03 3 \
  "projects/chirality-piping/execution/PKG-04_Solver Core and Numerical Methods/1_Working/DEL-04-03_Linear support and restraint models" \
  "SOW-011" "OBJ-003" \
  "A linear-support and restraint contract covering anchors, guides, line stops, vertical supports, springs, imposed-displacement boundary data, frame-kernel DOF mapping, boundary preparation/application, explicit findings, and deterministic tests is produced for the declared scope and objective." \
  "The contract preserves the accepted implemented linear-support boundaries, unit-bearing quantities, no-default behavior, frame-kernel indexing and prescribed-displacement integration, rights-safe fixtures, and unresolved support-coordinate, sparse/result-envelope, release, and constant-effort-hanger work without implying nonlinear behavior or approval." \
  "Validate the contract and review source parity, all SOW-011 families, FrameDof and boundary surfaces, dimensional metadata, missing/invalid-data findings, deterministic test evidence, protected-content controls, linear/nonlinear separation, and surviving governed residuals."

process_member DEL-04-04 4 \
  "projects/chirality-piping/execution/PKG-04_Solver Core and Numerical Methods/1_Working/DEL-04-04_Nonlinear support active-set solver" \
  "SOW-012" "OBJ-003" \
  "A nonlinear-support classifier and state-oracle contract covering one-way restraints, gaps, lift-off, friction, state-switched transitions, convergence and non-convergence reporting, report-facing records, and integration-facing deterministic verification is produced for the declared scope and objective." \
  "The contract preserves the accepted classifier versus assembled-loop ownership, implemented state-transition and bounded Coulomb-friction basis, unit and diagnostic boundaries, explicit missing inputs, mechanics-only posture, and unresolved path-history, convergence-threshold, sparse-live-path, and validation policies without inventing defaults or engineering acceptance." \
  "Validate the contract and review source parity, nonlinear behavior categories and state transitions, classifier/integration ownership, convergence diagnostics, units and provenance, protected-content and professional boundaries, deterministic transition witnesses, and every surviving governed residual."

process_member DEL-04-05 5 \
  "projects/chirality-piping/execution/PKG-04_Solver Core and Numerical Methods/1_Working/DEL-04-05_Sparse solver performance harness" \
  "SOW-035" "OBJ-003,OBJ-008" \
  "A sparse-solver performance and regression harness contract covering deterministic practical-model runs, reproducibility, performance and conditioning observations, lawful fixture provenance, solver/version/hash settings, diagnostics, limitations, and reviewable records is produced for the declared scope and objectives." \
  "The contract preserves the accepted observer-only harness boundary, deterministic regression intent, explicit units and provenance, no invented timing, memory, conditioning, model-size, or release thresholds, mechanics-only reporting, and formal-review, dimensional-validation, hosted-CI, and cross-machine policy residuals." \
  "Validate the contract and review source parity, harness/solver separation, repeated-run determinism, performance and conditioning records, unit and fixture provenance, protected-content controls, diagnostics and limitations, no compliance claims, and all unresolved governed threshold and release items."

event 0 BATCH batch finish 1 NONE
