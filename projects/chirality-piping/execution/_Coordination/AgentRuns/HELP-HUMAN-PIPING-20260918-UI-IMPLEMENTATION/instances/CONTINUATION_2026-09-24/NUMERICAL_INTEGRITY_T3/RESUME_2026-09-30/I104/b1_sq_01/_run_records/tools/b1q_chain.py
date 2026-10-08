"""[I104 SQ copy of I82 b1_mc_chain.py: the emulated rebinds and edges removed; otherwise unchanged]
I82 B1-S: the multi-case (c, a, l, L) variant of I65's cap-priced chain, made in a scratch copy.

Input: a copy of u4_g7_06's chain whose line-keyed rules are mapped to the code basis (b1_text_base.sh
makes it, WT/scratch/i82_b1_study/rr). Output: a patched copy (argv[2]). No maintained file and no
record of I65's is changed. Every textual patch must match exactly once, or this script fails.

New cap variables (G4_CAPS keys; g3lib.g4_caps derives the rest):
  c  requested load cases (the cap C)          a  attempted cases |A| <= c (default c, the worst case)
  l  loads per case (unchanged key)            L  total loads, sum_i l_i <= min(L, c*l) (default c*l)
  derived: cases = c, att = a, Pall = c * P_final (every row of the c-case envelope).

Scope classification applied (STUDY.md section 2 states each with its reason):
  per invocation       model/raw/request-level owners, the one basis (D1.5), the one CaseBatchCall and
                       group (C2 section 4), the reader's statics, R, the helper, the precommit invocation;
  per requested case   ordinary solve owners (CasePrefix, typed core, W2, observation, recovery, old-case
                       staging, preview rewrite and copy, T07), ordinary seeds and observations (T11.2-T11.6),
                       receipt `cases[]` and `ordinary_attempts[]`, envelope rows (c*P) and preview trees;
  per attempted case   T12-T15 (preparation, native, proof, trace), receipt run/selection/source/attempt
                       members, the N1 notice, the selected diagnostics and recovery_method deltas.
The I65 method is kept: every owner of a phase is summed as if live (no new liveness credit), so
scaling a per-case owner by c (or a) is the method's own upper bound.
Usage: python3 b1_mc_chain.py <base chain dir> <out dir>
"""
import json, os, shutil, sys

src, dst = sys.argv[1:3]
if os.path.exists(dst):
    shutil.rmtree(dst)
shutil.copytree(src, dst)
LOG = []


def patch(fname, old, new, count=1):
    p = os.path.join(dst, fname)
    t = open(p).read()
    k = t.count(old)
    if k != count:
        raise SystemExit(f"PATCH FAILED {fname}: expected {count} match(es), found {k}: {old[:80]!r}")
    open(p, "w").write(t.replace(old, new))
    LOG.append((fname, old[:70].replace("\n", " "), k))


# ---------------------------------------------------------------- g3lib: the new cap variables
patch("g3lib.py", '''    c.update(o)
    n, m, g, s_, r, l = c["n"], c["m"], c["g"], c["s"], c["r"], c["l"]''',
      '''    c.update(o)
    # I82 B1-S: requested cases c, attempted cases a <= c, total loads L <= c*l
    c.setdefault("c", 1); c.setdefault("a", c["c"]); c.setdefault("L", c["c"] * c["l"])
    c["L"] = min(c["L"], c["c"] * c["l"]); assert 1 <= c["a"] <= c["c"]
    c["cases"], c["att"] = c["c"], c["a"]
    n, m, g, s_, r, l = c["n"], c["m"], c["g"], c["s"], c["r"], c["l"]''')
patch("g3lib.py", '''             Q=7 * n + 30 * m + s_ + min(N, r) + 2 * g)
    return c''', '''             Q=7 * n + 30 * m + s_ + min(N, r) + 2 * g)
    c.update(Pall=c["c"] * c["P"])                     # I82: every row of the c-case envelope
    return c''')

# ---------------------------------------------------------------- TEXT: counts and multiplicities
patch("text_budget.py", '''    for _k in ("n", "m", "g", "s", "k", "r", "l", "N", "F", "Z", "C", "P", "R0", "E", "H", "Q"):''',
      '''    for _k in ("n", "m", "g", "s", "k", "r", "l", "N", "F", "Z", "C", "P", "R0", "E", "H", "Q", "cases", "att", "L", "Pall"):''')

