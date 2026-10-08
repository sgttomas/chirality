"""I100 B1 SC: the 07n records script, step 2 (expectations from the three readers' agreement).

Usage: fix_07n.py <draft.json> <plan.json> <py.jsonl> <rs.jsonl> <ts.jsonl> <out corpus.json> <out analysis.json>

For each new entry (the draft's mutations after 07m's 294), from the three readers' census lines:
- bound: all three equal -> the shared `expected` (a refusal: a mutation; admitted with equal eligibility: a must-pass
  entry, `expected: "pass"` and `expected_eligibility`). Unequal -> per-reader `expected_by_reader` (bound only) when a
  declared class covers it; otherwise the entry is held out and listed for ROOT.
  Declared classes: (R1) Rust's specific raw G7 preview-evidence codes where Python and TS give
  SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID (entry 139's class; RV113's RS addendum 02 N-3; RR ruling 3); (R2) the named
  compound and header probes' raw G7 codes (B1_SC items 12 and 13).
- unbound and transport: pinned as `expected_unbound` / `expected_transport` ("pass", or {gate, code}) when all three
  readers agree; a transport disagreement holds the entry out; an unbound disagreement leaves it unpinned.
07m's entries and bases are untouched (append only).
"""
import copy
import json
import sys
from pathlib import Path

draft_p, plan_p, py_p, rs_p, ts_p, out_p, an_p = sys.argv[1:8]
draft = json.loads(Path(draft_p).read_text())
plan = json.loads(Path(plan_p).read_text())
E = ("bound", "unbound", "transport")


def load(p):
    return {(r["set"], r["i"]): r for r in (json.loads(l) for l in open(p) if l.strip())}


runs = {"python": load(py_p), "rust": load(rs_p), "typescript": load(ts_p)}


def short(v):
    if v is None:
        return {"missing": True}
    if "ok" in v:
        return {"pass": True, "eligible": v["ok"]["numerical_eligible"], "bound": v["ok"]["invocation_bound"]}
    if "err" in v:
        return {"gate": v["err"]["gate"], "code": v["err"]["code"]}
    return {"escape": str(v)[:200]}


R2 = {"h_carrier_present", "h_carrier_and_quality_defect", "h_carrier_and_recovery", "h_recovery_and_evidence_null",
      "n6_carrier_evidence_with_case_defect", "n6_contract_evidence_null_and_source_block_recovery", "h_formulation_limitations_other"}


def declared(eid, v):
    py, rs, ts = v["python"], v["rust"], v["typescript"]
    if not all("gate" in x and x["gate"] == "G7" for x in (py, rs, ts)):
        return None
    inv = "SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID"
    if py == ts and py["code"] == inv and rs["code"].startswith("SOURCE_PREVIEW_PHYSICS_") and rs["code"] != inv:
        return "R1"
    if eid in R2:
        return "R2"
    return None


