#!/usr/bin/env python3
"""Build R4/PACKET_INDEX.csv and one fact sheet per packet (R4/_work/FACTS/P-nn_facts.md)
from the final R3 concordance and the frozen R3 CLUSTER_INDEX.csv. Deterministic; re-runnable."""
import collections, os, re
from r4lib import *

conc = load_concordance()
idx = load_cluster_index()
clusters_md = open(os.path.join(R3, "CLUSTERS.md"), encoding="utf-8").read()
spot_md = open(os.path.join(R3, "R3_SPOT_CHECK.md"), encoding="utf-8").read()

# Contested items carried from R3 (R3_SUMMARY §8, R3_SPOT_CHECK.md)
contested = collections.defaultdict(list)
sec = None
for line in spot_md.splitlines():
    if line.startswith("## REFUTED"):
        sec = "SPOT_REFUTED"
    elif line.startswith("## UNDECIDED"):
        sec = "SPOT_UNDECIDED"
    elif line.startswith("## "):
        sec = None
    m = re.match(r"\| (S\d-\d+) \| `([^`]+)` \| (\w+) \| ([^|]*) \| ([^|]*) \|", line)
    if sec and m:
        contested[m.group(2)].append(f"{sec} {m.group(1)}: {m.group(3)} checked `{m.group(4).strip()}`"
                                     + (f", checker proposes `{m.group(5).strip()}`" if sec == "SPOT_REFUTED" else f"; readings: {m.group(5).strip()[:160]}"))
for k in ("DEL-09-04#CLM-022", "DEL-09-04#CLM-023.3", "DEL-06-04#STATE-2"):
    contested[k].append("RESTORED_R4: sealed AUTHORITY_CONFLICT the verifiers read as needing no owner decision; R3 kept the Disposition and restored `R4` (R3_SUMMARY §8)")
for k, why in (("DEL-09-05#CLM-010.8", "Addendum 10 (OC-05)"), ("DEL-04-01#CLM-004.2", "tie-break"),
               ("DEL-06-06#STATE-2", "tie-break"), ("DEL-06-03#CLM-010.4", "subject test"),
               ("DEL-04-04#CLM-024", "R4-Q1"), ("DEL-04-05#CLM-024", "R4-Q1")):
    contested[k].append(f"R3_UNDECIDED: {why}; current value stands, both readings in the R3 task files (R3_SUMMARY §8)")

by_c = collections.defaultdict(list)
for r in idx:
    by_c[r["ClusterID"]].append((r["ClaimKey"], r["Role"]))

pi = []
for cid in sorted(by_c, key=lambda c: (c == "CL-EX", c)):
    for k, role in by_c[cid]:
        pi.append({"PacketID": cid_to_pid(cid), "ClaimKey": k, "Role": role})
write_csv(os.path.join(R4, "PACKET_INDEX.csv"), ["PacketID", "ClaimKey", "Role"], pi)

os.makedirs(os.path.join(R4, "_work", "FACTS"), exist_ok=True)
for cid, mem in by_c.items():
    pid = cid_to_pid(cid)
    m = re.search(r"^## " + re.escape(cid) + r" — (.*?)\n(.*?)(?=^- Rows:)", clusters_md, re.S | re.M)
    title, body = m.group(1), m.group(2).strip()
    prim = [k for k, ro in mem if ro == "PRIMARY"]
    other = [k for k, ro in mem if ro != "PRIMARY"]
    L = [f"# Fact sheet {pid} (cluster {cid}) — {title}", "",
         "Built by `R4/_scripts/r4_facts.py` from the final R3 concordance and `R3/CLUSTER_INDEX.csv`. Evidence, not rulings.", "",
         "## R3 cluster text", "", body, "",
         f"## Counts — PRIMARY rows ({len(prim)})", "",
         counts_table(prim, conc) if prim else "_none_", "",
         f"## Counts — ALSO/CONTEXT members ({len(other)}; these rows are decided in their own PRIMARY packet)", "",
         counts_table(other, conc) if other else "_none_", ""]
    for fld in ("AuthorityTier", "HumanDecisionNeeded", "CauseTag", "LatestDecision", "ClaimType", "Confidence"):
        c = collections.Counter(conc[k][fld] for k in prim)
        L.append(f"- PRIMARY {fld}: " + ", ".join(f"`{v}` {n}" for v, n in c.most_common(12)))
    c = collections.Counter(re.findall(r"REACH=(LIVE|LEGACY_ONLY|TEST_ONLY)", conc[k]["ImplementationEvidence"]) and
                            "+".join(sorted(set(re.findall(r"REACH=(LIVE|LEGACY_ONLY|TEST_ONLY)", conc[k]["ImplementationEvidence"]))))
                            or "no REACH tag" for k in prim)
    L.append("- PRIMARY reach mix (REACH tags in ImplementationEvidence): " + ", ".join(f"{v} {n}" for v, n in c.most_common()))
    L += ["", "## Contested or flagged members", ""]
    any_c = False
    for k, ro in mem:
        for s in contested.get(k, []):
            any_c = True
            L.append(f"- `{k}` ({ro}; now {conc[k]['Disposition']} / HDN {conc[k]['HumanDecisionNeeded']}): {s}")
        if conc[k].get("AltReading"):
            any_c = True
            L.append(f"- `{k}` ({ro}): AltReading: {conc[k]['AltReading']}")
    if not any_c:
        L.append("_none_")
    L += ["", "## Members by deliverable (° = ALSO/CONTEXT)", ""]
    byd2 = collections.defaultdict(list)
    for k, ro in mem:
        grp = k.split("#")[0] if "#" in k else k.split(":")[0]
        byd2[grp].append(k[len(grp) + 1:] + ("°" if ro != "PRIMARY" else "") if "#" in k else k + ("°" if ro != "PRIMARY" else ""))
    for g in sorted(byd2):
        L.append(f"- {g}: " + ", ".join(byd2[g]))
    open(os.path.join(R4, "_work", "FACTS", f"{pid}_facts.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print(len(pi), "index rows;", len(by_c), "packets")
