"""RV113 (RV-R): four more mutants for SR-PY repair 02 (2843a59a16), added to the reviewer's mutant copy after P01-P36
(the copy already holds `_mx`). Q17 for S-4, and three (4b) conjuncts that other checks also hold, for N-2.
Usage: python make_py_mutants_r2b.py <P root of the mutant copy> <manifest in/out>
"""
import json
import sys

root = sys.argv[1]
RP = f"{root}/core/analysis_runs/retained_precision.py"
text = open(RP).read()
assert "def _mx(i):" in text
M = json.load(open(sys.argv[2]))


def sub(old, new, mid, item, desc):
    global text
    assert text.count(old) == 1, (mid, text.count(old), old[:90])
    text = text.replace(old, new)
    M.append({"id": mid, "item": item, "description": desc})


sub('''            fail(c["product_attempt_ref"] is None and verdict == "checks_passed")''',
    '''            fail((_mx("P37") or c["product_attempt_ref"] is None) and verdict == "checks_passed")''',
    "P37", "S-4", "Q17: not_required without its product_attempt_ref null conjunct")
sub('''    return (case.get("run") is None and a["proof"] is None''',
    '''    return ((_mx("P38") or case.get("run") is None) and a["proof"] is None''',
    "P38", "N-2", "(4b): the case's Run absent dropped")
sub('''            and case["status"] == "unavailable" and cause.get("kind") == "prepared_product_failure"
            and cause.get("product_attempt_ref") == ai''',
    '''            and (_mx("P39") or case["status"] == "unavailable") and cause.get("kind") == "prepared_product_failure"
            and (_mx("P40") or cause.get("product_attempt_ref") == ai)''',
    "P39", "N-2", "(4b): the case's status unavailable dropped")
M.append({"id": "P40", "item": "N-2", "description": "(4b): the cause naming this attempt dropped"})
open(RP, "w").write(text)
json.dump(M, open(sys.argv[2], "w"), indent=1)
print(len(M), "mutants")
