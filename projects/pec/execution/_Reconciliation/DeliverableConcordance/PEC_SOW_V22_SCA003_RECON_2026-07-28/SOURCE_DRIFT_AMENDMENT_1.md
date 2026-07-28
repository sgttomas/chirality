---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
status: applied
prior_basis: 404e47c16a88e7ffdc6d1fc5fac61ebb6864211e
rebase_basis: 21e8e54e1f5648b7d3db29228271aaa8c7d8904f
reference_parity_merge: af62343d3af95fcd3af0742615cb92a7c813f44a
---

# Source-drift amendment 1

Before sealing, `origin/main` advanced beyond D-PEC-69. Comparison against the
frozen basis found:

- no change to PRD v2.2, decomposition revision 1.3, the hold register, any
  dependency register, or any active `ScopeOfWork.md`;
- a current-reference parity tranche updating all 64 `_REFERENCES.md` files
  to revision 1.3 / PRD v2.2; and
- unrelated coordination and non-PEC integrations.

The candidate was rebased to `21e8e54e1`. Because the selected contracts still
said their `_REFERENCES.md` files named revision 1.1, the basis-note prose in
all eleven selected contracts was aligned to the current reference-parity
state. This is a source-state accuracy correction inside the selected
contract fence, not a new semantic population or a change to the effective 57
claim repairs.

All frozen authority hashes remain valid. Full contract, register, hold,
containment, whitespace, and independent verification must be rerun after
this amendment.
