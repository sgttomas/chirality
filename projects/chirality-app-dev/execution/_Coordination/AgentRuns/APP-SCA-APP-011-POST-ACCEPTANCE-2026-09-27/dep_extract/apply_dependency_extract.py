#!/usr/bin/env python3
"""dependency-extract MODE=UPDATE for the confirmed SCA-APP-011 incremental plan (FULL_GRAPH).

Run from the repository root. Scope: the nine SCA-APP-011 MODIFY deliverables and their sixteen
FULL_GRAPH neighbours (INCREMENTAL_SETUP_PROPOSAL.md, confirmed by the owner on 2026-09-27).

Writes only each in-scope deliverable's Dependencies.csv and _DEPENDENCIES.md, plus
EXTRACTION_LOG.json next to this script. Source documents are read-only (their hashes are checked
before and after). Row decisions that need reasoning are explicit data below, each with its basis.
"""
from __future__ import annotations

import collections
import csv
import glob
import hashlib
import io
import json
import os
import re
import subprocess
import sys

TODAY = "2026-09-27"
RUN_ID = "APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27"
EX = "projects/chirality-app-dev/execution"
RUNDIR = f"{EX}/_Coordination/AgentRuns/{RUN_ID}"
DECOMP = f"{EX}/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
OWNER_WORDS = ("Confirm baseline SCA-APP-010 (accepted up to 2026-09-07) and the SCA-APP-011 incremental plan under "
               "FULL_GRAPH; HGD-2: retire DEP-02-01-008; APP-R058: option 1.")
MOD = ["DEL-02-02", "DEL-02-03", "DEL-03-03", "DEL-07-01", "DEL-07-02", "DEL-07-04", "DEL-07-05", "DEL-08-03", "DEL-09-03"]
NEI = ["DEL-02-01", "DEL-02-04", "DEL-02-05", "DEL-03-02", "DEL-03-04", "DEL-04-04", "DEL-05-02", "DEL-05-04", "DEL-06-03",
       "DEL-06-04", "DEL-07-03", "DEL-08-01", "DEL-08-02", "DEL-08-04", "DEL-08-05", "DEL-09-02"]
SCA = "SCA-APP-011 (DEC-026; groups 1-3 accepted 2026-09-27; landed PR #995 78e74f590)"
TRANSCRIPT = f"execution/_Coordination/AgentRuns/{RUN_ID}/CHAT_TRANSCRIPTION.md"

# ---------------------------------------------------------------------------------------------
# Row decisions (DependencyID -> action). Kinds:
#   RETIRE   Status=RETIRED (never deleted); SatisfactionStatus -> NOT_APPLICABLE (prior kept in Notes)
#   RESTATE  keep ID and ACTIVE; replace the named fields; LastSeen=TODAY
#   KEEP     keep ACTIVE; LastSeen=TODAY; append a note
#   HOLD     keep ACTIVE; LastSeen unchanged; append EVIDENCE_SOURCE_RETIRED note (owner decision proposed)
# ---------------------------------------------------------------------------------------------
RETIRED_FORMS = (f"retired_by=unseen_in_current_sources. The relationship is no longer a current obligation: {SCA} "
                 "retired the Workbench and Pipeline forms, their tests and the deliverable-api client this row describes; "
                 "DEL-02-02 ScopeOfWork.md §SCA-APP-011 Current Contract (Controlling) declares that content history only. "
                 "Accepted Propagation_Plan.md section 8 item 2 (retire DEP-02-02-005 to 009); expected outcome")
HOLD_NOTE = ("[WARNING] EVIDENCE_SOURCE_RETIRED: EvidenceQuote not re-seen. Its source, the `_STATUS.md` `## Remaining` section, "
             "was retired by the owner-directed finite Task Management account of 2026-09-23 "
             "(`_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/FINAL_CLOSEOUT.md`: 'the accepted "
             "Dependencies.csv rows and source quotes remain unchanged'), and the current governing ScopeOfWork.md does not "
             "restate this relationship. Held ACTIVE with LastSeen unchanged rather than retired, because that accepted account "
             "preserved the row{prov}; retire-or-re-evidence is proposed to the owner in "
             f"execution/_Coordination/AgentRuns/{RUN_ID}/DEPENDENCY_EXTRACT_RESULTS.md (ESR-1). Not an SCA-APP-011 effect.")

