#!/usr/bin/env python3
"""Function 4 of dependency-extract: refresh the agent-owned sections of each in-scope _DEPENDENCIES.md.

Run from the repository root after apply_dependency_extract.py and apply_esr1_reevidence.py. Each file is rebuilt
from its pre-image at the extraction's basis commit (hash-checked against EXTRACTION_LOG.json), so a rerun is
idempotent. Human-owned sections (Dependency Tracking, Declared Upstream, Declared Downstream) are never edited.
Following dependency-extract Function 4, each agent-owned section is refreshed under the heading the file already
uses. For each file this:
- replaces the body of the file's register section: `## Extracted Dependency Register`, or the legacy
  `## Current Extracted Dependency Summary — <date>` heading the file already uses (added under the SPEC §5.2
  heading before `## Run Notes` only when the file has neither);
- replaces the body of `## Lifecycle Summary`;
- adds `### 2026-09-27 SCA-APP-011 incremental setup refresh (UPDATE)` as a subsection at the end of the file's
  existing `## Run Notes` section;
- appends one Run History entry in the file's own table columns or bullet order.
DEL-02-01 additionally records the owner's HGD-2 ruling at the dated HGD line and in its Downstream Handoff Notes.
"""
from __future__ import annotations

import collections
import csv
import glob
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = json.load(open(os.path.join(HERE, "EXTRACTION_LOG.json")))
TODAY = LOG["date"]
RUN_ID = LOG["run_id"]
DECOMP_REL = "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
DSHA = LOG["decomposition_sha256"]
OWNER_WORDS = ("Confirm baseline SCA-APP-010 (accepted up to 2026-09-07) and the SCA-APP-011 incremental plan under "
               "FULL_GRAPH; HGD-2: retire DEP-02-01-008; APP-R058: option 1.")
TRANSCRIPT = f"execution/_Coordination/AgentRuns/{RUN_ID}/CHAT_TRANSCRIPTION.md"
RUN_HEAD = f"### {TODAY} SCA-APP-011 incremental setup refresh (UPDATE)"
BASIS = "0ca5ffcca2c2044b2d5e79201de9741b80b31585"


def section_bounds(lines, heading):
    """Return (start, end) line indexes of the first section whose heading line equals `heading`."""
    for i, l in enumerate(lines):
        if l.strip() == heading:
            j = i + 1
            while j < len(lines) and not lines[j].startswith("## "):
                j += 1
            return i, j
    return None


def counts_block(rows):
    act = [r for r in rows if r["Status"] == "ACTIVE"]
    c = collections.Counter
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
        tgt = tgt.replace("|", "/")
        lines.append(f"| {r['DependencyID']} | {r['DependencyClass']} | {r['Direction']} | {r['DependencyType']} | {tgt} | "
                     f"{r['Status']} | {r['SatisfactionStatus']} |")
    return lines


def lifecycle_block(rows):
    lines = [f"Current as of {TODAY} (`{RUN_ID}`), from `Dependencies.csv`; counts cover all rows (ACTIVE and RETIRED). This projection changes no satisfaction or maturity.", "",
             "| Dimension | Value | Count |", "|---|---|---:|"]
    for dim in ("Status", "SatisfactionStatus", "RequiredMaturity", "DependencyClass", "DependencyType"):
        for v, n in sorted(collections.Counter(r[dim] for r in rows).items()):
            lines.append(f"| {dim} | {v or '(blank)'} | {n} |")
    return lines


