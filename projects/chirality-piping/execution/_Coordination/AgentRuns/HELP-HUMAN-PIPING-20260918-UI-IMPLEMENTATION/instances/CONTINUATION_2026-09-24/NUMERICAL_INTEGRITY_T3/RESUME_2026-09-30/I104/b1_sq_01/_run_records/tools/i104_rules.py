"""I104 SQ G5: B1's TEXT rules, applied to a copy of the b1-q chain (b1q_chain.py's output; stdlib only).

- New loop rules for every loop on a B1-changed line that is reached from the D1 root and that no existing
  rule bounds correctly (gen/decisions.py NEW, by the loop inventory's index): each is the loop's exact
  header, anchored, placed first; FIRST rules (whole-envelope loops that a composite rule would bound at
  P_final) go ahead of them.
- Existing rules whose bound was D1's one case are re-bound (REBIND), or re-checked and kept (KEEP).
- The validate_profile -> problem edge's per-call count is re-bound (EDGE_PER_CALL).
- Stale keys (the line map's 7 unmapped keys) are dropped or re-keyed, and the two new identifier sites are
  audited (text_args id_audit).
Every action is logged to I104_RULES.json in the output chain. Each REBIND/KEEP pattern must match exactly
one existing rule, and each NEW index must be a reached loop of the inventory, or this script fails.
Usage: python3 i104_rules.py <chain in> <chain out> <loop inventory json> <decisions.py>
"""
import json, os, re, shutil, sys, runpy
src, dst, inv_p, dec_p = sys.argv[1:5]
if os.path.exists(dst):
    shutil.rmtree(dst)
shutil.copytree(src, dst)
D = runpy.run_path(dec_p)
inv = json.load(open(inv_p))["loops"]
LOG = {"new_loop_rules": [], "first_rules": [], "rebind": [], "keep": [], "edge_per_call": [], "callgraph_rules_dropped": [],
       "text_args": [], "inventory_dispositions": []}
lbp = os.path.join(dst, "loop_bounds.g4.json"); LB = json.load(open(lbp))
# --- REBIND and KEEP: each pattern names exactly one existing rule
def one_rule(pattern):
    hits = [i for i, r in enumerate(LB["loops"]) if r["re"] == pattern]
    if len(hits) != 1:
        raise SystemExit(f"RULE NOT UNIQUE ({len(hits)}): {pattern}")
    return hits[0]
for pat, new, why in D["REBIND"]:
    i = one_rule(pat); r = LB["loops"][i]
    LOG["rebind"].append({"index": i, "re": pat, "old": r["bound"], "new": new, "why": why, "old_why": r["why"]})
    r["bound"] = new; r["why"] = f"I104 SQ B1 rebind ({LOG['rebind'][-1]['old']} -> {new}): {why}. Was: {r['why']}"
for pat, bound, why in D["KEEP"]:
    i = one_rule(pat); r = LB["loops"][i]
    if r["bound"] != bound:
        raise SystemExit(f"KEEP BOUND DIFFERS: {pat}: {r['bound']} != {bound}")
    LOG["keep"].append({"index": i, "re": pat, "bound": bound, "why": why})
    r["why"] = f"I104 SQ B1 re-checked, kept ({bound}): {why}. Was: {r['why']}"
# --- NEW: exact anchored headers from the inventory
new_rules, seen = [], {}
for idx, (bound, why) in sorted(D["NEW"].items()):
    l = inv[idx]
    if not l["reached"]:
        raise SystemExit(f"NEW index {idx} is not reached: {l['header'][:80]}")
    h = l["header"]
    site = f"{l['file'].split('/src/')[-1]}:{l['line']}"
    if h in seen:
        if seen[h]["bound"] != bound:
            raise SystemExit(f"HEADER BOUND CONFLICT {h[:80]}: {seen[h]['bound']} vs {bound}")
        seen[h]["sites"].append(site); continue
    rule = {"re": "^" + re.escape(h) + "$", "bound": bound, "why": f"I104 SQ B1 (new or changed loop at {site}): {why}"}
    seen[h] = {"bound": bound, "sites": [site], "rule": rule}
    new_rules.append(rule)
for h, v in seen.items():
    LOG["new_loop_rules"].append({"header": h, "bound": v["bound"], "sites": v["sites"], "re": v["rule"]["re"]})
