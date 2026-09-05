#!/usr/bin/env python3
"""Generate the sealed N1 (report-only preview) and N3 (reviewed write)
launch briefs for the thirteen SCA-APP-010 carriers, plus WORK_GRAPH.json.

Deterministic: reads the applied decomposition row for each carrier and the
carrier's current register identities; writes only under this run folder.

Usage (repo root):
  python3 <run>/build_briefs.py --node N1
  python3 <run>/build_briefs.py --node N3 --review-sha <sha256 of REVIEW.md>
"""
import argparse
import hashlib
import json
import os
import re
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), *([".."] * 6)))
RUN_ID = "APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05"
RUN_REL = f"projects/chirality-app-dev/execution/_Coordination/AgentRuns/{RUN_ID}"
RUN = os.path.join(REPO, RUN_REL)
EXEC_REL = "projects/chirality-app-dev/execution"
DECOMP_REL = f"{EXEC_REL}/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
COMPANION_REL = f"{EXEC_REL}/_Decomposition/contract_invariant_coverage_register.csv"
SCA_REL = f"{EXEC_REL}/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA"

BASIS = "d66395d101143df68d956984f7ab93f5027418ec"  # PR #713 merge on main
PIN_COMMIT = "dbd812a52d5ed0cb3ed173f3aaaa68703a914291"
DECOMP_SHA = "c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61"
COMPANION_SHA = "63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca"
POINTER_SHA = "b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0"
ANALYZER_SHA = "e10abf213925df3aae69353c3a8c0dd5cfbb0402957d37c3766a3a9858c97b91"
TODAY = "2026-09-05"

SCC_001 = ["DEL-02-05", "DEL-03-02", "DEL-03-03", "DEL-03-04", "DEL-04-03",
           "DEL-04-05", "DEL-05-02", "DEL-05-03", "DEL-05-05"]

OWNER_DIRECTION = (
    "Merge PR #713.  Then proceed with the next steps.  Continue as the Agent 0 "
    "in your role of `HELP_HUMAN` and orchestrate the work according to your "
    "instructions on agents and delegation."
)

# carrier id -> (folder rel to EXEC_REL, applied row line, DEP write ids)
CARRIERS = {
    "DEL-02-01": ("PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-01_Desktop_Shell_and_Matrix_Navigation", 307, ("DEP-001", "DEP-002")),
    "DEL-02-02": ("PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX", 308, ("DEP-003", "DEP-004")),
    "DEL-02-04": ("PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State", 310, ("DEP-005", "DEP-006")),
    "DEL-02-05": ("PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback", 311, ("DEP-007", "DEP-008")),
    "DEL-03-02": ("PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-02_Thin_TurnEngine_and_Session_Locking", 318, ("DEP-009", "DEP-010")),
    "DEL-04-04": ("PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root", 329, ("DEP-011", "DEP-012")),
    "DEL-05-02": ("PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL", 337, ("DEP-013", "DEP-014")),
    "DEL-06-03": ("PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools", 348, ("DEP-015", "DEP-016")),
    "DEL-07-01": ("PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection", 357, ("DEP-017", "DEP-018")),
    "DEL-07-03": ("PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts", 359, ("DEP-019", "DEP-020")),
    "DEL-08-01": ("PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-01_Instruction_Root_Packaging_and_Agent_Conformance", 368, ("DEP-021", "DEP-022")),
    "DEL-08-03": ("PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch", 370, ("DEP-023", "DEP-024")),
    "DEL-08-04": ("PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge", 371, ("DEP-025", "DEP-026")),
}

# Scope Ledger row lines for the amended rows (applied decomposition)
SOW_LINES = {"SOW-001": 171, "SOW-002": 172, "SOW-004": 174, "SOW-006": 176,
             "SOW-007": 177, "SOW-008": 178, "SOW-010": 180, "SOW-081": 251,
             "SOW-082": 252, "SOW-083": 253, "SOW-084": 254}
AMENDED_SOW = set(SOW_LINES)
OI_008_LINE = 602
DEC_025_LINE = 634
REVERSE_VIEW = "lines 404 to 487 (Scope Ledger to Deliverables reverse view)"


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def load_decomp():
    with open(os.path.join(REPO, DECOMP_REL), "rb") as f:
        raw = f.read()
    assert hashlib.sha256(raw).hexdigest() == DECOMP_SHA, "decomposition identity mismatch"
    return raw.decode("utf-8").split("\n")


def row_fields(lines, n):
    row = lines[n - 1]
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    # | ID | Name | Status | Type | Scope | Artifacts | SOW refs | OBJ refs | Envelope | Notes |
    return {
        "id": cells[0], "name": cells[1], "type": cells[3], "scope": cells[4],
        "artifacts": cells[5], "sow": [s.strip() for s in cells[6].split(",")],
        "obj": [s.strip() for s in cells[7].split(",")], "notes": cells[9],
    }


