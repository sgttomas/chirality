# PREGATHER — DEL-08-04 Type 2 Subagent Governance Bridge

- **Deliverable:** DEL-08-04 (PKG-08). Folder `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/`.
- **Basis:** frozen tree at `00115c719`. Evidence pack `R2/PKG-08/EVIDENCE_PACK/` (REACHABILITY, TOUCHED_PATHS, DECISION_HITS, D-APP-127_APPLICATION_MAP, REFERENCE_HASHES).
- **Producer:** R2 PKG-08 pre-gather TASK (Type 2). Evidence location only: no dispositions, alignment judgments or CauseTags.
- **Method (searches run):**
  1. `grep DEL-08-04 R1_INVENTORY/CLAIM_INDEX.csv` found 40 rows. 39 have `DeliverableID = DEL-08-04`. The other row, `DEL-03-02#REM-1`, belongs to DEL-03-02, which names DEL-08-04-V3-02 as its gate. It is excluded here.
  2. `HINTS/DEL-08-04.csv` (581 rows) was summarized by python, counting per path and per ClaimKey token set. Most hits are generic-token noise, such as `Agent`, `docs/*.md`, `TBD` and `main` hitting electron, consent and manifest files. The real code leads came from the targeted greps in step 3.
  3. Targeted greps over `frontend/{src,electron}` and `chirality-runtime/{packages,tests}` for these terms: `delegate_agent`, `evaluateSubagentGovernance`, `ManagedDelegationService`, `managed-delegation`, `subagent-governance`, `evaluateSubagentPreflight`, `createExecutableSubagentBridge`, `subagentGovernance`, `role not mechanically enforced`, `instruction-asserted`, `G-ROLE`, `nativeDescendant`, `descendant`, `DELEGATION_POLICY_VIOLATION`, `bounded-briefs`/`ask-before-each-brief`, `delegationPolicy`, `cancel|interrupt|abort`, `overlap`, `sealedBrief`.
  4. REACH values were copied from `REACHABILITY.csv`. TOUCHED ranges were checked against `TOUCHED_PATHS.csv`. Decision IDs came from `DECISION_HITS.csv` and `_DECISIONS/_REGISTER.md`.
- **Counts:** 39 units (3 SEC, 33 CLM, 3 REM). 10 units have `NO_CANDIDATES` for code. No cited line falls in a TOUCHED range: see the cross-cutting section.
- **Path abbreviations** (repo-relative): `FE/` = `projects/chirality-app-dev/frontend/src/`, `FT/` = `projects/chirality-app-dev/frontend/src/__tests__/`, `RT/` = `projects/chirality-runtime/packages/`, `RTT/` = `projects/chirality-runtime/tests/`, `APPX/` = `projects/chirality-app-dev/execution/`.

## Module legend (REACH from REACHABILITY.csv)

| Key | Path | REACH |
|---|---|---|
| MD | `FE/lib/harness/managed-delegation.ts` | LEGACY_ONLY |
| SG | `FE/lib/harness/subagent-governance.ts` | LEGACY_ONLY |
| SB | `FE/lib/harness/subagent-bridge.ts` | LEGACY_ONLY |
| CT | `FE/lib/harness/mcp/coordination-tools.ts` | LEGACY_ONLY |
| TE | `FE/lib/harness/turn-engine.ts` | LEGACY_ONLY |
| AR | `FE/lib/harness/agent-roster.ts` | LEGACY_ONLY |
| ARC | `FE/lib/harness/agent-runtime-contract.ts` | LEGACY_ONLY |
| PO | `FE/lib/harness/permission-overlay.ts` | LEGACY_ONLY |
| CH | `FE/lib/harness/chirality-hooks.ts` | LEGACY_ONLY |
| SOB | `FE/lib/harness/sdk-options-builder.ts` | LEGACY_ONLY |
| OPT | `FE/lib/harness/options.ts` | LEGACY_ONLY |
| RF | `FE/lib/harness/runtime-fingerprint.ts` | LEGACY_ONLY |
| TK | `FE/lib/harness/toolkit.ts` | LIVE |
| HCP | `FE/lib/consent/hosted-engine-consent-port.ts` | LIVE |
| ACS | `FE/components/settings/account-consent-settings.tsx` | LIVE |
| CUX | `FE/lib/consent/consent-ux-fixtures.ts` | TEST_ONLY |
| GW | `FE/lib/workspace/governed-workflow.ts` | TEST_ONLY |
| SSV | `FE/components/shell/subagent-stream-view.tsx` | LIVE |
| TD | `RT/contracts/src/harness/tool-descriptor.ts` | LIVE |
| TN | `RT/contracts/src/harness/mcp/tool-names.ts` | LIVE |
| DLC | `RT/contracts/src/delegated.ts` | LIVE |
| V3C | `RT/contracts/src/v3.ts` | LIVE |
| RP | `RT/core/src/role-policy.ts` | LIVE |
| DR | `RT/core/src/delegated-runtime.ts` | LIVE |
| A1C | `RT/core/src/agent1-run-coordinator.ts` | LIVE |
| RS | `RT/core/src/runtime-service.ts` | LIVE |
| RMS | `RT/core/src/runtime-method-service.ts` | LIVE |
| WR | `RT/core/src/worker-retirement.ts` | LIVE |
| NRC | `RT/core/src/native-role-config.ts` | LIVE |
| DT | `RT/core/src/descendant-tracker.ts` | LIVE |
| CS | `RT/daemon/src/codex-supervisor.ts` | LIVE (touched file; cited lines outside ranges) |

---

