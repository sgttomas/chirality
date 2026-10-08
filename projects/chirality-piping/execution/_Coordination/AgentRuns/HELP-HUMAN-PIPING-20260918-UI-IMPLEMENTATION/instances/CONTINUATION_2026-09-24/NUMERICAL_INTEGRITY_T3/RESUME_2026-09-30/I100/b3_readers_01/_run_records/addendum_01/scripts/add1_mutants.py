"""I100 B3 addendum 01: the guarded mutants of the aligned sourced-case check (I100_MUT names one).
Usage: add1_mutants.py <mutant P root>"""
import sys
from pathlib import Path

f = Path(sys.argv[1]) / "core/analysis_runs/retained_precision.py"
G = '__import__("os").environ.get("I100_MUT")'
t = f.read_text()
old = '''            need((regions is None or (type(regions) is list and regions == [])) and case.get("equivalent_static") is None
                 and "analysis_state" not in case)'''
new = f'''            need(((not regions) if {G} == "C2" else (regions is None or (type(regions) is list and ({G} == "C3" or regions == []))))
                 and case.get("equivalent_static") is None and ("analysis_state" not in case or {G} == "C1"))'''
assert t.count(old) == 1
f.write_text(t.replace(old, new))
print("C1: analysis_state admitted on the preview route; C2: pressure_regions read as falsy (the old PY reading); C3: any list admitted")
