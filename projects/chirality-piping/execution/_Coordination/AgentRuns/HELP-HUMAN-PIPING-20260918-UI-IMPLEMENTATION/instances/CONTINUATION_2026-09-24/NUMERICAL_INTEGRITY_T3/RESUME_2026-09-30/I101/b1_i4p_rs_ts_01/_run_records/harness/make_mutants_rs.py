"""I101: RS's mutant schema at the b1-r head, in a scratch copy only (never committed).

First RV113's own schema (`make_mutants_r2.py`, applied unchanged: its 61 mutants N01-N65, guarded by mx(id), which
reads RV113_MUT), then I101's two mutants of ruling 2's new demand, under the same guard:
  X01  "extrema numbers": global_upper_bound_pa's conjunct dropped
  X02  "extrema numbers": certified_gap_pa's conjunct dropped
Usage: python make_mutants_rs.py <make_mutants_r2.py> <RE dir> <manifest out>
"""
import json
import runpy
import sys

rv113, re_dir, manifest_out = sys.argv[1], sys.argv[2], sys.argv[3]
sys.argv = [rv113, re_dir, manifest_out]
runpy.run_path(rv113, run_name="__main__")
manifest = json.load(open(manifest_out))
path = f"{re_dir}/src/retained_precision.rs"
rs = open(path).read()
old = '''                ["global_upper_bound_pa", "certified_gap_pa"]
                    .iter()
                    .all(|k| number(&x[*k]).is_some()),
                "extrema numbers",'''
new = '''                ["global_upper_bound_pa", "certified_gap_pa"]
                    .iter()
                    .all(|k| (mx("X01") && *k == "global_upper_bound_pa") || (mx("X02") && *k == "certified_gap_pa") || number(&x[*k]).is_some()),
                "extrema numbers",'''
assert rs.count(old) == 1, rs.count(old)
rs = rs.replace(old, new)
open(path, "w").write(rs)
manifest += [
    {"id": "X01", "item": "ruling 2", "description": "transport 'extrema numbers': the global_upper_bound_pa conjunct dropped"},
    {"id": "X02", "item": "ruling 2", "description": "transport 'extrema numbers': the certified_gap_pa conjunct dropped"},
]
json.dump(manifest, open(manifest_out, "w"), indent=1)
print(len(manifest), "mutants")
