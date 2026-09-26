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