DECISIONS: dict[str, dict] = {
    # DX-01..DX-05
    **{f"DEP-02-02-00{n}": {"kind": "RETIRE", "dx": f"DX-0{n - 4}", "note": RETIRED_FORMS + f" DX-0{n - 4}."} for n in range(5, 10)},
    # DX-06
    "DEP-02-01-007": {"kind": "RETIRE", "dx": "DX-06",
                      "note": (f"retired_by=accepted_amendment. {SCA}: accepted Impact_Assessment.md (group 1, DQ-R) 'Retire "
                               "DEP-02-01-007' and Propagation_Plan.md section 8 item 2 (group 2). DEL-02-02 was rescoped and "
                               "keeps no Workbench deep-link target duty. The DEP-02-01-007 half of HGD-2 is resolved by that "
                               "acceptance; HGD-2 is closed (see DEP-02-01-008). Expected outcome DX-06.")},
    # DX-07 (HGD-2 ruled)
    "DEP-02-01-008": {"kind": "RETIRE", "dx": "DX-07",
                      "note": (f"retired_by=owner_ruling_HGD-2. Owner ruling in chat, {TODAY} (verbatim, transcription "
                               f"{TRANSCRIPT}): \"{OWNER_WORDS}\" HGD-2 option (a) retire. The surviving /pipeline route/query "
                               "compatibility stays keyed with DEL-08-02 (DEP-08-02-013); the handler "
                               "mergeMatrixTargetIntoCurrentUrl is test-only legacy shell. HGD-2 CLOSED. Expected outcome DX-07.")},
    # DX-08..DX-10
    "DEP-07-05-025": {"kind": "RESTATE", "dx": "DX-08,DX-09,DX-10",
                      "fields": {
                          "TargetName": "Dependency library and retained Chirality tool contracts",
                          "TargetLocation": "frontend/src/lib/workspace/deliverable-contracts.ts; mcp__chirality__deps_read; mcp__chirality__deps_write",
                          "Statement": ("DEL-07-05 must expose dependency read and write behavior through the dependency library "
                                        "and the retained Chirality tool contracts (SCA-APP-011 retired the HTTP route)."),
                          "EvidenceFile": "ScopeOfWork.md",
                          "SourceRef": "ScopeOfWork.md §CLM-011 — Scope",
                          "EvidenceQuote": ("Expose read/write behavior through the product dependency library "
                                            "(`frontend/src/lib/workspace/deliverable-contracts.ts`) and the Chirality dependency tool contracts"),
                      },
                      "quote_line": 188,
                      "note": (f"RESTATED {TODAY} under {SCA}: the /api/working-root/deliverable/dependencies route is retired; "
                               "evidence moved from the '[RETIRED — SCA-APP-011]' bullet (CLM-021 step 7, line 345) to live "
                               "CLM-011 Scope line 188. The SCA-APP-011 controlling section names DEL-06-03 as owner of live "
                               "deps_read exposure (deps_write live registration governed by DEL-06-04-REQ-010); TargetType "
                               "stays UNKNOWN as the confirmed expected outcome states, and the deliverable edge DEL-07-05 -> "
                               "DEL-06-03 is carried by DEP-06-03-007. Prior TargetName=Dependency API and MCP contract surfaces; "
                               "TargetLocation=/api/working-root/deliverable/dependencies; mcp__chirality__deps_read; "
                               "mcp__chirality__deps_write; SourceRef=ScopeOfWork.md §CLM-021 — Steps; EvidenceQuote=Expose "
                               "read/write behavior through `/api/working-root/deliverable/dependencies` GET/PUT. Expected "
                               "outcomes DX-08 to DX-10.")},
    # Found by the re-seen check (not in the expected-outcome list): anchor to the restated REQ-DEL-07-05-013
    "DEP-07-05-015": {"kind": "RESTATE", "dx": "(beyond DX)",
                      "fields": {
                          "TargetName": "Dependency library read and write",
                          "TargetLocation": "ScopeOfWork.md",
                          "Statement": ("REQ-DEL-07-05-013: the dependency library supports read and write of Dependencies.csv "
                                        "snapshot rows (restated by SCA-APP-011; the HTTP route is retired)."),
                          "SourceRef": "ScopeOfWork.md §CLM-012 — Requirements",
                          "EvidenceQuote": ("The dependency library MUST support read and write of `Dependencies.csv` snapshot rows "
                                            "through `readDeliverableDependencies` and `writeDeliverableDependencies`"),
                      },
                      "quote_line": 218,
                      "note": (f"RESTATED {TODAY} under {SCA}: the prior quote 'API surface MUST support GET/PUT' is no longer "
                               "in the source; REQ-DEL-07-05-013 is restated to the library (CLM-012 line 218; SCA-APP-011 "
                               "controlling section). The trace anchor to the same requirement ID is kept. Prior "
                               "TargetName=Dependency API GET PUT; TargetLocation=Specification.md; Statement=Dependency API "
                               "supports GET and PUT for Dependencies.csv snapshot rows.; EvidenceQuote=API surface MUST support "
                               "GET/PUT. Found by the re-seen check; not listed in the expected outcomes.")},
    # DX-11, DX-12
    "DEP-08-03-010": {"kind": "RESTATE", "dx": "DX-11,DX-12",
                      "fields": {
                          "TargetName": "Task-scope selection, knowledge-type discovery, and disabled option tests",
                          "Statement": ("DEL-08-03 must produce or maintain test records for task-scope selection, knowledge-type "
                                        "discovery, disabled options, TASK scope, and stale-selection reset behavior."),
                      },
                      "note": (f"RESTATED {TODAY} under {SCA}: Pipeline selector tests are retired; current records name "
                               "task-scope selection tests (CLM-025 line 445; lines 42 and 292). The minor _CONTEXT.md "
                               "conflict noted earlier is resolved by the amendment's _CONTEXT edits (E24-E26). Prior "
                               "TargetName=Pipeline selector, knowledge-type discovery, and disabled option tests; prior "
                               "Statement named pipeline selectors. Expected outcomes DX-11, DX-12.")},
    # DX-13
    "DEP-08-02-003": {"kind": "RESTATE", "dx": "DX-13",
                      "fields": {
                          "TargetName": ("Active dialogue/persona plus right-panel Who is working and read-only Session views over "
                                         "canonical hierarchy and selected-session replay, and Agent 0/1/2 role entry for Codex "
                                         "sessions with exact non-enforcement/preview posture labels."),
                          "TargetLocation": "execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L414",
                          "Statement": ("DEL-08-02 covers SOW-006 for active dialogue/persona context, the right-panel Who is "
                                        "working and read-only Session views, and Agent 0/1/2 role entry."),
                      },
                      "note": (f"RESTATED {TODAY} under {SCA}: the WORKBENCH form is retired; SOW-006 keeps its current meaning "
                               "(decomposition Scope Ledger SOW-006, line 414; scope table line 181). TargetName follows the "
                               "SOW-006 label used by DEP-02-02-002. Prior TargetName=Workbench context; TargetLocation="
                               "...#L382; Statement named selected WORKBENCH agent, row, and column context. Expected outcome DX-13.")},
    # DX-14
    "DEP-08-02-005": {"kind": "RESTATE", "dx": "DX-14",
                      "fields": {
                          "TargetLocation": "execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L267",
                          "Statement": ("DEL-08-02 supports OBJ-001, the governed local desktop harness centred on human-agent "
                                        "dialogue as the invariant primary surface."),
                      },
                      "note": (f"RESTATED {TODAY} under {SCA}: the Statement no longer names the retired WORKBENCH and PIPELINE "
                               "forms; OBJ-001 row is decomposition line 267. Prior TargetLocation=...#L238; prior Statement "
                               "named governed WORKBENCH, PIPELINE, PORTAL, and operator workflow behavior. Expected outcome DX-14.")},
    # DX-15
    "DEP-02-03-009": {"kind": "KEEP", "dx": "DX-15",
                      "note": (f"{TODAY} UPDATE: kept ACTIVE. TENSION (residual, no decision asked): DEL-02-03-REQ-009 (lines 143 "
                               "and 181) still names PIPELINE `TASK*` preselection, while accepted E80 (CLM-029, line 322) "
                               "withdrew the old Pipeline scope-scan and deliverable-routing examples as compatibility "
                               "obligations. SCA-APP-011 did not amend REQ-009 and records no own-register change for DEL-02-03 "
                               "(Propagation_Plan.md section 7). The target is DEL-08-03's retained task-scope dispatch contract "
                               "(frontend/src/lib/pipeline/pipeline-dispatch-contract.ts), not the retired form. Aligning REQ-009 "
                               "is a DEL-02-03 scope question for a later change. Expected outcome DX-15.")},
    # Re-evidenced from the retired _STATUS source to the APP-R016 receiving clause
    "DEP-02-01-013": {"kind": "RESTATE", "dx": "(beyond DX)",
                      "fields": {
                          "Statement": ("DEL-02-01 hands the app-icon design-source to raster/package integrity record to "
                                        "DEL-09-04, which carries the packaging evidence."),
                          "EvidenceFile": "ScopeOfWork.md",
                          "SourceRef": "ScopeOfWork.md §Retired status detail (2026-09-23) (APP-R016)",
                          "EvidenceQuote": "the design-source to raster/package integrity handoff with DEL-09-04",
                      },
                      "quote_line": 373,
                      "note": (f"RE-EVIDENCED {TODAY}: the former source, _STATUS.md ## Remaining (DEL-02-01-V3-04 Return), was "
                               "retired by the 2026-09-23 finite Task Management account; its receiving clause APP-R016 "
                               "(ScopeOfWork.md line 373; APP-R017 line 375 'DEL-09-04 carries packaging evidence') states the "
                               "same handoff to DEL-09-04. Prior EvidenceFile=_STATUS.md; SourceRef=_STATUS.md#remaining "
                               "(DEL-02-01-V3-04 Return); EvidenceQuote=the reproducibility record (source SVG hash to raster) "
                               "is handed to DEL-09-04-V3-02.")},
}
HOLD = {
    "DEP-02-02-021": "",
    "DEP-02-02-022": " (emitted under owner ruling D-APP-109 H-007; DOCUMENT target from the D-APP-110 decompose)",
    "DEP-07-01-010": "",
    "DEP-02-01-014": "",
    "DEP-02-04-015": " (its bidirectional-pair question was addressed by the owner's D-APP-110 decompose)",
    "DEP-02-04-016": " (its mutual-dependency question was addressed by the owner's D-APP-110 decompose)",
    "DEP-02-04-017": " (emitted under owner ruling D-APP-109 H-010; decomposed under D-APP-110 SD-003)",
    "DEP-02-04-018": " (decomposed to a DOCUMENT target under owner ruling D-APP-110)",
    "DEP-02-04-019": " (decomposed to a DOCUMENT target under owner ruling D-APP-110)",
    "DEP-08-01-018": " (emitted under owner ruling D-APP-109 H-018)",
    "DEP-08-01-019": "",
    "DEP-08-04-013": " (emitted under owner ruling D-APP-109 H-019)",
}
for k, v in HOLD.items():
    DECISIONS[k] = {"kind": "HOLD", "dx": "(beyond DX)", "note": HOLD_NOTE.format(prov=v)}

