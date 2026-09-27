#!/bin/zsh
# Negative controls for the S1 (provisional D-PEC-104) verifiers, on scratch copies only.
# Usage: negative_controls.sh <repo (git objects)> <commit> <prep dir>
# Each control perturbs a copy and must FAIL; prints PASS when the control is caught.
set -u
REPO=$1; C=$2; PREP=${3:A}
export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d "${TMPDIR:-/tmp}/s1pneg.XXXXXX")
git -C "$REPO" archive "$C" | tar -x -C "$T" --one-top-level=tree 2>/dev/null || { mkdir -p "$T/tree"; git -C "$REPO" archive "$C" | tar -x -C "$T/tree"; }
fresh() { rm -rf "$T/p"; cp -R "$PREP" "$T/p"; rm -rf "$T/post"; cp -R "$T/tree" "$T/post"; (cd "$T/p/candidates" && find . -name ScopeOfWork.md | while read f; do cp "$f" "$T/post/$f"; done); }
cand() { print -r -- $(ls "$T"/p/candidates/projects/pec/execution/PKG-*/1_Working/$1_*/ScopeOfWork.md); }
q() { python3 "$T/p/verify_s1p_quotes.py" --tree "$T/post" --gitdir "$REPO" --prep "$T/p" --observation 125cfacc1 --obs-exempt DEL-03-06 --only $1 > "$T/out" 2>&1; }
ok() { [[ $1 -ne 0 ]] && print "PASS control caught: $2" || { print "FAIL control NOT caught: $2"; bad=1; }; }
bad=0
# 1. a Part B replacement string removed from the DEL-03-02 candidate (candidate side of the exhibit quote)
fresh; f=$(cand DEL-03-02); python3 - "$f" <<'P'
import sys; p=sys.argv[1]; s=open(p).read(); a="The exhibit's empty `BasisCitation` is frozen with the accepted DAG."; assert a in s; open(p,"w").write(s.replace(a,"The exhibit's empty BasisCitation is frozen."))
P
cp "$f" "$T/post/${f#$T/p/candidates/}"; q DEL-03-02; ok $? "DEL-03-02 Part B REM-016 replacement string altered"
# 2. one character of a PRD quotation changed in the DEL-02-02 candidate
fresh; f=$(cand DEL-02-02); python3 - "$f" <<'P'
import sys; p=sys.argv[1]; s=open(p).read(); a="The reconciler shall ingest"; assert a in s; open(p,"w").write(s.replace(a,"The reconciler shall ingestt",1))
P
cp "$f" "$T/post/${f#$T/p/candidates/}"; q DEL-02-02; ok $? "DEL-02-02 PRD PEC-RCN-002 quotation altered by one character"
# 3. a state claim with a wrong hash (DEL-01-04 claims file)
fresh; python3 - "$T/p/claims/DEL-01-04.json" <<'P'
import sys,json; p=sys.argv[1]; d=json.load(open(p))
for e in d["claims"]:
    if e["kind"]=="sha256": e["value"]="0"*64; break
json.dump(d,open(p,"w"))
P
python3 "$T/p/verify_s1p_state_claims.py" --gitdir "$REPO" --prep "$T/p" --only DEL-01-04 > "$T/out" 2>&1; ok $? "DEL-01-04 sha256 claim with a wrong value"
# 4. a cited sibling definition removed: DEL-03-01 CON-005 renamed (cited by DEL-10-02 and DEL-10-10)
fresh; f=$(cand DEL-03-01); sed -i '' 's/^- \*\*CON-005\*\*/- **CON-099**/' "$f"
python3 "$T/p/check_qualified_ids.py" --prep "$T/p" --gitdir "$REPO" --observation 125cfacc1 > "$T/out" 2>&1; ok $? "DEL-03-01 CON-005 definition removed while siblings cite it"
# 5. an S1 sibling quotation broken: DEL-03-01 OUT-001 text changed (quoted by DEL-03-02, DEL-03-03, DEL-10-10)
fresh; f=$(cand DEL-03-01); python3 - "$f" <<'P'
import sys; p=sys.argv[1]; s=open(p).read(); a="A full-rebuild reconciler entry point in the PEC service core"; assert a in s; open(p,"w").write(s.replace(a,"A full-rebuild reconciler entry point in PEC",1))
P
cp "$f" "$T/post/${f#$T/p/candidates/}"; q DEL-03-02; ok $? "DEL-03-01 OUT-001 changed under DEL-03-02's sibling quotation"
# 6. a candidate byte changed: the bound act refuses at preflight
fresh; f=$(cand DEL-10-10); print >> "$f"; rm -rf "$T/act"; cp -R "$T/tree" "$T/act"
python3 "$T/p/apply_s1p.py" --repo "$T/act" --candidates "$T/p/candidates" --check-only > "$T/out" 2>&1; ok $? "a candidate differs from its tabled postimage (apply --check-only)"
# 7. a matrix row removed: the validator fails and the checklist refuses with no artifact
fresh; f=$(cand DEL-01-04); python3 - "$f" <<'P'
import sys; p=sys.argv[1]; L=open(p).read().splitlines(True); i=max(k for k,l in enumerate(L) if l.startswith("| OUT-")); del L[i]; open(p,"w").write("".join(L))
P
d=$(dirname "${f#$T/p/candidates/}"); cp "$f" "$T/post/$d/ScopeOfWork.md"
(cd "$T/post" && python3 tools/scope_of_work/validate_scope_of_work.py "$d" > "$T/out" 2>&1); ok $? "DEL-01-04 matrix row removed (validator)"
(cd "$T/post" && python3 tools/scope_of_work/derive_review_checklist.py --output "$T/neg_checklist.json" "$d" > "$T/out" 2>&1); r=$?; [[ -e "$T/neg_checklist.json" ]] && r=0; ok $r "DEL-01-04 matrix row removed (checklist refuses, no artifact)"
rm -rf "$T"
print "RESULT $([[ $bad -eq 0 ]] && print PASS || print FAIL)"
exit $bad
