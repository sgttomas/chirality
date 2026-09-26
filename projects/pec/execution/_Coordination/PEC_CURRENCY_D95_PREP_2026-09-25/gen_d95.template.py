#!/usr/bin/env python3
"""D-PEC-95 exact generator: revision-1.5 currency packet (N1 records, N2 re-pin, N3 quotes).

Deterministic. Stdlib only. Run from any directory against a repository root
whose bytes equal origin/main 13df8b795e47ab2284018eeefc9d5473d00c232d for
every path listed in PREIMAGES. Every postimage is computed and every check
passes before the first byte is written; on any failure it exits 1 and writes
nothing.

Fail-closed checks before any write:
  * every PREIMAGES path hashes to its pinned SHA-256 (targets and basis);
  * N2 population: the _CONTEXT.md files carrying the revision-1.4 tail are
    exactly the pinned 42, and the _REFERENCES.md files naming revision 1.4
    are exactly the pinned 64; every anchor occurs exactly once;
  * N3: each of the 19 rows exists once, is ACTIVE EXECUTION, carries the
    pinned EvidenceFile, SourceRef and old EvidenceQuote; the new quote is a
    verbatim substring of its cited locus (the named register cell or PRD
    requirement row); every CSV row round-trips byte-exactly, so only
    EvidenceQuote, LastSeen and Notes of the 19 rows change;
  * after rendering, every ACTIVE EXECUTION row of every Dependencies.csv
    under projects/pec/execution has a verbatim EvidenceQuote (111/111);
  * N1: every replacement anchor occurs exactly once; appended notes land
    after a single trailing newline;
  * the local date equals --act-date, unless --reproduction is given (a
    verifier re-running the recorded act date on a scratch export).

Usage:
  python3 gen_d95.py --repo <REPO_ROOT> --act-date YYYY-MM-DD
      [--option A|P] [--retired-covers] [--check-only] [--reproduction]

Option A (recommended) = N1 including dated notes appended to the SCA-005
Handoff_State.md and RUN_SUMMARY.md, plus N2 and N3.
Option P (narrower) = the same without touching the two SCA-005 snapshot
files; _COORDINATION.md records their superseding pointers instead.
Add-on R (--retired-covers, not recommended by default) also rewrites the "covers" bullet
of the four retired deliverables' _REFERENCES.md (same files, different postimages).
The only varying bytes are the act-date slot {D} (N1 text; N3 LastSeen) and
the one hash of RUN_SUMMARY.md cited in the Handoff_State.md note.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import sys
import time
from pathlib import Path

PEC = "projects/pec"
EX = f"{PEC}/execution"
PRD = f"{PEC}/docs/PRD.md"
DELIVERABLES = f"{EX}/_Decomposition/Deliverables.csv"
LEDGER = f"{EX}/_Decomposition/ScopeLedger.csv"
DECOMP_LATEST = f"{EX}/_Decomposition/_LATEST.md"
SC_LATEST = f"{EX}/_ScopeChange/_LATEST.md"
SCA5 = f"{EX}/_ScopeChange/SCA-005_2026-09-23_2139"
HANDOFF = f"{SCA5}/Handoff_State.md"
RUNSUM = f"{SCA5}/RUN_SUMMARY.md"
COORD = f"{EX}/_Coordination/_COORDINATION.md"

# @@PINNED@@

CTX_OLD = "then by revision 1.4 (`current_basis`, SCA-004 successor).\n"
CTX_NEW = ("then by revision 1.4 (`current_basis`, SCA-004 successor),\n"
           "then by revision 1.5 (`current_basis`, SCA-005 successor).\n")
CTX_DONE_RE = re.compile(r"revision 1\.5 \(`current_basis`,\s+SCA-005 successor")
REF_PAIRS = [
    ("- `execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.4, accepted `current_basis`; SCA-004 successor)\n",
     "- `execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.5, accepted `current_basis`; SCA-005 successor)\n"),
    ("- `docs/PRD.md` v2.2 (accepted source corpus; see SourceRef column of the ledger)\n",
     "- `docs/PRD.md` v2.3 (accepted source corpus; see SourceRef column of the ledger)\n"),
]

# Optional add-on R (--retired-covers): the four retired deliverables' reference packets stop
# claiming coverage of scope items that revision 1.5 moved OUT (their register cells are blank).
RETIRED_COVERS = {
    "DEL-06-04": "SOW-029", "DEL-07-02": "SOW-035", "DEL-07-04": "SOW-037", "DEL-07-05": "SOW-087",
}
COVERS_OLD = "- `execution/_Decomposition/ScopeLedger.csv` (SOW→PKG→DEL→OBJ ledger; covers {S})\n"
COVERS_NEW = ("- `execution/_Decomposition/ScopeLedger.csv` (SOW→PKG→DEL→OBJ ledger; covers none — "
              "retired under SCA-005, formerly {S})\n")

V31 = ["RegisterSchemaVersion", "DependencyID", "FromPackageID", "FromDeliverableID",
       "FromDeliverableName", "DependencyClass", "AnchorType", "Direction",
       "DependencyType", "TargetType", "TargetPackageID", "TargetDeliverableID",
       "TargetRefID", "TargetName", "TargetLocation", "Statement",
       "EvidenceFile", "SourceRef", "EvidenceQuote", "Explicitness",
       "RequiredMaturity", "ProposedMaturity", "SatisfactionStatus", "Confidence",
       "Origin", "FirstSeen", "LastSeen", "Status", "Notes"]

DCSV, LCSV = "execution/_Decomposition/Deliverables.csv", "execution/_Decomposition/ScopeLedger.csv"
RCN = "PRD.md §9.2 requirement PEC-RCN-002"
Q_DEL0101_CEN = "16 entity types (DL-14's 14 plus WorkGraph and WorkNode) and the schema every derivation package depends on"
Q_DEL0601 = ("Harness-reported session records (kind, engine/model attribution, role, loop/package binding, "
             "declared write scopes), arriving only from an explicitly authorized hooks consumer; "
             "identity/lifecycle are Runtime-owned per application (C13).")
Q_DEL0905 = ("Sessions (when hook-reported) x worktrees x graph-declared activity with heartbeat/scan age "
             "and advisory overlap warnings")
OLD_RCN = "The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser dialect)"
OLD_RCN_TAIL = [
    "",
    ", decision registers and packets",
    ", decision registers and packets, `LOOP_RECEIPTS.md` (per-loop grammar; the D-APP-57 contract where a ledger has adopted it)",
    ", decision registers and packets, `LOOP_RECEIPTS.md` (per-loop grammar; the D-APP-57 contract where a ledger has adopted it), `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`",
    ", decision registers and packets, `LOOP_RECEIPTS.md` (per-loop grammar; the D-APP-57 contract where a ledger has adopted it), `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`, dependency registers",
    ", decision registers and packets, `LOOP_RECEIPTS.md` (per-loop grammar; the D-APP-57 contract where a ledger has adopted it), `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`, dependency registers, workplans/LOOP_INIT",
]

# DependencyID -> (register folder under EX, EvidenceFile, SourceRef, old quote, new quote,
#                  locus (kind, key, column), reason prefix for Notes)
QUOTES = {
    "DEP-03-01-005": ("PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command", DCSV,
                      "Deliverables.csv row DEL-01-01 ContextEnvelopeNotes",
                      "14 entity types and the schema every derivation package depends on", Q_DEL0101_CEN,
                      ("D", "DEL-01-01", "ContextEnvelopeNotes"), "SCA-005 A-12: DEL-01-01 envelope notes name 16 entity types"),
    "DEP-03-01-008": ("PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command", "docs/PRD.md", RCN,
                      OLD_RCN + OLD_RCN_TAIL[0], "at minimum: `_STATUS.md` (declared parser dialect)",
                      ("P", "PEC-RCN-002", None), "SCA-005 A-75: PRD v2.3 PEC-RCN-002 wording"),
    "DEP-03-01-009": ("PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command", "docs/PRD.md", RCN,
                      OLD_RCN + OLD_RCN_TAIL[1], "decision registers and packets (row identity and status only)",
                      ("P", "PEC-RCN-002", None), "SCA-005 A-75: PRD v2.3 PEC-RCN-002 wording"),
    "DEP-03-01-010": ("PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command", "docs/PRD.md", RCN,
                      OLD_RCN + OLD_RCN_TAIL[2],
                      "receipts — `LOOP_RECEIPTS.md` ledgers (per-loop grammar; the `receipt-contract-v2` marker where a "
                      "ledger carries it; live or declared historical per profile) and central "
                      "`execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md`",
                      ("P", "PEC-RCN-002", None), "SCA-005 A-75: PRD v2.3 PEC-RCN-002 wording"),
    "DEP-03-01-011": ("PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command", "docs/PRD.md", RCN,
                      OLD_RCN + OLD_RCN_TAIL[3],
                      "`STATUS.json` / `RUNTIME_SUMMARY.json` as declared historical grammar or current evidence per profile",
                      ("P", "PEC-RCN-002", None), "SCA-005 A-75: PRD v2.3 PEC-RCN-002 wording"),
    "DEP-03-01-012": ("PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command", "docs/PRD.md", RCN,
                      OLD_RCN + OLD_RCN_TAIL[4],
                      "dependency registers (`Dependencies.csv`; `WORK_GRAPH.json` as declared historical grammar)",
                      ("P", "PEC-RCN-002", None), "SCA-005 A-75: PRD v2.3 PEC-RCN-002 wording"),
    "DEP-03-01-013": ("PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command", "docs/PRD.md", RCN,
                      OLD_RCN + OLD_RCN_TAIL[5],
                      "`LOOP_INIT.md` loop identity, entrypoint and procedure SHA only (workplans as declared historical grammar)",
                      ("P", "PEC-RCN-002", None), "SCA-005 A-75: PRD v2.3 PEC-RCN-002 wording"),
    "DEP-05-01-004": ("PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-01_Gate_precondition_evaluators_Explain_shaped", DCSV,
                      "Deliverables.csv row DEL-01-01 (ContextEnvelopeNotes)",
                      "14 entity types and the schema every derivation package depends on", Q_DEL0101_CEN,
                      ("D", "DEL-01-01", "ContextEnvelopeNotes"), "SCA-005 A-12: DEL-01-01 envelope notes name 16 entity types"),
    "DEP-05-02-003": ("PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-02_Cross_loop_decision_slate", DCSV,
                      "Deliverables.csv row DEL-01-01 (ContextEnvelopeNotes)",
                      "14 entity types and the schema every derivation package depends on", Q_DEL0101_CEN,
                      ("D", "DEL-01-01", "ContextEnvelopeNotes"), "SCA-005 A-12: DEL-01-01 envelope notes name 16 entity types"),
    "DEP-06-03-003": ("PKG-06_Presence_Git_Observation/1_Working/DEL-06-03_Session_worktree_scope_correlation", DCSV,
                      "Deliverables.csv row DEL-06-01 (Description)",
                      "Harness-reported session records (kind, engine/model attribution, role, loop/package binding, "
                      "declared write scopes); identity/lifecycle stay daemon-owned.", Q_DEL0601,
                      ("D", "DEL-06-01", "Description"), "SCA-005 A-37: DEL-06-01 description re-expressed"),
    "DEP-08-04-005": ("PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms", "docs/PRD.md",
                      "PRD.md §9.6 requirement PEC-API-002",
                      "Orientation reads shall complete in ≤100 ms at p95 against the current corpus (session-start critical path).",
                      "Orientation reads shall complete in ≤100 ms at p95 against the current corpus (latency-sensitive pull "
                      "path; any session-start use requires a separately adopted consumer duty).",
                      ("P", "PEC-API-002", None), "PRD v2.2 PEC-API-002 wording, D-PEC-68; stale before SCA-005"),
    "DEP-08-05-004": ("PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription", DCSV,
                      "Deliverables.csv row DEL-06-01 Description",
                      "Harness-reported session records (kind, engine/model attribution, role, loop/package binding, "
                      "declared write scopes); identity/lifecycle stay daemon-owned.", Q_DEL0601,
                      ("D", "DEL-06-01", "Description"), "SCA-005 A-37: DEL-06-01 description re-expressed"),
    "DEP-09-05-006": ("PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board", DCSV, "Deliverables.csv row DEL-09-05",
                      "Sessions x worktrees x live hierarchy with heartbeat age and advisory overlap warnings.", Q_DEL0905,
                      ("D", "DEL-09-05", "Description"), "SCA-005 A-38: DEL-09-05 description re-expressed"),
    "DEP-09-05-007": ("PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board", LCSV, "ScopeLedger.csv row SOW-049",
                      "Dashboard — presence board: sessions × worktrees × live hierarchy with heartbeat age and advisory overlap warnings",
                      "Dashboard — presence board: sessions (when hook-reported) × worktrees × graph-declared activity, "
                      "with heartbeat/scan age and advisory overlap warnings",
                      ("L", "SOW-049", "ScopeItemStatement"), "SCA-005 A-33: SOW-049 statement re-expressed"),
    "DEP-09-05-008": ("PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board", DCSV, "Deliverables.csv row DEL-09-05",
                      "Sessions x worktrees x live hierarchy with heartbeat age and advisory overlap warnings.", Q_DEL0905,
                      ("D", "DEL-09-05", "Description"), "SCA-005 A-38: DEL-09-05 description re-expressed"),
    "DEP-10-05-004": ("PKG-10_Validation_Measurement/1_Working/DEL-10-05_Owner_consultation_logging", DCSV,
                      "Deliverables.csv row DEL-10-05 Description column",
                      "Orientation-read and dashboard-consultation logging sufficient to evaluate the P2 exit test",
                      "Owner use or non-use logging sufficient for the P2-B uptake observation and falsification evidence",
                      ("D", "DEL-10-05", "Description"), "SCA-003 revision 1.3: DEL-10-05 description re-expressed; stale before SCA-005"),
    "DEP-10-05-005": ("PKG-10_Validation_Measurement/1_Working/DEL-10-05_Owner_consultation_logging", LCSV,
                      "ScopeLedger.csv row SOW-085",
                      "Log orientation-read and dashboard-consultation activity sufficient to evaluate the §12 P2 exit test",
                      "Log owner use or non-use of PEC orientation and dashboard surfaces sufficient to evaluate the §12 "
                      "P2-B uptake observation and the §11 falsification clause",
                      ("L", "SOW-085", "ScopeItemStatement"), "SCA-003 revision 1.3: SOW-085 statement re-expressed; stale before SCA-005"),
    "DEP-10-10-003": ("PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation", DCSV,
                      "Deliverables.csv row DEL-02-05 (Description column)",
                      "`Dependencies.csv` and `WORK_GRAPH.json` into DependencyEdge.",
                      "`Dependencies.csv`, and `WORK_GRAPH.json` as a declared historical grammar for App/Piping, into DependencyEdge",
                      ("D", "DEL-02-05", "Description"), "SCA-005 A-16: DEL-02-05 description re-expressed"),
    "DEP-10-12-003": ("PKG-10_Validation_Measurement/1_Working/DEL-10-12_Poll_adoption_measurement", LCSV,
                      "ScopeLedger.csv row SOW-004 (ScopeItemStatement; DeliverableIDs names DEL-04-01)",
                      "Serve per-loop orientation: newest applicable receipt, examined-through SHA, gate states, owner "
                      "directions of record, open tranches/candidate briefs, parked lanes each with its unparking owner action",
                      "Serve per-loop orientation: newest applicable receipt over central receipts and ledgers, "
                      "examined-through SHA, gate states from decisions, scope-change state and graph BLOCKED nodes, owner "
                      "directions of record, open tranches/candidate briefs and parked lanes over graph READY/ACTIVE/BLOCKED "
                      "nodes, each parked lane with its unparking owner action",
                      ("L", "SOW-004", "ScopeItemStatement"), "SCA-005 A-02: SOW-004 statement re-sourced"),
}

# ------------------------------------------------------------------ N1 text

DECOMP_LATEST_OLD = """- **Audit:**
  `_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_2026-09-25_1344/`;
  `BLOCKERS` by the method's count rule (2 / 6 / 74). Both blockers are the
  absent DEL-02-08/09 folders, an expected consequence of the owner's
  deferral of Lane A4; excluding expected consequences, 0 blockers / 4
  warnings. The audit folder's own `_LATEST.md` still names the SCA-004
  audit; moving it was not part of this act.
