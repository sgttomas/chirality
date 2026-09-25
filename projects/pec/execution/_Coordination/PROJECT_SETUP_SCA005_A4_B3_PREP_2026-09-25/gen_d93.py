#!/usr/bin/env python3
"""D-PEC-93 exact generator: SCA-005 Lane A4 (DEL-02-08/09 preparation) + Lane B3.

Deterministic. Stdlib only. Run against a repository root whose tree equals
origin/main 6dac281c679e779e9e8507add693554f102242d2 for every touched path.
It fails closed (exit 1, nothing further written) on any preimage mismatch,
pre-existing target folder, ambiguous replacement anchor, CSV round-trip
difference, or a write_status.sh date that differs from --act-date.

Usage:
  python3 gen_d93.py --repo <REPO_ROOT> --act-date YYYY-MM-DD \
      [--actor TASK+preparation] [--mirror-set complete|plan] [--optional-edge]

Option A = defaults (--mirror-set complete, no --optional-edge).
The only varying bytes are the act-date slot (and the actor string).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import subprocess
import sys
from pathlib import Path

PEC = "projects/pec"
EX = f"{PEC}/execution"
WORK02 = f"{EX}/PKG-02_File_Truth_Parsers/1_Working"

DIRS = {
    "DEL-00-02": f"{EX}/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-02_Event_contract_schema_v1",
    "DEL-01-01": f"{EX}/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model",
    "DEL-01-02": f"{EX}/PKG-01_Service_Core_Store/1_Working/DEL-01-02_Presence_tier_schema_entity_model",
    "DEL-02-07": f"{WORK02}/DEL-02-07_adapter_yaml_feed_manifest_consumer",
    "DEL-03-01": f"{EX}/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command",
    "DEL-04-01": f"{EX}/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return",
    "DEL-06-01": f"{EX}/PKG-06_Presence_Git_Observation/1_Working/DEL-06-01_Session_presence_records",
    "DEL-06-04": f"{EX}/PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges",
    "DEL-07-01": f"{EX}/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-01_Idempotent_event_ingest_durable_message_store",
    "DEL-07-02": f"{EX}/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge",
    "DEL-07-03": f"{EX}/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-03_Hooks_CLI_bridge",
    "DEL-07-04": f"{EX}/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional",
    "DEL-07-05": f"{EX}/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2",
    "DEL-09-05": f"{EX}/PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board",
}

# Preimage SHA-256 at 6dac281c6 of every existing file the generator reads as basis or writes.
PREIMAGES = {
    f"{EX}/_Decomposition/Deliverables.csv": "b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a",
    f"{EX}/_Decomposition/ScopeLedger.csv": "83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df",
    f"{PEC}/docs/PRD.md": "fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32",
    f"{DIRS['DEL-00-02']}/_DEPENDENCIES.md": "2242ca8a785ba74d2fc885d86eff606587888af3ff4ed4f21ff52a52b141468f",
    f"{DIRS['DEL-01-01']}/_DEPENDENCIES.md": "91d67bc8fab21e6f62ba084383f5e5dae13ce27aef9cf5824f74c084dc80e6bf",
    f"{DIRS['DEL-01-02']}/_DEPENDENCIES.md": "2e566074e54d1d92fa7dcd5a632ae6d2f782568fcaccc446c915ba139a5dee0f",
    f"{DIRS['DEL-02-07']}/_DEPENDENCIES.md": "f5b6e9d2d84be5415b747cb04e32d5dffd1f38e8040ab41786bcc92bea9afed2",
    f"{DIRS['DEL-03-01']}/_DEPENDENCIES.md": "398f651d4b6701c7dd98cbe72f78c04035f5b1c7de8e9ae2e2e1d8c9837baa60",
    f"{DIRS['DEL-03-01']}/Dependencies.csv": "5f68759d07cc001e139fc351e33748ef7f03ba5ba9cd7ed77a6182ad8161bd65",
    f"{DIRS['DEL-04-01']}/_DEPENDENCIES.md": "ea0578890660a7d00f40a8278bf2ea5e320014d4713565b44b7826830c4b4c0c",
    f"{DIRS['DEL-04-01']}/Dependencies.csv": "2daee4e76382186657c52b01caf5c4435c8d6a501c6d2b305c9b1c9703a916e4",
    f"{DIRS['DEL-06-01']}/_DEPENDENCIES.md": "f2567c0ecd883673e3b2b73870bdfc479ee187a59af8acbad9ac71cb33249590",
    f"{DIRS['DEL-06-04']}/_DEPENDENCIES.md": "a9c3dd391c26628c4510544173f41bc1441b1d2279f384ecda0942da51a73426",
    f"{DIRS['DEL-06-04']}/Dependencies.csv": "f4eaf5266f131437b31cee5edfd5dcbadc9c7aee59e5b41cba76107bc7f7f4fb",
    f"{DIRS['DEL-07-01']}/_DEPENDENCIES.md": "8fc61c243907764803f40b04631b78883ad00b54a2189f727f71997af80ac6cb",
    f"{DIRS['DEL-07-02']}/_DEPENDENCIES.md": "07c16cc4937df6e3c15123cce31a35f99e6274a588ddfea01c450a223c9b9bde",
    f"{DIRS['DEL-07-02']}/Dependencies.csv": "bd4c16fadb7025f1b22c039713fc755a53b18949c85d8a60f8abbb51f8714821",
    f"{DIRS['DEL-07-03']}/_DEPENDENCIES.md": "b100e6b67a39d342751ec9e343d4bf391790bb5ffabb9974d3b001d703b42c69",
    f"{DIRS['DEL-07-04']}/_DEPENDENCIES.md": "cb354e3d4b601eb07047aff4a38dc4841801af0ebd617182265eb543b7a9bfb6",
    f"{DIRS['DEL-07-04']}/Dependencies.csv": "5d684e2425e365b2e09bd3e6e7faf63d5a2efd7acbe50634d52075a30bc90fe6",
    f"{DIRS['DEL-07-05']}/_DEPENDENCIES.md": "ba39a3898a7a76e26ffc72ec9b68a0d2d0db9edf36fd0775def2ddcf3e90981c",
    f"{DIRS['DEL-07-05']}/Dependencies.csv": "4c2c93eafff62d6f00e5668ebaaab40e75f06693a0bf5809478c81d14b4c322f",
    f"{DIRS['DEL-09-05']}/_DEPENDENCIES.md": "c41aa4e4ff8506f409c7f33fe90687906ac7489ec0fecbfa96632091bd77440f",
    f"{DIRS['DEL-09-05']}/Dependencies.csv": "c62d3d262b258be6151bb9ca6d8b8d096db917867febee7fc7bb4d5b0958dd68",
    "tools/scaffolding/scaffold_deliverable.sh": "7a04c1a9a9231befa50a5113de72ea148abc52808bd6c0c5d2b1225e1a7f7a23",
    "tools/scaffolding/write_status.sh": "b6194cc0b6a12b949583fd7b211594da0bbd8d6ead136b1ec01533d5700852ed",
    "tools/validation/check_min_viable_fileset.sh": "a6c4af3c684aa22b2ff9baa89ca4108cfe3a976da04aabfb852371c2c5c20f8c",
}

NEW = {
    "DEL-02-08": {"sow": "SOW-095", "action": "A-19"},
    "DEL-02-09": {"sow": "SOW-096", "action": "A-20"},
}
PACKAGE_NAME = {"PKG-02": "File-Truth Parsers"}
PACKAGE_FOLDER = {"PKG-02": "PKG-02_File_Truth_Parsers"}

C04 = ("- **C-04 (PHASE_PRECEDENCE)** — Release-strategy ordering; hard-vs-soft "
       "classification is a Phase 1.3 owner ruling")
C10 = ("- **C-10 (STRATUM_RULE)** — DECLARED = both endpoints ID-named with a "
       "dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/"
       "grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = "
       "heuristic. All strata require owner acceptance; strata are provenance not authority")

V31 = ["RegisterSchemaVersion", "DependencyID", "FromPackageID", "FromDeliverableID",
       "FromDeliverableName", "DependencyClass", "AnchorType", "Direction",
       "DependencyType", "TargetType", "TargetPackageID", "TargetDeliverableID",
       "TargetRefID", "TargetName", "TargetLocation", "Statement",
       "EvidenceFile", "SourceRef", "EvidenceQuote", "Explicitness",
       "RequiredMaturity", "ProposedMaturity", "SatisfactionStatus", "Confidence",
       "Origin", "FirstSeen", "LastSeen", "Status", "Notes"]


class Fail(Exception):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sanitize(name: str) -> str:
    """D-PEC-62 §3.1 label rule: non-alphanumerics -> _, collapse runs, strip ends."""
    return re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9]", "_", name)).strip("_")


def csv_line(values: list[str]) -> str:
    out = io.StringIO()
    csv.writer(out, lineterminator="\r\n").writerow(values)
    return out.getvalue()


def replace_once(text: str, old: str, new: str, where: str) -> str:
    n = text.count(old)
    if n != 1:
        raise Fail(f"anchor count {n} != 1 in {where}: {old[:80]!r}")
    return text.replace(old, new)


# ---------------------------------------------------------------- A4 content

def context_md(d: dict, act: str) -> str:
    return f"""# _CONTEXT — {d['DeliverableID']}

