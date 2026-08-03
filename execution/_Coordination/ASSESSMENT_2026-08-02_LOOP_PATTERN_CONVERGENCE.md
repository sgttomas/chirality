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

## Fan-in watch-list (session context worth persisting)

- All four dev loops branched from the same main (`97678a841`); at fan-in,
  check shared surfaces for quiet collisions: `agents/`, `init/`, exports,
  entrypoint validator.
- The piping loop's runtime-needs response is the critical path: it fires
  TM-ROOT-105/109 and gates the generic-contract workstream and App's
  deferred rows downstream of the product-delivery direction.
- Root's ~20 mirror rows with fired triggers (App dispositions landed after
  root's last review) await the next root TM pass.
