#!/usr/bin/env python3
"""Deterministic verifier selection for the EXT ledgers (CONVENTIONS §10; R2 package brief
step 7, as revised by RUN_BASIS Addendum 3). Writes _verify/SELECTION.csv.

Classes:
  a  all LOW, self-flagged (LEAST-CONFIDENT / SELF-FLAG in Notes), AUTHORITY_CONFLICT,
     UNKNOWN Disposition and REMAINING_WORK rows;
  b  30% of the other non-ALIGNED rows;
  c  15% of ALIGNED rows;
  e  every errata row (ClaimKey, Field).
Sampling is deterministic by sha256(ClaimKey), as in R0 (`select_rechecks.py`): keys whose
hash ends in 0-2 first, topped up in key order to ceil(n * pct).
Shards: grouped by worker family, at most 50 items each."""
import csv, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extlib import EXT, LEDGERS, ledger_path, read_rows, h

FAMILY = {"DEC": "DEC", "SOW": "SOW", "DOC_REL": "DOC4", "DOC_VAL": "DOC4", "DOC_DEV": "DOC67", "DOC_DEV_R1": "DOC67R"}


def pick(keys, pct):
    keys = sorted(keys); n = math.ceil(len(keys) * pct)
    sel = [k for k in keys if h(k)[-1] in "012"][:n]
    if len(sel) < n: sel += [k for k in keys if k not in sel][: n - len(sel)]
    return sorted(sel), n


items = []  # (family, ledger, class, key, field, reason)
for stem, item, folder in LEDGERS:
    p = ledger_path(stem, folder)
    if not os.path.exists(p) or not os.path.exists(os.path.join(os.path.dirname(p), "RETURN.md")) and folder != "SOW":
        continue  # ledger not yet sealed; its family is selected on a later run (selection is per-ledger deterministic)
    _, rs = read_rows(p)
    fam = FAMILY[folder]
    other_non, aligned = [], []
    for r in rs:
        why = []
        if r["Confidence"] == "LOW": why.append("LOW")
        if "LEAST-CONFIDENT" in r["Notes"] or "SELF-FLAG" in r["Notes"].upper(): why.append("self-flag")
        if r["Disposition"] == "AUTHORITY_CONFLICT": why.append("AUTHORITY_CONFLICT")
        if r["Disposition"] == "UNKNOWN": why.append("UNKNOWN")
        if r["ClaimType"] == "REMAINING_WORK": why.append("REMAINING_WORK")
        if why:
            items.append((fam, stem, "a", r["ClaimKey"], "", "a:" + ";".join(why)))
        elif r["Disposition"] == "ALIGNED":
            aligned.append(r["ClaimKey"])
        else:
            other_non.append(r["ClaimKey"])
    sel, n = pick(other_non, 0.30)
    for k in sel: items.append((fam, stem, "b", k, "", f"b:30% of {len(other_non)} other non-ALIGNED (n={n})"))
    sel, n = pick(aligned, 0.15)
    for k in sel: items.append((fam, stem, "c", k, "", f"c:15% of {len(aligned)} ALIGNED (n={n})"))
    ep = ledger_path(stem, folder, "errata")
    if os.path.exists(ep):
        _, es = read_rows(ep)
        for e in es: items.append((fam, stem, "e", e["ClaimKey"], e["Field"], "e:errata row"))

# Rerun ledgers (manager addition): every row not already selected is checked as class r.
RERUN = {"DOC_DEV_R1"}
for stem, item, folder in LEDGERS:
    if folder not in RERUN or not os.path.exists(ledger_path(stem, folder)): continue
    done = {x[3] for x in items if x[1] == stem}
    for r in read_rows(ledger_path(stem, folder))[1]:
        if r["ClaimKey"] not in done:
            items.append((FAMILY[folder], stem, "r", r["ClaimKey"], "", "r:rerun ledger, full check"))

out = []
for fam in ("DEC", "DOC4", "SOW", "DOC67", "DOC67R"):
    fi = [x for x in items if x[0] == fam]
    k = max(1, math.ceil(len(fi) / 50)) if fi else 0
    size = math.ceil(len(fi) / k) if k else 0
    for i, x in enumerate(fi):
        shard = f"{fam}-{i // size + 1}" if k > 1 else fam
        out.append((shard,) + x[1:])
os.makedirs(os.path.join(EXT, "_verify"), exist_ok=True)
with open(os.path.join(EXT, "_verify", "SELECTION.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, lineterminator="\n")
    w.writerow(["Shard", "Ledger", "Class", "ClaimKey", "ErrataField", "Reason"])
    w.writerows(out); fh.write("#END\n")
import collections
c = collections.Counter((o[0], o[2]) for o in out)
for kk in sorted(c): print(kk, c[kk])
print("SHARDS", dict(collections.Counter(o[0] for o in out)))
print("TOTAL", len(out))
