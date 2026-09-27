# Drafter brief A — pinned fixture manifest and goldens (X1, provisional D-PEC-106)

Role: TASK (Type 2), bounded executor under WORKING_ITEMS (X1 preparation, undertaking
`HELP-HUMAN-PEC-20260925-POST-SCA005`). You do not delegate. Model: Opus 5.5, high reasoning.

## Write boundary (binding)

- Create and delete files **only** inside one directory you create with
  `mktemp -d` under
  `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/`,
  with `TMPDIR` set to that directory for every command. Never delete any other file there.
- Never write in any Git worktree. Never check out, switch or create branches. Read the
  repository only with read-only Git plumbing (`git show`, `git cat-file`, `git ls-tree`,
  `git rev-parse`, `git log`, `git merge-base`) against
  `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep`.
- No network access.

## What X1 is

The packet commits golden-by-reference parser fixtures for DEL-02-03 (receipts parser),
DEL-02-08 (work-graph parser) and DEL-02-09 (MEMORY run-index parser). **No parser exists
and none may be written.** Read the three contracts in full first (paths under
`projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/`, each `ScopeOfWork.md`), then
SCA-005 `_ScopeChange/SCA-005_2026-09-23_2139/Impact_Assessment.md` §9.3 and
`_Coordination/SCA-005_PREP_2026-09-23/FEED_MODEL_V2_DESIGN_NOTE.md` §3.2 and §6.

The schema is fixed by the committed test module:
`projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/candidates/projects/pec/v2/tests/parsers/test_parser_fixture_integrity.py`.
Read it closely; your files must pass it. Run it with
`PEC_X1_FIXTURES_PREP_2026-09-26/run_fixture_suite.sh <repo> 6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240 <your parsers dir>`
where `<your parsers dir>` is a copy (in your mktemp dir) of the candidate `parsers/`
directory with your files added. The synthetic manifest is drafted by someone else; for
your runs, put a stub `fixtures/synthetic/MANIFEST.json` in your copy (for example
`{"schema":"pec-v2-parser-fixtures-synthetic/v1","cases":[]}`) and expect only
`test_synthetic_cases_cover_the_contract_minimums` (and possibly the binding test for
synthetic cases) to fail for that reason. Do not return the stub.

## Deliverables (return the full file contents in your final report, and leave them in your mktemp dir)

1. `fixtures/pinned/MANIFEST.json`
2. `fixtures/pinned/goldens/FC-1.json`, `FC-2.json`, `FC-3.json`, `FX-PEC-0.json`
3. A fact table: for every `source` value, the blob line number(s) where it occurs, so the
   manager and verifiers can recheck it.

JSON style: 2-space indent, keys in the order shown below, UTF-8, ASCII only, final newline.

## Manifest content

```json
{
  "schema": "pec-v2-parser-fixtures-pinned/v1",
  "policy": {"source_run_words": 3, "copy_run_words": 8},
  "templates": [
    {"id": "TPL.work-graph", "commit": "6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240", "path": "workflows/construct-local-work-graph/resources/work-graph-template.md", "blob": "91f10bfbe62c6442d6d56646f93f06f8bd7d9e1c"},
    {"id": "TPL.memory", "commit": "6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240", "path": "docs/templates/MEMORY_TEMPLATE.md", "blob": "0aebc32f72530576471c3bf6deff2aedbcbd6b7d"}
  ],
  "pins": [ ... ],
  "trees": [ ... ]
}
```

Each pin: `{"id", "fixture", "project", "kind", "commit", "path", "blob", "serves"}` —
`project` is the project folder (`projects/chirality-piping`, `projects/chirality-app-dev`,
`projects/pec`), `kind` is one of `graph`, `central-receipt`, `agentruns-evidence`,
`memory`, `ledger`, `registry`; `serves` lists exactly the deliverables the pin's
expectations bind. Full 40-hex commit and blob ids; resolve every blob yourself.

