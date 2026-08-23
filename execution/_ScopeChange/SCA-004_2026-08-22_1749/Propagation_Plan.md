---
amendment_id: SCA-004
doc_kind: scope_change.propagation_plan
decomp_variant: SOFTWARE
gate: 4
created: 2026-08-23
status: awaiting_gate_4_approval
accepted_gate_3_candidate: pending owner approval of Gate_3_Candidate
requested_by: Ryan Tufts through R2-A
---

# SCA-004 Gate 4 — propagation plan

Gate-4 owner approval is `PENDING_OWNER_APPROVAL`. This plan is executable
only after the owner separately approves the exact Gate-3 candidate. It does
not perform Gate 5, PREPARATION, dependency extraction, estimates, scheduling,
graph regeneration, audits, pointer changes, implementation, or activation.

`Amendment_Actions.csv` is the machine-readable Gate-4 register. It uses the
current nine-column STRUCTURE schema and records
`SupersessionBindingPresent=NO` for each of the eight actions: every action is
structural or organizational, and the accepted evidence identifies no
admitted-authority fact that these actions supersede.

## 1. Gate-5 direct authoritative writes — exact copy only

After Gate-3 and Gate-4 approval, the applying SCOPE_CHANGE act may copy only
the seven exact candidate surfaces to their matching live paths under
`execution/_Decomposition/`. Before copying, it must reverify the seven bound
basis SHAs and rerun `validate_gate3_candidate.py` with `PASS`, 98/98.

It must not edit candidate contents during application. Record each before/
after SHA. Gate-5 closure remains separate from the direct copy and requires
the post-application validation lane below.

## 2. PREPARATION INIT briefs — seven new folders, not dispatched here

Each INIT is a later PROJECT_SETUP/PREPARATION-owned act. Every brief creates
one exact folder under its existing package with these four metadata files:

- `_CONTEXT.md` grounded in the accepted candidate row;
- `_STATUS.md` initialized to `OPEN`;
- `_REFERENCES.md` citing SCA-004 accepted candidate/application evidence;
- `_DEPENDENCIES.md` initialized without invented dependencies.

No `ScopeOfWork.md` is created by these INIT briefs. SOW drafting and
acceptance remain a later separately gated WORKING_ITEMS act. Before any
consumer reads `_STATUS.md`, it also reads sibling `_MEMORY.md` / `MEMORY.md`
when present as non-authoritative operational context.

| INIT brief | Exact folder | Candidate row / boundary |
|---|---|---|
| INIT-01 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/` | Process supervisor/private-socket slice; daemon remains sole runtime broker; no TCP listener |
| INIT-02 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/` | exact supply/protocol slice; no pin amendment; OpenAI service endpoints separate from command network |
| INIT-03 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/` | root-private account/consent slice carrying G0 A3/A7; ambient `~/.codex` excluded |
| INIT-04 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/` | API/event/approval slice carrying G0 A7 and four terminals |
| INIT-05 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation/` | retirement/restart slice carrying G0 A4; no in-flight re-attach claim |
| INIT-06 | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in/` | conformance/source-identity/fan-in slice; all ten bindings remain held |
| INIT-07 | `execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/DEL-04-11_Root_Loop_Receipt_Validator/` | Root-specific TEST_SUITE; `tools/**` implementation requires separate M2 authority |

Each INIT return must report exact files created, hashes, preserved package
parent, `OPEN` lifecycle, and a blocker rather than inventing any SOW,
dependency, estimate, schedule, or activation state.

## 3. DEL-02-06 `_CONTEXT.md` edit list — later propagation write

After exact Gate-5 application, update only DEL-02-06 `_CONTEXT.md` fields
that mirror the accepted decomposition row:

1. restate the role as standing semantic integration and release assurance;
2. preserve `SOW-104`, OBJ-001/002/004/007, REQ-027, D-GOV-20, and the
   accepted ten-binding hold matrix;
