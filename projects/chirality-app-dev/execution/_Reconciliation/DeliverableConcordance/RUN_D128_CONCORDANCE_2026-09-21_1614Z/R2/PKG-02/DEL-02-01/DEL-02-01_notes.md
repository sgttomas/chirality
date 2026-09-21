# DEL-02-01 notes (merged by `_scripts/merge_split.py`; halves verbatim)


---

# Half A (SEC-1..5, CLM-001..015)

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

---

# Half B (CLM-016..030, REM-1..7)

# DEL-02-01 forward notes, split half B

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, R2 PKG-02. TASK worker (Type 2), half B of DEL-02-01.
Units: CLM-016..CLM-030 (SoW L320 to end: Praxeology, Axiology, Conflict Table) and REM-1..REM-7
(`_STATUS.md` `## Remaining`), plus run-local rows REGISTER-50 and STATE-50. Frozen basis `00115c719`.
Validated with `--index R2/PKG-02/_split/INDEX_B.csv`: `RESULT PASS errors=0 warnings=0`.

## 1. Census

Sealed figures only. No errata file exists.

- Rows: 37. The 22 indexed units are all covered, plus 2 run-local rows (REGISTER-50, STATE-50).
- Split rate: 4 of 22 units split (18%): CLM-020 (9 verification-table rows), CLM-023 (P45 note plus
  VER-001), CLM-029 (3 example rows) and CLM-030 (3 conflict rows). Together they produce 17 sub-rows.
- SEE rows, counted separately: 4 (CLM-025 to CLM-017; CLM-029.1 to CLM-020.6; CLM-029.2 to CLM-020.7;
  CLM-029.3 to CLM-020.1).

Rows by Disposition:

| Disposition | Rows |
|---|---|
| ACCEPTED_DIVERGENCE | 9 |
| STALE_SPECIFICATION | 9 |
| IMPLEMENTED_DIFFERENTLY | 5 |
| NOT_AUDITABLE | 4 |
| DOCUMENTED_UNIMPLEMENTED | 3 |
| REMAINING_STATE_MISMATCH | 3 |
| ALIGNED | 2 |
| PARTIALLY_IMPLEMENTED | 2 |

Rows by ClaimType, with their Dispositions:

| ClaimType | Rows | Dispositions |
|---|---|---|
| ACCEPTANCE | 13 | ACCEPTED_DIVERGENCE 7, DOCUMENTED_UNIMPLEMENTED 3, IMPLEMENTED_DIFFERENTLY 2, ALIGNED 1 |
| CONTEXT_CLAIM | 7 | NOT_AUDITABLE 4, STALE_SPECIFICATION 3 |
| STATE_ASSERTION | 6 | STALE_SPECIFICATION 5, ALIGNED 1 |
| REMAINING_WORK | 6 | REMAINING_STATE_MISMATCH 3, PARTIALLY_IMPLEMENTED 2, IMPLEMENTED_DIFFERENTLY 1 |
| REQUIREMENT | 4 | ACCEPTED_DIVERGENCE 2, IMPLEMENTED_DIFFERENTLY 2 |
| REGISTER_DEFECT | 1 | STALE_SPECIFICATION 1 |

Other counts:

- **HumanDecisionNeeded:** `NO` 27; `R4-Q4` 9; `R4` 1 (REM-7). No R4-Q1, because no cited code is
  `REACH=LEGACY_ONLY`. The only matrix-routing code is `TEST_ONLY`.
- **Confidence:** HIGH 15; MEDIUM 20; LOW 2.
- **MechanicallyUnblocked on REMAINING_WORK rows:**
  - YES on REM-3 (no gate and no Depends) and REM-7 (gate met);
  - NO on REM-2 (`MOOT:D-APP-127`), REM-4 (Depends DEL-02-04-V3-01 is still open), and REM-5 and
    REM-6 (gate V3-01 not landed; DEL-02-04-V3-01 open).
- **PostReleaseBasis:** `NO` on every row. `TOUCHED_PATHS.csv` lists no `frontend/**` path and no
  PKG-02 carrier.

## 2. Least-confident rows

- **CLM-023.2 (VER-001), LOW, `DOCUMENTED_UNIMPLEMENTED`.**
  - Finding: no claim map, parity report or review checklist for DEL-02-01 was found in the
    deliverable folder, the SOW-STAGE2 run folders, or the migration commits 8362783a2 and
    07e1a4f0b.
  - Alternative reading: those artifacts sit in a SoW-migration run outside the searched paths. In
    that case the row is ALIGNED.
- **REM-6 (DEL-02-01-V3-03), LOW, `PARTIALLY_IMPLEMENTED`.**
  - What is built: known roots, the folder line, and a cross-root navigator. The navigator combines
    the live listing, the local chat index, and running-session polling of the other roots.
  - Alternative reading: that design is what "spans every known root" meant. The open item would
    then be contradicted by the evidence, and the row would be `REMAINING_STATE_MISMATCH`, like
    REM-5.
