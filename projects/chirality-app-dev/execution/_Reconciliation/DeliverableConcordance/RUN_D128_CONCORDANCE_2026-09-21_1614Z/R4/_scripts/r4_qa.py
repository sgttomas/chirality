#!/usr/bin/env python3
"""R4 QA (RUN_D128). Writes R4/R4_QA.md. Deterministic; re-runnable.
C1 every PRIMARY row of R3/CLUSTER_INDEX.csv appears as PRIMARY in exactly one packet (and that packet file exists);
C2 every packet's generated counts reproduce from PACKET_INDEX.csv and the concordance; sub-question files cover
   every PRIMARY row of their packet exactly once;
C3 every UNKNOWN, AUTHORITY_CONFLICT and HumanDecisionNeeded != NO row is in some packet;
C4 no packet presents CONTEXT as GOVERNING (CONTEXT source on a [GOVERNING] line; header tier; P-24);
C5 packet form: header block fields, required headings, evidence tags on every 'What we found' bullet,
   recommendation labelled draft, no absolute paths in R4 outputs."""
import collections, glob, os, re
from r4lib import *
import r4_inject

conc = load_concordance()
idx = load_cluster_index()
pi = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))[1]
packets = {os.path.basename(f).split("_")[0]: f for f in glob.glob(os.path.join(R4, "PACKETS", "P-*.md"))}
res = []

# C1
prim_idx = [r["ClaimKey"] for r in idx if r["Role"] == "PRIMARY"]
prim_pi = collections.Counter(r["ClaimKey"] for r in pi if r["Role"] == "PRIMARY")
bad = [k for k in prim_idx if prim_pi[k] != 1]
extra = [k for k in prim_pi if k not in set(prim_idx)]
pids = sorted({r["PacketID"] for r in pi})
nofile = [p for p in pids if p not in packets and any(r["PacketID"] == p and r["Role"] == "PRIMARY" for r in pi)]
nofile_all = [p for p in pids if p not in packets]
res.append(("C1 every PRIMARY cluster row is PRIMARY in exactly one packet", not bad and not extra and not nofile_all,
            f"{len(prim_idx)} PRIMARY rows; not exactly once {len(bad)} {bad[:3]}; extra {len(extra)}; packets in index {len(pids)}, packet files {len(packets)}, missing files {nofile_all}"))

# C2
mism = []
for pid, f in packets.items():
    txt = open(f, encoding="utf-8").read()
    m = re.search(r"<!-- COUNTS -->.*?<!-- /COUNTS -->", txt, re.S)
    if not m or m.group(0) != r4_inject.block(pid):
        mism.append(pid)
subq = read_csv(os.path.join(R4, "PACKET_SUBQUESTIONS.csv"))[1]
sq_bad = []
for pid in sorted({r["PacketID"] for r in subq}):
    ks = collections.Counter(r["ClaimKey"] for r in subq if r["PacketID"] == pid)
    prim = {r["ClaimKey"] for r in pi if r["PacketID"] == pid and r["Role"] == "PRIMARY"}
    if set(ks) != prim or any(v != 1 for v in ks.values()):
        sq_bad.append(f"{pid}: missing {len(prim - set(ks))}, foreign {len(set(ks) - prim)}, dup {sum(1 for v in ks.values() if v > 1)}")
res.append(("C2 packet counts reproduce from PACKET_INDEX.csv and the concordance", not mism and not sq_bad,
            f"packets checked {len(packets)}; count blocks not reproducing {mism}; sub-question coverage problems {sq_bad}"))

# C3
inpk = {r["ClaimKey"] for r in pi}
need = [k for k, r in conc.items() if r["Disposition"] in ("UNKNOWN", "AUTHORITY_CONFLICT") or r["HumanDecisionNeeded"] != "NO"]
miss = [k for k in need if k not in inpk]
c = collections.Counter("UNKNOWN" if conc[k]["Disposition"] == "UNKNOWN" else "AUTHORITY_CONFLICT" if conc[k]["Disposition"] == "AUTHORITY_CONFLICT" else "HDN" for k in need)
res.append(("C3 every UNKNOWN, AUTHORITY_CONFLICT and HumanDecisionNeeded != NO row is in some packet", not miss,
            f"{len(need)} rows ({dict(c)}); missing {len(miss)} {miss[:5]}"))

