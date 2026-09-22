# DEL-02-01 forward notes — split half A (SEC-1..SEC-5, CLM-001..CLM-015)

- Run: RUN_D128_CONCORDANCE_2026-09-21_1614Z, R2 PKG-02, forward pass. Worker: TASK (Type 2), half A.
- Basis: frozen tree at `00115c719`. Ledger: `DEL-02-01_claims.csv` (41 rows + `#END`). It was validated with `--index R2/PKG-02/_split/INDEX_A.csv`: `RULES errors none | warnings none`, `RESULT PASS errors=0 warnings=0`.
- Sealed SHA-256: `5282a7a81f852ff84f4e49a78498e0b476c34373d8f5847e113f2966abe6e419`.
- Half A owns the `_REFERENCES.md` hash REGISTER rows, plus register defects in `_REFERENCES.md`, `Dependencies.csv`, `_CONTEXT.md` and the SoW front matter (REGISTER-1..6; no STATE rows).

## 1. Census

All figures are sealed. There is no errata file.

| ClaimType | Rows | Dispositions |
|---|---:|---|
| REQUIREMENT | 19 | IMPLEMENTED_DIFFERENTLY 8, PARTIALLY_IMPLEMENTED 5, DOCUMENTED_UNIMPLEMENTED 3, ACCEPTED_DIVERGENCE 2, STALE_SPECIFICATION 1 |
| ACCEPTANCE | 6 | STALE_VERIFICATION 5, ALIGNED 1 |
| STATE_ASSERTION | 5 | STALE_SPECIFICATION 5 |
| CONTEXT_CLAIM | 5 | NOT_AUDITABLE 3, STALE_SPECIFICATION 2 |
| REGISTER_DEFECT | 6 | STALE_SPECIFICATION 4, REMAINING_STATE_MISMATCH 2 |
| **Total** | **41** | STALE_SPECIFICATION 12, IMPLEMENTED_DIFFERENTLY 8, PARTIALLY_IMPLEMENTED 5, STALE_VERIFICATION 5, NOT_AUDITABLE 3, DOCUMENTED_UNIMPLEMENTED 3, ACCEPTED_DIVERGENCE 2, REMAINING_STATE_MISMATCH 2, ALIGNED 1 |

- **Coverage:** all 20 indexed units of half A are covered, and there are 6 run-local REGISTER rows.
- **Split rate:** 3 of 20 units (15%).
  - CLM-010 has 11 rows, one per DEL-02-01-REQ-001..011, because the unit holds separately numbered REQ items.
  - CLM-012 has 5 rows. The index SubItems are REQ-001, 004, 007, 010 and 011, matching the five verification table rows.
  - CLM-015 has 2 rows: the R4-P29 statement and AC-001.
  - SEC-2 and SEC-4 are not split. Their obligations are numbered lists, not REQ/AC/VER items.
- **SEE rows (counted separately): 5.**
  - CLM-001, CLM-004 and CLM-011 point to REGISTER-3 (Addendum 5 rule 3: PRD MATCH restated as current).
  - CLM-008 points to CLM-001 (verbatim repeat).
  - CLM-014 points to CLM-007 (repeat).
- **HumanDecisionNeeded:** `R4-Q4` on 22 rows; `NO` on 19 rows. There is no R4-Q1: no cited code is `REACH=LEGACY_ONLY` (Addendum 6 rule 3).
- **Confidence:** HIGH 14, MEDIUM 25, LOW 2.
- **PostReleaseBasis:** `NO` on all rows. No cited file is in `TOUCHED_PATHS.csv`: the touched list has no `frontend/**`, App `docs/**` or deliverable paths.

## 2. Least-confident rows

- **CLM-010.10 (REQ-010, disabled variants visible), LOW.**
  - Chosen: IMPLEMENTED_DIFFERENTLY + R4-Q4. The matrix-adjacent flows are gone. On the live path the composer shows Plan Mode disabled with a reason, and an off-roster role as "(unavailable)".
  - Alternative 1: ALIGNED, because the requirement is scoped to "where this deliverable exposes them".
  - Alternative 2: DOCUMENTED_UNIMPLEMENTED, if only matrix-adjacent flows count.
- **REGISTER-4 (duplicate RefIDs REF-009/REF-010 in `_REFERENCES.md`), LOW.**
  - Chosen: REMAINING_STATE_MISMATCH.
  - Alternative: STALE_SPECIFICATION (the table implies one source per RefID).
  - Neither register verdict fits an identity collision well (see §5).