- **CLM-023.1, MEDIUM.**
  - Chosen verdict: `STALE_SPECIFICATION`, because the same SoW carries an updated copy of the note
    at CLM-014 (half A).
  - Alternative reading: MR-8(iv). The note is dated 2026-07-12 and was true at that moment, which
    would make it a REGISTER row.
- **CLM-020.4 and CLM-020.5, MEDIUM, `ACCEPTED_DIVERGENCE`.**
  - Chosen verdict: accepted, because TYPES §4 (amended under D-APP-74) no longer requires a visual
    matrix.
  - Alternative reading: the vocabulary check is part of the route/query contract that TYPES §4
    keeps. That would make these rows R4-Q4 rows, like CLM-020.6 and CLM-020.7.
- **REM-7, MEDIUM, `IMPLEMENTED_DIFFERENTLY` with `R4`.**
  - Alternative reading: `REMAINING_STATE_MISMATCH`. The item cannot complete as written because the
    renderer icon was removed by owner direction recorded only in CONTEXT (the trial findings).
    D-APP-108 Q5 still says "ship the icon".

## 3. Register-defect summary

- **REGISTER-50 (`STALE_SPECIFICATION`).** The `_STATUS.md` L4 header ("P06 Record") says the generic
  concordance Remaining "stays open for R6". The file's own L84 records that R6 removed it on
  2026-07-12.
- **STATE-50 (`ALIGNED`).** The lifecycle header fields agree with D-APP-54 and D-APP-56 R4-P39.
- **Recorded, not rowed:**
  - The `_STATUS.md` History list is out of date order (L86 comes after L72-84).
  - `_STATUS.md` was last changed 2026-09-06, before the chat-organisation and per-chat-folder code
    landed (5bd5a63ef 2026-09-08; ca8e6935d 2026-09-12). This lag is carried on REM-5 and REM-6.
- **Hash rows.** The `_REFERENCES.md` hash REGISTER rows (CONTRACT, SPEC and PRD all recompute NO)
  belong to half A. Half B rows that restate PRD MATCH as current take `STALE_SPECIFICATION`:
  CLM-024, CLM-027 and CLM-030.2. They mention the half A row in prose only, because a SEE token
  across halves is not allowed.
- **MEMORY.md.** Its entries are dated and bounded, and none asserts a now-false present fact. No
  MEMORY row was needed.

## 4. Direction and cause

### Main CauseTags

| CauseTag | Rows | What it covers |
|---|---|---|
| SHELL_REDESIGN | 11 | Loop-first presentation, header and tertiary forms, superseded by SCA-APP-004 and SCA-APP-010 |
| OTHER:V3_ROLE_ADOPTION | 7 | See below |
| PRE_V3_DRIFT | 6 | See below |
| CARRIER_PROPAGATION | 4 | See below |
| V3_RELEASE_SCOPE | 2 | Removal of the in-app logo and favicon |
| A2_TOPOLOGY | 1 | The REM-2 daemon bounce |

- **OTHER:V3_ROLE_ADOPTION** is a new token. It covers the removals made by commit 9b005c23a (the
  2026-09-09 v3 four-role adoption):
  - the `AgentMatrix` grid, rewritten as a role directory;
  - the context-line "No delegation" / "Plain chat" spans, replaced by Interaction mode.
  - No vocabulary tag names this mechanism. It is the R4-Q4 subject.
- **PRE_V3_DRIFT** covers the July texts: UPD-105 and UPD-106, and the FR-008/TYPES rewrite of
  2026-07-23.
- **CARRIER_PROPAGATION** covers the PRD MATCH restatements and REM-5.

`CAUSE2:` secondaries used: SHELL_REDESIGN, OTHER:V3_ROLE_ADOPTION, CARRIER_PROPAGATION, DOC_HYGIENE
and V3_RELEASE_SCOPE.

### Governing rulings cited

| Ruling | What it establishes |
|---|---|
| D-APP-74 | Supersedes only the fixed presentation clauses of D-APP-28/30/31/32. It performs no old-UI retirement. TYPES §4 now calls the matrix a legacy route/query/alias contract. |
| D-APP-108 | Q3: Workbench/Pipeline are reachable by URL, unmounted and unlisted. Q5: ship the icon. Q9: folder conveniences. |
| D-APP-120 | The A1 locus addition is held. No-folder operation is restricted. |
| D-APP-127 | Supersedes D-APP-88's helper bundle and LaunchAgent. This makes REM-2 moot. |
| D-APP-127 / D-APP-98 | The PRD amendments behind the hash drift. |
| D-APP-56 | UPD-105 and UPD-106. |
| D-APP-109 | Re-extraction of the dependency register. |

