# PEC SOW v2.2 / SCA-003 backcheck

## Re-extraction

`CHANGED_CLAIM_REEXTRACTION.csv` and `DETAILED_EVIDENCE.csv` contain exactly
57 rows each, one per effective repair:

- 57 `CONFIRMED`;
- 0 `REFUTED`;
- 0 `UNVERIFIABLE`;
- 11 repaired contracts; and
- no stable-ID, unknown, topology, implementation, lifecycle, or hold-state
  mutation.

The initial failed independent verification remains preserved. Its versioned
amendment is applied, and the required fresh independent repair-verification
report is a separate artifact.

## Deterministic validation

- 32/32 active contracts pass all four SOW validators.
- Final validation summary SHA-256:
  `a295527cbe97e1aa7d85573917a37a30a58add18c9ffe2a1b7b18d5ab28193c2`.
- Strict register validator: 64 registers / 254 dependency rows / 0 errors /
  0 warnings.
- Hold tests: all expected allows and blocks pass; hold remains active.
- Candidate whitespace and `git diff --check`: pass after EOF normalization.
- Practitioner harness self-check: exit 0.

## Verdict

**PASS.** The terminal fresh independent verification
`INDEPENDENT_REPAIR_VERIFICATION_RERUN_3.md` records `PASS`; all earlier
failed returns remain preserved. The two baseline-only evidence corrections
and preserved mistaken bytes are recorded under `../EVIDENCE_CORRECTIONS/`.
The repair is complete and contained. `PEC-HOLD-001` remains active, so this
verdict authorizes no production reliance, dispatch, promotion, or
consumption.