## DEL-08-04#SEC-1 — Current responsibility (SoW L30)
- **Gist:** The deliverable is the managed-delegation bridge. It carries multi-child execution and the Agent 0/1/2 graph, consumes native descent as a distinct class, enforces boundaries, applies role labels and honours the per-chat policy.
- **Code:**
  - `MD:552 ManagedDelegationService.delegate` REACH=LEGACY_ONLY
  - `MD:259 resolveChild` REACH=LEGACY_ONLY
  - `MD:467 assertNoActiveWriteOverlap` REACH=LEGACY_ONLY
  - `SG:196 evaluateSubagentGovernance` (persona gate L205-213) REACH=LEGACY_ONLY
  - `A1C:105 GovernedAgent1RunCoordinator` (sealedBrief L220-303; interrupt L120) REACH=LIVE
  - `RS:223` agent2 direct-entry refusal `DELEGATION_POLICY_VIOLATION` REACH=LIVE
  - `RP:20 createRolePolicyEvidence` (L33 enforcementLabel, L34 evidencePosture, L43 nativeDescendant) REACH=LIVE
  - `NRC:141-143` native maxDepth pins REACH=LIVE
  - `DT` descendant tracking REACH=LIVE
  - `HCP:185-191 RoleEnforcement / ROLE_NOT_MECHANICALLY_ENFORCED_LABEL / INSTRUCTION_ASSERTED_EVIDENCE_LABEL` REACH=LIVE
  - `ACS:185 roleLabelApplies`, `ACS:439-445` label and "Native descendants acquire no role" hint REACH=LIVE
  - Per-chat policy: vocabulary only, in `GW:24,37` REACH=TEST_ONLY. No live policy carrier was found (grep `delegationPolicy|bounded-briefs|ask-before-each-brief` in FE/app, FE/lib, FE/components, RT/packages).
- **Tests:**
  - `FT/lib/managed-delegation.test.ts` (all 19 cases, L104-801)
  - `RTT/agent1-run.test.ts :: runs exactly one read-only Agent 2, records parentage/model epoch, and requires review`
  - `RTT/role-policy.test.ts` (L7, L12 nativeDescendant)
  - `FT/components/account-consent-settings-states.test.ts :: roleAgent2NotMechanicallyEnforced…`
- **Decisions:** D-APP-108 (seating), D-APP-68, D-GOV-35, D-GOV-14, D-APP-74. Also D-APP-127 in the register at L152: the D-APP-127 map shows `Revised=NO` for all 5 carriers.

## DEL-08-04#SEC-2 — Current acceptance obligations (SoW L57)
- **Gist:** There are three obligations: bridge enforcement plus class-aware routing, a per-chat `none`-default policy that narrows and adds no class, and the Codex role labels with WP-03/05 and D-GOV-35 prerequisites.
- **Code:**
  - Item 1: as SEC-1. Class-aware routing candidate: `RMS:589` route `primary|managed-delegation|unavailable` REACH=LIVE, `V3C:172` route type REACH=LIVE.
  - Item 2: `GW:24` policies list REACH=TEST_ONLY. No live candidate found.
  - Item 3: `RP:33-34` REACH=LIVE, `DLC:89-90 DelegatedRoleEvidence` REACH=LIVE, `DR:321` roleEvidence REACH=LIVE, `HCP:188,191` REACH=LIVE, `ACS:439-442` REACH=LIVE.
- **Tests:**
  - `RTT/role-policy.test.ts`
  - `RTT/delegated-runtime.test.ts :: runs a turn through the private envelope and records the committed terminal` (L113 enforcementLabel)
  - `RTT/runtime-v3-api.test.ts` L89-91 (managed-delegation route)
  - `FT/components/account-consent-settings.test.ts` L103-104
  - `FT/lib/governed-workflow.test.ts` (policy vocabulary)
- **Decisions:** D-APP-108, D-GOV-35, D-APP-127 (register L152).

## DEL-08-04#SEC-3 — Seating and rulings (SoW L63)
- **Gist:** Records seating under D-APP-108 (V3-02), SR-24, alignment writes WI-061..065 and pending DEP-025/026. States no lifecycle or product act.
- **Code:** NO_CANDIDATES. The unit is documentary. Searches: hints for this unit are empty. Grepped `WI-06|DEP-025|DEP-026|SR-24` in code trees: none.
- **Decisions:** D-APP-108 (DELIVERABLE hits: Dependencies.csv L14 etc.), D-APP-109, D-APP-110. Run evidence `APPX/_Coordination/AgentRuns/APP_SCA_APP_010_SEATING_2026-09-04/`.

## DEL-08-04#CLM-001 — Datasheet heading (SoW L74)
- **Gist:** Section heading only.
- **Code:** NO_CANDIDATES (heading, empty hint token).

