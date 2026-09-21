# V-SHARD-DEL-02-02-1 — verifier notes (RUN_D128 R2 PKG-02, DEL-02-02)

Frozen tree at `00115c719` only. Graded against CONVENTIONS (adopted) and RUN_BASIS §3, §5 and
Addenda 1–7. Git use: read-only `log`, `log -S` and `show` against the frozen tree.

## (i) Counts

| Class | Items | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (LOW, self-flag, REMAINING_WORK) | 9 | 7 | 1 | 1 |
| a30 (30% sample) | 16 | 15 | 0 | 1 |
| b (ALIGNED sample) | 1 | 1 | 0 | 0 |
| c (capability responses) | 7 | 7 | 0 | 0 |
| **Total** | **33** | **30** | **1** | **2** |

- **Refuted or contested on a verdict field (Disposition or Response): none.**
- REFUTED on another field: DEL-02-02#REM-2, on DirectionEvidence. The row also carries a
  LatestDecision point.
- CONTESTED on another field:
  - DEL-02-02#REMTXT-2, on CauseTag;
  - DEL-02-02#CLM-010.2, on Notes.

## (ii) Patterns

1. **The 7 RETIRED_BY_RULING rows in this shard hold.** They are CLM-004.1, CLM-009, CLM-010.11,
   CLM-010.5, CLM-014.1, CLM-018 and CLM-023.
   - Applied decomposition row L308 is GOVERNING. It names DEL-02-02 and retires Workbench and
     Pipeline from the active shell, keeping their code, routes and tests.
   - The SoW's SCA-APP-010 Gate-5 section (L69-78), seated under D-APP-108, keeps the earlier
     clauses as dated compatibility history.
   - D-APP-108 Q3 names the retired `/workbench` and `/pipeline` routes. LatestDecision
     `D-APP-108` is governing.
   - One caveat for R3:
     - The D-APP-108 record itself never names DEL-02-02; DECISION_HITS has no REGISTER or RULING
       hit for it. The retiring text is row L308 and the SoW section that D-APP-108 applied.
     - PRD FR-011 and FR-012 (P0) are unamended, and DIRECTIVE §0 ranks the PRD above
       scope-change records. That is a governing-document residue. It does not make these SoW
       rows wrong under MR-11 ("addresses the deliverable"), but R4 should see it.
     - The worker disclosed this alternative (AUTHORITY_CONFLICT).
2. **Modules that are LIVE by import but never rendered were handled correctly.**
   - I confirmed the SYMBOL-UNREACHED chain:
     - `WovenDialogueRoute` discards the `legacy` prop (`void legacy`, woven-dialogue-route.tsx:18);
     - `WorkbenchSurface`, `PipelineSurface` and `AgentMatrix` are built only in
       `createTertiarySidebarTabs`, inside the Loop, LoopTertiary and PortalLoop shells;
     - the shell ignores `defaultSurface` and always renders
       `data-woven-surface="dialogue"` (woven-dialogue-shell.tsx:822).
   - No row treats these symbols as live behaviour.
   - REMTXT-1 tags them `REACH=LIVE (unrendered)` and judges them on the product path.
   - CoordinationPanel, RightPanel, MethodLibraryView and ChatPanel/PersonaPicker are actually
     rendered (woven-dialogue-shell.tsx:855, :997, :1019), so the LIVE tags on REM-1, REM-3 and
     CLM-010.2 reflect rendered behaviour.
   - All REACH tags match REACHABILITY.csv. No cited file is in TOUCHED_PATHS, so
     `PostReleaseBasis=NO` is correct throughout.
3. **Direction and cause classification is uneven. These are field-level points only.**
   - **REM-2.** It cites a deliverable `_STATUS.md` (declared state) with a `CTX:` prefix. The
     governing explanation is D-GOV-43: IMPACT.md:92 retires Root DEL-02-10's closed event union v2,
     and ruling item 2 is "faithful transport". So `GOV:D-GOV-43` is correct, and LatestDecision
     should be governing, not `(context)`.
   - **CauseTag precedence.** It is applied mechanism-first on REMTXT-1 (SHELL_REDESIGN) but
     carrier-first on REMTXT-2 (CARRIER_PROPAGATION, with A2_TOPOLOGY only as CAUSE2) and REM-2.
   - **REGISTER-6.** LatestDecision reads `D-APP-109 (context)`, but DirectionEvidence reads
     `GOV:D-APP-109`.
   - **CLM-021.2.** NONE_FOUND was written before the CONTEXT AgentRuns search the rule requires.
     My spot-check found no explaining record, so the value stands.

Other checks that held:
- The tie-break was applied correctly on the dated D-APP-56 notes (CLM-001, CLM-007, CLM-021.1,
  CLM-022). The notes name no snapshot and call themselves current-state, so each takes
  STALE_SPECIFICATION with SEE:REGISTER-3 or SEE:CLM-007.
- REM-3 `MechanicallyUnblocked=YES` is verified:
  - V3-03 was removed from Remaining (`_STATUS` History 2026-09-06);
  - DEL-07-03-V3-01 was removed (DEL-07-03 `_STATUS` L27);
  - the only ACTIVE PREREQUISITE, DEP-02-02-021, is SATISFIED.
- The Dependencies.csv counts (22 rows: 21 ACTIVE, 1 RETIRED) and the removal of "All sessions (N)"
  in `03e61f38f` (found with `git log -S`) were recomputed and match.

## (iii) Effort

- **Files read:** about 30. These were:
  - the ledger rows, reverse and notes (by script);
  - CONVENTIONS and RUN_BASIS (the relevant sections);
  - the evidence pack (REACHABILITY, TOUCHED_PATHS, REFERENCE_HASHES, DECISION_HITS, the
    application map);
  - the SoW, `_STATUS`, `_CONTEXT`, `_DEPENDENCIES` and `Dependencies.csv`;
  - the D-APP-108 and D-APP-127 records;
  - the D-GOV-43 decision, proposal and IMPACT;
  - DIRECTIVE §0 and PRD FR-009..FR-013;
  - about 15 frontend source and test ranges.
- **Git:** 4 read-only calls.
- **Context:** not tight.
