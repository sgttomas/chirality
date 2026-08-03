# NOTICE — 2026-08-03 — Loop-reconnaissance findings held only in session context (TM candidates)

Coordination notice, not authority (K-TM-3/4/5: no duty, priority, or
selection effect). Owner-directed remediation session of 2026-08-03
(Receipt 86) ran a read-only reconnaissance of all four loops' init
entries via bounded subagents. The defects below were verified against
cited files but recorded nowhere durable; this notice makes them
reachable by the ordinary Task Management harvest (marker-class sweep).
Each is a candidate only; disposition belongs to the owner at triage in
the owning loop.

## Root-loop candidates

1. TM-CANDIDATE: `tools/practitioner_harness` `status` reports "No rows
   parsed" for the decision register against
   `docs/governance_harness/_DECISIONS/_REGISTER.md`, which visibly
   contains ruled rows — parser/format drift producing a silent zero
   count. A WARN finding would fit the D-GOV-02 taxonomy; silent empty
   output does not. Evidence: run `python3
   tools/practitioner_harness/harness.py status --project root` (section
   "Decision register (counts by state)").

2. TM-CANDIDATE: `tools/validation/validate_instruction_entrypoints.py`
   pins `PROJECTS = ("chirality-app-dev", "chirality-piping")` and
   byte-checks only those two dev launchers. The root (§2), bridge (§3),
   and PEC (§4) catalog entries in `init/dev-loop-init-prompt.md` and
   all four `taskmgmt-init-prompt.md` launchers are unvalidated; the
   2026-08-02/03 launcher drift class this validator exists to catch was
   found live in the uncovered files (Receipt 86 remediation).

3. TM-CANDIDATE: the root idle workplan
   (`execution/_Coordination/WORKPLAN_2026-07-27_root_idle.md`) contains
   no Step 0, while `execution/_Coordination/LOOP_INIT.md` §2 requires
   running the target workplan's Step 0 before selecting or dispatching
   work. Fold a minimal Step 0 into the successor workplan when the
   owner selects one, or amend the idle workplan.

4. TM-CANDIDATE: cross-loop wait with no root-side carrier — app-dev row
   `TM-APP-032` is DEFERRED on "Root's accepted successor identity for
   D-APP-48", but no live or archived root register row references
   D-APP-48, and root's consolidated response notice
   (`projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_ROOT_RESPONSE_DAPP84_DAPP85.md`)
   names no such identity. Either mint the root counterpart row or route
   a notice so App can re-cite its trigger to an existing root row.

## Shared-tool candidates (root register per K-AGENTS-1 tool ownership)

5. TM-CANDIDATE: `tools/taskmgmt/taskmgmt.py` `loop_of_source()` derives
   loop identity from the first two path segments, so PEC surfaces under
   `projects/pec/execution/**` attribute to a loop with no register
   while PEC's register lives at `_DomainEngines/pec/_TaskManagement/`.
   The split-home binding survives only as launcher prose
   (`projects/pec/init/taskmgmt-init-prompt.md`). A tool-level loop
   alias with tests would make the deterministic layer express what the
   prose currently patches.

6. TM-CANDIDATE: piping Step-0 ergonomics —
   `projects/chirality-piping/execution/_DAG/_LATEST.md` publishes the
   DAG pointer as a path (`execution/_DAG/DAG-009/`), while
   `tools/coordination/list_deliverable_status.py --dag` requires the
   bare name (`DAG-009`); the workplan's Step-0 command as written
   raises `FileNotFoundError` and every session silently re-derives the
   form. Accept both forms, or change what `_LATEST.md` publishes.

## Loop-owned candidates (disposition in the owning loops)

7. TM-CANDIDATE (app-dev and piping loops): both
   `projects/chirality-app-dev/loop/LOOP_INIT.md` and
   `projects/chirality-piping/loop/LOOP_INIT.md` state they restate
   nothing and "any loop can reuse it verbatim," then hardcode their own
   loop directory in the plan-loader step — the hardcoded path defeats
   the stated verbatim-reuse property. One-line rewording in each.

8. TM-CANDIDATE (piping loop): `init/piping-resume-one-time.md` is fully
   consumed (all prescribed work receipted through the D-41 R5 closeout)
   but is the only live carrier of three residuals: (a) the false "All
   pilots fable" attribution in
   `projects/chirality-piping/execution/_Reconciliation/DeliverableConcordance/D-41_.../PACKAGE_SUMMARIES/PKG-06.md`,
   `PKG-07.md`, `PKG-08.md` (W3 discovery pilots ran on opus; Receipt-25
   owner act #2(b), unrepaired); (b) the RUN_BASIS W3 pause entry naming
   the rescinded steer (owner act #2(a)); (c) the addendum-9
   frozen-evidence question — the six untracked artifact sets' worktree
   (`.claude-worktrees/`) no longer exists, and no record states whether
   they were restored or lost. Rehome all three (register rows or a
   repair tranche), then mark the prompt CONSUMED and catalog it in
   `init/dev-loop-init-prompt.md`, which currently does not list it.

Reconnaissance provenance: five bounded read-only subagent returns,
2026-08-03, fan-in validated in-session; claims above re-verified against
the cited files at `cf6bc15b9` before writing. Anything here that a later
reader finds contradicted by live files: the files govern (K-CONFLICT-1 —
surface, do not silently resolve).
