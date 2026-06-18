# Live Packaged agentSdk Read-Tool Proof Plan

**Date:** 2026-06-17
**Status:** ACTIVE GOVERNING DEVELOPMENT QUEUE - D-APP-16 AWAITING RULING
**Queue-selection authority:** human project authority in chat, 2026-06-17:
`APPROVE: Prepare D-APP-15 and a bounded active plan for the live packaged agentSdk read-tool proof as the next Chirality App Dev queue.`
**Decision packet:** `execution/_Coordination/_DECISIONS/D-APP-15_PACKET_2026-06-17.md`
**Ruling:** `execution/_Coordination/_DECISIONS/D-APP-15_RULING_2026-06-18.md`
**Product:** Chirality desktop harness and bundled agent operating system
**Working root:** `projects/chirality-app-dev/`
**Prepared by:** `WORKING_ITEMS`
**Follows:** `plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md` (completed, closed)
**Roadmap anchor:** `docs/PLAN.md` provider-adapter runtime; `D-APP-12` default-provider hold ruling

This plan is the active queue after R6 closeout. D-APP-15 Option A approved one bounded
live packaged `agentSdk` read-tool proof. The proof is intended to collect the missing
packaged-live evidence named by D-APP-12 before any later packet may recommend
default-provider cutover.

This plan does **not** approve default-provider cutover. `agentSdk` remains opt-in. It
does not approve concrete non-Anthropic providers, provider-network expansion, remote MCP,
plugins, broad tool search, domain tools, release readiness, lifecycle issuance,
professional approval, certification, sealing, authentication, code-compliance acceptance,
or professional-boundary changes.

## 1. Purpose

D-APP-12 Option B accepted non-live packaged SDK resolver/HOME evidence but held
default-provider cutover. The ruling says a later cutover packet should first request or
prepare one bounded live packaged read-tool proof path unless the human waives that proof.

This plan turns that prerequisite into a bounded queue. LP-00, LP-01, LP-02, and LP-03
have landed. LP-03 consumed the single D-APP-15-approved live run and failed before
read-tool execution because the selected model was unavailable or inaccessible for the
supplied key. D-APP-16 is now awaiting a human ruling before any retry, waiver, or close
disposition.

- prepare D-APP-15;
- obtain a ruling on whether live provider use is approved;
- finalize proof command, package path, key supply, artifact, stop-condition, and
  redaction details;
- run one tightly scoped packaged read-tool proof;
- review the evidence and either prepare a later D-APP-12 packet, record a blocker, or
  close with `agentSdk` still opt-in.

## 2. Current Evidence Basis

Already landed and not reopened by this plan:

- Runtime Stabilization and R6 are completed closed history.
- The runtime spine, event log, permission overlay, tool descriptors, read/write/Bash
  surfaces, bounded Chirality MCP tools, governed subagent bridge, Section 9 validation,
  persona composer, and no-live packaged SDK resolver/HOME evidence have landed.
- `agentSdk` is the opt-in first concrete adapter.
- D-APP-12 holds default-provider cutover.
- D-APP-13, D-APP-14, and D-APP-15 are ruled.

Known residual evidence gap:

- Live packaged `agentSdk` provider behavior from the packaged app path is not proven.
- Actual live SDK transcript creation/location under packaged execution is not proven.
- Default-provider readiness is not ruled.
- LP-03 app-directory live execution reached the live provider path but failed on selected
  model availability/access before any `Read` tool use; see
  `plans/artifacts/lp03_live_packaged_agentsdk_read_tool_evidence_2026-06-18.md`.

## 3. Tranche Spine

