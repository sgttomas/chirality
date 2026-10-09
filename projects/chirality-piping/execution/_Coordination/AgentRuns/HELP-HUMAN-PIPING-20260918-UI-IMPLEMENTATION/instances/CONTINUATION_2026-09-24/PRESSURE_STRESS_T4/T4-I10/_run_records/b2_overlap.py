"""Read-only: map T4-U3 edit sites (cited at ed012c7ccf) to main ec5d397359 line numbers,
and measure the distance to b2's hunks (e582b61f9e vs ec5d397359). Uses git show/diff only."""
import subprocess, re, difflib, sys
REPO = sys.argv[1]
MAIN, U3, B2 = "ec5d397359", "ed012c7ccf", "e582b61f9e"
P = "projects/chirality-piping/"
def show(c, p):
    return subprocess.run(["git","-C",REPO,"show",f"{c}:{P}{p}"],capture_output=True,text=True,check=True).stdout.splitlines()
def b2_hunks(p):
    out = subprocess.run(["git","-C",REPO,"diff","-U0",MAIN,B2,"--",P+p],capture_output=True,text=True,check=True).stdout
    hs = []
    for m in re.finditer(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", out, re.M):
        a, n = int(m.group(1)), int(m.group(2) or 1)
        # a pure insertion "-a,0" sits after line a
        hs.append((a, a + max(n,1) - 1, n))
    return hs
def u3_to_main(p):
    a, b = show(MAIN, p), show(U3, p)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    m = {}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(j2 - j1):
                m[j1 + k + 1] = i1 + k + 1
    return m
SITES = {
  "core/product_physics/src/lib.rs": [(51,53),(1225,1248),(1457,1457),(1558,1559),(2050,2050),(2412,2417),(2779,2781),(3541,3541),(3763,3767),(4435,4435),(5758,5758),(6104,6104),(6138,6138),(6259,6259),(6385,6385),(6440,6450),(7337,7338),(7417,7417),(7482,7593),(11906,12010),(17393,17587)],
  "core/product_physics/src/retained_product.rs": [(1558,1558)],
  "core/product_physics/tests/s11f_site_test.rs": [(215,224),(511,511),(1377,1383)],
  "core/reporting/result_export/tests/preview_physics_contract.rs": [(606,606)],
  "core/product_physics/src/retained_product_tests.rs": [(2435,2435)],
}
for p, sites in SITES.items():
    hs = b2_hunks(p)
    m = u3_to_main(p)
    print(f"== {p}: b2 hunks {len(hs)}")
    for s, e in sites:
        ms = [m.get(k) for k in range(s, e+1) if m.get(k)]
        if not ms:
            print(f"  site {s}-{e}@U3: no main counterpart (U3-only lines)"); continue
        lo, hi = min(ms), max(ms)
        best = None
        for (ha, hb, n) in hs:
            # distance in unchanged main lines between [lo,hi] and the hunk [ha,hb] (insertion after ha if n==0)
            if n == 0: ha2, hb2 = ha + 0.5, ha + 0.5
            else: ha2, hb2 = ha, hb
            d = 0 if (hb2 >= lo and ha2 <= hi) else (lo - hb2 if lo > hb2 else ha2 - hi)
            if best is None or d < best[0]: best = (d, ha, hb, n)
        print(f"  site {s}-{e}@U3 -> main {lo}-{hi}; nearest b2 hunk main {best[1]}-{best[2]} (n={best[3]}), gap {best[0]} lines")
