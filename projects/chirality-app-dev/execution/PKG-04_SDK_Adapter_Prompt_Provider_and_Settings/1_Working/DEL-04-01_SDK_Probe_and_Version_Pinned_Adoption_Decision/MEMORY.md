# MEMORY - DEL-04-01

## Decisions And Evidence

- 2026-06-21 - ADQ-04 refreshed SDK probe/default-provider evidence in `docs/harness/runtime_evidence_reconciliation.md` and `frontend/docs/harness/runtime_engine_contract.md`: package pins remain `@anthropic-ai/claude-agent-sdk@0.3.150` and `@anthropic-ai/sdk@0.93.0`, D-APP-17/D-APP-18 supersede the original opt-in/adoption TBD posture for bounded key-aware default selection, current Section 9 IDs use `section9.adapter_*`, and D-APP-38 corpus `v1` supersedes the old REF-006 hash-mismatch caveat. No lifecycle state, dependency row, provider expansion, release posture, or professional/code-compliance claim changed.
- 2026-06-16 - Human project authority advanced this deliverable lifecycle from SEMANTIC_READY to IN_PROGRESS because active code implementation is underway. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-05-24 - Added `@anthropic-ai/claude-agent-sdk@0.3.150` as the pinned first-adapter probe dependency.
- 2026-05-24 - Upgraded direct `@anthropic-ai/sdk` to `0.93.0` to satisfy the Claude Agent SDK peer dependency while keeping the existing direct adapter selectable.
- 2026-05-24 - Added opt-in SDK provider mode `CHIRALITY_HARNESS_PROVIDER=agentSdk`; default provider behavior remains unchanged.
- 2026-05-24 - SDK options builder defaults to `settingSources: []`, exposes no built-in tools for CODEV-001, and accepts only explicit `CHIRALITY_SDK_SETTING_SOURCES=project` as a development override.
- 2026-05-24 - first-adapter probe evidence recorded in `Evidence_CODEV-001_SDK_Probe_Record.md`.
- 2026-05-24 - Dependency closure assessment set `DEP-04-01-008` to `SATISFIED`; follow-up DepClosure blocker-subset scan is acyclic.

## Open Items

- Claude Code subprocess version remains `BLOCKED_TBD` pending live SDK init event.
- Live SDK session/resume behavior remains partially evidenced by metadata fields, tests, and D-APP-17 packaged proof history; broader controlled session/resume coverage remains residual.
- Interrupt/cancel subprocess behavior remains partially evidenced by adapter control calls, but requires controlled probe.
- App-directory packaged live read-tool proof passed under D-APP-17; broader packaged workflow evidence and release/distribution posture remain outside this deliverable.
- Bounded key-aware default adoption is governed by D-APP-18; broader provider expansion, release/distribution posture, and fallback/provider taxonomy remain unresolved unless separately ruled.
- Historical REF-006 hash mismatch is superseded by D-APP-38 authority corpus `v1`; no closure claim is made by ADQ-04.
- Strict all-active FULL_GRAPH closure remains open outside this deliverable.

## Dependency Note

`DEP-04-01-008` is now `SATISFIED`. No rows were waived, retired, or marked not applicable.
- 2026-07-12 - D-APP-56 R5 P40 executed UPD-069: REF-006 current-state kit/register wording now agrees with D-APP-38 MATCH; dated source-warning and assessment history is preserved. No lifecycle transition.

- 2026-07-12 - D-APP-56 R5 P45 executed UPD-118: current kit/register metadata now reflects live ruled state; dated history and genuine TBD/gates remain preserved. No lifecycle transition occurred.
- 2026-07-12 - D-APP-56 consolidated decision-application tranche recorded the applicable ruled ownership, mapping, gate-reaffirmation, or dated-deferral result for DEL-04-01; proposal-only source rows were not treated as human rulings, no unruled work was executed, and no lifecycle transition occurred.
- 2026-07-18 - D-APP-63 owner ruling ("Option A with the rider.", Ryan Tufts, in-session; packet `execution/_Coordination/_DECISIONS/D-APP-63_PACKET_DEP-04-01-012_RETIREMENT_2026-07-18.md`) resolved the DEP-04-01-012 referral: row retired `RETIRED`/`NOT_APPLICABLE`. Rider: any DEL-04-04-relevant output from the future D-APP-52 live probe mints a NEW row — revival by new recorded basis; the retired row is never reactivated. The retirement is the owner's act; WI-PKG04-01 executed mechanical conformance only. No lifecycle transition; no fence contact.
- 2026-07-18 - WI-PKG04-01 handover-evidence tranche under the D-APP-60 instrument: `DEP-04-01-010` closed `SATISFIED` (mirror `DEP-04-02-006` closed with it — version pin and option-shape material verifiably consumed by `sdk-options-builder.ts`/tests); `DEP-04-01-011`/`-013` annotated open solely on the D-APP-52-gated live-probe residual (mirrors `DEP-04-03-007`/`DEP-04-05-007` annotated); `DEP-04-01-012` referred to owner in near-miss form (retire-vs-keep both defensible; DEL-04-04 shows no consumption trace). Stale `Procedure.md` citations resolved by dated notes to `ScopeOfWork.md` CLM anchors per the 2026-07-13 ScopeOfWork-v1 migration commits. See `Evidence_HANDOVER_CONSUMPTION_2026-07-18.md`. No lifecycle transition; no fence contact.
- 2026-07-19 - D-APP-68 recommendation 8 rendered the owner verdict `ADOPT_WITH_RESIDUAL_RISK` for the repository demonstrator, pinned to `@anthropic-ai/claude-agent-sdk@0.3.150` and observed Claude Code `2.1.150`. `Decision_Version_Pinned_SDK_Adoption_2026-07-19.md` records all twelve required residual areas and fallback triggers. CODEV-001's dated `BLOCKED_TBD` cells are superseded prospectively by D-APP-52 live evidence; historical observations remain intact. No lifecycle, Approval SHA, dependency, runtime-source, release, issuance, or professional-reliance change.
