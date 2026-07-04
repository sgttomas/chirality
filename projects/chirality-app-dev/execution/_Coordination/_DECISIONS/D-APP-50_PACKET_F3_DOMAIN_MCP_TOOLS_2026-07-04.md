# D-APP-50 — PROPOSAL: F3 step 2 — domain MCP tools

**Status:** PROPOSAL / `AWAITING_RULING`. F3-crossing by design — this is D-T0-08 step (b), the second of the two owner-ruled PROPOSAL steps that open app-dev fence F3.
**Date:** 2026-07-04
**Decision ID:** D-APP-50
**Prepared by:** governance drafting agent, at owner direction; agents prepare packets labeled `PROPOSAL`, only the human project authority rules (K-AUTH-1; D-GOV-04; register preamble).
**Structural precedent:** D-APP-46 / D-APP-48 packet skeleton (verified-basis table, options table, recommendation with riders, scope constraints, open human ruling).
**Basis:** `_DomainEngines/_DECISIONS/D-T0-08_fence3_sequence.md` step (b); `_DomainEngines/_DECISIONS/D-T0-03_integration_level_staging.md` (per-operation risk grading); D-APP-49 (F3 step (a): `DomainEngineProfile`/`OperationProposal` source types packet, drafted in parallel under the same slate — the ruled-sequence prerequisite; `execution/_Coordination/_DECISIONS/D-APP-49_PACKET_F3_SOURCE_TYPES_2026-07-04.md`); DEC-041 harness-as-packages substrate and DEC-063 automation-condition-met declaration (`projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:619,641`); app-dev K-DOMAIN-1..4 (`docs/CONTRACT.md:131-141`).

This packet is a PROPOSAL only. **Nothing is implemented or exposed under this packet:** no tool name is registered, no descriptor is added, no MCP server code is written, no registry version is bumped, no catalog text is amended, and the reserved `mcp__chirality__domain_*` namespace stays reserved. Ruling this packet is the F3-step-2 owner act under D-T0-08. Even after a ruling, execution is additionally **sequenced**: the authorized tranche starts only after the D-APP-49 (step (a)) tranche has landed — D-T0-08 ruled the order sequential, "source types first, then domain MCP tools" — and only within D-T0-08's stated preconditions (D-T0-01 ruled; proven L2). No live binding, publication, lifecycle transition, or release/professional/certification/sealing/authentication/code-compliance claim is created.

## Decision to rule

Authorize (or decline) the **domain-MCP-tools tranche**: standing up governed `mcp__chirality__domain_*` in-process MCP tools in the app-dev harness — the R7-implementation act that D-T0-08 defines as F3 step (b) ("adding **domain MCP tools** (e.g. `piping_propose_operation`)", `D-T0-08_fence3_sequence.md:3`) — including which tools, in what order, under which gates, and what stays excluded.

The fence being crossed is D-APP-39 hard fence #3, verbatim: "R7 domain-engine implementation; PKG-10 stays future-boundary/doc-only." (`execution/_Coordination/_DECISIONS/D-APP-39_RULING_2026-06-20.md:33`; D-T0-08 cites this as `:26` — the line drifted to `:33` after the D-APP-44 F1 amendment expanded fence #1; the text is byte-identical). D-T0-08's verified facts state the specific act: "an OperationProposal-as-MCP-tool is R7 implementation" (`D-T0-08_fence3_sequence.md:7`). An MCP tool surface is exactly that act, so it cannot proceed under app-dev's autonomous latitude and requires this owner ruling.

## Why now

Every upstream member of the F3 opening set has moved except this step: the substrate is ruled and built
(D-APP-46 package extraction, D-APP-47 shim retirement, D-APP-48 pull mechanism — all RULED and landed);
the DEC-041 automation condition is owner-declared **met** (DEC-063, 2026-07-04); the proven-L2
demonstration tranche is scoped and ruled on the piping side (DEC-064, 2026-07-04); and step (a) — the
source-types packet D-APP-49 — is drafted in parallel under this same slate. Ruling D-APP-50 now completes
the two-packet decision set D-T0-08 requires, so the R7 build lane unblocks the moment the sequenced
preconditions land, without a further governance round-trip. Ruling it does not accelerate execution past
any precondition: riders 1-2 bind execution to the ruled order regardless of when the ruling is recorded.

