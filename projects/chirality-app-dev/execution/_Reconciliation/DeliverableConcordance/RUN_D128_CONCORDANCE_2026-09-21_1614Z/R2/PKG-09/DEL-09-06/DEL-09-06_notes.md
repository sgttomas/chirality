# DEL-09-06 — forward-pass notes (R2, PKG-09 wave 5)

This covers the ledger `DEL-09-06_claims.csv`, written from the frozen tree at `00115c719`. The deliverable folder is `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/`.

## 1. Census

- **Rows:** 59. 53 rows cover the 34 indexed units, and 6 are run-local (`REGISTER-1..3`, `STATE-1..3`).
- **Split rate:** 2 of 34 units were split (5.9%).
  - `CLM-010` has 15 rows, one for each REQ-001..015 in its requirements table.
  - `CLM-012` has 6 rows, one for each verification row. Its SubItems list is REQ-001/004/005/008/011/014, and each `.n` names its item in Notes.
  - `CLM-014` (AC-001) and `CLM-021` (VER-001) each hold a single sub-item, so they were not split.

| Disposition | Rows |
|---|---:|
| STALE_SPECIFICATION | 21 |
| ALIGNED | 15 |
| PARTIALLY_IMPLEMENTED | 11 |
| IMPLEMENTED_DIFFERENTLY | 5 |
| NOT_AUDITABLE | 5 |
| REMAINING_STATE_MISMATCH | 2 |

| ClaimType | Rows | Dispositions |
|---|---:|---|
| REQUIREMENT | 34 | ALIGNED 12, PARTIALLY_IMPLEMENTED 9, STALE_SPECIFICATION 8, IMPLEMENTED_DIFFERENTLY 5 |
| CONTEXT_CLAIM | 9 | NOT_AUDITABLE 5, STALE_SPECIFICATION 4 |
| STATE_ASSERTION | 7 | STALE_SPECIFICATION 6, REMAINING_STATE_MISMATCH 1 |
| REMAINING_WORK | 4 | ALIGNED 3, STALE_SPECIFICATION 1 |
| REGISTER_DEFECT | 3 | STALE_SPECIFICATION 2, REMAINING_STATE_MISMATCH 1 |
| ACCEPTANCE | 2 | PARTIALLY_IMPLEMENTED 2 |

- **SEE rows, counted separately:** 6.
  - 4 are MR-4 repeats of the same statement:
    - `CLM-008`, `CLM-011` and `CLM-022` point to `CLM-001`;
    - `CLM-012.6` points to `CLM-010.15`.
  - 2 follow tie-break rule 3 and point to the register row:
    - `CLM-001` and `CLM-006` point to `REGISTER-1`.
- **HumanDecisionNeeded:** NO on 51 rows, R4-Q1 on 5, D-APP-121 on 3.
- **Confidence:** HIGH on 25 rows, MEDIUM on 34, LOW on none.
- **Validator:** `RESULT PASS errors=0 warnings=0`.

## 2. Least-confident rows (with the alternative reading)

No row is LOW. These MEDIUM rows are the closest calls:

- **`SEC-1` (STALE_SPECIFICATION)**
  - Alternative: PARTIALLY_IMPLEMENTED. The Codex sole-engine statement matches code, and so does the S0 PDF fallback (`preload.ts:77`, `inlinePdfPreview: false`).
  - Only the retained-safeguard list (per-root consent, supplier identity-currentness, containment) is stale under D-APP-127.
  - I chose the text-repair verdict per tie-break rule 4.
- **`CLM-010.3` (REQ-003, IMPLEMENTED_DIFFERENTLY + R4-Q1)**
  - Alternative: AUTHORITY_CONFLICT. SPEC §16.2 (Electron `safeStorage` at `api-key.enc`) is unamended.
  - D-APP-127 supersedes the D-APP-126 safeStorage exception and puts credentials in Codex custody, but it does not name SPEC §16.2.
  - I did not use AUTHORITY_CONFLICT because §16.2 describes the retained Anthropic key store rather than Codex credentials. Whether that store is still an obligation is exactly R4-Q1.
- **`CLM-010.4` (REQ-004, IMPLEMENTED_DIFFERENTLY + R4-Q1)**
  - Alternative: ACCEPTED_DIVERGENCE. SEC-1, in the same SoW, declares the Anthropic text compatibility history, and amended CONTRACT K-NET-1 (read with D-GOV-43) calls the Anthropic path compatibility history. This is recorded as `ALSO:`.
- **`CLM-010.2` (REQ-002, ALIGNED)**
  - Alternative: PARTIALLY_IMPLEMENTED. No secret scan has been recorded since A2, the scan script is a manual `proof:*` entry, and the Codex field-family scan (REM-3) is still open.
  - On the live path the App holds no provider key material, and redaction is LIVE.
