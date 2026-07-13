# C2F-R1 Containment Audit

Verdict: `PASS`

## Reproduced tracked sets

- Live tracked source diff from
  `main@e150c972889d05a8fc270239451a35c7512dc9a9`: 53 paths.
- Expected set: 48 exact C2R source paths, four exact C2A source paths, and
  parent-owned `WORK_GRAPH.json`: 53 paths.
- Expected-versus-live symmetric difference: empty.
- C2R/C2A source intersection: empty.
- All 55 C2R/C1G manifest hashes and all nine final App caller hashes match.

The tracked diff contains no project deliverable folder, `PKG-*`/`DEL-*`
production path, `_STATUS.md`, Remaining, lifecycle, receipt, release,
governance decision/history, or P1 canon change. Root C2R did not write App
source; App C2A remained within its four-path source set and C2A-R1 within its
two-path repair subset.

This fan-in wrote only its declared reconciliation evidence plus terminal
instance return/status. The temporary reproduction fixture was outside the
repository and removed. No Git mutation, project conversion, lifecycle act,
H1/H2 action, release, or retirement action occurred.

The accepted basis records pre-existing ignored/untracked state, including
`.claude-worktrees/`; it was not inspected or modified. Ignored build/harness
artifacts remain evidence limitations rather than authority or project state.