## Verified basis

All rows cold-checked against the live tree 2026-07-04. Paths are repo-root-relative; app-dev-internal paths are relative to `projects/chirality-app-dev/`.

| Fact | Source |
|---|---|
| Reserved namespace, verbatim: "Chirality-owned in-process MCP tools use \`mcp__chirality__*\` adapter names. The future \`mcp__chirality__domain_*\` namespace is reserved for governed domain-profile tools and must not be implemented or exposed before the future domain-profile amendment." | `frontend/packages/harness-contract/src/tool-catalog.ts:110-112` ("Naming Boundary" section, `:108`) |
| Descriptor registry version constant, verbatim: `export const HARNESS_TOOL_REGISTRY_VERSION = 'harness-tools.v6.mutating-mcp';`. Descriptor shape `HarnessToolDescriptor` (name, surface, permissions, `pathScope`, idempotence, concurrency, provenance, `humanGate`, adapter, schemas, runtime). | `frontend/packages/harness-contract/src/tool-descriptor.ts:9` and `:80-101` |
| A `'reserved'` surface with a future-policy human gate already exists as the exact holding pattern for gated tools: `HarnessToolSurface = 'claude-agent-sdk-builtin' \| 'chirality-mcp' \| 'reserved'` (`:45`); `humanGate` gate union `'interactive-confirmation' \| 'approval-sha' \| 'future-policy'` (`:47-55`); precedents `web_fetch` (`:760`) and `web_search` (`:792`), both `surface: 'reserved'`, `humanGate: { required: true, gate: 'future-policy', … }`, descriptor-only runtime. | `frontend/packages/harness-contract/src/tool-descriptor.ts:45,47-55,760,792` |
| Tier-0 profile `deterministic_tools` (`:77-111`): `operation_applier.validate` — `mode: "proposal_validate"`, `requires_human_confirmation: false` (`:78-84`); `operation_applier.apply` — `mode: "proposal_apply"`, `requires_human_confirmation: true`, "K-DOMAIN-3: human acceptance required before any apply", "L3 only; gated" (`:85-90`); `completeness_checker` — `mode: "read_only"` (`:91-97`); `rule_check_runner` — `mode: "read_only"` (`:98-104`); `headless_runner` — `mode: "read_only"`, "validated-kernel runs (L2 candidate)", status "TOOLMAKER handoff — entrypoint not yet built" (`:105-111`). | `_DomainEngines/profiles/open_pipe_stress.yaml:77-111` |
| D-T0-03 HumanRuling, verbatim: "**(a) L3 is the destination**, reached risk-graded **per-operation** (engine-checkable vs engine-silent); staging L0→L1→L2→L3; L4 future-only. Human gate binds to `AnalysisStatus`." | `_DomainEngines/_DECISIONS/D-T0-03_integration_level_staging.md:16` |
| D-T0-08 step (b), verbatim: "(b) adding **domain MCP tools** (e.g. `piping_propose_operation`)" (`:3`); HumanRuling: "**(a) Sequential** — source types first, then domain MCP tools; not before D-T0-01 (ruled) + a proven L2. Each step its own PROPOSAL packet." (`:16`). | `_DomainEngines/_DECISIONS/D-T0-08_fence3_sequence.md:3,16` |
| K-DOMAIN-3, verbatim: "Domain operations require `OperationProposal` records and explicit human acceptance before application; accepted/applied transitions bind to human approval evidence per K-AUTH-2 and domain-engine-controlled apply or external terminal acceptance records. Specializes framework `K-DOMAIN-3`; MUST NOT weaken." K-DOMAIN-1/2/4 at `:138,139,141`; §1.10 pins framework canon at commit `77a327727605f05da5f304288f1ddd87dc09659d` (`:133-134`). | `docs/CONTRACT.md:140` (section `:131-141`) |
| Current state: **zero** `mcp__chirality__domain_*` tools exist. Grep over `frontend/` finds the string only in prose/reservation and rendered-doc contexts (`tool-catalog.ts` plus the generated `docs/harness/` catalog/tooling pages) — no registered tool anywhere; `tool-names.ts` registries contain no `domain_` entries (read names `:4-9`, mutating names `:11-14`, allowed-name template `:20-21`). | grep 2026-07-04; `frontend/packages/harness-contract/src/mcp/tool-names.ts:4-21` |
| DEC-041 rules the harness-as-versioned-packages substrate with the no-manual-toil execution condition; DEC-063 declares that automation condition **met** 2026-07-04 (D-APP-48 O-A pull mechanism), while stating it "does NOT open app-dev F3 (D-T0-08 sequence: proven L2, then source types, then MCP tools — each its own owner-ruled PROPOSAL)". | `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:619,641` |
| Proven-L2 status: DEC-064 rules the proven-L2 demonstration scoping (headless entrypoint tranche), but records that no L2 claim exists yet and the tier-0 "proven L2" acknowledgment is a separate act after evidence exists. | `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:642` |
| The four-layer tool declaration pattern this tranche would follow: (1) name registry `frontend/packages/harness-contract/src/mcp/tool-names.ts`; (2) descriptor + registry version `frontend/packages/harness-contract/src/tool-descriptor.ts`; (3) implementation `frontend/src/lib/harness/mcp/` (today: `read-tools.ts`, allowed-name-gated); (4) wiring via `frontend/src/lib/harness/tool-pool.ts` (`:9` imports `@chirality/harness-contract/tool-descriptor`) and `sdk-options-builder.ts` (`:10,13-15,140`). Rendered catalog `frontend/docs/harness/tool_catalog.md` is byte-checked against `renderHarnessToolCatalog()` by `frontend/src/__tests__/lib/tool-catalog.test.ts:9-10`. | files as cited |
| Substrate readiness: the dependency-free contract package `@chirality/harness-contract` exists (D-APP-46, RULED), in-repo importers were migrated and the shims retired (D-APP-47, RULED), and the intra-repo SHA-pinned pull mechanism is ruled and working (D-APP-48, RULED; pull contract `execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json`). | `_REGISTER.md` rows D-APP-46/47/48 and their ruling records |
| F3 fence text, verbatim: "R7 domain-engine implementation; PKG-10 stays future-boundary/doc-only." — hard fence #3 under "Hard Fences (always human-gated; never autonomous)" (`:21`). | `execution/_Coordination/_DECISIONS/D-APP-39_RULING_2026-06-20.md:33` |

