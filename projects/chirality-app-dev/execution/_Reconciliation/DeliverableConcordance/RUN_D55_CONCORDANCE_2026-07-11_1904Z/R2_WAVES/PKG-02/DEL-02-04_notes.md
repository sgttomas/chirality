# R2 Wave-1 Concordance Notes — DEL-02-04 Toolkit Options and Local UI State

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z` (D-APP-55, Option A whole corpus)
- **Deliverable:** DEL-02-04, PKG-02 Desktop Shell, Navigation, and Operator State
- **Source state:** `frontend/` at `fac46e33f` (byte-identical through HEAD `052b3c2b2`; verified by orchestrator), gate binding `GATE-TRANSCRIPT(W1@fac46e33f)`
- **Method:** pinned plan §§5–8 @ `551f84ef6`; R2 Method Addendum MR-1..MR-11; run-local AUTHORITY_MAP
- **Phase:** R2 Wave-1 discovery (read-only)

> Epistemic status: evidence artifact, not authority. Dispositions are agent classifications for human review; no lifecycle action or ruling is made here.

## 1. Census

22 claim rows.

By ClaimType:

| ClaimType | Count |
|---|---:|
| REQUIREMENT | 14 |
| EXCLUSION | 4 |
| REGISTER_DEFECT | 2 |
| ACCEPTANCE | 1 |
| REMAINING_WORK | 1 |

By Disposition:

| Disposition | Count | Rows |
|---|---:|---|
| ALIGNED | 14 | REQ-004/005/006/007/008/010/011/012/013, ACC-001, EXC-001/002/003, REMAINING-1 |
| PARTIALLY_IMPLEMENTED | 3 | REQ-003 (no mode/persona Toolkit control), REQ-009 (mode enforcement exists but not surfaced as a Toolkit control), REQ-014 (dense UI in code, no recorded polish/render evidence) |
| STALE_SPECIFICATION | 2 | REQ-001 (three-resizable-pane wording after Toolkit folded into the sidebar tab), EXC-004 (dependency-extraction deferral wording vs live 14-row register) |
| STALE_VERIFICATION | 1 | REQ-002 (keyboard Home/End/Arrow + focusable-separator behavior implemented but untested) |
| REMAINING_STATE_MISMATCH | 2 | REGISTER-1, REGISTER-2 (REF-006 hash-mismatch/PENDING lag) |

Derived summary (not a deliverable verdict): the local-storage / draft / preset / option-fallback behavioral core is current and well-tested (9 behavioral ALIGNED requirement rows). The discordant surfaces are (a) two stale kit statements overtaken by later work — the three-pane Toolkit wording (loop-first pivot D-APP-28) and the dependency-extraction deferral (register now exists); (b) the Toolkit's missing mode/persona controls, a persisting requirement-vs-implementation gap (REQ-003/009) that is a product decision, not a doc repair; (c) two verification gaps (REQ-002 keyboard/separator untested; REQ-014 polish evidence unrecorded); and (d) dependency-register lag on the reconciled REF-006 PRD hash.

Assessment recency: INSP-03 (2026-06-20, SHA 50b063f3e) was largely accurate at its own source state. Two of its conclusions are OVERTAKEN at fac46e33f — REQ-012 (its "unknown-key warning not visible in tests" PARTIAL is now covered by harness-options.test.ts:241-264) and REQ-014 (its "UI_POLISH_EXECUTION_PLAN.md absent" TBD basis, since the plan is now present). The rest STILL CURRENT. No `STALE_ASSESSMENT` disposition was raised: per MR-1 the operative defects live on kit/verification surfaces, not on the assessment being presented as current truth.

Dependency re-verification (plan §5): all 14 `Dependencies.csv` rows re-read live. 6 ANCHOR + 8 EXECUTION, 0 RETIRED. DEP-02-04-014 is a legitimately-open TBD (adjacent runtime option / permission-policy contracts) — consistent with REQ-009's forward-looking condition, not a defect. DEP-02-04-012 (REF-006) is the lagging row (REGISTER-1/2). DEL-02-04 was not in the D53A ten-deliverable reconciliation scope, so its ANCHOR rows still carry `SatisfactionStatus=NOT_APPLICABLE` by construction.

Lifecycle note: `_STATUS.md` header still carries the D-APP-19 Checking Approval SHA above an `IN_PROGRESS` state. Under D-APP-54 and AUTHORITY_MAP precedence note 2 these are preserved historical evidence; no `LIFECYCLE_REASSESSMENT_REQUIRED` row raised (corpus-wide header shape is an R3 concern).

## 2. Least-confident rows (mandatory self-flagging)

Flagged for fan-in recheck (plus all non-ALIGNED rows by rule):

- **REQ-002 (STALE_VERIFICATION).** Alternative reading that flips it: **ALIGNED.** The width/persistence/clamp math IS tested (layout-state.test.ts) and the drag delta helper is tested; a reader could treat the keyboard handlers + `role="separator"` markup as low-risk glue not requiring its own test, especially since the requirement is partly satisfied (drag + persist verified). I marked STALE_VERIFICATION because the requirement distinctively promises keyboard (Home/End/Arrow) and focusable-separator behavior, the spec Verification approach (Specification.md:56) names those checks, and the assessment's cited layout-state.test.ts asserts none of them — matching the R0 calibration precedent (DEL-02-01 REQ-003 was STALE_VERIFICATION for an analogous untested UI interaction).
- **REQ-009 (PARTIALLY_IMPLEMENTED).** Alternative reading that flips it: **ALIGNED** (as INSP-03 rated it PASS). The mode→permission-posture enforcement genuinely exists and is tested (sdk-options-builder.test.ts:259-307); if "Toolkit mode controls" is read loosely as "the mode option the UI participates in," the mapping is complete. I marked PARTIALLY_IMPLEMENTED on the literal reading: the Toolkit renders no mode control (operator-toolkit-panel.tsx:64-143), so the specific "Toolkit mode control → policy mode" wiring the requirement names does not exist; the enforcement is driven by session/runtime mode. This is the same product gap as REQ-003 and routes to one consolidated packet.
- **REQ-003 (PARTIALLY_IMPLEMENTED).** Alternative reading that flips it: **ALIGNED** under the spec's "as supported by runtime" qualifier — if mode/persona are deemed not runtime-supported *as Toolkit fields*, exposing only model/tools/maxTurns/governance would fully satisfy the requirement. I kept PARTIALLY_IMPLEMENTED because the requirement text explicitly enumerates mode and persona and they are runtime options exposed elsewhere (persona-picker; session mode), so their absence from the Toolkit is a real coverage gap, matching INSP-03's PARTIAL and Gap.
- **REQ-014 (PARTIALLY_IMPLEMENTED).** Alternative reading that flips it: **DOCUMENTED_UNIMPLEMENTED** (no binding verification at all) or **UNKNOWN**. I chose PARTIALLY_IMPLEMENTED because the dense professional UI is implemented in code; only the acceptance/render/browser evidence is missing (unproven by the spec's own line 62), so the residual is "record evidence," not "build UI."
- **ACC-001 (ALIGNED).** Alternative reading that flips it: **omit the row.** The professional-reliance-boundary Datasheet condition largely restates the non-authority requirements (REQ-005/013). I emitted it under MR-4 as a datasheet-distinct condition (reliance/decision-support posture, DIRECTIVE 2.3/2.4 + KG-015 is broader than "presets don't override governance") and let it cite the covering REQ rows' evidence; a stricter reader could fold it entirely into REQ-005/013.

## 3. Register-defect summary

Two REGISTER_DEFECT rows, both `REMAINING_STATE_MISMATCH`, both the same underlying lag — the reconciled REF-006 (docs/PRD.md) hash is not reflected in the dependency registers:

- **REGISTER-1** — `Dependencies.csv` DEP-02-04-012 still carries `ProposedMaturity=AVAILABLE_HASH_MISMATCH` / `SatisfactionStatus=PENDING` with a HASH_MISMATCH warning note, while live `_REFERENCES.md` (line 12) shows REF-006 `MATCH` (Expected==Actual==`ac35fba4…`) and Datasheet.md line 40 declares it reconciled.
- **REGISTER-2** — `_DEPENDENCIES.md` still reports a `[WARNING] PRD_HASH_MISMATCH` (line 58), a PENDING satisfaction count of 1 (line 80), and a closure note "DEP-02-04-012 remains PENDING because REF-006 has a hash mismatch" (line 86-87) — contradicted by the same reconciled reference and by Guidance.md's own "Resolved source-state note" (lines 50-54).

Both repairs are R5 dependency-register work and only if separately authorized (dependency mappings are updated under separate authority per plan §5). Note the reconciliation was by accepted-hash refresh (the live Expected `ac35fba4…` differs from the old Expected `86cb6f…` cited by the assessment and the register note), consistent with the D-APP-35 pattern; the reference itself is legitimately MATCH.

## 4. Method notes / deviations

- **PRD line anchors.** `docs/PRD.md` was not read this wave (its content is not load-bearing for these classifications and the deliverable cites it by FR-ID/section). NormativeSource cites the exact `Specification.md` row line numbers (the authoritative claim text) plus the PRD FR-IDs/sections as the deliverable states them, rather than fabricating PRD line numbers. No deviation from the CSV contract.
- **No IMPLEMENTED_UNMAPPED rows.** The Toolkit/pane-state/draft surface is comprehensively mapped by REQ-001..014; the subagent-governance opts (contextSealed/pipelineRunApproved/approvalRef) fall under REQ-003's "governance metadata," and the Turn Payload Preview under REQ-013's non-authoritative-visibility requirement. The dead `toolkit` entry retained in `layout-state.ts` (TOOLKIT_PANE_VISIBLE=false, kept only to satisfy the frozen `Record<ResizablePaneKey,...>` type) is inert code, not live behavior, so no UNMAPPED row.
- **No DEFERRED_AGENT_WORKFLOW.** Nothing in this deliverable required judging an agent-instruction or workflow contract. The mode/persona-control question (REQ-003/009) is product UI + runtime option ownership, not an agent-workflow contract.
- **Verification binding.** Behavioral rows cite `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667 passed / 4 skipped) plus named test files/cases with line anchors; tests were never executed by this agent. Where a requirement's behavior is genuinely untested (REQ-002 keyboard/separator; REQ-014 polish), `NONE_BINDING` is stated with what is and is not asserted.
