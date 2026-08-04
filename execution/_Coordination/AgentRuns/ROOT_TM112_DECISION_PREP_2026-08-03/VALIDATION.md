# N1 validation

Verdict: `PASS`

- `WORK_GRAPH.json` and `evidence/raw/CONTROLLED_RESULTS.json`: `jq empty` PASS.
- Exact source containment: Git blob equality PASS for
  `runtime/packages/daemon/src/runtime-daemon.ts` and
  `runtime/tests/daemon.test.ts` against HEAD.
- Existing daemon tests: 5/5 PASS outside the Unix-socket-restricted sandbox.
- Controlled direct reproducer: two terminal runs, all four cases completed
  within the declared stop/release boundaries.
- Controlled signal reproducer: child alive at 750 ms with live SSE; exited 0
  after controlled client release; no stdout/stderr error.
- Git whitespace check: `git diff --check` PASS.
- Write containment: initial repository state was clean; terminal `git status
  --short` lists only the untracked assigned RunID directory. No tracked file,
  Git index, branch, source, test, register, or foreign-loop change occurred.
- N2/N3 hold: preserved.
