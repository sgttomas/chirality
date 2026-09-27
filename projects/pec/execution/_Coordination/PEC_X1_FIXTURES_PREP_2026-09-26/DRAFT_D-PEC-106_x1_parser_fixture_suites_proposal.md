# D-PEC-106 — P1 parser fixture suites for DEL-02-03, DEL-02-08 and DEL-02-09 (work-graph node X1) — proposal

Status: **DRAFT PROPOSAL / AWAITING_RULING**. **The number D-PEC-106 is provisional.** It becomes final only when HELP_HUMAN publishes this packet in `_DECISIONS/` and adds its register row; at `origin/main` `6c6cc1b00` the register has no D-PEC-104, D-PEC-105 or D-PEC-106 row. Prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN (undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node X1) for the PEC loop, 2026-09-26 (session date), from brief `briefs/X1P_FIXTURES_PROPOSAL.md` (SHA-256 `1cefcc48d5f9ac7f94e20a539bcc75ce45008c496b1651da0bd7f7585be1bbac`) and its `COMMON.md` (`51b70e46f1049696c456be1d4ab7b4b236e3cbfc6fa3a667ed0426035510b311`; X1P overrides it where they conflict). No earlier direction approves this file. It performs no production act: no tracked production file was edited, and every check ran on `git archive` exports. Suggested filing name: `execution/_Coordination/_DECISIONS/D-PEC-106_x1_parser_fixture_suites_proposal_2026-09-26.md`.

The act it asks for is bounded: **create 34 new files under `projects/pec/v2/tests/parsers/` and replace `projects/pec/software-workflow.json` with the exact bytes tabled below**, in one run of a bound act script, with no parser code and no lifecycle change. Add-on L (the production-start lifecycle transition) and add-on M (MEMORY rows) are separate questions.

## Provenance

