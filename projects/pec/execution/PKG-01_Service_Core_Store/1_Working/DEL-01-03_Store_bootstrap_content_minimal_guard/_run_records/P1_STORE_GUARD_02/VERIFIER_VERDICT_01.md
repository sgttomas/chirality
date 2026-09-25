# VERIFIER VERDICT 01 — P1_STORE_GUARD_02

Saved verbatim by WORKING_ITEMS from the final message of the fresh read-only
TASK verifier (Claude Code Agent tool, `subagent_type: pec-reviewer`,
`model: opus`; host-reported model `claude-opus-5-5`; agent id
`a8e5f6d3e21db42cd`; parent: this WORKING_ITEMS manager). The verifier could
not write files. Candidate: uncommitted working tree against
`6b4a0f59d292ed9f5f0ca222986ca95bc01bb0b6` after AUTHOR cycle 1.

---

VERDICT: FAIL

The code matches R1–R8 and X-1, and every check passes. The verdict is FAIL on one in-grant documentation defect, B-1: the new PATH/Boundary text says multi-line content cannot travel as a path, and a probe shows it can, through a `str` subclass. The code closure for that channel is outside R1's exact rule and should be routed. Updating the document is within the grant.

## Identity and method
- **Role:** TASK (Type 2) verifier, read-only, no delegation. The host reports the model as Opus 5.5 (`claude-opus-5-5`). I cannot confirm the `high` reasoning effort myself.
- **Interpreter:** `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`, Python 3.13.7.
- **Candidate:** the uncommitted working tree against HEAD `6b4a0f59d292ed9f5f0ca222986ca95bc01bb0b6`.
- **Scratch work:** all probes ran on copies under the session scratchpad (`/private/tmp/claude-501/.../scratchpad/`). One posture log went to `/tmp/claude-501/posture.out`, also outside the checkout. `git status --porcelain` is the same before and after my run.

| Source loaded | SHA-256 |
|---|---|
| `.agents/skills/software-code-review/SKILL.md` | `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a` |
| `workflows/software-code-review/WORKFLOW.md` | `9054dfd47318a680e54fe390b00c67e2baf9595156487d4d1897a83458414810` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| D-PEC-87 proposal | `ba3d3e64eab7c0488b7973a10e360479d9f34bb075113f821266aea4a4684569` (matches the required value) |
| D-PEC-87 ruling | `7da38e54508b913efba445e1968d5c86383ea6235719fb1dc908fd91717f66fe` |
| `OBLIGATION_TRIAGE_DEL-01-03.md` | `db335614da29883212ce653cc12b672c68c5d6639200c33280c78c7b466ae6ea` |
| REM-001 / REM-002 / REM-003 `REPORT.md` | `8fcb3ff3…c312` / `b5d6632d…4c60` / `ca1b7b3e…a930` (all match the proposal) |
| `projects/pec/docs/PRD.md` | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| `AUTHOR_RETURN_01.md` / `RUN.md` / `PREIMAGE.md` | `fb5692b8…e0c1` / `27bf6b11…7539` / `46a7eb84…94e8` |

I spot-checked HEAD preimages for the guard, the adapter, `software-workflow.json` and `test_content_minimal_guard.py`; all equal the proposal's preimage values. All seven postimages and the unopened `__init__.py` (`c9d8b3e5…0880`) equal the values in `AUTHOR_RETURN_01.md`.

## Hold preflight (`rely-for-production`)
- Register `f877d931…1cbc`, script `b1712e4b…cd0e`.
- All seven granted paths returned `{"operation": "rely-for-production", "status": "ALLOW"}` with exit 0.

## Containment
- `git diff --name-only` lists exactly the seven granted paths. The only untracked path is the `P1_STORE_GUARD_02/` run root.
- `adapters/storage/__init__.py` is unchanged.
- No new source, test, fixture or config file. No new test ID; `TEST_TO_VERIFICATION` changed only at R7.
- `software-workflow.json` differs by exactly one line, the X-1 append.
- DDL (`_create_schema`), store location, engine and field classes are unchanged. No other code references the renamed message or the moved error classes.
- `MEMORY.md` is not yet touched; the run graph puts it at N6.

## Per-repair table

In the mutation results, "caught" means the named test fails when that change is applied to a scratch copy. "Survives" means all 13 tests still pass.

