# Brief S3 — draft the first Scope of Work contracts for DEL-02-08 and DEL-02-09 as an owner packet (read-only TASK)

Parent: HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S3. Role: TASK (Type 2); you do not delegate. Model steer: `claude-opus-5-5`, high reasoning.

## Why

SCA-005 added two parser deliverables in revision 1.5, and D-PEC-93 created their folders on 2026-09-25:
- DEL-02-08 Work graph parser;
- DEL-02-09 MEMORY run-index parser.

Neither has a `ScopeOfWork.md` yet. The work graph orders S3 after U1 (the D-PEC-95 re-pin, merged) and after SCA-006 checkpoint 1 (accepted). SCA-006 classifies neither deliverable as affected. The owner directed on 2026-09-25 (`D-PEC-94`): "You can continue with all the open work you identified."

`projects/pec/AGENTS.md` fences writes outside PEC's default surfaces behind an owner-ruled D-PEC packet. Your job is to draft that packet, with exact candidate bytes, so the owner can rule on it. The number is `D-PEC-98`.

## Basis (read; record SHA-256)

- **Checkout.** Use `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5`. Do not change it and do not switch branches. Read from `origin/main` (`git fetch` first, and report the SHA) with `git show` or `git archive`.
- **Method.** Use the bundled `scope-of-work` workflow (`workflows/scope-of-work/`), resolved from `workflows/index.json`. Record its source-qualified identity and hashes, and the SOW_V1 transition contract it names. Use the `preparation` skill if the method calls for it.
- **PEC precedent for SOW acts under owner packets.** Find how PEC's earlier SOW initializations and revisions were proposed, ruled and verified; for example, the DEL-01-06 `REV_DEL-01-06_2026-08-04_1113` REVIEW snapshot and its rulings, and the Phase 2.2 SOW initialization records. Follow that form.
- **Deliverable inputs.** Both folders (`_CONTEXT.md`, `_REFERENCES.md`, `_SEMANTIC.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, `_STATUS.md`), and their revision-1.5 rows in `Deliverables.csv`, `ScopeLedger.csv` (SOW-095, SOW-096 and any others they cover) and `SOFTWARE_DECOMP.md`.
- **PRD.** `docs/PRD.md` v2.3, especially §7.1 (WorkGraph / WorkNode, RunRecord, remaining items), the feed-profile text and the parser requirements.
- **SCA-005 records.** The feed-model design note `execution/_Coordination/SCA-005_PREP_2026-09-23/FEED_MODEL_V2_DESIGN_NOTE.md`, SCA-005 `Propagation_Plan.md` §B4 and §B7 (fixture strategy), and Impact_Assessment R-05.
- **Sibling SOWs, for form and interfaces.** DEL-02-03 (receipts-ledger parser), DEL-02-04 (run-evidence JSON parser) and DEL-02-01 (STATUS parser).
- **Registry packet.** `D-PEC-96` revision 3, merged but not yet ruled: `_DECISIONS/D-PEC-96_registry_schema_v2_feed_profiles_proposal_2026-09-25.md`. It defines the feed profiles and surfaces (`shared-dev-loop` and others) that the parsers read. Say how the SOWs depend on it, without presuming the ruling.
- **Shared method surfaces the parsers read.** The shared development loop's work-graph template (`workflows/construct-local-work-graph/resources/work-graph-template.md`), `docs/templates/MEMORY_TEMPLATE.md`, and the real App, Piping and PEC work graphs and `MEMORY.md` files that exist.
- **Recent Root notices** in `execution/_Coordination/NOTICE_2026-09-26_WORKFLOW_WAVE2A_*.md`. The EXECUTION notice changed `construct-local-work-graph`; account for its current form.
- **Instructions.** Root `AGENTS.md`, `projects/pec/AGENTS.md` and `agents/AGENT_TASK.md`.

## Task

Draft `D-PEC-98` in the D-PEC-95 and D-PEC-96 proposal format, so the owner can rule on one bounded act: writing the two `ScopeOfWork.md` files.

1. **Exact candidate bytes.** Write both candidate `ScopeOfWork.md` files under the method's contract.
   - They must be objective-anchored and traced to their scope items and the PRD, with requirements, acceptance criteria and verification.
   - State the fixture classes that SCA-005 §B7 assigns to X1: receipt present, evidence-only, and no AgentRuns record.
   - State the open decisions as TBD or CON items, not assumptions.
2. **Verification.** Run the method's validator or validators, and its independent-verification step as the method defines it. Check the candidates against sibling-SOW conventions and against the revision-1.5 registers.
3. **Lifecycle.** Say exactly what the method does to `_STATUS.md` when a first SOW is written. PEC precedent kept lifecycle changes out of SOW packets unless the owner rules them. If the method requires a transition, present it as an explicit owner question and do not assume it.
4. **Options, grant, rollback and limits.** Give the options, with A recommended. Give the exact paths with preimages (the files are new, so preimages are absent), the administrative run root, rollback, and limits. The limits are: no `v2/**`, PRD, decomposition or register write; no CHECKING, ISSUED or acceptance. CHECKING is not an owner gate.
5. **Owner questions.**

Prototype on a `git archive` export in your own `mktemp -d`. Run `pec_reliance_hold.py` with operation `exact-correction-preparation` on the targets.

## Limits

You are read-only on the repository: no edits in the checkout, no state-changing git and no PRs.

You may write only:
- the draft, to `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/s3/D-PEC-98_DRAFT.md`;
- the candidate files and evidence under that `s3/` folder, with a `SHA256SUMS`;
- prototypes, in your own temporary directory.

The status line is `PROPOSAL / AWAITING_RULING`. Do not ask the owner about CHECKING.

## Return

Return a short report with:
- the draft path and SHA-256;
- the candidate hashes;
- the recommended option;
- the lifecycle answer;
- dependencies on D-PEC-96;
- check results;
- the owner questions;
- anything unresolved.
