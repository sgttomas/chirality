"""I100 B1 SC: the 07n records script, step 1 (the draft).

Appends 07n's bases and entries to the shared corpus (07m), writing a DRAFT: every new entry sits in
`mutations` with a placeholder expectation and its design note, so that the three readers' census
harnesses (which read no expectation) can run it. Step 2 (`fix_07n.py`) sets each expectation from the
three readers' agreement and moves admitted entries to `must_pass`.

Usage: gen_07n.py <P root (scratch merge)> <RV113 probes_ts1.json> <RV113 probes_r2x.json> <PP dump dir> <out draft.json> <out plan.json>

Bases appended (each a D-U6-5 copy or a records-script derivation, resealed by the 07e format rule):
- w_c2_{mode}: I85's pinned W-C2 successors (fixtures committed at I3);
- d38_beside_selected: derived from w_c2_sparse_interactive (DESIGN_v2 §2): case C rewritten to (4b);
- cause_milestone_reversed_{mode}, sf2_c_b_a_{mode}, sf2_a_a2_{mode}: I85's pinned successors (PP
  `retained_facade_tests.rs`, REVERSED_PINNED, CBA_PINNED, AA2_PINNED), dumped from PP's own tests
  after their pin assertions held.
Entries: the D38, F-1 and not_required entries written here; the rest are RV113's probes, verbatim.
"""
import copy
import hashlib
import json
import sys
from pathlib import Path

P, PROBES, PROBES_R2X, DUMP, OUT, PLAN = sys.argv[1:7]
P = Path(P)
sys.path.insert(0, str(P))
from core.analysis_runs import retained_precision as rp  # noqa: E402

CORPUS = Path(__file__).resolve().parents[1] / "inputs/c07m.json"  # 07m, from git (52d83da275)
raw07m = CORPUS.read_bytes()
assert hashlib.sha256(raw07m).hexdigest() == "c21112fdbfad37dd4832c8dd64d066e1809dd70dce6c89cb920d1d6dd3d46807", "07m"
corpus = json.loads(raw07m)
assert (len(corpus["cases"]), len(corpus["mutations"]), len(corpus["must_pass"])) == (17, 294, 28)
B = ["retained_precision", "body"]
MODES = ["sparse_interactive", "dense_scrutiny"]


def s(path, value):
    return {"path": path, "op": "set", "value": value}


def rm(path):
    return {"path": path, "op": "remove"}


def strict_index(v):
    if type(v) not in (int, float) or v != v or v in (float("inf"), float("-inf")) or v != int(v) or v < 0:
        return None
    return int(v)


def reseal(source):
    """The 07e format rule: preparation hashes; selected source identities; publication; receipt."""
    body = source["retained_precision"]["body"]
    for src in body["sources"]:
        prep = src["preparation"]
        ai = strict_index(prep["attempt_ref"]) if prep is not None else None
        if ai is not None and ai < len(body["product_attempts"]):
            a = body["product_attempts"][ai]
            if all(m["result"]["kind"] == "prepared" for m in a["preparation"]["members"]):
                prep["sha256"] = rp._hash("retained_precision_preparation_v1", rp._preparation_payload(a))
    for c in body["cases"]:
        si = strict_index(c.get("source_ref")) if c["status"] == "selected" else None
        if si is not None and si < len(body["sources"]):
            c["source_identity_sha256"] = rp._source_hash(body["sources"][si])
    body["publication_sha256"] = rp._hash("retained_precision_publication_mp_v2", {k: v for k, v in source.items() if k != "retained_precision"})
    source["retained_precision"]["receipt_sha256"] = rp._hash("retained_precision_receipt_mp_v2", body)
    return source


def base_entry(bid, source, invocation, provenance, qualification):
    v = rp.validate_retained_precision(copy.deepcopy(source), copy.deepcopy(invocation))
    return {"id": bid, "provenance": provenance, "source": source, "invocation": invocation,
            "expected_classifications": v["classifications"],
            "expected": {k: v[k] for k in ("invocation_bound", "numerical_eligible", "standing")},
            "qualification": qualification}


def sha_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


# ---- bases ------------------------------------------------------------------------------------------
bases, plan = [], {"bases": [], "entries": []}
PRODUCER = {"component_name": "open_pipe_stress_product_physics", "component_version": "0.2.0",
            "semantic_contract_id": "openpipestress.result_semantics/0.3.0/preview-physics-retained-1"}
