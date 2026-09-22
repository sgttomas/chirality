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
