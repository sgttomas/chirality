# PKG-00 — R2 verification

- **Run:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, package PKG-00 (DEL-00-01, DEL-00-02). No double-blind unit (`NONE`).
- **Method:** `BRIEFS/R2_PACKAGE_MANAGER.md` step 7 with RUN_BASIS Addendum 3.
  - Selection is deterministic (`_scripts/select.py` → `_verify/SELECTION.csv`, SHA-256
    `0abd1ed031fcbb94a662ea9c55d2b7236080bae055085055a20c3efedc3507ef`).
  - There were two fresh verifier shards, one per unit, each with 50 items or fewer.
  - Both shards used one shared grading key (`_BRIEFS/VERIFIER_SHARD.md`).
  - Corrections are built by script (`_scripts/corrections.py` → `CORRECTIONS.csv`).
  - Verifiers edited no ledgers.

## 1. Structural result

All four files pass: 0 errors and 0 warnings on each. The validator is `_scripts/validate_ledger.py` v2, run from `projects/chirality-app-dev`.

| File | Mode | Result | SHA-256 |
|---|---|---|---|
| `DEL-00-01/DEL-00-01_claims.csv` (41 rows) | ledger | PASS, 0 errors / 0 warnings | `d87cf0978d2f2d9b4a0db7b43ad5f0fac97db963b136f8b96778e762fb815209` |
| `DEL-00-01/DEL-00-01_reverse.csv` (261) | reverse vs `REVERSE_INPUT/COMBINED_capabilities.csv` | PASS, 0 / 0 | `661ef66a48dff46718dbbf7ebde4bf37710f2c6692919912d5f2cbb73d96bf54` |
| `DEL-00-02/DEL-00-02_claims.csv` (49 rows) | ledger | PASS, 0 / 0 | `6fde4398266f04c369e76fc0616808b7066830e6931250bc25eb4e15a5edc98b` |
| `DEL-00-02/DEL-00-02_reverse.csv` (189) | reverse vs `REVERSE_INPUT/COMBINED_capabilities.csv` | PASS, 0 / 0 | `eaea8a203abea775bdc1a10759527a5b89792191bb0674d94536292b0e3b8fa5` |

- **Seals.** Each claims file has the same SHA-256 at three points: the forward return, after the reverse pass, and at verification.
- **Errata.** Neither worker wrote an errata file.
- **Combined capability files.** The validator accepts only one `--capabilities` file. Each unit's selected `R2/SURFACES/<AREA>_capabilities.csv` files were therefore concatenated by `_scripts/areas.py`, with the header written once. `REVERSE_INPUT/AREAS.md` records the selected areas and their basis.

## 2. Recheck table per deliverable

| Unit | Selected | a | n (30% other non-ALIGNED) | b (15% ALIGNED) | c (20% CLAIMED_BY/PARTIAL) | e (errata) | CONFIRMED | REFUTED | CONTESTED | Verdict-field REFUTED (distinct / checked) | Rerun? |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| DEL-00-01 | 14 | 1 | 6 | 7 | 0 | 0 | 13 | 0 | 1 | 0 / 14 = 0.0% | No |
| DEL-00-02 | 15 | 3 | 9 | 3 | 0 | 0 | 14 | 1 | 0 | 1 / 15 = 6.7% | No |
| **Reverse responses** | 0 | — | — | — | 0 | — | — | — | — | 0 / 0 (no CLAIMED_BY or PARTIAL to sample) | No |

- **Addendum 3 threshold.** Neither ledger exceeds 10% verdict-field refutations, either on ledger rows or on reverse responses. Neither ledger had a structural failure. **No rerun.**
- **Class c had no items.** Both reverse files are 100% `NOT_MINE`, so there were no CLAIMED_BY or PARTIAL responses to sample.
- **Shard files:**
  - `_verify/V-DEL-00-01.csv`: `399823f20a389796575af77d84d444d139ced71e34ba52c347fca7d0b3749162`.
  - `_verify/V-DEL-00-02.csv`: `005b117e6476755fa518cc57f922db347a10f50e8e0b96ddd2c9aa4a86ae632d`.
  - Each has a `_notes.md` alongside.

## 3. REFUTED and CONTESTED items

### REFUTED: `DEL-00-02#CLM-014.2` (AC-001, "every legacy source line preserved"), class a (LOW)

- **Disposition (verdict field).** The sealed value is `UNKNOWN`. The verifier reads `ALIGNED`, with `PARTIALLY_IMPLEMENTED` as the alternative if ruled amendments count as non-preservation.
  - The check can be run inside the evidence roots. `git -C <frozen> show fae8e5117^:` gives the pre-migration Datasheet, Specification, Procedure and Guidance files.
  - All 209 non-blank legacy lines appear in `ScopeOfWork.md` at `670a71ed0`; only heading levels changed.
  - At `00115c719`, 11 of those lines differ. The owner-ruled D-APP-65 and D-APP-68 repairs changed them (`_run_records/TASK_RUN_2026-07-19_DAPP68_concordance_repairs.md:12`).
  - Evidence: `…/DEL-00-02_…/ScopeOfWork.md:217`.
