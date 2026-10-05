# Brief AM: draft the Agent User Manual and App v4 consistency edits

TASK (Type 2) for HELP_HUMAN (ROOT), run `ROOT-LOOPINIT-AUM-ALIGNMENT-20261005`. You return to ROOT and do not delegate. You make no Git writes. Write only `RUN2/AUM_EDITS.md`.

**Placeholders.**
- `WT` = the T3 worktree root.
- `NUM` = `WT/numerics`. Read here; this checkout carries #1092's changes.
- `RUN2` = `NUM/execution/_Coordination/AgentRuns/ROOT-LOOPINIT-AUM-ALIGNMENT-20261005`.
- `PRUN` = `NUM/projects/chirality-piping/execution/_Coordination/AgentRuns/PIPING-LOOP-INIT-20261005`.
- `AUM` = `NUM/docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v3.md`.

## The basis

- **The owner's direction:** `RUN2/OWNER_DECISIONS.md`.
- **What changed, and what will change:**
  - **Piping's new `NUM/projects/chirality-piping/loop/LOOP_INIT.md`,** in the binding form. Read it in full. Its section numbering and procedure text are gone; the procedure now lives in the bundled workflows (`NUM/workflows/`), the Field Book and AUM.
  - **`PRUN/CONSISTENCY_EDITS.md` §C1,** which lists AUM passages made stale or dangling. Also read `PRUN/LOOP_INIT_MAPPING.md`, which says where each old piping rule now lives. Use it to re-point citations.
  - **App v4's LOOP_INIT** (`NUM/projects/chirality-app-v4/loop/LOOP_INIT.md`) will change one sentence: "If you are unsure whether something matters, ask the human." becomes "If you are unsure whether a section matters, read it."
- **Unchanged and still legacy:** the App (v3) loop (`NUM/projects/chirality-app-dev/loop/LOOP_INIT.md`), and the Runtime and PEC loops. AUM statements about them must stay true. Where a sentence covers "App and Piping" jointly, split it only as far as needed.

## The output: `RUN2/AUM_EDITS.md`

1. **Exact before and after edits to `AUM`,** each with its line numbers and a one-line reason. Each "before" must occur exactly once (check with a byte count). The edits must make the manual consistent with piping's binding-form LOOP_INIT and App v4's changed sentence. Cover every AUM passage that:
   - cites a piping loop section that no longer exists (`[Piping loop §…]`);
   - attributes to piping's LOOP_INIT content it no longer holds: procedure, recovery steps, receipt or cursor validation, closeout, terminal condition, or pointing to a graph;
   - says something about piping's loop that is now untrue, including the already-stale "none selected for a successor undertaking" statements about piping (C1). These concern the same passages, so include them.
   - describes App v4's entry or reading guidance in a way the changed sentence would contradict. Check this; AUM may say nothing about it.
   
   Re-point each citation to where the rule now lives: the bundled workflows, the Field Book or another AUM section. Use the existing link-reference definitions at the end of AUM where they fit. If you need a new definition, give it exactly. Keep the edits minimal and in AUM's voice. Do not revise other content.
2. **Any other minimal consistency edits outside AUM** made necessary by App v4's sentence change. Search `NUM/projects/chirality-app-v4` outside `execution/` records, `NUM/init/`, `NUM/docs/` (excluding AUM, archives and historical manifests) and `NUM/workflows/`.
   - **App v4's product resources** that pin LOOP_INIT's sha256 (`app/src-tauri/resources/instructions/SOURCE_MAP.json` and `policy_standing/**/basis.json`) are App v4's own basis. **List them; do not propose editing them.** ROOT routes a notice instead.
3. **Listed only, not proposed:**
   - Field Book or Consolidated v8 statements that conflict;
   - workflow sentences that would need `create-workflow`, such as construct's introduction;
   - anything about App v3, Runtime or PEC that is stale for other reasons.

## Rules

- Read sections, not whole chapters, except piping's new LOOP_INIT.
- Verify every quote and citation target exists.
- Use no machine-absolute paths.
- No tests, cargo, network, installs, or writes outside `RUN2/`.
- **Time box:** 60 minutes.
- **End your turn** with the number of AUM edits, what each covers in a few words, the non-AUM edits, the listed-only items, any question for ROOT, and the output's sha256.
