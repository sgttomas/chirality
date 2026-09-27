#!/usr/bin/env python3
"""Apply the owner's 2026-09-27 ruling on HGD-1, HGD-3 and FC-1 to FC-3 to the DEL-02-01 register (dependency-extract UPDATE).

Run from the repository root. `SCOPE=DEL-02-01`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, apply mode, in the form of
`AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/apply_esr1_ruling.py`:

- Function 3 (`Dependencies.csv`): DEP-02-01-006 and DEP-02-01-012 take the field values of `RECOMMENDATION.md`; the
  ruling is quoted verbatim in `Notes` with the prior values; IDs are kept; no row is added, retired or deleted; every
  other row is byte-identical. HGD-3, FC-2 and FC-3 are closed without a row.
- Function 4 (`_DEPENDENCIES.md`): the agent-owned sections are refreshed under the headings the file already uses
  (register summary and Compact Register, Lifecycle Summary, Run Notes, Run History, Downstream Handoff Notes). The
  human-owned sections (Dependency Tracking, Declared Upstream, Declared Downstream) are not edited.

Both pre-images are hash-checked, so the script refuses to run twice. Writes EXTRACTION_LOG.json next to this script.
"""
from __future__ import annotations

import collections
import csv
import glob
import hashlib
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
EX = "projects/chirality-app-dev/execution"
RUN_ID = "APP-HGD-1-3-RECOMMENDATION-2026-09-27"
TODAY = "2026-09-27"
FOLDER = glob.glob(f"{EX}/PKG-02_*/1_Working/DEL-02-01_*")[0]
CSV_P, MD_P = FOLDER + "/Dependencies.csv", FOLDER + "/_DEPENDENCIES.md"
PRE = {"Dependencies.csv": "3baf26609735bd519d7c0aaf4dd86a6a214e6701ef678fd8acbc0e4ad4d8411d",
       "_DEPENDENCIES.md": "d2ffed6866a654ea9dd32ffb28b3270dbb629d7c1368e4caf20adcff882c55fd"}
RULING = ("HGD-1: invert DEP-02-01-006 to UPSTREAM INTERFACE; HGD-3: close without emitting; FC-1: resolve "
          "DEP-02-01-012 to DEL-05-03; FC-2 and FC-3: close without emitting.")
TRANSCRIPT = f"execution/_Coordination/AgentRuns/{RUN_ID}/CHAT_TRANSCRIPTION_HGD_2026-09-27.md"
OWNER = f"Owner ruling in chat, {TODAY} (verbatim, transcription {TRANSCRIPT}): \"{RULING}\""
DECOMP = "execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
DECOMP_REL = "projects/chirality-app-dev/" + DECOMP
SOURCES = ("ScopeOfWork.md", "_CONTEXT.md", "_REFERENCES.md", "_STATUS.md")

CHANGES = {
    "DEP-02-01-006": {
        "set": {"Direction": "UPSTREAM", "DependencyType": "INTERFACE", "LastSeen": TODAY},
        "expect": {"Direction": "DOWNSTREAM", "DependencyType": "HANDOVER", "TargetDeliverableID": "DEL-08-02", "Status": "ACTIVE"},
        "note": (f" {TODAY} UPDATE: INVERTED by owner ruling HGD-1. {OWNER} HGD-1 CLOSED. Prior Direction=DOWNSTREAM, "
                 "DependencyType=HANDOVER. Basis: row Statement; ScopeOfWork.md CLM-015, CLM-027, DEL-02-01-REQ-007; "
                 "decomposition L413 (SOW-005 reverse view: DEL-02-01 presents; DEL-08-02 owns aliases, routing, selection guards, "
                 "and legacy compatibility); DEL-08-02 ScopeOfWork.md L139. Graph: " + RUN_ID + " scenario S1 (0 SCC). The earlier "
                 "clauses of these Notes about this row's direction and SCC-001 reachability are superseded."),
    },
    "DEP-02-01-012": {
        "set": {"TargetType": "DELIVERABLE", "TargetPackageID": "PKG-05", "TargetDeliverableID": "DEL-05-03",
                "TargetRefID": "DEL-05-03", "TargetName": "Redacted RunLogger and Secret Hygiene", "TargetLocation": DECOMP,
                "Explicitness": "IMPLICIT", "Confidence": "MEDIUM", "LastSeen": TODAY},
        "expect": {"TargetType": "UNKNOWN", "TargetPackageID": "", "TargetDeliverableID": "", "TargetRefID": "TBD",
                   "TargetLocation": "TBD", "Explicitness": "EXPLICIT", "Confidence": "MEDIUM", "Status": "ACTIVE"},
        "note": (f" {TODAY} UPDATE: TARGET RESOLVED to DEL-05-03 by owner ruling FC-1. {OWNER} FC-1 CLOSED. Prior TargetType=UNKNOWN, "
                 "TargetPackageID=(empty), TargetDeliverableID=(empty), TargetRefID=TBD, TargetName=Existing redaction helper under "
                 "frontend/src/lib/harness/** (derived chat titles, Q6), TargetLocation=TBD, Explicitness=EXPLICIT; Confidence "
                 "unchanged (MEDIUM). Basis: decomposition L343 (DEL-05-03 artifacts: App redaction helper) and SOW-041 L449; DEL-05-03 "
                 "ScopeOfWork.md L204 (a redaction helper among its implementation artifacts) and L77 (shared redaction helper identity "
                 "TBD in DEL-05-03). Explicitness IMPLICIT because the target comes from the decomposition's allocation, not from a "
                 "DEL-02-01 line naming DEL-05-03 (the ESR-1 ledger-based precedent). Fence F1 no longer applies: SCC-001 was resolved "
                 "by D-APP-110 SD-001; graph " + RUN_ID + " scenarios FC1 and S1+FC1 (0 SCC). The earlier PROPOSAL and F1 clauses are "
                 "superseded."),
    },
}


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise SystemExit(f"_DEPENDENCIES.md: expected one match for {old[:90]!r}, found {text.count(old)}")
    return text.replace(old, new)


