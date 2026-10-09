"""T4-I8: consumer-side check of rebuilt_reference_cases.json (standard library only).

Usage: python -I check_reference_json.py <rebuilt_reference_cases.json>

Checks, on the written bytes only:
1. every quantity's `exact` re-evaluates (Decimal, 120 digits, pi from the file) to its `decimal`
   within 1e-80 relative and to its `value` bitwise (the load_reference_1 generator rule);
2. every row names an existing expected quantity; zero expectations carry a zero scale that exists,
   is nonzero, and whose precomputed absolute tolerance equals 1e-9 * |scale|;
3. every wrong-result discriminator differs from the correct value of its quantity under the
   negative-assertion rule where the quantity is resolvable by name;
4. every document sketch parses, and the v2 0.3.0/0.4.0 documents agree on geometry, materials'
   E/nu, supports and pressure regions.
"""
import json
import sys
from decimal import Decimal, getcontext

getcontext().prec = 120
fails = []
counts = {"quantities": 0, "rows": 0, "zero_rows": 0, "discriminators": 0, "documents": 0}


def fail(msg):
    fails.append(msg)
    print("FAIL", msg)


def frac(text):
    if "/" in text:
        n, d = text.split("/")
        return Decimal(int(n)) / Decimal(int(d))
    return Decimal(int(text))


def evaluate(q, pi):
    e = q["exact"]
    k = e["kind"]
    if k == "rational":
        return frac(e["rational"])
    if k == "rational_times_pi":
        return frac(e["rational"]) * pi
    if k == "rational_over_pi":
        return frac(e["rational"]) / pi
    if k == "symbolic":
        # only sqrt((A*pi)^2 + (B)^2) occurs
        expr = e["expression"]
        inner = expr[len("sqrt(("):-1]
        a_txt, b_txt = inner.split("*pi)^2 + (")
        b_txt = b_txt.rstrip(")^2").rstrip(")")
        a, b = frac(a_txt), frac(b_txt)
        return ((a * pi) ** 2 + b ** 2).sqrt()
    raise ValueError(k)


def walk(node, path, pi):
    if isinstance(node, dict):
        if "exact" in node and "decimal" in node and "value" in node:
            counts["quantities"] += 1
            v = evaluate(node, pi)
            d = Decimal(node["decimal"])
            if v != 0 and abs(d - v) > abs(v) * Decimal(10) ** -80:
                fail(f"{path}: decimal disagrees with exact")
            if v == 0 and d != 0:
                fail(f"{path}: nonzero decimal for zero")
            if float(v) != node["value"]:
                fail(f"{path}: value not the binary64 rounding of exact")
            return
        for key, child in node.items():
            walk(child, f"{path}/{key}", pi)
    elif isinstance(node, list):
        for i, child in enumerate(node):
            walk(child, f"{path}/{i}", pi)


def check_load_case(name, lc):
    exp, scales = lc["expected"], lc["zero_scales"]
    for r in lc["rows"]:
        counts["rows"] += 1
        q = exp.get(r["expected"])
        if q is None:
            fail(f"{name}: row expects missing {r['expected']}")
            continue
        if q["value"] == 0:
            counts["zero_rows"] += 1
            c = r["criterion"]
            sc = scales.get(c.get("zero_scale_ref", ""))
            if c["kind"] != "zero_scale" or sc is None or sc["value"] == 0:
                fail(f"{name}: zero row without a valid scale {r}")
            elif abs(c["absolute_tolerance"] - 1e-9 * abs(sc["value"])) > 1e-24 * abs(sc["value"]):
                fail(f"{name}: zero tolerance mismatch {r}")
            elif sc["unit"] != q["unit"]:
                fail(f"{name}: zero-scale unit {sc['unit']} != reference unit {q['unit']}")
        else:
            if r["criterion"]["kind"] != "relative" or r["criterion"]["relative_tolerance"] != 1e-9:
                fail(f"{name}: nonzero row without relative 1e-9 {r}")
    keys = [(r["kind"], r["entity_ref"], r["component"], r["location"]) for r in lc["rows"]]
    if len(keys) != len(set(keys)):
        fail(f"{name}: duplicate row selectors")


def distinct(correct, wrong):
    return abs(correct - wrong) > 1e-9 * max(abs(correct), abs(wrong))


