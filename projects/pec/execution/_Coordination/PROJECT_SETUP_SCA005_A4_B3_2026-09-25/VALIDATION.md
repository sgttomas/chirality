# PROJECT_SETUP — SCA-005 A4 + B3 (D-PEC-93 option A) Validation

All commands ran from the repository root (worktree
`agent-adb8a84864c6fa862`, branch `claude/pec-d93-project-setup-act`) with
`PYTHONDONTWRITEBYTECODE=1`, Python 3.13.7, local date 2026-09-25 (MDT).
`checks/COMMANDS.txt` lists every command with its exit code; each output is
the file named in the table. The probe scripts are in `probes/` (they were run
from a scratch copy outside the repository; the committed copies are the same
bytes).

## Preconditions

| Check | Result |
|---|---|
| Fetched `origin/main` contains `04e04da00f620a1a5786ee744b167490cc90531c` (PR #913), with the ruling and register row `D-PEC-93 … RULED A / EFFECTIVE ON MERGE` | holds |
| Local date equals the act date | 2026-09-25 = 2026-09-25 (the generator's own guard also passed) |
| Branch cut from fresh `origin/main` | `claude/pec-d93-project-setup-act` at `04e04da00`, in an isolated worktree |
| Reliance-hold preflight, `dispatch-for-production`, 34 targets (31 product paths, `DecompCoverage/_LATEST.md`, audit-folder stem, run-root stem) — before the generator and before the audit dispatch | 34/34 `ALLOW`, exit 0 (`checks/00_preflight_dispatch-for-production.out`); register `ACTIVE_RELIANCE_HOLDS.csv` `f877d931…41cbc` has a header and no rows; script `b1712e4b…cd0e` |
| Reliance-hold preflight, `rely-for-production`, 34 targets (audit folder by its actual name) — before fan-in | 34/34 `ALLOW`, exit 0 (`checks/08_preflight_rely-for-production.out`) |
| Generator copy hash | `cfae005258659c55915d0e9e2a8566399c3c84a95ede8e567205fecaea08d6c2` |
| Preimages (19 MODIFY hashes; 12 CREATE targets absent) | 31/31 as tabled. Evidence: the generator's fail-closed preimage guard and its READ lines (`gen_d93_report.tsv`), and `checks/00b_preimages_at_04e04da00.out` (31/31 against the base commit). The manager's pre-run working-tree check also returned 31/31 but printed to the terminal only; its output was not saved, and `00b` was added after verifier note N-3 |

## Finite verification (proposal table, option A)

| Check | Required | Observed | Output |
|---|---|---|---|
| Generator | exit 0; 31 writes as tabled | exit 0; 31 WRITE lines, empty stderr | `gen_d93_report.tsv` |
| Written paths ⊆ 31-path list | holds | 31 product paths changed, all on the list; nothing else under `PKG-*` | `git diff --name-only origin/main...HEAD` |
| Byte identity | equal to the table (`{D}` = table date, no slot rule) | 31/31 OK | `checks/01_postimage_hashes.out` |
| Aggregate | `c4525add…727a`; path list `1133e1ab…b9f1` | equal | `checks/09_aggregate.out` |
| Strict registers | exit 0; 66 registers; 263 rows; 0 errors / 0 warnings | exit 0; 66 registers; 263 rows (ANCHOR 140 / EXECUTION 123); 0 / 0 | `checks/02_strict_registers.out` |
| Closure | exit 0; PASS; 111 edges; 66 nodes; 0 SCCs; 0 bidirectional pairs; 0 orphans; isolated exactly DEL-00-03, DEL-01-05, DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05; hub DEL-03-01 only | exit 0; `subject_status` PASS; 111 / 66 / 0 / 0 / 0; isolated exactly those six; hub DEL-03-01 (degree 25); checks `isolated_units` and `hubs` WARNING, all others PASS | `checks/03_closure.out`, `closure/` |
| Schema per register | VALID × 8 | VALID × 8 (exit 0 each) | `checks/04_schema_01..08.out` |
| Minimum fileset | PASS × 2 | PASS × 2 (generator run and separate rerun) | `checks/05_fileset_*.out` |
| Row conservation | each touched register's `DependencyID` set after ⊇ before; `ACTIVE` gains only the 8 added | holds for all 8; ACTIVE gained exactly the 8 added; 20 rows now `RETIRED`; 21 existing rows changed (20 retired + `DEP-03-01-007`), each only in the cells the proposal names | `checks/06_row_conservation_and_quotes.out` |
| Quote currency (new rows) | every new or refreshed `EvidenceQuote` verbatim in its `EvidenceFile` | 5/5 EXECUTION quotes verbatim (`DEP-02-08-003`, `DEP-02-09-003`, `DEP-03-01-007`, `-015`, `-016`). The 4 new ANCHOR rows carry the D-PEC-62 locus-descriptor form (`PackageID PKG-02`, `DeliverableIDs include DEL-02-0x`), identical in form to every existing anchor row (for example `DEP-02-07-001/002`); they are not verbatim-quote rows and the generator does not assert them | same |
| Whitespace | `git diff --check origin/main...HEAD` clean (proposal) | **Disclosed deviation.** Product paths: 0 notices. Whole diff: exit 2, 109 `trailing whitespace` notices, all in raw tool outputs kept byte-exact in this run root (82 in the CR-at-EOL rows of `closure/*.csv`; 27 in the empty fourth column of the generator's READ lines in `gen_d93_report.tsv`). They are not normalized because they are hashed evidence (`gen_d93_report.tsv` equals the verifier's independent rerun). `.gitattributes` states cosmetic whitespace does not gate CI | `checks/07_diff_check.out` |
| Containment | exactly the 31 paths, the `COV_SCA005_POSTSETUP_*` folder, `DecompCoverage/_LATEST.md` and the run root | holds at `995af4f36` and at `f64a9a7c0` (84 paths). The manager then adds only the brief-authorized return files under `AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/` (`C5_D93_PROJECT_SETUP_ACT.md`, `C5_VERIFIER_VERDICT_NN.md`) | `git diff --name-status origin/main...HEAD` |

## Re-audit and pointer

The TASK `audit-decomp` child wrote only
`_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/` (9 files:
the method's eight plus `PrePost_Comparison.md`). Result: 0 BLOCKER, 3
WARNING (PRE-EXISTING v2-artifact-location warnings, DEL-01-03, DEL-01-05,
DEL-08-02), 70 INFO; `overall_status` `WARNINGS` (the method's enum for the
proposal's "WARN"). Prior COV-001/002 (BLOCKER), COV-070/071, COV-068/069,
COV-079/080/081 and COV-072 are resolved; COV-006/008/042 and COV-077 carry;
COV-078 carries with "64 of 66". The pointer condition (0 BLOCKERs) held, so
`update_latest_pointer.sh` moved `DecompCoverage/_LATEST.md` (exit 0).

## Not claimed

No CHECKING, ISSUED, acceptance, readiness or reliance claim. Git closeout is
source-control hygiene, not lifecycle issuance. Independent verification is
recorded in `VERIFIER_VERDICT_NN.md` and in the HELP_HUMAN run's
`returns/C5_VERIFIER_VERDICT_NN.md`.
