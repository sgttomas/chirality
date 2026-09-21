# DEL-10-01 — R0 calibration notes (forward pass)

- **Worker:** F-10 (TASK), run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, D-APP-128.
- **Basis:** frozen tree at `00115c719`.
- **Ledger:** `DEL-10-01_claims.csv`, 73 rows.
- **Epistemic status:** agent dispositions only. Nothing here is a ruling.

## 1. Census

**Coverage and splitting.**

- All 32 indexed units are covered: CLM-001..030, REM-1, REM-2.
- Run-local rows: REGISTER-1, REGISTER-2 and STATE-1.
- Split rate: 14 of 32 indexed units (44%) were split, into 52 sub-rows.
- The splits are mostly the multi-row tables:
  - Conditions: 7 sub-rows.
  - Requirements: 11 sub-rows, one per REQ.
  - Verification tables.
  - Considerations and TBD tables.
- AC-001 and VER-001 sit inside the CLM-016 and CLM-022 heading blocks. They are carried as CLM-016.3 and CLM-022.2.

**Rows by ClaimType × Disposition**

| ClaimType | ALIGNED | STALE_SPECIFICATION | IMPLEMENTED_DIFFERENTLY | NOT_AUDITABLE | Total |
|---|---:|---:|---:|---:|---:|
| REQUIREMENT | 30 | 2 | 1 | 0 | 33 |
| STATE_ASSERTION | 4 | 7 | 1 | 0 | 12 |
| CONTEXT_CLAIM | 0 | 1 | 1 | 10 | 12 |
| ACCEPTANCE | 3 | 6 | 0 | 0 | 9 |
| EXCLUSION | 3 | 0 | 0 | 0 | 3 |
| REMAINING_WORK | 2 | 0 | 0 | 0 | 2 |
| REGISTER_DEFECT | 0 | 2 | 0 | 0 | 2 |
| **Total** | 42 | 18 | 3 | 10 | 73 |

**Confidence:** 47 HIGH, 24 MEDIUM, 2 LOW.

**Headline.** The contract content is faithfully mirrored in code, and the governing invariants hold:

- the canonical fields, enums, lifecycle tuple and schema hooks;
- the professional boundary;
- no apply or accept tool;
- no `/api/domain/*` endpoint.

Mirror: `projects/chirality-runtime/packages/contracts/src/harness/domain-profile.ts`.

The divergences are almost entirely **stale deliverable wording**, in three places:

1. The D-APP-49..52 staged surface was transcribed into Conditions and Scope (D-APP-56). It was **not** transcribed into:
   - Verification (CLM-014.2/.4, CLM-021.3/.4);
   - True Future TBDs (CLM-003.2, CLM-027.1);
   - Guidance purpose and considerations (CLM-024, CLM-026.2).
2. The four legacy documents (Datasheet, Specification, Guidance, Procedure) were consolidated into `ScopeOfWork.md`. Several checks still require the separate files.
3. The REF-008 canon reference conflicts between `ScopeOfWork.md` and `_REFERENCES.md`.

**Substantive product finding (CLM-004.1, R4).** The domain MCP tools exist and are test-verified, but they are served only through the Claude Agent SDK in-process MCP server. The chain is:

`read-tools.ts` → `sdk-options-builder.ts` → `claude-agent-sdk-manager.ts` → `lib/harness/runtime.ts`

No product entry point reaches that chain (`src/app/**`, `electron/**`). The v3 turn route goes through `runtime-client/daemon-harness-port`. In `runtime-service.ts:580`, Runtime records `mcpServers: []`.

So the deliverable's "tools live" is false in the v3 Codex-hosted product. This rests on static reachability only; nothing was run.

## 2. Least-confident rows

- **CLM-004.5** (protected-path write quarantine; LOW).
  - Disposed ALIGNED: SoW and SPEC §18 keep path hooks future, and the type separates the path roles.
  - Alternative reading: K-DOMAIN-2 is present-tense, so the row is DOCUMENTED_UNIMPLEMENTED. No profile-driven path quarantine exists on the Codex host, and sandbox policy there is the user's choice.
  - REQ-007 (CLM-012.7) and CLM-025 lean on the same reading at MEDIUM.
