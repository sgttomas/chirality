# W-A2 Package Fan-In

Verdict: `PASS`.

- Population and ownership: exact 16 members in disjoint packages 5/5/6.
- Terminal author/verifier pairs: 16/16; 32 exact terminal child status and
  self-excluding manifest surfaces.
- Package bindings: 208/208 mechanically reproduced.
- Child-manifest bindings: 1,052/1,052 mechanically reproduced, including
  file hashes and byte counts where declared.
- Candidates: 16/16 exact at the hashes in `CANDIDATE_MANIFEST.tsv`.
- Claim mappings: 491, all disposition `PRESERVED`.
- Legacy source lines: 5,584/5,584 dispositioned.
- Live source/status/control: 144/144 accepted preflight bindings reproduced.
- Replacement and rollback: exact 80/80; rollback is the action/hash inverse;
  paths are disjoint and exclude lifecycle/status/control surfaces.

The packages use three locally valid evidence schemas. Reconciliation
normalizes those schemas only in this derivative; it does not rewrite package
evidence. `detailed/PACKAGE_BINDINGS.tsv` and
`detailed/CHILD_MANIFEST_BINDINGS.tsv` are the exact current binding ledgers.

No partial, dual-live, ambiguous, stale, nonterminal, or non-reproducible
package return remains. Blockers, waivers, unknowns, and decision needs: none.

