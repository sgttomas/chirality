# V-DEL-08-04: verifier shard notes (R0 calibration, unit V)

Shard: `DEL-08-04`. There are 66 SELECTION items. SEC-1.1 and CLM-010.3 each appear twice, once in class a/b and once in class c.
Evidence was read at the frozen tree `00115c719`. No ledger, notes or reverse file was edited.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a | 57 | 42 | 3 | 12 |
| b | 7 | 5 | 1 | 1 |
| c | 2 | 1 | 0 | 1 |
| **Total** | **66** | **48** | **4** | **14** |

**REFUTED:**
- SEC-1.2 and CLM-016.3: the Disposition is wrong.
- CLM-003.1 and CLM-010.3: the evidence citation is wrong. The Disposition still holds on both rows.

**CONTESTED:**
- CLM-010.5, 013.2, 020, 025.2, 028.2 (the Agent 0 hierarchy);
- CLM-005.2, CLM-016.6, CLM-030.3, CLM-032 (CauseTag);
- REM-2, REM-3 (MechanicallyUnblocked);
- REGISTER-1, CLM-025.1;
- CAP-HARNESS-056 (Response).

**PostReleaseBasis.** I checked it with read-only `git show --stat` of `da95ec194`, `cb08dbe2f`, `9ecbdecdf` and `ccb95e06a`. None of them touches any file the ledger cites:
- `da95ec194` touches `core/src/session-store.ts`, not `delegated-runtime.ts`;
- `ccb95e06a` touches one line of `electron/plan-export-ipc-contract.ts` and a `.github` action.

The worker set `NO` on all 80 rows by assumption, and `NO` is correct for all of them. The reverse-notes revisit is confirmed, although it omits the `.github` file, which has no effect.

**Main finding holds.** No App route or Electron entry reaches the managed bridge:
- `runtime.ts` has no non-test importer;
- `coordination-tools.ts` loads it only through a dynamic `import('../runtime')`;
- `runtime-fingerprint.ts` imports `managed-delegation` but has no importer itself;
- `app/api/harness/turn/route.ts` goes to the Runtime through `daemon-harness-port`.

`managed-delegation.ts` has no cancel, abort or cleanup symbol. `subagent-governance.ts` has no native or class handling.

## (ii) Systematic patterns

1. **The GOVERNING map was not applied to the Agent 0 hierarchy rows** (MR-8 and "judge against GOVERNING").
   - The worker tagged the SoW's "Agent 0 → named Agent 1 only" as STALE_SPECIFICATION/PRE_V3_DRIFT, with root `AGENTS.md` and the deliverable's MEMORY as the basis.
   - But the GOVERNING App `docs/CONTRACT.md` K-SUBAGENT-1 (line 125) still says "0→1 or 1→2", which matches the SoW. Root `AGENTS.md` is classed as execution protocol in RUN_BASIS §5, and I found no D-APP ruling for the 2026-08-16 repair.
   - A strict reading is therefore IMPLEMENTED_DIFFERENTLY or AUTHORITY_CONFLICT.
   - Rows affected: CLM-010.5, CLM-013.2, CLM-020, CLM-025.2, CLM-028.2, and the Agent 0 half of CLM-032.
   - The worker noticed K-SUBAGENT-1 but did not let it decide the Disposition. The manager should rule on this.
2. **A divergence was claimed where the GOVERNING contract restates the claim** (SEC-1.2, CLM-016.3).
   - K-UNTYPED-1 (line 128) and K-ROLE-2 (line 229) both state that native descent assigns no role.
   - The Runtime records this literally: `delegated-runtime.ts:321` has the delegationPolicy string "native descent does not assign a role", and the `role-policy.test.ts` case covers it.
   - Choosing a role through a configured `[agents]` type is selection, not descent.
   - The worker's LOW alternative (ALIGNED) is the better reading. At most the row is PARTIALLY_IMPLEMENTED, and only if the App bridge must itself consume the class, which is the open V3-01 item.
