# Brief M1 — PEC development-loop migration tranche (HELPS_HUMANS)

Parent: HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`, node M1. Role: **HELPS_HUMANS** (Type 1), designing an instruction change with the human's direction already given. Model steer: `claude-opus-5-5`, high reasoning, for you and your children.

## Authority

On 2026-09-25 the owner directed:

> You can continue with all the open work you identified. Start with the loop migration, then use the loops for organizing the remaining work into a work graph to help plan and orchestrate the implementation.

`D-PEC-86` §3 I-7 had deferred PEC's loop migration until SCA-005 closed. SCA-005 closed on 2026-09-25 (`_ScopeChange/_LATEST.md`). HELP_HUMAN records this direction as `D-PEC-94` and writes that record and its register row itself. Do not write `_DECISIONS/**`.

Root `AGENTS.md` says instruction changes require their own authorized scope and a tranche manifest, and require notice to the affected loops. This brief is that scope.

## Goal

PEC adopts the shared development-loop method already running in App and Piping:
- evergreen `loop/LOOP_INIT.md`;
- steering-selected undertakings;
- a Git-tracked work graph at `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`;
- implementation through PRs;
- one bounded documentation/governance closeout;
- one central `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md` per undertaking;
- terse deliverable `MEMORY.md` run-index entries;
- conditional Task Management intake.

Preserve PEC's own authority: fences F-PEC-1..4, owner-ruled D-PEC packets for writes outside default surfaces, K-AUTH-1, the reliance-hold control, and D-PEC-88.

## Basis (read; record SHA-256)

- **Root:**
  - `AGENTS.md`, `agents/AGENT_HELPS_HUMANS.md`.
  - `docs/SPEC.md` §9.8 and the loop and MEMORY sections.
  - `docs/governance_harness/_DECISIONS/AMENDMENT_2026-09-22_DEVELOPMENT_LOOP_MEMORY_GRAPH.md`.
  - The tranche manifests under `docs/governance_harness/tranche_manifests/`: `ROOT-DEVELOPMENT-LOOP-MEMORY-20260922.yaml`, `ROOT-APP-PIPING-CENTRAL-RECEIPTS-20260923.yaml`, `ROOT-EVERGREEN-DEVELOPMENT-LOOPS-20260923.yaml`, and PEC's own precedent `PEC-LOOP-CONSOLIDATION-20260905.yaml`.
  - `docs/templates/MEMORY_TEMPLATE.md`.
  - Workflows: `construct-local-work-graph` (with its template), `bounded-reconciliation`, `task-management`.
- **Method instances to mirror:** `projects/chirality-piping/loop/LOOP_INIT.md` and `projects/chirality-app-dev/loop/LOOP_INIT.md`; both `init/dev-loop-init-prompt.md`; the loop, receipt and MEMORY sections of both project `AGENTS.md`; the App/Piping `NOTICE_2026-09-2[23]_*` files.
- **PEC today:**
  - `projects/pec/AGENTS.md`, `loop/LOOP_INIT.md`, `loop/LOOP_RECEIPTS.md` (with `tools/validation/validate_pec_loop_receipts.py`), `init/*.md`, `docs/STATUS.md`, `README.md`, `execution/_Coordination/_COORDINATION.md`.
  - The notices PEC received: `execution/_Coordination/NOTICE_2026-09-2[23]_*`.
  - `D-PEC-80`, including its owner-intent-of-record file and its tranche; `D-PEC-86` (I-7); `D-PEC-88`.
  - The current decomposition pointers `execution/_Decomposition/_LATEST.md` (revision 1.5) and `_ScopeChange/_LATEST.md` (SCA-005), and `docs/PRD.md` v2.3.
  - The Task Management register, if present.

## Produce (one tranche, in your isolated worktree)

Branch `claude/pec-loop-migration` from fresh `origin/main`.

1. **`projects/pec/loop/LOOP_INIT.md`.** Rewrite it as PEC's instance of the shared evergreen method. Keep the same numbered steps as App and Piping. Use PEC project pointers:
   - PRD v2.3, reached through `docs/PRD.md`;
   - the accepted decomposition through `_Decomposition/_LATEST.md` and `_ScopeChange/_LATEST.md`;
   - dependency registers and `_DEPENDENCIES.md`;
   - deliverable folders with `MEMORY.md` and `_STATUS.md`;
   - the decisions register and notices;
   - `software-workflow.json`;
   - the Task Management register.

   Keep it evergreen: no undertaking-specific pointers. Remove the `## Remaining`-driven selection, which the shared method replaces with steering-selected undertakings and work graphs. Do not delete `## Remaining` sections from deliverables.
2. **`projects/pec/init/dev-loop-init-prompt.md`.** Align it with App and Piping.
3. **`projects/pec/AGENTS.md`.**
   - Replace the loop, handoff-ledger and receipt text with the shared method's central-receipt, work-graph and MEMORY responsibilities.
   - Update L28 and L170 from PRD v2.2 to v2.3 (adopted under `D-PEC-92`).
   - Update the Shared Runtime Boundary for `D-GOV-43` A2, which supersedes `D-GOV-20` items 2–4.
   - Keep every fence and authority rule.
   - Say how `D-PEC-88`'s "trace in receipts" works now: it traces in the undertaking's central receipt and graph.

   These AGENTS.md fixes are the pending instruction tranche carried from SCA-005.
4. **`projects/pec/loop/LOOP_RECEIPTS.md`.** Append one final receipt (Receipt 197) that records the adoption and freezes the ledger as historical. It must be append-only and keep `validate_pec_loop_receipts.py` VALID. Check how App and Piping froze theirs and follow suit. State where handoff records go from now on.
5. **`projects/pec/execution/_Coordination/_COORDINATION.md`.** Change only the loop-description lines that become false. Its other stale lines (for example "revision 1.4 current_basis") may be fixed only if they sit in the same present-current section. List what you changed.
6. **Tranche manifest** `docs/governance_harness/tranche_manifests/PEC-DEVELOPMENT-LOOP-ADOPTION-20260925.yaml`. Follow the precedent format: changed paths, checks, authority (D-PEC-94, D-PEC-86 I-7) and rollback.
7. **Non-binding notices of PEC's adoption** to Root `execution/_Coordination/`, `projects/chirality-app-dev/execution/_Coordination/`, `projects/chirality-piping/execution/_Coordination/`, and Runtime if the Root manifests notified Runtime. Follow the precedent wording: grants nothing.
8. **`D-PEC-80`.** Do not rewrite it. State in the manifest and in `AGENTS.md` which of its parts the adoption supersedes: the loop home `projects/pec/loop/` stays; `## Remaining` selection and the per-loop receipt ledger are replaced. `D-PEC-80`'s ruling text needs no edit.

Do not create a work graph yet. HELP_HUMAN constructs the first graph after this merges.

## Checks

- `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` is VALID.
- `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution` returns 0/0.
- `git diff --check` is clean.
- Find and run any instruction, agents or manifest validators under `tools/` that apply, for example anything that checks tranche manifests, AGENTS files or init prompts. Report which you ran and their results.
- Run `tools/practitioner_harness/harness.py self-check` and compare it with the last recorded baseline.
- Run the reliance-hold preflight `projects/pec/execution/_Scripts/pec_reliance_hold.py` with operation `exact-correction-preparation` on the targets.

## Independent verification

Dispatch one fresh read-only verifier (`pec-reviewer`, opus). It checks:
- fidelity to the shared method as App and Piping run it;
- that nothing weakens Root governance or PEC's fences and authority rules;
- evergreen wording;
- that the receipt freeze is append-only and VALID;
- that the manifest is complete and accurate;
- that the notices grant nothing;
- truthfulness against the files.

Loop until nothing is blocking, and save each verdict.

## Write boundary

Write only:
- the files listed in Produce;
- `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/M1_PEC_LOOP_MIGRATION.md` (your return);
- `returns/M1_VERIFIER_VERDICT_NN.md`.

Do not write:
- `_DECISIONS/**`, the HELP_HUMAN `RUN.md`, `docs/STATUS.md` or `README.md` (HELP_HUMAN writes these under D-PEC-88);
- any decomposition file, register, SOW, `_CONTEXT.md`, `_REFERENCES.md`, `Dependencies.csv`, `_STATUS.md` or `MEMORY.md`;
- `v2/**`, `software-workflow.json`, Root `AGENTS.md`, Root `docs/**` (except the new tranche manifest), `workflows/**` or `tools/**`;
- any App or Piping file other than the notices.

Commit your return to the branch before you hand back.

## Publication

Commit, ending every message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Push and open a PR against `main`, ending the body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`. Do not merge.

## Return

- PR URL and head SHA.
- Each changed file with before and after SHA-256.
- The design choices you made, each with a one-line rationale. Flag any choice the owner should confirm.
- Check results.
- Verifier verdicts.
- Containment.
- Anything unresolved.

## Limits

This brief grants none of the following:
- no product, decomposition, lifecycle or SOW change;
- no CHECKING, ISSUED or acceptance, and do not ask the owner about CHECKING;
- no change to the D-PEC-90 reliance text, which is later work.