def run_notes(d, info, rows):
    acts = info["actions"]
    by = collections.defaultdict(list)
    for did, a in acts.items():
        by[a.split()[0]].append(did)
    role = ("SCA-APP-011 MODIFY deliverable" if info["role"] == "MODIFY" else "FULL_GRAPH neighbour of the SCA-APP-011 MODIFY set")
    act = [r for r in rows if r["Status"] == "ACTIVE"]
    parents = sum(1 for r in act if r["AnchorType"] == "IMPLEMENTS_NODE")
    src = "; ".join(f"`{n}` `{h}`" for n, h in info["sources_sha256"].items())
    out = [RUN_HEAD, "",
           f"- Run: `{RUN_ID}`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, "
           f"run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-011 incremental plan on {TODAY} (verbatim in "
           f"`{TRANSCRIPT}`). Role: {role}.",
           f"- Runtime overrides: `SCOPE={d}`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH={DECOMP_REL}`; "
           "`MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, "
           "`_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.",
           f"- Decomposition authority: FOUND, SHA-256 `{DSHA}` (as amended by SCA-APP-011).",
           f"- Source-preservation gate: {src}; read-only and unchanged by this run.",
           "- Pre-images: `Dependencies.csv` `" + info["pre_sha256"]["Dependencies.csv"] + "`, `_DEPENDENCIES.md` `"
           + info["pre_sha256"]["_DEPENDENCIES.md"] + "`.",
           "- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only "
           "inside a `[RETIRED` clause or a clause SCA-APP-011 declared history). Text added to the sources since the previous "
           "extraction (2026-09-22) was scanned for new explicit cross-deliverable relationships. Unchanged source text yields the rows "
           "already recorded.",
           f"- Results: re-seen {len(by['RESEEN'])} (`LastSeen={TODAY}`); restated in place {len(by['RESTATE'])}; kept with a note "
           f"{len(by['KEEP'])}; retired {len(by['RETIRE'])}; added {len(by['ADDED'])}; held with `[WARNING] EVIDENCE_SOURCE_RETIRED` "
           f"{len(by['HOLD'])}. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted."]
    for kind in ("RETIRE", "RESTATE", "KEEP", "ADDED", "HOLD"):
        for did in by[kind]:
            r = next(x for x in rows if x["DependencyID"] == did)
            label = {"RETIRE": "RETIRED", "RESTATE": "RESTATED", "KEEP": "KEPT", "ADDED": "ADDED", "HOLD": "HELD"}[kind]
            if kind == "RESTATE" and "ESR-1" in acts[did]:
                label = "RE-EVIDENCED"
            ref = acts[did].split(" ", 1)[1] if " " in acts[did] else ""
            tgt = r["TargetDeliverableID"] or r["TargetRefID"] or r["TargetName"][:60]
            out.append(f"  - {label} {did} ({r['DependencyClass']} {r['Direction']} {r['DependencyType']} -> {tgt}) {ref}; see the row `Notes`.")
    out += ["- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; "
            "entries skipped 0.",
            f"- Parent anchor check: {'PASS; exactly one' if parents == 1 else ('[WARNING] FLOATING_NODE: no' if parents == 0 else '[WARNING] AMBIGUOUS_ANCHOR:')} "
            f"ACTIVE `IMPLEMENTS_NODE` row{'' if parents == 1 else 's'} ({parents}).",
            "- Function 5 checks (`execution/_Coordination/AgentRuns/" + RUN_ID + "/dep_extract/FUNCTION5_CHECKS.json`): "
            "`validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID "
            "(`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` "
            "(`validate_id_format.sh`; the PROJECT_ID_FORMAT_PROFILE warning of earlier runs no longer reproduces); index counts "
            "match `Dependencies.csv`.",
            "- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the validator resolves "
            "`EvidenceFile` from the project root, so it reports every App register row whose `EvidenceFile` is deliverable- or "
            "repository-relative. This is a project-wide pre-existing convention finding, not a defect introduced here; no EVQ-003, "
            "EVQ-004 or DRB-006 finding."]
    esr = [k for k, v in acts.items() if "ESR-1 (re-evidenced)" in v]
    if esr:
        out.append("- ESR-1 re-evidence: " + ", ".join(esr) + " cited the former `_STATUS.md` `## Remaining` section, retired on "
                   "2026-09-23. Each is re-anchored in place to a current accepted source that states the dependency: the owner "
                   "ruling record D-APP-110 (its SD-003 decompose names the row) or the decomposition Scope Ledger allocation "
                   "(IMPLICIT, MEDIUM). The D-APP-110 record lies outside the workflow's default read boundary and was read because it "
                   "is the accepted ruling that names these rows. No edge, target, status or satisfaction changed.")
    ruled = [k for k, v in acts.items() if "ESR-1 (owner ruling)" in v]
    if ruled:
        out.append("- ESR-1 CLOSED 2026-09-27: " + ", ".join(ruled) + (" was" if len(ruled) == 1 else " were")
                   + " held as retire candidates (no current source; preserved by the accepted 2026-09-23 instrument) and are now "
                   "RETIRED by the owner's ruling in chat on 2026-09-27 (verbatim, transcription `execution/_Coordination/AgentRuns/"
                   + RUN_ID + "/CHAT_TRANSCRIPTION_ESR-1_2026-09-27.md`): \"ESR-1: retire DEP-02-02-021, DEP-02-04-015, "
                   "DEP-02-04-016 and DEP-02-01-014.\"")
    if by["HOLD"]:
        out.append("- [WARNING] EVIDENCE_SOURCE_RETIRED: " + ", ".join(by["HOLD"]) + (" cites" if len(by["HOLD"]) == 1 else " cite")
                   + " the former `_STATUS.md` `## Remaining` section, retired by the owner-directed 2026-09-23 finite Task "
                   "Management account. That accepted instrument preserved the rows (FINAL_CLOSEOUT.md: 'the accepted "
                   "Dependencies.csv rows and source quotes remain unchanged'; the current-source note at the top of this file directs "
                   "gating to `Dependencies.csv`) and takes precedence over the workflow's own unseen-row retirement, so they stay "
                   "ACTIVE with `LastSeen` unchanged. No current source states them; they are retire candidates proposed to the owner "
                   "(ESR-1 in `execution/_Coordination/AgentRuns/" + RUN_ID + "/DEPENDENCY_EXTRACT_RESULTS.md`).")
    return out


