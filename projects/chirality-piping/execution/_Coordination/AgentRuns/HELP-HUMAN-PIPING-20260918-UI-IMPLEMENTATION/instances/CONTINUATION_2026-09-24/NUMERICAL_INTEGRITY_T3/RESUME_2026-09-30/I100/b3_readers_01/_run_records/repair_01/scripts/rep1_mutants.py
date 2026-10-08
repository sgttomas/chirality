"""I100 B3 repair 01: guarded mutants of the repaired PY reader (I100_MUT names one; unset is the control).
R1 (F1): the exact G5b evidence check back in the per-case shared loop (the placement before the repair).
R2 (PY's B28): G8 step 4's E bits unchecked, in both material-basis loops.
R3 (PY's B29): G8 step 4's G-hat bits unchecked, in both material-basis loops.
R4: R2, and the attempts loop's own binding of each prepared member's old E to the authored material dropped too.
R5: R3, and the attempts loop's own binding of each prepared member's old G-hat to the authored material dropped too.
Usage: rep1_mutants.py <mutant P root>"""
import sys
from pathlib import Path

f = Path(sys.argv[1]) / "core/analysis_runs/retained_precision.py"
G = '__import__("os").environ.get("I100_MUT")'
t = f.read_text()
edits = [
    ('''        absolute = []; uncovered = []
''', f'''        if exact_evidence is not None and {G} == "R1": _g5b_exact_evidence(exact_evidence[0], case, source)
        absolute = []; uncovered = []
''', 1),
    ('''    if exact_evidence is not None:
        # DESIGN''', f'''    if exact_evidence is not None and {G} != "R1":
        # DESIGN''', 1),
    ('''[m["elastic_modulus"],m["shear_modulus"]] == [bits(v) for v in pair])''',
     f'''[m["elastic_modulus"] if {G} not in ("R2", "R4") else bits(pair[0]), m["shear_modulus"] if {G} not in ("R3", "R5") else bits(pair[1])] == [bits(v) for v in pair])''', 2),
    ('''            need(old[:2] == [bits(v) for v in pair] and facts[:2] == [bits(d), bits(wall - tolerance)]''',
     f'''            need([old[0] if {G} != "R4" else bits(pair[0]), old[1] if {G} != "R5" else bits(pair[1])] == [bits(v) for v in pair] and facts[:2] == [bits(d), bits(wall - tolerance)]''', 1),
]
for old, new, count in edits:
    assert t.count(old) == count, old[:60]
    t = t.replace(old, new)
f.write_text(t)
print("R1: the exact G5b evidence check in the shared per-case loop; R2/R3: step 4's E/G-hat bits unchecked; R4/R5: and the attempts loop's old E/G-hat binding too")
