# DEL-04-05 — forward-pass notes (RUN_D128, R2, PKG-04)

Frozen basis `00115c719`. Ledger `DEL-04-05_claims.csv`: 63 data rows. Validator: 0 errors, 0 warnings.

## 1. Census

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 35 |
| STATE_ASSERTION | 10 |
| CONTEXT_CLAIM | 8 |
| REGISTER_DEFECT | 5 |
| ACCEPTANCE | 4 |
| REMAINING_WORK | 1 |

| Disposition | Rows |
|---|---:|
| STALE_SPECIFICATION | 43 |
| ALIGNED | 6 |
| NOT_AUDITABLE | 6 |
| IMPLEMENTED_DIFFERENTLY | 3 |
| AUTHORITY_CONFLICT | 2 |
| REMAINING_STATE_MISMATCH | 2 |
| PARTIALLY_IMPLEMENTED | 1 |

- Indexed units: 36 (35 CLM + REM-1). Every unit is covered.
- Split rate: 2 of 36 units split (5.6%).
  - CLM-009 has 17 rows, one per numbered requirement RQ-001..017.
  - CLM-022 has 4 rows: VER-001 plus the three numbered HR items.
- Run-local rows: REGISTER-1..5 and STATE-1..3.
- SEE rows, counted separately: 6.
  - CLM-007, CLM-015 and CLM-023 point to CLM-001.
  - CLM-016 points to CLM-008.
  - CLM-019 points to CLM-011.
  - CLM-027 points to CLM-009.2.
- Rows with HumanDecisionNeeded other than NO: 34.
  - R4-Q1: 26 rows.
  - R4: 3 rows.
  - D-APP-127: 3 rows.
  - R4-Q1; R4-Q2: 1 row.
  - D-GOV-43: 1 row.
- Errata: none yet (forward pass only).

## 2. Least-confident rows (LOW)

- **CLM-009.9 (RQ-009, Node/SDK network).** Disposition IMPLEMENTED_DIFFERENTLY. Two other readings are possible:
  - STALE_SPECIFICATION, because the Anthropic bridge wording is compatibility history.
  - ALIGNED, because K-NET-1 as amended makes the Node-side policy explicit, so nothing broadens silently.
- **CLM-009.10 (RQ-010, remote MCP / non-Anthropic network).** Disposition STALE_SPECIFICATION. The alternative is AUTHORITY_CONFLICT:
  - K-NET-1 says remote MCP and remote providers fail closed.
  - D-GOV-43 says the App does not veto the user's Codex configuration.
  - I did not find live enforcement.
- **CLM-009.14 (RQ-014, K-ENGINE-4).** Disposition IMPLEMENTED_DIFFERENTLY. The alternative is AUTHORITY_CONFLICT:
  - K-ENGINE-4 is unamended.
  - K-EVENT-6, as amended for D-GOV-43, keeps upstream Codex notification payloads.
- **CLM-026 (Chirality ownership principle).** Disposition AUTHORITY_CONFLICT. The alternative is IMPLEMENTED_DIFFERENTLY, if D-GOV-43 counts as the "governed change" that DIRECTIVE §0 contemplates.
- **CLM-030 (redact at every boundary).** Disposition ALIGNED. The alternatives are UNKNOWN or PARTIALLY_IMPLEMENTED. I did not trace live structural-redaction coverage; DEL-05-03 owns it.
- **STATE-3 (V3-01 history / MEMORY entry).** Disposition STALE_SPECIFICATION. The alternative is NOT_AUDITABLE, because a dated history entry may be provenance only.

## 3. Register-defect summary

- **REGISTER-1..3.** In `_REFERENCES.md`, REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD all record MATCH.
  - None of the three hashes reproduces at `00115c719` (pack `REFERENCE_HASHES.csv`, Match=NO).
  - These SoW rows restate the stale MATCH:
    - the D-APP-56 note in CLM-001, 007, 015 and 023;
    - CLM-004, CLM-006, CLM-010, CLM-014 and CLM-017;
    - CLM-022.2 and CLM-035.
- **REGISTER-4.** `Dependencies.csv` DEP-04-05-013 is ACTIVE and PENDING.
  - It rests on per-root command-network postures and typed login transport.
  - D-GOV-43 and D-APP-127 retired or reshaped both.
  - The carrier was not revised (pack item 5: `Dependencies.csv` Revised=NO).
- **REGISTER-5.** The DEP-04-05-007 Notes still describe the RQ-011 four-class assertion gap as a gated Remaining item.
  - D-APP-65 closed that gap on 2026-07-18.
  - `_STATUS.md` has no such item.
- Not audited: REF-001, 004, 005, 007, 009 and 010 (DIRECTIVE, TYPES, PLAN and the workflow files). They are outside the pack's recompute scope (see §5).

## 4. Direction and cause

- **Main CauseTags.**
  - CODEX_SOLE_ENGINE: 30 rows.
  - DOC_HYGIENE: 10 rows.
  - A2_TOPOLOGY: 6 rows.
  - PRE_V3_DRIFT: 5 rows.
