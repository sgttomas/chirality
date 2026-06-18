# Deliverable Issuance & Evidence Consolidation Program Plan

**Date:** 2026-06-18
**Status:** PROPOSAL / DRAFT — requires human acceptance ruling (`D-APP-19`) before it becomes an active development queue. It does **not** re-point `_COORDINATION.md` / `NEXT_INSTANCE_PROMPT.md` / `_LATEST.md`; those change only on acceptance.
**Product:** Chirality desktop harness and bundled agent operating system
**Working root:** `projects/chirality-app-dev/`
**Prepared by:** `WORKING_ITEMS` (RESEARCHER fan-out evidence, 2026-06-18)
**Relates to (does not supersede):** `plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md` (active, runtime/provider track, parked on `D-APP-18`)
**Roadmap anchor:** `docs/PLAN.md` §4 (R0–R7); `docs/SPEC.md` §4.2–4.3 lifecycle; `docs/CONTRACT.md` K-GATE-1 / K-AUTH-1 / K-AUTH-2

This plan addresses a gap no existing plan covers: the runtime roadmap (R0–R6) is built and
proven, the dependency DAG is closed, **but zero of the 53 deliverables have been advanced
through the human-gated `CHECKING → ISSUED` lifecycle.** It opens and executes the
deliverable-issuance phase — evidence consolidation, a small set of real code/scope fixes,
control-plane reconciliation, then per-deliverable human-gated issuance in dependency order.

It does **not** decide `D-APP-18` (default-provider cutover — a separate runtime track), does
**not** authorize R7 / domain-engine implementation, and crosses **no** `docs/PLAN.md` §11
fence. Issuance is **not** a §11 fence; it is the normal lifecycle gate that has simply never
been opened.

---

## 1. Purpose

Make the project's *formal deliverable state* catch up to its *engineering reality*. STAB-00..06,
the executable R5 subagent bridge, and R6-01..05 landed real, test-green runtime; the strict
dependency graph is acyclic. Yet every deliverable still reads `IN_PROGRESS`, so the project
cannot yet make any issued-deliverable reliance claim. This program carries the deliverables —
package by package, in dependency-wave order — to `ISSUED`, with the evidence and human
approvals the lifecycle requires.

The goal is **comprehensive coverage of all 11 packages / 53 deliverables**, not a slice.

## 2. Evidence Basis

Scoped from a 15-stream `RESEARCHER` fan-out (one per package + roadmap/decision/dependency
cross-cuts + a completeness critic) run 2026-06-18 against the **live tree** (the retrieval
index `domains/chirality-app-dev/_LocalIndexes/_LATEST.md` is `STALE` — `CONTENT_DRIFT`, 49/660
artifacts changed — so it was used for discovery only). Immutable evidence packets:
`domains/chirality-app-dev/_Research/RCH_20260618T04*_gap_pkg0[0-9]|pkg10|xc_*`.

Load-bearing facts independently re-verified by the orchestrator (`:RUN`):

- **53 deliverables, all `Current State: IN_PROGRESS`; 0 in `2_Checking`, 0 in `3_Issued`**
  (only placeholder `README`/`_Archive`). The issuance phase has never been opened.
- **Full suite green:** `npm run test` → 54 files / 383 tests; `harness:validate:section9` →
  13/13; Section 8 → 8/8; arm64 unsigned DMG builds with `instruction-root-integrity` pass.
- **DAG closed:** `tools/coordination/analyze_dep_closure.py execution` → 46 nodes, 97 edges,
  **SCC count 0**, 0 bidirectional pairs, 51/51 schema-valid. A valid 14-wave topological
  issuance order exists (5 deliverables are true graph orphans, issuable any time).
- **Evidence consolidation is the universal blocker:** only **2** `Evidence_*.md` files exist
  across all 53 deliverables (`DEL-03-01`, `DEL-04-01`), and **both are stale** (dated
  2026-05-24, predating current code).
- **Critic correction folded in:** the PKG-06 stream's claim that
  `section9.chirality_mcp_status_dependencies` and `section9.context_compaction_boundary` are
  "absent" is **REFUTED** — both exist (`frontend/scripts/validate-harness-section9.mjs:55,85`).
  Those are **not** gaps and are excluded below.

## 3. Current-State Map (per package)

Implementation reality is judged against each deliverable's `Specification.md` from the live
`frontend/src` + `__tests__`, not from `_STATUS.md` history.

