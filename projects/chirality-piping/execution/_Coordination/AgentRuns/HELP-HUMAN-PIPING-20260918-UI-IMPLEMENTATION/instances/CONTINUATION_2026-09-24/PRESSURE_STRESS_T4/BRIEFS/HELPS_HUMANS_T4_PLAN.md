# HELPS_HUMANS for T4 (Agent 1): the T4 plan

You are HELPS_HUMANS (Type 1), the design manager for **T4: pressure, stress and section mechanics**, in the piping undertaking `HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION`. You are engaged by HELP_HUMAN (Agent 0), the owner's point of continuity, by the owner's decision of 2026-10-09 to start T4 now, in parallel with T3.

**Read first:**
- `NUM4/AGENTS.md`;
- `NUM4/agents/AGENT_HELPS_HUMANS.md`;
- the work graph's T4 row, the COR-PRESSURE row, the M-items M01, M02, M07, M08, M14, M30, M31 and M37, and the "Order" paragraph with its 2026-10-08 consequence.

**The owner's standing direction is production code first:** working code for the app matters most, and documents should be short and decision-useful.

## Why T4, and why now

On 2026-10-08 the owner retired the legacy pressure contract and computation product-wide. Pressure is now analysable only under the exact contract (`2.0.0/exact_straight_pressure_v2`). Today that covers straight pipe with linear supports, and refuses:
- bends, joints, fittings and other components;
- nonlinear and constant-effort supports;
- combinations and `equivalent_static`;
- materials without E/ν.

So no realistic piping layout can be analysed under pressure until T4 delivers. T4 is the critical path for:
- pressure on bends, joints and fittings;
- T2's hydrotest pressure;
- T6's pressure combinations;
- T7's components.

T3's retained-precision pressure coverage widens only behind T4, element by element.

## The deliverable: a T4 plan for the owner's approval

Write `R4/PLAN_01/PLAN.md`, about ten pages at most, plus whatever small evidence it needs. It must cover:

1. **The usable result.** Which pressure and stress capabilities the user gets, in what order, and what "done" means for each, as delivered app capability rather than internal milestones.
2. **The first usable path** (`workflows/coordinated-knowledge-work` §1). Choose an early unit that runs end to end, from authored input through solve, published outputs and readers, and that tests the premises most likely to invalidate later work. For example, pressure on a single curved bend under the exact contract.
3. **The decomposition:** units, dependencies and order, with the interfaces to:
   - T3: retained precision; the stress-recovery precision interface; the curved element's rotation consistency and W1c;
   - T1: load states;
   - T2: hydrotest;
   - T5: supports;
   - T6: combinations and result semantics;
   - T7: components.

   Use a decomposition workflow (`software-decomp` or `project-decomp`) only if it actually helps.
4. **The design questions,** each with options, evidence and your recommendation. Mark explicitly which are the owner's to decide and which are design choices within authority.
5. **Validation per unit:** independent references (VP-STATIC, VP-PUBLISHED, VP-SOURCES), and the validation T4 must rebuild:
   - `MECH-CURVED-BEND-PRESSURE-THRUST-ARC`;
   - the membrane values of `STRESS-TP-PMM-P3-MILLTOL-EFFECTIVE-WALL-STRESS`;
   - MECH-TP-PHYS-008/009's pressure halves, which were removed with the retired computation.

   All of these are rebuilt under the exact contract.
6. **The corrected joint (M07).** By the owner's decision (option A), the flawed user-stiffness element (`FK user_stiffness_local_matrix` and its plumbing) is deleted in the PR that lands T4's corrected joint. No historical copy is kept, which supersedes JR J-A's "historical witnesses only". Plan that PR, including its refusal design for legacy finite-span joints (JR J-B, `LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED`).
7. **Reviews, effort and risks:**
   - the independent reviewers each unit needs;
   - a rough effort estimate;
   - the main risks and their stop rules.

## Inputs, read on demand

- **The prior correctness design:** `I/CORRECTNESS_DESIGN/`, in particular `PRESSURE_INTEGRATION.md`, `PRESSURE_REFERENCE_QUALIFICATION.md`, `STRESS_REFERENCE.md`, `SHEAR_REFERENCE/`, `JOINT_REFERENCE/` (JR, including `CONTRACT.md`), `RESULTS_AND_COMBINATIONS.md` and `NUMERICAL_POLICY_REVIEW/`. Also read `I/T0_REASSESSMENT/` (T0's dispositions of M01, M08 and M14) and `I/DEFAULT_ROUTE_DESIGN/`.
- **The current code:**
  - the exact pressure path: PP `pressure_runtime.rs` and its exact composition;
  - the curved element: `core/solver/curved_bend`;
  - `core/loads/stress_recovery`;
  - FK's joint and rigid-body code;
  - the exact contract's refusals.
- **Today's decisions in T3's rulings** (`I/NUMERICAL_INTEGRITY_T3/ROOT_RULINGS_V1.md`, read from main or NUM; the sections dated 2026-10-08):
  - "Owner decisions: the legacy pressure contract is retired product-wide; …";
  - "Owner decision: M07's flawed joint element, option A; …";
  - the U3 rulings, D-1 A (0.1.0/0.2.0 stay as the pressure-free namespace) and D-2 A1;
  - the Stage 2 rulings.
- **T3's U3 PR,** the pressure retirement, which is in flight on `codex/piping-t3-pressure-retire-20261008` and merges to main soon. Plan against main plus U3.

## How to work

- **Engage the owner through HELP_HUMAN.** Send consequential design questions with SendMessage to `main`. Keep them few and concrete, each with a recommendation. Do not ask about ordinary choices; make them and record them.
- **You may dispatch bounded TASKs** (Type 2) for research: code inventories, reference surveys, small probes. Give each a brief under `R4/BRIEFS/` and a record under `R4/<id>/`. Use IDs **T4-I1**, **T4-I2**, … and reviewers **T4-RV1**, ….
- **When the plan is approved,** HELP_HUMAN commissions T4's WORKING_ITEMS to implement it. You stay the design partner and are re-engaged when implementation reveals something that changes the design.

## Host and records

- **The host is shared with T3.** Every cargo goes through `WT/tools/t3_cargo.sh` (`--locked --offline`), and other heavy jobs through `WT/tools/t3_slot.sh`. No DEC-025 or exclusive jobs; planning is read-mostly. Scratch goes in `WT/scratch/t4_*`.
- **Records** use placeholder paths only (`WT`, `NUM4`, `P`, `PP`, `R4`, `I`). Before every commit, run both screens exactly as T3 does (see `I/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/BRIEFS/WORKING_ITEMS_T3.md`, "Host, records and screens"). A hit stops the commit until it is read. Never print the private list.
- **Commit** on T4's branch `codex/piping-t4-pressure-stress-20261009` (worktree `WT/t4`). HELP_HUMAN pushes.

## Return

Return to HELP_HUMAN:
- the plan's path and sha256;
- a one-page summary of the first usable path and the order;
- the owner's decisions with your recommendations;
- anything that blocks.

**Budget:** 6–10 h.
