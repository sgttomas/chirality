#!/usr/bin/env python3
"""I106 B1 SG: the Direct-entry gates' comparer (adapted from I61's u9_g8_01 compare_g8.py).

Usage: compare_sg.py OUT_DIR CAND_FIXTURES BASE_FIXTURES OUT_JSON
  OUT_DIR holds sweep_{cand,base}_{reg,stale}.tsv and gates_{cand,base}_{reg,stale}.json (+ successor dumps).
  CAND_FIXTURES / BASE_FIXTURES are the copies' P/fixtures directories.
Standard library only. Prints a summary; exit 1 on any failed check or unexplained sweep row.

Gate 3's rule (PLAN_v2 §3.10): Stale must be byte-identical to base; every registered difference is
listed row by row and must be explained by T-4, D1.4's widening or T-12. Each explanation is a
predicate over the two rows and the fixture, checked here:
  D1.4  base refused the request at D1.4 (c != 1), the fixture has 2 <= c <= 3 load cases and no
        combination or component, and the candidate passes D1.4;
  T-12  (with D1.4) the candidate's W1 work ran and fell back: the ordinary bytes plus one N1
        notice per case in A, in request order (`notice` / `notice_x<k>`, the harness's check);
  T-4   a c = 1 request admitted in both, whose base W1 ran (a W1 cause or a successor) and whose
        candidate cause is NoTriggeredCase with the exact ordinary bytes (T-4's only return).
Every other differing row, and any difference on a typed, value or Headless route, is UNEXPLAINED.
"""
import hashlib, json, os, sys

out_dir, cand_fix, base_fix, out_json = sys.argv[1:5]
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
P = lambda name: os.path.join(out_dir, name)

def load(p):
    rows = {}
    for line in open(p).read().splitlines():
        rel, route, mode, rest = line.split("\t", 3)
        rows[(rel, route, mode)] = rest
    return rows

CR, CS, BR, BS = (load(P(f"sweep_{t}_{b}.tsv")) for t, b in (("cand", "reg"), ("cand", "stale"), ("base", "reg"), ("base", "stale")))
rep = {"sweep": {}, "registered_differences": [], "coexistence": [], "gates": [], "failures": []}
fail = rep["failures"].append

def fixture_shape(rel):
    shapes = {}
    for side, root in (("cand", cand_fix), ("base", base_fix)):
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            shapes[side] = None
            continue
        v = json.load(open(path))
        m = v["model"] if "model" in v else v
        shapes[side] = {"sha256": sha(path), "cases": len(m.get("load_cases") or []),
                        "combinations": len(m.get("combinations") or []), "components": len(m.get("components") or [])}
    return shapes

W1_CAUSES = ("Preparation", "Native", "Candidate", "Staging(", "Serializer(", "Precommit")

def fields(v):
    if v is None or v.startswith("ERR:") or v == "PANIC":
        return None
    sha_, cls, report, cause = v.split("\t")
    return {"sha": sha_, "class": cls, "report": report, "cause": cause}

def explain(key, base_v, cand_v):
    rel, route, mode = key
    if route != "retained_direct":
        return None, f"route {route} differs"
    b, c = fields(base_v), fields(cand_v)
    if b is None or c is None:
        return None, "an ERR/PANIC/missing row"
    shape = fixture_shape(rel)
    if shape["cand"] != shape["base"]:
        return None, "the fixture differs between base and candidate"
    s = shape["cand"]
    value = CR.get((rel, "value_mode", mode), "").split("\t")[0]
    tags, why = [], []
    if b["report"] == "Some((Registered, Some(\"D1.4\")))" and "D1.4" not in c["report"] and c["report"].startswith("Some((Registered,") \
            and 2 <= s["cases"] <= 3 and s["combinations"] == 0 and s["components"] == 0:
        tags.append("D1.4")
        why.append(f"base refused c = {s['cases']} at D1.4 (C = 1); the candidate's D1.4 admits 1 <= c <= 3, then {c['report']} / {c['cause']}")
        if c["class"].startswith("notice"):
            k = 1 if c["class"] == "notice" else int(c["class"].split("_x")[1])
            if not c["cause"].startswith(W1_CAUSES):
                return None, "a notice without W1 work"
            tags.append("T-12")
            why.append(f"W1 ran on {k} case(s) in A and fell back ({c['cause']}): the ordinary bytes plus {k} N1 notice(s) in request order")
        elif c["class"] == "exact":
            if c["sha"] != value:
                return None, "exact class but not the value route's bytes"
            if c["cause"].startswith(W1_CAUSES) or c["cause"] == "successor":
                return None, "W1 work ran but no notice"
            if c["cause"] == "NoTriggeredCase":
                tags.append("T-4")
                why.append("no case in A: T-4's NoTriggeredCase, the exact ordinary bytes")
        elif c["class"] == "successor":
            if c["cause"] != "successor":
                return None, "successor class without a successor cause"
            why.append("a precommit-validated multi-case successor")
        else:
            return None, f"class {c['class']}"
        return tags, "; ".join(why)
    if s["cases"] == 1 and b["report"] == c["report"] == "Some((Registered, None))" \
            and (b["cause"].startswith(W1_CAUSES) or b["cause"] == "successor") \
            and c["cause"] == "NoTriggeredCase" and c["class"] == "exact" and c["sha"] == value:
        return ["T-4"], f"c = 1 admitted in both; base W1 ran ({b['class']}, {b['cause']}); the candidate's T-4 finds no case in A: NoTriggeredCase, the exact ordinary bytes"
    return None, "no rule applies"