## DEL-08-04#CLM-002 — Identification (SoW L79)
- **Gist:** Identity table: ID, name, package, variant v3.2, BACKEND_FEATURE_SLICE, ResponsibleParty TBD, SOW-063, OBJ-005/007.
- **Code:** NO_CANDIDATES. Documentary. Hint tokens are field names only, and none hit a code path.
- **Records:** decomposition `APPX/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (row L371, per SoW L32).

## DEL-08-04#CLM-003 — Attributes (SoW L98)
- **Gist:** Lists the primary function, the authoritative gate, `delegate_agent` as the sole path with the SDK `Agent` retired, parent-relative hierarchy, restricted child constraints, required inputs, denials and the child-record behavior.
- **Code:**
  - `CT:269-298 buildCoordinationMcpTools` (delegate_agent registration) REACH=LEGACY_ONLY
  - `MD:558-600 delegate` (metadata checks) REACH=LEGACY_ONLY
  - `MD:259-340 resolveChild` (0→named 1 / TASK; 1→2; 2→deny L267-269) REACH=LEGACY_ONLY
  - `MD:191 assertChildToolPolicy` REACH=LEGACY_ONLY
  - `MD:172 contained` REACH=LEGACY_ONLY
  - `SG:196` REACH=LEGACY_ONLY
  - `SB:84 createExecutableSubagentBridge` (returns undefined), `SB:92 evaluateSubagentPreflight` (hard-denied) REACH=LEGACY_ONLY
  - `SOB:152` bridge not attached REACH=LEGACY_ONLY
  - `ARC:138 createDelegationChildRunRecord` REACH=LEGACY_ONLY
  - `TD:635` `delegate_agent` descriptor REACH=LIVE
  - `TN:25` REACH=LIVE
  - Live-path analogue: `A1C:105` REACH=LIVE, `RS:223` REACH=LIVE
- **Tests:**
  - `FT/lib/managed-delegation.test.ts :: allows 0→named 1…; allows Agent 1→TASK and denies every delegation attempt from Agent 2; fails closed on missing governance metadata and capability inheritance`
  - `FT/lib/sdk-options-builder.test.ts :: does not attach or expose the retired SDK Agent bridge`
  - `FT/lib/permission-overlay.test.ts :: denies the retired Agent bridge in every mode`
  - `FT/lib/agent-runtime-contract.test.ts :: creates provider-neutral child-run preflight records from governance decisions`
- **Decisions:** D-GOV-14, D-APP-68 (register L83).

## DEL-08-04#CLM-004 — Conditions (SoW L114)
- **Gist:** PRD is current under D-APP-38. R5 sequencing. The boundary is admission and legacy fence, with persistence in DEL-08-05. D-GOV-14 retirement. Dependencies are TBD, with an extracted register.
- **Code:**
  - `SG:196` REACH=LEGACY_ONLY
  - `SB:5-11` policy version / disabled reason REACH=LEGACY_ONLY
  - `ARC:71 ChildRunRecord` (DEL-08-05 handoff) REACH=LEGACY_ONLY
- **Records:** deliverable `_DEPENDENCIES.md`, `Dependencies.csv`. REFERENCE_HASHES shows CONTRACT/SPEC/PRD recorded `MATCH` with recompute `Match=NO`.
- **Decisions:** D-APP-38, D-GOV-14, D-APP-62 (DELIVERABLE `_DEPENDENCIES.md` L164).

## DEL-08-04#CLM-005 — Construction (SoW L127)
- **Gist:** The expected components are the governance bridge, parent-relative child resolution, the legacy fence, the named tests, the DEL-08-05 handoff, and implementation paths naming managed-delegation, subagent-bridge and coordination registration.
- **Code:**
  - `MD:552` REACH=LEGACY_ONLY
  - `MD:259` REACH=LEGACY_ONLY
  - `SB:84,92` REACH=LEGACY_ONLY
  - `CT:269` REACH=LEGACY_ONLY
  - `ARC:138` REACH=LEGACY_ONLY
  - `PO:196,232 requiresManagedDelegationPolicy` REACH=LEGACY_ONLY
  - `CH:469` preflight REACH=LEGACY_ONLY
- **Tests:**
  - `FT/lib/managed-delegation.test.ts` (L402 missing metadata; L127 hierarchy; L436 escaped context/writes/unbounded Bash)
  - `FT/lib/chirality-hooks.test.ts :: blocks the retired Agent bridge even for formerly eligible children`
  - `FT/lib/tool-descriptor.test.ts` L49, L170, L231 (delegate_agent surface)
  - `FT/lib/chirality-tool-bridge.test.ts` L181
- **Decisions:** D-GOV-14, D-APP-68.

## DEL-08-04#CLM-006 — References (SoW L141)
- **Gist:** REF-001..007 table (DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, PRD, AGENT_SOFTWARE_DECOMP), each marked MATCH.
- **Code:** NO_CANDIDATES. Documentary.
- **Records:** `EVIDENCE_PACK/REFERENCE_HASHES.csv` rows for DEL-08-04: CONTRACT, PRD and SPEC are `RecordedVerdict=MATCH` with `Match=NO`. Deliverable `_REFERENCES.md`. REF-007 is cited in the SoW as an absolute user-home path rather than repo-relative (SoW L153).

## DEL-08-04#CLM-007 — D-APP-56 R5 P45 reconciliation (SoW L156)
- **Gist:** Records that the `SubagentGovernanceDecision`, preflight `safeMetadata` and `ChildRunRecord` shapes landed. Only the approval-reference question stays open. UPD-137 aligns DEP-08-04-003.
- **Code:**
  - `SG:23 SubagentGovernanceDecision` REACH=LEGACY_ONLY
  - `SB:22 SubagentPreflightDecision` (safeMetadata L100-113) REACH=LEGACY_ONLY
  - `ARC:71 ChildRunRecord` REACH=LEGACY_ONLY
- **Tests:**
  - `FT/lib/agent-runtime-contract.test.ts :: creates provider-neutral child-run preflight records…; records denied delegation without queueing execution`
  - `FT/lib/harness-subagent-governance.test.ts` (L84-485)
- **Decisions:** D-APP-56 (15 DELIVERABLE hits), D-APP-53.

## DEL-08-04#CLM-033 — Applied decomposition v3 carrier row (SoW L162)
- **Gist:** Verbatim applied row: bridge plus class-aware routing, native descent assigning no role, Codex role labels, daemon-client dispatch outputs, D-APP-74 superseded prospectively, D-GOV-35 plus WP-03/05 required.
- **Code:**
  - Daemon/runtime side: `A1C:105` REACH=LIVE, `DR:321` REACH=LIVE, `RP:20-43` REACH=LIVE, `RMS:589` REACH=LIVE, `NRC:141-143` REACH=LIVE, `CS:280-309` descendant handling REACH=LIVE (touched file; L280-309 outside touched ranges), `RS:223` REACH=LIVE
  - App side: `HCP:185-191` REACH=LIVE, `ACS:185,439-445` REACH=LIVE
  - Legacy bridge: `MD` (overlap `MD:467-505`) REACH=LEGACY_ONLY, `SG:205-213` REACH=LEGACY_ONLY
- **Tests:**
  - `RTT/role-policy.test.ts`
  - `RTT/agent1-run.test.ts` (L201-522)
  - `RTT/codex-supervisor.test.ts :: defers for an active grandchild after the primary retires without interrupting it; resolves descendant questions…`
  - `RTT/descendant-tracker.test.ts`
  - `FT/lib/managed-delegation.test.ts :: rejects active exact and ancestor-overlapping sibling writes`
- **Decisions:** D-GOV-35 (`APPX/_Coordination/NOTICE_D-GOV-35_DELEGATED_HARNESS_NATIVE_CLASS.md`, L3 notes the D-GOV-43 re-expression), D-APP-74, D-APP-108, D-APP-127 (register L152).

## DEL-08-04#CLM-008 — Specification heading (SoW L176)
- **Gist:** Section heading only.
- **Code:** NO_CANDIDATES (heading).

## DEL-08-04#CLM-009 — Scope (SoW L181)
- **Gist:** Covers `delegate_agent` as the sole path, the governance gate, parent-relative eligibility, the retired SDK `Agent` and child tool/cwd restrictions with tests. Excludes SDK mechanics, persistence and Dependencies.csv.
- **Code:** `CT:269` REACH=LEGACY_ONLY, `SG:196` REACH=LEGACY_ONLY, `MD:259`, `MD:191` REACH=LEGACY_ONLY, `SB:84,92` REACH=LEGACY_ONLY, `SOB:152-160` REACH=LEGACY_ONLY.
- **Tests:** as CLM-005.
- **Decisions:** D-GOV-14, D-APP-68.

## DEL-08-04#CLM-010 — Requirements R01–R11 (SoW L201)
- **Gist:** Eleven MUST/SHOULD requirements: pre-launch admission, hierarchy/seal/approval denial, metadata and allowlist denial, sole path, restricted children, fail-closed, Chirality semantics, unknown→deny, DEL-08-05 interface.
- **Code (per requirement):**
  - R01, R08: `MD:558-600` REACH=LEGACY_ONLY; `CT:288-297` REACH=LEGACY_ONLY; child turns call `TE:232 evaluateSubagentGovernance` via `CT:130-146` REACH=LEGACY_ONLY.
  - R02, R05: `MD:259-340` REACH=LEGACY_ONLY; `SG:142-195 resolveDelegatedSubagents` REACH=LEGACY_ONLY.
  - R03, R10: `SG:250-289` REACH=LEGACY_ONLY; `MD:559-585` REACH=LEGACY_ONLY.
  - R04: `MD:282-284` allowlist REACH=LEGACY_ONLY; `SG:239-247` REACH=LEGACY_ONLY.
  - R06: `SB:84-90` REACH=LEGACY_ONLY; `SOB:152-160` REACH=LEGACY_ONLY; `PO:196` REACH=LEGACY_ONLY; `CH:469` REACH=LEGACY_ONLY.
  - R07: `MD:191-208`, `MD:172`, `MD:210-257` REACH=LEGACY_ONLY.
  - R09: `ARC` REACH=LEGACY_ONLY.
  - R11: `ARC:71,138` REACH=LEGACY_ONLY; `MD:431 refreshOrchestrationHandoff` REACH=LEGACY_ONLY.
  - Live analogue: `A1C:140-290` (Agent 1 target and one-child rules) REACH=LIVE; `RS:223` REACH=LIVE.
- **Tests:**
  - `FT/lib/managed-delegation.test.ts` (L104-801)
  - `FT/lib/harness-subagent-governance.test.ts :: fails closed on instruction-root errors` and others
  - `FT/lib/sdk-options-builder.test.ts :: denies legacy Agent permission callbacks even for formerly eligible children`
  - `FT/api/harness/routes.test.ts :: does not allow opts.subagentGovernance to bypass runtime environment gate`
  - `RTT/agent1-run.test.ts :: rejects empty approval attribution before creating a run`
- **Decisions:** D-GOV-14, D-APP-68.

## DEL-08-04#CLM-011 — Governance Decision Contract (SoW L220)
- **Gist:** The decision object is TBD. Minimum field families: allow/deny/ask, audit-safe reason, decision source, approval ref, candidate/scope facts, DEL-08-05 handoff.
- **Code:**
  - `SG:13-38 GovernanceGateId / SubagentGovernanceDecision` REACH=LEGACY_ONLY
  - `SB:22-38`, `SB:92-117` safeMetadata REACH=LEGACY_ONLY
  - `ARC:71` REACH=LEGACY_ONLY
  - `MD:693` policyVersion REACH=LEGACY_ONLY
  - `RF:31` REACH=LEGACY_ONLY
  - Live analogue: `DLC:86-93 DelegatedRoleEvidence` REACH=LIVE
- **Tests:** `FT/lib/harness-subagent-governance.test.ts`; `FT/lib/agent-runtime-contract.test.ts` L68, L102; `FT/api/harness/routes.test.ts` L374 (managedDelegationPolicyVersion).
- **Decisions:** D-APP-56, D-APP-117 (approval/decision evidence; AWAITING_RULING, register L133).

## DEL-08-04#CLM-012 — Standards (SoW L236)
- **Gist:** Lists the applicable CONTRACT K-SEAL/K-GHOST/K-SUBAGENT, SPEC §14-15, TYPES §10, PLAN R5, PRD §8.15 and decomposition sizing rules.
- **Code:** `SG:196` REACH=LEGACY_ONLY (named `evaluateSubagentGovernance`); no further code.
- **Records:** `projects/chirality-app-dev/docs/CONTRACT.md` (L128 K-UNTYPED-1 and L229 K-ROLE-2 are D-GOV-43-era clauses bearing on delegation). REFERENCE_HASHES as CLM-006.

## DEL-08-04#CLM-013 — Verification R01–R11 (SoW L250)
- **Gist:** A verification approach for each requirement, plus a closure list of fixtures: missing metadata, approval ref, unsealed context, allowlist, hierarchy, launch error, broad capability, allowed path, audit-safe reasons, handoff.
- **Tests (candidates):**
  - `FT/lib/managed-delegation.test.ts`: L402 (missing metadata, capability inheritance), L127 and L280 (hierarchy), L166 (TASK class), L229 (dedicated A2 unruled), L436 (escaped context/writes), L601 (failed node isolation), L626 (schema-invalid returns)
  - `FT/lib/harness-subagent-governance.test.ts`: L124 missing metadata, L147 strict booleans, L185 empty approvalRef, L109 allowlist, L485 instruction-root errors
  - `FT/lib/permission-overlay.test.ts` L195
  - `FT/lib/chirality-hooks.test.ts` L541
  - `FT/lib/sdk-options-builder.test.ts` L576, L840
  - `FT/lib/agent-runtime-contract.test.ts` L68, L102
- **Code:** as CLM-010. All REACH=LEGACY_ONLY.
- **Note:** No test case named "launch error" or "hook failure" by title was found. Candidates are `managed-delegation.test.ts :: isolates a failed node…` and `harness-subagent-governance.test.ts :: fails closed on instruction-root errors`.

## DEL-08-04#CLM-014 — Documentation (SoW L271)
- **Gist:** Required artifacts: the bridge, resolution/admission logic, tool-surface and retirement tests, denial fixtures, the DEL-08-05 handoff, and an implementation path record.
- **Code:** `SG`, `MD`, `SB`, `CT`, `ARC` (all REACH=LEGACY_ONLY).
- **Tests:** as CLM-013.
- **Records:** deliverable `_run_records/` (e.g. `AGENT0_DIRECT_A2_HARNESS_REPAIR_2026-08-16.md`, which carries D-APP-64 at L23).

## DEL-08-04#CLM-015 — Conflict Table C-001 (SoW L285)
- **Gist:** The PRD source-state warning (REF-006) is resolved by D-APP-38. Proposed handling uses PRD text while keeping implementation proof separate.
- **Code:** NO_CANDIDATES. Documentary.
- **Decisions:** D-APP-38 (13 DELIVERABLE hits).

## DEL-08-04#CLM-016 — D-APP-56 reconciliation + REQ-001..005, AC-001/002 (SoW L294; SubItems REQ-001|…|AC-002)
- **Gist:** Repeats the UPD-135/136 shapes. v3 REQ-001..005: bridge/graph, native class, enforcement set, Codex role labels, D-APP-74 superseded plus prerequisites. AC-001 covers the legacy checks and AC-002 the v3 outputs.
- **Code:**
  - REQ-001, REQ-003: `MD:552`, `MD:467` REACH=LEGACY_ONLY; `A1C:105`, `A1C:235-303` (sealed brief) REACH=LIVE; `A1C:120` interrupt REACH=LIVE; `DR` cancellation/cleanup REACH=LIVE.
  - REQ-002: `RP:43 nativeDescendant` REACH=LIVE; `NRC:141-143` REACH=LIVE; `CS:280-309` REACH=LIVE; `ACS:445` REACH=LIVE.
  - REQ-004: `RP:33-34` REACH=LIVE; `HCP:185-191` REACH=LIVE; `ACS:185,439-442` REACH=LIVE; `RS:223` REACH=LIVE.
  - REQ-005: NO code (governance prerequisite).
  - AC-001: legacy MD/SG/SB REACH=LEGACY_ONLY.
  - AC-002: as CLM-033.
- **Tests:**
  - `RTT/delegated-runtime.test.ts :: latches cancellation before acquisition publication…; order A/order B…cleanup settles once; closes by interrupting live turns and retiring every worker`
  - `RTT/agent1-run.test.ts :: interrupts an active Agent 2 child…`
  - `RTT/role-policy.test.ts`
  - `FT/components/account-consent-settings-states.test.ts` L368, L390, L398
  - `FT/lib/managed-delegation.test.ts` L471, L491, L517
- **Decisions:** D-APP-56, D-APP-74, D-GOV-35, D-APP-127.

## DEL-08-04#CLM-017 — Procedure heading (SoW L310)
- **Gist:** Section heading only.
- **Code:** NO_CANDIDATES (heading).

## DEL-08-04#CLM-018 — Purpose (procedure) (SoW L315)
- **Gist:** Define the steps that produce and verify managed child admission through `delegate_agent`.
- **Code:** `CT:269` REACH=LEGACY_ONLY, `MD:552` REACH=LEGACY_ONLY.

## DEL-08-04#CLM-019 — Prerequisites (SoW L322)
- **Gist:** Prerequisites: corpus available, status INITIALIZED, `evaluateSubagentGovernance` shape TBD, permission/hook infrastructure, D-GOV-14 ruled, upstream dependencies TBD.
- **Code:** `SG:196` exists REACH=LEGACY_ONLY. `PO` and `CH` (permission/hook infrastructure) REACH=LEGACY_ONLY.
- **Records:** `_STATUS.md` L3 (Current State IN_PROGRESS). `_DEPENDENCIES.md`.
- **Decisions:** D-GOV-14.

## DEL-08-04#CLM-020 — Steps 1–13 (SoW L336)
- **Gist:** Thirteen steps: locate the gate, define inputs, set fail-closed defaults, record paths, resolve eligibility, restrict the child, keep the SDK Agent disabled, admit before launch, deny on failure, return safe reasons, provide the handoff, add tests, and cover `allowedTools`-alone regressions.
- **Code:** `SG:196` (step 1), `MD:54-79 DelegateAgentInput` (step 2), `MD:558-585` (step 3), `MD:259` (step 5), `MD:191,172` (step 6), `SB:84` and `SOB:152` (step 7), `MD:552`→`CT:288` (step 8), `SG:58 deny` (step 10), `ARC:138` (step 11). All REACH=LEGACY_ONLY.
- **Tests:** `FT/lib/sdk-options-builder.test.ts` L576, L840 (step 13 candidate); `FT/lib/permission-overlay.test.ts :: denies unapproved write, shell, network, subagent, and unknown tools in dontAsk mode`.

## DEL-08-04#CLM-021 — Verification checks table (SoW L355)
- **Gist:** Eleven expected results: denials, hook-error fail-close, narrowing, allowed governed request, legacy bridge disabled, audit-safe reasons, persistence handoff.
- **Code/Tests:** as CLM-013. All code REACH=LEGACY_ONLY.

## DEL-08-04#CLM-022 — Records + VER-001/VER-002 (SoW L374; SubItems VER-001|VER-002)
- **Gist:** Lists the records to produce and says not to touch Dependencies.csv. VER-001 runs the legacy checks. VER-002 runs the v3 routing, overlap, role/native-origin, sealed-brief, containment, approval, cancellation and cleanup tests and checks the labels.
- **Code:**
  - VER-001: MD/SG/SB/CT/ARC REACH=LEGACY_ONLY.
  - VER-002: `RMS:589` REACH=LIVE; `MD:467` REACH=LEGACY_ONLY; `RP:20-43` REACH=LIVE; `A1C` REACH=LIVE; `DR` REACH=LIVE; `ACS:185` REACH=LIVE.
- **Tests:**
  - VER-001: as CLM-013.
  - VER-002: `RTT/runtime-v3-api.test.ts` L89-91, `RTT/role-policy.test.ts`, `RTT/agent1-run.test.ts`, `RTT/delegated-runtime.test.ts`, `RTT/codex-supervisor.test.ts` L282, L436, `RTT/descendant-tracker.test.ts`, `FT/components/account-consent-settings-states.test.ts` L368-398, `FT/lib/managed-delegation.test.ts` L471-545.
  - No test was found that names WP-03/WP-05 fixtures (grep `WP-03|WP-05` in test trees: none).

## DEL-08-04#CLM-023 — Guidance heading (SoW L395)
- **Gist:** Section heading only.
- **Code:** NO_CANDIDATES (heading).

## DEL-08-04#CLM-024 — Purpose (guidance) (SoW L400)
- **Gist:** Admit a child only when the product gate allows, eligibility holds, context is sealed, approvals are traceable and capabilities are bounded. The SDK Agent is no fallback.
- **Code:** `MD:552-600` REACH=LEGACY_ONLY, `SB:84-117` REACH=LEGACY_ONLY.

## DEL-08-04#CLM-025 — Principles (SoW L407)
- **Gist:** Deny first, Chirality-owned semantics, parent-relative hierarchy, no capability inheritance, sealed context only, approval as evidence, gate separate from persistence.
- **Code:** `SG:196-318` REACH=LEGACY_ONLY; `MD:191,259,558` REACH=LEGACY_ONLY; `MD:311-329` dedicated-A2 approval resolution against `docs/governance_harness/_DECISIONS` REACH=LEGACY_ONLY; `ARC:138` REACH=LEGACY_ONLY.
- **Tests:** `FT/lib/managed-delegation.test.ts :: fails closed for a dedicated Agent 2 whose qualification is not ruled`; `FT/lib/harness-subagent-governance.test.ts`.

## DEL-08-04#CLM-026 — Considerations (SoW L422)
- **Gist:** The bridge stays disabled if prerequisites are absent. `allowedTools` is not a boundary. Hook failure fails closed. Prefer `AGENT_TYPE: 2`. Child cwd is bounded. Denial reasons are safe. REF-006 is current.
- **Code:**
  - `SG:233-240` env gate `CHIRALITY_ENABLE_SUBAGENTS` REACH=LEGACY_ONLY
  - `SG:302-317` INTERNAL_ERROR catch REACH=LEGACY_ONLY
  - `SG:142-195` AGENT_TYPE/AGENT_CLASS parse REACH=LEGACY_ONLY
  - `MD:172 contained` (executionRoot L~642) REACH=LEGACY_ONLY
  - `SOB:152-160` allowed/disallowed tool lists REACH=LEGACY_ONLY
- **Tests:** `FT/lib/harness-subagent-governance.test.ts :: denies when CHIRALITY_ENABLE_SUBAGENTS is not true; warns but allows TYPE 2 subagents that are not TASK class; fails closed on instruction-root errors`.

## DEL-08-04#CLM-027 — Trade-offs (SoW L435)
- **Gist:** Prefer denial, Chirality types over provider shape, narrow child capability, and a minimal handoff to DEL-08-05.
- **Code:** `MD:191`, `MD:210-257` (bounded Pi/oMLX selection), `ARC` (all REACH=LEGACY_ONLY).
- **Tests:** `FT/lib/managed-delegation.test.ts :: authorizes and attributes only the bounded Pi/oMLX Agent 2 shape; fails closed on Pi/oMLX scope expansion…`.
- **Decisions:** D-APP-72 (Pi child engine selection, DELIVERABLE `_STATUS.md` L66).

## DEL-08-04#CLM-028 — Examples (SoW L447)
- **Gist:** Eight scenarios: missing approval ref, mutable approval evidence, 0→2 denied, 1→TASK eligible, 2→any denied, unsealed context, broad tools, hook throw.
- **Code:** `MD:559-561` (seal/approval), `MD:291-300` (0→2), `MD:267-269` (2 denied), `MD:302-304` (1→2), `MD:191` (tools), `SG:302` (throw). All REACH=LEGACY_ONLY.
- **Tests:** `FT/lib/managed-delegation.test.ts` L127, L280, L402, L436; `FT/lib/harness-subagent-governance.test.ts` L185, L485.
- **Note:** No code was found that validates approval-ref *format* beyond non-empty. Dedicated-A2 approval uses `D-GOV-\d+` at `MD:312-314`.

## DEL-08-04#CLM-029 — Conflict Table (guidance) C-001 (SoW L463)
- **Gist:** The REF-006 warning is resolved by D-APP-38. No further ruling is needed.
- **Code:** NO_CANDIDATES. Documentary.
- **Decisions:** D-APP-38.

## DEL-08-04#CLM-030 — Open Items (SoW L472)
- **Gist:** Implementation paths resolved. Decision-object shape TBD. Approval-ref format TBD. Legacy posture resolved. DEL-08-05 boundary TBD.
- **Code:** `SG:23`, `SB:22`, `ARC:71` REACH=LEGACY_ONLY.
- **Decisions:** D-GOV-14; D-APP-117 (AWAITING_RULING; register L133) for the approval/decision-evidence line; D-APP-103 (RULING record `APPX/_Coordination/_DECISIONS/D-APP-103_RULING_PER_ATTEMPT_DECISION_REPLAY_PACKET_2026-08-17.md` L16).

## DEL-08-04#CLM-031 — D-APP-56 reconciliation (axiology copy) (SoW L485)
- **Gist:** Same text as CLM-007.
- **Code/Tests/Decisions:** as CLM-007.

## DEL-08-04#CLM-032 — D-APP-68 managed-delegation refresh (SoW L491)
- **Gist:** SDK Agent retired, `delegate_agent` is the sole path, parent-relative eligibility, DEL-08-04 owns admission and DEL-08-05 the lifecycle, and decision replay stays gated.
- **Code:** `SB:8-11,84-117` REACH=LEGACY_ONLY; `CT:269` REACH=LEGACY_ONLY; `MD:259` REACH=LEGACY_ONLY; `MD:806 reportCoordinationNotice`, `MD:835 sendAgentUpdate`, `MD:975 acknowledgeAgentUpdate` REACH=LEGACY_ONLY.
- **Tests:** `FT/lib/managed-delegation.test.ts :: persists child→parent notices and parent→child updates with acknowledgments`; `FT/lib/pkg08-compatibility-boundaries.test.ts :: does not turn Pipeline presentation state into delegation authority`.
- **Decisions:** D-APP-68 (register L83), D-GOV-14, D-APP-53.

## DEL-08-04#REM-1 — Per-attempt decision-replay packet (_STATUS L11)
- **Gist:** The D-APP-117 packet was prepared under D-APP-103. Implementation is gated on the owner ruling. The packet is PROPOSAL/AWAITING_RULING.
- **Gate suffix (verbatim):** `gated: owner ruling on D-APP-117`
- **Gate status check (App):** `APPX/_Coordination/_DECISIONS/_REGISTER.md` L133 (State `AWAITING_RULING` at basis); packet `APPX/_Coordination/_DECISIONS/D-APP-117_PACKET_PER_ATTEMPT_DECISION_REPLAY_2026-09-05.md`.
- **Code:** NO_CANDIDATES. No implementation is expected while the item is gated. Grep `decision-replay|perAttempt|per-attempt` in code trees found nothing relevant.
- **Decisions:** D-APP-117 (AWAITING_RULING), D-APP-103 (RULED; register L118, ruling L16), D-APP-114 (register L129), D-APP-53.

## DEL-08-04#REM-2 — DEL-08-04-V3-01 class-aware managed/native bridge (_STATUS L17)
- **Gist:** A class-aware delegation bridge for v3 with role/native-origin, sealed-brief, containment, approval, cancellation and cleanup conformance evidence. The write locus is `subagent-governance.ts` L205-213 and `managed-delegation.ts`.
- **Gate suffix (verbatim):** `NOT_SELECTABLE_UNTIL: Root WP-03/WP-05 fixtures (accepted DEL-02-07 supervisor and DEL-02-10 API v2 returns routed to App); G-ROLE/G-APPR/G-SBX/G-SENT/G-PROT/G-ENV/G4 for claims`
- **Gate status check (App surfaces):**
  - Root WP-03/WP-05 and DEL-02-07/DEL-02-10 returns: routed notices in `APPX/_Coordination/NOTICE_*.md`. None names WP-03/WP-05 at basis (grep).
  - D-GOV-35 class: `APPX/_Coordination/NOTICE_D-GOV-35_DELEGATED_HARNESS_NATIVE_CLASS.md` (L3: read with D-GOV-43).
  - G-* gates: `projects/chirality-app-dev/docs/CONTRACT.md` (G-ROLE in K-ROLE-2 L229) and `APPX/_Decomposition/contract_invariant_coverage_register.csv` (G-SENT/G-PROT hits).
  - Hold state: `APPX/_Coordination/APP_HOLD_REGISTER.csv` (header only at basis).
- **Code:**
  - Named write locus: `SG:205-213` REACH=LEGACY_ONLY; `MD:467-505` (sibling-overlap fail-close; the SoW cites 480-496) REACH=LEGACY_ONLY.
  - Live analogues: `RP` REACH=LIVE, `A1C` REACH=LIVE, `DR` REACH=LIVE, `NRC` REACH=LIVE, `CS:280-309` REACH=LIVE, `RS:223` REACH=LIVE.
- **Tests:** as CLM-022 VER-002. No WP-03/05 fixture was found.
- **Decisions:** D-GOV-35 (ROOT), D-APP-127 (register L152), D-APP-36 (render bar), D-APP-108.

## DEL-08-04#REM-3 — DEL-08-04-V3-02 per-session delegation policy (_STATUS L26)
- **Gist:** The managed bridge honours the per-session delegation policy (`none` default; ask-per-brief, approve-brief-writes, bounded-briefs) as narrowing. It adds no new class.
- **Gate suffix (verbatim):** `NOT_SELECTABLE_UNTIL: DEL-02-02-V3-04 selected`
- **Gate status check (App):** `APPX/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX/_STATUS.md` L42. At basis, DEL-02-02-V3-04 carries its own `NOT_SELECTABLE_UNTIL: DEL-02-02-V3-03 landed; DEL-07-03-V3-01 landed`, and History L53 records a bounded read-only V3-04 slice. Paired item: `APPX/PKG-03*/1_Working/DEL-03-02*/_STATUS.md` L11 (DEL-03-02-V3-01, gated on this item).
- **Code:**
  - Policy vocabulary `GW:24,37,87-91` REACH=TEST_ONLY (policy names in the test fixture: `none`, `ask-before-each-brief`, `approve-each-write`, `bounded-briefs`; they differ in spelling from the _STATUS wording).
  - Named write locus `MD:552`, `SG:196` REACH=LEGACY_ONLY.
  - `RP:11 delegationPolicy` field (RolePolicySettings) REACH=LIVE.
  - No live per-chat policy carrier or admission check was found. Grep `delegationPolicy|delegation_policy|bounded-briefs|ask-before-each-brief` hits only `RP:11,27` and test fixtures.
- **Tests:** `FT/lib/governed-workflow.test.ts` (L11, L59-62 policy validation).
- **Decisions:** D-APP-108 (seating), SR-24 (named in SoW L66; not located as a separate register ID).

---

## Cross-cutting

- **Recurring modules (units citing them):**
  - `MD` managed-delegation.ts REACH=LEGACY_ONLY: ~25 units
  - `SG` subagent-governance.ts REACH=LEGACY_ONLY: ~20
  - `SB` subagent-bridge.ts REACH=LEGACY_ONLY: ~12
  - `ARC` agent-runtime-contract.ts REACH=LEGACY_ONLY: ~11
  - `CT` coordination-tools.ts REACH=LEGACY_ONLY: ~9
  - `RP` role-policy.ts REACH=LIVE and `A1C` agent1-run-coordinator.ts REACH=LIVE: ~7 each
  - `HCP`/`ACS` consent port and settings REACH=LIVE: ~6
- **Live-versus-legacy split (reach facts only):**
  - The whole App-side `delegate_agent` stack is REACH=LEGACY_ONLY in `REACHABILITY.csv`, with each module listed as its own entry point (no LIVE import chain). That stack covers the `delegate_agent` MCP registration (CT), `ManagedDelegationService` (MD), `evaluateSubagentGovernance` (SG), the disabled SDK bridge (SB), preflight hooks/overlay (CH, PO), TurnEngine (TE), the ChildRunRecord contract (ARC) and the fingerprint (RF).
  - The `delegate_agent` descriptor and name in runtime contracts (TD, TN) are LIVE.
  - Live delegation-related code is in the runtime: the Agent 1 coordinator with sealed brief, one child, interrupt (A1C); delegated runtime with role evidence, cancellation and cleanup (DR); role-policy labels and `nativeDescendant` (RP); the Agent 2 direct-entry refusal (RS:223); the managed-delegation route disposition (RMS:589); native role pins and descendant handling (NRC, DT, CS).
  - On the App side, live code is limited to the role-label UI and port (ACS, HCP, SSV). `toolkit.ts` (TK, LIVE) still builds an `opts.subagentGovernance` object at TK:150-160.
  - Per-chat policy vocabulary exists only in TEST_ONLY `governed-workflow.ts`.
- **Touched paths:** no cited line falls in a `TOUCHED_PATHS.csv` range. `codex-supervisor.ts` is a touched file (`da95ec194`/`cb08dbe2f`). The cited L280-309 lies outside its ranges (nearest: 271-273, 391-392). No `frontend/src/lib/harness/**` path is on the touched list.
- **D-APP-127 application map:** all five DEL-08-04 carriers show `Revised=NO` / `NONE_FOUND`.
- **Reference hashes:** CONTRACT, SPEC and PRD are recorded `MATCH` in `_REFERENCES.md`, but the recompute gives `Match=NO`.

#END