- **`CLM-010.7` (REQ-007, ALIGNED)**
  - Alternative: PARTIALLY_IMPLEMENTED. `danger-full-access` sends no `networkAccess` restriction.
  - I read it as the user's explicit, visible choice under D-GOV-43 item 4, not a silent broadening. I did not verify that the composer displays the choice.
- **`REM-2` (STALE_SPECIFICATION)**
  - Alternative: ALIGNED. The item is correctly still open.
  - What is stale is its gate: effective home and login are LIVE (`codex-effective-home.ts`, `codex-login.ts`). Its A1 re-stage check and G-WIRE removal condition are also stale.
- **`REM-4` (ALIGNED)**
  - Alternative: REMAINING_STATE_MISMATCH. SEC-1 says the S1 built-in PDF is inapplicable this release, yet the item stays on Remaining.
  - I kept ALIGNED because D-APP-121's effect is HELD and no ruling deferring S1 was found.
- **`CLM-001` (STALE_SPECIFICATION)**
  - Alternative: an MR-8(iv) REGISTER row. The note is dated 2026-07-12, but it presents MATCH as current state.

## 3. Register-defect summary

- **`REGISTER-1`:** `_REFERENCES.md` REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD are recorded MATCH, but none reproduces at `00115c719` (`HASH-RECOMPUTE@00115c719`, `REFERENCE_HASHES.csv`). DIRECTIVE, TYPES and PLAN still match. The SoW rows that restate MATCH are `CLM-001`, `CLM-004`, `CLM-006`, `CLM-008`, `CLM-011`, `CLM-022`, `CLM-025` and `CLM-028`.
- **`REGISTER-2`:**
  - `_DEPENDENCIES.md` still says "no accepted dependency edges (TBD)", although `Dependencies.csv` has 11 ACTIVE rows.
  - DEP-09-06-008 and DEP-09-06-009 say the test commands and implementation paths are "currently TBD". Both are now located.
- **`REGISTER-3`:** DEP-09-06-011 is still PENDING, although its consumer V3-01 landed on 2026-09-03 and D-APP-127 has since changed the credential bridge. This is a status lag.
- **Stale conflict table:** `CLM-028` records "no conflict" plus MATCH. It omits three conflicts now present:
  - SEC-1 versus AC-001/VER-001/REM-4 on the D121 S1 proof;
  - amended SPEC §16.1 versus REQ-011/012;
  - D-APP-127 versus the key-storage requirements.
- **Carrier gaps:**
  - `_CONTEXT.md` still says Claude Agent SDK/Anthropic is the current path (`STATE-1`).
  - `MEMORY.md` has no entry for the D-APP-127 application (`STATE-3`).
  - The D-APP-127 application map shows only `_STATUS.md` revised.

## 4. Direction and cause

- **Main CauseTags:**
  - CODEX_SOLE_ENGINE (16): key, endpoint and attachment-failure text written for the legacy Anthropic path;
  - DOC_HYGIENE (11): the MATCH restatements and register lag;
  - PRE_V3_DRIFT (5): TBD path and command slots from 2026-05-20;
  - CREDENTIAL_CUSTODY (3);
  - CARRIER_PROPAGATION (3);
  - A2_TOPOLOGY (1).
- **Secondary CAUSE2 tags:** CARRIER_PROPAGATION 5, DOC_HYGIENE 4, A2_TOPOLOGY 3, CREDENTIAL_CUSTODY 3, CODEX_SOLE_ENGINE 3, PRE_V3_DRIFT 1.
- **Governing records used:**
  - D-APP-127, which names DEL-09-06 as revised and sets families 3 adapts and 4 retains;
  - D-GOV-43 through amended CONTRACT line 17 and K-NET-1;
  - D-APP-38 (reference-integrity model);
  - D-APP-121 (PDF, RULED with effect HELD);
  - D-APP-97.
