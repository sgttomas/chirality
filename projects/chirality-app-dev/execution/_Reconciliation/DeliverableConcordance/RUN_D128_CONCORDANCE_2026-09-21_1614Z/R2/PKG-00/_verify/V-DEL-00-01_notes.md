# Verifier shard V-DEL-00-01: notes

Shard: DEL-00-01 (PKG-00), run RUN_D128_CONCORDANCE_2026-09-21_1614Z. The shard read only the frozen tree at `00115c719` and the allowed run inputs.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a | 1 | 0 | 0 | 1 |
| n | 6 | 6 | 0 | 0 |
| b | 7 | 7 | 0 | 0 |
| c | 0 | - | - | - |
| e | 0 | - | - | - |
| **Total** | **14** | **13** | **0** | **1** |

- Distinct items refuted on a verdict field (Disposition or Response): **0 of 14**.
- One item is CONTESTED on Disposition: `DEL-00-01#CLM-018.2`. It does not count toward the Addendum 3 rerun threshold.

## (ii) Patterns and item notes

1. **The stale "current snapshot" cluster holds.** `CLM-003` and `REGISTER-1` are correctly `STALE_SPECIFICATION`.
   - The present facts are false: `_REFERENCES.md:13` and SoW `:49` call D53A the current snapshot. At the frozen basis, `DepClosure/_LATEST.md:1` and `DAG_CLOSURE_CONTROL.md:9,64,109` name `CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034`.
   - Addendum 5 rule 1 therefore applies.
   - The other attributes still hold: the 1034 snapshot has `scc_count` 0, and `edge_list.csv:120` shows DEP-10-03-006 active with no DEP-10-02-004 edge.
   - Register rows D-APP-111 and D-APP-114 (`_REGISTER.md:126,129`) do not name DEL-00-01. The worker was right not to apply MR-11 and to tag them `(context)`.
   - CauseTag `CARRIER_PROPAGATION` with `CAUSE2:DOC_HYGIENE` is acceptable. For REGISTER-1, DOC_HYGIENE as the primary tag would also be defensible, but it is not a refutation.
2. **ALIGNED control-record rows reproduce from in-root records.** These rows are CLM-005, CLM-008, CLM-009.2, CLM-009.3, CLM-014 and CLM-026. The records checked were:
   - `Ruling_Register.csv:2-7`;
   - `CONTROL_REGISTER.csv:12`;
   - `CLOSURE_SCC002_CHANGE_HANDOFF_2026-05-24_2020/Decision_Log.md:9-10` and `Dependency_Closure_Report.md:35`;
   - the absence of a `Dependencies.csv` in the deliverable folder;
   - `_STATUS.md:3,19`;
   - `D-APP-54_RULING_2026-07-11.md:40-54`;
   - INSP-03 lines 17, 24, 25 and 36, which match the AssessmentEvidence tokens.
   - `CLM-012.2` (AC-001) was re-checked independently with a read-only `git show 7f1b8f746`. All 250 removed legacy lines reappear in the SoW, apart from 26 heading lines that were demoted in level. Preservation holds.
3. **The only contested item is the LOW self-flag on `CLM-018.2` (VER-001).** In-root absence of a claim map or parity report supports `DOCUMENTED_UNIMPLEMENTED`. The alternative reading is `UNKNOWN`.
   - D-APP-68 packet `:62-64` says Root D-GOV-16 authorized the SoW conversion.
   - Any migration validation or parity output would therefore sit in Root tooling or execution, outside the evidence roots.
   - Under the brief's roots rule, the item is recorded as CONTESTED.
   - CauseTag `PRE_V3_DRIFT` is correct: the migration is dated 2026-07-13/14.

Items checked with nothing further to note:

- `CLM-001` and `CLM-007` are heading-only `NOT_AUDITABLE`.
- `CLM-002`: identity values match `_CONTEXT.md:5-16` and PKG-00 `README.md`.
- `CLM-006`: every in-root reference path exists.
- The PKG-10 registers were not opened (other packages' deliverable folders). The worker's use of `coverage.csv:50-51` and the R6 backcheck (`CHANGED_CLAIM_REEXTRACTION.csv:72-73`) as proxies is sound.
- `PostReleaseBasis = NO` is correct on every row. No cited path appears in `TOUCHED_PATHS.csv`.
- There is no code evidence in this deliverable, so REACH and R4-Q1 do not arise.

## (iii) Effort

- About 25 files or line ranges read, plus 3 read-only `git show`/`log` calls against the frozen tree.
- The context budget was not tight.
- No tests were run, nothing was installed, and no ledger or worker file was edited.
