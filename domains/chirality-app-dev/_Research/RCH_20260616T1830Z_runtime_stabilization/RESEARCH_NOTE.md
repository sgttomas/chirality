# Research Note - Runtime Stabilization Plan Completion

Status: DERIVATIVE_RESEARCH_PACKET

**Run:** RCH_20260616T1830Z_runtime_stabilization
**Domain:** `domains/chirality-app-dev`
**Source repo:** `projects/chirality-app-dev` (live tree, source of truth)
**Retrieval snapshot:** `domains/chirality-app-dev/_LocalIndexes/snapshots/SRCIDX_20260616T043733Z` (chirality-source-db/v2; 660 artifacts, 20,398 chunks, BAAI/bge-base-en-v1.5 embeddings)
**Consumer:** `projects/chirality-app-dev/plans/PLAN_2026-06-16_runtime_stabilization.md` (completed and accepted as the active governing development queue)

This packet is a derivative research package. It aids discovery and supports the
completed runtime stabilization plan; it does not replace accepted decomposition truth,
governed docs, source, tests, or human rulings. Most current-state claims were verified
directly against the live tree; the retrieval snapshot was used for discovery across the
large corpus (PRD/SPEC/decomposition/atom ledger).

## Question

What is the current landed state of the Chirality desktop harness runtime, what remains,
and how should the draft Runtime Stabilization plan (tranches STAB-00..05) be completed in
detail — current-state matrix, Section 9 validation surface, SDK readiness, session
replay/artifact evidence, deterministic Chirality MCP maturity, governance reconciliation,
and the human rulings each requires?

## Accepted Basis

- Decomposition topology: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
  (10 packages PKG-00..PKG-10, ~51 deliverables DEL-PP-NN; Gates 1-7 PASSED).
- Runtime contract baseline: `frontend/docs/harness/runtime_engine_contract.md`.
- Governance: `docs/PRD.md`, `docs/PLAN.md`, `docs/SPEC.md`, `docs/TYPES.md`,
  `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/VALIDATION_STRATEGY.md`,
  `docs/RELEASE_QUALITY_GATES.md`.
- Decisions D-APP-01..D-APP-10 RULED (`execution/_Coordination/_DECISIONS/_REGISTER.md`);
  scope change `SCA-APP-001`.
- All 53 deliverable `_STATUS.md` files read `Current State: SEMANTIC_READY` (uniform
  2026-05-20 decomposition value).

## Short Answer

The runtime stack is substantially landed with a clean separation between provider-neutral
product contracts (AgentEnginePort, TurnEngine, HarnessEvent, descriptors, permission
overlay, hooks, child-run contract) and the opt-in Claude Agent SDK adapter. Read/write/
Bash tool surfaces, the four read-only Chirality MCP tools, hooks, the R5 executable
subagent bridge, and the context-compaction mirror are all landed and unit/contract-tested.

Genuine gaps and partials that the stabilization program must close:

1. **No Section 9 running-validation artifact** (DEL-09-02). All 13 candidate IDs already
   map to existing deterministic vitest tests; the missing piece is an aggregator script.
2. **agentSdk API-key supply is unwired** (DEL-04-05) — load-bearing: the SDK path cannot
   complete a real turn from a UI-only key. No real (even dev-build) agentSdk turn has
   executed anywhere; all tests mock `query()`.
3. **Packaging `BLOCKED_TBD`** (DEL-09-04) — no `asarUnpack` for the SDK; no
   packaged-subprocess proof.
4. **Mutating Chirality MCP tools are metadata-only** (DEL-07-04/05 MCP half) — but BOTH
   write engines (`lib/lifecycle/transition.ts`, `lib/dependencies/register-writer.ts`)
   are landed and tested, so STAB-04 is bounded MCP exposure + in-handler evidence.
5. **PersonaComposer is still a stub** (DEL-04-04) — `StubPersonaManager` is still wired.
6. **Replay/artifact partials** (DEL-05-04/05) — overflow spill is Bash/hook-path only and
   absent from the mapper path; `malformedLineCount` is unsurfaced; no full event-class
   replay-coverage test; `tool-evidence`/`tool-result-artifacts` have no direct tests.
7. **Subagent child-run record adapter mapping** (DEL-08-05) —
   `createAdapterObservedChildRunRecord` has zero callers.

The decomposition `_STATUS.md` files (all SEMANTIC_READY) systematically under-report
landed work and must be reconciled (as a derived note, not bulk edits). A few governance
passages over-report forward roadmap; the persona-stub clause remains accurate.

## Evidence

See `Evidence_Map.csv` (curated, load-bearing rows with file:line citations and evidence
levels) and `Conflicts.csv` (packet-vs-packet conflicts the reconciliation critic resolved
by live spot-check). Query trail in `Query_Log.csv`.

Highest-value evidence:

- Provider selection opt-in + default stub: `frontend/src/lib/harness/runtime.ts:24-76`.
- agentSdk key not wired: zero `ANTHROPIC_API_KEY` refs in
  `claude-agent-sdk-manager.ts` / `sdk-options-builder.ts`; `turn-engine.ts` presence-check
  only (R4, verified live).
- Compaction mirror LANDED: `sdk-message-mapper.ts:818-840` + tests (R4, verified live;
  corrects an earlier "partial" assumption).
- Mutating engines landed: `lib/lifecycle/transition.ts`, `lib/dependencies/register-writer.ts`,
  `lib/workspace/deliverable-contracts.ts` (R3, verified live).
- Section 8 surface + premerge wrapper: `frontend/scripts/validate-harness-section8.mjs`,
  `validate-harness-premerge.mjs`; no `validate-harness-section9.mjs` exists (R4).
- All 53 `_STATUS.md` at SEMANTIC_READY (R2, `grep` over the live tree).

## Interpretation

The program's central risk is conflating "has a passing unit test" with "completes a real
turn." The opt-in posture (settingSources `[]`, hard-deny precedence, descriptor
metadata-only reserved tools, agentSdk opt-in) is the strongest, most settled evidence
base (R4/R5); scrutiny belongs on the unproven edges — key wiring, packaging, mutating-MCP
exposure, persona, and end-to-end turn execution. STAB-04's design pivots on one
unverified architectural assumption (whether `canUseTool`/hooks fire for in-process MCP
tools under SDK 0.3.150), which must be probed before committing the wrapper-only design.

## Caveats

- Current-state claims verified against the live tree; the retrieval snapshot is a derived
  mirror used for discovery and may lag.
- Evidence levels follow the RESEARCH rubric (R1 retrieval-only .. R5 accepted ruling).
  "LANDED" rests on reading source + test files and their assertions; the test suite was
  not freshly executed in this pass.
- Two of eight research streams (decomposition-status, decisions-and-rulings) were salvaged
  from primary sources after transient retrieval-agent failures; their findings were
  corroborated directly against the live tree and the decision register.

## Open Questions

See `Open_Questions.csv`. Load-bearing ones: does `query()` in 0.3.150 read the key only
from `process.env`; does `canUseTool` fire for in-process MCP tools; does packaged Electron
resolve HOME so SDK transcripts land in a resolvable path; should Section 9 own the
mutating-MCP round-trip IDs.

## Handoff / Next Action

See `HANDOFF_STATE.md`. The completed plan
(`projects/chirality-app-dev/plans/PLAN_2026-06-16_runtime_stabilization.md`) was
accepted as the active governing queue (D-APP-11). No source changes are recommended by
this packet; STAB-00 (governance-only) is the next bounded tranche.
