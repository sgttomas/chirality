# Evidence - DEL-04-01 Handover-Consumption Pass (DEP-04-01-010..013)

Date: 2026-07-18
Run: WI-PKG04-01 (WORKING_ITEMS, PKG-04, handover-evidence tranche;
`execution/_Coordination/AgentRuns/DEL-04-01_HANDOVER_EVIDENCE_2026-07-18/ORCHESTRATION_PLAN.md`)
Authority for judgments: D-APP-60 instrument
(`execution/_Coordination/_DECISIONS/D-APP-60_PACKET_FROZEN_BLOCK_INSTRUMENT_2026-07-17.md`);
dispositions below are the agent's decisions under owner-delegated latitude, never owner acts.
Rationale artifact: `_run_records/TASK_RUN_2026-07-18_DEP-04-01-010-013_handover_evidence.md`
Precedent followed: `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md` (structure and hygiene).

## Epistemic Status

This is derivative evidence produced by a governed dependency-register evidence pass. It does
not replace decomposition truth, source/test evidence, decision records, or human lifecycle
approvals. It authorizes no issuance: no `CHECKING -> ISSUED` transition (F-APP-4), no
release/distribution act (F-APP-2), no provider or network expansion (F-APP-1 as amended by
D-APP-44), no domain-engine implementation (F-APP-3), and no new standing surface (F-APP-5).
`_STATUS.md` state is untouched and remains `IN_PROGRESS`; the `Checking Approval SHA` is
untouched. Satisfaction-state changes below are register bookkeeping against cited live
evidence under the D-APP-60 class test; every exercised judgment and every rejection is
recorded in the rationale artifact.

## Source-Citation Migration Note (recorded 2026-07-18)

The four HANDOVER rows cite `Procedure.md#Steps` step 13. Owner commit `548caa731`
("Migrate DEL-04-01 to ScopeOfWork v1", 2026-07-13) consolidated the four-document kit into
`ScopeOfWork.md`; the routing requirement survives verbatim at `ScopeOfWork.md` CLM-018 —
Steps, step 13: "Route downstream work. Send implementation requirements to DEL-04-02
through DEL-04-05 as appropriate." The stale citations are corrected by dated notes only
(this note plus per-row CSV notes); original citation text is retained as history. The
parallel consumer-kit migrations are `fe4bdee53` (DEL-04-02), `603384787` (DEL-04-03),
`222a26b53` (DEL-04-04), and `036e0769c` (DEL-04-05), all 2026-07-13.

## What DEL-04-01 Had To Hand Over