- **Owner acts relied on.**
  - The owner's 2026-09-25 steering (`D-PEC-94`, `_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md`, `b6814e90…5a6b`): "You can continue with all the open work you identified." The work graph (`WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`, `1ec5719f…51ad8` at `6c6cc1b00`) turns it into node X1, "P1 fixture suites", state READY, with the carried items quoted under Findings.
  - SCA-005 checkpoint 2 (`D-PEC-92`) accepted `Propagation_Plan.md` (`50cd0b1d…1350`). Its §B7 is the fixture strategy; Impact Assessment §9.3 (`Impact_Assessment.md`, `0bcbe9bd…39bf`) is its source; checkpoint-1 question Q5 selected "(a) P1 pinned parser fixture suites only, three fixture classes".
  - `D-PEC-96` (ruled A, 2026-09-26; ruling `852057f0…399e`; revision 4 `4506597b…180e`; the owner's revision-4 direction `D-PEC-96_AMEND_DIRECTION_2026-09-26.md`, `c506732e…d3b2`) and its applied act (PR #950): registry schema v2, the closed vocabulary `shared-dev-loop`, `loop-receipts-ledger`, `agentruns-json`; `remaining-loop` dropped.
  - `D-PEC-99` (ruled A, 2026-09-26; ruling `3e34403a…c989`) and its act (PR #957): the `## Remaining` sections are retired, with no surface that reads them.
  - `D-PEC-98` (ruled A + S + M; ruling `039dc7e2…8361`) and `D-PEC-100` (ruled A + confirm B + M; ruling `13690e20…729b`): the current DEL-02-08/DEL-02-09 and DEL-02-03 contracts, which place the fixture suites at node X1 "under a later v2 packet".
  - The `D-PEC-101` currency act (PR #976) and the `D-PEC-103` act (PR #992, merged at the observation commit).
- **Fence.** `projects/pec/AGENTS.md` (`df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`) §"Write Scopes And Fences": "Every other write under `projects/pec` — including any new v2 source tree, scaffolding, manifest, or configuration — requires an owner-ruled `D-PEC` packet naming the exact paths, acts, verification, and rollback." No earlier ruling opens `v2/tests/parsers/**` or `software-workflow.json` for this work.
- **Precedents followed.** The `v2/**` slice packets `D-PEC-85` (`7389826d…7def`), `D-PEC-87` (`ba3d3e64…4569`), `D-PEC-89` (`962a7879…8a73`) and `D-PEC-91` (`5c044b09…13ec`): exact paths, registered checks, a fresh verifier applying `software-code-review`, rollback, limits, owner questions. The exact-bytes act packets `D-PEC-98` (`92b6f1a2…3e40`) and `D-PEC-100` (`39c4331e…e25b`): pinned preimages and basis files, temp-write-and-rename, rollback on failure, write-set inventory under `projects/pec`, refusal of a second run, run-root location guard, fault-injection tests, export-only checks. The `D-PEC-85` ruling's production-start lifecycle clause is the precedent for add-on L.
- **Source state.** Checked at `origin/main` **`6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240`** (PR #992 merge; the observation commit), after `git fetch`. The SCA-006 checkpoint-3 acceptance commit **`189f205ff`** is an ancestor; the decomposition, `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv` and `docs/PRD.md` (v2.4) are byte-identical at both commits (`9374c21f…8eb1`, `94ee5d18…9805`, `1d24a4b8…916e`, `93b0bb07…4c7c`, `ae49b806…3fbe`); `_Decomposition/_LATEST.md` is `768ae4c4…a771` (revision 1.6, `current_basis`).
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e`), run from `projects/pec` with `--operation exact-correction-preparation` on all 41 possible targets (the 35 act paths, three `_STATUS.md`, three `MEMORY.md`): `ALLOW`, exit 0, ×41 (`evidence/reliance_hold_preflight.out`).

## Method

- **Preparation.** Ad hoc WORKING_ITEMS plan under the reliance operation `exact-correction-preparation`, with the bundled `software-test-planning` workflow (`workflows/software-test-planning/WORKFLOW.md`, `8f36adc77c18b58ee331867542f068f8bb714a014d52036caea610adba4fdfcd`) for the risk-to-test mapping and the accepted profile `docs/SOFTWARE_WORKFLOW_PROFILE.md` (`9cc54bfb649168801c2ea060acb242145f48a0e08ac893e6ca38824439f7c5b3`) for check registration. Catalog `workflows/index.json` `2bfa2c5faae1081c55ce95fd3d81c00b1d87ba1f51d0bc13e03c8fcb6ccdafb3` (precedence project → user → bundled; no project or user workflow of these names). The catalog lists `software-bounded-implementation`, which `D-PEC-91` named, as `historicalOnly`; the current implementation-node rules are those of `construct-local-work-graph` (`workflows/construct-local-work-graph/WORKFLOW.md`, `fa04e1347f8594654e81e5c097414f8b6f602560fe15267a374145f43ae3a4c9`), as `projects/pec/AGENTS.md` states.
- **Independent check.** Fresh read-only `pec-reviewer` TASKs applying `.agents/skills/software-code-review/SKILL.md` (`ee085d589c44f912d11a59eead8edac214f0343761d26b0d33e886a979888bca`) to the candidates, plus a packet review (verdicts in this folder).
- **Scope-of-work workflow.** Not used: no contract is written or changed. One-line disclosure: Root's `scope-of-work` `MODE=REVISE` is not adopted in PEC and plays no part here.
- **Actors.** Two Type 2 TASK drafters (`pec-task`): one for the pinned manifest and goldens, one for the synthetic fixtures, each writing only in its own scratch directory. WORKING_ITEMS wrote the test module, the `software-workflow.json` postimage, the act script and all check aids, integrated the drafts (normalizing the pinned JSON and retiering one expectation, below) and ran the checks. Models: Opus 5.5 (`claude-opus-5-5`) at `high`, per the brief; the host reports the serving model, and role identity is instruction-asserted.

## What preparation found

### Scope, lifecycle and dependencies

- **Targets.** Source and test files under `projects/pec/v2/**` plus the check registry `software-workflow.json`. No `ScopeOfWork.md`, `_STATUS.md` (outside add-on L), `MEMORY.md` (outside add-on M), register, dependency, context, decomposition or `docs/**` file.
- **Lifecycle.** DEL-02-03 (`_STATUS.md` `6f94c04f…f06f`), DEL-02-08 (`4341d6b2…4fe`) and DEL-02-09 (`e67be587…1056`) are all **`INITIALIZED`** at `6c6cc1b00`. None is `CHECKING` or `ISSUED`, so nothing stops the packet.
- **What the method implies.** Committing fixture suites that the three contracts name as outputs (DEL-02-08 OUT-002/OUT-003, DEL-02-09 OUT-002, DEL-02-03 OUT-003) is production work in those deliverables. Root `docs/SPEC.md` §3.3 (`feb5e79c…109e`) lists `INITIALIZED → IN_PROGRESS` for WORKING_ITEMS "when semantic step is skipped", and `IN_PROGRESS` as the state in which "Human or WORKING_ITEMS begins work". So the method implies the production-start transition for all three. It is **not** assumed: option A changes no `_STATUS.md`, and the transition is offered as **add-on L** (question 4), on the `D-PEC-85` pattern (a production-start `INITIALIZED → IN_PROGRESS` at actual start, after fresh checks).
- **Dependency rows.** Each deliverable has one ACTIVE `PREREQUISITE` row on DEL-01-01 (`DEP-02-03-003`, `DEP-02-08-003`, `DEP-02-09-003`) at `SatisfactionStatus` `PENDING`. Under `projects/pec/AGENTS.md` §"Selection and decisions" such a row blocks work only when the work needs its target. The fixtures need no record-tier type: the goldens are expectations, not typed output (below). Parser production (each OUT-001) does need it; that is the later packets' concern.

### Smallest honest scope: why no golden states parser output

The brief says the parsers are later packets and asks for the smallest honest scope if a fixture cannot be meaningful without parser code. A golden that stated the full expected parser output would have to fix choices the three contracts leave to production: which tables are node tables and how the identity bullet is recognized (DEL-02-08 TBD-002), PR syntaxes and resolution method (TBD-003), SHA representation (TBD-007), receipt constructs and cursor recognition (DEL-02-03 TBD-002, TBD-004, TBD-007), row, bullet and heading grammars (DEL-02-09 TBD-002, TBD-005), and the output shape, which the record-tier contract types (DEL-01-01). DEL-02-08 REQ-003 and DEL-02-03 REQ-002 also require the grammar to be declared before code exists. So **no golden here states parser output**. Instead each golden expectation is one of two tiers:

- **`fixed`** — the contract itself fixes the expectation for this case, so any conforming parser must produce it. Examples: DEL-02-08 AC-005 (terminal node `F1` declared `ACTIVE` while its PR is merged, with no completion, liveness or lag claim); AC-006 (declared identity, never the folder); DEL-02-03 AC-017 (Receipt-ID from the cursor field; FC-2 and FC-3 absences are coverage limits, never nonconformance); DEL-02-09 AC-004 (a dated heading carrying only decision identifiers or parenthesized prose tokens yields run-ID-unavailable).
- **`observed`** — a content-minimal value that occurs in the pinned blob and that a declared grammar may or may not yield. If the parser yields the fact, its value must equal this one; if the declared grammar cannot yield it, the parser must mark it unavailable (DEL-02-08 REQ-009, DEL-02-03 REQ-004, DEL-02-09 REQ-007).

Facts that depend on a grammar choice are left out and listed for the parser packets: node lists, node counts, per-state counts and non-terminal node states; DEL bindings, SHAs and paths in graph cells; `Owner-Direction`/`Model-Attribution` presence; which ledger entries the marker governs; Examined-Through ancestry (DEL-02-03 TBD-008); MEMORY entry and row counts, non-run dated headings, and code-span paths as link targets. The synthetic manifest follows the same rule: the drafter removed 33 grammar-dependent expectations (mostly counts) at the manager's direction and kept only counts the case fixes by construction (for example `nodes_emitted: 0` for a graph with no table).

What the X1 tests can then check without any parser is the fixture itself: every pin resolves through read-only plumbing and is on integrated history; every class's tree shape holds at its pin; every golden `source` value occurs in its pinned blob; every golden is content-minimal; no source is copied into PEC's tree; the synthetic set covers every contract minimum; every record binds a REQ, an AC and a VER. These implement **the fixture-side part** of DEL-02-03 VER-017, DEL-02-08 VER-016/VER-017 and DEL-02-09 VER-014. The golden tests that run each parser over these fixtures, and every other VER, belong to the parser packets. No AC is claimed as met by X1.

### The candidates

| Group | Files | What they are |
|---|---|---|
| Registration | `software-workflow.json` (modified) | New check `v2-parsers` (`python3 -m unittest discover -s v2/tests/parsers -p test_*.py`, cwd `.`) and path rule `["v2/tests/parsers/**", "software-workflow.json"] → v2-parsers`. Nothing else changes; the `v2-core-posture` rule the posture checker asserts is byte-identical. |
| Test module | `v2/tests/parsers/test_parser_fixture_integrity.py` | Ten stdlib-only tests with an exact `TEST_TO_VERIFICATION` map (the `test_store_lifecycle.py` pattern). One Git call site, allowlisted to `cat-file`, `ls-tree`, `rev-parse`, `merge-base` and `config --get`, run with `GIT_NO_LAZY_FETCH=1`, `GIT_NO_REPLACE_OBJECTS=1`, `GIT_TERMINAL_PROMPT=0`, `GIT_OPTIONAL_LOCKS=0`. No write call (checked by an AST test). |
| Pinned fixtures | `fixtures/pinned/MANIFEST.json`; `fixtures/pinned/goldens/{FC-1,FC-2,FC-3,FX-PEC-0}.json` | 2 template pins, 17 source pins, 3 tree records, 65 expectations (30 `fixed`, 35 `observed`). |
| Synthetic fixtures | `fixtures/synthetic/MANIFEST.json`; 27 Markdown files under `fixtures/synthetic/{work_graph,memory,receipts}/` | 24 cases, 21 file-backed and 3 constructed at test time. |

Layout choices this packet makes, since it is the first PKG-02 test packet: the suite root is `v2/tests/parsers/` (as `v2/tests/config/` and `v2/tests/storage/` hold theirs), fixtures sit under it (the `v2/tests/config/fixtures/` pattern), and the parser packets add their tests to the same `v2-parsers` check. No synthetic file uses a canonical feed name (`WORK_GRAPH.md`, `MEMORY.md`, `RECEIPT.md`, `LOOP_RECEIPTS.md`), because other tools and name-based discovery glob those names (SCA-005 risk R-09); the parser tests copy them into place at test time.

**Golden format and threshold (fixes DEL-02-08 TBD-006, DEL-02-03 TBD-006 and DEL-02-09 TBD-007).** The contracts leave the golden format, the pinned MEMORY blobs and "the length threshold for the no-source-text assertion" to this packet. Proposed, subject to question 3:

- Golden format: the schemas `pec-v2-parser-fixtures-pinned/v1`, `pec-v2-parser-fixtures-golden/v1` and `pec-v2-parser-fixtures-synthetic/v1` that the test module enforces. Golden strings are single tokens (no whitespace, no URL, at most 200 characters); `source` strings, PR numbers, SHAs and dates are checked against the blob with word boundaries.
- `source_run_words = 3`: a golden, and later a parser output, may hold no run of three or more consecutive whitespace-separated words that also occurs in a pinned source blob. This is the no-source-text assertion; PEC-K-10 values (identifiers, paths, SHAs, counts, states) are single tokens and never trip it.
- `copy_run_words = 8`: no fixture file may hold an eight-word run that occurs in a pinned source blob unless the run also occurs in a shared template (the `work-graph-template.md` and `MEMORY_TEMPLATE.md` pins). Fresh fixtures may reuse template structure; the synthetic drafter's wider check over all 300 feed-named blobs at `d61981ee2` and `6c6cc1b00` found no overlap.

### Fixture inventory with its bindings

Pins (full ids in `fixtures/pinned/MANIFEST.json`; all resolve, all equal, all unchanged at `6c6cc1b00`, see the pinned-reference verification below):

| Pin | Commit | Path (project-relative where long) | Blob | Serves |
|---|---|---|---|---|
| TPL.work-graph | `6c6cc1b00` | `workflows/construct-local-work-graph/resources/work-graph-template.md` | `91f10bfb…` | copy check only |
| TPL.memory | `6c6cc1b00` | `docs/templates/MEMORY_TEMPLATE.md` | `0aebc32f…` | copy check only |
| FC-1.graph | `d61981ee2` | Piping `WorkGraphs/PIPING_LINTER_SCOPE_20260923/WORK_GRAPH.md` | `ae942d99…` | DEL-02-08 |
| FC-1.receipt | `d61981ee2` | Piping `AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md` | `23623e2c…` | DEL-02-03 |
| FC-1.memory.DEL-08-01 / DEL-08-05 | `d61981ee2` | Piping DEL-08-01 and DEL-08-05 `MEMORY.md` (bullet `## Runs`) | `15dcfee1…` / `91700122…` | DEL-02-09 |
| FC-2.graph | `d61981ee2` | Piping `WorkGraphs/dec025-clean-base-repair-2026-09-23/WORK_GRAPH.md` | `e471421c…` | DEL-02-08 |
| FC-2.evidence | `d61981ee2` | Piping `AgentRuns/PIP-DEC025-BASELINE-2026-09-23/EVIDENCE.md` (never read as a receipt) | `76e618a5…` | DEL-02-03 |
| FC-2.memory.DEL-00-08 / DEL-10-04 / DEL-12-01 / DEL-17-06 | `d61981ee2` | Piping `MEMORY.md` of the four deliverables the run's M1 names | `71921955…` / `53ec1d47…` / `7c683795…` / `5f1a8beb…` | DEL-02-09 |
| FC-3.graph | `d61981ee2` | App `WorkGraphs/replay-session-boundary-2026-09-23/WORK_GRAPH.md` | `d25cae61…` | DEL-02-08 |
| FC-3.memory.DEL-05-04 | `d61981ee2` | App DEL-05-04 `MEMORY.md` (bullet `## Runs`) | `4d1e8a96…` | DEL-02-09 |
| FX-PEC-0.registry | `6c6cc1b00` | `projects/pec/v2/config/loops.json` | `d5e60779…` | DEL-02-03 |
| FX-PEC-0.ledger | `6c6cc1b00` | `projects/pec/loop/LOOP_RECEIPTS.md` (closed, historical, carries the marker) | `ea6f32cc…` | DEL-02-03 |
| FX-PEC-0.graph | `6c6cc1b00` | `WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` | `bf0b0c62…` | DEL-02-08 |
| FX-PEC-0.memory.DEL-01-06 / DEL-01-03 | `6c6cc1b00` | PEC DEL-01-06 `MEMORY.md` (template table, no rows) / DEL-01-03 `MEMORY.md` (dated headings) | `fdf9351d…` / `497bb004…` | DEL-02-09 |

DEL-10-04's blob is one object at `d61981ee2` carrying the FC-1 run as a `## Runs` bullet and the FC-2 run as a dated section; it is pinned once, under FC-2, as the real mixed-form instance (DEL-02-09 TBD-005). Tree records: FC-1's AgentRuns run folder holds `RECEIPT.md`; FC-2's holds `EVIDENCE.md` and no `RECEIPT.md`; the App AgentRuns folder holds neither `APP-REPLAY-BOUNDARY-2026-09-23` nor `replay-session-boundary-2026-09-23`. Each binds DEL-02-03 REQ-016/-017, AC-017/-018, VER-016/-017.

Bindings by requirement (the full per-expectation lists are in the goldens; `verify_x1p_bindings.py` found all 424 binding references defined in the contracts at `6c6cc1b00`):

| Deliverable | Pinned expectations bind | Synthetic cases bind |
|---|---|---|
| DEL-02-08 | REQ-005/AC-005/VER-005 (F1 `ACTIVE` ×4 graphs); REQ-006/AC-006/VER-006 (declared identity; FC-2, FC-3 ≠ folder); REQ-008/AC-008/VER-008 (final PR #876, #873, #868 → local merge commit, `observed`); REQ-010/AC-010/VER-010 (FC-3 em-dash node suffix not emitted); REQ-016/AC-016/VER-016 (the pinned suites) | REQ-004/-006/-007/-008/-009/-010/-015/-017 with their AC and VER (SYN-WG-01..08) |
| DEL-02-09 | REQ-001/AC-001/VER-001 (FC-2 partial coverage; DEL-01-06 zero rows); REQ-002/-003/-004/-005 with AC/VER (form, token, links, date); REQ-004/AC-004/VER-004/CON-004 (run-ID-unavailable, fixed); REQ-007/TBD-005 (DEL-10-04 mixed); REQ-014/AC-014/VER-014 | REQ-001..005/-007/-008/-014 with AC/VER, TBD-005 (SYN-MEM-01..08) |
| DEL-02-03 | REQ-003/AC-003/VER-003 (marker, Receipt-197 fields, `observed`); REQ-004/-007 (central receipt best-effort; Gate-Outcome presence only); REQ-014/AC-015/VER-014 (EVIDENCE.md never a receipt; declared surfaces); REQ-015/AC-016/VER-015 (historical label, silence not staleness); REQ-016/AC-017/VER-016 (cursor Receipt-ID; coverage limits); REQ-017/AC-018/VER-017 | REQ-003/-004/-007/-014/-016/-017 with AC/VER (SYN-RCP-01..08) |

Synthetic cases: DEL-02-08 REQ-017's six (missing and duplicated identity, unrecognized state token — all six vocabulary states plus `MARINATING`, no node table, unresolved `#99999999`, two graphs binding `DEL-99-01`), plus prose-in-every-position and links-and-bindings; DEL-02-09 REQ-014's table form and five edges (deliverable without a MEMORY file constructed at test time), plus prose and links in each form; DEL-02-03 REQ-017's six (unreadable file and undeclared loop constructed at test time), plus a folder-divergent receipt (VER-016) and prose in every position. All identities are obviously synthetic (`SYN-RUN-…`, `DEL-99-NN`, PR numbers from `#9001`, `example.invalid` links, `ZEBRA-PROSE` markers). The files are UTF-8 with U+2014 as the only non-ASCII character, where the observed corpus and the template use the em dash.

### FX-PEC-0 redefinition (carried from `D-PEC-96`)

§B7 names "FX-PEC-0 PEC self-ingest (`remaining-loop`)". The graph carries: "fixture FX-PEC-0 is redefined without the `## Remaining` sections". The owner's direction of 2026-09-26 is that there must be none going forward and no scanning for them. Proposed redefinition (question 2):

- **FX-PEC-0 is PEC's own shared-development-loop surfaces and its closed historical ledger**, pinned at the observation commit `6c6cc1b00`: the registry row, the ledger, the undertaking graph and the two `MEMORY.md` files tabled above. It is the only fixture that exercises the real registry: `pec` is the only registered loop, declaring `shared-dev-loop` `live` and `loop-receipts-ledger` `historical`.
- It pins no `_STATUS.md`, declares or relies on no profile or surface that reads `## Remaining` sections, and names no `remaining-items` surface. No manifest key, golden, synthetic file or test names them or scans for them. PEC's former `remaining-loop` undertaking profile is not a source. The retirement undertaking's graph and receipt are left out, so that no FX-PEC-0 id or value carries that undertaking's name.
- Pinned PEC blobs mention the retired sections in their own prose. No expectation touches that prose, and PEC-K-10 keeps it out of any output.
- Preparation checked the candidate bytes once for the word (case-insensitive, `evidence/run_main/hygiene.out`): absent. That check is a preparation step on this packet's own bytes; nothing committed repeats it.
- It departs from §B7 in one respect that the owner rules on: §B7 pinned every fixture at `d61981ee2`, where PEC had no shared-loop surfaces, only the retired shape. FC-1, FC-2 and FC-3 stay pinned at `d61981ee2` as §B7 and the contracts (DEL-02-08 AC-016, DEL-02-09 REQ-014, DEL-02-03 REQ-017) require.
- None of the three contracts requires FX-PEC-0 (DEL-02-08 CON-004, DEL-02-09 CLM-013, DEL-02-03 CON-007). DEL-02-03 CON-007 leaves "whether PEC's closed ledger is exercised as a historical-grammar fixture" to this packet. FX-PEC-0 is therefore supplementary real-corpus evidence bound to requirements the contracts already state; it adds no output. Directed self-ingest remains DEL-10-10's (SOW-064).
- One expectation was retiered at integration: the PEC graph's identity bullet uses the bold spelling `- **Stable run identity:**`, and DEL-02-08 TBD-002 leaves recognition of that spelling to the grammar, so its identity value is `observed`, not `fixed`.

### R-05 re-read against the revision-4 vocabulary

SCA-005 risk R-05 (Impact Assessment §8.4): "PEC's own P1 self-ingest corpus stays old-shape (57 `## Remaining`, ledger, 64 `Dependencies.csv`) for the whole SCA-005 horizon (DN I-16)"; risk "P1 exercises almost none of the new feeds"; control "fixtures carry the new grammars; `remaining-loop` profile covers PEC (Q8 a)".

Reading at `6c6cc1b00`:

1. **The fact no longer holds.** PEC adopted the shared development loop (`D-PEC-94`), and it writes a work graph, one central receipt so far and `MEMORY.md` files. `D-PEC-99` retired all 57 `## Remaining` sections. The PEC ledger is closed at Receipt 197 and declared `historical`. The registry row declares `shared-dev-loop` v1 `live`, `loop-receipts-ledger` v1 `historical` and `agentruns-json` v1 `historical`.
2. **The control's second half is void.** The revision-4 vocabulary has no `remaining-loop`, so nothing "covers PEC" under that profile.
3. **Residual risk, restated.** PEC's new-shape corpus is small and young: two graphs, one central receipt, two `MEMORY.md` files (one dated-heading, one template table with no rows), and no bullet-form or populated table-form run index. Self-ingest alone still exercises the new feeds thinly.
4. **Control, restated.** FC-1, FC-2 and FC-3 carry the other loops' shapes, and the synthetic set carries the grammar edges. FX-PEC-0 adds the real registry path and PEC's historical ledger, which no other fixture has. `Dependencies.csv` belongs to DEL-02-05 and is outside X1. R-05 is recorded here as **retired in its original form and superseded by the residual above**. The SCA-005 record itself is not edited.

### DEL-02-08/09 contract-wording items (reported, no contract changed)

| Item carried in the graph | Bearing on the fixtures |
|---|---|
| DEL-02-08 CLM-013 still calls `c9e5cd87d` "the decomposition pin" (now `189f205ff`) | None. The synthetic graphs follow the template at `6c6cc1b00`, whose six state tokens are unchanged since `c9e5cd87d`. |
| The re-pinned observation clause does not list the `AnticipatedArtifacts` and DL-4 loci | None for bytes. The fixture set is grounded in DEL-02-08's `AnticipatedArtifacts` cell (three fixture classes plus synthetic), found verbatim by the `D-PEC-98` verifier. |
| DEL-02-08 L29–31 / DEL-02-09 L30–32 "…did not exist at `c9e5cd87d`" | None. |
| "`_CONTEXT.md` and `_REFERENCES.md` name revision 1.5 and PRD v2.3" (DEL-02-08 L44, DEL-02-09 L43); since `D-PEC-101` both name revision 1.6 | None. |
| (Also carried) DEL-02-08/09 still quote the prior DEL-01-01 `REQ-006` text, anchored to its old hash (`D-PEC-100` downstream consequence), and their CON-001 says DEL-01-01 does not yet type WorkGraph/WorkNode or MEMORY-sourced RunRecord evidence; the rebuilt DEL-01-01 now does | None for bytes: no golden depends on record-tier typing. It matters to the parser packets' AC-014/AC-012 review. |
| (Also carried) DEL-02-08 TBD-004 and DEL-02-09 TBD-003 still say the profile identifiers arrive with a DEL-01-06 rebuild; the rebuilt DEL-01-06 contract and applied registry now fix them | **Bears on FX-PEC-0.** The registry expectations are bound to DEL-02-03 only, whose contract relies on those identifiers (CLM-018). No DEL-02-08/09 expectation relies on a profile identifier or asserts discovery through the registry. A later DEL-02-08/09 revision could add those bindings. |

### Carry-forwards and external anchors

- **`D-PEC-99` Part B.** The exhibit (`69b646f8…f45e`) routes its twelve Part B items to nodes S1, S2 and S4 only. **No Part B item names X1**, so there is nothing to land. DEL-02-03-REM-001 is a Part A evidence inquiry, unselected; it stays in the exhibit and this packet does not select it.

  | Part B item | Landing |
  |---|---|
  | none for node X1 | — |

- **Old S2 quotations.** The `D-PEC-100` consequence rule covers contracts that quote replaced S2 text. X1 writes no contract, and no candidate quotes any contract text (bindings are IDs only). The DEL-02-08/09 quotations of prior DEL-01-01 text stay with a later DEL-02-08/09 revision.
- **External anchors.** No ACTIVE `Dependencies.csv` `EvidenceQuote` cites any X1 target (a scan of every `Dependencies.csv` under `projects/pec/execution` for `software-workflow.json` and `v2/tests` found none). The three contracts are not changed, so their anchors are unaffected, and no register is written.

### Pinned-reference verification

- **Resolution.** `report_x1p_pins.py` at `6c6cc1b00` (`evidence/run_main/pins.md`): 19/19 pins resolve. Each commit is an ancestor of the observation commit, and each `(commit, path)` resolves to the tabled blob. Every blob is also byte-unchanged at the same path at `6c6cc1b00`, so there is no drift today. `d61981ee2` is `d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b` (PR #881 merge), an ancestor of `origin/main`. The FC-1/2/3 blob prefixes match Impact Assessment §9.3 (`ae942d99…`, `23623e2c…`, `e471421c…`, `76e618a5…`, `d25cae61…`).
- **Goldens against blobs.** `test_golden_source_values_are_grounded_in_their_pinned_blobs` checks every `source` value against its blob with word boundaries (PR numbers as `#N` or `/pull/N`). Each `local_merge_commit` is a merge commit integrated at its pin: #876 `0b276a7f…`, #873 `c56ae4a2…`, #868 `10b672ca…`. The drafter's fact table gives the blob line numbers (drafter return, saved with the verdicts). Negative control: a changed value fails.
- **If a pinned commit becomes unreachable.** Four cases:
  - **Shallow clone or partial clone.** The suite checks first. `rev-parse --is-shallow-repository` must be `false` and `config --get extensions.partialclone` must be unset. With lazy fetching disabled, a missing blob fails rather than touching the network (REQ-019/-015/-012).
  - **Commit or blob missing from the object store.** The failing test names the pin and says: `PIN UNREACHABLE <id> (<commit>:<path>): <cause>. The fixture suite needs a full, non-shallow clone without a partial-clone filter. If the commit is gone from the canonical repository, the fixture must be re-pinned by a new owner-ruled packet; nothing re-pins automatically.`
  - **Commit no longer an ancestor of `HEAD`** (a history rewrite). The same message.
  - **In every case** nothing is skipped, and neither goldens nor pins change automatically.

  Negative controls (shallow, partial clone and wrong blob) confirm the failures. Hosted CI does not run the v2 Python checks today. Its PEC job runs the frozen corpus's `npm test` with a sparse, blob-filtered, shallow checkout, so a future hosted v2 job must fetch full history. That is Root/CI scope (F-5/X-2, as in `D-PEC-91`).

### Check results (preparation)

`run_x1p_checks.sh` at `6c6cc1b00`, on two `git archive` exports (pre and post) whose `.git` borrows the source repository's objects (`evidence/run_main/SUMMARY.out`; every raw output is beside it):

```text
basis commit: 6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240
python: Python 3.13.7; git: git version 2.54.0 (Apple Git-157)
PASS act: check-only 0, apply 0, rerun refuses 1
PASS containment: software-workflow.json modified; new directory v2/tests/parsers with 34 files; nothing else
INFO affected checks: harness-self-check v2-api-contract v2-core-posture v2-loop-registry v2-parsers v2-store-guard
PASS registered checks after the act: v2-parsers exit=0 v2-core-posture exit=0 v2-api-contract exit=0 v2-loop-registry exit=0 v2-store-guard exit=0 harness-self-check exit=0
PASS v2-parsers verbose: 10 tests ok
PASS bindings: RESULT PASS 424/424
PASS pins: RESULT PASS 19/19
PASS strict identical before/after, export root normalized (exit=1)
PASS harness identical before/after, export root normalized (exit=0)
PASS receipts identical before/after, export root normalized (exit=0)
PASS candidate hygiene and carried-constraint word absent
PASS fault injection: RESULT PASS 11/11
PASS negative controls: RESULT PASS 14/14
OVERALL PASS
```

- **Strict registers** (D-GOV-48): exit 1 before and after, 0 errors and 26 pre-existing `XRG-013` warnings (owner-deferred), identical output.
- **`v2-core-posture`**: `core_tree_sha256` `dd7e1dda…6e5a` unchanged; `workflow_sha256` moves from `8ec9ba6d…8a8b` to `d55fff77…bbd`; verdict PASS.
- **Negative controls** (`negative_controls_x1p.py`): each of 13 single mutations makes its named test fail and the unmutated copy passes. The mutations are a wrong blob id; a false `RECEIPT.md` presence; `tree_absent` on an existing folder; an ungrounded golden value; a three-word source run in a golden; a copied 12-word run in a synthetic file; a whole pinned blob copied in; a required case removed; an unlisted synthetic file; an expectation without a VER; a partial clone; a shallow clone; a test missing from the verification map.
- **Fault injection** (`test_apply_x1p.py`), 11 cases. Rename failure, unexpected modified file, extra file, temporary hash mismatch and a write failure after the modify each exit 1 and restore the tree exactly: created files and directories removed, modify restored. A changed pinned file, a modified target not at its preimage and an already-present new directory are each refused at preflight. Check-only writes nothing; apply succeeds; a second run refuses. Run-root evidence written during the act is tolerated, and a bound copy outside a run root is refused.

## Options

- **A — the 35 exact paths in one act, no lifecycle change (recommended).** 34 created files under `projects/pec/v2/tests/parsers/` and `software-workflow.json` modified, as tabled; FX-PEC-0 as redefined; no parser code; no `_STATUS.md` or `MEMORY.md` touched. Add-ons L and M are independent.
- **A + L, A + M, A + L + M** — as A, with the add-ons tabled below.
- **Amend** — for example: drop FX-PEC-0 (the manifest, the FX-PEC-0 golden and the test's fixture set change, so re-preparation); drop the synthetic set and leave it to the parser packets (the test module's synthetic checks change, so re-preparation); different thresholds (two constants, re-preparation); a different suite root or check name.
- **Defer** — nothing opens; the parser packets would each have to author and pin their own fixtures.

A variant without the `software-workflow.json` change is not offered: no registered check would run the tests.

## Exact product grant (A)

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance may run the bound act script **once**. Paths are relative to the repository root. Preimage `—` means the file must be absent (created). Every postimage is the candidate file of the same path under `candidates/`, copied byte for byte into the run root.

| Path | Preimage SHA-256 | Postimage SHA-256 |
|---|---|---|
| `projects/pec/software-workflow.json` | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` | `d55fff77a1d216a7b1ab78b16e3ff3f2747fb3b542a2b269367ec3afa83e0bbd` |
| `projects/pec/v2/tests/parsers/test_parser_fixture_integrity.py` | — | `1ec0a7902c95907439d3579e2eed4308922b92ed1798cbc1eb2b42dc99d65bd3` |
| `projects/pec/v2/tests/parsers/fixtures/pinned/MANIFEST.json` | — | `0a07807081840f55c581c36264bec76b254d1c956574c0806a014140a423a5a9` |
| `projects/pec/v2/tests/parsers/fixtures/pinned/goldens/FC-1.json` | — | `3e93a8d7d4b6350a2268ec091d6796db1dcdf488d5025a2d18a6adb0d674d68e` |
| `projects/pec/v2/tests/parsers/fixtures/pinned/goldens/FC-2.json` | — | `19c9a6e8fc1b55efeefa7537cfc46ff508344b34d993a613aaf3812da4fe4770` |
| `projects/pec/v2/tests/parsers/fixtures/pinned/goldens/FC-3.json` | — | `a23725af786c9da96faf8c3b971b0ae0b4ed06c7ceb10132e6b93e81ac8efb25` |
| `projects/pec/v2/tests/parsers/fixtures/pinned/goldens/FX-PEC-0.json` | — | `ea38966446ce5b3eb4d4ff9f4841ac96fc7b9dfa5cfb98967ac724131c43a6b1` |
| `projects/pec/v2/tests/parsers/fixtures/synthetic/MANIFEST.json` | — | `7c9ba70561584b6a29934554fb645eb62cf6b830282b387d617b7977c84e1849` |
| `…/synthetic/memory/entry_without_readable_run_token.md` | — | `38243567f072606fe5214a0e86223a32bf6c62bbe7de7a3205e2a10f7c4313cc` |
| `…/synthetic/memory/file_without_run_index_entry.md` | — | `21891babb92e21a16637b7851a1ec1ce91e9145974baf8903788f5b0553fbf41` |
| `…/synthetic/memory/links_in_each_form_bullet.md` | — | `29972401929b3e3bd0c83691cb001be5f7b50dbb720e49627e5cec9aaaaa39cc` |
| `…/synthetic/memory/links_in_each_form_heading.md` | — | `d98b0e6baa3deaa330ffec5731224b083c58a0bc8fd2c43b11b007e8f5f5c0f4` |
| `…/synthetic/memory/links_in_each_form_table.md` | — | `f0b7561f1d92ba20b56edfdaedc006714b1bac92b1e14c100d61ba479de8ce29` |
| `…/synthetic/memory/prose_in_every_position_bullet.md` | — | `02843c9a1769a221dda1c4900905cacf7be7948bd3480b218dde3af497df6547` |
| `…/synthetic/memory/prose_in_every_position_heading.md` | — | `456d3d87c7adbb8efba45ecc9c6bf8381cdc39081300073e658862e261830748` |
| `…/synthetic/memory/prose_in_every_position_table.md` | — | `f436fd3263efb1bf27029c0942cc1e8038d21bb665349d1b1cc9f8ffd32ef1c7` |
| `…/synthetic/memory/runs_section_mixed_with_dated_sections.md` | — | `20d7ffb89b8fe47a7b03d017aaf60c4aa3148dac1793496638548c3c424f77a9` |
| `…/synthetic/memory/template_table_form.md` | — | `4bdf79945eff6308fda4a7f0f1c3ac603181e2d8d1e49964c8b404d62e77067f` |
| `…/synthetic/memory/unreadable_date.md` | — | `d5b0ff8be0a05f75ebbd450a5ea2ae0a9583fd3a630c756bb1670ff145ecea63` |
| `…/synthetic/receipts/malformed_ledger.md` | — | `44dd411d61dac4e192c192d96aabf2681b982ae42682884bbbcbc8127ed7cbd7` |
| `…/synthetic/receipts/marker_carrying_ledger_entry.md` | — | `aa74d4e35883dc02dcb1162700258974da1c796cb5c8fa4f10386c5e390c27b1` |
| `…/synthetic/receipts/prose_in_every_position_central.md` | — | `8a91d677f951bdb2621f1242114fd7acc74e747820890111fd2455bfe3bd0045` |
| `…/synthetic/receipts/prose_in_every_position_ledger.md` | — | `9acf2a98c38c1758e2df28ef8a89ce67268403c9b235216cedbbd5e0c939c782` |
| `…/synthetic/receipts/prose_structured_ledger_entry.md` | — | `66df3795f7aa49a292f57095ba5720c4247ded553492ce0925784325ae4d0e90` |
| `…/synthetic/receipts/receipt_folder_diverges_from_cursor.md` | — | `b5582c4d7c3963eb45432f6c95d5584ba9627c8d1f401ed87f7f50b5b2256fdc` |
| `…/synthetic/receipts/receipt_without_examined_through.md` | — | `8ab389eebe7a35448098afde63834d96847b27d6b8f972a70e8e60226da5f072` |
| `…/synthetic/work_graph/duplicated_run_identity.md` | — | `cb0f16cbd96e15d9973eefb2db75c394fa2ad77926f0310296d77caace398e8f` |
| `…/synthetic/work_graph/links_and_bindings.md` | — | `e06d4323510ed2eb2c604908a766745056f11a451bdf46c5bcefeb87dec9fb1d` |
| `…/synthetic/work_graph/missing_run_identity.md` | — | `1394b4b435ce33c43b5e6280d5098d1170af9d5db805946df62334c7166a1a1e` |
| `…/synthetic/work_graph/no_node_table.md` | — | `3192a26bffaff4bc62035f72be52b6ad08eb47eada25f4ad4891d7cd11d6674d` |
| `…/synthetic/work_graph/prose_in_every_position.md` | — | `1752d8e889a32ff5123b63e6231f8cfd71bb896d4bd96bfe97cc5177d410a166` |
| `…/synthetic/work_graph/two_graphs_bind_one_deliverable_a.md` | — | `2517e96eeaa4311370af7cabf4f7d7c9df0e6460e7fbde5581c5c1830fe28462` |
| `…/synthetic/work_graph/two_graphs_bind_one_deliverable_b.md` | — | `f8492a641361b7e6183ce76dcbaf18b70d1369cc5bd89e98607cfb2a3e64853c` |
| `…/synthetic/work_graph/unrecognized_state_token.md` | — | `a6142d24708ecddcd2b74c20e2b2ba8f685e339e480c5ed83db4edf13be0e376` |
| `…/synthetic/work_graph/unresolved_pr_number.md` | — | `03bf235275cad181cdfc131a63c439896658b5651871831c59c4ade00f65075f` |

(`…/synthetic/` is `projects/pec/v2/tests/parsers/fixtures/synthetic/`.) The directory `projects/pec/v2/tests/parsers` must not exist before the act. The grant creates no other file, directory, source, parser, dependency or configuration and modifies no other path; in particular no file under `v2/src/**`, `v2/config/**`, `v2/contracts/**`, `v2/tools/**`, `v2/docs/**` or the other `v2/tests/**` suites.

Read-only files the act re-verifies and never writes (SHA-256 at `6c6cc1b00`):

- `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`
- `projects/pec/execution/_Decomposition/Deliverables.csv` `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805`
- `projects/pec/execution/_Decomposition/ScopeLedger.csv` `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e`
- `projects/pec/docs/PRD.md` `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe`
- `projects/pec/AGENTS.md` `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`
- `projects/pec/v2/config/loops.json` `fd342b4f29edf3bece24a8d785b4a03d1a60158e62227753e4e1fa03529f53d7`
- `projects/pec/v2/config/loops.schema.json` `104ed64820b7a1fa6f24249cb6817653b8a624f43c52ea181ae4fd5d510cb143`
- `projects/pec/v2/config/service_core_posture.json` and `projects/pec/v2/tools/check_service_core_posture.py` (hashes in `apply_x1p.py`)
- the three `ScopeOfWork.md` (DEL-02-03 `c8bb9f1bb64d1772aff1be7ab9ef67e3e873bf708074639aa6096ec5ae7b294b`, DEL-02-08 `2319661b3225aa8c48ca4a82423e0459e806373fccb67985c4c7536a843fdd26`, DEL-02-09 `eab18e17a41f9ca979a932cc0dc2ba4dea590340e4e3a8a404ffd5f3013b6f5e`) and the three `_STATUS.md` (`6f94c04f79b678082b0407f93ec9c898d988c2693c0d1e19791f5cff985cf06f`, `4341d6b2e192b3ada04a5897de94245639980d0d2048b2b8cb3202771dfe04fe`, `e67be5871d8cd0f2a02e96c76418d5e161be5d17c7e5e44c7577bf829e171056`).

The act re-verifies the three `_STATUS.md` before writing. If add-on L is selected, its transition runs **after** the act script and verifier (below), so the pin holds during the act.

### Add-on L — production-start lifecycle transition (only if question 4 selects it)

At actual production start of X1 — after the act has run, the registered checks have passed and the verifier has passed — WORKING_ITEMS runs, from the repository root:

```text
zsh tools/scaffolding/write_status.sh "projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars" IN_PROGRESS "WORKING_ITEMS+production-start"
zsh tools/scaffolding/write_status.sh "projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser" IN_PROGRESS "WORKING_ITEMS+production-start"
zsh tools/scaffolding/write_status.sh "projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser" IN_PROGRESS "WORKING_ITEMS+production-start"
```

- **Tool.** `tools/scaffolding/write_status.sh` `0bf835f54f4bb9a78a51d0b56392a8686d1f255f06d3c2bcaf7e8665f77bece3` at `6c6cc1b00`. Recompute before use and stop on mismatch.
- **Preimages.** The three `_STATUS.md` hashes above.
- **Postimages.** Each file changes in exactly three ways: `**Current State:** INITIALIZED` becomes `**Current State:** IN_PROGRESS`; `**Last Updated:**` takes the act date `{D}`; and one History line is appended, `- {D} — State set to IN_PROGRESS (WORKING_ITEMS+production-start)`.
- **Prototype.** A run on an export with `{D}` = `2026-09-26` produced `935f8885…9c43`, `17d60ae2…2abe` and `24a20b34…208e`, exit 0 ×3. The verifier checks that no other byte departs from the preimage.
- **Meaning.** The transition records the semantic-step skip that `docs/SPEC.md` §3.3 allows and implies no acceptance, CHECKING or ISSUED. Downstream edges that require `INITIALIZED` (`DEP-03-01-010/-015/-016`, `DEP-04-05-003`) remain satisfied as maturity.
- **Without L.** The three deliverables stay `INITIALIZED` while fixtures they own exist in the tree. The graph records that as an open lifecycle consequence, and the first parser packet raises it again.

### Add-on M — MEMORY rows (only if question 5 selects it)

At the undertaking's closeout (graph node M1), WORKING_ITEMS appends one `## Runs` row to each of the three `MEMORY.md` files:

- **DEL-02-08 and DEL-02-09.** Their files are created at M1 under `D-PEC-98` add-on M.
- **DEL-02-03.** Its file is created at M1 under `D-PEC-100` add-on M.
- **Preimage.** Each file is absent at `6c6cc1b00`. X1's row goes after the row those add-ons write.
- **The row, in each file:**

```text
| HELP-HUMAN-PEC-20260925-POST-SCA005 / {D} | P1 fixture suites committed under D-PEC-106 (graph node X1). | <link to the central receipt>; PR #{PR}; <link to the D-PEC-106 ruling record> |
```

The verifier checks that no other byte departs from the file as the earlier add-on leaves it plus this row.

## Generation method (binding)

The act is one run of `apply_x1p.py`, **SHA-256 `815957272cf3474d5ac9efd1a03ae518a636ec7f28b3f5e593abae91aceffe0e`**. It is stdlib-only Python, prepared with CPython 3.13.7, generated by `build_apply_x1p.py` from `apply_x1p.template.py`, and copied byte for byte into the run root with the candidates:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/X1_FIXTURES_{D}/apply_x1p.py --repo <REPO_ROOT> --candidates projects/pec/execution/_Coordination/X1_FIXTURES_{D}/candidates [--check-only]
```

**Failure semantics.**

- **Preflight.** Any of the following exits 1 before any byte is written:
  - a candidate does not hash to its postimage;
  - `software-workflow.json` does not hold its preimage;
  - a created target or the new directory exists;
  - a temporary sibling exists;
  - a pinned file differs;
  - the script's directory is inside `projects/pec` but outside a run root (`projects/pec/execution/_Coordination/X1_FIXTURES_*`).
- **Write.** Each postimage is written to `<path>.x1ptmp`, hash-checked and renamed into place, creating parent directories as needed.
  - On any failure after the first write, the script rolls back and exits 1. The failures covered are an I/O error, a hash mismatch, a write-set mismatch and a changed pinned file.
  - Rollback removes every created file, restores `software-workflow.json` from the preimage bytes read at preflight, and removes every directory the script created and every temporary file.
  - Exit 2 reports an incomplete rollback. It was never observed in testing.
- **Write set.** Every file under `projects/pec` is inventoried (path and SHA-256) before and after the write. The run root is excluded. The difference must be exactly the 34 creates and the one modify.
- **Second run.** It fails preflight. The script never touches `_STATUS.md`, `MEMORY.md` or a Scope of Work.

The check aids are not bound:

| Aid | SHA-256 | Role |
|---|---|---|
| `test_apply_x1p.py` | `c194c7a2577c229c3200b8e91dd0334a4768610cdd781c2894aed860a3548c57` | fault injection, 11 cases |
| `build_apply_x1p.py` / `apply_x1p.template.py` | `ef4478ca…3357` / `99cd6c9b…a80e` | regenerate the act script from the candidates at a commit |
| `run_x1p_checks.sh` | `48d6a456a5cf448341e2526421e4167ccd27e16dd8b1dd1e6ac932331c127953` | every preparation check on pre/post exports (the rerun method) |
| `run_fixture_suite.sh` | `7c7559f0d203770580e768da80c910cbca1b2bfd0df124ea87041554d9e2ee02` | the candidate suite against a borrowed-object scratch repository |
| `verify_x1p_bindings.py` | `039e4f56aa7d68a3dc3c237e3ccb41449300da43f8d4c107c8277da4733ca135` | every binding defined in its contract at a commit |
| `report_x1p_pins.py` | `1177a02015569d4205ecd637f5ed39ebd7595d29abd3a789031279f0f76d1e61` | pinned-reference table and drift |
| `negative_controls_x1p.py` / `.sh` | `e476c8b1…6c` / `06f8fec3…5ee` | 13 mutations plus the unmutated control |

## Finite verification

Run with `PYTHONDONTWRITEBYTECODE=1`, an explicit Python 3.10 or later (record the path and version) and a Git that honours `GIT_NO_LAZY_FETCH` (2.44 or later; the observed version was 2.54.0), on the act branch in a **full, non-shallow clone without a partial-clone filter**. Record each command, exit code and output in the run root.

| Check | Command | Required result |
|---|---|---|
| 1. Preconditions | ruling and register row on fetched `origin/main`; `apply_x1p.py --check-only`; `pec_reliance_hold.py --operation dispatch-for-production` on each of the 35 targets before dispatch, and `--operation rely-for-production` before fan-in | pins as tabled; `CHECK preflight passed`; `ALLOW` everywhere; on any mismatch stop and route to the owner (no re-pin is pre-authorized) |
| 2. Act | `apply_x1p.py` | exit 0; closing `CHECK targets 35/35 byte-exact; write set = grant (34 created, 1 modified, 0 removed …)` |
| 3. Registered checks | from `projects/pec`: `v2-parsers`, `v2-core-posture`, `v2-api-contract`, `v2-loop-registry`, `v2-store-guard`, and `harness-self-check` (cwd `../..`), via `tools/software_workflow/run_registered_checks.py` or their registered commands | exit 0 each; `v2-parsers` lists the ten tests of `TEST_TO_VERIFICATION`; posture `core_tree_sha256` unchanged |
| 4. Selection | `select_affected_checks.py software-workflow.json <changed paths>` | the six checks of row 3 |
| 5. Bindings and pins | `verify_x1p_bindings.py <repo> HEAD <run root>/candidates`; `report_x1p_pins.py <repo> HEAD <manifest>` | `RESULT PASS 424/424`; `RESULT PASS 19/19` |
| 6. Every-PR and registers | `harness.py self-check`; `validate_pec_loop_receipts.py --repo-root .`; `validate_decomposition_registers.py --strict projects/pec/execution`, before and after | outputs identical before and after (at `6c6cc1b00`: strict exit 1 with 0 errors and 26 `XRG-013` warnings; harness and receipts exit 0) |
| 7. Lifecycle | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md'` | empty (unless add-on L ran, then exactly the three tabled files) |
| 8. Containment | `git diff --name-status origin/main...HEAD` | the 35 paths; the run root and HELP_HUMAN's records under `execution/_Coordination/**`; L's and M's files if selected; nothing else |
| 9. Whitespace | `git diff --check origin/main...HEAD` | clean |

Re-audit: not recommended. No decomposition truth, register or topology changes.

### Independent verifier

A fresh read-only TASK that authored nothing applies `software-code-review` to the written files and returns a verdict file. Defects go back to WORKING_ITEMS; the verifier does not repair. It checks:

1. **Basis.** The ruling and register row are on `origin/main`, the run-root script hashes as bound and the pins match.
2. **Byte identity.** The written files equal the tabled postimages.
3. **Test and fixture review.** Every golden `fixed` expectation is fixed by the contract text it binds. Every `observed` value occurs in its blob and leaves the grammar choice open. No golden or synthetic `expect` pre-empts a TBD or CON. The synthetic cases meet the contract minimums without copied text. The Git helper is read-only and fails closed on shallow and partial clones.
4. **FX-PEC-0.** It is as ruled (question 2). No manifest key, golden, synthetic file or test names or scans for the retired sections.
5. **Containment and lifecycle.** As rows 7–8 above.

## Administrative grant

- **Scope.** One WORKING_ITEMS instance runs the act and the checks, add-on L if selected (after the verifier passes), and add-on M at closeout if selected. It runs the reliance preflights. One fresh read-only TASK is the verifier.
- **Run root.** `execution/_Coordination/X1_FIXTURES_{D}/`, in the default-writable fence. It holds `apply_x1p.py` (exact bytes), `candidates/`, the check aids and all outputs, plus `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md` and `VERIFIER_VERDICT_NN.md`. No `_run_records/` entry is written in any deliverable.
- **Records not opened.** `docs/STATUS.md` and `README.md` stay with HELP_HUMAN under `D-PEC-88`. Registers, dependency files, contracts and `_Evaluation/**` stay closed.
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning, unless the owner states otherwise.
- **Publication.** Branch, commit, push, PR and merge follow the standing Git authorization of 2026-09-12, with required CI and independent review on the actual candidate. The register row, receipt and graph records are HELP_HUMAN's.

## Rollback

- **During execution.** On exit 1 the tree under `projects/pec` is as before, with no temporary file. If a later check fails, discard the branch or worktree.
- **Before merge.** Close the PR and discard the branch.
- **After merge, at owner direction.** A revert PR:
  - removes the 34 created files and the `v2/tests/parsers/` directory;
  - restores `software-workflow.json` to `8ec9ba6d…8a8b`;
  - removes M's rows, if M ran;
  - if L ran, restores the three `_STATUS.md` preimages by file revert. `write_status.sh` blocks backward moves, and SPEC §3.4 treats such a correction as a human-authorized administrative act.

  No schema, store or source is involved. The ruling record and register row are never reverted; a rollback is its own register row and record. The run root stays as non-current evidence with a rollback note.

## Limits

This proposal, and any ruling selecting A, an add-on or an amendment, grants none of the following:

- any parser, grammar declaration, per-loop grammar table or other source under `v2/src/**`, or any change to `v2/config/**`, `v2/contracts/**`, `v2/tools/**`, `v2/docs/**` or the existing `v2/tests/**` suites;
- any claim that an acceptance criterion of DEL-02-03, DEL-02-08 or DEL-02-09 is met. The X1 tests implement only the fixture-side part of the VER items named in `TEST_TO_VERIFICATION`;
- any `ScopeOfWork.md` change, including the carried DEL-02-08/09 wording items and the DEL-02-07 `CLM-011` count;
- any register, dependency, context, reference, decomposition, `_ScopeChange/**`, PRD, `AGENTS.md`, `docs/**` or foreign-project write;
- any lifecycle change other than add-on L's single `INITIALIZED → IN_PROGRESS` per deliverable, and none under A;
- `CHECKING`, `ISSUED`, artifact acceptance or a REVIEW gate act;
- a resolution of any TBD or CON item, other than the golden format, pinned blobs and threshold that DEL-02-08 TBD-006, DEL-02-03 TBD-006 and DEL-02-09 TBD-007 assign to this packet;
- a hosted-CI or Root change (F-5/X-2), or any re-pin: a pin that becomes unreachable is re-pinned only by a new owner-ruled packet;
- any reading, writing or scanning of `## Remaining` sections or a `remaining-items` surface;
- selection of the `D-PEC-99` Part A inquiry DEL-02-03-REM-001, or an edit of the exhibit.

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, amend or defer.** Recommendation: **A**, the 35 exact paths in one act, with no parser code and no lifecycle change.
2. **FX-PEC-0 redefinition.** Confirm FX-PEC-0 as PEC's own shared-loop surfaces and closed historical ledger, pinned at `6c6cc1b00` rather than §B7's `d61981ee2`. It reads no retired section, uses no retired profile, and leaves out the retirement undertaking. Recommendation: **confirm**. Without an answer, the tabled bytes apply.
3. **Golden scope and threshold.** Confirm that the goldens record only contract-fixed and observed facts, with grammar-dependent facts left to each parser packet. Confirm the thresholds: 3 words for the no-source-text assertion (golden and, later, parser output) and 8 words, net of shared-template text, for the no-copied-text check. Recommendation: **confirm**.
4. **Add-on L — production start.** Record `INITIALIZED → IN_PROGRESS` for DEL-02-03, DEL-02-08 and DEL-02-09 at actual X1 production start, as tabled, or leave them `INITIALIZED`. The method implies the transition, since committing contract-named fixture outputs is production work. `D-PEC-85` is the precedent. It is your decision, and this packet does not assume it.
5. **Add-on M — MEMORY rows.** Add one row to each of the three `MEMORY.md` files at closeout, as tabled, or record the run only in the graph and central receipt. `projects/pec/AGENTS.md` allows either.
6. **Model steer.** Keep the defaults above, or state others.

## Preparation evidence

Everything ran on `git archive` exports in the session scratchpad, never on a checkout. Interpreter: Python 3.13.7 (CPython); Git 2.54.0; local date 2026-09-26. Artifacts, all in this prep folder with hashes in `SHA256SUMS`:

- `candidates/projects/pec/…` (the 35 postimages);
- `apply_x1p.py` (bound), `apply_x1p.template.py`, `build_apply_x1p.py`, `test_apply_x1p.py`;
- `run_x1p_checks.sh`, `run_fixture_suite.sh`, `verify_x1p_bindings.py`, `report_x1p_pins.py`, `negative_controls_x1p.py` and `.sh`;
- `DRAFTER_BRIEF_PINNED.md`, `DRAFTER_BRIEF_SYNTHETIC.md` and `drafting_stub/` (the drafters' inputs);
- `evidence/` (`run_main/` with every check output, `reliance_hold_preflight.out`, and the drafter returns);
- `VERIFIER_VERDICT_NN.md` (the preparation verdicts, with dispositions).

Basis at `6c6cc1b00`:

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` / `agents/AGENT_WORKING_ITEMS.md` / `projects/pec/AGENTS.md` | `c8ce87ef…1dffd` / `9ae4bea2…9665` / `df9196d1…5eb8` |
| `_Decomposition/SOFTWARE_DECOMP.md` / `Deliverables.csv` / `ScopeLedger.csv` / `ContextBudgetQA.csv` / `_LATEST.md` | `9374c21f…8eb1` / `94ee5d18…9805` / `1d24a4b8…916e` / `93b0bb07…4c7c` / `768ae4c4…a771` |
| `docs/PRD.md` (v2.4) / Root `docs/SPEC.md` | `ae49b806…3fbe` / `feb5e79c…109e` |
| SCA-005 `Propagation_Plan.md` / `Impact_Assessment.md` / `FEED_MODEL_V2_DESIGN_NOTE.md` | `50cd0b1d…1350` / `0bcbe9bd…39bf` / `4b9ccb9f…2d12` |
| Work graph / `_REGISTER.md` | `1ec5719f…51ad8` / `fe2cc825…45ea` |
| `D-PEC-96` ruling / revision 4 / amend direction | `852057f0…399e` / `4506597b…180e` / `c506732e…d3b2` |
| `D-PEC-99` ruling / exhibit; `D-PEC-98` ruling; `D-PEC-100` ruling | `3e34403a…c989` / `69b646f8…f45e`; `039dc7e2…8361`; `13690e20…729b` |
| DEL-02-03 / DEL-02-08 / DEL-02-09 `ScopeOfWork.md` | `c8bb9f1b…294b` / `2319661b…dd26` / `eab18e17…6f5e` |
| `loops.json` / `loops.schema.json` / `write_status.sh` | `fd342b4f…53d7` / `104ed648…b143` / `0bf835f5…ece3` |
| `software-test-planning` / `software-code-review` / `construct-local-work-graph` / profile / catalog | `8f36adc7…fdcfd` / `ee085d58…8bca` / `fa04e134…a4c9` / `9cc54bfb…c5b3` / `2bfa2c5f…fdb3` |

Attribution: prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN, node X1 of `HELP-HUMAN-PEC-20260925-POST-SCA005`, with two TASK drafters and fresh read-only reviewers as described under Method. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The roles and the `high` reasoning effort are instruction-asserted.
