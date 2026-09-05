# Impact Assessment — SCA-APP-010

**Status:** `AWAITING_OWNER_ACCEPTANCE`
**Assessment basis:** `95b5687a7c9a4c6fe6e655f628495dec08ce04d8`
**Gate-1 confirmation:** `Decision_Log.md` G1-CONFIRM, 2026-09-04
**Effect today:** none outside this snapshot folder. No decomposition, companion, contract, pointer, deliverable, Root, product, or release surface changes by this assessment.

## Summary

SCA-APP-010 changes what the App shell is: the centre dialogue becomes the
invariant primary, the left panel becomes the chat navigator, the right
panel becomes a one-view-at-a-time tertiary surface, and a prompted
specification ladder (plain chat, specified chat, governed workflow) becomes
the operator-workflow model. In decomposition terms it adds four scope items
and modifies one objective, seven scope items, one package row, thirteen
deliverable rows, the Vocabulary Map, the Open Issues, and the companion
register. It adds, removes, reclassifies, merges, or splits no package or
deliverable, so there is no parent-lineage or orphan risk. Its structural
weight is on carrier breadth: thirteen existing deliverables gain duties, and
three of those duties depend on Root-owned semantics that the App can only
present and consume.

## Evidence basis

| Evidence | Reproducible fact |
| --- | --- |
| `plans/shell-redesign_2026-09-04/02_CURRENT_STATE.md` §2, §11 (SHA-256 in `Brief.md`) | `dialogue-viewport.tsx` hides the primary dialogue for replay and focused surfaces; the navigator lists sessions by `dialogue`/`workbench`/`pipeline` mode group; the Work projection always receives an empty array. Twelve code/design contradictions listed. |
| Decomposition line 296 (`DEL-02-02`) | Row text still says "Re-host Workbench and Pipeline around central dialogue" and names "Workbench/Pipeline views" as anticipated artifacts. |
| Decomposition line 168 (`SOW-006`) and line 397 | Coordination Panel and Codex role entry are the current accepted presentation. |
| `execution/_Coordination/_DECISIONS/D-APP-74_RULING_2026-07-23.md:107` | "Old-UI retirement requires separate owner acceptance after parity, accessibility, compatibility, and packaged Desktop evidence." |
| `DEL-02-02/_STATUS.md` `## Remaining` | Two open v3 items (V3-01, V3-02) present managed/native descendant records on the Work/Agents surface; both are `NOT_SELECTABLE_UNTIL` Root/DEL-08-05 gates. |
| `DEL-02-05/_STATUS.md` `## Remaining` | DEL-02-05-V3-03 is gated on the Root DEL-02-09 account/consent contract; the fake `HostedEngineConsentPort` remains underneath. |
| `DEL-05-02/_STATUS.md` `## Remaining` | DEL-05-02-V3-01 consumes closed `HarnessEvent` schema v2 only after Root DEL-02-10 acceptance is routed to App. |
| `DEL-08-04/_STATUS.md` `## Remaining` | DEL-08-04-V3-01 is the class-aware delegation bridge, gated on Root WP-03/WP-05 fixtures; `managed-delegation.ts` carries `MANAGED_DELEGATION_POLICY_VERSION` but no per-session policy field. |
| `frontend/src/lib/harness/mcp/` | Fifteen `mcp__chirality__*` tools exist across `read-tools.ts`, `coordination-tools.ts`, and `domain-proposal-tools.ts`; no `propose` tool. |
| `frontend/src/**` grep | No `.chirality/workflows` handling and no per-session delegation-policy field exist today. |
| `docs/CONTRACT.md` K-ROOT-1, K-PATH-2, K-MCP-1, K-KEY-1, K-CONSENT-1, K-ROLE-2, K-EVENT-3 | Invariant text unchanged by this amendment; K-EVENT-3 declares the closed `HarnessEvent` schema v2, Root-owned. |
| Companion register rows K-ROOT-1, K-PATH-2, K-MCP-1 | Current App deliverable mappings: K-ROOT-1 → DEL-07-01, DEL-08-01, DEL-09-04; K-PATH-2 → DEL-06-04, DEL-07-01, DEL-07-05, DEL-09-03; K-MCP-1 → DEL-06-02, DEL-06-03, DEL-09-02. |
| Decomposition §10 | Telemetry: 80 scope items, 10 packages, 52 deliverables, 10 objectives, S=9 M=41 L=2 XL=0. |
| `Evidence/Gate1/PRE_CHANGE_AUDIT/` | Baseline `WARNINGS`, zero blockers; forward 52/52, reverse 52/54; companion 83/50; corpus v20 no drift. |

