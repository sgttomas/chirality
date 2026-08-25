# Staleness and closure echo — remaining OPEN rows

Status: `READ-ONLY FINDINGS — NO DISPOSITION`

Scope: TM-APP-029, 033, 034, 036, 038, 040, and 042. Every cited `SourceSha`
still equals the current tracked source bytes. Therefore no row is
cryptographically stale at the basis. The semantic echo below is narrower:
whether applied SCA-APP-008, its Gate-5 audit, or routed notices changed the
row's factual basis.

Common current evidence:

- Applied pointer `_ScopeChange/_LATEST.md`, SHA-256
  `12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b`.
- Gate-5 dependency report, SHA-256
  `540d50daaceaa5d09bcae41128c4f5b6eb2486649fdf41378b091e00fdbd4f7f`.
- Gate-5 closure summary, SHA-256
  `88e07de9d40a9fa659c10301c1eef28bf48d0cd2ace8b5dcc120d2c38e72d662`.
- Gate-5 handoff, SHA-256
  `f11446d1466f0a621e9021b034d86ce03793c839afd34def41cf90b5f51c3b32`.

| Row | Exact source identity check | Effect of SCA/audit/notices | Echo finding |
| --- | --- | --- | --- |
| `TM-APP-029` | `APP_RUNTIME_BASIS.../FINDINGS.csv` equals SourceSha `dcfd8289ec78e31c933993e460deaca00ad3a69e536a3646479ed7c334da7ed8` | SCA-APP-008 seats later v3 carriers and Gate-5 verifies dependency endpoints; neither artifact records a governed live PEC daemon-consumption proof. No routed notice in the scoped set supplies one. | `CURRENT / REMAINS OPEN`; no closure evidence. |
| `TM-APP-033` | `DAPP49_CURRENT_LOCATION_AUDIT.../FINDINGS.csv` equals SourceSha `eb88b15632a7dfedd772b5cc32496d58c3612231b7c5194474f04666db836597`; D49-006 remains `OPEN` and requires rerun after remediation. | The Gate-5 dependency audit is a different current graph audit; it neither reruns the D-APP-49 focused environment nor dispositions its `MODULE_TYPELESS_PACKAGE_JSON` and dependency-audit observations. | `CURRENT / REMAINS OPEN`; do not equate a later dependency-closure PASS-with-warnings with D49-006 remediation. |
| `TM-APP-034` | SCA-APP-007 `RUN_SUMMARY.md` equals SourceSha `71d0b7f4e55504e4594a396d9bbb1bb1da766530c470983c1967477c0acdf129`. | SCA-APP-008 is prospective v3 scope and does not create the historical DEL-03 old-to-vNext supersession map. The Gate-5 audit checks active dependency closure, not provenance of reused historical stable IDs. | `CURRENT / REMAINS OPEN`; no closure echo. |
| `TM-APP-036` | Parity `NOTICE_TO_HELP_HUMAN.md` equals SourceSha `bd3bd64f6498053f20545e8656d9a6388da7a6c0e46f025318bf6b7d4544ea1f`. | The 2026-08-21 owner maintenance already narrowed this live row to the three-deliverable pointer/status review. The Root graceful-stop notice at `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-04_ROOT_TM-ROOT-112_ACCEPTED_GRACEFUL_STOP_REPAIR.md`, SHA-256 `1029648d039edd3c0449d0bea867853b033cc457a4b1f477c458dd4e127a6ed3`, says any distinct-helper rider is coordination only; that rider was later retired and is no longer in the row. SCA-APP-008/Gate-5 do not evidence the three reviews. | `CURRENT / REMAINS OPEN`; no stale retired rider remains in live fields. |
| `TM-APP-038` | CASE-SCC-001 `Open_Questions.md` equals SourceSha `20a8962a7b09aeff5179bdfa2ee400c12adfee2e51e39bf365d1039e336f6943`. | Gate-5 surfaces a different objective-relative nine-node dependency SCC. It does not reconcile CASE-SCC-001's 9 questions, 20 non-closed findings, or the owning status contradiction. | `CURRENT / REMAINS OPEN`; the shared term `SCC` is not closure evidence. |
| `TM-APP-040` | `CANDIDATE_HARVEST_REPORT_2026-08-03_GEN_PASS.md` equals SourceSha `534d45c3684b35ef42646360a4b83509c46cb0a0dfae660eb6b7432668add7b2`. | No tracked App notice ledger exists on the basis. The two present notice-adoption questions reinforce, but do not rule, the ledger/scanner/noise choice. The historical `18 of 59` generation count remains a source-era count, not a claim about today's total. | `CURRENT CORE / REMAINS OPEN`; no adoption or scanner disposition inferred. |
| `TM-APP-042` | D-APP-94 handoff equals SourceSha `06a3b3ddea0ba1267cfb2d31bbe9463bcea3e9b0f146158643a02172b7307088`. | SCA-APP-008, Gate-5, and scoped notices do not authorize deletion or record current existence of the three reboot-volatile roots. This repository-byte triage did not probe or mutate `/private/tmp`. | `SOURCE CURRENT / LIVE BULK STATE UNVERIFIED`; retain OPEN until an owner-gated disposition or exact OBE evidence. |

## Closure-echo conclusion

- Zero of these seven rows has current cited closure evidence.
- Zero SourceSha values are stale or missing.
- TM-APP-036 already reflects its 2026-08-21 narrowing; no second maintenance
  is proposed beyond `LastReviewed`.
- TM-APP-040's historic scan count should not be silently restated as a
  current census, but the structural no-ledger concern remains current.
- TM-APP-042's external volatile state is explicitly unknown; unknown is not
  closure.

All seven remain unchanged in the live register.
