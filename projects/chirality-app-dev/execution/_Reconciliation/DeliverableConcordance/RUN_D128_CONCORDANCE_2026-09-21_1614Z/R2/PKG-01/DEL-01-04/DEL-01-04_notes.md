# DEL-01-04 Scope Boundary and Retired Scope Register: forward-pass notes (R2, PKG-01)

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`. Frozen basis `00115c719`. Forward pass only; the ledger
`DEL-01-04_claims.csv` is sealed once its SHA-256 is returned.

## 1. Census

- **Rows:** 67. That is 28 indexed units (all CLM; no REM or REMTXT units), 3 `REGISTER-n` rows and 4 `STATE-n` rows.
- **Split rate:** 7 of 28 units were split (25%). The splits are CLM-003 (8), CLM-004 (6), CLM-006 (7), CLM-007 (3), CLM-010 (11), CLM-013 (2, AC-001) and CLM-020 (2, VER-001).
  - CLM-010 was split one row per REQ item (REQ-001..REQ-011).
  - CLM-003, CLM-004, CLM-006 and CLM-007 are tables of rows that can each take their own disposition.
  - CLM-024 and CLM-025 are tables too, but each was kept as one row, because splitting them would only add SEE rows.
  - The validator's `SubItems` check (AC-001 and VER-001) is met.
- **SEE rows (counted separately):** 17. They are CLM-004.1, 006.1–006.4, 007.2, 010.2, 010.4, 010.5, 010.7, 010.8, 011, 018 and 028, plus STATE-1, STATE-3 and STATE-4.
- **Rows by Disposition:**

| Disposition | All rows | Of which SEE |
|---|---:|---:|
| ALIGNED | 22 | 5 |
| STALE_SPECIFICATION | 15 | 7 |
| NOT_AUDITABLE | 13 | 0 |
| AUTHORITY_CONFLICT | 12 | 5 |
| PARTIALLY_IMPLEMENTED | 4 | 0 |
| REMAINING_STATE_MISMATCH | 1 | 0 |

- **Rows by ClaimType and Disposition:**
  - REQUIREMENT (20): 13 ALIGNED, 5 AUTHORITY_CONFLICT, 2 PARTIALLY_IMPLEMENTED.
  - CONTEXT_CLAIM (18): 13 NOT_AUDITABLE, 5 STALE_SPECIFICATION.
  - EXCLUSION (12): 5 ALIGNED, 5 AUTHORITY_CONFLICT, 1 PARTIALLY_IMPLEMENTED, 1 STALE_SPECIFICATION.
  - STATE_ASSERTION (9): 6 STALE_SPECIFICATION, 2 AUTHORITY_CONFLICT, 1 ALIGNED.
  - ACCEPTANCE (5): 3 ALIGNED, 1 PARTIALLY_IMPLEMENTED, 1 STALE_SPECIFICATION.
  - REGISTER_DEFECT (3): 2 STALE_SPECIFICATION, 1 REMAINING_STATE_MISMATCH.
- **HumanDecisionNeeded:**
  - `NO`: 52.
  - `R4; R4-Q1`: 8 (CLM-003.5, 006.2, 010.4, 024, 025; REGISTER-3; STATE-2, STATE-4).
  - `R4`: 6 (CLM-003.1, 003.4, 004.5, 006.1, 010.2, 023).
  - `R4-Q1`: 1 (CLM-006.5).
- **Confidence:** 46 HIGH, 21 MEDIUM, 0 LOW.
- **No errata:** this is the sealed pass-1 figure.
- **Validator:** `RESULT PASS errors=0 warnings=0`.

## 2. Least-confident rows (with the alternative reading)

No row is LOW. These are the MEDIUM rows most open to a different verdict:

- **CLM-003.4 / 006.1 / 010.2 (remote MCP and plugins → AUTHORITY_CONFLICT).**
  - Alternative reading: D-GOV-43 item 3 shares only the user's own configuration. Remote MCP would still "fail closed" as K-NET-1 says, because the product ships no remote MCP of its own. On that reading the rows are ALIGNED or PARTIALLY_IMPLEMENTED (no live control stops a user-configured remote server).
  - Why the conflict route was chosen: D-GOV-43 finding 2 deliberately retires the empty-`mcp_servers`/`plugins` veto. DIRECTIVE §4.2 forbids exposing plugins. That is a ruling undercutting an unamended clause without naming it.
- **CLM-003.5 / 006.2 / 010.4 / 024 / 025 (shipped bypass → AUTHORITY_CONFLICT).**
  - Alternative reading: Codex "Full access" is not `bypassPermissions`, which is a Claude-SDK term. K-PERM-6 would then be moot for the Codex engine (ACCEPTED_DIVERGENCE under D-GOV-43 item 4).
  - Why the conflict route was chosen: the App's own permission mode is literally `bypass`. D-GOV-43 item 4 says Chirality permissionMode maps onto the Codex settings. K-PERM-6, DIRECTIVE §4.2 and PRD §3.2/§6.4 stay unamended, and item 4 does not name them.
- **STATE-2 / STATE-4 (Claude as the current path → AUTHORITY_CONFLICT).**
  - Alternative reading: apply DIRECTIVE §0 as written. DIRECTIVE §2.8 (Claude key-aware default) outranks the Codex-only CONTRACT/PRD preambles. On that reading the text is ALIGNED with the higher source and the code is nonconforming.
  - Why the conflict route was chosen: a ruling (D-GOV-43, which keeps the Codex sole-engine rule) exists outside the §0 order and does not name §2.8. The brief's authority note was followed in not letting the lower preambles override §2.8.
- **CLM-006.5 (BR-005 domain carve-in → PARTIALLY_IMPLEMENTED, R4-Q1).**
  - Alternative reading: "in scope" is a permission, not an obligation. The row then says nothing false, so ALIGNED (recorded as `ALSO_MODULE:ALIGNED`).
- **CLM-009 (Scope → ALIGNED).**
  - Alternative reading: the in-scope bullets "record that ... forbidden by product invariants" are product-behaviour claims. By subject-test rule 2 that would make the row AUTHORITY_CONFLICT, like CLM-003.5.
  - Why ALIGNED was chosen: the bullets describe the register's own recording duty.
- **CLM-026 (Examples → STALE_SPECIFICATION).**
  - Alternative reading: the example is conditional ("if aligned with runtime contract"), so NOT_AUDITABLE.
- **REGISTER-3 (DEP-01-04-010 SATISFIED → STALE_SPECIFICATION).**
  - Alternative reading: the row is a dated D-APP-53 snapshot, which MR-8(iv) would leave standing. Whether the constraint still binds turns on the CLM-003.5 conflict.
- **CLM-005 and CLM-020.2 (PARTIALLY_IMPLEMENTED).**
  - Alternative reading: CLM-005's families are labelled ASSUMPTION, so NOT_AUDITABLE. For CLM-020.2, VER-001 is only a method statement.

## 3. Register-defect summary

- **REGISTER-1: `_REFERENCES.md` hashes (STALE_SPECIFICATION).**
  - REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD are recorded as MATCH but do not reproduce (`REFERENCE_HASHES.csv`). REF-001, REF-004 and REF-005 do reproduce.
  - The D-GOV-43 application tranche `23b3879b3` re-hashed this file (corpus v23). Three later 2026-09-12 commits (`95b342519`, `9eaddb596`, `7f1e9f387`) edited CONTRACT, SPEC and PRD without a re-hash.
  - Restated by CLM-004.1, 007.2, 011, 016, 018 and 027, and by STATE-3 (the checklist doc).
  - REF-007, REF-009 and REF-010 point to Root `workflows/software-decomp/**` and were not recomputed (reading bound).
- **REGISTER-2: `_STATUS.md` `Last Updated` (REMAINING_STATE_MISMATCH).** It says 2026-07-12; the last History entry is 2026-07-19.
- **REGISTER-3: `Dependencies.csv` DEP-01-04-010 (STALE_SPECIFICATION, R4; R4-Q1).**
  - The row is SATISFIED on the basis of the LEGACY_ONLY `sdk-options-builder.ts`. Meanwhile the live composer ships ungated Full access.
  - `_DEPENDENCIES.md` line 35 and its Lifecycle Summary repeat the same 2026-07-10 basis.
- **Other stale carrier text (STATE and SoW rows):**
  - The CLM-006 preamble and CLM-028 say human ruling fields "remain TBD"; D-APP-56 rulings are now recorded.
  - CLM-016 says "none extracted yet"; 13 dependency rows exist.
  - SoW REF-007 points to a deleted agent file through a machine-specific absolute path.
  - `_CONTEXT.md` says Pi is corpus-only (STATE-1) and that Claude is the current path (STATE-2).

## 4. Direction and cause

- **Primary CauseTags:**
  - CODEX_SOLE_ENGINE 8: bypass rows, the BR-005 carve-in, STATE-2/4, REGISTER-3.
  - DOC_HYGIENE 8: hash restatements, REF-007, `_STATUS`.
  - PRE_V3_DRIFT 7: the D-APP-56 and D-APP-72 era drift in BR-006, the preamble, CLM-016, CLM-026, CLM-005, STATE-1.
  - A2_TOPOLOGY 6: the remote MCP/plugin conflict and principle 4.
  - CARRIER_PROPAGATION 2.
  - LIFECYCLE_GATE_PENDING 1.
- **`CAUSE2:` secondaries:**
  - CARRIER_PROPAGATION on most D-GOV-43 rows. The D-APP-127 application map shows every DEL-01-04 carrier as `NO`. The tranche touched `_REFERENCES.md` only, and only to re-hash it.
  - CODEX_SOLE_ENGINE on the Pi rows and on CLM-023/024.
  - A2_TOPOLOGY on REGISTER-1 and CLM-026.
  - DOC_HYGIENE on CLM-027.
- **Governing records cited (`GOV:`):**
  - D-GOV-43 items 1, 3, 4, 7–8, 13 and 14, and finding 2. Source: the Root `_PROPOSALS/D-GOV-43_…/D-GOV-43.proposed.md`, accepted as revision 3.
  - D-APP-127.
  - D-APP-72 / SCA-APP-002.
  - D-APP-56 R4-P22, R4-P25 and R4-P45.
- **CONTEXT records:** none used. No CONTEXT source was needed or used to explain a divergence.
- **Searches behind each `NONE_FOUND`:**
  - `execution/_Coordination/_DECISIONS/_REGISTER.md`, searched for DEL-01-04, SOW-065/076/077/078, bypass, plugin, PKG-08, K-RETIRED-1 and re-snapshot rulings.
  - The D-APP-127 ruling, grepped for MCP, plugin, permission, approval, sandbox, Windows and notarization: no hits.
  - The deliverable's 12 `_run_records`, and grep of the folder for parity, claim map and VER-001.
- **Authority routes on governance-invariant rows (per the brief):**
  - **Conflict route** (a ruling undercuts an unamended clause without naming it): CLM-003.1, 003.4, 003.5, 023, 024, 025 and STATE-2 (with their SEE rows).
  - **MR-11 route** (the ruling names the clause): CLM-006.6 (D-APP-72 names the D-APP-01/02 prohibition).
  - **No conflict:** CLM-003.7 (K-RELEASE-1 is read with D-GOV-43 item 1 by the amended preambles; platforms unchanged) and CLM-004.3.
  - **DIRECTIVE §0 order route:** considered on STATE-2 but not sufficient, because the ruling lies outside the order.

## 5. Method friction

- **DIRECTIVE §0 does not place D-GOV rulings.** Its order ranks only App documents, so every Codex-era conflict with the unamended DIRECTIVE falls to the conflict route. Proposed revision: say where Root D-GOV rulings sit relative to DIRECTIVE §0, or frame one R4 question ("do D-GOV-43 items 3–4 and the Codex sole-engine rule amend DIRECTIVE §2.8/§4.2 and K-PERM-6?"). Many PKG-01 rows would then cite a named `R4-Qn` rather than plain `R4`.
- **Negative (exclusion) claims met by absence on LIVE.** The ImplementationEvidence rule expects code. I used `NONE_FOUND` search statements (CLM-003.6) or LIVE code showing the absence (CLM-010.3). A convention for exclusion rows would help.
- **Split rule for guidance tables.** CLM-024 and CLM-025 are tables, but splitting them yields only SEE rows. Proposed: allow a whole-table row whose Notes name the rows that diverge.
- **REF-007/009/010.** They point to Root workflow files. Hashing them was outside this worker's reading bound, so they were left unverified.

## 6. Effort

- **Files read:** about 30. That covers the deliverable carriers, the INSP-03 assessment, three run records, and App DIRECTIVE, CONTRACT and PRD slices. Also D-GOV-43's proposed items and findings, the D-APP-56 ruling slice, and the D-APP-127 headings.
- **Code:** effective home, app-server client, supervisor, electron main, chat-panel, delegated contracts, sdk-options-builder, domain tools and package.json.
- **Other inputs:** the evidence pack, the claim index and git log/show/blame.
- **Context budget:** comfortable.

## Coverage gaps

- **Post-release Runtime application-owned dynamic tools** (`da95ec194`, 2026-09-19).
  - Files: `projects/chirality-runtime/packages/daemon/src/application-tools.ts`, `projects/chirality-runtime/packages/contracts/src/application-tools.ts` and `projects/chirality-runtime/docs/APPLICATION_TOOLS.md`.
  - What it is: a host-only API that lets an authenticated owning application register tools for Codex conversations. The first intended consumer is SWBPIPE, a piping domain application.
  - It is LIVE in the packaged runtime-service module graph but has no App caller.
  - The boundary register does not address it. It bears on SOW-065 ("plugin-like extension points", FR-105) and BR-005 (domain-engine integration). No forward row owns it; the owner is unclear (DEL-01-04 boundary versus a PKG-10 or Runtime deliverable).
- **User Codex configuration shared by reference** (D-GOV-43 item 3). This covers model providers, MCP servers, plugins, skills and hooks. It is the Codex-era counterpart of the SOW-076 "ambient settings" boundary. The register has no row for it; it is touched only on CLM-010.3 and CLM-023.
- **No cross-deliverable repair was made.** `docs/BOUNDARY_REVIEW_CHECKLISTS.md` is shared with DEL-01-03. Its stale MATCH and Anthropic-default text is recorded here as STATE-3 and STATE-4 for DEL-01-04's use of it.
