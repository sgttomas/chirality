#!/usr/bin/env python3
"""Function 4 of dependency-extract: refresh the agent-owned sections of each in-scope _DEPENDENCIES.md.

Run from the repository root after apply_dependency_extract.py. Each file is rebuilt from its pre-image at the
extraction's basis commit (hash-checked against EXTRACTION_LOG.json), so a rerun is idempotent. Human-owned sections
(Dependency Tracking, Declared Upstream, Declared Downstream) are never edited. Following dependency-extract Function 4
and the SCA-APP-011 run's script of the same name, each agent-owned section is refreshed under the heading the file
already uses. For each file this:
- replaces the body of the file's register section: `## Extracted Dependency Register`, or the legacy
  `## Current Extracted Dependency Summary — <date>` heading the file already uses (where a file carries both and the
  legacy section already points to the canonical one, the pointer is left as it is);
- replaces the body of `## Lifecycle Summary`;
- adds `### 2026-09-27 SCA-APP-012 incremental setup refresh (UPDATE)` as a subsection at the end of the file's
  existing `## Run Notes` section;
- appends one Run History entry in the file's own table columns or bullet order.
"""
from __future__ import annotations

import collections
import csv
import hashlib
import json
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = json.load(open(os.path.join(HERE, "EXTRACTION_LOG.json")))
TODAY = LOG["date"]
RUN_ID = LOG["run_id"]
DECOMP_REL = "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
DSHA = LOG["decomposition_sha256"]
OWNER_WORDS = "I Confirm the SCA-APP-012 incremental plan under FULL_GRAPH; DEP-02-03-008: retire; TM-APP-051: option 1."
TRANSCRIPT = f"execution/_Coordination/AgentRuns/{RUN_ID}/CHAT_TRANSCRIPTION.md"
RUN_HEAD = f"### {TODAY} SCA-APP-012 incremental setup refresh (UPDATE)"
BASIS = "63e5de1f2f19c3a1dab073babbadfbfcc6199e70"
OLDER = {"DEL-05-03", "DEL-06-01", "DEL-06-02", "DEL-09-04"}
# Rows this run changed only in `LastSeen` that carry the pre-existing EVQ-006 finding (validator report, 84 rows).
# No other row this run changed carries it, so every other index keeps the plain statement.
EVQ006_LASTSEEN = {"DEL-05-03": "DEP-05-03-001", "DEL-06-01": "DEP-06-01-001"}

