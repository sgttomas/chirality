# D-APP-68 — Scoped Concordance Rulings and Governed Repair Authorization

**Status:** RULED — owner approval 2026-07-19, transcribed verbatim below

**Decision ID:** D-APP-68

**Date:** 2026-07-19

**Ruled by:** Ryan Tufts (K-AUTH-1), demonstrator scope

**Recording basis:** `96563e8e09b89908e13e6b2f1f1139aca3283855`

**Discovery basis:**
`execution/_Reconciliation/DeliverableConcordance/SCOPED_D65_CONCORDANCE_2026-07-19/`
(agent-authored derivative evidence, not authority), produced under D-APP-65
disposition 7 from the accepted D-APP-55/R6 snapshots.

## Authority and evidence trace

- D-APP-56 ruling and its immutable draft-packet basis:
  `execution/_Coordination/_DECISIONS/D-APP-56_RULING_2026-07-12.md`
  (R4-P28/R4-P32 ruled in §4) and
  `execution/_Reconciliation/DeliverableConcordance/RUN_D55_CONCORDANCE_2026-07-11_1904Z/PROPOSED_DECISION_FINDINGS.md`
  (the exact P28/P32 option text).
- D-GOV-14 item 7:
  `docs/governance_harness/_DECISIONS/D-GOV-14_pr188_review_closure.md`.
- D-GOV-16 items 5 and 7:
  `docs/governance_harness/_DECISIONS/D-GOV-16_deliverable_scope_of_work_stage2.md`.
- D-APP-65 owner-role assignment and scoped-pass authorization:
  `execution/_Coordination/_DECISIONS/D-APP-65_PACKET_ACCEPTED_RECOMMENDATIONS_2026-07-18.md`.
- D-APP-52 transport authority and D-APP-67 Option-B limit:
  `execution/_Coordination/_DECISIONS/D-APP-52_RULING_2026-07-06.md` and
  `execution/_Coordination/_DECISIONS/D-APP-67_PACKET_SECRET_REGISTRY_REDACTION_TAXONOMY_2026-07-18.md`.
- DEL-04-01's twelve-area requirement and live version-pinned evidence:
  `execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/ScopeOfWork.md`
  (DEL-04-01-REQ-015) and sibling
  `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`.

## Owner ruling

The owner approved the eight recommendations after the agent presented the
numbered slate, answered two follow-up questions, corrected recommendation 5,
and expressly reported the earlier Pipeline suggestion as stale. The words
below are the owner's complete ruling text; the chronology and corrected
meanings are bound in the next section.

<!-- BEGIN OWNER RULING VERBATIM -->
I approve recommendations 1–8.
<!-- END OWNER RULING VERBATIM -->

**Canonical ruling-text SHA-256:**
`0b4e3c7e32d09fe0230595d98141ed70b8cd41ebc2162292442155f702384218`
(32 UTF-8 bytes between the markers, excluding the marker lines and delimiter
newlines).

## Chronology-bound dispositions

1. **Legacy CLM blocks remain live normative content.** Quotation formatting
   introduced by the `chirality-deliverable-sow/v1` migration does not make
   the migrated content inert history. Repair the eight PKG-00/01 contradiction
   rows identified by the scoped concordance pass. Preserve genuinely dated
   history, but add a current-state note or update the live cell so it cannot
   still assert a false current state.
2. **No redundant standalone D-APP pointer merely for D-GOV-16.** D-GOV-16
   already authorizes the Scope-of-Work conversion. D-APP-68 may and does cite
   D-GOV-16 because this packet is the governed home of the omnibus ruling; it
   is not a second conversion authorization. Annotate live dangling citations
   to deleted `Datasheet.md`, `Specification.md`, `Guidance.md`, and
   `Procedure.md` locations with their current `ScopeOfWork.md` CLM location.
   Prior immutable concordance ledgers and historical extraction records stay
   unchanged.
3. **One consolidated managed-orchestration ownership mapping; no new
   deliverable.** The implemented surface is distributed to its nearest
   existing owners as follows:

   | Surface | Owning deliverable | Boundary |
   |---|---|---|
   | Optional managed-delegation fields persisted in `SessionRecord` | DEL-05-01 | Session identity/canonical folder semantics remain unchanged. |
   | `coordination.notice`, `coordination.update`, and `coordination.acknowledged` event vocabulary | DEL-05-02 | Provider-neutral append-only `HarnessEvent` ownership only. |
   | `artifacts/subagents/` child-output persistence | DEL-08-05 | D-APP-56 R4-P32 already assigns both the child-output storage path and its 16 KiB/512 KiB policy to the child-run record owner. DEL-05-05 retains only the distinct ordinary tool-result `descriptor.resultBudget` and ToolResultStore semantics. |
   | `coordination` descriptor permission class and `harness-permission.v7.coordination-mode` | DEL-06-01 | Deny-first mode/capability mapping. |
   | Four registered coordination MCP tool descriptors/catalog entries | DEL-06-02 | Registry, descriptor, and validation ownership. |
   | Co-location/composition of the coordination tools on the in-process Chirality MCP server | DEL-06-03 | Composition boundary only; it does not duplicate DEL-06-02 descriptor ownership. |
   | Managed-child declared read/write path enforcement | DEL-06-04 | Symlink-safe path-policy ownership. |
   | Managed-child Bash scope gate | DEL-06-05 | Bash policy ownership; arbitrary Bash remains serialized under the project-root read/write-scope rule. |
   | Managed child lifecycle, parent linkage, declared-context/write-target linkage, and replayable child-run records | DEL-08-05 | Record/lifecycle ownership; admission and delegation mechanism stay with DEL-08-04. |

