#!/usr/bin/env python3
"""Replace the `<!-- COUNTS -->` marker (or a previously injected COUNTS block) in every packet with
the generated package x Disposition table, from R4/PACKET_INDEX.csv and the final concordance.
Also builds R4/PACKET_SUBQUESTIONS.csv from R4/_work/SUBQ/*.csv. Idempotent."""
import glob, os, re
from r4lib import *

conc = load_concordance()
pi = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))[1]
subq_rows = []
for p in sorted(glob.glob(os.path.join(R4, "_work", "SUBQ", "P-*_subq.csv"))):
    pid = os.path.basename(p).split("_")[0]
    for r in read_csv(p)[1]:
        subq_rows.append({"PacketID": pid, "SubQ": r["SubQ"], "ClaimKey": r["ClaimKey"]})
write_csv(os.path.join(R4, "PACKET_SUBQUESTIONS.csv"), ["PacketID", "SubQ", "ClaimKey"], subq_rows)

BLOCK_RE = re.compile(r"<!-- COUNTS -->.*?<!-- /COUNTS -->|<!-- COUNTS -->", re.S)


def block(pid):
    prim = [r["ClaimKey"] for r in pi if r["PacketID"] == pid and r["Role"] == "PRIMARY"]
    other = [r["ClaimKey"] for r in pi if r["PacketID"] == pid and r["Role"] != "PRIMARY"]
    L = ["<!-- COUNTS -->",
         f"**{len(prim)} rows are decided in this packet** (PRIMARY); {len(other)} more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `{pid}`.", ""]
    if prim:
        L += [counts_table(prim, conc), ""]
    sq = [r for r in subq_rows if r["PacketID"] == pid]
    if sq:
        L.append("By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):")
        L.append("")
        for s in sorted({r["SubQ"] for r in sq}):
            ks = [r["ClaimKey"] for r in sq if r["SubQ"] == s]
            c = collections.Counter(conc[k]["Disposition"] for k in ks)
            L.append(f"- {pid}.{s}: {len(ks)} rows — " + ", ".join(f"{PLAIN[d]} {n}" for d, n in sorted(c.items(), key=lambda x: -x[1])))
        L.append("")
    if other:
        c = collections.Counter(conc[k]["Disposition"] for k in other)
        L.append(f"ALSO/CONTEXT members by Disposition: " + ", ".join(f"{PLAIN[d]} {n}" for d, n in sorted(c.items(), key=lambda x: -x[1])) + ".")
        L.append("")
    L.append("<!-- /COUNTS -->")
    return "\n".join(L)


n = 0
for f in sorted(glob.glob(os.path.join(R4, "PACKETS", "P-*.md"))):
    pid = os.path.basename(f).split("_")[0]
    txt = open(f, encoding="utf-8").read()
    if not BLOCK_RE.search(txt):
        print("NO COUNTS MARKER:", os.path.basename(f))
        continue
    new = BLOCK_RE.sub(lambda m: block(pid), txt, count=1)
    if new != txt:
        open(f, "w", encoding="utf-8").write(new)
        n += 1
print(f"injected/updated {n} packets; subquestion rows {len(subq_rows)}")