lbp = os.path.join(dst, "loop_bounds.g4.json")
LB = json.load(open(lbp))
LB["counts"]["caps"].update({"att": 1, "L": 192, "Pall": LB["counts"]["caps"]["P"]})
LB["counts"]["milestone"].update({"att": 1, "L": LB["counts"]["milestone"]["l"], "Pall": LB["counts"]["milestone"]["P"]})
# I104 SQ: I82's 22 emulated loop-rule rebinds and 22 emulated edge multiplicities are NOT applied here.
# B1's real loops get real rules (i104_rules.py, applied after this script), with I82's list as the checklist.
rebind = []; per_call = []
json.dump(LB, open(lbp, "w"), indent=1)

# the diagnostics fixpoint starts above c x the D1 start and may iterate longer; convergence is reported
patch("sens.py", '''D = 25_544
for _ in range(4):                                   # the diagnostics fixpoint (loops over a diagnostics vector use D)
    d_new = tb("", D)["D_diagnostics"]
    if d_new == D:
        break
    D = d_new''', '''D = 25_544 * json.loads(caps).get("c", 1)          # I82: start above the c-case fixpoint
D_converged = False
for _ in range(12):                                  # the diagnostics fixpoint (loops over a diagnostics vector use D)
    d_new = tb("", D)["D_diagnostics"]
    if d_new == D:
        D_converged = True
        break
    D = d_new''')
patch("sens.py", '''summary = {"caps": json.loads(caps), "eps": int(eps), "text_complete": complete, "D": D, "D_env": txt["D_env"],''',
      '''summary = {"caps": json.loads(caps), "eps": int(eps), "text_complete": complete, "D": D, "D_converged": D_converged, "D_env": txt["D_env"],''')

# ---------------------------------------------------------------- ordinary_caps (O_base)
patch("ordinary_caps.py", '''ID = __import__("g3lib").g4_caps()["ident"] if which == "caps" else 128''',
      '''ID = __import__("g3lib").g4_caps()["ident"] if which == "caps" else 128
_mc = __import__("g3lib").g4_caps()
CC, LL = (_mc["c"], _mc["L"]) if which == "caps" else (1, l)   # I82: requested cases, total loads
PA = CC * P                                                   # I82: rows of the c-case envelope''')
patch("ordinary_caps.py", '''strings = (mats * (7 + pts * 7) + 6 + 2 * n + 12 * m + 6 * g + r + 2 + 7 * l) if which == "caps" else 0''',
      '''strings = (mats * (7 + pts * 7) + 6 + 2 * n + 12 * m + 6 * g + r + 2 * CC + 7 * LL) if which == "caps" else 0''')
patch("ordinary_caps.py", '''+ Xc("PreviewLoadCase", 1)
     + Xc("PrimitiveLoadInput", l)''', '''+ Xc("PreviewLoadCase", CC)
     + Xc("PrimitiveLoadInput", LL)''')
patch("ordinary_caps.py", '''    (Xc("ResultItem", P) + tx("row") * P) * 2 + X({"Node(String,BTreeMap)": P}) + X({"Node(String,ResultItem)": P})
    + HashReq("(String,String)", P) + B(2 * P * ID))''', '''    (Xc("ResultItem", PA) + tx("row") * PA) * 2 + X({"Node(String,BTreeMap)": PA}) + X({"Node(String,ResultItem)": PA})
    + HashReq("(String,String)", PA) + B(2 * PA * ID))''')
PER_CASE_FAMILIES = [
    "Primitive loads and application", "AssembledForce, nodal family",
    "Sparse reduction (+ caller prescribed, observation force)", "Formation-guard Bodies (build + resident)",
    "Legacy profile observation", "Straight member recovery (+ stress supplement)",
    "Formation-guard late maps and RecoveryFinding", "Ordinary scalar maximum (one helper at a time)",
    "Source row qualification", "Existing ordinary/failed source case (FinalizedSourceBlockCase::ordinary)",
    "Preview rewrite", "Preview tree final copy (envelope evidence)", "T07 generic deep legacy-exact (RESIDUALS_G3 T07)"]
