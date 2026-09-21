# DEL-05-01 — forward-pass notes (R2, PKG-05)

Deliverable: DEL-05-01 Canonical Session Folder and Legacy Session Migration. Frozen basis `00115c719`.
Worker: TASK (Type 2), pass 1. The RUN_BASIS Addendum 6 notice (R4-Q1 legacy-versus-live subject test)
arrived **before** sealing and was applied to every row.

## 1. Census

- Rows: 56. That is 33 indexed units (50 rows) plus 6 run-local rows (REGISTER-1..5, STATE-1).
- Split rate: 3 of 33 units split (9%).
  - CLM-010: the requirements table, 16 rows R001..R016.
  - CLM-014: the guard paragraph plus AC-001.
  - CLM-021: the records plus VER-001.
  - The SubItems units (CLM-014 AC-001, CLM-021 VER-001) each have k = 1.
- SEE rows, counted separately: 13 rows carry `SEE:`. They are CLM-004, 005, 009, 011, 016, 019, 020, 021.2, 024, 025, 027, 030 and REGISTER-4.
  - Two of these also carry their own findings: CLM-004 (its SEE points to REGISTER-1 for the MATCH clause) and CLM-024.
  - The other 11 point at a row that holds the same statement.

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 27 |
| CONTEXT_CLAIM | 14 |
| STATE_ASSERTION | 5 |
| REGISTER_DEFECT | 5 |
| ACCEPTANCE | 4 |
| REMAINING_WORK | 1 |

| Disposition | Rows |
|---|---:|
| STALE_SPECIFICATION | 26 |
| NOT_AUDITABLE | 10 |
| ALIGNED | 9 |
| PARTIALLY_IMPLEMENTED | 5 |
| STALE_VERIFICATION | 3 |
| IMPLEMENTED_DIFFERENTLY | 1 |
| REMAINING_STATE_MISMATCH | 1 |
| AUTHORITY_CONFLICT | 1 |

- Confidence: HIGH 31, MEDIUM 25, LOW 0.
- HumanDecisionNeeded:
  - `NO` 33;
  - `D-APP-73; R4-Q1` 12;
  - `R4` 4;
  - `R4-Q1` 3;
  - `R4; R4-Q1` 2;
  - `D-APP-73` 2.
- No errata file yet.

## 2. Least-confident rows (with the alternative reading)

No row is LOW. These are the MEDIUM rows where another reading is live:

