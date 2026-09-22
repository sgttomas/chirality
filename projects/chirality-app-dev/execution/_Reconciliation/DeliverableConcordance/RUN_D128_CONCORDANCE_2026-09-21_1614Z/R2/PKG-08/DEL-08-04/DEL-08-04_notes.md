# DEL-08-04 forward notes (RUN_D128, R2 PKG-08)

- Ledger: `DEL-08-04_claims.csv`. It was sealed after the forward pass with SHA-256 `9f0081348675b4f1c8aa13b2556aec335c6d3f2cd0b1d1c8ce91af6e45211267`.
- Validator result: `RULES errors none | warnings none`, `RESULT PASS errors=0 warnings=0`.
- Basis: the frozen tree at `00115c719`. Disposition is evidence only, not a ruling.

## 1. Census

- **Rows:** 56 in total. 48 rows cover the 39 indexed units (3 SEC, 33 CLM, 3 REM), and 8 are run-local (REGISTER-1..5, STATE-1).
- **Split rate:** 5 of the 39 units are split (12.8%).
  - SEC-2 has 3 numbered obligations.
  - CLM-003 is an attribute table: the "Governance gate" row is split from the other rows.
  - CLM-010: R06 is split from the other ten requirements.
  - CLM-016 lists 7 SubItems: REQ-001..005, AC-001, AC-002.
  - CLM-022 lists 2 SubItems: VER-001, VER-002.
- **SEE rows** (counted separately): 14. SEC-2.1, CLM-033 and CLM-016.3 point to SEC-1. CLM-009 points to CLM-003.1. CLM-016.4 points to SEC-2.3. CLM-021 and CLM-022.1 point to CLM-013. CLM-024, CLM-025, CLM-026 and CLM-028 point to CLM-003.2. CLM-029 points to CLM-015. CLM-030 points to CLM-011. CLM-031 points to CLM-007.

| ClaimType | n |
|---|---|
| REQUIREMENT | 24 |
| CONTEXT_CLAIM | 11 |
| STATE_ASSERTION | 8 |
| ACCEPTANCE | 5 |
| REGISTER_DEFECT | 5 |
| REMAINING_WORK | 3 |

| Disposition | n (of which SEE) |
|---|---|
| STALE_SPECIFICATION | 14 (2) |
| ALIGNED | 11 (2) |
| PARTIALLY_IMPLEMENTED | 10 (5) |
| NOT_AUDITABLE | 8 (1) |
| IMPLEMENTED_DIFFERENTLY | 6 (4) |
| REMAINING_STATE_MISMATCH | 6 (0) |
| DOCUMENTED_UNIMPLEMENTED | 1 (0) |

- **HumanDecisionNeeded:** NO 27, R4-Q1 26, `D-APP-117; R4-Q1` 2, D-APP-117 1.
- **Errata:** none yet. Sealed and errata-applied figures will be shown side by side if the reverse pass writes an errata file.

**Central finding.**
- On the live path, the Runtime service owns delegation (K-RUNTIME-1).
  - Children come from Codex-native `[agents]` descent: `native-role-config.ts:141-143` pins `maxDepth 2`.
  - Nothing implements `delegate_agent` beyond the contracts descriptor.
- The whole App `delegate_agent` admission stack is `REACH=LEGACY_ONLY`. That covers managed-delegation, subagent-governance, subagent-bridge, coordination-tools and agent-runtime-contract. Its tests pass (GATE-TRANSCRIPT APP).
- `GovernedAgent1RunCoordinator` is LIVE in the static map (exported by core `index.ts`), but only `tests/agent1-run.test.ts` constructs it.
- What is live:
  - role labels: `role-policy.ts` and the consent port/settings UI;
  - native no-role handling;
  - Agent 2 direct-entry refusal (`runtime-service.ts:223`);
  - a route label (`runtime-method-service.ts:589`).
- The per-chat delegation policy has no live carrier. `delegated-runtime.ts:321` uses a fixed policy string.
- Where a legacy behaviour requirement is judged on the live path, it is `IMPLEMENTED_DIFFERENTLY` / `R4-Q1`. Module-level artifact claims (documentation, steps, AC-001, dated notes) are `ALIGNED` with `REACH=LEGACY_ONLY`.

## 2. Least-confident rows

- **REM-3 (LOW):** REMAINING_STATE_MISMATCH / A2_TOPOLOGY, with MechanicallyUnblocked NO.
  - Alternative reading 1: the DEL-02-02 History L53 records a bounded read-only V3-04 slice. That can be read as V3-04 having been "selected", which would make the gate YES.
  - Alternative reading 2: the disposition could be ALIGNED if the App-harness write locus is read as legitimate compatibility scope, pending R4-Q1.
- **SEC-2.3 / CLM-016.4 (MEDIUM, ALIGNED):**
  - Is Codex role selection in the Settings UI actually wired through to the Runtime role evidence? This was not traced end to end.
  - The Runtime labels every role, not only Agent 2/TASK.
- **CLM-016.2 (MEDIUM, ALIGNED):** no production caller sets `nativeDescendant=true`. The native class is tracked in the supervisor instead. A stricter reader could call this PARTIALLY_IMPLEMENTED.
- **CLM-016.5 (MEDIUM, ALIGNED):** it is not stated on an App surface whether the WP-03/05 prerequisite (Root DEL-02-07 supervisor, DEL-02-10 API v2) survives D-GOV-43. Its premise may be partly moot.
- **SEC-3 (MEDIUM):** the DEP-025/026 → DEP-08-04-013/014 mapping is inferred.
- **REGISTER-1..3 (MEDIUM):** DirectionEvidence attributes the CONTRACT/SPEC/PRD drift to the D-GOV-43 application tranche. That was inferred from the K-RUNTIME-1 wording, not from a diff.

