#!/usr/bin/env python3
"""Reverse-pass capability areas for one sealed ledger (brief step 6), by script.
Areas = Area (R1_INVENTORY/IMPLEMENTATION_SURFACES.csv) of every code path cited in the sealed
ledger's ImplementationEvidence, plus the areas of R1_INVENTORY/HINTS/<DEL>.csv hits.
Writes _reverse_inputs/<DEL>_AREAS.md and the concatenated capability file
_reverse_inputs/<DEL>_capabilities.csv (validator input: header + all rows of the areas + #END).
Usage: areas.py DEL-04-0n"""
import csv, io, os, re, sys, hashlib, collections
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(H); R2 = os.path.dirname(P); RUN = os.path.dirname(R2)
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip("\n")
    body = t[: t.rfind("\n#END")] if t.endswith("#END") else t
    return list(csv.DictReader(io.StringIO(body)))
d = sys.argv[1]
surf = {r["Path"]: r["Area"] for r in rows(os.path.join(RUN, "R1_INVENTORY", "IMPLEMENTATION_SURFACES.csv"))}
led = os.path.join(P, d, d + "_claims.csv")
cited = collections.Counter(); unmapped = collections.Counter()
for r in rows(led):
    for p in re.findall(r"(projects/[A-Za-z0-9_./@\-\[\]()]+?\.[A-Za-z0-9]+)(?=[:\s;,)]|$)", r["ImplementationEvidence"]):
        if p in surf: cited[surf[p]] += 1
        else: unmapped[p] += 1
hints = collections.Counter(surf[r["HitPath"]] for r in rows(os.path.join(RUN, "R1_INVENTORY", "HINTS", d + ".csv")) if r["HitPath"] in surf)
areas = sorted(set(cited) | set(hints))
os.makedirs(os.path.join(P, "_reverse_inputs"), exist_ok=True)
hdr = None; out = []
for a in areas:
    f = os.path.join(R2, "SURFACES", a + "_capabilities.csv")
    txt = open(f, encoding="utf-8").read().rstrip("\n")
    lines = txt[: txt.rfind("\n#END")] if txt.endswith("#END") else txt
    h, body = lines.split("\n", 1)
    hdr = hdr or h
    assert h == hdr
    out.append(body)
capf = os.path.join(P, "_reverse_inputs", d + "_capabilities.csv")
open(capf, "w", encoding="utf-8").write(hdr + "\n" + "\n".join(out) + "\n#END\n")
sha = lambda f: hashlib.sha256(open(f, "rb").read()).hexdigest()
md = [f"# Reverse-pass areas — {d}", "", f"- Sealed ledger SHA-256: `{sha(led)}`",
      f"- Areas from cited ImplementationEvidence paths: " + ", ".join(f"{k} ({v})" for k, v in sorted(cited.items())),
      f"- Areas from HINTS hits: " + ", ".join(f"{k} ({v})" for k, v in sorted(hints.items())),
      f"- **Union ({len(areas)}):** " + ", ".join(areas),
      f"- Cited paths not in IMPLEMENTATION_SURFACES (no area): {len(unmapped)}" + (" — " + "; ".join(sorted(unmapped)[:15]) if unmapped else ""),
      "", "| Area file | SHA-256 |", "|---|---|"]
md += [f"| `R2/SURFACES/{a}_capabilities.csv` | `{sha(os.path.join(R2, 'SURFACES', a + '_capabilities.csv'))}` |" for a in areas]
md += ["", f"Concatenated validator input `_reverse_inputs/{d}_capabilities.csv`: `{sha(capf)}`"]
open(os.path.join(P, "_reverse_inputs", d + "_AREAS.md"), "w").write("\n".join(md) + "\n")
print("\n".join(md))
