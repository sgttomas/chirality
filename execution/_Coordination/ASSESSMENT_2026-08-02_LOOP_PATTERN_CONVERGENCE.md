# Assessment — Work-Loop Pattern Convergence Across Locations

- **Date:** 2026-08-02
- **Status:** Decision support only. Nothing here is selected, scheduled, or
  authorized. This record creates no duty and no priority effect.
- **Author:** HELP_HUMAN session (Agent 0), recorded at owner direction.
- **Basis:** Four read-only location profiles produced in-session
  (root governance, chirality-app-dev, chirality-piping, PEC), each
  characterizing entry, discovery, planning, execution, assessment,
  integration, and closure against the same template. Profiles were
  derived from the live instruments cited below; live sources govern.

## Owner claim under assessment

The owner stated: each location executes the same prescribed loop of
development, assessment, feedback, and integration before the next
discovery/planning/development phase, bounded by PRDs, governance, and
typed loops that repeat regardless of subject.

## Finding

The claim holds at the level of loop grammar. All four locations share an
isomorphic skeleton: thin paste-ready launcher with steer slot → typed
`HELP_HUMAN` entry → `LOOP_INIT.md` as orientation-not-authority → standing
`WORKPLAN_*.md` carrying protocol and pointers but no status → deterministic
Step 0 discovery with live-source-wins → PRD-bounded scope → Agent 0/1/2
dispatch with disjoint write fences → branch-first integration with owner
merge as the gate → one minimal append-only receipt with a gate outcome.
The Task Management child loop is not merely a repeated pattern but one
shared implementation across all four registers (same schema, `taskmgmt`
archive verb, federation preflight, five-step closeout).

Subject-driven fences (root's supervisor scope and structural self-fence,
piping's F-PIP-2 claims fence, PEC's frozen reference corpus and
no-dispatch boundary) differ by design and do not count against the claim.

## Divergences — same problem, different mechanism

1. **Plan selection.** App-dev and piping share an identical committed-HEAD
   bytewise loader with blob-mode validation (`git show HEAD:<path>`,
   `LC_ALL=C` sort, mode `100644` check). Root uses a `CURRENT_WORKPLAN.md`
   pointer file with an anti-mtime rule. PEC uses "newest `WORKPLAN_*.md`
   beside `LOOP_INIT.md`" informally, readable from the worktree — the
   weakest of the three mechanisms.
2. **Receipt enforcement.** Piping and app-dev run machine validators with
   byte-capped grammar (`tools/validation/validate_piping_loop_receipts.py`,
   `tools/validation/validate_app_dev_loop_receipts.py`) before read and
   after append. Root and PEC state receipt rules in prose with no
   validator.
3. **Parallel inventions.** `projects/chirality-app-dev/execution/_Scripts/app_hold.py`
   and `projects/pec/execution/_Scripts/pec_reliance_hold.py` implement the
   same fail-closed reliance-hold concept twice. Piping's DEC-082/083/087
   and app-dev's D-APP-60/D-APP-64 are the same delegated-disposition
   apparatus evolved separately. Model attribution is mandatory in piping
   receipts (Receipt 46+), optional in app-dev, launcher-assigned in PEC,
   and unnamed at root.

## Convergence candidates (unranked options, not selections)

1. **Shared plan-loader** on the piping/app-dev committed-HEAD model,
   offered to PEC first (most exposed) and root (pointer mechanism could
   remain or adopt).
2. **Per-loop-parameterized receipt validator** extended to root and PEC.
3. **Single reliance-hold script** replacing the two parallel ones.

Each is a governance-to-code conversion in the `tools/taskmgmt/taskmgmt.py`
mold — code absorbing drift rather than new doctrine. None should move
while the 2026-08-02 dev-loop generation is in flight on shared main.

## Sequencing (owner direction, recorded verbatim in intent)

