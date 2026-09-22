# DEL-02-05 — forward-pass notes (RUN_D128 R2, PKG-02)

Worker: TASK (Type 2), forward pass. Basis: frozen tree at `00115c719`. The R0 calibration
ledger for this deliverable was not read. PREGATHER.md served only as a locator; every cited
path was re-opened at the frozen tree.

## 1. Census

- **Rows:** 73 (32 indexed units: 3 SEC, 28 CLM, 1 REM; plus 5 REGISTER rows and 1 STATE row).
- **By ClaimType:** REQUIREMENT 39, CONTEXT_CLAIM 14, STATE_ASSERTION 8, ACCEPTANCE 6,
  REGISTER_DEFECT 5, REMAINING_WORK 1.
- **By Disposition:** STALE_SPECIFICATION 26, AUTHORITY_CONFLICT 15, ALIGNED 10,
  NOT_AUDITABLE 8, PARTIALLY_IMPLEMENTED 7, IMPLEMENTED_DIFFERENTLY 5,
  DOCUMENTED_UNIMPLEMENTED 1, REMAINING_STATE_MISMATCH 1.
- **Split rate:** 9 of 32 indexed units split (28%), giving 44 sub-rows:
  - SEC-2: 5 numbered obligations;
  - CLM-003: 2 row groups;
  - CLM-004: 5 table rows;
  - CLM-005: 5 table rows;
  - CLM-010: R01 to R10;
  - CLM-011: 4 table rows;
  - CLM-013: REQ-001 to REQ-005, AC-001, AC-002 and the TBD list;
  - CLM-020: VER-001, VER-002 and the binding table;
  - CLM-027: CT001 and CT002.
  
  The SubItems obligations are met: CLM-013 has 8 rows (7 required) and CLM-020 has 3 rows
  (2 required).
- **SEE rows (MR-4), counted separately:** 24.
  - 7 point to REGISTER-3 (REF-006 PRD MATCH restated as current).
  - 17 point to anchors: CLM-003.1, CLM-003.2, CLM-004.2, CLM-004.3, CLM-004.4, CLM-005.2,
    CLM-005.3, CLM-010.8, CLM-012, SEC-1 and SEC-2.5.
  - Excluding SEE rows leaves 49 dispositioned rows.
- **HumanDecisionNeeded ≠ NO:** 22 rows.
  - R4: 13.
  - R4-Q5: 5.
  - R4-Q4: 2.
  - `R4; R4-Q5`: 1.
  - `R4-Q1; R4-Q5`: 1.
- **Errata:** none yet (forward pass).

## 2. Least-confident rows

- **CLM-004.4, CLM-010.9 and CLM-011.4 (LOW, PARTIALLY_IMPLEMENTED; redaction).**
  - Only configured-key redaction (run-logger.ts, symbol reach not traced) and e-mail
    redaction of App Server stderr were found. The live ChatPanel shows `turn:error`
    `payload.message` as received.
  - Alternative: ALIGNED. Under Codex custody the App holds no key, and K-EVENT-6 structural
    redaction may sit in runtime contracts that were not traced to the live sinks.
- **CLM-020.1 (LOW, DOCUMENTED_UNIMPLEMENTED; VER-001).** The deliverable folder has no record
  that VER-001 was run.
  - Alternative: ALIGNED, if the 2026-09-03 pathway-seating AgentRun (not opened) holds the
    VER-001 checks.
- **REGISTER-5 (LOW).** REF-009 and REF-010 are each used twice in `_REFERENCES.md`.
  - Alternative: not a defect, if each table is read as its own RefID namespace.
- **SEC-2.2 (MEDIUM, AUTHORITY_CONFLICT; D-APP-108 Q7 account row).**
  - Alternative: MR-11 with STALE_SPECIFICATION. D-APP-127's account-row clause (the row acts
    on the Runtime child and Codex login; the oMLX/residency status statements are superseded)
    could be read as addressing Q7, although it names D-APP-122, not D-APP-108.
- **CLM-003.1 anchor and its SEE family (MEDIUM, AUTHORITY_CONFLICT; Anthropic API-key UI).**
  - Alternative 1: DOCUMENTED_UNIMPLEMENTED on the live path, if App DIRECTIVE §2.8/§4.1
    controls by the §0 order.
  - Alternative 2: STALE_SPECIFICATION, if the Codex-only preambles control.
  - The worker does not choose (CONVENTIONS §1).

## 3. Register-defect summary