Per the decomposition (DEL-04-01 row: "First-adapter probe notes; version decision; fallback
criteria; future-provider criteria; residual-risk notes") and `ScopeOfWork.md` CLM-018 step
13, the handover content is the probe/version-decision material each consumer recorded as its
own need:

| Consumer | Consumer-recorded need (mirror row) | Deliverable now? |
|---|---|---|
| DEL-04-02 | probe/version decision before exact SDK TypeScript option fields are frozen (DEP-04-02-006; `ScopeOfWork.md` CLM-017 Prerequisites) | Yes — compile-time contract, fully determined by the pinned package |
| DEL-04-03 | exact observed SDK message sequence / probe-backed payload fixtures (DEP-04-03-007; `ScopeOfWork.md` CLM-003 Attributes, OI-001) | No — a live-runtime observation; owner-gated (D-APP-52) |
| DEL-04-04 | none recorded anywhere (no DEL-04-01 reference in any DEL-04-04 register or document) | n/a |
| DEL-04-05 | probe/version decision before finalizing exact SDK error object shapes and packaged SDK behavior (DEP-04-05-007; `ScopeOfWork.md` CLM-017 Prerequisites) | Partially — live-confirmed error shapes and packaged live behavior are owner-gated (D-APP-52) |

## Per-Row Disposition

| DependencyID | Prior | Disposition 2026-07-18 | Basis |
|---|---|---|---|
| DEP-04-01-010 | ACTIVE / TBD | ACTIVE / **SATISFIED** (mirror DEP-04-02-006 likewise) | Consumption evidence section A below. The consumer-recorded need is compile-time and fully delivered: pinned versions, frozen option shape, isolation posture — implemented and tested in the live tree. |
| DEP-04-01-011 | ACTIVE / TBD | ACTIVE / TBD (evidence landed; annotate-only) | Section B. Deterministic mapping material is consumed, but the consumer's principal recorded need — the exact observed SDK message sequence — is owner-gated (D-APP-52) and cannot yet be handed over. Residual is the same live-probe residual recorded at DEP-04-01-007. |
| DEP-04-01-012 | ACTIVE / TBD | ACTIVE / TBD (**referred to owner**, near-miss form) | Section C. No consumption trace exists and two defensible outcomes (retire vs. keep/re-scope) survive live-tree analysis; class-test gate (b) fails, so the row is not decided. See the rationale artifact's referral slate. |
| DEP-04-01-013 | ACTIVE / TBD | ACTIVE / TBD (evidence landed; annotate-only) | Section D. Error-classification implementation and scripted packaged proofs are consumed, but live-confirmed exact SDK error object shapes and packaged live behavior remain owner-gated (D-APP-52; DEL-04-05 `_STATUS.md` Remaining four-class assertion gap). |

## A. DEP-04-01-010 -> DEL-04-02 (SdkOptionsBuilder and Settings Isolation) — consumed

Consumer-recorded need: "first-adapter probe/version decision | TBD; required before final
exact SDK TypeScript option fields are frozen" (DEP-04-02-006; DEL-04-02 `ScopeOfWork.md`
CLM-017 Prerequisites). This need is compile-time: once the package version is pinned, the
exact TypeScript option fields are determined by the pinned package's types.

Live-tree consumption evidence (each item opened and confirmed 2026-07-18):

1. **Version decision delivered:** `frontend/package.json` pins
   `@anthropic-ai/claude-agent-sdk@0.3.150` and `@anthropic-ai/sdk@0.93.0` (lines 37-38;
   lockfile agrees per `Evidence_CODEV-001_SDK_Probe_Record.md` Version Evidence).
   D-APP-18 Option A (owner ruling) approved the bounded key-aware default-provider
   implementation on this pin.
2. **Option fields frozen against the pin:** `frontend/src/lib/harness/sdk-options-builder.ts`
   implements the full governed option shape and typechecks against the pinned SDK package.
3. **Requirements consumed and tested:**
   `frontend/src/__tests__/lib/sdk-options-builder.test.ts` proves settings-source isolation
   (`settingSources: []`), user/local setting-source exclusion, tool allow/deny construction,
   permission mode, hooks, `canUseTool`, MCP server attachment, resume, and delegated-agent
   option shaping (crosswalk: `Evidence_CODEV-001_SDK_Probe_Record.md`, Probe Evidence
   Matrix rows "SDK settingSources isolation", "user/local setting source exclusion",
   "Current governed SDK option shape" — all PASS).
4. **Reconciled posture:** `docs/harness/runtime_evidence_reconciliation.md` (DEL-04-02 row)
   records "`sdk-options-builder` keeps `settingSources: []` by default, accepts only the
   explicit `project` override" with no probe-dependent residual for the option shape.

The residuals that do remain for DEL-04-01 (live Claude Code subprocess version
`BLOCKED_TBD`; adoption-verdict approving role TBD) are separately recorded at
DEP-04-01-007 (owner-gated per D-APP-52) and `_STATUS.md` Remaining item 1 (owner-gated per
D-APP-56 R4-P47); they are not part of the consumer-recorded need this row tracks. Keeping
row 010 open would duplicate those recorded residuals under a category that tracks routing.

**Disposition:** DEP-04-01-010 `SATISFIED` (ProposedMaturity `SEMANTIC_READY`); mirror
DEP-04-02-006 `SATISFIED` (ProposedMaturity `SEMANTIC_READY`).

