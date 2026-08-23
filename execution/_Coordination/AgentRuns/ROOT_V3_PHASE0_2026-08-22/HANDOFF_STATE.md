# Handoff State — Root v3 Phase 0

Run ID: `ROOT_V3_PHASE0_2026-08-22`

State: `NODE_FAN_IN_ACCEPTED — PUBLICATION BLOCKED ON OWNER SYNC AUTHORIZATION`

## Accepted upstream state

- Owner-authorized execution basis:
  `main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776`.
- Owner steer SHA-256:
  `c348e9767db4af20787bbcb74c64791ef08d700b08dc19d86289a88a58f067e3`.
- Owner G0 record SHA-256:
  `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b`.
- N1 return SHA-256:
  `dabe5c3826ff17801015301cb1ffec685d0fc96ffa96cf1f3178b5505949994e`;
  accepted cycle-3 review SHA-256:
  `2bad195c74726c9ec203cb45a3149644536d3fe8883dba1f71d0f73b004a7c7f`.
- N2 return SHA-256:
  `3ac4e6356e21f0b2f680bcb1ed09fc4d04c57ef944195b3e9e80f4cb212c6047`;
  accepted fresh-review SHA-256:
  `6a22c65fed127115889eb95996fa912ba158ff49690f606fa1aab58939cf723b`.
- N3 return SHA-256:
  `5163e1737bead5ddc3c4b201e4cf2434db6ca897c2d15f97b630acc3dff12d2a`;
  accepted cycle-2 review SHA-256:
  `0e8d7cacb1e9b24806249ec2f59ec2061f838271cac501b3ecdeaca85b69a6a7`.

## Derivative-package status

- The D-GOV-35 folder is a proposal packet only. It is not a decision and its
  inactive `AGENTS.proposed.patch` has not been applied.
- `DEL-02-03-M2-PREP-001` is a draft preparation package only. Its notices are
  unrouted, its manifest is not in the live corpus, and application remains
  blocked on an owner ruling plus separate M2 application authority.
- SCA-004 is a Gate-1 assessment only. Its graph and audits are current to the
  accepted execution basis; `_LATEST.md` remains unchanged and Gate 2 is not
  entered.
- Root-owned public-export regeneration remains explicitly deferred to the
  later authorized instruction-application handoff.

## Closure verdict

Node production and fresh-review fan-in: `COMPLETE`.

Governance/lifecycle closure: `NOT ENTERED`.

Publication closeout: `BLOCKED`. During execution, `origin/main` advanced from
the authorized basis to `166efa82748133e90674be62304b81f8a0a8c1b4`. No sync,
rebase, push, PR, or merge has been performed. The owner steer requires
explicit sync authorization before publication can proceed.

## Holds and remaining blockers

1. Owner sync authorization is required before bringing the branch onto the
   current `main` line and performing the final Receipt 114 / PR closeout.
2. D-GOV-35 remains `PROPOSED — AWAITING OWNER RULING`.
3. SCA-004 remains `AWAITING_OWNER_ACCEPTANCE`; Gate 2 is closed.
4. All ten DEL-02-06 `HELD_UNAVAILABLE` bindings remain held.
5. TM-ROOT-106 and TM-ROOT-122 remain separate G1 blockers; no pin amendment
   is present in this tranche.

## Rerun requirements

- After any owner-authorized sync, reproduce every basis/protected-surface
  identity that the new base can affect and fresh-review any semantic conflict.
- Run the full owner-specified closeout validator set against the integrated
  candidate before push.
- Append Receipt 114 only after the node commits are known, transcribe the
  complete steer and G0 record byte-for-byte, record sync authority and
  validator outputs, and update the owning Root handoff counts/state.
- Do not merge. Owner review remains the final Git gate.

## Next lawful owner

Ryan Tufts decides whether HELP_HUMAN may sync this accepted preparation branch
to the advanced `main`. If authorized, HELP_HUMAN resumes byte verification and
routes Git publication through CHANGE; otherwise this handoff remains the
durable stopped state.
