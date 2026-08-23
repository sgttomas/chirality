# Disposition 05 — PR #632 UID diagnosis accepted

- Disposition: `RECORD / RELEASE WP-F2`.
- Accepted return: `instances/A2-PKG09-R20-PR632-UID-DIAGNOSE-01/RETURN.md` with `PASS_DIAGNOSIS`.
- Accepted cause: the coherent mock UID family reaches the product's expected-UID metadata guard while real fixture objects carry the test process UID. CI exposes the mismatch; the local UID-501 host cannot prove that class.
- Accepted scope: focused-test-only `REAL_UID` derivation and deliberate-mismatch conversion exactly as inventoried. No product, fixture, package, daemon, or procedure change.
- Controls: R19 fixture and product proof script remain byte-identical at the recorded hashes. No GID or additional real-state path entanglement was found.
