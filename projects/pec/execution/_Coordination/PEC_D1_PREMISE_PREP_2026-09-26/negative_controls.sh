#!/bin/zsh
# Negative controls for the D1 premise-amendment (provisional D-PEC-105) check aids. Each
# control first shows its check PASSING on an undamaged scratch copy of the prep folder
# (baseline), then damages a fresh scratch copy and requires that same check, and the named
# line where one exists, to FAIL. Adapted from the S4 negative_controls.sh.
# Usage: negative_controls.sh <repo (git objects)> <commit> <prep dir> <out dir>
# Prints one line per control and a final `RESULT PASS|FAIL negative controls k/n`; exit 0
# only if every baseline passes and every control trips. Read-only on <repo> and <prep dir>;
# scratch lives in a mktemp -d directory under $TMPDIR, removed at exit.
set -u
REPO=$1; C=$2; PREP=${3:A}; OUT=${4:A}
export PYTHONDONTWRITEBYTECODE=1
mkdir -p "$OUT"
T=$(mktemp -d "${TMPDIR:-/tmp}/d1pneg.XXXXXX")
[[ ${D1P_KEEP:-0} == 1 ]] || trap 'rm -rf "$T"' EXIT
X=$T/x; mkdir -p "$X"
# The checks below read only tools/ and projects/pec from the export.
git -C "$REPO" archive "$C" tools projects/pec | tar -x -C "$X"
OBS=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["observation_commit"])' "$PREP/targets.json")
PIN=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["pin_commit"])' "$PREP/targets.json")
: > "$OUT/NEGATIVE_CONTROLS.out"
say() { print -r -- "$1" | tee -a "$OUT/NEGATIVE_CONTROLS.out"; }
fresh() { rm -rf "$T/p"; cp -R "$PREP" "$T/p"; }
n=0; good=0
# ctl <number> <name> <command> [<line regex that must appear in the failing output>]
ctl() {
  local num=$1 name=$2 cmd=$3 must=${4:-}
  n=$((n+1))
  if [[ ${BASE_OK:-0} != 1 ]]; then say "FAIL control $num baseline did not pass, control not meaningful: $name"; return; fi
  if eval "$cmd" > "$OUT/neg_$num.out" 2>&1; then say "FAIL control $num did not trip: $name"; return; fi
  if [[ -n $must ]] && ! grep -qE -- "$must" "$OUT/neg_$num.out"; then
    say "FAIL control $num tripped, but not on the named line /$must/: $name"; return; fi
  good=$((good+1)); say "PASS control $num tripped: $name (${$(grep -m1 -E -- "${must:-RESULT|FAIL}" "$OUT/neg_$num.out")[1,140]})"
}
base() { # <number> <command>: the undamaged check passes
  if eval "$2" > "$OUT/neg_${1}_baseline.out" 2>&1; then BASE_OK=1; else BASE_OK=0; fi
}
# target facts: first target, first SOW target, and the prep files that carry evidence
read -r K1 P1 <<< "$(python3 -c 'import json,sys;t=json.load(open(sys.argv[1]))["targets"][0];print(t["key"],t["path"])' "$PREP/targets.json")"
read -r KS PS <<< "$(python3 -c 'import json,sys;t=[x for x in json.load(open(sys.argv[1]))["targets"] if x["kind"]=="sow"][0];print(t["key"],t["path"])' "$PREP/targets.json")"
QF=$(python3 -c 'import json,sys,pathlib
for f in sorted(pathlib.Path(sys.argv[1]).glob("quotes/*.json")):
    if json.load(open(f,encoding="utf-8"))["quotes"]: print(f.stem); break' "$PREP")
CF=$(python3 -c 'import json,sys,pathlib
for f in sorted(pathlib.Path(sys.argv[1]).glob("claims/*.json")):
    c=json.load(open(f,encoding="utf-8"))["claims"]
    if any(e["kind"] in ("sha256","sha256_prefix") for e in c): print(f.stem); break' "$PREP")

# 1. a one-character change to a candidate fails render_candidates.py check
fresh; base 1 "python3 $T/p/render_candidates.py --gitdir $REPO --prep $T/p --only $K1"
python3 - "$T/p/candidates/$P1" <<'EOF'
import sys; p=sys.argv[1]; b=bytearray(open(p,"rb").read()); i=len(b)//2
while not (65 <= b[i] <= 90 or 97 <= b[i] <= 122): i+=1
b[i]^=0x20; open(p,"wb").write(bytes(b))
EOF
ctl 1 "$K1 candidate one character changed -> render_candidates.py check" \
    "python3 $T/p/render_candidates.py --gitdir $REPO --prep $T/p --only $K1" "^FAIL $K1 candidate differs from ledger rendering"

# 2. a changed quote text fails verify_d1p_quotes.py
if [[ -n $QF ]]; then
  fresh; base 2 "python3 $T/p/verify_d1p_quotes.py --tree $X --gitdir $REPO --prep $T/p --observation $OBS --only $QF"
  QID=$(python3 - "$T/p/quotes/$QF.json" <<'EOF'
import json,sys; p=sys.argv[1]; q=json.load(open(p,encoding="utf-8")); e=q["quotes"][0]; s=e["text"]; i=len(s)//2
while not s[i].isalpha(): i+=1
e["text"]=s[:i]+s[i].swapcase()+s[i+1:]; json.dump(q,open(p,"w",encoding="utf-8"),ensure_ascii=False); print(e["id"])
EOF
)
  ctl 2 "$QF quote $QID text changed by one character -> verify_d1p_quotes.py" \
      "python3 $T/p/verify_d1p_quotes.py --tree $X --gitdir $REPO --prep $T/p --observation $OBS --only $QF" "^FAIL $QF $QID "
else BASE_OK=0; ctl 2 "no quotes file with an entry" "true"; fi

# 3. a wrong hash in a state claim fails verify_d1p_state_claims.py
if [[ -n $CF ]]; then
  fresh; base 3 "python3 $T/p/verify_d1p_state_claims.py --gitdir $REPO --prep $T/p --only $CF"
  CID=$(python3 - "$T/p/claims/$CF.json" <<'EOF'
import json,sys; p=sys.argv[1]; c=json.load(open(p,encoding="utf-8"))
e=next(e for e in c["claims"] if e["kind"] in ("sha256","sha256_prefix"))
e["value"]="0"*len(e["value"]); json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False); print(e["id"])
EOF
)
  ctl 3 "$CF claim $CID hash value wrong -> verify_d1p_state_claims.py" \
      "python3 $T/p/verify_d1p_state_claims.py --gitdir $REPO --prep $T/p --only $CF" "^FAIL $CF $CID .*git=NO"
else BASE_OK=0; ctl 3 "no claims file with a sha256 claim" "true"; fi

# 4. a removed matrix row in a SOW candidate fails validation (on the export, damaged candidate copied in)
fresh; cp "$T/p/candidates/$PS" "$X/$PS"
VAL="cd $X && python3 tools/scope_of_work/validate_scope_of_work.py ${PS:h} > $T/val.out 2>&1; cat $T/val.out; grep -q '^PASS format=SOW_V1' $T/val.out"
base 4 "$VAL"
python3 - "$T/p/candidates/$PS" <<'EOF'
import sys; p=sys.argv[1]; L=open(p,encoding="utf-8").read().splitlines(keepends=True)
i=max(k for k,l in enumerate(L) if l.startswith("| OUT-")); del L[i]; open(p,"w",encoding="utf-8").writelines(L)
EOF
cp "$T/p/candidates/$PS" "$X/$PS"
ctl 4 "$KS last output-matrix row removed -> validate_scope_of_work.py" "$VAL" "^FAIL"
git -C "$REPO" show "$C:$PS" > "$X/$PS"   # restore the export's preimage

# 5. a candidate that drops the pin commit fails the PIN check
fresh; base 5 "python3 $T/p/verify_d1p_quotes.py --tree $X --gitdir $REPO --prep $T/p --observation $OBS --only $K1"
python3 - "$T/p/candidates/$P1" "$PIN" <<'EOF'
import sys; p,pin=sys.argv[1],sys.argv[2]; t=open(p,encoding="utf-8").read(); assert pin in t
open(p,"w",encoding="utf-8").write(t.replace(pin,""))
EOF
ctl 5 "$K1 candidate without pin commit $PIN -> verify_d1p_quotes.py PIN" \
    "python3 $T/p/verify_d1p_quotes.py --tree $X --gitdir $REPO --prep $T/p --observation $OBS --only $K1" "^FAIL $K1 PIN "

# 6. a stale postimage hash in apply_d1p.py fails --check-only
fresh; base 6 "python3 $T/p/apply_d1p.py --repo $X --candidates $T/p/candidates --check-only | grep -q '^CHECK preflight passed'"
python3 - "$T/p/apply_d1p.py" "$T/p/candidates/$P1" <<'EOF'
import hashlib,sys; s,c=sys.argv[1],sys.argv[2]; t=open(s,encoding="utf-8").read()
post=hashlib.sha256(open(c,"rb").read()).hexdigest(); assert t.count(post)==1
stale=hashlib.sha256(open(c,"rb").read()+b"\n").hexdigest()
open(s,"w",encoding="utf-8").write(t.replace(post,stale))
EOF
ctl 6 "apply_d1p.py carries a stale postimage hash for $K1 -> --check-only" \
    "python3 $T/p/apply_d1p.py --repo $X --candidates $T/p/candidates --check-only" "^FAIL candidate hash mismatch: $K1 "

say "RESULT $( [[ $good -eq $n && $n -eq 6 ]] && print PASS || print FAIL ) negative controls $good/$n"
[[ $good -eq $n && $n -eq 6 ]]
