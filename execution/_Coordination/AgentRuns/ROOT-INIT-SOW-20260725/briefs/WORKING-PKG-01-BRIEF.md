---
node: PKG-01_Product_Definition_Normative_Basis_and_Authority
write_targets:
  - execution/PKG-01_Product_Definition_Normative_Basis_and_Authority/**
---

# Sealed Brief — W-01: PKG-01_Product_Definition_Normative_Basis_and_Authority scope-of-work initialization (ROOT-INIT-SOW-20260725)

Issued by: `HELP_HUMAN` (Agent 0), 2026-07-25. Executor: WORKING_ITEMS
(Agent 1) posture, `opus-5`, running in an **isolated git worktree** of the
repository (M4). You manage exactly this one package. You delegate authoring
to Agent 2 children; you do not author scopes of work yourself. Terminal
return in-channel; Agent 0 files it. No commits, no branches, no PRs.

## Authorization

Owner-approved phase plan (in-session, 2026-07-25), recorded verbatim in
`execution/_Coordination/WORKPLAN_2026-07-25_root_initialization.md`; run
record `execution/_Coordination/AgentRuns/ROOT-INIT-SOW-20260725/`. G3
dispatch-mode PASS precedes your launch. Owner ruling 3 authorizes each
member run to **create candidate `AC-*`/`VER-*` definitions** grounded ONLY
in: the member's deliverable-register row
(`execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`),
its `_CONTEXT.md`, the scope-ledger statements of its covered items
(`execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv`), and the
adopted PRD (`docs/PRD_ROOT.md`). Nothing else grounds a criterion
(K-INVENT-1). Candidates claim no acceptance; the owner reviews them at the
PR gate. Approval binds at the human-gated PR merge (K-AUTH-2).

## Role and instruction stack (read before dispatching)

`agents/AGENT_WORKING_ITEMS.md` (batch discipline, fan-in duties),
`agents/AGENT_TASK.md` (run-record contract), `skills/scope-of-work/SKILL.md`
+ `BRIEF_SCHEMA.md` + `TOOL_POLICY.md` + `QA_CHECKS.md`,
`docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`, `docs/SPEC.md` §2–§3. Where a
companion doc frames a rule around CONVERT mode, this is an INIT run: the
applicable tool set reduces to `tools/scope_of_work/validate_scope_of_work.py`
(required); conversion/claim-map/parity/finalize tools do not apply (no
source markers exist in INIT output). Verify your worktree with
`git rev-parse --show-toplevel` and work repo-relative inside it.

## Objective

For every member below, produce `1_Working/{DEL}/ScopeOfWork.md` — a
`SOW_V1` production contract that passes
`python3 tools/scope_of_work/validate_scope_of_work.py <member folder>`
(exit 0, `format=SOW_V1`) — plus the member's TASK run record. All 45
lifecycle states remain `OPEN` in this phase; the transition is a later,
separate act. **Do not create or modify `_STATUS.md` or any underscore file
anywhere.**

Members and frozen author batches (ascending; ≤5 per batch):

- **Batch A** (4 members):
  - `DEL-01-01_Genus_Concordance_Closure_and_Standing_Map`
  - `DEL-01-02_Invariant_Catalog_Conformance_Register`
  - `DEL-01-03_Authority_Chain_and_Conflict_Surfacing_Conformance`
  - `DEL-01-04_Human_Authority_and_Three_Judgment_Gate_Model`
- **Batch B** (4 members):
  - `DEL-01-05_File_Native_Authority_Substrate_Conformance`
  - `DEL-01-06_Four_Pillars_and_Professional_Responsibility_Conformance`
  - `DEL-01-07_Jurisdiction_Accountability_and_v1_User_Scope_Register`
  - `DEL-01-08_Non_Goal_Boundary_and_Open_Conflict_Register`

## Method

1. **Author batches.** Dispatch one Agent 2 author session per batch via your
   subagent facility (`opus-5`). Each author processes its members strictly in
   ascending order, under one deliverable-local sealed member brief per
   member (template below, frozen — instantiate per member, do not vary the
   contract). Authors must not delegate further.
2. **Fresh package verifier.** After you accept all author returns, dispatch
   one NEW Agent 2 session (read-only; no writes anywhere) that, for every
   member: re-runs the validator verbatim; checks the INIT-applicable QA
   items (`skills/scope-of-work/QA_CHECKS.md` #4, #8, #9, #16); confirms
   every `OUT-*` traces to declared scope/objective refs and every
   `AC-*`/`VER-*` stays within the grounding sources of the Authorization
   section; confirms no underscore file changed (`git status` in its
   worktree). Evidence-only: the verifier repairs nothing.
3. **Defects.** A defective member returns to a fresh author run for that
   member only (record the retry: member, attempt, failure class,
   disposition). Do not repair author output yourself.
4. **Fallback.** If your environment cannot dispatch subagents, STOP — do not
   author inline. Return `STATUS: FALLBACK_REQUIRED` with your frozen member
   briefs embedded in the return; Agent 0 dispatches them directly.

## Frozen member brief template (instantiate per member)

```text
PURPOSE: INIT — author the SOW_V1 production contract for {DEL-ID}
ScopePath: execution/PKG-01_Product_Definition_Normative_Basis_and_Authority/1_Working/{DEL-FOLDER}
TaskSkill: scope-of-work
AllowedWriteTargets:
  - execution/PKG-01_Product_Definition_Normative_Basis_and_Authority/1_Working/{DEL-FOLDER}/ScopeOfWork.md
  - execution/PKG-01_Product_Definition_Normative_Basis_and_Authority/1_Working/{DEL-FOLDER}/_run_records/**
RuntimeOverrides:
  DELIVERABLE_PATH: (same as ScopePath)
  DECOMPOSITION_BASIS: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
  PROJECT_SCOPE_REFS: (the `Scope items:` list in {DEL}/_CONTEXT.md ## Scope Traceability)
  PACKAGE_OBJECTIVE_REFS: (the `Objectives:` list in the same section)
  MODE: INIT
  SOURCE_STATE: OPEN
ExpectedOutputs: validating SOW_V1 ScopeOfWork.md; TASK run record
  ({DEL}/_run_records/TASK_RUN_{YYYY-MM-DD}_{HHmm}.md, run-status PENDING at
  start, finalized at completion, never modified after); validator output
  verbatim; sha256 of the final ScopeOfWork.md
CustomInstructions: candidate AC-*/VER-* authorized per the Authorization
  grounding sources only; use `HUMAN_REVIEW: <named method>` where no
  deterministic verification exists; STOP and report on any validator
  failure you cannot resolve within your write scope — never touch files
  outside AllowedWriteTargets, never modify underscore files, never claim
  acceptance or lifecycle state.