patch("ordinary_caps.py", '''out = {"which": which, "counts": dict(n=n, m=m, g=g, s=sp, r=r, l=l, N=N, F=F, k=k, C=C, Z=Z, Zf=Zf, E=E,''',
      '''PER_CASE_FAMILIES = ''' + repr(PER_CASE_FAMILIES) + '''
for _f in PER_CASE_FAMILIES:                       # I82: one owner set per requested case, all counted live
    assert _f in fam, _f
    fam[_f] = fam[_f] * CC
out = {"which": which, "counts": dict(n=n, m=m, g=g, s=sp, r=r, l=l, N=N, F=F, k=k, C=C, Z=Z, Zf=Zf, E=E,''')
patch("ordinary_caps.py", '''    rows.update({f"Typed core [{mode}]: {k_}": v for k_, v in core.items()})
    rows["W2 (two evaluations + unscale + return tail + direction error)"] = w2_req
    if mode == "dense":
        rows["Dense parity tail (DenseScrutiny, formed, no W2)"] = dense_parity''',
      '''    rows.update({f"Typed core [{mode}]: {k_}": v * CC for k_, v in core.items()})
    rows["W2 (two evaluations + unscale + return tail + direction error)"] = w2_req * CC
    if mode == "dense":
        rows["Dense parity tail (DenseScrutiny, formed, no W2)"] = dense_parity * CC''')

# ---------------------------------------------------------------- producer_caps (T11-T15)
patch("producer_caps.py", '''    _c = _gc(); n, m, sp, r, l, g = _c["n"], _c["m"], _c["s"], _c["r"], _c["l"], _c["g"]''',
      '''    _c = _gc(); n, m, sp, r, l, g = _c["n"], _c["m"], _c["s"], _c["r"], _c["l"], _c["g"]
    CC, AA = _c["c"], _c["a"]                       # I82: requested and attempted cases''')
patch("producer_caps.py", '''    n, m, sp, r, l, g = 2, 1, 3, 6, 3, 4
d = 0''', '''    n, m, sp, r, l, g = 2, 1, 3, 6, 3, 4
    CC, AA = 1, 1
d = 0''')
patch("producer_caps.py", '''out = {"which": which, "counts": dict(n=n, m=m, s=sp, r=r, l=l, g=g, N=N, F=F, k=k, Q=Q, U=U, P=P, Zu=Zu, H=Hp,''',
      '''# I82: T11.2-T11.6 are held per requested case by the one ProductCapture (T-2); T12-T15 per attempted
# case, every Run and frozen candidate live until staging (T-8, T-9, T-11). Scaled before the rows are
# written, so the rows, the terms and the gate forms (T11.4, T11.5) all carry the scope.
for k_ in list(rows):
    p_ = k_.split(" ")[0]
    if p_ in ("T11.2", "T11.3", "T11.4", "T11.5", "T11.6"):
        rows[k_] = rows[k_] * CC
    elif p_.split(".")[0] in ("T12", "T13", "T14", "T15"):
        rows[k_] = rows[k_] * AA
out = {"which": which, "counts": dict(n=n, m=m, s=sp, r=r, l=l, g=g, N=N, F=F, k=k, Q=Q, U=U, P=P, Zu=Zu, H=Hp,''')

# ---------------------------------------------------------------- t25_g4 (branch X, T25)
patch("t25_g4.py", '''    n, m, g, sp, r, l = (CAPS.get(k_, v_) for k_, v_ in (("n", 32), ("m", 32), ("g", 32), ("s", 32), ("r", 192), ("l", 192)))
else:
    n, m, g, sp, r, l = 2, 1, 4, 3, 6, 3
N = 6 * n; F = N; k = min(N, r); C = 144 * m + sp''', '''    n, m, g, sp, r, l = (CAPS.get(k_, v_) for k_, v_ in (("n", 32), ("m", 32), ("g", 32), ("s", 32), ("r", 192), ("l", 192)))
else:
    n, m, g, sp, r, l = 2, 1, 4, 3, 6, 3
CC = CAPS.get("c", 1) if which == "caps" else 1      # I82: requested cases (every one may be exact-selected)
LL = min(CAPS.get("L", CC * l), CC * l) if which == "caps" else l
N = 6 * n; F = N; k = min(N, r); C = 144 * m + sp''')
patch("t25_g4.py", '''strings_typed = 8 * (7 + 16 * 7) + 6 + 2 * n + 12 * m + 6 * g + r + 2 + 7 * l''',
      '''strings_typed = 8 * (7 + 16 * 7) + 6 + 2 * n + 12 * m + 6 * g + r + 2 * CC + 7 * LL''')
