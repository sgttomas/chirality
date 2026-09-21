# V-SOW verifier shard notes (RUN_D128 R2 EXT, ledger SOW)

Shard output: `V-SOW.csv`, 31 verdict lines covering 29 selected items, then `#END`.
SHA-256 `39f908d53a888b7fe9fb38d53735772b0f2ff833ae200395b732c785068a75db`.

Grading basis: `BRIEFS/V_SHARD.md` key; CONVENTIONS §1, §2, §4, §8; `_COMMON_RULES.md`
(Addendum 5 tie-break, Addendum 6 subject test, mixed-row R4-Q1 reading); RUN_BASIS §5 and
Addenda 3–8. The manager rule was applied as given: a gated Remaining item that names the
row's scope counts as an explicit deferral, and build scripts may carry REACH=LIVE. No errata
file exists for SOW, so no class `e` items were checked.

## (i) Counts

| Class | Items | CONFIRMED lines | REFUTED lines | CONTESTED lines |
|---|---|---|---|---|
| a (self-flag / LOW / AUTHORITY_CONFLICT) | 9 | 5 | 0 | 4 |
| b (other non-ALIGNED) | 8 | 7 | 2 | 1 |
| c (ALIGNED) | 12 | 12 | 0 | 0 |
| **Total** | **29** | **24** | **2** | **5** |

By Field (non-CONFIRMED lines):

- Disposition: REFUTED 1 (SOW-045.2), CONTESTED 4 (SOW-003, 050.2, 075.2, 076).
- LatestDecision: REFUTED 1 (SOW-045.2).
- CauseTag: CONTESTED 1 (SOW-084.2).

Verdict-field refutation rate (Addendum 3): 1 of 29 distinct items (3.4%), under the 10%
threshold. Field-only refutation: SOW-045.2 LatestDecision (goes to CORRECTIONS.csv).

Mechanical checks passed on every selected row: all cited code paths exist at the frozen tree,
and the cited lines hold the named symbols. Every REACH tag matches REACHABILITY.csv. The one
UNREACHED file, `engine-claude/src/index.ts`, is correctly tagged LEGACY_ONLY under
Addendum 1. All cited test files exist. PostReleaseBasis NO holds on every row: the only
cited touched files are `app-owned-composition.ts` and `session-store.ts`, and none of the
relied-on lines falls inside a TOUCHED_PATHS range. The live-deliverable mapping holds on
every `.1` and unsplit row: each mapped DEL's ScopeOfWork front matter cites the SOW row, and
each mapped DEL is IN_PROGRESS in DELIVERABLE_INVENTORY.

## (ii) Systematic patterns

1. **The same D-GOV-43 shared-configuration mechanism is dispositioned inconsistently.**
   - SOW-076 (OUT, ambient settings) is AUTHORITY_CONFLICT.
   - SOW-045.2 (settings-isolation conformance), which rests on the same
     `codex-effective-home.ts` sharing, is IMPLEMENTED_DIFFERENTLY. Its LatestDecision is
     also D-APP-127 governing, although D-APP-127 names neither DEL-04-02 nor the row.
   - Under CONVENTIONS §1 a ruling that undercuts an unamended clause without naming it
     gives AUTHORITY_CONFLICT, so SOW-045.2 is REFUTED.
2. **The AUTHORITY_CONFLICT boundary is soft on the D-GOV-43 policy rows.**
   - SOW-050.2: the `workspaceWrite` default is an App choice. D-GOV-43 forbids pinning
     policy, not a read-only default.
   - SOW-075.2: whether Codex memories count as project truth.
   - SOW-076: the literal Claude and SDK wording of the OUT row.
   - Each can be read as a conflict or as not forced by the ruling, so all three are
     CONTESTED. All were self-flagged LOW or MEDIUM by the workers.
   - Proposal: the manager states whether a user-selectable Codex policy with an App-chosen
     default counts as the ruling undercutting the clause.
3. **Manager-rule deferrals: most name the row, one only traces to it.**
   - SOW-008 and SOW-010 cite gated items that name the SOW row explicitly, so they are
     CONFIRMED.
   - SOW-003's DEL-02-03-V3-01 names SOW-001/002/004. It reaches scope scans only through its
     trace to decomposition L309 ("scan-state feedback"), so SOW-003 is CONTESTED.
   - SOW-063's DEL-08-04-V3-01 traces CLM-033, not SOW-063. The row is still CONFIRMED because
     the live dispatch and AgentRuns code carries it.
4. **Minor line anchors and rendering nuances (immaterial, in ConventionIssue).**
   - SOW-034: the anchor `transition.ts:55` points at the type field; the check is at :96–117.
   - SOW-061.2: the cited range starts in the collabAgent branch.
   - SOW-019.2: ApiKeySettings still mounts in the non-woven header variant.
   - SOW-006.2: the non-rendering is driven by `settings-view.tsx:31`.
5. **Cross-deliverable observation (not a SOW ledger error).** DEL-08-02 `_STATUS.md`
   Remaining prose still says route/query/matrix compatibility is "implemented and validated",
   although the matrix helper is TEST_ONLY (SOW-005.2). This is a PKG-08 matter.
6. **New OTHER token.** `OTHER:WORKFLOW_CONVENTION` appears on SOW-033.2 and is reported in the
   half-A notes, so the manager can register it.

## (iii) Effort

- Read: V_SHARD, `_COMMON_RULES`, W_SOW_A, CONVENTIONS §1/§2/§4/§8, RUN_BASIS §5 and addenda,
  SOW_notes, the 29 ledger rows, the decomposition §7/§9 rows for 27 SOW numbers, the D-APP-127
  record, and the Remaining sections of 12 deliverables' `_STATUS.md`.
- Also read: about 25 code files by targeted grep and line ranges.
- Script checks: REACHABILITY, TOUCHED_PATHS and test-file existence, plus ScopeOfWork front
  matter and inventory lifecycle for 24 deliverable mappings.
- Git: none needed; no blame was required, because no relied-on line fell in a touched range.
  No installs and no test runs.
- The context budget was adequate.
