"""RV120 (RV-R): my own RS mutants on ruling 2's new check, added on top of RV113's schema (make_mutants_r2.py, run
first on the same copy, which defines `mx` on RV113_MUT). One build serves all. Each anchor must match exactly once.
Usage: python3 make_mutants_rv120_rs.py <RE dir> <manifest out>
"""
import json
import sys

re_dir, manifest_out = sys.argv[1], sys.argv[2]
path = f"{re_dir}/src/retained_precision.rs"
rs = open(path).read()
assert rs.count("fn mx(id: &str) -> bool") == 1, "run RV113's make_mutants_r2.py first"
manifest = []


def sub(old, new, mid, desc):
    global rs
    assert rs.count(old) == 1, (mid, rs.count(old), old[:90])
    rs = rs.replace(old, new)
    manifest.append({"id": mid, "item": "ruling 2 (RS)", "description": desc})


def also(mid, desc):
    manifest.append({"id": mid, "item": "ruling 2 (RS)", "description": desc})


sub('''            demand(
                ["global_upper_bound_pa", "certified_gap_pa"]
                    .iter()
                    .all(|k| number(&x[*k]).is_some()),
                "extrema numbers",
            )?;''',
    '''            demand(
                mx("V01") || mx("V05") || ["global_upper_bound_pa", "certified_gap_pa"]
                    .iter()
                    .all(|k| (mx("V02") && *k == "certified_gap_pa") || (mx("V03") && *k == "global_upper_bound_pa")
                        || (mx("V04") && x[*k].is_null()) || (mx("V07") && x[*k].is_string()) || number(&x[*k]).is_some()),
                if mx("V06") { "extrema fractions" } else { "extrema numbers" },
            )?;''', "V01", "the extrema-number demand dropped")
also("V02", "certified_gap_pa's half dropped (only global_upper_bound_pa typed)")
also("V03", "global_upper_bound_pa's half dropped (only certified_gap_pa typed)")
also("V04", "null admitted as a number")
also("V05", "the demand moved after the extrema bounds (PY's place lost)")
also("V06", "the demand reported with another detail ('extrema fractions')")
also("V07", "a string admitted as a number")
sub('''                lower.zip(upper).is_some_and(|(l, h)| l >= 0.0 && l <= h),
                "extrema bounds",
            )?;''',
    '''                lower.zip(upper).is_some_and(|(l, h)| l >= 0.0 && l <= h),
                "extrema bounds",
            )?;
            if mx("V05") {
                demand(
                    ["global_upper_bound_pa", "certified_gap_pa"].iter().all(|k| number(&x[*k]).is_some()),
                    "extrema numbers",
                )?;
            }''', "V05b", "(V05's second half; not a separate mutant)")
manifest = [m for m in manifest if m["id"] != "V05b"]
open(path, "w").write(rs)
json.dump(manifest, open(manifest_out, "w"), indent=1)
print(len(manifest), "mutants")