def check_documents(name, docs):
    d3, d4 = docs["v2_model_0.3.0"]["model"], docs["v2_model_0.4.0"]["model"]
    counts["documents"] += 2
    if d3["schema_version"] != "0.3.0" or d4["schema_version"] != "0.4.0":
        fail(f"{name}: schema versions")
    for key in ("nodes", "pipe_segments", "supports"):
        if d3[key] != d4[key]:
            fail(f"{name}: {key} differ between 0.3.0 and 0.4.0")
    for m3, m4 in zip(d3["materials"], d4["materials"]):
        if (m3["elastic_modulus"], m3["poisson_ratio"]) != (m4["elastic_modulus"], m4["poisson_ratio"]):
            fail(f"{name}: material E/nu differ")
    for c3, c4 in zip(d3["load_cases"], d4["load_cases"]):
        if c3["pressure_regions"] != c4["pressure_regions"]:
            fail(f"{name}: regions differ")
        th3 = {l["target"]["pipe"]: l["magnitude"]["value"] for l in c3["primitive_loads"] if l["category"] == "thermal"}
        th4 = {e["pipe_ref"]: e["thermal_state"]["temperature_change"]["value"] for e in c4["analysis_state"]["element_states"]
               if e["thermal_state"]["kind"] == "constant_alpha_interval"}
        if th3 != th4:
            fail(f"{name}: thermal states differ {th3} {th4}")
        src = {s["source_ref"] for s in c4["analysis_state"]["load_sources"]}
        if src != {l["id"] for l in c4["primitive_loads"]} or any(l["category"] == "thermal" for l in c4["primitive_loads"]):
            fail(f"{name}: 0.4.0 load sources incomplete or a thermal primitive remains")
        if {s["support_ref"] for s in c4["analysis_state"]["support_states"]} != {s["id"] for s in d4["supports"]}:
            fail(f"{name}: support states incomplete")
    if docs["v3_patch_for_both"]["value"] != {"version": "3.0.0", "mode": "exact_pressure_v3"}:
        fail(f"{name}: v3 patch")


def main():
    raw = open(sys.argv[1], "rb").read()
    doc = json.loads(raw)
    pi = Decimal(doc["numeric_representation"]["pi_decimal"])
    walk(doc, "", pi)
    cases = doc["cases"]
    # rows
    for key, case in cases.items():
        holders = [case] + list(case.get("variants", {}).values())
        for h in holders:
            for cid, lc in h.get("load_cases", {}).items():
                check_load_case(f"{key}/{cid}", lc)
            if "documents" in h:
                check_documents(key, h["documents"])
    # discriminators resolvable by name
    m = cases["milltol_lame_membrane"]
    mf = list(m["variants"]["free_transferring"]["load_cases"].values())[0]["expected"]
    mr = list(m["variants"]["axially_restrained_transferring"]["load_cases"].values())[0]["expected"]
    target = {"lame_inner_hoop": mf["lame_inner_hoop"]["value"], "sigma_z (free)": mf["sigma_z"]["value"],
              "sigma_z (restrained)": mr["sigma_z"]["value"], "Nw (restrained)": mr["Nw"]["value"]}
    for dsc in m["wrong_result_discriminators"]:
        counts["discriminators"] += 1
        if not distinct(target[dsc["quantity"]], dsc["wrong"]["value"]):
            fail(f"milltol discriminator {dsc['id']} not distinct")
    t = cases["tp_phys_pressure_halves"]["load_cases"]
    for dsc in cases["tp_phys_pressure_halves"]["wrong_result_discriminators"]:
        counts["discriminators"] += 1
        e = t[dsc["case"]]["expected"]
        name = {"Nw": "Nw", "S": "S", "support:A Fx": "A_Fx", "support:A Mz": "A_Mz",
                "pipe:A-B midspan bending_moment_z": "A-B_midspan_bending_moment_z", "node:D uy": "D_uy"}[dsc["quantity"]]
        if not distinct(e[name]["value"], dsc["wrong"]["value"]):
            fail(f"tp discriminator {dsc['id']} not distinct")
    c3 = cases["pressure_membrane_thin_wall_limit"]["load_cases"]["case:membrane-free"]["expected"]
    for dsc in cases["pressure_membrane_thin_wall_limit"]["wrong_result_discriminators"]:
        counts["discriminators"] += 1
        names = ["lame_inner_hoop", "lame_outer_hoop"] if "outer" in dsc["quantity"] else (["sigma_z"] if dsc["quantity"] == "sigma_z" else ["lame_inner_hoop"])
        for n in names:
            if not distinct(c3[n]["value"], dsc["wrong"]["value"]):
                fail(f"membrane discriminator {dsc['id']} vs {n} not distinct")
    # spot identities on written values
    e = t["case:combined"]["expected"]
    if not (e["A_Fx"]["value"] == -e["S"]["value"] and e["D_Fx"]["value"] == e["S"]["value"]):
        fail("combined: root Fx != -S or stop Fx != S")
    if not e["Nw"]["value"] < 0 < t["case:pressure-half"]["expected"]["Nw"]["value"]:
        fail("sign: pressure-half Nw must be tension and combined Nw compression")
    print("counts:", json.dumps(counts, sort_keys=True))
    print("RESULT:", "PASS" if not fails else f"FAIL ({len(fails)})")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
