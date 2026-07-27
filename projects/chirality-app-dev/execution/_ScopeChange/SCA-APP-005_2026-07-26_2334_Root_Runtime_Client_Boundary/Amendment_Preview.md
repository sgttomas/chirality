# SCA-APP-005 Exact Amendment — Revision 2

**Gate:** 3
**Status:** `APPROVED_AND_APPLIED`
**Date:** 2026-07-27
**Accepted envelope:** `Gate_2_Exhaustive_Seam_Matrix.md`, Revision 2
**Owner ruling:** “I Approve the corrected SCA-APP-005 Revision 2 envelope.”
**Provenance:** Ryan Tufts, in-session owner ruling, 2026-07-27

## Exact amendment identity

The exact Gate-3 amendment is the complete set of post-change cells and
paragraphs in the authoritative App decomposition for the entities below,
plus the corresponding post-change metadata in the 25 affected context
files. Any byte outside this enumerated entity/section set is not authorized
by this amendment.

### Direct entities

- 31 scope items, in both SSOW and Scope Ledger:
  `SOW-009`, `SOW-010`, `SOW-011`, `SOW-012`, `SOW-014`, `SOW-015`,
  `SOW-016`, `SOW-018`, `SOW-019`, `SOW-020`, `SOW-021`, `SOW-037`,
  `SOW-038`, `SOW-039`, `SOW-041`, `SOW-044`, `SOW-045`, `SOW-046`,
  `SOW-047`, `SOW-049`, `SOW-051`, `SOW-052`, `SOW-053`, `SOW-055`,
  `SOW-056`, `SOW-057`, `SOW-058`, `SOW-059`, `SOW-061`, `SOW-062`,
  `SOW-063`.
- Packages: `PKG-03`, `PKG-04`, `PKG-05`, `PKG-06`, `PKG-08`.
- Deliverables: `DEL-03-01`, `DEL-03-02`, `DEL-03-04`, `DEL-04-01`,
  `DEL-04-02`, `DEL-04-03`, `DEL-04-05`, `DEL-05-01`, `DEL-05-02`,
  `DEL-05-03`, `DEL-05-05`, `DEL-06-01`, `DEL-06-02`, `DEL-06-05`,
  `DEL-06-06`, `DEL-08-04`, `DEL-08-05`.
- Objectives: `OBJ-002`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-007`.

### Cross-cutting exact sections

- Intake paragraphs 2 and 3 only.
- Hard constraints for the R0/R1 App slice, runtime-audit posture, and bounded
  Pi exception only.
- Only the vocabulary rows classified `MODIFY` in the Revision 2 matrix.
- Invariant-family rows 506, 509, 510, 511, and 513 at the accepted basis.
- SPEC/TYPES/PLAN notes corresponding to accepted-basis rows 519, 523, 527.
- Acceptance rows for SPEC and TYPES only; PLAN sequencing remains unchanged.
- `OI-002`, `OI-006`, `OI-007`.
- The R0/R1 and shared-runtime downstream notes.
- Additive `DEC-021` and the dated change-log entry.

Historical `DEC-019`, all Revision 2 `NO_CHANGE` rows, and U1–U5 remain
unchanged or explicitly unresolved.

## Context metadata

All existing `_CONTEXT.md` files in PKG-03, PKG-04, PKG-05, PKG-06, and
PKG-08 receive package-scope parity: 25 files total. The 17 directly amended
deliverables also receive exact deliverable-scope, anticipated-artifact, and
context-note parity. The remaining 8 contexts receive package-scope parity
only.

## Authority partition preserved

The amendment transcribes the D-GOV-20 boundary without inventing U1–U5:

- the daemon owns generic engines, credentials, sessions, delegation, tools,
  turn locks, interruption, model residency, and operational runtime state;
- App/project authority, instructions, permissions, approvals, project-
  specific deterministic acts, human gates, AgentRuns, and acceptance
  evidence remain checkout-contained;
- App is a runtime client and packaged-daemon provider, not the generic
  semantic owner.

## Deterministic concordance

Run:

```sh
bash projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-005_2026-07-26_2334_Root_Runtime_Client_Boundary/check_gate3_concordance.sh
```

Recorded result: `PASS`.
