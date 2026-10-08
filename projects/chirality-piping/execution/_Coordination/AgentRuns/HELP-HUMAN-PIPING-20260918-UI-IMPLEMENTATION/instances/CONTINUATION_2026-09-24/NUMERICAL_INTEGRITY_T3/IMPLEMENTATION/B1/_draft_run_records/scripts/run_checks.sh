#!/bin/sh
# I108 (B1 SK): build citations.json and run main's check_citations.py on PR-B1 (records only, read-only Git).
# Usage: WT=<T3 host root> sh run_checks.sh   (writes only WT/scratch/i108_b1_sk/, the package's citations.json and outputs/)
# source_equality.py ran by hand after SHA256SUMS: outputs/source_equality_*.out (check 4 on a detached scratch commit, since removed).
set -eu
: "${WT:?set WT}"
PY="$WT/venv/bin/python"
T="$WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3"
B="$T/IMPLEMENTATION/B1"; O="$B/_draft_run_records/outputs"; S="$WT/scratch/i108_b1_sk"; TOOL="$T/IMPLEMENTATION/F2A_D1/check_citations.py"
REPO="$WT/pr-b1"; BASE=953d8c9446; HEAD=7f5f72912e; NUM=31eed8497fef9770feace42fc83880b7c6bd01ac
export GIT_OPTIONAL_LOCKS=0
mkdir -p "$S" "$O"

# 1. An empty index at NUM's head (T6S's documents table), for --suggest and --list.
"$PY" -I -c "import json,sys; d=json.load(open(sys.argv[1])); d.update(num_commit=sys.argv[2], citations=[], named_references=[], code_anchors=[]); json.dump(d, open(sys.argv[3],'w'), indent=1, ensure_ascii=False)" \
  "$T/IMPLEMENTATION/T6S/citations.json" "$NUM" "$S/probe_index.json"
"$PY" -I "$TOOL" --repo "$REPO" --base $BASE --head $HEAD --index "$S/probe_index.json" --package "$B" --suggest "$S/suggest.json" --list > "$S/probe_list.txt" 2>&1 || true

# 2. Build the index.
"$PY" -I "$B/_draft_run_records/scripts/build_citations.py" "$S/suggest.json" "$S/probe_list.txt" "$B/citations.json" "$B" "$T/IMPLEMENTATION/T6S/citations.json"

# 3. The brief's run: --base main --head the PR's code commit.
rc=0; "$PY" -I "$TOOL" --repo "$REPO" --base $BASE --head $HEAD --index "$B/citations.json" --package "$B" --out "$O/resolved.md" --list > "$O/check_pr.out" 2>&1 || rc=$?
echo "exit $rc" >> "$O/check_pr.out"

# 4. Negative controls (each must fail): an entry removed; R6b's entry pointed at R6a's heading line; a copy's bytes changed.
"$PY" -I -c "import json,sys; d=json.load(open(sys.argv[1])); d['citations']=[c for c in d['citations'] if c['token']!='R/I104/b1_sq_01/QUAL_B1.md']; json.dump(d, open(sys.argv[2],'w'), indent=1, ensure_ascii=False)" "$B/citations.json" "$S/nc1.json"
rc=0; "$PY" -I "$TOOL" --repo "$REPO" --base $BASE --head $HEAD --index "$S/nc1.json" --package "$B" > "$O/nc1_missing_entry.out" 2>&1 || rc=$?; echo "exit $rc" >> "$O/nc1_missing_entry.out"
"$PY" -I -c "import json,sys; d=json.load(open(sys.argv[1])); [c.update(heading_line=15954) for c in d['citations'] if c['token'].startswith('R6b: ')]; json.dump(d, open(sys.argv[2],'w'), indent=1, ensure_ascii=False)" "$B/citations.json" "$S/nc2.json"
rc=0; "$PY" -I "$TOOL" --repo "$REPO" --base $BASE --head $HEAD --index "$S/nc2.json" --package "$B" > "$O/nc2_wrong_heading_line.out" 2>&1 || rc=$?; echo "exit $rc" >> "$O/nc2_wrong_heading_line.out"
mkdir -p "$S/nc3/copies"; cp "$B/copies/RSS_TIME.md" "$B/copies/registration.diff" "$S/nc3/copies/"; printf 'x' | cat "$B/copies/QUAL_B1.md" - > "$S/nc3/copies/QUAL_B1.md"
rc=0; "$PY" -I "$TOOL" --repo "$REPO" --base $BASE --head $HEAD --index "$B/citations.json" --package "$S/nc3" > "$O/nc3_copy_changed.out" 2>&1 || rc=$?; echo "exit $rc" >> "$O/nc3_copy_changed.out"

# 5. The heads read.
{ echo "pr_head $(git -C "$REPO" rev-parse $HEAD)"; echo "main_base $(git -C "$REPO" rev-parse $BASE)"; echo "num_pin $NUM"; } > "$O/heads.txt"