# Deliverable-specific observations from the scan of text added since the previous extraction.
EXTRA = {
    "DEL-02-03": [
        "- DX outcomes: DX-01 (DEP-02-03-009 RETIRED under group 1 R-b), DX-02 (DEP-02-03-004 re-evidenced to the restated "
        "CLM-003 row, line 63), DX-06 (DEP-02-03-007 re-evidenced to the restated DEL-02-03-REQ-010, line 153; transition-control "
        "wording dropped) and DX-07 (DEP-02-03-008 RETIRED). DX-07 was confirmed by the owner in chat on "
        f"{TODAY} (verbatim, transcription `{TRANSCRIPT}`): \"{OWNER_WORDS}\" The DX-15 tension recorded by the SCA-APP-011 "
        "refresh above is resolved by the DX-01 retirement.",
        "- New text scanned: the SCA-APP-012 controlling section cites DEL-08-03-REQ-010 for the scan surface and states that "
        "DEL-08-03 keeps the TASK scope semantics and that no deliverable summary widget routes to a dispatch intent; this names "
        "no dependency, so no row is emitted and the DEL-02-03 -> DEL-08-03 edge is not restated.",
    ],
    "DEL-08-03": [
        "- DX-03: DEP-08-03-007 `TargetName` now names the deliverable scan API (CLM-004 'Deliverable scan API', line 124). The "
        "source no longer names the retired scope route, so the 2026-09-05 source-endpoint label conflict no longer reproduces "
        "and is not reported by this run.",
        "- Inbound DEP-02-03-009 (DEL-02-03 -> DEL-08-03) is RETIRED in the DEL-02-03 register (DX-01).",
    ],
    "DEL-02-01": ["- New text scanned: the SCA-APP-012 controlling section keeps the TYPES §4 route/query compatibility question "
                  "keyed with DEL-08-02, unchanged; DEP-02-01-006 is re-seen and unchanged apart from `LastSeen` (P-keep)."],
    "DEL-08-02": ["- DX-04 does not apply (P-keep): DEP-08-02-013 is re-seen and unchanged apart from `LastSeen`."],
    "DEL-07-02": ["- New text scanned: the SCA-APP-012 bullet naming DEL-06-03 for the read-only scaffold preview is marked "
                  "`[RETIRED — SCA-APP-012]` and states ownership, not a dependency; no row is emitted."],
    "DEL-09-04": ["- [INFO] New text scanned: APP-R078 in the 2026-09-23 retired status detail ('Preserve source artwork and the "
                  "renderer removal direction with DEL-02-01') names DEL-02-01 without a direction. The relationship is already "
                  "recorded from the supplier side as DEP-02-01-013 (DEL-02-01 -> DEL-09-04, re-evidenced to APP-R016 on "
                  "2026-09-27), so under `STRICTNESS=CONSERVATIVE` no row is emitted here; noted for the register owner."],
    "DEL-05-03": ["- New text scanned: APP-R045 in the 2026-09-23 retired status detail names no other deliverable. The retired "
                  "`_STATUS.md` `## Remaining` section was cited by no row of this register."],
    "DEL-06-01": ["- New text scanned: the 2026-09-23 edit to procedure step 5 names no other deliverable. The retired `_STATUS.md` "
                  "`## Remaining` section was cited by no row of this register."],
    "DEL-06-02": ["- New text scanned: the 2026-09-23 edit to procedure step 5 names no other deliverable. The retired `_STATUS.md` "
                  "`## Remaining` section was cited by no row of this register."],
}


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
    role = ("SCA-APP-012 MODIFY deliverable" if info["role"] == "MODIFY" else "FULL_GRAPH neighbour of the SCA-APP-012 MODIFY set")
    act = [r for r in rows if r["Status"] == "ACTIVE"]
    parents = sum(1 for r in act if r["AnchorType"] == "IMPLEMENTS_NODE")
    src = "; ".join(f"`{n}` `{h}`" for n, h in info["sources_sha256"].items())
    prev = ("2026-09-22; the 2026-09-23 retired-status clauses are the text added since" if d in OLDER
            else "2026-09-27, `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`; the accepted SCA-APP-012 scope text is the text added since"
            if info["role"] == "MODIFY" else "2026-09-27, `APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27`; no source text changed since")
    out = [RUN_HEAD, "",
           f"- Run: `{RUN_ID}`, `project-setup` INCREMENTAL Phase 5.6 (FULL_GRAPH) dispatch of `bundled:chirality-root/dependency-extract`, "
           f"run directly by WORKING_ITEMS after the owner confirmed the SCA-APP-012 incremental plan on {TODAY} (verbatim in "
           f"`{TRANSCRIPT}`). Role: {role}.",
           f"- Runtime overrides: `SCOPE={d}`; `RUN_ROOT=projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH={DECOMP_REL}`; "
           "`MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO` (`ScopeOfWork.md`, `_CONTEXT.md`, "
           "`_REFERENCES.md`, `_STATUS.md`); `ANCHOR_DOC=ScopeOfWork.md`; `EXECUTION_DOC_ORDER=ScopeOfWork.md, _CONTEXT.md`.",
           f"- Decomposition authority: FOUND, SHA-256 `{DSHA}` (as amended by SCA-APP-012).",
           f"- Source-preservation gate: {src}; read-only and unchanged by this run.",
           "- Pre-images: `Dependencies.csv` `" + info["pre_sha256"]["Dependencies.csv"] + "`, `_DEPENDENCIES.md` `"
           + info["pre_sha256"]["_DEPENDENCIES.md"] + "`.",
           "- Method: every existing ACTIVE row was re-checked against its cited current source (quote found verbatim, and not only "
           f"inside a `[RETIRED` clause). Previous extraction: {prev}; that text was scanned for new explicit cross-deliverable "
           "relationships. Unchanged source text yields the rows already recorded.",
           f"- Results: re-seen {len(by['RESEEN'])} (`LastSeen={TODAY}`); restated in place {len(by['RESTATE'])}; retired "
           f"{len(by['RETIRE'])}; added 0. No row deleted; every existing `DependencyID` preserved; `Status=CANDIDATE` not emitted."]
    for kind in ("RETIRE", "RESTATE"):
        for did in by[kind]:
            r = next(x for x in rows if x["DependencyID"] == did)
            label = {"RETIRE": "RETIRED", "RESTATE": "RESTATED"}[kind]
            if kind == "RESTATE" and did in ("DEP-02-03-004", "DEP-02-03-007"):
                label = "RE-EVIDENCED"
            ref = acts[did].split(" ", 1)[1] if " " in acts[did] else ""
            tgt = r["TargetDeliverableID"] or r["TargetRefID"] or r["TargetName"][:60]
            out.append(f"  - {label} {did} ({r['DependencyClass']} {r['Direction']} {r['DependencyType']} -> {tgt}) {ref}; see the row `Notes`.")
    out += EXTRA.get(d, [])
    out += ["- Declared entries: none (the declared sections carry no SPEC §5.2 entry). Mirror rows added 0, refreshed 0, retired 0; "
            "entries skipped 0.",
            f"- Parent anchor check: {'PASS; exactly one' if parents == 1 else ('[WARNING] FLOATING_NODE: no' if parents == 0 else '[WARNING] AMBIGUOUS_ANCHOR:')} "
            f"ACTIVE `IMPLEMENTS_NODE` row{'' if parents == 1 else 's'} ({parents}).",
            "- Function 5 checks (`execution/_Coordination/AgentRuns/" + RUN_ID + "/dep_extract/FUNCTION5_CHECKS.json`): "
            "`validate_dependencies_schema.py` PASS; `DependencyID` unique; every enum value written by this run VALID "
            "(`validate_enum.py`); ID format PASS for `FromDeliverableID`, `FromPackageID` and every `DependencyID` "
            "(`validate_id_format.sh`); index counts match `Dependencies.csv`.",
            "- [INFO] EVQ-006 (report-only, `validate_decomposition_registers.py --families EVQ,DRB`): the current validator "
            "resolves `EvidenceFile` under its allowed bases, which do not include the repository-relative "
            "`projects/chirality-app-dev/...` form some App rows use; it reports 84 such rows project-wide. This run changed no "
            "`EvidenceFile`, so the count is unchanged "
            + (f"and no row whose evidence fields this run changed carries the finding (one `LastSeen`-only row, "
               f"{EVQ006_LASTSEEN[d]}, carries the pre-existing finding)" if d in EVQ006_LASTSEEN
               else "and no row this run changed carries the finding")
            + "; no EVQ-003, EVQ-004 or DRB-006 finding."]
    return out


