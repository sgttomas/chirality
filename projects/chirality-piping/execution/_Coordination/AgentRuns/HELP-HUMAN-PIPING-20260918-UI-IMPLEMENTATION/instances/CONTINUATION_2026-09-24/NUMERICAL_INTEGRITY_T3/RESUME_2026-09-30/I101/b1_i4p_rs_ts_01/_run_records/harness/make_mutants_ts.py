"""I101: TS's mutant schema at the b1-t head, in a scratch copy only (never committed). Each mutant is an edit of
previewPhysicsEvidence.ts guarded by mx(id), true only when the environment's I101_MUT equals the id; with I101_MUT
unset the copy behaves as the head (a control run checks it).
  Y01  "extrema numbers" (readCases, raw and transport): global_upper_bound_pa's conjunct dropped
  Y02  "extrema numbers" (readCases, raw and transport): certified_gap_pa's conjunct dropped
Usage: python make_mutants_ts.py <previewPhysicsEvidence.ts> <manifest out>
"""
import json
import sys

path, manifest_out = sys.argv[1], sys.argv[2]
ts = open(path).read()
anchor = "const TINY = 2.2250738585072014e-308; // binary64 minimum positive normal\n"
assert ts.count(anchor) == 1
ts = ts.replace(anchor, anchor + "const mx = (id: string): boolean => (globalThis as any).process?.env?.I101_MUT === id;\n")
old = 'demand(finite(x.global_upper_bound_pa) && finite(x.certified_gap_pa), "extrema numbers");'
new = 'demand((mx("Y01") || finite(x.global_upper_bound_pa)) && (mx("Y02") || finite(x.certified_gap_pa)), "extrema numbers");'
assert ts.count(old) == 1
ts = ts.replace(old, new)
open(path, "w").write(ts)
manifest = [
    {"id": "Y01", "item": "rulings 2 and 3", "description": "readCases 'extrema numbers': the global_upper_bound_pa conjunct dropped"},
    {"id": "Y02", "item": "rulings 2 and 3", "description": "readCases 'extrema numbers': the certified_gap_pa conjunct dropped"},
]
json.dump(manifest, open(manifest_out, "w"), indent=1)
print(len(manifest), "mutants")
