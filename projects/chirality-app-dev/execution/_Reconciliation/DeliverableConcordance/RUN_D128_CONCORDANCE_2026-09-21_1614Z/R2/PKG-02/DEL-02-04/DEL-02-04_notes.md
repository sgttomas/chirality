# DEL-02-04 forward notes (RUN_D128, R2 PKG-02)

Forward pass by a TASK worker. Reading basis: the frozen tree at `00115c719`. This file is evidence, not a ruling.

## 1. Census

- **Rows:** 74, covering 37 indexed units plus 7 `REGISTER-n` rows. There are no `STATE-n` rows.
- **Split rate:** 6 of 37 units are split (16%).
  - `CLM-003` into 7 rows, `CLM-004` into 6 and `CLM-005` into 5. Each is a table whose rows get independent dispositions.
  - `CLM-010` into 14 rows, one per item REQ-001..014.
  - `CLM-015` into 2 rows: the repeated note, and AC-001.
  - `CLM-021` into 2 rows: the Records list, and VER-001.
  - The SubItems items AC-001 and VER-001 each have their own row.
- **SEE rows (counted separately):** 19.
  - 6 point to `REGISTER-3`, the PRD hash row.
  - 13 point to earlier indexed units.
  - Rows that are not SEE rows: 55.

Disposition by ClaimType:

| ClaimType | ALIGNED | STALE_SPEC | PART_IMPL | IMPL_DIFF | DOC_UNIMPL | RSM | UNKNOWN | NOT_AUDITABLE | Total |
|---|---|---|---|---|---|---|---|---|---|
| REQUIREMENT | 18 | 6 | 5 | 4 | 3 | 0 | 1 | 0 | 37 |
| ACCEPTANCE | 3 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 6 |
| STATE_ASSERTION | 1 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| CONTEXT_CLAIM | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 10 | 13 |
| REMAINING_WORK | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 |
| REGISTER_DEFECT | 0 | 6 | 0 | 0 | 0 | 1 | 0 | 0 | 7 |
| **Total** | 23 | 23 | 7 | 4 | 3 | 2 | 2 | 10 | 74 |

- **HumanDecisionNeeded:** `NO` on 68 rows and `R4-Q1` on 6 rows.
  - The R4-Q1 rows are CLM-003.4, CLM-005.5, CLM-010.12, CLM-012, CLM-020 and CLM-024.
  - On each, the only code that warns on unknown option keys is the `LEGACY_ONLY` module `frontend/src/lib/harness/options.ts`. Addendum 6 rule 3 applies.
  - Every one of these rows also records `ALSO_MODULE:ALIGNED`.
- **Other R4 questions:** no row turns on R4-Q2..Q5.
- **Errata:** none yet, because the reverse pass has not run.

## 2. Least-confident rows

- **`CLM-010.14` (REQ-014, dense-but-readable UI): `UNKNOWN`.**
  - The last recorded visual evidence is the D123 screenshot inspection of 2026-09-07. The UI was refined again on 2026-09-12.
  - Alternative readings:
    - `ALIGNED`, if later App v3 browser evidence is accepted;
    - `PARTIALLY_IMPLEMENTED`, given the disclosed clipping of the narrow right-tab label.
- **`CLM-021.2` (VER-001, SoW-conversion verification): `UNKNOWN`.**
  - No record in the deliverable folder. The SoW was finalized in commit `22146b9e7`.
  - Alternative readings:
    - `ALIGNED`, if the conversion run's evidence exists outside the folder;
    - `DOCUMENTED_UNIMPLEMENTED`, if no such record exists.
- **`REGISTER-7` (DEP-02-04-021 names a "Root-owned daemon session record"): `STALE_SPECIFICATION`, LOW.**
  - Alternative reading: "daemon" is still a valid name, because `packages/daemon` exists and hosts the Codex supervisor. On that reading the row is not false and would be `ALIGNED`.

## 3. Register-defect summary

- **REGISTER-1..3.** In `_REFERENCES.md`:
  - The MATCH verdicts for CONTRACT (REF-002), SPEC (REF-003) and PRD (REF-006) do not reproduce at `00115c719`. The pack's `REFERENCE_HASHES.csv` shows all three as `NO`.
  - Recomputed by this worker: DIRECTIVE, TYPES, PLAN and the three `workflows/software-decomp` files still match.
  - SoW rows that restate PRD "reconciled/MATCH" as current are STALE_SPECIFICATION with `SEE:REGISTER-3`: CLM-004.6, CLM-011, CLM-018, CLM-025 and CLM-028.