### CONTEXT records used

- `AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909` (the v3 role adoption);
- `AgentRuns/APP_V3_DIRECT_TRIAL_20260910/TRIAL_FINDINGS.md`, which records the owner direction "no
  logo in the UI", commit b2b32669c;
- `AgentRuns/APP_V3_UI_REFINEMENT_20260912` (commit ca8e6935d);
- `AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/pkg02/HANDOFF.md`.

### NONE_FOUND searches

- **CLM-023.2.** Three searches, all with no DEL-02-01 hit:
  - `_REGISTER.md` grep for "parity report" / "claim map" (0 hits);
  - a grep of the `APP_V3_*`, `APPDEV_V3_NODE_*` and `CHIRALITY_V3_APP_ADOPTION_20260909` CONTEXT
    folders for the same terms;
  - a listing of the SOW-STAGE2 run folders.
- **CLM-030.1.** `_REGISTER.md` grep for `Desktop_UI_and_Local_Experience` found no ruling. The row is
  NOT_AUDITABLE, so no DirectionEvidence was needed.

### R4-Q4 rows (9)

- CLM-017, CLM-019, CLM-020.6, CLM-020.7, CLM-025, CLM-026, CLM-029.1, CLM-029.2 and REM-4.
- The question behind them: TYPES §4.1-4.3 (GOVERNING, unamended for the v3 role adoption) still
  defines matrix rows, columns and destinations as a legacy route/query contract. PRD §7.2 L423
  still says "matrix/query behavior ... remain compatible". On the live path only `?agent=` is
  honoured: `?row`, `?column` and `?category` are read only by unrendered `WorkbenchSurface` and
  `PipelineSurface`.

## 5. Method friction and coverage gaps

### Method friction

- **No v3 role-adoption CauseTag.** Removals made by the v3 four-role adoption fit no vocabulary tag.
  I used `OTHER:V3_ROLE_ADOPTION` on 7 rows. Proposal: add a tag `V3_ROLE_ADOPTION`, paired with
  R4-Q4.
- **Import-LIVE, never rendered.** `REACHABILITY.csv` tags the whole loop-first/PORTAL/matrix
  generation LIVE, because every page imports it as a `legacy` prop. `WovenDialogueRoute` then
  discards that prop (`void legacy`). I kept the pack tag and wrote `SYMBOL-UNREACHED` in Notes, per
  the brief.
- **SoW dated-history framing vs MR-8.** SoW L20-26 declares every older clause dated compatibility
  history. That supports ACCEPTED_DIVERGENCE for presentation clauses. It does not support it for
  matrix route/query semantics, which D-APP-74 did not retire. A rule saying when an SCA
  "controlling section" counts as the MR-8(ii) acknowledgement would reduce judgment calls.
- **REM rows without a gate.** I used `NONE_RECORDED` in RemainingGate. For REM-3 (no gate, no
  Depends), MechanicallyUnblocked is YES only vacuously.

### Coverage gaps (for R3)

- **SCA-APP-010 obligation 5 is not met.** It says "the loop-first UI remain[s a] compatibility
  surface", yet the loop-first UI is reachable from no route: `legacyHref` is voided at
  `navigator.tsx:119`, and the `legacy` element is voided at `woven-dialogue-route.tsx:18`. This is
  half A's unit (SEC-4). It is flagged here because half B's legacy-clause rows depend on it.
- **The matrix route/query contract belongs to another deliverable.** The legacy contract in TYPES
  §4 is owned by DEL-08-02, not DEL-02-01 (Dependencies.csv DEP-02-01-006). DEL-02-01 holds no unit
  for a live `?row/?column` handler.
- **The macOS icon changed without the recorded handoff.** DEP-02-01-013 names a DEL-09-04 handoff
  (the icon reproducibility record) that was never produced. Meanwhile b2b32669c changed
  `build/icon-macos.svg` and `icon.icns`. `DEL-09-04#REM-2` (DEL-09-04-V3-02, gated on V3-04 being
  selected) owns the packaging side.

## 6. Effort

- **Read:**
  - the brief, split plan, CONVENTIONS, RUN_BASIS §3-5 and Addenda 1-7, and PREGATHER;
  - the DEL-02-01 SoW (half B range plus the SCA sections), `_STATUS.md`, `MEMORY.md` and
    Dependencies.csv;
  - the pack rows, the gate transcript, and a few register and ruling excerpts (D-APP-108, D-APP-127);
  - about 12 frontend files, by line range;
  - short git log/show/blame checks (9b005c23a, b2b32669c, 5bd5a63ef, PRD, TYPES).
- **Total:** about 35 files or excerpts.
- **Context budget:** adequate, not tight.
