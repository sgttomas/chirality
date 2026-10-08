"""[RV124: B1-site controls on I104's copy; I104 SQ copy of I65 u4_g7_06 audit_controls_g7.py: the control sites re-keyed to b1-q by the line map (lib.rs:5592->5773, :8795->8976; retained_product.rs:3125->3404; retained_precision.rs:4272->4421, :1722->1745), and the cap vector from G4_CAPS_RUN; otherwise unchanged]
G7 (from G6 repair's audit_controls_g6r.py): enforcement controls on the integrated tree, plus the cycle control. Each control is one change to a scratch copy of
text_args.g4.json; the whole-run text_budget.py (D from the run's summary, TB_D_RUN) must then be
incomplete with the named finding, and the unmodified copy must be complete.
Usage: python3 audit_controls_g6r.py <sens work dir> <snapshot P dir> <edges json> <lexicon json> <out dir>"""
import json, os, subprocess, sys, copy
work, snap, edges, lexicon, out = sys.argv[1:6]
os.makedirs(out, exist_ok=True)
TA0 = json.load(open(os.path.join(work, "text_args.g4.json")))
LB0 = json.load(open(os.path.join(work, "loop_bounds.g4.json")))
def drop(site, k):
    def f(ta):
        del ta["id_audit"][site][k]
        if not ta["id_audit"][site]:
            del ta["id_audit"][site]
    return f
def add(fam, k, v):
    def f(ta):
        ta.setdefault(fam, {})[k] = v
    return f
def rekey(fam, old, new):
    def f(ta):
        ta[fam][new] = ta[fam].pop(old)
    return f
def bogus_entry(site):
    def f(ta):
        ta["id_audit"][site]["no_such_expression.id"] = {"bytes": 128, "source": "IN128"}
    return f
def drop_site(site):
    def f(ta):
        del ta["id_audit"][site]
    return f
def drop_args_rule(rx):
    def f(ta):
        n=len(ta["args"]); ta["args"]=[r for r in ta["args"] if r["re"]!=rx]; assert len(ta["args"])==n-1
    return f
CONTROLS = [
    ("c0_unmodified", None, None),
    ("b1_wire_1634_case_id", drop("core/product_physics/src/retained_wire.rs:1634", "case_id"), ("id-unaudited", "retained_wire.rs:1634 case_id")),
    ("b1_product_4492_row_id", drop("core/product_physics/src/retained_product.rs:4492", "row.id"), ("id-unaudited", "retained_product.rs:4492 row.id")),
    ("b1_lib_3078_site", drop_site("core/product_physics/src/lib.rs:3078"), ("id-unaudited", "lib.rs:3078")),
    ("b1_wire_1946_site", drop_site("core/product_physics/src/retained_wire.rs:1946"), ("id-unaudited", "retained_wire.rs:1946")),
    ("b1_rs_4371_site", drop_site("core/reporting/result_export/src/retained_precision.rs:4371"), ("id-unaudited", "retained_precision.rs:4371")),
    ("b1_terminal_kind_rule", drop_args_rule(r'^terminal\[" "\]\.as_str\(\)\.unwrap_or_default\(\)$'), ("", "terminal")),
]
res = []
for name, mod, expect in CONTROLS:
    ta = copy.deepcopy(TA0); lb = copy.deepcopy(LB0)
    if isinstance(mod, str) and mod.startswith("LB:"):
        caller, callee = mod[3:].split(">")
        lb["edge_zero"] = [e for e in lb["edge_zero"] if not (e["caller"] == caller and e["callee"] == callee)]
    elif isinstance(mod, str) and mod.startswith("LBR:"):
        lb["recursion_reviewed"] = [e for e in lb["recursion_reviewed"] if e["fn"] != mod[4:]]
    elif isinstance(mod, str) and mod == "TA:si":
        ta["args"] = [r for r in ta["args"] if r["re"] != "^si$"]
    elif mod:
        mod(ta)
    tap = os.path.join(out, f"text_args.{name}.json")
    json.dump(ta, open(tap, "w"), indent=1)
    lbp = os.path.join(out, f"loop_bounds.{name}.json")
    json.dump(lb, open(lbp, "w"), indent=1)
    env = dict(os.environ, G4_CAPS=os.environ.get("G4_CAPS_RUN", '{"l": 128}'), TB_LEXICON=lexicon, TB_COMPOSITE=os.path.join(work, "composite_text.caps.json"), TB_D=os.environ["TB_D_RUN"])   # G7 Pass B (RV89 S-1(d)): the run's own D, never a constant
    op = os.path.join(out, f"{name}.out.json")
    with open(op, "w") as fh:
        subprocess.run(["python3", os.path.join(work, "text_budget.py"), snap, os.path.join(work, "template_inventory_head.out.json"), edges,
                        lbp, tap, "run_linear_static_preview_value_with_retained_direct", "caps"],
                       cwd=snap, env=env, stdout=fh, check=True)
    t = json.load(open(op))
    found = [u for u in t["unclassified_args"]]
    hit = expect is None or any(u[0][0] == expect[0] and all(p in u[0][1] for p in expect[1].split(" ")) for u in found)
    # c9: restoring one cut edge re-forms the cycle; the run must be incomplete with an `scc` finding
    ok = (t["complete"] and not found) if expect is None else ((not t["complete"]) and hit and (len(found) == 1 or expect[0] == "scc"))
    res.append({"control": name, "expect": expect, "complete": t["complete"], "TAV": t["total_text_requested_bytes"], "findings": found, "pass": ok})
    os.remove(op)   # keep the summary only (the whole-run output is ~MBs)
json.dump(res, open(os.path.join(out, "audit_controls_g7.out.json"), "w"), indent=1)
for r in res:
    print(r["control"], "complete=", r["complete"], "TAV=", r["TAV"], "pass=", r["pass"], r["findings"][:2])
