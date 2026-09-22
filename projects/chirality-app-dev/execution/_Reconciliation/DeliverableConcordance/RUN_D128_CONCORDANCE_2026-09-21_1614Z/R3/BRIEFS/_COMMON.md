# R3 TASK common rules (RUN_D128, R3 cross-package synthesis)

You are a TASK (Type 2) worker dispatched by the R3 WORKING_ITEMS synthesis manager. You do not
delegate. You return a short report to the manager. Placeholders `<FROZEN_TREE>`, `<RUN>` and
`<APP_WORK>` are resolved in your dispatch prompt; never write their values into any output.

**Rulebook.** `<RUN>/CONVENTIONS.md` (read the sections your brief names) and
`<RUN>/RUN_BASIS.md` Addenda 3–11. CONTEXT never changes a Disposition. An agent disposition is
never a ruling. The owner's recorded R4-Q6 answer (Addendum 9) and the owner's statement that
v3.0.1 was notarized (Addendum 10) are NOT GOVERNING and are never applied to a row.

**Evidence roots (read-only):**
- `<FROZEN_TREE>/projects/chirality-app-dev/**` (deliverables, decision register, AgentRuns
  records, docs, frontend code);
- `<FROZEN_TREE>/projects/chirality-runtime/{packages,tests}/**`;
- the run folder `<RUN>/**`;
- Root governance docs (`<FROZEN_TREE>/docs/**`) only where the App docs defer to them.
- NOT Root `execution/`, NOT `projects/chirality-runtime/execution/**`, NOT the working
  repository's deliverables (they may carry run edits: always read the frozen tree).
- Git: only read-only `git -C <FROZEN_TREE> log|show|blame -L`. No other git, no installs, no
  test runs, no builds.

**Inputs.** The merged concordance is `<RUN>/R3/CLAIM_CONCORDANCE.csv` (deliverables) and
`<RUN>/R3/EXTENSION_CONCORDANCE.csv` (EXT). Read CSVs only through scripts (Python `csv`);
they contain quoted newlines. The helper `<RUN>/R3/_scripts/r3lib.py` has `read_csv` and
`write_csv` (header, rows, final `#END`). Do not edit anything under `<RUN>/R2/`, `<RUN>/R3/*.csv`
or `<RUN>/R3/_scripts/`.

**Write scope.** Only the output paths your brief names, under `<RUN>/R3/_work/`. Every CSV you
write is UTF-8, has a header, and ends with a final `#END` record (use `write_csv`). Put any
helper script you write in `<RUN>/R3/_work/<your task id>_scripts/`.

**Paths in outputs.** Never an absolute path. Use repo-relative paths
(`projects/chirality-app-dev/frontend/...:120`) or run-relative paths (`R2/PKG-09/...`).

**Style.** Plain, short sentences. Evidence, not opinion. No options or recommendations for
the owner: R4 packets are drafted later. Where you cannot decide, say so (`UNDECIDED`) with the
two readings; never force a verdict.

**Return** (≤ 12 lines): counts by verdict, output paths with SHA-256 (`shasum -a 256`), and
anything you could not decide.
