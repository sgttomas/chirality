# DEL-08-05 — reverse-pass notes (RUN_D128, R2 PKG-08, rerun worker)

## Summary

- **Sealed ledger:** `DEL-08-05_claims.csv`. Its SHA-256 is re-checked and unchanged: `543a194e954f8992ae7916e725f42a9816144a071adaa47f49496b55eb473e0f`.
- **Inputs:** `REVERSE_INPUT_capabilities.csv`, 326 rows from 7 areas: BUILD, ELECTRON, HARNESS, RTCONTRACT, RTCORE, SETTINGS and SHELL. I read the area `*_capabilities.csv` and `*_notes.md` files for their content.
- **Responses:** 1 CLAIMED_BY, 14 PARTIAL and 311 NOT_MINE.
  - **CLAIMED_BY:** CAP-HARNESS-059 → CLM-006.
  - **PARTIAL:** each one maps to the DEL-08-05 slice of a capability that another deliverable mainly owns. The rationale column names that slice.
    - The two children-related delegation capabilities, HARNESS-056 and HARNESS-057 → CLM-012.13. Admission and launch belong to DEL-08-04.
    - The child-output artifact part of HARNESS-048 → CLM-012.7. Ordinary tool results belong to DEL-05-05 under D-APP-68.
    - The live lineage and role-evidence inputs → CLM-018.2 and CLM-018.3.
- **NOT_MINE rows:**
  - Every BUILD, ELECTRON and SETTINGS capability.
  - SHELL-034, SHELL-039 and SHELL-040. They present subagent and child activity; that presentation belongs to DEL-02-02 and the shell deliverables.
  - HARNESS-058, the governance gates owned by DEL-08-04.
  - RTCORE-038, RTCORE-044 and RTCORE-047.
- **Validators:**
  - `reverse`: RULES errors none | warnings none; RESULT PASS.
  - `errata`: RULES errors none | warnings none; RESULT PASS.

## Errata (11 rows; no Disposition changes)

**Why.** Following verification lesson 4, the SURFACES files showed that two symbols I cited as REACH=LIVE evidence of native-descendant lineage are never executed on the product path:

- **CAP-RTCONTRACT-028.** The daemon-to-supervisor tool callback bridge (`delegated.ts:247`, the `nativeChild` association) is a dead contract, with no implementation and no caller.
- **The consumer in `runtime-method-service.ts:454-469`.** A re-grep of `projects/chirality-runtime/packages/*/src` at `00115c719` finds no producer of `executionContext.nativeChild`. Only tests supply it. So the `native-child.method-loaded` history code is also not executed on the product path.

**What changed.** The module-level `REACH=LIVE` tags are kept, as the rule requires. Each affected citation now carries an explicit not-executed qualifier.

| Field | Rows |
|---|---|
| ImplementationEvidence | CLM-004, CLM-012.3, CLM-018.1, CLM-018.2, CLM-018.3, CLM-018.6, CLM-022, CLM-037, REM-1 |
| Notes | CLM-037, CLM-018.2 |

**What did not change.** No Disposition changes, because each row still rests on live evidence:
- the supervisor parent-thread map;
- `collabAgentToolCall` `agentThreadIds`;
- per-turn `instruction-asserted` role evidence.

## Coverage gaps and observations (for the manager)

- **Cancellation/cleanup evidence.** CAP-RTCORE-029 notes that `codex-supervisor.ts` `handleNotification` contains post-release lines from `da95ec194` (526, 535-544 and 570-573) that cancel child-thread application-tool calls. That code is live native-child cleanup behaviour bearing on REQ-002 / CLM-018.2 ("cancellation/cleanup"). The forward ledger cites only the `observationEnded` notice (lines 588-592, which blame outside those commits).
  - No forward row cites the touched lines, so no PostReleaseBasis=YES row exists for this behaviour.
  - This is a partial evidence gap, not a missing unit. It cannot be expressed as an erratum.
- **The managed AgentRun path.** CAP-RTCORE-024 and CAP-RTCONTRACT-048 confirm the forward reading that the coordinator is not constructed. The App-owned composition passes no `Agent1RunPort`, and `runAgent1` throws `REQUIRED_DELEGATION_MISSING` (`runtime-service.ts:664-670`). They also classify `agent1-run-coordinator.ts` as effectively TEST_ONLY at symbol level.
- **Descendant process tracking.** CAP-RTCORE-047 (the descendant process tracker) is TEST_ONLY and DISABLED. It adds no live descendant evidence.
- **No capability in these seven areas lacks a matching forward row where DEL-08-05 plausibly owns it.**

## Census: sealed and errata-applied

The Disposition, CauseTag, HumanDecisionNeeded, Confidence and ClaimType counts are identical before and after errata. That is because the errata touch only ImplementationEvidence and Notes. See `DEL-08-05_notes.md` §1 for the figures.