def section(lines, heading):
    for i, l in enumerate(lines):
        if l.strip() == heading:
            j = i + 1
            while j < len(lines) and not lines[j].startswith("## "):
                j += 1
            return i, j
    raise SystemExit(f"heading not found: {heading}")


def counts_block(rows):
    act = [r for r in rows if r["Status"] == "ACTIVE"]
    lines = [f"Current as of {TODAY} (`{RUN_ID}`). Dated sections elsewhere in this file keep the counts of their dates.", "",
             "| Count Type | Count |", "|---|---:|",
             f"| Total rows | {len(rows)} |", f"| ACTIVE rows | {len(act)} |", f"| RETIRED rows | {len(rows) - len(act)} |",
             f"| ACTIVE ANCHOR rows | {sum(1 for r in act if r['DependencyClass'] == 'ANCHOR')} |",
             f"| ACTIVE EXECUTION rows | {sum(1 for r in act if r['DependencyClass'] == 'EXECUTION')} |",
             f"| ACTIVE parent anchors (`IMPLEMENTS_NODE`) | {sum(1 for r in act if r['AnchorType'] == 'IMPLEMENTS_NODE')} |",
             f"| ACTIVE Origin=DECLARED rows | {sum(1 for r in act if r['Origin'] == 'DECLARED')} |", "",
             "### Compact Register", "",
             "| DependencyID | Class | Direction | Type | Target | Status | SatisfactionStatus |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        tgt = r["TargetDeliverableID"] or r["TargetRefID"] or (r["TargetName"][:60] + ("…" if len(r["TargetName"]) > 60 else ""))
        lines.append(f"| {r['DependencyID']} | {r['DependencyClass']} | {r['Direction']} | {r['DependencyType']} | "
                     f"{tgt.replace('|', '/')} | {r['Status']} | {r['SatisfactionStatus']} |")
    return lines


def lifecycle_block(rows):
    lines = [f"Current as of {TODAY} (`{RUN_ID}`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). "
             "This projection changes no satisfaction or maturity.", "", "| Dimension | Value | Count |", "|---|---|---:|"]
    for dim in ("Status", "SatisfactionStatus", "RequiredMaturity", "DependencyClass", "DependencyType"):
        for v, n in sorted(collections.Counter(r[dim] for r in rows).items()):
            lines.append(f"| {dim} | {v or '(blank)'} | {n} |")
    return lines


def main():
    for name, path in (("Dependencies.csv", CSV_P), ("_DEPENDENCIES.md", MD_P)):
        if sha(path) != PRE[name]:
            raise SystemExit(f"{name}: pre-image mismatch (already applied?)")
    src_hashes = {n: sha(f"{FOLDER}/{n}") for n in SOURCES}

    # Function 3
    with open(CSV_P, encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        fields, rows = reader.fieldnames, list(reader)
    diffs = {}
    for did, change in CHANGES.items():
        hits = [r for r in rows if r["DependencyID"] == did]
        if len(hits) != 1:
            raise SystemExit(f"{did}: expected one row")
        r = hits[0]
        for k, v in change["expect"].items():
            if r[k] != v:
                raise SystemExit(f"{did}: {k}={r[k]!r}, expected {v!r}")
        before = dict(r)
        r.update(change["set"])
        r["Notes"] = r["Notes"] + change["note"]
        diffs[did] = {k: [before[k], r[k]] for k in fields if before[k] != r[k] and k != "Notes"}
        diffs[did]["Notes"] = ["(prior text)", "(prior text)" + change["note"]]
    out = io.StringIO()
    w = csv.DictWriter(out, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    open(CSV_P, "w", encoding="utf-8", newline="").write(out.getvalue())

    # Function 4
    text = open(MD_P, encoding="utf-8").read()
    L = text.split("\n")
    b = section(L, "## Current Extracted Dependency Summary — 2026-09-22")
    L[b[0] + 1:b[1]] = [""] + counts_block(rows) + [""]
    b = section(L, "## Lifecycle Summary")
    L[b[0] + 1:b[1]] = [""] + lifecycle_block(rows) + [""]
    act = [r for r in rows if r["Status"] == "ACTIVE"]
    n_anchor = sum(1 for r in act if r["DependencyClass"] == "ANCHOR")
    n_exec = sum(1 for r in act if r["DependencyClass"] == "EXECUTION")
    parents = sum(1 for r in act if r["AnchorType"] == "IMPLEMENTS_NODE")
    b = section(L, "## Run History")
    last = max(i for i in range(b[0], b[1]) if L[i].startswith("|"))
    L.insert(last + 1, f"| {TODAY} (`{RUN_ID}`) | UPDATE | CONSERVATIVE | `{DECOMP_REL}` | FOUND (unchanged) | none | "
                       f"ACTIVE={len(act)} (ANCHOR={n_anchor}; EXECUTION={n_exec}) |")
    notes = [
        f"### {TODAY} owner ruling on HGD-1, HGD-3 and FC-1 to FC-3 applied (UPDATE)", "",
        f"- Run: `{RUN_ID}`, `bundled:chirality-root/dependency-extract` in apply mode, run directly by a TASK-type executor for the "
        f"coordinating session after the owner's ruling. {OWNER}",
        f"- Runtime overrides: `SCOPE=DEL-02-01`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH={DECOMP_REL}`; "
        "`MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `ApplyEdits=true`. No extraction from prose: the run applies the ruled field "
        f"values of `execution/_Coordination/AgentRuns/{RUN_ID}/RECOMMENDATION.md`, in the form of the ESR-1 application.",
        f"- Pre-images: `Dependencies.csv` `{PRE['Dependencies.csv']}`, `_DEPENDENCIES.md` `{PRE['_DEPENDENCIES.md']}`.",
        "- Source-preservation gate: " + "; ".join(f"`{n}` `{h}`" for n, h in src_hashes.items()) + "; read-only and unchanged.",
        "- INVERTED DEP-02-01-006 (EXECUTION DOWNSTREAM HANDOVER -> DEL-08-02 becomes EXECUTION UPSTREAM INTERFACE on DEL-08-02). "
        "HGD-1 CLOSED; see the row `Notes`.",
        "- TARGET RESOLVED DEP-02-01-012 (EXECUTION UPSTREAM INTERFACE, UNKNOWN TBD -> DELIVERABLE DEL-05-03; Explicitness EXPLICIT -> "
        "IMPLICIT; Confidence MEDIUM unchanged). FC-1 CLOSED; see the row `Notes`.",
        "- CLOSED WITHOUT A ROW: HGD-3 (the DEL-02-01-V3-01 prerequisite on DEL-02-02-V3-03), FC-2 (DEL-03-02) and FC-3 (DEL-02-05). "
        "No row added, retired or deleted; every other row byte-identical; `Status=CANDIDATE` not emitted.",
        "- Graph: " + RUN_ID + " scenario S1+FC1 predicts 104 edges and 0 SCC; the post-apply closure snapshot records the observed "
        "result (see the run receipt).",
        f"- Parent anchor check: {'PASS; exactly one' if parents == 1 else 'FAIL;'} ACTIVE `IMPLEMENTS_NODE` row ({parents}).",
        f"- Function 5 checks (`execution/_Coordination/AgentRuns/{RUN_ID}/dep_extract/FUNCTION5_CHECKS.json`): schema, `DependencyID` "
        "uniqueness, the enum values of the two changed rows, ID format and index counts.",
        "",
    ]
    b = section(L, "## Run History")
    L[b[0]:b[0]] = notes
    text = "\n".join(L)

    closed = (f"  - {TODAY} (`{RUN_ID}`): HGD-1 CLOSED: DEP-02-01-006 inverted to UPSTREAM INTERFACE on DEL-08-02. HGD-3 CLOSED without "
              f"emitting a row. {OWNER}")
    text = replace_once(text, "HGD-3 stays open for its owner. (Its seated items now live in the 2026-09-23 receiving clauses.)\n",
                        "HGD-3 stays open for its owner. (Its seated items now live in the 2026-09-23 receiving clauses.)\n" + closed + "\n")
    text = replace_once(text, "into a thirteen-node SCC because every SCC-001 member already reaches DEL-02-01 through DEP-02-01-006 "
                        "(DEL-04-04 to DEL-08-02 to DEL-02-01).\n",
                        "into a thirteen-node SCC because every SCC-001 member already reaches DEL-02-01 through DEP-02-01-006 "
                        "(DEL-04-04 to DEL-08-02 to DEL-02-01).\n"
                        f"  - {TODAY} (`{RUN_ID}`): FC-1 resolved into DEP-02-01-012 (target DEL-05-03, IMPLICIT/MEDIUM); FC-2 and FC-3 "
                        f"closed without a row. SCC-001 no longer exists (resolved by D-APP-110 SD-001). {OWNER}\n")
    text = replace_once(text, "- [WARNING] TARGET_UNRESOLVED: DEP-02-01-012 keeps `TargetType=UNKNOWN` because the only explicit "
                        "resolution (DEL-05-03) is fenced by F1.\n",
                        "- [WARNING] TARGET_UNRESOLVED: DEP-02-01-012 keeps `TargetType=UNKNOWN` because the only explicit "
                        "resolution (DEL-05-03) is fenced by F1.\n"
                        f"  - RESOLVED {TODAY} (`{RUN_ID}`): DEP-02-01-012 now targets DEL-05-03 by the owner's FC-1 ruling.\n")
    text = replace_once(text, "any UPSTREAM row into SCC-001 or into a node that reaches it makes DEL-02-01 a member.\n",
                        "any UPSTREAM row into SCC-001 or into a node that reaches it makes DEL-02-01 a member.\n"
                        f"  - Superseded {TODAY} (`{RUN_ID}`): SCC-001 was resolved by D-APP-110, and DEP-02-01-006 is now UPSTREAM, so "
                        "no path runs from DEL-08-02 to DEL-02-01.\n")
    old181 = ("- Owner rulings still open (2026-09-27): HGD-1 (DEP-02-01-006 direction) and HGD-3 (DEL-02-02-V3-03 prerequisite, held "
              "non-gating, not emitted; its premise changed as recorded below). Fenced candidates FC-1 to FC-3 stay out of the register "
              "unless separately ruled.\n")
    text = replace_once(text, old181,
                        f"- HGD-1, HGD-3 and FC-1 to FC-3 CLOSED {TODAY} by the owner's ruling \"{RULING}\" (transcription `{TRANSCRIPT}`): "
                        "DEP-02-01-006 is UPSTREAM INTERFACE on DEL-08-02; DEP-02-01-012 targets DEL-05-03 (IMPLICIT/MEDIUM); no row was "
                        "emitted for HGD-3, FC-2 or FC-3. No owner graph ruling remains open for this register.\n")
    text = replace_once(text, "HGD-3's four-node SCC concern no longer arises from them; HGD-3 itself is not decided.",
                        f"HGD-3's four-node SCC concern no longer arises from them; HGD-3 was closed without emitting on {TODAY}.")
    text = replace_once(text, "and its acceptance as the loop's DepClosure pointer remains a separate owner act.\n\n## Current dependency refresh",
                        "and its acceptance as the loop's DepClosure pointer remains a separate owner act. After the "
                        f"{TODAY} HGD-1 inversion and FC-1 resolution DEL-02-01 remains outside any SCC; the post-apply closure snapshot "
                        "is named in the run receipt.\n\n## Current dependency refresh")
    open(MD_P, "w", encoding="utf-8").write(text)

    for n, h in src_hashes.items():
        if sha(f"{FOLDER}/{n}") != h:
            raise SystemExit(f"source {n} changed")
    log = {"run_id": RUN_ID, "date": TODAY, "ruling": RULING, "transcript": TRANSCRIPT, "scope": "DEL-02-01", "folder": FOLDER,
           "pre_sha256": PRE, "post_sha256": {"Dependencies.csv": sha(CSV_P), "_DEPENDENCIES.md": sha(MD_P)},
           "sources_sha256": src_hashes, "row_diffs": diffs,
           "closed_without_row": ["HGD-3", "FC-2", "FC-3"]}
    json.dump(log, open(os.path.join(HERE, "EXTRACTION_LOG.json"), "w", encoding="utf-8"), indent=1)
    print(json.dumps(diffs, indent=1))


if __name__ == "__main__":
    main()
