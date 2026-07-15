# VERIFY-B1 Attempts

One terminal verifier invocation completed all five members. There were zero member failures, retries, candidate repairs, semantic repairs, or member-evidence normalization repairs. The inherited verifier harness was bound before invocation to trim comma-separated reference tokens and to use a visible verifier-only mutation in the negative probe; these are established template bindings, not runtime failures or candidate changes.

After member closure, the first package-test invocation used the nonexistent
`tools/scope_of_work/tests` discovery directory and exited `1`. This was a
safe mechanical verifier-evidence defect: no candidate or project path was
touched, and all three exact outputs are retained under
`attempts/test-runner-path-001/` with SHA-256 values
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
(stdout),
`08985c809fcd7a316f70e4120d00d76d03aa62f7556e02bf4de952dbfcad4898`
(stderr), and
`4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865`
(exit record). The corrected exact target,
`tools/scope_of_work/test_scope_of_work_tools.py`, then passed 19/19. Its
stdout, empty stderr, and zero exit record are bound by the terminal manifest.
