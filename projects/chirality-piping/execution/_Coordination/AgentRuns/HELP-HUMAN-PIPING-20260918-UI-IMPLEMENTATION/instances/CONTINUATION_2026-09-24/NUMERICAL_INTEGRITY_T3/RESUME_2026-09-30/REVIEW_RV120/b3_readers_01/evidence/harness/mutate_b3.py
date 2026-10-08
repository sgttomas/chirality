"""RV120 (B3): apply or revert one of I101's B28/B29 mutants (its exact strings) in the reviewer's mutant copy.
Usage: mutate_b3.py <P> <orig P> <id> apply|revert"""
import sys, pathlib
P, O, mid, act = sys.argv[1:5]
RS = "core/reporting/result_export/src/retained_precision.rs"; TS = "apps/desktop/src/features/results/retainedPrecision.ts"
M = {"B28": [(RS, '                        && m["elastic_modulus"] == bits(e)\n', ''), (TS, " && m.elastic_modulus === binary64Bits(e)", "")],
     "B29": [(RS, '                        && m["shear_modulus"] == bits(g),', '                        ,'), (TS, " && m.shear_modulus === binary64Bits(g));", ");")]}
for f, a, b in M[mid]:
    p = pathlib.Path(P) / f; t = p.read_text()
    if act == "apply": assert t.count(a) == 1, (mid, f); p.write_text(t.replace(a, b))
    else: p.write_text((pathlib.Path(O) / f).read_text())
print(mid, act, "ok")