- **Scope-change snapshot:** `_ScopeChange/SCA-005_2026-09-23_2139/`.
- **Derivative state:** `INCOMPLETE`; `DownstreamRerunState = FROZEN`;
  `MetadataAlignmentState = IN_PROGRESS`; `ReadyForNextPhase = NO`. The
  SCA-004 downstream repairs closed on 2026-08-09
  (`_Coordination/PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md`).
  Open SCA-005 work, each separately gated, is listed in the SCA-005
  `Handoff_State.md` and `RUN_SUMMARY.md`: DEL-02-08/09 preparation with
  the dependency rerun (PROJECT_SETUP, own packet), context and reference
  re-pinning, SOW currency, derivative-artifact review, the registry source
  packet, fixtures, TM-PEC-023 disposition, the `projects/pec/AGENTS.md`
  instruction tranche, the D-PEC-90 reliance amendment, a re-audit after the
  DEL-02-08/09 preparation, and (under its own grant) moving the audit
  folder's `_LATEST.md` to the SCA-005 audit.
"""
DECOMP_LATEST_NEW = """- **Audit:**
  `_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/`, which
  the audit folder's `_LATEST.md` names: `WARNINGS`, 0 blockers / 3
  warnings / 70 info, run after PROJECT_SETUP created DEL-02-08/09 and
  applied the dependency rerun under `D-PEC-93`. The three warnings are
  pre-existing (v2 artifacts held outside their deliverable folders). Its
  INFO findings COV-068/069 (context and reference pins), COV-072
  (evidence-quote currency) and COV-073 (stale handoff text) were addressed
  on {D} under `D-PEC-95` without a further audit. The checkpoint-3 audit
  `COV_SCA005_POSTCHANGE_2026-09-25_1344/` is superseded.