## B. DEP-04-01-011 -> DEL-04-03 (SdkMessageMapper) — partially consumed; row stays open

Consumer-recorded need: "Exact SDK message sequence and payload-field mappings depend on
DEL-04-01 / OI-001 probe evidence" (DEP-04-03-007; DEL-04-03 `ScopeOfWork.md` CLM-003
Attributes: "TBD pending DEL-04-01 first-adapter probe / OI-001").

Consumed now (live-tree, opened and confirmed 2026-07-18):
`frontend/src/lib/harness/sdk-message-mapper.ts` and
`frontend/src/__tests__/lib/sdk-message-mapper.test.ts` implement and test SDK-to-`UIEvent`
and SDK-to-`HarnessEvent` mapping with deterministic raw-SDK fixture provenance against the
pinned package; `docs/harness/runtime_evidence_reconciliation.md` (DEL-04-03 row) records
the active `section9.adapter_message_mapper` posture.

Not yet handed over (and not currently possible to hand over): the exact observed live
`query()` message sequence and payload fixtures. `Evidence_CODEV-001_SDK_Probe_Record.md`
records "Exact live `query()` payload-sequence capture remains separate from deterministic
fixture provenance" and Claude Code subprocess version `BLOCKED_TBD`; the live-LLM
demonstration is owner-gated per D-APP-52. Marking this row `SATISFIED` would manufacture
evidence standing for a handover whose principal recorded content does not exist yet.

**Disposition:** ACTIVE / TBD retained; dated annotation ties the row's sole residual to the
DEP-04-01-007 / D-APP-52 owner-gated live-probe residual. Mirror DEP-04-03-007 annotated the
same way; the partially stale DEL-04-03 `_DEPENDENCIES.md` warning ("probe evidence is still
TBD") is corrected with a dated note (deterministic probe evidence exists; the exact observed
sequence remains gated).

## C. DEP-04-01-012 -> DEL-04-04 (PersonaComposer) — no consumption trace; referred

Live-tree findings (opened and confirmed 2026-07-18, skeptical in both directions):

- DEL-04-04 records **no DEL-04-01 dependency anywhere**: `Dependencies.csv` rows
  DEP-04-04-001..008 target PKG-04, SOW-017, SOW-030, DEL-04-02 (INTERFACE), DEL-08-01,
  DEL-08-02, `docs/PRD.md`, and a downstream fingerprint handover — never DEL-04-01; no
  DEL-04-04 document references DEL-04-01.
- DEL-04-04 `ScopeOfWork.md` CLM-008 scope exclusions assign SDK option construction to
  DEL-04-02, SDK stream/message translation to DEL-04-03, and key/base-URL/network/error
  classification to DEL-04-05.
- `frontend/src/lib/harness/persona-manager.ts` (`PERSONA_COMPOSER_VERSION =
  'persona-composer.v1.instruction-root'`) imports instruction-root, permission-overlay,
  subagent-bridge, tool-pool, and harness-contract surfaces — no SDK package, no
  sdk-options-builder, no DEL-04-01 output.
- Counter-direction check: DEL-04-04 PC-REQ-010 wants boot fingerprints to include "SDK tool
  names/versions ... when those inputs are available", citing DEP-04-04-004 (DEL-04-02
  INTERFACE) and DEP-04-04-008 — a mediated route through which future probe-derived
  version material could still reach DEL-04-04.

Because both "retire as not-applicable" and "keep/re-scope pending the owner-gated live
probe" survive adversarial analysis (and the only prior retirement of a DEL-04-01 row,
DEP-04-01-008, was executed under an explicit ruling, RUL-SCC-001-TRANCHE-001), the class
test's determinism gate (b) fails. **The row is not decided here.** It is referred to the
owner in near-miss form via the rationale artifact's referral slate. No DEL-04-04 file is
modified (the brief permits DEL-04-04 writes only on actual consumption evidence, which does
not exist).