## Impact by action

| Action | Decomposition structure | Variant-local metadata (write scope at Gate 5) | Downstream consumers | Invariant / telemetry risk and control |
| --- | --- | --- | --- | --- |
| A001 `MODIFY OBJ-001` | Objective description; `CoveredScopeItems` extended to `SOW-001–SOW-008, SOW-023, SOW-081–SOW-082`. | none | AUDIT_DECOMP objective mapping | Objective may over-claim the ladder as done. Control: description names the model, not completion. |
| A002 `MODIFY SOW-001` | SSOW and Scope Ledger rows; notes name reachable-but-unmounted routes. | DEL-02-01 `ScopeOfWork.md` and `_CONTEXT.md` restatement | WORKING_ITEMS, AUDIT_DECOMP | Compatibility surfaces silently dropped. Control: routes stay reachable pending Q3; D-APP-74 supersession row (A015). |
| A003 `MODIFY SOW-002` | "global" → per-chat folder with known-folder set. | DEL-07-01 and DEL-02-03 context notes | dependency extraction (DEL-02-03 → DEL-07-01 unchanged) | Validation ownership drift. Control: DEL-07-01 stays owner; DEL-02-03 stays UI touchpoint. |
| A004 `MODIFY SOW-004` | Layout vocabulary; artifact-focus removed from the list. | DEL-02-04 `ScopeOfWork.md` | WORKING_ITEMS | Schema-string bump temptation. Control: additive fields only under `chirality.woven-workspace/v1`. |
| A005 `MODIFY SOW-006` | Coordination Panel → Who is working / Session views; Work projection unmounted; role entry relocated. `DEC-024` mapping kept. | DEL-02-02, DEL-05-04, DEL-08-02 context notes | DEL-02-02-V3-01/V3-02 (their presentation target moves from "Work/Agents" to "Who is working"); RECONCILIATION | Two open Remaining items name a surface that will not exist. Control: Gate 4 rewrites their target surface wording only; gates and dependencies untouched. |
| A006 `MODIFY SOW-007` (deferred type) | Notes: controls unmounted; DEL-08-03 semantics retained. | DEL-08-03 and DEL-02-02 context notes | AUDIT_DECOMP | Dormant presentation clause. Owner chooses at Gate 2: keep dormant (parsed) or retire the presentation half. |
| A007 `MODIFY SOW-008` | Add rung, declined triggers, annotations, known folders. | DEL-02-04 `ScopeOfWork.md` | WORKING_ITEMS | Local state mistaken for truth. Control: existing "never authoritative" clause retained and extended to rung state. |
| A008 `MODIFY SOW-010` | Boot binding carries delegation policy. | DEL-03-02 `ScopeOfWork.md` | DEL-03-02, dependency extraction | Daemon session record is Root-owned. Control: App binds the request; the stored field is Root DEL-02-11's (OI-008). |
| A009 `ADD SOW-081` | New SSOW and Scope Ledger rows; `PKG-07`; `DEL-07-03, DEL-02-02, DEL-04-04`; `OBJ-001, OBJ-006, OBJ-007`; `DEC-025`; `IsOpenIssue=TRUE` (OI-008 for Q15/Q16). | DEL-07-03, DEL-02-02, DEL-04-04 `ScopeOfWork.md`; new Remaining items | PREPARATION not needed (no new folder); dependency extraction for the three carriers; WORKING_ITEMS | Workflow file could become a second status store. Control: "steers, never records" is row text; K-PATH-2 governs the write. |
| A010 `ADD SOW-082` | New rows; `PKG-06`; `DEL-06-03, DEL-05-02, DEL-02-02, DEL-08-01`; `OBJ-001, OBJ-005, OBJ-007`; `IsOpenIssue=TRUE` (OI-008 for the event types). | four carriers' `ScopeOfWork.md`; new Remaining items | dependency extraction; DEL-06-02 collision check; Root notice | `proposal.*` types extend the closed Root schema v2 (K-EVENT-3). Control: App consumes; the additive types are proposed to Root DEL-02-10 by notice; DEL-05-02 stays gated until routed. |
| A011 `ADD SOW-083` | New rows; `PKG-08`; `DEL-08-04, DEL-03-02`; `OBJ-005, OBJ-007`. | DEL-08-04, DEL-03-02 `ScopeOfWork.md` | dependency extraction; DEL-08-04-V3-01 (policy becomes an input to the class-aware bridge) | Capability expansion beyond SCA-APP-008. Control: policy only narrows (`none` default); no new delegation class. |
| A012 `ADD SOW-084` (deferred type) | New rows; `PKG-07`; `DEL-07-01, DEL-08-01, DEL-04-04`; `OBJ-006, OBJ-007`; `IsOpenIssue=TRUE` (Q14). | three carriers' `ScopeOfWork.md` | dependency extraction; DEL-09-04 packaging integrity (instruction-root hash set) | Second instruction root outside protection. Control: same K-ROOT-1 protections, hash-pinned; Q14 ruling fixes the final shape. |
| A013 `MODIFY PKG-02` | Package description. | none | AUDIT_DECOMP | none |
| A014 `MODIFY DEL-02-01` | Description, AnticipatedArtifacts. | `_CONTEXT.md`, `ScopeOfWork.md` | WORKING_ITEMS | Envelope M holds; presentation only. |
| A015 `MODIFY DEL-02-02` | Name, Description, AnticipatedArtifacts (Workbench/Pipeline views removed; Workflows view, forms, proposal card added). | `_CONTEXT.md`, `ScopeOfWork.md`; V3-01/V3-02 surface wording | WORKING_ITEMS; Task Management label refresh | Name change flags label implications (folder name stays `DEL-02-02_Workbench_and_Pipeline_Selection_UX`, as SCA-APP-004 left it). Envelope M: the Workflows view, forms, and card add breadth; Gate 3 records the envelope as M with a split trigger if implementation review finds cross-domain churn. `Supersession_Delta.csv` row against D-APP-74:107. |
| A016 `MODIFY DEL-02-04` | Description, AnticipatedArtifacts. | `_CONTEXT.md`, `ScopeOfWork.md` | WORKING_ITEMS | Envelope S holds: additive fields and one strip. |
| A017 `MODIFY DEL-02-05` | Description (app-wide account presentation; per-folder consent; Settings host). | `_CONTEXT.md`, `ScopeOfWork.md`; V3-03 wording unchanged | WORKING_ITEMS; Root notice | UI could imply a shared login the port does not have. Control: row text says presentation only, port semantics per-root until Root DEL-02-09 lands; envelope S holds. |
| A018 `MODIFY DEL-03-02` | Description note. | `ScopeOfWork.md` | dependency extraction | none beyond A008. |
| A019 `MODIFY DEL-04-04` | Description: roadmap seam; layered root. | `ScopeOfWork.md` | dependency extraction | Prompt injection of untrusted file content. Control: delimited block; file under K-PATH-2 containment; templates from declared skills only. |
| A020 `MODIFY DEL-05-02` | Description note. | `ScopeOfWork.md` | Root notice | Gated on schema acceptance (OI-008). |
| A021 `MODIFY DEL-06-03` | Description, AnticipatedArtifacts (`propose`). | `ScopeOfWork.md` | DEL-06-02 catalog; Section 9 validation | K-MCP-1 applies unchanged; PreToolUse may double-check once-per-chat. |
| A022 `MODIFY DEL-07-01` (deferred) | Description. | `ScopeOfWork.md` | packaging integrity | follows A012. |
| A023 `MODIFY DEL-07-03` | Description, AnticipatedArtifacts (workflow file contract). | `ScopeOfWork.md` | WORKING_ITEMS | Contract must forbid status/approval/evidence fields; Gate 3 text. |
| A024 `MODIFY DEL-08-01` | Description (proposal clauses, templates, organisation-layer checks). | `ScopeOfWork.md` | Root instruction surfaces `agents/`, `skills/` (owner-granted Root write scope this session); G4 tranche manifest; routed agent-index notices | Instruction change without notice. Control: AGENTS.md change-notice rule and G4 manifest at implementation. |
| A025 `MODIFY DEL-08-04` | Description. | `ScopeOfWork.md` | DEL-08-04-V3-01 | none beyond A011. |
| A026 `MODIFY` Vocabulary Map | Nine synonym additions; canonical terms unchanged. | none | RECONCILIATION terminology check | Surface words leaking into doctrine. Control: added as synonyms only. |
| A027 `MODIFY` companion register | Rebind 83 rows to the post-image SHA; add DEL-07-03 to K-PATH-2 (workflow write) and keep K-ROOT-1 mapping (DEL-07-01 already present). No new invariant IDs. | none | invariant census; RECONCILIATION | Row-count drift. Control: exactly 83 rows / 50 families after; Gate 3 shows the diff. |
| A028 `ADD DEC-025` + Change Log | Decision Log rows. | none | AUDIT_DECOMP | none |
| A029 `MODIFY` Open Issues (`OI-008`) | New row `SHELL_LADDER_BOUNDARY`, affected `SOW-081–SOW-084`, `SOW-010`; telemetry counts updated. | none | AUDIT_DECOMP | none |