patch("t25_g4.py", '''+ Xc("PreviewLoadCase", 1) + Xc("PrimitiveLoadInput", l)''', '''+ Xc("PreviewLoadCase", CC) + Xc("PrimitiveLoadInput", LL)''')
patch("t25_g4.py", '''env_vf = (VF(arr=P + 4 * P, obj=3 * P, ent=15 * P, strb=P * ROW, keyb=15 * P * 24, nums=P, depth=4)
          + VF(arr=D + 4 * D + 3 * (1 + l), obj=D, ent=6 * D, strb=DIAG, keyb=6 * D * 16, depth=4)''',
      '''PA = CC * P                                  # I82: rows of the c-case envelope
env_vf = (VF(arr=PA + 4 * PA, obj=3 * PA, ent=15 * PA, strb=PA * ROW, keyb=15 * PA * 24, nums=PA, depth=4)
          + VF(arr=D + 4 * D + 3 * (CC + LL), obj=D, ent=6 * D, strb=DIAG, keyb=6 * D * 16, depth=4)''')
patch("t25_g4.py", '''               keyb=(9 + 15 * m + 2 * g) * 40, nums=10 * m, depth=6)
          + VF(arr=64, obj=24, ent=160, strb=24 * 1024, keyb=160 * 40, nums=60, depth=5))
publication = env_vf.tree()''', '''               keyb=(9 + 15 * m + 2 * g) * 40, nums=10 * m, depth=6).scale(CC)
          + VF(arr=64, obj=24, ent=160, strb=24 * 1024, keyb=160 * 40, nums=60, depth=5).scale(CC))
publication = env_vf.tree()''')
patch("t25_g4.py", '''rows["T25.8 ids set, accounted set, observations"] = (X({"Node(&str,())": (P + D) // 5 + 1}) + X({"Node(String,())": R // 5 + 1})
                                                      + B(R * RID) + Xc("String", P) + B(P * RID))''',
      '''rows["T25.8 ids set, accounted set, observations"] = (X({"Node(&str,())": (PA + D) // 5 + 1}) + X({"Node(String,())": PA // 5 + 1})
                                                      + B(PA * RID) + Xc("String", PA) + B(PA * RID))''')
patch("t25_g4.py", '''rows["T25.9 per case: actual rows clone + serialized(actual) + wire entry"] = (
    Xc("ResultItem", P) + B(P * ROW) + rowjson + case_wire_vf.tree())
body_vf = case_wire_vf + VF(arr=P, obj=4, ent=20, strb=P * RID + 512, keyb=20 * 32, nums=4)''',
      '''rows["T25.9 per case: actual rows clone + serialized(actual) + wire entry"] = (
    Xc("ResultItem", P) + B(P * ROW) + rowjson + case_wire_vf.tree()) * CC
body_vf = case_wire_vf.scale(CC) + VF(arr=PA, obj=4, ent=20, strb=PA * RID + 512, keyb=20 * 32, nums=4)''')
patch("t25_g4.py", '''out["stage_forms"] = {"carried_case": dict(carried_case),''',
      '''out["stage_forms"] = {"carried_case": dict(carried_case * CC),''')   # I82: every case's carried outputs live at the finalize

# ---------------------------------------------------------------- g4_caps (T16-T19, envelope, receipt)
patch("g4_caps.py", '''Q = 7 * n + 30 * m + sp + k + 2 * g
ID, RID, KB''', '''Q = 7 * n + 30 * m + sp + k + 2 * g
CC = CAPS.get("c", 1) if which == "caps" else 1   # I82: requested cases
AA = CAPS.get("a", CC) if which == "caps" else 1  # I82: attempted cases (|A| <= c)
LL = min(CAPS.get("L", CC * l), CC * l) if which == "caps" else l
PA = CC * P                                       # I82: rows of the c-case envelope
ID, RID, KB''')
patch("g4_caps.py", '''ENV = (VF(arr=P + 4 * P, obj=3 * P, ent=15 * P, strb=P * ROW, keyb=15 * P * 24, nums=P, depth=4)
       + VF(arr=DENV + 4 * DENV + 3 * (1 + l),''', '''ENV = (VF(arr=PA + 4 * PA, obj=3 * PA, ent=15 * PA, strb=PA * ROW, keyb=15 * PA * 24, nums=PA, depth=4)
       + VF(arr=DENV + 4 * DENV + 3 * (CC + LL),''')