- **MEDIUM rows where the verifier may read the subject differently:**
  - **CLM-007 / CLM-014, UPD-106 "implemented".** I judged this on product behaviour: the header row is gone. The module-level reading is ALIGNED, because the ShellFrame test exists and passes.
  - **CLM-003 / CLM-005 / CLM-009, mixed attribute tables.** The presentation part reads as ACCEPTED_DIVERGENCE (D-APP-74/D-APP-108, which the SoW acknowledges). The compatibility part reads as IMPLEMENTED_DIFFERENTLY. I chose the compatibility reading as primary, because it carries the open R4-Q4 question.

## 3. Register-defect summary

| Key | File | Defect | Disposition |
|---|---|---|---|
| REGISTER-1 | `_REFERENCES.md` L8 | REF-002 CONTRACT recorded MATCH `fa8fc9dc…`, recomputed `57411f8d…` | STALE_SPECIFICATION |
| REGISTER-2 | `_REFERENCES.md` L9 | REF-003 SPEC recorded MATCH `01e1c75c…`, recomputed `8b0d805b…` | STALE_SPECIFICATION |
| REGISTER-3 | `_REFERENCES.md` L12 | REF-006 PRD recorded MATCH `8649ccba…`, recomputed `17ca3f3c…` (restated in CLM-001/004/008/011) | STALE_SPECIFICATION |
| REGISTER-4 | `_REFERENCES.md` L14-15, L22, L34 | REF-009 and REF-010 each name two different sources | REMAINING_STATE_MISMATCH |
| REGISTER-5 | `_REFERENCES.md` L44-46 | `_ScopeChange/_LATEST.md` SHA `b297f43e…` is tied to PR #711. The file is now `10df19ec…`, changed by 480fcb8ab and 23b3879b3. This is a snapshot row (MR-8(iv)). | REMAINING_STATE_MISMATCH |
| REGISTER-6 | `Dependencies.csv` DEP-02-01-011 | ACTIVE target "Root-owned daemon session record", but the daemon was retired by D-APP-127 (A2). The row's Statement also says the context line shows delegation and rung. | STALE_SPECIFICATION |

- My own recompute shows the other `_REFERENCES.md` hashes (DIRECTIVE, TYPES, PLAN and the three software-decomp workflow files) still reproduce. The decomposition post-image `c7c05169…` reproduces too.
- The SoW front-matter pin `dbd812a5…` is still the decomposition's last-change commit, so it is not a defect.
- `_CONTEXT.md`: no defect found. Its Deliverable Scope restates decomposition L307 (governing), including "delegation, rung". That gap is dispositioned on SEC-3, not as a register defect.

## 4. Direction and cause

- **Main finding: the v3 four-role adoption commit `9b005c23a` (2026-09-09).**
  - What it changed:
    - `agent-matrix.tsx` became a role directory with no 3x4 grid.
    - `WovenDialogueRoute` now voids its `legacy` element. Before this commit, `?legacy=1` and the non-dialogue surfaces rendered the loop-first/PORTAL/Pipeline UI.
    - The "No delegation" placeholder and the rung/ladder wording were removed from the composer and matrix (`git log -S`).
  - What it conflicts with: the unamended App TYPES §4.1-4.3, PRD FR-007 and DIRECTIVE §4.1 still keep the legacy matrix, loop-first UI and route/query behaviour as a compatibility contract. SoW SEC-2 ob.2 and SEC-4 ob.5 restate that contract. No App ruling retires it.
  - How the rows cite it: `R4-Q4` on 22 rows, with CauseTag `OTHER:V3_ROLE_ADOPTION` (21 rows as primary, 1 as CAUSE2).
- **SHELL_REDESIGN (SCA-APP-010, D-APP-108)** is used in two ways:
  - As the governing basis for the accepted header/tab divergences (CLM-010.2 and .3; `GOV:D-APP-108`).
  - As a CAUSE2 secondary on 8 rows.
- **DOC_HYGIENE (9 rows):** the hash drift behind REGISTER-1..3 and their SEE rows. CONTRACT, SPEC and PRD were edited 2026-09-12 (23b3879b3, 9eaddb596, 7f1e9f387, 95b342519), and the references were not refreshed. CAUSE2 is CARRIER_PROPAGATION.
- **CARRIER_PROPAGATION (SEC-5):** the D-APP-109 dependency re-extraction did not update the SoW sentence saying the DEP writes "await" extraction.
- **A2_TOPOLOGY (REGISTER-6):** `GOV:D-APP-127`.
- **CONTEXT and GOV records used:**
  - `CTX:` `projects/chirality-app-dev/execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/UI_SOURCE_FREEZE_v7.md`. The v7 freeze lists `agent-matrix.tsx` and `portal-loop-shell.tsx`. It is thin: it records the change but not a retirement rationale.
  - `GOV:` D-APP-56, D-APP-108, D-APP-109, D-APP-127.
  - Root D-GOV-42 (status "candidate implementation", not in the RUN_BASIS GOVERNING map) is cited in Notes only.
