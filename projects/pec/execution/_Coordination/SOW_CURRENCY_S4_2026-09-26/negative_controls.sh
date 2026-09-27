#!/bin/zsh
# Negative controls for the S4 (provisional D-PEC-102) check aids: each control damages a
# scratch copy of the prep folder and must make the named check FAIL.
# Usage: negative_controls.sh <repo (git objects)> <commit> <prep dir>
# Prints one line per control; exit 0 only if every control fails as expected. Read-only on <prep dir>.
set -u
REPO=$1; C=$2; PREP=${3:A}
export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d "${TMPDIR:-/tmp}/s4pneg.XXXXXX")
git -C "$REPO" archive "$C" | tar -x -C "$T/"
bad=0
ctl() { # name, expected-fail command (run in a subshell)
  if eval "$2" > "$T/ctl.out" 2>&1; then print -r -- "FAIL control did not trip: $1"; bad=1
  else print -r -- "PASS control tripped: $1 ($(tail -1 "$T/ctl.out"))"; fi
}
fresh() { rm -rf "$T/p"; cp -R "$PREP" "$T/p"; }
F41="candidates/projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md"
F81="candidates/projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md"
F42="candidates/projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/ScopeOfWork.md"
# 1. a dropped word in a carried D-PEC-99 Gate line (DEL-04-01) fails its exhibit quote on the candidate side
fresh; python3 - "$T/p/$F41" <<'EOF'
import sys; p=sys.argv[1]; t=open(p,encoding="utf-8").read()
old="WORKING_ITEMS activation; current reliance preflight)"; assert old in t
open(p,"w",encoding="utf-8").write(t.replace(old,"WORKING_ITEMS activation)",1))
EOF
ctl "DEL-04-01 Gate line altered -> quote check" "python3 $T/p/verify_s4p_quotes.py --tree $T --gitdir $REPO --prep $T/p --observation 125cfacc1 --only DEL-04-01"
# 2. a one-character change to the DEL-08-01 OUT-001 sentence fails the two raw dependency quotes
fresh; python3 - "$T/p/$F81" <<'EOF'
import sys; p=sys.argv[1]; t=open(p,encoding="utf-8").read()
old="The PEC Unix-socket server: the listener"; assert old in t
open(p,"w",encoding="utf-8").write(t.replace(old,"The PEC Unix-socket server; the listener",1))
EOF
ctl "DEL-08-01 OUT-001 altered -> DEP-08-04-006/DEP-08-05-005 raw quotes" "python3 $T/p/verify_s4p_quotes.py --tree $T --gitdir $REPO --prep $T/p --observation 125cfacc1 --only DEL-08-01"
# 3. a documentary-correction replacement text removed (DEL-04-02 REM-002 (4)) fails its exhibit quote
fresh; python3 - "$T/p/$F42" <<'EOF'
import sys; p=sys.argv[1]; t=open(p,encoding="utf-8").read()
old="and this contract repairs nothing and invents no evidence."; assert old in t
open(p,"w",encoding="utf-8").write(t.replace(old,"and this contract repairs nothing.",1))
EOF
ctl "DEL-04-02 Part B replacement (4) altered -> quote check" "python3 $T/p/verify_s4p_quotes.py --tree $T --gitdir $REPO --prep $T/p --observation 125cfacc1 --only DEL-04-02"
# 4. a wrong hash in a state claim fails it
fresh; python3 - "$T/p/claims/DEL-10-03.json" <<'EOF'
import json,sys; p=sys.argv[1]; c=json.load(open(p,encoding="utf-8"))
e=next(e for e in c["claims"] if e["kind"]=="sha256"); e["value"]="0"*64
json.dump(c,open(p,"w",encoding="utf-8"))
EOF
ctl "DEL-10-03 sha256 claim value wrong -> state-claim check" "python3 $T/p/verify_s4p_state_claims.py --gitdir $REPO --prep $T/p --only DEL-10-03"
# 5. a sibling citation to an undefined ID fails the sibling check
fresh; python3 - "$T/p/$F42" <<'EOF'
import sys; p=sys.argv[1]; t=open(p,encoding="utf-8").read()
old="`DEL-04-03/REQ-017`"; assert old in t
open(p,"w",encoding="utf-8").write(t.replace(old,"`DEL-04-03/REQ-099`",1))
EOF
ctl "DEL-04-02 cites undefined DEL-04-03/REQ-099 -> sibling check" "python3 $T/p/check_sibling_ids.py $T/p"
# 6. a removed matrix row fails validation (run on the export with the damaged candidate)
fresh; python3 - "$T/p/$F81" <<'EOF'
import sys,re; p=sys.argv[1]; L=open(p,encoding="utf-8").read().splitlines(keepends=True)
i=max(k for k,l in enumerate(L) if l.startswith("| OUT-"))
del L[i]; open(p,"w",encoding="utf-8").writelines(L)
EOF
cp "$T/p/$F81" "$T/projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md"
ctl "DEL-08-01 last matrix row removed -> validator" "cd $T && python3 tools/scope_of_work/validate_scope_of_work.py projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access | grep -q '^PASS format=SOW_V1'"
rm -rf "$T"
print -r -- "RESULT $( [[ $bad -eq 0 ]] && print PASS || print FAIL ) negative controls"
exit $bad
