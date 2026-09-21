# V-DEL-04-05: verifier shard notes (RUN_D128 R0 calibration, unit V)

Fresh evidence-only verifier. Read-only against the frozen tree `00115c719`. Git use was limited to read-only `log`, `show` and `blame`. No ledger, notes or reverse file was edited.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (non-ALIGNED, LOW, self-flag, reverse-notes) | 58 | 54 | 3 | 1 |
| b (ALIGNED sample) | 1 | 0 | 0 | 1 |
| c (reverse PARTIAL) | 2 | 2 | 0 | 0 |
| **Total** | **61** | **56** | **3** | **2** |

- **REFUTED:**
  - CLM-009.14: Disposition.
  - CLM-010: AuthorityTier.
  - CLM-012: AuthorityTier.
- **CONTESTED:**
  - CLM-009.9: Disposition, LOW self-flag.
  - CLM-028: Disposition, class b.

## (ii) Systematic patterns

1. **The self-flagged governance-conflict rows are right, but the stated alternative rests on a false premise.** Keys: CLM-004.2 and CLM-009.10.
   - The worker's alternative says K-NET-1 is "untranscribed" wording that D-APP-127 overrides. That is not so.
   - At the frozen tree, CONTRACT K-NET-1 (line 134) is post-D-GOV-43 text: it reads with item 4, yet it still says remote MCP and providers "fail closed".
   - SPEC §16.3 (line 922) says remote MCP and plugins need a governed tranche. SPEC §25.1 (lines 1254-1256) says the effective home shares the user's "plugins, MCP definitions" by reference.
   - The conflict therefore sits inside the GOVERNING corpus. That makes AUTHORITY_CONFLICT the stronger reading, not a weak one.
   - The same misreading of MR-11 appears in the CLM-009.9 alternative. Under K-NET-1 item 4 the posture is user-chosen and labelled, so the ALIGNED reading there is live.

2. **Code that the ledger calls unwired is treated inconsistently.** Keys: CLM-028 versus CLM-009.6, CLM-009.7 and CLM-009.11. Also CLM-004.1 versus CLM-009.15.
   - The worker correctly found that `runtime.ts` is imported only by tests and by the `coordination-tools → read-tools → sdk-options-builder → claude manager` island, so the Anthropic and Claude managers are off the shipped path.
   - Most rows apply this as IMPLEMENTED_DIFFERENTLY. CLM-028 is the exception: it is marked ALIGNED while partly relying on the same unwired base-URL and classification code. It also cites the Codex login `authUrl` check as if it were provider base-URL evidence.
   - CLM-004.1 and CLM-009.15 cover identical settings-isolation substance but carry different CauseTags (`A2_TOPOLOGY` versus `CODEX_SOLE_ENGINE`).
   - Suggested convention: one rule for "conforming code off the shipped path", and one CauseTag for it.

3. **Convention slips on AuthorityTier and UNKNOWN.**
   - **AuthorityTier on CONTEXT_CLAIM rows.** CLM-010 is GOVERNANCE_INVARIANT and CLM-012 is LOCAL_DESIGN. The rule reserves NOT_APPLICABLE for CONTEXT_CLAIM.
   - **The reverse ambiguity.** NOT_APPLICABLE is also used on STATE_ASSERTION rows (CLM-001, 007, 015, 023, 004.4 and 014.1). The rule neither permits nor forbids this, so it should be clarified.
   - **UNKNOWN used for evidence that was simply not inspected (CLM-009.14).** The public Runtime event contract carries stock Codex method names and raw params: `projects/chirality-runtime/packages/contracts/src/v2-events.ts:22-27`, per K-EVENT-6 (CONTRACT:83).
     - The correct reading is IMPLEMENTED_DIFFERENTLY, or AUTHORITY_CONFLICT between K-ENGINE-4 and K-EVENT-6.
     - Suggested convention: UNKNOWN only after a stated search.

**Minor observations:**

- **Line drift.** Some cited line ranges are off by 1-6 lines: `claude-agent-sdk-manager.ts` 55-57 is actually 53-59, and 67-76 is 61-80; `codex-supervisor.ts` 103-108 is actually 104-108. None of this changes a finding.
- **CauseTag fit.** PRE_V3_DRIFT is used for verification-breadth gaps (CLM-009.2), which are not divergences.
- **Dated notes.** The worker treats "dated current-state notes" (CLM-001 group, STALE_SPECIFICATION) differently from "dated History entries" (STATE-2, STALE_VERIFICATION). That distinction is defensible, but the conventions do not document it.

**PostReleaseBasis.** The forward ledger set NO for every row by assumption, and the reverse notes revisited it. I confirmed that with `git blame` at the frozen tree:

- The relied-on lines predate all four post-v3.0.1 commits: `app-owned-composition.ts:180,225`, `codex-supervisor.ts:104-108`, `runtime-daemon.ts:465-474,515-536` and `client.ts:695-698`.
- They come from commits dated 2026-07-22 to 2026-09-12.
- `da95ec194` touches these files, but only other lines.

So NO holds for all selected rows.

**Reverse-notes items:**

- **E-1** (the oMLX D-APP-72 scope has no forward row) is a real coverage gap. The `_STATUS.md:32` History entry and `api-key-store.ts:38-39` show the oMLX scope was delivered. It does not refute CLM-009.6.
- **E-2** (`api-key-store.ts:33-45` is not cited on CLM-009.1) is valid and immaterial.
- **Class c:** both PARTIAL responses are confirmed.
  - CAP-HARNESS-016: `hosted-bootstrap-client.ts:142-158` has login start, cancel and sign-out.
  - CAP-HARNESS-038: `session-events.ts:17,74` applies `redactJsonLike`.

**Checks that held:**

- Hash staleness: I recomputed PRD, CONTRACT and SPEC on the frozen tree, and PLAN matches.
- Unwired island, null Runtime credential port, and the invalid-status IPC path. The status has no `source`, so `api-key-ipc.ts:120-126` rejects it.
- Dependencies.csv: 13 rows, 11 ACTIVE and 2 RETIRED, with the missing `Datasheet.md`, `Specification.md` and `Procedure.md` targets.
- The REGISTER-4 pointers.
- REM-1 has MechanicallyUnblocked = NO, and that holds on the App-surface dependencies alone: DEL-02-05-V3-03 and DEL-09-06-V3-03 are still Remaining.
- DirectionEvidence: the APP_EXECUTION_RETURN "Files changed" list does not name DEL-04-05, and TOPOLOGY_COMPARISON C4 says what the ledger says it does.
- All 22 cited test case names exist.

## (iii) Effort

- **Files read:** about 30, mostly by grep and line ranges. They cover:
  - SoW, `_STATUS`, `_REFERENCES`, `_CONTEXT`, `_DEPENDENCIES`, `Dependencies.csv`, the Assessment and MEMORY;
  - App CONTRACT, SPEC and PRD;
  - the D-APP-127 ruling and register;
  - the re-platform tranche returns and TOPOLOGY_COMPARISON;
  - about 12 frontend and Runtime source and test files;
  - blame and show of the 4 commits.
- **Context:** moderately tight. The 62 KB ledger had to be paged in pieces. The SoW was large but manageable.
- Many rows shared the same evidence, which made 61 items feasible in one shard.