3. **Evidence overstates module-level conformance** (CLM-003.1, CLM-010.3; this also touches CLM-020 steps 1 and 8).
   - `delegate_agent` (`coordination-tools.ts:269-297`) calls `ManagedDelegationService.delegate`. That method runs its own seal, approvalRef and hierarchy checks and never calls `evaluateSubagentGovernance`.
   - The gate's only production-code caller is `turn-engine.ts:232`, on the legacy SDK subagent path.
   - Rows citing `subagent-governance.ts` as "the gate over delegate_agent" are therefore imprecise.
   - The line numbers are also slightly off: CLM-010.3 cites `:270-290`, but the missing-metadata denial is at `:250-257`.
4. **Dated history is treated inconsistently.**
   - CLM-033 (the SCA-APP-008 transcription) is NOT_AUDITABLE as history.
   - The dated reconciliation copies CLM-007, CLM-016.1, CLM-031 and CLM-032 are STALE_SPECIFICATION.
   - The CONVENTIONS explicitly class dated notes as STATE_ASSERTION, so I confirmed the stale rows. But the SoW's own clause (lines 27-28) says earlier sections are "dated compatibility history". The rulebook should say which one wins.
5. **Single-valued CauseTag on two-cause rows.**
   - CLM-032: PRE_V3_DRIFT is the tag, yet the row cites the re-platform steer as DirectionEvidence.
   - CLM-016.8: part of the row is A2_TOPOLOGY.
   - SEC-1.4 and SEC-2.2: SHELL_REDESIGN names where the requirement came from, not why the code diverges.
   - REM-3 cites the re-platform steer, while SEC-1.4 cites NONE_FOUND for the same unimplemented policy.
6. **Gate semantics.**
   - **REM-3.** "DEL-02-02-V3-04 selected" is undefined. A V3-04 slice was implemented on 2026-09-06. DEP-08-04-013 is an INTERFACE dependency, not a PREREQUISITE. So YES is arguable under MR-2/MR-6.
   - **REM-2 and REGISTER-1.** Both rest on K-CONTROL-1, which retires the DEL-02-07 supervisor-socket design. But the A2 supplement retains the Runtime supervisor module. MR-6 UNKNOWN is applied correctly.
7. **Path convention.** Every DirectionEvidence cites `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/`, which is App-relative rather than repo-relative. The Root steer path is correct.
8. **Unrecorded adjacent register defect.** The DEP-08-04-012 Notes say `_CONTEXT.md` lists SOW-063 only. In fact `_CONTEXT.md:58` lists SOW-063 and SOW-083, so that note is stale. The worker's CLM-002 finding is correct.

### CAP-HARNESS-057 ownership judgement (requested)

My reading is **PARTIAL**, not NOT_MINE. The covering key should be **CLM-014 or CLM-005.1** rather than CLM-016.2.

- **For PARTIAL:**
  - The SoW names "coordination tool registration" as a DEL-08-04 implementation path and required artifact (lines 138, 282, 343, 386 and 478).
  - `reportCoordinationNotice`, `sendAgentUpdate` and `acknowledgeAgentUpdate` live in `managed-delegation.ts:806-992`.
  - They are covered by DEL-08-04's own test file (`managed-delegation.test.ts:642`, "persists child→parent notices and parent→child updates with acknowledgments").
- **Against CLAIMED_BY:**
  - D-APP-68 disposition 4 (SoW line 495) gives DEL-08-05 the managed-child lifecycle and records.
  - Notice and update semantics are K-SUBAGENT-3 lifecycle evidence.
- **Why not CLM-016.2:** the link through "multi-child managed execution" is weaker than the explicit registration-path claims.

## (iii) Effort

- **Files read:** about 30 files or ranges.
  - Deliverable: SoW (all 502 lines), `_STATUS`, `Dependencies.csv`, MEMORY, `_CONTEXT`, `_REFERENCES`, the Assessment header.
  - App code: 6 harness/consent source files, 5 test-name lists, `route.ts`.
  - Runtime: 4 source files and 2 test files.
  - Governance: App and Root CONTRACT rows, D-GOV-43 with its A2 supplement and proposal items 7-10, the register rows, and a DEL-02-02 `_STATUS` excerpt.
  - Run files: gate transcripts, the capability rows, and four `git show --stat` calls.
- **Context:** moderately tight. The 80-row ledger dump (about 34k tokens) and the full SoW were the main cost. A 60-plus item shard on a 500-line SoW is near the practical ceiling for one verifier context.
