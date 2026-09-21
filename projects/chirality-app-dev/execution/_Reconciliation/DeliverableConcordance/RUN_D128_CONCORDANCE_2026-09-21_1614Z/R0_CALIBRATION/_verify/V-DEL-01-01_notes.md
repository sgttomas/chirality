# V-DEL-01-01 — verifier shard notes (RUN_D128 R0 calibration, unit V)

Evidence-only shard. Scope: 34 SELECTION items for DEL-01-01, checked against the frozen tree `00115c719`. No ledger was edited. Git use was read-only `log`, `show` and `blame`.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 28 | 18 | 2 | 8 |
| b | 5 | 3 | 1 | 1 |
| c | 1 | 1 | 0 | 0 |
| **Total** | **34** | **22** | **3** | **9** |

**REFUTED (3).** Each is a single-field error. The Disposition holds in all three.

| Key | Field | Error |
|---|---|---|
| CLM-008 | DirectionEvidence | Cites a non-CONTEXT notice. |
| CLM-009.11 | AssessmentEvidence | STILL CURRENT is wrong. INSP-03 REQ-005 does not cite the path. |
| CLM-009.4 | VerificationEvidence | `DOC-BASIS(D-APP-127)` is misattributed. K-FS-1 and K-NOMEM-1 were last changed 2026-07-23. |

**PostReleaseBasis.** All rows say NO, and that is confirmed. Of the four post-v3.0.1 commits, only `da95ec194` touches a cited file that carries relied-upon content (`session-store.ts`). Its hunks are at about lines 3 and 122. The cited content at lines 969-974, 1111-1113 and 1124-1126 blames to `8b3643e6c`. The cited line numbers are correct at the frozen tree. `cb08dbe2f` touches `codex-supervisor.ts`, but rows cite that file only to show the stock Codex child exists. `9ecbdecdf` and `ccb95e06a` touch no cited evidence. The reverse-notes claim that 0 rows change is confirmed.

## (ii) Systematic patterns

1. **Human-only authority is a declared-actor check.** Rows CLM-004.1, CLM-009.2 and CLM-021 are CONTESTED.
   - The sealed ALIGNED rows rely only on the HUMAN-only transition rules (`transition.ts:24-29`).
   - `normalizeActor` maps HUMAN, USER and OPERATOR to HUMAN.
   - `approvalSha` is checked for hex format only.
   - The legacy MCP `status_transition` tool (`read-tools.ts:934-942`, `:1125-1136`) takes the actor string from the caller.
   - That tool has no production importer outside `lib/harness`, so live exposure is limited. This is why the rows are CONTESTED rather than REFUTED.
   - The reverse pass found this correctly. The convention gives no path to carry a reverse-notes correction into the ledger's verdict.
2. **MR-8 is ambiguous when a claim is literally true against a stale snapshot.** Rows CLM-003.2, CLM-015 and CLM-017.2 are CONTESTED. CLM-010.2, CLM-022.1 and REGISTER-2 are CONFIRMED.
   - Several SoW clauses say that `_REFERENCES.md` or the D-APP-38 corpus snapshot records REF-006 as MATCH. That is literally true: corpus v23 pins `8649ccba`.
   - The live PRD, CONTRACT and SPEC bytes differ from those pins.
   - The worker rated CLM-003.2 STALE_SPECIFICATION with HIGH confidence, but rated the equivalent CLM-017.2 LOW. The confidence is inconsistent across equivalent rows.
   - Where a clause flatly says "hash match" (CLM-010.2 for CONTRACT and SPEC), the row is clearly stale.
   - **Suggested rule.** Put a literally-true snapshot claim under REGISTER-n. Reserve STALE_SPECIFICATION for flat present-tense assertions.
3. **Evidence-token and direction discipline slips.**
   - **CONTEXT-only DirectionEvidence.** CLM-008 cites `NOTICE_2026-09-19_APP_LOOP_WORKGRAPH.md` although the worker itself notes the notice is outside RUN_BASIS §5.
   - **MR-10 token.** CLM-009.4 has `DOC-BASIS(D-APP-127)` for invariants that D-APP-127 never touched.
   - **MR-1 token.** CLM-009.11 has STILL CURRENT while its own Disposition is STALE_SPECIFICATION, and the parenthetical citation is wrong.
   - **CONTEXT driving a Disposition.** In CLM-023 the stale reading rests on the Codex re-platform steer. The governing CONTRACT K-PERM-2 and K-PERM-3 still name the permission overlay and hooks. The row is a recommended posture, not a flat state assertion.

**Other observations:**

- **CLM-017.3.**
  - It introduces the token `OTHER:PENDING_HUMAN_GATE`, which should be reported.
  - It applies DOCUMENTED_UNIMPLEMENTED to a pass condition that is conditional and not yet triggered.
- **CLM-025 is CONFIRMED, but its RULING-RECORD evidence is indirect.**
  - The D-APP-56 ruling row P48 is titled "Missing doc artifacts". The dispatch-label resolution links to it only through UPD-159 in the R6 CHANGED_CLAIM_REEXTRACTION file.
  - `Table_Conflict_Source_Warnings_DEL-01-01.md:18`, dated 2026-07-18, still carries C002 as OPEN. That is a further stale surface the ledger did not record.
- **CLM-009.7.** Its VerificationEvidence cites the legacy frontend `session-events.test.ts`, not a Runtime event-schema test.
- **CLM-023.** The cited anchor `delegated.ts:317-329` is actually 316-329. This is minor.
- **Class c (CAP-HARNESS-038, PARTIAL on CLM-009.11).** CONFIRMED. The legacy writer at `session-events.ts:6-11` writes the project-local path that the stale claim names. NOT_MINE is also defensible.

## (iii) Effort

- **Files read:** about 25 files or ranges. These were:
  - the deliverable SoW, `_REFERENCES`, `_STATUS`, `_CONTEXT`, `Dependencies`, INSP-03 and checklist;
  - CONTRACT, SPEC and PRD (by grep);
  - `transition.ts`, `read-tools.ts`, `session-store.ts`, `session-events.ts`, `delegated.ts`, the reliance register and 5 test-name greps;
  - 2 steers, the corpus v21 candidate, the workgraph notice, the D-APP-56 ruling, the R6 re-extraction and the register.
- **Git:** 6 read-only git calls.
- **Context:** comfortable, not tight. Shared evidence (the hashes, K-EVENT-4 and `transition.ts`) covered many rows.