def n1_brief(cid, folder, line, deps, f, pre):
    pkg = f"PKG-{cid[4:6]}"
    scc = cid in SCC_001
    amended = [s for s in f["sow"] if s in AMENDED_SOW]
    sow_lines = "; ".join(f"{s} line {SOW_LINES[s]}" for s in amended)
    inst = f"N1-TASK-{cid}"
    inst_rel = f"{RUN_REL}/instances/{inst}"
    car_rel = f"{EXEC_REL}/{folder}"
    scc_block = (
        f"- **F1 applies to this carrier: {cid} is a member of SCC-001.** No new "
        "`EXECUTION` row may have both endpoints inside SCC-001. Every existing row "
        "whose `FromDeliverableID` and `TargetDeliverableID` are both SCC-001 members "
        "is preserved byte-identically except a `LastSeen` refresh when still "
        "evidenced; if such a row is no longer evidenced by the live sources, keep it "
        "`ACTIVE` and unchanged and list it under `NEEDS_HUMAN_GRAPH_DECISION` in "
        "`PREVIEW.md` and in the Run Notes. Retirement of an SCC-internal edge is an "
        "SCC change and belongs to the cycle-resolution workflow, not to this pass."
        if scc else
        f"- **F1: {cid} is not a member of SCC-001.** No new `EXECUTION` row may "
        "target an SCC-001 member in a way that would make this carrier a member "
        "(that is, do not add a row to an SCC-001 member if an SCC-001 member already "
        "has an active row back to this carrier); report any such candidate under "
        "`FENCE_F1_CANDIDATES` in `PREVIEW.md` instead of emitting it."
    )
    return f"""# Sealed Brief — {inst} — TASK + dependency-extract (REPORT-ONLY PREVIEW)

- **RunID:** `{RUN_ID}` · **Node:** N1 · **InstanceID:** `{inst}`
- **Parent:** HELP_HUMAN (Agent 0) in an untyped Claude Code session; RequestedBy: HELP_HUMAN for the `TASK_dependency-extract` owner named in SCA-APP-010 `OWNER_ACTION_MATRIX.csv` step 19 and `DOWNSTREAM_HANDOFFS.csv` row 3.
- **Role:** `TASK` (Agent 2) with `TaskSkill: dependency-extract`; a fresh bounded Claude Code subagent; **no delegation**; role not mechanically enforced.
- **Repository root:** `{REPO}` (git worktree, branch `claude/sca-app-010-dependency-closure`). Run every command from this root. Do not `cd` into subfolders in a way that persists.
- **Basis:** `origin/main` `{BASIS}` (PR #713 merge). Stop if `git rev-parse HEAD` is not this commit or a fast-forward descendant that leaves the paths below unchanged.
- **Accepted upstream truth:** applied decomposition `{DECOMP_REL}` SHA-256 `{DECOMP_SHA}` at content commit `{PIN_COMMIT}` (the carrier's `ScopeOfWork.md` front matter pins `@{PIN_COMMIT}`); companion register `{COMPANION_REL}` SHA-256 `{COMPANION_SHA}`; pointer `_ScopeChange/_LATEST.md` SHA-256 `{POINTER_SHA}` naming SCA-APP-010; authority corpus v20, no drift. Recompute the decomposition hash before extracting and stop on a mismatch.
- **Authorization:** SCA-APP-010 `FUTURE_WRITE_SET.csv` rows `{deps[0]}` and `{deps[1]}` (permitted effect: "Write only reviewed report-only-preview rows for the SOW-081..084 and revised SOW-001/002/004/006/007/008/010 relations; retire rather than delete stale rows"; forbidden effect: "Any edge inside the live nine-node SCC; any Root path; any unreviewed write"), triggered by the owner's acceptance of the WORKING_ITEMS alignment (Ryan Tufts, 2026-09-05, verbatim: "{OWNER_DIRECTION}"). This instance is the **report-only preview**. It authorizes no write under the carrier folder.

## Scope

- **Carrier:** `{cid}` — {f["name"]} ({f["type"]}, {pkg}); folder `{car_rel}`.
- **Applied decomposition row:** `{DECOMP_REL}` line {line}. Scope refs on the row: {", ".join(f["sow"])}. Objectives: {", ".join(f["obj"])}. Amended Scope Ledger rows for this carrier: {sow_lines or "none (this carrier's refs were not amended; its row prose was)"}. Also read the Scope Ledger to Deliverables reverse view ({REVERSE_VIEW}), open issue OI-008 (line {OI_008_LINE}), and DEC-025 (line {DEC_025_LINE}).
- **Pre-images (must match before you start):** `Dependencies.csv` SHA-256 `{pre["csv"]}` ({pre["rows"]} data rows); `_DEPENDENCIES.md` SHA-256 `{pre["md"]}`.

## Runtime overrides

```yaml
TaskSkill: dependency-extract
SCOPE: {folder.split("/")[-1]}
RUN_ROOT: {EXEC_REL}
DECOMPOSITION_PATH: {DECOMP_REL}
MODE: UPDATE
STRICTNESS: CONSERVATIVE
CONSUMER_CONTEXT: RECONCILIATION
SOURCE_DOCS: [ScopeOfWork.md, _CONTEXT.md, _STATUS.md]
ANCHOR_DOC: ScopeOfWork.md
EXECUTION_DOC_ORDER: [ScopeOfWork.md, _CONTEXT.md, _STATUS.md]
ApplyEdits: false
ScopePath: {inst_rel}
AllowedWriteTargets:
  - {inst_rel}/
```

`_STATUS.md` is an execution source only for its `## Remaining` section (the seated items' `Depends`, `Write locus`, and gate lines are owner-adopted information-flow signals); its lifecycle, history, and approval fields are not dependency evidence. `_REFERENCES.md` is read to resolve document pointers. Exclude `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `Evidence*`, and `_run_records/**` as sources.

## Read

`AGENTS.md`; `agents/AGENT_TASK.md`; `skills/dependency-extract/SKILL.md`, `BRIEF_SCHEMA.md`, `QA_CHECKS.md`, `TOOL_POLICY.md`; the carrier folder; the decomposition at the lines above; the precedent run record `{EXEC_REL}/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/_run_records/TASK_RUN_2026-08-24_0053.md` and the precedent child return `{EXEC_REL}/_Coordination/AgentRuns/APP_V3_GATE5_2026-08-24/instances/N4-SCOPE-CHANGE-01/children/TASK-DEL-08-04/RETURN.md` and `STATUS.json` (form only). Read other deliverable folders only to confirm that a target deliverable exists and to quote its applied row; never as a source for this carrier's rows. No network.

## Write (only these; nothing else anywhere)

- `{inst_rel}/POSTIMAGE_Dependencies.csv` — the complete proposed post-image of the carrier's `Dependencies.csv` (all rows, v3.1, 29 columns, same column order and quoting convention as the pre-image).
- `{inst_rel}/POSTIMAGE__DEPENDENCIES.md` — the complete proposed post-image of `_DEPENDENCIES.md`.
- `{inst_rel}/PREVIEW.md` — see contract below.
- `{inst_rel}/RETURN.md` and `{inst_rel}/STATUS.json` — the child return in the precedent shapes (`schema: chirality-managed-child-status/v1`, `parentRunId: N1`, `status: PASS | WARNINGS | BLOCKED`, `humanRulingRequired`).
- `{inst_rel}/_run_records/TASK_RUN_{TODAY}_<HHmm>.md` — the TASK run record required by `agents/AGENT_TASK.md` (ScopePath is this instance folder, so the record lives here, not under the carrier).

Do not create or modify any byte under `{car_rel}` or under any other deliverable, decomposition, snapshot, register, `docs/**`, `frontend/**`, `agents/**`, `skills/**`, or Root surface. No state-changing git command. LF line endings, no trailing whitespace, final newline.

## Method

1. Verify the basis and the three upstream identities; verify both pre-image hashes.
2. **Pass 1 (ANCHOR).** From `ScopeOfWork.md` (front matter `decomposition_basis`, `project_scope_refs`, objective refs, and the traceability matrix) and `_CONTEXT.md`: exactly one `IMPLEMENTS_NODE` row (preserve the existing one and its `DependencyID`); one `TRACES_TO_REQUIREMENT` row per scope ref on the applied row and per objective (preserve existing IDs; add rows for refs that are new on the applied row, for example SOW-081 to SOW-084 where this carrier carries them; keep the existing `TargetType=UNKNOWN` convention for objectives with the existing note). An anchor to a scope ref that is no longer on the applied row becomes `Status=RETIRED` with a `Notes` entry citing the applied row line and DEC-025; never delete it.
3. **Pass 2 (EXECUTION).** Extract the information-flow and constraint relations that the applied row's Scope, Artifacts, and Notes columns, the amended Scope Ledger rows, `ScopeOfWork.md` requirements and verification claims, `_CONTEXT.md`, and the seated `## Remaining` items state for this carrier. Ownership statements on the row ("X owns the file contract; Y owns the view") are interface or constraint edges only when this carrier consumes or supplies a named artifact, contract, tool, event, or policy; pure coordination is not an edge. Root-owned semantics (Root DEL-02-09 login home, Root DEL-02-10 `proposal.*` event acceptance, Root DEL-02-11 delegation-policy field, daemon session store, closed `HarnessEvent` schema) are `TargetType=EXTERNAL` with `TargetLocation=TBD` and `SatisfactionStatus=PENDING`; never a Root path (Gate-5 and A12 convention).
4. **Existing rows.** Preserve every `DependencyID` and every `Origin=DECLARED` row. The legacy four-document kit (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) no longer exists in this carrier; a row whose `EvidenceFile` names one of them must be re-evidenced to live bytes (`ScopeOfWork.md#<heading or REQ/CLM id>`, `_CONTEXT.md#<heading>`, or the decomposition `#L<n>`) when the relation is still stated, with `LastSeen={TODAY}`; when the relation is not stated anywhere in the live sources, set `Status=RETIRED`, keep every other field, and explain in `Notes` (`RETIRED {TODAY}: legacy kit retired; relation not restated in SOW_V1 sources`). Never delete a row. `Status=CANDIDATE` is never emitted.
5. **Fences (report, never suppress silently).**
{scc_block}
- **F2 (Root path).** `TargetLocation` may name only paths under `projects/chirality-app-dev/**` or repo-root files this carrier's `_REFERENCES.md` already pins; every Root-owned target is `EXTERNAL` with `TargetLocation=TBD`. List any candidate that would need a Root path under `FENCE_F2_CANDIDATES` and do not emit it.
- **F3 (permitted effect).** New rows are limited to relations introduced or revised by the amended rows named above and by this carrier's applied row prose; do not invent edges from SCC ordering, schedule, or "keep aligned" statements.
6. **Function 5 checks** against the post-image files in this instance folder: `PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py {inst_rel}/POSTIMAGE_Dependencies.csv`; `python3 tools/validation/validate_enum.py <ENUM> <value>` for every enum value you emit or change; `tools/validation/validate_id_format.sh` (the generic three-digit profile rejects the accepted App two-digit IDs; record that as the known `PROJECT_ID_FORMAT_PROFILE` warning and change no ID); exactly one ACTIVE `IMPLEMENTS_NODE`; every ACTIVE row has `EvidenceFile` and `SourceRef` that resolve to live bytes; `_DEPENDENCIES.md` tables reconciled to the post-image CSV following that file's existing count conventions; `FromDeliverableID={cid}` on every row; unique `DependencyID`s.
7. In `POSTIMAGE__DEPENDENCIES.md`: keep the declared sections and their headings; refresh `## Extracted Dependency Register`, add Run Notes for this run (defaults, paths, warnings, fence results, every `NEEDS_HUMAN_GRAPH_DECISION`), append one `## Run History` row (`{TODAY}`, `UPDATE`, `CONSERVATIVE`, decomposition found at the pinned identity, warnings, ACTIVE count), refresh `## Lifecycle Summary`, and refresh `## Downstream Handoff Notes` for `RECONCILIATION`. Place the new history row under `## Run History` (a prior pass once mis-placed it under `## Lifecycle Summary`).

## PREVIEW.md contract

1. Header: instance, carrier, basis, decomposition identity, pre-image hashes, post-image hashes (of the two `POSTIMAGE_*` files), row census pre and post (total / ACTIVE / RETIRED / ANCHOR / EXECUTION).
2. Row-level diff table over every row of the post-image: `DependencyID | Change (ADDED, RE-EVIDENCED, REFRESHED, RETIRED, UNCHANGED) | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note`. `UNCHANGED` means byte-identical.
3. Fence results: `F1`, `F2`, `F3` each `NONE` or the list; `NEEDS_HUMAN_GRAPH_DECISION` (`none` or the rows); `FENCE_F1_CANDIDATES` / `FENCE_F2_CANDIDATES` (`none` or the list with the evidence you would have cited).
4. Validator outputs verbatim (schema, enum summary, ID-format warning, anchor check).
5. Epistemic notes: FACT / ASSUMPTION / PROPOSAL per new or re-evidenced row where not obvious.
6. Attribution: "Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched."

## Acceptance

`STATUS.json.status` is `PASS` when every check above passes and every fence result is `NONE`; `WARNINGS` when checks pass but a fence candidate or `NEEDS_HUMAN_GRAPH_DECISION` row exists (set `humanRulingRequired: true` in that case); `BLOCKED` when a pre-image, basis, or identity check fails (then write nothing but `RETURN.md`, `STATUS.json`, and the run record). Return the post-image hashes, the row census, the fence results, and the run-record path in `RETURN.md`.
"""