- **Searches behind each `NONE_FOUND`:**
  - Matrix/Pipeline/PORTAL/legacy retirement: grep of `_REGISTER.md` for rung, ladder and the retirement terms, the D-GOV-42 text, and the CHIRALITY_V3_APP_ADOPTION run files. None names the matrix or loop-first UI retirement.
  - Hash refresh: `_REGISTER.md` plus the D-APP-127 application map (DEL-02-01 `_REFERENCES.md` Revised=NO). No record directs or defers the refresh.
  - Duplicate RefIDs: `_REGISTER.md`; no reference-numbering ruling.
  - `_LATEST.md`: `_REGISTER.md` D-APP-111 moves other pointers, not this one.
- **Symbol-level reach.** The whole loop-first generation is LIVE by import in `REACHABILITY.csv` but has no render path, so those rows carry `SYMBOL-UNREACHED` notes. This covers `PortalLoopShell`, `LoopShell`, `LoopTertiaryShell`, `SidebarRightLoopLayout`, `createTertiarySidebarTabs`, `AgentMatrix`, `PipelineSurface`, `WorkbenchSurface`, and the ShellFrame header branch (rendered only on `not-found`, where pathname is never `/`).

## 5. Method friction

- **Coverage gaps (for R3):**
  - The SoW purpose line OUT-001 (L16) and the SCA-APP-004/010 section preambles (L20-26, L75-82) are not indexed units. No false fact was found there, so none was needed.
  - SoW CLM-023 (half B) says UPD-106 "remains withheld", while CLM-007/014 (half A) say it is "implemented". I dispositioned my half only. The contradiction needs the merged view.
  - SEC-3/SEC-4's "delegation, rung" gap also sits in decomposition row L307. That row is governing and not an audit target, so it needs an R4-Q4 consequence note rather than a ledger key.
- **No CauseTag names the v3 four-role adoption mechanism.**
  - I used `OTHER:V3_ROLE_ADOPTION` rather than stretch `V3_RELEASE_SCOPE`: no CONTEXT record explicitly scopes the matrix out of v3.
  - Proposal: add `V3_ROLE_ADOPTION` to the vocabulary as the CauseTag paired with R4-Q4.
- **REGISTER_DEFECT verdicts:** the vocabulary has only STALE_SPECIFICATION and REMAINING_STATE_MISMATCH. Neither fits an identity collision (duplicate RefIDs). Proposal: allow `OTHER`-style register-integrity handling, or state which verdict applies.
- **Mixed tables:**
  - CLM-003 and CLM-005 hold rows whose presentation part is an accepted divergence and whose compatibility part turns on R4-Q4.
  - Splitting them is not licensed, since they have no REQ/AC/VER items. A single row therefore records one reading and notes the other.
  - Proposal: allow `.n` splits for attribute tables when the rows fall under different governing rulings.
- **`R4-Q4` on verification rows (CLM-012.x):** I cited it because whether the tests should be re-pointed or the behaviour restored depends on the ruling. A narrower reading would put `NO` there.

## 6. Effort

- **Read:**
  - The deliverable `ScopeOfWork.md` (full), `_STATUS.md` L1-70, `_CONTEXT.md`, `_REFERENCES.md`, `Dependencies.csv` (all rows, by script), and `_DEPENDENCIES.md` (grep).
  - `Assessment_INSP-03`.
  - CONVENTIONS, the RUN_BASIS sections and addenda, the evidence-pack rows, PREGATHER, and the gate transcript head.
  - Register rows and ruling excerpts: D-APP-108, D-APP-127, D-GOV-42.
  - App docs: DIRECTIVE §4.1, TYPES §4, and PRD FR rows (grep).
  - About 20 frontend source files (line ranges) and 10 test files (case lists).
- **Git (read-only):** `show`/`log` on 9b005c23a, 8aaee11f6, db0dff954 and f38f14486, plus `log -S` for rung and delegation.
- **Other:** hash recomputes by `shasum` on the frozen tree. HINTS were summarized by script: 536 rows, 279 on half-A keys, used as leads only.
- **Context budget:** not tight. The PREGATHER locator saved most of the code search.