- **REGISTER-4.** RefIDs REF-009 and REF-010 are each used twice in `_REFERENCES.md`. The corpus table and the SCA-APP-004/010 tables both use them.
- **REGISTER-5.** These dependency records still claim hash matches:
  - `Dependencies.csv` DEP-02-04-008/009/012 (`ProposedMaturity AVAILABLE_LOCAL_HASH_MATCH`; DEP-012 Notes "REF-006 MATCH");
  - `_DEPENDENCIES.md:154` ("all … report MATCH").
  - SATISFIED at the required maturity `AVAILABLE_LOCAL` remains true.
- **REGISTER-6.** The summary at `_DEPENDENCIES.md:145-153` lags `Dependencies.csv`:
  - it says DEP-016 is PENDING, but the CSV says SATISFIED;
  - its counts are 8/6, but the CSV gives 9/5;
  - handover rows DEP-017..019 stay PENDING although the additive fields are on main.
  - Disposition: REMAINING_STATE_MISMATCH, under tie-break rule 2(b).
- **REGISTER-7.** DEP-02-04-021 targets a "Root-owned daemon session record". Under D-GOV-43/A2, the session record lives in the App-owned Runtime service. The D-APP-127 carrier map shows `Dependencies.csv` with `Revised=NO`.

## 4. Direction and cause

- **CauseTag counts (non-NONE):**
  - `DOC_HYGIENE`: 12;
  - `SHELL_REDESIGN`: 10;
  - `CODEX_SOLE_ENGINE`: 10;
  - `PRE_V3_DRIFT`: 5;
  - `CARRIER_PROPAGATION`: 2;
  - `LIFECYCLE_GATE_PENDING`: 1;
  - `A2_TOPOLOGY`: 1.
- **CAUSE2 secondaries:**
  - DOC_HYGIENE ×4;
  - CARRIER_PROPAGATION ×3;
  - LIFECYCLE_GATE_PENDING ×2 (the producers of chat-rung and reference chips are items of other deliverables that have not landed);
  - SHELL_REDESIGN ×2;
  - CODEX_SOLE_ENGINE ×2;
  - PRE_V3_DRIFT ×1.
- **Main findings:**
  1. **Toolkit UI is off the product path** (SHELL_REDESIGN).
     - `OperatorToolkitPanel` is rendered only inside `AppShell > WorkspaceSidebar`, whose only page caller is `app/not-found.tsx`.
     - Every product route renders `WovenDialogueShell` (`woven-dialogue-route.tsx:18` voids the legacy element).
     - The persisted toolkit values (tools, maxTurns, subagentGovernance) still flow into turn `opts` from `chat-panel.tsx:320,830,1514`. On the live route the user cannot see or edit them.
     - Model/effort and permission/interaction mode moved to the composer. Persona is set in the persona picker.
  2. **The Codex path does not consume tools/maxTurns** (CODEX_SOLE_ENGINE).
     - `delegated-engine-adapter.ts:203-207` forwards only model, reasoning effort and permission mode.
     - Fallback is deterministic but is not the PRD FR-023 chain. The PRD's Codex-only preamble demotes default-provider rules, so no AUTHORITY_CONFLICT was raised.
  3. **Unknown option keys are dropped silently on the live path.**
     - `turn-coordinator.ts:180-187` rebuilds `opts` from known keys only.
     - SPEC §13.1 (`SPEC.md:780`) requires a warning.
     - Only the legacy `options.ts` warns, hence R4-Q1.
  4. **Several fields are stored but have no producer on the live path.**
     - The workspace-state fields `contextReferences`, `focusedArtifact`, `dialogueAnchorId` and `chatRung` (with `declined`) are sanitized and persisted.
     - No product component writes them.
     - Explicit context rides on composer attachments. Per-chat documents use `openDocumentPath`/`chatDocuments`.
     - Visible artifacts never become model context: `ChatPanel` receives no document path.
  5. **DEL-02-04-V3-01 looks done in code but is still open in Remaining** (REM-2, REMAINING_STATE_MISMATCH).
     - On main: the strip, the right-panel Activity view, the `primarySessionId` caller (D-APP-123 effect now observable) and the additive fields with migration tests.
     - The gate DEL-02-02-V3-03 has landed (`DEL-02-02 _STATUS.md:52`), so MechanicallyUnblocked is `YES`.
     - Residuals: the retired `ActivityShelf` export is unrendered, and the chat-rung fields have no producer.