def run_history_row(header_line, info, rows):
    cols = [c.strip() for c in header_line.strip().strip("|").split("|")]
    act = [r for r in rows if r["Status"] == "ACTIVE"]
    holds = [k for k, v in info["actions"].items() if v.startswith("HOLD")]
    warn = ("EVIDENCE_SOURCE_RETIRED " + ",".join(holds)) if holds else "none"
    vals = []
    for c in cols:
        lc = c.lower()
        if lc.startswith("timestamp"):
            vals.append(f"{TODAY} (`{RUN_ID}`)")
        elif lc == "mode":
            vals.append("UPDATE")
        elif lc.startswith("strictness"):
            vals.append("CONSERVATIVE")
        elif "decomposition path" in lc:
            vals.append(f"`{DECOMP_REL}`")
        elif "decomposition" in lc:
            vals.append(f"FOUND `{DSHA[:12]}…` (SCA-APP-011 amended)")
        elif "warning" in lc:
            vals.append(warn)
        elif "active" in lc:
            vals.append(f"ACTIVE={len(act)} (ANCHOR={sum(1 for r in act if r['DependencyClass'] == 'ANCHOR')}; "
                        f"EXECUTION={sum(1 for r in act if r['DependencyClass'] == 'EXECUTION')})")
        else:
            vals.append("—")
    return "| " + " | ".join(vals) + " |"


def main() -> int:
    for d, info in LOG["deliverables"].items():
        fold = info["folder"]
        mdp = fold + "/_DEPENDENCIES.md"
        rows = list(csv.DictReader(open(fold + "/Dependencies.csv", encoding="utf-8")))
        raw = subprocess.run(["git", "show", f"{BASIS}:{mdp}"], capture_output=True).stdout
        import hashlib
        if hashlib.sha256(raw).hexdigest() != info["pre_sha256"]["_DEPENDENCIES.md"]:
            raise SystemExit(f"{d}: pre-image at {BASIS} does not match EXTRACTION_LOG")
        text = raw.decode("utf-8")
        L = text.split("\n")
        # Lifecycle Summary body
        b = section_bounds(L, "## Lifecycle Summary")
        L[b[0] + 1:b[1]] = [""] + lifecycle_block(rows) + [""]
        # Run History: a new table row, or a new bullet in the file's own bullet order
        b = section_bounds(L, "## Run History")
        tbl = [i for i in range(b[0] + 1, b[1]) if L[i].startswith("|")]
        if tbl:
            L.insert(tbl[-1] + 1, run_history_row(L[tbl[0]], info, rows))
        else:
            bl = [i for i in range(b[0] + 1, b[1]) if L[i].startswith("- ")]
            dates = [re.match(r"- (\d{4}-\d{2}-\d{2})", L[i]).group(1) for i in bl if re.match(r"- (\d{4}-\d{2}-\d{2})", L[i])]
            act = [r for r in rows if r["Status"] == "ACTIVE"]
            holds = [k for k, v in info["actions"].items() if v.startswith("HOLD")]
            bullet = (f"- {TODAY} (`{RUN_ID}`): `dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`; "
                      f"decomposition found, SHA-256 `{DSHA[:12]}…` (SCA-APP-011 amended); warnings: "
                      + (f"EVIDENCE_SOURCE_RETIRED {','.join(holds)}" if holds else "none")
                      + f"; ACTIVE={len(act)} (ANCHOR={sum(1 for r in act if r['DependencyClass'] == 'ANCHOR')}, "
                      f"EXECUTION={sum(1 for r in act if r['DependencyClass'] == 'EXECUTION')}); RETIRED={len(rows) - len(act)}.")
            newest_first = len(dates) > 1 and dates[0] > dates[-1]
            L.insert(bl[0] if newest_first else bl[-1] + 1, bullet)
        # Run Notes: a dated subsection at the end of the existing `## Run Notes` section
        b = section_bounds(L, "## Run Notes")
        end = b[1]
        while end > b[0] + 1 and L[end - 1].strip() == "":
            end -= 1
        L[end:end] = [""] + run_notes(d, info, rows)
        # Register section under the heading the file already uses
        canon = any(l.strip() == "## Extracted Dependency Register" for l in L)
        legacy = next((l.strip() for l in L if l.startswith("## Current Extracted Dependency Summary")), None)
        if canon and legacy:
            # Two agent-owned register sections: refresh the canonical one; the dated legacy summary keeps its heading
            # and points to it, so the file carries one current register section (its dated table is in git history).
            b = section_bounds(L, legacy)
            L[b[0] + 1:b[1]] = ["", f"Superseded on {TODAY} (`{RUN_ID}`): the current register summary is under "
                                "`## Extracted Dependency Register` below. The dated table of this section is kept in git history.", ""]
        reg = "## Extracted Dependency Register" if canon else legacy
        if reg:
            b = section_bounds(L, reg)
            L[b[0] + 1:b[1]] = [""] + counts_block(rows) + [""]
        else:
            i = next(k for k, l in enumerate(L) if l.strip() == "## Run Notes")
            L[i:i] = ["## Extracted Dependency Register", ""] + counts_block(rows) + [""]
        if d == "DEL-02-01":
            L = hgd_updates(L)
        open(mdp, "w", encoding="utf-8").write("\n".join(L))
    print("refreshed", len(LOG["deliverables"]))
    return 0