| Field | Value |
|---|---|
| DeliverableID | {d['DeliverableID']} |
| Canonical name | {d['Name']} |
| PackageID | {d['PackageID']} ({PACKAGE_NAME[d['PackageID']]}) |
| Type | {d['Type']} |
| ContextEnvelope | {d['ContextEnvelope']} |
| PhaseHint | {d['PhaseHint']} |
| CoversScopeItems | {d['CoversScopeItems']} |
| SupportsObjectives | {d['SupportsObjectives']} |
| ResponsibleParty | {d['ResponsibleParty']} (assignment at WORKING_ITEMS activation) |

## Description

{d['Description']}

## Anticipated artifacts

{d['AnticipatedArtifacts']}

## Envelope notes

{d['ContextEnvelopeNotes'] or '(none)'}

## Provenance

Scaffolded under `D-PEC-93` ({act}) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.5 (`current_basis`,
SCA-005 successor; deliverable added by {NEW[d['DeliverableID']]['action']}). Fields templated
deterministically from `Deliverables.csv`; this file restates register truth
and is not an independent authority.
"""


def references_md(d: dict, act: str) -> str:
    pkg = d["PackageID"]
    return f"""# _REFERENCES — {d['DeliverableID']}

- `execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.5, accepted `current_basis`; SCA-005 successor)
- `execution/_Decomposition/Deliverables.csv` (authoritative deliverable register)
- `execution/_Decomposition/ScopeLedger.csv` (SOW→PKG→DEL→OBJ ledger; covers {d['CoversScopeItems']})
- `docs/PRD.md` v2.3 (accepted source corpus; see SourceRef column of the ledger)
- `execution/_ScopeChange/SCA-005_2026-09-23_2139/` (accepted scope change that added this deliverable, {NEW[d['DeliverableID']]['action']})
- `{PACKAGE_FOLDER[pkg]}/0_References/` (package reference staging)
- `execution/_Coordination/_COORDINATION.md` (coordination representation: FULL_GRAPH, threshold INITIALIZED)

Populated deterministically under `D-PEC-93` ({act}); extend during production.
"""


def dependencies_md(d: dict, act: str, upstream: list[tuple], downstream: list[tuple]) -> str:
    lines = [f"# _DEPENDENCIES — {d['DeliverableID']}", "",
             f"Seeded deterministically under `D-PEC-93` ({act}) from accepted",
             f"decomposition revision 1.5 (SCA-005, {NEW[d['DeliverableID']]['action']}) and PRD v2.3; the D-PEC-62",
             "DAG exhibit predates this deliverable. `Dependencies.csv` (v3.1)",
             "is the structured register; this file is the human-readable view.",
             "Register storage is deliverable-local by owner ruling (no central register).", "",
             "## Upstream (this deliverable depends on)", "",
             "| Predecessor | Stratum | Kind | Flag | EdgeID |", "|---|---|---|---|---|"]
    lines += [f"| {pid} ({pname}) | PROPOSAL | CONSUMES |  | {edge} |" for pid, pname, edge in upstream]
    lines += ["", "## Downstream (informational; consumers of this deliverable)", ""]
    lines += [f"- {sid} ({sname}) — CONSUMES [{edge}]" for sid, sname, edge in downstream]
    lines += ["", "## Non-gating constraints and register-wide rules", "", C04, C10, "",
              "## Blocker semantics", "",
              "Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).",
              "Blocker output is advisory visibility only — never work assignment.", ""]
    return "\n".join(lines)


def anchor_rows(d: dict, act: str) -> list[list[str]]:
    del_id, pkg = d["DeliverableID"], d["PackageID"]
    pp, ll = del_id.split("-")[1:]
    sow = d["CoversScopeItems"]
    base = dict(RegisterSchemaVersion="v3.1", FromPackageID=pkg, FromDeliverableID=del_id,
                FromDeliverableName=d["Name"], DependencyClass="ANCHOR", Direction="UPSTREAM",
                DependencyType="OTHER", Explicitness="EXPLICIT", RequiredMaturity="NOT_APPLICABLE",
                ProposedMaturity="TBD", SatisfactionStatus="SATISFIED", Confidence="HIGH",
                Origin="DECLARED", FirstSeen=act, LastSeen=act, Status="ACTIVE",
                Notes="Tree anchor seeded under D-PEC-93")
    r1 = dict(base, DependencyID=f"DEP-{pp}-{ll}-001", AnchorType="IMPLEMENTS_NODE",
              TargetType="PACKAGE", TargetPackageID=pkg, TargetDeliverableID="", TargetRefID=pkg,
              TargetName=PACKAGE_FOLDER[pkg], TargetLocation="execution/_Decomposition/SOFTWARE_DECOMP.md",
              Statement=f"{del_id} is package-local to {pkg}.",
              EvidenceFile="execution/_Decomposition/Deliverables.csv",
              SourceRef=f"Deliverables.csv row {del_id}", EvidenceQuote=f"PackageID {pkg}")
    r2 = dict(base, DependencyID=f"DEP-{pp}-{ll}-002", AnchorType="TRACES_TO_REQUIREMENT",
              TargetType="REQUIREMENT", TargetPackageID="", TargetDeliverableID="", TargetRefID=sow,
              TargetName=sow, TargetLocation="execution/_Decomposition/ScopeLedger.csv",
              Statement=f"{del_id} covers scope item {sow}.",
              EvidenceFile="execution/_Decomposition/ScopeLedger.csv",
              SourceRef=f"ScopeLedger.csv row {sow}", EvidenceQuote=f"DeliverableIDs include {del_id}")
    return [[r[k] for k in V31] for r in (r1, r2)]


def exec_row(dep_id, frm, target, target_dir, statement, evfile, srcref, quote, edge, act):
    r = dict(RegisterSchemaVersion="v3.1", DependencyID=dep_id, FromPackageID=frm["PackageID"],
             FromDeliverableID=frm["DeliverableID"], FromDeliverableName=frm["Name"],
             DependencyClass="EXECUTION", AnchorType="NOT_APPLICABLE", Direction="UPSTREAM",
             DependencyType="PREREQUISITE", TargetType="DELIVERABLE",
             TargetPackageID=target["PackageID"], TargetDeliverableID=target["DeliverableID"],
             TargetRefID=target["DeliverableID"], TargetName=target["Name"],
             TargetLocation=target_dir[len(PEC) + 1:], Statement=statement, EvidenceFile=evfile,
             SourceRef=srcref, EvidenceQuote=quote, Explicitness="IMPLICIT",
             RequiredMaturity="INITIALIZED", ProposedMaturity="TBD", SatisfactionStatus="PENDING",
             Confidence="MEDIUM", Origin="EXTRACTED", FirstSeen=act, LastSeen=act, Status="ACTIVE",
             Notes=f"PROPOSAL; Flag=none; EdgeID={edge}; seeded under D-PEC-93 (SCA-005 B3)")
    return [r[k] for k in V31]


# ---------------------------------------------------------------- B3 CSV edits

RETIRE_REASON = {
    "DEL-06-04": "A-34: DEL-06-04 retired, SOW-029 OUT",
    "DEL-07-02": "A-35: DEL-07-02 retired, SOW-035 OUT",
    "DEL-07-04": "A-78: DEL-07-04 retired, SOW-037 OUT",
    "DEL-07-05": "A-36: DEL-07-05 retired, SOW-087 OUT",
}
RETIRE_ROWS = {
    "DEL-06-04": ["DEP-06-04-001", "DEP-06-04-002", "DEP-06-04-003", "DEP-06-04-004", "DEP-06-04-005", "DEP-06-04-006"],
    "DEL-07-02": ["DEP-07-02-001", "DEP-07-02-002", "DEP-07-02-003", "DEP-07-02-004"],
    "DEL-07-04": ["DEP-07-04-001", "DEP-07-04-002", "DEP-07-04-003", "DEP-07-04-004"],
    "DEL-07-05": ["DEP-07-05-001", "DEP-07-05-002", "DEP-07-05-003", "DEP-07-05-005"],
}


def edit_register(path: Path, edits: dict[str, dict], appends: list[list[str]]) -> bytes:
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    lines = text.split("\r\n")
    if lines[-1] != "" or any("\n" in ln for ln in lines):
        raise Fail(f"{path}: not uniformly CRLF-terminated single-line rows")
    lines = lines[:-1]
    header = next(csv.reader([lines[0]]))
    if header != V31:
        raise Fail(f"{path}: header is not exact v3.1")
    seen = set()
    out = [lines[0] + "\r\n"]
    for ln in lines[1:]:
        values = next(csv.reader([ln]))
        if csv_line(values) != ln + "\r\n":
            raise Fail(f"{path}: row does not round-trip byte-exactly: {values[1]}")
        dep = values[1]
        if dep in edits:
            row = dict(zip(V31, values))
            if row["Status"] != "ACTIVE":
                raise Fail(f"{path}: {dep} is not ACTIVE")
            for k, v in edits[dep].items():
                row[k] = v(row[k]) if callable(v) else v
            out.append(csv_line([row[k] for k in V31]))
            seen.add(dep)
        else:
            out.append(ln + "\r\n")
    if seen != set(edits):
        raise Fail(f"{path}: rows not found {sorted(set(edits) - seen)}")
    existing = {next(csv.reader([ln]))[1] for ln in lines[1:]}
    for row in appends:
        if row[1] in existing:
            raise Fail(f"{path}: {row[1]} already exists")
        out.append(csv_line(row))
    return "".join(out).encode("utf-8")


# ---------------------------------------------------------------- mirror edits

def struck_bullet(text, why, row, act):
    return (f"- ~~{text}~~ — **RETIRED {act} under SCA-005 (D-PEC-93)**: {why}; "
            f"register row `{row}` kept with `Status=RETIRED`\n")


def struck_row(pred, stratum, kind, flag, edge):
    return f"| ~~{pred}~~ | {stratum} | {kind} | {flag} | ~~{edge}~~ |\n"


def mirror_edits(act: str, complete: bool, optional: bool) -> dict[str, list[tuple[str, str]]]:
    E = {}

    def bullet(del_id, text, why, row):
        E.setdefault(del_id, []).append((f"- {text}\n", struck_bullet(text, why, row, act)))

    def row(del_id, pred, stratum, kind, flag, edge):
        E.setdefault(del_id, []).append((f"| {pred} | {stratum} | {kind} | {flag} | {edge} |\n",
                                         struck_row(pred, stratum, kind, flag, edge)))

    # Plan-named consumer mirrors (Propagation_Plan.md B3 last row)
    bullet("DEL-00-02", "DEL-07-02 (Daemon SSE subscriber bridge) — CONSUMES [E-A03]", "DEL-07-02 retired (A-35)", "DEP-07-02-003")
    bullet("DEL-00-02", "DEL-07-04 (cmux socket adapter (optional)) — CONSUMES [E-A04]", "DEL-07-04 retired (A-78)", "DEP-07-04-003")
    bullet("DEL-00-02", "DEL-07-05 (Shared-runtime client seam (v2)) — CONSUMES [E-N01]", "DEL-07-05 retired (A-36)", "DEP-07-05-003")
    bullet("DEL-01-01", "DEL-07-05 (Shared-runtime client seam (v2)) — CONSUMES [E-P14]", "DEL-07-05 retired (A-36)", "DEP-07-05-005")
    E["DEL-01-01"].append((
        "`DEP-07-05-005` kept with `Status=RETIRED`\n",
        "`DEP-07-05-005` kept with `Status=RETIRED`\n"
        "- DEL-02-08 (Work-graph parser) — CONSUMES [E-P79]\n"
        "- DEL-02-09 (MEMORY run-index parser) — CONSUMES [E-P80]\n"))
    bullet("DEL-01-02", "DEL-06-04 (Live hierarchy edges) — CONSUMES [E-N09]", "DEL-06-04 retired (A-34)", "DEP-06-04-003")
    bullet("DEL-06-01", "DEL-06-04 (Live hierarchy edges) — CONSUMES [E-N10]", "DEL-06-04 retired (A-34)", "DEP-06-04-004")
    bullet("DEL-07-01", "DEL-07-02 (Daemon SSE subscriber bridge) — CONSUMES [E-P48]", "DEL-07-02 retired (A-35)", "DEP-07-02-004")
    bullet("DEL-07-01", "DEL-07-04 (cmux socket adapter (optional)) — CONSUMES [E-P50]", "DEL-07-04 retired (A-78)", "DEP-07-04-004")
    bullet("DEL-07-03", "DEL-06-04 (Live hierarchy edges) — CONSUMES [E-P47]", "DEL-06-04 retired (A-34)", "DEP-06-04-006")
    row("DEL-09-05", "DEL-06-04 (Live hierarchy edges)", "DERIVED", "CONSUMES", "PHASE_TENSION", "E-N02")
    E["DEL-09-05"].append((
        "| E-P66 |\n\n## Non-gating",
        "| E-P66 |\n\n"
        f"**RETIRED {act} under SCA-005 (D-PEC-93):** `E-N02` — register row `DEP-09-05-005`\n"
        "kept with `Status=RETIRED`: DEL-06-04 is retired and the presence board no longer\n"
        "renders live hierarchy edges (A-33, A-38).\n\n## Non-gating"))
    row("DEL-03-01", "DEL-02-07 (`adapter.yaml` feed-manifest consumer)", "PROPOSAL", "CONSUMES", "", "E-P25")
    E["DEL-03-01"].append((
        "| ~~E-P25~~ |\n\n## Downstream",
        "| ~~E-P25~~ |\n"
        "| DEL-02-08 (Work-graph parser) | PROPOSAL | CONSUMES |  | E-P81 |\n"
        "| DEL-02-09 (MEMORY run-index parser) | PROPOSAL | CONSUMES |  | E-P82 |\n\n"
        f"**SCA-005 dependency refresh {act} (D-PEC-93):** `E-P25` is retired — register\n"
        "row `DEP-03-01-014` kept with `Status=RETIRED`, because `_harness/adapter.yaml`\n"
        "is a parity-peer input, not the feed manifest (A-07, A-18). `E-P18`\n"
        "(`DEP-03-01-007`) now cites PRD v2.3 PEC-RCN-002: each loop-registry row declares\n"
        "the feed profile the reconciler reads. `E-P81` and `E-P82` (`DEP-03-01-015`,\n"
        "`DEP-03-01-016`) add the work-graph and MEMORY run-index parsers (A-19, A-20).\n\n"
        "## Downstream"))
    if complete:
        # Completeness mirrors: every other _DEPENDENCIES.md that names a retired edge
        bullet("DEL-02-07", "DEL-03-01 (Full-rebuild reconciler (one command)) — CONSUMES [E-P25]",
               "`_harness/adapter.yaml` is a parity-peer input, not the feed manifest (A-07, A-18)", "DEP-03-01-014")
        own = {
            "DEL-06-04": ("A-34; SOW-029 OUT", "`DEP-06-04-001`/`002` and execution rows `DEP-06-04-003`..`006`",
                          [("DEL-01-02 (Presence-tier schema & entity model)", "PROPOSAL", "E-N09"),
                           ("DEL-06-01 (Session presence records)", "PROPOSAL", "E-N10"),
                           ("DEL-07-02 (Daemon SSE subscriber bridge)", "DERIVED", "E-P46"),
                           ("DEL-07-03 (Hooks CLI bridge)", "DERIVED", "E-P47")], "E-P47"),
            "DEL-07-02": ("A-35; SOW-035 OUT", "`DEP-07-02-001`/`002` and execution rows `DEP-07-02-003`/`004`",
                          [("DEL-00-02 (Event-contract schema v1)", "DERIVED", "E-A03"),
                           ("DEL-07-01 (Idempotent event ingest + durable message store)", "PROPOSAL", "E-P48")], "E-P48"),
            "DEL-07-04": ("A-78; SOW-037 OUT", "`DEP-07-04-001`/`002` and execution rows `DEP-07-04-003`/`004`",
                          [("DEL-00-02 (Event-contract schema v1)", "DERIVED", "E-A04"),
                           ("DEL-07-01 (Idempotent event ingest + durable message store)", "PROPOSAL", "E-P50")], "E-P50"),
            "DEL-07-05": ("A-36; SOW-087 OUT", "`DEP-07-05-001`/`002` and execution rows `DEP-07-05-003`/`005`",
                          [("DEL-00-02 (Event-contract schema v1)", "DERIVED", "E-N01"),
                           ("DEL-01-01 (Record-tier schema & entity model)", "PROPOSAL", "E-P14")], "E-P14"),
        }
        for del_id, (why, rows, preds, last) in own.items():
            for pred, stratum, edge in preds:
                row(del_id, pred, stratum, "CONSUMES", "", edge)
            para = (f"**RETIRED {act} under SCA-005 (D-PEC-93):** {del_id} is retired ({why}).\n"
                    f"Every row of `Dependencies.csv` is kept with `Status=RETIRED` — tree anchors\n"
                    f"{rows}; the struck edges above no longer gate or feed any deliverable.\n\n")
            nxt = "**DECLINED" if del_id == "DEL-07-05" else "## "
            E[del_id].append((f"| ~~{last}~~ |\n\n{nxt}", f"| ~~{last}~~ |\n\n{para}{nxt}"))
        bullet("DEL-06-04", "DEL-09-05 (Presence board) — CONSUMES [E-N02]", "DEL-06-04 retired (A-34, A-38)", "DEP-09-05-005")
        bullet("DEL-07-02", "DEL-06-04 (Live hierarchy edges) — CONSUMES [E-P46]", "DEL-06-04 and DEL-07-02 retired (A-34, A-35)", "DEP-06-04-005")
    if optional:
        E.setdefault("DEL-04-01", []).append((
            "| DEL-03-01 (Full-rebuild reconciler (one command)) | PROPOSAL | CONSUMES |  | E-P32 |\n",
            "| DEL-03-01 (Full-rebuild reconciler (one command)) | PROPOSAL | CONSUMES |  | E-P32 |\n"
            "| DEL-02-08 (Work-graph parser) | PROPOSAL | CONSUMES |  | E-P83 |\n"))
    return E


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    ap.add_argument("--act-date", required=True)
    ap.add_argument("--actor", default="TASK+preparation")
    ap.add_argument("--mirror-set", choices=["complete", "plan"], default="complete")
    ap.add_argument("--optional-edge", action="store_true")
    a = ap.parse_args()
    repo, act = a.repo.resolve(), a.act_date
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", act):
        raise Fail("act-date must be YYYY-MM-DD")
    report = []
    try:
        # 0. preconditions (write_status.sh stamps the local date; it must equal the slot)
        import time
        if time.strftime("%Y-%m-%d") != act:
            raise Fail(f"local date {time.strftime('%Y-%m-%d')} != --act-date {act}; nothing written")
        for rel, want in PREIMAGES.items():
            p = repo / rel
            got = sha(p.read_bytes())
            if got != want:
                raise Fail(f"preimage mismatch {rel}: {got} != {want}")
            report.append(("READ", rel, got, ""))
        with open(repo / f"{EX}/_Decomposition/Deliverables.csv", newline="", encoding="utf-8") as f:
            dels = {r["DeliverableID"]: r for r in csv.DictReader(f)}
        folders = {}
        for del_id in NEW:
            d = dels[del_id]
            label = sanitize(d["Name"])
            folder = repo / WORK02 / f"{del_id}_{label}"
            if list((repo / WORK02).glob(f"{del_id}_*")):
                raise Fail(f"target folder exists for {del_id}")
            folders[del_id] = folder

        writes: list[tuple[Path, bytes]] = []
        d01, d0301, d0401 = dels["DEL-01-01"], dels["DEL-03-01"], dels["DEL-04-01"]
        d08, d09 = dels["DEL-02-08"], dels["DEL-02-09"]
        # 1-4. compute every postimage and check every anchor before any write
        dir08 = str(folders["DEL-02-08"].relative_to(repo))
        dir09 = str(folders["DEL-02-09"].relative_to(repo))
        prd = f"{PEC}/docs/PRD.md"
        rows = {
            "DEL-02-08": anchor_rows(d08, act) + [exec_row(
                "DEP-02-08-003", d08, d01, DIRS["DEL-01-01"], "Parser emits WorkGraph/WorkNode entities of the record-tier model",
                "execution/_Decomposition/Deliverables.csv", "Deliverables.csv row DEL-01-01 Description",
                "16 entity types (Workplan/Step/Gate, Package/Deliverable and WorkGraph/WorkNode are compound rows)", "E-P79", act)],
            "DEL-02-09": anchor_rows(d09, act) + [exec_row(
                "DEP-02-09-003", d09, d01, DIRS["DEL-01-01"], "Parser emits RunRecord join evidence from the MEMORY run index",
                "execution/_Decomposition/Deliverables.csv", "Deliverables.csv row DEL-01-01 Description",
                "RunRecord is sourced from central receipts, work graphs and the MEMORY run index", "E-P80", act)],
        }
        down08 = [("DEL-03-01", d0301["Name"], "E-P81")] + ([("DEL-04-01", d0401["Name"], "E-P83")] if a.optional_edge else [])
        spec = {
            "DEL-02-08": ([("DEL-01-01", d01["Name"], "E-P79")], down08),
            "DEL-02-09": ([("DEL-01-01", d01["Name"], "E-P80")], [("DEL-03-01", d0301["Name"], "E-P82")]),
        }
        for del_id, folder in folders.items():
            d = dels[del_id]
            writes.append((folder / "_CONTEXT.md", context_md(d, act).encode()))
            writes.append((folder / "_REFERENCES.md", references_md(d, act).encode()))
            writes.append((folder / "_DEPENDENCIES.md", dependencies_md(d, act, *spec[del_id]).encode()))
            writes.append((folder / "Dependencies.csv", (csv_line(V31) + "".join(csv_line(r) for r in rows[del_id])).encode()))
        # 2. B3 — register edits
        for del_id, deps in RETIRE_ROWS.items():
            why = RETIRE_REASON[del_id]
            ed = {dep: {"Status": "RETIRED", "LastSeen": act,
                        "Notes": (lambda old, w=why: f"Retired under SCA-005 ({w}); {old}")} for dep in deps}
            p = repo / DIRS[del_id] / "Dependencies.csv"
            writes.append((p, edit_register(p, ed, [])))
        p = repo / DIRS["DEL-09-05"] / "Dependencies.csv"
        writes.append((p, edit_register(p, {"DEP-09-05-005": {
            "Status": "RETIRED", "LastSeen": act,
            "Notes": lambda old: f"Retired under SCA-005 (A-33, A-38: target DEL-06-04 retired); {old}"}}, [])))
        p = repo / DIRS["DEL-03-01"] / "Dependencies.csv"
        writes.append((p, edit_register(p, {
            "DEP-03-01-014": {"Status": "RETIRED", "LastSeen": act,
                              "Notes": lambda old: ("Retired under SCA-005 (A-07, A-18: adapter.yaml is a parity-peer input, "
                                                    f"not the feed manifest; see DEP-03-01-007); {old}")},
            "DEP-03-01-007": {"EvidenceFile": "docs/PRD.md", "SourceRef": "PRD.md §9.2 requirement PEC-RCN-002",
                              "EvidenceQuote": "The reconciler shall ingest, per the closed, PEC-versioned feed profile declared on each loop-registry row",
                              "LastSeen": act,
                              "Notes": lambda old: ("Evidence refreshed under SCA-005 (A-07, A-18: loop-registry feed profiles "
                                                    f"replace the adapter.yaml feed manifest); {old}")},
        }, [
            exec_row("DEP-03-01-015", d0301, d08, dir08, "Full rebuild ingests work graphs", "docs/PRD.md",
                     "PRD.md §9.2 requirement PEC-RCN-002",
                     "work graphs `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`", "E-P81", act),
            exec_row("DEP-03-01-016", d0301, d09, dir09, "Full rebuild ingests the MEMORY run index", "docs/PRD.md",
                     "PRD.md §9.2 requirement PEC-RCN-002",
                     "run evidence — deliverable `MEMORY.md` run-index entries as RunRecord join evidence", "E-P82", act),
        ])))
        if a.optional_edge:
            p = repo / DIRS["DEL-04-01"] / "Dependencies.csv"
            writes.append((p, edit_register(p, {}, [exec_row(
                "DEP-04-01-006", d0401, d08, dir08, "Orientation reads work-graph node states", "docs/PRD.md",
                "PRD.md §9.1 requirement PEC-ORI-001",
                "gate states (from decision registers, scope-change state and work-graph `BLOCKED` nodes)", "E-P83", act)])))
        # 3. mirror edits
        for del_id, pairs in mirror_edits(act, a.mirror_set == "complete", a.optional_edge).items():
            p = repo / DIRS[del_id] / "_DEPENDENCIES.md"
            text = p.read_text(encoding="utf-8")
            for old, new in pairs:
                text = replace_once(text, old, new, str(p))
            writes.append((p, text.encode("utf-8")))
        # 4. evidence quotes must be verbatim in their evidence files
        prd_text = (repo / prd).read_text(encoding="utf-8")
        dcsv = (repo / f"{EX}/_Decomposition/Deliverables.csv").read_text(encoding="utf-8")
        for q in ["The reconciler shall ingest, per the closed, PEC-versioned feed profile declared on each loop-registry row",
                  "work graphs `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`",
                  "run evidence — deliverable `MEMORY.md` run-index entries as RunRecord join evidence",
                  "gate states (from decision registers, scope-change state and work-graph `BLOCKED` nodes)"]:
            if q not in prd_text:
                raise Fail(f"quote not verbatim in PRD: {q}")
        for q in ["16 entity types (Workplan/Step/Gate, Package/Deliverable and WorkGraph/WorkNode are compound rows)",
                  "RunRecord is sourced from central receipts, work graphs and the MEMORY run index"]:
            if q not in dcsv:
                raise Fail(f"quote not verbatim in Deliverables.csv: {q}")
        # 5a. A4 — every check passed: create folders with the repository tools
        for del_id, folder in folders.items():
            d = dels[del_id]
            folder.mkdir()
            r = subprocess.run(["zsh", str(repo / "tools/scaffolding/write_status.sh"), str(folder), "OPEN", a.actor],
                               capture_output=True, text=True)
            if r.returncode != 0:
                raise Fail(f"write_status.sh {del_id}: {r.returncode} {r.stdout}{r.stderr}")
            r = subprocess.run(["zsh", str(repo / "tools/scaffolding/scaffold_deliverable.sh"), str(repo / WORK02),
                                del_id, sanitize(d["Name"])], capture_output=True, text=True)
            if r.returncode != 0:
                raise Fail(f"scaffold_deliverable.sh {del_id}: {r.stdout}{r.stderr}")
            created = sorted(Path(x.split("CREATED_PATH: ", 1)[1]).name for x in r.stdout.splitlines() if x.startswith("CREATED_PATH: "))
            if created != ["_CONTEXT.md", "_DEPENDENCIES.md", "_REFERENCES.md", "_SEMANTIC.md"]:
                raise Fail(f"unexpected created set {del_id}: {created}")
            status = (folder / "_STATUS.md").read_text(encoding="utf-8")
            if f"**Last Updated:** {act}\n" not in status:
                raise Fail(f"write_status.sh date differs from --act-date for {del_id}")
            for stub in ("_CONTEXT.md", "_DEPENDENCIES.md", "_REFERENCES.md"):
                if (folder / stub).stat().st_size != 0:
                    raise Fail(f"stub not empty {del_id}/{stub}")
        # 5b. commit writes (all computed before any existing file is overwritten)
        for p, data in writes:
            pre = sha(p.read_bytes()) if p.exists() and p.stat().st_size else "(new)"
            p.write_bytes(data)
            report.append(("WRITE", str(p.relative_to(repo)), pre, sha(data)))
        for del_id, folder in folders.items():
            for name in ("_STATUS.md", "_SEMANTIC.md"):
                q = folder / name
                report.append(("WRITE", str(q.relative_to(repo)), "(new)", sha(q.read_bytes())))
            r = subprocess.run(["zsh", str(repo / "tools/validation/check_min_viable_fileset.sh"), str(folder)],
                               capture_output=True, text=True)
            report.append(("CHECK", f"check_min_viable_fileset {del_id}", str(r.returncode), r.stdout.strip()))
            if r.returncode != 0:
                raise Fail(r.stdout)
    except Fail as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    for kind, path, pre, post in report:
        print(f"{kind}\t{path}\t{pre}\t{post}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