```

## SOW_V1 exact requirements (validator-binding; do not guess)

- Frontmatter (`---` fenced, line 1): `schema: chirality-deliverable-sow/v1`;
  `deliverable_id` bare (`DEL-01-NN`), `package_id: PKG-01` (bare);
  `decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`;
  `project_scope_refs: [ ... ]`, `package_objective_refs: [ ... ]` as inline
  lists, exactly the `_CONTEXT.md` Scope Traceability values.
- Title `# Scope of Work — {DEL-ID}`, then the six `##` headings in exact
  order, em-dashes literal, no duplicates: `Purpose and Objective
  Traceability`; `Deliverable Definition — Ontology`; `Completion and
  Reliance Basis — Epistemology`; `Production and Verification Method —
  Praxeology`; `Governing Values and Decisions — Axiology`; `Output and
  Evaluation Matrix`.
- Definitions: `- **XXX-NNN** — text` (or `###` heading form), IDs exactly
  3 digits, prefixes `OUT/AC/VER/CLM/REQ/CON/AX` as needed; no `REM-*`
  (belongs to `_STATUS.md`); no duplicate definitions; every referenced local
  ID defined; ≥1 `OUT-*` and ≥1 `AC-*`; no orphans (every defined
  `OUT/AC/VER` appears in the matrix).
- Matrix header row byte-exact:
  `| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |`
  Per `OUT-*` row: objective-refs cell holds space-separated tokens from the
  frontmatter ref lists; acceptance cell ≥1 `AC-NNN`; verification cell ≥1
  `VER-NNN` or exactly `HUMAN_REVIEW: <non-empty method>`.
- Content grounding: `OUT-*` from the register's `AnticipatedArtifacts` and
  `_CONTEXT.md` Anticipated Artifacts (1–4 outputs typical); `CLM-*`/`REQ-*`
  restate covered scope-ledger obligations with their `SOW-*` and SourceRef
  cited in prose; `AC-*` 1–3 concise testable criteria; `VER-*` name real
  repo commands/surfaces where deterministic verification exists. Target
  120–250 lines; no legacy blockquotes, no `sow-source-*` markers, no
  migration-authority line. Where the deliverable's `AnticipatedWriteLocus`
  mentions the instruction surface, the SOW must state that any such act
  requires an independently authorized M2 tranche (it grants none).

## Hard scope limits

Writes confined to `execution/PKG-01_Product_Definition_Normative_Basis_and_Authority/**`, and within it ONLY member
`ScopeOfWork.md` files and `_run_records/` content. Everything else in the
repository is read-only to you and your children. Prohibited: modifying any
underscore file, any other package, `execution/_harness/**`,
`execution/_Coordination/**`, `execution/_Decomposition/**`, the instruction
surface; git commits/branches; machine-absolute paths inside any written
artifact or inside your return block; lifecycle or acceptance claims;
altering `ResponsibleParty` anywhere.

## Package fan-in (yours, before returning)

Accept a member only with: file present; author validator PASS verbatim;
run record present; verifier PASS verbatim; findings dispositioned. Then
compute sha256 per `ScopeOfWork.md` and assemble the terminal return.

## Terminal return (in-channel; Agent 0 files it verbatim)

A single fenced return block containing: `PACKAGE`, `STATUS`
(`COMPLETE`/`FALLBACK_REQUIRED`/`FAILED`), a MEMBERS table
(`DeliverableID | ScopeOfWork.md repo-relative path | sha256 | author
validator line | verifier validator line | batch | run-record filename`), a
VERIFIER section (per-member verdict + QA findings), FINDINGS (numbered
F-1…, each with your disposition or `ROUTED TO AGENT 0`), and EVENT_LOG
(one line per session/batch/retry event: timestamp, actor, event, member,
outcome). After the block, on its own line outside it: `WORKTREE: <absolute
path>` (transient execution detail; not filed).
