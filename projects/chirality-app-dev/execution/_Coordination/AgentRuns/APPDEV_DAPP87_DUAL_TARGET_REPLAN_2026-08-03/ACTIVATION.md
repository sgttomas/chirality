# D-APP-87 Option B — Dual-Target Re-plan Activation

RunID: `APPDEV_DAPP87_DUAL_TARGET_REPLAN_2026-08-03`

Manager: `HELPS_HUMANS`, under App `HELP_HUMAN`

State: `ACTIVE — DERIVATIVE PLANNING ONLY`

## Authority

- D-APP-87 ruling SHA-256:
  `d13543f7164a688cd6ee5472455564e76eeba5f30acc1c157beb87017a82f0fe`.
- Selected packet SHA-256:
  `079d9b9874a3a0e37d6778d907329a360efab63996a134fa67738ef3f186a577`.

The following requirements are adopted and are not reopened by this run:

1. Chirality App has two targets: standalone Desktop and a per-domain
   control-plane target.
2. Domain applications are the primary delivery vehicle for agents; the
   re-plan therefore uses domain-first delivery emphasis.

The implementation form is deliberately unselected. The run must compare a
lightly skinned one-codebase design, a shared core with target-specific shells,
and at least one evidence-grounded third form.

## Output contract

The derivative package covers the six D-APP-87 §5 lanes: UI, packaging,
affected-client runtime contract, deliverables/work order, validation, and
later decisions. It fans in to an owner-ready proposal using the next verified
live App decision ID.

Generic runtime, sandbox, identity, version, resume, and Bash lanes are
`BLOCKED_BY_ROOT`. This run may state App affected-client requirements and
interfaces but cannot select or implement generic semantics.

## Work graph

`basis inventory → bounded UI/packaging review + bounded runtime/work-order review → six-lane manager synthesis → owner proposal → independent adversarial verification → owner gate`

## Write scope

Allowed writes:

- this fresh AgentRuns root;
- one new proposal in `execution/_Coordination/_DECISIONS/`;
- the App decision register only as required to register that proposal.

Forbidden writes include PRD, decomposition, SCOPE_CHANGE, deliverable/status,
source, frontend/runtime, Task Management, receipt, corpus, completion log,
Git, and every foreign-loop surface. Existing planning and D-APP-88 route
artifacts are preserve-byte-for-byte inputs. The six D-APP-81
`HISTORICAL_RELATION_UNKNOWN` relations are untouched.