3. name DEL-02-07..DEL-02-12 as separately gated implementation/conformance
   carriers and require their evidence fan-in;
4. preserve the accountable-human release disposition and client non-
   ownership boundary;
5. retain `ContextEnvelope=M` and the accepted anticipated write locus;
6. add SCA-004 accepted candidate/application evidence references.

Do not change DEL-02-06 `_STATUS.md`, `ScopeOfWork.md`, `_DEPENDENCIES.md`,
accepted compatibility bytes, or any held binding in this propagation step.

## 4. Dependency, estimate, and schedule advisories

1. After all seven folders are live, run dependency extraction for each new
   folder and reassess DEL-02-06 as the integration/fan-in carrier. Record
   cross-loop App coupling only as notice/fan-in edges, never foreign
   authority.
2. Produce a fresh estimate snapshot for the seven new carriers and reassess
   DEL-02-06 only after accepted SOWs, Context Envelopes, write loci,
   dependencies, gates, and acceptance checks exist.
3. Recompute scheduling only after dependency extraction and estimate
   acceptance. TM-ROOT-106 and TM-ROOT-122 remain G1 blockers; this plan embeds
   no pin assumption.
4. No dependency, estimate, or schedule artifact is written by Gate 5's exact
   decomposition-copy act.

## 5. Graph and audit reruns

- After the seven folders are live, re-derive the objective-relative
  `WORK_GRAPH.json` and `DAG.md` from live Root nodes; recompute SCCs; then
  dispatch a fresh `AUDIT_DEP_CLOSURE`. Until then, the Gate-1 graph remains
  current for the live topology and deliberately omits candidate IDs.
- After Gate-5 application, run the deterministic register/trace/telemetry
  postcheck and a fresh scoped `AUDIT_DECOMP` backcheck. Compare it to the
  Gate-1 baseline at
  `Evidence/AUDIT_DECOMP/coverage_summary.json` SHA-256
  `2210e77f989f29c11e005d7fe89944e2e0f0fe265e0a514f53042aaa89de9e45`.
- The expected applied topology is 53 deliverables, PKG-02=12, PKG-04=11,
  packages=6, scope items=104, objectives=7, zero unmapped IN items, zero
  unmapped objectives, and zero untraced reverse units.

## 6. Closure-validation lane — separate from Gate-5 writes

The direct Gate-5 copy cannot itself claim closure. Before SCOPE_CHANGE can
present an applied state, the closure lane must:

1. reverify applied-file hashes against the owner-approved candidate;
2. rerun `validate_gate3_candidate.py` or an applied-state equivalent;
3. run the post-application `AUDIT_DECOMP` backcheck;
4. confirm no live folder/SOW/status/dependency was created by the copy act;
5. confirm every ten-binding hold remains `HELD_UNAVAILABLE`;
6. record derivative staleness/currentness and all downstream reruns;
7. return applied state to the owner for Gate-5 confirmation.

PREPARATION, dependency, estimate, schedule, graph, AUDIT_DEP_CLOSURE, SOW,
implementation, client, cutover, and release work remain downstream and must
not be described as satisfied by the copy or closure lane.

## 7. `_LATEST.md` pointer treatment

`execution/_ScopeChange/_LATEST.md` is not in this Gate-4 write scope. Any
pointer change requires its own accepted authority and exact pointer
treatment. Gate-3/4 approval, Gate-5 application, or creation of this plan
does not silently grant that authority.

## 8. Rollback and stop rules

Before Gate-3/4 approval and Gate-5 application, there is no live
decomposition change to roll back. If any bound basis SHA drifts, any exact
candidate validation fails, or a required write falls outside an approved
later act, stop and return the blocker. After an accepted application, any
substantive reversal is a new human-initiated SCOPE_CHANGE.

## Gate-4 question

**Do you approve this propagation plan, separately from approval of the exact
Gate-3 candidate bytes?**
