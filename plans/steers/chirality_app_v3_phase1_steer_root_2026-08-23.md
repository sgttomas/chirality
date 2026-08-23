# STANDING DIRECTION — Root governance loop — v3 release pathway, Phase 1 (SCA-004 propagation: seven PREPARATION INITs, DEL-02-06 context edit, graph re-derivation, dependency-closure audit)

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing. Owner: Ryan Tufts. Scope: Root Phase 1 of the v3 release pathway. Target workspace: Root governance loop. Paste whole; transcribe verbatim into the closeout receipt as CHAT_TRANSCRIPTION. The owner authorizes this tranche by carrying this steer; its authority derives from already-transcribed rulings — R3-B (Gate-4 propagation plan approval, Receipt 117) whose §2, §3, and §5 this steer executes, and R6-A (Gate-5 confirmation, Receipt 120). No new byte-approval is required: every output's form is prescribed by the approved `Propagation_Plan.md`.


Owner-carried steer, drafted by HELP_HUMAN 2026-08-23 after PR #635 closed
SCA-004 (Receipt 120). This is the first propagation tranche. SOW drafting,
dependency extraction, estimates, scheduling, implementation, and activation
remain later, separately gated acts and are NOT in this tranche.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `179f78fa91e66d1e1155552b03d6042df5461f7e` (PR #635). Branch from current `main`.
- `AGENTS.md` SHA-256 `377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3`.
- Live decomposition is applied revision 1.3: the seven files under `execution/_Decomposition/` carry exactly the R4-A applied identities (full values in the R4 record, Receipt 118/119); `validate_gate5_applied.py` reruns PASS 65/65 (the JSON's recorded absolute root path may differ; leave the committed JSON unchanged).
- `execution/_ScopeChange/_LATEST.md` SHA-256 `4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c` (revision-1.3 pointer; untouched by this tranche).
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/`: `Propagation_Plan.md` `abf5ff142b351eef3c16a7d33525f5688db8826f3e0eda58810eb47637645a05` (the owner-approved plan this steer executes); `Decision_Log.md` `e123d3000bb087d3939d8e05582fbd75df7817cb685cc160944ec107e491e092`; `Handoff_State.md` `d7a63c8607e7b0f1b329da909d6aacc29e71a2cde5a1ff9cedff915172429644` (status `CLOSED_CONFIRMED_PROPAGATION_PENDING`).
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/` contains exactly DEL-02-01..DEL-02-06 and `execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/` exactly DEL-04-01..DEL-04-10; none of the seven new folders exists anywhere under `execution/`.
- `execution/PKG-02_…/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_CONTEXT.md` SHA-256 `1e914009863fd67aca343eb2a1ae2cb5ca7ddefe698139b00614ad7e042cec45`.
- `execution/_Coordination/_TaskManagement/REGISTER.csv` SHA-256 `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` (19 live; untouched by this tranche).
- `execution/_Coordination/HANDOFF_STATE.md` SHA-256 `03eb195290bda6d7e173679ac9f65e9359b19defcfa400f259c4cae23bce1a39`.
- Last Root receipt is 120. This tranche writes Receipt 121.

## Objective

Execute the approved `Propagation_Plan.md` §2, §3, and §5: materialize the
seven new deliverable folders with initialized metadata, update DEL-02-06's
`_CONTEXT.md` per the approved edit list, re-derive the objective-relative
work graph from live Root nodes, and run a fresh dependency-closure audit.
No SOW, dependency extraction, estimate, schedule, lifecycle transition
beyond `OPEN` initialization, TM, tool, runtime, pin, or App surface
changes. No hold is lifted; all ten DEL-02-06 bindings remain
`HELD_UNAVAILABLE`.

## Nodes (N=2, write-disjoint, N1 before N2; Agent 2 instances with sealed briefs under `execution/_Coordination/AgentRuns/ROOT_V3_PHASE1_2026-08-<DD>/instances/<NODE>/`)

### N1 — PREPARATION (PROJECT_SETUP lane): seven INIT folders + DEL-02-06 context edit
Write targets, exactly: the seven new folders below, and `execution/PKG-02_…/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_CONTEXT.md`.
Create each folder at the exact path from the approved plan §2 table, under its existing package `1_Working/`:
- `DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/` (PKG-02)
- `DEL-02-08_Exact_Supply_and_Protocol_Pinning/` (PKG-02)
- `DEL-02-09_Hosted_Account_and_Consent_Boundary/` (PKG-02)
- `DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/` (PKG-02)
- `DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation/` (PKG-02)
- `DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in/` (PKG-02)
- `DEL-04-11_Root_Loop_Receipt_Validator/` (PKG-04)
Each folder gets exactly four files, per plan §2:
- `_CONTEXT.md` — grounded in the accepted revision-1.3 candidate row for that DeliverableID (name, type, Context Envelope M, scope/objective mappings, description, anticipated artifacts, anticipated write locus as planning note never authorization) plus the plan-§2 boundary note for that row (e.g. DEL-02-07: daemon remains sole runtime broker, no TCP listener; DEL-02-08: no pin amendment, OpenAI service endpoints separate from command network; DEL-02-09: G0 A3/A7 carriage, ambient `~/.codex` excluded; DEL-02-10: G0 A7 and the exact four terminal identifiers; DEL-02-11: G0 A4, no in-flight re-attach claim; DEL-02-12: all ten bindings remain held; DEL-04-11: `tools/**` implementation requires separate M2 authority).
- `_STATUS.md` — initialized `OPEN`; no other lifecycle state.
- `_REFERENCES.md` — citing the SCA-004 accepted evidence: the approved candidate row (register SHA `2cdf1e68…`), R3-A and R6-A via Receipts 117/120, the applied working surface `546b6e4c…`, and `_LATEST.md` `4335593a…`.
- `_DEPENDENCIES.md` — initialized without invented dependencies (explicitly states dependency extraction is a later act).
No `ScopeOfWork.md` is created. Before relying on any sibling `_STATUS.md`, read sibling `_MEMORY.md`/`MEMORY.md` when present as non-authoritative context (plan §2).
DEL-02-06 `_CONTEXT.md`: apply exactly the plan-§3 six-item edit list — (1) restate the role as standing semantic integration and release assurance; (2) preserve SOW-104, OBJ-001/002/004/007, REQ-027, D-GOV-20, and the accepted ten-binding hold matrix; (3) name DEL-02-07..DEL-02-12 as separately gated implementation/conformance carriers and require their evidence fan-in; (4) preserve the accountable-human release disposition and client non-ownership boundary; (5) retain ContextEnvelope M and the accepted anticipated write locus; (6) add SCA-004 accepted candidate/application evidence references. Do not change DEL-02-06 `_STATUS.md`, `ScopeOfWork.md`, `_DEPENDENCIES.md`, accepted compatibility bytes, or any held binding.
Check surface: exactly 7 folders × 4 files created with recorded SHA-256 values; every `_CONTEXT.md` fact traceable to the applied register row or plan §2 (no invented scope); `_STATUS.md` files say `OPEN` and nothing more; DEL-02-06 `_CONTEXT.md` diff confined to the six items; no other `_STATUS.md`, SOW, or `_DEPENDENCIES.md` changed; each INIT return reports files, hashes, preserved package parent, `OPEN` lifecycle, and blockers rather than inventing SOW/dependency/estimate/schedule/activation state.

### N2 — Graph re-derivation + dependency-closure audit (derivative evidence; runs after N1)
Write targets, exactly: `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/DEP_GRAPH_POST_GATE5/` (new folder: re-derived `WORK_GRAPH.json`, `DAG.md`, SCC report) and `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/AUDIT_DEP_CLOSURE_POST_GATE5/` (new folder: fresh `AUDIT_DEP_CLOSURE` run). The Gate-1 `WORK_GRAPH.json` and `Evidence/AUDIT_DEP_CLOSURE/` baseline are preserved untouched.
- Re-derive the objective-relative work graph from live Root nodes including the seven new folders, per plan §5; recompute SCCs; resolve or hold cycle-participating edges per the cycle-resolution rule (`docs/CYCLE_DRIVEN_RESOLUTION.md`); cuts/merges are human-gated — if one is needed, record it as a blocker and stop that step rather than deciding it.
- Dispatch a fresh `AUDIT_DEP_CLOSURE` over the live state; expected shape: 53 deliverables present, the seven new folders in `OPEN` with initialized-empty declared dependencies (record that as the expected post-INIT state, not a defect), zero unresolved closure violations among pre-existing folders versus their prior audit.
- Both outputs are derivative packages: cite the accepted SCA-004 snapshot, the applied revision-1.3 identities, and this tranche's N1 outputs; state explicitly that they must be re-derived after dependency extraction and SOW acceptance (the recorded downstream reruns per plan §6 item 6).
Check surface: graph node set equals the 53 register rows plus packages; SCC report present; audit return, decision log, and summary recorded with hashes; no live decomposition, pointer, folder-metadata, or TM write.

## Not selectable in this tranche
`AGENTS.md`, `agents/**`, `docs/**`, the seven live decomposition files, `execution/_ScopeChange/_LATEST.md`, every SCA-004 file outside the two new `Evidence/` subfolders, any existing folder's `_STATUS.md`/`ScopeOfWork.md`/`_DEPENDENCIES.md` (except the DEL-02-06 `_CONTEXT.md` edit named in N1), estimates, schedules, dependency extraction, the Task Management register, `tools/**`, `runtime/**`, `projects/**`, `exports/**`, pins, and any App surface. No lifecycle state beyond initializing the seven new `_STATUS.md` files to `OPEN`.

## Failure rule
Unlimited repair with fresh re-review per node. A node that cannot complete
returns its handoff state with blockers instead of narrowing silently. Never
widen a node's write set; if a needed write falls outside it, report and stop
that node. A human-gated graph cut/merge decision stops N2's affected step
and returns the SCC evidence for owner ruling.

## Closeout
One tranche, one branch `codex/root-v3-phase1-2026-08-<DD>`, one PR to
`main`, commits in order N1 → N2. Append Receipt 121 to
`execution/_Coordination/LOOP_RECEIPTS.md` after the fact, in-PR, with: this
steer as CHAT_TRANSCRIPTION (record its SHA-256); per-node write sets; every
created file's SHA-256; the DEL-02-06 `_CONTEXT.md` before/after SHAs and
diff summary; graph/SCC/audit results; validator outputs including the
CI-form G4 output (expected: zero instruction-surface paths);
`execution/_Coordination/HANDOFF_STATE.md` updated (SCA-004 propagation:
INITs done, graph/audit re-derived; remaining: SOWs, dependency extraction,
estimates, schedule, and their reruns). Run before pushing:
`validate_candidate_whitespace.py --base-ref origin/main`,
`validate_agent_instructions.py`, `validate_instruction_entrypoints.py`,
`validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only`,
`tools/taskmgmt/taskmgmt.py validate --register execution/_Coordination/_TaskManagement/REGISTER.csv`,
`git diff --check`. Raw captured logs follow the evidence-whitespace
convention (normalize or gzip preimages) before committing. Do not merge. If
`main` advances, request sync authorization from the owner and record it in
the receipt. HELP_HUMAN byte-verifies before endorsement; SOW drafting and
all later propagation remain separately gated owner-routed work.
