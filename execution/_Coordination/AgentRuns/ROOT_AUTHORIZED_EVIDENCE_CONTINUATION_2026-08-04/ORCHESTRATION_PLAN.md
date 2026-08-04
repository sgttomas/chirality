# Root authorized evidence continuation — orchestration plan

RunID: `ROOT_AUTHORIZED_EVIDENCE_CONTINUATION_2026-08-04`

Plan version: `1`

Selection authority: `HUMAN`

Descriptive posture: `TERMINAL_FAN_OUT_IN`

## Objective and accepted basis

Pursue the two evidence-only Root lanes that remain separately authorized
while the standing Root workplan remains idle:

1. refresh and re-ingest the Root `TM-ROOT-106` G1-B validation target against
   the owner-verified seven-hash App set; and
2. execute TM105 acquisition briefs AB-01 and AB-09 under the standing
   preparation-only posture.

The exact authority carriers are:

- App ruling
  `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/APP_RULING_JOINT_PI_G1B_TM_APP_039_TM_ROOT_106_V1_2026-08-03.md`,
  SHA-256 `48ecaa5753bbf021990fc121bcdbb3edfc7c39c0e43f4fee82398911fa3f6aff`;
- signed TM105 owner-return transcript
  `execution/_Coordination/AgentRuns/ROOT_SEMANTIC_RETURNS_2026-08-03/OWNER_RETURN_TRANSCRIPT_2026-08-03.txt`,
  SHA-256 `6396dd26c3fb8b6ed922c1cb7da584f67a08188d5b27525d650bf3ca1560c566`;
- TM105 Phase-1 handoff
  `execution/_Coordination/AgentRuns/ROOT_TM105_EVIDENCE_COLLECTION_2026-08-03/HANDOFF_STATE.md`,
  SHA-256 `03245133a99b8844950e9cc33c6c2b08ce20ae525ba7dbcad2223630b5c2e3a7`;
- current accepted repository state through merged PR #510 at
  `origin/main@cdc76a1d398231267f1379e7143b4de27abaa01b`.

## Nodes, dependencies, and ownership

| Node | Manager | Objective | Writes | Depends on | Expected return |
|---|---|---|---|---|---|
| H1 | HELPS_HUMANS | Materialize an immutable G1-B refresh/re-ingest derivative against the seven ruled hashes; preserve every Pi/PIA hold. | `instances/H1-TM106-G1B-REFRESH/`; new immutable `g1b_refresh_2026-08-04/` only | accepted H4 target; App ruling | validated refresh package, exact drift/re-ingest report, blocker and rerun handoff |
| H2 | HELPS_HUMANS | Execute AB-01 threat-model and AB-09 DEL/compatibility evidence acquisition with explicit UNKNOWNs. | `instances/H2-TM105-AB01-AB09/` only | TM105 Phase-1 carrier; accepted DEL-02-06 V2 in exact scope | validated AB-01/AB-09 evidence carrier, Agent-2 fan-in evidence, blocker and rerun handoff |

H1 and H2 may run concurrently because their write scopes are disjoint. They
must not edit the Task Management register, loop receipts, current workplan,
accepted contracts, runtime/product source, App/Piping surfaces, or each
other's directories.

## Fan-in gate and human decisions

HELP_HUMAN accepts only manager-validated terminal returns whose hashes and
write containment reproduce. H1 must preserve `TM-ROOT-106=OPEN`,
`PIA-U30=HELD_NO_DISPATCH`, the operative D-APP-72/SCA-APP-002 basis, and the
absence of Pi approval or Electron supersession. H2 must preserve all TM105
semantic and implementation holds and must not present a byte gate.

Human decisions remain required for any Pi approval/supersession, PIA-U30
dispatch, owner/vendor/platform fact selection, TM105 semantic bytes,
implementation, lifecycle, release, reliance, or merge. A later plan version
must add any integration or CHANGE node after terminal fan-in.

## Failure isolation

Failure or blockage in one node does not stop the other. Any basis drift,
authority conflict, shared-write need, substantive semantic choice, or scope
expansion returns to HELP_HUMAN without implementation.
