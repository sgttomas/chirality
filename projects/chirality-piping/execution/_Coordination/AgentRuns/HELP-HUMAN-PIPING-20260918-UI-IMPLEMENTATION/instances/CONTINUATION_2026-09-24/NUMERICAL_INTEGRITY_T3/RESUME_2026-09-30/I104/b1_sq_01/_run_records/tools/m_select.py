"""I104 SQ G5 -> R6a: D-7's M proposal from G5's in-build E_mov,max + R (the law test's I65_G5_PROFILE lines) and
TAV_W (the c = 3 run's summary): the smallest 256 MiB step M with E+R <= 0.9 M and a text-error budget
(0.9 M - (E+R)) / TAV_W >= 5 % in both modes, against the 12 GiB ceiling; with ADD §1's priced values beside it.
Also checks SF-1's premise: the c = 3 late-capture and ordinary-seed forms are exactly 3 x the c = 1 forms.
Usage: m_select.py <law log> <c3 summary> <c3 profile_tree> <c1 profile_tree>"""
import json, re, sys
log, s3, t3p, t1p = sys.argv[1:5]
E = {m: int(v) for m, v in re.findall(r"I65_G5_PROFILE mode=(\w+) max_without_R=\d+ E_mov_plus_R=(\d+)", open(log).read())}
TAVW = json.load(open(s3))["dense"]["TAV_W"]; assert TAVW == json.load(open(s3))["sparse"]["TAV_W"]
ADD = {"dense": 9_747_725_678, "sparse": 9_688_594_334}; ADD_TAVW = 4_189_696_338
STEP, CEIL, GiB = 256 * 2**20, 12 * 2**30, 2**30
def check(M):
    lim = M * 9 // 10
    return {m: {"E_plus_R": E[m], "fraction_of_M": round(E[m] / M, 4), "under_0.9M_by": lim - E[m], "text_error_budget": round((lim - E[m]) / TAVW, 4)} for m in E}
M = STEP
while not all(v["text_error_budget"] >= 0.05 for v in check(M).values()):
    M += STEP
out = {"G5_in_build": E, "TAV_W": TAVW, "ADD_1": ADD, "delta_vs_ADD_1": {m: E[m] - ADD[m] for m in E},
       "delta_share_of_ADD_TAV_W": {m: round((E[m] - ADD[m]) / ADD_TAVW, 4) for m in E},
       "smallest_M_for_0.9M_rule": max(-(-E[m] * 10 // 9) for m in E),
       "proposed_M": M, "proposed_M_GiB": M / GiB, "within_12GiB": M <= CEIL, "at_proposed_M": check(M),
       "at_step_below": {"M": M - STEP, "M_GiB": (M - STEP) / GiB, "modes": check(M - STEP)}, "at_12GiB": check(CEIL)}
t3, t1 = json.load(open(t3p)), json.load(open(t1p))
sf1 = {}
for f in ("T11_late_capture", "T11_ordinary_seed"):
    a, b = t1["forms"][f], t3["forms"][f]
    sf1[f] = {"c1": a, "c3": b, "c3_is_exactly_3x_c1": set(a) == set(b) and all(b[k] == 3 * a[k] for k in a)}
out["SF1_late_forms"] = sf1
print(json.dumps(out, indent=1))
