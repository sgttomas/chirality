#!/usr/bin/env python3
"""Generate the scripted parts of R2/PKG-02/VERIFICATION.md (§1 structural, §2 rechecks, §3 all
REFUTED/CONTESTED items, §5 superseded first ledgers). Re-runs the validator on every accepted file.
Usage (from projects/chirality-app-dev): python3 <RUN>/R2/PKG-02/_scripts/verification_tables.py > <out>
The hand-written §4 patterns section is added by the manager."""
import csv, glob, hashlib, io, os, subprocess, collections
PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN = os.path.dirname(os.path.dirname(PKG)); VAL = os.path.join(RUN, "_scripts", "validate_ledger.py")
rel = lambda p: os.path.relpath(p, PKG)
def dicts(p):
    r = list(csv.reader(io.StringIO(open(p, encoding="utf-8", newline="").read())))
    if r and r[-1] == ["#END"]: r = r[:-1]
    return [dict(zip(r[0], x)) for x in r[1:]]
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def val(args):
    o = subprocess.run(["python3", VAL] + args, capture_output=True, text=True).stdout.strip().splitlines()
    return o[-1] if o else "NO OUTPUT"
DELS = sorted(os.path.basename(d) for d in glob.glob(os.path.join(PKG, "DEL-*")))
print("## §1 Structural validator (re-run by the manager)\n")
print("| File | Mode | Result | SHA-256 |"); print("|---|---|---|---|")
for d in DELS:
    f = os.path.join(PKG, d, f"{d}_claims.csv"); print(f"| `{rel(f)}` | ledger | {val(['ledger', f])} | `{sha(f)}` |")
    cap = os.path.join(PKG, d, "REVERSE_INPUT_capabilities.csv")
    rv = os.path.join(PKG, d, f"{d}_reverse.csv")
    if os.path.exists(rv): print(f"| `{rel(rv)}` | reverse | {val(['reverse', '--capabilities', cap, rv])} | `{sha(rv)}` |")
    er = os.path.join(PKG, d, f"{d}_errata.csv")
    if os.path.exists(er): print(f"| `{rel(er)}` | errata | {val(['errata', er])} | `{sha(er)}` |")
    print(f"| `{rel(cap)}` | capabilities | {val(['capabilities', cap])} | `{sha(cap)}` |")
V = []
for p in sorted(glob.glob(os.path.join(PKG, "_verify", "V-SHARD-*.csv"))):
    for r in dicts(p): r["_shard"] = os.path.basename(p)[2:-4]; V.append(r)
print("\n## §2 Recheck results\n")
print("Selection: `_scripts/select_rechecks.py` → `_verify/SELECTION.csv` (classes: a = LOW, self-flagged, AUTHORITY_CONFLICT, UNKNOWN, REMAINING_WORK, errata-touched rows; a30 = 30% of other non-ALIGNED; b = 15% of ALIGNED; e = each errata row; c = 20% of CLAIMED_BY/PARTIAL).\n")
print("| Deliverable | Shards | Items | a | a30 | b | e | c | CONFIRMED | REFUTED | CONTESTED | Distinct rows checked (ledger+reverse) | Rows REFUTED on a verdict field | Verdict share (Addendum 3) | Rows REFUTED on any field (info) | Rerun rule |")
print("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|")
for d in DELS:
    vs = [v for v in V if v["Unit"] == d]; c = collections.Counter(v["Verdict"] for v in vs); k = collections.Counter(v["Class"] for v in vs)
    key = lambda v: ("REV:" + v["CapabilityID"] + "|" + v["ClaimKey"]) if v["Class"] == "c" else v["ClaimKey"]
    rows = {key(v) for v in vs}
    vr = {key(v) for v in vs if v["Verdict"] == "REFUTED" and v["Field"].strip().split(" ")[0] in ("Disposition", "Response")}
    ar = {key(v) for v in vs if v["Verdict"] == "REFUTED"}
    share = 100 * len(vr) / len(rows) if rows else 0
    print(f"| {d} | {', '.join(sorted({v['_shard'] for v in vs}))} | {len(vs)} | {k['a']} | {k['a30']} | {k['b']} | {k['e']} | {k['c']} | {c['CONFIRMED']} | {c['REFUTED']} | {c['CONTESTED']} | {len(rows)} | {len(vr)} | {share:.1f}% | {len(ar)} ({100*len(ar)/len(rows):.1f}%) | {'RERUN' if share > 10 else 'pass'} |")
