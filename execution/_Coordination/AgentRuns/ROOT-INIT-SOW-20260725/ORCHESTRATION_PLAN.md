# Orchestration Plan — ROOT-INIT-SOW-20260725 (all 45 scopes of work)

Agent 0: `HELP_HUMAN` posture · 2026-07-25 · Basis:
`main@31b8dc94acca50dbaf9a518a23dad8583c8c6c62` · Branch:
`claude/root-init-sow-20260725`

## Authorization

Owner acts of record (in-session, 2026-07-25): the phase was named ahead of
closeout ("let's close out what we can now before proceeding to the
per-deliverable initialization and creation of scopes of work", Receipt 49)
and opened by the owner's planning direction ("Plan out your approach so that
delegation through the Agent 0/1/2 paradigm can execute efficiently over it.
The objective is to compete all scopes of work.") followed by owner approval
of the phase plan with four recorded decisions — one PR for all 45 SOWs; one
closing M2 tranche for state flips; sealed briefs authorize candidate
`AC-*`/`VER-*` creation from accepted inputs only; ResponsibleParty "Ryan
Tufts" assigned in the closing tranche. Full verbatim record:
`execution/_Coordination/WORKPLAN_2026-07-25_root_initialization.md`.
Approval of produced artifacts binds at each human-gated PR merge (K-AUTH-2).

## Work graph (frozen; plan version 1)

Posture: `TERMINAL_FAN_OUT_IN`. Selection authority: owner-approved plan
(HUMAN); intra-package partition by Agent 0 under
`agents/AGENT_WORKING_ITEMS.md` batch discipline.

| Node | Actor | Work | Write targets | Status at freeze |
|---|---|---|---|---|
| W-01 | WORKING_ITEMS (Agent 1, opus-5, isolated worktree) | PKG-01: 8 SOWs, batches 4+4, then fresh verifier | `execution/PKG-01_Product_Definition_Normative_Basis_and_Authority/**` | dispatched at G3-PASS |
| W-02 | WORKING_ITEMS (Agent 1, opus-5, isolated worktree) | PKG-02: 5 SOWs, batch 5, then fresh verifier | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/**` | dispatched at G3-PASS |
| W-03 | WORKING_ITEMS (Agent 1, opus-5, isolated worktree) | PKG-03: 6 SOWs, batches 3+3, then fresh verifier | `execution/PKG-03_Governed_Execution_Structure_and_Root_Containment/**` | dispatched at G3-PASS |
| W-04 | WORKING_ITEMS (Agent 1, opus-5, isolated worktree) | PKG-04: 10 SOWs, batches 5+5, then fresh verifier | `execution/PKG-04_Developmental_Machinery_and_Change_Control/**` | dispatched at G3-PASS |
| W-05 | WORKING_ITEMS (Agent 1, opus-5, isolated worktree) | PKG-05: 8 SOWs, batches 4+4, then fresh verifier | `execution/PKG-05_Evidence_Provenance_and_Audit/**` | dispatched at G3-PASS |
| W-06 | WORKING_ITEMS (Agent 1, opus-5, isolated worktree) | PKG-06: 8 SOWs, batches 4+4, then fresh verifier | `execution/PKG-06_Self_Application_Variants_and_Release/**` | dispatched at G3-PASS |
| A0 | HELP_HUMAN (Agent 0, this session) | Fan-in: accept/reject each package return; serial integration of six disjoint worktree results; independent re-validation ×45; containment check; PR staging | phase branch (integration owner) | after all W-* return |
| GATE | Owner | PR 1 review and merge (all 45 SOWs) | — | human gate |

No `depends_on`/`serialized_after` edges among W-01..W-06: write targets are
pairwise disjoint by construction (each node confined to its own package
tree), and each executes in an isolated git worktree (M4). A0 is the single
serialized integration owner; no child commits, no child branch/PR work.
Child failure blocks only its own package's members; independent packages
proceed. Partial or invalid returns are not accepted at fan-in.

Dispatch precondition (satisfied before any child launch): G3 dispatch mode
PASS over `briefs/WORKING-PKG-0{1..6}-BRIEF.md` against
`execution/_harness/work_graph.yaml` with all six nodes `active` and
`accepted_basis` re-pinned to the phase basis (M3 between-runs re-basing,
recorded in the workplan).

## Method bindings carried into briefs

- Production: `TASK + scope-of-work` semantics, `MODE=INIT`, one
  deliverable-local sealed member brief per member (frozen template embedded
  in each activation brief). Authors write ONLY
  `{DEL}/ScopeOfWork.md` + `{DEL}/_run_records/TASK_RUN_*.md`.
- Lifecycle neutrality: no child touches `_STATUS.md` or any underscore file;
  all 45 states remain `OPEN` in PR 1. The `OPEN → INITIALIZED` transition is
  the closing tranche's separate deterministic act
  (`tools/scaffolding/write_status.sh`), per SPEC §3.3 after `SOW_V1`
  validation.
- Uniform parameters: `decomposition_basis` =
  `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`;
  `project_scope_refs`/`package_objective_refs` per member from `_CONTEXT.md`
  `## Scope Traceability`, cross-checked against the companion registers.
- Candidate `AC-*`/`VER-*` authorization (owner ruling 3): grounded only in
  the deliverable-register row, `_CONTEXT.md`, the scope-ledger statements of
  the member's covered items, and `docs/PRD_ROOT.md`. `HUMAN_REVIEW: <method>`
  is the honest verification entry where no deterministic check exists.
  Candidates claim no acceptance.
- Verification: `python3 tools/scope_of_work/validate_scope_of_work.py <DEL>`
  must PASS per member — run by the author (reported verbatim), re-run by the
  fresh package verifier (read-only, evidence-only, no repair), re-run by
  Agent 0 at fan-in.

## Runtime-telemetry adaptation (recorded, not silent)

`agents/AGENT_WORKING_ITEMS.md` requires a run-local telemetry ledger for
multi-member batch execution, normally initialized via
`tools/workflow_runtime/runtime_telemetry.py`. In this platform-native run
the managers execute in isolated worktrees and cannot append to a shared
ledger; telemetry is therefore satisfied by (a) per-member TASK run records
inside each deliverable folder and (b) each manager's structured event log
carried in its terminal return, filed verbatim by Agent 0 under
`instances/WORKING-PKG-0N/`. This is an adaptation of the mechanism, not a
waiver of the obligation; the owner reviews it at the PR gate.

## Return filing convention

Children return terminal content in-channel; Agent 0 files each return
verbatim as `returns/W-0N_RETURN_RAW.md` and never edits it (any transient
execution detail such as a machine-local worktree path is reported outside
the return block and is not filed). Acceptance notes, if needed, are separate
`returns/W-0N_RETURN.md` files.

## Fan-in gates (A0)

1. Every member present: 45/45 `ScopeOfWork.md` + 45/45 TASK run records.
2. `validate_scope_of_work.py` exit 0 ×45, run independently by A0.
3. Verifier verdicts accepted per package; every finding dispositioned here.
4. Containment: integrated diff paths ⊆ `execution/PKG-*/**` ∪
   `execution/_Coordination/**` ∪ `execution/_harness/work_graph.yaml`; zero
   underscore-file modifications inside deliverable folders; all 45
   `_STATUS.md` byte-identical to basis.
5. Battery: full verification battery per the workplan before PR staging.

## Stop state

Stops at the PR 1 human gate. Consequential conditions per root `AGENTS.md`
and `LOOP_INIT.md` §6 return to the owner; uncertainty about
consequentiality itself returns to the owner.

## Fan-in record (A0, 2026-07-25, appended at fan-in)

All six package returns ACCEPTED (W-01..W-06, raw returns filed under
`returns/`, never edited). Aggregate: 45/45 `ScopeOfWork.md` present and
independently re-validated by A0 (`PASS format=SOW_V1`, exit 0, 45/45); all
sha256 values match each manager's table; 45/45 `_STATUS.md` remain `OPEN`;
54 TASK run records (45 members + 9 defect-retry/attempt-2 records); zero
machine-absolute paths in package artifacts; containment exact — the
integrated tree adds only member `ScopeOfWork.md` + `_run_records/` content
plus this run record; zero tracked files modified. Defect discipline worked
end to end: 4 members repaired via fresh single-member author retries with
fresh re-verification (DEL-01-08 anchor errors ×2; DEL-05-06 AC-to-method
binding; DEL-04-03 false-absence claim; PKG-06 tautological
self-verifications ×4 + guard-count error + population predicate), and no
attempt-1 run record was modified anywhere.

A0 dispositions of routed findings (owner-facing items consolidated in
Receipt 51):

1. **Worktree basing / uncommitted-brief hazard** (W-01 F-7, W-02 F-8, W-03
   F-1, W-04 F-11, W-05 F-7, W-06 F-9): ACCEPTED with no content effect —
   Phase A was committed at `e0aae7c2f` on the phase branch, but the isolated
   worktrees were provisioned from `main` (`31b8dc94a`), which predates it;
   every manager located and executed the committed brief read-only (or
   fast-forwarded, a non-destructive act) and every package tree is identical
   between the two commits. Integration re-validated all artifacts on the
   phase branch, so no result rests on a stale base. Standing lesson recorded
   for future dispatches: provision child worktrees from the phase branch, or
   carry the sealed brief in-channel.
2. **Upstream register/ledger objective divergences** (W-01 F-5 SOW-010;
   W-03 F-3 SOW-020/SOW-001/SOW-061; W-06 F-5 SOW-069; boundary-item
   visibility W-03 F-10 SOW-103, W-06 F-6 SOW-075): ROUTED TO OWNER as one
   consolidated reconciliation packet on the accepted decomposition's
   companion registers (the registers are the amendment surface). Authors
   uniformly took `_CONTEXT.md`/register as controlling and surfaced the
   divergence in-contract — accepted as the correct K-CONFLICT-1 posture.
3. **PRD §5.2 O-1 instruction-surface enumeration conflict** (W-02 F-1,
   recorded as DEL-02-01 CON-001): already part of the standing owner
   exact-prose correction packet (PRD O-1 stale enumeration; D-13
   supersession mechanics); now also carried in-contract where the membership
   register will settle it. No new action.
4. **Instrument conflicts surfaced, instruction-surface (M2) matters, not
   repaired in this run**: `AGENT_TASK.md` absolute-path run-record fields vs
   the no-machine-absolute-paths rule (all six packages; children uniformly
   chose repo-relative/`{REPO_ROOT}` token form — accepted for this run);
   `validate_id_format.sh` regex rejecting this decomposition's own ID widths
   (W-03 F-4); `tools/REGISTRY.md` line 57 stale argument note (W-02 F-5);
   `validate_scope_of_work.py` open prefix set (W-02 F-6) and inability to
   detect factual falsehoods (W-04 F-7 — noted: A0's 45× re-run provides
   schema assurance; content assurance came from the fresh-verifier stages);
   QA #16 category-vocabulary labeling (W-06 F-7). All ROUTED TO OWNER as
   candidates for a future instruction-surface maintenance tranche.
5. **Child stop-directive deviation** (W-04 F-2): output accepted (verified
   correct three ways); the precedent question — one author stopped on the
   brief's STOP directive, the sibling proceeded from authoritative sources
   and disclosed — ROUTED TO OWNER for visibility. A0 view: the STOP author
   behaved per contract; the deviation was harmless here only because the
   grounding sources agreed.
6. **DEL-06-02 run-record population predicate** (W-06 F-2): carried OPEN —
   owner must rule the predicate before that deliverable's OUT-001 register
   can be produced. Recorded in-contract as CON-002.
7. **HUMAN_REVIEW share** (W-06 F-10 and package-wide): observation for the
   owner — a substantial share of candidate verification routes to named
   human-review methods, honestly reflecting that these are conformance and
   register deliverables over governance prose, and that some scope items
   forbid mechanical discharge.
8. **Provenance-only cosmetics** (W-02 F-7 filename-timestamp drift; W-04
   F-6 two run-record shapes; W-06 F-8; UTC/local mixes): ACCEPTED as
   disclosed; run records immutable once finalized.

Runtime-telemetry adaptation honored as declared: per-member run records +
manager EVENT_LOGs filed within the raw returns.
