# PEC Task Management — deferral review follow-on

**Status:** DECISION SUPPORT — OWNER RULING REQUIRED

**Date:** 2026-08-02

**Mode:** deferral review

**Invoking loop:** PEC

**Register:** `_DomainEngines/pec/_TaskManagement/REGISTER.csv`, schema 1.0,
SHA-256 `c2f9ba5acde10f6ba7f152761445205971a00f883721575c274d6767fe7a773e`

**Repository state reviewed:** branch head
`50f9b892b465f4b55a8fabcb181e84dc318e18a6`; `origin/main`
`4a162adb1ee4c318859501eecd3d987ad974b4eb`

**Authority:** Decision support only. This report classifies every live PEC
row whose `Status=DEFERRED`; it does not trigger, activate, dispatch, amend,
close, archive, reprioritize, assign, or otherwise disposition a row. The two
handoff packages cited below are undelivered drafts inside the PEC register
home. No foreign surface was written.

## Federation preflight

The mandatory read-only federation preflight completed before this review:

- coverage: `COMPLETE`;
- canonical registers discovered and validated: 4 (`PEC`, `ROOT`, `APP`,
  `PIP`);
- PEC live state: 6 `OPEN`, 2 `DEFERRED`, 0 `ELEVATED`, 0 `CLOSED`, with 2
  archived rows;
- invalid, unreadable, or ambiguous registers: 0; and
- federation observation: one unrelated `REMOTE_CLOSED_LOCAL_OPEN`
  relationship between `TM-PIP-023` and `TM-ROOT-053`; it does not involve a
  PEC row.

The preflight wrote no authoritative state.

## TRIGGER_FIRED

None.

Neither deferred row has its recorded closure trigger satisfied. In
particular, a now-existing v2 service-core source surface is not the
DEL-01-05 enforcement artifact and does not itself close DEL-01-06 RF-001;
and DEL-01-06's replaceable local registry default is not the owner ruling
required by OI-003.

## ACTIVATABLE

### TM-PEC-009 — DEL-01-06 deferred VER-005 review obligation

**Classification:** `ACTIVATABLE`

**Recorded trigger:** DEL-01-05 enforcement becomes available; closure then
requires the DEL-01-06 SELF_CHECK rerun closing RF-001 with exact evidence
(`VER-005` is not waived).

**Trigger assessment:** Not fired. DEL-01-05 remains `INITIALIZED`; its
current folder contains a production contract and support/run-record
surfaces, but no produced enforcement artifact. DEL-01-06 RF-001 remains
`DEFERRED`. The condition can now be pursued through bounded PEC instruments:
D-PEC-75's earlier reason for not selecting DEL-01-05 was the absence of an
established v2 core, while the repository now contains a typed core port and
replaceable config adapter. That new source surface removes the earlier
physical bootstrap absence but grants no source authority and does not cure
the stale DEL-01-05 contract by itself.

**SourceRef + SourceSha:**

- `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/Review_Findings.csv`,
  row `RF-001` — SHA-256
  `fa04561fe97cc33cc8198ef2f5dfa31b4c92f4aff41d591556e312f1e2e735bb`;
- `projects/pec/execution/_Coordination/D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/EXECUTION_HANDOFF.md`,
  SELF_CHECK disposition and remaining gates — SHA-256
  `65064ec696ce57cb743ca50a99abef52ac58746a2fd04f820149ab71442e130d`;
- `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_STATUS.md`
  — SHA-256
  `f7cb08a6e229b6195a239547c09b47f00cdccd73a723f93ea05a8cb25feae9d9`;
- `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/ScopeOfWork.md`
  — SHA-256
  `ce51490178a4e07f4266a09e156e2b8d7bca618a41477f57eb746b4596b49824`;
- `projects/pec/execution/_Coordination/D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/PACKET.md`,
  “DEL-01-05 guard-first” — SHA-256
  `065241b87fe97b8b8227ef4e9ad09d74baa6b8b04043779018ae00c7aa10e300`;
- `projects/pec/v2/src/pec_v2/core/ports/loop_registry.py` — SHA-256
  `3d5862bef122af27d61883fe5542b80daefb3418bccfba31486e4d60289b3662`;
  and
- `projects/pec/v2/src/pec_v2/adapters/config/loop_registry.py` — SHA-256
  `7101740dea837e6077e048ec2a8ef8600c7d1014bd339915aaea285b8236eb2f`.

**Named instruments:**

1. the PEC Agent 0 D-PEC packet route, to present a separately owner-ruled
   DEL-01-05 contract-currency and source-production packet with exact paths,
   acts, verification, rollback, and authority fence;
2. `WORKING_ITEMS`, only after that ruling, to perform the bounded contract
   repair and authorized production;
3. `REVIEW`, to run DEL-01-05's governed checklist and owner gates; and
4. `REVIEW` again, after DEL-01-05 enforcement is available, to reopen
   DEL-01-06 RF-001 and rerun SELF_CHECK against exact enforcement evidence.

**Draft handoff package:**
`_DomainEngines/pec/_TaskManagement/DRAFT_HANDOFF_TM-PEC-009_DEL-01-05_ENFORCEMENT.md`.

**Proposed register posture pending instrument completion:** retain
`DEFERRED`; the recorded trigger remains accurate. No automatic closure
follows from authorizing or completing DEL-01-05 production: closure still
requires the DEL-01-06 SELF_CHECK rerun to close RF-001 with exact evidence.