| Pkg | Roadmap | Deliverable reality | Dominant gap to ISSUED |
|---|---|---|---|
| PKG-00 | DAG/control | 1 COMPLETE, 1 SUBSTANTIAL | Control-plane bookkeeping stale; reconcile + Evidence + gate |
| PKG-01 | R0 governance | 2 SUBSTANTIAL, 2 PARTIAL | Author `reliance_boundary_register.md`; checklists; Evidence; PRD-hash ruling |
| PKG-02 | Baseline UI | 1 COMPLETE, 4 SUBSTANTIAL | Evidence; UI render-test acceptance-bar ruling; TBD reconciliations |
| PKG-03 | R1 engine | 4 SUBSTANTIAL | Evidence (refresh stale); 2 spec↔impl reconciliations; interrupt-taxonomy ruling; 2 missing docs |
| PKG-04 | R0/R1 adapter | 2 COMPLETE, 3 SUBSTANTIAL | Evidence; refresh probe record; PRD-hash; adoption verdict (human) |
| PKG-05 | R1 audit | 1 COMPLETE, 3 SUBSTANTIAL, 2 PARTIAL | **Code:** session-folder/migration (05-01), transcript view (05-04); Evidence; tests |
| PKG-06 | R2/R3/R4 tools | 2 COMPLETE, 4 SUBSTANTIAL | Evidence; confirm 2 policy values; PRD-hash (no Section-9 gap) |
| PKG-07 | R3 filesystem | 4 COMPLETE, 2 PARTIAL | **Code:** PREPARATION-seeding (07-02), doc-kit scanner (07-03); convention docs (07-06); Evidence |
| PKG-08 | R5 subagents | 1 COMPLETE, 3 SUBSTANTIAL, 1 PARTIAL | Evidence; conformance fixtures (08-01); naming reconciliation (08-05); rulings |
| PKG-09 | Validation/release | 4 COMPLETE, 1 SUBSTANTIAL, 1 PARTIAL | Evidence; CI step + runbook (09-05); packaging probe evidence (09-04) |
| PKG-10 | R7 (future) | 5 NONE (docs by design) | Doc-only acceptance basis; fix false `_STATUS` wording; **R7 impl stays fenced** |

## 4. Two Independent Tracks (do not conflate)

- **Track A — Runtime/provider (existing plan).** `D-APP-18` decides whether `agentSdk`
  becomes the harness default after the passing live packaged read-tool proof. Owned by
  `plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md` (LP-05). **This plan does
  not touch it.**
- **Track B — Issuance (this plan).** Advancing deliverables `IN_PROGRESS → CHECKING → ISSUED`.
  The decision/governance research is explicit: `D-APP-18` bears **only** on provider default
  and even disclaims "lifecycle issuance"; **no deliverable is blocked at the issuance step by
  any fence or by `D-APP-18`.** Issuance has simply never been opened.

These are orthogonal. Track B can proceed regardless of how `D-APP-18` is ruled.

## 5. Cross-Cutting Prerequisites (clear before/early in issuance)

- **P1 — `REF-006` PRD-hash ruling.** `docs/PRD.md` `HASH_MISMATCH` is carried as an open item
  across PKG-01/03/04/06/07/08/10 (PKG-10 notes the live hash drifted again). One human
  ruling/reconcile (refresh the accepted hash, or record a governed bypass) clears PRD-derived
  acceptance criteria everywhere.
- **P2 — PKG-00 control-plane reconciliation (`SCC-CLOSEOUT-001`).**
  `execution/PKG-00.../1_Working/DAG_CLOSURE_CONTROL.md` still reads `CYCLIC` / `SCC=1` citing
  the 2026-05-24 snapshot, although the live graph is acyclic. Repoint it (and
  `execution/_Reconciliation/_LATEST.md`) to `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z`;
  mark both SCC cases CLOSED. Route: `CHANGE` / `RECONCILIATION`.
- **P3 — UI render-test acceptance bar (AMD-01).** No React render-test infrastructure exists
  (no `@testing-library/react`/jsdom/`.tsx` tests). Several PKG-02/08 specs nominally call for
  "UI tests." Human/ORCHESTRATOR ruling: do the verification clauses require component-render
  tests for `CHECKING`, or does logic-module/API-route coverage satisfy them?
- **P4 — PKG-10 doc-only acceptance basis + status truth.** All five PKG-10 `_STATUS.md` claim
  "active code implementation underway," which is false (R7 is unimplemented by design). Correct
  the wording and define a doc-only (`Evidence`-file-based) acceptance path so the five
  future-boundary **contract** deliverables can be `ISSUED` *as contracts* while R7
  implementation stays fenced.
- **P5 — Evidence-file convention.** Author one `Evidence_*.md` template/schema (REQ → live
  `file:line` → executed green test/command, with `VerificationSource`/`AssertionMode`) so all
  53 consolidations are uniform and reviewable.

## 6. Genuine Code/Scope Gaps (the only real engineering)

Most packages need **no code** — only evidence + the gate. The real engineering is small and
bounded:

