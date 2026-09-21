# V-SHARD-DEL-02-03-1: verifier notes (RUN_D128 R2 PKG-02, DEL-02-03)

Evidence-only. No ledger, notes, reverse or errata file was edited. Frozen tree only. Git use was read-only `log`, `show` and `blame -L`.

## (i) Counts

| Class | Items | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (LOW, self-flag, UNKNOWN, REMAINING_WORK) | 4 | 3 | 0 | 1 (REM-1, MechanicallyUnblocked) |
| a30 (other non-ALIGNED sample) | 12 | 10 | 0 | 2 (CLM-003 and CLM-005, RemainingWork) |
| b (unselected ALIGNED sample) | 2 | 2 | 0 | 0 |
| c (reverse responses) | 7 | 7 | 0 | 0 |
| **Total** | **25** | **22** | **0** | **3** |

- **Verdict-field refutations (Disposition or Response):** none.
- **Disposition CONTESTED:** none. All three CONTESTED items are on non-verdict fields.
- **Reverse responses:** all 7 hold (CLAIMED_BY, PARTIAL, and the claim each one names).

## (ii) Patterns

1. **The live path was checked, and the ledger's reading holds.**
   - The ledger's `SYMBOL-UNREACHED` reasoning reproduces at the frozen tree:
     - `WovenDialogueRoute` discards the `legacy` prop (`void legacy`, woven-dialogue-route.tsx:18).
     - `PipelineSurface` and `WorkbenchSurface` are constructed only in `createTertiarySidebarTabs`, which is called only by LoopShell, LoopTertiaryShell and PortalLoopShell. All three are passed as that discarded prop.
   - REACH tags on every cited module match `REACHABILITY.csv` (all LIVE).
   - No cited file is in `TOUCHED_PATHS.csv`, so `PostReleaseBasis = NO` holds throughout.
   - Examples: CLM-004.2, CLM-009.8, CLM-009.9, CLM-009.13.
2. **The not-found fallback page is a missed live surface.**
   - `app/not-found.tsx` renders the legacy `AppShell`. That brings in two things:
     - the `ShellFrame` working-root bar (Working Root input, Apply Path, Choose Folder, **Clear**), because `AppShell` passes no `renderWorkspaceContent`;
     - the `WorkspaceSidebar`, whose Document tab renders `LegacyDocumentView`. That view fetches and shows `/api/project/deliverables`.
   - So "no live Clear control" and "the deliverable roster has no rendered live consumer" are false on that route. They are true everywhere else.
   - This changes no Disposition. It is CONTESTED on RemainingWork for CLM-003 and CLM-005, and noted in ConventionIssue for CLM-019.
   - Outside my items, CLM-009.1's Notes say Clear "renders only by the unrendered LoopShell/PortalLoopShell". That is factually incomplete for the same reason.
   - Whether a 404 fallback counts as the product path is not defined by the conventions. It is worth one line in the §2.3 rule.
3. **MechanicallyUnblocked on REM rows.**
   - REM-1's `NO` rests on the prose `Depends` entry DEL-02-04-V3-01. The only written gate (DEL-02-02-V3-03 landed) is satisfied (DEL-02-02 `_STATUS.md:52`).
   - `Dependencies.csv` has no PREREQUISITE rows, so a literal reading of §2.5 gives `YES`.
   - This is the same undefined point as R0 VERIFICATION §3 #76.
   - The unchanged NOT_SELECTABLE_UNTIL marker could also have been recorded as `ALSO:REMAINING_STATE_MISMATCH` (tie-break rule 2b).
4. **Reference and anchor defects reproduce.**
   - PRD hash mismatch: REFERENCE_HASHES row, Match=NO.
   - Stale PRD and TYPES section pointers: PRD §7.2 was retitled by 416b29033; TYPES §8.2 is 'Permission Decision'; TaskScopeMode is at TYPES:177.
   - Stale decomposition line anchors: the old L285, L378, L379 and L346 now hold PKG-07, DEL-09-01, DEL-09-02 and DEL-06-01.
   - Examples: CLM-001, CLM-004.3, CLM-024, CLM-006, REGISTER-5.
5. **Test-name citations.** All the named test cases I checked exist at the cited files.

## (iii) Effort

- **Files read:** about 30 files or line ranges: ledger rows, reverse rows, four capability files, CONVENTIONS, RUN_BASIS, the evidence pack, the SoW, `_STATUS`, `_REFERENCES`, `_CONTEXT`, `Dependencies.csv`, the register and D-APP-108, and about 15 frontend source and test files.
- **Git:** 6 read-only calls (`blame -L`, `log`, `show --stat`).
- **Context budget:** comfortable.
