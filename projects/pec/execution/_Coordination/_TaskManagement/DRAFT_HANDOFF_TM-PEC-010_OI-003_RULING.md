# DRAFT — PEC handoff package for TM-PEC-010

**Delivery status:** ROUTED BY OWNER RULING — 2026-08-02

**Routed request:**
`projects/pec/execution/_Coordination/TASK_MANAGEMENT_DPEC_REQUESTS_2026-08-02/REQUEST_TM-PEC-010_OI-003_PACKET.md`

**From:** PEC TASK_MANAGEMENT

**To:** PEC Agent 0 / D-PEC packet route

**Register row:** `TM-PEC-010`

**Purpose:** Prepare the owner-ruling packet required by PRD §16.3 / OI-003
for the long-term home and shape of the loop registry, without treating the
DEL-01-06 PEC-local default as the decision.

## Accepted and implemented basis

- `SOW-077` remains `TBD`; OI-003's disposition path remains “§16 ruling”.
- DEL-01-06 implemented a replaceable local default at
  `projects/pec/v2/config/loops.json`, validated by a schema and consumed
  through a typed core port plus JSON adapter.
- D-PEC-75 expressly left the long-term home/shape, later loop entries, and
  consumer activation open.
- PEC's accepted DEL-00-01 architecture uses ports-and-adapters / hexagonal
  isolation and states that no governed act depends on PEC-held state. The
  OI-003 ruling must preserve that authority boundary and imposes no
  architecture on another loop.

## Bound evidence

| EvidenceRef | EvidenceSha |
|---|---|
| `projects/pec/execution/_Decomposition/ScopeLedger.csv`, row `SOW-077` | `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5` |
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`, row `OI-003` | `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` |
| `projects/pec/execution/_Coordination/D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/EXECUTION_HANDOFF.md` | `65064ec696ce57cb743ca50a99abef52ac58746a2fd04f820149ab71442e130d` |
| `projects/pec/v2/config/loops.json` | `e24db354841e1b33d3ec4f74330351deaa7a18df0e0cd9e26bde248b6aed503e` |
| `projects/pec/v2/config/loops.schema.json` | `1f4d1f0cf9abe5754ebb4260f588dea0d71e7f3cc37af2487b30b9c4aa39ba9b` |
| `projects/pec/v2/src/pec_v2/core/ports/loop_registry.py` | `3d5862bef122af27d61883fe5542b80daefb3418bccfba31486e4d60289b3662` |
| `projects/pec/v2/src/pec_v2/adapters/config/loop_registry.py` | `7101740dea837e6077e048ec2a8ef8600c7d1014bd339915aaea285b8236eb2f` |
| accepted DEL-00-01 `artifacts/v2/ADRs.md` | `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5` |

## Requested D-PEC decision packet

The packet should present, without selecting for the owner, at least these
faithful decision shapes:

1. **PEC-local long-term registry.** Confirm the existing PEC-owned home and
   typed shape as the long-term authority for which loops PEC serves, while
   preserving adapter replaceability and graceful absence. State how later
   loop entries are proposed, validated, accepted, and consumed without
   granting PEC authority over those loops.
2. **Shared contract with loop-owned contributions.** Define a shared typed
   contract while each loop remains authoritative for its own declaration and
   PEC consumes an assembled or adapted view. This option must name the
   prospective owning loop/instrument, reciprocal contract, absence behavior,
   compatibility and migration gates, and must not write or impose policy on
   another loop before that loop's own ruling.
3. **Continue the replaceable local default and defer the long-term shape.**
   Keep `SOW-077` open, but record a sharper future trigger and the interim
   limits: no later-loop activation, consumer duty, cross-loop authority, or
   inferred permanence.

The packet may present a materially distinct owner-authored option, but it
must keep the current local default and the long-term authority decision
separate.

For each option the packet should name:

- authority owner and source of truth;
- typed contract and compatibility/versioning behavior;
- proposal, validation, acceptance, and removal path for a loop entry;
- read/write boundary, absence/failure posture, and whether any governed act
  could become dependent on PEC-held state;
- exact current and prospective paths;
- migration and rollback;
- effects on DEL-01-06 and future consumers; and
- whether the ruling changes accepted `SOW-077` decomposition truth.

## Instrument routing after the ruling

- A ruling that merely selects the long-term decision may close
  `TM-PEC-010` as `RESOLVED_BY_DECISION`, citing the exact decision record.
- A ruling that changes accepted decomposition truth must prepare an SCA
  intake and route it to `SCOPE_CHANGE`; Task Management must not amend
  `ScopeLedger.csv` or `SOFTWARE_DECOMP.md`. The row may be closed as
  `SUPERSEDED_BY_SCOPE_CHANGE` only when the owner explicitly transfers the
  issue into that governed SCA and exact evidence is recorded.
- An option that assigns work or authority to another loop requires a routed
  notice with reciprocal citations and that loop's own ruling. This draft is
  not that notice and has not been delivered outside PEC.

## Non-effects of this draft

Routing this draft does not mint a D-PEC ID, select a registry home or shape, make the
local JSON file permanent, amend decomposition, create cross-loop authority,
dispatch any instrument, activate another P1 node, accept artifacts, alter
lifecycle, authorize release, or change `TM-PEC-010`.