- **G1 — `DEL-07-02`:** `scaffoldExecutionRoot` creates deliverable folders but does not seed
  the minimum PREPARATION fileset (`_STATUS.md` `OPEN`, `_CONTEXT.md`, `_DEPENDENCIES.md`, …)
  per REQ-004/005. Implement, or amend the spec.
- **G2 — `DEL-07-03`:** the deliverable-metadata / document-kit scanner (required-metadata
  findings, kit present/partial/absent, `_MEMORY.md` canonical handling) is not implemented
  (least-realized deliverable). Finding-category/severity enums are themselves TBD.
- **G3 — `DEL-05-01`:** canonical `<sessionId>/session.json` folder + legacy-flat migration is
  not implemented (live `session-manager.ts` writes flat `{sessionId}.json`). Implement, or
  amend `DEL-05-01` to accept the flat layout + add the missing legacy read/list/resume/delete
  + session-root-override tests.
- **G4 — `DEL-05-04`:** only backend replay exists; the "Transcript View" (view-model / route /
  component / dedicated parser) is absent. Implement a minimal view, or rescope to
  backend-replay-only with a human ruling.
- **G5 — Spec↔impl reconciliations (governed, mostly doc):** `DEL-03-01`
  `runTurn(TurnInput)` vs implemented `startTurn(AgentEngineRunInput)`; `DEL-03-02`
  whether adapter-level `turn.accepted` satisfies REQ-008 or the TurnEngine must own a
  provider-agnostic accepted event; `DEL-03-04` interruption terminal taxonomy
  (`CONFLICT-001`, de-facto resolved in code); `DEL-08-05` `HarnessSubagentRun/runId` (spec) vs
  `ChildRunRecord/childRunId` (impl). Reconcile names/contracts before contract closure.
- **G6 — Targeted additions:** `DEL-01-02` author `docs/harness/reliance_boundary_register.md`;
  `DEL-05-05` deterministic-replay-under-concurrency test; `DEL-08-01` agent-conformance
  fixtures; `DEL-09-05` add the "verify required instruction-root assets" CI step + macOS DMG
  release-verification runbook; `DEL-09-04` run/record the packaged SDK-subprocess probe;
  confirm two `DEL-06-04`/`DEL-06-05` policy values (exact-edit precondition; Bash
  120000/600000 timeouts) against accepted policy.

## 7. Tranche Spine

| Tranche | Purpose | Primary scope | Minimum validation |
|---|---|---|---|
| `ISS-00` Open Issuance Phase | Prepare `D-APP-19` (open issuance + accept this plan as active queue); on ruling, repoint coordination pointers. | Governance/control-plane only. | Governance gate; diff hygiene; path/JSON checks; no-runtime-change confirmation. |
| `ISS-01` Cross-Cutting Unblock | Land P1–P5 (PRD-hash ruling/reconcile; PKG-00 control-plane reconcile; render-test acceptance bar; PKG-10 doc-only basis + status fix; Evidence template). | Docs/control-plane + 1 reconciliation; no runtime behavior change. | Governance gate; rerun `analyze_dep_closure.py`; static checks. |
| `ISS-02` Close Code/Scope Gaps | Land G1–G6 (only engineering tranche; each item separately, behavior-additive). | `frontend/src` + tests for the named deliverables. | `npm run test`, `npm run typecheck`, focused suites, `premerge` where exposure could change. |
| `ISS-03` Evidence Consolidation Sweep | Author `Evidence_*.md` for every COMPLETE/SUBSTANTIAL deliverable (REQ → `file:line` → green test). Refresh the 2 stale Evidence files. | Per-deliverable Evidence docs only. | Evidence-template QA; cited commands re-run green; diff hygiene. |
| `ISS-04` Pilot Issuance | Prove the human-gated `IN_PROGRESS → CHECKING → ISSUED` flow end-to-end (with `approvalSha`) on the most-complete, lowest-risk set (e.g. `DEL-09-01/02/03/06`, `DEL-07-01/04/05`, `DEL-06-01/02`, `DEL-02-01`). | Lifecycle transitions via `transition.ts` / `mcp__chirality__status_transition`. | Per-transition human approval + SHA; transition tests; `_STATUS.md` audit. |
| `ISS-05…N` Wave Issuance | Walk remaining deliverables through `CHECKING → ISSUED` in the 14-wave topological order, package by package, each human-gated. | Lifecycle transitions + any residual Evidence. | Same as ISS-04, per wave. |
| `ISS-10` PKG-10 Future-Boundary Issuance | Issue the five PKG-10 **contract** deliverables under the P4 doc-only basis; reaffirm the R7 implementation fence. | Doc-only acceptance; no domain-engine code. | Doc-acceptance QA; fence reaffirmation. |
| `ISS-FINAL` Closeout | Update PKG-00 control plane to all-issued posture; record project-wide issuance status; close the program. | Control-plane + completion log. | Governance gate. |

