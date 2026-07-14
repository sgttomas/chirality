# W-A3 Package Fan-In

Verdict: `PASS`.

- Population and ownership: exact 16 members in disjoint packages 5/6/5.
- Terminal author/verifier pairs: 16/16; 32 accepted terminal child surfaces.
- Package bindings: 220/220 mechanically reproduced.
- Accepted child-manifest bindings: 1,470/1,470 mechanically reproduced,
  including file hashes and byte counts where declared.
- Candidates: 16/16 exact at the hashes in `CANDIDATE_MANIFEST.tsv`.
- Claim mappings: 481, all disposition `PRESERVED`.
- Legacy source lines: 4,985/4,985 dispositioned.
- Live source/status/control: 144/144 accepted preflight bindings reproduced.
- Replacement and rollback: exact 80/80; rollback is the action/hash inverse;
  paths are disjoint and exclude lifecycle/status/control surfaces.
- Simulations: 16/16 apply and exact rollback.

The packages use locally valid evidence schemas. Reconciliation normalizes
those schemas only in this derivative; it does not rewrite package evidence.
`detailed/PACKAGE_BINDINGS.tsv` and
`detailed/CHILD_MANIFEST_BINDINGS.tsv` are the current exact ledgers.

No partial, dual-live, ambiguous, stale, nonterminal, or non-reproducible
accepted return remains. Blockers, waivers, unknowns, and decision needs:
none.