## Options

| ID | Option | Consequence |
|---|---|---|
| **O-A** | **Staged read-first tool set under the reserved `mcp__chirality__domain_*` namespace**, strictly wrapping the tier-0 profile's `deterministic_tools` by risk grade; `operation_applier.apply` excluded (details below). | Opens F3 step (b) in the same conservative shape the tier-0 ladder rules: read tools first, proposal records second, apply never under this packet. Fits the existing descriptor/gate machinery with no new governance primitives. |
| **O-B** | **Full set in one step, including an apply tool.** | Rejected: violates D-T0-03's per-operation risk grading ("not wholesale", `D-T0-03:11,16`) and K-DOMAIN-3's human-acceptance-before-application conservatism; collapses the L2→L3 staging into a single exposure. |
| **O-C** | **Single generic `domain_tool` multiplexer** (one MCP tool dispatching on an `operation` argument). | Rejected: evades per-operation risk grading and descriptor-level gates — one descriptor cannot truthfully carry per-tool `humanGate`/`pathScope`/mode metadata for operations of different risk classes; defeats the registry's collision/gating tests. |
| **O-D** | **Defer.** | Leaves F3 step (b) unruled; the R7 build lane stays closed after step (a) lands; costless but forfeits the ruled sequence's momentum. |

## Recommendation

Recommend **O-A**, with the riders below as binding conditions of the ruling.

### Proposed O-A tool set

