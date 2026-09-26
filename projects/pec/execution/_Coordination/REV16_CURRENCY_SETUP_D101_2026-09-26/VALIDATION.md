# PROJECT_SETUP — D-PEC-101 revision-1.6 currency and setup (K1, K4 with add-on C, add-on V): Validation

All commands ran from the repository root (worktree `pec-d101-act`, branch `claude/pec-d101-act`)
with `PYTHONDONTWRITEBYTECODE=1`, CPython 3.13.7, local date 2026-09-26 (America/Denver, MDT), unless
a line says otherwise. `checks/COMMANDS.txt` lists every command with its exit code; each output
is the file named in the tables below. Helper scripts written for this run: `check_hashes.py`
(byte identity and aggregates against the proposal's tables), `check_k4_extras.py`,
`containment.py`, `run_holds.sh`.

## Preconditions

| Check | Result | Output |
|---|---|---|
| Fetched `origin/main` contains the ruling `D-PEC-101_RULING_2026-09-26.md` (`baa4fc09…ba28`) and register row `D-PEC-101 … RULED K4+C / K1 / V / EFFECTIVE ON MERGE` (PR #969, `f392294b5`) | holds | — |
| Branch cut from fresh `origin/main` in an isolated worktree | `claude/pec-d101-act` at `f392294b5` | — |
| Run-root copies byte-identical to the preparation folder | `gen_d101_k1.py` `4892c6a3…cecb`, `gen_d101_k4.py` `075036f0…0e73`, `verify_d101_k1.py` `8b42926e…c42`, `verify_d101_k4.py` `39f9bbd0…240f` (each `cmp`-equal) | `checks/00a_run_root_copies.sha256` |
| Reliance-hold preflight, `dispatch-for-production`, 164 targets (161 product paths, `DecompCoverage/_LATEST.md`, audit-folder stem, run root), before any dispatch; again before the V dispatch | 164/164 `ALLOW`, exit 0, both times. Register `ACTIVE_RELIANCE_HOLDS.csv` `f877d931…41cbc` (header, no rows); script `b1712e4b…cd0e` | `checks/01_…`, `checks/40_…` |
| Reliance-hold preflight, `rely-for-production` | 164/164 `ALLOW` at 16:31:49 MDT (after the K1 and K4 commits; **disclosed deviation 1** below) and at 17:12:24 MDT before the V fan-in and pointer move (audit folder by its actual name) | `checks/36_…`, `checks/41_…` |
| Preimages | 161/161 as tabled; pre aggregates equal the proposal (K4 `7d6d8016…2105`, path list `bbd1374c…f7f3`; K1 modified `48e96f72…6782516`, path list `8c569e60…db2f`). The generators' own fail-closed guards re-checked them | `checks/06_pre_preimages.out`, generator READ lines |
| Local date equals `{D}` | 2026-09-26 = 2026-09-26 (and the K1 generator's own guard passed) | K1 TASK return |

## Generator runs

| Part | Executor | Command (from the repository root; literal `--repo` equal to `git rev-parse --show-toplevel`) | Result |
|---|---|---|---|
| K1 check-only | TASK `pec-task` (`preparation` actor) | `python3 {RR}/gen_d101_k1.py --repo <root> --act-date 2026-09-26 --check-only` (16:24:54 MDT) | exit 0; empty stderr; 27 READ / 28 RENDER / 1 CHECK; nothing written |
| K1 act | same TASK, once | `python3 {RR}/gen_d101_k1.py --repo <root> --act-date 2026-09-26` (16:25:08 MDT) | exit 0; empty stderr; 27 READ / 32 WRITE / 3 CHECK; report byte-identical to preparation `k1/evidence/genK1.tsv` |
| K4 check-only | manager | `python3 {RR}/gen_d101_k4.py --repo <root> --covers --check-only` (16:27:02 MDT) | exit 0; empty stderr; 136 READ / 129 RENDER / 10 CHECK |
| K4 act | manager, once | `python3 {RR}/gen_d101_k4.py --repo <root> --covers` (16:27:10 MDT) | exit 0; empty stderr; 136 READ / 129 WRITE / 10 CHECK; WRITE lines identical to the preparation A+C run on the base; only the population/census counts differ (68 folders, K1's two tolerated) (`checks/12_…diff`) |

Reports and stderr were captured in the session scratchpad and copied byte for byte into the run root.

## Finite verification (the proposal's table; K1 with K4)

| Check | Required | Observed | Output |
|---|---|---|---|
| Strict registers | exit 1; 68 registers; 285 rows (ANCHOR 146 / EXECUTION 139); 0 ERROR; exactly the same 26 XRG-013; 0 DRB-008 | exit 1; 68; 285 (146 / 139); 0 ERROR; 26 XRG-013 identical to pre (full JSON findings compared); 0 DRB-008 (pre: 66 / 263, 26 XRG-013 + 2 DRB-008). Byte-identical to the preparation's combined run | `checks/02_…`, `20_…`, `24_…` |
| Closure | exit 0; PASS; 127 edges; 68 nodes; 0 SCCs; 0 bidirectional; 0 orphans; 0 declared disagreements; isolated exactly the six; hub DEL-03-01 only; `declared_only_rows` 127; `declared_unread_count` 136 | all as required; `subject_status` PASS. The hub line in `checks/25` prints DEL-03-01's InDegree (13); its TotalDegree is 25 (`closure/hubs.csv` `DEL-03-01,13,12,25`), as the proposal states (verifier note 7). `closure_summary.json` identical to the preparation's combined run | `checks/21_…`, `25_…`, `closure/` |
| Quote currency | 127/127 | K1 report `CHECK active_execution_quotes_verbatim 127 127`; K1 verifier PASS 127/127 | `gen_d101_k1_report.tsv`, `checks/26_…` |
| Anchor coverage (COV-080) | every IN item traced by each deliverable it names; SOW-097..100 traced | PASS (74 IN items, 0 gaps; SOW-097..100 traced) | `checks/26_…` |
| K1 postimage verifier | `verify_d101_k1.py <pre> <post> --allow-k4` PASS | PASS (75 PASS lines; identical to the preparation's `verify_both.out`) | `checks/26_…` |
| K4 postimage verifier on the combined tree | `verify_d101_k4.py <original export> <post> --covers --allow-k1`: exactly one FAIL (containment, 149 vs 129), every other check PASS | exactly that: one FAIL "changed 149 (expected 129)", 10 PASS. `check_k4_extras.py` shows the 20 extras are exactly K1's MODIFY set, the 12 additions exactly K1's CREATE set, 0 removed | `checks/27_…`, `28_…` |
| Schema per register | VALID ×6 | VALID ×6 | `checks/30_schema_01..06.out` |
| Minimum fileset | PASS ×2 | PASS ×2 (generator report and a separate rerun) | `gen_d101_k1_report.tsv`, `checks/31_…` |
| Every-PR checks | exit 0; output identical before and after | harness self-check and receipts validator exit 0, outputs identical pre/post the act | `checks/04_`, `05_`, `22_`, `23_` |
| Byte identity | equal to the tables (`{D}` = table date; no slot rule) | K1 32/32, K4 129/129 (A+C column); aggregates `all_K1` `483ec239…0234`, `modified_K1` `186d9c72…6e8f`, `created_K1` `e72fc7e9…e887`, `all_A+C` `01bd1f7b…6b3d` | `checks/10_`, `11_`, `32_`, `33_` |
| Containment | exactly the selected parts' paths, the run root and (with V) the audit folder and pointer | PASS: 161/161 granted paths with their tabled act (149 M, 12 A); the run root; with V the 11-file `COV_D101_POSTSETUP_2026-09-26_1651/` folder and `DecompCoverage/_LATEST.md`; nothing outside. **Administrative records also present (verifier note 4):** the brief-authorized copies `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K14A_D101_ACT.md` and `…/returns/K14A_D101_ACT.md` (default-writable `_Coordination/**`, not product paths). HELP_HUMAN's later Notes (a) commit to `_COORDINATION.md` and its own STATUS and graph records are outside this manager's account | `checks/34_…`, `56_…` |
| Whitespace | `git diff --check origin/main...HEAD` clean for the product paths | clean for the whole diff (the run root's `.gitattributes` exempts its reports and outputs) | `checks/35_…`, `57_…` |

## Add-on V and the pointer

One TASK ran `audit-decomp` (SOFTWARE, scope ALL, prior `COV_SCA006_POSTCHANGE_2026-09-26_0051`)
into `_Evaluation/DecompCoverage/COV_D101_POSTSETUP_2026-09-26_1651/` (11 files). Result: 0 BLOCKER,
3 WARNING (the pre-existing Check-6 warnings, carried), 73 INFO, 2 EXPECTED_CONSEQUENCE;
`overall_status` `WARNINGS`; forward, reverse and objective coverage 100 % (68/68 production units);
no DEFECT. Prior COV-003/004/073/074/075/076/077/078/080 are RESOLVED. Condition "0 BLOCKERs" held
(`coverage_summary.json` `issues_blocker: 0`), so `update_latest_pointer.sh` moved
`DecompCoverage/_LATEST.md` from `f8469f88…a9dea` to `e5ad5190…c8e` (exit 0, `checks/42_…`).

## Independent verification

`VERIFIER_VERDICT_01.md` (fresh read-only TASK, candidate `b56dad37d`): **PASS WITH NOTES; K1
passes; K4 with C passes; no BLOCKING finding.** Same-day reproduction on a fresh `git archive`
export of `aca930622`: 161/161 product files and both reports byte-identical. Dispositions of its
seven notes: `VERIFIER_VERDICT_01_DISPOSITIONS.md`. The records-only repairs changed no product byte.

## After merging `origin/main`

`origin/main` `17da1a013` (PRs #964, #968, #970–#974) was merged at `dc68b5afd`. None of its 351
changed paths is one of the act's paths; the pinned basis files (`Deliverables.csv`,
`ScopeLedger.csv`, `SOFTWARE_DECOMP.md`, `docs/PRD.md`), `_COORDINATION.md`, the holds register and
`DecompCoverage/_LATEST.md` are unchanged there. Two tools the act used changed on main:

- `tools/scaffolding/write_status.sh`, a K1-pinned tool, is now `0bf835f5…` (Root PR #968,
  D-GOV-51; it adds conditions for `ISSUED → IN_PROGRESS`, creating `OPEN` files is unchanged). The
  K1 writes were made on base `f392294b5` with the pinned tool `1857ad59…97bc` and stand. On
  post-merge main a K1 `--check-only` would stop on that pin by design; the generators were not
  rerun. Reproduction is against an export of `aca930622`, as the verifier did.
- `tools/validation/validate_decomposition_registers.py` is now `300a321f…`. Rerun post-merge, its
  strict output is byte-identical to the pre-merge result (`checks/50_…`).

Post-merge reruns: closure summary identical (`51_`); receipts identical (`53_`); harness self-check
exit 0, differing only in `pointer_files_scanned` 37 → 40, which is attributable to the pointer
files main added or changed elsewhere (`chirality-app-dev` recorded-register fixtures and
`chirality-piping` pointers), not to this act (`52_`); byte identity 32/32 and 129/129 (`54_`,
`55_`); containment with V PASS (`56_`); `git diff --check` clean (`57_`).

## Disclosed deviations (accepted by HELP_HUMAN as recorded, 2026-09-26)

1. **Late `rely-for-production` preflight.** The proposal (Preconditions row) and
   `projects/pec/AGENTS.md` require it before fan-in. It ran at 16:31:49 MDT, after the K1
   (`345266081`) and K4 (`62230fa46`) fan-in commits. The register was empty and byte-identical at
   every commit, so the outcome could not differ (164/164 ALLOW; the verifier's rerun agrees).
   Nothing was rerun. For the V fan-in it ran before the fan-in (`checks/41_…`).
2. **Pre export for the postimage verifiers.** The proposal describes the before-state as an
   export of `aca930622`; the manager used `git archive f392294b5 projects/pec` as pre and the act
   commit's `projects/pec` (excluding the run root and the K14A brief copy) as post, so the
   verifiers' whole-tree containment sees product paths only. All 161 targets and basis files are
   identical at the two commits. The verifier reran both verifiers with an `aca930622` pre export
   and got byte-identical outputs, and judged `f392294b5` the correct choice for the candidate tree.

## Not claimed

No CHECKING, ISSUED, artifact acceptance, readiness or reliance claim. Git closeout is
source-control hygiene, not lifecycle issuance. Nothing here prompts about CHECKING.
