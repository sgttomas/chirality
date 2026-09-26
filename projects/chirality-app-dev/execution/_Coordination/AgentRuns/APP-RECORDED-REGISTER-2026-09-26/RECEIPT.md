# Receipt — APP-RECORDED-REGISTER-2026-09-26

Derivative account of App follow-up FU5 from the
[APP-LIFECYCLE-DEPS work graph](../../WorkGraphs/app-lifecycle-deps-2026-09-26/WORK_GRAPH.md).
The sources below keep their authority.

## Owner direction

CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING. Ryan Tufts, 2026-09-26, Claude Code
conversation, on the parent session's decisions and work plan:

> D1 and D2 as recommended, D3 (a), and D4 yes proceed that way. Your work plan is approved.

This run carries item 3c of that plan, App follow-up FU5. As the parent session
relayed it, App dependency reads should compute blockers from the recorded
register, including the D-GOV-49 split between a project with an accepted DAG
and one without. Before this run they were CSV-only register evidence, and
`activeUpstreamBlockerCandidates` was the known surface. The parent session
relayed only this item's content; D1–D4 are recorded here only as part of the
quoted approval.

## What changed

- `frontend/src/lib/dependencies/recorded-register.ts` (new) is a TypeScript
  reading of the Root reference tools. It covers:
  - `tools/coordination/dependency_evidence.py`: `parse_declarations`,
    `union_register`, `recorded_register`, `resolve_accepted_dag` and
    `check_currency`;
  - the project mode of `tools/coordination/build_dev001_blocker_queue.py`
    (`build_project_queue` without `--evidence`).

  The module parses the declared sections, including the legacy headings of
  Root SPEC §5.2. It takes the union with `Dependencies.csv`. A matching entry
  counts once. On disagreement the declaration governs and the disagreement is
  reported. A declaration that matches only a RETIRED row is reported too.
  Each arc is judged by its supplier's `_STATUS.md` state against its required
  maturity: a declared maturity, then the rows, then the default threshold
  recorded in `_COORDINATION.md` (`INITIALIZED` when the record names none).
  Cycle arcs are held, and `NOT_TRACKED` deliverables get no verdict. With an
  accepted DAG, blockers come from the version named by `_DAG/_LATEST.md`, and
  a departure marks the affected deliverables `DAG_PENDING` with no verdict.
- `readDeliverableDependencies` covers the working-root dependencies API and
  the MCP `deps_read` tool. It keeps the raw CSV rows, headers and warnings,
  adds a `recordedRegister` field, and reads the execution root only inside the
  project root. When `_DEPENDENCIES.md` is present without a CSV, the absence
  warning now says the recorded register is read from the declared sections.
- `summarizeDependencyRows` keeps `activeUpstreamBlockerCandidates`. With a
  recorded register it is the number of blocking suppliers. Additive fields
  carry the verdict, the DAG-pending reasons, the disagreement count and the CSV
  blocker-subset count. The workbench and pipeline panels label the metric
  "Blocking upstream" and show the verdict or the reason there is none. The
  workbench lists the blocking suppliers.
- App SPEC §5.2 states the new behaviour. The FU5 row of the work graph points
  here, and a DEL-07-05 MEMORY row records the run.

## Parity

- Fixtures:
  `frontend/src/__tests__/fixtures/recorded-register/cases/` holds eight
  execution roots:
  - union without a CSV;
  - union with a CSV, where a declaration disagrees on maturity;
  - a declaration matching only a RETIRED row;
  - legacy headings;
  - a missing or `TBD` maturity taking the default threshold;
  - DOWNSTREAM-first rows judged by the supplier, with a cross-deliverable
    disagreement, a `NOT_TRACKED` unit and a held cycle;
  - an accepted DAG that is current;
  - a DAG departure.
- Expected results: `expected/<case>.json`, written by `generate_expected.py`
  from the Root functions themselves. `--check` re-checks them without writing.
- Test: `src/__tests__/lib/recorded-register-parity.test.ts` compares the
  TypeScript results with those files. Its header gives the regeneration
  command. A negative control broke the maturity override and the DOWNSTREAM
  reversal in the module. The affected parity cases then failed.
- Wider check, not committed: on this basis, the TypeScript and Python queues
  were compared on the four live project execution roots (App, Runtime,
  Piping with its accepted DAG, and pec). Queue rows, disagreements, arc counts
  and DAG-pending sets were identical.

## Checks (worktree candidate)

Recorded in the commit's hand-off to the parent session: typecheck, focused
and full Vitest, the parity generator `--check`, APP-HOLD `dispatch` ALLOW for
DEL-07-05, DEL-06-03 and DEL-02-01, `app_hold.py scan
--require-register-match` PASS, export regeneration, Root validators, the
tranche-manifest validator and this ledger's receipt validator.

## Limits

- The Runtime-owned `deps_read` descriptor
  (`projects/chirality-runtime/packages/contracts/src/harness/tool-descriptor.ts`)
  and the generated tool catalog still describe a CSV-only read. This run did
  not edit Runtime.
- The module skips symbolic-link unit folders and reads only regular files. It
  therefore never reads outside the folders it inventories. The Python tools
  follow links. The default-threshold reading of `_COORDINATION.md` is the App's
  own; the Root tools take it as `--default-maturity`.
- An unresolvable `_DAG/_LATEST.md` gives `NOT_ASSESSED` with its reason, where
  the Python tool stops with an error.
- The panels' new text is covered by the formatter's unit test. The panels
  render their loaded dependency state only after a client fetch, which the
  existing static render tests do not reach.
- No lifecycle transition, dependency acceptance, DAG acceptance,
  authority-corpus repin, Runtime change or release.

Execution: a Claude Code subagent (TASK-type executor, no delegation) in an
isolated worktree for the parent session. Model identifiers are withheld at
the dispatching session's instruction; the commit's session trailer identifies
the run.