| Key | Defect | Disposition |
|---|---|---|
| REGISTER-1 | `_REFERENCES.md` REF-002 CONTRACT recorded MATCH `fa8fc9dcc2f0…`; recompute `57411f8df49e…` (`HASH-RECOMPUTE@00115c719`) | STALE_SPECIFICATION |
| REGISTER-2 | REF-003 SPEC recorded MATCH `01e1c75cdf7b…`; recompute `8b0d805b6abc…` | STALE_SPECIFICATION |
| REGISTER-3 | REF-006 PRD recorded MATCH `8649ccba8f68…`; recompute `17ca3f3c2b86…`. SoW rows restating it as current SEE this key | STALE_SPECIFICATION |
| REGISTER-4 | Dependencies.csv DEP-02-05-008/009/013 still ACTIVE/PENDING against the retired port, the Root/App consent contract with G3/G-CSP/G4, and Root DEL-02-09 | STALE_SPECIFICATION |
| REGISTER-5 | Duplicate RefIDs REF-009/REF-010 in `_REFERENCES.md` | REMAINING_STATE_MISMATCH |

The worker also recomputed three hashes; none is a defect:

- DIRECTIVE, TYPES and PLAN match their recorded values.
- TYPES matches even though it was amended under D-GOV-43, so its reference row was already
  refreshed.

STATE-1 records that `_CONTEXT.md` was not revised under D-APP-127: the pack's item 5 shows
`NO` for every DEL-02-05 carrier except `_STATUS.md`.

## 4. Direction and cause

**Main CauseTags:**

| CauseTag | Rows | Scope |
|---|---|---|
| CODEX_SOLE_ENGINE | 13 | The Anthropic API-key UI family (AUTHORITY_CONFLICT). |
| CREDENTIAL_CUSTODY | 12 | Port, per-root consent and identity retirement under D-APP-127; storage states. |
| DOC_HYGIENE | 11 | The REF-006 MATCH restatements and the register rows. |
| A2_TOPOLOGY | 7 | SSE names (R4-Q5), postures, REQ-005 and TurnEngine. |
| PRE_V3_DRIFT | 3 | TBDs already stale at the 2026-06-20 INSP-03. |
| CARRIER_PROPAGATION | 3 | — |
| LIFECYCLE_GATE_PENDING | 2 | — |
| OTHER:V3_FOUR_ROLE_ADOPTION | 2 | The role rows. No vocabulary tag names the v3 four-role adoption; the rows cite R4-Q4. |
| SHELL_REDESIGN | 1 | — |
| FACADE_DEPRECATION | 1 | — |

**CAUSE2 secondaries:** CARRIER_PROPAGATION, which reflects that only `_STATUS.md` was revised
under D-APP-127; CREDENTIAL_CUSTODY; A2_TOPOLOGY; CODEX_SOLE_ENGINE; FACADE_DEPRECATION.

**Direction records used:**

- GOVERNING:
  - D-APP-127 (lines 44-48, 56-124, 183);
  - CONTRACT §4 retirement of K-CONSENT-1 and amended K-NET-1, K-KEY-1, K-EVENT-1;
  - SPEC §11 and TYPES §7.4 as amended;
  - D-APP-89 (direct-import migration away from the facade);
  - D-APP-109 (dependency re-extract);
  - D-APP-108 (Q7, Q8; package rename seating);
  - D-APP-56 (R4-P35, R4-P36).
- CONTEXT:
  - `AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/tranche/APP_EXECUTION_RETURN.md:46`, which
    states that only `_STATUS.md` API-key clauses were revised;
  - `AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/MANAGER_RETURN.md` (four-role adoption).
- Also read: D-GOV-43 record and IMPACT.md (families 1-4).

**Authority handling:**

- **Anthropic key UI.** App DIRECTIVE §2.8 and §4.1 were never amended for D-GOV-43. They
  still name the Anthropic path as the key-aware default and "current Anthropic provider
  access". The lower-authority PRD, SPEC and CONTRACT preambles treat Anthropic as
  compatibility history. §0 alone would favour the DIRECTIVE, but the Codex-only basis undercuts
  §2.8 without naming it, so these rows are AUTHORITY_CONFLICT + R4.
- **SSE names.** Amended K-EVENT-1, SPEC §11 and TYPES §7.4 conflict with unamended K-ENGINE-4
  and SPEC §10.3, so these rows cite R4-Q5.
- **Roles.** Unamended K-ROLE-2 conflicts with the v3 four-role registry, so these rows cite
  R4-Q4.
- **R4-Q1.** Cited only on CLM-025, where the only code meeting the claim (TurnEngine) is
  LEGACY_ONLY.

**Searches behind each NONE_FOUND:**

- **CLM-013.8** (DirectionEvidence): `_REGISTER.md` rows D-APP-56 and D-APP-89, and the
  CONTEXT AgentRuns, for a direction keeping the TBDs. Nothing found.