wc2 = {}
for mode in MODES:
    rel = f"fixtures/results/retained_precision_w_c2_successor_{mode}.json"
    doc = json.loads((P / rel).read_text())
    wc2[mode] = doc
    prov = {"kind": "producer_solved", "producer": PRODUCER, "solver_mode": mode, "fixture": rel, "fixture_sha256": sha_file(P / rel),
            "receipt_sha256": doc["source"]["retained_precision"]["receipt_sha256"],
            "pinned_by": ["core/product_physics/src/retained_facade_tests.rs b1_sp_w_c2_direct_entry_publishes_the_pinned_successor",
                          "core/product_physics/src/retained_facade_tests.rs b1_sp_w_c2_fixtures_are_the_live_successors"]}
    qual = ("PRODUCER-SOLVED (B1, W-C2): the three-case acceptance witness on U8's two-body model (DESIGN_v2 §1.4): case A selected "
            "at b = 518, case B not_required and W2-published (checks_passed), case C unavailable at its native Ceiling (the (4a) shape). "
            f"Source and invocation are D-U6-5 copies of {rel}. Not native Current evidence; the public reader accepts it, not eligible "
            "with its invocation (case C is unavailable).")
    bases.append(base_entry(f"w_c2_{mode}", copy.deepcopy(doc["source"]), copy.deepcopy(doc["invocation"]), prov, qual))

# d38_beside_selected: DESIGN_v2 §2's derivation, from W-C2 sparse.
d38 = copy.deepcopy(wc2["sparse_interactive"]["source"])
body = d38["retained_precision"]["body"]
C = 2
case_c = body["cases"][C]
ai, si, run_c = case_c["product_attempt_ref"], case_c["source_ref"], case_c["run"]["id"]
assert (ai, si, run_c) == (1, 1, 1)
case_c["run"] = None
case_c["reason"] = {"code": "source_unavailable", "phase": "preparation", "cause": {"kind": "prepared_product_failure", "product_attempt_ref": ai}}
a = body["product_attempts"][ai]
a["run_ref"] = None
a["proof"] = None
a["stages"] = dict.fromkeys(rp.STAGE_ORDER, "not_entered")
a["stages"].update(preparation="completed", native="failed")
a["result"] = {"kind": "unavailable", "error": {"kind": "capture", "cause": {"kind": "origin", "cause": {"kind": "capacity"}}}}
kept_builds = [x for x in body["builds"] if x["origin"]["run"] != run_c]
removed_builds = [x for x in body["builds"] if x["origin"]["run"] == run_c]
assert [x["id"] for x in kept_builds] == list(range(len(kept_builds)))
body["builds"] = kept_builds
call = body["calls"][0]
after = body["cases"][0]["run"]["invocation_after"]
call["owner_refs"] = [o for o in call["owner_refs"] if o != {"kind": "case", "index": C}]
call["run_refs"] = [r for r in call["run_refs"] if r != run_c]
call["source_refs"] = [x for x in call["source_refs"] if x != si]
call["invocation_after"] = after
for g in body["groups"]:
    g["source_refs"] = [x for x in g["source_refs"] if x != si]
body["work"]["charged"] = after
body["work"]["execution_order"] = [e for e in body["work"]["execution_order"] if e != {"kind": "case", "index": C}]
reseal(d38)
bases.append(base_entry("d38_beside_selected", d38, copy.deepcopy(wc2["sparse_interactive"]["invocation"]),
    "synthetic_reader_control_not_producer_execution_or_native_current",
    "SYNTHETIC: not producer-emittable under T-8 (DESIGN_v2 §2, R-D38 (4b)). Derived from w_c2_sparse_interactive by "
    "gen_07n.py: case C's Run, its execution_order entry and the Builds its Run originated removed; its source removed from the "
    "call's and the group's source_refs; the shared group and case A's builds kept; charged and the call's after-value set to case "
    "A's after-value; case C's attempt a capture failure with a typed CaptureError::Origin (capacity), native failed after a "
    "completed preparation, no proof; case C's reason (source_unavailable, preparation) naming its attempt; every hash resealed. "
    "G0-G8 pass with its invocation; not eligible (case C is unavailable)."))

DUMPED = {"cause_milestone_reversed": ("reversed", "b1_sp_constructor_ordinal_is_the_authored_index", "REVERSED_PINNED",
                                       "I98's cause_milestone_reversed (R/I98/b2_w_probe_01/PROBE.md §7): the milestone with its three moments "
                                       "authored RZ, RY, RX; the out-of-order-authored base (RR \"I98's B2-W verified; ...\", ruling 4)"),
          "sf2_c_b_a": ("sf2__c_b_a", "b1_sp_sf2_selected_not_first_and_two_selected_pins", "CBA_PINNED",
                        "RV109's SF-2 (C, B, A): W-C2's cases in the order C, B, A; the selected case is not first"),
          "sf2_a_a2": ("sf2__a_a2", "b1_sp_sf2_selected_not_first_and_two_selected_pins", "AA2_PINNED",
                       "RV109's SF-2 (A, A2): W-C2's case A and its copy A2, both selected")}
