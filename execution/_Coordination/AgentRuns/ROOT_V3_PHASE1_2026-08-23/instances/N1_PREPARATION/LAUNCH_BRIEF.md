# Sealed launch brief — N1 PREPARATION

## Identity and authority

- **Role:** Agent 2 PREPARATION; load and obey `agents/AGENT_PREPARATION.md` in full.
- **Role enforcement:** instruction-asserted; do not delegate or create another orchestration layer.
- **Caller:** HELP_HUMAN (Agent 0), owner-authorized Phase 1 steer.
- **Basis:** `origin/main@e677edbe81188465eb36e700b6bd441715bcbccd`; branch `codex/root-v3-phase1-2026-08-23`.
- **Authority:** Phase 1 steer SHA-256 `2bbd449330b25d2ab88cec4097d3e224b95305954d30196e94fbd21c21062452`, executing only approved `Propagation_Plan.md` §§2 and 3.

## Objective

Initialize exactly seven accepted revision-1.3 deliverables with the four-file steer-prescribed metadata set, and apply exactly the six-item DEL-02-06 context propagation. Do not create a SOW, dependencies, estimates, schedule, activation, or any other lifecycle state.

## Required reads

Read `AGENTS.md`, `agents/AGENT_PREPARATION.md`, the Phase 1 steer, `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md`, the seven applied decomposition files, the complete DEL-02-06 folder surfaces, and relevant sibling `_MEMORY.md`/`MEMORY.md` before relying on sibling statuses. Treat memory as non-authoritative. Inspect patterns in live sibling deliverable metadata without importing facts not present in the accepted row/plan.

## Project-content write ownership

Exactly:

1. `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/`
2. `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/`
3. `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/`
4. `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/`
5. `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation/`
6. `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in/`
7. `execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/DEL-04-11_Root_Loop_Receipt_Validator/`
8. `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_CONTEXT.md`

Control-plane return ownership is limited to this instance directory's `RETURN.md` and `STATUS.json`.

Each new folder contains exactly `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md`. Follow the steer when its prescribed four-file set narrows PREPARATION's general template. `_STATUS.md` is `OPEN` only. `_DEPENDENCIES.md` states extraction is later and invents no edge. No `ScopeOfWork.md`, `_MEMORY.md`, or `_SEMANTIC.md` is created in this tranche.

## Content contract

For each `_CONTEXT.md`, copy facts from the accepted revision-1.3 deliverable-register row: ID/name/type, `ContextEnvelope=M`, mappings, description, anticipated artifacts, and anticipated write locus labelled planning only, never authorization. Add only that row's Propagation Plan §2 boundary. Preserve the exact terminal identifiers and G0 references where named by the steer.

For DEL-02-06 `_CONTEXT.md`, make only the steer §3 six-item semantic edit: standing semantic integration/release assurance; preserve SOW-104, OBJ-001/002/004/007, REQ-027, D-GOV-20, ten holds; name DEL-02-07..12 as separately gated carriers with evidence fan-in; preserve accountable-human release disposition and client non-ownership; retain M and write locus; add SCA-004 candidate/application evidence.

## Stops

Stop and return a blocker for any identity drift, pre-existing target folder, needed out-of-scope write, overwrite, invented fact, lifecycle other than OPEN, SOW/dependency/estimate/schedule/activation need, or uncertain authority. Unlimited repair is allowed only inside the declared writes. Do not commit.

## Acceptance and return

- exactly 28 new files (7 x 4), with SHA-256 table;
- seven exact folder parents, `OPEN` status, and deferred-dependency statements;
- no SOW and no extra file;
- DEL-02-06 before/after SHA and diff summary confined to six items;
- protected `_STATUS.md`, SOW, `_DEPENDENCIES.md`, decomposition, pointer, TM register, and unrelated files unchanged;
- every INIT return states parent, files/hashes, OPEN lifecycle, and blockers;
- `git diff --check` and candidate-whitespace validation pass;
- write `RETURN.md` and terminal `STATUS.json` in this instance directory.
