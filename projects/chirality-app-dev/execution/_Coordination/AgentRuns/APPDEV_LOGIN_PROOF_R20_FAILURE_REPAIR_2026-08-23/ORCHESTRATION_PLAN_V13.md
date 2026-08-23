# Orchestration plan v13 — PR #632 UID exact-revision package/restage closeout

1. `WP-G1 BUILD_RESTAGE`: one Agent 2 invokes the frozen supply verifier once and network-denied pack once, verifies the unsigned package, rebinds only R20/status/package evidence to the immutable revision, runs unchanged-label/root read-only Step 0, and extends the TM candidate.
2. `WP-G2 FRESH_REVIEW`: a genuinely fresh evidence-only Agent 2 reviews package identity, one-shot evidence, R20 shell/claim safety, Step-0 nonmutation, TM calibration, retained source evidence, and all hard fences without rerunning commands.
3. `WP-G3 GOVERNANCE`: WORKING_ITEMS runs only unreached governance/control-plane pre-push gates, then freezes an exact Receipt-excluded content candidate.
4. `WP-G4 CONTENT_COMMIT`: CHANGE creates the immutable content commit and returns it.
5. `WP-G5 RECEIPT`: WORKING_ITEMS appends the after-the-fact receipt with verbatim owner direction and receipt-only checks, then returns publication readiness to CHANGE.

All shared writes are serialized. Any failed one-shot, package, review, governance, receipt, scope, or fence gate stops dependent nodes without retry.