def run_history_row(header_line, info, rows):
    cols = [c.strip() for c in header_line.strip().strip("|").split("|")]
    act = [r for r in rows if r["Status"] == "ACTIVE"]
    vals = []
    for c in cols:
        lc = c.lower()
        if lc.startswith("timestamp") or lc == "date":
            vals.append(f"{TODAY} (`{RUN_ID}`)")
        elif lc == "mode":
            vals.append("UPDATE")
        elif lc.startswith("strictness"):
            vals.append("CONSERVATIVE")
        elif "decomposition path" in lc:
            vals.append(f"`{DECOMP_REL}`")
        elif "decomposition" in lc:
            vals.append(f"FOUND `{DSHA[:12]}…` (SCA-APP-012 amended)")
        elif "warning" in lc:
            vals.append("none")
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
            bullet = (f"- {TODAY} (`{RUN_ID}`): `dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`; "
                      f"decomposition found, SHA-256 `{DSHA[:12]}…` (SCA-APP-012 amended); warnings: none"
                      f"; ACTIVE={len(act)} (ANCHOR={sum(1 for r in act if r['DependencyClass'] == 'ANCHOR')}, "
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
            b = section_bounds(L, legacy)
            body = "\n".join(L[b[0] + 1:b[1]])
            if "the current register summary is under `## Extracted Dependency Register`" not in body:
                L[b[0] + 1:b[1]] = ["", f"Superseded on {TODAY} (`{RUN_ID}`): the current register summary is under "
                                    "`## Extracted Dependency Register` below. The dated table of this section is kept in git history.", ""]
        reg = "## Extracted Dependency Register" if canon else legacy
        if reg:
            b = section_bounds(L, reg)
            L[b[0] + 1:b[1]] = [""] + counts_block(rows) + [""]
        else:
            i = next(k for k, l in enumerate(L) if l.strip() == "## Run Notes")
            L[i:i] = ["## Extracted Dependency Register", ""] + counts_block(rows) + [""]
        open(mdp, "w", encoding="utf-8").write("\n".join(L))
    print("refreshed", len(LOG["deliverables"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