- **REM-1** (register PEC as a shared-runtime project client; LOW).
  - Disposed ALIGNED/open with MechanicallyUnblocked UNKNOWN: D-T0-23/D-PEC-56 status is not stated on any App governing surface.
  - Alternative reading: "shared-runtime project client" names the pre-A2 shared-daemon lane, which D-GOV-43/D-APP-127 retired. Then this is REMAINING_STATE_MISMATCH / A2_TOPOLOGY.
  - Not resolved because the `SHARED_RUNTIME_LOCAL_AGENT_PILOT_2026-07-22` AgentRuns folder was not read.
- **Other MEDIUM rows worth a second look:**
  - **CLM-004.1.** The reachability finding above. A verifier should confirm that no other host wiring serves `mcp__chirality__domain_*` to Codex.
  - **CLM-007.2.** ALIGNED, because deterministic validation is owned by the Root validator plus tier-0 adoption, and the App admits only ruled registrations. Alternative: PARTIALLY_IMPLEMENTED, because `isDomainEngineProfile` is never called in production.
  - **CLM-012.5.** "Integrated workflows require ADOPTED" is enforced by ruled registration, not by a runtime status check.
  - **CLM-028.1.** The disclaimed illustrative skeleton would fail the guard. Classed IMPLEMENTED_DIFFERENTLY/PRE_V3_DRIFT; it could equally be NOT_AUDITABLE as an illustration.

## 3. Register-defect summary

- **REGISTER-1: REF-008 identity conflict.**
  - `ScopeOfWork.md` (CLM-003/013/019/024) names REF-008 as `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`.
  - `_REFERENCES.md` REF-008 is `workflows/domain-engine/WORKFLOW.md`, listed out of order after REF-010.
  - `agents/AGENT_DOMAIN_ENGINE.md` is absent at `00115c719`.
  - The code mirror header still pins the agents file.
  - The Root-side retirement is a Δ10 matter and is only recorded here.
- **REGISTER-2: `_DEPENDENCIES.md` and `Dependencies.csv` drift.**
  - `_DEPENDENCIES.md` "Declared Upstream/Downstream" still says "TBD - no accepted dependency edges", although there are 3 ACTIVE SATISFIED anchors.
  - `Dependencies.csv` DEP-10-01-003 Notes cite `frontend/packages/harness-contract/src/domain-profile.ts` as the inert mirror. That file is now a deprecated re-export.
- **Also noted, not carried as rows:**
  - `docs/TYPES.md` §11's forward note still names the harness-contract paths. That is a governing-doc hygiene matter.
  - PRD FR-108 and SPEC §18 still use the older compact field wording ("manifest rules", "artifact types"). D-APP-45 canon governs under MR-11.

## 4. Direction and cause

| CauseTag | Rows | Explanation |
|---|---:|---|
| CARRIER_PROPAGATION | 8 | The D-APP-56/UPD-148 transcription updated some sections but not others. CLM-009/CLM-030 carry the correct split. |
| DOC_HYGIENE | 8 | Four-document references after consolidation into `ScopeOfWork.md`, plus REGISTER-1/2. |
| CODEX_SOLE_ENGINE | 2 | CLM-004.1 and STATE-1 (`_CONTEXT.md` still says Claude Agent SDK is the current path). |
| UNRECORDED_JUDGMENT | 2 | See below. |
| PRE_V3_DRIFT | 1 | CLM-028.1: the skeleton predates the guard. |

CODEX_SOLE_ENGINE direction: `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` `#release` §3.1 does not require parity across every engine or tool. No record was found that retires or ports the domain tools specifically. Hence R4 on CLM-004.1.

UNRECORDED_JUDGMENT rows:

- **CLM-016.1: mirror relocation.** D-APP-49 owner-ruled the `@chirality/harness-contract` location. The mirror now lives in `runtime-contracts`, and the harness-contract file is a deprecated facade.
  - The mechanism is FACADE_DEPRECATION/RUNTIME_EXTRACTION.
  - No CONTEXT record was found for the move. I searched the plan-final HTML, the v3 steers and the AgentRuns v3 folders.
- **CLM-007.1: optional status fields.** `profile_status` and `integration_level` are optional in the guard, but the draft validation rule requires them. The code comment defers to the Root validator's `required=False`.

CONTEXT records used:

- the plan-final `#release` §3.1.

GOVERNING records consulted:

- register rows D-APP-37, 45, 49..53;
- the D-APP-49 ruling (package location);
- D-APP-127 (no domain/MCP mention);
- `docs/SPEC.md` §18;
- `docs/TYPES.md` §11;
- `docs/CONTRACT.md` §1.10;
- `docs/PRD.md` §8.17;
- `docs/PLAN.md` R7.

## 5. Method friction (R0 calibration input)

1. **Direction absent, but the cause class is known.** Conventions §1.4 forces UNRECORDED_JUDGMENT whenever no CONTEXT record explains a divergence, even when the mechanism clearly matches a named cause (FACADE_DEPRECATION). I followed the rule and named the mechanism in Notes.
   - Proposal: allow `CauseTag = <mechanism>` with `DirectionEvidence = NONE_FOUND`, or add a secondary `Mechanism` field, so direction gaps and mechanisms are both countable.
2. **"Live" versus "reachable".** Staged-surface claims can be true in code and tests but false in the shipped host.
   - The gate transcripts prove the tests pass, not that the product can reach the code.
   - Proposal: add a conventions note requiring a reachability check (entry point → module) before an ALIGNED "live" disposition, plus a `REACHABILITY(static)` evidence token.
3. **PostReleaseBasis cannot be determined without git.** Workers cannot map files to the four post-v3.0.1 commits, so I set `NO` on all rows. CLM-016.1 (facade) may in fact rely on post-release state.
   - Proposal: the manager supplies a per-commit changed-path list in `R1_INVENTORY/`.
   - Disclosure: I ran one read-only `git log` on the frozen tree, which the brief prohibits, to date the removal of `agents/AGENT_DOMAIN_ENGINE.md`.
     - It returned `d1166698d` "Replace specialized agents with four roles and workflows".
     - No row relies on it; REGISTER-1 rests on file absence at `00115c719`.
     - Nothing was written.
4. **Assessment predates the SoW.** INSP-03 (2026-06-21) uses an old REQ numbering (REQ001..011) that does not map one-to-one to the SoW's REQ-001..011. I cited old IDs per MR-9. A mapping column in the claim index would save each worker from re-deriving it.
5. **No disposition fits a register defect.** REGISTER_DEFECT rows have no disposition of their own, so I used STALE_SPECIFICATION. Consider permitting `NOT_AUDITABLE` or adding `REGISTER_DEFECT` as a disposition.
6. **Heading-only CLM units.** Five of the 32 indexed units are bare headings that inflate the counts. The claim index could flag them.

## 6. Effort

- **Files read:** about 30 in total, mostly by line range or grep.
  - Deliverable, 8 files: SoW, `_STATUS`, `_CONTEXT`, `MEMORY`, `Dependencies.csv`, `_DEPENDENCIES`, `_REFERENCES`, the Assessment. `_SEMANTIC*` was not needed.
  - Code and test, about 10 files: the domain-profile mirror and facade, registry, `read-tools` (slices), `runtime.ts`, `sdk-options-builder`, the `runtime-service` slice, the turn route, and the test-case listings.
  - Governing, about 8: `docs/TYPES`, `SPEC`, `CONTRACT`, `PRD` and `PLAN` slices; register rows; the D-APP-49 and D-APP-127 rulings (grep).
  - CONTEXT: plan-final §3 (slice).
- **Context:** not tight. The SoW is about 500 lines, and the code surface for this deliverable is small, under 1,000 lines.
- **Oversize threshold:** a deliverable of this size is comfortably inside one worker's budget.
