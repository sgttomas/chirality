# DEL-02-06 compatibility-completion preparation authorization handoff

Date: `2026-08-21`

Status: `OWNER AUTHORIZATION RECORDED — SEPARATE WORKING_ITEMS TRANCHE NOT YET LAUNCHED`

This handoff records the owner act for the next Root production session. It is
not an activation record, work graph, preparation output, compatibility
package, exact-byte acceptance, implementation authorization, lifecycle
change, release, publication, reliance statement, or foreign-loop act.

## Owner ruling

```text
DEL-02-06 — SUPPLY INITIAL ROOT COMPATIBILITY EPOCH `1`, YIELDING
CANDIDATE IDENTITY `root-runtime-1`, AND AUTHORIZE ONE SEALED
WORKING_ITEMS ACTIVATION TO PREPARE AND VALIDATE THE EXACT
COMPATIBILITY-COMPLETION PACKAGE AGAINST ACCEPTED SNAPSHOT
`3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`.
PREPARATION ONLY: DO NOT ACCEPT THE RESULTING BYTES BY INFERENCE; DO NOT
IMPLEMENT, CHANGE LIFECYCLE, RELEASE, PUBLISH, ASSERT RELIANCE, OR WRITE
A FOREIGN LOOP.
```

The exact complete direction, including sequencing and PR fences, is
transcribed at
`OWNER_DIRECTION_TRANSCRIPT_PR602_REPAIR_AND_RULINGS_2026-08-21.md`,
SHA-256
`2d89d0aa1410e9bec74af54a1a8cb8b151cf60009c2214a3c682f925ba8ddb3e`.

## Accepted basis and supplied fields

- Package: `PKG-02_Operative_Instruction_Surface_and_Runtime_Layers`.
- Selected deliverable: `DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance`.
- Accepted semantic snapshot SHA-256:
  `3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`.
- Owner-supplied initial compatibility epoch: positive decimal `1`.
- Candidate identity yielded by that field: `root-runtime-1`.
- Authorized production form: one sealed `WORKING_ITEMS` activation,
  preparation and validation only.

`root-runtime-1` is now the owner-supplied candidate identity for preparation;
it is not an accepted compatibility-completion package identity until the
resulting exact package bytes and their SHA-256 receive a separate accountable
human acceptance.

## Next-session activation boundary

The next Root session may instantiate one package-scoped `WORKING_ITEMS`
manager against PKG-02, narrowed to DEL-02-06, with a new immutable run root
and a frozen work graph. It must:

1. reproduce the accepted snapshot and all six member hashes without changing
   accepted historical semantic members;
2. apply epoch `1` to the new compatibility-completion candidate;
3. assemble the single complete immutable binding manifest required by the
   accepted compatibility member, preserving honest held/unavailable fields;
4. validate hashes, completeness, determinism, collisions, and reserved-value
   constraints, then run fresh refutation; and
5. return the exact prepared bytes and SHA-256 to the owner.

The activation must live on its own branch/tranche/PR. No preparation output
may be attached to PR #602. It may not implement, change lifecycle, release,
publish, assert reliance, or write any foreign loop. Any unavailable required
binding is returned as a blocker; it is never invented.

## Remaining human gate

The prepared exact bytes and their SHA-256 require a separate owner acceptance
decision. No acceptance is inferred from this authorization or from epoch
selection.