def n3_brief(cid, folder, deps, post, review_sha):
    inst = f"N3-TASK-{cid}"
    inst_rel = f"{RUN_REL}/instances/{inst}"
    n1_rel = f"{RUN_REL}/instances/N1-TASK-{cid}"
    car_rel = f"{EXEC_REL}/{folder}"
    return f"""# Sealed Brief — {inst} — TASK + dependency-extract (REVIEWED WRITE)

- **RunID:** `{RUN_ID}` · **Node:** N3 · **InstanceID:** `{inst}`
- **Parent:** HELP_HUMAN (Agent 0); RequestedBy: HELP_HUMAN for the `TASK_dependency-extract` owner (SCA-APP-010 `OWNER_ACTION_MATRIX.csv` step 19, "then reviewed write").
- **Role:** `TASK` (Agent 2) with `TaskSkill: dependency-extract`, apply mode; a fresh bounded Claude Code subagent; **no delegation**; role not mechanically enforced.
- **Repository root:** `{REPO}`; branch `claude/sca-app-010-dependency-closure`; basis `{BASIS}`. No network; no state-changing git command.
- **Authorization:** `FUTURE_WRITE_SET.csv` rows `{deps[0]}` and `{deps[1]}`; the owner's 2026-09-05 acceptance quoted in `ORCHESTRATION_PLAN.md`; the independent review `REVIEW.md` (SHA-256 `{review_sha}`) PASS for this carrier; the N2-gate disposition in `HANDOFF_STATE.md`.

## What to write, exactly

1. Verify `REVIEW.md` hashes to `{review_sha}` and records `{cid}` as PASS; verify the carrier's live `Dependencies.csv` (SHA-256 `{post["pre_csv"]}`) and `_DEPENDENCIES.md` (SHA-256 `{post["pre_md"]}`) still equal the pre-images; verify the reviewed post-images `{n1_rel}/POSTIMAGE_Dependencies.csv` (SHA-256 `{post["csv"]}`) and `{n1_rel}/POSTIMAGE__DEPENDENCIES.md` (SHA-256 `{post["md"]}`). Stop with `BLOCKED` on any mismatch and write nothing under the carrier.
2. Copy the two reviewed post-images byte-for-byte to `{car_rel}/Dependencies.csv` and `{car_rel}/_DEPENDENCIES.md` (for example `cp`), then prove parity by SHA-256.
3. Run Function 5 in place: `PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py {car_rel}/Dependencies.csv`; enum spot checks with `python3 tools/validation/validate_enum.py`; the parent-anchor count; `git diff --check -- {car_rel}`; `git status --short -- {car_rel}` must list only the two files and your run record.
4. Write the TASK run record `{car_rel}/_run_records/TASK_RUN_{TODAY}_<HHmm>.md` in the exact `agents/AGENT_TASK.md` format (frontmatter fields; body headings `## Requested Tasks`, `## Expected Outputs`, `## Tools Used`, `## Tool Policy Compliance`, `## Write Authorization`, `## Outputs Produced`, `## Missing`, `## Needs Human Ruling`, `## Dependency Notes`, `## Applied Changes`, `## Proposed Changes`), naming: the preview instance and its run record, the review identity, pre and post SHA-256 of both files, the row census, the fence results carried from `PREVIEW.md`, and the attribution "Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (reviewed write), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched". `write-authorization: EXPLICIT_BRIEF_TEXT`.
5. Write `{inst_rel}/RETURN.md` and `{inst_rel}/STATUS.json` (`schema: chirality-managed-child-status/v1`, `parentRunId: N3`, `status: PASS | BLOCKED`, `outputs` with both post-image hashes and the run-record hash).

Write nothing else. Do not edit the post-image bytes, `_STATUS.md`, `MEMORY.md`, `ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, or any other path. LF, no trailing whitespace, final newline in the files you author.

Return in your final message: STATUS, both post-write hashes, run-record path, `git status --short` for the carrier.
"""


