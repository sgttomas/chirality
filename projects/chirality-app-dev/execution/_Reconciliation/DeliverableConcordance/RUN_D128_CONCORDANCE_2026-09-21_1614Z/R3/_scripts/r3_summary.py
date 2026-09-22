#!/usr/bin/env python3
"""Build R3/R3_SUMMARY.md: script-built census sections plus the hand-written section kept in
R3/_work/SUMMARY_HANDWRITTEN.md (included verbatim)."""
import os, re, collections, hashlib
from r3lib import *

DISP = ["ALIGNED", "IMPLEMENTED_UNDOCUMENTED", "DOCUMENTED_UNIMPLEMENTED", "PARTIALLY_IMPLEMENTED",
        "IMPLEMENTED_DIFFERENTLY", "STALE_SPECIFICATION", "STALE_ASSESSMENT", "STALE_VERIFICATION",
        "ACCEPTED_DIVERGENCE", "RETIRED_BY_RULING", "LIFECYCLE_REASSESSMENT_REQUIRED",
        "REMAINING_STATE_MISMATCH", "DEFERRED_AGENT_WORKFLOW", "AUTHORITY_CONFLICT", "UNKNOWN", "NOT_AUDITABLE"]


def main():
    cc = read_csv(os.path.join(R3, "CLAIM_CONCORDANCE.csv"))[1]
    ec = read_csv(os.path.join(R3, "EXTENSION_CONCORDANCE.csv"))[1]
    sealed = read_csv(os.path.join(WORK, "SEALED_ROWS.csv"))[1]
    log = read_csv(os.path.join(R3, "REMAP_LOG.csv"))[1]
    ci = read_csv(os.path.join(R3, "CLUSTER_INDEX.csv"))[1]
    oc = open(os.path.join(R3, "OWNER_CHECK.md"), encoding="utf-8").read()
    qa = open(os.path.join(R3, "COVERAGE_AND_QA.md"), encoding="utf-8").read()
    cl = open(os.path.join(R3, "CLUSTERS.md"), encoding="utf-8").read()
    out = []
    w = out.append
    w("# R3 summary — RUN_D128_CONCORDANCE_2026-09-21_1614Z\n")
    w("Script-built sections by `R3/_scripts/r3_summary.py`; the last section is hand-written by the R3 manager. "
      "Evidence for HELP_HUMAN and the owner, not rulings.\n")
    # QA
    w("## 1. Coverage QA verdicts\n")
    for l in qa.splitlines():
        if l.startswith("| Q"):
            w(l)
    w("\nDetail: `COVERAGE_AND_QA.md`.\n")
    # census
    for label, fin, sl in (("Deliverable ledgers (54)", cc, [s for s in sealed if s["Kind"] == "DEL"]),
                           ("Extension ledgers (13)", ec, [s for s in sealed if s["Kind"] == "EXT"])):
        sc = collections.Counter(s["Disposition"] for s in sl)
        fc = collections.Counter(r["Disposition"] for r in fin)
        w(f"## 2{'a' if 'Deliv' in label else 'b'}. Disposition census — {label}: sealed → final\n")
        w("| Disposition | Sealed | Final | Delta |\n|---|---:|---:|---:|")
        for d in DISP:
            if sc[d] or fc[d]:
                w(f"| {d} | {sc[d]} | {fc[d]} | {fc[d] - sc[d]:+d} |")
        w(f"| **Total** | {sum(sc.values())} | {sum(fc.values())} | {sum(fc.values()) - sum(sc.values()):+d} |\n")
    # deltas by source
    w("## 3. Sealed-to-final deltas by Source (REMAP_LOG)\n")
    w("Each REMAP_LOG line is one step; `SealedValue` is the value before that step. Net Disposition moves are "
      "counted per step (a row moved twice counts twice).\n")
    w("| Source | Lines | Rows touched | Disposition steps | HumanDecisionNeeded steps | Other fields |\n|---|---:|---:|---:|---:|---:|")
    for s in ("ERRATA", "CORRECTION", "R3_RULE", "R3_RUNWIDE", "OWNER_CHECK"):
        ls = [l for l in log if l["Source"] == s]
        d = sum(1 for l in ls if l["Field"] == "Disposition")
        h = sum(1 for l in ls if l["Field"] == "HumanDecisionNeeded")
        w(f"| {s} | {len(ls)} | {len({l['ClaimKey'] for l in ls})} | {d} | {h} | {len(ls) - d - h} |")
    w("")
    moves = collections.Counter((l["Source"], l["SealedValue"], l["NewValue"]) for l in log if l["Field"] == "Disposition" and l["SealedValue"] != l["NewValue"])
    w("Disposition moves (Source: from → to × n):\n")
    for (s, a, b), n in sorted(moves.items(), key=lambda x: (x[0][0], -x[1])):
        w(f"- {s}: {a} → {b} × {n}")
    rej = sum(1 for l in log if l["Source"] == "CORRECTION" and "erratum rejected" in l["RuleOrEvidence"])
    rev = sum(1 for l in log if "SPOT-CHECK REVERT" in l["RuleOrEvidence"])
    w(f"\nErrata rejected by CORRECTIONS (sealed value kept): {rej}. Spot-check reverts (second pass): {rev}.\n")
    # HDN
    w("## 4. HumanDecisionNeeded by token (rows citing the token; all rows)\n")
    allf = cc + ec
    st, ft = collections.Counter(), collections.Counter()
    for s in sealed:
        for t in hdn_tokens(s["HumanDecisionNeeded"]):
            st[t] += 1
    for r in allf:
        for t in hdn_tokens(r["HumanDecisionNeeded"]):
            ft[t] += 1
    w("| Token | Sealed | Final | Delta |\n|---|---:|---:|---:|")
    for t in sorted(set(st) | set(ft), key=lambda t: (not t.startswith("R4"), t != "NO", t)):
        w(f"| {t} | {st[t]} | {ft[t]} | {ft[t] - st[t]:+d} |")
    w("")
    # clusters
    w("## 5. Clusters (candidate R4 packets)\n")
    rows = [l for l in cl.splitlines() if l.startswith("| CL-")]
    w("| Cluster | Title | PRIMARY | ALSO/CONTEXT | Packages | AuthorityTier mix |\n|---|---|---:|---:|---|---|")
    for l in rows:
        w(l)
    prim = collections.Counter(r["ClusterID"] for r in ci if r["Role"] == "PRIMARY")
    w(f"\n{len(rows)} clusters (including the exceptions list); {sum(prim.values())} rows with a PRIMARY cluster. "
      "Full populations: `CLUSTERS.md`, `CLUSTER_INDEX.csv`.\n")
    # owner check
    nq = len(re.findall(r"^\*\*OC-\d+\.\*\*", oc, flags=re.M))
    m = re.search(r"(\d+) questions over (\d+) rows", oc)
    w("## 6. Owner check\n")
    w(f"`OWNER_CHECK.md`: {nq} questions over {m.group(2) if m else '?'} rows, grouped by event (release act; build and "
      "signing; notarization; publication; CI and release jobs; attestation, SBOM and build matrix; packaged proofs; "
      "manual reviews). It includes the owner-reported fact that v3.0.1 was notarized, as a statement to confirm "
      "(not applied). HELP_HUMAN puts it to the owner before any R4 packet is drafted.\n")
    # spot check
    sp = os.path.join(R3, "R3_SPOT_CHECK.md")
    if os.path.exists(sp):
        txt = open(sp, encoding="utf-8").read()
        mm = re.search(r"<!-- SUMMARY -->(.*?)<!-- /SUMMARY -->", txt, re.S)
        w("## 7. Independent spot check\n")
        w((mm.group(1).strip() if mm else "See `R3_SPOT_CHECK.md`.") + "\n")
    hw = os.path.join(WORK, "SUMMARY_HANDWRITTEN.md")
    if os.path.exists(hw):
        w(open(hw, encoding="utf-8").read().strip() + "\n")
    w("## Output hashes (SHA-256)\n")
    for f in ("CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv", "REVERSE_CONCORDANCE.csv", "REMAP_LOG.csv",
              "INPUT_MANIFEST.md", "RUNWIDE_CALLS.md", "COVERAGE_AND_QA.md", "UNMAPPED_IMPLEMENTATION.csv",
              "COVERAGE_GAPS.csv", "CROSS_PACKAGE_FINDINGS.csv", "CLUSTERS.md", "CLUSTER_INDEX.csv",
              "OWNER_CHECK.md", "R3_SPOT_CHECK.md"):
        p = os.path.join(R3, f)
        if os.path.exists(p):
            w(f"- `{f}` `{sha256(p)}`")
    with open(os.path.join(R3, "R3_SUMMARY.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