# New row found in text SCA-APP-011 added (DEL-07-04 SCA-APP-011 controlling section, line 22)
NEW_ROWS = {
    "DEL-07-04": [{
        "DependencyClass": "EXECUTION", "AnchorType": "NOT_APPLICABLE", "Direction": "DOWNSTREAM", "DependencyType": "INTERFACE",
        "TargetType": "DELIVERABLE", "TargetPackageID": "PKG-06", "TargetDeliverableID": "DEL-06-03", "TargetRefID": "",
        "TargetName": "Initial Chirality MCP Read Tools",
        "TargetLocation": "execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md",
        "Statement": ("DEL-07-04's status library (readDeliverableStatus, transitionDeliverableStatus) is the interface that the "
                      "status_read tool wraps; live exposure of status_read through the Runtime application-tool interface is "
                      "DEL-06-03's open work."),
        "EvidenceFile": "ScopeOfWork.md", "SourceRef": "ScopeOfWork.md §SCA-APP-011 Current Contract (Controlling)",
        "EvidenceQuote": ("Live exposure of the read tool `status_read` through the Runtime application-tool interface is "
                          "DEL-06-03's open work"),
        "Explicitness": "EXPLICIT", "RequiredMaturity": "TBD", "ProposedMaturity": "TBD", "SatisfactionStatus": "TBD",
        "Confidence": "MEDIUM", "Origin": "EXTRACTED",
        "Notes": (f"FACT: added {TODAY} from text SCA-APP-011 introduced (ScopeOfWork.md line 22); the consumer deliverable is "
                  "named explicitly. The parallel DEL-07-05 edge to DEL-06-03 is carried by DEP-06-03-007. status_transition "
                  "live registration is governed by DEL-06-04-REQ-010 and has no live registration, so no DEL-06-04 row is "
                  "emitted. Confidence MEDIUM because the exposure is open work."),
        "_quote_line": 22,
    }],
}

