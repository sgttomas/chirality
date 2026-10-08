"""I104 SQ G5: I82's 22 emulated loop-rule rebinds and 22 emulated edge multiplicities (I82_PATCHES.json), each
against B1's real code: the rule I104 applies (rebind, keep, or the real loop's new rule) and, for each emulated
edge, the callee's TEXT multiplicity at c = 3 in I82's run and in B1's (main text run), with B1's real path.
Usage: i82_checklist.py <I82_PATCHES.json> <I104_RULES.json> <i82 tb c3> <b1 tb c3> > out.json"""
import json, sys, re
P, R, ti, tb = (json.load(open(p)) for p in sys.argv[1:5])
Mi = {k.split("/src/")[-1]: v for k, v in ti["function_multiplicity"].items()}
Mb = {k.split("/src/")[-1]: v for k, v in tb["function_multiplicity"].items()}
def by_name(M, name):
    return {k: v for k, v in M.items() if k.rsplit(":", 1)[1] == name}
REAL = {  # I82's emulated caller -> callee: B1's real call path (the loop that now carries the multiplicity)
 "reserve": "retained_w1 -> ReservedNotices::reserve (lib.rs:3072), whose loops over A (att) call ReservedNotice::reserve (lib.rs:3049)",
 "publish": "retained_w1 -> ReservedNotices::publish once (one call site); its loop over the reserved notices is att",
 "prepare_case": "w1_transaction -> prepare_cases -> `for (attempt,&request) in attempted` (att) -> prepare_attempt -> prepare_active_case",
 "freeze_candidate": "w1_transaction -> PreparedCases::freeze -> `for attempt in attempts..Selected` (att) -> freeze_case",
 "selection": "serialize_cases_with -> `for attempt in attempts` (att) -> serialize_attempt -> selection",
 "product_attempt": "serialize_attempt (att) -> product_attempt",
 "one_run": "replaced: serialize_attempt's case_run per attempt (att); the one-case one_run is only on the private driver",
 "kernel_outcome": "serialize_attempt (att) -> kernel_outcome",
 "run_value": "serialize_attempt (att) -> run_value",
 "bind_preparation": "serialize_attempt (att) -> bind_preparation",
 "case_source": "serialize_attempt (att) -> case_source",
 "typed_trace": "serialize_attempt (att) -> CaseAttempt::typed_trace (and the name fan-out to the other typed_trace methods)",
 "bind_rows": "serialize_attempt (att) -> bind_rows_scoped -> bind_rows_view; freeze_case (att) -> bind_rows_view",
 "domain_hash": "serialize_attempt (att) -> domain_hash (source identity), plus finish's per-invocation hashes",
 "one_case": "replaced: serialize_cases_with's loops over the requested cases (cases); one_case is only on the private driver",
 "ordinary_value": "serialize_cases_with -> `for (index, ((seed, ..)))` (cases) -> ordinary_entry",
 "legacy_source": "serialize_cases_with -> `for (index, seed) in pc.ordinary` (cases) -> legacy_source",
}
edges = []
for caller, callee, k in P["edge_per_call_added"]:
    name = callee.rsplit(":", 1)[1]
    real_name = {"one_run": "case_run", "one_case": "serialize_cases_with", "ordinary_value": "ordinary_entry", "freeze_candidate": "freeze_case",
                 "prepare_case": "prepare_active_case", "bind_rows": "bind_rows_view"}.get(name, name)
    edges.append({"i82_caller": caller, "i82_callee": callee, "i82_per_call": k,
                  "i82_M_c3": by_name(Mi, name), "b1_real_path": REAL.get(name, "?"), "b1_M_c3": by_name(Mb, real_name)})
reb = []
applied = {r["re"]: r for r in R["rebind"]}; kept = {r["re"]: r for r in R["keep"]}
for r in P["loop_rebinds"]:
    d = applied.get(r["re"]) or kept.get(r["re"])
    reb.append({"i82_index": r["index"], "re": r["re"], "i82": f"{r['old']} -> {r['new']}",
                "i104": (f"rebind {d['old']} -> {d['new']}" if r["re"] in applied else f"kept {d['bound']}") if d else "not matched by name: see note",
                "i104_why": d["why"] if d else None})
json.dump({"edges": edges, "rebinds": reb}, sys.stdout, indent=1)
