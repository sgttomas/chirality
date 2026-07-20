# W4-DAPP50-REPAIR-REPIN-CORRECTION — WORKING_ITEMS Brief

- **Role:** WORKING_ITEMS
- **Package:** `PKG-10_Domain_Engine_Future_Boundary`
- **Selected deliverable:** `DEL-10-01_DomainEngineProfile_Contract_Draft`
- **Required branch/HEAD:**
  `codex/app-dev-dapp50-headless-live-20260720` /
  `fcf152bdae1e1764b11dfabf3f87d50c5680213d`
- **Posture:** serialized single-manager correction; delegation prohibited
- **Objective:** bind the D-APP-48 private pull contract to the reachable repair
  commit and durably record the V1 repair without rewriting W2 history.

Read full `AGENTS.md`, `agents/AGENT_WORKING_ITEMS.md`, `updates/v7.md`, W2,
V1, W3, and G1 terminal records, the live D-APP-48 pull contract, DEL-10-01
status and W2 run record, and the receipt ledger. Reproduce the required HEAD,
G1 topology/path hashes, W2 hashes and Receipt-83, W3 repair evidence,
`frontend/dist` absence, zero staged paths, and dirty-state containment. Return
`BLOCK` before writes on mismatch.

## Exact project-content authority

Write only these four project-content surfaces:

1. `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json`
   - change only `source.commitSha` from the G0 commit to
     `fcf152bdae1e1764b11dfabf3f87d50c5680213d`;
   - preserve registry version, exports, hashes, order, commands, package
     identity, constants, and every boundary flag byte-for-byte otherwise;
   - prove the deterministic pull-contract validator passes at the new pin.
2. DEL-10-01 `_STATUS.md`
   - preserve `Current State: IN_PROGRESS`, Checking Approval SHA, the complete
     `## Remaining` section, and all earlier history;
   - append one concise dated repair/repin history line only. Do not reopen or
     re-close a residual and do not change lifecycle state.
3. Create exactly one new record:
   `projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft/_run_records/WORKING_ITEMS_RUN_2026-07-20_DAPP50_RESULT_CONTRACT_REPAIR.md`.
   Bind V1 findings, W3 repair/cleanup evidence, G1 commit/topology/hashes,
   strict result-contract scope, validation evidence, unchanged D-APP-50
   boundaries, and next V2 gate. State that deleted `frontend/dist` was ignored
   generated packaging residue, reproducible only by rerunning packaging and
   not Git-restorable.
4. `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`
   - preserve Receipt-83 byte-for-byte;
   - append exactly one new `Receipt 84`, parent `Receipt-83`, with
     `Examined-Through` equal to the G1 commit, pointers to the new repair run
     record, V1 evaluation, W3/G1 terminals, and corrected D-APP-48 contract;
   - distinguish the failed V1 evidence, executed repair, ignored-output
     cleanup, and held V2/final-publication gates.

Also write this instance's terminal `RETURN.md`, `HANDOFF.md`, and terminal
`STATUS.json`. Do not edit the W2 run record, Receipt-83, implementation/test
bytes, any other source, decision/register, piping/tier-0/PEC surface, prior
control/evaluation file, or ignored/build output.

## Required validation

- strict duplicate-key JSON for D-APP-48 and terminal status;
- `python3 tools/coordination/validate_harness_contract_pull.py --pull-contract projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json`;
- recorded harness-contract dependency lint;
- focused repaired runner suite;
- receipt validator before and after Receipt-84;
- authority corpus v9, repository self-check, validation pytest, and
  practitioner-harness pytest baselines;
- exact diff/no-index/cached/staged/whitespace/write-containment checks;
- confirm `frontend/dist` remains absent and no packaging command runs.

No Git action, push, PR, merge, apply transport, piping/tier-0/PEC edit,
packaging, release, publication, lifecycle transition, boundary expansion,
waiver, or professional/solver-truth claim. Return `ACCEPT | BLOCK` with exact
before/after hashes, validation evidence, blockers/unknowns/conflicts/waivers,
and V2 as the sole next gate.