first = [{"re": p, "bound": b, "why": f"I104 SQ B1 (placed first): {w}"} for p, b, w in D["FIRST"]]
LOG["first_rules"] = first
LB["loops"][0:0] = first + new_rules
# --- edges
for caller, callee, old, new, why in D["EDGE_PER_CALL"]:
    hits = [e for e in LB["edge_per_call"] if e["caller"] == caller and e["callee"] == callee]
    if len(hits) != 1 or hits[0]["per_call"] != old:
        raise SystemExit(f"EDGE NOT FOUND {caller} -> {callee}")
    hits[0]["per_call"] = new; hits[0]["why"] = f"I104 SQ B1 rebind ({old} -> {new}): {why}. Was: {hits[0]['why']}"
    LOG["edge_per_call"].append({"caller": caller, "callee": callee, "old": old, "new": new, "why": why})
# per-invocation totals and caps whose D1 reason counted one case (scaled by the case count)
SCALE = [
  ("loop_total", "fn", "source_receipt/source.rs:46:lowered_products", "total", "16384", "16384*cases"),
  ("loop_total", "fn", "source_receipt/source.rs:17:products", "total", "16384", "16384*cases"),
  ("loop_total", "fn", "source_receipt/source.rs:252:commitment", "total", "16384", "16384*cases"),
  ("loop_total", "fn", "source_receipt/source.rs:11:matrix12", "total", "3*m*144", "cases*3*m*144"),
  ("loop_total", "fn", "source_receipt/source.rs:5:matrix", "total", "N*N", "cases*N*N"),
  ("fn_cap", "fn", "lib.rs:249:new", "cap", "4*(g+r)", "4*cases*(g+r)"),
  ("fn_cap", "fn", "lib.rs:634:add_restrained_dof", "cap", "4*r", "4*cases*r"),
]
LOG["scaled_totals"] = []
for fam, kf, key, field, old, new in SCALE:
    hits = [e for e in LB[fam] if e[kf] == key]
    if len(hits) != 1 or hits[0][field] != old:
        raise SystemExit(f"SCALE NOT FOUND {fam} {key}")
    hits[0][field] = new
    hits[0]["why"] = (f"I104 SQ B1 ({old} -> {new}): the D1 reason counts one case's T25 replay / boundary preparations; at c cases "
                      f"each requested case may run them, so the per-invocation total is scaled by c (conservative: whether a meter is "
                      f"per case or per invocation is not re-derived). Was: " + hits[0]["why"])
    LOG["scaled_totals"].append({"family": fam, "key": key, "old": old, "new": new})
json.dump(LB, open(lbp, "w"), indent=1)
# --- the call graph's R-1 rules for the removed `impl SelectedCandidate for rp::FrozenCandidate`
cgp = os.path.join(dst, "callgraph_rules.g4.json"); CG = json.load(open(cgp))
gone = ("core/product_physics/src/retained_wire.rs:1493:capture", "core/product_physics/src/retained_wire.rs:1494:certificate",
        "core/product_physics/src/retained_wire.rs:1495:typed_trace")
keep = []
for r in CG["rules"]:
    if r.get("caller") in gone:
        LOG["callgraph_rules_dropped"].append({"rule": r, "why": "B1 SP removed `impl SelectedCandidate for rp::FrozenCandidate` "
            "(retained_wire.rs; the Direct path serializes through `serialize_cases`), so the rule's caller no longer exists; "
            "the line map left its keys unmapped (they lie in a changed hunk)"})
    else:
        keep.append(r)
if len(LOG["callgraph_rules_dropped"]) != 3:
    raise SystemExit("expected 3 FrozenCandidate rules")
