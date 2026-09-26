# G1 return: D-PEC-96 draft, transcribed

- **Executor:** `pec-task` (TASK, `claude-opus-5-5`, high). It was read-only, so HELP_HUMAN transcribed its final report verbatim from the host subagent transcript.
- **Brief:** `../briefs/G1_REGISTRY_SOURCE_PROPOSAL.md`, SHA-256 `084eadd8eeb77a3c2fa31e0c51646e69bbb18c8bd2a30da750c69222c2b0fca1`.
- **SHA-256 of the report text below (UTF-8):** `1ea79afc4015b73affeb81b0cfa63c5e381f6328673558bfcaa8fc5aba6ffcc9`.

## Publication (HELP_HUMAN)

- **The draft** is published unchanged as `_DECISIONS/D-PEC-96_registry_schema_v2_feed_profiles_proposal_2026-09-25.md`, SHA-256 `f486111927dbd0b29ec7ec9ff653e51b5169d02dce53e4ab7357f544c1697d87`. That is the same hash as `D-PEC-96_DRAFT.md` in the preparer's `SHA256SUMS`.
- **The rest of the `g1/` folder** is published unchanged as `../../../PEC_REGISTRY_D96_PREP_2026-09-25/`. Every file listed in its `SHA256SUMS` verifies there, except the draft, which lives at the `_DECISIONS/` path above.
- **One file added at publication:** HELP_HUMAN added `.gitattributes` (`evidence/** -whitespace`) to that folder. It keeps the exact bytes of the unified diffs and check reports past `git diff --check`, as for D-PEC-95. The file is not in `SHA256SUMS`.
- **Basis.** The draft's basis is `abfd0897b`. Since then, `origin/main` has moved to `4d5f7b911` through PRs #925 and #926. Those PRs changed only records, the work graph, STATUS/README and the SCA-006 scope-change files, and touched no `v2/**` path. HELP_HUMAN re-ran `apply_d96.py --check-only` on a `git archive` export of `4d5f7b911`, initialized as a scratch git repository. It exited 0 with 11 `RENDER` lines and `OK option=A files=11 mode=check-only`, so the preimages have not drifted.

## Report (verbatim)

## G1 return: D-PEC-96 draft (registry source packet)

