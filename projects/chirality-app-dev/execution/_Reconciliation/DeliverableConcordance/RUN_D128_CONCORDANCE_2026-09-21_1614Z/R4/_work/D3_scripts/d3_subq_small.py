"""D3: sub-question files for P-15 and P-11. Deterministic rules by deliverable / key.
P-15: a = DEL-07-02 and SOW rows (execution-root scaffolding); b = DEL-09-01 and DEL-09-06 rows
      (other live services not composed: CI wrapper binding, provider-key storage).
P-11: a = DEL-05-04, DEL-08-02 (replay lens vs continuation);
      b = DEL-05-01#STATE-1, DEL-05-01#REM-1, DEL-06-04#STATE-2, DEL-04-01 (D-GOV-43 topology undercuts
          unamended decomposition or scope text without naming it);
      c = DEL-05-01#CLM-010.2, #CLM-014.2 (session folder layout, SPEC 8.2);
      d = DEL-02-01, DEL-02-02, DEL-02-05 (presentation rulings vs later direction);
      e = everything else (event-registry drift, ruling superseded by later direction, singletons)."""
import collections, csv, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts"))
import r4lib
idx = r4lib.read_csv(os.path.join(r4lib.R4, "PACKET_INDEX.csv"))[1]
def prim(p): return sorted(r["ClaimKey"] for r in idx if r["PacketID"] == p and r["Role"] == "PRIMARY")
def p15(k): return "a" if k.startswith(("DEL-07-02#", "SOW:")) else "b"
def p11(k):
    if k.startswith(("DEL-05-04#", "DEL-08-02#")): return "a"
    if k in ("DEL-05-01#STATE-1", "DEL-05-01#REM-1", "DEL-06-04#STATE-2") or k.startswith("DEL-04-01#"): return "b"
    if k in ("DEL-05-01#CLM-010.2", "DEL-05-01#CLM-014.2"): return "c"
    if k.startswith(("DEL-02-01#", "DEL-02-02#", "DEL-02-05#")): return "d"
    return "e"
for p, fn in (("P-15", p15), ("P-11", p11)):
    rows = [(k, fn(k)) for k in prim(p)]
    with open(os.path.join(r4lib.R4, "_work", "SUBQ", f"{p}_subq.csv"), "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n"); w.writerow(["ClaimKey", "SubQ"]); w.writerows(rows); f.write("#END\n")
    print(p, len(rows), collections.Counter(s for _, s in rows))
    for s in sorted({s for _, s in rows}): print("  ", s, [k for k, x in rows if x == s])