### TM-PEC-010 — OI-003 long-term loop-registry home and shape

**Classification:** `ACTIVATABLE`

**Recorded trigger:** The owner initiates the PRD §16 ruling on OI-003's
long-term registry home and shape; DEL-01-06's replaceable local default is
not that ruling.

**Trigger assessment:** Not fired. `SOW-077` remains `TBD` with `OI-003`
open, while the implemented PEC-local JSON configuration remains explicitly
replaceable. No external prerequisite prevents presenting the owner decision
now. The PEC D-PEC packet route can prepare the bounded decision; if the
ruling changes accepted decomposition truth, the resulting amendment must be
routed separately through `SCOPE_CHANGE` rather than written by Task
Management.

**SourceRef + SourceSha:**

- `projects/pec/execution/_Decomposition/ScopeLedger.csv`, row `SOW-077` —
  SHA-256
  `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5`;
- `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`, row `OI-003` —
  SHA-256
  `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`;
- `projects/pec/execution/_Coordination/D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/EXECUTION_HANDOFF.md`,
  final paragraph — SHA-256
  `65064ec696ce57cb743ca50a99abef52ac58746a2fd04f820149ab71442e130d`;
- `projects/pec/v2/config/loops.json` — SHA-256
  `e24db354841e1b33d3ec4f74330351deaa7a18df0e0cd9e26bde248b6aed503e`;
- `projects/pec/v2/config/loops.schema.json` — SHA-256
  `1f4d1f0cf9abe5754ebb4260f588dea0d71e7f3cc37af2487b30b9c4aa39ba9b`;
- `projects/pec/v2/src/pec_v2/core/ports/loop_registry.py` — SHA-256
  `3d5862bef122af27d61883fe5542b80daefb3418bccfba31486e4d60289b3662`;
  and
- `projects/pec/v2/src/pec_v2/adapters/config/loop_registry.py` — SHA-256
  `7101740dea837e6077e048ec2a8ef8600c7d1014bd339915aaea285b8236eb2f`.

**Named instruments:**

1. the PEC Agent 0 D-PEC packet route, to present the PRD §16.3/OI-003
   owner decision faithfully without selecting for the owner; and
2. `SCOPE_CHANGE`, only if the owner ruling changes the accepted
   `SOW-077`/decomposition truth or establishes a cross-loop home requiring
   governed integration.

**Draft handoff package:**
`_DomainEngines/pec/_TaskManagement/DRAFT_HANDOFF_TM-PEC-010_OI-003_RULING.md`.

**Proposed register posture pending the ruling:** retain `DEFERRED`. The
recorded trigger is sufficiently exact and needs no sharpening. Once the
owner initiates and rules the decision packet, the closure disposition should
be selected from the ruling's actual effect: ordinarily
`RESOLVED_BY_DECISION`, or `SUPERSEDED_BY_SCOPE_CHANGE` if the ruling instead
opens and transfers the issue into a governed SCA.

## STILL_BLOCKED

None.

Both rows await owner-routable PEC work, not an unavailable external event.
This classification does not authorize either workstream.

## Owner ruling gate

The owner may rule whether either `ACTIVATABLE` package is to be routed. Until
then:

- `TM-PEC-009` and `TM-PEC-010` remain unchanged and `DEFERRED`;
- no manager or specialist is dispatched;
- neither draft handoff is delivered;
- no foreign loop surface is written; and
- no row is eligible for `taskmgmt archive` because neither row is closed.

## Owner ruling and routing outcome

The owner ruled the follow-on review on 2026-08-02:

The verbatim ruling is recorded at
`projects/pec/execution/_Coordination/TASK_MANAGEMENT_DPEC_REQUESTS_2026-08-02/OWNER_RULING.md`,
SHA-256
`ce96dcaf8f73b9c9cb6963b372fc72df3080378bd9ccc9d8551efd41583efe78`.

| Row | Classification and retained state | Authorized route |
|---|---|---|
| `TM-PEC-009` | `ACTIVATABLE` confirmed; retain `DEFERRED` with its trigger unchanged. Authorizing or completing DEL-01-05 production does not close the row; closure requires the DEL-01-06 SELF_CHECK rerun closing RF-001 with exact VER-005 evidence. | The draft handoff was authorized for delivery through the PEC Agent 0 D-PEC packet path as `projects/pec/execution/_Coordination/TASK_MANAGEMENT_DPEC_REQUESTS_2026-08-02/REQUEST_TM-PEC-009_DEL-01-05_PACKET.md`. Packet preparation and presentation occur at the owner's cadence. |
| `TM-PEC-010` | `ACTIVATABLE` confirmed; retain `DEFERRED` with its trigger unchanged. Closure disposition follows the future ruling's actual effect; any decomposition change routes separately through `SCOPE_CHANGE`. | The draft handoff was authorized for delivery through the same D-PEC packet path as `projects/pec/execution/_Coordination/TASK_MANAGEMENT_DPEC_REQUESTS_2026-08-02/REQUEST_TM-PEC-010_OI-003_PACKET.md`, with faithful presentation and no pre-selection. |

No register row changed because the owner retained both statuses and both
triggers exactly. No archive operation ran because neither row is closed. The
two routed requests ask Agent 0 to prepare future owner packets; they do not
themselves mint D-PEC IDs, draft those packets, dispatch another manager, or
open production.
