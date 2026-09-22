# T6 — Run-wide call (e): DEL-02-01 half A / half B splits

Fresh re-examination against the frozen tree `00115c719`. I formed my reading from the SoW, the
governing sources and the code before I read the halves' cells. Remaps: `R3/_work/T6_REMAPS.csv`.

## Evidence

- **Governing texts keep the legacy UI.** These all keep the loop-first UI and the legacy 3x4 matrix
  as compatibility surfaces until they are separately retired:
  - D-APP-74 ruling (`_DECISIONS/D-APP-74_RULING_2026-07-23.md:94-108`);
  - PRD FR-001 and FR-007 (`docs/PRD.md:591,602`);
  - App DIRECTIVE §4.1 (`docs/DIRECTIVE.md:234`);
  - TYPES §4 (`docs/TYPES.md:139-145`);
  - decomposition SOW-001 and SOW-005 (`_Decomposition/..._v3_2.md:171,175`).

  D-APP-74 adds that "Old-UI retirement requires separate owner acceptance after parity,
  accessibility, compatibility, and packaged Desktop evidence".
- **What the governing rulings do permit.** SCA-APP-010 and D-APP-108 (DEC-025, SOW-001) permit:
  - a frame with no header row;
  - Workbench and Pipeline presentation retired from the active shell, with the code kept;
  - (Q3) `/workbench` and `/pipeline` staying reachable by URL, unlisted and unmounted.

  D-APP-74 and TYPES §4 permit a target shell with no visual matrix.
- **No ruling covers the matrix removal.** No App register row rules the retirement of the matrix or
  the loop-first UI. I searched `_REGISTER.md` for matrix, PORTAL, loop-first, role adoption,
  `9b005c23a`, Pipeline and Workbench. `9b005c23a` touched no App `docs/` file and no App register.
- **Code history.**
  - `03e61f38f` (2026-09-05, implementing SCA-APP-010) made non-dialogue routes render the legacy
    loop-first element (`git show`).
  - `9b005c23a` (2026-09-09) removed that branch and the `?legacy=1` branch. At
    `woven-dialogue-route.tsx:16-18` the route now does `void legacy`.
  - `9b005c23a` also rewrote `agent-matrix.tsx` into a role directory with no grid (`:38-59`).
  - `WovenDialogueShell` ignores `defaultSurface` (`woven-dialogue-shell.tsx:77`).
  - Result: no live path renders PORTAL, the matrix, or the Workbench/Pipeline surfaces.

## Call

1. **Rows about the matrix or PORTAL compatibility surface are not ACCEPTED_DIVERGENCE.** No
   GOVERNING ruling permits removing that surface, and D-APP-74 requires owner acceptance first.
   The matching verdicts are `IMPLEMENTED_DIFFERENTLY` (another live mechanism) or
   `DOCUMENTED_UNIMPLEMENTED` (row and column labels absent on the live path). Both carry R4-Q4 and
   `OTHER:V3_ROLE_ADOPTION`. This matches half A.
2. **Rows about the header only keep ACCEPTED_DIVERGENCE.** SCA-APP-010 obligation 1 (no header
   row) is a GOVERNING ruling. Both halves agree, so there is no change.
3. **Rows about the `/workbench` and `/pipeline` URLs stay ACCEPTED_DIVERGENCE.** The Q3 wording
   still holds literally: reachable, no 404, unmounted. The other reading is recorded in Notes:
   Q3 was implemented as the URL showing the retired surface, and `9b005c23a` removed that. The
   Disposition is not changed.
4. **REQ-010 / CLM-020.8 (unsupported variants) splits between the halves, and both readings stay
   defensible.** The Disposition is kept, and each row gets a marker.

## Affected rows

