# DEL-04-01 Version-Pinned SDK Adoption Decision

**Decision:** `ADOPT_WITH_RESIDUAL_RISK`

**Decision date:** 2026-07-19

**Approver:** Ryan Tufts (K-AUTH-1), demonstrator scope

**Authority:** D-APP-68 recommendation 8, executing the owner ruling “I
approve recommendations 1–8.” D-APP-65 assigned the approving role; D-APP-68
renders the verdict.

**Version boundary:** `@anthropic-ai/claude-agent-sdk@0.3.150` with observed
Claude Code `2.1.150`. This decision does not float to later SDK or Claude
Code versions. An upgrade requires fresh regression evidence against the
product-owned contracts and a fresh adoption ruling.

## Scope of the Decision

The pinned SDK is adopted as the first replaceable adapter behind Chirality's
`AgentEnginePort` and product-owned runtime contracts for this repository's
demonstrator. The SDK and its subprocess are privileged implementation
substrate, not product identity, governance authority, or a source of
canonical Chirality semantics.

This verdict is not release approval, issuance, certification, professional
acceptance, signing, notarization, publication, or external distribution. It
does not establish production-default readiness beyond the demonstrated
scope, and it makes no claim for Windows, Linux, architectures other than the
observed macOS arm64 environment, signing, notarization, or distributed
packages.

## Version-Pinned Evidence

- `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md` and its SHA-bound JSON summaries
  record SDK `0.3.150`, Claude Code `2.1.150`, and `darwin:arm64`.
- The live development probe observed `system/init -> assistant ->
  assistant(tool_use Read) -> user(tool_result) -> assistant ->
  result/success`, SDK session IDs, result keys, controlled
  `CLAUDE_CONFIG_DIR` transcript placement, 401 and unreachable-base-URL
  shapes, and abort behavior.
- The packaged live proof observed an SDK-backed Read turn using the platform
  binary under `app.asar.unpacked` in a fresh unsigned local package.
- `frontend/package.json` and `frontend/package-lock.json` bind the SDK
  package version. `Evidence_CODEV-001_SDK_Probe_Record.md` preserves the
  earlier deterministic and scripted evidence and now points to the D-APP-52
  live evidence for superseded `BLOCKED_TBD` cells.
- RATE_LIMITED was not live-triggered. D-APP-65 separately accepted simulated
  unit coverage for DEL-04-05's four-class criterion; this decision does not
  convert that fact into live evidence.

## Authority and Evidence Paths

- D-APP-68 ruling and explicit packet fences:
  `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-68_PACKET_CONCORDANCE_RULINGS_2026-07-19.md`.
- D-APP-52 transport authority and live-demonstration boundary:
  `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-52_RULING_2026-07-06.md` and
  `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`.
- D-APP-65 approver assignment and demonstrator boundary:
  `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-65_PACKET_ACCEPTED_RECOMMENDATIONS_2026-07-18.md`.
- Managed-delegation bridge retirement:
  `docs/governance_harness/_DECISIONS/D-GOV-14_pr188_review_closure.md`
  item 7 and root `AGENTS.md`.
- Product and reliance boundaries:
  `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-02_Reliance_Boundary_Register/ScopeOfWork.md` and
  `projects/chirality-app-dev/execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/ScopeOfWork.md`.
- Runtime and adapter contracts:
  `projects/chirality-app-dev/frontend/docs/harness/runtime_engine_contract.md` and
  `projects/chirality-app-dev/frontend/packages/harness-contract/src/agent-engine-port.ts`.
- Package, settings, and permission evidence:
  `projects/chirality-app-dev/frontend/package.json`,
  `projects/chirality-app-dev/frontend/package-lock.json`,
  `projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-options-builder.test.ts`, and
  `projects/chirality-app-dev/frontend/src/lib/harness/persona-manager.ts`.
- Packaged-proof boundary:
  `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/Evidence_ADQ-15_Packaging_Instruction_Root_Refresh.md`.
- Normative twelve-area census and managed-delegation evidence:
  this deliverable's `ScopeOfWork.md` DEL-04-01-REQ-015 and
  `projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/SCOPED_D65_CONCORDANCE_2026-07-19/PKG_LEDGERS/PKG-08_SCOPED_LEDGER.csv`.

## Twelve Residual-Risk Assessments

