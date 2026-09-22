#!/usr/bin/env python3
"""RUN_BASIS Addendum 10 scan: sealed ledger-of-record rows (errata applied) whose non-ALIGNED verdict may rest on the
absence of an in-root record of an out-of-code event (notarization, signing, publication, release/CI job run,
attestation, manual or credentialed step). Keyword screen only; the manager curates the list by hand."""
import csv, io, os, re, sys
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UNITS = ["DEL-09-01", "DEL-09-02_A", "DEL-09-03", "DEL-09-04", "DEL-09-05", "DEL-09-06", "DEL-09-07"]
EV = re.compile(r"notari|publish|signed|signing|Developer ID|release (job|run|act)|run record|execution record|build (record|evidence)|no (recorded|record|green|packaged|execution|v3)|never (run|ran|executed)|attest|manual|credential|packaged (run|proof)|proof run|not recorded|AgentRuns", re.I)
SKIP = {"ALIGNED", "NOT_AUDITABLE", "RETIRED_BY_RULING"}
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip()
    t = t[:-6] if t.endswith('"#END"') else (t[:-4] if t.endswith("#END") else t)
    return list(csv.DictReader(io.StringIO(t)))
for u in UNITS:
    d = u.split("_")[0]; led = rows(os.path.join(P, u, d + "_claims.csv"))
    for r in led:
        if r["Disposition"] in SKIP: continue
        txt = " ".join(r[k] for k in ("DeclaredState", "ImplementationEvidence", "VerificationEvidence", "RemainingWork", "Notes"))
        if EV.search(txt):
            m = sorted({x.group(0).lower() for x in EV.finditer(txt)})
            print(f"{r['ClaimKey']}\t{r['Disposition']}\t{r['ClaimType']}\t{','.join(m)[:80]}\tRW: {' '.join(r['RemainingWork'].split())[:170]}")
