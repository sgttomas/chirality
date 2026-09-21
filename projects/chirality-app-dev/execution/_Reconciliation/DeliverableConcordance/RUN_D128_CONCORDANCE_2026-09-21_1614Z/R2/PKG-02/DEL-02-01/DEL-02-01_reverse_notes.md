# DEL-02-01 reverse-pass notes (whole merged deliverable)

- Run: RUN_D128_CONCORDANCE_2026-09-21_1614Z, R2 PKG-02. Worker: the half-A TASK, resumed for the reverse pass over the merged ledger.
- Input: `REVERSE_INPUT_capabilities.csv`, 307 rows across seven areas: BUILD 41, ELECTRON 35, HARNESS 60, ROUTES 44, SHELL 45, WORKSPACE 39, WOVEN 43.
- Content source: the capability descriptions and REACH/STATE notes in that file.
- Ledger of record: `DEL-02-01_claims.csv`, 78 rows. Its SHA-256 `5cf0d262…6772f360` is unchanged, and the half-A sealed SHA `5282a7a8…6e419` is unchanged.

## 1. Responses

| Response | Rows |
|---|---:|
| CLAIMED_BY | 20 |
| PARTIAL | 35 |
| NOT_MINE | 252 |

Validator result: `RULES errors none | warnings none`, `RESULT PASS errors=0 warnings=0`.

Claimed or partial rows, by area:

| Area | CLAIMED_BY / PARTIAL rows | What they are |
|---|---:|---|
| WOVEN | 30 | Shell frame, primary dialogue, navigator organisation, read-only replay, activity strip, legacy/Work projection gaps |
| SHELL | 12 | Headerless frame, context line, folder select, role picker, legacy loop shells and header |
| ROUTES | 6 | Page routes, the not-found header, the layout (REM-1) and Stone tokens (REM-4) |
| WORKSPACE | 7 | Role directory, retired matrix helpers, route keys, coming-soon options |
| ELECTRON | 2 | Folder conveniences and the native picker (SEC-4 Q9) |
| BUILD | 1 | macOS icon regeneration (REM-7) |
| HARNESS | 0 | — |

- **NOT_MINE rows** are API routes, turn and session mechanics, settings and updates, and right-panel files, workflows and plans. They also include Electron security and packaging, build and supply chain, and the harness client and legacy runtime.
- **Why they are NOT_MINE:** SEC-1 limits DEL-02-01 to shell integration and presentation. The adjacent owners are named in the SoW and in `Dependencies.csv`: DEL-02-02 for the right panel, DEL-02-03 for files, DEL-02-04 for local state, DEL-02-05 for account presentation, DEL-07-01 for validation, and DEL-08-02/03 for routing and Pipeline.
- **HARNESS:** DEL-02-01 consumes the redaction helper (Q6) but does not own it, so it is NOT_MINE.

## 2. Errata

None. Nothing in the capability descriptions contradicts a forward row, in either half. Several capabilities confirm forward findings:

- CAP-WOVEN-002: `legacyHref` is not rendered.
- CAP-WOVEN-035: ActivityShelf is DISABLED.
- CAP-WOVEN-041: the Work projection is TEST_ONLY.
- CAP-WOVEN-039: session-to-surface attribution is DISABLED.
- CAP-SHELL-001/002 and CAP-ROUTES-043: the legacy shells are DISABLED.
- CAP-WORKSPACE-035: the role directory is DISABLED.

## 3. Cross-half consistency (for R3; not errata)

The same verdict is split across the two halves. The halves agree on the evidence and differ only in the reading.

