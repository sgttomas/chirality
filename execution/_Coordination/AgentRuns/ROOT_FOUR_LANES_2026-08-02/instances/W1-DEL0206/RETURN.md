# W1 WORKING_ITEMS return — DEL-02-06 accepted-turn recovery

Status: `PLANNING_PACKAGE_COMPLETE_NOT_ADOPTED — HANDOFF_READY_FOR_HUMAN_GATE — NOT_CLOSED`

## W6 terminal post-N0 planning continuation

Parent plan 12 released the complete post-N0 planning graph after the C4
current-main guard. W6 revalidated all frozen W5/N0 evidence; ran actual
concurrent N1/N2/N3 Agent 2 sessions; accepted N4 sole-writer attempt 3 after
two fresh read-only verifier returns were repaired only by N4 and rechecked;
accepted fresh N5-R3 `ADMIT` with 18/18 inputs, zero findings, zero writes, and
zero repair; and accepted N6's exact three-file owner-gate handoff.

The decision-ready handoff is `handoff/OWNER_GATE_HANDOFF.md`, SHA-256
`bf8020460d475c0e101c8675bf5721cc1358299e3e5b799ecead9901eb74d151`.
Its one-entry manifest SHA-256 is
`53d9a00764fb870f812142e4f8c10b371d838539ead6e00b502ef44647e13770`
and verifies. The verdict is `PLANNING_PACKAGE_COMPLETE_NOT_ADOPTED`; closure
is not claimed. The exact next gate is accountable-human semantic review, not
implementation. No runtime/client/project write, executable test, profile or
check adoption, semantic inference, lifecycle, release, reliance, Task
Management, Git, or foreign-loop effect occurred.

All subsequent sections describe historical W1-W5 states and are superseded
for the current handoff by this W6 terminal continuation.

## W5 terminal continuation

Exact manifest `360f8f12…d508f` is owner-accepted and copied byte-identically
to RunID-local `accepted_inputs/`; acceptance/live validation passes.

Actual fresh child `/root/w1_del0206/n0_r2_w5` returned
`RELEASE_N1_N2_N3` with 26/26 PASS and no findings. WORKING_ITEMS accepted
child return `ca8c1b18…ac522` and basis report `e11d4c28…7cd8`. This is a
validated release recommendation only: parent plan 11 requires W5 to stop
after N0, so N1 through N6 remain held and undispatched.

## Historical W4 terminal regeneration

Against exact corrected and Gate-1-confirmed current basis, W4 regenerated
the six-file candidate under `packet_candidate/`. The current exact
CandidateSetManifestSHA256 is
`360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f`.
Content-only validation passes, full validation passes twice with identical
output, and all 20 isolated negative cases reject as expected.

The sole exact owner-token form for the current candidate is:

```text
ACCEPT DEL-02-06 INPUT PACKET 360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f — Ryan Tufts 2026-08-03
```

The old W3 manifest `dd007522…53cf` was never accepted and is stale
derivative history, preserved in
`packet_presentation/STALE_CANDIDATE_HISTORY.md`. No acceptance record,
`accepted_inputs/`, or N0 dispatch exists.

## Historical W3 terminal continuation

The exact six-file current-basis candidate now exists at the RunID-local
`packet_candidate/` directory. Its exact candidate-set manifest identity is
`dd0075229486b98a5b28936ce55ea94e0fcbb6c8d5befc2f453cff78f6d053cf`.
Content-only and full validation pass; the full result reproduced twice with
byte-identical JSON, and all 20 isolated negative cases rejected as expected.

The historical matching token form was the following; it is stale and MUST
NOT be used for acceptance:

```text
ACCEPT DEL-02-06 INPUT PACKET dd0075229486b98a5b28936ce55ea94e0fcbb6c8d5befc2f453cff78f6d053cf — Ryan Tufts 2026-08-03
```

Manager disposition: `DEFER`, not accept. The candidate binds live
decomposition SHA-256 `69bdb9ca…1278c`; fresh audit SHA-256
`0c49c5e1…630a5` marks `COV-POST-001` blocking. A separately approved
three-location correction will change that decomposition hash, invalidate
this candidate basis, and require regeneration, revalidation, and presentation
of a new manifest. N0 remains blocked even if this packet were accepted now.
No acceptance record, `accepted_inputs/`, or N0 dispatch exists.

Exact presentation and currency record:
`packet_presentation/PRESENTATION_RECORD.md` under the DEL-02-06 RunID root.

## Plan-v4 continuation return

