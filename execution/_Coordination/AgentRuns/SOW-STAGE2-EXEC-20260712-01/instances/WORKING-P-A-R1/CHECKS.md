# WORKING-P-A-R1 Evidence Portability Repair Checks

Verdict: `PASS`

Basis: WORKING-P-A terminal PASS; RECON-PF blocked solely by `PF-PORT-001`;
P3/G3 PASS; `PILOT-VALIDATION-001`; `PF-EVIDENCE-PORTABILITY-001`; unchanged
`main@0d260eb024d8b8dada0df477b70ac880a6906ffa`.

## Amendment gates

1. **Exact pre-edit inventory — PASS.** The amendment's 13 App files were the
   complete package match set: 12 accepted evidence files with 32 occurrences
   and one preserved failed-attempt file with four occurrences. Temporary
   prefix count was zero.
2. **Literal substitution only — PASS.** Exactly 36 occurrences were replaced
   with the portable `~/` form in the 13 named files. No other content repair or
   verifier rerun occurred.
3. **Preimage equivalence — PASS.** Every resulting file hash equals the hash
   computed from its preimage under only the authorized literal substitution.
   Exact pre/post hashes and counts are recorded in `REPAIR_MANIFEST.tsv`.
4. **Direct binding refresh — PASS.** Search of package-local summaries found
   one direct binding surface, `instances/WORKING-P-A/PACKAGE_HANDOFF.md`.
   Its six accepted child-return hashes were rebound to the repaired bytes.
   Pre-hash `01441ff8dcbb2d3ebff54cf7e3abce27330b4ff003921cd7b07909b8b5493388`;
   post-hash `b719b32fd2d052d15f1bb72f53f3db0438c486e54e3d6e563e7d34936080a434`.
   No run-record hash had another direct package-local binding.
5. **Verdict and semantic preservation — PASS.** Six accepted terminal PASS
   returns remain accepted with 191/191 mappings and 2,173/2,173 source lines.
   Candidate, source/status, parity, checklist, render, replacement/rollback,
   lifecycle, and authority evidence is unchanged. The original V-01-A attempt
   remains `FAILED_SUBSTRATE_NONTERMINAL`, `DISPATCHED`, `PENDING`, and
   unaccepted.
6. **Portability and structure — PASS.** Checkout-prefix count and temporary-
   prefix count are both zero across `instances/WORKING-P-A/**`. All package
   JSON parses; CSV/TSV column structure is consistent; Markdown files are
   nonempty. Direct binding hashes equal their repaired targets.
7. **Package containment and hygiene — PASS.** Package aggregate manifests and
   candidate hashes are unchanged; `git diff --check` passes; the App project
   status is empty; `HEAD`, `main`, and `origin/main` remain the accepted base.

## Unchanged substantive package bindings

- Pilot manifest SHA-256:
  `46a3decdbca321ed2c11c9c3f01f35c625c8fb1ff3257a437f48fe3dba5481be`.
- Replacement manifest SHA-256:
  `9a439ce90c48438f9cec1cfb2aaa5a463739c93e0fc85cc2c82926f8ca2efe94`.
- Rollback manifest SHA-256:
  `c3b17cbe5259ae9120fef5a03f717689b8151988ab7cb2f9fe91ce06e1d652db`.
- Work graph SHA-256:
  `c654a1a3434f8f364219ad8c17c59ee13fb9c6cfbe38f338dc6a085b6e6ef3dd`.
- Repair manifest SHA-256:
  `73cc5515d4578356100c09ee43888b933feb5fedbf3bb8b2b1b7063029e08799`.

Changed pre-existing surfaces: the 13 exact amendment files plus the one direct
package-local binding file. New repair records are confined to
`instances/WORKING-P-A-R1/`.

Blockers, semantic deltas, unexplained bindings, waivers, project writes, Git
writes, lifecycle actions, and temporary residue: none.