for stem, (dump, test, const, what) in DUMPED.items():
    for mode in MODES:
        sp, ip = Path(DUMP) / f"{dump}__{mode}.successor.json", Path(DUMP) / f"{dump}__{mode}.invocation.json"
        source, invocation = json.loads(sp.read_bytes()), json.loads(ip.read_bytes())
        prov = {"kind": "producer_solved", "producer": PRODUCER, "solver_mode": mode, "successor_bytes_sha256": sha_file(sp),
                "receipt_sha256": source["retained_precision"]["receipt_sha256"],
                "pinned_by": [f"core/product_physics/src/retained_facade_tests.rs {test} ({const})"]}
        qual = (f"PRODUCER-SOLVED (B1 SP at I3): {what}. The successor PP's test pins (receipt and bytes sha256, {const}); source and "
                "invocation are copies of the successor bytes and the invocation that test validates. Not native Current evidence.")
        bases.append(base_entry(f"{stem}_{mode}", source, invocation, prov, qual))
for bse in bases:
    plan["bases"].append({"id": bse["id"], "expected": bse["expected"], "classifications": len(bse["expected_classifications"])})

# ---- entries ----------------------------------------------------------------------------------------
entries = []


def add(eid, base, edits, item, design=None, invocation_edits=None, after_rehash=None, source=None):
    e = {"id": eid, "base": base, "edits": edits}
    if invocation_edits:
        e["invocation_edits"] = invocation_edits
    if after_rehash:
        e["after_rehash"] = after_rehash
    e["rehash"] = "all"
    entries.append(e)
    plan["entries"].append({"id": eid, "item": item, "design": design, "source": source or "gen_07n.py"})


