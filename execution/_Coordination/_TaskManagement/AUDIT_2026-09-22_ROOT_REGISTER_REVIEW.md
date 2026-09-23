# Root Task Management register review — 2026-09-22

Invoking loop: Root. Mode: owner-selected review of all live rows for triage,
staleness, closure echo, deferral triggers, row maintenance, and archive. Basis:
`main@212564bc472fa56e232ef116d73f4065e32c111a`. The owner authorized
evidence-based closure decisions in this review; this is a manager assessment,
not a claim that the owner personally reviewed each row.

## Federation and coverage

`python3 tools/taskmgmt/taskmgmt.py federation --register
execution/_Coordination/_TaskManagement/REGISTER.csv --out
.chirality/tmp/root-tm-federation-2026-09-22.json` returned **COMPLETE**:
four tracked canonical registers and archives; no operational or integrity
errors, no register writes. The output path was verified ignored by
`.gitignore` before use. Root validated with 18 live rows (10 OPEN, 8
DEFERRED) and 109 archived CLOSED rows. `archive --dry-run` found zero live
CLOSED rows to move. This invocation did not run a broad candidate harvest.

All 109 archived rows remain historical closures. The archive validates in the
federation survey. Its dispositions are 44 DUPLICATE, 34
INFORMATIONAL_NO_ACTION, 20 RESOLVED_BY_DECISION, 9 RESOLVED_WITH_CHANGE,
one OBE, and one SUPERSEDED_BY_SCOPE_CHANGE. The federation found 22
Root-closed/Piping-open linked pairs (TM-ROOT-077–097) or Root-closed/App-open
(TM-ROOT-117/TM-APP-032), and one App-closed/Root-open pair
(TM-APP-001/TM-ROOT-035). These are independent loop dispositions, not
evidence that the Root archive should be rewritten or that TM-ROOT-035 is
closed. No archived row is reopened or reclosed here; its original ruling and
closure evidence remain the authority for its historical treatment.

## Live row rulings