def n4_brief(regs, ts):
    inst = "N4-AUDIT-DEP-CLOSURE"
    inst_rel = f"{RUN_REL}/instances/{inst}"
    snap = f"{EXEC_REL}/_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_{ts}"
    reg_lines = "\n".join(f"  - {cid} `Dependencies.csv` `{r['csv']}`; `_DEPENDENCIES.md` `{r['md']}`" for cid, r in regs.items())
    return f"""# Sealed Brief — {inst} — AUDIT_DEP_CLOSURE `SCA-APP-010-GATE5-POST-APPLICATION`

- **RunID:** `{RUN_ID}` · **Node:** N4 · **InstanceID:** `{inst}` · **Parent:** HELP_HUMAN (Agent 0) · **RequestedBy:** HELP_HUMAN for SCA-APP-010 `OWNER_ACTION_MATRIX.csv` step 20 / `DOWNSTREAM_HANDOFFS.csv` row 4.
- **Role:** `AUDIT_DEP_CLOSURE` (named dedicated Agent 2, D-GOV-13); a fresh bounded Claude Code subagent; **no delegation**; read-only on every deliverable; role not mechanically enforced.
- **Repository root:** `{REPO}`; branch `claude/sca-app-010-dependency-closure`; basis `{BASIS}` plus the thirteen refreshed registers below (working tree, uncommitted). No network; no state-changing git command.
- **RunLabel:** `SCA-APP-010-GATE5-POST-APPLICATION`. **ExecutionRoot:** `{EXEC_REL}`. **Scope:** `ALL`. **FilterActiveOnly:** `true`. **NormalizeIds:** `true`. **PriorRun:** the pre-extraction baseline `{RUN_REL}/Evidence/baseline_closure/` (registered analyzer at basis, before any register changed) and the accepted SCA-APP-008 post-application audit `{EXEC_REL}/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase5/Audit/SCA-APP-008-GATE5-POST-APPLICATION_2026-08-24/`.
- **Applied decomposition:** `{DECOMP_REL}` SHA-256 `{DECOMP_SHA}`.
- **Refreshed registers to consume and identify explicitly:**
{reg_lines}

## Human override to the generic role (record it in `Decision_Log.md` and the return)

Write the new immutable snapshot under `{snap}/**` (the loop's DepClosure surface named in `loop/LOOP_INIT.md` §9, not the generic `_Evaluation/DepClosure/` root). Do **not** move `{EXEC_REL}/_Reconciliation/DepClosure/_LATEST.md` or any other `_LATEST.md`: in this loop the accepted DepClosure snapshot is an owner act. Do not create `_Evaluation/DepClosure/`. Do not modify any dependency register, deliverable file, decomposition, register, snapshot, `docs/**`, `frontend/**`, or Root surface. Control output: `{inst_rel}/RETURN.md` and `{inst_rel}/STATUS.json` only.

## Required checks

1. Read `AGENTS.md` and `agents/AGENT_AUDIT_DEP_CLOSURE.md` completely; read the SCA-APP-008 post-application `Brief.md`, `Dependency_Closure_Report.md`, and `RUN_SUMMARY.md` for form; read `docs/CYCLE_DRIVEN_RESOLUTION.md` for the SCC posture.
2. Run the registered analyzer exactly once: `PYTHONDONTWRITEBYTECODE=1 python3 tools/coordination/analyze_dep_closure.py {EXEC_REL} --output-dir {snap}/Evidence`. Record its SHA-256 (expected `{ANALYZER_SHA}`) and copy it to `{snap}/analyze_closure.py`.
3. Verify every discovered register against v3.1; resolve every active deliverable endpoint; record missing or invalid registers without guessing.
4. Confirm the thirteen refreshed registers hash to the identities above and consume them explicitly.
5. Compare with the baseline and with the SCA-APP-008 audit: nodes, edges, SCC membership, isolates, bidirectional pairs, hubs. `SCC-001` (nine nodes) must be reported with identical membership unless the live registers changed it; any change, any new SCC, and any new cycle is reported and never linearized. State whether any SCC-internal edge was added or retired by the refresh (expected: none).
6. Confirm the A2-B posture: E-018, E-020, E-032 remain non-gating objective-relative feedback edges; the managed and delegated-harness-native descendant classes each occur once in DEL-08-04 and DEL-08-05 with no Agent-role inference.
7. Confirm Root-owned targets appear only as `EXTERNAL` with `TargetLocation=TBD` in the thirteen refreshed registers (no Root path).
8. Return `PASS`, `WARNINGS`, or `BLOCKER` with evidence; never upgrade a blocking result.

## Required snapshot outputs

`Brief.md` (this brief verbatim plus a normalized summary), `RUN_SUMMARY.md` (`RUN_STATUS = OK|WARNINGS|FAILED_INPUTS` and the closure verdict), `QA_Report.md`, `Decision_Log.md`, `Dependency_Closure_Report.md`, `Dependency_Closure_IssueLog.csv` (`ID,Severity,Check,FromDeliverableID,TargetDeliverableID,DependencyID,Evidence,FixSuggestion`), `closure_summary.json` (copy of `Evidence/closure_summary.json`), `analyze_closure.py`, `Evidence/*` from the analyzer, and `MANIFEST.sha256` over every file in the snapshot. Attribution in `RUN_SUMMARY.md`: "Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as AUDIT_DEP_CLOSURE, dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched". LF, no trailing whitespace, final newline.
"""


