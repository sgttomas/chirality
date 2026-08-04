# Sealed brief — H1-A2-G4-VERIFY

- Parent: `HELPS_HUMANS`, node `H1` in run
  `ROOT_FOUR_LANES_2026-08-02`, plan v2.
- Construction: ephemeral Agent 2 generalist; no delegation.
- Objective: read-only review of the proposed G4 CI integration boundary.
- Context:
  - `.github/workflows/governance-harness.yml`
  - `tools/validation/validate_instruction_tranche_manifest.py`
  - `tools/validation/test_validate_instruction_tranche_manifest.py`
  - `execution/_Coordination/_TaskManagement/G4_CI_HANDOFF_TM-ROOT-110_2026-08-02.md`
- Questions:
  1. Which PR/push base and head refs are canonical in the existing workflow?
  2. Why would unqualified all-manifest diff coverage fail to prove that the
     candidate tranche carries a manifest?
  3. What is the smallest backward-compatible validator/CI contract that
     makes a missing candidate manifest fail while preserving whole-corpus
     schema validation?
  4. What positive, negative, and workflow-wiring tests prove that contract?
- Tools: read-only repository inspection and non-mutating commands.
- Write scope: none. Return findings through the governed child-session return.
- Prohibitions: no edits, no commits, no pushes, no delegation, no authority
  interpretation beyond the cited handoff and current validator contract.
- Acceptance: concise recommendation, edge cases, exact proposed assertions,
  and any blocker or compatibility risk.