All tools live under the reserved namespace (adapter names `mcp__chirality__domain_*`), consume the D-APP-49 `DomainEngineProfile`/`OperationProposal` type contract, and wrap `_DomainEngines/profiles/open_pipe_stress.yaml` `deterministic_tools` one-to-one — no tool exists without a profile-declared deterministic tool behind it. D-T0-08's example name `piping_propose_operation` (`:3`) is realized generically as `domain_propose_operation` (profile-parameterized) so the namespace reservation, not an engine-specific prefix, governs.

**Tranche 1 — read-only (L1/L2-grade, `engine_checkable`-side, no confirmation flag at tier-0):**

- `domain_completeness_check` — wraps `completeness_checker` (`mode: read_only`, `open_pipe_stress.yaml:91-97`).
- `domain_rule_check_run` — wraps `rule_check_runner` (`mode: read_only`, `:98-104`; result shape `projects/chirality-piping/schemas/rule_check_run_result.schema.json`).
- `domain_headless_preview_run` — wraps `headless_runner` (`mode: read_only`, "validated-kernel runs (L2 candidate)", `:105-111`); exposable only once the DEC-064 entrypoint exists.

**Tranche 2 — proposal-record tools (write only to profile-approved agent-writable paths; nothing is applied):**

- `domain_propose_operation` — creates an `OperationProposal` **record** (lifecycle `draft`) in an agent-writable path per K-DOMAIN-2; it changes no domain truth.
- `domain_proposal_validate` — wraps `operation_applier.validate` (`mode: proposal_validate`, `requires_human_confirmation: false`, `:78-84`); validates a proposal record and returns the deterministic outcome; applies nothing.

**Excluded — `operation_applier.apply`** (`mode: proposal_apply`, `requires_human_confirmation: true`, "L3 only; gated", `:85-90`): no apply-capable MCP tool is proposed, named, or reserved-for-next under this packet. Any future apply exposure requires its own PROPOSAL packet, keeps the profile's `requires_human_confirmation: true`, sits at L3 per D-T0-03, and binds to K-DOMAIN-3 human-acceptance evidence per K-AUTH-2.

