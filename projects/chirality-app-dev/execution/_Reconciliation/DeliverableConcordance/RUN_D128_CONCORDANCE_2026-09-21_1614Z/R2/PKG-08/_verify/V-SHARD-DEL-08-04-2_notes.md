# V-SHARD-DEL-08-04-2: verifier notes (DEL-08-04)

Evidence only. These verdicts are not rulings. Graded against `CONVENTIONS.md`, the shared PKG-08 grading key and the frozen tree at `00115c719`.

## (i) Counts

| Class | Items | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| b (sampled ALIGNED) | 1 | 0 | 0 | 1 |
| e (errata rows) | 19 | 15 | 0 | 4 |
| c (reverse responses) | 5 | 4 | 1 | 0 |
| **Total** | **25** | **19** | **1** | **5** |

- No item is REFUTED at Disposition level.
- One item is REFUTED on the reverse `Response` field: CAP-HARNESS-056.
- Three items are CONTESTED at Disposition level: CLM-020 (sealed), and the SEC-2.3 and CLM-016.4 errata Disposition rows.

## (ii) Systematic patterns

1. **The REACH retag in the errata rows is code-verified but departs from the pack.** Examples: SEC-1, CLM-010.2, CLM-016.2 and REM-2 (ten ImplementationEvidence errata rows).
   - What the errata do: they move `native-role-config.ts:141-143` from `REACH=LIVE` to `REACH=TEST_ONLY`, and add `product-native-role-config.ts:33-34 REACH=LIVE`.
   - What I checked in the frozen tree:
     - `loadTrustedNativeRoleConfiguration` and `codexNativeRoleConfigOverrides` are reached only through the `core/src/index.ts:26` barrel and from tests.
     - `materializeProductNativeRoles` is called by `delegated-engine-adapter.ts:213`.
     - That adapter is composed in `daemon/src/app-owned-composition.ts:214`.
     - `DescendantTracker` is constructed only by `ProcessSupervisor` (`process-supervisor.ts:57`), and `ProcessSupervisor` has no product constructor.
   - Verdict: CONFIRMED, under the brief's "code-verified reason" allowance.
   - ConventionIssue: `REACHABILITY.csv` tags these modules LIVE. The same ledger keeps `agent1-run-coordinator.ts` as `REACH=LIVE` with a Notes caveat for the identical situation, so the tag practice is inconsistent. It has no effect on any Disposition.
2. **An unrendered UI surface changes the Disposition** (SEC-2.3, CLM-016.4). The errata's code facts hold:
   - `shell-frame.tsx:377` calls the consent controller with no port;
   - `shell-frame.tsx:404` always passes a truthy hosted controller;
   - `settings-view.tsx:31-32` therefore renders `HostedBootstrapView` in place of the K-ROLE-2 label view.

   Two facts the errata missed:
   - `contracts/src/v3.ts:27` sets TASK to `directEntry:false`, and `persona-picker.tsx:51` filters on that flag.
   - D-APP-24 (RULED, Option C) restricts the direct-chat picker to Type-0/Type-1. D-APP-24 is not in DECISION_HITS for DEL-08-04.

   This yields two readings, so the Disposition is CONTESTED:
   - PARTIALLY_IMPLEMENTED: K-ROLE-2 "always offered" and "label/copy checks" are unmet on the live path. The verifier leans this way.
   - ALIGNED or AUTHORITY_CONFLICT: no Agent 2/TASK entry exists to label, and Runtime role evidence carries both labels.

   On the other errata fields:
   - DirectionEvidence is CONTESTED because it is incomplete: GOV:D-APP-24 should join GOV:D-APP-127.
   - CauseTag CREDENTIAL_CUSTODY and RemainingWork are CONFIRMED.
3. **Module-level and live-path judgement disagree within the ledger.** CLM-020 (Steps 1-13 for the admission bridge) is ALIGNED at module level. CLM-010.1 and CLM-003.2 judge the same bridge on the live path as IMPLEMENTED_DIFFERENTLY. I also flag a possible ClaimType issue: CONTEXT_CLAIM covers "method notes".
4. **A reverse response overclaims ownership** (CAP-HARNESS-056). The capability bundles launch lock, orchestration records and handoff state. DEL-08-05 CLM-036 (`ScopeOfWork.md:487`) makes DEL-08-05 the sole owner of lifecycle, records and persistence, while DEL-08-04 owns admission and `delegate_agent`. The response should be PARTIAL, not CLAIMED_BY.

## Other checks that held

- Line anchors (all within 1 line):
  - `role-policy.ts:33-35,43`
  - `delegated-runtime.ts:321`
  - `runtime-service.ts:223-229` and `664-670`
  - `runtime-method-service.ts:589`
  - `hosted-engine-consent-port.ts:185-191`
  - `account-consent-settings.tsx:185,437-446`
  - the `managed-delegation.ts`, `subagent-governance.ts`, `subagent-bridge.ts`, `coordination-tools.ts`, `agent-runtime-contract.ts` and `sdk-options-builder.ts` citations
- Every cited test case name exists at the frozen tree.
- PostReleaseBasis NO holds. `codex-supervisor.ts:280-309` falls outside every TOUCHED_PATHS range (271-273, then 391-392). The other cited files are not listed.

## (iii) Effort

- Files read: about 30 files or ranges in the frozen tree, plus CONVENTIONS, RUN_BASIS §3/§5/addenda, the evidence pack (REACHABILITY, TOUCHED_PATHS, DECISION_HITS) and three capability rows.
- Git was not needed. PostReleaseBasis was settled from the TOUCHED_PATHS line ranges.
- The context budget was adequate. Most time went into the SEC-2.3/CLM-016.4 render-path and D-APP-24 check.