Owner continuation ruling SHA-256
`9b98fe3dc6f8d9abb53c5b087e666cd17d53569ea0f39f1dea489534c9ebf6b6`
authorizes a fresh six-file current-basis candidate, not reconstruction of the
missing historical bytes. W2 completed the preparatory blueprint only.
This final digest replaces the provisional pre-normalization digest; the
correction changes provenance only and has no semantic effect.

Blueprint root:
`execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-RUNTIME-SPEC-001/packet_blueprint/`.

Key immutable observations and hashes:

| Artifact | SHA-256 |
|---|---|
| `ACTIVATION_RECORD.md` | `c3b3bd769dbbef545075e2cf98742d883e94767308fcd6b4b0585a94f6df19f2` |
| `packet_blueprint/README.md` | `a43bec79357e8dbc81ef9cb830298a6c7c4059455af9f7078e56d15db3ab3b7b` |
| `packet_blueprint/PROVENANCE_CONTRACT.md` | `89f0abf6d6d0e05d4515ffaf7ca4767cbfb6a1424a326f575728fdb9ff973fa3` |
| `packet_blueprint/SIX_FILE_CONTENT_REQUIREMENTS.md` | `ac3ca46a29fe57c40dd8e19fde88e348205891f661f0057738dc4247eb05c8dc` |
| `packet_blueprint/HASH_BINDING_PROCEDURE.md` | `e2071fcdd22cd1f854c6308e55987d1b2e6851ca21af2d799ad7bd6edc7504c0` |
| `packet_blueprint/NON_RECONSTRUCTION_STATEMENT.md` | `95a3aa60f1db42e87b01bf38f979e7bbd15469ba5535985c7ca7845b4e3c8ad1` |
| `packet_blueprint/OWNER_ACCEPTANCE_FORM.md` | `e5945833da68b8aa965c079410e992a443dd40d633b7f002b2ea92fcaae29313` |
| `packet_blueprint/N0_RERUN_BRIEF.md` | `d9519594a6fe1a9eb115725bef4d16ac73e1d459853b7c98577da4061e99be36` |
| `packet_blueprint/N0_RERUN_CHECKLIST.md` | `fb326c03008c3bbfc58efa9a98d4cf22e58c60b80d36bcdc8462624ebff14af7` |
| Candidate validator | `d35d0748a8837f7d4c50a5e298a4ea0bedcb52ecbf4c6a6496b2c8c209143539` |
| Owner-acceptance validator | `fb153b5648bbb909838c50215a11705ae4f7c66737d75a6f2d46016d89c3d152` |
| Negative-case harness | `fbd47a25b1c6aab51969e2ab2bf106ecca2192154e2721470d7258368dd1c21c` |
| Local work graph plan v3 | `6de9eee4667fa7f5f5d7f2e6729aba0f4e372eb52eddf6ef66c5910a79a46dcd` |
| `templates/DEGRADED_MODE_CONTRACT_CANDIDATE.md.template` | `b6ca6dcb394b9c9fd601a7d947ed9ca9d722a712c0dbdd6772c4fe3d88747f0a` |
| `templates/OWNER_GATE.md.template` | `c6d3f8184d7c67a401d7a715d308b47a2bd6aed6fdedb751dd596d3b48a0d884` |
| `templates/ROOT_COMPATIBILITY_POLICY_CANDIDATE.md.template` | `d477255283385cede83e2e1fb36a8f9f11e5a09a7a60fb38d5d2876b6202f3d8` |
| `templates/OWNER_SELECTION.md.template` | `a750480093c0ce7e7f0e16769f6f1d32b1f221174485860e53502489fabad8a6` |

Six `.template` files define exact final membership and contain placeholders
only for post-S2 identities or hashes derived after those substitutions. They
are not candidate bytes. The accepted Scope of Work resolves containment to
the RunID-local future path
`_run_records/DEL-02-06-RUNTIME-SPEC-001/accepted_inputs/`; parent plan-v4
clarification SHA-256 is
`5d84ae468c6bb64607052c6b100674a237d1cd146b25d8b84838728dc4855737`.
Neither the corrected path nor the erroneous deliverable-root path exists.

Validation: both Python validators compile; blueprint and work-graph JSON
parse; template count is exactly six; OPEN_ITEMS template has one header plus
sixteen rows; W2 candidate whitespace passes. Positive candidate validation is
correctly not claimed before S2.

## Coverage

- Package: `PKG-02` only.
- Deliverable: `DEL-02-06` only.
- Run: `DEL-02-06-RUNTIME-SPEC-001` under parent
  `ROOT_FOUR_LANES_2026-08-02`, plan version 2.
- Authority exercised: REQ-027 specification, read-only inventory, evidence
  design, and change planning only.

## Durable return

- Activation record:
  `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-RUNTIME-SPEC-001/ACTIVATION_RECORD.md`.
