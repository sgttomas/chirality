# Handoff State — Root v3 Phase 0

Run ID: `ROOT_V3_PHASE0_2026-08-22`

State: `NODE_FAN_IN_ACCEPTED — PR #620 OPEN; GOVERNANCE GATES REMAIN`

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
- Owner-authorized current-main merge:
  `0bd042e5299c81301cc726bc54eea265285b4159`, with parents N3
  `7590c002b1dc9399e95029d51551895bb700b302` and
  `origin/main@166efa82748133e90674be62304b81f8a0a8c1b4`. Incoming paths were
  34/34 App-owned with zero Root overlap.
- Final integrated validation evidence:
  `FINAL_VALIDATION.md`, SHA-256
  `281715b71990c49d4ef942c3adb7a012904800121eec94d819109ef53295fefe`.

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

Publication closeout: `COMPLETE TO PR REVIEW GATE`. The owner explicitly
authorized the current-main sync, push, and PR creation. The branch was merged
without conflict, pushed normally, and opened as ready PR #620:
`https://github.com/sgttomas/chirality/pull/620`. Receipt 114 and the final
Root handoff are included in its closeout commit. No PR approval, auto-merge,
or merge was performed.

## Holds and remaining blockers

1. D-GOV-35 remains `PROPOSED — AWAITING OWNER RULING`.
2. DEL-02-03 M2 application requires that ruling and separate application
   authority.
3. SCA-004 remains `AWAITING_OWNER_ACCEPTANCE`; Gate 2 is closed.
4. All ten DEL-02-06 `HELD_UNAVAILABLE` bindings remain held.
5. TM-ROOT-106 and TM-ROOT-122 remain separate G1 blockers; no pin amendment
   is present in this tranche.

## Rerun requirements

- After any later base or candidate-byte change, reproduce every protected
  identity and rerun the complete validator set.
- If D-GOV-35 is ruled, separately authorize and execute the M2 application;
  finalize documentary concordance, route notices, and regenerate or
  explicitly defer the Root-owned public-export derivative.
- If SCA-004 Gate 1 is accepted, enter Gate 2 only through SCOPE_CHANGE and
  update `_LATEST.md` only when that workflow permits.
- Do not merge PR #620 in-session. Owner review remains the final Git gate.

## Next lawful owner

Ryan Tufts is the next lawful owner for the D-GOV-35 ruling, SCA-004 Gate-1
acceptance, and PR #620 review/merge decision. Each is an independent gate;
none is inferred from preparation or validator success.
