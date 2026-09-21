#!/usr/bin/env python3
"""Print one status token per PKG-01 unit folder (file-driven polling), incl. DEL-01-02/S1,S2."""
import os, glob
pkg = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def ended(p):
    if not os.path.exists(p): return "-"
    t = open(p, encoding="utf-8", errors="replace").read().rstrip()
    return "END" if t.endswith("#END") or t.endswith("\"#END\"") else "partial"
out = []
dirs = sorted(glob.glob(os.path.join(pkg, "DEL-*")) + glob.glob(os.path.join(pkg, "DEL-*", "S[12]")) + glob.glob(os.path.join(pkg, "RERUN_*", "DEL-*")))
for d in dirs:
    u = os.path.relpath(d, pkg); dl = [p for p in u.split("/") if p.startswith("DEL-")][-1].split("_")[0]
    s = [f"claims={ended(os.path.join(d, dl + '_claims.csv'))}",
         f"notes={'Y' if os.path.exists(os.path.join(d, dl + '_notes.md')) else '-'}",
         f"rev={ended(os.path.join(d, dl + '_reverse.csv'))}",
         f"err={ended(os.path.join(d, dl + '_errata.csv'))}",
         f"pg={'Y' if os.path.exists(os.path.join(d, 'PREGATHER.md')) else '-'}"]
    out.append(u + " " + " ".join(s))
for v in sorted(glob.glob(os.path.join(pkg, "_verify", "V-*.csv"))):
    out.append(os.path.basename(v) + " " + ended(v))
print("\n".join(out))
