#!/usr/bin/env python3
"""dependency-extract MODE=UPDATE for the confirmed SCA-APP-012 incremental plan (FULL_GRAPH).

Run from the repository root. Scope: the eight SCA-APP-012 MODIFY deliverables and their sixteen
FULL_GRAPH neighbours (INCREMENTAL_SETUP_PROPOSAL.md, confirmed by the owner on 2026-09-27).

Writes only each in-scope deliverable's Dependencies.csv, plus EXTRACTION_LOG.json next to this
script (the _DEPENDENCIES.md indexes are refreshed by refresh_dependency_indexes.py). Source
documents are read-only (their hashes are checked before and after). Row decisions that need
reasoning are explicit data below, each with its basis; every other ACTIVE row must be re-seen in
its cited source or the run stops. Modelled on the SCA-APP-011 run's script of the same name.
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
import sys

TODAY = "2026-09-27"
RUN_ID = "APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27"
EX = "projects/chirality-app-dev/execution"
DECOMP = f"{EX}/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
OWNER_WORDS = "I Confirm the SCA-APP-012 incremental plan under FULL_GRAPH; DEP-02-03-008: retire; TM-APP-051: option 1."
MOD = ["DEL-02-01", "DEL-02-02", "DEL-02-03", "DEL-06-03", "DEL-07-02", "DEL-07-03", "DEL-08-02", "DEL-08-03"]
NEI = ["DEL-02-04", "DEL-02-05", "DEL-04-04", "DEL-05-02", "DEL-05-03", "DEL-05-04", "DEL-06-01", "DEL-06-02", "DEL-07-01",
       "DEL-07-04", "DEL-07-05", "DEL-08-01", "DEL-08-04", "DEL-08-05", "DEL-09-02", "DEL-09-04"]
SCA = "SCA-APP-012 (DEC-027; groups 1-3 accepted 2026-09-27; landed PR #1020 bc1ea504d)"
TRANSCRIPT = f"execution/_Coordination/AgentRuns/{RUN_ID}/CHAT_TRANSCRIPTION.md"
IMPACT = "execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/Impact_Assessment.md"

# ---------------------------------------------------------------------------------------------
# Row decisions (DependencyID -> action). Kinds:
#   RETIRE   Status=RETIRED (never deleted); SatisfactionStatus -> NOT_APPLICABLE (prior kept in Notes)
#   RESTATE  keep ID and ACTIVE; replace the named fields; LastSeen=TODAY
# ---------------------------------------------------------------------------------------------
DECISIONS: dict[str, dict] = {
    # DX-01
    "DEP-02-03-009": {"kind": "RETIRE", "dx": "DX-01",
                      "note": (f"retired_by=accepted_amendment. {SCA}: accepted group 1 R-b retires DEL-02-03-REQ-009 "
                               "('DEP-02-03-009 expected to retire at re-extraction (DX-01)', checkpoint_snapshots/"
                               "SCA-APP-012_GROUP-1_2026-09-27/DECISION.md) and Propagation_Plan.md section 8 item 2 (group 2). "
                               "The quoted verification row now reads '[RETIRED — SCA-APP-012] Routing test from deliverable "
                               "row to PIPELINE `TASK*` preselection.' (ScopeOfWork.md lines 152 and 190), so the quote is not "
                               "re-seen outside a retired clause; the controlling section (line 23) states that no deliverable "
                               "summary widget routes to a dispatch intent and that DEL-08-03 keeps the TASK scope semantics. "
                               "The DX-15 tension recorded above is resolved by this retirement. Prior EvidenceQuote and Notes "
                               "kept above. Expected outcome DX-01.")},
    # DX-07 (the owner confirmed the retirement with the plan)
    "DEP-02-03-008": {"kind": "RETIRE", "dx": "DX-07",
                      "note": (f"retired_by=unseen_in_current_sources, confirmed by the owner. {SCA}: the cited CLM-005 widget "
                               "row (ScopeOfWork.md line 90) now reads 'Present deliverable identity and lifecycle status "
                               "read-only from `/api/project/deliverables` (SCA-APP-012 retired the routeable deliverable rows "
                               "for TASK workflows and moved dependency snapshots out of this UI)'; the prior quote occurs "
                               "nowhere, and no current DEL-02-03 text states that its widgets consume DEL-07-05 dependency "
                               "snapshots (restated DEL-02-03-REQ-010, line 153, names the dependency library only as where "
                               f"snapshots are read instead of a browser API). The accepted {IMPACT} lines 457-464 (Row 3, "
                               "ScopeChanging YES) records that the dependency-snapshot presentation leaves DEL-02-03. Owner act "
                               f"in chat, {TODAY} (verbatim, transcription {TRANSCRIPT}): \"{OWNER_WORDS}\" Prior EvidenceQuote "
                               "and Notes kept above. Expected outcome DX-07.")},
    # DX-02
    "DEP-02-03-004": {"kind": "RESTATE", "dx": "DX-02",
                      "fields": {
                          "EvidenceQuote": "`/api/working-root/validate`, `/api/working-root/tree`, `/api/project/deliverables`",
                      },
                      "quote_line": 63,
                      "note": (f"RE-EVIDENCED {TODAY} under {SCA}: the restated CLM-003 row (ScopeOfWork.md line 63) lists "
                               "the workspace APIs without the retired `/api/working-root/scope` (now '[RETIRED — SCA-APP-012] "
                               "`/api/working-root/scope`'); the scope-scan surface is `/api/project/deliverables` (controlling "
                               "section, line 22). Relationship, target (REF-003, docs/SPEC.md section 17.2), status and "
                               "satisfaction unchanged. Prior EvidenceQuote=api/working-root/validate`, `/api/working-root/tree`, "
                               "`/api/working-root/scope`, `/api/project/deliverables. Expected outcome DX-02.")},
    # DX-03
    "DEP-08-03-007": {"kind": "RESTATE", "dx": "DX-03",
                      "fields": {
                          "TargetName": "docs/SPEC.md Section 17.2 deliverable scan API",
                      },
                      "note": (f"RESTATED {TODAY} under {SCA}: register row 6 (E19) renames the CLM-004 row to 'Deliverable scan "
                               "API' (ScopeOfWork.md line 124: '`/api/project/deliverables` scans deliverables and knowledge types "
                               "for the active root'), and the SOW no longer names `/api/working-root/scope`, so the label-only "
                               "CONFLICT recorded above is resolved. EvidenceQuote (DEL-08-03-REQ-010, line 244) re-seen "
                               "unchanged; target REF-003 unchanged. Prior TargetName=docs/SPEC.md Section 17.2 working-root "
                               "scope API. Expected outcome DX-03.")},
    # DX-06
    "DEP-02-03-007": {"kind": "RESTATE", "dx": "DX-06",
                      "fields": {
                          "Statement": ("Deliverable summaries present lifecycle status read-only from /api/project/deliverables; "
                                        "DEL-07-04 owns the lifecycle status semantics and the canonical _STATUS.md parser."),
                          "SourceRef": "ScopeOfWork.md §CLM-009 — Requirements (DEL-02-03-REQ-010, line 153 current)",
                          "EvidenceQuote": "present lifecycle status read-only from `/api/project/deliverables`",
                      },
                      "quote_line": 153,
                      "note": (f"RE-EVIDENCED {TODAY} under {SCA}: register row 3 restated DEL-02-03-REQ-010, so the prior quote "
                               "no longer occurs. The restated requirement (ScopeOfWork.md line 153) still has deliverable "
                               "summaries present lifecycle status read-only from `/api/project/deliverables`; DEL-07-04 owns the "
                               "lifecycle status semantics and the canonical _STATUS.md parser (DEL-07-04 OUT-001; "
                               "frontend/src/lib/lifecycle/), so the read-only status relationship holds and only its evidence "
                               "moves. The Statement drops the transition-control wording: that clause leaves DEL-02-03 "
                               f"({IMPACT} lines 463-464). Relationship, target, status and satisfaction unchanged. Prior "
                               "Statement=Deliverable summary widgets consume lifecycle/status information read-only where "
                               "available; transition controls remain owned by supported workflows.; SourceRef=ScopeOfWork.md "
                               "§CLM-009 — Requirements; EvidenceQuote=consume status and dependency contract snapshots "
                               "read-only where applicable. Expected outcome DX-06.")},
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
        text = open(csvp, encoding="utf-8", newline="").read()
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
                if s is True:
                    raise SystemExit(f"{did}: RETIRE but quote is still seen")
                prior = r["SatisfactionStatus"]
                r["Status"] = "RETIRED"
                r["SatisfactionStatus"] = "NOT_APPLICABLE"
                r["Notes"] = (r["Notes"] + " " if r["Notes"] else "") + f"{TODAY} UPDATE: RETIRED. {dec['note']} Prior SatisfactionStatus={prior}."
            elif k == "RESTATE":
                if "quote_line" not in dec and s is not True:
                    raise SystemExit(f"{did}: RESTATE keeps its quote, but the quote is not seen")
                for f, v in dec["fields"].items():
                    r[f] = v
                if "quote_line" in dec:
                    src = resolve(fold, r["EvidenceFile"])
                    line = open(src, encoding="utf-8").read().split("\n")[dec["quote_line"] - 1]
                    if r["EvidenceQuote"] not in line:
                        raise SystemExit(f"{did}: new EvidenceQuote not verbatim in {src}:{dec['quote_line']}")
                    if "[RETIRED" in r["EvidenceQuote"] or len(r["EvidenceQuote"].split()) > 30:
                        raise SystemExit(f"{did}: EvidenceQuote retired or over 30 words")
                r["LastSeen"] = TODAY
                r["Notes"] = (r["Notes"] + " " if r["Notes"] else "") + dec["note"]
            acts[did] = f"{k} {dec['dx']}"
        missing = [k for k in DECISIONS if k.startswith(f"DEP-{d[4:6]}-{d[7:9]}-") and k not in acts]
        if missing:
            raise SystemExit(f"{d}: decisions not applied {missing}")
        out = io.StringIO()
        w = csv.DictWriter(out, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
        open(csvp, "w", encoding="utf-8", newline="").write(out.getvalue())
        post_src = {n: sha(fold + "/" + n) for n in srcs}
        if post_src != srcs:
            raise SystemExit(f"{d}: a source document changed")
        log["deliverables"][d] = {"role": "MODIFY" if d in MOD else "NEIGHBOUR", "folder": fold, "sources_sha256": srcs,
                                  "pre_sha256": pre, "post_sha256": {"Dependencies.csv": sha(csvp)},
                                  "csv_changed": sha(csvp) != pre["Dependencies.csv"], "actions": acts}
    json.dump(log, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "EXTRACTION_LOG.json"), "w"), indent=1)
    c = collections.Counter(v.split()[0] for x in log["deliverables"].values() for v in x["actions"].values())
    print(dict(c), "csv changed:", [d for d, x in log["deliverables"].items() if x["csv_changed"]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
