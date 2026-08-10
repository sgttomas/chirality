# Validation R4.4.6 — successor freeze

Verdict: `PASS_MANAGER_STATIC — HELD_FOR_HELP_HUMAN_ACCEPTANCE`

Accepted freeze SHA-256:
`13566daa015b49fe1d88d4048bd0d961a29c19bfb653921a6a22a524033f5f89`.

The index and every bound object reproduce. Exactly 89 full-path return
occurrences target absent sibling `returned_r4_4_6/`; accepted `returned/`
remains 28 files with aggregate identity
`ea52c8ee03ba3e5cd0ce04013885aae35d3ac283026f5ca4a42626e95a81d618`.
The temp root is absent, stale prior-run fixed-root count is zero, the current
run-root count is 103 ledger mentions, C196/C197 and LLDB script are exact,
the 180-entry normalized command digest is
`adb9c9c36661b22929d4796ba8f3024d54c76d1d72fda36eeed388ab61b5ae27`,
and `git diff --check` passes. No frontend or non-App write occurred.

No fresh verifier was dispatched. No execution or product effect occurred.