- **Scope-change snapshot:** `_ScopeChange/SCA-005_2026-09-23_2139/`.
- **Derivative state:** `INCOMPLETE`; `DownstreamRerunState = IN_PROGRESS`;
  `MetadataAlignmentState = COMPLETE`; `ReadyForNextPhase = NO`. Done under
  their own packets: DEL-02-08/09 preparation with the dependency rerun, the
  re-audit and the audit-pointer move (`D-PEC-93`; closeout
  `_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/HANDOFF_STATE.md`);
  context and reference re-pinning and the evidence-quote refresh
  (`D-PEC-95`). `projects/pec/AGENTS.md` names PRD v2.3 and the D-GOV-43
  Runtime boundary since `D-PEC-94`. Open, each separately gated: SOW
  currency, derivative-artifact review, the registry source packet,
  fixtures and the D-PEC-90 reliance amendment; TM-PEC-023's state is in
  the Task Management register. Undertaking
  `HELP-HUMAN-PEC-20260925-POST-SCA005` plans the open items in
  `_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`.
  The SCA-004 downstream repairs closed on 2026-08-09
  (`_Coordination/PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md`).
"""

SC_LATEST_ROWS = [
    ("| DerivativePackageState | `INCOMPLETE` — Lane B and the deferred A4 remain open |\n",
     "| DerivativePackageState | `INCOMPLETE` — A4 and B3 done under `D-PEC-93`, B1 under `D-PEC-95`; B4–B7 and the D-PEC-90 reliance amendment remain open |\n"),
    ("| DownstreamRerunState | `FROZEN` — no Lane B rerun authorized by checkpoint 3 |\n",
     "| DownstreamRerunState | `IN_PROGRESS` — B1 and B3 applied under their own packets; each other Lane B rerun is separately gated |\n"),
    ("| MetadataAlignmentState | `IN_PROGRESS` — 22 direct context mirrors done; 42 contexts and 64 references await re-pinning |\n",
     "| MetadataAlignmentState | `COMPLETE` — 22 direct context mirrors, the two new deliverables' files, and 42 contexts and 64 references re-pinned to revision 1.5 on {D} (`D-PEC-95`) |\n"),
    ("| AuditState | **`BLOCKED`** by the count rule — `COV_SCA005_POSTCHANGE_2026-09-25_1344`, 2 blockers (both the A4 deferral's expected consequence) / 6 warnings / 74 info; excluding expected consequences 0 blockers / 4 warnings |\n",
     "| AuditState | `WARNINGS` — `COV_SCA005_POSTSETUP_2026-09-25_1606`, 0 blockers / 3 pre-existing warnings / 70 info; its INFO findings COV-068/069/072/073 addressed on {D} under `D-PEC-95` without a further audit |\n"),
]
SC_LATEST_BOUNDARY_OLD = """Checkpoint 3 authorizes no downstream repair. `SCA-005_2026-09-23_2139/Handoff_State.md`
and `RUN_SUMMARY.md` name every open item and owner: DEL-02-08/09 folders
with the dependency rerun (PROJECT_SETUP under its own packet), context and
reference re-pinning, SOW currency, DEL-00-01/00-03 derivative review, the
registry source packet, P1 fixtures, TM-PEC-023 disposition, the D-PEC-90
reliance amendment, and the `projects/pec/AGENTS.md` instruction tranche.
Each is separately gated.
"""
SC_LATEST_BOUNDARY_NEW = """Checkpoint 3 authorized no downstream repair; each downstream item is
separately gated. Done: the DEL-02-08/09 folders with the dependency
rerun, the post-setup re-audit and the audit-pointer move (`D-PEC-93`;
closeout `_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/HANDOFF_STATE.md`),
and context and reference re-pinning with the evidence-quote refresh
(`D-PEC-95`, {D}). `projects/pec/AGENTS.md` names PRD v2.3 and the D-GOV-43
Runtime boundary since `D-PEC-94`. Open: SOW currency, DEL-00-01/00-03
derivative review, the registry source packet, P1 fixtures and the D-PEC-90
reliance amendment; TM-PEC-023's state is in the Task Management register.
Undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005` plans the open items in
`_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`.
"""

COORD_BASIS_OLD = """- Accepted upstream basis: `execution/_Decomposition/SOFTWARE_DECOMP.md`
  revision **1.4** (`current_basis`, SCA-004 successor, accepted
  2026-08-03 under D-PEC-78 O-A; evidence
  `execution/_ScopeChange/SCA-004_2026-08-02_2325/`). Historical:
  revision 1.1 was the basis at this gate's ruling, revision 1.2 was accepted
  through SCA-002, and revision 1.3 through SCA-003; read
  `execution/_Decomposition/_LATEST.md` first, always.
"""
COORD_BASIS_NEW = """- Accepted upstream basis: `execution/_Decomposition/SOFTWARE_DECOMP.md`
  revision **1.5** (`current_basis`, SCA-005 successor, accepted
  2026-09-25 at SCA-005 checkpoint 3 after the checkpoint-2 ruling
  `D-PEC-92`; evidence `execution/_ScopeChange/SCA-005_2026-09-23_2139/`).
  Historical: revision 1.1 was the basis at this gate's ruling, revision 1.2
  was accepted through SCA-002, revision 1.3 through SCA-003, and revision
  1.4 through SCA-004 (2026-08-03, D-PEC-78 O-A); read
  `execution/_Decomposition/_LATEST.md` first, always.
"""
COORD_ITEM14_ANCHOR = """    separate TASK_MANAGEMENT disposition; this item records no row closure.

## Notes (human-owned)
"""
COORD_ITEM14 = """    separate TASK_MANAGEMENT disposition; this item records no row closure.

14. **SCA-005 feed-model rebaseline and downstream currency (2026-09-25):**
    revision **1.5** is accepted `current_basis` and PRD v2.3 is the
    product definition of record (SCA-005 checkpoint 3, after the
    checkpoint-2 ruling `D-PEC-92`). The owner's TM-PEC-023 selections are
    applied in revision 1.5: every IN scope item and active deliverable maps
    to an objective. Four deliverables are retired (DEL-06-04, DEL-07-02,
    DEL-07-04, DEL-07-05) and two added (DEL-02-08, DEL-02-09). `D-PEC-93`
    prepared the two new folders and applied the dependency rerun: 66
    registers, 263 rows, strict validator 0 errors / 0 warnings; 111
    execution edges over 66 nodes, 0 SCCs, 0 bidirectional pairs. Evidence:
    `PROJECT_SETUP_SCA005_A4_B3_2026-09-25/HANDOFF_STATE.md` and the audit
    `execution/_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/`.
    `D-PEC-95` ({D}) re-pinned the remaining 42 contexts and 64 reference
    packets to revision 1.5 and refreshed 19 stale dependency evidence
    quotes. {SNAPSHOT_SENTENCE}
    This item supersedes the present-tense statements of items 12 and 13
    (revision 1.4 as `current_basis`, TM-PEC-023 held for a mapping
    session, and the two-category derivative state). Remaining
    downstream work is planned in
    `WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`. No
    source, lifecycle, release, or reliance act is inferred.

## Notes (human-owned)
"""
SNAPSHOT_SENTENCE = {
    "A": ("The SCA-005 snapshot's `Handoff_State.md` and `RUN_SUMMARY.md` carry\n"
          "    dated post-closure notes; their earlier sections are unchanged."),
    "P": ("The SCA-005 snapshot's `Handoff_State.md` (SHA-256\n"
          "    `a86ae910d0c9ae7bf20a7ebb47de3edb345d1a6067cb1988fc04d5c1d213328a`) and\n"
          "    `RUN_SUMMARY.md` (SHA-256\n"
          "    `e9a0224ec0152bba75c78b84e2c9abe7a5996014eec602b46de4fe3153c1e518`)\n"
          "    stay byte-identical; for current state they are superseded by this\n"
          "    item and the two `_LATEST.md` pointers."),
}
COORD_NOTE_OLD = """  (revision 1.1 at seeding; revision 1.4 is `current_basis` since
  SCA-004, with topology and execution-dependency bytes preserved) and are never a
  substitute for decomposition truth.
"""
COORD_NOTE_NEW = """  (revision 1.1 at seeding; revision 1.5 is `current_basis` since
  SCA-005, whose dependency rerun under `D-PEC-93` retired, refreshed and
  added register rows) and are never a substitute for decomposition truth.
"""

HANDOFF_NOTE = (
    "\nAmendment {D} (post-closure outcome note, `D-PEC-95`; append-only): this note records "
    "later downstream acts and rewrites nothing above; the checkpoint-3 state fields above remain "
    "the record of that acceptance. After checkpoint 3, PROJECT_SETUP ran A4 with B3 under `D-PEC-93` "
    "(PR #914, merge `961ee1054210fbae7ef5b403547e7a397fb18c95`; closeout "
    "`_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/HANDOFF_STATE.md`): the DEL-02-08 and "
    "DEL-02-09 folders exist at `OPEN`; 20 dependency rows were retired, 1 refreshed and 8 added; the "
    "strict register validator reads 0 errors / 0 warnings; the dependency graph has 111 execution "
    "edges and 0 SCCs. The re-audit `COV_SCA005_POSTSETUP_2026-09-25_1606` reads `WARNINGS` "
    "(0 blockers / 3 warnings / 70 info), and `_Evaluation/DecompCoverage/_LATEST.md` names it. On {D}, "
    "under `D-PEC-95`, B1 re-pinned the remaining 42 `_CONTEXT.md` and 64 `_REFERENCES.md` to "
    "revision 1.5, and 19 stale `EvidenceQuote` cells in 10 `Dependencies.csv` registers were "
    "refreshed (that re-audit's COV-072). `projects/pec/AGENTS.md` names PRD v2.3 and the D-GOV-43 "
    "Runtime boundary since `D-PEC-94` (PR #917). State fields now: `DecompositionTruthState` "
    "`COMPLETE`; `DerivativePackageState` `INCOMPLETE`; `ContentRemediationState` `NOT_REQUIRED`; "
    "`DownstreamRerunState` `IN_PROGRESS`; `MetadataAlignmentState` `COMPLETE`; `AuditState` "
    "`WARNINGS`; `ReadyForNextPhase` `NO`; closure verdict `CLOSED_FOR_SCOPE_CHANGE_ONLY` (unchanged). "
    "Open, each separately gated: B4–B7 and the D-PEC-90 reliance amendment; TM-PEC-023's state "
    "is in the Task Management register. `RUN_SUMMARY.md` gains a dated section with the same facts "
    "and now hashes `{RUNSUM_POST}`.\n")

RUNSUM_SECTION = """
## Post-closure outcome ({D}, `D-PEC-95`; append-only)

This section adds later facts. Nothing above is rewritten; the sections above
remain the record of checkpoint 3. Audit IDs below are those of
`COV_SCA005_POSTSETUP_2026-09-25_1606`, not of the checkpoint-3 audit.

| Item | State on {D} | Record |
|---|---|---|
| A4 — DEL-02-08/09 folders | DONE — both `OPEN` | `D-PEC-93`, PR #914; `_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/HANDOFF_STATE.md` |
| B3 — dependency rerun | DONE — 20 rows retired, 1 refreshed, 8 added; 111 execution edges, 0 SCCs; strict validator 0 / 0 | same |
| Re-audit after A4 and B3 | DONE — `WARNINGS`, 0 blockers / 3 warnings / 70 info; `_Evaluation/DecompCoverage/_LATEST.md` names it | same |
| B1 — re-pin 42 `_CONTEXT.md` and 64 `_REFERENCES.md` | DONE | `D-PEC-95` |
| Evidence-quote currency, 19 rows in 10 registers (COV-072) | DONE — every ACTIVE execution quote is verbatim in its cited file | `D-PEC-95` |
| B4–B7 | OPEN — each separately gated | undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005` work graph |
| B8 — D-PEC-90 reliance amendment | OPEN — next PEC scope change | same |
| B8 — `projects/pec/AGENTS.md` L28/L170 and Shared Runtime Boundary | DONE — PRD v2.3 and the D-GOV-43 Runtime boundary | `D-PEC-94`, PR #917 |
| B8 — TM-PEC-023 | see the Task Management register | task-management |