| Key | Half | Current Disp / HDN | R3 Disp / HDN | Reason |
|---|---|---|---|---|
| CLM-017 | B | ACCEPTED_DIVERGENCE / R4-Q4 | IMPLEMENTED_DIFFERENTLY / R4-Q4 | PORTAL access removed with no ruling; same content as CLM-010.1 (A) |
| CLM-025 | B | ACCEPTED_DIVERGENCE / R4-Q4 | IMPLEMENTED_DIFFERENTLY / R4-Q4 | SEE:CLM-017 row; follows it |
| CLM-020.3 | B | ACCEPTED_DIVERGENCE / NO | IMPLEMENTED_DIFFERENTLY / R4-Q4 | Role directory replaces the 3x4 matrix; matches CLM-010.4 (A) |
| CLM-020.4 | B | ACCEPTED_DIVERGENCE / NO | DOCUMENTED_UNIMPLEMENTED / R4-Q4 | No live row labels; matches CLM-010.5 (A) |
| CLM-020.5 | B | ACCEPTED_DIVERGENCE / NO | DOCUMENTED_UNIMPLEMENTED / R4-Q4 | No live column labels; matches CLM-010.6 (A) |
| CLM-021 | B | STALE_SPECIFICATION / NO | STALE_SPECIFICATION / R4-Q4 | Matrix-test evidence went stale through `9b005c23a`; matches CLM-012.2-.5 (A) |
| CLM-020.8 | B | ACCEPTED_DIVERGENCE / NO | unchanged (marker) | Half A read IMPLEMENTED_DIFFERENTLY (CLM-010.10) |
| CLM-010.10 | A | IMPLEMENTED_DIFFERENTLY / R4-Q4 | unchanged (marker) | Half B read ACCEPTED_DIVERGENCE (CLM-020.8) |
| CLM-010.2 | A | ACCEPTED_DIVERGENCE / NO | unchanged (note) | Q3 holds literally; other reading recorded |
| CLM-020.1 | B | ACCEPTED_DIVERGENCE / NO | unchanged (note) | Same as CLM-010.2 |
| CLM-029.3 | B | ACCEPTED_DIVERGENCE / NO | unchanged (note) | SEE:CLM-020.1 row; same as above |

The CauseTag on the five changed rows goes from `SHELL_REDESIGN` to `OTHER:V3_ROLE_ADOPTION`.

**Checked and consistent, no change** (all `IMPLEMENTED_DIFFERENTLY`, `DOCUMENTED_UNIMPLEMENTED`,
`PARTIALLY_IMPLEMENTED` or `STALE_*` with R4-Q4): SEC-1 to SEC-4; CLM-003, 005, 009, 010.1,
010.4-010.9, 010.11; CLM-012.1-012.5, 015.1; CLM-019, 020.6, 020.7, 026, 029.1, 029.2; REM-4.

CLM-010.3 and CLM-020.2 are header-only and stay ACCEPTED_DIVERGENCE.

## Limits

- **CAUSE2 conflict.** The five changed rows already have `CAUSE2:OTHER:V3_ROLE_ADOPTION` in Notes,
  and Notes can only be appended to. After the CauseTag swap that token equals the primary. The
  appended note records the secondary as SHELL_REDESIGN, and the manager should reconcile it.
- **LatestDecision not changed.** It says D-APP-108 on CLM-017, 025 and 020.3-.5. The ruling that
  governs the matrix clause is arguably D-APP-74. This task's output fields do not cover it.
- **Static reach.** `REACHABILITY.csv` tags `agent-matrix.tsx` and `portal-loop-shell.tsx` as LIVE
  because of imports. The runtime render is voided at `woven-dialogue-route.tsx:18`, so the live
  readings above rest on symbol-level non-render (SYMBOL-UNREACHED), not on the import map.
- **Root D-GOV-42** (the Root record of the adoption) is not on the App GOVERNING map (RUN_BASIS §5).
  Whether it amends the App texts is R4-Q4 itself, and I did not decide it.
- **Not run.** No tests and no builds. Git was read-only against the frozen tree.
