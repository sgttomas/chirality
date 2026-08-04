# Evidence and cutover plan candidate V1

- Status: `DESIGN_ACCEPTED_FOR_CANDIDATE_NOT_EXECUTED`
- N3 evidence design: `e05b56d3b3a1bd349cd0b9da8e2df761126f2c46c44baf1c9282c6cf55180dd0`
- Upstream implementation plan: `e2f4fda9fa44eff9caf3c6894b6112c4eec39fc9bbac43b8e840382fc3b17bd9`

## Semantic conformance and regression matrix

The complete N3 design is the required future evidence plan. Its status is
`DESIGN_COMPLETE_NOT_EXECUTED`; no row is a pass result. Later exact authority
must execute and bind all of:

- N3-R01 through N3-R16;
- RR-01 through RR-18;
- DA-01 through DA-06;
- all eight exactly-one-terminal corpus cases;
- CO-01 through CO-07; and
- all eight retained-function cases plus a complete route/direct-entry census.

Every result must bind exact contract, source, fixture, runtime artifact, and
evidence SHA-256 identities; distinguish deterministic fact, human judgment,
client-owned evidence, and unresolved fields; and include positive,
negative, and adversarial evidence. Root CLI and App evidence remain under
their separate owning gates. PEC evidence is forbidden absent a PEC ruling.

## Recovery cutover replay and indeterminate completion

The staged policy is:

1. freeze exact pre-change source, contract, runtime, fixture, and corpus
   manifests before mutation;
2. validate candidate bytes and rehearse all N3 cases in isolation;
3. keep readiness and all consequential paths closed during recovery;
4. never retry, resume, replay, or infer completion of an indeterminate turn;
5. preserve all partial output and classify it as indeterminate evidence;
6. atomically reconcile per turn under the single-writer/final-manifest rule;
7. stop on any failed precondition, malformed evidence, identity drift, or
   incomplete audit; and
8. require a separate accountable-human cutover act after evidence acceptance.

Any later operation is a new independent turn. Reconnect/rebind only reruns
preconditions.

## Cutover rollback and irreversible boundary

Source/runtime rollback is permitted only before the first recovery-corpus
mutation. The first durable recovery terminal, marker, summary update, audit
mutation, or other accepted recovery write crosses the irreversible boundary.
After that boundary:

- historical corpus and audit bytes are preserved;
- the system remains stopped on failure;
- the old runtime may be restored only if exact evidence proves it can read
  every possible post-mutation corpus state; and
- otherwise recovery proceeds only through a separately approved forward
  repair with its own contract, evidence, and deployment gate.

Rollback never erases evidence or silently replays work. Git, deployment,
lifecycle, and release are separately authorized acts.

## Candidate implementation sequence and exact gate

| Stage | Planning-only objective | Held gate |
|---|---|---|
| P0 | freeze accepted semantic bytes, future epoch/binding, and fixtures | exact semantic and compatibility acceptance |
| P1 | align terminal, recovery-state, compatibility, and error envelopes | exact contract-byte and source-locus gate |
| P2 | implement corpus classification, writer, atomic append, quarantine, audit, and manifest | exact storage/reconciliation gate |
| P3 | gate ordinary and Agent 1 admission; preserve no replay | implementation and parity evidence gate |
| P4 | implement durable attribution and drain/blocker ledgers | attribution/drain gate |
| P5 | run recovery before socket readiness and classify every route/direct entry | retained-function and readiness gate |
| P6 | implement Root client/CLI exact classes with no resend | Root CLI conformance gate |
| P7 | execute the complete N3 evidence and cutover rehearsal | exact check authority and evidence acceptance |
| P8 | route App work separately; route PEC ruling without prescribed outcome | foreign-owner gates |
| P9 | assemble immutable fan-in for cutover and release decisions | accountable-human cutover/release gates |

No stage authorizes the next. Before any implementation, a later activation
must identify a lawful Root-local workflow profile, exact checks, source and
test files, writable paths, rollback, evidence, and return contract. Client
profiles may not be borrowed. Basis drift or a new client returns to the
owner.

## No-effect boundary

No check was run and no pass result, source edit, implementation, cutover,
rollback, client work, profile, dependency, lifecycle, release, reliance, Git,
deployment, or foreign-loop effect occurs in this candidate.
