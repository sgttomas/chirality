# DEL-09-07 — forward-pass notes (R2, PKG-09, light worker)

Deliverable: Two-Job Runtime-Control Installer Migration and Rollback. Lifecycle `OPEN`.
Ledger: `DEL-09-07_claims.csv` (18 rows). Validator: `RESULT PASS errors=0 warnings=0`.

## Retirement basis (governing)

- **Ruling:** D-APP-127 (application of D-GOV-43, topology A2; GOVERNING per RUN_BASIS §5),
  `execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md`.
  - Lines 44-45: "Retired: the LaunchAgent and installer (DEL-09-07, APP-HOLD-1)".
  - Lines 159-173: D-APP-107 superseded in whole; DEL-09-07 "retires with the LaunchAgent under
    D-GOV-43 item 7"; "The DEL-09-07 folder, its ScopeOfWork and D-APP-104 remain immutable
    history; DEL-09-07 `_STATUS.md` records the retirement."
  - Line 182: "DEL-09-07 retired."
  - Register row D-APP-127 (`_REGISTER.md:152`) is `RULED`.
- So CONVENTIONS §2.6 (iii) applies: the ruling names the deliverable retired and preserves its
  text as history. The preserved set is the whole folder. `RETIRED_BY_RULING` is used on all
  SoW units and on one whole-section row (STATE-3) for the rest of the folder.
- The D-GOV-43 record itself (`docs/governance_harness/_DECISIONS/…`) is outside the permitted
  Root docs. It was not read. D-APP-127 quotes and applies it: OUT_OF_ROOT:docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md.
- **The lifecycle carrier agrees with the ruling.** `_STATUS.md` says `Current State: OPEN`,
  records the retirement and says "lifecycle state unchanged (OPEN)". D-APP-127 directs
  `_STATUS.md` to record the retirement and directs no lifecycle transition. App SPEC:201 /
  TYPES:235 have no RETIRED lifecycle state. The `APP-HOLD-1-INIT-DEL-09-07` row is absent
  from the frozen `APP_HOLD_REGISTER.csv`, which holds only its header. Row: STATE-1, ALIGNED.
- **Code agrees.** No installer, journal, inspector or fixture exists. On the live path, the
  App owns the Runtime service as a child process: `frontend/electron/runtime-service-host.ts:1-9`,
  `frontend/electron/main.ts:753-761`, and `frontend/electron/runtime-control-ipc.ts:10-14`,
  where the LaunchAgent verbs are retired. All three are REACH=LIVE, and none is in TOUCHED_PATHS.

## 1. Census

| ClaimType | Rows |
|---|---|
| REQUIREMENT | 6 (SEC-1, SEC-2.1-2.3, SEC-4) |
| EXCLUSION | 1 (SEC-2.4) |
| ACCEPTANCE | 8 (SEC-2.5-2.8, SEC-3.1-3.4) |
| STATE_ASSERTION | 3 (STATE-1..3) |
| REGISTER_DEFECT | 1 (REGISTER-1) |

| Disposition | Rows |
|---|---|
| RETIRED_BY_RULING | 15 (all 4 indexed units, as 14 rows, plus STATE-3) |
| ALIGNED | 1 (STATE-1) |
| STALE_SPECIFICATION | 1 (STATE-2) |
| REMAINING_STATE_MISMATCH | 1 (REGISTER-1) |

- **Split rate:** 2 of 4 units were split (SEC-2 into 8 rows for REQ-001..004 and AC-001..004;
  SEC-3 into 4 rows for VER-001..004), as the SubItems column requires. SEC-1 and SEC-4 are
  whole-section rows.
- **SEE rows:** 0.
- **Errata:** none (pass 1).

## 2. Least-confident rows

- **REGISTER-1 (LOW).** `_REFERENCES.md` records "Accepted SHA-256" pins for CONTRACT, SPEC and
  PRD, not a MATCH verdict. Checked directly: REFERENCE_HASHES `NOT_RECORDED`/`NO` is correct.
  The pins do not reproduce at `00115c719`, so the row is bookkeeping lag
  (REMAINING_STATE_MISMATCH, tie-break 2b).
  - Alternative reading: no defect. The pins sit inside the preserved-history set, and the
    validator bars RETIRED_BY_RULING on REGISTER_DEFECT.
  - `git log` shows the pins were refreshed in the retirement tranche `23b3879b3` itself.