- **CLM-020.1:** `_run_records/`, MEMORY.md and `_REGISTER.md` for VER-001, parity and claim
  map. Only dependency-register parity was found.
- **REGISTER-5:** `_REGISTER.md` for a reference-numbering direction. Nothing found.
- **LatestDecision NONE_FOUND on the role rows:** `_REGISTER.md` rows D-APP-108..127 and the
  Root AGENTS text for a ruling adopting the four-role registry against K-ROLE-2. Nothing found.
- **CLM-013.5** (ImplementationEvidence): `canonical-identity-producer-unavailable` and
  `hostedReady` in App `src` and `electron` and runtime `packages/*/src`. No hits.

**Reach (symbol level).** Several modules are LIVE by import but their relevant symbols are not
rendered or constructed on the woven live path; the Notes carry `SYMBOL-UNREACHED` for these:

- `ApiKeySettings` and `AccountConsentSettingsView` are rendered only when `hosted` is null.
  `useHostedBootstrapController` at `shell-frame.tsx:379` always returns a controller, so they
  never render there. `ApiKeySettings` is reachable only from `app/not-found.tsx` via
  `AppShell`.
- `SafeStorageCredentialStore` has no product construction.
- The live Runtime composition passes a credentials stub (`app-owned-composition.ts:225`) whose
  status has no `source`. `api-key-ipc.ts` `parseCredentialStatus` therefore rejects it, and
  set/remove throw `ENGINE_UNAVAILABLE`.

**PostReleaseBasis:**

- No frontend path is in `TOUCHED_PATHS.csv`.
- Blame of the relied-on runtime lines found no line from the four post-release commits:
  - `app-owned-composition.ts:180` → `95364569ae`;
  - `:225` → `95364569ae`;
  - `:226` → `9eaddb5965`.
- Every row is `NO`.

## 5. Method friction

1. **CONTEXT_CLAIM versus ALIGNED.** A conflict-table row that is accurate (CT002) cannot be
   ALIGNED; it can only be NOT_AUDITABLE. That under-reports true statements.
   - Proposal: allow ALIGNED on CONTEXT_CLAIM rows whose checkable assertion reproduces.
2. **Composite rows.** SEC-1 (the whole responsibility paragraph) and CLM-023 (a bullet list)
   mix sub-claims with different dispositions. The split rule allows splitting only
   REQ/AC/VER items or tables, so one row had to carry the dominant defect, with the others
   named in prose.
   - Proposal: allow splitting enumerated bullet lists when their dispositions differ.
3. **No CauseTag for the v3 four-role adoption.** This needed `OTHER:V3_FOUR_ROLE_ADOPTION`.
   - Proposal: add a vocabulary tag paired with R4-Q4.
4. **REACH granularity.** The module-level tag LIVE is formally correct for
   `api-key-settings.tsx`, `account-consent-settings.tsx` and `api-key-storage.ts`. It misleads
   without the SYMBOL-UNREACHED notes, because the product path never renders or constructs
   the relied-on symbol.

### Coverage gaps (for R3)

- **MEMORY.md** has no D-APP-127 entry. Its dated 2026-09-07 entry ("Account and consent remain
  unavailable in the actual shell") no longer describes the frozen basis, where Codex sign-in
  is live. MEMORY.md is not an indexed unit, and the worker did not assign a key.
- **`_STATUS.md:11`** says the command-network postures are retired. Amended K-NET-1 retains
  them, read as the user's Codex configuration shown in the composer. This is noted on
  CLM-013.3 and REM-1; there is no separate row.
- **The live Codex account surface** (`HostedBootstrapView`, `hosted-bootstrap-client.ts`, the
  hosted-bootstrap routes and the runtime `codex-login.ts`) is owned here only through REM-1
  and the retired REQ-001. No current SoW requirement describes it. The capability sits
  between DEL-02-05 and DEL-04-05; ownership should be checked in the reverse pass.
- **Attachment picker and preview chips** are SoW OUT-002 and SOW-023 duties. They are covered
  only indirectly: through AC-002 (CLM-013.7) and the retry rows. No indexed unit states their
  behaviour directly, and the D-APP-80 note (SoW:19-23) lies outside the indexed units.

## 6. Effort

- **Files read:** about 40, most as line ranges. They were:
  - the deliverable's SoW, `_STATUS`, `_CONTEXT`, `_REFERENCES`, `Dependencies.csv`, MEMORY
    and INSP-03;
  - D-APP-127, D-GOV-43 and IMPACT.md;
  - App CONTRACT, PRD, SPEC, TYPES and DIRECTIVE sections;
  - about 15 frontend and runtime source files;
  - pack files, gate transcripts and the validator.
- **Context budget:** adequate. PREGATHER.md saved most of the locating work.