## D. DEP-04-01-013 -> DEL-04-05 (Provider Key, Base URL, Network Bridge) — partially consumed; row stays open

Consumer-recorded need: "first-adapter probe/version decision | TBD - required for exact SDK
error object shapes and packaged SDK behavior" (DEP-04-05-007; DEL-04-05 `ScopeOfWork.md`
CLM-017 Prerequisites).

Consumed now (live-tree, opened and confirmed 2026-07-18):
`frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` implements provider error
classification against the pinned SDK — categories `API_RESPONSE_ERROR` (lines 514, 521,
545, 551), `RATE_LIMITED` (538, 629), `NETWORK_ERROR` (656, 664), `REQUEST_TIMEOUT` (976) —
and the bounded network posture (`DEFAULT_ANTHROPIC_BASE_URL = 'https://api.anthropic.com'`,
line 36); `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` exists;
packaged SDK behavior is evidenced by the ADQ-15 scripted no-live packaged proofs (PKG-09
`Evidence_ADQ-15_Packaging_Instruction_Root_Refresh.md`;
`frontend/src/__tests__/scripts/verify-packaged-agent-sdk-runtime.test.ts`) and the ADQ-16
secret-scan / scripted network proofs (`docs/harness/runtime_evidence_reconciliation.md`
DEL-04-05 row).

Not yet handed over: **live-confirmed** exact SDK error object shapes and packaged **live**
behavior. ADQ-15 is explicitly "scripted no-live proof"; DEL-04-05 `_STATUS.md` Remaining
records the RQ-011 four-class assertion gap "(gate: future owner-authorized test tranche)";
the live demonstration is owner-gated per D-APP-52.

**Disposition:** ACTIVE / TBD retained; dated annotation records the consumed portion and
ties the residual to DEP-04-01-007 / D-APP-52 and the DEL-04-05 RQ-011 gated gap. Mirror
DEP-04-05-007 annotated the same way.

## Additional Stale-Map Deltas Found (beyond the DEL-04-01 Procedure.md citation)

1. Consumer mirror rows cite deleted four-document files: DEP-04-02-006
   (`Procedure.md > Prerequisites`, now `ScopeOfWork.md` CLM-017 per `fe4bdee53`),
   DEP-04-03-007 (`Datasheet.md#Attributes`, now `ScopeOfWork.md` CLM-003 per `603384787`),
   DEP-04-05-007 (`Procedure.md#Prerequisites`, now `ScopeOfWork.md` CLM-017 per
   `036e0769c`). Corrected by dated notes on the touched rows only.
2. DEL-04-05 `_DEPENDENCIES.md` per-row table listed DEP-04-05-011 as ACTIVE and the counts
   line claimed "12 ACTIVE rows", but the CSV records DEP-04-05-011 `RETIRED /
   NOT_APPLICABLE` (Lifecycle Summary ACTIVE 10 / RETIRED 2 was already correct). Corrected
   with a dated note in that file's sync.
3. DEL-04-03 `ScopeOfWork.md` (e.g., CLM-003 Attributes, CLM-020 open-issue rows) still
   carries "REF-006 ... HASH_MISMATCH warning applies" wording, although REF-006 has been
   `MATCH` under D-APP-38 since 2026-07-10. Out of this run's write scope; reported only.
4. DEL-04-02 `ScopeOfWork.md` CLM-017 Prerequisites row and DEL-04-05 `ScopeOfWork.md`
   CLM-017 Prerequisites row still read "first-adapter probe/version decision | TBD ...";
   for DEL-04-02 that kit wording now diverges from the closed register row DEP-04-02-006
   (kit contract text is outside this run's write scope; divergence reported for the next
   owner-authorized kit/concordance pass).

## Validation

`python3 execution/_Scripts/validate_dependencies.py` run 2026-07-18 from the project root on
every touched CSV (DEL-04-01, DEL-04-02, DEL-04-03, DEL-04-05 `Dependencies.csv`): all PASS,
0 errors (outputs recorded in the rationale artifact).
