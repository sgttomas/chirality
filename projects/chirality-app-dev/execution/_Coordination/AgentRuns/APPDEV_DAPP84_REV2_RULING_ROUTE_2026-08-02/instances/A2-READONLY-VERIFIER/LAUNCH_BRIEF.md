# Launch Brief — Fresh Read-Only Ruling-and-Route Verifier

RunID: `APPDEV_DAPP84_REV2_RULING_ROUTE_2026-08-02`

BriefVersion: `1`

Parent: `HELPS_HUMANS`

Construction: `ephemeral bounded Agent 2 generalist`

## Objective

After the manager materializes the D-APP-84 Revision 2 ruling-and-route
tranche, independently verify it. Do not edit any file and do not delegate.

## Read scope

Repository-wide read access limited in purpose to the two D-APP-84 proposal
packets, the new ruling, the App decision register, the Root notice, this
RunID, App receipt rules/ledger/validator, current Root Bash doctrine, Root
DEL-02-06, Git refs/diffs, the six historical-UNKNOWN preservation evidence,
parity-selection evidence, and both Task Management registers for non-write
comparison.

## Acceptance checks

- Owner token is exact and maps to B1/V1/P1/X1/H1/R1 exactly.
- Conditions, exclusions, and no-effect boundaries match Revision 2 without
  creating Root or implementation authority.
- Proposal Revision 1 SHA-256 remains
  `0f4ddfb3c71b1862225ce35430fc18b275588b2dfafbca7d884aaef524a9830e`;
  Revision 2 remains
  `59e3f668f742bc8e100630781da3be975c0c6861410d06ee2ed019d5c79cf5d9`.
- Exactly one D-APP-84 register row exists, is `RULED`, and links the ruling.
- Root notice is ordinary coordination, includes the exact selection and all
  required Root requests plus `TM-CANDIDATE` lines, and writes no register.
- Changed paths fit the sealed write scope; parity and the six historical
  `UNKNOWN` relations are unchanged; Task Management registers are unchanged.
- Refreshed `origin/main` drift is scoped-disjoint; the receipt is one new
  valid Receipt-107 with exact cursor and pass/fail-only checks.

## Return

Return `PASS` or a severity-ranked, evidence-linked finding list. Distinguish
structural validation from semantic acceptance. Make no authority claim.
