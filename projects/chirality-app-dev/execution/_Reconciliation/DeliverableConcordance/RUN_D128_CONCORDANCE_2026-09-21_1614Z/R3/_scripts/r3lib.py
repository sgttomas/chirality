"""Shared helpers for R3 synthesis scripts (RUN_D128). Deterministic; no model judgment.

Paths are resolved relative to the run folder; nothing absolute is written to outputs.
"""
import csv, hashlib, io, os, re

RUN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R2 = os.path.join(RUN, "R2")
R3 = os.path.join(RUN, "R3")
WORK = os.path.join(R3, "_work")

HEADER = [
    "ClaimKey", "ClaimID", "PackageID", "DeliverableID", "ClaimType", "NormativeSource",
    "AuthorityTier", "LatestDecision", "DeclaredState", "RecordedRemaining", "RemainingSource",
    "RemainingGate", "MechanicallyUnblocked", "ImplementationEvidence", "VerificationEvidence",
    "LifecycleState", "AssessmentEvidence", "DirectionEvidence", "PostReleaseBasis", "Disposition",
    "CauseTag", "Confidence", "RemainingWork", "HumanDecisionNeeded", "Notes",
]

# Ledgers of record, identified from each package's STATE.jsonl and PACKAGE_SUMMARY.md
# (superseded attempts, double-blind B ledgers and split halves are evidence only).
DELIVERABLE_LEDGERS = [
    "PKG-00/DEL-00-01", "PKG-00/DEL-00-02",
    "PKG-01/DEL-01-01", "PKG-01/DEL-01-02", "PKG-01/DEL-01-03_A", "PKG-01/DEL-01-04",
    "PKG-02/DEL-02-01", "PKG-02/DEL-02-02", "PKG-02/DEL-02-03", "PKG-02/DEL-02-04", "PKG-02/DEL-02-05",
    "PKG-03/DEL-03-01", "PKG-03/DEL-03-02", "PKG-03/DEL-03-03", "PKG-03/DEL-03-04",
    "PKG-04/DEL-04-01", "PKG-04/DEL-04-02", "PKG-04/DEL-04-03", "PKG-04/DEL-04-04", "PKG-04/DEL-04-05",
    "PKG-05/DEL-05-01", "PKG-05/DEL-05-02_A", "PKG-05/DEL-05-03", "PKG-05/DEL-05-04", "PKG-05/DEL-05-05",
    "PKG-06/DEL-06-01_RERUN", "PKG-06/DEL-06-02_A", "PKG-06/DEL-06-03", "PKG-06/DEL-06-04_RERUN",
    "PKG-06/DEL-06-05", "PKG-06/DEL-06-06_RERUN",
    "PKG-07/DEL-07-01", "PKG-07/DEL-07-02_A", "PKG-07/DEL-07-03", "PKG-07/DEL-07-04", "PKG-07/DEL-07-05",
    "PKG-07/DEL-07-06",
    "PKG-08/DEL-08-01", "PKG-08/DEL-08-02", "PKG-08/DEL-08-03", "PKG-08/DEL-08-04", "PKG-08/DEL-08-05",
    "PKG-09/DEL-09-01", "PKG-09/DEL-09-02_A", "PKG-09/DEL-09-03", "PKG-09/DEL-09-04", "PKG-09/DEL-09-05",
    "PKG-09/DEL-09-06", "PKG-09/DEL-09-07",
    "PKG-10/DEL-10-01", "PKG-10/DEL-10-02", "PKG-10/DEL-10-03", "PKG-10/DEL-10-04", "PKG-10/DEL-10-05",
]
EXT_LEDGERS = [
    "EXT/DEC/DEC", "EXT/SOW/SOW",
    "EXT/DOC_REL/DOC-BUILDREL", "EXT/DOC_REL/DOC-RQGATES", "EXT/DOC_REL/DOC-RQRUN",
    "EXT/DOC_VAL/DOC-RELIANCE", "EXT/DOC_VAL/DOC-VALSTRAT",
    "EXT/DOC_DEV/DOC-PRODAGENTS", "EXT/DOC_DEV/DOC-README", "EXT/DOC_DEV/DOC-RUNTIME_ENGINE_CONTRACT",
    "EXT/DOC_DEV/DOC-TOOL_CATALOG", "EXT/DOC_DEV/DOC-TRACEABILITY",
    "EXT/DOC_DEV_R1/DOC-ADDING_A_TOOL",
]
# Expected SHA-256 prefixes of the ledgers of record (from STATE.jsonl / Addendum 11).
EXPECTED_SHA = {
    "PKG-04/DEL-04-05": "277a6777a1867def62fae5c1fbe6e2f3f8692566f7794fa06fa11e441ced39d4",
    "PKG-06/DEL-06-01_RERUN": "461799194da83088b879714bf1773517c017d181555efc8aff9749f3cd012d8a",
    "PKG-06/DEL-06-04_RERUN": "839f78e13c4c41de25a706deb2fe52c813b609dbeb8227f32f84ab9ebfaa250a",
    "PKG-06/DEL-06-06_RERUN": "036f0a6c040ec73967f4fa221f191cdd4f3dacdc574c1b8a54832471f2eb0c29",
    "PKG-01/DEL-01-02": "59ad30af76b3beb512b25ae42d9ab66aade5689c3fc1fcf23171ef1302cb2bad",
    "PKG-02/DEL-02-01": "5cf0d2620c90c337a3a5a110c2886c97891077fec08e609e9657d07e6772f360",
    "PKG-09/DEL-09-04": "be6f865c16da843757b361468be147e6172ded925da075558c6798cf7c4d9374",
    "PKG-09/DEL-09-05": "3038765cd14efe3f69c93942e542b1de0a0cd9d3a33e1bdca32cf49ca9d9fc2d",
    "EXT/SOW/SOW": "42535b767466d709c29920f7110445a440ee44816f424632bc6003941bf5c352",
    "EXT/DOC_DEV_R1/DOC-ADDING_A_TOOL": "655604ed7d20dc6c00070e1fd6f13340b644f1c225fe4851e0973890de9c8f26",
}
DB_B_LEDGER = "PKG-06/DEL-06-02_B"
DB_B_KEYS = ["DEL-06-02#CLM-005", "DEL-06-02#CLM-032"]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def rel(path):
    return os.path.relpath(path, RUN)


