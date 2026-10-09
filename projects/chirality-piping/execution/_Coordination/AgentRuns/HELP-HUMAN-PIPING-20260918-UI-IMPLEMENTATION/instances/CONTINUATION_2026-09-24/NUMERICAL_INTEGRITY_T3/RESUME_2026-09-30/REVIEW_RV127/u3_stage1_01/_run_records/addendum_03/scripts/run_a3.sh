#!/bin/zsh
# RV127 addendum 03: Git-read evidence for the A2-B-1 repair. Usage: WT=<T3 root> run_a3.sh
# Git reads only (GIT_OPTIONAL_LOCKS=0); writes only $S/out and $S/se_* work dirs.
set -u
export GIT_OPTIONAL_LOCKS=0
NUM=$WT/numerics; S=$WT/scratch/rv127_u3/a3; O=$S/out
P=projects/chirality-piping
T=$P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3
X=":!$P/execution"
B3='invented_mechanics_result.json invented_mechanics_result_precision_1_dense.json invented_mechanics_result_precision_1_sparse.json'
san() { sed -e "s#$WT#WT#g" -e "s#$T#T#g" -e "s#projects/chirality-piping/#P/#g"; }
cd $NUM
{
echo "# RV127 addendum 03: the A2-B-1 repair on PR #1168 (Git reads, GIT_OPTIONAL_LOCKS=0)"
echo "## commits"; for c in 8a12de28db 98733368f9 ed012c7ccf 3bfcceb4c0 70aa51b076; do git log -1 --format='%h parents %p  %s' $c; done
echo "## git diff --no-renames --name-status 98733368f9 ed012c7ccf (all paths)"; git diff --no-renames --name-status 98733368f9 ed012c7ccf
echo "## git diff --no-renames --name-status 98733368f9 ed012c7ccf -- . ':!P/execution'"; git diff --no-renames --name-status 98733368f9 ed012c7ccf -- . $X
echo "## git diff --no-renames --name-status 8a12de28db ed012c7ccf -- . ':!P/execution'"; git diff --no-renames --name-status 8a12de28db ed012c7ccf -- . $X
echo "## git diff --no-renames --name-status ed012c7ccf 3bfcceb4c0 (all paths)"; git diff --no-renames --name-status ed012c7ccf 3bfcceb4c0
echo "## outside P/execution, --no-renames: line counts of name-status diffs"
for pair in "3bfcceb4c0 70aa51b076" "ed012c7ccf 70aa51b076" "ed012c7ccf cfeb5b76fe" "ed012c7ccf 2fd24aedf1" "ed012c7ccf 29710d848e"; do set -- ${=pair}; echo "$1..$2: $(git diff --no-renames --name-status $1 $2 -- . $X | wc -l | tr -d ' ')"; done
echo "## the package at the PR head against NUM: $(git diff --no-renames --name-status 3bfcceb4c0 70aa51b076 -- $T/IMPLEMENTATION/U3 | wc -l | tr -d ' ') differing paths"
echo "## the PR's maintained paths, ba500defa4..ed012c7ccf outside P/execution"
echo "default (rename detection): $(git diff --name-only ba500defa4 ed012c7ccf -- . $X | wc -l | tr -d ' ')"
echo "--no-renames: $(git diff --no-renames --name-only ba500defa4 ed012c7ccf -- . $X | wc -l | tr -d ' ')"; git diff --no-renames --name-status ba500defa4 ed012c7ccf -- . $X | cut -f1 | sort | uniq -c
echo "## blobs of the three files"
for b in ${=B3}; do for c in ba500defa4 98733368f9 ed012c7ccf 3bfcceb4c0 70aa51b076; do echo "$b $c $(git rev-parse -q --verify $c:$P/fixtures/product_preview/$b 2>/dev/null)"; done; done
echo "## PR #1168 on GitHub (gh pr view, read only)"; gh pr view 1168 --repo sgttomas/chirality --json headRefOid,baseRefOid,state -q '"head \(.headRefOid) base \(.baseRefOid) \(.state)"'
} 2>&1 | san > $O/repair_tree.txt
{
echo "# RV127 addendum 03: mentions of the three basenames at 3bfcceb4c0, outside P/execution"
for b in ${=B3}; do echo "## exact '$b'"; git grep -n -F "$b" 3bfcceb4c0 -- . $X | sed 's#^3bfcceb4c0:##' | cut -c1-220; done
echo "## the stem 'invented_mechanics_result' without an exact basename (other files or build-asset names)"
git grep -n -F 'invented_mechanics_result' 3bfcceb4c0 -- . $X | sed 's#^3bfcceb4c0:##' | grep -v -E 'invented_mechanics_result(_precision_1_(dense|sparse))?\.json' | python3 -I -c 'import re,sys
for l in sys.stdin:
    f,n,t=l.split(":",2); m=re.search(r"invented_mechanics_result[^ \"`)\\]*",t); print(f"{f}:{n}: {m.group(0)}")'
echo "## code reads (include_str!/include_bytes!/import/open) of the three basenames in .rs .ts .tsx .js .mjs .py, outside P/execution"
git grep -n -E 'invented_mechanics_result(_precision_1_(dense|sparse))?\.json' 3bfcceb4c0 -- '*.rs' '*.ts' '*.tsx' '*.js' '*.mjs' '*.py' '*.toml' '*.yml' '*.yaml' $X | sed 's#^3bfcceb4c0:##'; echo "(end; empty means none)"
} 2>&1 | san > $O/readers_sweep.txt
cd $S
for run in "pos 3bfcceb4c0 fixed" "neg 98733368f9 fixed" "pos_oldtool 3bfcceb4c0 old" "neg_oldtool 98733368f9 old"; do
  set -- ${=run}; tool=$S/scripts/source_equality_70aa.py; [ "$3" = old ] && tool=$S/scripts/source_equality_cfeb_renames_on.py
  { echo "# source_equality.py ($3 tool: $( [ $3 = old ] && echo 'cfeb5b76fe, names() with rename detection' || echo '70aa51b076, names() with --no-renames')) --pr $2 --int 70aa51b076 --main ba500defa4 --package T/IMPLEMENTATION/U3"
    python3 -I $tool --repo $NUM --pr $2 --int 70aa51b076 --main ba500defa4 --work $S/se_$1 --json $O/source_equality_$1.json --package $T/IMPLEMENTATION/U3; echo "exit $?"; } 2>&1 | san > $O/source_equality_$1.txt