- Validated work graph: same run root, `WORK_GRAPH.json`.
- Exact recovery and evidence plan: same run root,
  `MANAGER_RECOVERY_CHANGE_PLAN.md`.
- N0 manager evidence: same run root, `basis/BASIS_REPORT.json` and
  `basis/N0_RETURN.md`.
- Handoff: same run root, `HANDOFF_STATE.md`.

## Fan-in disposition

No child return is accepted. The N0 child did not terminate with its required
files; WORKING_ITEMS interrupted and rejected it. Independent manager checks
found substantive N0 failures, so N1–N6 correctly remain held:

1. the six mandatory hash-verified authoring-envelope inputs are absent;
2. the live v1.2 decomposition text says candidate/not accepted while the
   SCA-002 Decision Log records accepted/applied/Gate-5-validated state.

S1 independently confirms that conflict: AUDIT_DECOMP structural coverage
passes while authority-state consistency fails (return SHA-256
`3d2a09dd35da0c26bc87a1e156c7b1a5e35fd7875ff9a39d4294b8d6a369a868`).
S1 also proves a second N0 blocker: live `docs/PRD_ROOT.md` still labels
Revision 7 candidate and Revision 6 accepted while the Root handoff and live
D-8 state say Revision 8 adopted. S1's current return SHA-256 is
`a003ec10bd7731cbd038e8b6c4df05ac897cf9f0ea58d2cbda8c889d10017b00`;
it authorizes no reconciliation.

The graph itself is complete and validated for version, selection authority,
posture, N0–N6 nodes, edges, concurrency, disjoint writes, integration owner,
fan-in gates, holds, escalation points, return sequencing, and telemetry
limitation. Both JSON artifacts parse. The accepted `ScopeOfWork.md` validates
as `SOW_V1`, valid, with zero issues.

## Recovery requirements and affected surfaces

The provisional manager plan records REC-001 through REC-016. It requires a
startup barrier before socket exposure, admission, or model activation;
crash-safe/idempotent reconciliation of every persisted `turn.accepted`
without a terminal; exactly one terminal; no provider/model/prompt replay;
stable session/drain accounting; fail-closed malformed or contradictory
history; append-only/redacted evidence; and explicit compatibility review.

Candidate Root surfaces are `session-store.ts`, a new accepted-turn
reconciler, `runtime-service.ts`, `runtime-daemon.ts`, shared terminal
predicates only where necessary, and Root runtime tests. `turn-coordinator.ts`
and `residency-coordinator.ts` require exact invariant/caller review. No App,
PEC, Piping, Tier-0, register, lifecycle, contract, runtime, or release surface
was written. No client is formally classified affected because N2 is held.

## Implementation and executable evidence plan

The plan defines a later six-step implementation/review sequence and ten
restart/replay scenarios: initial orphan recovery; repeated restarts; injected
crash between terminal/status persistence; mixed project/session histories;
malformed/duplicate/failing stores; startup-barrier races; residency drain
ordering; redaction; canonical-log replay; and repeated clean-checkout check
selection. No scenario was executed because REQ-027 and REQ-052 forbid it in
this activation.

## Historical pre-W6 verdict, blockers, and next gate

Historical verdict: `PACKET_ACCEPTED_APPLIED — N0_PASS — STOPPED_AFTER_N0`, not
activated for implementation and not closed.

Immediate next sequence: HELP_HUMAN/human owner makes an explicit post-N0
continuation decision. N1–N6 remain held under parent plan 11. After N0–N6
complete, the owner must rule
the recovery terminal/
payload/identity, duplicate-history posture, and compatibility-epoch effect;
S1 and a lawful Root software-workflow profile must precede any sealed
implementation activation.

Task Management row closure remains excluded and requires its own later
session after applied bytes and executable restart/replay evidence are
accepted.

## Validation and preservation

- `ScopeOfWork.md`: `SOW_V1`, valid, zero issues.
- `WORK_GRAPH.json`: JSON parse PASS.
- `basis/BASIS_REPORT.json`: JSON parse PASS.
- Packet validator and acceptance-validator syntax: PASS.
- Packet-blueprint JSON and exact six-template count: PASS.
- W1-owned candidate whitespace: PASS.
- Runtime/client/lifecycle/decomposition/register write count: zero.
- Owner acceptance, byte-identical live input, and fresh N0: complete and
  validated; N1–N6 dispatch and all implementation/lifecycle effects: zero.
- Commit/push/merge: none.

Derivative status: `INCOMPLETE_HELD`. Rerun requirements and exact blockers
are authoritative only as this manager handoff; they do not amend
decomposition or Scope-of-Work truth.
