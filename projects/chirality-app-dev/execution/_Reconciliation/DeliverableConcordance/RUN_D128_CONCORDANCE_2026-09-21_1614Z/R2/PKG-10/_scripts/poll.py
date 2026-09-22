#!/usr/bin/env python3
"""Print one status token per PKG-10 unit folder (file-driven polling)."""
import os, glob
pkg = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def ended(p):
    if not os.path.exists(p): return "-"
    t = open(p, encoding="utf-8", errors="replace").read().rstrip()
    return "END" if t.endswith("#END") or t.endswith("\"#END\"") else "partial"
out = []
for d in sorted(glob.glob(os.path.join(pkg, "DEL-*"))):
    u = os.path.basename(d); dl = u.split("_")[0]
    s = [f"claims={ended(os.path.join(d, dl + '_claims.csv'))}",
         f"notes={'Y' if os.path.exists(os.path.join(d, dl + '_notes.md')) else '-'}",
         f"rev={ended(os.path.join(d, dl + '_reverse.csv'))}",
         f"err={ended(os.path.join(d, dl + '_errata.csv'))}",
         f"pg={'Y' if os.path.exists(os.path.join(d, 'PREGATHER.md')) else '-'}"]
    out.append(u + " " + " ".join(s))
for v in sorted(glob.glob(os.path.join(pkg, "_verify", "V-*.csv"))):
    out.append(os.path.basename(v) + " " + ended(v))
print("\n".join(out))