done
{ echo "# check_citations.py (main's IMPLEMENTATION/F2A_D1 tool) --base ba500defa4 --head 3bfcceb4c0 --index T/IMPLEMENTATION/U3/citations.json --package T/IMPLEMENTATION/U3"
  python3 -I $S/scripts/check_citations.py --repo $NUM --base ba500defa4 --head 3bfcceb4c0 --index $NUM/$T/IMPLEMENTATION/U3/citations.json --package $NUM/$T/IMPLEMENTATION/U3 --out $O/citations_resolved.md; echo "exit $?"; } 2>&1 | san > $O/citations.txt
sed -i '' -e "s#$WT#WT#g" -e "s#$T#T#g" $O/citations_resolved.md
{ echo "# sha256 of the tools as run (scratch copies) and their repo blobs"
  shasum -a 256 $S/scripts/source_equality_70aa.py $S/scripts/source_equality_cfeb_renames_on.py $S/scripts/check_citations.py
  cd $NUM; for spec in "70aa51b076:$T/IMPLEMENTATION/F2A_D1/source_equality.py" "cfeb5b76fe:$T/IMPLEMENTATION/F2A_D1/source_equality.py" "70aa51b076:$T/IMPLEMENTATION/F2A_D1/check_citations.py"; do echo "$spec $(git show $spec | shasum -a 256 | cut -c1-64)"; done; } 2>&1 | san > $O/tools.txt
