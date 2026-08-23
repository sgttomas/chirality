# SCA-004 R3 transcription and Gate-5 package handoff state

Status: `AWAITING_OWNER_GATE_5_APPEND_APPROVAL`

## Four-state handoff

| State | Value |
|---|---|
| Accepted upstream state | R1-C records Gate 1 accepted; R2-A records Gate 2 accepted; R3-A approves the exact seven Gate-3 candidate bytes plus exact diff/validation/preview; R3-B approves the Gate-4 propagation plan with CONDITION R3-B-1. Live SOFTWARE decomposition revision 1.2 remains accepted at SHA-256 `23f6ae0f…64f3d`; `_LATEST.md` remains SCA-002 at SHA-256 `b2849c6e…80a1`. |
| Authoritative truth state | `UNCHANGED` — Gate 5 is not executed. No live decomposition/companion register, pointer, folder, SOW, lifecycle, dependency, estimate, schedule, runtime, tool, App, or held-binding byte changed. |
| Derivative package state | `Gate_5_Application_Append.diff` is the exact draft application append over the R3-A-approved bytes; `Gate_5_Applied_Candidate/` and `Gate_5_Applied_Preview.md` identify the resulting seven surfaces; `Gate_5_Validation.json` records deterministic package validation. `Gate_5_Brief.md` and `Gate_5_Pointer_Candidate.md` remain drafts. |
| Closure / next state | `OPEN_PENDING_OWNER_GATE_5_APPEND_APPROVAL`; after append approval, Gate-5 execution authorization is a separate owner act; pointer authority remains separate. Next owner is Ryan Tufts through HELP_HUMAN. |

## Fixed state fields

| Field | Value |
|---|---|
| AmendmentID | `SCA-004` |
| DecompositionTruthState | `INCOMPLETE` — owner-approved revision 1.3 bytes exist only in the snapshot; live revision 1.2 is unchanged |
| DerivativePackageState | `INCOMPLETE` — exact Gate-5 package drafted and validated; append-byte approval and execution authorization remain pending |
| ContentRemediationState | `NOT_REQUIRED` |
| DownstreamRerunState | `FROZEN` — no application, PREPARATION, SOW, dependency, estimate, schedule, graph, audit, implementation, pointer, or App act is authorized |
| MetadataAlignmentState | `NOT_REQUIRED` |
| AuditState | `NON_BLOCKING_PASS` — original Gate-3 validator PASS 98/98 in a clean scratch Phase-0c layout with byte-identical protected JSON; Gate-5 validator PASS 64/64 with zero failures; applied-state Gate-3 equivalent PASS 98/98 |
| ReadyForNextPhase | `NO` |
| ClosureVerdict | `OPEN_PENDING_OWNER_GATE_5_APPEND_APPROVAL` |

## Exact approved candidate and applied preview identities

| Surface | R3-A-approved SHA-256 | Applied-preview SHA-256 |
|---|---|---|
| Working surface | `0696190db9fb9319ccee40232d1a5ed77133030fea1361716ae1c05c4d8a9641` | `546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986` |
| Deliverable register | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` |
| Scope ledger | `54287bad4a9561e7dc38bea305ecb232ce081d51d49c05b94d8d86a44017a3cc` | `63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417` |
| Objective register | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` |
| Forward trace | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` |
| Reverse trace | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` |
| Coverage telemetry | `316185be54ec75f0ddaad847a00427a9051527ce9b94019cad2a3b4c2120d765` | `bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c` |

Applied topology remains 53 deliverables: PKG-02=12, PKG-04=11, packages=6,
scope items=104, objectives=7, zero unmapped IN items, zero unsupported
objectives, and zero untraced reverse units.

## Derivative-package state

| Package | Owner | Status | Evidence | Next required action |
|---|---|---|---|---|
| Exact Gate-3 candidate | SCOPE_CHANGE | `APPROVED_BY_OWNER_R3-A_NOT_APPLIED` | protected Gate-3 files and R3-A record | Preserve exact bytes until separately authorized Gate 5. |
| Gate-4 propagation plan | SCOPE_CHANGE | `APPROVED_BY_OWNER_R3-B_WITH_CONDITION_R3-B-1` | protected plan/action bytes and R3-B record | Condition package returns to owner. |
| Gate-5 application append | SCOPE_CHANGE | `AWAITING_OWNER_APPROVAL` | slot inventory, exact append, applied preview, deterministic validation | Owner approves, corrects, or declines exact append bytes. |
| Gate-5 execution | SCOPE_CHANGE | `NOT_AUTHORIZED` | `Gate_5_Brief.md` draft | After append approval, owner separately authorizes or declines execution. |
| Pointer candidate | SCOPE_CHANGE | `DRAFT_REQUIRES_OWN_AUTHORITY` | `Gate_5_Pointer_Candidate.md` | Owner rules only after Gate-5 confirmation. |
| Live decomposition package | SOFTWARE_DECOMP / SCOPE_CHANGE | `CURRENT_REVISION_1_2_UNCHANGED` | seven protected live SHA-256 identities | Later authorized Gate-5 act only. |
| Downstream folders/SOWs/dependencies/estimates/schedule/graph/audits | owning workflows | `NOT_STARTED_NOT_AUTHORIZED` | approved plan only | Later acts under their own authority. |

## Held bindings and blockers

All ten DEL-02-06 compatibility objects remain `HELD_UNAVAILABLE`.

1. Owner approval of the exact `Gate_5_Application_Append.diff` bytes.
2. Separate owner authorization of Gate-5 execution.
3. Separate owner authority for `_LATEST.md` pointer treatment after Gate-5 confirmation.
4. TM-ROOT-106 and TM-ROOT-122 remain unchanged G1 blockers; no pin change.
5. PREPARATION INIT, SOW, context propagation, dependency, estimate,
   schedule, graph, audit reruns, implementation, App work, cutover, release,
   C1 artifact download, and every hold lift remain unauthorized.

## Rerun requirements

- Before Gate 5, reverify the seven live basis and seven approved candidate
  SHAs, then require a fresh zero-failure Gate-5 validation.
- Apply only after append-byte approval and separate Gate-5 authorization,
  following `Gate_5_Brief.md` exactly.
- Run the owner-approved closure lane, then return applied state to Ryan
  Tufts for Gate-5 confirmation.
- Do not update `_LATEST.md` absent its own accepted authority.

## Repair evidence — legacy live invocation

During parent fan-in, the protected Phase-0c validator was invoked directly
in the live Phase-0d tree. It returned 98 checks with one expected failure at
`gate5_artifacts_absent` because this tranche's Gate-5 draft artifacts were
present, and it rewrote its report. This was a validator-context mismatch,
not a product or candidate failure. The protected report was restored exactly
to SHA-256 `dc5fe4355322a96b7da61606fff7d8dd51943a7d606f132966705bfb70b9f129`.
The original validator now runs only in a clean scratch Phase-0c layout;
the applied-state equivalent remains the separate 98-check run described in
`validate_gate5_package.py`.

## Next owner

Ryan Tufts through HELP_HUMAN: decide the exact append bytes. Approval of
those bytes does not itself authorize Gate-5 execution or pointer treatment.
