"""Shared helpers for R4 scripts (RUN_D128). Deterministic; no model judgment.
Paths are resolved relative to the run folder; nothing absolute is written to outputs."""
import collections, csv, hashlib, os, re, sys

RUN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R3 = os.path.join(RUN, "R3")
R4 = os.path.join(RUN, "R4")
sys.path.insert(0, os.path.join(R3, "_scripts"))
from r3lib import read_csv, write_csv  # noqa: E402

PLAIN = collections.OrderedDict([
    ("ALIGNED", "Matches"),
    ("IMPLEMENTED_UNDOCUMENTED", "Built, not written down"),
    ("DOCUMENTED_UNIMPLEMENTED", "Written, not built"),
    ("PARTIALLY_IMPLEMENTED", "Partly built"),
    ("IMPLEMENTED_DIFFERENTLY", "Built differently"),
    ("STALE_SPECIFICATION", "Text out of date"),
    ("STALE_ASSESSMENT", "Old assessment overtaken"),
    ("STALE_VERIFICATION", "Verification out of date"),
    ("ACCEPTED_DIVERGENCE", "Difference already permitted"),
    ("RETIRED_BY_RULING", "Retired by a ruling"),
    ("LIFECYCLE_REASSESSMENT_REQUIRED", "Lifecycle needs reassessing"),
    ("REMAINING_STATE_MISMATCH", "To-do list out of step"),
    ("DEFERRED_AGENT_WORKFLOW", "Agent-instruction matter"),
    ("AUTHORITY_CONFLICT", "Governing texts disagree"),
    ("UNKNOWN", "Unknown"),
    ("NOT_AUDITABLE", "Nothing to check"),
])


def cid_to_pid(cid):
    return "P-EX" if cid == "CL-EX" else "P-" + cid.split("-")[1]


def load_concordance():
    rows = {}
    for f in ("CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"):
        for r in read_csv(os.path.join(R3, f))[1]:
            rows[r["ClaimKey"]] = r
    return rows


def load_cluster_index():
    return [r for r in read_csv(os.path.join(R3, "CLUSTER_INDEX.csv"))[1]]


def pkg_of(r):
    return r["PackageID"]


def counts_table(keys, conc):
    """Markdown table: package x plain Disposition (+ code), totals. Deterministic."""
    c = collections.Counter((pkg_of(conc[k]), conc[k]["Disposition"]) for k in keys)
    pkgs = sorted({p for p, _ in c})
    disps = [d for d in PLAIN if any(c[(p, d)] for p in pkgs)]
    out = ["| Package | " + " | ".join(f"{PLAIN[d]} (`{d}`)" for d in disps) + " | Total |",
           "|---|" + "---:|" * (len(disps) + 1)]
    for p in pkgs:
        out.append(f"| {p} | " + " | ".join(str(c[(p, d)] or "") for d in disps) + f" | {sum(c[(p, d)] for d in disps)} |")
    out.append("| **Total** | " + " | ".join(f"**{sum(c[(p, d)] for p in pkgs)}**" for d in disps) + f" | **{len(keys)}** |")
    return "\n".join(out)


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()
