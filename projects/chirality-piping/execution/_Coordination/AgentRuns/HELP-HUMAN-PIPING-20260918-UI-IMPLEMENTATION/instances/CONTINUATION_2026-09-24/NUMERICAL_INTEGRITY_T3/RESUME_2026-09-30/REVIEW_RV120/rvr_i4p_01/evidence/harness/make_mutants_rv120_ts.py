"""RV120 (RV-R): my own TS mutants on rulings 2 and 3's new check (previewPhysicsEvidence.ts readCases, "extrema
numbers"), each guarded by `mx('<id>')`, true only when the environment's RV120_MUT equals the id. With RV120_MUT unset
the copy behaves as the head (the control checks it). Each anchor must match exactly once.
Usage: python3 make_mutants_rv120_ts.py <previewPhysicsEvidence.ts> <manifest out>
"""
import json
import sys

path, manifest_out = sys.argv[1], sys.argv[2]
ts = open(path).read()
manifest = []


def sub(old, new):
    global ts
    assert ts.count(old) == 1, (ts.count(old), old[:90])
    ts = ts.replace(old, new)


def m(mid, desc):
    manifest.append({"id": mid, "item": "rulings 2 and 3 (TS)", "description": desc})


anchor = "const TINY = 2.2250738585072014e-308; // binary64 minimum positive normal\n"
sub(anchor, anchor + "const mx = (id: string): boolean => (globalThis as any).process?.env?.RV120_MUT === id;\nlet rv120Transport = false;\n")
sub('''      demand(finite(x.global_upper_bound_pa) && finite(x.certified_gap_pa), "extrema numbers");''',
    '''      const rv120Num = (k: string) => (mx('W02') && k === "certified_gap_pa") || (mx('W03') && k === "global_upper_bound_pa")
        || (mx('W04') && x[k] === null) || (mx('W10') && typeof x[k] === "string") || finite(x[k]);
      demand(mx('W01') || mx('W05') || (mx('W07') && rv120Transport) || (mx('W08') && !rv120Transport)
        || (rv120Num("global_upper_bound_pa") && rv120Num("certified_gap_pa")), mx('W06') ? "extrema fractions" : "extrema numbers");''')
m("W01", "the extrema-number demand dropped (raw and transport)")
m("W02", "certified_gap_pa's half dropped")
m("W03", "global_upper_bound_pa's half dropped")
m("W04", "null admitted")
m("W05", "the demand moved after the extrema bounds")
m("W06", "the demand reported with another detail ('extrema fractions')")
m("W07", "raw only: the transport check skips the demand")
m("W08", "transport only: the raw reader skips the demand")
m("W10", "a string admitted")
sub('''      demand(["value_lower_pa", "value_upper_pa"].every(k => finite(x[k])) && x.value_lower_pa >= 0 && x.value_lower_pa <= x.value_upper_pa, "extrema bounds");''',
    '''      demand(["value_lower_pa", "value_upper_pa"].every(k => finite(x[k])) && x.value_lower_pa >= 0 && x.value_lower_pa <= x.value_upper_pa, "extrema bounds");
      if (mx('W05')) demand(finite(x.global_upper_bound_pa) && finite(x.certified_gap_pa), "extrema numbers");''')
sub('''    finiteTree(evidence);
    readCases(evidence);
    readGates(evidence);''',
    '''    finiteTree(evidence);
    rv120Transport = true; try { readCases(evidence); } finally { rv120Transport = false; }
    readGates(evidence);''')
open(path, "w").write(ts)
json.dump(manifest, open(manifest_out, "w"), indent=1)
print(len(manifest), "mutants")
