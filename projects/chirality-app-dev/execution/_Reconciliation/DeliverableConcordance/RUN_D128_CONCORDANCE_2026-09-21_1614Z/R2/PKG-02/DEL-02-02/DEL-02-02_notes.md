# DEL-02-02 — forward notes (RUN_D128 R2 PKG-02)

Deliverable: DEL-02-02, which keeps the folder name "Workbench and Pipeline Selection UX". The applied
display name is "Right-Panel Coordination, Workflows, and Proposal UX". Basis: frozen tree at
`00115c719`. The ledger is `DEL-02-02_claims.csv` (forward pass, sealed after validation). No errata
file exists yet.

## 1. Census

- **Rows:** 62, covering all 38 indexed units: SEC 5, CLM 28, REMTXT 2, REM 3. There are 7
  run-local `REGISTER-n` rows and no `STATE-n` rows.
- **Split rate:** 5 of 38 units are split (13%), giving 22 split rows:
  - CLM-004 (Conditions table), 4 rows;
  - CLM-010 (REQ-001..REQ-011), 11 rows;
  - CLM-014 (amendment text and AC-001), 2 rows;
  - CLM-021 (reconciliation note and VER-001), 2 rows;
  - CLM-028 (conflict table), 3 rows.
  - No `SubItems` unit needs k ≥ 2 rows: CLM-014 and CLM-021 each list one item.
- **SEE rows (counted separately):** 5.
  - `SEE:DEL-02-02#REGISTER-3` on CLM-001, CLM-004.3, CLM-022 and CLM-028.2.
  - `SEE:DEL-02-02#CLM-007` on CLM-021.1.

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 25 |
| CONTEXT_CLAIM | 13 |
| REGISTER_DEFECT | 7 |
| ACCEPTANCE | 6 |
| STATE_ASSERTION | 6 |
| REMAINING_WORK | 4 |
| EXCLUSION | 1 |

| Disposition | Rows |
|---|---:|
| RETIRED_BY_RULING | 25 |
| STALE_SPECIFICATION | 17 (5 are SEE rows) |
| NOT_AUDITABLE | 7 |
| REMAINING_STATE_MISMATCH | 5 |
| PARTIALLY_IMPLEMENTED | 4 |
| ALIGNED | 2 |
| IMPLEMENTED_DIFFERENTLY | 1 |
| UNKNOWN | 1 |

- **HumanDecisionNeeded other than NO:** 9 rows.
  - `R4-Q4` alone: 4 (CLM-010.2, CLM-019, CLM-024, CLM-027).
  - `R4; R4-Q4`: 2 (SEC-3, SEC-4).
  - `R4`: 1 (REM-3).
  - `D-APP-117; R4`: 1 (REM-1).
  - `D-APP-117; R4-Q5`: 1 (REM-2).
- **R4-Q1:** not cited. No claim is met only by `LEGACY_ONLY` code; every code citation is `LIVE`
  or `TEST_ONLY`.
- **Sealed vs errata-applied figures:** not applicable (no errata).

**The central finding (read first).** The pack tags `workbench-surface.tsx`,
`pipeline-surface.tsx`, `deliverable-api.ts` and `task-scope.ts` `LIVE`, but only through imports.
- `WorkbenchSurface` and `PipelineSurface` are built only by `createTertiarySidebarTabs`, inside
  LoopShell, LoopTertiaryShell and PortalLoopShell.
- Those shells reach the routes only as the `legacy` prop, which `WovenDialogueRoute` discards
  (`woven-dialogue-route.tsx:18`, `void legacy`).
- `/workbench` and `/pipeline` therefore render only the dialogue shell (`data-woven-surface="dialogue"`).
- Up to `9b005c23a` (2026-09-09), the T1 route (`03e61f38f`) still rendered the legacy shell at those
  URLs.

Every Workbench/Pipeline row keeps the pack's `LIVE` tag and records `SYMBOL-UNREACHED` in Notes. The
older SoW clauses are `RETIRED_BY_RULING` (D-APP-108 plus the SCA-APP-010 Gate-5 section of the SoW);
see §5 for the tension with PRD and SPEC.

## 2. Least-confident rows (LOW)