- **CAUSE2 secondaries.**
  - A2_TOPOLOGY: CLM-003, 008, 009.1, 009.3, 009.9, 009.15.
  - CODEX_SOLE_ENGINE: CLM-005, 009.13, 020.
  - DOC_HYGIENE: CLM-010, 012, 017, 035.
  - CARRIER_PROPAGATION: REM-1, REGISTER-4, CLM-022.4.
  - CREDENTIAL_CUSTODY: CLM-026, STATE-1, STATE-3.
- **Governing direction used.**
  - D-GOV-43: Root `docs/DIRECTIVE.md`, "Codex is the sole engine", plus the "Current Codex-only MVP release basis" preamble in App CONTRACT, PRD and SPEC, lines 13–17.
  - D-APP-127: supersession of per-root consent, of daemon credential custody (D-APP-126) and of the DEL-02-05-V3-03 Root DEL-02-09 gate.
  - No CONTEXT record was needed.
  - The v3 plan (CONTEXT, 2026-08-22) still retained Claude API-key authentication for the RC, so it does not explain the Codex-only divergence.
- **Authority handling.** The pitfall in the brief was applied.
  - Rows that restate SPEC, PRD or CONTRACT are judged by those documents' own Codex-only preamble. They are STALE_SPECIFICATION, not AUTHORITY_CONFLICT.
  - The two AUTHORITY_CONFLICT rows (CLM-024 and CLM-026) rest on App `docs/DIRECTIVE.md` §2.8. That section is unamended: it still names Claude/Anthropic as the key-aware default provider and lists Chirality-owned key, network and event semantics.
  - App DIRECTIVE §0 ranks DIRECTIVE above CONTRACT, SPEC and PRD, so their preambles cannot resolve §2.8.
  - D-GOV-43 undercuts §2.8 without naming it (CONVENTIONS §1).
- **NONE_FOUND searches.** Rows CLM-005, 012, 017, 020, 035 and REGISTER-5 were checked against:
  - `_DECISIONS/_REGISTER.md` rows D-APP-19..127;
  - the ruling records for D-APP-127 and D-APP-65;
  - the RUN_BASIS §5 CONTEXT set (v3 plan text searched for Anthropic/Claude).
  - No record directs leaving the TBDs, stale prerequisites or DEP notes in place.
- **Key live finding (STATE-3, CLM-009.3 and CLM-009.4).** The typed-storage wiring that V3-01 describes is not on the live path at the frozen basis.
  - The App-owned Runtime composition's credential port is a stub: `app-owned-composition.ts:225` returns `{configured:false}` with no source or storage, and set/remove are offline.
  - `SafeStorageCredentialStore` is instantiated nowhere outside tests.
  - The still-registered credential IPC (`main.ts:990`) would return "invalid credential status".
  - The API keys settings section is hidden in the hosted shell.
- **PostReleaseBasis.** NO on every row. The touched files I cited were blamed on their relied-on lines:
  - `app-owned-composition.ts`:180 and :225;
  - `runtime-daemon.ts`:515–522;
  - `client.ts`:656–661;
  - `codex-supervisor.ts`:104–108.
  - None of those lines blames to da95ec194, cb08dbe2f, 9ecbdecdf or ccb95e06a.

## 5. Method friction

- **CLM-003 against CLM-009 (MR-4).** CLM-003's attribute table and CLM-009's requirements overlap, and MR-4 would make the earlier unit (CLM-003) the anchor.
  - I kept CLM-003 as one summary row and dispositioned each numbered RQ in CLM-009 separately. The RQ rows are the numbered items.
  - Proposal: MR-4 should prefer the numbered-item unit as anchor when an earlier unit is an unnumbered summary.
- **Symbol-level reach.** `api-key-storage.ts` is LIVE at module level only because `api-key-ipc.ts` imports `isProviderCredentialId`.
  - I tagged `SafeStorageCredentialStore` `REACH=LEGACY_ONLY` with UNREACHED in Notes (Addendum 1 item 4).
  - Proposal: allow an explicit symbol qualifier in ImplementationEvidence.
- **Authority order across Root and App.** App DIRECTIVE §0 orders only App documents, so the Root D-GOV-43 rule and the App DIRECTIVE §2.8 clause have no stated precedence.
  - Suggest R4 frame this as a named question alongside R4-Q1.
- **Reference hashes.** The pack recomputes only CONTRACT, SPEC and PRD.
  - The other `_REFERENCES.md` MATCH rows (DIRECTIVE, TYPES, PLAN and the workflow files) went unchecked.
  - Proposal: extend the pack item 3 scope.
- **Gate transcript.** The App gate transcript lists only totals (222 files passed), not per-file results.
  - Test-file citations rely on the file existing and on the whole suite passing.

## 6. Effort

- About 30 file reads or greps, covering:
  - the deliverable files (SoW, _STATUS, _CONTEXT, _REFERENCES, MEMORY, Dependencies.csv, INSP-03, V3-01 evidence);
  - the governing preambles, K-NET-1/K-KEY-1, SPEC 12/16 and DIRECTIVE §0/§2.8;
  - the D-APP-127 record;
  - main.ts, api-key-storage.ts/ipc.ts, the legacy managers, app-owned-composition.ts, runtime-daemon.ts, codex-supervisor.ts and the test listings.
- The context budget was comfortable. I did not read `_SEMANTIC*.md`, `_DEPENDENCIES.md` or `_run_records/`.