for name, cur, base, cp, bp in (("registered", CR, BR, P("sweep_cand_reg.tsv"), P("sweep_base_reg.tsv")),
                                ("stale", CS, BS, P("sweep_cand_stale.tsv"), P("sweep_base_stale.tsv"))):
    diff = sorted(k for k in set(cur) | set(base) if cur.get(k) != base.get(k))
    rep["sweep"][name] = {"rows": len(cur), "base_rows": len(base), "sha256": sha(cp), "base_sha256": sha(bp),
                          "identical": sha(cp) == sha(bp), "differing_rows": len(diff)}
    if name == "stale":
        if diff or sha(cp) != sha(bp):
            fail(f"sweep stale: {len(diff)} rows differ from base (must be byte-identical)")
        rep["sweep"][name]["rows_listed"] = [[*k, base.get(k), cur.get(k)] for k in diff]
        continue
    for k in diff:
        tags, why = explain(k, base.get(k), cur.get(k))
        rep["registered_differences"].append({"fixture": k[0], "route": k[1], "mode": k[2], "base": base.get(k), "candidate": cur.get(k),
                                              "explained_by": tags, "explanation": why, "shape": fixture_shape(k[0])})
        if tags is None:
            fail(f"UNEXPLAINED registered row {k}: {why}")

# Stale sanity: every Stale Direct row is the exact value-route bytes, refused at D1.1, cause none.
for k, v in CS.items():
    if k[1] == "retained_direct" and not v.startswith("ERR:"):
        f = fields(v)
        if not (f and f["class"] == "exact" and f["report"] == 'Some((Stale, Some("D1.1")))' and f["cause"] == "none"
                and f["sha"] == CS[(k[0], "value_mode", k[2])].split("\t")[0]):
            fail(f"stale Direct row not exact at D1.1: {k} {v}")

# Registered Direct classes and causes, both trees.
for tag, rows in (("candidate", CR), ("base", BR)):
    classes, causes, reports = {}, {}, {}
    for k, v in rows.items():
        if k[1] == "retained_direct" and not v.startswith("ERR:"):
            f = fields(v)
            classes[f["class"]] = classes.get(f["class"], 0) + 1
            causes[f["cause"]] = causes.get(f["cause"], 0) + 1
            reports[f["report"]] = reports.get(f["report"], 0) + 1
    rep["sweep"][f"registered_direct_{tag}"] = {"classes": classes, "causes": causes, "reports": reports}

# Gate 2 (sweep part): n05/n06 source-block fixtures through Direct, candidate.
for k in sorted(CR):
    if k[1] == "retained_direct" and ("/n05-" in "/" + k[0] or "/n06-" in "/" + k[0]):
        rc, sc = CR[k].split("\t"), CS[k].split("\t")
        row = {"fixture": k[0], "mode": k[2], "registered": rc[1:], "stale": sc[1:],
               "direct_equals_value_registered": rc[0] == CR[(k[0], "value_mode", k[2])].split("\t")[0],
               "direct_equals_value_stale": sc[0] == CS[(k[0], "value_mode", k[2])].split("\t")[0],
               "registered_equals_base": CR[k] == BR.get(k)}
        rep["coexistence"].append(row)
        ok = (rc[1] == "exact" and rc[2] == "Some((Registered, None))" and rc[3] == "Coexistence" and row["direct_equals_value_registered"]
              and sc[1] == "exact" and sc[2] == 'Some((Stale, Some("D1.1")))' and sc[3] == "none" and row["direct_equals_value_stale"])
        if not ok:
            fail(f"coexistence {k}: {rc[1:]} / {sc[1:]}")
if not rep["coexistence"]:
    fail("no n05/n06 rows found")

# Gates 1 and 2 (the harness): candidate registered and Stale, base registered for comparison.
G = {}
for t in ("cand", "base"):
    for b in ("reg", "stale"):
        G[(t, b)] = {(r["label"], r["mode"]): r for r in json.load(open(P(f"gates_{t}_{b}.json")))}
