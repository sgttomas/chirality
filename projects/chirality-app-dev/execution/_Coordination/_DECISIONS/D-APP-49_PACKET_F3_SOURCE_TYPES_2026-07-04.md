# D-APP-49 — PROPOSAL: F3 step 1 — DomainEngineProfile / OperationProposal source types

**Status:** PROPOSAL — this packet confers no authority, implements nothing, and rules
nothing. Only the human project authority rules (K-AUTH-1; D-GOV-04). Ruling this packet
is itself the owner act that opens F3 step (a); nothing opens, and no source file changes,
under the packet itself.
**Date prepared:** 2026-07-04
**Decision ID:** D-APP-49
**Prepared by:** agent at owner in-session direction ("execute the DEC-064 tranche now, in
this session, then stage the L2-acknowledgment CHANGE and both F3 PROPOSAL packets while
the evidence is fresh" — `_DomainEngines/bridge/CHANGE_PREP_2026-07-04_proven_l2_acknowledgment.md:12-14`).
**Structural precedent:** D-APP-46/D-APP-48 packet skeleton; ruling sections per the eight
2026-07-04 piping PROPOSAL packets and D-32 (open human-ruling section + ruling mechanism).
**Basis:** `D-T0-08` (F3 opening sequence), `D-T0-01` (canonical contract shape),
`DEC-064`/piping `D-32` (proven-L2 tranche in-flight this PR; owner acknowledgment staged
as a separate tier-0 act).
**Paths:** `docs/`, `execution/`, and `frontend/` citations are relative to
`projects/chirality-app-dev/`; `agents/`, `tools/`, `_DomainEngines/`, and
`projects/chirality-piping/` citations are repo-root-relative.

The fence being stepped through, verbatim
(`execution/_Coordination/_DECISIONS/D-APP-39_RULING_2026-06-20.md:33`):

> 3. R7 domain-engine implementation; PKG-10 stays future-boundary/doc-only.

## Decision to rule

Whether to authorize F3 **step (a)** of the D-T0-08 ruled sequence — standing up
`DomainEngineProfile` / `OperationProposal` **source types** in the app-dev frontend — and
in which location and shape. D-T0-08 rules the sequence sequential: "source types first,
then domain MCP tools; not before D-T0-01 (ruled) + a proven L2. Each step its own
PROPOSAL packet" (`_DomainEngines/_DECISIONS/D-T0-08_fence3_sequence.md:16`); "standing up
source types crosses F3" (`:7`). Step (b), domain MCP tools, is **not** in scope here — it
stays a separate later packet (D-APP-50 lane).

## Verified basis

All rows checked cold 2026-07-04 at the current tree.

| Fact | Source |
|---|---|
| F3 fence text: "R7 domain-engine implementation; PKG-10 stays future-boundary/doc-only." (D-T0-08 cites this at `:26`; the line drifted to `:33` after the D-APP-44 F1 amendment; text unchanged.) | `execution/_Coordination/_DECISIONS/D-APP-39_RULING_2026-06-20.md:33` |
| D-T0-08 RULED: F3 scope = "(a) standing up `DomainEngineProfile`/`OperationProposal` source types in `frontend/src`, and (b) adding domain MCP tools" (`:3`); sequential, each step its own PROPOSAL packet, not before D-T0-01 + a proven L2 (`:16`). | `_DomainEngines/_DECISIONS/D-T0-08_fence3_sequence.md:3,:7,:16` |
| D-T0-01 RULED: framework-root persona canonical; app-dev conforms DOWN; its richer `OperationProposal` merged UP (FM-04). | `_DomainEngines/_DECISIONS/D-T0-01_precedence.md:3,:20` |
| PRD fence texts: "Generic `DomainEngineProfile` contracts" out of current-release scope (`:239`); §8.17 domain engines not part of current release (`:717`); §9.4 `DomainEngineProfile`/`OperationProposal` are future-amendment interfaces (`:807-808`); §9.5 `/api/domain/*` endpoint families provisional, not current-release (`:819-830`); R7 heading "— Future Amendment" (`:1452`). | `docs/PRD.md:239,:717,:807-808,:819-830,:1452` |
| PLAN fence texts: R7 "— Future Amendment" heading (`:277`); §11 out-of-scope until amendment: "Domain-engine operation execution." / "Direct protected-domain-path writes by agents." (`:452-453`). | `docs/PLAN.md:277,:452-453` |
| CONTRACT §1.10: K-DOMAIN-1..4 specialize framework `docs/CONTRACT.md` §1.12 at commit `77a327727605f05da5f304288f1ddd87dc09659d` and MUST NOT weaken (`:133-134`); K-DOMAIN-1..4 rows (`:138-141`). | `docs/CONTRACT.md:131-141` |
| Boundary checklists: Scope row keeps "R7 domain-engine implementation" behind its hard fence (`:25`); SB-06 red-flags work that "implements R7 domain engine behavior" (`:50`). | `docs/BOUNDARY_REVIEW_CHECKLISTS.md:25,:50` |
| TYPES §11 doc-only boundary sentence: "It is documentation only. It does not stand up source types, domain MCP tools, protected-path hooks, domain runtime, or operation-application behavior." — the exact line step (a) crosses. Conforms to `agents/AGENT_DOMAIN_ENGINE.md` @ `77a327727…` (`:501-502`). | `docs/TYPES.md:501-504` |
| Canonical shape: the persona's Minimal Domain Engine Profile Shape (YAML, `:693-748`) is the `DomainEngineProfile` source; the persona's `OperationProposal` shape is its separate "Valid Operation Proposal" section. App-dev field tables are the conformance mirrors — §11.1 `DomainEngineProfile` (canonical snake_case form; `:509-510`, table `:512-529`), §11.2 `OperationProposal` 20-field table (`:537-558`). | `agents/AGENT_DOMAIN_ENGINE.md:693-748` (profile shape) + its "Valid Operation Proposal" section; `docs/TYPES.md:506-529,:531-558` |
| Deterministic field lists/enums: `CONTRACT_SOURCE = "agents/AGENT_DOMAIN_ENGINE.md@77a327727"` (`:56`); required string/list fields (`:62-76`), deterministic-tool fields (`:78-84`), operation-contract fields (`:86-91`); enums for profile status, integration level, tool mode, risk class, lifecycle order (`:93-130`). | `tools/validation/validate_domain_engine_profile.py:56,:62-130` |
| Package home: `@chirality/harness-contract`, version `0.0.0-private`, `private: true`; barrel `src/index.ts` re-exports 10 modules; `src/types.ts` `UIEvent` union (`:206`) with `harness:event` passthrough member (`:269`); `src/event-schema.ts` `HARNESS_EVENT_TYPES` = **43** members (last `runtime.mirror.error`); `src/sdk-version.ts:1` `FLOW_A_CONTRACT_VERSION = 'flow-a.contract.v0.1.0'` (D-T0-09). | `frontend/packages/harness-contract/package.json`; `frontend/packages/harness-contract/src/{index.ts,types.ts,event-schema.ts,sdk-version.ts}` |
| Reserved step-(b) namespace: "The future `mcp__chirality__domain_*` namespace is reserved for governed domain-profile tools and must not be implemented or exposed before the future domain-profile amendment." | `frontend/packages/harness-contract/src/tool-catalog.ts:110-112` |
| No `DomainEngineProfile`/`OperationProposal` TypeScript types exist today: grep over `frontend/src/**` and `frontend/packages/**` (`*.ts`/`*.tsx`) returns zero hits — F3 is un-opened; the vocabulary is doc-only. | grep, 2026-07-04 |
| Precondition state: D-T0-01 RULED (above). Proven-L2 evidence lands in this PR under `DEC-064` (piping D-32 O-A, TP-RUNNER-014): PROVISIONAL entrypoint `projects/chirality-piping/core/runner/headless/src/bin/headless_preview_runner.rs` + validated-kernel fixture run witness `projects/chirality-piping/validation/witness/generated/tp_runner_014_headless_entrypoint_preview_run.json`. The owner's proven-L2 **acknowledgment is staged, not given**: tier-0 CHANGE prep + register row `D-T0-10` (HumanRuling OPEN), owner act pending. | `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:642` (DEC-064); `_DomainEngines/bridge/CHANGE_PREP_2026-07-04_proven_l2_acknowledgment.md:1-44`; `_DomainEngines/_DECISIONS/_REGISTER.md` row D-T0-10 |
| Shim retirement (bears on location choice): D-APP-47 RULED — importers migrated to direct `@chirality/harness-contract` imports; `frontend/src/lib/harness/` re-export shims retired. | `execution/_Coordination/_DECISIONS/_REGISTER.md` row D-APP-47; `D-APP-47_RULING_2026-07-04.md` |

## Options

| ID | Option | Consequence |
|---|---|---|
| **O-A** | **Two type modules in `@chirality/harness-contract`.** Add `src/domain-profile.ts` and `src/operation-proposal.ts` to `frontend/packages/harness-contract/`, re-exported from the barrel `src/index.ts`. Field-for-field mirrors of the framework-root persona @ `77a327727…` as tabulated in `docs/TYPES.md` §11.1/§11.2, preserving the canonical snake_case field names and the validator's enums/lifecycle order. **Types + type guards only** — no runtime behavior. D-T0-08 `:3` says "in `frontend/src`"; the package is that surface's ruled successor (D-APP-46 extraction + D-APP-47 shim retirement), and this deviation is surfaced here for the owner to rule, not assumed. | Opens F3 step (a) at the smallest honest surface: the contract spine gains the domain vocabulary as inert types. Excluded: no MCP tools (step (b) / D-APP-50; `mcp__chirality__domain_*` stays reserved per `tool-catalog.ts:110-112`), no `/api/domain/*` endpoints (PRD §9.5 stays provisional), no protected-path hooks, no piping import or coupling, no new members in `HARNESS_EVENT_TYPES` (stays 43; the `harness:event` passthrough in `types.ts:269` already covers future domain event flow), package stays `private: true` / `0.0.0-private`, `FLOW_A_CONTRACT_VERSION` untouched. |
| **O-B** | **Types in `frontend/src/lib/harness/` instead of the package.** Literal reading of D-T0-08 `:3` "in `frontend/src`". | Rejected shape: re-fragments the extracted contract spine and contradicts D-APP-47's shim retirement — `frontend/src/lib/harness/` was just emptied of contract material in favor of the package. Would recreate the drift D-APP-46/47 removed. |
| **O-C** | **Types plus a domain sources registry / domain eventing in one step.** Add the type modules and wire a profile registry, domain event members, or endpoint stubs. | Rejected: exceeds step (a) and pulls step-(b)-adjacent surface (tool/eventing/runtime) forward, against the D-T0-08 sequential ruling and the K-ENGINE-6 adapter/contract posture. |
| **O-D** | **Defer (status quo).** | The R7 build lane stays closed although both D-T0-08 preconditions are ruled or evidence-complete-pending-acknowledgment. Doc-only vocabulary continues to drift-risk against a live validator contract. |

## Recommendation

Recommend **O-A**, with riders:

1. **SHA-pinned mirror source.** The module doc comments pin the mirrored contract source:
   `agents/AGENT_DOMAIN_ENGINE.md@77a327727605f05da5f304288f1ddd87dc09659d` (canonical per
   D-T0-01) with `docs/TYPES.md` §11 as the app-dev conformance mirror, matching the pin
   already carried by `docs/CONTRACT.md:133-134` and
   `tools/validation/validate_domain_engine_profile.py:56`.
2. **Doc-contract mirrors only.** The modules export types and type guards — no behavior,
   no persistence, no UI, no I/O, no imports. K-ENGINE-6 posture (adapter/contract, not a
   harness or solver) is unchanged.
3. **Execution waits for the L2 acknowledgment.** The owner may rule this packet at any
   time, but the implementing tranche executes only after the owner's proven-L2
   acknowledgment is recorded (D-T0-08 `:16` precondition; the acknowledgment is the staged
   tier-0 act in `_DomainEngines/bridge/CHANGE_PREP_2026-07-04_proven_l2_acknowledgment.md`).
4. **Invariants carry through unchanged.** K-DOMAIN-1..4 (`docs/CONTRACT.md:138-141`) and
   the professional boundary (K-DOMAIN-4; SB-06) are not weakened or restated. The
   `docs/TYPES.md:503-504` "documentation only" sentence receives a forward-note edit
   **only as part of the executed tranche** (it becomes factually stale the moment types
   exist), never under this packet.
5. **Execution hygiene.** Branch-first; the app-dev check set green (`npm run typecheck`,
   `npm run test`, `harness:validate:contract-deps`, `harness:validate:premerge`); close
   with an adversarial review.

## Risks

- **Mirror drift.** The persona could move past `77a327727…`, silently orphaning the TS
  mirror. Mitigation: rider 1's in-file SHA pin makes staleness detectable; any re-pin is
  a visible diff reviewed against D-T0-01 canon.
- **Types read as implementation.** Inert types could invite premature step-(b) work
  ("the types exist, wire a tool"). Mitigation: rider 2; the reserved
  `mcp__chirality__domain_*` namespace text stays in force; SB-06 red-flag wording already
  catches R7 behavior.
- **Sequence violation.** Executing before the acknowledgment is recorded would breach
  D-T0-08's precondition even with a ruling in hand. Mitigation: rider 3 makes the
  ordering explicit in the ruling itself.
- **Shape divergence.** Hand-transcription could diverge from the validator's field
  lists/enums. Mitigation: mirror the tabulated fields exactly (TYPES §11.1/§11.2;
  `validate_domain_engine_profile.py:62-130` incl. the order-exact lifecycle tuple); type
  guards assert the same enums.
- **Location misread.** O-A's package location deviates from D-T0-08's literal
  "`frontend/src`" wording. Mitigation: surfaced above; the ruling text should name the
  package location explicitly so the deviation is owner-ruled, not agent-assumed.

## Validation implications

- The package's dependency-free lint (`harness:validate:contract-deps`) must stay green:
  the two new modules import nothing (no React/Next/Electron/Node/SDK, no piping).
- `npm run typecheck` and the vitest suite must pass; `harness:validate:premerge` must
  stay green.
- Type-guard unit tests follow the existing convention: the package has no in-package test
  files today — its modules are tested from `frontend/src/__tests__/` via
  `@chirality/harness-contract` subpath imports (e.g.
  `frontend/src/__tests__/components/harness-stream-views.test.ts`). New guard tests land
  there, not inside the package.
- No `HARNESS_EVENT_TYPES` change → no event-vocabulary count reconciliation is triggered
  (the count stays 43).
- The executed tranche's `docs/TYPES.md` forward-note is a `docs/*` authority-doc edit and
  therefore triggers a D-APP-38 corpus version bump; this packet alone triggers none.

## Affected files (PROPOSAL — not applied by this packet)

On O-A, the implementing tranche — after ruling **and** the recorded L2 acknowledgment —
would touch:

- `frontend/packages/harness-contract/src/domain-profile.ts` (new; types + guards).
- `frontend/packages/harness-contract/src/operation-proposal.ts` (new; types + guards).
- `frontend/packages/harness-contract/src/index.ts` (two re-export lines).
- `frontend/src/__tests__/` (type-guard tests per the existing package-test convention).
- `docs/TYPES.md` §11 forward-note (rider 4; triggers the D-APP-38 corpus bump).

Explicitly untouched: `event-schema.ts`, `tool-descriptor.ts`, `tool-catalog.ts`,
`mcp/tool-names.ts`, `sdk-version.ts` (`FLOW_A_CONTRACT_VERSION`), the package
`package.json` (`private`/version), `frontend/src/app/**` (no `/api/domain/*`), all hook
surfaces, and everything under `projects/chirality-piping/`.

## Human Ruling And Disposition

**Ruling recorded:** **O-A** — two type modules in `@chirality/harness-contract`, riders 1-5
adopted as binding conditions; the package-location deviation owner-ruled (owner, Ryan Tufts,
in-session 2026-07-04, via the run steer quoted verbatim in the ruling record; as-recommended
reading per the Receipt 20/21 precedent). Ruling record:
`execution/_Coordination/_DECISIONS/D-APP-49_RULING_2026-07-04.md`. The rider-3 precondition —
the recorded proven-L2 acknowledgment — was recorded the same session as `D-T0-10` before any
tranche execution.

## Ruling Mechanism

Per existing practice, the human project authority selects an option (with any
riders/edits) or rules directly. Register row `D-APP-49` (to be appended to
`execution/_Coordination/_DECISIONS/_REGISTER.md` as `AWAITING_RULING` by the
orchestrator) then moves to `RULED` with a separate
`execution/_Coordination/_DECISIONS/D-APP-49_RULING_<date>.md` record per the two-file
convention. The implementing tranche executes only after that ruling **and** the owner's
recorded proven-L2 acknowledgment (rider 3). Step (b) — domain MCP tools — remains a
separate, later PROPOSAL packet (D-APP-50 lane) per the D-T0-08 sequence. This packet
edits nothing: no register row, no source file, no authority doc, no tier-0 file.