| Tranche | Status | Purpose | Primary scope | Minimum validation |
|---|---|---|---|---|
| `LP-00` Queue Activation and D-APP-15 Packet | **LANDED 2026-06-17.** | Created this active plan, prepared D-APP-15 packet, updated decision register and coordination pointers. | Governance/control-plane only. | Governance gate: diff hygiene, JSON/path checks, stale active-queue search, no-runtime-change confirmation. |
| `LP-01` D-APP-15 Ruling Intake | **LANDED 2026-06-18.** | Recorded D-APP-15 Option A approval for one bounded live packaged `agentSdk` read-tool proof. | Decision record and control-plane updates only. | Governance gate: diff hygiene, path checks, targeted D-APP-15 state checks, no-runtime-change confirmation. |
| `LP-02` Proof Harness Finalization | **LANDED 2026-06-18.** | Finalized exact command path, package path, API-key-file supply, artifact directory, stop conditions, and redaction checks. Added `npm run harness:validate:agentsdk-packaged-live-read-tool` and `plans/artifacts/lp02_live_packaged_agentsdk_read_tool_procedure.md`. | Proof script/test and docs/control-plane evidence updates. | Passed focused packaged-proof tests, live-proof fixture test, typecheck, and diff hygiene. |
| `LP-03` Live Packaged Read-Tool Proof | **EXECUTED 2026-06-18 - BLOCKER RECORDED.** | Executed the one D-APP-15-approved app-directory live proof. The package build and no-live packaged resolver baseline passed; the live proof failed on selected-model availability/access before `Read` tool use. | Local proof artifact generation; no default-provider change. | `npm run desktop:pack`; no-live packaged proof pass; live proof fail; redaction scans pass; evidence recorded in `plans/artifacts/lp03_live_packaged_agentsdk_read_tool_evidence_2026-06-18.md`. |
| `LP-04` Evidence Review and D-APP-12 Disposition | **NEXT / BLOCKED ON D-APP-16 RULING.** | Decide whether to approve one model-corrected retry, deny retry and close with blocker, waive successful proof for later D-APP-12 review, or apply a custom disposition. | Decision packet/control-plane only unless proof retry is separately approved. | Governance gate plus any proof-artifact checks referenced by the review. |
| `LP-05` Closeout | **BLOCKED on LP-04.** | Close the plan, update coordination, completion log, and handoff state. | Governance/control-plane only. | Governance gate; runtime commands skipped unless executable behavior changed. |

## 4. Boundaries

This queue does not authorize:

- default-provider cutover;
- governance text declaring SDK-backed Anthropic execution the active default;
- more than one live provider proof run without a later human ruling;
- non-Anthropic provider implementation or routing;
- provider-network broadening beyond the current Anthropic first-adapter proof path;
- remote MCP servers, plugins, broad tool search, or domain tools;
- Pi adapter, fork, import, sidecar, runtime-floor migration, or spike work;
- release publication, signing, notarization, lifecycle issuance, professional approval,
  certification, sealing, authentication, code-compliance, or professional-boundary
  claims.

## 5. Required Human Rulings

D-APP-15 is ruled Option A. It permitted one bounded live packaged proof run only. LP-03
consumed that run.

D-APP-16 is awaiting ruling. It blocks any second live packaged proof run, any retry with a
different model, and any waiver-based D-APP-12 cutover packet after the failed proof.

After LP-03, a separate D-APP-12 ruling remains required before any default-provider
cutover. A successful proof does not itself make `agentSdk` the default.

## 6. Validation Policy

LP-00 and LP-01 are governance/control-plane work. Use:

```bash
git diff --check
```

plus targeted stale-reference searches, path/link existence checks, JSON parse checks when
JSON is touched, and an explicit no-runtime-code-change confirmation.

LP-02 and LP-03 use the gate family selected by `docs/VALIDATION_STRATEGY.md`,
`docs/RELEASE_QUALITY_GATES.md`, `docs/BUILD_AND_RELEASE.md`, and the D-APP-15 ruling.
Expected commands may include:

```bash
npm run test
npm run typecheck
npm run instruction-root:integrity
npm run desktop:pack
npm run desktop:dist
npm run harness:validate:agentsdk-packaged-proof
```

The live proof command and network/key checks are named in
`plans/artifacts/lp02_live_packaged_agentsdk_read_tool_procedure.md`. LP-03 used that
procedure once under D-APP-15. No further live proof run may proceed without D-APP-16 or a
later human ruling.

## 7. Acceptance Criteria

This plan is complete when one of the following is true:

- D-APP-15 approves a proof, the bounded live packaged read-tool proof runs, evidence is
  reviewed, and the plan records whether to prepare a later D-APP-12 packet or continue
  holding default-provider cutover;
- D-APP-15 waives the proof and the plan records the waiver path for later D-APP-12 review;
- D-APP-15 denies the proof and the plan closes with `agentSdk` remaining opt-in; or
- the proof blocks with explicit evidence and the plan records the blocker and remaining
  requirements.

In all outcomes, `agentSdk` remains opt-in unless a later D-APP-12 ruling explicitly
approves default-provider cutover.

## 8. Finalization Rule

LP-00 updated `_COORDINATION.md`, `NEXT_INSTANCE_PROMPT.md`, `_LATEST.md`, and the
decision register so future instances treat this file as the active queue and D-APP-15 as
the first required ruling. Later tranche closeouts must move landed narrative to
`plans/PLAN_COMPLETION_LOG.md` and stop when the next action requires a human ruling.