FIX = os.path.join(cand_fix, "results")
for (label, mode), r in sorted(G[("cand", "reg")].items()):
    s, br = G[("cand", "stale")][(label, mode)], G[("base", "reg")].get((label, mode), {})
    checks = {}
    checks["stale_exact_at_D1_1_build"] = s.get("class") == "exact" and s.get("clause") == "D1.1" and s.get("cause") == "none" \
        and s.get("notices") == 0 and s.get("profile") == "Stale" and s.get("direct_sha") == s.get("value_sha")
    checks["value_route_same_in_both_builds"] = r.get("value_sha") == s.get("value_sha")
    if br.get("direct") != "ABSENT" and br:
        checks["value_route_same_as_base"] = r.get("value_sha") == br.get("value_sha")
    if label in ("milestone", "w_c2"):
        name = "milestone" if label == "milestone" else "w_c2"
        pinned = json.load(open(os.path.join(FIX, f"retained_precision_{name}_successor_{mode}.json")))
        dump = P(f"gates_cand_reg.json.successor_{label}_{mode}.json")
        checks["registered_successor_equals_pinned_fixture"] = r.get("class") == "successor" and r.get("profile") == "Registered" \
            and r.get("refusal") is None and os.path.exists(dump) and json.load(open(dump)) == pinned["source"] \
            and pinned["invocation"]["solver_mode"] == mode
        checks["registered_no_n1_notice"] = r.get("n1_notices") == 0
    else:
        checks["registered_exact_no_notice"] = r.get("class") == "exact" and r.get("notices") == 0 and r.get("profile") == "Registered" \
            and r.get("direct_sha") == r.get("value_sha")
    if label in ("milestone_with_pressure", "milestone_two_cases_pressure_on_second"):
        checks["refused_at_D1_5_pressure_regions"] = r.get("clause") == "D1.5" and r.get("refusal") == "Family(Case, PressureRegions)" \
            and r.get("cause") == "none"
    if label == "milestone_two_cases_pressure_on_second":
        checks["two_cases"] = r.get("load_cases") == 2
    if label == "phys_r4_pressurized":
        checks["refused_at_D1_namespace"] = r.get("clause") == "D1.3" and "Namespace" in (r.get("refusal") or "")
        checks["ordinary_refusal_numerical_integrity"] = r.get("value_status") == "MODEL_INCOMPLETE" and r.get("value_blocking") == ["NUMERICAL_INTEGRITY_UNRESOLVED"]
    if label == "phys_r4_without_pressure":
        checks["refused_at_D1_namespace"] = r.get("clause") == "D1.3" and "Namespace" in (r.get("refusal") or "")
        checks["no_pressure_published"] = r.get("value_status") == "MECHANICS_SOLVED" and r.get("value_blocking") == []
    if label == "n05_two_cases":
        checks["multi_case_coexistence_admitted"] = r.get("refusal") is None and r.get("cause") == "Coexistence" and r.get("load_cases") == 2
    rep["gates"].append({"label": label, "mode": mode, "candidate_registered": r, "candidate_stale": s, "base_registered": br, "checks": checks})
    for c, v in checks.items():
        if not v:
            fail(f"gate {label} {mode}: {c}")

json.dump(rep, open(out_json, "w"), indent=1)
open(out_json, "a").write("\n")
for name in ("registered", "stale"):
    s = rep["sweep"][name]
    print(f"sweep {name}: rows {s['rows']} (base {s['base_rows']}) sha {s['sha256'][:16]} base {s['base_sha256'][:16]} identical {s['identical']} differing {s['differing_rows']}")
for tag in ("candidate", "base"):
    d = rep["sweep"][f"registered_direct_{tag}"]
    print(f"registered Direct {tag}: classes {d['classes']} causes {d['causes']}")
for d in rep["registered_differences"]:
    print("DIFF", d["fixture"], d["route"], d["mode"], "| base", (d["base"] or "")[66:] if d["base"] else None, "| cand", (d["candidate"] or "")[66:] if d["candidate"] else None, "|", d["explained_by"], "|", d["explanation"])
for c in rep["coexistence"]:
    print("coexistence", c["fixture"], c["mode"], c["registered"], c["stale"][:2], "= base", c["registered_equals_base"])
for g in rep["gates"]:
    r, s, b = g["candidate_registered"], g["candidate_stale"], g["base_registered"]
    print("gate", g["label"], g["mode"], "| reg", r.get("class"), r.get("clause"), r.get("refusal"), r.get("cause"), "notices", r.get("notices"), r.get("n1_notices"),
          "| stale", s.get("class"), s.get("clause"), "| base reg", b.get("class"), b.get("clause"), b.get("refusal"), b.get("cause"), "| all", all(g["checks"].values()))
print("FAILURES", rep["failures"])
sys.exit(1 if rep["failures"] else 0)