- **Amended SPEC §16.1:** commit `9eaddb596` (2026-09-12, #778) scopes partial-failure and `ATTACHMENT_FAILURE` behaviour to the legacy provider path. I cite it as `GOV:SPEC §16.1 as amended 9eaddb596`. No register row names it, so `LatestDecision` is `NONE_FOUND` on REQ-011/012.
- **CONTEXT used:** `R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md`, for the G-WIRE row ("superseded by faithful transport"), DONE-11 and DONE-19. It is mentioned only in Notes and never changes a Disposition.
- **Relevant done-declaration questions:**
  - Q-02 (release act and F-APP-2 lift: REM-1, and `desktop:dist` chaining `verify-codex-pin --after-signing`);
  - Q-06 (no record ruling the sole-engine decision: SEC-1);
  - Q-07 (containment replaced by user policy: SEC-1, REQ-007).
- **Searches behind each `NONE_FOUND`:**
  - I grepped `_REGISTER.md` for DEL-09-06, DEP-09-06, TBD, "command family", D-APP-121 and SPEC §16.1.
  - I searched `_STATUS.md` History, `MEMORY.md` and D-APP-127 for instructions to keep the TBD slots or to defer S1.
  - The in-root `plans/` tree has no v3 steer. The CONTEXT steers live at the repository root and were not read: OUT_OF_ROOT:plans/steers/chirality_app_v3_app_ruling_record_a15_2026-09-04.md and OUT_OF_ROOT:plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html.
  - The only in-root trace of an S1 deferral is the constant `D121_S1_MATRIX_STATUS = 'INAPPLICABLE_OWNER_DEFERRED'` at `run-packaged-security-proof.mjs:92`, from commit `5bd5a63ef`.
- **R4-Q1 rows** (by evidence: the only code meeting the claim is LEGACY_ONLY or UNREACHED): CLM-010.1, CLM-010.3, CLM-010.4, CLM-010.11 and CLM-010.12.
- **UNREACHED, tagged LEGACY_ONLY per Addendum 1:**
  - `SafeStorageCredentialStore` and `storeProviderApiKey`/`readProviderCredential` have no non-test caller. `api-key-ipc.ts` imports only `isProviderCredentialId`.
  - `getProviderApiKey` is reached only through legacy managers.
  - The `proof:*` scripts are not chained by `desktop:pack`, `desktop:dist` or `validate:release-quality`.
- **Live credential port:** `app-owned-composition.ts:225`. `get` returns undefined and `status` returns configured:false; `set` and `remove` throw ENGINE_UNAVAILABLE.
- **PostReleaseBasis:** NO on every row.
  - The only TOUCHED paths I cite are `app-owned-composition.ts` (lines 180, 225, 226) and `codex-supervisor.ts` (lines 104-108, 470-490).
  - Blame attributes those lines to `95364569a` and `9eaddb596`. Neither is one of the four post-release commits.

## 5. Method friction

- **S0 fallback basis:** SEC-1 cites an "owner-directed" S0/default-app fallback, but I found no governing record for it in-root, and D-APP-121 selected A-design/A-proof. The rulebook has no token for a deliverable claim whose governing basis may sit only in an out-of-root steer. I recorded the out-of-root sources in Notes and did not use AUTHORITY_CONFLICT.
  - Proposal: an `OUT_OF_ROOT_BASIS` note convention that R3 can cluster.
- **SEE token semantics:** tie-break rule 3 asks SoW MATCH restatements to point to the REGISTER row with `SEE:`. The validator requires a SEE target to carry the same Disposition. That works here because REGISTER-1 is STALE_SPECIFICATION, but it would break if a register row took REMAINING_STATE_MISMATCH.
- **Proof scripts under the reach rule:** `proof:*` scripts are package.json entries, but no release or packaging script chains them. I tagged them LEGACY_ONLY with UNREACHED in Notes, as the brief directs.
  - Their reach has no bearing on R4-Q1 for VER-001, because the checked surface (`main.ts`) is LIVE.
  - Proposal: a clarification that manual proof entries are "not live for release proof" without implying legacy-harness status.

## 6. Effort

- **Files read:** about 45, selectively.
  - Deliverable: SoW, `_STATUS`, `_REFERENCES`, `_CONTEXT`, `_DEPENDENCIES`, the `Dependencies.csv` rows, `MEMORY`, INSP-03, and one Evidence summary. `_SEMANTIC*` was not read.
  - Also: the D-APP-127 excerpts, register rows, CONTRACT/SPEC/PRD clauses, about 20 code and test files by line range, the evidence pack, the gate transcripts and the done-declaration excerpts.
- **Git use:** 8 read-only blame/log/show calls against the frozen tree.
- **Context budget:** adequate, not tight.

## Coverage gaps

- **Unindexed SoW text:** the SoW's "Purpose and Objective Traceability" section (OUT-001, L18-22) and "Output and Evaluation Matrix" (L428-432) are outside the claim index. I covered them in run-local `STATE-2`. The index builder may want to emit OUT-nnn units.
- **Undocumented delivered work:** `DEL-09-06-V3-01/04/05/06` were delivered (per `_STATUS` History and `Evidence/Node_*`), but none of them has a requirement row in the SoW.
  - The delivered work covers credential IPC sender authorization, renderer window hardening, the CSP nonce, and the egress-probe restriction.
  - It is not reflected as REQ/AC text: REQ-005/006 cover only the egress allowlist.
  - Candidate owner: this deliverable, with a SoW revision.
- **Unowned requirement:** the amended CONTRACT K-NET-1 adds the update-metadata GET to `api.github.com/.../releases/latest`, a main-process egress path. No DEL-09-06 requirement covers it, and ownership (DEL-02-01 or DEL-09-06) is unclear. The done-declaration's DONE-19 names both.
- **REM-2 dependencies:** `Depends` names DEL-04-05-V3-02 and DEL-02-05-V3-03. Their status is outside this worker's read set, so `MechanicallyUnblocked = UNKNOWN`.