def hgd_updates(L):
    ruling = (f"  - {TODAY} (`{RUN_ID}`): HGD-2 CLOSED. DEP-02-01-007 RETIRED as accepted with SCA-APP-011 (Impact_Assessment.md "
              "group 1; Propagation_Plan.md section 8 item 2, group 2). DEP-02-01-008 RETIRED by the owner's ruling in chat on "
              f"{TODAY} (verbatim, transcription `{TRANSCRIPT}`): \"{OWNER_WORDS}\" HGD-3 is not decided. Its premise has "
              "changed: with DEP-02-02-005 and DEP-02-01-007 both RETIRED, emitting the DEL-02-01-V3-01 prerequisite on "
              "DEL-02-02-V3-03 would no longer close the four-node SCC {DEL-02-01, DEL-02-02, DEL-08-02, DEL-08-03} that simulation "
              "S2 showed. HGD-3 stays open for its owner. (Its seated items now live in the 2026-09-23 receiving clauses.)")
    i = next(k for k, l in enumerate(L) if l.startswith("- NEEDS_HUMAN_GRAPH_DECISION: HGD-1 DEP-02-01-006"))
    L.insert(i + 1, ruling)
    j = next(k for k, l in enumerate(L) if l.startswith("- Owner rulings still open: HGD-1"))
    L[j:j + 2] = [
        f"- Owner rulings still open ({TODAY}): HGD-1 (DEP-02-01-006 direction) and HGD-3 (DEL-02-02-V3-03 prerequisite, held "
        "non-gating, not emitted; its premise changed as recorded below). Fenced candidates FC-1 to FC-3 stay out of the register "
        "unless separately ruled.",
        f"- HGD-2 CLOSED {TODAY}: DEP-02-01-007 RETIRED (accepted with SCA-APP-011) and DEP-02-01-008 RETIRED by the owner's "
        f"ruling \"{OWNER_WORDS}\" (transcription `{TRANSCRIPT}`).",
        "- Reconcile with the DEL-02-02 register: its reverse row DEP-02-02-005 and this register's DEP-02-01-007, the matrix-era "
        f"pair HGD-2 and HGD-3 turned on, are both RETIRED as of {TODAY}. HGD-3's four-node SCC concern no longer arises from them; "
        "HGD-3 itself is not decided. The DEL-02-04 reciprocal DEP-02-04-017 (D-APP-110 SD-003) is unchanged in topology and is "
        "re-evidenced to the D-APP-110 ruling record (ESR-1). ESR-1 is CLOSED: its four retire candidates, including this "
        "register's DEP-02-01-014, were retired by the owner's ruling of 2026-09-27.",
    ]
    return L


if __name__ == "__main__":
    raise SystemExit(main())
