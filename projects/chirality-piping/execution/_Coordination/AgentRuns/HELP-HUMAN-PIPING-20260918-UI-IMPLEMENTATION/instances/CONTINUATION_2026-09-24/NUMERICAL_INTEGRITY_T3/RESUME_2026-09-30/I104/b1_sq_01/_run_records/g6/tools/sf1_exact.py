"""I104 SQ G6 (RV112 SF-1): G5 asserts the c = C late-capture form is exactly C times the c = 1 form,
term by term (and the ordinary-seed form likewise), on the chain's own profile trees.
Usage: python3 sf1_exact.py <profile_tree c=1> <profile_tree c=C> C"""
import json, sys
t1, tc, C = json.load(open(sys.argv[1])), json.load(open(sys.argv[2])), int(sys.argv[3])
out = {}
for name in ("T11_late_capture", "T11_ordinary_seed"):
    f1, fc = t1["forms"][name], tc["forms"][name]
    scaled = {a: C * v for a, v in f1.items()}
    out[name] = {"atoms_c1": len(f1), "atoms_cC": len(fc), "exact_C_times": scaled == fc,
                 "differences": {a: [scaled.get(a), fc.get(a)] for a in set(scaled) | set(fc) if scaled.get(a) != fc.get(a)}}
print(json.dumps(out, indent=1))
sys.exit(0 if all(v["exact_C_times"] for v in out.values()) else 1)
