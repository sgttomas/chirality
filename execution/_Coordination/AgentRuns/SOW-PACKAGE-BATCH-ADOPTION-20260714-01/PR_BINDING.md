# PR Binding

PR: `https://github.com/sgttomas/chirality/pull/227`
Number: `227`
Base: `main@3efa950aa981f9d3491bab2ab3b3319a5a2c6d5c`
Head branch: `codex/adopt-pkg-batch-workflow`
Initial integration head: `bc3b65aa99648cfacb0aaaff9807b0ddb442e710`
Final PR head: `0a1e5559209d7ee768a99566e37bd70dbca4e9ec`
Final state: `MERGED — REQUIRED FINAL-HEAD CI PASSED`
Merge commit: `4296d3f4069b838ae2e0d1c4845ebe0b944aece9`

The PR contains the accepted PKG-02 experiment evidence with its explicitly
approved immutable-evidence whitespace warnings, the bounded package-batch
workflow adoption, and the exact eight-member PKG-01/PKG-02 clean production
replacement. `DEL-01-01`, PKG-00, lifecycle, H1/H2, release, and retirement
remain excluded.

Both required checks passed on published head
`0a1e5559209d7ee768a99566e37bd70dbca4e9ec`. An earlier superseded-head
pre-merge run failed one App Dev concurrency test; the final-head rerun passed,
so the failure is retained as non-reproducing runtime evidence rather than
silently discarded.
