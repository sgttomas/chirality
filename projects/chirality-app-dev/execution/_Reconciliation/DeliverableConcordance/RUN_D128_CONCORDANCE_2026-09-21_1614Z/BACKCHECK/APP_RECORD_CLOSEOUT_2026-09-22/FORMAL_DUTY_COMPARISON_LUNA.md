# Formal dependency-duty comparison

This comparison assesses all 81 `FORMAL_DUTY_PENDING_SOURCE_SPECIFIC_ASSESSMENT` rows in `DDEPEND_ROWS.csv`, preserving each exact ClaimKey and source-row identity. It compares current formal dependency records with the current deliverable ScopeOfWork and prepared dependency previews. It reports record state only: no live source/register was edited, no new edge or satisfaction state is inferred, and no acceptance is declared.

## Result

The 81 rows classify as: CURRENT_ROWS_PRESENT_NO_UNSUPPORTED_STATE_CHANGE=31, NO_DEPENDENCY_CSV_FIELD_DUTY=14, NO_FORMAL_DEPENDENCY_ROW_IDENTIFIED=3, OPEN_FORMAL_RECORD_REPAIR=8, REFERENCE_STATE_RECONCILED_CURRENT_ROWS_REMAIN_DISTINCT=25.

Eight source rows identify concrete formal-record repair candidates, converging on six distinct DependencyIDs; no new DependencyID is required:

Agent 0 clarification after the comparison: the dated `DEP-02-04-008/-009` note in the table is a **no-change historical review**, not a seventh repair candidate. The CSV correctly classifies it outside `OPEN_FORMAL_RECORD_REPAIR`. The six actual repair IDs were applied and checked in `FORMAL_DUTY_FINAL.csv`; the table below preserves the comparison's pre-application observations.

| DependencyID | Field(s) | Finding |
|---|---|---|
| `DEP-02-04-008/-009` | `Notes/LastSeen` assessment | Source duty asks to restate hash maturity after recompute. Current dated v20 notes remain historically accurate; v25 D38 state is separately recorded. No concrete update inferred without owner-specific postimage. |
| `DEP-05-03-009` | `Statement` | Says REF-006 has HASH_MISMATCH despite current MATCH evidence and its own current MATCH quote. |
| `DEP-07-02-004` | `TargetLocation` | Still machine-absolute; current source duty calls for repo-relative location. |
| `DEP-08-01-013` | `TargetLocation` | Still points at the machine-absolute old agent-file path; REF-007/current CLM-006 identify the workflow method file. |
| `DEP-08-04-002` | `Statement/Notes/LastSeen/SatisfactionStatus` | Still says seven v19 references are MATCH with v19/v20 notes; D38_CHECKS records v25. A v25/PENDING postimage is in the prepared source-specific comparison basis; it is not yet applied. |
| `DEP-09-05-011` | `TargetRefID / TargetName / TargetLocation / Statement / EvidenceQuote` | Still asserts CI workflow path is TBD; current ScopeOfWork CLM-004 names the repository-root workflow. |
| `DEP-10-05-009` | `Statement` | Still says hash-mismatch warning is preserved although current REF-006 is MATCH and Notes say resolved. |

The DEP-08-01-013 comparison is limited to retargeting the existing DOCUMENT/REF-007 locator to its current source; it changes no graph edge identity/type. For DEP-08-04-002, the current v25/PENDING state is recorded as a prepared proposal only; the current table remains unchanged. Keep all other Status/SatisfactionStatus values unchanged unless separate live evidence and the owning procedure justify a change.

Rows already represented and consistent with current source/previews include the current-session/runtime retargets, retired SDK-era dependencies, current Codex-only descriptive boundaries, current REF-002/003/006 source-currency rows, and dependency locators that now point to ScopeOfWork. A preview match is comparison evidence, not approval. Specific ClaimKey-to-row evidence and the exact source line identities are in the CSV.

## Evidence-gated work remains distinct