- **CONTEXT/GOV records used:**
  - `GOV:D-APP-108` (SCA-APP-010 seating; Q2 quote-as-attachment);
  - `GOV:D-APP-109`;
  - `GOV:D-APP-56` (R4-P07: mode and persona moved out of Toolkit);
  - `GOV:D-APP-127` (Codex sole engine; A2 topology);
  - `GOV:SCA-APP-004` Gate-5 (REF-008).
- **Searches behind each `NONE_FOUND`:**
  - `_REGISTER.md` rows D-APP-38/56/108/109/110/123/127, plus grep of `_REGISTER.md` for "toolkit" and "unknown opt". Neither grep found a hit.
  - grep for "toolkit" across the CONTEXT AgentRuns `APP_V3_*`, `APPDEV_V3_NODE_*`, `CHIRALITY_V3_APP_ADOPTION_20260909`, the v3 steers and the final release plan. The hits were deliverable-record copies and CSS only; none gave direction to retire the Toolkit panel or drop unknown-key warnings.
- **PostReleaseBasis:**
  - The only cited file on `TOUCHED_PATHS.csv` is `packages/daemon/src/codex-supervisor.ts`.
  - `git blame -L 104,112` shows `95364569ae`/`1cb09c09da`, so the value is `NO`.
  - Line 219 blames to `da95ec194`. It was deliberately not relied on.
  - All rows are `NO`.

## 5. Method friction

- **Duplicate RefIDs (REGISTER-4).** Neither register-defect verdict fits well:
  - the defect is an identity collision, not a now-false fact or lagging metadata;
  - `STALE_SPECIFICATION` was used, at MEDIUM.
  - Proposal: allow `REGISTER_DEFECT` rows a `DOC_HYGIENE`-only defect class, or name a verdict for structural register errors.
- **Legacy CLM clauses under an SoW that says "SCA-APP-010 controls".**
  - The SoW's own Gate-5 section declares that earlier clauses are "dated compatibility history". That is deliverable text, not a ruling that names them retired, so `RETIRED_BY_RULING` was not used.
  - Superseded pane and Toolkit wording was dispositioned `STALE_SPECIFICATION`, with GOV:D-APP-108.
  - Proposal: state whether an applied SCA section that preserves earlier clauses as history counts as the GOVERNING ruling for `RETIRED_BY_RULING`.
- **SEE across split rows.** SEE requires the same Disposition. Mixed units (CLM-005.5, CLM-020) therefore point to the closest same-verdict row, and the differing facet is recorded in Notes.
- **SubItems parsing.** `CLM-010` holds 14 REQ items but has an empty `SubItems` cell; the parser appears to catch only bold bullet IDs. The rows were split anyway, under the table rule.

### Coverage gaps (for R3)

- **`_SEMANTIC.md`, `_SEMANTIC_LENSING.md` and `MEMORY.md`** are declared-state files with no indexed units.
  - They were not audited row by row. `MEMORY.md` was read.
  - Its 2026-09-06 and 2026-09-07 entries say the D123 strip is "held". They are dated, and the code now shows the caller landed.
- **Scope with no owning unit:**
  - ownership of SPEC §13.1 unknown-key warnings on the Codex Runtime path (Runtime-owned; DEP-02-04-014 still `TBD`);
  - the co-carrier of SOW-016 (DEL-04-02 per the DEP-014 PROPOSAL).
  - Neither has an indexed DEL-02-04 unit beyond the restated requirements.
- **Stored fields with no producer.** DEL-02-04 owns the fields; the producers belong to DEL-02-02-V3-04 (rung) and DEL-02-03-V3-02 (context chips/quote).
  - `chatRung`/`declined`: producer DEL-02-02-V3-04.
  - `contextReferences`/`focusedArtifact`/`dialogueAnchorId`: producer DEL-02-03-V3-02.

## 6. Effort

- **Files read:** about 30, as focused reads and greps.
  - Deliverable files: SoW, `_STATUS`, `_CONTEXT`, `_REFERENCES`, `MEMORY`, `Dependencies.csv` (by script) and the INSP-03 assessment.
  - Parts of `_DEPENDENCIES.md`.
  - Pack items 1–5.
  - Gate transcripts.
  - Register rows.
  - PRD/SPEC/CONTRACT anchors.
  - About 15 frontend and runtime source and test files.
- **Git:** a few read-only `git log` and `git blame -L` calls against the frozen tree.
- **Context budget:** moderate, not tight.