ADJ = [
  ("core/product_physics/src/lib.rs:3279:w1_transaction", "freeze", ["core/product_physics/src/retained_product.rs:3716:freeze"],
   "lib.rs w1_transaction `prepared.freeze()`: prepared is the PreparedCases returned by prepare_cases, so PreparedCases::freeze"),
  ("core/product_physics/src/retained_product.rs:3678:native", "freeze", ["core/product_physics/src/retained_receipt.rs:57:freeze"],
   "retained_product.rs native `attempt.trace.freeze(capture)`: attempt is a &mut CaseAttempt, whose trace is a trace::PreparedTrace (retained_receipt.rs:57)"),
  ("core/product_physics/src/retained_product.rs:3882:prepare_attempt", "freeze", ["core/product_physics/src/retained_receipt.rs:57:freeze"],
   "retained_product.rs prepare_attempt `trace.freeze(self)`: trace is the local trace::PreparedTrace::default() (retained_receipt.rs:57)"),
]
LOG["callgraph_rules_added"] = []
for caller, name, targets, ev_ in ADJ:
    keep.append({"caller": caller, "name": name, "targets": targets, "added": "I104 SQ G5 (B1's new same-named methods)",
                 "evidence": ev_ + "; the receiver is an untyped binding, so the call would fan out by name to both freeze methods"})
    LOG["callgraph_rules_added"].append(keep[-1])
CG["rules"] = keep; json.dump(CG, open(cgp, "w"), indent=1)
# --- text_args: stale keys and the two new identifier sites
tap = os.path.join(dst, "text_args.g4.json"); TA = json.load(open(tap))
def ta(action, key, value, why):
    LOG["text_args"].append({"action": action, "key": key, "value": value, "why": why})
v = TA["id_audit"].pop("core/product_physics/src/lib.rs:3042")
TA["id_audit"]["core/product_physics/src/lib.rs:3078"] = v
ta("re-key", "core/product_physics/src/lib.rs:3042 -> :3078", v, "B1 SP moved the notice id's format! from ReservedNotice::reserve "
   "into ReservedNotices::reserve (lib.rs:3078), same text and argument (the request case id, <= 128 B)")
v = TA["id_audit"].pop("core/product_physics/src/retained_wire.rs:1593")
TA["id_audit"]["core/product_physics/src/retained_wire.rs:1946"] = v
ta("re-key", "core/product_physics/src/retained_wire.rs:1593 -> :1946", v, "the source-identity binding's `source.clone()`: serialize_selected_from's "
   "(the one-case serializer, now reached only by the private driver) moved into serialize_attempt (retained_wire.rs:1946), same expression")
TA["id_audit"]["core/product_physics/src/retained_wire.rs:1634"] = {"case_id": {"bytes": 128, "source": "IN128"}}
ta("add", "core/product_physics/src/retained_wire.rs:1634", TA["id_audit"]["core/product_physics/src/retained_wire.rs:1634"],
   "unavailable_case_envelope's notice id format!: the request case id, as selected_case_envelope's (retained_wire.rs:772, IN128)")
for site in ("retained_wire.rs:1796", "retained_wire.rs:1863"):
    TA["site_zero"][site] = ("I104 SQ B1: Option::replace on an attempt or source slot (serialize_cases_with), not a String "
                             "(as text_args' `rigid_owner[global]` rule)")
    ta("add site_zero", site, TA["site_zero"][site], "Option::replace, no text")
TA["args"].insert(0, {"re": r'^terminal\[" "\]\.as_str\(\)\.unwrap_or_default\(\)$', "max": "static",
    "why": "I104 SQ B1: a Run's kernel_terminal.kind, one of kernel_outcome's fixed terminal tokens (retained_wire.rs), copied with to_owned "
           "(serialize_attempt :1989; serialize_unavailable :1712): a static literal"})
ta("add args rule (first)", TA["args"][0]["re"], "static", TA["args"][0]["why"])
v = TA["lex_site_size"].pop("retained_wire.rs:1359")
ta("remove", "lex_site_size retained_wire.rs:1359", v, "one_case's case-id copy, in the one-case serializer (unreached from the D1 root at B1)")
TA["id_audit"]["core/product_physics/src/retained_product.rs:4492"] = {
    "row.unit": {"bytes": 128, "source": "STATIC"}, "row.entity_ref": {"bytes": 128, "source": "IN128"}, "row.id": {"bytes": 1024, "source": "RES"}}
ta("add", "core/product_physics/src/retained_product.rs:4492", TA["id_audit"]["core/product_physics/src/retained_product.rs:4492"],
   "stage_headlines' LocatedQuantity copies a staged row's unit, entity_ref and id: the same classes as the ordinary headline's "
   "copy of a row (preview_physics.rs:690: row.unit STATIC, row.entity_ref IN128, row.id RES)")