Some current formal rows remain ACTIVE/PENDING or ACTIVE/TBD. This comparison preserves those states. Examples include the three DEL-07-03 rows `DEP-07-03-012/-013/-014`, native implementation rows `DEP-06-01-014`, `DEP-06-04-007/-008`, `DEP-06-06-004..007`, and existing evidence-gated rows in DEL-04-02 and DEL-09-04. They are not record repairs merely because their validation remains open. For DEL-06-01, DEL-06-02, DEL-06-04 and DEL-06-06, REF-006 source-currency rows are not owners of separate native implementation tests; see row-level notes in the CSV.

DEL-07-04 row `DEP-07-04-008` now has current module locators and a current ScopeOfWork quote, but the source asks to reconsider its prior SATISFIED state because the MCP half may be legacy-only. This comparison lacks current live reach/evidence and preserves its recorded state for owner review.

## Method and provenance

- APP-HOLD-1 reliance was run from the App root against all 54 folder targets derived from `execution/PKG-*/1_Working/DEL-*`; verdict `ALLOW`, 54 targets, none blocked. The 54-target set is the target of the preflight, not a claim that all 54 are nonretired reference files.
- Read Root `AGENTS.md`, `agents/AGENT_TASK.md`, App `AGENTS.md`, App `instructions/AGENTS.md`, and the Chirality change skill. Hashes: `AGENTS.md` `1bb670ca339a990b153cf033dac2d8e29ca71bdea0accee4200e6dd1feed3d57`; `agents/AGENT_TASK.md` `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`; `projects/chirality-app-dev/AGENTS.md` `abb4ff48987b427015ef412874aef8651e028fbc62c49fc3e53a3a9b755b015f`; `projects/chirality-app-dev/instructions/AGENTS.md` `12b2c01c7e960bc35ef7bf55d2a968687bef776826f12edfea8b8fdbc778e3de`.
- Source matching used exact ClaimKey joins. `SourceDataRow` is the 1-based CSV data row excluding header; `SourceFileLine` is the physical line including the header. `DDEPENDDataRow` similarly identifies the 1-based data row in `DDEPEND_ROWS.csv`.
- Current dependencies are resolved from each of the 54 actual `DEL-*` folders. `CurrentDependencyRowLocators` gives the exact Dependencies.csv physical line and recorded status/satisfaction. `_DEPENDENCIES.md` was checked where the duty depended on a mirror; older extracted/history tables were kept distinct from current summary tables.
- Prepared preview post-images are counted only when every named ChangedFields value matches the current row. D38 reference evidence is `D38_CHECKS.json`: corpus v25 filtered apply and audit PASS on 51 nonretired deliverable reference files; retired DEL-09-07 is excluded and the file explicitly records the unfiltered retired-reference mismatch. This is not a broad canonical PASS.
- Requested model was gpt-6-luna/xhigh per parent brief; execution model metadata is not exposed by this runtime. Comparison was records-only; no delegation.

Input SHA-256:

- `DDEPEND_ROWS.csv` `18a4ae70c2021e192846bedab7c2dfe0f871d15fdfc2a241acc2e53e90e9977b`
- `W00_03_ROWS.csv` `1b0339be830ddac9fb85a5074b1e08126ec523e224c8d669050c8f35e7583e44`
- `W02_03_ROWS.csv` `def8b681d418aab70bff55380aca0f3cd62b29dffcedcb45872eafdffe662459`
- `W04_06_ROWS.csv` `8371d948a4404e139f4fa447427753f66dbcab18bcaf3f963cacd2e12130f996`
- `W07_10_ROWS.csv` `75a599517105b4e6da9ff37482cc569cfc194cbaea7677b01ae4777e5c26cf73`
- `W10_ROWS.csv` `ac8b12429b59380d23d6c433717913d2bfbb149ecd016178bd39fe676299e15c`
- `D38_CHECKS.json` `a64d3375ff17427557e0b65a7d595e6ca151cc5a557425a0fffa11c41466dcb4`

## Limits

The comparison does not close live product tests, re-establish historical acceptance, modify the 81 source records, or resolve decisions outside the existing record basis. The row-level CSV identifies each source duty and whether its current formal record is present, already consistent, evidence-gated, or needs a concrete record repair.
