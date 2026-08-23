# Phase-B orchestration plan v10 — PR #632 fixture-mode portability repair

1. `WP-C1 DIAGNOSE`: one read-only Agent 2 runs the focused login-proof suite exactly once under `umask 0002`, freezes exact results, and inspects every relevant fixture/product creation site. No frontend write.
2. `WP-C2 IMPLEMENT`: only after accepted diagnosis, one bounded Agent 2 owns the test file and any diagnosis-proven minimal product mode hardening. It pins fixture directory/file modes, runs the authorized focused normal and single `umask 0002` proof plus syntax/typecheck/APP-HOLD, and freezes the frontend candidate.
3. `WP-C3 REVIEW`: one genuinely fresh source/evidence reviewer verifies diagnosis, complete fixture coverage, unchanged guards, any product hardening necessity, tests, scope, and no hidden umask reliance. Findings follow the standing failure rule.
4. `WP-C4 SOURCE_COMMIT`: on PASS, WORKING_ITEMS returns the exact frontend candidate to CHANGE; no build occurs until CHANGE supplies the immutable final frontend-touching commit.
5. `WP-C5 BUILD_RESTAGE`: after exact source commit, run the supply verifier once and offline pack once, verify package identity/guard/instruction root, restage only R20 revision/package identity/notes, and re-run read-only unchanged label/root gates.
6. `WP-C6 SUITES_TM_REVIEW`: run the prescribed sandbox diagnostic, single local-socket cure, and single `umask 0002` focused proof; record TM candidate; complete fresh overall review and governance-only pre-push gates.
7. `WP-C7 RECEIPT_PUBLICATION`: amend the governed receipt after content commit, validate, and hand publication to CHANGE. No rebase, force-push, or merge.

All shared writes are serialized. Any failed gate stops its dependent nodes; no node broadens product/proof/release authority.