| Row | Verdict | Alternative reading |
|---|---|---|
| CLM-007 | STALE_SPECIFICATION ("the nine-row derivative register exists"; the register now has 22 rows) | The 2026-07-12 dated heading makes this a snapshot-true note (MR-8(iv)), so it would be a REGISTER row with REMAINING_STATE_MISMATCH. |
| CLM-021.1 | Repeats CLM-007 (SEE row) | Same as CLM-007. |
| CLM-017 | STALE_SPECIFICATION ("Declared upstream dependencies: TBD" while 21 ACTIVE rows exist) | "No *accepted* edges" may be literally true, since no row is satisfaction-closed or owner-accepted. The row would then be NOT_AUDITABLE. |
| REGISTER-6 | REMAINING_STATE_MISMATCH (`_DEPENDENCIES.md` L14/L18 "TBD - no accepted dependency edges") | Same "accepted" reading, under which the header is accurate and the row is void. |
| CLM-021.2 | UNKNOWN (no record that the VER-001 conversion checks and human review ran) | DOCUMENTED_UNIMPLEMENTED, if the absence of a record is taken as evidence they never ran. |

MEDIUM rows that a verifier should look at:
- **All 25 `RETIRED_BY_RULING` rows.** The alternative is `AUTHORITY_CONFLICT` (R4): SCA-APP-010 is a
  scope-change record, which ranks seventh in DIRECTIVE §0, and it retires surfaces that PRD FR-010..
  FR-013 and SPEC §17.3(6)/§17.9 still require. I applied MR-11 because D-APP-108 names this
  deliverable and rules on the retired routes (Q3).
- **CLM-010.2.** The alternative is `AUTHORITY_CONFLICT` with R4-Q4 instead of
  `IMPLEMENTED_DIFFERENTLY`.

## 3. Register-defect summary

| Key | Defect | Disposition |
|---|---|---|
| REGISTER-1 | `_REFERENCES.md` REF-002 CONTRACT hash MATCH does not reproduce (recorded `fa8fc9dc…`, recomputed `57411f8d…`) | STALE_SPECIFICATION |
| REGISTER-2 | REF-003 SPEC hash MATCH does not reproduce (`01e1c75c…` vs `8b0d805b…`) | STALE_SPECIFICATION |
| REGISTER-3 | REF-006 PRD hash MATCH does not reproduce (`8649ccba…` vs `17ca3f3c…`); SoW restatements point here | STALE_SPECIFICATION |
| REGISTER-4 | `_DEPENDENCIES.md` Lifecycle Summary says 8 PENDING and that DEP-02-02-021 is waiting; the CSV has 7 PENDING and DEP-02-02-021 SATISFIED | REMAINING_STATE_MISMATCH |
| REGISTER-5 | DEP-02-02-013 is PENDING on DEL-07-03-V3-01, which landed 2026-09-06 | REMAINING_STATE_MISMATCH |
| REGISTER-6 | `_DEPENDENCIES.md` Declared Upstream/Downstream still say "TBD - no accepted edges extracted" | REMAINING_STATE_MISMATCH (LOW) |
| REGISTER-7 | `_REFERENCES.md` reuses REF-009 and REF-010 for two different sources each | REMAINING_STATE_MISMATCH |

The pack (item 3) covers only CONTRACT, SPEC and PRD. DIRECTIVE, TYPES, PLAN and the workflow
references were not recomputed. REGISTER-1..3 take `STALE_SPECIFICATION` for two reasons:
- tie-break rule 1 lists "a hash recorded as MATCH" as a now-false present fact;
- the validator's SEE check needs the REGISTER-3 target to carry the same Disposition as the SoW
  restatements.

## 4. Direction and cause

- **Primary CauseTags:**
  - SHELL_REDESIGN: 28 (the Workbench/Pipeline retirement under SCA-APP-010 and D-APP-108);
  - DOC_HYGIENE: 11 (hashes and register bookkeeping);
  - CARRIER_PROPAGATION: 7;
  - LIFECYCLE_GATE_PENDING: 3 (SEC-3, SEC-4, REM-1);
  - V3_RELEASE_SCOPE: 2 (CLM-010.2, REM-3);
  - PRE_V3_DRIFT: 2 (CLM-020, whose Guidance.md was removed in the 2026-07-13 four-document merge
    `96c141719`, and CLM-021.2).
- **CAUSE2 secondaries:**
  - V3_RELEASE_SCOPE on SEC-3 and SEC-4;
  - CARRIER_PROPAGATION on CLM-002, CLM-014.2, CLM-020, REMTXT-1 and REM-3;
  - SHELL_REDESIGN on CLM-010.2;
  - A2_TOPOLOGY on REMTXT-2;
  - NATIVE_DELEGATION on REM-1;
  - CODEX_SOLE_ENGINE on REM-2.
- **GOVERNING rulings used as `GOV:`:** D-APP-108 (SCA-APP-010 seating and Q3), D-APP-109 (dependency
  re-extraction) and D-APP-127 (D-APP-88 helper bundle superseded, so REMTXT-2 is `MOOT:D-APP-127`).