FC-1, FC-2, FC-3 are pinned at `d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b` (SCA-005 §B7).
FX-PEC-0 is pinned at the observation commit `6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240`.

Pins to include (resolve paths; check each exists):

- **FC-1** (Piping `PIPING_LINTER_SCOPE_20260923`): the graph
  (`.../WorkGraphs/PIPING_LINTER_SCOPE_20260923/WORK_GRAPH.md`, blob `ae942d99…`), the central
  receipt (`.../AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md`, `23623e2c…`), and the
  `MEMORY.md` of each deliverable whose `## Runs` bullet records this run (expected
  Piping DEL-08-01, DEL-08-05, DEL-10-04 — verify). Pin ids like `FC-1.graph`,
  `FC-1.receipt`, `FC-1.memory.DEL-08-05`.
- **FC-2** (Piping `PIP-DEC025-BASELINE-2026-09-23`): the graph
  (`.../WorkGraphs/dec025-clean-base-repair-2026-09-23/WORK_GRAPH.md`, `e471421c…`), the
  AgentRuns `EVIDENCE.md` (`76e618a5…`) as a negative for DEL-02-03 (an AgentRuns file other
  than `RECEIPT.md` is never read as a receipt: DEL-02-03 REQ-014/AC-015/VER-014), and the
  `MEMORY.md` of each deliverable the run's M1 names (DEL-00-08, DEL-10-04, DEL-12-01,
  DEL-17-06 — verify which carry dated headings, which carry `## Runs`, and whether
  DEL-10-04's blob mixes forms; if DEL-10-04's blob is the same blob as FC-1's pin, pin it
  once under the fixture it serves best and say so).
- **FC-3** (App `APP-REPLAY-BOUNDARY-2026-09-23`): the graph
  (`.../WorkGraphs/replay-session-boundary-2026-09-23/WORK_GRAPH.md`, `d25cae61…`) and App
  DEL-05-04 `MEMORY.md`.
- **FX-PEC-0** (PEC self-ingest, redefined): `projects/pec/v2/config/loops.json`
  (registry), `projects/pec/loop/LOOP_RECEIPTS.md` (closed historical ledger carrying the
  `receipt-contract-v2` marker), the PEC graph
  `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`,
  and the two PEC `MEMORY.md` files (DEL-01-06: template table with no rows; DEL-01-03:
  dated headings). **Binding carried constraint:** FX-PEC-0 must not reference or scan for
  `## Remaining` sections or the `remaining-items` surface, and PEC's former undertaking
  profile `remaining-loop` is not a source. So: pin no `_STATUS.md`, do not pin the
  `HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT` graph or receipt, and put no word
  "Remaining"/"remaining" anywhere in any file you return (ids, facts, labels, keys).

Trees (`present`/`absent` names in a directory at the pinned commit, or `tree_absent`):
FC-1 AgentRuns run folder holds `RECEIPT.md`; FC-2 AgentRuns run folder holds `EVIDENCE.md`
and no `RECEIPT.md`; FC-3 has no AgentRuns folder named for the run identity and none named
for the graph folder. Each tree record binds DEL-02-03 REQ-016 / AC-017 / VER-016 (and any
other REQ/AC/VER it truly serves).

## Goldens

Each golden: `{"schema": "pec-v2-parser-fixtures-golden/v1", "fixture": "<F>", "expectations": [...]}`.
Each expectation: `{"id", "pin", "tier", "fact", "source"?, "expect"?, "binds"}`.

- `tier: "fixed"` — the contract itself fixes this expectation for this case, so any
  conforming parser must produce it (for example DEL-02-08 AC-005: a terminal node declared
  `ACTIVE` while its cited PR is merged is reported as declared, with no completion,
  liveness or lag claim; AC-006: declared identity, never the folder name; DEL-02-03 AC-017:
  Receipt-ID from the cursor field, FC-2/FC-3 absences are coverage limits, never
  nonconformance; DEL-02-09 AC-004: a dated heading carrying only decision identifiers or
  parenthesized prose tokens yields a run-ID-unavailable marking).