TA["id_audit"]["core/reporting/result_export/src/retained_precision.rs:4371"] = {
    'text(&run["kernel_terminal"]["kind"])': {"bytes": 128, "source": "STATIC"}}
ta("add", "core/reporting/result_export/src/retained_precision.rs:4371", TA["id_audit"]["core/reporting/result_export/src/retained_precision.rs:4371"],
   "g5_ordinary's `kernel_{kind}`: the Run's kernel_terminal.kind, one of the producer's fixed terminal tokens (retained_wire.rs kernel_outcome), STATIC <= 128 B")
TSCALE = [
  ("site_total", "load_ledger.rs:133", "bytes", "5*l*2*128", "5*cases*l*2*128", "the case ledger and the T25 replay's are per requested case, the three prepare_sources folded ledgers per case (5 per case, c cases)"),
  ("site_total", "load_ledger.rs:408", "bytes", "4*l*2*128", "4*cases*l*2*128", "W2's two evaluations run per requested case"),
  ("site_total", "load_ledger.rs:670", "bytes", "5*l*2*128", "5*cases*l*2*128", "as LoadLedger::push: 5 ledgers per case"),
  ("site_total", "source_receipt/source.rs:147", "bytes", "16384*2*87", "cases*16384*2*87", "the unit limit per T25 replay, one per requested case (conservative)"),
  ("site_from", "retained_precision.rs:211", "per", "1+4*64", "1+4*64*att", "g5_native's tw() swallows sum()'s WORK_MISMATCH over each Run's <= 4 records x 64 amounts, one Run per submitted case"),
  ("site_from", "retained_precision.rs:213", "per", "1+4*64", "1+4*64*att", "as :211"),
]
for fam, key, field, old, new, why in TSCALE:
    e = TA[fam][key]
    if e[field] != old:
        raise SystemExit(f"TSCALE {fam} {key}: {e[field]} != {old}")
    e[field] = new; e["why"] = f"I104 SQ B1 ({old} -> {new}): {why}. Was: " + e["why"]
    ta("scale " + fam, key, new, why)
for key in ("source_receipt.rs:28", "source_receipt.rs:31", "source_receipt.rs:55"):
    TA["site_total"][key]["why"] = ("I104 SQ B1 re-checked, kept: at c = 3, 2*cases + 2 = 8 errors per invocation, the 8 already charged. Was: "
                                     + TA["site_total"][key]["why"])
    ta("keep site_total", key, TA["site_total"][key]["bytes"], "2*cases + 2 = 8 at c = 3: the charged 8 holds")
json.dump(TA, open(tap, "w"), indent=1)
# --- the profile tree's basis label (g4_caps.py writes it into profile_tree.json; g5_profile.py into the block's comment)
g4p = os.path.join(dst, "g4_caps.py"); g4 = open(g4p).read()
OLD_B = 'tree = {"basis": "NUM 1e323058f3 (G5 part 1 code); text at l <= 128 on the R-4 graph"'
NEW_B = 'tree = {"basis": "b1-q 57c92a7b33 (B1 SQ G5: C = 3, L <= 384, I104 rules); text at l <= 128 on the R-4 graph"'
if g4.count(OLD_B) != 1:
    raise SystemExit("basis label not found")
open(g4p, "w").write(g4.replace(OLD_B, NEW_B))
LOG["basis_label"] = {"old": OLD_B, "new": NEW_B}
# --- every inventory loop's disposition
for i, l in enumerate(inv):
    if i in D["NEW"]:
        d = "new rule: " + D["NEW"][i][0]
    elif not l["reached"]:
        d = "not reached from the D1 root (test or private-driver code): no rule needed"
    else:
        r = l["rule"]
        d = f"existing {r['kind']}" + (f" #{r.get('index')}" if r.get("index") is not None else "") + f": {r.get('bound')} (correct at B1)"
    LOG["inventory_dispositions"].append({"index": i, "site": f"{l['file'].split('/src/')[-1]}:{l['line']}", "header": l["header"][:200],
                                          "reached": l["reached"], "text_ancestor": l["text_ancestor"], "disposition": d})
json.dump(LOG, open(os.path.join(dst, "I104_RULES.json"), "w"), indent=1)
print(json.dumps({k: len(v) for k, v in LOG.items()}))