c = collections.Counter(v["Verdict"] for v in V)
print(f"| **Total** | | {len(V)} | | | | | | {c['CONFIRMED']} | {c['REFUTED']} | {c['CONTESTED']} | | | | | |")
print("\nShard CSV SHA-256: " + "; ".join(f"`{os.path.basename(p)}` `{sha(p)}`" for p in sorted(glob.glob(os.path.join(PKG, '_verify', 'V-SHARD-*.csv')))))
print("\n## §3 Every REFUTED and CONTESTED item\n")
for d in DELS:
    vs = [v for v in V if v["Unit"] == d and v["Verdict"] != "CONFIRMED"]
    print(f"### {d} — {len(vs)} items\n")
    if not vs: print("None.\n"); continue
    print("| Shard | Class | Key | Capability | Verdict | Field | Row value | Correct reading | Evidence | Convention issue |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    esc = lambda s: s.replace("|", "\\|").replace("\n", " ")
    for v in vs:
        print(f"| {v['_shard']} | {v['Class']} | `{v['ClaimKey']}` | {v['CapabilityID'] or '-'} | {v['Verdict']} | {v['Field']} | {esc(v['RowValue'])} | {esc(v['CorrectReading'])} | {esc(v['Evidence'])} | {esc(v['ConventionIssue'])} |")
    print()
OV = []
for p in sorted(glob.glob(os.path.join(PKG, "_verify", "_ORIGINAL", "V-SHARD-*.csv"))):
    for r in dicts(p): r["_shard"] = os.path.basename(p)[2:-4]; OV.append(r)
if OV:
    print("## §5 Superseded first ledgers (kept under `_ORIGINAL/`; verification under `_verify/_ORIGINAL/`)\n")
    print("| Deliverable | Sealed SHA-256 | Items | CONFIRMED | REFUTED | CONTESTED | Distinct ledger rows | Rows REFUTED | Share |"); print("|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for d in sorted({v["Unit"] for v in OV}):
        vs = [v for v in OV if v["Unit"] == d]; c = collections.Counter(v["Verdict"] for v in vs)
        led = [v for v in vs if v["Class"] in ("a", "a30", "b", "e")]; rows = {v["ClaimKey"] for v in led}; rr = {v["ClaimKey"] for v in led if v["Verdict"] == "REFUTED"}
        f = os.path.join(PKG, "_ORIGINAL", d, f"{d}_claims.csv")
        print(f"| {d} | `{sha(f)}` | {len(vs)} | {c['CONFIRMED']} | {c['REFUTED']} | {c['CONTESTED']} | {len(rows)} | {len(rr)} | {100*len(rr)/len(rows):.1f}% |")
    print("\nVerdict-field refutations in the superseded attempts (Addendum 3): " + "; ".join(f"{v['Unit']} `{v['ClaimKey']}` {v['Field']}" for v in OV if v["Verdict"] == "REFUTED" and v["Field"].split(" ")[0] in ("Disposition", "Response")) + ".\n")
    print("\nAll REFUTED items in the superseded attempts:\n")
    for v in OV:
        if v["Verdict"] == "REFUTED": print(f"- {v['Unit']} `{v['ClaimKey']}` {v['Field']}: {v['CorrectReading'][:300]} ({v['Evidence'][:160]})")
    print()