4. **DEL-08-04 reflects the active delegation path.** D-GOV-14 item 7 is the
   governing decision: the record-less SDK `Agent` bridge is retired, and
   managed child sessions are the sole executable app-harness delegation path.
   Refresh DEL-08-04 so `delegate_agent` is the active mechanism, the SDK
   `Agent` tool is not model-visible in the current posture, and hierarchical
   parent/child eligibility remains consistent with root `AGENTS.md`.
5. **Child-output thresholds — confirmed no-op.** The initially presented
   recommendation was corrected before the owner's approval: D-APP-56 R4-P32
   already made 16 KiB inline and 512 KiB artifact-backed child-output limits
   normative solely under DEL-08-05. DEL-05-05 expressly does not duplicate
   that policy and instead owns `descriptor.resultBudget` plus tool-result
   artifact storage semantics. No threshold ruling, source edit, or ownership
   transfer is authorized by this item.
6. **Bash timeout values ratified.** DEL-06-05 owns and shall state the live,
   test-pinned policy: default `120000` ms and maximum `600000` ms.
7. **PEC credential/cookie envelope hygiene belongs to DEL-05-03.** Record
   the D-APP-52 transport-envelope practice and D-APP-67 Option-B limit: PEC
   credentials/cookies stay out of returned envelopes by construction, while
   the runtime logger remains API-key-specific and does not gain a generic
   secret registry. This is documentary ownership only; it authorizes no
   runtime redaction expansion.
8. **DEL-04-01 adoption verdict:** `ADOPT_WITH_RESIDUAL_RISK`, version-pinned
   to `@anthropic-ai/claude-agent-sdk@0.3.150` and the observed Claude Code
   `2.1.150`, for this repository's demonstrator scope. It is not release
   approval, issuance, certification, professional acceptance, signing,
   notarization, publication, or external distribution.

## DEL-04-01 live evidence and twelve residual-risk areas

The verdict consumes the D-APP-52 live-probe evidence rather than erasing its
limits. The live dev probe on `darwin:arm64` observed the SDK sequence
`system/init -> assistant -> assistant(tool_use Read) -> user(tool_result) ->
assistant -> result/success`, SDK session IDs, result keys, controlled
`CLAUDE_CONFIG_DIR` transcript placement, 401 and unreachable-base-URL shapes,
and abort behavior. The packaged proof observed an SDK-backed Read turn with
the platform binary under `app.asar.unpacked`. RATE_LIMITED was not triggered
live; D-APP-65 separately accepted unit-level simulated coverage for the
DEL-04-05 four-class criterion.

The required twelve-area appraisal is:

| # | Residual-risk area | D-APP-68 assessment |
|---|---|---|
| 1 | SDK API drift | Accept with pin and regression-on-upgrade requirement. The verdict does not float to later SDK/Claude Code versions. |
| 2 | Settings leakage | Accept with `settingSources: []` shipped posture and controlled config roots; SDK-created config files remain an observable substrate effect. |
| 3 | Allowed-tools misconception | Accept only with Chirality deny policy, mode policy, hooks, `canUseTool`, and human gates; `allowedTools` alone is never the restriction boundary. |
| 4 | Transcript location | Accept with SDK transcript/store data secondary and Chirality JSONL canonical; the observed path under `CLAUDE_CONFIG_DIR/projects/` is adapter metadata. |
| 5 | Electron packaging | Accept for the demonstrated unsigned local `darwin:arm64` packaged path with `app.asar.unpacked`; no signing, notarization, distribution, or other-platform claim. |
| 6 | SDK security boundary | Accept with the SDK/subprocess treated as privileged implementation substrate behind product-owned permission, path, redaction, and event boundaries. |
| 7 | Subagent inherited permissions | Accept only through managed child sessions with sealed context and explicit scopes; the retired record-less SDK Agent bridge is not an executable fallback. |
| 8 | Session-mirror reliability | Accept with SDK session/transcript linkage secondary; loss or drift of the SDK mirror must not replace canonical Chirality events or session identity. |
| 9 | Product-identity drift | Accept with Claude/Anthropic implementation metadata kept out of Chirality's product identity and governance authority. |
| 10 | Platform dependency | Accept for the observed macOS arm64 demonstrator only; Windows, Linux, and other architectures remain unproven by this evidence. |
| 11 | Reliance-boundary ambiguity | Accept only where product-critical behavior is observed, mapped, and fail-closed in Chirality terms; opaque or unverifiable behavior remains a fallback trigger. |
| 12 | Engine-adapter lock-in | Accept as the pinned first adapter behind `AgentEnginePort`/product contracts; preserve the replaceable-engine boundary and custom-runtime fallback. |

## Explicit refutation/no-op: Pipeline ownership

The earlier derivative slate's Pipeline scaffold suggestion is refuted and
was not part of the operative eight-item slate. D-APP-56 R4-P28 already
assigns the PIPELINE Execution Root Scaffold and co-resident contract/lifecycle
panels to DEL-02-02. Receipt-74 records the authorized render-test obligation
as executed. D-APP-68 authorizes no PKG-02 dispatch, ownership change, or
source edit for this item.

## Execution authorization and fences

The exact repair graph is frozen in the derivative package
`execution/_Reconciliation/DeliverableConcordance/SCOPED_D65_RULING_EXECUTION_2026-07-19/`.
Only its manifest-listed documentary writes are authorized. The five package
slices are disjoint and may execute after RECONCILIATION fan-in accepts the
manifest. Prior concordance ledgers, decomposition truth, frontend runtime
source, lifecycle state/Approval SHA, loop receipts, and completion log are
outside package-manager scope. No new deliverable, provider, network,
domain-engine apply/accept, release, issuance, or professional-reliance scope
is authorized.
