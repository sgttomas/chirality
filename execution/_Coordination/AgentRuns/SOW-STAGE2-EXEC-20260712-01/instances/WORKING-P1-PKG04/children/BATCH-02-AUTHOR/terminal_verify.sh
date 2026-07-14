#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
RUN_REL="execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CHILD="$REPO_ROOT/$RUN_REL/instances/WORKING-P1-PKG04/children/BATCH-02-AUTHOR"
CAND="$REPO_ROOT/$RUN_REL/candidates/W_P1/PIP-PKG04"
FROZEN="$REPO_ROOT/$RUN_REL/snapshots/W_P1/preflight-r1/P1_MANIFEST.tsv"
DID=DEL-04-06

sha() { shasum -a 256 "$1" | awk '{print $1}'; }

[ "$(git rev-parse HEAD)" = 2a5e3825d8d2fc4943742a53ccad3b89c4c81902 ]
[ "$(git rev-parse origin/main)" = 2a5e3825d8d2fc4943742a53ccad3b89c4c81902 ]
[ "$(git branch --show-current)" = main ]
[ "$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["status"])' "$CHILD/STATUS.json")" = PASS ]
[ "$(awk -F '\t' 'NR>1{s+=$6} END{print s}' "$CHILD/MEMBER_RESULTS.tsv")" -eq 276 ]
[ "$(awk -F '\t' 'NR>1{s+=$7} END{print s}' "$CHILD/MEMBER_RESULTS.tsv")" -eq 276 ]
[ "$(find "$CAND/$DID" -type f | wc -l | tr -d ' ')" -eq 3 ]

mdir="$CHILD/members/$DID"
row="$(awk -F '\t' -v d="$DID" '$4==d {print; exit}' "$FROZEN")"
live="$REPO_ROOT/$(printf '%s\n' "$row" | cut -f5)"
[ ! -e "$live/ScopeOfWork.md" ]
[ "$(wc -l < "$mdir/SOURCE_HASHES.tsv")" -eq 19 ]
[ "$(awk -F '\t' 'NR>1 && $4!="PASS"{n++} END{print n+0}' "$mdir/SOURCE_HASHES.tsv")" -eq 0 ]
cmp -s "$mdir/workspace-a/ScopeOfWork.md" "$mdir/workspace-b/ScopeOfWork.md"
cmp -s "$mdir/final-a/ScopeOfWork.md" "$mdir/final-b/ScopeOfWork.md"
cmp -s "$mdir/final-a/report.json" "$mdir/final-b/report.json"
cmp -s "$mdir/claim-map-a.csv" "$mdir/claim-map-b.csv"
cmp -s "$mdir/parity-a.json" "$mdir/parity-b.json"
cmp -s "$mdir/parity-a.md" "$mdir/parity-b.md"
cmp -s "$mdir/checklist-a.json" "$mdir/checklist-b.json"
cmp -s "$mdir/render-a.html" "$mdir/render-b.html"
[ "$(python3 -c 'import json,sys; print(str(json.load(open(sys.argv[1]))["pass"]).lower())' "$mdir/parity-a.json")" = true ]
[ "$(python3 -c 'import json,sys; print(str(json.load(open(sys.argv[1]))["valid"]).lower())' "$mdir/validation-sow-v1.json")" = true ]
for probe in negative-mutated-map negative-mutated-parity negative-partial-validation negative-unauthorized-dual negative-ambiguous-checklist negative-unauthorized-checklist negative-evidence-render; do
  [ "$(cat "$mdir/$probe.exit")" -ne 0 ]
done
! rg -ni 'sow-source-begin|sow-source-end|migration-authority:|pilot-variance:|issued-preparation-|migration candidate' "$CAND/$DID/production/ScopeOfWork.md"

while IFS=$'\t' read -r before after before_bytes after_bytes rel operation; do
  [ "$before" = before_sha256 ] && continue
  [ "$(sha "$REPO_ROOT/$rel")" = "$after" ]
  [ "$(wc -c < "$REPO_ROOT/$rel" | tr -d ' ')" = "$after_bytes" ]
  [ "$before" != "$after" ]
  [ "$before_bytes" -gt "$after_bytes" ]
  [ -n "$operation" ]
done < "$CHILD/NORMALIZATION.tsv"

: > "$CHILD/WHOLE_DIFF_HYGIENE.warnings"
while IFS= read -r -d '' path; do
  [ "$path" = "$CHILD/LAUNCH_BRIEF.md" ] && continue
  [ "$path" = "$CHILD/MANIFEST.tsv" ] && continue
  [ "$path" = "$CHILD/WHOLE_DIFF_HYGIENE.warnings" ] && continue
  set +e
  git diff --no-index --check -- /dev/null "$path" >> "$CHILD/WHOLE_DIFF_HYGIENE.warnings" 2>&1
  set -e
done < <(find "$CHILD" "$CAND/$DID" -type f -print0)
[ ! -s "$CHILD/WHOLE_DIFF_HYGIENE.warnings" ]

printf 'sha256\tbytes\tpath\n' > "$CHILD/MANIFEST.tsv"
while IFS= read -r path; do
  [ "$path" = "$CHILD/MANIFEST.tsv" ] && continue
  rel="${path#$REPO_ROOT/}"
  printf '%s\t%s\t%s\n' "$(sha "$path")" "$(wc -c < "$path" | tr -d ' ')" "$rel" >> "$CHILD/MANIFEST.tsv"
done < <(find "$CHILD" -type f | LC_ALL=C sort)
while IFS=$'\t' read -r expected bytes rel; do
  [ "$expected" = sha256 ] && continue
  [ "$(sha "$REPO_ROOT/$rel")" = "$expected" ]
  [ "$(wc -c < "$REPO_ROOT/$rel" | tr -d ' ')" = "$bytes" ]
done < "$CHILD/MANIFEST.tsv"
