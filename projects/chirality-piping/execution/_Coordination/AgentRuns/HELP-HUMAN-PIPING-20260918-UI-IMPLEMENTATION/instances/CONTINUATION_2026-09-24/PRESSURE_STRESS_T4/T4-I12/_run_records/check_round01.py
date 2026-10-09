"""T4-I12 round 01: consumer-side check of the appended cases, and proof that the 18 frozen
round-0 cases, every round-0 top-level key and the four round-01 cases committed at
2e79cf469e are unchanged.

The FROZEN hashes are SHA-256 of json.dumps(obj, sort_keys=True, separators=(",", ":"),
ensure_ascii=False) for each round-0 case and top-level key, taken from
u3_reference_cases.json at commit a744c09021 (file sha256 46816c84...ff5cdf).

Usage: python -I check_round01.py <u3_reference_cases.json> [<frozen round-0 json>]
"""
import hashlib
import json
import sys
from decimal import Decimal, getcontext

getcontext().prec = 80
doc = json.load(open(sys.argv[1]))
N_OK, FAILS = 0, []


def ok(name, cond):
    global N_OK
    print(("ok   " if cond else "FAIL ") + name)
    if cond:
        N_OK += 1
    else:
        FAILS.append(name)


def canon(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


FROZEN_TOP = {
    "schema_version": "ff68c820863992725f3e5f65b7b4c2146cbd8e07c463fd835bad697dca3ef21c",
    "status": "a30001cc27aa7df6bbdbfa5bff6eb6ed61ad7db00fdc79200cd82012b3168f6d",
    "author": "70f5160246a4465af3c4c22bbb1ba656df5849e895a90dd863bef654ad837273",
    "basis": "1923a0df36bea072c017183806c9002e5d6a1afb478c3a9bd7ec0dae35122f43",
    "conventions": "82a10305c76c823dbb5df1f8d5864f3745987beba39c091d029b38d2d5de8ceb",
    "criteria": "d382967aca6f43d7440112cf0d81f9307eb999d285f9145cca0886bb3d772d22",
    "findings": "0c5632339f0f0a3ef14bfd7430362e6a25349450aceaee111a7054ad703823a7",
    "jr_comparison_summary": "a464ffc42f8d79c3009c9e41588a3104ba6296b6be99e1e5416ec96534c0ab77",
}
FROZEN_CASES = [
    ("U3-J1-LATERAL", "9a359cae65a82c9ea8d9bd7b7d059fab135139a767bfe0bb66f2f4bbcd88e3f3"),
    ("U3-J1-COMMON-ROTATION", "f9ab1d49cb11a208df87493f4b694454d11f445e554e0ea4859d76760f8ef8f0"),
    ("U3-J2-ROTATION", "012d8cd5b81562b5446ecd507fc4d2a260454bd023bcd3fd48cff15a09b0984d"),
    ("U3-J2-ROTATION-HELD", "7d2d7d1537191249443cfbab85e64cf2728b41cc4be49cb66329a108da4e94e2"),
    ("U3-REF-ENDMOMENT", "5d954e00e00905a8cff8ae8170540f5c87c9ec2f37fe71c52f93665d559e4806"),
    ("U3-SIX-COMPONENTS", "82f9f706dd8ac27ebac8709dfa3928890853daf84f12298baf09924f0e23681b"),
    ("U3-B-ORACLE", "18786dea94bf9af5781c065ad69c7067bd5a93830701b794c4a1de432784f8bb"),
    ("U3-GENERIC-SKEW-OFFSET-PRESTRESS", "4761c5063d5fb32d48675978f60ffe2c138acbc61eba910de85447878bcbd4b8"),
    ("U3-W4-LINK-RULE", "84aa3be5c16bf428dc30e1abb90db8ff38e71226844a48885df448940f5f79c2"),
    ("U3-FRAME-COVARIANCE", "62c3e38605803ec3564ae17a986eaf43221524accecb2689c51f79e0d45c8238"),
    ("U3-OFFSETS", "78601f492da277f7a6f7c190525ee0e965fee0c2204210797128653349574925"),
    ("U3-COUPLED-H-SCALE-PRELOAD", "a584678561d0c78358bd0d11af9bf7557bfd37ec50d20c7188c2573e00315cc6"),
    ("U3-PRELOAD-RELIEF", "86fdef33228df69bb66573902b0cabede027bdca4771d2f2576811d8157c0874"),
    ("U3-REVERSAL", "630ab4608eff28dd4c4a09aad5c6c5e4fb059c0a9086a4761233fa49608fca57"),
    ("U3-FINITE-ROTATION-NEGATIVE", "08ca970cac4590d058c649088b5358db2f805361af746b77fe170d6fd3274088"),
    ("U3-RAW-DIFFERENCE-NEGATIVE", "68b6dbd64807f6f3c99881acff7c756fcb4ddbf348c3c517e2116de075ce2124"),
    ("U3-SYS-DEMO-CONNECTOR-001", "42b36d2a9b5f58ac296022aa16bdbc9206c48481aa1e523d887eae7e6aa1a3f7"),
    ("U3-NI-FRICTION-FRAME", "2a159ac0e02d83b7888049c303a83f4be3e8edd38c1d27b250ed3fb0be4954c4"),
]
ROUND01_COMMITTED = [  # canonical sha256 of each case at commit 2e79cf469e (file sha256 42896cca...2d28c)
    ("U3-SYS-DEMO-CONNECTOR-002-LR1", "d1b0a2df8785296dcdd14901171bffd2fb033040dc72711b13d7cb68c6a751e4"),
    ("U3-SYS-LR1-REPLACED-SPAN-EIGENSTRAIN-REFUSAL", "206075c5265c1c9b04c2b8d5c2a31e8eedd9abd543b0d3e487f91487809b8cfa"),
    ("U3-SYS-REPLACED-SPAN-MATERIAL-CONTROL", "ac66b77bda38059f786c27df2746c56ce8918d3e8a50fa39cf894886395310bf"),
    ("U3-SYS-LR1-REPLACED-SPAN-STORED-UNAPPLIED-CONTROL", "4cbf1512fc6bbf945bd7a5454a98681dfa0a939ff49f9335657a5c3aabd80c96"),
]
APPENDED = ["U3-SYS-DEMO-CONNECTOR-002-LR1", "U3-SYS-LR1-REPLACED-SPAN-EIGENSTRAIN-REFUSAL", "U3-SYS-REPLACED-SPAN-MATERIAL-CONTROL",
            "U3-SYS-LR1-REPLACED-SPAN-STORED-UNAPPLIED-CONTROL", "U3-KD5-UTM-SKEW-OFFSET-COUPLED"]

# ---- 1. the frozen part is unchanged
ids = list(doc["cases"])
ok("case order: the 18 frozen cases keep indices 0-17", ids[:18] == [c for c, _ in FROZEN_CASES])
ok("case order: exactly the five round-01 cases are appended at indices 18-22", ids[18:] == APPENDED)
for k, (cid, h) in enumerate(FROZEN_CASES):
    ok(f"frozen case {k} {cid}: canonical sha256 unchanged", canon(doc["cases"][cid]) == h)
for k, (cid, h) in enumerate(ROUND01_COMMITTED):
    ok(f"committed round-01 case {18 + k} {cid}: canonical sha256 unchanged since 2e79cf469e", canon(doc["cases"][cid]) == h)
for key, h in FROZEN_TOP.items():
    ok(f"frozen top-level key {key}: canonical sha256 unchanged", canon(doc[key]) == h)
ok("top-level keys: round-0 keys plus round_01 only", list(doc) == list(FROZEN_TOP)[:8] + ["cases", "round_01"])
if len(sys.argv) > 2:
    fz = json.load(open(sys.argv[2]))
    ok("direct comparison with the supplied round-0 file: every frozen case equal", all(fz["cases"][c] == doc["cases"][c] for c, _ in FROZEN_CASES))

# ---- 2. the 0.4.0 form
c001 = doc["cases"]["U3-SYS-DEMO-CONNECTOR-001"]
c002 = doc["cases"]["U3-SYS-DEMO-CONNECTOR-002-LR1"]
m3 = c001["inputs"]["document_v3_0.3.0"]["model"]
m4 = c002["inputs"]["document_v3_0.4.0"]["model"]
ok("0.4.0: schema 0.4.0, same contract, nodes, pipes, supports, components and combinations as the 0.3.0 document",
   m4["schema_version"] == "0.4.0" and all(m4[k] == m3[k] for k in ("pressure_contract", "nodes", "pipe_segments", "supports", "components", "combinations")))
ok("0.4.0: materials equal the 0.3.0 materials without the thermal coefficient",
   m4["materials"] == [{k: v for k, v in mt.items() if k != "thermal_expansion_coefficient"} for mt in m3["materials"]])
pipes = [p["id"] for p in m4["pipe_segments"]]
pmat = {p["id"]: p["material"] for p in m4["pipe_segments"]}
refs = m4["reference_configurations"][0]["member_references"]
ok("0.4.0: one reference member per pipe, direct_strain_reference, fit none", sorted(r["pipe_ref"] for r in refs) == sorted(pipes)
   and all(r["basis"] == {"kind": "direct_strain_reference"} and r["fit"] == {"kind": "none"} for r in refs))
for case3, case4 in zip(m3["load_cases"], m4["load_cases"]):
    cid = case4["id"]
    st = case4["analysis_state"]
    ok(f"0.4.0 {cid}: primitives are the 0.3.0 primitives without the thermal primitive",
       case4["primitive_loads"] == [ld for ld in case3["primitive_loads"] if ld["category"] != "thermal"])
    ok(f"0.4.0 {cid}: every stored primitive listed once in load_sources with factor 1",
       [s["source_ref"] for s in st["load_sources"]] == [ld["id"] for ld in case4["primitive_loads"]] and all(s["factor"] == 1.0 for s in st["load_sources"]))
    ok(f"0.4.0 {cid}: every support active_model_device", [s["support_ref"] for s in st["support_states"]] == [s["id"] for s in m4["supports"]]
       and all(s["participation"] == {"kind": "active_model_device"} for s in st["support_states"]))
    es = {e["pipe_ref"]: e for e in st["element_states"]}
    ok(f"0.4.0 {cid}: one element state per pipe naming the pipe's own material", sorted(es) == sorted(pipes)
       and all(es[p]["material_selection"]["material_ref"] == pmat[p] and es[p]["material_selection"]["kind"] == "explicit_base_properties" for p in pipes))
    ok(f"0.4.0 {cid}: the replaced span P-130 is cold (unchanged_reference)", es["pipe:P-130"]["thermal_state"]["kind"] == "unchanged_reference")
    th3 = [ld for ld in case3["primitive_loads"] if ld["category"] == "thermal"]
    hot = {p for p in pipes if es[p]["thermal_state"]["kind"] != "unchanged_reference"}
    ok(f"0.4.0 {cid}: strained members are exactly the 0.3.0 thermal targets", hot == {ld["target"]["pipe"] for ld in th3})
    for ld in th3:
        t = es[ld["target"]["pipe"]]["thermal_state"]
        alpha3 = [mt for mt in m3["materials"] if mt["id"] == pmat[ld["target"]["pipe"]]][0]["thermal_expansion_coefficient"]
        ok(f"0.4.0 {cid}: {ld['target']['pipe']} constant_alpha_interval carries the 0.3.0 alpha and dT",
           t["kind"] == "constant_alpha_interval" and t["coefficient"] == alpha3 and t["temperature_change"]["value"] == ld["magnitude"]["value"]
           and t["coefficient_meaning"] == "engineering_interval")
    ok(f"0.4.0 {cid}: expected values identical to U3-SYS-DEMO-CONNECTOR-001", c002["expected"][cid] == c001["expected"][cid])
    # statics from the 0.4.0 document's load sources and the 0.4.0 frozen reactions
    nodes = {n["id"]: [Decimal(repr(n["position"][q])) for q in "xyz"] for n in m4["nodes"]}
    pend = {p["id"]: (p["from"], p["to"]) for p in m4["pipe_segments"]}
    snode = {s["id"]: s["node"] for s in m4["supports"]}
    axis = {"global_x": 0, "global_y": 1, "global_z": 2, "rotation_x": 3, "rotation_y": 4, "rotation_z": 5}
    Ft, Mt = [Decimal(0)] * 3, [Decimal(0)] * 3
    prim = {ld["id"]: ld for ld in case4["primitive_loads"]}

    def addF(x, fv):
        global Ft, Mt
        Ft = [a + b for a, b in zip(Ft, fv)]
        Mt = [a + b for a, b in zip(Mt, [x[1] * fv[2] - x[2] * fv[1], x[2] * fv[0] - x[0] * fv[2], x[0] * fv[1] - x[1] * fv[0]])]
    for s in st["load_sources"]:
        ld = prim[s["source_ref"]]
        val = Decimal(repr(ld["magnitude"]["value"])) * Decimal(repr(s["factor"]))
        ax = axis[ld["direction"]]
        if ld["target"]["type"] == "element":
            a, b = pend[ld["target"]["pipe"]]
            L = sum((p - q) ** 2 for p, q in zip(nodes[a], nodes[b])).sqrt()
            fv = [Decimal(0)] * 3
            fv[ax] = val * L
            addF([(p + q) / 2 for p, q in zip(nodes[a], nodes[b])], fv)
        elif ax < 3:
            fv = [Decimal(0)] * 3
            fv[ax] = val
            addF(nodes[ld["target"]["node"]], fv)
        else:
            Mt[ax - 3] += val
    for sid, rv in c002["expected"][cid]["reactions_support_on_pipe_global_Fx_Fy_Fz_Mx_My_Mz"].items():
        rv = [Decimal(x) for x in rv]
        addF(nodes[snode[sid]], rv[0:3])
        Mt = [a + b for a, b in zip(Mt, rv[3:6])]
    fl = Decimal(c002["expected"][cid]["zero_scale_floors"]["force_N"])
    ok(f"0.4.0 {cid}: load sources plus frozen reactions balance (force and moment, 1e-24 of the floor)",
       max(abs(x) for x in Ft) <= Decimal("1e-24") * fl and max(abs(x) for x in Mt) <= Decimal("1e-23") * fl)


# ---- 3. refusal variants
def strip(m):
    return json.loads(json.dumps(m))


ref = doc["cases"]["U3-SYS-LR1-REPLACED-SPAN-EIGENSTRAIN-REFUSAL"]
base4 = m4
for key, exp_eig, exp_cases in (("a_thermal_on_replaced_span", {"load:L-100": "3/20000", "load:L-200": "0", "load:L-300": "0"}, ["load:L-100"]),
                                ("b_fit_strain_on_replaced_span", {"load:L-100": "1/10000", "load:L-200": "1/10000", "load:L-300": "1/10000"}, ["load:L-100", "load:L-200", "load:L-300"]),
                                ("c_weight_on_replaced_span", {"load:L-100": "0", "load:L-200": "0", "load:L-300": "0"}, ["load:L-100"])):
    v = ref["expected"][key]
    mv_ = v["document_v3_0.4.0"]["model"]
    ok(f"refusal {key}: resolved P-130 eigenstrain per case as stated", v["resolved_eigenstrain_P130_by_case"] == exp_eig)
    ok(f"refusal {key}: code JOINT_REPLACED_SPAN_LOAD_UNOWNED, refused cases {exp_cases}, refs include C-150 and P-130",
       v["expected"]["blocking_code"] == "JOINT_REPLACED_SPAN_LOAD_UNOWNED" and v["expected"]["refused_cases"] == exp_cases
       and {"component:C-150", "pipe:P-130"} <= set(v["expected"]["affected_refs_include"]))
    # the variant differs from the 0.4.0 base only where it says
    a, b = strip(mv_), strip(base4)
    if key == "a_thermal_on_replaced_span":
        for c in a["load_cases"]:
            for e in c["analysis_state"]["element_states"]:
                if e["pipe_ref"] == "pipe:P-130" and c["id"] == "load:L-100":
                    ok("refusal a: P-130 in L-100 is constant_alpha_interval 1.2e-5 x 12.5", e["thermal_state"]["kind"] == "constant_alpha_interval"
                       and e["thermal_state"]["coefficient"]["value"] == 1.2e-05 and e["thermal_state"]["temperature_change"]["value"] == 12.5)
                    e["thermal_state"] = {"kind": "unchanged_reference", "provenance": e["thermal_state"]["provenance"]}
    elif key == "b_fit_strain_on_replaced_span":
        for r in a["reference_configurations"][0]["member_references"]:
            if r["pipe_ref"] == "pipe:P-130":
                ok("refusal b: P-130 fit is fit_strain 1e-4", r["fit"] == {"kind": "fit_strain", "strain": {"value": 0.0001, "unit": "1"}})
                r["fit"] = {"kind": "none"}
    else:
        c = a["load_cases"][0]
        extra = [ld for ld in c["primitive_loads"] if ld["target"].get("pipe") == "pipe:P-130"]
        ok("refusal c: one weight primitive on P-130, listed in load_sources", len(extra) == 1 and extra[0]["category"] == "weight"
           and any(s["source_ref"] == extra[0]["id"] for s in c["analysis_state"]["load_sources"]))
        c["primitive_loads"] = [ld for ld in c["primitive_loads"] if ld not in extra]
        c["analysis_state"]["load_sources"] = [s for s in c["analysis_state"]["load_sources"] if s["source_ref"] != extra[0]["id"]]
    ok(f"refusal {key}: the variant differs from the 0.4.0 base only in that change", a == b)
bz = ref["boundary_zero_strain"]["document_v3_0.4.0"]["model"]
ok("boundary: zero explicit strain on P-130, otherwise the 0.4.0 base", all(
    e["thermal_state"] == {"kind": "explicit_interval_strain", "strain": {"value": 0.0, "unit": "1"}, "interval_reference": "T4-I12 round 01 zero-strain boundary",
                           "provenance": e["thermal_state"]["provenance"]}
    for c in bz["load_cases"] for e in c["analysis_state"]["element_states"] if e["pipe_ref"] == "pipe:P-130"))
bzs = strip(bz)
for c in bzs["load_cases"]:
    for e in c["analysis_state"]["element_states"]:
        if e["pipe_ref"] == "pipe:P-130":
            e["thermal_state"] = {"kind": "unchanged_reference", "provenance": e["thermal_state"]["provenance"]}
ok("boundary: differs from the 0.4.0 base only in P-130's zero strain", bzs == strip(base4))
ok("boundary: admitted, every expected value equal to the cold case 002-LR1",
   "admitted" in ref["boundary_zero_strain"]["expected"] and ref["boundary_zero_strain"]["expected_values"] == c002["expected"])

# ---- 3b. stored but unapplied load on the replaced span (admitted control)
su = doc["cases"]["U3-SYS-LR1-REPLACED-SPAN-STORED-UNAPPLIED-CONTROL"]
ms = strip(su["inputs"]["document_v3_0.4.0"]["model"])
stored = [(c["id"], ld) for c in ms["load_cases"] for ld in c["primitive_loads"] if ld["target"].get("pipe") == "pipe:P-130"]
ok("stored-unapplied: exactly one primitive on P-130, stored in load:L-100", len(stored) == 1 and stored[0][0] == "load:L-100" and stored[0][1]["category"] == "weight")
ok("stored-unapplied: no case lists it in load_sources", all(s_["source_ref"] != stored[0][1]["id"] for c in ms["load_cases"] for s_ in c["analysis_state"]["load_sources"]))
ms["load_cases"][0]["primitive_loads"] = [ld for ld in ms["load_cases"][0]["primitive_loads"] if ld["id"] != stored[0][1]["id"]]
ok("stored-unapplied: differs from the 0.4.0 base only by that stored primitive", ms == strip(base4))
ok("stored-unapplied: every expected value equal to 002-LR1", su["expected"] == c002["expected"])
ok("stored-unapplied: no refusal expected", "JOINT_REPLACED_SPAN_LOAD_UNOWNED" in su["criterion"] and "no JOINT_REPLACED_SPAN_LOAD_UNOWNED" in su["criterion"])

# ---- 4. material control
ctl = doc["cases"]["U3-SYS-REPLACED-SPAN-MATERIAL-CONTROL"]
other = ctl["inputs"]["material_added"]
ok("control: the added material is E 1e11 Pa, nu 0.25, E/nu basis", other["elastic_modulus"]["value"] == 1e11 and other["poisson_ratio"]["value"] == 0.25
   and other["constitutive_basis"] == "homogeneous_isotropic_E_nu_v1")
for form, base_m in (("0.3.0", m3), ("0.4.0", m4)):
    cm = strip(ctl["inputs"][f"document_v3_{form}"]["model"])
    ok(f"control {form}: P-130 names the other material", [p["material"] for p in cm["pipe_segments"] if p["id"] == "pipe:P-130"] == [other["id"]])
    ok(f"control {form}: the other material is used by no other pipe", sum(p["material"] == other["id"] for p in cm["pipe_segments"]) == 1)
    for p in cm["pipe_segments"]:
        if p["id"] == "pipe:P-130":
            p["material"] = "material:invented-carbon-steel"
    cm["materials"] = [mt for mt in cm["materials"] if mt["id"] != other["id"]]
    if form == "0.4.0":
        for c in cm["load_cases"]:
            for e in c["analysis_state"]["element_states"]:
                if e["pipe_ref"] == "pipe:P-130":
                    ok(f"control 0.4.0 {c['id']}: P-130's element state selects the other material", e["material_selection"]["material_ref"] == other["id"])
                    e["material_selection"]["material_ref"] = "material:invented-carbon-steel"
    ok(f"control {form}: differs from its base only in P-130's material", cm == strip(base_m))
for cid, dsc in ctl["wrong_result_discriminators"].items():
    a, b = dsc["reactions_with_P130_E_2e11_nu_0.3"], dsc["reactions_with_P130_E_1e11_nu_0.25"]
    fl = Decimal(c001["expected"][cid]["zero_scale_floors"]["force_N"])
    moved = [f"{sid}.{['Fx', 'Fy', 'Fz', 'Mx', 'My', 'Mz'][k]}" for sid in a for k in range(6) if abs(Decimal(a[sid][k]) - Decimal(b[sid][k])) > Decimal("1e-6") * fl]
    ok(f"control {cid}: with P-130 retained its E/nu moves the reactions (discriminating), as listed", len(moved) > 0 and set(moved) <= set(dsc["moved_reaction_components"]))
    ok(f"control {cid}: and the parallel reactions differ from the reference", any(abs(Decimal(a[sid][k]) - Decimal(c001["expected"][cid]["reactions_support_on_pipe_global_Fx_Fy_Fz_Mx_My_Mz"][sid][k])) > Decimal("1e-6") * fl for sid in a for k in range(6)))

# ---- 5. K-D5 at ordinary and UTM coordinates (RV130 S-3), re-derived with the rigid-arm form
from fractions import Fraction as Fr


def P(x):
    return Fr(x)


def Pv(v):
    return [Fr(x) for x in v]


def Pm(m):
    return [[Fr(x) for x in r] for r in m]


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def sub(a, b):
    return [x - y for x, y in zip(a, b)]


def mv(m, v):
    return [sum(x * y for x, y in zip(r, v)) for r in m]


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def arm_q(d, ai_, aj_, r_, Q):
    """q from rigid arms to the common midpoint (a formulation distinct from the generator's B)."""
    h = [x / 2 for x in r_]
    bi, bj = add(ai_, h), sub(aj_, h)
    mi = add(d[0:3], cross(d[3:6], bi))
    mj = add(d[6:9], cross(d[9:12], bj))
    QT = [list(c) for c in zip(*Q)]
    return mv(QT, sub(mj, mi)) + mv(QT, sub(d[9:12], d[3:6]))


def arm_f(g, ai_, aj_, r_, Q):
    h = [x / 2 for x in r_]
    bi, bj = add(ai_, h), sub(aj_, h)
    Fv, Mv = mv(Q, g[0:3]), mv(Q, g[3:6])
    return [-x for x in Fv] + [-x for x in add(cross(bi, Fv), Mv)] + Fv + add(cross(bj, Fv), Mv)


def K_from(inp):
    Ls = Fr(inp["translation_scale_Ls_m"])
    u = [Fr(x) for x in inp["H_upper_triangle_21_N_m"]]
    H = [[Fr(0)] * 6 for _ in range(6)]
    k = 0
    for i in range(6):
        for j in range(i, 6):
            H[i][j] = H[j][i] = u[k]
            k += 1
    D = [Ls] * 3 + [Fr(1)] * 3
    return [[H[i][j] / (D[i] * D[j]) for j in range(6)] for i in range(6)]


def b64ok(e):
    v = float(e["binary64"])
    return Fr(v) == P(e["exact"]) and float.fromhex(e["hex"]) == v


def cr(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


kd = doc["cases"]["U3-KD5-UTM-SKEW-OFFSET-COUPLED"]
sh = kd["inputs"]["shared"]
ok("KD5: every shared input is an exact binary64 value (round-trip string, hex and rational agree)",
   all(b64ok(e) for key in ("a_i_global", "a_j_global", "q_ref", "d") for e in sh[key]) and all(b64ok(e) for row in sh["Q_row_major_columns_are_axes"] for e in row))
ai = [P(e["exact"]) for e in sh["a_i_global"]]
aj = [P(e["exact"]) for e in sh["a_j_global"]]
Qk = [[P(e["exact"]) for e in row] for row in sh["Q_row_major_columns_are_axes"]]
ok("KD5: Q entries are the binary64 roundings of (1,2,2)/3, (2,1,-2)/3, (-2,2,-1)/3 as columns",
   Qk == [[Fr(float(Fr(n, 3))) for n in row] for row in ((1, 2, -2), (2, 1, 2), (2, -2, -1))])
ok("KD5: x offsets have binary64 tails finer than 2^-30", all((x * 2 ** 30).denominator != 1 for x in (ai[0], aj[0])))
ok("KD5: offsets nonzero", any(x != 0 for x in ai) and any(x != 0 for x in aj))
Kk = K_from(sh)
ok("KD5: K coupled (nonzero off-diagonal) and recorded consistently", any(Kk[i][j] != 0 for i in range(6) for j in range(6) if i != j) and Kk == Pm(sh["K_physical"]))
exp = kd["expected"]["identical_at_every_location"]
qref = [P(e["exact"]) for e in sh["q_ref"]]
dd = [P(e["exact"]) for e in sh["d"]]
for tag, loc in kd["inputs"]["locations"].items():
    ok(f"KD5 {tag}: node coordinates exact binary64", all(b64ok(e) for e in loc["x_i"] + loc["x_j"]))
    xi = [P(e["exact"]) for e in loc["x_i"]]
    xj = [P(e["exact"]) for e in loc["x_j"]]
    ok(f"KD5 {tag}: x_j,x - x_i,x = 1.3125 exactly and X0 as stated", xj[0] - xi[0] == Fr(21, 16) and xi[0] == Fr(float(loc["X0_m"])) + Fr(1, 2))
    r = add(sub(xj, xi), sub(aj, ai))
    ok(f"KD5 {tag}: r = (x_j - x_i) + (a_j - a_i) equals the recorded r and is parallel to (1, 2, 2)", r == Pv(sh["r_exact"]) and cross(r, [1, 2, 2]) == [0, 0, 0])
    B = Pm(exp["B"])
    allcols = True
    for k in range(12):
        e = [Fr(0)] * 12
        e[k] = Fr(1)
        allcols &= arm_q(e, ai, aj, r, Qk) == [B[i][k] for i in range(6)]
    ok(f"KD5 {tag}: B (all 12 columns) from the rigid-arm form with the binary64 Q", allcols)
    ok(f"KD5 {tag}: Ke = B^T K B", Pm(exp["Ke"]) == [[sum(B[a][i] * Kk[a][b] * B[b][j] for a in range(6) for b in range(6)) for j in range(12)] for i in range(12)])
    q = arm_q(dd, ai, aj, r, Qk)
    g = mv(Kk, sub(q, qref))
    ok(f"KD5 {tag}: q and g", q == Pv(exp["q"]["exact"]) and g == Pv(exp["g"]["exact"]))
    f = arm_f(g, ai, aj, r, Qk)
    ea = exp["end_actions_node_on_element"]
    ok(f"KD5 {tag}: end actions (arm transpose)", f == Pv(ea["Fi"]["exact"]) + Pv(ea["Mi"]["exact"]) + Pv(ea["Fj"]["exact"]) + Pv(ea["Mj"]["exact"]))
    ms = add(add(add(cr(xi, f[0:3]), f[3:6]), cr(xj, f[6:9])), f[9:12])
    ok(f"KD5 {tag}: end actions balance about the origin at this location", add(f[0:3], f[6:9]) == [0, 0, 0] and ms == [0, 0, 0])
    ill = loc["binary64_formation_illustration"]
    if tag != "ORDINARY":
        ok(f"KD5 {tag}: illustration shows the absolute form's r defect above 1e-12 and the difference form's below 1e-15",
           float(ill["r_absolute_form_rel_error"]) > 1e-12 and float(ill["r_difference_form_rel_error"]) < 1e-15)
pv = kd["expected"]["perturbed_variant"]
Ke = Pm(exp["Ke"])
kmax = max(abs(x) for row in Ke for x in row)
ok("KD5 perturbed: delta = 2^-20 max|Ke|, on the largest diagonal entry", P(pv["delta_exact"]) == kmax / 2 ** 20 and P(pv["max_abs_Ke_exact"]) == kmax
   and max(abs(Ke[k][k]) for k in range(12)) == P(pv["Ke_kk_exact"]))
ok("KD5 perturbed: delta exceeds the absolute-form Ke defect at UTM by more than 1000x",
   2 ** -20 > 1000 * float(kd["inputs"]["locations"]["X7P3E6"]["binary64_formation_illustration"]["Ke_absolute_form_max_dev_over_max_Ke"]))

print(f"round-01 checks: {N_OK} pass, {len(FAILS)} fail")
for f_ in FAILS:
    print("FAIL:", f_)
print("PASS" if not FAILS else "FAIL")
sys.exit(1 if FAILS else 0)
