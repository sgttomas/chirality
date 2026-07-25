# §7 Preflight Report — scratch root PKG-* skeleton (ROOT-LANE-B-20260725)

Executed by: Agent 0 (parent-executed N0), 2026-07-25.
Basis: throwaway git worktree at `origin/main` (`ba2b80bf2`), detached.
Scratch materialization (never committed, untracked only):
`execution/PKG-00_Scratch_Preflight/1_Working/DEL-00-01_Scratch_Deliverable/`
with `STATUS.md`, `DELIVERABLE.md`, `_run_records/`. Worktree destroyed
after the runs below; `git status` in the worktree showed the skeleton as
untracked throughout; nothing entered any integration branch.

## Per-suite outcomes against the scratch tree

| # | Suite | Outcome | Detects scratch PKG? |
|---|---|---|---|
| S1 | `python3 -m pytest tools/practitioner_harness -q` | **311 passed** (exit 0) | No — blind |
| S2 | `tools/practitioner_harness/harness.py self-check` | exit 0 | No — blind |
| S3 | G0 test suite (`test_validate_root_materialization_fence.py`) | 8 passed, **1 failed: `test_live_repo_state_is_clean`** (exit 1) | Yes — G0's own live-state test |
| S4 | G0 fence (`validate_root_materialization_fence.py`) | **BLOCK**, exit 1: "materialized root packages/deliverables found: PKG-00_Scratch_Preflight … registration surface … absent … while PKG-*/DEL-* structure exists" | Yes — **the fence working as designed** |
| S5 | `validate_path_anchors.py` | PASS (992 surfaces, exit 0) | No — blind |
| S6 | `validate_skill_metadata.py` | exit 0 | No — blind |
| S7 | `validate_agent_instructions.py` | exit 0 | No — blind |
| S8 | `validate_instruction_entrypoints.py` | exit 0 | No — blind |

S1–S4 are exactly the production governance-harness CI battery; S5–S8 are
the general-purpose standalone validators.

## Finding (confirms D-GOV-21 §5.1)

No production harness or validator code other than G0 guards root
`execution/` structure: the full practitioner-harness suite, self-check,
and every general standalone validator accept a materialized root `PKG-*`
skeleton without complaint. The G0 BLOCK (S4) and its live-state test
failure (S3) are the intended fence behavior, not defects and not the
finding itself. Consequence: G1–G4 capability is a genuine precondition
for lawful materialization — nothing else would catch undeclared root
packages, ownership violations, work-graph conflicts, or unmanifested
instruction-surface tranches.

## Disposition

Worktree destroyed immediately after the runs (`git worktree remove
--force`); no scratch bytes survive outside this report.