# C4
CTX_PAT = re.compile(r"plans/|steers|SCA-APP-008|AgentRuns/APP_V3|APP_V3_|APPDEV_V3_NODE|CHIRALITY_V3_APP_ADOPTION|DONE_DECLARATION|done[- ]declaration|OWNER_DIRECTION|r2_r4q6_answer|owner'?s? (recorded )?answer", re.I)
viol = []
for pid, f in packets.items():
    txt = open(f, encoding="utf-8").read()
    for i, line in enumerate(txt.splitlines(), 1):
        if "[GOVERNING]" in line and CTX_PAT.search(line):
            viol.append(f"{pid}:{i}")
    hm = re.search(r"^tier:\s*(\S+)", txt, re.M)
    if pid == "P-24" and hm and hm.group(1).upper() == "GOVERNING":
        viol.append("P-24 header tier GOVERNING")
res.append(("C4 no packet presents CONTEXT as GOVERNING", not viol,
            f"CONTEXT source on a [GOVERNING]-tagged line or GOVERNING tier on the CONTEXT packet: {len(viol)} {viol[:8]}"))

# C5
HEAD = ["## What we found", "## Affected rows", "## Options", "## HELP_HUMAN recommendation (draft)", "## Who decides",
        "## On ruling", "## Risks, contested rows and dependencies"]
FIELDS = ["id", "cluster", "title", "question", "recommended", "depends_on", "decision_type", "tier"]
TAG = re.compile(r"\[(GOVERNING|CONTEXT|code|owner testimony|run finding)\]")
form = []
for pid, f in sorted(packets.items()):
    txt = open(f, encoding="utf-8").read()
    hb = re.search(r"<!-- PACKET\n(.*?)\n-->", txt, re.S)
    if not hb:
        form.append(f"{pid}: no header block")
    else:
        got = {l.split(":", 1)[0].strip() for l in hb.group(1).splitlines() if ":" in l}
        for fl in FIELDS:
            if fl not in got:
                form.append(f"{pid}: header missing {fl}")
    pos = [txt.find(h) for h in HEAD]
    if any(p < 0 for p in pos) or pos != sorted(pos):
        form.append(f"{pid}: headings missing/out of order {[h for h, p in zip(HEAD, pos) if p < 0]}")
    m = re.search(r"## What we found\n(.*?)\n## ", txt, re.S)
    if m:
        buls = re.split(r"\n(?=- )", m.group(1).strip())
        untagged = [b[:50] for b in buls if b.startswith("- ") and not TAG.search(b)]
        if untagged:
            form.append(f"{pid}: {len(untagged)} untagged evidence bullets")
if True:
    absp = []
    for f in glob.glob(os.path.join(R4, "**", "*"), recursive=True):
        if os.path.isfile(f) and f.endswith((".md", ".csv")) and "/_work/pre_owner_check/" not in f and "/BRIEFS/" not in f:
            t = open(f, encoding="utf-8", errors="replace").read()
            if re.search(r"/Users/|/private/tmp/|/tmp/claude", t):
                absp.append(os.path.relpath(f, R4))
    form += [f"absolute path in {a}" for a in absp]
res.append(("C5 packet form (header, headings, evidence tags, no absolute paths)", not form,
            f"problems {len(form)}: {form[:12]}"))

with open(os.path.join(R4, "R4_QA.md"), "w", encoding="utf-8") as fh:
    fh.write("# R4 QA — RUN_D128_CONCORDANCE_2026-09-21_1614Z\n\n")
    fh.write("Built by `R4/_scripts/r4_qa.py` from `R3/CLUSTER_INDEX.csv`, the final R3 concordance, `R4/PACKET_INDEX.csv`, "
             "`R4/PACKET_SUBQUESTIONS.csv` and the packet files. C1–C4 are the checks the R4 brief requires; C5 is a form check.\n\n")
    fh.write("| Check | Verdict | Detail |\n|---|---|---|\n")
    for name, ok, d in res:
        fh.write(f"| {name} | {'PASS' if ok else 'FAIL'} | {d.replace('|', '/')} |\n")
    fh.write("\nInput hashes (SHA-256):\n\n")
    for p in ("R3/CLAIM_CONCORDANCE.csv", "R3/EXTENSION_CONCORDANCE.csv", "R3/CLUSTER_INDEX.csv", "R4/PACKET_INDEX.csv",
              "R4/PACKET_SUBQUESTIONS.csv"):
        fh.write(f"- `{p}` `{sha256(os.path.join(RUN, p))}`\n")
for name, ok, d in res:
    print("PASS" if ok else "FAIL", name, "|", d[:300])
