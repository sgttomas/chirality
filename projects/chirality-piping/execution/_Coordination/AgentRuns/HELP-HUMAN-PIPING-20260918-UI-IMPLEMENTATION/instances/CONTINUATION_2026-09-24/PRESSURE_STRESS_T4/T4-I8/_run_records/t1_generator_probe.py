"""T4-I8 repair 01 (T4-RV4 S-1): feed every row of rebuilt_reference_cases.json through T1's own
generator functions, unmodified, as the exact_pressure_1 package generator would.

Usage: python -I t1_generator_probe.py <generate_reference_values.py extracted at ed012c7ccf> <rebuilt_reference_cases.json>

For each row: origin_value(document, reference_origin, row unit) and, for zero rows,
zero_scale_value(document, zero_scale, row unit). The probe reports which rows T1's generator
accepts, which it refuses and why, and checks the accepted values against the file's binary64
projection converted into the row unit and the precomputed zero tolerances.
"""
import importlib.util
import json
import sys
from collections import Counter
from decimal import Decimal


def main():
    spec = importlib.util.spec_from_file_location("t1_generator", sys.argv[1])
    gen = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gen)
    doc = json.loads(open(sys.argv[2], "rb").read())
    accepted, refused, bad = 0, Counter(), []
    for key, case in doc["cases"].items():
        holders = [case] + list(case.get("variants", {}).values())
        for h in holders:
            for cid, lc in h.get("load_cases", {}).items():
                for r in lc["rows"]:
                    o = r["reference_origin"]
                    label = f"{key}/{cid}/{r['kind']}/{r['entity_ref']}/{r['location']}/{r['component']}"
                    try:
                        value = gen.origin_value(doc, o, r["unit"], label)
                        if "zero_scale" in o:
                            scale = gen.zero_scale_value(doc, o["zero_scale"], r["unit"], label)
                            tol = gen.to_binary64(gen.RELATIVE * scale)
                            if value != 0 or tol != r["criterion"]["absolute_tolerance"]:
                                bad.append(f"{label}: zero {value} tol {tol} vs {r['criterion']['absolute_tolerance']}")
                        else:
                            q = gen.resolve(doc, o["pointer"])
                            factor = gen.UNIT_FACTORS[(o["reference_unit"], r["unit"])]
                            want = gen.to_binary64(gen.exact_decimal(doc, q, o["pointer"]) * factor)
                            if gen.to_binary64(value) != want:
                                bad.append(f"{label}: {value} != {want}")
                        accepted += 1
                    except gen.GenerationError as error:
                        text = str(error)
                        reason = ("unit factor Pa->MPa not in UNIT_FACTORS" if "Pa -> MPa" in text
                                  else "symbolic form outside T1's exp pattern" if "symbolic" in text
                                  else text)
                        refused[reason] += 1
    print(f"rows accepted by T1's generator functions: {accepted}")
    for reason, n in sorted(refused.items()):
        print(f"rows refused: {n}  ({reason})")
    for line in bad:
        print("MISMATCH", line)
    expected_refusals = {"unit factor Pa->MPa not in UNIT_FACTORS", "symbolic form outside T1's exp pattern"}
    ok = not bad and set(refused) <= expected_refusals and refused["symbolic form outside T1's exp pattern"] == 3
    print("RESULT:", "PASS (only the declared refusals)" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