corpus = copy.deepcopy(draft)
new = corpus["mutations"][294:]
corpus["mutations"] = corpus["mutations"][:294]
assert len(new) == len(plan["entries"])
analysis = {"entries": [], "held_out": [], "design_mismatch": [], "unbound_unpinned": [], "counts": {}}
for k, (e, meta) in enumerate(zip(new, plan["entries"])):
    assert e["id"] == meta["id"]
    i = 294 + k
    v = {r: {x: short(runs[r][("mutation", i)].get(x)) for x in E} for r in runs}
    for r in runs:
        assert runs[r][("mutation", i)]["id"] == e["id"], (r, i)
    entry = {kk: vv for kk, vv in e.items() if kk != "expected"}
    row = {"id": e["id"], "item": meta["item"], "design": meta["design"], "verdicts": v}
    bound = {r: v[r]["bound"] for r in runs}
    if all(bound[r] == bound["python"] for r in runs):
        b = bound["python"]
        if "gate" in b:
            entry["expected"] = b
            kind = "mutations"
        elif "pass" in b:
            entry["expected"] = "pass"
            src = runs["python"][("mutation", i)]["bound"]["ok"]
            entry["expected_eligibility"] = {"invocation_bound": src["invocation_bound"], "numerical_eligible": src["numerical_eligible"], "standing": src["standing"]}
            kind = "must_pass"
            # The readers' must-pass rule compares the base's classifications; an admitted rewrite that changes them
            # (a case no longer selected, a row added or removed) states its own, when all three readers agree on them.
            full = {r: runs[r][("mutation", i)]["bound"]["ok"].get("classifications_full") for r in runs}
            if not all(full[r] == full["python"] for r in runs) or full["python"] is None:
                analysis["held_out"].append({"id": e["id"], "why": "classifications disagree", "item": meta["item"],
                                             "counts": {r: None if full[r] is None else len(full[r]) for r in runs}})
                continue
            base_cls = next(c for c in draft["cases"] if c["id"] == e["base"])["expected_classifications"]
            if full["python"] != base_cls:
                entry["expected_classifications"] = full["python"]
        else:
            analysis["held_out"].append({"id": e["id"], "why": "bound escape", "verdicts": v})
            continue
        row["bound"] = "shared"
    else:
        cls = declared(e["id"], bound)
        if cls is None:
            analysis["held_out"].append({"id": e["id"], "why": "bound disagreement", "item": meta["item"], "verdicts": v})
            continue
        entry["expected"] = bound["python"]
        entry["expected_by_reader"] = {"python": bound["python"], "typescript": bound["typescript"], "rust": bound["rust"]}
        kind = "mutations"
        row["bound"] = f"per reader ({cls})"
    for x in ("unbound", "transport"):
        vals = [v[r][x] for r in runs]
        if all(val == vals[0] for val in vals):
            val = vals[0]
            entry[f"expected_{x}"] = "pass" if "pass" in val else val
        elif x == "transport":
            analysis["held_out"].append({"id": e["id"], "why": "transport disagreement", "item": meta["item"], "verdicts": v})
            entry = None
            break
        elif x == "unbound" and "expected_by_reader" in entry and all(v[r]["unbound"] == entry["expected_by_reader"][r] for r in runs):
            # The unbound read is the raw read without the invocation: each reader's declared raw code, as bound.
            entry["expected_unbound_by_reader"] = copy.deepcopy(entry["expected_by_reader"])
        else:
            analysis["unbound_unpinned"].append({"id": e["id"], "item": meta["item"], "bound": row["bound"], "unbound": {r: v[r]["unbound"] for r in runs}})
    if entry is None:
        continue
    d = meta["design"]
    if d is not None and kind == "mutations" and {"gate": d["gate"], "code": d["code"]} != entry["expected"]:
        analysis["design_mismatch"].append({"id": e["id"], "item": meta["item"], "design": d, "got": entry["expected"], "per_reader": entry.get("expected_by_reader")})
    order = ["id", "base", "edits", "invocation_edits", "after_rehash", "rehash", "expected", "expected_by_reader", "expected_eligibility", "expected_classifications", "expected_unbound", "expected_unbound_by_reader", "expected_transport"]
    corpus[kind].append({kk: entry[kk] for kk in order if kk in entry})
    row["kind"] = kind
    analysis["entries"].append(row)
analysis["counts"] = {"cases": len(corpus["cases"]), "mutations": len(corpus["mutations"]), "must_pass": len(corpus["must_pass"]),
                      "new_cases": len(corpus["cases"]) - 17, "new_mutations": len(corpus["mutations"]) - 294, "new_must_pass": len(corpus["must_pass"]) - 28,
                      "held_out": len(analysis["held_out"]), "per_reader": sum(1 for r in analysis["entries"] if r["bound"] != "shared"),
                      "with_expected_unbound": sum("expected_unbound" in e for e in corpus["mutations"][294:] + corpus["must_pass"][28:]),
                      "with_expected_classifications": sum("expected_classifications" in e for e in corpus["must_pass"][28:]),
                      "with_expected_unbound_by_reader": sum("expected_unbound_by_reader" in e for e in corpus["mutations"][294:] + corpus["must_pass"][28:]),
                      "with_expected_transport": sum("expected_transport" in e for e in corpus["mutations"][294:] + corpus["must_pass"][28:])}
Path(out_p).write_text(json.dumps(corpus, indent=2) + "\n")
Path(an_p).write_text(json.dumps(analysis, indent=1) + "\n")
print(json.dumps(analysis["counts"]))
print("held out:", [(h["id"], h["why"]) for h in analysis["held_out"]])
print("design mismatches:", [(m["id"], m["design"], m["got"]) for m in analysis["design_mismatch"]])
