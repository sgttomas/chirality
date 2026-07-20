# W2-DAPP50-REPIN-CLOSEOUT — Sealed WORKING_ITEMS Brief

## Identity and basis

- **Role:** WORKING_ITEMS (Agent 1), serialized closeout owner
- **Parent control:** ORCHESTRATOR for HELP_HUMAN
- **RunID:** `APPDEV_LOOP_2026-07-20_DAPP50_HEADLESS_LIVE`
- **Required branch/HEAD:** `codex/app-dev-dapp50-headless-live-20260720` /
  `f67d44706f4b2b5495833f809cb0bc714d2bbc18`
- **Required parent:** `bc35e3b0049d990f494dd3610603be285c7aa9ed`
- **Delegation/Git:** prohibited

Read full `AGENTS.md`, `agents/AGENT_WORKING_ITEMS.md`, run controls through
`updates/v3.md`, W1/G0 terminal records, D-APP-48 packet/contract/validator,
D-APP-50 packet/ruling, DEL-10-01 `_STATUS.md`, and the receipt ledger rules.
Reproduce the exact reachable commit and 14-path tree before writing. Any
mismatch returns `BLOCK` without repair.

## Exact work

1. Repin
   `execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json`
   to source commit `f67d44706f4b2b5495833f809cb0bc714d2bbc18`.
   Set `constants.harnessToolRegistryVersion` to
   `harness-tools.v14.headless-preview-live`; refresh only export hashes whose
   committed bytes changed (expected `./tool-catalog` =
   `27504b2a5a487116a6c7a886d56efdc5f3cf4426779f2a3dca665e184977f83e`
   and `./tool-descriptor` =
   `a121391ec71851e7280db4ebf2731b53db6829cb42d1bf07604cb8a4f76dc6d4`).
   Preserve package identity, other constants, export order/targets/hashes,
   validation commands, and boundaries unless the deterministic validator
   proves a different byte-current export hash. Do not reinterpret a boundary
   flag: the contract records what D-APP-48 itself authorizes, not a new ruling.
2. Run the established validator exactly:
   `python3 tools/coordination/validate_harness_contract_pull.py --pull-contract projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_2026-07-04.json`.
   Also run the recorded dependency-lint command. Both must pass against the
   reachable commit.
3. In DEL-10-01 `_STATUS.md`, remove exactly the Remaining bullet beginning
   `Flip mcp__chirality__domain_headless_preview_run from descriptor-only to live`.
   Preserve the separate new-owner-ruling Remaining bullet byte-for-byte,
   preserve `IN_PROGRESS`, `Checking Approval SHA`, and all earlier history,
   and append one dated history line naming D-APP-50, the implementation commit,
   live `open_pipe_stress` read-only transport, D-APP-48 repin, and no lifecycle
   change.
4. Create exactly one run record:
   `execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft/_run_records/WORKING_ITEMS_RUN_2026-07-20_DAPP50_HEADLESS_PREVIEW_LIVE.md`.
   Record authority, staged-closeout rationale, implementation commit,
   `runnerInputRef` rationale, configured path/hash/process boundaries, DEC-065
   exit semantics, tests/checks, repin values, exact changed paths, rejected
   alternatives, exclusions, and surviving Remaining item. Make no lifecycle,
   release, professional, or solver-truth claim.
5. Only after 1–4 and all checks pass, append exactly one versioned Receipt-83
   to `loop/LOOP_RECEIPTS.md` under its local grammar: Parent-Receipt Receipt-82,
   Examined-Through `bc35e3b0049d990f494dd3610603be285c7aa9ed`, pointers to this run and G0
   commit, a concise executed gate outcome, pass/fail-only checks, and no
   invented owner attribution. Rerun the receipt validator.

## Validation and containment

Run strict JSON duplicate-key parsing on the pull contract and W2 status,
pull-contract validator, contract dependency lint, focused 23-test transport
suite (read-only confirmation), generated catalog test, typecheck, receipt
validator, authority corpus v9 status, repo-wide self-check, validation pytest
123 baseline, practitioner-harness pytest 311 baseline, and tracked/untracked/
cached diff/whitespace/scope checks. Packaging, instruction-root bundle checks,
network proof, and release commands are prohibited/not applicable.

## Write scope and prohibitions

Allowed writes are exactly:

- D-APP-48 pull-contract JSON;
- DEL-10-01 `_STATUS.md`;
- the one exact DEL-10-01 run record above;
- `loop/LOOP_RECEIPTS.md`, one append only;
- this W2 instance's `RETURN.md`, `HANDOFF.md`, terminal `STATUS.json`.

All frontend source/tests/docs, other controls, decisions/registers,
deliverables, piping, tier-0, pec, and repo-root paths are read-only. No source
repair, apply/proposal transport, lifecycle transition, provider/network,
packaging, publication, distribution, release/professional/certification/
sealing/authentication/code-compliance/solver-truth claim, waiver, or Git.

Return terminal `ACCEPT | BLOCK` with exact before/after hashes, validator
outputs, changed path accounting, Receipt-83 ledger hash, preserved-boundary
proof, blockers/unknowns/waivers, and the independent-EVALUATION next gate.