- **MOOT:D-GOV-43 on REM-2.** It rests on the DEL-05-02 `_STATUS.md` History of 2026-09-12: the Root
  DEL-02-10 schema-v2 acceptance was replaced by the D-GOV-43 extensible representation, and "no Root
  acceptance is awaited". The D-APP-127 ruling itself does not name DEL-02-10.
- **CONTEXT records used (`CTX:`):**
  - `execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/pkg02-agents-presentation/OWNER_DIRECTION.md`.
    This owner direction, in commit `6670864ab`, removed currency, source, identifier, evidence and
    engine metadata from Agents cards. It explains why the SCA-APP-010 "source, authority class,
    responsible reference, currency, and evidence" text is unmet. It is not a register ruling, so
    SEC-3, SEC-4 and REM-1 carry R4.
  - `execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/MANAGER_RETURN.md`, the v3
    one-role conversation with HELP_HUMAN as default. It explains the replaced agent matrix and the
    method-library Workflows tab.
  - The DEL-05-02 `_STATUS.md` History of 2026-09-12, used on REM-2.
- **`NONE_FOUND` searches:**
  - REGISTER-1..3, CLM-001, CLM-004.3, CLM-022 and CLM-028.2: I searched `_REGISTER.md` for a
    reference re-reconciliation of DEL-02-02 after corpus v16, and read the v3 adoption return. The
    only thing found is a corpus v21 *candidate*, which is not an accepted refresh.
  - REGISTER-4, -5 and -7: I searched `_REGISTER.md`, looking at D-APP-109/110 and later rows, and
    found nothing.
  - CLM-021.2: I searched the deliverable folder, `_run_records` and `git log -S VER-001` on the SoW.
    Only the migration commit `96c141719` turned up, with no validation record.
- **No UNRECORDED_JUDGMENT rows.**

## 5. Method friction

- **Coverage gaps (for R3).**
  - The v3 method library and draft registration (`method-library-view.tsx`,
    `workflow-draft-review.tsx`, `lib/shell/workflow-library.ts` and the `api/harness/methods`
    routes) are live in DEL-02-02's Workflows tab. No DEL-02-02 unit specifies them; they appear only
    as a divergence on SEC-3, SEC-4 and REM-3. Their scope owner is probably DEL-07-03, DEL-08-02 or
    a Runtime method-catalog deliverable.
  - The composer role picker (`chat-panel.tsx:2124` → `persona-picker.tsx`, with HELP_HUMAN as
    default) is the live Agent 0/1/2 role entry. DEL-02-02's applied row L308 claims role entry, but
    REM-1 says it is seated on DEL-02-05 and DEL-08-04 (see also DEP-02-02-019). Ownership is
    unresolved.
  - The Plan tab (`native-plan-panel.tsx`) in the right panel is not in any DEL-02-02 unit.
- **Splitting of SEC units.** SEC-2 and SEC-4 each hold six numbered acceptance obligations whose
  findings differ. They are neither REQ/AC/VER items nor a table, so §2.2 does not allow a split. Each
  gets one row, with per-obligation findings in Notes. *Proposal:* also allow splitting of numbered
  acceptance-obligation lists in SCA Gate-5 sections.
- **STATE-n for a sentence inside an indexed unit.** REM-1's Depends line says "Row L294 was not
  amended … role entry … unseated here". That is now false: L294 is a PKG-01 heading, and applied row
  L308 includes role entry. §2.2 limits `STATE-n` to assertions outside indexed units, so I recorded
  it as `ALSO:STALE_SPECIFICATION` in the REM-1 Notes. *Proposal:* allow one `STATE-n` row for a
  separable false sentence embedded in a REMAINING_WORK unit.
- **RETIRED_BY_RULING vs DIRECTIVE §0.** SCA-APP-010 (a scope-change record) retires surfaces that
  higher-ranked PRD and SPEC text still requires. I used MR-11 because D-APP-108 explicitly addresses
  the deliverable and the retired routes. R3 should decide whether the PKG-02 managers treat this
  uniformly.
- **The REACH module-versus-symbol caveat was material here.** Four modules are tagged LIVE, but their
  claimed symbols are never rendered.

## 6. Effort

- **Read:** about 45 files or ranges. These were:
  - the deliverable's SoW, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `MEMORY.md`, INSP-03,
    `_DEPENDENCIES.md` (parts), `Dependencies.csv` (by script) and one run record;
  - five ruling records and register rows;
  - SPEC §17.3–17.9, PRD FR rows and DIRECTIVE §0;
  - about 15 frontend source and test files, as line ranges;
  - the pack files, the PREGATHER and the CONVENTIONS and RUN_BASIS files.
- **Git:** read-only `log` and `show` on 8 commits.
- **Context budget:** moderate, not tight.