- **Matrix shape and vocabulary.** Half A (CLM-010.4/.5/.6) reads PRD FR-007 and SEC-2 ob.2 as keeping the legacy matrix as compatibility. Half B (CLM-020.3/.4/.5) reads TYPES §4 as no longer requiring a visual matrix. Half B records the R4-Q4 reading as its own alternative.

  | Rows | Disposition | HumanDecisionNeeded |
  |---|---|---|
  | Half A: CLM-010.4 | IMPLEMENTED_DIFFERENTLY | R4-Q4 |
  | Half A: CLM-010.5, CLM-010.6 | DOCUMENTED_UNIMPLEMENTED | R4-Q4 |
  | Half B: CLM-020.3, CLM-020.4, CLM-020.5 | ACCEPTED_DIVERGENCE | NO |

  Suggestion: R3 should cluster these six rows under one R4-Q4 disposition.
- **CLM-010.10 (REQ-010) vs CLM-020.8.** Half A: IMPLEMENTED_DIFFERENTLY + R4-Q4, LOW. Half B: ACCEPTED_DIVERGENCE. Same subject.
- **CLM-010.1 (REQ-001) vs CLM-020.1 and CLM-017/025.** Half A: IMPLEMENTED_DIFFERENTLY + R4-Q4, because SCA-APP-010 ob.5 keeps the loop-first UI as a compatibility surface. Half B: ACCEPTED_DIVERGENCE (CLM-020.1, CLM-025) and ACCEPTED_DIVERGENCE + R4-Q4 (CLM-017).
- **UPD-106.** CLM-007/014 (half A) and CLM-023.1 (half B) are both STALE_SPECIFICATION, so they are consistent. Half B's evidence (`_STATUS.md` L71, `MEMORY.md` L9: the final code tranche implemented UPD-106) confirms that CLM-023's "withheld" is the stale copy. My CLM-007 row stands on product behaviour: the header row is gone.
- **CauseTag.** Both halves independently chose `OTHER:V3_ROLE_ADOPTION` and proposed adding `V3_ROLE_ADOPTION` to the vocabulary.

## 4. Coverage gaps (missing forward rows)

1. **Runtime connectivity indicator and reconnect control** (CAP-SHELL-010, CAP-SHELL-011, and the reconnect in CAP-WOVEN-034).
   - `_STATUS.md` History (2026-07-25, 2026-08-15) records this as DEL-02-01 work.
   - No SoW unit or `## Remaining` item claims it, so there is no forward row.
   - It is now rendered through the woven activity strip.
   - Answered NOT_MINE for CAP-SHELL-010/011. R3 should decide whether DEL-02-01 or DEL-02-05 owns it.
2. **Theme control / light-dark-system** (CAP-SHELL-018, CAP-WOVEN-038). REM-4 covers only the Stone tokens. No DEL-02-01 unit covers theme choice; it is likely DEL-02-04's, so it was answered NOT_MINE.
3. **Chat continuity across launches** (CAP-WOVEN-017) and **new chat / resume** (CAP-SHELL-031). These are shell behaviour with no DEL-02-01 unit; they are partly DEL-02-04 state. Answered NOT_MINE.
4. **Carried from the half-A forward notes:**
   - The SoW OUT-001 purpose line and the SCA section preambles are not indexed units. No false fact was found in them.
   - Decomposition L307 "delegation, rung" is governing text and needs an R4-Q4 consequence note rather than a key.
5. **Carried from the half-B forward notes:**
   - SCA-APP-010 ob.5 is not met. It is covered by half A's SEC-4 row.
   - The legacy matrix route/query handler belongs to DEL-08-02 (DEP-02-01-006).
   - The DEP-02-01-013 icon handoff to DEL-09-04 was never produced, while b2b32669c changed `build/icon-macos.svg` and `icon.icns`. CAP-BUILD-037 is answered PARTIAL on REM-7.

## 5. Method

- One scripted pass mapped the capability IDs to ClaimKeys. Each CLAIMED_BY/PARTIAL row was checked against the forward row's evidence paths and the capability's REACH/STATE note.
- Unmatched rows were NOT_MINE, with a rationale per area.
- No new code was read beyond the capability descriptions.
- Half B's ledger rows and notes were read only after the manager's message.