G5P, G5A, G5W = ({"gate": "G5", "code": "RETAINED_PRECISION_" + x} for x in ("PRODUCT_ATTEMPT_MISMATCH", "ATTEMPT_MISMATCH", "WORK_MISMATCH"))
G3C = {"gate": "G3", "code": "RETAINED_PRECISION_COVERAGE_MISMATCH"}
G8P = {"gate": "G8", "code": "RETAINED_PRECISION_PREPARATION_MISMATCH"}
A1 = B + ["product_attempts", 1]
# D38 m1-m9 on d38_beside_selected (DESIGN_v2 §2; I90's first-failure notes; RR "I91's SR-PY verified; ...", ruling 1).
D = "d38_beside_selected"
add("d38_m1_error_kind_native", D, [s(A1 + ["result", "error"], {"kind": "native", "run_ref": 1})], "1 D38 m1 (I90: the whole error value)", G5P)
add("d38_m2_native_completed", D, [s(A1 + ["stages", "native"], "completed")], "1 D38 m2", G5P)
add("d38_m3_run_ref_without_run", D, [s(A1 + ["run_ref"], 1)], "1 D38 m3", None)
add("d38_m4_execution_order_lists_case", D, [s(B + ["work", "execution_order"], [{"kind": "case", "index": 0}, {"kind": "case", "index": 2}])], "1 D38 m4 (I90: G3)", G3C)
add("d38_m5_proof_start_completed", D, [s(A1 + ["stages", "proof_start"], "completed")], "1 D38 m5", G5P)
add("d38_m6_attempt_source_null", D, [s(A1 + ["source_ref"], None)], "1 D38 m6", None)
add("d38_m7_call_lists_source", D, [s(B + ["calls", 0, "source_refs"], [0, 1])], "1 D38 m7 (I90: G5 ATTEMPT)", G5A)
add("d38_m8_case_source_other", D, [s(B + ["cases", 2, "source_ref"], 0)], "1 D38 m8", None)
add("d38_m9_case_c_builds_kept", D, [s(B + ["builds"], kept_builds + removed_builds)], "1 D38 m9 (RR ruling: the Build check)", G5W)
# F-1 (DESIGN_v2 §3.2-3.4), five.
WD, WS = "w_c2_dense_scrutiny", "w_c2_sparse_interactive"
L0D, L0S = "u8_l0_isolated_node_dense_scrutiny", "u8_l0_isolated_node_sparse_interactive"
cases_by_id = {c["id"]: c for c in corpus["cases"]}
l0d_rows = cases_by_id[L0D]["source"]["results"]
parity = next(r for r in l0d_rows if r["kind"] == "sparse_live_path_dense_parity_relative_delta")
pi = l0d_rows.index(parity)
row_a = dict(copy.deepcopy(parity), id="result:loadcase:case-a:sparse-live:dense-parity-relative-delta", basis_ref={"ref_type": "load_case", "ref_id": "case-a"})
add("f1_p4_parity_on_w2_published_case_a_dense", WD, [s(["results"], copy.deepcopy(wc2["dense_scrutiny"]["source"]["results"]) + [row_a])], "2 F-1 P4 (the edit grammar has no append: the whole list is set)", G8P)
dup = dict(copy.deepcopy(parity), id=parity["id"] + ":duplicate")
add("f1_p2_parity_duplicated_l0_dense", L0D, [s(["results"], copy.deepcopy(l0d_rows) + [dup])], "2 F-1 P2 (appended, so no case-row index moves)", G8P)
l0s_rows = cases_by_id[L0S]["source"]["results"]
mode_i = next(i for i, r in enumerate(l0s_rows) if r["kind"] == "linear_solver_mode_basis")
sparse_parity = dict(copy.deepcopy(parity), basis_ref=copy.deepcopy(l0s_rows[mode_i]["basis_ref"]))
add("f1_p3_parity_in_sparse_l0", L0S, [s(["results"], copy.deepcopy(l0s_rows) + [sparse_parity])], "2 F-1 P3 (appended)", G8P)
add("f1_p1_mode_code_3_sparse_l0", L0S, [s(["results", mode_i, "value"], 3.0)], "2 F-1 P1", G8P)
add("f1_requested_mode_flipped_w_c2_case_b", WS, [s(B + ["ordinary_attempts", 1, "requested_mode"], "dense_scrutiny")], "2 F-1 requested mode", G8P)
# not_required on W-C2 case B (DESIGN_v2 §3.3), three.
add("nr_w_c2_case_b_verdict_sensitive", WS, [s(["numerical_quality", "cases", 1, "solve_quality"], "sensitive")], "3 not_required", G5A)
add("nr_w_c2_case_b_initial_not_attempted", WS, [s(B + ["ordinary_attempts", 1, "initial"], {"kind": "not_attempted", "cause": "ineligible"})], "3 not_required", G5A)
own = copy.deepcopy(wc2["sparse_interactive"]["source"]["retained_precision"]["body"]["product_attempts"][1])
own.update(id=2, owner_ref={"kind": "case", "index": 1}, ordinary_attempt_ref=1)
add("nr_w_c2_case_b_product_attempt_ref_own_attempt", WS, [s(B + ["product_attempts"], copy.deepcopy(wc2["sparse_interactive"]["source"]["retained_precision"]["body"]["product_attempts"]) + [own]), s(B + ["cases", 1, "product_attempt_ref"], 2)],
    "3 not_required (RR: case B's own product attempt, to reach G5)", G5A)
# RV108 N2 (a missing solve_quality): not_required reads the verdict.
add("n2_w_c2_case_b_solve_quality_missing", WS, [rm(["numerical_quality", "cases", 1, "solve_quality"])], "11 RV108 N2", G5A)

# ---- edit minimization (size only; every entry's materialized statement is unchanged) ---------------
def same(a, b):
    return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def diff_ops(path, old, new, out):
    """set/remove ops (the shared edit grammar) turning `old` into `new` at `path`: dicts key by key, equal-length lists
    index by index, anything else set whole."""
    if same(old, new):
        return
    if type(old) is dict and type(new) is dict:
        for k in old:
            if k not in new:
                out.append(rm(path + [k]))
        for k in new:
            if k in old:
                diff_ops(path + [k], old[k], new[k], out)
            else:
                out.append(s(path + [k], new[k]))
    elif type(old) is list and type(new) is list and len(old) == len(new):
        for i, (x, y) in enumerate(zip(old, new)):
            diff_ops(path + [i], x, y, out)
    else:
        out.append(s(path, new))


def resolve(value, path):
    for k in path:
        value = value[k]
    return value


def apply_one(root, e):
    at = resolve(root, e["path"][:-1])
    last = e["path"][-1]
    if e["op"] == "remove":
        del at[last]
    else:
        at[last] = copy.deepcopy(e["value"])


def minimize(base_id, edits):
    """Replace each large `set` whose path exists by the ops that reach the same value."""
    src = copy.deepcopy(next(c for c in corpus["cases"] + bases if c["id"] == base_id)["source"])
    out = []
    for e in edits:
        try:
            cur = resolve(src, e["path"])
            exists = True
        except (KeyError, IndexError, TypeError):
            exists = False
        if e["op"] == "set" and exists and len(json.dumps(e["value"])) > 2048:
            ops = []
            diff_ops(list(e["path"]), cur, e["value"], ops)
            out += ops
        else:
            out.append(e)
        apply_one(src, e)
    check = copy.deepcopy(next(c for c in corpus["cases"] + bases if c["id"] == base_id)["source"])
    for e in out:
        apply_one(check, e)
    assert same(check, src), base_id
    return out


