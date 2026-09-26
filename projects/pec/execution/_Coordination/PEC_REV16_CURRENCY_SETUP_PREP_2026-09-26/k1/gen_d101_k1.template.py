#!/usr/bin/env python3
"""D-PEC-101 part K1 exact generator: SCA-006 Lane B1 (DEL-08-06 / DEL-10-13 setup),
B2 (dependency rows and SOW-097..100 anchors, audit COV-080) and B3 (two EvidenceQuotes).

Deterministic. Stdlib only. Run against a repository root whose bytes equal
origin/main aca930622ba167689881416044ba0feaee3ef003 for every path in PREIMAGES.
Independent of part K4 (the revision-1.6 re-pin of existing _CONTEXT.md and
_REFERENCES.md): K1 reads none of K4's targets, so the two parts may run in
either order or alone.

Fail-closed checks before the first write:
  * every PREIMAGES path hashes to its pinned SHA-256 (write targets, read-only
    basis files and the three repository tools it invokes);
  * neither target folder exists (no DEL-08-06_* under PKG-08/1_Working, no
    DEL-10-13_* under PKG-10/1_Working);
  * the local date equals --act-date (write_status.sh stamps the local date),
    unless --reproduction is given (a verifier replaying a recorded date on a
    scratch export; the _STATUS.md date is then rewritten to --act-date);
  * every _CONTEXT.md field equals its revision-1.6 Deliverables.csv cell;
  * every CSV row of every touched register round-trips byte-exactly, so only
    the named cells change and appended rows are the only additions;
  * every mirror anchor occurs exactly once;
  * every new or refreshed EvidenceQuote is a verbatim substring of its cited
    locus (the named register cell, or the PRD requirement row / section line);
  * after rendering, every ACTIVE EXECUTION row of every Dependencies.csv under
    projects/pec/execution has a verbatim EvidenceQuote in its EvidenceFile;
  * no new DependencyID or EdgeID collides with one already in use;
  * the write set equals the grant.
Only then does it create the two folders with the repository tools
(write_status.sh OPEN, then scaffold_deliverable.sh) and write. It exits 1 on
any failure; a second run exits 1 (preimages changed, folders exist).

Usage:
  python3 gen_d101_k1.py --repo <REPO_ROOT> --act-date YYYY-MM-DD
      [--actor TASK+preparation] [--check-only] [--reproduction]

The only varying bytes are the act-date slot {D} (and the actor string).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import subprocess
import sys
import time
from pathlib import Path

PEC = "projects/pec"
EX = f"{PEC}/execution"
DCSV_REL = "execution/_Decomposition/Deliverables.csv"
LCSV_REL = "execution/_Decomposition/ScopeLedger.csv"
PRD_REL = "docs/PRD.md"
W08 = f"{EX}/PKG-08_API_Access/1_Working"
W10 = f"{EX}/PKG-10_Validation_Measurement/1_Working"

# @@PINNED@@

NEW = {
    "DEL-08-06": {"work": W08, "sow": "SOW-099", "action": "A-28", "anchor_actions": "A-26, A-28",
                  "pkg_name": "API & Access", "pkg_folder": "PKG-08_API_Access"},
    "DEL-10-13": {"work": W10, "sow": "SOW-100", "action": "A-29", "anchor_actions": "A-27, A-29",
                  "pkg_name": "Validation & Measurement", "pkg_folder": "PKG-10_Validation_Measurement"},
}
SCA6 = "execution/_ScopeChange/SCA-006_2026-09-25_1912/"

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

# Locus kinds: ("D", DeliverableID, column) = Deliverables.csv cell;
# ("P", RequirementID, None) = the single PRD requirement table row;
# ("S", literal line prefix, None) = the single PRD line starting with that text.
API007 = ("P", "PEC-API-007", None)
AGENT_CLASS = ("S", "  class is read-only query access for tool calls: orientation, deltas, gate", None)
D1013 = ("D", "DEL-10-13", "Description")
Q_API_RESP = "over the same versioned API and responses (PEC-API-003, PEC-API-004, PEC-API-006, PEC-ORI-007)"
Q_PARSERS = "the PKG-02 parser fixture suites"
SR_API007 = "PRD.md §9.6 requirement PEC-API-007"
SR_AGENT = "PRD.md §8 access classes (`agent` class)"
SR_D1013 = "Deliverables.csv row DEL-10-13 Description"
EV_D = DCSV_REL

# (row suffix, target, stratum, kind, explicitness, confidence, statement, EvidenceFile, SourceRef, quote, locus, edge)
EDGES = {
    "DEL-08-06": [
        ("003", "DEL-08-01", "DERIVED", "CONSUMES", "EXPLICIT", "MEDIUM",
         "Tool-call queries run under the read-only agent access class of the socket server",
         PRD_REL, SR_API007, "under the `agent` access class", API007, "E-P84"),
        ("004", "DEL-08-02", "DERIVED", "CONSUMES", "EXPLICIT", "MEDIUM",
         "Tool calls query over the versioned API schema (PEC-API-003)",
         PRD_REL, SR_API007, Q_API_RESP, API007, "E-P85"),
        ("005", "DEL-08-03", "DERIVED", "CONSUMES", "EXPLICIT", "MEDIUM",
         "Tool calls return the compact citation-bearing, budget-bounded responses (PEC-API-004, PEC-API-006)",
         PRD_REL, SR_API007, Q_API_RESP, API007, "E-P86"),
        ("006", "DEL-04-01", "PROPOSAL", "CONSUMES", "IMPLICIT", "MEDIUM",
         "Tool-call queries serve orientation reads",
         PRD_REL, SR_AGENT, "class is read-only query access for tool calls: orientation", AGENT_CLASS, "E-P87"),
    ],
    "DEL-10-13": [
        ("003", "DEL-03-04", "DERIVED", "TESTS", "EXPLICIT", "MEDIUM",
         "The reliance-advertisement gate composes the harness parity result",
         EV_D, SR_D1013, "composes DEL-03-04 parity", D1013, "E-P88"),
        ("004", "DEL-04-03", "DERIVED", "TESTS", "EXPLICIT", "MEDIUM",
         "The reliance-advertisement gate composes the reliance envelope",
         EV_D, SR_D1013, "the DEL-04-03 reliance envelope", D1013, "E-P89"),
        ("005", "DEL-04-05", "DERIVED", "TESTS", "EXPLICIT", "MEDIUM",
         "The reliance-advertisement gate composes coverage honesty under seeded feed failures",
         EV_D, SR_D1013, "DEL-04-05 coverage honesty under seeded feed failures", D1013, "E-P90"),
        ("006", "DEL-10-02", "DERIVED", "TESTS", "EXPLICIT", "MEDIUM",
         "The reliance-advertisement gate composes the kill test",
         EV_D, SR_D1013, "the DEL-10-02 kill test", D1013, "E-P91"),
    ] + [
        (f"{7 + i:03d}", t, "PROPOSAL", "TESTS", "IMPLICIT", "MEDIUM",
         f"The reliance-advertisement gate composes the {t} parser fixture suite",
         EV_D, SR_D1013, Q_PARSERS, D1013, f"E-P{92 + i}")
        for i, t in enumerate(["DEL-02-01", "DEL-02-02", "DEL-02-03", "DEL-02-04",
                               "DEL-02-05", "DEL-02-06", "DEL-02-08", "DEL-02-09"])
    ],
}

# B2: SOW-097 / SOW-098 anchors appended to existing registers.
EXTRA_ANCHORS = [("DEL-04-03", "DEP-04-03-005", "SOW-097", "A-24, A-30"),
                 ("DEL-08-03", "DEP-08-03-005", "SOW-098", "A-25, A-32")]

# B3: the two quotes of the revision-1.5 DEL-08-01 description.
OLD_0801 = ("Local-only Unix-socket binding with token-scoped access classes (owner, harness, admin); "
            "auth-reuse choice tracked by OI-006.")
REFRESH = {
    "DEL-09-06": "DEP-09-06-003",
    "DEL-10-03": "DEP-10-03-003",
}
REFRESH_NOTE = "Evidence refreshed under D-PEC-101 (SCA-006 A-31: DEL-08-01 description re-expressed); "

# Mirror sections: where each target's downstream bullet goes.
# "append": after the last line of the existing downstream section, before `\n\n<next>`.
# "insert": a new downstream section inserted before `<next>` (no downstream section yet).
DOWN_HEAD = "## Downstream (informational; consumers of this deliverable)"
MIRROR_MODE = {
    "DEL-08-01": ("append", "## Non-gating constraints and register-wide rules"),
    "DEL-08-02": ("append", "## Non-gating constraints and register-wide rules"),
    "DEL-08-03": ("append", "## Non-gating constraints and register-wide rules"),
    "DEL-04-01": ("append", "## Non-gating constraints and register-wide rules"),
    "DEL-03-04": ("append", "## Standing obligation (constraint C-08)"),
    "DEL-04-03": ("append", "## Non-gating constraints and register-wide rules"),
    "DEL-04-05": ("insert", "## Non-gating constraints and register-wide rules"),
    "DEL-10-02": ("insert", "## Standing obligation (constraint C-08)"),
    "DEL-02-01": ("append", "## Non-gating constraints and register-wide rules"),
    "DEL-02-02": ("append", "## Non-gating constraints and register-wide rules"),
    "DEL-02-03": ("append", "## Non-gating constraints and register-wide rules"),
    "DEL-02-04": ("append", "## Non-gating constraints and register-wide rules"),
    "DEL-02-05": ("append", "## Non-gating constraints and register-wide rules"),
    "DEL-02-06": ("append", "## Non-gating constraints and register-wide rules"),
    "DEL-02-08": ("append", "## Non-gating constraints and register-wide rules"),
    "DEL-02-09": ("append", "## Non-gating constraints and register-wide rules"),
}


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


def split_register(raw: bytes, where: str) -> tuple[str, list[str]]:
    text = raw.decode("utf-8")
    if not text.endswith("\r\n"):
        raise Fail(f"{where}: register does not end with CRLF")
    lines = text.split("\r\n")[:-1]
    if lines[0] != ",".join(V31):
        raise Fail(f"{where}: header is not the v3.1 header")
    return text, lines


def parse_row(line: str, where: str) -> dict[str, str]:
    vals = next(csv.reader([line]))
    if len(vals) != len(V31) or csv_line(vals) != line + "\r\n":
        raise Fail(f"{where}: row does not round-trip: {line[:60]!r}")
    return dict(zip(V31, vals))


def locus_text(locus, prd_text: str, dels: dict) -> str:
    kind, key, col = locus
    if kind == "P":
        rows = [ln for ln in prd_text.splitlines() if ln.startswith(f"| {key} |")]
        if len(rows) != 1:
            raise Fail(f"PRD requirement row {key} found {len(rows)} times")
        return rows[0]
    if kind == "S":
        rows = [ln for ln in prd_text.splitlines() if ln.startswith(key)]
        if len(rows) != 1:
            raise Fail(f"PRD line {key[:40]!r} found {len(rows)} times")
        return rows[0]
    if kind == "D":
        return dels[key][col]
    raise Fail(f"unknown locus kind {kind}")


# ---------------------------------------------------------------- new files

def context_md(d: dict, act: str) -> str:
    n = NEW[d["DeliverableID"]]
    return f"""# _CONTEXT — {d['DeliverableID']}

