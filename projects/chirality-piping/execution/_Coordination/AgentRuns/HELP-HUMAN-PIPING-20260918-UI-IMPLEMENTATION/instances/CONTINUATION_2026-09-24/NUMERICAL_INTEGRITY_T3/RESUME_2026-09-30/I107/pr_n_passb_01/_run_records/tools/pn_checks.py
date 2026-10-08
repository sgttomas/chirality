"""I107 SB round 2 (PR-N): round 1's `controls_sq` (b1_checks.py) with the findings' line numbers dropped, since PR-N
moves PP lib.rs's control sites by two lines: each control's name, outcome, completeness, TAV and finding (file and
expression) must equal SQ's. Usage: python3 pn_checks.py controls_pn <controls json> <SQ controls json>; exit 0 or 6."""
import json, re, sys
cmd, a_p, b_p = sys.argv[1:4]
assert cmd == "controls_pn"
nl = lambda s: re.sub(r":\d+", "", s)
norm = lambda d: [(r["control"], r["pass"], r["complete"], r["TAV"], nl(json.dumps(r["findings"]))) for r in d]
a, b = json.load(open(a_p)), json.load(open(b_p))
ok = norm(a) == norm(b)
print(json.dumps({"check": "controls_pn", "code": 0 if ok else 6, "controls": [len(a), len(b)], "differ": [x for x, y in zip(norm(a), norm(b)) if x != y][:5]}))
sys.exit(0 if ok else 6)
