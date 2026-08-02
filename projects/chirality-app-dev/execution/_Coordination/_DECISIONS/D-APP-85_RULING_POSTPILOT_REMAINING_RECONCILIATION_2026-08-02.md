# D-APP-85 — Ruling: Post-Pilot `Remaining` Truth Reconciliation

Status: `RULED / ACTIVATION_PENDING_MAIN`

DecisionID: `D-APP-85`

Date: `2026-08-02`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

Selected proposal:
`execution/_Coordination/_DECISIONS/D-APP-85_PACKET_POSTPILOT_REMAINING_RECONCILIATION_2026-08-02.md`
at SHA-256
`56fedf46e067d2bd2edf25eabf259bf2edf4c7d8f69df640775145c41ad7f4d4`.

## Exact owner ruling

The owner returned exactly:

> APPROVE D-APP-85 OPTION A: ACTIVATE THE NARROW READ-ONLY RECONCILIATION RUN AND STOP AT GATE 2.

No rider, target repair, lifecycle act, or broader effect is inferred.

## Selected semantics

Option A is selected exactly as proposed. It activates RECONCILIATION only
over the packet's exact C01-C18 candidate population and accepts the frozen
method and calibration conventions in packet section 5. After this
ruling/register tranche is merged to `main`, the run may perform read-only
calibration, inventory, claim verification, synthesis, and fresh adversarial
fan-in at the frozen merge basis.

The prospective immutable run root is:

`execution/_Reconciliation/DeliverableConcordance/RUN_DAPP85_POSTPILOT_REMAINING_RECONCILIATION_2026-08-02/`

The run must produce the packet section 6 outputs, including an exact
repair/no-change manifest representing all 18 claims exactly once, then stop
at Gate 2. The manifest is recommendation evidence only until the owner rules
on its exact SHA-256.

## Hard ordering and stop state

1. This ruling record and the D-APP-85 register transition must first be
   committed and merged to `main` through CHANGE.
2. The run basis must freeze the merge commit, method hashes, candidate
   hashes, accepted authority/decomposition/dependency pointers, and overlap
   state. Any changed C01-C18 source block stops activation for revalidation.
3. Discovery is read-only. It may write only the new derivative run root and
   the governed child-return surface described by the packet.
4. The run stops at Gate 2 with the exact manifest hash and owner token.
5. No target-corpus repair or associated receipt may occur before the later
   exact Gate-2 owner ruling.

## Preserved boundaries

The packet's exclusions and preservation rules remain binding. In
particular:

- all unrelated sibling and out-of-scope `Remaining` blocks stay outside the
  activated population;
- DEL-05-04 and the UI/API parity-evidence bundle remain unselected;
- the six D-APP-81 clause-6 historical relations remain
  `HISTORICAL_RELATION_UNKNOWN`;
- both Task Management registers remain unchanged;
- D-APP-84's Root-conditioned posture remains unchanged, including that H1
  grants no Bash now;
- all lifecycle states and all `Checking Approval SHA` values remain
  unchanged; and
- authority, decomposition, accepted scope-change snapshots and pointers,
  dependency truth, runtime/source/frontend behavior, release, issuance,
  publication, professional reliance, and blanket closure remain outside
  this ruling.

## Receipt timing

No loop receipt is appended for this pre-main activation record. Consistent
with the selected packet sections 7 and 10, one governed loop receipt becomes
eligible only after a later exact Gate-2 ruling, the enumerated repairs, and
the fresh accepted backcheck. The present owner ruling is durably recoverable
from this record and the register.

## No-effect boundary

Before the ruling/register tranche is merged to `main`, the activation state
is `ACTIVATION_PENDING_MAIN` and no reconciliation dispatch is permitted.
Recording this ruling creates no discovery result, claim disposition, target
repair, status/dependency/memory/run-record/completion-log/receipt write,
source/runtime/frontend change, Task Management disposition, lifecycle,
release, issuance, professional-reliance, commit, push, or merge effect.