patch("g4_caps.py", '''            nums=10 * m, depth=6)
       + VF(arr=64, obj=24, ent=160, strb=24 * 1024, keyb=160 * 40, nums=60, depth=5))''',
      '''            nums=10 * m, depth=6).scale(CC)
       + VF(arr=64, obj=24, ent=160, strb=24 * 1024, keyb=160 * 40, nums=60, depth=5).scale(CC))''')
patch("g4_caps.py", '''SUCC_DELTA = (VF(ent=P, strb=P * 41, keyb=P * 15)
              + VF(arr=2, obj=1, ent=6, strb=(30 + ID + 9) + 26 + 4 + 300 + 20 + ID, keyb=6 * 16)''',
      '''SUCC_DELTA = (VF(ent=PA, strb=PA * 41, keyb=PA * 15)
              + VF(arr=2, obj=1, ent=6, strb=(30 + ID + 9) + 26 + 4 + 300 + 20 + ID, keyb=6 * 16).scale(AA)''')
patch("g4_caps.py", '''          + rec(m, slots=1, obj=2, ent=13, strb=TOK + 10 * BITS, nums=1))             # section_terms''',
      '''          + rec(m, slots=1, obj=2, ent=13, strb=TOK + 10 * BITS, nums=1))             # section_terms
SOURCE = SOURCE.scale(AA)                            # I82: one prepared CaseSource per attempted case''')
patch("g4_caps.py", '''CASE = rec(1, obj=4, ent=16, strb=4 * TOK + ID + SHA, nums=4) + RUN + SELECTION''',
      '''CASE = rec(CC, obj=4, ent=16, strb=4 * TOK + ID + SHA, nums=4) + RUN.scale(AA) + SELECTION.scale(AA)   # I82''')
patch("g4_caps.py", '''ATTEMPT = rec(1, obj=8, ent=40, strb=4 * TOK + 10 * TOK, nums=20) + PREPARATION + OPERATIONAL + PROOF''',
      '''ATTEMPT = rec(1, obj=8, ent=40, strb=4 * TOK + 10 * TOK, nums=20) + PREPARATION + OPERATIONAL + PROOF
ATTEMPT = ATTEMPT.scale(AA)                          # I82: product_attempts[], one per attempted case''')
patch("g4_caps.py", '''ORDINARY = rec(1, obj=6, ent=20, strb=2 * TOK + ID + 4 * L_DIAGID) + VF(arr=DENV, strb=DENV * L_DIAGID)  # diagnostic_refs''',
      '''ORDINARY = rec(1, obj=6, ent=20, strb=2 * TOK + ID + 4 * L_DIAGID) + VF(arr=DENV, strb=DENV * L_DIAGID)  # diagnostic_refs
ORDINARY = ORDINARY.scale(CC)                        # I82: ordinary_attempts[], one per requested case''')
patch("g4_caps.py", '''CALLS = rec(1, slots=4, obj=3, ent=11, strb=2 * TOK, nums=6) + rec(1, slots=2, obj=2, ent=7, strb=SHA + TOK, nums=4)''',
      '''CALLS = rec(1, slots=4 * AA, obj=3, ent=11, strb=2 * TOK, nums=6) + rec(1, slots=2 * AA, obj=2, ent=7, strb=SHA + TOK, nums=4)''')
patch("g4_caps.py", '''STAGED = (s("MechanicsEnvelope") + Xc("ResultItem", P) + B(P * ROW) + Xc("Diagnostic", DENV) + B(DIAGENV)
          + PREVIEW_T + B(64 * 1024)
          + s("String") * (4 * P))''', '''STAGED = (s("MechanicsEnvelope") + Xc("ResultItem", PA) + B(PA * ROW) + Xc("Diagnostic", DENV) + B(DIAGENV)
          + PREVIEW_T * CC + B(64 * 1024)
          + s("String") * (4 * PA))''')
patch("g4_caps.py", '''LOCALS16 = (s("PreparedAttemptView") + B(8 * (4 * m + P + 64))                       # the typed trace view
            + Xc("RowBinding", P) + HashReq("(&str,&T)", P) + B(P * RID)              # bind_rows
            + s("String") * pushcap(P) + B(P * RID) + Xc("ProductRecipe", P))''',
      '''LOCALS16 = (s("PreparedAttemptView") + B(8 * (4 * m + PA + 64))                     # the typed trace view
            + Xc("RowBinding", PA) + HashReq("(&str,&T)", PA) + B(PA * RID)           # bind_rows
            + s("String") * pushcap(PA) + B(PA * RID) + Xc("ProductRecipe", PA))''')
