#!/usr/bin/env python3
"""Build R4/R4_DECISION_BOOK.md from R4/_work/BOOK_OVERVIEW.md and BOOK_ORDER.md (hand-written by the
manager) plus the packet header blocks and PACKET_INDEX.csv (generated table and ruling form)."""
import glob, os, re
from r4lib import *

pi = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))[1]
# Cause-cluster groups, in R3 cluster priority order
GROUP = [("Owner-reserved and owner-check items", ["P-01", "P-02", "P-03"]),
         ("Named governance questions (R4-Q1..Q6)", ["P-04", "P-05", "P-06", "P-07", "P-08", "P-09"]),
         ("Rows held on existing or unframed decisions", ["P-10", "P-11"]),
         ("Live Codex path findings", ["P-12", "P-13", "P-14", "P-15", "P-16"]),
         ("Repair classes by cause (no new direction expected)", ["P-17", "P-18", "P-19", "P-20", "P-21", "P-22"]),
         ("Lifecycle, done-declaration and exceptions", ["P-23", "P-24", "P-EX"])]
TIER_ORDER = {"GOVERNING": 0, "mixed": 1, "CONTEXT": 2}

hdr = {}
for f in glob.glob(os.path.join(R4, "PACKETS", "P-*.md")):
    pid = os.path.basename(f).split("_")[0]
    t = open(f, encoding="utf-8").read()
    hb = re.search(r"<!-- PACKET\n(.*?)\n-->", t, re.S)
    d = {}
    for l in hb.group(1).splitlines():
        if ":" in l:
            k, v = l.split(":", 1)
            d[k.strip()] = v.strip()
    d["file"] = os.path.relpath(f, R4)
    hdr[pid] = d

def rows(pid):
    p = sum(1 for r in pi if r["PacketID"] == pid and r["Role"] == "PRIMARY")
    o = sum(1 for r in pi if r["PacketID"] == pid and r["Role"] != "PRIMARY")
    return p, o

L = [open(os.path.join(R4, "_work", "BOOK_OVERVIEW.md"), encoding="utf-8").read().rstrip(), "",
     "## 2. The packets", "",
     "Ordered by cause group, then by the authority the question turns on (GOVERNING before mixed before CONTEXT). "
     "\"Rows\" = rows decided in the packet (+ rows that touch it but are decided elsewhere). "
     "Recommendations are HELP_HUMAN drafts, not rulings.", ""]
for g, members in GROUP:
    L += [f"### {g}", "", "| Packet | Question | Rows | Authority | Recommended (draft) | Depends on |", "|---|---|---:|---|---|---|"]
    for pid in sorted(members, key=lambda p: (TIER_ORDER.get(hdr.get(p, {}).get("tier", "mixed").split()[0], 1), p)):
        d = hdr.get(pid)
        if not d:
            L.append(f"| {pid} | _packet missing_ | | | | |")
            continue
        p, o = rows(pid)
        L.append(f"| [{pid}]({d['file']}) — {d['title']} | {d['question']} | {p} (+{o}) | {d['tier']} | {d['recommended']} | {d['depends_on']} |")
    L.append("")
L += [open(os.path.join(R4, "_work", "BOOK_ORDER.md"), encoding="utf-8").read().rstrip(), "",
      "## 4. Ruling form", "",
      "Answer in shorthand, one line per packet: an option letter (for example `A`), `A with <change>`, `REC` "
      "(adopt the draft recommendation), `DEFER`, or `ASK` (send back with a question). Sub-questions take one "
      "answer each (`P-09.a A; P-09.b B`).", "", "```text"]
for g, members in GROUP:
    for pid in members:
        if pid in hdr:
            L.append(f"{pid:<5} {hdr[pid]['title'][:48]:<48} : ")
L += ["```", "", "Riders or general directions (optional):", "", "```text", "", "```", ""]
open(os.path.join(R4, "R4_DECISION_BOOK.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print("book written;", len(hdr), "packets")