## Derivative-surface classification

| Surface | Classification | Authority basis |
| --- | --- | --- |
| Active SOFTWARE_DECOMP document | `DIRECT_EDIT` at Gate 5 only | SCOPE_CHANGE Gate-3 approved text |
| `contract_invariant_coverage_register.csv` | `RECOMPUTE` at Gate 5 (rebind + two mapping rows) | DEC-022 companion rule |
| App `docs/CONTRACT.md` | `NO_CHANGE` | No invariant text changes; K-ROOT-1 reading recorded in Gate-3 notes |
| Affected deliverables' `_CONTEXT.md` / `ScopeOfWork.md` | `DIRECT_EDIT` under the Gate-4 propagation plan | Gate-4 approved plan; sealed briefs |
| Affected deliverables' `_STATUS.md` `## Remaining` | `DIRECT_EDIT`: the owner seats the new items (the SCA carries proposals; seating is the owner's act) | K-AUTH-1; D-APP-60 |
| `Dependencies.csv` for the thirteen carriers | `RECOMPUTE` after application (dependency extraction) | registered extraction workflow |
| Authority corpus snapshot | `RECOMPUTE` (new corpus version after decomposition post-image) | `reconcile_authority_corpus.py` |
| `Supersession_Map.csv` | `RECOMPUTE` from SCA-APP-009's map plus this delta | `accumulate_supersession_map.py` |
| Task Management register | `NO_CHANGE` here; label refresh for DEL-02-02 is a TASK_MANAGEMENT act | D-GOV-32 |
| Root instruction surfaces (`agents/`, `skills/`) | `NO_CHANGE` by the amendment; `DIRECT_EDIT` only in the implementation tranche for A024 with G4 manifest | Owner Root write-scope grant G1-CONFIRM |
| Root loop coordination surface (`execution/_Coordination/`) | `DIRECT_EDIT` of one routed notice after Gate 5 | AGENTS.md notice rule; precedent `NOTICE_2026-08-24_APP_SCA-APP-008_GATE5_APPLIED_STATE.md` |
| `_ScopeChange/_LATEST.md` | `NO_CHANGE` until SCA-APP-009 derivative closure is dispositioned | sequencing rule |