- **STATE-2 (LOW).** `_STATUS.md:9` says "the four-document kit" is preserved unchanged.
  - The legacy four-document set was never created in this SOW_V1 folder
    (`_SEMANTIC_LENSING.md:9`).
  - If "kit" means the underscore files, `23b3879b3` edited `_REFERENCES.md` in the same
    tranche.
  - Alternative reading: ALIGNED, treating the phrase as harmless boilerplate. Minor in either
    case.

## 3. Register-defect summary

- REGISTER-1: CONTRACT, SPEC and PRD pins lag the frozen basis. The verdict is NOT_RECORDED.
  Repair is an owner choice, because D-APP-127 holds the folder as immutable history.
- There are no stale conflict tables, because the deliverable has none.
- `Dependencies.csv` rows remain `ACTIVE`, with the Root DEL-02-07/02-11 prerequisites and
  three other prerequisites `PENDING`. They are covered by STATE-3 (RETIRED_BY_RULING) as
  preserved history, not as register defects.

## 4. Direction and cause

- **CauseTag:** `A2_TOPOLOGY` on all 15 retired rows; `DOC_HYGIENE` on REGISTER-1;
  `CARRIER_PROPAGATION` on STATE-2. No `CAUSE2`.
- **DirectionEvidence:** `GOV:D-APP-127` (primary); `CTX:` done-declaration candidate OOS-14,
  which lists DEL-09-07 as retired machinery.
- **Done-declaration questions (Notes only):** Q-02 (release act / F-APP-2) touches SEC-4
  AX-003 only as context. The release fence is independent of this retired deliverable.
- **Searches:** `DECISION_HITS.csv` (D-APP-97, 104, 107, 127, D-GOV-43), `_REGISTER.md` rows
  104/107/127, the D-APP-127 record, and done-declaration lines 69-80, 212-219 and 386-399.
  No `NONE_FOUND` DirectionEvidence was needed.

## 5. Method friction

- A retired deliverable still carries a references register. MR-5/§2.7 forces
  REMAINING_STATE_MISMATCH or STALE_SPECIFICATION, even where the ruling freezes the register
  as history.
  - Proposal: allow RETIRED_BY_RULING on REGISTER_DEFECT rows inside a preserved set, or
    exempt preserved sets from the per-deliverable hash row.
- The V-SUBITEMS rule forces 12 near-identical RETIRED_BY_RULING rows, where §2.6 (iii) allows
  one whole-section row per ruling. The two rules pull in different directions for retired
  deliverables.
  - Proposal: let one whole-section RETIRED_BY_RULING row satisfy V-SUBITEMS.
- Brief hint: "RETIRED_BY_RULING only if so." Confirmed from the governing record, not from
  the CONVENTIONS §10 list.

## 6. Effort

About 15 files or ranges read: the brief, CONVENTIONS, RUN_BASIS §3-§5 and addenda, the
evidence-pack rows, 7 deliverable files, D-APP-127, 3 register rows, 3 electron sources, the
verify script, package.json, AGENTS.md lines 194-200, decomposition greps and done-declaration
excerpts. Context budget was not tight.

## Coverage gaps

- **Decomposition (GOVERNING), outside the preserved set.**
  `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` still lists these as
  live:
  - SOW-080 as `IN` (lines 250, 483);
  - DEL-09-07 (line 384);
  - OI-003 and OI-007 with the SOW-080 installer (lines 597, 601);
  - OBJ-008 mapping SOW-080 (line 269).

  D-APP-127 names no decomposition revision. This falls under MR-11 for the EXT item-5 unit
  `SOW:SOW-080`, which is not owned by this ledger. The EXT manager should confirm it is
  covered there.
- **`projects/chirality-app-dev/AGENTS.md:196-199`.** D-APP-127 flagged its D-APP-107
  preflight paragraph for revision. At the frozen basis the paragraph already records the
  supersession. No gap for this ledger; noted for EXT/PRODAGENTS if relevant.
