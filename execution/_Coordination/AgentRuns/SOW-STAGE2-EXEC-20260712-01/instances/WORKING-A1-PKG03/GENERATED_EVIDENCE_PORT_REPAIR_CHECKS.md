# A1 PKG-03 Generated-Evidence Portability Repair Checks

Authority: `amendments/A1-PKG03-GENERATED-EVIDENCE-PORT-001.md`.

Verdict: `PASS`.

- The child run record had exactly two authorized checkout-prefix-with-slash substitutions and no other tilde preimage. The portable PENDING intermediate had exactly two `~/` anchors and zero checkout prefix. This row is retained as the intermediate-event proof; the later required TASK PENDING-to-SUCCESS finalization is reconciled separately under `A1-PKG03-AUTHOR02-RUN-RECORD-RECON-001`.
- The registered-check JSON had exactly four authorized checkout-root substitutions and no tilde preimage. Postimage has exactly four `~` anchors and zero checkout prefix.
- Exact reverse substitution reproduced each recorded preimage SHA-256.
- The JSON postimage parses. Package status and every registered result remain `PASS`; commands, exit codes, and substantive stdout/stderr are unchanged modulo the authorized literals.
- Search before repair found no direct preimage-hash binding inside the package instance. The only bindings were the authorizing amendment itself; refreshed bindings: `NONE`.
- Candidate, source, status, map, parity, checklist, render, project, lifecycle, and sibling bytes were not modified.

The amendment, portable PENDING intermediate proof, current frozen terminal
binding, and reconciliation proof must be included in final package MANIFEST
and handoff.