patch("g4_caps.py", '''THIRD = RUN.tree() + SELECTION.tree()''', '''THIRD = RUN.scale(AA).tree() + SELECTION.scale(AA).tree()   # I82: every case_v json! copy''')
patch("g4_caps.py", '''SETS = (X({"Node(&str,())": tree_nodes(P) + 2 * tree_nodes(DENV) + tree_nodes(n + m + g)})   # rowids, diagnostic ids x2, model ids
        + HashReq("(&str,&Value)", P) * 3 + HashReq("&str", m + g) * 8 + B(8 * 3 * P)      # preview evidence maps and vectors
        + Xc("RowClassification", pushcap(P)) + B(P * (2 * ID + 64))                       # classifications (+ basis_ref clones)''',
      '''SETS = (X({"Node(&str,())": tree_nodes(PA) + 2 * tree_nodes(DENV) + tree_nodes(n + m + g)})   # rowids, diagnostic ids x2, model ids
        + HashReq("(&str,&Value)", PA) * 3 + HashReq("&str", m + g) * 8 + B(8 * 3 * PA)    # preview evidence maps and vectors
        + Xc("RowClassification", pushcap(PA)) + B(PA * (2 * ID + 64))                     # classifications (+ basis_ref clones)''')
patch("g4_caps.py", '''        + s("&Value") * (8 * P) + B(8 * 4 * n)                                             # rows_for vectors, extents, raw
        + X({"Node(String,Value)": P}))''', '''        + s("&Value") * (8 * PA) + B(8 * 4 * n)                                            # rows_for vectors, extents, raw
        + X({"Node(String,Value)": PA}))''')
patch("g4_caps.py", '''G5C = VF(arr=2 * P, obj=P, ent=2 * P, strb=P * (RID + BITS), keyb=P * 2 * 10).tree() * 2''',
      '''G5C = VF(arr=2 * PA, obj=PA, ent=2 * PA, strb=PA * (RID + BITS), keyb=PA * 2 * 10).tree() * 2''')
patch("g4_caps.py", '''G8_VALUES = SOURCE.tree() * 2 + VF(arr=Q, obj=3 * Q, ent=11 * Q, strb=3 * TOK * Q, keyb=11 * Q * KB).tree() * 2
G8_BYTES = B(2 * pushcap(36_742 + 4_986, 8) + 4 * 16 * m)''',
      '''G8_VALUES = SOURCE.tree() * 2 + VF(arr=Q, obj=3 * Q, ent=11 * Q, strb=3 * TOK * Q, keyb=11 * Q * KB).scale(AA).tree() * 2
G8_BYTES = B(AA * 2 * pushcap(36_742 + 4_986, 8) + 4 * 16 * m)''')
patch("g4_caps.py", '''T17 = T17v + Xc("Validation", 1) + Xc("RowClassification", pushcap(P))''',
      '''T17 = T17v + Xc("Validation", 1) + Xc("RowClassification", pushcap(PA))''')
patch("g4_caps.py", '''form("T17_output", Xc("Validation", 1) + Xc("RowClassification", pushcap(P)))''',
      '''form("T17_output", Xc("Validation", 1) + Xc("RowClassification", pushcap(PA)))''')
patch("g4_caps.py", '''NOTICE = B(2 * (30 + ID + 12) + 30 + 4 + 196 + 20 + ID) + s("String") + s("Diagnostic")''',
      '''NOTICE = (B(2 * (30 + ID + 12) + 30 + 4 + 196 + 20 + ID) + s("String") + s("Diagnostic")) * AA   # I82: one per case in A (T-5)''')

json.dump({"patches": LOG, "loop_rebinds": rebind, "edge_per_call_added": per_call,
           "per_case_ordinary_families": PER_CASE_FAMILIES}, open(os.path.join(dst, "B1Q_CHAIN_PATCHES.json"), "w"), indent=1)
print(json.dumps({"patches": len(LOG), "loop_rebinds": len(rebind), "edge_per_call_added": len(per_call)}))