- **STATE-1 (AUTHORITY_CONFLICT).**
  - Alternative: `STALE_SPECIFICATION`, on the reading that "daemon-centralized" is only a name for the
    central Runtime store, which still exists under A2.
  - Chosen because `_CONTEXT.md` mirrors GOVERNING decomposition row L322 ("daemon sessions remain
    Root-owned"). D-GOV-43/D-APP-127 retired daemon mode and, per App surfaces, Root DEL-02-11. They do so
    without naming L322 or DEL-05-01.
- **REM-1 (STALE_SPECIFICATION).**
  - Alternative: `REMAINING_STATE_MISMATCH`.
  - Chosen because the item's open status is not contradicted: migration is still incomplete on the live
    path. The false fact is its gate, which waits on a retired Root dependency (tie-break rule 1).
  - MechanicallyUnblocked is `NO`, with `MOOT:D-APP-127`.
- **CLM-010.3 (PARTIALLY_IMPLEMENTED, UNRECORDED_JUDGMENT).**
  - Alternative: `STALE_SPECIFICATION` via MR-11 (D-APP-73), with the bootstrap gap treated as REM-1 residual.
  - Chosen because SPEC 25.4 (GOVERNING) requires lazy migration of legacy project-local records, and the live
    bootstrap declares no legacy roots. So the GOVERNING requirement is only partly met on the live path.
- **CLM-010.2 (PARTIALLY_IMPLEMENTED).**
  - Alternative: `STALE_SPECIFICATION` if SPEC 8.2's subfolder layout is taken as superseded by 25.4.
  - Neither SPEC 25.4 nor D-APP-73 speaks to turns/, artifacts/ or sdk/. Routed to R4.
- **CLM-010.9 (IMPLEMENTED_DIFFERENTLY).**
  - Alternative: `ALIGNED`, on the reading that the SDK-conditioned clause simply does not apply under the
    Codex sole engine.
- **CLM-031 (ALIGNED).**
  - Alternative: `STALE_SPECIFICATION`, because the cited path is a deprecated facade (FACADE_DEPRECATION).
  - The facade still re-exports `SessionRecord`, so the pointer is indirect but not false.
- **CLM-010.5 / 010.13 (ALIGNED).**
  - No focused live-path test was located. The conclusion rests on code inspection only.

## 3. Register-defect summary

- **REGISTER-1.** `_REFERENCES.md` still records MATCH for CONTRACT, SPEC and PRD, but those hashes do not
  reproduce (`HASH-RECOMPUTE@00115c719`).
  - I also recomputed DIRECTIVE, TYPES, PLAN and the three `workflows/software-decomp` refs. All six
    reproduce.
- **REGISTER-2.** DEP-05-01-006 is marked SATISFIED as the "current" storage implementation
  (`session-manager.ts`). That module is LEGACY_ONLY.
- **REGISTER-3.** DEP-05-01-009 and `_DEPENDENCIES.md:62` still assert flat-record removal. The A13 tranche
  amended the SoW but not the register.
- **REGISTER-4.** DEP-05-01-013 is still PENDING on a "Root-owned daemon-centralized session store". Its
  premise is retired under D-GOV-43/A2.
- **REGISTER-5.** `_STATUS.md` shows Last Updated 2026-09-03, and none of the five carriers records the
  D-APP-127 application (all NO in the map). This is bookkeeping lag (tie-break 2b).

## 4. Direction and cause

- **Main finding.** On the live path, sessions are stored by the Runtime `SessionStore`, reached through
  `app-owned-composition.ts:169`. The store lives at `<userData>/runtime/projects/<projectId>/sessions`
  (SPEC 25.4, D-APP-73).
  - The App `FileSessionManager` (`session-manager.ts`) is constructed only by LEGACY_ONLY `runtime.ts`.
    The only live symbol in that file is `assertProjectRootAccessible`, which the working-root routes use.
  - The SoW is written around the App module and D-APP-41 (project-local, eager, CHIRALITY_SESSION_ROOT).
  - D-APP-73 (RULED 2026-07-22) explicitly makes D-APP-41 "immutable historical authority" and extends it
    prospectively to a central store with lazy, non-destructive migration.
  - So MR-11 applies: stale SoW text is `STALE_SPECIFICATION` with LatestDecision D-APP-73.
- **Main CauseTag.** `PRE_V3_DRIFT` (25 rows): the divergence dates from 2026-07-22/23 (`8b3643e6c`,
  `99fe2edae`), with `CAUSE2:RUNTIME_EXTRACTION`.
- **Other CauseTags:**
  - `CARRIER_PROPAGATION`: CLM-026, CLM-032, REGISTER-3, REGISTER-5.
  - `A2_TOPOLOGY`: REM-1, REGISTER-4, STATE-1.
  - `CODEX_SOLE_ENGINE`: CLM-010.9.
  - `RUNTIME_EXTRACTION` as primary: CLM-010.10.
  - `DOC_HYGIENE`: CLM-011, REGISTER-1.
  - `UNRECORDED_JUDGMENT`: CLM-010.3.
- **v3-era finding.** The 2026-09-03 A13 amendment and the V3-01 code landed in the LEGACY_ONLY App module.
  CLM-032 states that D-APP-41's project-local canonical storage and first-touch conversion "remain in force".
  That was six weeks after D-APP-73.
  - The live Runtime migration has no duplicate merge, no `legacySource` hash marker and no changed-flat
    diagnostic (CLM-010.10).
- **Live gap.** `bootstrap-project.ts:43-53` (2026-09-10) writes manifests with no `legacySessionRoots`. So
  for bootstrapped projects the Runtime never reads legacy records.
  - The v2 App stored sessions under `process.cwd()/.chirality/sessions`, not under the project. Only the
    app-dev manifest names that root (`frontend/.chirality/sessions`).
- **CONTEXT and GOVERNING records used:**
  - A13 steer: `plans/steers/chirality_app_v3_app_ruling_record_a13_2026-09-03.md`, CONTEXT per RUN_BASIS §5.
  - `AgentRuns/APPDEV_V3_NODE_D_2026-09-03/`.
  - `AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/MAPPING.md`.
  - App surfaces DEL-03-02 and DEL-03-03 `_STATUS.md:14`, which record Root DEL-02-11 as retired under
    D-GOV-43.
  - SPEC 25.1 and 25.4.
- **Searches behind each `NONE_FOUND`:**
  - Searched `_REGISTER.md` for the D-APP-41, D-APP-73, D-APP-127 and D-APP-116 rows, and for "session"
    together with legacy, migration, central or daemon.
  - Grepped CONTEXT AgentRuns (`APP_V3_*`, `APPDEV_V3_NODE_*`, `CHIRALITY_V3_APP_ADOPTION_20260909`,
    `CODEX_MVP_PRODUCT/PACKAGING_20260910`, `APP_V3_CODEX_HOST_REPLATFORM_20260912`) and `plans/steers` for
    `legacySessionRoots`, "legacy session" and `.chirality/sessions`.
  - None records a direction on bootstrap legacy roots (CLM-010.3), on the central folder layout
    (CLM-010.2), or on a corpus refresh (REGISTER-1, CLM-011).
  - A13 has no row in the App decision register.
- **PostReleaseBasis.** `NO` on every row.
  - `session-store.ts` is on `TOUCHED_PATHS.csv` (`da95ec194`, lines 6-8 and 128-158).
  - Blame of every relied-on range (65-100, 102-121, 160-178, 213-226, 644-667, 911-1062, 1111-1135) shows
    only `8b3643e6c`, `99fe2edae`, `9b005c23a` and `e8ed4abb4`.
  - I dropped a citation to the touched range 128-158 (application-tools.json) rather than rely on it.
- **Addendum 6 applied.**
  - `R4-Q1` is cited on 17 rows where the project-local behaviour the text requires is met only by
    LEGACY_ONLY code, each with `ALSO_MODULE:ALIGNED`.
  - CLM-014.1 does not cite it: the live Runtime `assertSafeIdentifier` meets the guarantee.

## 5. Method friction

- **R4-Q1 on mixed rows.** Several rows are met in part by LIVE code and in full only by LEGACY_ONLY code
  (CLM-010.3, 010.10). I cited `R4-Q1` there too, reading "the only code meeting the claim" as the code
  that meets the whole claim.
  - Proposal: state explicitly whether a partial live match suppresses R4-Q1.
- **MR-11 inside one GOVERNING document.** SPEC 8.2 (project-local, unamended) and SPEC 25.4 (central, from
  D-APP-73) are both GOVERNING. The deciding fact was that D-APP-73 names D-APP-41.
  - Proposal: add a note that an intra-SPEC split resolved by a ruling naming the older basis is MR-11, not
    AUTHORITY_CONFLICT.
- **Owner rulings in plans/steers.** The A13 ruling-record class (`plans/steers/..._a*.md`) is CONTEXT, but
  A13 is an owner K-AUTH-1 ruling that amended SoW rows. Only the register and its ruling records are
  GOVERNING.
  - Proposal: confirm whether A13-style owner rulings that were never registered stay CONTEXT.
- **Coverage gaps (no forward row owns them):**
  - v2→v3 migration of the packaged App's cwd-based v2 session store for end users is not named by any SoW
    unit. It sits between REM-1 and PKG-09 upgrade work.
  - `SessionStore.delete` tombstones (`.deleted/<id>.json`) are live, product-visible deletion state that
    no DEL-05-01 text describes.
  - `list()` uses readdir order when a project-local directory record and a retained flat file share a
    sessionId, so in principle the flat file could be read as the list source. This was not tested; noted
    only.

## 6. Effort

- About 45 files or ranges read. They cover the deliverable folder, the evidence pack, CONVENTIONS and
  RUN_BASIS, the Runtime `session-store.ts`, project registry and bootstrap, App routes and the port, SPEC 8
  and 25, the D-APP-73 and D-APP-127 records, and the test names.
- `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` (78 KB) were not read in full. They hold no indexed units.
- The context budget was adequate but not loose.