- `tier: "observed"` — a content-minimal value present in the pinned blob that a declared
  grammar may or may not yield. **This is how the goldens avoid pre-empting the grammar
  choices the contracts leave to production** (DEL-02-08 TBD-002/TBD-003/TBD-007,
  DEL-02-03 TBD-002/TBD-004/TBD-007, DEL-02-09 TBD-002/TBD-005): if the parser yields the
  fact its value must equal this; if its declared grammar cannot, it must mark the fact
  unavailable. Do not record node lists, node counts, per-state counts or table-shape facts
  that depend on which tables a grammar counts as node tables (DEL-02-08 TBD-002) — leave
  those to the parser packet, and list them in your report as "deferred to the grammar".
- `source` — values that must occur in the pinned blob (the test checks each with word
  boundaries): identifiers and tokens as strings, PR numbers as integers under key `pr` or
  `*_pr`, SHAs as cited under keys ending `_sha`, dates under key `date`. Single tokens
  only; no whitespace, no URL, no prose.
- `expect` — booleans, integers, lowercase-hyphen labels, lists of labels, or the full
  40-hex `local_merge_commit` of a cited PR (must be a merge commit integrated at the pin;
  resolve with `git log --merges --grep '^Merge pull request #N from'`).
- `binds` — `DEL-02-0X/REQ-NNN`, `/AC-NNN`, `/VER-NNN` (and optionally `/CON-`, `/TBD-`) IDs
  that the expectation serves; per deliverable it binds, at least one REQ, one AC and one
  VER. Bind only IDs that exist in the current contract and whose text the expectation
  genuinely serves; cite the contract line for each in your fact table.

Minimum expectations to cover (add others only if contract-grounded and grammar-independent):

- FC-1/FC-2/FC-3 graphs: declared run identity (with `expect.equals_folder`); terminal node
  `F1` declared `ACTIVE`; the cited final PR with its `local_merge_commit` (#876, #873,
  #868); `expect.derived_claims: "none"` (no completion, liveness or lag claim).
  FC-3 additionally: the em-dash node-ID suffix prose is not emitted (DEL-02-08 REQ-010/AC-010).
- FC-1 receipt: Receipt-ID from the cursor field (equals folder); Examined-Through SHA as
  cited (observed); Parent-Receipt token (observed); Gate-Outcome yields presence only
  (value not emitted); generation is a central receipt with no shared validated schema.
- FC-2 EVIDENCE.md: never read as a receipt.
- MEMORY pins: form (`bullet`, `dated-heading`, `table`) as fixed where the contract names
  the class for that form (DEL-02-09 REQ-014/AC-014), run token/date/link targets
  (paths or PR numbers) as observed; run-ID-unavailable where AC-004 applies; partial
  coverage in FC-2 where a touched deliverable has no `## Runs`.
- FX-PEC-0: the registry declares, for loop `pec`, `loop-receipts-ledger` `historical`
  and `shared-dev-loop` `live` (bind DEL-02-03 only: REQ-014, REQ-015, AC-015, AC-016,
  VER-014, VER-015 — the DEL-02-08/09 contracts do not rely on these identifiers); the
  ledger carries the marker (observed) and a marker-governed entry's four fields (observed);
  the historical ledger's silence is never staleness (fixed, DEL-02-03 AC-016); the PEC graph's
  declared identity in its bold-bullet spelling (value fixed, equals folder); DEL-01-06
  `MEMORY.md` table with zero rows is a stated coverage limit (DEL-02-09 REQ-001/AC-001);
  DEL-01-03 dated headings: dates observed, run-ID-unavailable where AC-004 applies.

## Report

Return: the five files verbatim; the fact table with line numbers; the suite result from
`run_fixture_suite.sh` (verbatim tail); every judgment call; anything you could not
ground; your mktemp path. Do not claim anything you did not check.