| Repair | Status | Proving test IDs | Evidence and mutation probes |
|---|---|---|---|
| R1 | Code: DONE, exact. Doc: DEFECT (B-1) | `test_ver_008_policy_is_fixed_finite_and_domain_checked`, `test_ver_008_forged_wrappers_are_revalidated_and_rejected_without_crashing` | `_PATH_FORBIDDEN`, `_MAX_PATH_BYTES` and `_MAX_SEGMENT_BYTES` match the R1 rule byte for byte (`content_minimal_guard.py:13-15`). All listed rejections and admissions are present, plus NUL, a lone surrogate and multibyte segments. Both `SOURCE_CITATION` and `INVALID_VALUE` codes are asserted. The forged multi-line `RepositoryPath` is tested as a field and as `source_path`, with empty readback. Caught: HEAD check restored (4 tests fail), C1 range dropped, U+2028 dropped, U+2029 dropped, TAB dropped, total cap 4097 or 4095, segment cap 256 or 254, `surrogatepass`. Survives: total cap measured in characters (N-5). |
| R2 | DONE | `test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution` | All nine codes are asserted with their locations, plus `<input:1>`, `<input:10>` and `<input:13>`; `rejected` = 13 = distinct failing inputs. Caught: relocation disabled; duplicate count dropped (trips the `RuntimeError`). Survives: `rejected = attempted - accepted`, and removing the `RuntimeError` check (N-3). |
| R3 | DONE | `test_ver_003_port_isolated_and_adapter_has_one_guarded_record_write_surface` | The AST assertions match the spec. Caught: an `UPDATE` in `reopen`, DDL in `delete`, and a second `_insert_guarded` call before the guard. |
| R4 | DONE | VER-004 rejection test, forged-wrapper test, and VER-006 | Making the helper a no-op survives, as expected for an assertion helper. Positive control: after admitting `docs/payload.md`, the helper fails with `'payload' unexpectedly found`. The raw dump is meaningful. |
| R5 | DONE | `test_ver_006_reconciler_presence_and_event_stand_ins_share_the_same_boundary` | One shared corpus, including the multi-line PATH fixture, goes through three shapes; per-fixture `(field_name, code, constraint)` tuples are equal; readback is empty. |
| R6 | DONE | `test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation` | The spec's sequence is present. My probe confirms the doc's loss claim: an admission after `rmtree` returns accepted=1 and is readable on the open handle. After `close()`, both a new instance and a same-instance `reopen()` read `()`. |
| R7 | DONE | `test_ver_009_loaded_suite_has_exact_execution_mapping` | `test_store_lifecycle.py:47` now reads `("VER-003", "VER-007")`. Reverting to `("VER-003",)` survives, as expected for a tag-only repair. |
| R8 | DONE | `test_ver_003…`, `test_ver_002…` | The port defines both errors; the adapter and package objects are the same objects. Engine-neutral: the port has no sqlite import. Caught: removing the `read_all` wrapping. Survives: removing the wrapping in `admit_batch`, `reopen` (either site) or `delete` (N-4; the spec required proof for `read_all` only). |
| X-1 | DONE | selector | BEFORE lacks `v2-store-guard`; AFTER selects it, with reason `v2/src/pec_v2/core/__init__.py`. The posture registration check passes. |

## Checks (run by me; all exit 0)

| Check | Result |
|---|---|
| `v2-store-guard` (verbose storage suite) | Ran 13, OK |
| `v2-core-posture` | `"verdict": "PASS"` |
| `v2-loop-registry` | Ran 12, OK |
| `v2-api-contract` | Ran 6, OK |
| `harness-self-check` (from REPO) | INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124; no finding names a changed path or the run root |
| X-1 selector | exit 0 as above |
| `git diff --check` | exit 0 |
| Run-root trailing whitespace | none |

## PATH row vs PRD §7.1/§7.2
- **What is accurate:**
  - The syntactic bound matches D-PEC-87.
  - The row correctly admits PATH for §7.1 source locators and §7.2 dirty path names (PRD:220, "never content").
  - Placing the "prose-like single line" residual with the caller is right in principle.
- **What is not accurate:**
  - B-1 below: the text overclaims what the bound stops.
  - N-1 below: for §7.2 dirty paths, the named residual owner and the "exists at the cited source SHA" check do not fit.

## Findings

