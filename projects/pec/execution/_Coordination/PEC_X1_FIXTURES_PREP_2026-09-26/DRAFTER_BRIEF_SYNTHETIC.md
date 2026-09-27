# Drafter brief B — synthetic grammar-edge fixtures (X1, provisional D-PEC-106)

Role: TASK (Type 2), bounded executor under WORKING_ITEMS (X1 preparation, undertaking
`HELP-HUMAN-PEC-20260925-POST-SCA005`). You do not delegate. Model: Opus 5.5, high reasoning.

## Write boundary (binding)

- Create and delete files **only** inside one directory you create with `mktemp -d` under
  `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/`,
  with `TMPDIR` set to that directory for every command. Never delete any other file there.
- Never write in any Git worktree. Never check out, switch or create branches. Read the
  repository only with read-only Git plumbing or plain reads of
  `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep`.
- No network access.

## Task

Author, fresh, the synthetic grammar-edge fixture files for the three PKG-02 parser
contracts and their manifest. **No parser exists and none may be written.** Read the three
contracts in full first (`projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/`
DEL-02-03, DEL-02-08, DEL-02-09 `ScopeOfWork.md`), the shared templates
(`workflows/construct-local-work-graph/resources/work-graph-template.md`,
`docs/templates/MEMORY_TEMPLATE.md`), and the committed test module that fixes the schema:
`projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/candidates/projects/pec/v2/tests/parsers/test_parser_fixture_integrity.py`.

Rules for every synthetic file:

- **No text copied from another loop's files** (DEL-02-08 REQ-017, DEL-02-09 REQ-014,
  DEL-02-03 REQ-017). The test rejects any 8-word run that also occurs in a pinned source
  blob, unless that run also occurs in a shared template. You may use the templates'
  structural text (headings, table headers, the "Stable run identity" bullet, the state
  vocabulary) and bare identifiers such as `receipt-contract-v2`, `Receipt-ID`,
  `Examined-Through`, `Parent-Receipt`, `Gate-Outcome`.
- Clearly synthetic identities only: run identities `SYN-RUN-…`, deliverables `DEL-99-NN`,
  commit SHAs made of repeated patterns that are obviously fake (for example `aaaaaaa` or a
  40-character run), PR numbers from `#9001` upward (the unresolved case uses `#99999999`).
- Put distinctive, obviously invented prose (for example "ZEBRA-PROSE-…" marker words) in
  every prose-bearing position of the prose fixtures, so later parser tests can assert that
  none of it reaches output.
- **File names must not be canonical feed names**: never `WORK_GRAPH.md`, `MEMORY.md`,
  `RECEIPT.md` or `LOOP_RECEIPTS.md` (other tools and name-based discovery glob those
  names). Use `work_graph/<case>.md`, `memory/<case>.md`, `receipts/<case>.md` under
  `fixtures/synthetic/`. Parser tests copy them into place at test time.
- No word "Remaining" or "remaining" anywhere (binding carried constraint on this packet).
- ASCII only, LF line endings, final newline, no trailing spaces, no tabs.

## Cases (labels are fixed by the test's `REQUIRED_SYNTHETIC_CASES`)

DEL-02-08 (REQ-017 minimum, plus VER-004/-007/-010 support):
`missing-run-identity`; `duplicated-run-identity`; `unrecognized-state-token` (one graph
carrying all six vocabulary states PLANNED READY ACTIVE BLOCKED UNCERTAIN COMPLETE on
different nodes plus one node whose state cell begins with a non-vocabulary token);
`no-node-table`; `unresolved-pr-number` (cites `#99999999`); `two-graphs-bind-one-deliverable`
(two files, both binding `DEL-99-01`); also `prose-in-every-position` (VER-010) and
`links-and-bindings` (DEL ids, relative links with link text, external URLs; VER-007).

DEL-02-09 (REQ-014 minimum, plus VER-003/-008 support):
`template-table-form` (the template `## Runs` table with rows); `entry-without-readable-run-token`;
`unreadable-date`; `file-without-run-index-entry`; `deliverable-without-memory-file`
(**no file**: constructed at test time as a deliverable folder with no MEMORY file);
`runs-section-mixed-with-dated-sections`; also `prose-in-every-position` and
`links-in-each-form`.

DEL-02-03 (REQ-017 minimum, plus VER-003/-007/-016 support):
`marker-carrying-ledger-entry` (a synthetic ledger with a `receipt-contract-v2` marker,
entries the marker governs carrying the four fields, and earlier entries it does not govern,
so AC-003's governed/ungoverned split is exercised in one file); `prose-structured-ledger-entry`;
`receipt-without-examined-through` (a central-receipt-shaped file); `malformed-ledger`;
`unreadable-file` (**no file**: constructed at test time by removing read permission from a
copy); `undeclared-loop` (**no file**: constructed at test time as a loop with no registry
declaration); also `receipt-folder-diverges-from-cursor` (VER-016: a receipt whose cursor
Receipt-ID differs from the folder it will be placed in; state both tokens in `expect`) and
`prose-in-every-position` (VER-007).

## Manifest

`fixtures/synthetic/MANIFEST.json`:

```json
{
  "schema": "pec-v2-parser-fixtures-synthetic/v1",
  "cases": [
    {"id": "SYN-WG-01", "case": "missing-run-identity", "files": ["work_graph/missing_run_identity.md"],
     "expect": {"run_identity_available": false, "fabricated_identity": false},
     "binds": ["DEL-02-08/REQ-006", "DEL-02-08/REQ-017", "DEL-02-08/AC-006", "DEL-02-08/AC-017", "DEL-02-08/VER-006", "DEL-02-08/VER-017"]}
  ]
}
```

- `id`: `SYN-WG-NN`, `SYN-MEM-NN`, `SYN-RCP-NN`.
- `files`: list of paths relative to `fixtures/synthetic/`; empty list only for test-time
  cases, which then carry a short `construction` sentence in your own words.
- `expect`: booleans, integers, lowercase-hyphen labels or lists of labels only — what the
  contract requires for the case (for example `limitation: "unrecognized-state"`,
  `coerced_state: false`). These labels are fixture-local; they are not an output schema.
- `binds`: per deliverable at least one REQ, one AC and one VER from the current contract that
  the case genuinely serves; cite the contract line for each in your report.
- 2-space JSON, ASCII, final newline.

## Checking

Copy the candidate `parsers/` directory into your mktemp dir, add your `fixtures/synthetic/`
files, and put the drafting stub
`PEC_X1_FIXTURES_PREP_2026-09-26/drafting_stub/pinned/` in place of `fixtures/pinned/`
(it pins the principal source blobs so the copy check is real). Run
`PEC_X1_FIXTURES_PREP_2026-09-26/run_fixture_suite.sh /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep 6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240 <your parsers dir>`.
Your cases must pass `test_synthetic_cases_cover_the_contract_minimums`,
`test_every_record_binds_a_requirement_criterion_and_verification` (synthetic part) and
`test_no_fixture_source_is_copied_into_the_tree`; failures that come only from the stub goldens
are expected.

## Report

Return: every file verbatim (path then content), the manifest verbatim, a case → contract-line
table for the bindings, the suite output tail, judgment calls, and your mktemp path.