| # | Residual-risk area | Evidence | `ADOPT_WITH_RESIDUAL_RISK` assessment |
|---:|---|---|---|
| 1 | SDK API drift | `frontend/package.json`; `frontend/package-lock.json`; D-APP-52 live probe | Accept only at SDK `0.3.150` and Claude Code `2.1.150`. An upgrade triggers regression against Chirality contracts and a fresh adoption ruling. |
| 2 | Settings leakage | D-APP-52 controlled `CLAUDE_CONFIG_DIR` observations; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` | Accept the shipped `settingSources: []` posture. SDK-created `.claude.json`, `backups/`, and `policy-limits.json` remain observed substrate effects inside the controlled config root, not Chirality configuration authority. |
| 3 | Allowed-tools misconception | `ScopeOfWork.md` DEL-04-01-REQ-015; `frontend/src/lib/harness/persona-manager.ts`; permission and hook tests | `allowedTools` alone is never a restriction boundary. Chirality mode policy, deny policy, hooks, `canUseTool`, and human gates remain authoritative and must fail closed. |
| 4 | Transcript location | D-APP-52 transcript/config-root observations; `frontend/docs/harness/runtime_engine_contract.md` | SDK transcript/store linkage under `CLAUDE_CONFIG_DIR/projects/` is secondary adapter metadata. Chirality's JSONL event record and canonical session identity remain authoritative. |
| 5 | Electron packaging | D-APP-52 packaged live proof; `Evidence_CODEV-001_SDK_Probe_Record.md`; `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/Evidence_ADQ-15_Packaging_Instruction_Root_Refresh.md` | Accept only the demonstrated unsigned local `darwin:arm64` path with the binary under `app.asar.unpacked`. Signing, notarization, distribution, release readiness, and other platforms remain outside the evidence. |
| 6 | SDK security boundary | `ScopeOfWork.md` residual-risk method; permission, path, redaction, and event contracts | Treat the SDK/subprocess as privileged substrate behind Chirality-owned permission, path, redaction, and event boundaries. An SDK default cannot replace those boundaries. |
| 7 | Subagent inherited permissions | D-GOV-14 item 7; root `AGENTS.md`; scoped PKG-08 managed-delegation/path-policy evidence | Accept delegation only through managed child sessions with sealed context and explicit scopes. The retired record-less SDK `Agent` bridge is not an executable fallback. |
| 8 | Session-mirror reliability | D-APP-52 SDK session IDs and transcript placement; `frontend/docs/harness/runtime_engine_contract.md` | SDK session/transcript linkage is secondary. Loss, drift, or unavailability of that mirror must not replace canonical Chirality events or session identity. |
| 9 | Product-identity drift | `ScopeOfWork.md` DEL-04-01-REQ-015; DEL-01-03 product-boundary SOW; root product contracts | Claude and Anthropic names remain implementation metadata, not Chirality product identity or governance authority. |
| 10 | Platform dependency | D-APP-52 live probe `darwin:arm64`; packaged proof macOS binary path | Accept for the observed macOS arm64 demonstrator only. Windows, Linux, and other architectures remain unproven. |
| 11 | Reliance-boundary ambiguity | DEL-01-02 reliance-boundary SOW/register; `ScopeOfWork.md` residual-risk method | Accept only product-critical behavior that is observed, mapped, and fail-closed in Chirality terms. Opaque or unverifiable behavior triggers fallback. |
| 12 | Engine-adapter lock-in | `frontend/packages/harness-contract/src/agent-engine-port.ts`; provider-neutral runtime contracts | Accept the pinned SDK as the first adapter behind `AgentEnginePort`, while preserving the replaceable-engine boundary and custom-runtime fallback. |

## Fallback Triggers

Fallback to the custom-runtime path, or hold the affected capability, if any
of the following occurs and cannot be corrected and re-evidenced within the
pinned adapter boundary:

1. SDK or Claude Code behavior changes outside the pins without passing fresh
   contract regression and a fresh adoption ruling.
2. Shipped execution admits ambient user/local settings or cannot contain SDK
   config effects to the controlled posture.
3. Chirality cannot enforce deny precedence, human gates, path policy,
   redaction, or canonical event persistence independently of `allowedTools`
   and opaque SDK defaults.
4. SDK-specific messages, IDs, transcript paths, or permission terms become
   public or canonical Chirality contracts rather than adapter metadata.
5. Required terminal outcomes or session cleanup cannot be observed and
   persisted in Chirality-owned records.
6. The packaged subprocess cannot execute in the intended environment or
   requires an unaccepted signing, platform, path, storage, or distribution
   assumption.
7. Managed child execution cannot preserve sealed context and explicit read,
   write, and tool scopes without falling back to the retired SDK `Agent`
   bridge.
8. A product-critical reliance boundary remains opaque, unverifiable, or
   unable to fail closed in Chirality terms.

## Decision Boundary

The decision satisfies DEL-04-01's requirement to select and document a
version-pinned adapter verdict and its twelve residual categories. It does
not change the deliverable lifecycle (`IN_PROGRESS`), its Checking Approval
SHA, dependency states, frontend runtime source, provider/network scope, or
any release or professional-reliance gate.
