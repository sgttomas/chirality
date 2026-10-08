#!/usr/bin/env python3
"""I109: check every published magnitude row in a document against its component rows.

For each support/combination magnitude row whose components are present (same entity, basis,
kind family), compare the published value with the exact correctly rounded 3-norm and with the
exact correctly rounded chain RN(hypot(RN(hypot(x, y)), z)). Intensified rows are checked against
RN(i * (RN(|(My, Mz)|) / Z)) with the measure's inputs. Usage: analyze_magnitudes.py <doc.json> [...]
A document may be an envelope ({results, ...}) or a successor/W-C2 wrapper (source.results).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import norm_oracle as o  # noqa: E402

PAIRS = {
    "support_reaction_force_magnitude_v2": ("support_reaction_component_v2", ["Fx", "Fy", "Fz"]),
    "support_reaction_moment_magnitude_v2": ("support_reaction_component_v2", ["Mx", "My", "Mz"]),
}


def results_of(doc):
    if "results" in doc:
        return doc["results"]
    if "source" in doc and "results" in doc["source"]:
        return doc["source"]["results"]
    return []


def comp(row):
    md = row.get("metadata") or {}
    return md.get("component")


def basis(row):
    b = row.get("basis_ref") or {}
    return (b.get("ref_type"), b.get("ref_id"))


def analyse(doc):
    rows = results_of(doc)
    index = {}
    for r in rows:
        index.setdefault((r.get("kind"), r.get("entity_ref"), basis(r), comp(r)), []).append(r)
    out = {"magnitudes": 0, "eq_norm3": 0, "eq_chain": 0, "eq_both": 0, "neither": [], "intensified": 0, "intensified_cr": 0}
    for r in rows:
        k = r.get("kind")
        parts = None
        if k in PAIRS:
            ck, names = PAIRS[k]
            parts = [index.get((ck, r.get("entity_ref"), basis(r), n)) for n in names]
        elif comp(r) in ("force_magnitude", "moment_magnitude") and k and "support" in k:
            names = ["Fx", "Fy", "Fz"] if comp(r) == "force_magnitude" else ["Mx", "My", "Mz"]
            cands = [[x for x in rows if x.get("entity_ref") == r.get("entity_ref") and basis(x) == basis(r) and comp(x) == n and x.get("kind") == k] for n in names]
            parts = cands
        if parts is None or not all(p and len(p) == 1 for p in parts):
            continue
        xs = [float(p[0]["value"]) for p in parts]
        v = float(r["value"])
        n3, ch = o.ref_norm(xs), o.ref_chain(*xs)
        out["magnitudes"] += 1
        a, b = o.same(v, n3), o.same(v, ch)
        out["eq_norm3"] += a
        out["eq_chain"] += b
        out["eq_both"] += a and b
        if not a and not b:
            out["neither"].append({"id": r.get("id"), "value": v, "norm3": n3, "chain": ch})
    return out


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(json.dumps({"doc": os.path.basename(p), **analyse(json.load(open(p)))}))