def n5_brief(regs, ts):
    inst = "N5-RECONCILIATION"
    inst_rel = f"{RUN_REL}/instances/{inst}"
    snap = f"{EXEC_REL}/_Reconciliation/RECON_SCA_APP_010_POST_ALIGNMENT_{ts}"
    carriers = ", ".join(regs)
    return f"""# Sealed Brief — {inst} — RECONCILIATION read-only checks after the SCA-APP-010 alignment

- **RunID:** `{RUN_ID}` · **Node:** N5 · **InstanceID:** `{inst}` · **Parent:** HELP_HUMAN (Agent 0) · **RequestedBy:** HELP_HUMAN for SCA-APP-010 `DOWNSTREAM_HANDOFFS.csv` row 5 ("No-drift and claim-level concordance checks; versioned reconciliation report; read-only").
- **Role:** bounded ephemeral Agent 2 generalist executing the read-only checks the RECONCILIATION manager (`agents/AGENT_RECONCILIATION.md`) would run before any activation; this is **not** an activated claim-level concordance run (no activation ruling exists) and must say so; a fresh Claude Code subagent; **no delegation**; role not mechanically enforced.
- **Repository root:** `{REPO}`; branch `claude/sca-app-010-dependency-closure`; basis `{BASIS}` plus the thirteen refreshed registers (working tree). No network; no state-changing git command.
- **Write:** only `{snap}/**` (`RUN_BASIS.md`, `RECONCILIATION_REPORT.md`, `CARRIER_CONCORDANCE.csv`, `Evidence/*`, `MANIFEST.sha256`) and `{inst_rel}/RETURN.md`, `{inst_rel}/STATUS.json`. Do not move `{EXEC_REL}/_Reconciliation/_LATEST.md`. No other write anywhere.

## Checks

1. **Authority corpus.** From `projects/chirality-app-dev`: `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status`; record version and drift verbatim into `Evidence/corpus_status.txt`.
2. **Applied pair.** Decomposition `{DECOMP_REL}` SHA-256 must be `{DECOMP_SHA}`; companion `{COMPANION_REL}` must be `{COMPANION_SHA}`; pointer `{EXEC_REL}/_ScopeChange/_LATEST.md` must be `{POINTER_SHA}`; companion structure 83 rows, 83 pins on the decomposition identity (reproduce the Gate-5 table in `{EXEC_REL}/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Evidence/Gate5/RECONCILIATION_REPORT.md`).
3. **Carrier concordance (claim level, read-only)** for {carriers}: for each carrier compare the applied decomposition row (ID, name, scope refs, objectives, envelope) with `ScopeOfWork.md` front matter (`decomposition_basis` pin `@{PIN_COMMIT}`, `project_scope_refs`, objective refs) and its "SCA-APP-010 Gate-5 Current Contract" section, `_CONTEXT.md` identity and scope prose, `_REFERENCES.md` applied identities, the `_STATUS.md` seated items' `Trace` lines, and the refreshed `Dependencies.csv` ANCHOR rows (each scope ref on the row has an ACTIVE `TRACES_TO_REQUIREMENT`; refs not on the row are RETIRED; one `IMPLEMENTS_NODE`). Run `PYTHONDONTWRITEBYTECODE=1 python3 tools/scope_of_work/validate_scope_of_work.py <carrier folder>` for each. Emit one `CARRIER_CONCORDANCE.csv` row per claim: `Carrier,Claim,DecompositionValue,CarrierSurface,CarrierValue,Disposition(ALIGNED|MISMATCH|UNKNOWN),Evidence`.
4. **Lifecycle and fences untouched.** For each carrier, `Current State`, `Checking Approval SHA`, and the F-APP fences are unchanged versus `git show origin/main:<path>`; the only working-tree changes under the carriers are `Dependencies.csv`, `_DEPENDENCIES.md`, and one new `_run_records/TASK_RUN_2026-09-05_*.md`.
5. **Derivative state.** State, with evidence, which SCA-APP-010 derivative packages are now current (carrier working surfaces; carrier dependency registers; closure audit if `{EXEC_REL}/_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_*` exists at read time) and which remain open (SCA-APP-009 closure; TM label if any; owner disposition of `Handoff_State.md`). Claim no closure.

`RECONCILIATION_REPORT.md`: date, basis, result `PASS | FINDINGS`, the tables above, findings list, "Not reconciled here", attribution "Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting for RECONCILIATION's read-only checks, dispatched by HELP_HUMAN; not an activated concordance run; role not mechanically enforced; no descendant launched". LF, no trailing whitespace, final newline.
"""


