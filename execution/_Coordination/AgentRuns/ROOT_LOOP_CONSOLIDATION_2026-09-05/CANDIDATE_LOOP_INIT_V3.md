# Root Governance Work Loop — session init

Orientation, not authority. Live sources govern; record disagreements in the next receipt.
Candidate pending owner ruling on the 2026-09-05 consolidation packet, items A–C.
Until accepted, read `git show origin/main:execution/_Coordination/LOOP_INIT.md`; this branch grants nothing.

## 1. Map

Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`; work from it. All paths below are repo-relative.
Read `AGENTS.md` and the selected role package (Root launcher: `agents/AGENT_HELP_HUMAN.md`).
Read `execution/_Coordination/CURRENT_WORKPLAN.md` and its exact `Target`: intent and successor selection only.
Missing, malformed, escaping, or missing-target pointers stop entry; never guess a replacement.

- Authority: `docs/PRD_ROOT.md` current document control; `docs/CONTRACT.md`; `docs/SPEC.md` §0.2; `docs/governance_harness/_DECISIONS/_REGISTER.md` and its ruling records.
- Owner steers: `plans/steers/`; reopen the applicable ruling and steer, including their basis gates and pins.
- Handoffs: `execution/_Coordination/LOOP_RECEIPTS.md`, `HANDOFF_STATE.md`, `NOTICE_*`; relevant App and Piping `loop/LOOP_RECEIPTS.md` under their `projects/chirality-*` roots.
- Attention: `execution/_Coordination/_TaskManagement/REGISTER.csv` and its cited rulings; `agents/AGENT_TASK_MANAGEMENT.md` governs disposition, never automatic harvesting on entry.
- Product: `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`, companions and `execution/_ScopeChange/_LATEST.md`; `execution/PKG-*/1_Working/DEL-*/` holds scopes, `_STATUS.md` `## Remaining`, dependencies and `_run_records/`.
- Delegation and evidence: `AGENTS.md`; actual runs at `execution/_Coordination/AgentRuns/`; empirical evidence requirements in the applicable steer (R17 N3 for v3).
- Containment and checks: `execution/_harness/` and D-GOV-21; Git closeout: `agents/AGENT_CHANGE.md` and PRD_ROOT §5.3.1.

Discover in order: owner steer of record → routed notices without a recorded disposition → register rows ruled for action → deliverable `## Remaining` items.
The first three are control-plane discovery surfaces, not automatic work grants; each action needs its own recorded authority and write scope. Product work remains deliverable-local. Empty or absent `Remaining` records no open product scope.

## 2. Limits

Owner adoption, rulings, acceptance, pointer moves and merge remain owner acts (K-AUTH-1/2).
Stop at unresolved scope, lifecycle, Stage-2, ownership, shared-write or consequential-authority gates; preserve historical and ratified bytes through their owning amendment paths.
Root records grant no foreign working-root writes; project pilots need their owning loop's accepted variance and activation. Instruction changes require independent M2 authorization and a G4 tranche manifest (D-GOV-21).
Owner acts and routed notices used to release work must be observable on fetched `origin/main`. Current chat direction permits its explicitly bounded candidate preparation, not presumed satisfaction of a merged-act gate.
A predecessor may satisfy an execution dependency on this run's branch only with its commit, passing checks and durable return, and only if the consuming item requires no owner acceptance or merged act. Ambiguous gates stay owner-class.

## 3. Protocol

### Step 0 — Discover before selection, every iteration

```bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
git fetch origin
git status --short --branch
git worktree list
git rev-parse HEAD origin/main
git rev-list --left-right --count HEAD...origin/main
cat execution/_Coordination/CURRENT_WORKPLAN.md
python3 - <<'PYREAD'
from pathlib import Path
import csv,re
root=Path.cwd(); pointer=(root/'execution/_Coordination/CURRENT_WORKPLAN.md').read_text()
targets=re.findall(r'^Target:[ \t]*\n`([^`\n]+)`[ \t]*$',pointer,re.M)
if len(targets)!=1 or len(re.findall(r'^[ \t]*Target:',pointer,re.M))!=1: raise SystemExit('BLOCK: malformed or duplicate plan pointer')
if Path(targets[0]).is_absolute(): raise SystemExit('BLOCK: target must be repo-relative')
p=(root/targets[0]).resolve()
if not p.is_relative_to(root) or not p.is_file(): raise SystemExit('BLOCK: plan target')
print(p.relative_to(root)); print(p.read_text())
s=(root/'execution/_Coordination/LOOP_RECEIPTS.md').read_text(); h=list(re.finditer(r'^### Receipt [0-9]+ .*$',s,re.M))
print(s[h[-1].start():] if h else 'No Root receipt')
for row in csv.DictReader((root/'execution/_Coordination/_TaskManagement/REGISTER.csv').open()):
 if row['Status'] in ('OPEN','DEFERRED'): print({k:row[k] for k in ('ActionItemID','Status','Disposition','Trigger','EvidenceRef')})
PYREAD
rg -n '^\| D-GOV-[0-9]+ \|' docs/governance_harness/_DECISIONS/_REGISTER.md || test "$?" -eq 1
rg --files execution/_Coordination plans/steers | rg '(NOTICE_|ruling_record|steer).*\.md$' || test "$?" -eq 1
rg -n -A 12 '^## Remaining' execution/PKG-*/1_Working/DEL-*/_STATUS.md || test "$?" -eq 1
python3 tools/practitioner_harness/harness.py status --project root
for guard in root_materialization_fence root_harness_adapter root_surface_ownership root_work_graph_dispatch instruction_tranche_manifest; do
 python3 "tools/validation/validate_${guard}.py" || exit "$?"
done
python3 tools/practitioner_harness/harness.py self-check
```

Stop on failed required commands (an empty discovery query is not a gate failure). Read the map's handoffs and relevant foreign receipts in full, then reopen cited accepted sources. Recompute relied-on pins; report stale maps rather than adopting their counts or grants. `status` does not parse Root decision rows; the register query above is necessary. Read complete selected `Remaining` sections and dependency evidence beyond the excerpt; apply `docs/CYCLE_DRIVEN_RESOLUTION.md` to cycles.

### First return

State branch, worktree, clean/dirty state, divergence and inspected main SHA; newest Root and relevant App/Piping receipts; live PRD/decomposition and lifecycle census; governing directions and check outcomes; widest lawful lanes with authority/write scope; parked lanes with exact releasing owner acts or accepted predecessors; stale-map deltas. If only owner decisions remain, present the slate and stop.

### Select, execute, close

Select the widest authorized compatible tranche from §1; verify product scope, lifecycle, named dependencies/gates, write locus, checks and return contract. Never infer scope from a notice, register status or plan. Preserve R17's deliverable engineering and evidence bar by pointer for v3 work; a blocked node holds its dependants, not independent lawful work.
Use the declared delegation mechanism and sealed scopes in `AGENTS.md`; record actual parentage, briefs and returns. Never represent an unexecuted brief as a child run.
One branch per run from `origin/main`; one receipt and commit per iteration, pushed after each closeout. Independent nodes may run concurrently with disjoint writes; dependent nodes may run in later iterations under §2. Open one PR at terminus, or when the next lawful step needs a merged act. Never self-merge.
Before closeout run Step 0 guards, affected-profile checks, `python3 tools/validation/validate_instruction_entrypoints.py`, `python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main`, `python3 tools/run_affected_tests.py --base origin/main`, and `git diff --check`; repair within authority and rerun failed checks. On committed instruction changes also run `python3 tools/validation/validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only` before push.
Append one minimal receipt using the existing ledger form; cite authority, artifacts, gates, checks and blockers. No Root receipt validator exists: inspection is manual, not a machine-enforced grammar.
Emit handoff with accepted upstream snapshots, derivative status, closure verdict, reruns and blockers; attribute model truthfully and state role-enforcement limits. Use CHANGE for scoped commit/push. Continue until only owner decisions remain, then return one PR and a decision slate.
A per-run steer may narrow or direct this protocol; it cannot supply an absent owner act or relax ratified governance. Historical citations use the section numbers at their cited Git revision.
