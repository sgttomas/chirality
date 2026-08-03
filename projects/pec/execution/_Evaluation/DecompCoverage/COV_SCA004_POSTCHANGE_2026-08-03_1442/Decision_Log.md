# Decision Log — COV_SCA004_POSTCHANGE

| Ref | Decision | Rationale |
|---|---|---|
| D-1 | Audit full SOFTWARE decomposition and compare with `COV_SCA004_PRECHANGE_2026-08-02_2327`. | Owner-authorized SCA-004 Gate 5 plan. |
| D-2 | Bind the audit to exact revision-1.4 candidate hashes before pointer movement. | Approved serialization and rollback posture. |
| D-3 | Retain Check 9 as `SKIPPED`; apply companion-register checks at full severity in Check 9b. | SOFTWARE variant with authoritative companion registers. |
| D-4 | Retain deliverable-folder-local artifact matching and the DEL-08-02 warning. | The warning is real, unchanged, and unrelated. |
| D-5 | Treat the pre-pointer state as sequenced Gate 5 state and require an exact post-move parity check by SCOPE_CHANGE. | The propagation plan forbids pointer movement before snapshot/audit completeness. |
| D-6 | Report no new finding and no coverage regression. | Post-change metrics and issue identities equal the pre-change baseline except for the intended SCA-004 mapping delta. |