def n6_brief(regs, ts):
    inst = "N6-AUDIT-DECOMP"
    inst_rel = f"{RUN_REL}/instances/{inst}"
    snap = f"{EXEC_REL}/_Evaluation/DecompCoverage/COV_SCA_APP_010_POST_ALIGNMENT_{ts}"
    prior = f"{EXEC_REL}/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Evidence/Gate5/AUDIT_DECOMP"
    return f"""# Sealed Brief — {inst} — AUDIT_DECOMP fresh full audit after the SCA-APP-010 alignment

- **RunID:** `{RUN_ID}` · **Node:** N6 · **InstanceID:** `{inst}` · **Parent:** HELP_HUMAN (Agent 0) · **RequestedBy:** HELP_HUMAN for SCA-APP-010 `DOWNSTREAM_HANDOFFS.csv` row 6 ("Fresh full audit and pre/post comparison; own versioned surface").
- **Role:** `AUDIT_DECOMP` (named dedicated Agent 2, D-GOV-13); a fresh bounded Claude Code subagent; read-only on deliverables and the decomposition; **no delegation**; role not mechanically enforced.
- **Repository root:** `{REPO}`; branch `claude/sca-app-010-dependency-closure`; basis `{BASIS}` plus the thirteen refreshed registers (working tree). No network; no state-changing git command.
- **Parameters:** `EXECUTION_ROOT={EXEC_REL}`; `DECOMPOSITION_PATH={DECOMP_REL}` (expected SHA-256 `{DECOMP_SHA}`; live and applied, active pointer SCA-APP-010 at `{POINTER_SHA}`); companion `{COMPANION_REL}` (`{COMPANION_SHA}`); `DECOMP_VARIANT=SOFTWARE`; `SCOPE=ALL`; `RUN_LABEL=SCA_APP_010_POST_ALIGNMENT`; `REQUESTED_BY=HELP_HUMAN`; `PRIOR_RUN_LABEL=SCA_APP_010_GATE5_POSTCHANGE` at `{prior}/` (its `coverage_summary.json` is the comparison basis); `EXPECTED_SOURCE_SNAPSHOT` = the SCA-APP-010 snapshot folder; `EXPECTED_HANDOFF_PHASE` = post-Gate-5 downstream alignment (steps 18 to 20 done on this branch; owner disposition pending).
- **Write:** exactly the nine files under `{snap}/` (`Brief.md`, `AUDIT_DECOMP_RETURN.md`, `Decision_Log.md`, `Decomp_Coverage_IssueLog.csv`, `Decomp_Coverage_Matrix.csv`, `Decomp_Coverage_Report.md`, `QA_Report.md`, `RUN_SUMMARY.md`, `coverage_summary.json`) plus `MANIFEST.sha256`, and `{inst_rel}/RETURN.md`, `{inst_rel}/STATUS.json`. Same shapes and columns as the prior run's files. Do **not** move `{EXEC_REL}/_Evaluation/DecompCoverage/_LATEST.md` (record the override in `Decision_Log.md`). No other write.

## Expectations to test (report every deviation)

10 packages / 52 deliverables / 84 scope rows (79 IN / 4 OUT / 1 TBD), envelopes S9 M41 L2 XL0, forward 52/52, reverse 52/54 (PKG-00 and DEL-00-01/02 carried), companion 83 rows / 50 families, OI-008 AffectedScope 4. Versus the Gate-5 post-change audit: the thirteen amended carriers' `_CONTEXT.md` lags (G5-010-COV-004) and the DEL-02-02 name lag (G5-010-COV-005) are expected to be **resolved** by PR #713 (WORKING_ITEMS alignment); confirm or report each. Expect the thirteen refreshed dependency registers to be schema-valid and anchored to the applied rows. Report every new finding and state explicitly whether any new BLOCKER or MAJOR condition exists relative to the Gate-5 post-change audit. Read `agents/AGENT_AUDIT_DECOMP.md` completely and the prior run's nine files for method and form before auditing. Attribution in `RUN_SUMMARY.md`: "Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as AUDIT_DECOMP, dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched". LF, no trailing whitespace, final newline.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--node", choices=["N1", "N3", "N456"], required=True)
    ap.add_argument("--review-sha", default=None)
    ap.add_argument("--ts", default=None, help="snapshot timestamp YYYY-MM-DD_HHMM for N456")
    args = ap.parse_args()
    lines = load_decomp()
    graph_nodes = []
    regs = {}
    for cid, (folder, line, deps) in CARRIERS.items():
        f = row_fields(lines, line)
        assert f["id"] == cid, (cid, f["id"])
        car = os.path.join(REPO, EXEC_REL, folder)
        csv_p = os.path.join(car, "Dependencies.csv")
        md_p = os.path.join(car, "_DEPENDENCIES.md")
        with open(csv_p, "rb") as fh:
            rows = fh.read().count(b"\n") - 1
        pre = {"csv": sha(csv_p), "md": sha(md_p), "rows": rows}
        if args.node == "N1":
            inst = os.path.join(RUN, "instances", f"N1-TASK-{cid}")
            os.makedirs(inst, exist_ok=True)
            with open(os.path.join(inst, "LAUNCH_BRIEF.md"), "w", encoding="utf-8", newline="\n") as fh:
                fh.write(n1_brief(cid, folder, line, deps, f, pre))
            graph_nodes.append({"id": f"N1-TASK-{cid}", "carrier": cid, "row_line": line,
                                "dep_write_ids": list(deps), "scc_001_member": cid in SCC_001,
                                "pre_images": pre})
        elif args.node == "N3":
            assert args.review_sha, "--review-sha required"
            n1 = os.path.join(RUN, "instances", f"N1-TASK-{cid}")
            post = {"pre_csv": pre["csv"], "pre_md": pre["md"],
                    "csv": sha(os.path.join(n1, "POSTIMAGE_Dependencies.csv")),
                    "md": sha(os.path.join(n1, "POSTIMAGE__DEPENDENCIES.md"))}
            inst = os.path.join(RUN, "instances", f"N3-TASK-{cid}")
            os.makedirs(inst, exist_ok=True)
            with open(os.path.join(inst, "LAUNCH_BRIEF.md"), "w", encoding="utf-8", newline="\n") as fh:
                fh.write(n3_brief(cid, folder, deps, post, args.review_sha))
            graph_nodes.append({"id": f"N3-TASK-{cid}", "carrier": cid, "reviewed_post_images": post})
        else:
            regs[cid] = {"csv": pre["csv"], "md": pre["md"], "rows": rows}
    if args.node == "N1":
        with open(os.path.join(RUN, "Evidence", "n1_preimages.json"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump({"basis": BASIS, "decomposition_sha256": DECOMP_SHA, "carriers": graph_nodes}, fh, indent=2)
            fh.write("\n")
        print(f"wrote {len(graph_nodes)} N1 briefs")
    elif args.node == "N3":
        with open(os.path.join(RUN, "Evidence", "n3_reviewed_postimages.json"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump({"review_sha256": args.review_sha, "carriers": graph_nodes}, fh, indent=2)
            fh.write("\n")
        print(f"wrote {len(graph_nodes)} N3 briefs")
    else:
        assert args.ts, "--ts required"
        for inst, fn in (("N4-AUDIT-DEP-CLOSURE", n4_brief), ("N5-RECONCILIATION", n5_brief), ("N6-AUDIT-DECOMP", n6_brief)):
            d = os.path.join(RUN, "instances", inst)
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "LAUNCH_BRIEF.md"), "w", encoding="utf-8", newline="\n") as fh:
                fh.write(fn(regs, args.ts))
        with open(os.path.join(RUN, "Evidence", "n3_postwrite_identities.json"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump({"basis": BASIS, "carriers": regs}, fh, indent=2)
            fh.write("\n")
        print("wrote N4, N5, N6 briefs")


if __name__ == "__main__":
    main()