# ---- RV113's probes, verbatim ------------------------------------------------------------------------
probes = {p["id"]: p for p in json.load(open(PROBES))}
probes.update({p["id"]: p for p in json.load(open(PROBES_R2X))})


def bare(pid):
    return pid.split(":", 1)[1] if ":" in pid else pid


def take(pids, item):
    for pid in pids:
        p = probes[pid]
        w = p.get("want") or {}
        design = w.get("bound") if isinstance(w.get("bound"), dict) and not w["bound"].get("observe") else None
        add(bare(pid), p["base"], minimize(p["base"], copy.deepcopy(p["edits"])), item, design, copy.deepcopy(p.get("invocation_edits") or []),
            copy.deepcopy(p.get("after_rehash") or []), source=f"RV113 {pid}")


byitem = {}
for p in json.load(open(PROBES)):
    byitem.setdefault(p.get("item"), []).append(p["id"])
take(byitem["2 (4a)"], "4 (4a) positive and its neighbours")
take(byitem["F"], "7 (f) family and the ordinary basis reference")
take(byitem["G"], "7 (g) model scope")
take(byitem["C-a"], "7 C2 receipt and facade branches")
take([p for p in byitem["C-b"] if not p.startswith("r2:cb_pre_")], "7 C2 source_error, receipt, facade and kernel branches; 14 ruling 5")
KEYS = {"caller": "caller_not_qualified", "resource_admission": "resource_admission_not_available",
        "upstream_no_wrap": "upstream_no_wrap_not_established", "capture": "source_unavailable", "source_family": "source_unavailable"}
CODES = ["caller_not_qualified", "resource_admission_not_available", "source_unavailable", "upstream_no_wrap_not_established"]
pre = []
for key, code in KEYS.items():
    pre += [f"r2:cb_pre_{key}_{code}_routing", f"r2:cb_pre_{key}_{code}_preparation", f"r2:cb_pre_{key}_{code}_kernel"]
    pre += [f"r2:cb_pre_{key}_{other}_routing" for other in CODES if other != code]
assert all(x in probes for x in pre), [x for x in pre if x not in probes]
take(pre, "7 C2 precondition keying: own code at routing and preparation, wrong phase, each wrong code")
take(byitem["C-c"], "7 C2 precondition keyed")
take(byitem["C-d"], "7 C2 kernel branch")
take(byitem["SR-TS C2"], "7 C2 through the whole reader")
take(byitem["H"], "7 the transport header at G2, the metadata at G7 (RV108 N5); 12-14")
take(byitem["SR-TS N6"], "11 RV108 N1 (list and dict enums); 13 and 14 the compound N6 pair")
take(byitem["SR-TS N4"], "11 RV108 N4 (a raw row not an object, on transport)")
for it in ("control", "(b)", "(c)", "(d1)", "(d2)", "(e)", "(c) count"):
    take(byitem[it], f"8-9 I91 repair 01 {it}")
take(byitem["3 G8"], "2 F-1 text B and the mode rows (P1-P4); 10 a copied parity row's recovery_method")
take(byitem["3 limit"], "2 F-1 the disclosed limit (a deleted parity row is not detected)")
take(byitem["4 G5"], "3 the not_required rule")
take(byitem["2 audit"], "4 D38 audit: an orphan source beside T-7")
take(byitem["T"], "7 the transport metadata at G7; 14 rulings 2 and 3")
take(["r2x:t_measure_extra_member", "r2x:t_gate_extra_member"], "7 the transport metadata at G7")

ids = [e["id"] for e in corpus["mutations"] + corpus["must_pass"]] + [e["id"] for e in entries]
assert len(set(ids)) == len(ids), [x for x in ids if ids.count(x) > 1][:5]
assert len({b["id"] for b in corpus["cases"] + bases}) == len(corpus["cases"]) + len(bases)

draft = copy.deepcopy(corpus)
draft["cases"] += bases
for e in entries:
    draft["mutations"].append(dict(e, expected={"gate": "DRAFT", "code": "DRAFT"}))
Path(OUT).write_text(json.dumps(draft, indent=2) + "\n")
Path(PLAN).write_text(json.dumps(plan, indent=1) + "\n")
print(f"bases +{len(bases)}, entries +{len(entries)}; draft {len(Path(OUT).read_bytes())} bytes")
