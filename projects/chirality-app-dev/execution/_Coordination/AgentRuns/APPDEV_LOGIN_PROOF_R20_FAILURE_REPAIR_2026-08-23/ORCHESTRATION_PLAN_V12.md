# Orchestration plan v12 — PR #632 UID and host-identity portability

1. `WP-F1 DIAGNOSE`: one read-only Agent 2 traces mocked UID through failure-log metadata validation, inventories every host-entangled UID/GID/path/symlink/homedir assumption in the focused test, and freezes fixture/product identities. No frontend write or local reproduction claim.
2. `WP-F2 IMPLEMENT`: after manager acceptance, one Agent 2 owns only the focused test and its instance records; it applies the complete accepted test-only portability repair and runs the authorized focused normal, single `umask 0002` focused, full local-socket suite, typecheck, syntax, and APP-HOLD checks. Product source remains untouched.
3. `WP-F3 SOURCE_REVIEW`: a genuinely fresh Agent 2 reviews the entire sweep, repair, tests, fixture identity, scope, and fences. Failure cycles are bounded by the standing rule.
4. `WP-F4 SOURCE_COMMIT`: on PASS, CHANGE creates the immutable final frontend-touching commit and returns the exact revision. No package build occurs before this gate.
5. `WP-F5 BUILD_RESTAGE`: one supply verifier and one network-denied offline package build bind R20 to the new revision; package identity and unchanged-label/root read-only Step 0 are verified.
6. `WP-F6 CLOSEOUT`: extend the TM candidate, complete fresh review and governance gates, create a Receipt-excluded content commit, append the after-the-fact receipt, and hand normal publication to CHANGE. No merge.

Shared writes are serialized. Any failed gate stops its dependent nodes without broadening authority.
