# X1A return — D-PEC-106 act: P1 parser fixture suites, with add-on L (WORKING_ITEMS)

Undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node X1 (the act). Returned by WORKING_ITEMS (Type 1) to HELP_HUMAN under brief `briefs/X1A_D106_FIXTURES_ACT.md` (SHA-256 `8cde96bf5779e5339b2c05ac5728d39c5357ebcb5e914300bf0a781b765ab81a`, copied unchanged). The host reports the serving model as Opus 5.5 (`claude-opus-5-5`) for the manager and the verifier; the roles and the `high` effort are instruction-asserted.

## PR

- **PR:** #1008, https://github.com/sgttomas/chirality/pull/1008, `claude/pec-d106-x1-fixtures-act` → `main`. OPEN and **not merged**, as the brief requires.
- **Head at hand-back:** the commit that carries this return's last update and the run-root `SHA256SUMS`. Its SHA is given in the hand-back report, because a file cannot contain the SHA of its own commit.
- **Base:** cut from `origin/main` `c5d852c4a` (contains the ruling, PR #1006). `origin/main` moved to `0adfbc747` (PR #1009, App-only); merged without a rebase as `0040299f6`, with the brief's reruns.
- **CI:** at `04a333f73` every check was pass or skipping (`harness`, `pec`, `PEC workspace tests`, `Harness pre-merge`, `Desktop E2E (source mode)`, the three selectors). Each push re-triggers the checks; read CI on the final head. No "Update the PR base" notice.

## Act report

- **Row 1 preconditions** (all at `c5d852c4a`, 17:36–17:41 UTC): ruling `5161630b…96fe`, proposal `677b59f6…d279` and register row `RULED A / FX-PEC-0 AND THRESHOLDS CONFIRMED / L / M / EFFECTIVE ON MERGE` on fetched `origin/main`; full, non-shallow clone with no partial-clone configuration; Git 2.54.0, Python 3.13.7; prep `SHA256SUMS` 112/112 and run-root bound copies 45/45; `write_status.sh` `0bf835f5…ece3` recomputed; the three `_STATUS.md` at their tabled preimages; dependency rows as tabled (10/10 ACTIVE `PENDING`); `pec_reliance_hold.py --operation dispatch-for-production` ALLOW 41/41 (35 act paths, three `_STATUS.md`, three `MEMORY.md`), with a `date -u` line; `apply_x1p.py --check-only` passed; pins 19/19; the full prep suite `run_x1p_checks.sh` OVERALL PASS on exports; fixture suite 10/10.
- **Add-on L:** the three tabled `write_status.sh` commands, `{D}` = `2026-09-27`, exit 0 ×3; slot rule 3/3; committed as `3f1e1a4d7` **before** the act.
- **A:** `apply_x1p.py` (`452ff66a…2428`) `--check-only` exit 0, then **one real run, exit 0** (`26b27b2b0`, HEAD at run = `3f1e1a4d7`): `CHECK targets 35/35 byte-exact; write set = grant (34 created, 1 modified, 0 removed under projects/pec outside the run root); pinned 12/12 unchanged`. **The grant is consumed.** No rolled-back, refused or repeated run occurred.
- **Fan-in:** `rely-for-production` ALLOW 41/41 before fan-in.

## Written paths and hashes

| Path | Writer | SHA-256 |
|---|---|---|
| `projects/pec/software-workflow.json` (modified from `8ec9ba6d…8a8b`) | `apply_x1p.py` | `d55fff77a1d216a7b1ab78b16e3ff3f2747fb3b542a2b269367ec3afa83e0bbd` |
| `projects/pec/v2/tests/parsers/**` (34 created) | `apply_x1p.py` | each equals its tabled postimage in the proposal's grant (35/35 verified: `X1_FIXTURES_2026-09-27/evidence/row2b_bytes_hygiene.out`) |
| DEL-02-03 `_STATUS.md` | add-on L | `84b238d263c6272f9e4845ad7c2804cf871bd417e40b161026e0fc91bf4c9b5e` |
| DEL-02-08 `_STATUS.md` | add-on L | `bfc995867fa2c87fb7c94acaf95c64fbc42aade174ac77c5c92ace14e3451ff6` |
| DEL-02-09 `_STATUS.md` | add-on L | `50bc10f4135b49e669921ee7d733b5e2bda0c4bcf541c7b2f8fb5ce8f034372a` |
| `projects/pec/execution/_Coordination/X1_FIXTURES_2026-09-27/**` | WORKING_ITEMS | every file hashed in its `SHA256SUMS` |
| `…/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/X1A_D106_FIXTURES_ACT.md` | copy | `8cde96bf5779e5339b2c05ac5728d39c5357ebcb5e914300bf0a781b765ab81a` |
| this return | WORKING_ITEMS | given in the hand-back report |

## Check results

| Row | Result |
|---|---|
| 3 | six registered checks exit 0 (`v2-parsers` with the 10 tests of `TEST_TO_VERIFICATION`, `v2-core-posture`, `v2-api-contract`, `v2-loop-registry`, `v2-store-guard`, `harness-self-check`); posture `core_tree_sha256` unchanged |
| 4 | selection = the same six |
| 5 | bindings `RESULT PASS 442/442`; pins `RESULT PASS 19/19` |
| 6 | strict registers (exit 1, 0 errors, 26 `XRG-013`), harness (0) and receipts (0) identical before and after |
| 7 | exactly the three `_STATUS.md` |
| 8 | containment below |
| 9 | `git diff --check origin/main...HEAD` clean (two earlier failed attempts, caused by trailing whitespace inside captured outputs, are recorded in `VALIDATION.md`) |
| hygiene | 35/35 |
| after merge of `0adfbc747` | act pins, targets and L postimages 53/53; pins 19/19; `run_x1p_checks.sh` OVERALL PASS; suite 10/10; registered checks exit 0; bindings 442/442; row 6 identical after root-path normalization |

Every command, exit code and output: `X1_FIXTURES_2026-09-27/VALIDATION.md` and `evidence/`.

## Verifier verdicts

- `VERIFIER_VERDICT_01.md` (head `f4ab6c307`, `software-code-review` `ee085d58…8bca`): **PASS WITH NOTES**. Three non-blocking evidence-recording findings (row-9 file label; post-commit whitespace normalization of two captures; a composite command label), all repaired or recorded.
- `VERIFIER_VERDICT_02.md` (backcheck, head `04a333f73`): **PASS WITH NOTES**. Final row 7–9 captures then pending (now captured); one inferred HEAD stated as fact (reworded); one observation on a disclosed scratch write. Nothing blocking in either verdict. Verified items include the add-on L postimages, the L-before-act ordering, no parser code and no scanning for retired sections.

## Containment

`git diff --name-status origin/main...HEAD` (`evidence/row8_containment_final.out`): 34 `A` under `projects/pec/v2/tests/parsers/`; `M projects/pec/software-workflow.json`; `M` of the three `_STATUS.md` (DEL-02-03, DEL-02-08, DEL-02-09); the run root `X1_FIXTURES_2026-09-27/**`; the brief copy and this return under `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/`. Nothing else: no `v2/src/**`, `MEMORY.md`, `ScopeOfWork.md`, register, `Dependencies.csv`, `_DEPENDENCIES.md`, `_CONTEXT.md`, `_REFERENCES.md`, decomposition, PRD, `docs/**`, `README.md`, `_DECISIONS/**` or work-graph path.

## Deviations disclosed

- Before `TMPDIR` was exported in one early shell, the manager wrote one scratch file (a filtered copy of the prep `SHA256SUMS`) under `/var/folders`; it was removed at once. No aid ran there and nothing reached the repository.
- Two captured outputs were whitespace-normalized after their first commit so that row 9 is clean; raw bytes are at `2886540c0` and `3f1e1a4d7` (`VALIDATION.md`).

## For HELP_HUMAN to resolve

1. Add the graph and STATUS records, including the lifecycle census after add-on L (three deliverables now `IN_PROGRESS`), to PR #1008; carry the `docs/STATUS.md` change into the work graph and central receipt (`D-PEC-88` item 4).
2. Merge under the standing authorization when required CI passes on the actual head and review has no blocking finding. If `origin/main` moves again, merge without a rebase and rerun the row-1 pin checks, `run_x1p_checks.sh` and the fixture suite.
3. Add-on M at M1: one `## Runs` row in each of the three `MEMORY.md`, after the rows the `D-PEC-98` and `D-PEC-100` add-ons write. None was written here.
4. Carried to the parser packets: FX-PEC-0's run-index declaration presupposition (DEL-02-09 TBD-003, CON-002); golden tests over these fixtures, every other VER, and value representations (DEL-02-03 TBD-007, DEL-02-08 TBD-007); the DEL-02-08/09 contract-wording items. Hosted CI does not run the v2 Python checks (Root/CI, F-5/X-2).

## Limits

No lifecycle change other than add-on L's three `INITIALIZED → IN_PROGRESS`. No dependency `SatisfactionStatus` written. No `CON` resolved. No CHECKING, ISSUED, REVIEW gate, acceptance, readiness, release or reliance claim, and nothing here asks about CHECKING.

*HELP_HUMAN note, added after PR #1008 review 01:* the review-01 repair appended one line to `VALIDATION.md` and regenerated its `SHA256SUMS` entry. Any hashes of those two files given in the hand-back report are superseded: `VALIDATION.md` is now `138fa1f30b6eb4a9f52e1c4ac46a0bef002c53588fb63302f63cf88eed2b1727` and `SHA256SUMS` is now `779a755b361c9a6be02346090f12204e5e4abd2102e18bd6dc3b860ddad191c6`.