## Derivative-package status

| Package | Owner | State after this assessment | Required action after Gate-5 application |
| --- | --- | --- | --- |
| Active decomposition | SCOPE_CHANGE | `CURRENT_UNCHANGED` | Apply exact Gate-3 text; post-change AUDIT_DECOMP |
| Companion register | SCOPE_CHANGE | `CURRENT_UNCHANGED` | Rebind and add two mapping rows; census 83/50 |
| Deliverable SOW/context set (13 carriers) | WORKING_ITEMS / owning carrier | `CURRENT_UNCHANGED` | Amend per Gate-4 plan under sealed briefs |
| Dependency registers and closure audit | dependency extraction / AUDIT_DEP_CLOSURE | `CURRENT_UNCHANGED` | Re-extract the 13 carriers; fresh named closure audit; the nine-node SCC stays a separate transaction |
| Authority corpus | RECONCILIATION | v20 current | Regenerate after post-image |
| Supersession map | SCOPE_CHANGE | SCA-APP-009 map current | Accumulate this delta (D-APP-74:107 prospective supersession; SOW-001/006/007 presentation facts) |
| Root coordination | Root loop | none | Route one App notice: shared login home, additive `proposal.*` types, session-record delegation field |
| SCA-APP-009 closure | SCOPE_CHANGE / WORKING_ITEMS | `OPEN_PENDING_DERIVATIVE_CLOSURE` | Unchanged by SCA-APP-010; pointer stays until dispositioned |