## 3. Register-defect summary

- **REGISTER-1..3:** `_REFERENCES.md` records MATCH for CONTRACT, SPEC and PRD, but those hashes do not recompute at `00115c719` (pack `REFERENCE_HASHES.csv`, all three `Match=NO`). DIRECTIVE, TYPES, PLAN and REF-007 (the software-decomp WORKFLOW) recompute equal.
- **REGISTER-4:** `_REFERENCES.md` reuses REF-009 and REF-010 for two different sources each (L14-15 vs L22-23).
- **REGISTER-5:** SoW REF-007 is an absolute user-home path to `agents/AGENT_SOFTWARE_DECOMP.md`. That file is absent at the basis, and the SoW table disagrees with `_REFERENCES.md` REF-007.
- **Also recorded:**
  - STATE-1: the `daemon` wording in `_CONTEXT.md`, `Dependencies.csv` and the SoW applied-row notes, stale under A2.
  - D-APP-127 application map: all five carriers `Revised=NO`. D-APP-127 names no PKG-08 carrier.

## 4. Direction and cause

- **Main CauseTags:**
  - NATIVE_DELEGATION (11): the live path uses Codex-native descent, not the managed bridge.
  - LIFECYCLE_GATE_PENDING (8): v3 items REM-2 and REM-3 are gated.
  - DOC_HYGIENE (7), PRE_V3_DRIFT (5), CARRIER_PROPAGATION (2), A2_TOPOLOGY (2), SHELL_REDESIGN (1), CODEX_SOLE_ENGINE (1).
- **CAUSE2 secondaries:** CARRIER_PROPAGATION 9, NATIVE_DELEGATION 8, CODEX_SOLE_ENGINE 7, A2_TOPOLOGY 4, PRE_V3_DRIFT 3.
- **GOVERNING records used:**
  - D-GOV-43, through App CONTRACT K-UNTYPED-1 L128 and K-RUNTIME-1 L224;
  - D-GOV-35;
  - D-APP-68, D-APP-56, D-APP-108, D-APP-109, D-APP-54, D-APP-103;
  - D-APP-117 (AWAITING_RULING; its rows are held).
- **CONTEXT record used:** `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/SPIKE_DESIGN.md` §4 L212-216 ("No Chirality-side spawner"; delegation via Codex `[agents]`), with HANDOFF.md L223-225.
- **Authority handling:**
  - TYPES §10 (L560-561) outranks the SoW that calls `evaluateSubagentGovernance` "the authoritative gate" (CLM-003.1, CLM-009).
  - CONTRACT K-RUNTIME-1 outranks decomposition row L371's "daemon owns operational managed delegation" (STATE-1).
  - DIRECTIVE §0 order resolves both, so neither is AUTHORITY_CONFLICT.
- **Searches behind the NONE_FOUND values:**
  - CLM-006, CLM-012, REGISTER-4, REGISTER-5: searched `_REGISTER.md` (D-APP-38 L53, D-APP-108 L123) and the CONTEXT sources (plans/steers, AgentRuns APP_V3_*, APPDEV_V3_NODE_*). None records the REF-007 retarget or the RefID reuse.
  - WP-03/WP-05 routing: grep over `execution/_Coordination/NOTICE_*` found none.
- **Done-declaration:** not consulted (CONTEXT only). No Q-01..Q-13 cited.

## 5. Method friction

- **REACH for exported-but-unconstructed classes.** The static map tags `agent1-run-coordinator.ts` LIVE because `index.ts` re-exports it, but no product code instantiates it.
  - Proposal: add a note token such as `UNINSTANTIATED` alongside `REACH=LIVE`, or let the reachability builder follow construction sites for classes.
- **Module-level versus live-path judgment.** For a legacy deliverable whose whole subject is the retained harness, the line between "a claim about the retained module" (module-level) and "a requirement met only on LEGACY_ONLY" (live path) is thin.
  - This ledger applied it as: artifact, method and dated-note claims are module-level; behavioural MUST/guidance claims are judged on the live path. The two classes get opposite dispositions for the same code.
  - Proposal: state this split in CONVENTIONS §2.3.
- **Carrier wording that the GOVERNING decomposition row shares.** "daemon" in STATE-1 has no dedicated route when the governing decomposition row carries the same stale wording. The EXT `SOW` ledger may hold the row-level finding.

## 6. Effort

- **Files read:** about 30, mostly in part.
  - Rulebook, run basis, pregather, brief, and five pack files (filtered).
  - Deliverable: SoW, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, MEMORY, Assessment, Dependencies (filtered).
  - Register rows, D-APP-127, D-GOV-43, the D-GOV-35 notice header, CONTRACT/TYPES/PRD extracts, and the decomposition rows.
  - About 12 code files (line ranges), test-title greps, and both gate transcripts.
- **Not read:** `_SEMANTIC*.md`, `_DEPENDENCIES.md` in full, and `_run_records/**` bodies.
- **Git:** read-only `blame -L` on `codex-supervisor.ts` L280-309 and `app-owned-composition.ts` L200-205. Both blame to non-listed commits, so PostReleaseBasis is NO for every row.
- **Context budget:** adequate, not tight.
- **Inadvertent read:** one broad `grep -l` listed file names under `projects/chirality-runtime/execution/**`. No such file was opened.