**B-1 — BLOCKING (inside the grant, documentation only).**
- **Where:** `projects/pec/v2/docs/STORE_LIFECYCLE_AND_GUARD.md:138-144`. The PATH row at `:83` has the same problem, and so does the author's claim at `AUTHOR_RETURN_01.md:169` ("It is not a content channel").
- **Claim:** the text says the PATH bound "stops multi-line file bodies, diff hunks, and oversized text from travelling as a path". That is false for a `str` subclass.
- **Cause:** the guard checks the characters of the supplied string, then persists the caller's own object. `_validated_repository_path` (`content_minimal_guard.py:244-248`) returns the caller's object, and `_insert_guarded` (`sqlite_store.py:282-299`) binds it. `sqlite3` calls `__conform__` on a non-exact `str` when binding.
- **Reproduction:** `RepositoryPath(Sneaky("docs/readme.md"))`, where `Sneaky.__conform__` returns `"SECRET FILE BODY\n+diff line two"`. It passes the public constructor with no forged shell. It is admitted (accepted=1), and `read_all()` returns the multi-line text in both `source_path` and the PATH field.
- **Wider reach:** the same channel works through the record ID (`:144`), field names (`:175`), and SHA digests (`:256-259`, including `__format__` in the rendered f-string). It reproduces identically at HEAD, so it is pre-existing. It is the same class of defect as D85 V-F001 ("forged wrappers persisted arbitrary text", REM-002 E18).
- **Remediation, inside the grant:** amend the Boundary section and the PATH row to state this residual: it is guard-wide, pre-existing since D-PEC-85 and not closed by R1. Closing it needs an exact-`str` rule (a `type(x) is str` check, or copying to an exact `str`) applied to every string the guard outputs, which should be routed for an owner ruling. The next author return should correct item 5.

**N-1 — NON-BLOCKING.**
- **Where:** `STORE_LIFECYCLE_AND_GUARD.md:141-143`.
- **Issue:** for §7.2 dirty path names, the observing caller is DEL-06-02 (Git worktree scanner, PKG-06), not "DEL-03-01 or the PKG-02 scanners". Untracked or dirty paths have no source SHA, so the closing check is presence in the observed worktree status.
- **Related coverage gap:** the D-PEC-87 survey covers tracked paths only. An untracked path containing a control character or non-UTF-8 bytes (which Python decodes to a lone surrogate) is rejected as `INVALID_VALUE`; the caller should count it rather than drop it.
- **Note:** the wording copies the proposal verbatim, so it is not blocking. I recommend fixing it in the same doc cycle.

**N-2 — NON-BLOCKING.** `STORE_LIFECYCLE_AND_GUARD.md:62` says commit and rollback happen in "`admit_batch()` only", but `reopen()` commits at `sqlite_store.py:159`.

**N-3 — NOTE.** R2's independent counting and the `RuntimeError` cannot be observed by a test: every input lands in exactly one bucket, so the check can never fire. This is acceptable because the spec's proving test does not require it. Raising it before commit is sound, since the batch rolls back.

**N-4 — NOTE.** Only the R8 wrapping in `read_all` is proven by a test.

**N-5 — NOTE.** No fixture exceeds the 4,096-byte total with multibyte characters, so measuring the total in characters goes undetected.

## Routed residuals (the author's notes)
1. **`close()` not wrapped** (`sqlite_store.py:141-144`): fine under R8's explicit list. `delete()` wraps its own close. A direct `close()` can still raise a raw `sqlite3.Error`. Route as a scope decision.
2. **`str`-subclass bypass:** it is a content channel, not only a normalization bypass (see B-1). The code closure is guard-wide and outside R1's exact rule, so it needs an owner-ruled packet, high priority. Only the documentation part blocks.
3. **Invalid identifiers echoed in returned results:** fine for the store, since failures are returned and never persisted. Route to the consumers (DEL-03-01, DEL-06-02, API): arbitrary caller text in `AdmissionFailure.record_id` or `field_name` must not be logged or persisted.
4. **R6 test does not assert post-delete loss:** fine. The spec's proving test is met, and my probe confirms the doc's loss statement.
5. **Accounting `RuntimeError` raised before commit:** fine and sound. Note that it is a plain `RuntimeError`, not a port error; `StoreDataError` is a subclass of it.
6. **X-1 redundant exact paths:** harmless. Cleaning them up needs its own scope.
