"""RV120 (SC): static checks on 07n, written to one JSON: 07m prefix equality; D38's diff from W-C2 sparse; the nine
bases' receipts against their provenance and PP's pinned constants; each 07n entry's origin (RV113's or RV120's
probe: same base and edits, or re-encoded edits that materialize identically; else new) and RV113's stated wants
against the corpus's expectations; the 16 own-class entries against their bases.
Usage: python3 sc_static_checks.py <07m corpus> <07n corpus> <probes json> <PP retained_facade_tests.rs> <P root> <out>"""
import copy
import json
import sys

m, n, probes, pp, root, out = sys.argv[1:7]
a, b = json.load(open(m)), json.load(open(n))
res = {"prefix_equal": {k: b[k][:len(a[k])] == a[k] for k in ("cases", "mutations", "must_pass")},
       "other_keys_equal": {k: a[k] == b[k] for k in b if k not in ("cases", "mutations", "must_pass")},
       "counts": {k: [len(a[k]), len(b[k])] for k in ("cases", "mutations", "must_pass")}}
B = {c["id"]: c for c in b["cases"]}


def diff(x, y, path=""):
    out = []
    if type(x) != type(y):
        return [[path, "type"]]
    if isinstance(x, dict):
        for k in sorted(set(x) | set(y)):
            if k not in x:
                out.append([path + "/" + k, "added"])
            elif k not in y:
                out.append([path + "/" + k, "removed"])
            else:
                out += diff(x[k], y[k], path + "/" + k)
    elif isinstance(x, list):
        if len(x) != len(y):
            out.append([path, f"length {len(x)} -> {len(y)}"])
        else:
            for i, (u, v) in enumerate(zip(x, y)):
                out += diff(u, v, f"{path}/{i}")
    elif x != y:
        out.append([path, f"{str(x)[:60]} -> {str(y)[:60]}"])
    return out


res["d38_vs_w_c2_sparse"] = {"source": diff(B["w_c2_sparse_interactive"]["source"], B["d38_beside_selected"]["source"]),
                             "invocation_equal": B["w_c2_sparse_interactive"]["invocation"] == B["d38_beside_selected"]["invocation"],
                             "qualification": B["d38_beside_selected"]["qualification"]}
pptext = open(pp).read()
prov = []
for c in b["cases"][17:]:
    p, r = c["provenance"], c["source"]["retained_precision"]["receipt_sha256"]
    row = {"id": c["id"], "kind": p.get("kind") if isinstance(p, dict) else p}
    if isinstance(p, dict):
        row.update(receipt_equals_provenance=r == p.get("receipt_sha256"), receipt_in_pp_tests=r in pptext,
                   bytes_sha_in_pp_tests=(p.get("successor_bytes_sha256") in pptext) if p.get("successor_bytes_sha256") else None,
                   solver_mode_equal=p.get("solver_mode") == c["invocation"].get("solver_mode"))
        if "fixture" in p:
            f = json.load(open(f"{root}/{p['fixture']}"))
            row["fixture_source_and_invocation_equal"] = f["source"] == c["source"] and f["invocation"] == c["invocation"]
    prov.append(row)
res["bases_provenance"] = prov


def apply(rootv, edits):
    for e in edits:
        at = rootv
        for k in e["path"][:-1]:
            at = at[k]
        last = e["path"][-1]
        if e["op"] == "remove":
            if isinstance(at, list):
                at.pop(last)
            else:
                del at[last]
        else:
            at[last] = copy.deepcopy(e["value"])
    return rootv


P = {p["id"].split(":", 1)[-1]: p for p in json.load(open(probes))}
origin, stated, agree, disagree = {}, 0, 0, []
for e in b["mutations"][294:] + b["must_pass"][28:]:
    p = P.get(e["id"])
    if not p:
        origin[e["id"]] = "new (PLAN_v2 §2.5 / RR)"
        continue
    same = p["base"] == e["base"] and p["edits"] == e["edits"] and (p.get("invocation_edits") or []) == (e.get("invocation_edits") or [])
    if not same:
        base = B[e["base"]]
        same_mat = (p["base"] == e["base"] and apply(copy.deepcopy(base["source"]), e["edits"]) == apply(copy.deepcopy(base["source"]), p["edits"])
                    and apply(copy.deepcopy(base["invocation"]), e.get("invocation_edits") or []) == apply(copy.deepcopy(base["invocation"]), p.get("invocation_edits") or []))
        origin[e["id"]] = "probe, re-encoded (materializes identically)" if same_mat else "probe, DIFFERENT input"
    else:
        origin[e["id"]] = "probe, same base and edits"
    for v, key in (("bound", "expected"), ("unbound", "expected_unbound"), ("transport", "expected_transport")):
        w = (p.get("want") or {}).get(v)
        if not w or w.get("observe"):
            continue
        stated += 1
        ev = e.get(key)
        if key == "expected" and "expected_by_reader" in e:
            ev = e["expected_by_reader"]["rust"]
        if key == "expected_unbound" and ev is None:
            ev = e.get("expected_unbound_by_reader", {}).get("rust")
        ok = (isinstance(ev, dict) and ev.get("gate") == w["gate"] and ev.get("code") == w["code"]) if "gate" in w else ev == "pass"
        agree += ok
        if not ok:
            disagree.append({"id": e["id"], "verdict": v, "want": w, "corpus": ev})
from collections import Counter
res["entry_origin"] = {"counts": Counter(origin.values()), "new": [k for k, v in origin.items() if v.startswith("new")],
                       "rv113_stated_wants": stated, "agree": agree, "disagree": disagree}
own = []
for e in b["must_pass"][28:]:
    if "expected_classifications" in e:
        bc = B[e["base"]]["expected_classifications"]
        own.append({"id": e["id"], "base_classes": len(bc), "entry_classes": len(e["expected_classifications"]), "differs": bc != e["expected_classifications"]})
res["own_classes"] = own
json.dump(res, open(out, "w"), indent=1, default=dict)
print(json.dumps({"prefix_equal": res["prefix_equal"], "origin": dict(res["entry_origin"]["counts"]), "stated": stated, "agree": agree,
                  "own_classes_all_differ": all(o["differs"] for o in own), "bases_ok": all(all(v for k, v in r.items() if k not in ("id", "kind") and v is not None) for r in prov)}))
