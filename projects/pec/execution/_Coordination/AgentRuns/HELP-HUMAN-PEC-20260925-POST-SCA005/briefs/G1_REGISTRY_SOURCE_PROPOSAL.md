# Brief G1 — draft the registry source packet (D-PEC-96) (read-only TASK)

Parent: HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node G1. Role: TASK (Type 2). You do not delegate. Model steer: `claude-opus-5-5`, high reasoning.

## Why

SCA-005 was accepted at checkpoint 2 (`D-PEC-92`) and checkpoint 3. Its `Propagation_Plan.md` §B6 names a later D-PEC packet as the registry source work. That packet covers:
- `v2/config/loops.schema.json` v2, carrying feed-profile declarations;
- `v2/config/loops.json` rows that declare profiles;
- a `RegisteredLoop` port field.

It must name exact paths, rerun VER-001/VER-003, and give rollback. `F-PEC-1` fences `v2/**` until an owner-ruled packet opens it (`projects/pec/AGENTS.md` §Write Scopes And Fences).

The owner directed on 2026-09-25 (`D-PEC-94`): "You can continue with all the open work you identified." Your job is to draft that packet so the owner can rule on it. The number `D-PEC-96` is assigned by this brief.

## Premise to resolve

§B6 and checkpoint-1 question Q8 (a) had PEC's own `pec` row declare the `remaining-loop` profile. That rested on `D-PEC-86` I-7, which deferred PEC's loop migration. PEC has since migrated to the shared development-loop method: `D-PEC-94`, PR #917, evergreen `loop/LOOP_INIT.md`, work graphs, central `AgentRuns/<RunID>/RECEIPT.md`, `## Remaining` no longer selecting work, and `LOOP_RECEIPTS.md` frozen at Receipt 197.

Determine which profile or profiles PEC's own row should now declare under the accepted revision-1.5 feed model. Base this on the accepted SCA-005 records:
- the Q8 wording, including its "migration later as one row change under its own ruling";
- the feed-profile definitions (O-B2, P-β);
- SOW-077/094;
- the DEL-02-08/09 parser scopes.

State whether the change stays within this packet or needs the owner's separate ruling, and present it as an explicit owner question with a recommendation. Do the same for any other registry row whose accepted profile is unclear.

## Basis (read; record SHA-256)

- **Checkout:** `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5`. Do not change it, and do not switch branches. Read everything from `origin/main` (`git fetch` first; report the SHA) using `git show` or `git archive`.
- **SCA-005 records:**
  - `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/`: `Propagation_Plan.md` (§B6, §B7, the derivative table), `Impact_Assessment.md` (Q8, R-05, feed model), `Amendment_Preview.md`;
  - the checkpoint snapshots `checkpoint_snapshots/SCA-005_GROUP-{1,2,3}_*`;
  - the design note `execution/_Coordination/SCA-005_PREP_2026-09-23/FEED_MODEL_V2_DESIGN_NOTE.md`.
- **Decomposition and PRD:**
  - accepted revision 1.5 `_Decomposition/SOFTWARE_DECOMP.md` and registers (SOW-077, SOW-094, DEL-01-06, DEL-02-08, DEL-02-09);
  - `docs/PRD.md` v2.3.
- **DEL-01-06** (`PKG-01_*/1_Working/DEL-01-06_Loop_registry_local_config_default/`):
  - `ScopeOfWork.md` (the accepted revision-1.4 contract, `5fdcfd96…a2fa8`);
  - `_STATUS.md` (`INITIALIZED`, Gate 5 HOLD);
  - `MEMORY.md`, `_CONTEXT.md`, `_REFERENCES.md`.

  Say how a source packet relates to DEL-01-06's Gate 5 HOLD and its SOW currency (graph node S2 puts the DEL-01-06 SOW after G1). A source packet must not imply any lifecycle change.
- **Source and tests:**
  - `v2/config/loops.json` and `v2/config/loops.schema.json`;
  - `v2/src/pec_v2/core/ports/loop_registry.py` and `v2/src/pec_v2/adapters/config/loop_registry.py`;
  - `v2/tests/config/`;
  - `software-workflow.json`, especially the `v2-store-guard` rule;
  - VER-001/VER-003 as they are defined;
  - earlier `v2/**` source packets and rulings under `_DECISIONS/` (for example D-PEC-85, and D-PEC-87 X-1) for format.
- **Decision records:**
  - `D-PEC-94`, `D-PEC-95` (proposal and ruling) and their register rows, which set the precedent format;
  - `D-T0-15`/`D-T0-19` (fences);
  - the reliance-hold control `execution/_Scripts/pec_reliance_hold.py` and `ACTIVE_RELIANCE_HOLDS.csv`;
  - SCA-006 `_ScopeChange/SCA-006_2026-09-25_1912/Impact_Assessment.md` §7.1 (DEL-01-06 NOT_AFFECTED). Confirm nothing in SCA-006 bears on the registry.
- **Instructions:** Root `AGENTS.md`, `projects/pec/AGENTS.md`, `agents/AGENT_TASK.md`, and the skill `.agents/skills/chirality-change/SKILL.md` if relevant.

## Task

Draft `D-PEC-96` in the D-PEC-95 proposal format. It must let the owner rule on one bounded source act with these parts.

1. **Exact change.**
   - The schema v2 bytes: give them in full, or as a byte-exact generation method.
   - The `loops.json` rows, including the migration of existing rows from version 1.
   - The port field.
   - The adapter changes and tests needed.
   - Backward compatibility: say whether version-1 files are accepted, rejected or migrated, justified from the accepted SOWs.
2. **Verification.**
   - VER-001 and VER-003 reruns.
   - The v2 test suite and `v2-store-guard`.
   - Any repository validators that apply.
   - An independent verifier and what it checks.
3. **Options.**
   - A, recommended.
   - Narrower options if they make sense.
   - Amend or defer.
4. **Grant, rollback and limits.**
   - A product grant listing exact paths, with preimage SHA-256 for every existing file touched.
   - An administrative grant covering the run root and records.
   - Rollback with preimages.
   - Limits: no lifecycle change; no DEL-01-06 Gate 5 or SOW change; no PRD or decomposition change; no CHECKING, ISSUED or acceptance. CHECKING is not an owner gate here.
5. **Owner questions,** including the premise above.

**Prototype.**
- Apply option A to a scratch copy exported with `git archive` into your own `mktemp -d` directory. Never apply it to the checkout.
- Run the v2 tests and checks there, and report exit codes and counts.
- Run `pec_reliance_hold.py` with operation `exact-correction-preparation` on the targets.
- Keep small evidence under the scratchpad folder below, and delete large exports.

## Limits

You are read-only on the repository: no edits in the checkout, no state-changing git, no PRs.

You may write only:
- the draft, to `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/g1/D-PEC-96_DRAFT.md`;
- small evidence, under that `g1/` folder, with a `SHA256SUMS`;
- prototypes, in your own temporary directory.

The draft's status line is `PROPOSAL / AWAITING_RULING`, prepared by TASK under HELP_HUMAN node G1. Do not ask the owner about CHECKING.

## Return

A short return with:
- the draft path and SHA-256;
- the recommended option in a few lines;
- your resolution of the PEC-row premise;
- the exact paths and counts;
- prototype check results;
- the owner questions;
- anything unresolved.