**Descriptor discipline:** every tool gets its own `HarnessToolDescriptor` carrying an explicit `humanGate` and `pathScope` per the existing shape (`tool-descriptor.ts:80-101`); tranche-1 tools are read-scoped; tranche-2 tools are write-scoped only to agent-writable proposal paths. `HARNESS_TOOL_REGISTRY_VERSION` bumps per its convention (v6 → a v7 identifier naming the change, mirroring `'harness-tools.v6.mutating-mcp'`). The existing collision/enumeration tests extend to the new names. Indicative descriptor sketch (final values are the executing tranche's to set, within these bounds):

| Tool | Wraps (profile tool, mode) | surface | pathScope | humanGate |
|---|---|---|---|---|
| `domain_completeness_check` | `completeness_checker`, `read_only` | `chirality-mcp` | `project-root-read` | `{ required: false }` (mirrors `requires_human_confirmation: false`) |
| `domain_rule_check_run` | `rule_check_runner`, `read_only` | `chirality-mcp` | `project-root-read` | `{ required: false }` |
| `domain_headless_preview_run` | `headless_runner`, `read_only` | `reserved` until the DEC-064 entrypoint + L2 acknowledgment exist, then `chirality-mcp` | `project-root-read` | `{ required: true, gate: 'future-policy', … }` while reserved |
| `domain_propose_operation` | none (record author; no deterministic tool invoked) | `chirality-mcp` | `project-root-write` (agent-writable proposal paths only, K-DOMAIN-2) | tranche sets; at minimum truthful `required` + reason |
| `domain_proposal_validate` | `operation_applier.validate`, `proposal_validate` | `chirality-mcp` | `project-root-write` (proposal record + validation outcome only) | `{ required: false }` (mirrors profile flag; validates, never applies) |

**Invocation transport — flagged honestly as an open design point:** the wrapped deterministic tools are piping-built Rust binaries (`impl:` paths in `open_pipe_stress.yaml:79,92,99,106`). The MCP implementation must NOT import piping source directly; cross-repo consumption goes through the ruled pull-contract substrate (D-APP-48 O-A / DEC-063). How the harness invokes the binaries at runtime — local child-process execution of pinned artifacts vs a sidecar per DEC-041's sidecar staging — is not settled by this packet; the executing tranche must settle it inside DEC-041's posture and record the choice, and may stop at descriptor-only (`reserved`-style) exposure for any tool whose transport is not yet sound.

### Riders (conditions of an O-A ruling)

1. **Sequence:** the tranche executes only after the D-APP-49 (step (a)) tranche has landed, and within D-T0-08's preconditions (D-T0-01 ruled; proven L2 — per DEC-064 the L2 evidence and its tier-0 acknowledgment are still pending, so `domain_headless_preview_run` and any L2-dependent exposure wait on them).
2. **Per-operation risk grading per D-T0-03:** tools are exposed by risk grade in the tranche order above, never wholesale; `operation_applier.apply` is excluded outright.
3. **Gates and quarantine:** every descriptor declares `humanGate` explicitly and respects K-DOMAIN-2 — no tool writes outside profile-approved agent-writable paths; protected domain paths stay write-quarantined.
4. **No piping core writes, no live-binding claim:** the tranche makes no claim that L3 is reached or that a live agent is bound; L2→L3 movement stays tier-0-governed (D-T0-03), and no `AnalysisStatus`-bound acceptance flow is implemented here.
5. **Execution hygiene:** branch-first; the app-dev check set (K-VALIDATE-1: `npm run test`, `typecheck`, `harness:validate:premerge`, `instruction-root:integrity`, `desktop:dist` as applicable) plus an adversarial review before merge.
6. **Reservation text:** the reserved-namespace sentence at `tool-catalog.ts:110-112` is amended only as part of the executed tranche (with the rendered catalog regenerated in the same change), never under this packet.

## Scope constraints (what an O-A ruling does NOT authorize)

- **No apply.** No `proposal_apply`-mode exposure, no apply tool name, no apply descriptor. K-DOMAIN-3 human acceptance before application stands unweakened (`docs/CONTRACT.md:140`); the profile's `requires_human_confirmation: true` on `operation_applier.apply` (`open_pipe_stress.yaml:87`) is not wrapped away.
- **No protected-path writes.** K-DOMAIN-2 quarantine holds: agents write proposals/summaries only in profile-approved agent-writable paths (`docs/CONTRACT.md:139`); no path hook is weakened.
- **No L3 claim, no live binding.** Integration level remains tier-0-governed (`open_pipe_stress.yaml:26`, `integration_level: "MANUAL_BRIDGE"`); this packet neither advances it nor binds a live agent to piping.
- **No F1/F2/F4 crossing.** No provider/network expansion beyond the ruled posture, no publication/distribution (the package stays `private:true` per D-APP-48 O-A), no `CHECKING -> ISSUED` issuance.
- **No piping-side writes.** Nothing under `projects/chirality-piping/` is edited; piping's own gates (D-21 lineage, DEC-042 non-consumption clause) are untouched.
- **No professional claims.** K-DOMAIN-4 (`docs/CONTRACT.md:141`): no output of these tools is represented as professional approval, code compliance, certification, sealing, authentication, or solver truth.
- **K-ENGINE-6 preserved.** The harness remains a governance/UI/audit/adapter layer; the domain tools are adapters over profile-declared deterministic tools, not a competing solver or agent harness.
- **No tier-0 authoring.** The tranche does not edit `_DomainEngines/` profiles or decisions; any profile change (e.g. `headless_runner` status) is a tier-0 act.

## Risks

- **Transport risk:** wrapping Rust binaries from a Node/Electron harness can smuggle in exactly the manual cross-repo toil DEC-041 forbids; mitigated by rider on pull-contract-only consumption and permission to hold tools at descriptor-only until transport is sound.
- **Scope-creep risk:** an MCP surface adjacent to `apply` invites "just one more mode"; mitigated by the explicit apply exclusion and O-C rejection (no multiplexer to hide behind).
- **Sequencing risk:** ruling this packet before the D-APP-49 tranche lands could tempt out-of-order execution; mitigated by rider 1 making the sequence a condition of the ruling itself.
- **Precondition risk:** D-T0-08's "proven L2" is not yet satisfied (DEC-064 records no L2 claim exists); exposing `domain_headless_preview_run` early would fake the precondition it depends on; mitigated by its `reserved`-until-acknowledged descriptor posture.
- **Vocabulary drift:** tool names/descriptors hard-coding piping-specific shapes would violate the generic-profile posture (K-DOMAIN-1); mitigated by profile-parameterized tools consuming the D-APP-49 types.
- **Risk-class immaturity:** `operation_risk_class` (`engine_checkable`/`engine_silent`) is a PROPOSED field not yet implemented in the engine (`open_pipe_stress.yaml:122-127`); descriptors must not pretend the engine enforces it; the grading is carried honestly as governance metadata until the engine lands it.
- **False-capability risk:** a registered-but-unwired tool could be read as a working capability claim; mitigated by the existing `runtime.exposedToModel:false` descriptor-only pattern (`web_fetch`/`web_search` precedent) and truthful catalog text.

## Validation implications

- Registry/collision tests must pass with the new names; the catalog test (`frontend/src/__tests__/lib/tool-catalog.test.ts:9-10`) forces regeneration of `frontend/docs/harness/tool_catalog.md` in the same change as any descriptor edit.
- `HARNESS_TOOL_REGISTRY_VERSION` consumers (D-APP-48 pull contract, piping D-30 consumption metadata, DEC-063 record) see a version change; the pull-contract validator must be re-run green and the pinned SHA advanced by the normal mechanism — the tranche must not silently break the recorded contract.
- The harness-contract package must stay dependency-free (D-APP-46 posture): names/descriptors go in the package; any transport/runtime code stays in `frontend/src/lib/harness/` runtime side.
- New tool behavior needs unit tests per tool (allowed-name gating, pathScope enforcement, refusal shapes) mirroring the existing `read-tools.ts` test coverage.
- Tranche-2 tools need fixture tests proving proposal records land only in profile-approved agent-writable paths and that a write attempt outside them is refused (K-DOMAIN-2 evidence, not just policy text).
- The descriptor `provenance.emits` events for domain tools must come from the existing `HarnessEventType` vocabulary or a governed vocabulary addition — event additions ride the same tranche, not ad hoc strings.
- No `docs/*` authority document is edited by this packet; if the executing tranche later touches authority docs (e.g. TYPES.md wording), the D-APP-38 corpus-version-bump rule applies to that tranche.

## Affected files (at execution only — this packet edits nothing)

On an O-A ruling, the executing tranche (after D-APP-49's tranche) would touch, per the four-layer pattern:

- `frontend/packages/harness-contract/src/mcp/tool-names.ts` — new `domain_*` name registry entries (likely a distinct domain-name array parallel to read/mutating).
- `frontend/packages/harness-contract/src/tool-descriptor.ts` — new descriptors + `HARNESS_TOOL_REGISTRY_VERSION` bump.
- `frontend/src/lib/harness/mcp/` — new `domain-tools.ts` implementation module beside `read-tools.ts` (allowed-name-gated, transport per rider).
- `frontend/src/lib/harness/tool-pool.ts` and `frontend/src/lib/harness/sdk-options-builder.ts` — pool/server wiring.
- `frontend/packages/harness-contract/src/tool-catalog.ts` — Naming Boundary prose amendment (rider 6) + regenerated `frontend/docs/harness/tool_catalog.md`.
- Tests: descriptor/collision suites, catalog test, new domain-tool unit tests.

## Human Ruling And Disposition

**Ruling recorded:** _Awaiting owner ruling._

## Ruling Mechanism

- The owner rules; agents never self-rule (K-AUTH-1; D-GOV-04).
- Register row `D-APP-50` is appended by the orchestrator as `AWAITING_RULING`; on ruling it moves to `RULED` with a separate `D-APP-50_RULING_<date>.md` record (two-file convention; register Decision Preparation Rules).
- An O-A ruling authorizes the tranche as scoped by the riders; execution begins only after the ruling **and** completion of the D-APP-49 tranche (ruled sequence, D-T0-08:16), within D-T0-08's preconditions.
- This packet edits nothing; approval is recorded only when the ruling record is added, and no broader implementation approval may be inferred than the ruling text grants.