**The draft is ready for the owner to rule on, after the independent review noted under "Unresolved".** Brief hash verified (`084eadd8…fca1`). The basis is `origin/main` `abfd0897b` (fetched first); I re-fetched at the end and `origin/main` was then `3245f9acd` (PR #925). Between the two, only `_REGISTER.md` (still no D-PEC-96 row) and the work graph (G1 now READY) changed. Every product preimage and every other basis hash is unchanged.

**Draft:** `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/g1/D-PEC-96_DRAFT.md`
- SHA-256 `f486111927dbd0b29ec7ec9ff653e51b5169d02dce53e4ab7357f544c1697d87`, 587 lines.
- Status line: `PROPOSAL / AWAITING_RULING`. It follows the D-PEC-95 format.
- Suggested filing name: `D-PEC-96_registry_schema_v2_feed_profiles_proposal_2026-09-25.md`.

### Recommended option A
- **Schema v2** in `loops.schema.json` (full bytes are in the draft). A row now requires `feed_profiles`: a non-empty list of `{profile, version, state, basis}` entries, with no profile repeated in a row.
  - The closed vocabulary is `shared-dev-loop`, `remaining-loop`, `loop-receipts-ledger` and `agentruns-json`, all at version 1.
  - `state` is `live` or `historical`.
  - `basis` must be a repository-relative path.
- **Port:** `RegisteredLoop` gains one required field, `feed_profiles: tuple[FeedProfile, ...]`, plus two core types, `FeedProfile` and `FeedProfileState`. The core stays stdlib-only.
- **Adapter:** accepts only `schema_version` 2. Every failure is reported with its location.
- **Version 1:** version-1 files are rejected at `$.schema_version`, and the one checked-in default is migrated. No dual read, because accepting a version-1 file would need an invented profile, which SOW-077 and REQ-003 forbid. The exact version-1 bytes are kept as a test fixture.
- **Alternatives:** A-R has the same paths but PEC's row declares `remaining-loop`; the other choices are amend and defer.

### PEC-row premise
- **Resolution:** PEC's row should declare `shared-dev-loop` v1 `live` (basis: the D-PEC-94 record) and `loop-receipts-ledger` v1 `historical` (basis: `projects/pec/AGENTS.md`).
- **Why:** Q8 (a) chose `remaining-loop` because "PEC's `LOOP_INIT.md` still selects from `## Remaining`". D-PEC-94 ended that. This is exactly the migration the design note describes: "one owner-gated row change from `remaining-loop` to `shared-dev-loop`, with the ledger declared `historical`".
- **Ruling needed:** SOW-094's Notes and Q8 (a) both require the migration to happen "under its own ruling". The draft therefore asks it as a separate owner question (Q2). No scope change is needed, because no scope statement changes.
- **Consequences, none blocking:**
  - The "declares `remaining-loop` now" sentences in the SOW-094 Notes and the DEL-01-06 description/`_CONTEXT.md` go stale. They pass to node S2 and the next scope change.
  - PEC's 57 `## Remaining` sections are not read under `shared-dev-loop`.
  - SCA-005 R-05 and fixture FX-PEC-0 rest on the old premise. They pass to node X1.
- **Other rows:** there are none. `loops.json` has one row, and P2 rows need their own packets.

### Exact paths and counts (relative to `projects/pec/`)
- **11 product paths:** 10 modified, 1 created, 0 deleted.
  - Modified: `v2/config/loops.json`, `v2/config/loops.schema.json`, `v2/src/pec_v2/core/ports/loop_registry.py`, `v2/src/pec_v2/core/ports/__init__.py`, `v2/src/pec_v2/core/__init__.py`, `v2/src/pec_v2/adapters/config/loop_registry.py`, `v2/tests/config/test_json_loop_registry.py`, `v2/tests/config/test_loop_registry_contract.py`, `v2/tests/config/fixtures/duplicate_loop_id.json`, `v2/tests/config/fixtures/missing_loop_id.json`.
  - Created: `v2/tests/config/fixtures/schema_version_1.json`.
  - Path-list SHA-256 `b5db12e5…c73c`. Preimage and postimage hashes are tabled in the draft.
- **6 must-remain files**, which the act checks are unchanged: `software-workflow.json`, `service_core_posture.json`, `malformed.json`, and three `__init__.py`.
- **Administrative paths:** run root `DEL-01-06/_run_records/D-PEC-96_REGISTRY_V2/**`, and a new `DEL-01-06/MEMORY.md` if the owner says yes to Q5.
- **Bound act script:** `apply_d96.py` (`08c75241…3664`) embeds all postimages and checks every preimage before writing.

### Prototype results
All in scratch; Python 3.13.7.
- **Registered checks (all five exit 0, before and after):**

| Check | Before | After option A |
|---|---|---|
| `v2-loop-registry` | 12 OK | 16 OK |
| `v2-store-guard` | 13 OK | 13 OK |
| `v2-api-contract` | 6 OK | 6 OK |
| `v2-core-posture` | PASS, 0 findings | PASS, 0 findings (core tree hash `88f590c0…` becomes `dd7e1dda…`) |
| `harness-self-check` | output `e5f9ff70…d110` | byte-identical |

- `v2/tests/enforcement`: 28 OK. The receipts validator and the strict register validator both exit 0 with output unchanged.
- `git diff --check` is clean, and the postimages contain no non-ASCII bytes. The affected-check selector picks all five checks.
- **Act script behaviour:**
  - On a fresh export it writes exactly the 11 paths, byte-identical to the hand-applied prototype.
  - A second run exits 1 and writes nothing; so does a run with a drifted must-remain file.
  - `--check-only` leaves the tree unchanged.
  - The A-R variant passes 16/16.
- **Mutation testing:** 13 of 13 mutations caught.
- **`pec_reliance_hold.py`** with `--operation exact-correction-preparation`: ALLOW with exit 0 on all 13 targets.

### Owner questions
1. A, A-R, amend or defer. Recommended: A.
2. PEC's row, as its own ruling: migrated (recommended), as accepted (`remaining-loop`), or other.
3. Confirm the four-profile v1 vocabulary; `feed_profiles` as a list; later vocabulary additions made as packets within schema v2.
4. Version-1 files: rejected (recommended), or a time-bounded dual read.
5. Create DEL-01-06 `MEMORY.md` from the template (recommended), or complete without the row.
6. Model steer.

### Unresolved and carried
- **Review before presenting.** D-PEC-78 §4.3 says the owner accepts exact config, schema and test bytes "only after … tests and REVIEW". HELP_HUMAN should have the draft independently reviewed before presenting it, as was done for D-PEC-95 in PR #921.
- **SOW wording lags.** DEL-01-06's accepted SOW still says "strict version-1" until node S2 rebuilds it. The new tests go beyond the revision-1.4 wording; the packet writes no SOW. Gate 5 HOLD and `INITIALIZED` stand, and there is no lifecycle, PRD or decomposition change and no CHECKING.
- **Vocabulary fixed for the first time.** The accepted records only gave the four profile names as examples ("e.g."); this packet makes them the closed set.
- **"A feed profile" versus a list.** The accepted text says each row declares "a" feed profile; the draft uses a list and discloses this (Q3).
- **Inherited path check is loose.** The existing path rule accepts `./`, `//` and a trailing `/`. The draft discloses this and offers tightening only as an amendment.
- **SCA-006:** confirmed not to bear on the registry. DEL-01-06 is NOT_AFFECTED, and none of its 54 actions touches the registry.
- **Checkout state (external).** During my run another actor moved the checkout: HEAD went `0401c6bc1` → `1f37702e1`, then to branch `claude/pec-sca006-cp1-accept` at `4398370947`. I ran only read-only Git commands and `git fetch`. `git status` is clean.

### Files
- Evidence folder: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/g1/`, with `SHA256SUMS` covering 28 files: the scripts, `evidence/*`, and `postimages/*`.
- Prototype helpers: `/private/tmp/claude-501/g1work.uHT090/`. I deleted the large exports and clones.

## Revision 2 (after PR #928 review 01)

HELP_HUMAN returned the draft to the preparer with the review's findings 1–4, 6, 7 and 8. The preparer's revision-2 report follows.

- **SHA-256 of the report text (UTF-8):** `7365abe12613980386245ff44ad0f8c48fee90083a1057589119e223b9040945`.
- **Publication:** HELP_HUMAN replaced the published proposal with revision 2, SHA-256 `4655e757ae759de28e82f9cdea5cc785bcf4ede856496efcf0e8469488df8da7`. It replaced the preparation folder with the revision-2 `g1/` contents; its `SHA256SUMS` verifies except for the draft, and `.gitattributes` was added again. Revision-1 bytes stay recoverable from this PR's earlier commits (`57db67a0e`).

### Revision-2 report (verbatim)

## G1 revision 2: D-PEC-96 draft revised for all seven review points

The revised draft is ready for review. All seven review points are addressed. Every prototype check passes, 19 of 19 mutations are caught, and nothing was written outside `scratchpad/g1/` or my own temporary directories.

**Basis:** `origin/main` `56a626c3b5515fea790b0d40549e7729669b7dff` (PR #927), re-fetched at the end with no change. It descends from `4d5f7b911` with nothing changed under `projects/pec` since then. No `v2/**` path has changed since `abfd0897b`, and all 10 product preimages and 6 must-remain hashes are identical. The register still has no D-PEC-96 row. SCA-006 checkpoint 1 is now accepted, and DEL-01-06 is still NOT_AFFECTED.

**Checkout:** unchanged and clean. Another actor moved it to branch `claude/pec-d96-registry-proposal`; I switched nothing and ran only read-only Git commands plus `git fetch`.

### New hashes
- **Draft** (overwritten): `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/g1/D-PEC-96_DRAFT.md` — SHA-256 `4655e757ae759de28e82f9cdea5cc785bcf4ede856496efcf0e8469488df8da7` (753 lines, status "PROPOSAL / AWAITING_RULING (revision 2)"). Revision 1 was `f4861119…7d87`.
- **`apply_d96.py`:** `b314213a7b4e615fd97c6c1b7f0fdac170c8c7c493354e2f54c390cc35a36dd4` (revision 1 was `08c75241…3664`).
- **Changed postimages, option A:**
  - `loops.json`: `aad704700748055e8f5cc1ec0c4f3a29c000c775994e1280dcf651952094678e`
  - `loops.schema.json`: `27b8ff110c07bbba67b17ce98955db9e665f67b55cff92cbe3a34011800f04ce`
  - adapter `loop_registry.py`: `4fc4bbf72e2b0cc7507a020fe4cce93c793ab2d5b65f2cc6dbbc2db2c6328ad4`
  - `test_json_loop_registry.py`: `d410afa5a32d4fd11384a4960b1ea28352f3f930f8902488e28b46d392dc3fae`
- **Option A-R:** `loops.json` unchanged from revision 1 (`6e1321e3…7961`); its test file is now `586fcd5e…ee01`.
- **Unchanged from revision 1:** the port file, both `__init__.py` files, the contract test and all three fixtures.
- **Paths and path list:** still 11 product paths (10 modified, 1 created); path-list SHA-256 `b5db12e5…c73c`.
- **Evidence:** `SHA256SUMS` in `g1/` covers 28 files and verifies. The revision-1 evidence was replaced; the diff file is now `evidence/optionA_vs_56a626c3b.diff`.

### What changed, by review point
1. **Remaining sections.**
   - **New profile:** `remaining-items` v1 covers only the `status-remaining` surface. It reads the `## Remaining` sections as records of open scope with their gate markers, never as a selection signal and without the ledger.
   - **Evidence:**
     - PRD v2.3 §7.1 calls remaining items "a per-loop optional field, read only where the loop's feed profile declares it".
     - The add-on keeps the O-B2 bundles the owner selected at checkpoint 1.
     - Splitting every profile into single-surface ones would drift toward O-B1, which was not selected.
   - **PEC's row** declares it `live`, with basis `projects/pec/AGENTS.md`, because the sections are still updated under packets.
   - **Owner choice:** new owner question 3.
2. **Profile coherence.** Each profile now declares the surfaces it covers, and the draft has a surface table.
   - `FEED_PROFILE_SURFACES` in the adapter holds the lists, each schema option's description ends with the same list, and a test ties the two together.
   - The adapter now rejects a row whose profiles overlap on any surface. The failure is located at the later entry's `.profile` and names the surface and the earlier entry. One rule covers live/live overlap, a surface both live and historical, and two historical grammars on one surface.
   - It also rejects a row with no live profile.
   - Validating at load rather than in the parsers is justified from REQ-003: parsers resolving overlaps would each need their own hidden precedence rule.
   - New test sub-cases: ledger live and historical, two live lifecycle readers, Remaining read twice, no live profile.
   - New mutations M14–M19 are all caught.
3. **`agentruns-json` coverage.**
   - Coverage is now JSON run evidence anywhere under the loop's `execution/` tree, including `AgentRuns/` and deliverable `_run_records/`, matching PRD §7.1. The identifier keeps its SCA-005 name.
   - PEC's row declares it `historical`. That covers PEC's one file, `DEL-01-03/_run_records/P1_STORE_GUARD_01/WORK_GRAPH.json`, which fixture FX-PEC-0 includes.
   - Its basis is the D-PEC-94 record, by implication; the draft discloses this. PEC has no `STATUS.json`, so the design note's "13" does not reproduce and its origin is recorded as UNKNOWN.
4. **§B6 quote.** Now quoted in full, including "D-PEC-86 I-7 (PEC's own migration) stays deferred; migration later is one owner-gated row change (Q8)". Owner question 2 now says in one sentence that option A departs from the letter of §B6 and SCA005-CP1-Q8 (a), because D-PEC-94 exercised I-7 after checkpoint 3.
5. **Containment.** The check now allows HELP_HUMAN's records to ride the act PR, or go separately:
   - the D-PEC-96 register row and the ruling and proposal files;
   - the work graph;
   - the undertaking's `AgentRuns` briefs, returns and receipt;
   - `docs/STATUS.md` and `README.md` under D-PEC-88.

   The rollback section notes these records too.
6. **HOLD citation.** Now DEL-01-06 `_REVIEW.md` L45–48 (`570506a6…cdac`), quoted.
7. **Test and schema nits.**
   - Added a non-string `state` case and a `null` `profile` case.
   - New `test_failures_do_not_echo_document_values` covers six fields, and mutation M18 (echoing a value) is caught.
   - Schema `$id` is now `https://chirality.local/pec/v2/config/loops.schema.v2.json`, and a test pins it.

### Updated owner questions
1. A, A-R, amend or defer. Recommended: A.
2. PEC's row, ruled as its own item, with the departure sentence.
   - **Migrated (recommended):** `shared-dev-loop` live, `loop-receipts-ledger` historical, `agentruns-json` historical.
   - **As accepted (A-R):** `remaining-loop` alone.
   - **Other.**
3. PEC's 57 Remaining sections:
   - (a) read through `remaining-items`, `live` (recommended);
   - (b) the same, but `historical`;
   - (c) left unread.
4. Confirm the five-profile v1 vocabulary with its surface lists, `feed_profiles` as a list, the coherence rules (disjoint surfaces, at least one live), and future vocabulary changes as packets within schema v2.
5. Version-1 files: rejected (recommended), or a time-bounded dual read.
6. DEL-01-06 `MEMORY.md`: create it (recommended), or complete without the row.
7. Model steer.

### Prototype results (on `56a626c3b`)
- **Registered checks:** all five exit 0 before and after.

  | Check | Before | After option A |
  |---|---|---|
  | `v2-loop-registry` | 12 OK | 17 OK |
  | `v2-store-guard` | 13 OK | 13 OK |
  | `v2-api-contract` | 6 OK | 6 OK |
  | `v2-core-posture` | PASS, 0 findings | PASS, 0 findings; core tree `88f590c0…` → `dd7e1dda…`, unchanged from revision 1 |
  | `harness-self-check` | stdout `e5f9ff70…d110` | byte-identical |

- **Other checks:**
  - enforcement tests 28 OK;
  - receipts validator and strict register validator exit 0, output unchanged;
  - `git diff --check` clean;
  - 0 non-ASCII bytes;
  - the check selector picks all five checks.
- **Act script:**
  - `--check-only` exits 0 and leaves the tree unchanged.
  - Option A exits 0, writes exactly the 11 paths, and matches the prototype byte for byte.
  - A second run exits 1 and writes nothing; so does a run against a drifted must-remain file.
  - A-R exits 0, and its registry suite runs 17 OK.
- **Mutations:** 19 of 19 caught; `RESULT PASS`.
- **Reliance-hold preflight:** `exact-correction-preparation` returned ALLOW on all 13 targets. The register (`f877d931…`) and the script (`b1712e4b…`) are unchanged.

### Still open
- **D-PEC-78 §4.3 order.** Revision 2 changes bytes, so the reviewer should follow up on the new bytes before the ruling.
- **New profile.** `remaining-items` is not among the SCA-005 example profiles; the owner confirms it in question 4.
- **Basis by implication.** The `agentruns-json` basis for PEC is implied by the D-PEC-94 record rather than stated in it (question 2 lets the owner name another).
- **Carried from revision 1:**
  - the path-normalization residual, offered as an amendment only;
  - the lagging DEL-01-06 SOW text, which node S2 rebuilds;
  - the stale "declares `remaining-loop` now" decomposition sentences;
  - FX-PEC-0 and R-05, which pass to node X1.

### Files
- My helpers are in `/private/tmp/claude-501/g1work.uHT090/` (revision-2 files in its `r2/` folder). Large exports and clones were deleted.

## Revision 3 (after PR #928 review 02)

HELP_HUMAN returned revision 2 to the preparer with review 02's blocking finding B1 (the A-R mutation crash) and its non-blocking findings 1, 3 and 5. The preparer's revision-3 report follows.

- **SHA-256 of the report text (UTF-8):** `700f22e03ed4d2edf6f098f1228b3b6bac856da52fe9ab74ab7561c2b0f80faf`.
- **Publication:** HELP_HUMAN replaced the published proposal with revision 3, SHA-256 `2f7d987540131ae2d31b0d64d9eff1de7b5b368da02dfed7b8feec88e2f4afc4`, and replaced the preparation folder with the revision-3 `g1/` contents. Its `SHA256SUMS` verifies except for the draft, and `.gitattributes` was added again. `apply_d96.py` and every postimage are unchanged from revision 2. Revision-2 bytes stay recoverable at `d38f1744b`.

### Revision-3 report (verbatim)

## G1 revision 3: D-PEC-96 draft, blocking finding fixed

The blocking finding is fixed: the mutation runner now catches all 19 mutations under both option A and option A-R, with `RESULT PASS` each. I also addressed the three non-blocking points. The product bytes and `apply_d96.py` are unchanged from revision 2; only the mutation runner, the evidence and the draft text changed.

**Basis:** `origin/main` `7f33b4dd51f93553f17607167077c28ddd773ff6` (PR #930), fetched at the start and again at the end with no change.
- It is newer than the `56a626c3b` you named. Since then it changed one PEC file, adding `execution/_Coordination/NOTICE_2026-09-26_WORKFLOW_WAVE2A_EXECUTION.md`. That Root tranche also retired `workflows/software-bounded-implementation`, which the draft had cited, so the draft now cites `construct-local-work-graph` instead (details below).
- No `v2/**` path has changed. All 10 product preimages and the 6 files the act must leave unchanged were re-verified. The register still has no D-PEC-96 row.
- The checkout is clean and I switched no branch; it is on `claude/pec-d96-registry-proposal`, where another actor left it.

### Hashes
- **Draft:** `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/g1/D-PEC-96_DRAFT.md`, SHA-256 `2f7d987540131ae2d31b0d64d9eff1de7b5b368da02dfed7b8feec88e2f4afc4` (768 lines, status "revision 3").
- **`apply_d96.py`:** `b314213a7b4e615fd97c6c1b7f0fdac170c8c7c493354e2f54c390cc35a36dd4`, unchanged from revision 2.
- **`mutate_d96.py`:** `8d3d2fb3cc555dfec64bbd40feec0783ce791d40b4077921d487b3b08e2efe45`.
- **Postimages:** all 11 unchanged from revision 2 (`loops.json` A `aad70470…678e`; A-R `6e1321e3…7961`).
- **Evidence:** `SHA256SUMS` in `g1/` covers 30 files and verifies. The diff file is now `evidence/optionA_vs_7f33b4dd5.diff`.

### Mutation results
| Run | Result |
|---|---|
| Option A, `mutate_d96.py <pec> --pec-row migrated` | baseline OK; M1–M19 all CAUGHT; `RESULT PASS` |
| Option A-R, `mutate_d96.py <pec> --pec-row remaining` | baseline OK; M1–M19 all CAUGHT; `RESULT PASS` |
| Revision-2 runner on an A-R tree | exit 1 with `IndexError: pop index out of range` at M19, no `RESULT` line — the finding, reproduced |

Evidence files: `evidence/mutate_optionA.out`, `evidence/mutate_optionAR.out`, `evidence/mutate_optionAR_revision2_runner.out`.

### What changed
- **Blocking finding: `mutate_d96.py` is now option-aware** (`--pec-row migrated|remaining`, default `migrated`).
  - M1–M10 and M12–M18 are the same for both options.
  - M11 and M19 each have an A and an A-R variant, both acting on the checked-in default:
    - M11 swaps only the profile identifier and keeps basis and state. Under A this is `remaining-loop`; under A-R it is `shared-dev-loop`. Under A-R, M11 is therefore no longer caught only because the basis differs.
    - M19 under A drops `remaining-items`. Under A-R it makes the only profile historical, so the no-live-profile rule fails.
  - A mutation that cannot apply is now reported `NOT_APPLIED` and fails the run, instead of crashing it.
  - The verification table states the expectation per option: M1–M19 each CAUGHT, none `NOT_APPLIED`, `RESULT PASS`.
- **Rollback.** The owner's ruling record and every register row are never reverted. Under the register header's convention, a ruled row is not reopened or annotated. A rollback is therefore recorded as its own new register row and record, citing D-PEC-96 and the revert PR. HELP_HUMAN's other records that rode the act PR stay as history; a revert may only add to them.
- **Question 2.** It now says A-R as offered leaves PEC's one `WORK_GRAPH.json` unread (`DEL-01-03/_run_records/P1_STORE_GUARD_01/`, part of FX-PEC-0). It also says "Other" can pair `remaining-loop` v1 live with `agentruns-json` v1 historical, which is valid under the surface rules.
- **Numbering.** A new revision-3 table was added. The revision-2 table is kept as history, now numbered by review 01's findings: 1–4 and 6–8.
- **Basis-driven change.** The administrative grant used to cite the retired `workflows/software-bounded-implementation`. It now says an optional script-running TASK is commissioned as an implementation node under `construct-local-work-graph` (`3e197c9d…9dc3`). The notice (`d194b1b5…4383`) and that workflow were added to the basis table.

### Owner questions
These are unchanged from revision 2, apart from the question-2 additions above:
1. A, A-R, amend or defer. Recommended: A.
2. PEC's row as its own ruling. Recommended: migrated.
3. The Remaining sections. Recommended: (a) `remaining-items`, live.
4. Confirm the five-profile vocabulary, the surfaces and the coherence rules.
5. Version-1 files. Recommended: rejected.
6. DEL-01-06 `MEMORY.md`. Recommended: create it.
7. Model steer.

### Prototype results (on `7f33b4dd5`)
- **Registered checks:** all five exit 0 before and after.

  | Check | Before | After (option A) |
  |---|---|---|
  | `v2-loop-registry` | 12 OK | 17 OK |
  | `v2-store-guard` | 13 OK | 13 OK |
  | `v2-api-contract` | 6 OK | 6 OK |
  | `v2-core-posture` | PASS, 0 findings | PASS, 0 findings; core tree `88f590c0…` → `dd7e1dda…` |
  | `harness-self-check` | stdout `e5f9ff70…d110` | byte-identical |

- **Other checks:**
  - enforcement tests: 28 OK;
  - receipts validator: exit 0, output unchanged;
  - strict register validator: exit 0, output byte-identical;
  - `git diff --check`: clean.
- **Act script:**
  - `--check-only` exits 0 and leaves the tree unchanged.
  - Option A exits 0 and writes exactly the 11 paths.
  - A second run exits 1 and writes nothing; so does a run against a drifted must-remain file.
  - Option A-R exits 0, and its registry suite runs 17 OK.
- **Reliance-hold preflight:** `exact-correction-preparation` returned ALLOW with exit 0 on all 13 targets.

### Unresolved
- **Re-review.** Revision 3 changes only the runner, the evidence and the text. A reviewer follow-up on the mutation runner and the per-option expectation completes the D-PEC-78 §4.3 order.
- **Carried from revision 2:**
  - The `agentruns-json` basis for PEC is by implication from D-PEC-94.
  - `remaining-items` is not among the SCA-005 example profiles.
  - The path-normalization residual (amendment only).
  - The DEL-01-06 SOW lag, for S2.
  - The stale "declares `remaining-loop` now" sentences.
  - FX-PEC-0 and R-05, carried to X1.

### Files
- My helpers are in `/private/tmp/claude-501/g1work.uHT090/` (`r3/` for this revision). The large exports and clones are deleted.

## Revision 4 (by owner direction, 2026-09-26)

HELP_HUMAN relayed the owner's direction ("revision 4: drop remaining-items and remaining-loop"; recorded in `_DECISIONS/D-PEC-96_AMEND_DIRECTION_2026-09-26.md`). The preparer's revision-4 report follows.

- **SHA-256 of the report text (UTF-8):** `c3e729d08ff6930890a2a893f09fbf9d463e7a363e72cd387f0b1309925d9252`.
- **Publication.** HELP_HUMAN replaced the published proposal with revision 4, SHA-256 `4506597b1bfd6cafd8fc561c688bcb9e803d9c2b04c3abdec9dc05edf155180e`, and replaced the preparation folder with the revision-4 `g1/` contents. `SHA256SUMS` verifies, apart from the draft, and `.gitattributes` was added again. Revision-3 bytes stay recoverable at `6721457be`.

### Revision-4 report (verbatim)

## G1 revision 4: D-PEC-96 draft with `remaining-items` and `remaining-loop` removed

Revision 4 is written and every check passes. It carries out the owner's direction: "revision 4: drop remaining-items and remaining-loop". All five registered checks, enforcement, the act-script runs and the reliance-hold preflight pass. The registry suite runs 19 tests, and the mutation run catches 19 of 19 with `RESULT PASS`.

**Basis.** `origin/main` is at `8f9bd314c5f2499e6faf5bf4bdce917927e8185e`, the same at the start and the end of the work.
- Nothing under `projects/pec/v2/**`, and nothing in `projects/pec/software-workflow.json`, has changed since `7f33b4dd5`, or since `abfd0897b`. All 10 product preimages and all 6 files the act must leave unchanged were re-verified at `8f9bd314c`.
- Other PEC changes since revision 3:
  - HELP_HUMAN's records: the filed revision-3 proposal, the prep folder, the register row and the graph;
  - seven Root notices dated 2026-09-26;
  - SCA-006 checkpoint 2, accepted ("SCA-006 CP2: accept; Q1 a; Q2 a").

  None of them touches the registry.
- The checkout is clean. I switched no branch; another actor has since moved it to `claude/pec-owner-directions-20260926`.

### New hashes
- **Draft:** `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/g1/D-PEC-96_DRAFT.md`, SHA-256 `4506597b1bfd6cafd8fc561c688bcb9e803d9c2b04c3abdec9dc05edf155180e`, 729 lines, status "revision 4".
- **`apply_d96.py`:** `80725b4ff0180e858e6a0ecf0cf50fc8bcf19d861fcf53278f115567e6d6bbf3`
- **`mutate_d96.py`:** `57c2f03107aec5056f03847c43b9443a6986fbfd522017971c3cab72c3c826f0`
- **Changed postimages:**
  - `v2/config/loops.json`: `fd342b4f29edf3bece24a8d785b4a03d1a60158e62227753e4e1fa03529f53d7`
  - `v2/config/loops.schema.json`: `104ed64820b7a1fa6f24249cb6817653b8a624f43c52ea181ae4fd5d510cb143`
  - adapter `loop_registry.py`: `620a173d19d881ef396ebb339e4097f5ee4e3a0b6ada231718ca700926832f07`
  - `test_json_loop_registry.py`: `8b45495fdc78eb77c12a4ebefdb064d34d40d5602fde573be4b4e817ddbe0c9b`
- **Unchanged since revision 2:** the port file, both `__init__.py` files, the contract test and the three fixtures.
- **Grant:** still 11 paths (10 modified, 1 created); path-list hash `b5db12e5…c73c`.
- **Evidence:** `SHA256SUMS` in `g1/` covers 24 files and verifies. The diff is now `evidence/optionA_vs_8f9bd314c.diff`. The A-R postimages and outputs are removed.

### Changes by item
1. **Vocabulary.**
   - The closed vocabulary is now `shared-dev-loop`, `loop-receipts-ledger` and `agentruns-json`, each at version 1. The schema options, `FEED_PROFILE_VERSIONS`, `FEED_PROFILE_SURFACES`, the surface table and the tests were all updated to match.
   - `status-remaining` was declared only by the two dropped profiles, so it is removed from the surface set. No other surface lost its only profile.
   - `grep -ri remaining` over the applied `v2/` tree finds nothing.
   - **Coherence rules are kept.** The three shipped profiles are pairwise disjoint, so the overlap rule has no shipped case to fire on today; it now guards later vocabulary changes. Two tests keep it honest:
     - `test_shipped_vocabulary_surfaces_are_pairwise_disjoint` pins the disjointness.
     - `test_overlapping_profiles_are_rejected_with_location` adds two probe profiles through `mock.patch.dict`, without touching the shipped files. It exercises three real overlaps: live and historical on one surface, two live readers, and two historical grammars. It also checks a disjoint control row and that the probes are removed afterwards.
   - The at-least-one-live rule keeps its real test case.
2. **PEC's row.** `shared-dev-loop` v1 live (basis: the D-PEC-94 record); `loop-receipts-ledger` v1 historical (basis: `projects/pec/AGENTS.md`); `agentruns-json` v1 historical (basis: the D-PEC-94 record, by implication).
3. **Options.**
   - A-R is gone: its postimage overrides, its mutation variants and the `--pec-row` path of both scripts. `apply_d96.py --pec-row …` now exits 2.
   - The runner stays fail-closed. A probe run with M1's anchor made invalid gives `NOT_APPLIED`, `TOTAL 18/19`, `RESULT FAIL` and exit 1; it is in the evidence.
   - Three replacement mutations: M11 is now "default declares the ledger live", M16 is now "`shared-dev-loop` also claims the receipt ledger", and M19 is now "default drops `agentruns-json`". The runner prints `TOTAL 19/19 CAUGHT`.
4. **Owner questions.** The Remaining question is recorded as settled, under its own heading, "Settled by the owner's direction": not read, and no profile. The owner's words are quoted verbatim.
5. **Text.**
   - A revision-4 table quotes both of the owner's statements verbatim. It is labelled evidence of the direction, not the ruling.
   - The stale "declares `remaining-loop` now" sentences in the SOW-094 Notes and the DEL-01-06 description and `_CONTEXT.md` are carried to S2, as before.
   - The `projects/pec/AGENTS.md` Remaining sentences are corrected separately, in the SCA-006 checkpoint-3 instruction tranche, as you relayed the owner's direction. At `8f9bd314c`, the accepted checkpoint-2 `AGENTS.candidate.md` still carries that paragraph.
   - The FX-PEC-0 fixture is redefined without the Remaining sections, and that is carried to X1.
6. **Preimages** re-verified at `8f9bd314c`, as above.

### Test and mutation counts
- `v2-loop-registry`: Ran 19, OK (12 before). The invalid-profile test has 21 located sub-cases, the overlap test 3 cases plus a control, and the no-echo test 6 fields.
- Mutations: 19 of 19 caught; `RESULT PASS`.

### Updated owner questions
1. A, amend or defer. Recommended: A.
2. PEC's row, as its own ruling. It keeps the sentence stating the departure from the letter of the CP2-accepted §B6 and from SCA005-CP1-Q8 (a), and why: D-PEC-94 exercised I-7 after checkpoint 3.
   - It says plainly that the owner's revision-4 direction leaves only the migrated row expressible, but is not itself the ruling.
   - Choices: migrated (recommended), or other states and bases within the three profiles.
3. Confirm the three-profile vocabulary, the surface lists, the list-shaped `feed_profiles`, and the coherence rules, kept as a guard.
4. Version-1 files: rejected (recommended), or a time-bounded dual read.
5. DEL-01-06 `MEMORY.md`: create it (recommended), or complete without the row.
6. Model steer.

### Prototype results (on `8f9bd314c`)
- **Registered checks:** all five exit 0 before and after the act.

| Check | Before | After |
|---|---|---|
| `v2-loop-registry` | 12 OK | 19 OK |
| `v2-store-guard` | 13 OK | 13 OK |
| `v2-api-contract` | 6 OK | 6 OK |
| `v2-core-posture` | PASS, 0 findings | PASS, 0 findings |
| `harness-self-check` | stdout `e5f9ff70…d110` | byte-identical |

  The core tree hash moves from `88f590c0…` to `dd7e1dda…`.
- **Enforcement:** 28 OK. The receipts and strict register validators exit 0 with unchanged output. `git diff --check` is clean, and there are 0 non-ASCII bytes. The check selector still picks all five checks.
- **Act script:**
  - `--check-only`: exit 0, tree unchanged.
  - The act: exit 0, exactly 11 paths written, byte-identical to the prototype.
  - A second run: exit 1, nothing written.
  - A run with a drifted file that must stay unchanged: exit 1, nothing written.
  - `--pec-row`: exit 2.
- **Reliance-hold:** `exact-correction-preparation` returns ALLOW with exit 0 on all 13 targets.

### Unresolved
- **Review of the new bytes.** Revision 4 changes the schema, the default instance, the adapter, the tests and the runner. Under D-PEC-78 §4.3, a reviewer should look at these bytes before the ruling.
- **Where the owner direction lives.** The owner's 2026-09-26 words reached me only through your relay. Their repository record is yours to file.
- **Filed copy is stale.** The proposal filed on `origin/main` is revision 3 (`2f7d9875…afc4`). The prep folder `_Coordination/PEC_REGISTRY_D96_PREP_2026-09-25/` also holds the revision-3 scripts. Both need replacing when revision 4 is published.
- **Carried forward:**
  - The `agentruns-json` basis rests on implication from D-PEC-94.
  - The path-normalization residual (amendment only).
  - The DEL-01-06 Scope of Work lag, for S2.
  - The `SOFTWARE_DECOMP.md` §9 vocabulary term still lists `remaining-loop` as an example.
  - FX-PEC-0 and R-05, for X1.

### Files
- Helpers are in `/private/tmp/claude-501/g1work.uHT090/r4/`. The large exports and clones are deleted.