| Row | Review result and present evidence |
|---|---|
| TM-ROOT-035 | **Retain OPEN pending an owning disposition of the original recommendation.** SCA-004 `Task_Management_Harvest.csv` sent `source_identity` acceptance to the former G0.5 route, and R16 recorded it held at that time. The later Runtime D-GOV-43 SCA-004 `HOLD_SUCCESSOR_MAP.csv` explicitly marks that binding closed and retires the old fan-ins; D-APP-127 supersedes G-HELPER. The historical Root DEL-02-06 and its OUT-003/004/005 activation ladder are no longer the live implementation route. No Root row-level act was found that accepts the successor result as disposition of the 07-28 recommendation or expressly retires that recommendation. Do not ask for retired G0.5/G-HELPER proof or infer completion of the recommendation from the new host alone. |
| TM-ROOT-037 | **Retain DEFERRED, STILL_BLOCKED.** Piping's linked TM-PIP-001 is still DEFERRED. D-58 retains the successor mechanism as unresolved; no cited Piping owner record names all required owner, carrier, and activation/schedule elements. |
| TM-ROOT-039 | **Retain DEFERRED, STILL_BLOCKED.** The required Root PRD or D-GOV choice assigning reusable work-surface authority to Root, App, or both was not found in the current Root decision register through D-GOV-44 or `docs/PRD_ROOT.md`. |
| TM-ROOT-040 | **Retain DEFERRED, STILL_BLOCKED.** No D-GOV act explicitly disposes the application-environment-profile authority/schema and RUNTIME-OPEN-005 together. D-GOV-43's Codex configuration rules address a different host concern. |
| TM-ROOT-041 | **Retain DEFERRED, STILL_BLOCKED.** No Root act explicitly assigns or declines all four resource-governance elements in this row's trigger. |
| TM-ROOT-042 | **Retain OPEN for the unresolved cadence/disposition question.** D-GOV-43 and its A2 supplement select the App-owned Runtime service, socket and stock Codex child; D-APP-127 supersedes G-HELPER, and the later Runtime D-GOV-43 SCA-004 closes the old physical `source_identity` binding. The former G-HELPER path is not a live prerequisite. No owning row-level decision was found that disposes the original logical-composition versus physical-bundling/cadence question for the A2 arrangement. |
| TM-ROOT-104 | **Retain DEFERRED, STILL_BLOCKED.** Current Root PRD and D-GOV register do not contain the row's required explicit Root product-basis disposition of the 2026-08-02 owner direction. Piping's own decisions do not decide Root basis. |
| TM-ROOT-106 | **Retain OPEN; owner judgment needed on scope.** D-GOV-43 makes Codex the sole MVP engine and Pi/oMLX compatibility history, while App `docs/CONTRACT.md` K-ENGINE-6 still states the Pi `0.80.10` exception and legacy adapters/packages remain. This row requires a Root decision plus supply-chain validation; no exact retirement of the historical acceptance question or equivalent validation was found. The newer engine decision alone cannot establish that every part of the concern is resolved. |
| TM-ROOT-108 | **Retain OPEN; partial implementation evidenced.** SCA-004 maps terminal reconciliation into DEL-02-11, and App K-EVENT-3 retains exactly one durable terminal outcome. Current Runtime `SessionStore.settleRunningOnStart` settles persisted `running` sessions to `interrupted`; `app-owned-composition.ts` calls it during production startup. `session-and-residency.test.ts` checks replay and a second idempotent settlement, and `app-owned-composition.test.ts` checks startup recovery and a subsequent new turn. These are real repair evidence. The startup caller catches settlement errors and continues, the startup fixture expressly does not test actual SIGKILL, and append-event/status-update are separate writes. Exact one-terminal and drain behavior under repeated crash, plus owner acceptance of the closure evidence, remain unestablished. |
| TM-ROOT-111 | **Retain OPEN.** The original candidate-whitespace gate was simplified later, but the requested standing local pre-push cheap-guard step is not present in Root role/workflow or validation guidance. Other receipt/register/diff guards remain meaningful. The row needs a scoped owner decision if narrowed. |
| TM-ROOT-113 | **Retain OPEN.** `tools/validation/loop_receipt_contract.py` still matches `number + tests/cases/rows/claims` without the reported governed-identifier exclusion; no narrow detector and regression evidence found. |
| TM-ROOT-114 | **Retain OPEN.** `tools/practitioner_harness/adapter_project.py` still requires `State` and `ID` headers in `parse_decision_register`, then reports `no rows parsed` as a parsed fact; the Root D-GOV register instead has `ID`, `Decision`, `HumanRuling`, and `Unblocks` headings. |
| TM-ROOT-115 | **Retain OPEN.** `validate_instruction_entrypoints.py` currently names App, Piping and PEC project launchers, but does not validate all nine surfaces described by this row, including four `taskmgmt-init-prompt.md` files. The v3 workflow changes may alter the right target; an explicit retirement or replacement verdict is needed before closure. |
| TM-ROOT-118 | **Retain OPEN.** `tools/taskmgmt/taskmgmt.py` still derives loop identity from the first two path segments and deduplicates by loop, basename, class and ID. Those rules still expose the cited PEC alias and same-basename collapse classes; no complete repair or regression evidence found. |
| TM-ROOT-119 | **Retain DEFERRED, STILL_BLOCKED.** The 2026-08-09 owner direction requires an owner declaration that the observation period is complete; no such declaration or selection of the four options was found. |
| TM-ROOT-120 | **Retain DEFERRED, ACTIVATABLE on next export act.** The current `exports/chirality-app/export-manifest.csv` claims `docs/PRD_ROOT.md` is 95,590 bytes with SHA-256 `83cea4...`; the tracked file is 96,009 bytes with SHA-256 `b6fa4e...`. Later export activity did not cure this stale derivative. Regeneration evidence is absent. |
| TM-ROOT-123 | **Retain DEFERRED, STILL_BLOCKED.** The TM105 candidate's `OPEN_DECISIONS_AND_ACCEPTANCE_FORM.md` retains TBD-105-01–21 and expressly says no no-TBD successor exists. No exact qualified successor and fresh independent refutation were found. |
| TM-ROOT-127 | **Retain OPEN.** `validate_instruction_tranche_manifest.py` still checks `basis` only against the 7–40 lowercase hexadecimal regex; it does not resolve it as a Git commit. |

The Root live and archive CSVs have **no row deltas** from this review. There
is no justified closure to archive at this revision. In particular, a passing
rerun, changed SHA, routed owner, or retired implementation alone would not
meet the rows' explicit closure conditions. A future owner disposition may
reframe TM-ROOT-035/042/106/115 under the new runtime and workflow basis, but
this review records that as unresolved judgment rather than a current closure.