Owner, 2026-08-02: "We're going to attend to this once each dev loop has
landed." Expected re-entry: after dev-loop fan-in, these candidates enter
the next owner-triggered Task Management harvest on the owner's ruling, or
the owner directs them as a workstream outright.

## Addendum — DAG/SCC adoption assessment (same session, owner-prompted)

The owner identified a further coordination difference: piping selects work
through an approved dependency DAG (`execution/_DAG/_LATEST.md`, consumed by
its project-local `tools/coordination/list_deliverable_status.py --dag`) with
SCC resolution per `docs/CYCLE_DRIVEN_RESOLUTION.md`. Assessment of whether
the other locations could adopt it, from two read-only research passes:

- **Portable core:** the doctrine itself, `tools/coordination/audit_dag.py`
  (fully parameterized: `--edges/--nodes/--strict`), the v3.1 29-column
  `Dependencies.csv` edge schema produced by the `dependency-extract` skill,
  and the propose → SHA-freeze → owner-accept → repoint acceptance sequence.
  Piping-bound: `list_deliverable_status.py` (project-local; hardcodes
  `PKG-*/1_Working/DEL-*` layout, `_STATUS.md` header form, 5-state enum —
  conventions app-dev and PEC already share, so it ports near-unchanged).
- **App-dev: READY.** 51 deliverable-local `Dependencies.csv` in v3.1
  (byte-compatible columns); dependency closure already audited
  (`execution/_Reconciliation/DepClosure/CLOSURE_D53A_...`: 46 nodes,
  97 edges, `scc_count = 0`, 5 orphans). App-dev is also the repo's live
  SCC-resolution exemplar (`PKG-00_DAG_Closure_and_Project_Control` case
  folders) while piping's own cycle machinery is dormant since DAG-007.
  Gap is materialization only: `DeliverableNodes.csv`, a versioned
  `_DAG/DAG-001` bundle with provenance hashes, `_LATEST.md` pointer,
  approval record, ported status tool.
- **PEC: NEEDS-DATA.** 254 v3.1 edge rows (119 deliverable→deliverable)
  exist but no dependency-closure audit has ever run; acyclicity unproven.
  A DAG would subsume the hand-maintained P0→P4 tranche table and the
  redundant `PhaseHint` column. Prerequisite: closure audit first.
- **Root: STRUCTURALLY-UNSUITED, by design.** The accepted root
  decomposition declares six flat packages with no inter-package ordering;
  K-INVENT-1 forbids inferring edges. Adoption would require a scope change
  to the decomposition, not a tooling run. Pointer-and-slate selection
  remains the right mechanism for an edgeless graph.
- **Doctrine already permits adoption:** PRD_ROOT O-8 makes central graphs
  derived coordination state over authoritative deliverable-local registers,
  so adoption is materialization plus a project-local decision (piping's
  DEC-040 pattern), not new governance.
- **Shared gap for all adopters:** no SCC backlog register and no
  `--list-sccs`/`--scc <id>` tool modes exist anywhere yet (flagged unbuilt
  in piping's PLAN_2026-06-13 doctrine adoption, §3.7).

This adds a **fourth convergence candidate**: generalize
`list_deliverable_status.py` (glob/ID-grammar/state-enum as parameters) and
the DAG-surface materialization pattern; for app-dev it is plausibly the
highest-leverage of the four. Same status as the rest of this record:
decision support only, nothing selected.

## Fan-in watch-list (session context worth persisting)

- All four dev loops branched from the same main (`97678a841`); at fan-in,
  check shared surfaces for quiet collisions: `agents/`, `init/`, exports,
  entrypoint validator.
- The piping loop's runtime-needs response is the critical path: it fires
  TM-ROOT-105/109 and gates the generic-contract workstream and App's
  deferred rows downstream of the product-delivery direction.
- Root's ~20 mirror rows with fired triggers (App dispositions landed after
  root's last review) await the next root TM pass.