## 8. Sequencing

`ISS-00` (acceptance) → `ISS-01` (unblock) → `ISS-02` (code gaps) ∥ `ISS-03` (evidence sweep)
→ `ISS-04` (pilot) → `ISS-05…N` (wave issuance) → `ISS-10` (PKG-10 contracts) → `ISS-FINAL`.
`ISS-02` and `ISS-03` overlap (evidence for code-complete deliverables can be written while
the few code gaps are closed). Issuance order follows the verified wave topology; the 5 orphan
deliverables (`DEL-01-01`, `DEL-01-03`, `DEL-02-04`, `DEL-10-04`, `DEL-10-05`) carry no
ordering constraint.

## 9. Boundaries — Explicit Out of Scope (human-gated)

This plan does **not** authorize, and these remain fenced (`docs/PLAN.md` §11;
`docs/CONTRACT.md`):

- `D-APP-18` default-provider cutover (separate Track A; this plan is provider-neutral and
  changes no default);
- R7 / domain-engine implementation, operation execution, `mcp__chirality__domain_*` tools
  (PKG-10 contracts may issue as *documents*; the implementation stays a future amendment);
- remote MCP, plugin marketplace, remote execution, broad tool search;
- concrete non-Anthropic providers; Windows/Linux packaging; shipped `bypassPermissions`;
- release signing/notarization/publication; professional approval, certification, sealing,
  authentication, code-compliance, or reliance/professional-boundary claims beyond what an
  individual `ISSUED` deliverable's own accepted scope supports.

Issuing a deliverable records that **Chirality's own governed acceptance** is met; it makes no
external professional/regulatory claim.

## 10. Required Human Rulings

- **`D-APP-19` (new) — Open the issuance phase + accept this plan** as the active Track-B queue.
  Without it this file stays a proposal.
- **`REF-006` PRD-hash** — refresh the accepted `docs/PRD.md` hash or record a governed bypass
  (clears P1 across 7 packages).
- **AMD-01 render-test acceptance bar** — whether `CHECKING` requires component-render tests
  for PKG-02/08 UI deliverables (P3).
- **PKG-10 doc-only acceptance basis** — accept the future-boundary contract acceptance path
  (P4).
- **Per-deliverable gates** — every `IN_PROGRESS → CHECKING` and `CHECKING → ISSUED` is itself
  a non-delegable human approval requiring a valid `approvalSha` recorded in `_STATUS.md`
  (`docs/SPEC.md` §4.3; `CONTRACT` K-GATE-1/K-AUTH-1/K-AUTH-2; enforced in `transition.ts`).
- **`D-APP-18`** — named for completeness only; it is Track A and does not block this plan.

## 11. Validation Policy

- Governance/control-plane tranches (`ISS-00`, `ISS-01` docs portions, `ISS-FINAL`): `git diff
  --check`, path/link existence, JSON parse where touched, stale-reference search, explicit
  no-runtime-change confirmation, and `analyze_dep_closure.py` after P2.
- Code tranche (`ISS-02`) and any Evidence whose claims re-run commands: `npm run test`,
  `npm run typecheck`, focused suites, and `npm run harness:validate:premerge` /
  `instruction-root:integrity` where exposure or packaging could change. Per
  `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, `docs/BUILD_AND_RELEASE.md`.
- Lifecycle tranches (`ISS-04`, `ISS-05…N`, `ISS-10`): each transition exercises `transition.ts`
  human-gate enforcement (`approvalSha` required/validated) with the `_STATUS.md` audit trail.

## 12. Acceptance Criteria

This plan is complete when:

- every deliverable is either `ISSUED` with a consolidated `Evidence_*.md` and a recorded
  `approvalSha`, or explicitly **held** with a named reason (open ruling, deferred scope);
- the PKG-00 control plane reports the live acyclic posture and project-wide issuance status;
- the recurring `REF-006` PRD-hash item is ruled/reconciled;
- PKG-10 contracts are issued under the doc-only basis with the R7 implementation fence intact;
- no §11 fence was crossed and no provider default changed.

A partial outcome (a subset issued, the rest held with reasons) is acceptable and is recorded
explicitly rather than hidden.

## 13. Finalization Rule

On acceptance (`D-APP-19`), `ISS-00` updates `_COORDINATION.md`, `NEXT_INSTANCE_PROMPT.md`,
`_LATEST.md`, and the decision register so this becomes the active Track-B queue alongside the
Track-A provider plan. Landed tranche narrative moves to `plans/PLAN_COMPLETION_LOG.md`. Work
stops whenever the next step requires a human ruling (acceptance, PRD-hash, render-test bar, or
any per-deliverable gate). Until acceptance, this file changes no coordination surface.