State fields now: `DecompositionTruthState` `COMPLETE`; `DerivativePackageState` `INCOMPLETE`; `ContentRemediationState` `NOT_REQUIRED`; `DownstreamRerunState` `IN_PROGRESS`; `MetadataAlignmentState` `COMPLETE`; `AuditState` `WARNINGS`; `ReadyForNextPhase` `NO`; closure verdict `CLOSED_FOR_SCOPE_CHANGE_ONLY` (unchanged).
"""


class Fail(Exception):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def replace_once(text: str, old: str, new: str, where: str) -> str:
    n = text.count(old)
    if n != 1:
        raise Fail(f"anchor count {n} != 1 in {where}: {old[:80]!r}")
    return text.replace(old, new)


def append_note(text: str, note: str, where: str) -> str:
    if not text.endswith("\n") or text.endswith("\n\n"):
        raise Fail(f"{where}: does not end with exactly one newline")
    return text + note


def csv_line(values: list[str]) -> str:
    out = io.StringIO()
    csv.writer(out, lineterminator="\r\n").writerow(values)
    return out.getvalue()


def split_register(raw: bytes, where: str) -> tuple[str, list[str]]:
    text = raw.decode("utf-8")
    lines = text.split("\r\n")
    if lines[-1] != "" or any("\n" in ln for ln in lines):
        raise Fail(f"{where}: not uniformly CRLF-terminated single-line rows")
    lines = lines[:-1]
    if next(csv.reader([lines[0]])) != V31:
        raise Fail(f"{where}: header is not exact v3.1")
    return lines[0], lines[1:]


def locus_text(kind, key, col, prd_text, dels, ledger) -> str:
    if kind == "P":
        rows = [ln for ln in prd_text.splitlines() if ln.startswith(f"| {key} |")]
        if len(rows) != 1:
            raise Fail(f"PRD requirement row {key} found {len(rows)} times")
        return rows[0]
    if kind == "D":
        return dels[key][col]
    if kind == "L":
        return ledger[key][col]
    raise Fail(f"unknown locus kind {kind}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    ap.add_argument("--act-date", required=True)
    ap.add_argument("--option", choices=["A", "P"], default="A")
    ap.add_argument("--check-only", action="store_true")
    ap.add_argument("--reproduction", action="store_true")
    ap.add_argument("--retired-covers", action="store_true")
    a = ap.parse_args()
    repo, act = a.repo.resolve(), a.act_date
    report: list[tuple[str, str, str, str]] = []
    try:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", act):
            raise Fail("act-date must be YYYY-MM-DD")
        today = time.strftime("%Y-%m-%d")
        if today != act and not a.reproduction:
            raise Fail(f"local date {today} != --act-date {act}; nothing written")
        # 0. preimages (targets and basis)
        for rel, want in PREIMAGES.items():
            got = sha((repo / rel).read_bytes())
            if got != want:
                raise Fail(f"preimage mismatch {rel}: {got} != {want}")
            report.append(("READ", rel, got, ""))
        prd_text = (repo / PRD).read_text(encoding="utf-8")
        with open(repo / DELIVERABLES, newline="", encoding="utf-8") as f:
            dels = {r["DeliverableID"]: r for r in csv.DictReader(f)}
        with open(repo / LEDGER, newline="", encoding="utf-8") as f:
            ledger = {r["ScopeItemID"]: r for r in csv.DictReader(f)}

        writes: dict[str, bytes] = {}
        # 1. N2 population (fail closed on any drift) and re-pin
        work = repo / EX
        all_ctx = sorted(str(p.relative_to(repo)) for p in work.glob("PKG-*/1_Working/DEL-*/_CONTEXT.md"))
        all_ref = sorted(str(p.relative_to(repo)) for p in work.glob("PKG-*/1_Working/DEL-*/_REFERENCES.md"))
        ctext = {p: (repo / p).read_text(encoding="utf-8") for p in all_ctx}
        rtext = {p: (repo / p).read_text(encoding="utf-8") for p in all_ref}
        need_ctx = [p for p in all_ctx if CTX_OLD in ctext[p]]
        need_ref = [p for p in all_ref if REF_PAIRS[0][0] in rtext[p]]
        if (len(all_ctx), len(all_ref)) != (66, 66):
            raise Fail(f"deliverable population {len(all_ctx)} contexts / {len(all_ref)} references, expected 66 / 66")
        for p in all_ctx:  # each context is pending (1.4 tail) or already names revision 1.5, never both or neither
            if (CTX_OLD in ctext[p]) == bool(CTX_DONE_RE.search(ctext[p])):
                raise Fail(f"context provenance is both or neither pending and current: {p}")
        for p in all_ref:
            if (REF_PAIRS[0][0] in rtext[p]) == (REF_PAIRS[0][1] in rtext[p]):
                raise Fail(f"reference packet is both or neither at revision 1.4 and 1.5: {p}")
        if need_ctx != sorted(CTX_PATHS) or need_ref != sorted(REF_PATHS):
            raise Fail(f"re-pin population {len(need_ctx)} / {len(need_ref)} differs from the pinned 42 / 64 lists")
        for p in need_ctx:
            writes[p] = replace_once(ctext[p], CTX_OLD, CTX_NEW, p).encode("utf-8")
        for p in need_ref:
            t = rtext[p]
            for old, new in REF_PAIRS:
                t = replace_once(t, old, new, p)
            if a.retired_covers:
                folder = Path(p).parent.name
                for del_id, sow in RETIRED_COVERS.items():
                    if folder.startswith(del_id + "_"):
                        if dels[del_id]["CoversScopeItems"] or ledger[sow]["InOutStatus"] != "OUT":
                            raise Fail(f"{del_id}/{sow}: register no longer shows the retirement")
                        t = replace_once(t, COVERS_OLD.replace("{S}", sow), COVERS_NEW.replace("{S}", sow), p)
            writes[p] = t.encode("utf-8")

        # 2. N3 quote refresh
        by_reg: dict[str, dict[str, tuple]] = {}
        for dep, spec in QUOTES.items():
            by_reg.setdefault(f"{EX}/{spec[0]}/Dependencies.csv", {})[dep] = spec
        if sorted(by_reg) != sorted(REG_PATHS):
            raise Fail("register set differs from the pinned 10")
        for reg, specs in sorted(by_reg.items()):
            header, lines = split_register((repo / reg).read_bytes(), reg)
            out, seen = [header + "\r\n"], set()
            for ln in lines:
                values = next(csv.reader([ln]))
                if csv_line(values) != ln + "\r\n":
                    raise Fail(f"{reg}: row does not round-trip byte-exactly: {values[1]}")
                dep = values[1]
                if dep not in specs:
                    out.append(ln + "\r\n")
                    continue
                if dep in seen:
                    raise Fail(f"{reg}: duplicate {dep}")
                _, evfile, srcref, old_q, new_q, (kind, key, col), why = specs[dep]
                row = dict(zip(V31, values))
                if (row["DependencyClass"], row["Status"]) != ("EXECUTION", "ACTIVE"):
                    raise Fail(f"{dep}: not ACTIVE EXECUTION")
                if (row["EvidenceFile"], row["SourceRef"], row["EvidenceQuote"]) != (evfile, srcref, old_q):
                    raise Fail(f"{dep}: EvidenceFile/SourceRef/EvidenceQuote differ from the pinned preimage")
                if new_q not in locus_text(kind, key, col, prd_text, dels, ledger):
                    raise Fail(f"{dep}: new quote not verbatim in its locus {kind}:{key}:{col}")
                row["EvidenceQuote"] = new_q
                row["LastSeen"] = act
                row["Notes"] = f"Evidence refreshed under D-PEC-95 ({why}); {row['Notes']}"
                out.append(csv_line([row[k] for k in V31]))
                seen.add(dep)
            if seen != set(specs):
                raise Fail(f"{reg}: rows not found {sorted(set(specs) - seen)}")
            writes[reg] = "".join(out).encode("utf-8")

        # 3. corpus-wide quote currency on the rendered state (ACTIVE EXECUTION rows)
        n_active = n_ok = 0
        for p in sorted(work.glob("PKG-*/1_Working/DEL-*/Dependencies.csv")):
            rel = str(p.relative_to(repo))
            data = writes.get(rel, p.read_bytes()).decode("utf-8")
            for r in csv.DictReader(io.StringIO(data, newline="")):
                if (r["DependencyClass"], r["Status"]) != ("EXECUTION", "ACTIVE"):
                    continue
                n_active += 1
                ev = repo / PEC / r["EvidenceFile"]
                if ev.is_file() and r["EvidenceQuote"] in ev.read_text(encoding="utf-8"):
                    n_ok += 1
                else:
                    raise Fail(f"quote not verbatim after rendering: {r['DependencyID']} in {r['EvidenceFile']}")
        report.append(("CHECK", "active_execution_quotes_verbatim", str(n_ok), str(n_active)))

        # 4. N1 records currency
        t = (repo / DECOMP_LATEST).read_text(encoding="utf-8")
        writes[DECOMP_LATEST] = replace_once(t, DECOMP_LATEST_OLD, DECOMP_LATEST_NEW.replace("{D}", act),
                                             DECOMP_LATEST).encode("utf-8")
        t = (repo / SC_LATEST).read_text(encoding="utf-8")
        for old, new in SC_LATEST_ROWS:
            t = replace_once(t, old, new.replace("{D}", act), SC_LATEST)
        t = replace_once(t, SC_LATEST_BOUNDARY_OLD, SC_LATEST_BOUNDARY_NEW.replace("{D}", act), SC_LATEST)
        writes[SC_LATEST] = t.encode("utf-8")
        t = (repo / COORD).read_text(encoding="utf-8")
        t = replace_once(t, COORD_BASIS_OLD, COORD_BASIS_NEW, COORD)
        t = replace_once(t, COORD_ITEM14_ANCHOR,
                         COORD_ITEM14.replace("{D}", act).replace("{SNAPSHOT_SENTENCE}", SNAPSHOT_SENTENCE[a.option]),
                         COORD)
        t = replace_once(t, COORD_NOTE_OLD, COORD_NOTE_NEW, COORD)
        writes[COORD] = t.encode("utf-8")
        if a.option == "A":
            rs = append_note((repo / RUNSUM).read_text(encoding="utf-8"), RUNSUM_SECTION.replace("{D}", act), RUNSUM)
            writes[RUNSUM] = rs.encode("utf-8")
            note = HANDOFF_NOTE.replace("{D}", act).replace("{RUNSUM_POST}", sha(writes[RUNSUM]))
            writes[HANDOFF] = append_note((repo / HANDOFF).read_text(encoding="utf-8"), note, HANDOFF).encode("utf-8")

        expected = set(CTX_PATHS) | set(REF_PATHS) | set(REG_PATHS) | {DECOMP_LATEST, SC_LATEST, COORD}
        if a.option == "A":
            expected |= {HANDOFF, RUNSUM}
        if set(writes) != expected:
            raise Fail(f"write set differs from the grant: {sorted(set(writes) ^ expected)[:5]}")
        for rel in writes:
            if rel not in PREIMAGES:
                raise Fail(f"write target without a pinned preimage: {rel}")

        # 5. write (all postimages computed and checked above)
        agg_pre, agg_post = hashlib.sha256(), hashlib.sha256()
        for rel in sorted(writes):
            pre = (repo / rel).read_bytes()
            agg_pre.update(pre)
            agg_post.update(writes[rel])
            if not a.check_only:
                (repo / rel).write_bytes(writes[rel])
            report.append(("WRITE" if not a.check_only else "RENDER", rel, sha(pre), sha(writes[rel])))
        paths = "".join(r + "\n" for r in sorted(writes)).encode("utf-8")
        tag = a.option + ("+R" if a.retired_covers else "")
        report.append(("AGGREGATE", f"option={tag} files={len(writes)}", agg_pre.hexdigest(), agg_post.hexdigest()))
        report.append(("PATHLIST", f"option={tag}", sha(paths), ""))
    except Fail as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    for row in report:
        print("\t".join(row))
    return 0


if __name__ == "__main__":
    sys.exit(main())