def read_csv(path, require_end=True):
    """Parse a run CSV (header, rows, final #END record). Returns (header, rows as dicts)."""
    with open(path, encoding="utf-8", newline="") as f:
        txt = f.read()
    rows = list(csv.reader(io.StringIO(txt)))
    while rows and rows[-1] == []:
        rows.pop()
    if rows and rows[-1] == ["#END"]:
        rows = rows[:-1]
    elif require_end:
        raise ValueError(f"{rel(path)}: missing #END")
    rows.append(["#END"])
    header = rows[0]
    out = []
    for r in rows[1:-1]:
        if r == []:
            continue
        if len(r) != len(header):
            raise ValueError(f"{rel(path)}: row width {len(r)} != {len(header)}: {r[:1]}")
        out.append(dict(zip(header, r)))
    return header, out


def write_csv(path, header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    for r in rows:
        w.writerow([r.get(c, "") for c in header])
    buf.write("#END\n")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(buf.getvalue())


def ledger_path(stem):
    d, name = os.path.split(stem)
    folder = os.path.join(R2, stem) if not stem.startswith("EXT/") else os.path.join(R2, d)
    if stem.startswith("EXT/"):
        return os.path.join(R2, d, f"{name}_claims.csv"), os.path.join(R2, d, f"{name}_errata.csv")
    del_id = os.path.basename(stem).split("_")[0]
    return (os.path.join(folder, f"{del_id}_claims.csv"), os.path.join(folder, f"{del_id}_errata.csv"))


def reverse_path(stem):
    folder = os.path.join(R2, stem)
    del_id = os.path.basename(stem).split("_")[0]
    return os.path.join(folder, f"{del_id}_reverse.csv")


REACH_RE = re.compile(r"REACH=(LIVE|LEGACY_ONLY|TEST_ONLY)")


def reach_tags(ev):
    return REACH_RE.findall(ev or "")


def hdn_tokens(v):
    return [t.strip() for t in (v or "").split(";") if t.strip()]


def hdn_join(tokens):
    toks = [t for t in tokens if t and t != "NO"]
    # stable, de-duplicated
    seen = []
    for t in toks:
        if t not in seen:
            seen.append(t)
    return "; ".join(seen) if seen else "NO"
