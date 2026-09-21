# V-DEL-07-03 — verifier shard notes (DEL-07-03)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a30 | 11 | 8 | 2 | 1 |
| b | 5 | 3 | 2 | 0 |
| c | 3 | 3 | 0 | 0 |
| **Total** | **19** | **14** | **4** | **1** |

Refutations on a verdict field (Addendum 3): 1 of 19 distinct items (`CLM-009.1`, Disposition).
Field-only refutations: 3 (`CLM-014` RemainingWork, `CLM-009.10` Notes, `CLM-009.7` AssessmentEvidence).
CONTESTED: `CLM-030` DirectionEvidence.

## (ii) Patterns

1. **Missed existing fixtures (REQ-001).** The worker did not find the invalid-name and
   missing-`_STATUS.md` fixtures in the deliverables route test (`DEL-07-99_No_Status`,
   `D07-03_Invalid_Folder`, route test lines 243-263, which assert that only DEL-07-03 is returned).
   This makes `CLM-009.1` ALIGNED, not PARTIALLY_IMPLEMENTED (CauseTag NONE). It also removes the
   REQ-001 half of `CLM-014`'s RemainingWork. `CLM-014` stays PARTIALLY_IMPLEMENTED because no
   REQ-008 path or root containment fixture exists. The same misreading may affect `CLM-017`, `CLM-023`
   and `CAP-WORKSPACE-011`, which were not in this shard. R3 should check them.
2. **Small annotation errors on rows whose Disposition is correct.**
   - `CLM-009.7` marks INSP-03's `TBD` (not assessed) as OVERTAKEN. Under MR-1, no conclusion
     means NOT APPLICABLE.
   - `CLM-009.10` Notes calls `document-view.tsx` a legacy app-shell consumer. The live woven right
     panel also renders it (`right-panel.tsx:10,191`).
   - `CLM-030` cites `GOV:D-APP-68` for the fail-closed OPEN-baseline resolver. D-APP-68 only
     confirms D-GOV-16's conversion authority, and the row itself tags D-APP-68 `(context)`. Both
     readings are recorded.

Confirmed:
- Hash recomputes: CONTRACT/SPEC/PRD do not match, and DIRECTIVE/TYPES/PLAN reproduce.
- STALE_SPECIFICATION on the REF-006 "is MATCH" restatements (tie-break rule 3, `SEE:REGISTER-1`).
- SEC-3's stale "await" for DEP-019/020 (applied 2026-09-05 under D-APP-109).
- SEC-1/SEC-2: `governed-workflow.ts` is TEST_ONLY, has no product importer, and the live
  Workflows view renders MethodLibraryView. Their PARTIALLY_IMPLEMENTED holds, and R4-Q1 correctly
  does not apply.
- None of the cited files is in TOUCHED_PATHS, so PostReleaseBasis NO is correct.

## (iii) Effort

About 20 file reads/greps. Frozen tree: SoW, `_REFERENCES`, `_STATUS`, `_DEPENDENCIES`,
`_CONTEXT`, INSP-03, `filesystem.ts`, `governed-workflow.ts`, `right-panel.tsx`, two test files,
the deliverables route, `workflow-store.ts`, decomposition L251/359/484, and D-APP-68.
Read-only `git blame`/`log` on `filesystem.ts`, the route test and PRD. The context budget was not tight.
