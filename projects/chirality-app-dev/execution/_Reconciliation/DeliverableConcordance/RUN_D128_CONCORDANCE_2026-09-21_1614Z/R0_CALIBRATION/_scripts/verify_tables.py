#!/usr/bin/env python3
"""Aggregate verifier shard CSVs into markdown tables (_verify/AGG_TABLES.md) and run the structural validator over every R0 file."""
import csv, os, glob, collections, subprocess, hashlib
H = os.path.dirname(os.path.abspath(__file__)); R0 = os.path.dirname(H); RUN = os.path.dirname(R0)
APP = os.path.abspath(os.path.join(RUN, "..", "..", "..", ".."))
V = os.path.join(RUN, "_scripts", "validate_ledger.py"); IDX = os.path.join(RUN, "R1_INVENTORY", "CLAIM_INDEX.csv")
CAP = os.path.join(R0, "SURFACES", "HARNESS_capabilities.csv")
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip("\n").split("\n")
    if t and t[-1].strip() == "#END": t = t[:-1]
    return list(csv.DictReader(t))
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def rel(p): return os.path.relpath(p, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(APP))))))
out = ["# Aggregated verifier tables (script-derived)\n", "## §1 Structural validator (run from projects/chirality-app-dev)\n", "| File | Mode | SHA-256 | Result |", "|---|---|---|---|"]
def val(mode, extra, f):
    r = subprocess.run(["python3", V, mode] + extra + [f], cwd=APP, capture_output=True, text=True)
    return [l for l in r.stdout.splitlines() if l.startswith("RESULT")][0]
out.append(f"| SURFACES/HARNESS_capabilities.csv | capabilities | `{sha(CAP)}` | {val('capabilities', [], CAP)} |")
for f in sorted(glob.glob(os.path.join(R0, "DEL-*", "*_claims.csv"))):
    out.append(f"| {os.path.relpath(f, R0)} | ledger | `{sha(f)}` | {val('ledger', ['--index', IDX], f)} |")
for f in sorted(glob.glob(os.path.join(R0, "DEL-*", "*_reverse.csv"))):
    out.append(f"| {os.path.relpath(f, R0)} | reverse | `{sha(f)}` | {val('reverse', ['--capabilities', CAP], f)} |")
out += ["\n## §2 Recheck table per unit\n", "| Unit | Class | Checked | CONFIRMED | REFUTED | CONTESTED |", "|---|---|---|---|---|---|"]
sel = collections.Counter((r["Unit"], r["Class"]) for r in rows(os.path.join(R0, "_verify", "SELECTION.csv")))
tot = collections.Counter(); allv = []
for f in sorted(glob.glob(os.path.join(R0, "_verify", "V-*.csv"))):
    rs = rows(f); allv += [(os.path.basename(f), r) for r in rs]
    by = collections.defaultdict(collections.Counter)
    for r in rs: by[(r["Unit"], r["Class"])][r["Verdict"].strip()] += 1
    for k in sorted(by):
        c = by[k]; n = sum(c.values()); tot.update(c); tot["checked"] += n
        exp = sel.get(k)
        out.append(f"| {k[0]} | {k[1]} | {n}{'' if exp in (None, n) else f' (selected {exp})'} | {c['CONFIRMED']} | {c['REFUTED']} | {c['CONTESTED']} |")
out.append(f"| **TOTAL** | | **{tot['checked']}** | **{tot['CONFIRMED']}** | **{tot['REFUTED']}** | **{tot['CONTESTED']}** |")
out.append(f"\nSelection items: {sum(sel.values())}. Shard CSV hashes: " + "; ".join(f"`{os.path.basename(f)}` {sha(f)[:16]}" for f in sorted(glob.glob(os.path.join(R0, '_verify', 'V-*.csv')))))
out += ["\n## Field at issue (REFUTED + CONTESTED)\n"]
fc = collections.Counter((r["Verdict"].strip(), r["Field"].strip()) for _, r in allv if r["Verdict"].strip() != "CONFIRMED")
for k, v in sorted(fc.items(), key=lambda x: -x[1]): out.append(f"- {k[0]} / {k[1]}: {v}")
cc = collections.Counter(r["ConventionIssue"].strip() for _, r in allv if r["ConventionIssue"].strip() not in ("-", ""))
out += ["\n## ConventionIssue tokens (all verdicts, raw)\n"] + [f"- {k}: {v}" for k, v in cc.most_common(40)]
out += ["\n## §3 source rows: every REFUTED and CONTESTED item\n", "| Unit | Class | ClaimKey | CapabilityID | Verdict | Field | RowValue | CorrectReading | Evidence | ConventionIssue |", "|---|---|---|---|---|---|---|---|---|---|"]
for _, r in allv:
    if r["Verdict"].strip() != "CONFIRMED":
        out.append("| " + " | ".join(r[c].replace("|", "/") for c in ["Unit", "Class", "ClaimKey", "CapabilityID", "Verdict", "Field", "RowValue", "CorrectReading", "Evidence", "ConventionIssue"]) + " |")
open(os.path.join(R0, "_verify", "AGG_TABLES.md"), "w").write("\n".join(out) + "\n")
print("\n".join(out[:60]))
