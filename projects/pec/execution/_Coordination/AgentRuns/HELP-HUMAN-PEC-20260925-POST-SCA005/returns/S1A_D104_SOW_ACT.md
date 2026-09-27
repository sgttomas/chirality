# Return — S1A: D-PEC-104 act (S1 Scope of Work currency, twelve exact replacements)

WORKING_ITEMS (Type 1) under HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`,
work-graph node S1 (the act). Brief `S1A.md` `b60d21db…296a`, copied unchanged to
`AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S1A_D104_SOW_ACT.md`. Model:
`claude-opus-5-5` (host-reported), high effort per the owner's "defaults"
(instruction-asserted). Act date 2026-09-27.

## PR and head

- **PR:** https://github.com/sgttomas/chirality/pull/1010 (against `main`; not merged by
  the manager).
- **Head at this return's writing:** `1f0a8fefc` (records). This return's own commit
  follows it and is the only addition; the final head SHA is given in the hand-back.
- **Base:** `origin/main` `0adfbc747` (merged without a rebase at `8e09da59f`); the act
  branch was cut from `16010b4ca`.

## Act report

1. **Preconditions (all met).** Fetched `origin/main` `16010b4ca` carries the ruling
   (`bb88deb5…1bd`) and the register row `D-PEC-104` `RULED A / PART B, SCOPE AND Q4
   CONFIRMED / M / EFFECTIVE ON MERGE`; the proposal hashes `35301840…5f51`; the prep
   `SHA256SUMS` checks 158/158; since `b0a9a52b6` no S1 target or pin changed (the S1
   prep folder, the ruling and Piping only). Reliance preflight `dispatch-for-production`
   ALLOW ×12 at 17:18:24Z. `apply_s1p.py --check-only` exit 0 with all 12 preimages and
   35 pins as tabled.
2. **Run root** `projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27/`: 46
   files copied from the prep folder, 46/46 OK. **Write-set decision:** the script
   excludes its own directory from its inventory and accepts only a
   `SOW_CURRENCY_S1_*` run root, so the run-root copy was run and its output written
   beside it in the run root (`MANIFEST.md`).
3. **A.** `apply_s1p.py` ran once at 17:19:45Z from the repository root: exit 0,
   `CHECK targets 12/12 byte-exact; write set = grant (0 created, 12 modified, 0 removed
   under projects/pec outside the run root); pinned 35/35 unchanged`. Reliance preflight
   `rely-for-production` ALLOW ×12 at 17:19:59Z, inside the act commit `1e33df616`;
   again at 18:01:23Z before the verdict's fan-in.
4. **Verify.** The proposal's finite-verification table, all rows as required
   (`VALIDATION.md`). Rerun method OVERALL PASS at `16010b4ca` and `0adfbc747`;
   negative controls 9/9 caught.
5. **Verifier.** One fresh read-only `pec-reviewer` (opus), foreground:
   `VERIFIER_VERDICT_01.md` PASS WITH NOTES.
6. **Base moved.** `origin/main` moved to `0adfbc747` (PR #1006: the `D-PEC-105` and
   `D-PEC-106` rulings and records; PR #1009: App). Merged without a rebase; no pinned
   file or quoted locus changed; `--check-only` (main export), quotes, state claims,
   qualified IDs, pins and baselines rechecked, all passing.
7. **Add-on M** not written (node M1). No `MEMORY.md` created.

## Written paths (SHA-256)

Contracts (under `projects/pec/execution/`), each the tabled postimage:

| Deliverable | Path | SHA-256 |
|---|---|---|
| DEL-01-03 | `PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/ScopeOfWork.md` | `65c7f4086f8a053c41219c4966dd062a3821d43927c24fffe29f4e9046d2a367` |
| DEL-01-04 | `PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/ScopeOfWork.md` | `16ac1cd956c90f0e757c9ce54c4e6645eea50e6d46d69b26f8052ad0484cca41` |
| DEL-01-05 | `PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/ScopeOfWork.md` | `347f73c7969cc777027110f101faec6ad40c728e17e095aa2270f268498798bb` |
| DEL-02-01 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/ScopeOfWork.md` | `82caf28a3757089ec07cd9a21ef70f97840fda7b92f1017236ce5062fdf55872` |
| DEL-02-02 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/ScopeOfWork.md` | `84e55e58e6632845f7462970180c052ebec5fc677072a4bd883f871a002ffa86` |
| DEL-03-01 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/ScopeOfWork.md` | `5b71d3583b2e661564acf889c0a0d6fef93ce24302f29845c3cda0a367ae8276` |
| DEL-03-02 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/ScopeOfWork.md` | `d823d55d9e714ac3142c02ee5d599d7167e0836c89c1abee7c513b072073a3d0` |
| DEL-03-03 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/ScopeOfWork.md` | `c2b88cb65c71bf017fc42c85e164470f0ea86696bd100ed0157d4c2a53f79526` |
| DEL-03-06 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/ScopeOfWork.md` | `f9c3a057717292e7ccd6def6e0496f69ad6c5100457b15cd17b37477adff8bd4` |
| DEL-04-05 | `PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/ScopeOfWork.md` | `9c2ede6ceff643b09a380fcbecb649c953783ed25ca044f35bc6376fd49309db` |
| DEL-10-02 | `PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/ScopeOfWork.md` | `f5590cf55b19f3170cb04e65340e076e672d5d54d8f1e98385372d1dd8f3436e` |
| DEL-10-10 | `PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md` | `813839a080d7e245a0174959bc4f67be265cfabfd5b2177f83cb6fdc934737c8` |

Records (under `projects/pec/execution/_Coordination/`):

| Path | SHA-256 |
|---|---|
| `SOW_CURRENCY_S1_2026-09-27/MANIFEST.md` | `3d88ed9d4d5db71198c73eee1f045fda8ed0800803f60c2fba1164fe1706b7c3` |
| `SOW_CURRENCY_S1_2026-09-27/VALIDATION.md` | `73b32e8c41b4fc6fd8e47bab5e42b0cb3c465e7f7065df49837a1ee2d624537a` (after the PR #1010 review-01 repair; originally `b9756dcc…a4e3`) |
| `SOW_CURRENCY_S1_2026-09-27/HANDOFF_STATE.md` | `53c640c60c6df739b24388b9cdf975cdd8f78c5904c575f79080aa195544516f` |
| `SOW_CURRENCY_S1_2026-09-27/VERIFIER_VERDICT_01.md` | `5dab70b3c7b1725127777b14dd7f37b320e3208ff91b47ce3f039ba1e6361c5f` |
| `SOW_CURRENCY_S1_2026-09-27/SHA256SUMS` (334 entries: every run-root file except itself) | `6dde9d7824133f77c179eda50b431d5c24a86839f840b2596d21b0cc45eb4db7` (after the PR #1010 review-01 repair; originally `7f3efc6c…cbae`) |
| `SOW_CURRENCY_S1_2026-09-27/apply_s1p.py` (bound copy) | `26b677a70d5d51041f0d49dd34e9a09685120f136071e906d7ff702719f1625f` |
| `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S1A_D104_SOW_ACT.md` | `b60d21dba14d0a6805b74a611eab057d6318f952e31f8c934247b237d590296a` |
| `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/S1A_D104_SOW_ACT.md` (this file) | given in the hand-back |

The run root holds 335 files: the 334 listed in its `SHA256SUMS` and `SHA256SUMS` itself.

## Check results

| Check | Result |
|---|---|
| Validator | `PASS format=SOW_V1` ×12 |
| Checklists | exit 0; reruns byte-identical; equal to the prepared hashes ×12 |
| Boundary owners | exit 0 ×12; no `UNRESOLVED_OWNER`/`UNDEFINED_CLAIM`; `NOT_CHECKABLE` exactly the proposal's QA 21 rows; JSON identical to prepared |
| Quotes / state claims / qualified IDs | 884/884 / 905/905 / 44/44 |
| S4 overlay | no-op (DEL-04-01 and DEL-04-03 hold the S4 postimages) |
| Dependency-quote currency | 127/127 before and after, identical |
| `_STATUS.md` / `_REVIEW.md` / `Review_Findings.csv` / `MEMORY.md` | no change |
| Strict registers | exit 1, 0 errors, 26 `XRG-013` (D-GOV-48 deferred), identical before and after |
| Harness self-check / loop receipts ("closure" read as these and the strict identity) | exit 0, identical before and after |
| Pins / postimages | 35/35 / 12/12; second run refuses ×12 |
| DEL-01-03 / DEL-01-05 REQ, AC, VER | 29/29 and 32/32 definition lines byte-identical |
| DEL-03-06 | hunks only at L220, L222–225, L229, L476 |
| Rerun method | `run_s1p_checks.sh` OVERALL PASS at `16010b4ca` and `0adfbc747` (summaries identical apart from the basis line) |
| Negative controls | 9/9 caught |
| Post-merge (`0adfbc747`) | `--check-only` passes on a main export and refuses on HEAD by design; quotes, state claims, qualified IDs, pins, baselines all as above |
| `git diff --check origin/main...HEAD` | clean |
| CI | reported in the hand-back for the final head |

## Verifier verdicts

- `VERIFIER_VERDICT_01.md` (agent `ad6128330fe02ce7a`, candidate `1cc8ce997`): **PASS WITH
  NOTES**, 0 BLOCKING, 0 NON-BLOCKING, 9 NOTEs. Item by item PASS: basis; byte identity;
  `MODE=VERIFY` subset (checks.md 1, 3, 4, 8, 9, 13, 16, 18–21, QA 21 hand resolution);
  semantics, including the Part B landings byte-exact with gates binding, DEL-03-06
  correction-only, DEL-01-03 and DEL-01-05 REQ/AC/VER byte-identical, DEL-04-05's
  statements verbatim in the landed S4 text; containment and lifecycle. Dispositions:
  N1, N2, N3, N4, N7, N8, N9 recorded (bound bytes or no action; later currency items in
  `HANDOFF_STATE.md`); N5 recorded (the check shell exported the variable; the recorded
  line shows only the command); N6 acted on (containment rechecked after the merge and
  at the records commit).

## Containment

At the records commit `1f0a8fefc` against merge base `0adfbc747`:
`git diff --name-status origin/main...HEAD` lists 12 `M` contracts, the run-root files
(`A`) and the brief copy (`A`), and nothing else; this return adds one `A` under
`AgentRuns/…/returns/`. No `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`,
`MEMORY.md`, register, `Dependencies.csv`, `_DEPENDENCIES.md`, `_CONTEXT.md`,
`_REFERENCES.md`, decomposition, `v2/**`, PRD, `_DomainEngines/**`, `docs/**`,
`README.md`, `_DECISIONS/**` or work-graph path. `git diff --check` clean.

Footprint: scratch under the session scratchpad (`s1a/`, `s1a_hold.zsh`); nothing in
`/tmp` or `/var/folders`. One slip, disclosed in `MANIFEST.md`: a drift check at 18:01:41Z
created a Git-ignored `__pycache__` in the run root (never committed), which the first
`SHA256SUMS` listed; removed and `SHA256SUMS` regenerated in `1f0a8fefc`.

## For the caller to resolve

1. Add the work-graph and `docs/STATUS.md` records (with the `D-PEC-88` trace) to PR
   #1010, run the independent PR review on the actual head, and merge on green CI.
2. Add-on M at closeout (node M1): eleven `MEMORY.md` created and one section appended to
   DEL-01-03's, as the proposal tables; the preimages still hold at `8e09da59f`.
3. Later currency items and disclosed consequences, none acted on
   (`HANDOFF_STATE.md`): the "(provisional `D-PEC-104`)" wording in eleven AX entries
   (N1); DEL-04-05 AX-012's process text (N2); QA 21 owner binding in DEL-02-01 and
   DEL-02-02 REQ-005 (N3); the rest of DEL-03-06 and its two sibling quotations now
   non-verbatim; DEL-03-04's stale quotation of DEL-03-01 `CON-005`; DEL-02-07 and
   DEL-10-13 `CON-003` premises; the DEL-10-02 `C-08` / `_DEPENDENCIES.md` wording; the
   open `CON`/`TBD` items the contracts carry.
4. REVIEW: the new bytes carry no REVIEW acceptance; the earlier DEL-03-01 and DEL-01-05
   acceptances stay as history (ruling question 4). Any REVIEW act is separate.

No CHECKING, ISSUED, REVIEW gate, acceptance, readiness, release or reliance claim is
made, and nothing here asks the owner about CHECKING. No ruling is recorded.
