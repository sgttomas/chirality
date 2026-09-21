# D-APP-128 — PROPOSAL: Whole-corpus post-v3 deliverable concordance activation

> **Epistemic status: agent-authored PROPOSAL packet — not authority (K-AUTH-1; D-GOV-04).**
> Prepared 2026-09-21 by the HELP_HUMAN (Agent 0) session on branch
> `claude/app-concordance-d128-activation`, under the owner direction recorded in
> `execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/OWNER_DIRECTION.md`.
> Nothing here authorizes work; only an owner ruling recorded in a
> `D-APP-128_RULING_*.md` record does. The recommendation is non-binding. The register
> row lands `AWAITING_RULING`.

## 1. Decision to be ruled

Whether to **activate a whole-corpus deliverable concordance** of the App — the Root
`reconciliation` workflow (R0–R6) — over every live deliverable, now that v3 has shipped
and development is paused pending reconciliation (owner direction of 2026-09-19 in
`AgentRuns/HELP-HUMAN-APP-20260919-LOOP-WORKGRAPH/OWNER_DIRECTION.md`), and under which
pinned method.

The question this run answers differs from D-APP-55's. From about 2026-08-22 the App was
driven by a dependency graph, an evolving owner declaration of "done", and in-session code
judgments, **without reference to the deliverables folders** (owner, 2026-09-21). Agents
still propagated some carrier notes into the deliverables, so the corpus is unevenly
updated, not uniformly stale. The run therefore compares four things per claim:
deliverable text · implementation · *recorded* v3 direction · *unrecorded* judgment
(visible only as "it shipped"). It audits forward (every claim → implemented?) and in
reverse (every implementation surface → which deliverable owns it?). The owner rules at
R4, per discrepancy class, which side changes.

## 2. What this decision blocks

The whole run: R0 freeze and calibration, R1 inventories, R2 package concordance, R3
synthesis, the R4 owner decision gate (a later D-APP row), R5 repair tranches (each
separately gated at R4), and R6 backcheck and closeout. The 54 bootstrap `## Remaining`
items seeded with this packet (§8) carry `(gated: D-APP-128)` and are not selectable until
the ruling flips them.

## 3. Preconditions and live state (verified 2026-09-21 at `main` `620ff6387`)

- **No concordance run is open.** D-APP-55's run closed `CLOSED / PASS` at R6
  (`execution/_Reconciliation/DeliverableConcordance/R6_D55_BACKCHECK_2026-07-12_1903Z/HANDOFF.md`);
  later scoped runs (D-APP-68/69, D-APP-85) are closed evidence.
- **Development is paused** by owner direction pending this reconciliation (2026-09-19).
  No App product lane is in flight. Concurrent activity on `main` is in the piping
  project (e.g. PR 834), outside App and Runtime paths.
- **Corpus:** 11 packages, **54** `1_Working/DEL-*` deliverables (53 `IN_PROGRESS`;
  `DEL-09-07` `OPEN`, 0 claims); each is a single SOW_V1 `ScopeOfWork.md` with file-local
  `### CLM-NNN` claims (1,635 claim headings; 13 SoWs also carry claim-less
  Gate-5 current-contract sections).
- **APP-HOLD-1:** `execution/_Coordination/APP_HOLD_REGISTER.csv` is header-only; the
  dispatch preflight still runs per wave.
