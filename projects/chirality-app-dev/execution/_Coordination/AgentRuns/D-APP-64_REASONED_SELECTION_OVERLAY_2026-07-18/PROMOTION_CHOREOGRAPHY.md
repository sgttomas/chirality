# Promotion Choreography — D-APP-64 (executed by the orchestrator in CHANGE-posture mechanics; no judgment)

1. Recompute the frozen candidate's span SHA-256, file byte count, and
   `git hash-object`; require equality with `LANDING_MANIFEST.md`.
2. Confirm the active path
   `projects/chirality-app-dev/loop/WORKPLAN_2026-07-18b_app_dev_loop.md`
   is absent from `HEAD`, the index, and the worktree.
3. Materialize the active path by byte-copy of the frozen candidate
   (`cp` — never regeneration), as late as possible before staging.
4. Prove byte equality: `cmp -s` candidate ⇄ active, and equal
   `git hash-object` for both (`5f01938c92b719426e9c0716a5d5a3980cf78566`).
5. Dispatch V2 (invariant matrix I1–I12); fill its packet §10 verdict only
   after `RETURN_INVARIANTS_1.md` exists; nothing proceeds on `BLOCK`.
6. Append Receipt-70; rerun the receipt validator; dispatch V3
   (governed-diff, NM-5 enumeration-derived claims + whole-diff claim) over
   the full staged diff; fill its verdict only after
   `RETURN_GOVERNED_DIFF_1.md` exists; nothing lands on `BLOCK`.
7. Stage exactly the six manifest items; verify the staged file list equals
   the manifest scope and that pre-commit `HEAD` discovery (per the amended
   loader rule) still selects `WORKPLAN_2026-07-18_app_dev_loop.md`.
8. Commit the complete scope atomically (one commit).
9. Post-commit: require exactly one `HEAD` tree entry for the active path,
   mode `100644`, blob equal to the candidate blob; `HEAD` discovery selects
   `WORKPLAN_2026-07-18b_app_dev_loop.md`; run the deterministic closeout
   battery; push the branch; open the PR. Owner merge is the terminal
   integration act — never self-merge.