- **Field refutations that follow from the Disposition.** These are recorded in `CORRECTIONS.csv` and do not count toward the rerun threshold.

| Field | Sealed value | Corrected value |
|---|---|---|
| ImplementationEvidence | `NONE_FOUND` + search | documentary claim: legacy files at `fae8e5117^` vs SoW at `670a71ed0` / `00115c719` |
| VerificationEvidence | `NONE_FOUND` | `RUN-INSPECTION@00115c719` |
| DirectionEvidence | `NONE_FOUND` | `NOT_APPLICABLE` |
| CauseTag | `DOC_HYGIENE` | `NONE` |
| RemainingWork | `UNKNOWN` | `NONE_OBSERVED` |

- These corrected values presuppose the verifier's ALIGNED reading. If R3 settles on `PARTIALLY_IMPLEMENTED` instead, the CauseTag, DirectionEvidence and RemainingWork corrections do not apply as written.

### CONTESTED: `DEL-00-01#CLM-018.2` (VER-001, parity record), class a (LOW, self-flagged)

- **Disposition.** The sealed value is `DOCUMENTED_UNIMPLEMENTED`: no claim map, parity report or checklist exists in the App roots, and migration commit `7f1b8f746` carries no parity record.
- **Alternative reading:** `UNKNOWN`. D-APP-68 packet `:62-64` says Root D-GOV-16 authorized the SoW conversion, so any parity output would sit in Root tooling or execution. Those are outside the evidence roots.
- The item is contested under the roots rule.
- CauseTag `PRE_V3_DRIFT` is confirmed.

## 4. Patterns

1. **The same AC/VER family was handled differently in the two units.**
   - The family is the SoW-conversion parity and preservation claims: DEL-00-01 CLM-012.2 / CLM-018.2 and DEL-00-02 CLM-014.2 / CLM-021.2.
   - For DEL-00-01, the verifier independently confirmed CLM-012.2 (AC-001 preservation) ALIGNED by `git show 7f1b8f746`.
   - For DEL-00-02, the worker left the equivalent AC-001 as UNKNOWN; its verifier refuted that on the same kind of git evidence.
   - The two VER-001 rows (parity record) were sealed differently: DEL-00-01 CLM-018.2 as `DOCUMENTED_UNIMPLEMENTED` (LOW) and DEL-00-02 CLM-021.2 as `PARTIALLY_IMPLEMENTED` (LOW; rechecked and CONFIRMED by its shard). Both turn on artifacts that would sit under Root D-GOV-16 tooling, outside the roots.
   - R3 should treat these four rows together. The same pattern probably recurs in every deliverable migrated under D-APP-68 and D-GOV-16.
2. **The stale "current DepClosure snapshot" cluster reproduces in both units.**
   - The SoW, `_REFERENCES.md`, `CONTROL.md` and register rows of both deliverables still name D53A (or SAFE_MOVES in `CONTROL.md`) as current.
   - At the frozen basis, `_LATEST.md` and `DAG_CLOSURE_CONTROL.md` name `CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034` (D-APP-111, D-APP-114).
   - Both verifiers confirmed `STALE_SPECIFICATION` under the Addendum 5 tie-break.
   - Both confirmed that MR-11 is correctly not applied, because D-APP-111 and D-APP-114 do not name either deliverable.
3. **No code surface.** Neither ledger cites code, so REACH, R4-Q1 and PostReleaseBasis do not arise. PostReleaseBasis is `NO` throughout, and verifiers confirmed that no cited path is in `TOUCHED_PATHS.csv`. Every HumanDecisionNeeded value is `NO`.
4. **Minor anchor slips that change no verdict (DEL-00-02, not refuted).**
   - `CLM-010.4` calls HOFF-SCC-001-009 superseded, closed or deferred. It is actually `COMPLETE_GRAPH_REDUCTION_ONLY`.
   - `CLM-003`'s `DAG_CLOSURE_CONTROL.md:97-98` anchor holds no snapshot text.
   - `CONTROL.md` also calls SAFE_MOVES current.
5. **Evidence-root incident (DEL-00-01 worker, self-reported).**
   - One grep filter failed, and output lines from PKG-10 deliverable folders appeared: DEL-10-02 and DEL-10-03 `Dependencies.csv`, `_DEPENDENCIES.md` and `Evidence_D53A_*`.
   - No row cites or relies on them. The verifier independently judged the in-root proxies sound: snapshot `edge_list.csv`, `coverage.csv` and the R6 backcheck rows.
   - Recorded here and in `STATE.jsonl`; no rerun.
