# Rider and assessment audit

## Versioned rider

The initial independent W1 verification is preserved at
`WAVES/W1/W1_LEDGER_VERIFICATION.md` with its `FAIL` verdict. It found one
omitted stale quotation: `DEL-10-11/CLM-002`.

The correction was added through:

- `WAVES/W1/W1_DISPOSITION_AMENDMENT_1.md`;
- `DECISION_PACKETS/R4_AMENDMENT_1.md`; and
- `WAVES/W1/W1_ADDITION_NOTICE.md`.

That owner-approved rider changes the effective set from 56 to 57 claim
repairs without adding a contract, changing a claim ID, resolving an unknown,
or broadening the repair fence.

The first post-repair independent report is preserved at
`BACKCHECK/INDEPENDENT_REPAIR_VERIFICATION.md` with its `FAIL` verdict. Its two
missed narrative facts and one unauthorized addition are dispositioned
additively by `W1_DISPOSITION_AMENDMENT_2.md` and `R4_AMENDMENT_2.md`; the
effective claim set remains 57. The second failed verification is preserved
at `INDEPENDENT_REPAIR_VERIFICATION_RERUN_2.md`; its sole source-chain
omission is dispositioned by `W1_DISPOSITION_AMENDMENT_3.md` and
`R4_AMENDMENT_3.md`. The terminal third verification is preserved separately
at `INDEPENDENT_REPAIR_VERIFICATION_RERUN_3.md` with verdict `PASS`.

## Assessment preservation

- Original worker ledgers remain immutable pre-repair discovery evidence.
- 794 claim definitions still correspond to 794 ledger rows.
- The 22 explicit `UNKNOWN` ledger dispositions remain unresolved.
- The repaired corpus still carries its explicit deliverable-contract
  unknowns: 126 `TBD-*` and 105 `CON-*` definitions across the 32 active
  contracts.
- No historical assessment was silently re-rated; the amendment and the fresh
  independent rerun are separate, additive evidence.
- No `AUTHORITY_CONFLICT` was found during W1. The PRD §13 ADR-014 wording
  discrepancy remains a routed source-governance issue, not a contract-level
  precedence invention.

The final fresh independent repair verification is
`INDEPENDENT_REPAIR_VERIFICATION_RERUN_3.md`.

The post-repair accidental refresh of two baseline-only artifacts is recorded
under `../EVIDENCE_CORRECTIONS/`. The mistaken bytes remain preserved; the
pre-repair manifest and W1 baseline PASS were restored from corroborating
R1/Git evidence under the owner's standing 2026-07-28 direction.