| Field | Value |
|---|---|
| DeliverableID | {d['DeliverableID']} |
| Canonical name | {d['Name']} |
| PackageID | {d['PackageID']} ({n['pkg_name']}) |
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

Scaffolded under `D-PEC-101` ({act}) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.6 (`current_basis`,
SCA-006 successor; deliverable added by {n['action']}). Fields templated
deterministically from `Deliverables.csv`; this file restates register truth
and is not an independent authority.
"""


def references_md(d: dict, act: str) -> str:
    n = NEW[d["DeliverableID"]]
    return f"""# _REFERENCES — {d['DeliverableID']}

- `execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.6, accepted `current_basis`; SCA-006 successor)
- `execution/_Decomposition/Deliverables.csv` (authoritative deliverable register)
- `execution/_Decomposition/ScopeLedger.csv` (SOW→PKG→DEL→OBJ ledger; covers {d['CoversScopeItems']})
- `docs/PRD.md` v2.4 (accepted source corpus; see SourceRef column of the ledger)
- `{SCA6}` (accepted scope change that added this deliverable, {n['action']})
- `{n['pkg_folder']}/0_References/` (package reference staging)
- `execution/_Coordination/_COORDINATION.md` (coordination representation: FULL_GRAPH, threshold INITIALIZED)

Populated deterministically under `D-PEC-101` ({act}); extend during production.
"""


def dependencies_md(d: dict, act: str, dels: dict) -> str:
    """The docs/SPEC.md §5.2 (D-GOV-46) skeleton, as the preparation skill writes it for a new file,
    with the extracted section filled by this packet-ruled seed."""
    del_id = d["DeliverableID"]
    n = NEW[del_id]
    edges = EDGES[del_id]
    pp, ll = del_id.split("-")[1:]
    lines = [
        f"# Dependencies: {del_id} {d['Name']}", "",
        "## Dependency Tracking Mode",
        "- **Mode:** FULL_GRAPH",
        "- **Register:** the declared sections of this file together with Dependencies.csv (schema v3.1) when present (docs/SPEC.md §5.3)",
        "- **Notes:** `execution/_Coordination/_COORDINATION.md` (coordination representation FULL_GRAPH; "
        "RequiredMaturity threshold `INITIALIZED`, owner-ruled Phase 1.3). Register storage is deliverable-local "
        "by owner ruling (no central register). Blocker output is advisory visibility only — never work assignment.",
        "", "---", "",
        "## Declared Upstream (I need these before I can proceed)",
        "- None declared at setup. The upstream edges in the Extracted Dependency Register below are "
        "extracted-stratum rows seeded under `D-PEC-101`; none is a human declaration.",
        "",
        "## Declared Downstream (These need me)",
        "- None declared at setup.",
        "", "---", "",
        "## Extracted Dependency Register",
        f"- **Status:** SEEDED {act} under `D-PEC-101` from accepted decomposition revision 1.6 "
        f"(SCA-006, {n['action']}) and PRD v2.4, outside the `dependency-extract` lifecycle by packet ruling "
        "(the D-PEC-62 §3.2 and D-PEC-93 precedent). A later `dependency-extract` run refreshes this section.",
        f"- **Rows:** `Dependencies.csv` — 2 ANCHOR (`DEP-{pp}-{ll}-001` → {d['PackageID']}, "
        f"`DEP-{pp}-{ll}-002` → {n['sow']}) and {len(edges)} EXECUTION (`DEP-{pp}-{ll}-003`..`-{edges[-1][0]}`).",
        "",
        "| Predecessor | Stratum | Kind | Flag | EdgeID |",
        "|---|---|---|---|---|",
    ]
    lines += [f"| {e[1]} ({dels[e[1]]['Name']}) | {e[2]} | {e[3]} |  | {e[11]} |" for e in edges]
    lines += ["", "No deliverable depends on this one at setup.", "", "---", "",
              "## Lifecycle Summary", "- (placeholder)", "", "---", "",
              "## Run Notes",
              "- Register-wide rules carried from the D-PEC-62 exhibit (non-gating):",
              "  " + C04, "  " + C10]
    if del_id == "DEL-10-13":
        lines += ["- The accepted register row says the gate is \"re-proved at each such release\" and consumes no "
                  "internals \"(as DEL-10-02)\". Whether DEL-10-13 is a C-08 standing node, like DEL-10-02 and "
                  "DEL-03-04, is an owner classification that `D-PEC-101` does not make."]
    lines += ["", "## Run History",
              f"- {act} — seeded under `D-PEC-101` (WORKING_ITEMS with `project-setup`; `preparation` skill scaffold; "
              "rows and this file written by the bound generator `gen_d101_k1.py`).", ""]
    return "\n".join(lines)


def anchor_row(del_id: str, dep_id: str, d: dict, anchor: str, target: str, act: str, note: str) -> dict:
    base = dict(RegisterSchemaVersion="v3.1", DependencyID=dep_id, FromPackageID=d["PackageID"],
                FromDeliverableID=del_id, FromDeliverableName=d["Name"], DependencyClass="ANCHOR",
                Direction="UPSTREAM", DependencyType="OTHER", Explicitness="EXPLICIT",
                RequiredMaturity="NOT_APPLICABLE", ProposedMaturity="TBD", SatisfactionStatus="SATISFIED",
                Confidence="HIGH", Origin="DECLARED", FirstSeen=act, LastSeen=act, Status="ACTIVE", Notes=note)
    if anchor == "IMPLEMENTS_NODE":
        pkg = d["PackageID"]
        return dict(base, AnchorType="IMPLEMENTS_NODE", TargetType="PACKAGE", TargetPackageID=pkg,
                    TargetDeliverableID="", TargetRefID=pkg, TargetName=NEW[del_id]["pkg_folder"],
                    TargetLocation="execution/_Decomposition/SOFTWARE_DECOMP.md",
                    Statement=f"{del_id} is package-local to {pkg}.", EvidenceFile=DCSV_REL,
                    SourceRef=f"Deliverables.csv row {del_id}", EvidenceQuote=f"PackageID {pkg}")
    return dict(base, AnchorType="TRACES_TO_REQUIREMENT", TargetType="REQUIREMENT", TargetPackageID="",
                TargetDeliverableID="", TargetRefID=target, TargetName=target,
                TargetLocation="execution/_Decomposition/ScopeLedger.csv",
                Statement=f"{del_id} covers scope item {target}.", EvidenceFile=LCSV_REL,
                SourceRef=f"ScopeLedger.csv row {target}", EvidenceQuote=f"DeliverableIDs include {del_id}")


def exec_row(frm_id: str, e: tuple, dels: dict, dirs: dict, act: str) -> dict:
    suffix, tgt, stratum, _kind, expl, conf, stmt, evf, sref, quote, _locus, edge = e
    frm, t = dels[frm_id], dels[tgt]
    pp, ll = frm_id.split("-")[1:]
    return dict(RegisterSchemaVersion="v3.1", DependencyID=f"DEP-{pp}-{ll}-{suffix}",
                FromPackageID=frm["PackageID"], FromDeliverableID=frm_id, FromDeliverableName=frm["Name"],
                DependencyClass="EXECUTION", AnchorType="NOT_APPLICABLE", Direction="UPSTREAM",
                DependencyType="PREREQUISITE", TargetType="DELIVERABLE", TargetPackageID=t["PackageID"],
                TargetDeliverableID=tgt, TargetRefID=tgt, TargetName=t["Name"],
                TargetLocation=dirs[tgt][len(PEC) + 1:], Statement=stmt, EvidenceFile=evf, SourceRef=sref,
                EvidenceQuote=quote, Explicitness=expl, RequiredMaturity="INITIALIZED", ProposedMaturity="TBD",
                SatisfactionStatus="PENDING", Confidence=conf, Origin="EXTRACTED", FirstSeen=act, LastSeen=act,
                Status="ACTIVE", Notes=f"{stratum}; Flag=none; EdgeID={edge}; seeded under D-PEC-101 (SCA-006 B2)")


def mirror_edit(text: str, del_id: str, bullet: str, where: str) -> str:
    mode, nxt = MIRROR_MODE[del_id]
    if mode == "insert":
        if DOWN_HEAD in text:
            raise Fail(f"{where}: downstream section exists but insert mode pinned")
        return replace_once(text, f"\n\n{nxt}\n", f"\n\n{DOWN_HEAD}\n\n{bullet}\n\n{nxt}\n", where)
    start = text.find(f"\n{DOWN_HEAD}\n\n")
    if start < 0 or text.count(f"\n{DOWN_HEAD}\n\n") != 1:
        raise Fail(f"{where}: downstream section not found exactly once")
    end = text.find(f"\n\n{nxt}\n", start)
    if end < 0 or text.find("\n## ", start + 1) != end + 1:
        raise Fail(f"{where}: downstream section is not followed directly by {nxt!r}")
    anchor = text[text.rfind("\n", start, end) + 1:end] + f"\n\n{nxt}\n"
    if not anchor.startswith(("- ", "  ")):
        raise Fail(f"{where}: last downstream line is not a bullet or continuation: {anchor[:60]!r}")
    return replace_once(text, anchor, anchor.replace(f"\n\n{nxt}\n", f"\n{bullet}\n\n{nxt}\n", 1), where)


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    ap.add_argument("--act-date", required=True)
    ap.add_argument("--actor", default="TASK+preparation")
    ap.add_argument("--check-only", action="store_true")
    ap.add_argument("--reproduction", action="store_true")
    a = ap.parse_args()
    repo, act = a.repo.resolve(), a.act_date
    report: list[tuple[str, str, str, str]] = []
    try:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", act):
            raise Fail("act-date must be YYYY-MM-DD")
        today = time.strftime("%Y-%m-%d")
        if today != act and not a.reproduction:
            raise Fail(f"local date {today} != --act-date {act}; nothing written")
        # 0. preimages
        for rel, want in PREIMAGES.items():
            p = repo / rel
            if not p.is_file():
                raise Fail(f"missing preimage {rel}")
            got = sha(p.read_bytes())
            if got != want:
                raise Fail(f"preimage mismatch {rel}: {got} != {want}")
            report.append(("READ", rel, got, ""))
        with open(repo / EX / "_Decomposition/Deliverables.csv", newline="", encoding="utf-8") as f:
            dels = {r["DeliverableID"]: r for r in csv.DictReader(f)}
        with open(repo / EX / "_Decomposition/ScopeLedger.csv", newline="", encoding="utf-8") as f:
            ledger = {r["ScopeItemID"]: r for r in csv.DictReader(f)}
        prd_text = (repo / PEC / PRD_REL).read_text(encoding="utf-8")
        dirs = dict(DIRS)
        # 1. new folders
        folders: dict[str, Path] = {}
        for del_id, n in NEW.items():
            d = dels[del_id]
            if d["CoversScopeItems"] != n["sow"] or ledger[n["sow"]]["DeliverableIDs"] != del_id:
                raise Fail(f"{del_id}: register coverage differs from {n['sow']}")
            if list((repo / n["work"]).glob(f"{del_id}_*")):
                raise Fail(f"target folder exists for {del_id}")
            folders[del_id] = repo / n["work"] / f"{del_id}_{sanitize(d['Name'])}"
            dirs[del_id] = str(folders[del_id].relative_to(repo))
        for del_id, n in NEW.items():
            sib = [p for p in (repo / n["work"]).glob("DEL-*/_CONTEXT.md")]
            want = f"| PackageID | {dels[del_id]['PackageID']} ({n['pkg_name']}) |\n"
            if not sib or any(want not in p.read_text(encoding="utf-8") for p in sib):
                raise Fail(f"{del_id}: package name {n['pkg_name']!r} differs from sibling contexts")
        # 2. id collisions
        used_ids, used_edges = set(), set()
        for p in (repo / EX).glob("PKG-*/1_Working/DEL-*/Dependencies.csv"):
            for r in csv.DictReader(io.StringIO(p.read_text(encoding="utf-8"), newline="")):
                used_ids.add(r["DependencyID"])
                m = re.search(r"EdgeID=(E-[A-Z]\d+)", r["Notes"])
                if m:
                    used_edges.add(m.group(1))
        for p in (repo / EX).glob("PKG-*/1_Working/DEL-*/_DEPENDENCIES.md"):
            used_edges.update(re.findall(r"\bE-[A-Z]\d+\b", p.read_text(encoding="utf-8")))
        new_ids = [dep for _, dep, _, _ in EXTRA_ANCHORS]
        new_edges = []
        for frm_id, edges in EDGES.items():
            pp, ll = frm_id.split("-")[1:]
            new_ids += [f"DEP-{pp}-{ll}-00{i}" for i in (1, 2)] + [f"DEP-{pp}-{ll}-{e[0]}" for e in edges]
            new_edges += [e[11] for e in edges]
        if used_ids & set(new_ids) or used_edges & set(new_edges) or len(set(new_edges)) != len(new_edges):
            raise Fail(f"id collision: {sorted(used_ids & set(new_ids))} {sorted(used_edges & set(new_edges))}")
        # 3. quotes verbatim in their loci (and so in their files)
        for frm_id, edges in EDGES.items():
            for e in edges:
                if e[1] not in dels or dels[e[1]]["PackageID"] == "":
                    raise Fail(f"unknown target {e[1]}")
                loc = locus_text(e[10], prd_text, dels)
                if e[9] not in loc:
                    raise Fail(f"{frm_id}->{e[1]}: quote not verbatim in its locus {e[10][:2]}")
        new_0801 = dels["DEL-08-01"]["Description"]
        if new_0801 == OLD_0801:
            raise Fail("DEL-08-01 description unchanged; B3 not needed")
        # 4. render
        writes: list[tuple[Path, bytes]] = []
        for del_id, folder in folders.items():
            d = dels[del_id]
            pp, ll = del_id.split("-")[1:]
            rows = [anchor_row(del_id, f"DEP-{pp}-{ll}-001", d, "IMPLEMENTS_NODE", "", act,
                               "Tree anchor seeded under D-PEC-101"),
                    anchor_row(del_id, f"DEP-{pp}-{ll}-002", d, "TRACES_TO_REQUIREMENT", NEW[del_id]["sow"], act,
                               "Tree anchor seeded under D-PEC-101")]
            rows += [exec_row(del_id, e, dels, dirs, act) for e in EDGES[del_id]]
            ctx = context_md(d, act)
            for label, col in (("Canonical name", "Name"), ("Type", "Type"), ("ContextEnvelope", "ContextEnvelope"),
                               ("PhaseHint", "PhaseHint"), ("CoversScopeItems", "CoversScopeItems"),
                               ("SupportsObjectives", "SupportsObjectives")):
                if f"| {label} | {d[col]} |\n" not in ctx:
                    raise Fail(f"{del_id}: context field {label} not templated from the register")
            writes.append((folder / "_CONTEXT.md", ctx.encode("utf-8")))
            writes.append((folder / "_REFERENCES.md", references_md(d, act).encode("utf-8")))
            writes.append((folder / "_DEPENDENCIES.md", dependencies_md(d, act, dels).encode("utf-8")))
            writes.append((folder / "Dependencies.csv",
                           (csv_line(V31) + "".join(csv_line([r[k] for k in V31]) for r in rows)).encode("utf-8")))
        # 4b. appended anchors (B2) and refreshed quotes (B3)
        edits: dict[str, tuple[dict[str, dict], list[dict]]] = {}
        for del_id, dep_id, sow, acts in EXTRA_ANCHORS:
            if sow not in dels[del_id]["CoversScopeItems"].split(";") or ledger[sow]["DeliverableIDs"] != del_id:
                raise Fail(f"{del_id} does not cover {sow} in the registers")
            edits.setdefault(del_id, ({}, []))[1].append(
                anchor_row(del_id, dep_id, dels[del_id], "TRACES_TO_REQUIREMENT", sow, act,
                           f"Tree anchor seeded under D-PEC-101 (SCA-006 B2; {acts})"))
        for del_id, dep_id in REFRESH.items():
            edits.setdefault(del_id, ({}, []))[0][dep_id] = {
                "check": {"DependencyClass": "EXECUTION", "Status": "ACTIVE", "TargetDeliverableID": "DEL-08-01",
                          "EvidenceFile": DCSV_REL, "SourceRef": "Deliverables.csv row DEL-08-01 Description column",
                          "EvidenceQuote": OLD_0801},
                "set": {"EvidenceQuote": new_0801, "LastSeen": act},
                "prefix": REFRESH_NOTE}
        for del_id, (changes, appends) in sorted(edits.items()):
            p = repo / DIRS[del_id] / "Dependencies.csv"
            where = str(p.relative_to(repo))
            text, lines = split_register(p.read_bytes(), where)
            out, seen, last_n = [lines[0] + "\r\n"], set(), 0
            for line in lines[1:]:
                r = parse_row(line, where)
                last_n = max(last_n, int(r["DependencyID"].rsplit("-", 1)[1]))
                spec = changes.get(r["DependencyID"])
                if spec:
                    for k, v in spec["check"].items():
                        if r[k] != v:
                            raise Fail(f"{where} {r['DependencyID']}: {k} is {r[k]!r}, expected {v!r}")
                    r.update(spec["set"])
                    r["Notes"] = spec["prefix"] + r["Notes"]
                    seen.add(r["DependencyID"])
                    out.append(csv_line([r[k] for k in V31]))
                else:
                    out.append(line + "\r\n")
            if seen != set(changes):
                raise Fail(f"{where}: rows not found {sorted(set(changes) - seen)}")
            for r in appends:
                if int(r["DependencyID"].rsplit("-", 1)[1]) != last_n + 1:
                    raise Fail(f"{where}: {r['DependencyID']} is not the next row number after {last_n}")
                last_n += 1
                out.append(csv_line([r[k] for k in V31]))
            writes.append((p, "".join(out).encode("utf-8")))
        # 4c. downstream mirrors
        mirror: dict[str, list[str]] = {}
        for frm_id, edges in EDGES.items():
            for e in edges:
                mirror.setdefault(e[1], []).append(f"- {frm_id} ({dels[frm_id]['Name']}) — {e[3]} [{e[11]}]")
        if set(mirror) != set(MIRROR_MODE):
            raise Fail(f"mirror set differs: {sorted(set(mirror) ^ set(MIRROR_MODE))}")
        for del_id, bullets in sorted(mirror.items()):
            if len(bullets) != 1:
                raise Fail(f"{del_id}: expected one new downstream bullet")
            p = repo / DIRS[del_id] / "_DEPENDENCIES.md"
            text = p.read_text(encoding="utf-8")
            writes.append((p, mirror_edit(text, del_id, bullets[0], str(p.relative_to(repo))).encode("utf-8")))
        # 5. corpus-wide quote currency on the rendered state
        staged = {str(p.relative_to(repo)): data for p, data in writes}
        n_active = n_ok = 0
        regs = sorted({str(p.relative_to(repo)) for p in (repo / EX).glob("PKG-*/1_Working/DEL-*/Dependencies.csv")}
                      | {k for k in staged if k.endswith("/Dependencies.csv")})
        for rel in regs:
            data = staged.get(rel) or (repo / rel).read_bytes()
            for r in csv.DictReader(io.StringIO(data.decode("utf-8"), newline="")):
                if (r["DependencyClass"], r["Status"]) != ("EXECUTION", "ACTIVE"):
                    continue
                n_active += 1
                ev = repo / PEC / r["EvidenceFile"]
                if ev.is_file() and r["EvidenceQuote"] in ev.read_text(encoding="utf-8"):
                    n_ok += 1
                else:
                    raise Fail(f"quote not verbatim after rendering: {r['DependencyID']} in {r['EvidenceFile']}")
        report.append(("CHECK", "active_execution_quotes_verbatim", str(n_ok), str(n_active)))
        # 6. write set equals the grant
        created = {f"{dirs[k]}/{n}" for k in NEW for n in
                   ("_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "_SEMANTIC.md", "Dependencies.csv")}
        write_set = set(staged) | created
        if write_set != set(GRANT_MODIFY) | created or set(GRANT_MODIFY) - set(staged):
            raise Fail(f"write set differs from grant: {sorted(write_set ^ (set(GRANT_MODIFY) | created))}")
        if a.check_only:
            for p, data in writes:
                report.append(("RENDER", str(p.relative_to(repo)), "", sha(data)))
            for kind, path, pre, post in report:
                print(f"{kind}\t{path}\t{pre}\t{post}")
            return 0
        # 7. create the folders with the repository tools, then write
        for del_id, folder in folders.items():
            d = dels[del_id]
            folder.mkdir()
            r = subprocess.run(["zsh", str(repo / "tools/scaffolding/write_status.sh"), str(folder), "OPEN", a.actor],
                               capture_output=True, text=True)
            if r.returncode != 0:
                raise Fail(f"write_status.sh {del_id}: {r.returncode} {r.stdout}{r.stderr}")
            r = subprocess.run(["zsh", str(repo / "tools/scaffolding/scaffold_deliverable.sh"),
                                str(repo / NEW[del_id]["work"]), del_id, sanitize(d["Name"])],
                               capture_output=True, text=True)
            if r.returncode != 0:
                raise Fail(f"scaffold_deliverable.sh {del_id}: {r.stdout}{r.stderr}")
            made = sorted(Path(x.split("CREATED_PATH: ", 1)[1]).name for x in r.stdout.splitlines()
                          if x.startswith("CREATED_PATH: "))
            if made != ["_CONTEXT.md", "_DEPENDENCIES.md", "_REFERENCES.md", "_SEMANTIC.md"]:
                raise Fail(f"unexpected created set {del_id}: {made}")
            st = folder / "_STATUS.md"
            status = st.read_text(encoding="utf-8")
            if a.reproduction and today != act:
                status = status.replace(today, act)
                st.write_text(status, encoding="utf-8")
            want = (f"# Status: {del_id}\n\n**Current State:** OPEN\n**Last Updated:** {act}\n\n"
                    f"## History\n- {act} — State set to OPEN ({a.actor})\n")
            if status != want:
                raise Fail(f"write_status.sh output differs from the expected OPEN form for {del_id}")
            for stub in ("_CONTEXT.md", "_DEPENDENCIES.md", "_REFERENCES.md", "_SEMANTIC.md"):
                if (folder / stub).stat().st_size != 0:
                    raise Fail(f"stub not empty {del_id}/{stub}")
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
            report.append(("CHECK", f"check_min_viable_fileset {del_id}", str(r.returncode), r.stdout.strip().replace("\n", " | ")))
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
