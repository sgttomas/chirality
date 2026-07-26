# APP-HOLD-1 Candidate Handoff

Status: `READY_FOR_OWNER_CANDIDATE_REVIEW`  
Closure verdict: `PREPARATION_COMPLETE_HOLD_NOT_APPLIED`  
Prepared: 2026-07-26  
Accepted upstream basis: OD-1 preparation approval; Git
`918bb48b8fcee66c031d0d6d4040a46089f96067`

## Result

The exact APP-HOLD-1 candidate is staged entirely inside this proposal
directory. No live App instruction, contract, validator, workflow profile,
status, dependency record, decision, or SOW basis changed.

The deterministic live scan found 53 contracts and classified exactly six as
held:

| Deliverable | Package | Reason |
|---|---|---|
| `DEL-02-01` | `PKG-02` | `416b29033bbacb0bc3648d84033272b7ab4e6e11` does not resolve |
| `DEL-02-02` | `PKG-02` | same |
| `DEL-02-04` | `PKG-02` | same |
| `DEL-05-04` | `PKG-05` | same |
| `DEL-08-02` | `PKG-08` | same |
| `DEL-08-03` | `PKG-08` | same |

`SCAN_RESULT.json` records `PASS`, `held_count=6`, and exact register parity.
The corrected candidate regression suite passed 12/12 tests.

## Exact candidate surfaces

- `CANDIDATE.md` — proposed authority, semantics, boundaries, and no-repin
  posture.
- `APP_HOLD_REGISTER.csv` — six-row machine-readable held-contract register.
- `tools/app_hold.py` — runnable scan and target/operation gate.
- `tests/test_app_hold.py` and `tests/fixtures/` — positive and negative
  regression evidence.
- `INTEGRATION_CONTRACT.md` — exact proposed live placement, App instruction
  clause, WORKING_ITEMS preflight, lifecycle/dependency use, fan-in
  validation, workflow integrity check, and closure tests.
- `D-APP-75_RULING_TEMPLATE.md` — durable App-loop application authority
  template; remains non-ruling until exact owner text and candidate identity
  are transcribed.
- `SCAN_RESULT.json` and `TEST_RESULT.txt` — live-basis evidence.
- `ARTIFACT_HASHES.sha256` — candidate identity list.

## Proposed application surfaces

If the exact candidate is accepted, the separately authorized application
would be limited to:

1. live App hold register under `execution/_Coordination/`;
2. live deterministic tool and tests under `execution/_Scripts/`;
3. root and project-local deterministic-tool catalog entries;
4. D-APP-75 ruling materialization and the App decision-register row;
5. the exact App `AGENTS.md` instruction clause;
6. the `app-hold-integrity` registered check and `always_checks` entry in
   `software-workflow.json`; and
7. run-local preflight and fan-in evidence produced by future App work.

Application would not change any `ScopeOfWork.md` basis, repin a contract,
advance lifecycle, or authorize Root/App architecture changes.

## Remaining owner gate

DecisionID: `OD-1-APP-HOLD-1-EXACT-CANDIDATE`  
RequestedBy: `HELPS_HUMANS` through `HELP_HUMAN`  
Question: Whether to accept and apply the exact APP-HOLD-1 candidate.  
Options: accept exact candidate application; return bounded amendments; or
decline/defer.  
Recommendation: accept exact candidate application because the scan matches
the reviewed set, the prohibition is entry-path independent, the enforcement
fails closed, unaffected work remains eligible, and no unverifiable provenance
is invented.  
Evidence: this packet, especially `SCAN_RESULT.json`, `TEST_RESULT.txt`, and
`INTEGRATION_CONTRACT.md`.  
DownstreamBlocked: application of APP-HOLD-1 and any reliance on the six held
contracts.

Owner acceptance of preparation alone does not activate the hold. Exact
candidate bytes must be approved before any live application.
