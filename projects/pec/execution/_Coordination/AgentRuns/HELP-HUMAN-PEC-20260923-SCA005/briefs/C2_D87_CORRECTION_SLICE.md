# Brief C2 — D-PEC-87 C-A correction slice (WORKING_ITEMS)

Parent: HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`. Role: WORKING_ITEMS (Type 1), owning PKG-01 / DEL-01-03 only. Model steer: `claude-opus-5-5`, high reasoning, for you and your children (D-PEC-86 I-8; D-PEC-87 ruling).

## Purpose

Execute the owner-ruled D-PEC-87 correction slice (C-A) and the L-1a Remaining-row edit, exactly as specified, and return a merge-ready PR with independent verification.

## Accepted basis (read first, in this order)

1. Root `AGENTS.md`; `projects/pec/AGENTS.md`; `agents/AGENT_WORKING_ITEMS.md`.
2. `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-87_RULING_2026-09-24.md` (the ruling) and the proposal it selects, `D-PEC-87_del_01_03_store_guard_correction_proposal_2026-09-24.md` at SHA-256 `ba3d3e64eab7c0488b7973a10e360479d9f34bb075113f821266aea4a4684569`. The proposal's per-repair table, exact R1 rule, finite verification, administrative grant, rollback and limits are your specification. Do not enlarge them.
3. `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/OBLIGATION_TRIAGE_DEL-01-03.md` and the three inquiry reports under DEL-01-03 `_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-00{1,2,3}/REPORT.md`.
4. D-PEC-85 closeout for context only: `projects/pec/execution/_Coordination/D85_PRODUCTION_CLOSEOUT_2026-09-08/` (immutable).
5. Methods: `.agents/skills/software-bounded-implementation/SKILL.md` for the author; `.agents/skills/software-code-review/SKILL.md` for the verifier.

## Preconditions (stop and return if any fails)

- The ruling and its register row are on fetched `origin/main`.
- Fresh preimage verification: the seven granted paths and the unopened `v2/src/pec_v2/adapters/storage/__init__.py` match the proposal's preimage table.
- Reliance-hold preflight passes: `python3 projects/pec/execution/_Scripts/pec_reliance_hold.py --register projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <path> --operation dispatch-for-production` per granted path (repeat with `rely-for-production` before fan-in).

## Write scope (exactly)

Product/config, relative to `projects/pec/`: the seven paths in the ruling, `software-workflow.json` limited to X-1.
Administrative: DEL-01-03 `_run_records/P1_STORE_GUARD_02/**`, DEL-01-03 `MEMORY.md` (append one run entry), and the single L-1a `_STATUS.md` edit (tick REM-001..003 plus one history line citing the three reports `8fcb3ff3…`, `b5d6632d…`, `ca1b7b3e…`, the triage `db335614…` and the ruling). No lifecycle transition; DEL-01-03 stays `IN_PROGRESS`.

Do NOT write: `loop/LOOP_RECEIPTS.md`, the HELP_HUMAN `RUN.md`, `docs/STATUS.md`, `README.md`, `_DECISIONS/**`, `_ScopeChange/**`, any other deliverable, any Root/CI/sister path. HELP_HUMAN owns those shared writes and the receipt.

## Work graph

1. You: preconditions; branch `claude/pec-d87-correction-slice` from fresh `origin/main`; create `P1_STORE_GUARD_02/` with a `RUN.md` graph and `PREIMAGE.md`.
2. One TASK author (`subagent_type: pec-task`, `model: opus`): R1–R8 and X-1 under software-bounded-implementation, extending tests in place where the proposal says so; keep `test_ver_009`'s map equal to the suite. Records commands, exit codes, interpreter path and version.
3. Run all five registered checks from the proposal's finite-verification table, plus `select_affected_checks.py` before/after for X-1; store outputs under `P1_STORE_GUARD_02/checks/`.
4. One fresh read-only TASK verifier (`subagent_type: pec-reviewer`, `model: opus`) under software-code-review. It must confirm substantive admissibility, not only green tests, and re-review the documented PATH row against PRD §7.1/§7.2. Defects return to the author; the verifier does not repair. Repeat until no blocking finding. Save the verdict under `P1_STORE_GUARD_02/`.
5. Containment check (`git diff --name-only origin/main`): only the granted paths plus the run root, `MEMORY.md` and `_STATUS.md`. Whitespace check.
6. L-1a `_STATUS.md` edit and `MEMORY.md` entry.
7. Commit (end messages with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`), push, open the PR against `main` (end the body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`). Do not merge; HELP_HUMAN merges after CI and its own check of the evidence.

## Return

PR URL and head SHA; per-repair status with the proving test IDs; check IDs with exit codes; verifier verdict and cycles; containment output; any discrepancy routed instead of worked around; delegation record (mechanism, parentage, model reported, instruction-asserted limits).

## Limits

No CHECKING, ISSUED or artifact acceptance, and do not ask the owner about CHECKING (the owner reserves it). No SOW, field-class, store location/engine, hosted-CI (X-2) or D-PEC-85 evidence change.