NORM_RX = re.compile(r"[`*>|]")


def norm(t: str) -> str:
    t = t.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", NORM_RX.sub(" ", t)).strip().lower()


def sha(p: str) -> str:
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def folder(d: str) -> str:
    return glob.glob(f"{EX}/PKG-*/1_Working/{d}_*")[0]


def resolve(fold: str, ef: str):
    for c in (os.path.join(fold, ef), ef, os.path.join("projects/chirality-app-dev", ef)):
        if os.path.isfile(c):
            return c
    return None


def seen(fold, r, cache):
    q = r["EvidenceQuote"].strip()
    if not q:
        return None
    p = resolve(fold, r["EvidenceFile"].strip())
    if p is None:
        return None
    lines = cache.setdefault(p, open(p, encoding="utf-8").read().split("\n"))
    nq = norm(q)
    whole = norm("\n".join(lines))
    if nq not in whole:
        return False
    # the quote counts as seen only if at least one occurrence is outside a [RETIRED line
    hits = [l for l in lines if nq in norm(l)]
    if hits and all("[retired" in l.lower() for l in hits):
        return "RETIRED_LINE"
    return True


def main() -> int:
    log = {"run_id": RUN_ID, "date": TODAY, "decomposition": DECOMP, "decomposition_sha256": sha(DECOMP), "deliverables": {}}
    for d in MOD + NEI:
        fold = folder(d)
        csvp, mdp = fold + "/Dependencies.csv", fold + "/_DEPENDENCIES.md"
        srcs = {n: sha(fold + "/" + n) for n in ("ScopeOfWork.md", "_CONTEXT.md", "_REFERENCES.md", "_STATUS.md") if os.path.exists(fold + "/" + n)}
        pre = {"Dependencies.csv": sha(csvp), "_DEPENDENCIES.md": sha(mdp)}
        text = open(csvp, encoding="utf-8").read()
        rows = list(csv.DictReader(io.StringIO(text)))
        fields = list(rows[0].keys())
        cache: dict = {}
        acts = collections.OrderedDict()
        for r in rows:
            did = r["DependencyID"]
            dec = DECISIONS.get(did)
            if r["Status"] != "ACTIVE":
                if dec:
                    raise SystemExit(f"{did}: decision for a non-ACTIVE row")
                continue
            s = seen(fold, r, cache)
            if dec is None:
                if s is True:
                    r["LastSeen"] = TODAY
                    acts[did] = "RESEEN"
                else:
                    raise SystemExit(f"{did}: not re-seen ({s}) and no explicit decision")
                continue
            k = dec["kind"]
            if k == "RETIRE":
                prior = r["SatisfactionStatus"]
                r["Status"] = "RETIRED"
                r["SatisfactionStatus"] = "NOT_APPLICABLE"
                r["Notes"] = (r["Notes"] + " " if r["Notes"] else "") + f"{TODAY} UPDATE: RETIRED. {dec['note']} Prior SatisfactionStatus={prior}."
            elif k == "RESTATE":
                for f, v in dec["fields"].items():
                    r[f] = v
                if "quote_line" in dec:
                    src = resolve(fold, r["EvidenceFile"])
                    line = open(src, encoding="utf-8").read().split("\n")[dec["quote_line"] - 1]
                    if r["EvidenceQuote"] not in line:
                        raise SystemExit(f"{did}: new EvidenceQuote not verbatim in {src}:{dec['quote_line']}")
                    if len(r["EvidenceQuote"].split()) > 30:
                        raise SystemExit(f"{did}: EvidenceQuote over 30 words")
                r["LastSeen"] = TODAY
                r["Notes"] = (r["Notes"] + " " if r["Notes"] else "") + dec["note"]
            elif k == "KEEP":
                if s is not True:
                    raise SystemExit(f"{did}: KEEP but quote not seen")
                r["LastSeen"] = TODAY
                r["Notes"] = (r["Notes"] + " " if r["Notes"] else "") + dec["note"]
            elif k == "HOLD":
                if s is True:
                    raise SystemExit(f"{did}: HOLD but quote is seen")
                r["Notes"] = (r["Notes"] + " " if r["Notes"] else "") + f"{TODAY} UPDATE: " + dec["note"]
            acts[did] = f"{k} {dec['dx']}"
        for nr in NEW_ROWS.get(d, []):
            nr = dict(nr)
            ql = nr.pop("_quote_line")
            line = open(fold + "/ScopeOfWork.md", encoding="utf-8").read().split("\n")[ql - 1]
            if nr["EvidenceQuote"] not in line:
                raise SystemExit(f"{d}: new-row quote not verbatim at line {ql}")
            seqs = [int(x["DependencyID"].rsplit("-", 1)[1]) for x in rows]
            did = f"DEP-{d[4:6]}-{d[7:9]}-{max(seqs) + 1:03d}"
            base = rows[0]
            new = {f: "" for f in fields}
            new.update({"RegisterSchemaVersion": "v3.1", "DependencyID": did, "FromPackageID": base["FromPackageID"],
                        "FromDeliverableID": d, "FromDeliverableName": base["FromDeliverableName"],
                        "FirstSeen": TODAY, "LastSeen": TODAY, "Status": "ACTIVE"})
            new.update(nr)
            rows.append(new)
            acts[did] = "ADDED (beyond DX)"
        # unseen rows without a decision were rejected above; anything seen only on a [RETIRED line also needs a decision
        out = io.StringIO()
        w = csv.DictWriter(out, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
        open(csvp, "w", encoding="utf-8", newline="").write(out.getvalue())
        post_src = {n: sha(fold + "/" + n) for n in srcs}
        if post_src != srcs:
            raise SystemExit(f"{d}: a source document changed")
        log["deliverables"][d] = {"role": "MODIFY" if d in MOD else "NEIGHBOUR", "folder": fold, "sources_sha256": srcs,
                                  "pre_sha256": pre, "actions": acts}
    json.dump(log, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "EXTRACTION_LOG.json"), "w"), indent=1)
    c = collections.Counter(v.split()[0] for x in log["deliverables"].values() for v in x["actions"].values())
    print(dict(c))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