## Orphan and structural risk

- Package additions: `0`. Deliverable additions: `0`. Removals, reclassifications, merges, splits: `0`. Parent changes: `0`. Stable ID reuse: `0`.
- Scope items: `80 → 84`, all `IN`, each with one owner package and mapped deliverables. `UnassignedScopeItems` and `ScopeItemsWithoutDeliverableMapping` stay `0`.
- Context envelopes: unchanged (S=9, M=41, L=2, XL=0). DEL-02-02 is the only carrier whose breadth grows materially; it stays `M` with a recorded split trigger.
- Open issues: `7 → 8`; `OpenIssueAffectedScopeCounts` gains `SHELL_LADDER_BOUNDARY=5`.
- Dependency graph: four new scope items imply new edges among DEL-02-02, DEL-07-03, DEL-04-04, DEL-06-03, DEL-05-02, DEL-08-01, DEL-08-04, DEL-03-02, DEL-07-01. None of these is in the live nine-node SCC (DEL-02-05 is; its new duty is presentation and adds no edge). Extraction after application decides exact edges; no register is edited by this SCA.

## Estimate and schedule staleness

No estimates or schedule live in the decomposition. Deliverable-level effort implied by the redesign tranches T1 to T7 is carried in the intake package and the owner-seated Remaining items, not here. DEL-02-02's name change requires a Task Management label refresh only.

## Active snapshot and handoff-state impact

- `_LATEST.md` continues to point at SCA-APP-009. SCA-APP-010 may proceed through Gates 3 and 4 and may apply at Gate 5 on a candidate branch, but the pointer moves only after the owner dispositions SCA-APP-009's derivative closure or rules that SCA-APP-010 supersedes it as the active snapshot.
- This snapshot now carries `Brief.md`, `PARSED_ACTIONS.csv`, `Impact_Assessment.md`, `Decision_Log.md`, `Handoff_State.md`, and the pre-change audit; the remaining required top-level artifacts (`Propagation_Plan.md`, `Amendment_Actions.csv`, `Pre_Change_Coverage.json`, `Post_Change_Coverage.json`, `Supersession_Delta.csv`, `Supersession_Map.csv`, `RUN_SUMMARY.md`) are produced at their gates so the SCA-APP-008 layout defect is not repeated.

## Recommended downstream reruns (after Gate 5)

1. Post-change `AUDIT_DECOMP`, full scope.
2. Dependency extraction for the thirteen carriers, then named `AUDIT_DEP_CLOSURE — SCA-APP-010-GATE5-POST-APPLICATION`.
3. Authority corpus regeneration and status.
4. Supersession map accumulation with check mode.
5. Routed Root notice; routed agent-index notices when A024's instruction changes land.
6. Owner seating of the Remaining items the amendment makes proposable, in dependency order T1 → T2/T3 → T4/T5/T6 → T7.

## Gate-2 question

**Do you accept this impact assessment?**

Two choices are folded into acceptance unless you answer them separately:

- **A006 (SOW-007):** keep the Pipeline presentation clause dormant with DEL-08-03 semantics retained (as parsed), or retire the presentation half of SOW-007 now.
- **A012 (SOW-084):** accept the organisation-layer default from Q14 (bundled base plus a client-owned, hash-pinned layer under instruction-root protections) as the Gate-3 basis, or hold A012/A022 out of this amendment until Q14 is ruled separately.

Acceptance authorizes Gate 3 exact amendment preview only. No decomposition, companion, contract, pointer, deliverable, Root, or product write occurs before Gate 5.
