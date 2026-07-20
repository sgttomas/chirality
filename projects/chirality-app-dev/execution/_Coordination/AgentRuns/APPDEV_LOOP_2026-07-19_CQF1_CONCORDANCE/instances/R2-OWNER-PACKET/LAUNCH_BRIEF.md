# R2-OWNER-PACKET Launch Brief — D-APP-70 Candidate Owner Ruling Packet

- **Role:** RECONCILIATION (Agent 1; load and obey
  `agents/AGENT_RECONCILIATION.md`)
- **Parent/dispatcher:** HELP_HUMAN
- **RunID:** `APPDEV_LOOP_2026-07-19_CQF1_CONCORDANCE`
- **Instance:** `R2-OWNER-PACKET`
- **Basis:** `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- **Accepted dependency:** V1-RECHECK3 terminal `ACCEPT`, accepted by
  HELP_HUMAN for owner-decision routing only
- **Decision:** D-APP-70
- **Target state:** `AWAITING_RULING`
- **Repair authority:** none
- **W1 release authority:** none

## Objective

Prepare and register one governed D-APP-70 candidate owner ruling packet from
the accepted V1 evidence and unchanged candidate slate. Preserve all 22
`OWNER_CLASS` rows as proposals. Consolidate them into nine complete decision
groups with recommendations and real alternatives, append Receipt-78, and
leave an `AWAITING_RULING` handoff. Do not execute or infer an owner ruling.

## Mandatory preflight

Before any write:

1. require exact basis
   `57652ba1cd0905e8f47131e4c4ebf518272f7c16`;
2. recompute V1-RECHECK3 return/status hashes
   `28fd98d46a160016d6fd875ea0281c07ee85971054b4e7de45fbe9af83b62936`
   and `9f71e6d7604439f69d94c78cea66bbe0f1feb2924b06adfcc37e0b25e3274460`;
3. require terminal `ACCEPT`, zero blocking findings, no unknowns, no waivers,
   and the two exact fresh child return hashes
   `072d816045939e345a10ad837905b49153e6321d660bc72d153e5c2ca2f0d4fb`
   and `fa2572ce449004e846bf6684328db54a18affe23eef16c100df0aa7a041d93b3`;
4. recompute the unchanged 14-file activated-package binding recorded by V1,
   exactly as enumerated in this instance's released `STATUS.json`, including
   candidate slate
   `f6e630e9294c4779f87a0f7734667f565113127769cdaed3ab20b32cd099ce93`,
   proposed mapping
   `a01651fb49883d2f15971cbc8a85c5cff4c5039eeffb2500be6a78fd62378e86`,
   path ledger
   `b56f87731920765279639d528393bae212403fe49ffb5de6c27065ddd4095288`,
   and fidelity matrix
   `100445dd4e2054440776a60e1be36e53d7cdb0bf6cbe94b9e21555f420f1706c`;
5. prove 22 unique rows, all `OWNER_CLASS`, all unaccepted proposals, nine
   non-overlapping groups totaling `5+4+6+1+1+1+1+1+2=22`, and ordered
   manifest hash
   `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`;
6. require Receipt-77 is the latest receipt, D-APP-70 has no existing packet,
   register row, or ruling, and every shared write can be append-only; and
7. record a before-write containment inventory. Fail closed on any mismatch.

## Required D-APP-70 decision content

Create
`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-70_PACKET_CQF1_CANDIDATE_OWNER_RULING_2026-07-19.md`
as a `PROPOSAL` with status `AWAITING_RULING`. Bind the exact V1/package/slate
hashes above and state that V1 validates decision readiness, not ownership.

Present these nine numbered group decisions without dropping any retained
boundary:

1. **Shell integration and shared presentation (5).** Recommend the exact
   proposed mapping and DEL-02-01 as `globals.css` integration lead without
   semantic transfer. Alternatives must include ownerless/shared physical-file
   treatment, capability-level split, and deferral; retain every capability
   boundary named in the accepted slate.
2. **Working-root document UX (4).** Recommend DEL-02-03 primary for the four
   paths while retaining DEL-02-04 attachment UI state and DEL-09-06/server
   enforceable security. Alternatives must include a FilePicker carve-out or
   deferral; do not substitute DEL-06-04.
3. **Replay and projection (6).** Recommend DEL-05-04 primary for the six
   session/event projection paths while retaining DEL-05-02, DEL-05-05,
   DEL-06-01, and DEL-08-05 semantics. Alternatives must preserve shared
   application infrastructure for HarnessEventsProvider, split-by-capability
   or ownerless/shared treatment for harness-event views, and deferral.
4. **Working-root content route (1).** Recommend DEL-07-03 as nearest existing
   owner while retaining DEL-07-01 containment and DEL-02-03 consumption.
   Alternatives: another explicitly named physical route-contract integration
   owner or deferral.
5. **Catalog generation (1).** Recommend DEL-06-02 only for the generator/check
   mechanism, with generated-catalog semantics remaining distributed.
   Alternatives: an explicitly named shared tooling/integration owner or
   deferral; semantic centralization is not an option.
6. **Electron preload (1).** Recommend an explicit shared implementation
   boundary across DEL-02-03 `selectDirectory`, DEL-02-05 `apiKey`, and
   DEL-09-06 `safeStorage`/security, with a physical integration lead required
   before any repair. Alternatives: name one of those three deliverables as
   physical integration lead or defer; no semantic transfer may be implied.
7. **Network-policy fixture (1).** Recommend DEL-09-06 primary with a DEL-04-01
   evidence edge and an express no-packaged-proof caveat. Alternatives:
   DEL-04-01 primary with DEL-09-06 policy boundary, explicit shared fixture,
   or deferral.
8. **Contract dependency lint (1).** Recommend DEL-03-01 for the semantic lint
   with DEL-09-05 as release-quality consumer. Alternatives: an explicitly
   shared lint utility boundary or deferral.
9. **PEC evidence (2).** Recommend DEL-10-04 primary for both evidence-driver
   paths while retaining DEL-10-03 proposal-tool verification and F-APP-3.
   Alternatives: an explicit split by evidence-driver/proposal-tool function
   or deferral.

Conclude with a response surface:

- **Option A (recommended):** approve recommendations 1–9 exactly as stated;
- **Option B:** approve selected recommendations and explicitly name each
  group-level alternative/substitution; and
- **Option C:** defer all nine groups unchanged.

The packet must warn that partial owner wording applies only to named groups;
silence never selects a recommendation. It must list affected files and
validation implications and state that even a future mapping ruling does not
authorize repair, W1, lifecycle transition, release, publication, or a
hard-fence crossing.

## Registration, receipt, and handoff

After the complete packet is internally validated:

1. append exactly one `_REGISTER.md` row for D-APP-70 with subject, affected
   scope, status `AWAITING_RULING`, packet path, and no ruling path;
2. append exactly one Receipt-78 block to `LOOP_RECEIPTS.md`, with parent
   Receipt-77, exact evidence pointers/hashes, zero stale-map delta unless
   actually observed, checks run, model attribution, and Gate-Outcome
   `AWAITING_OWNER` explicitly identifying D-APP-70 as `AWAITING_RULING`;
3. write `HANDOFF.md` in this instance with accepted upstream hashes,
   derivative-package status, `AWAITING_RULING`, exact owner response syntax,
   W1/repair rerun requirements, and all remaining blockers; and
4. write `RETURN.md` plus terminal `STATUS.json`.

Return exactly `READY_FOR_OWNER_RULING | BLOCK`. On success, terminal status
must be `AWAITING_RULING`; this means packet preparation is complete, not that
the owner decision exists.

## Write authorization and prohibitions

Write only the new D-APP-70 packet, append-only register row, append-only
Receipt-78, and this instance's `HANDOFF.md`, `RETURN.md`, and `STATUS.json`.
Do not edit the activated package, 22 subject paths, Remaining containers,
prior R1/V1/evaluation records, plan/graph, authority, SOW/dependencies,
lifecycle state, any ruling file, W1 reservation, or Git state. Do not
delegate: this is a bounded packet/registration task with no independent
subject investigation or repair stage. Waivers: none.