- **Open register rows:** D-APP-116, 117, 118 and 119 are `AWAITING_RULING` (§6.4).
- **Source state and the shipped bytes.** The owner directed current `main`. App
  `frontend/package.json` reads 3.0.1 (commit `cf4653526`, "Prepare Chirality v3.0.1
  maintenance release"); no `v3.0.1` tag exists. After `cf4653526`, `main` carries four
  App/Runtime commits: `da95ec194` and `cb08dbe2f` (Runtime application-owned dynamic
  tools), `9ecbdecdf` (MCP V2 compatibility observation), and `ccb95e06a` (a one-line
  frontend export fix). The run pins a `main` SHA as directed; evidence rows that rest
  on those post-release commits are marked as such, so shipped-vs-`main` stays visible.
- **Known input carried as a finding, not fixed:** the 2026-09-19 work graph defers
  "Authority corpus reports pre-existing drift in CONTRACT, SPEC and PRD" to an
  owner-directed reconciliation.

## 4. Options

### Option A — Whole corpus, all 54 deliverables (recommended; owner already indicated)

All of `PKG-00`..`PKG-10`. Activation is not execution order: R0 calibrates on a sample
(§6.5) and R2 proceeds in bounded, capacity-limited package batches.

### Option B — Named package subset(s)

The ruling names the packages; the other bootstrap gates stay unflipped. The costs are
the same as in D-APP-55 §4, and they bite harder here: the reverse pass cannot say that
implementation is unowned when part of the deliverable universe is excluded.

## 5. Pinned method (ruling-record requirement; kernel §6)

The ruling record pins, **at `main` revision `620ff6387b211c774c0de7dabec0a170acdf6017`**
(SHA-256 of each file at that revision):

| Role | Path | SHA-256 |
|---|---|---|
| Shared kernel (Rev 1, RATIFIED) | `docs/DELIVERABLE_CONCORDANCE_METHOD.md` | `abf3e78f…0ef627` |
| Workflow entry | `workflows/reconciliation/WORKFLOW.md` | `75948a77…fa380` |
| Workflow contract | `workflows/reconciliation/resources/contract.md` | `da47475c…4d5` |
| Workflow method | `workflows/reconciliation/resources/method.md` | `d7b5e22a…86d` |
| Workflow execution descriptor | `workflows/reconciliation/execution.json` | `35e108bc…ab2` |
| Project adoption record | `plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md` | `7b8c645d…1b1` |

Full hashes are in the ruling record once transcribed. The adoption record is the one
D-APP-55 pinned; it predates SOW_V1, the Runtime extraction and the workplan retirement.
It is therefore pinned **as amended by this named delta list**. Plan text governs except
where a delta applies. Kernel/plan conflicts remain `AUTHORITY_CONFLICT` and are never
resolved by agent precedence.

- **Δ1 Deliverable format.**
  - Plan references to the four-document kit (`Specification.md`, `Datasheet.md`,
    `Procedure.md`, `Guidance.md`) read as the SOW_V1 `ScopeOfWork.md` plus the live
    deliverable-local files: `_STATUS.md`, `_CONTEXT.md`, `_SEMANTIC*.md`,
    `_REFERENCES.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, `MEMORY.md`,
    `Assessment_*`/`Evidence_*`, and `_run_records/**`.
  - The atomic audit unit is the SoW claim.
  - The claim key is `DEL-xx-yy#CLM-NNN`, because CLM IDs are file-local.
  - Claim-less contract sections (the Gate-5 current-contract blocks) are indexed under
    run-local keys `DEL-xx-yy#SEC-n` and dispositioned like claims, so nothing escapes
    coverage. `OUT-`/`AC-`/`VER-` matrix references are evidence links, not separate rows.
- **Δ2 Execution protocol.** The plan's `loop/WORKPLAN_*.md` references read as the
  owning run's work graph (`loop/LOOP_INIT.md` §4; D-APP-105/106/114).
- **Δ3 Evidence roots.**
  - `frontend/**` and `projects/chirality-runtime/{packages,tests}/**` are
    implementation and verification evidence, both read-only. The Runtime part is the
    owner-accepted MR-6 split for this run.
  - The Runtime execution tree is not read.
  - Gate and lifecycle status for Runtime-owned work comes only from App surfaces.
  - Plan §3 boundary 6 (no cross-project edits) is unchanged.
- **Δ4 Reverse pass.**
  - R1 inventories implementation surfaces from the code, by disjoint code area, as
    capability rows, with no candidate-owner column.
  - Each R2 worker seals its forward rows first and only then answers the capability
    rows as `CLAIMED_BY <claim key>`, `PARTIAL` or `NOT_MINE`.
  - R3 owns the final unmapped set.
  - This refines the plan's §6 unmapped-implementation sweep; the kernel minimum is
    unchanged.
- **Δ5 Ledger schema.**
  - The plan §6 19-column header and the §7 controlled dispositions are the baseline.
  - Extensions are **candidates ruled at the R0 gate**, not in force on activation:
    `ClaimKey`, `DirectionEvidence`, `AuthorityTier` (`LOCAL_DESIGN | PRD |
    GOVERNANCE_INVARIANT`), `CauseTag` (controlled vocabulary), and `MechanicallyUnblocked`.
  - `MechanicallyUnblocked` is the successor name for `SelectableUnderCurrentLoop`, with
    an explicit mapping to the kernel's selectability minimum.
- **Δ6 Run-local conventions.** July's MR-1..MR-11
  (`RUN_D55_…/R2_METHOD_ADDENDUM.md`) enter R0 as **candidate** conventions (owner,
  2026-09-21). None is in force until the R0 gate rules on it.
- **Δ7 Gate transcript.**
  - Candidate replacement for MR-3's per-wave transcript: one transcript per project
    (App frontend, Runtime), taken at the frozen source state.
  - They are produced in a detached scratch worktree outside the repository, so
    install and build output never enters the evidence tree.
  - Workers cite the transcripts and do not run suites.
- **Δ8 Discharged start-gate items.** Plan §3a/§4's lifecycle-semantics precondition and
  one-time rebaseline were discharged for D-APP-55 and are not re-applied. Plan §4
  item 3 (bootstrap items) is this packet's §8.
- **Δ9 Delegation.**
  - Harness-native descendants (D-GOV-35): HELP_HUMAN → one WORKING_ITEMS manager per
    package → TASK workers. TASK does not delegate.
  - At most 16 concurrent agents including HELP_HUMAN. The owner may change the cap
    between sub-batches.
  - The actual model is recorded per dispatch.
  - The plan's July orchestration notes are non-binding.
- **Δ10 Boundary 8 retained.**
  - Agent-instruction and workflow surfaces stay out of repair scope.
  - Findings on the packaged instruction bundle (Root-owned sources) are routed to
    `AGENT_WORKFLOW_OBSERVATIONS.md` and a Root notice, and are not repaired.
- **Δ11 Kernel §5 home 3** (checking-entry profile asset) is out of scope unless
  separately ruled.

## 6. Questions this ruling settles (besides scope)

1. **Bootstrap seeding (kernel §6).** Recommended: follow the kernel. Waiving it would
   need an explicit ruling clause, because the kernel treats seeded items as the
   per-deliverable carrier.
2. **Authority classes for v3 direction sources.**
   - Recommended classification, to be finalized in `RUN_BASIS.md`:
     - **GOVERNING:** `docs/PRD.md`; DIRECTIVE, CONTRACT, SPEC and TYPES; decomposition
       v3_2 and accepted SCAs; `RULED` register rows; D-GOV-43.
     - **CONTEXT:**
       - `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (§3,
         §10);
       - `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`;
       - App and Root v3 ruling records a1–a15 and r1–r18 (self-labelled
         non-governing);
       - SCA-APP-008 (unaccepted; partly superseded);
       - the `APP_V3_*` AgentRuns folders.
   - CONTEXT may explain a divergence and drive clustering. It **never changes a claim's
     Disposition**.
   - `RULED`-but-not-applied rows (e.g. D-APP-104, 107, 121–123, 125, 126) are flagged
     as such.
3. **The v3 "done" declaration.**
   - It is not recorded in one place (owner, 2026-09-21).
   - At R0 one TASK assembles `V3_DONE_DECLARATION_CANDIDATE.md` with every line cited.
     The owner confirms or edits it at the R0 gate.
   - The confirmation is recorded as a register ruling and merged before R2. Until then
     it is CONTEXT.
4. **D-APP-116..119 (AWAITING_RULING).** Recommended: leave them open. Claims touching
   them carry `HumanDecisionNeeded = D-APP-11x` and are held from R5 until ruled. The
   alternative is to rule them before R0.
5. **R0 calibration sample.**
   - Recommended, eight deliverables:
     - DEL-01-01: governance invariants; largest SoW.
     - DEL-02-05: carrier-heavy; shell redesign; credential custody under D-APP-126/127.
     - DEL-03-01: engine port and conformance; the code moved to Runtime.
     - DEL-04-05: Anthropic provider path under a Codex-only engine.
     - DEL-06-04: write/edit surface under the Codex approval policy.
     - DEL-08-04: Type 2 governance bridge; native delegation.
     - DEL-09-07: the only `OPEN` deliverable; zero claims.
     - DEL-10-01: doc-only; July calibration continuity.
   - **DEL-03-01 is audited double-blind by two workers** to measure disposition
     variance.
   - **One reverse-pass code area (`frontend/src/lib/harness/**`)** is also calibrated.
   - One fresh verifier checks the calibration. R0 findings go to the owner before any
     scale-out.
6. **Overlap.** Recommended: the R1 *deterministic* inventories (index scripts, no
   judgment) may run while the R0 gate is pending. The reverse-pass capability rows wait
   for the R0 gate, which fixes their granularity.
7. **Network installs for gate transcripts.** `npm ci` in both projects, which needs
   the network, runs in the scratch worktree only.

## 7. Run mechanics (the pinned method governs)

- **Run folder:**
  `execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_<date>/`.
  - It is immutable and append-only, and bound to the frozen source state.
  - It also holds the briefs, the append-only `RUN_STATE.jsonl`, the `RESUME.md` and the
    run-local scripts.
  - The coordination home is `execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/`,
    holding `WORK_GRAPH.json`, the owner direction and the plan of record.
- **Discovery writes.** R0–R3 write nothing outside those two folders.
- **R4 and R5.**
  - R4 is a separate D-APP row.
  - R5 writes only under its ruling, partitioned by owning deliverable.
  - Structural outcomes (retire, merge or create deliverables) go to `scope-change` as a
    handoff package.
  - Code defects become Remaining items only where the R4 ruling names them. Any code
    change is a separate bounded implementation brief.
- **Program state.**
  - Open/closed run visibility lives on this row's ruling-record cell.
  - No new standing surface is created (F-APP-5).
- **Commit discipline.**
  - HELP_HUMAN is the sole committer.
  - The standing Git authorization applies.
  - Fresh-context review is required on the activation, R0, R3/R4, R5 and R6 PRs.

## 8. Packet-time bootstrap seeding (executed with this packet)

Each of the 54 `_STATUS.md` receives, under `## Remaining`:

```
- Run claim-level concordance per the reconciliation method (source: Root workflows/reconciliation/ and docs/DELIVERABLE_CONCORDANCE_METHOD.md with plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md as amended by the D-APP-128 delta list, at pinned main revision <commit SHA>) (gated: D-APP-128)
```

The literal `<commit SHA>` is supplied at ruling time.

- **Where the item goes:**
  - 51 files: appended to the existing section.
  - `DEL-03-04`: the sole `None.` line is replaced, since that line marks an empty
    section.
  - `DEL-07-03` and `DEL-09-07`: a new `## Remaining` section is added before
    `## History`, following the July precedent.
- **History line.** Each file gets one non-state-bearing `History` line: "Remaining
  item added: concordance bootstrap seeded at packet time per D-APP-128 packet; no state
  change."
- **Untouched:**
  - no existing Remaining item or suffix;
  - no `Current State`, `Last Updated` or approval SHA;
  - no lifecycle transition.

## 9. Risks and validation implications

- **Volume and variance.** The volume exceeds D-APP-55's, since the reverse findings
  are expected to dominate.
  - Mitigated by cause-clustered R4 packets, each carrying its full claim population.
  - Mitigated by the double-blind calibration pair.
  - Mitigated by independent verification per package.
- **Anchoring toward ALIGNED.** Mitigated by the sealed two-pass worker design (Δ4).
- **Stale input over a multi-session run.**
  - The source state is frozen.
  - The diff is checked at every sub-batch boundary.
  - `STALE_INPUT` triggers a rerun of the affected deliverables only.
- **Session usage limits.**
  - Mitigated by the append-only run state, idempotent briefs and replaceable managers.
  - HELP_HUMAN drains, and does not launch, when usage is low.
- **Checks.**
  - This packet's tranche changes `execution/**` only.
  - Registered checks: `harness-pytest`, `harness-self-check`, `app-hold-integrity`.
- **Affected files (this tranche):**
  - this packet;
  - the register row;
  - the 54 `_STATUS.md` seedings;
  - `AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/**`.
- **On ruling:**
  - the ruling record;
  - the register flip;
  - the 54 gate flips and SHA substitutions.

## 10. Recommendation (non-binding)

**Option A**, with §6 items 1, 2, 4, 5, 6 and 7 as recommended and §6.3 as described.

## 11. On-ruling mechanism

An in-session owner ruling suffices, for example: "D-APP-128: Option A; §6 as
recommended", with any riders. HELP_HUMAN then:

1. transcribes the ruling verbatim into `D-APP-128_RULING_<date>.md` with full method
   hashes and the pinned SHA;
2. flips this register row to `RULED`;
3. flips the 54 bootstrap gates and substitutes the pinned SHA;
4. obtains a fresh-context review; and
5. merges to `main` **before dispatching anything**. A branch push is not landing on
   `main`.
