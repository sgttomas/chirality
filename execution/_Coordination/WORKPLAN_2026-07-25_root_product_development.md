# Root Governance Workplan — Root Product Development under D-GOV-21

Status: `ACTIVE — ROOT PRODUCT DEVELOPMENT`
Date: 2026-07-25
Supervising role: `HELP_HUMAN`

## Goal

Develop the root product under D-GOV-21 by executing the remaining ruled
sequence — packet §6 steps 5 through 9 — stopping at every human gate.

D-GOV-21 sequence step 3 (the implementation tranche) is complete at the
EffectiveSHA. Step 4 (root-loop reorientation) is complete when this workplan
is the standing pointer target selected by
`execution/_Coordination/CURRENT_WORKPLAN.md`. This workplan therefore opens
steps 5 and 6 as live lanes, which the packet permits to run in parallel, and
records steps 7 through 9 as gated downstream work that it does **not**
release.

## Authority basis (cited, not claimed)

This workplan is a coordination surface. It records intent, protocol,
constraints, gates, and source pointers. **It carries no authority merely
because it exists** (`execution/_Coordination/LOOP_INIT.md` §2, §4). On any
disagreement between this file and a live source, the live source governs and
the delta is recorded in the next receipt.

Governing decision:

- **D-GOV-21 — Root working-root exception and replacement containment
  contract.** Status RULED, 2026-07-25. Owner ruling of record: "I rule
  APPROVED for O-A against candidate SHA
  c038c493e871c95871823281b45890ba9404624b".
  - AcceptedCandidateSHA `c038c493e871c95871823281b45890ba9404624b`
  - PublicationSHA `75b7aa6d1fb019846ac76fb775df2fc1652ab8a8`
  - EffectiveSHA `ee42157290618e3f84be0e0b651c041387ad6ee0`
- Record:
  `docs/governance_harness/_DECISIONS/D-GOV-21_root_working_root_exception.md`
- Ruled candidate (substantive content; governs on disagreement with the
  record summary):
  `docs/governance_harness/_PROPOSALS/D-GOV-21_root-working-root-exception/PACKET.md`
  at the AcceptedCandidateSHA
- Implementation handoff:
  `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md`
- Amended doctrine in force at the EffectiveSHA: `docs/DIRECTIVE.md` §2.6,
  `docs/SPEC.md` §0.2.1–§0.3, `docs/TYPES.md` §1.4 (Annex A S1–S9), and the
  S10 rewrite of `execution/_Coordination/LOOP_INIT.md`.

What the ruling does **not** do (packet §4) remains true and constrains every
lane below: it adopts no root PRD, changes no public-export boundary, extends
the exception to no other working root, waives no part of the decomposition
pipeline, and grants no blanket authority for future root-structure changes.

## Step 0 — Preflight (run before selecting or dispatching any lane)

1. Resolve `REPO_ROOT` with `git rev-parse --show-toplevel` and work from it.
   Derive every path in this workplan `REPO_ROOT`-relative.
2. Require a synchronized `main` that contains the D-GOV-21 EffectiveSHA
   `ee42157290618e3f84be0e0b651c041387ad6ee0`. If the local `main` ref is
   behind the remote, synchronize before asserting the basis; if the
   EffectiveSHA is absent from the integration branch, stop — the basis of
   this workplan is not present.
3. Read, in this order:
   `docs/governance_harness/_DECISIONS/D-GOV-21_root_working_root_exception.md`;
   the ruled packet at the AcceptedCandidateSHA (§§4, 5, 6, 7, 11 govern the
   lanes below);
   `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md`.
   Then read the newest entry in `execution/_Coordination/LOOP_RECEIPTS.md`.
4. Run and record:
   - `python3 -m pytest tools/practitioner_harness -q` (governance-harness
     suite)
   - `python3 tools/practitioner_harness/harness.py self-check`
   - `python3 tools/validation/validate_root_materialization_fence.py` (G0)
     and `python3 -m pytest tools/validation/test_validate_root_materialization_fence.py -q`
5. **Require G0 PASS.** At this basis G0 passes idle: no `execution/PKG-*` or
   `execution/DEL-*` children exist, and none may be created by this workplan.
   A G0 BLOCK in the working checkout means materialization has occurred ahead
   of its gate — stop and return it.
6. Treat any BLOCK, or any unexplained delta between a derivative surface and
   its live source, as a **new decision request** to the owner. Do not absorb
   it silently.
7. Known accepted finding, non-gating, carried from the implementation
   tranche: self-check WARN `UNRESOLVED_SOURCE_REF` at `PACKET.md:356` — the
   packet's declined O-B option names a path that deliberately does not exist.
   The packet is the exact ruled candidate and must not be amended.

## Live lanes

Lanes A and B may run in parallel (packet §6: after step 4, steps 5 and 6 may
proceed concurrently; nothing else reorders). Each lane stops at its own named
gate. Neither lane materializes anything under root `execution/`.

### Lane A — Candidate root PRD development (packet §6 step 5)

> **Status: CLOSED 2026-07-25 by D-GOV-22.** The Rev 5 adoption-ready PRD was
> adopted by owner ruling against candidate SHA `90fae458b` (verbatim fence
> in `docs/governance_harness/_DECISIONS/D-GOV-22_root_prd_adoption.md`;
> Receipt 39). Adopted copy: `docs/PRD_ROOT.md` (RD-4-D). Follow-ons routed
> there: obligations (a)/(b)/(c), C-2/C-4 corrections. Lane B is next.

**Basis:** authorized by D-GOV-21 effect 5 — development of the candidate root
PRD is authorized on this basis. The candidate PRD may cite
root-as-working-root as **TRANSCRIBED** rather than carrying it as PROPOSED
(packet §10).

**Adoption is reserved.** PRD adoption is a separate future act on a separate
instrument (packet §11, §6 step 7). Drafting, revising, and reviewing the
candidate is in scope; adopting it is not, and no artifact produced in this
lane may present itself as adopted.

**Reserved decisions the lane must surface, never resolve.** Packet §11
expressly withholds four decisions from D-GOV-21 and routes them to the PRD
development/adoption track. This lane must surface each one to the owner as a
decision, with options and consequences, and must not settle any of them
unilaterally:

1. **Genus wording** of the root product statement.
2. **Accountability model** — one accountable human per consequential act
   versus one owner per root — *including who may amend*
   `docs/governance_harness/human_actors.md`.
3. **Adoption instrument** for the root PRD and its **concordance map**
   against `docs/DIRECTIVE.md` §1.
4. **Placement** of the adopted PRD relative to the public-export boundary
   (root `docs/` is exported; root `execution/` is not — placement is a
   publication decision).

**Gate:** the candidate PRD stops at owner review. Presenting a candidate is
the terminal act of this lane; adoption requires the separate instrument in
the gated-downstream section.

### Lane B — Guard capability G1–G4 (packet §6 step 6)

**Scope:** implement and validate the deterministic guard *capability* —
validator code plus CI wiring — for G1 through G4 as specified in packet §5.3:

- **G1 — Root harness adapter.** Root `_harness/adapter.yaml` (or equivalent
  registration) with pinned baselines, giving root `execution/` the same
  deterministic status/drift surface the project working roots have.
- **G2 — Static surface-ownership register + validator.** Validator code and
  CI wiring only in this lane; the register itself is *instantiated later*, by
  root Project Setup (gated downstream). Fails BLOCK on undeclared write
  targets, unregistered materialized packages, or register/decomposition
  mismatch. Static facts only; no concurrency claims.
- **G3 — Pre-dispatch work-graph check.** Validates at dispatch time that each
  active node's write targets are declared, that concurrently active nodes'
  targets are disjoint or serialized per M1, and that instruction-surface
  intersection carries the M2 marker.
- **G4 — Instruction-surface tranche manifest check.** Verifies manifest
  presence, path coverage of the actual diff, and the M2 gate and M6 notice
  for the tranche. Checks recorded provenance; never infers origin from diffs.

**Required preflight before G1–G4 design (packet §7, "Preflight
verification").** Run the full practitioner-harness and validation suites
against a **scratch materialization of a root `PKG-*` skeleton** to confirm the
§5.1 finding that no production harness or validator code currently guards
root `execution/` structure. Conditions:

- The scratch materialization is created **in a throwaway git worktree** and
  is **never committed** and never present in the integration branch.
- Expected and intended outcome: G0 reports BLOCK against that scratch tree,
  because `execution/PKG-*` children exist while G1–G4 are not yet registered
  and passing. That BLOCK is the fence working as designed — it is not a
  defect and is not the §5.1 finding. The §5.1 finding concerns what the
  *other* suites do and do not detect.
- Record the observed per-suite outcomes as the evidence for the finding, then
  destroy the worktree before any further work.

**Gate:** guard capability lands through a human-gated PR. G1–G4 touch
`tools/`, `.github/workflows/`, and possibly root `docs/` — the protected
instruction surface — so the tranche is an M2 governance action: independent
owner authorization, a single serialized integration owner, a tranche manifest
(the G4 discipline, applied to itself), an M6 routed notice to every project
loop that pins or mirrors the touched surfaces, and no self-merge.

## Gated downstream (not released by this workplan)

The following are recorded so the sequence is legible. **None is released
here**; each requires its named predecessor and human act.

1. **PRD adoption (packet §6 step 7, §11).** A separate instrument, adopting
   exact bytes, ruled by the owner. Requires Lane A's candidate plus owner
   resolution of the four §11 reserved decisions.
2. **First root decomposition (packet §6 step 8).** Derived from the *adopted*
   PRD only. Packet §4: nothing authorizes inventing packages from discussion.
3. **Root Project Setup (packet §6 step 8).** Instantiates the G2 ownership
   register and the first accepted work graph — G3's input. Requires guard
   capability (Lane B) to exist first; G0 enforces the ordering.
4. **Materialization of `PKG-*`/`DEL-*` under root `execution/` (packet §6
   step 9, §5.3 gate).** Permitted only from that accepted decomposition, and
   only while G0–G4 are registered, running in CI, and passing — both
   registered passing guard *capability* and instantiated guard *state*.

Until item 4's gate closes, root `execution/` holds control-plane records
only, and this workplan creates no `PKG-*`/`DEL-*` structure anywhere.

## Parked lanes and carried-forward follow-ons

These are independent of the live lanes. **None blocks Lane A or Lane B**, and
none is released by this workplan.

### Packet §7 class (b) — independent historical reconciliation

- Reconcile the missing root receipts for **D-GOV-19 and D-GOV-20** as a
  historical-reconciliation act (not required by the D-GOV-21 ruling; may run
  in parallel).
- Reconcile the **K-WRITE-2 explanatory gloss** routed as debt in packet §5.1:
  the gloss inside the K-WRITE-2 entry of `docs/CONTRACT.md` ("confines a
  task's effects to its working root") overstates the invariant's mechanical
  reach in a monorepo. Not amended by D-GOV-21; recorded for separate
  reconciliation.

### Packet §7 class (c) — conditional runtime work

- Author a root `chirality.project.json` and test project-registry containment
  with `instructionRoot` = `workingRoot` = `.` — never exercised at the
  AcceptedBasis. Required **only before runtime-backed root execution**; not a
  precondition for Lanes A or B.

### Standing follow-ons carried forward from Receipts 31–32

Carried here so the pointer move does not orphan them:

- **App Dev managed-delegation deflake.** Per the sealed brief at
  `execution/_Coordination/AgentRuns/AGENT-INDEX-REDISPOSITION-20260721/notices/APPDEV-MANAGED-DELEGATION-DEFLAKE-BRIEF.md`.
  Adoption remains the App Dev loop's own act; the root loop relays, it does
  not direct.
- **Optional strict branch-protection hardening.** Adding `Harness pre-merge`
  as a second required context, paired with an always-run no-op reporting job
  in `harness-premerge.yml` so path-filtered PRs cannot hang. Sequenced
  **after** the deflake lands — a flaky required check is a merge blocker.
  Receipt 32 records that required check `harness` (`strict: false`,
  `enforce_admins: true`) is already applied on `main`.
- **CHANGE merge-verdict standing rule.** A one-line standing rule in
  `agents/AGENT_CHANGE.md` merge semantics — inspect check verdicts explicitly
  before executing any merge; never chain a merge behind a watch. This is a
  governed agent-instruction edit and therefore an M2 instruction-surface
  tranche in its own right.

Also still parked from the predecessor workplan
(`execution/_Coordination/WORKPLAN_2026-07-15_pkg00_post_consolidation.md`,
CLOSED, immutable history): root compatibility-tool retirement (new explicit
human ruling required); the DAG successor owed by the Piping DAG-owning
workflow; PDU-007 and TP-SEAM-WASM-001 routed to REVIEW through their existing
project authority paths.

## Stop state

Every lane stops at its named human gate:

- **Lane A** stops at owner review of the candidate PRD, and stops
  additionally at each of the four packet §11 reserved decisions — which are
  surfaced, never resolved by an agent.
- **Lane B** stops at the human-gated M2 PR for guard capability, and stops
  before it at the §7 preflight if the scratch-materialization evidence
  contradicts the §5.1 finding.
- **Gated downstream** is not released at all; each item stops on its named
  predecessor plus a human act.

Beyond the lane gates, stop for anything in `LOOP_INIT.md` §6 and for any
condition the root `AGENTS.md` enumerates as **consequential**: scope
expansion, a change in consequential risk, a change in authority, an
unresolved shared-write or ownership conflict, or a change in acceptance
criteria or lifecycle acceptance. **Any uncertainty about whether one of these
conditions applies is itself returned to the owner.**

Falsifier watch (packet §9): if F1 (containment failure), F2 (loop bypass —
root product development proceeding outside this governed loop), or F3
(self-authorization — a root node consuming a capability produced by root
development before that capability was accepted) is observed, record it and
raise packet §8 rollback consideration to the owner.

## Closeout

After any lawful tranche under this workplan, follow `LOOP_INIT.md` §7: run
the checks required above plus `python3 tools/validation/validate_path_anchors.py`;
append one minimal receipt to `execution/_Coordination/LOOP_RECEIPTS.md`; emit
an explicit handoff state naming accepted upstream snapshots, derivative
status, closure verdict, rerun requirements, and remaining blockers; and use
CHANGE for Git closeout. Never self-merge.

Derivative-package note carried from the implementation handoff: public-export
staging (`exports/chirality-app`) regeneration is **DEFERRED**. Root `docs/` is
in the export allowlist and the Annex A edits stale the exported copies and
manifest hashes. Regenerate from the EffectiveSHA before any subsequent
public-export apply; do not apply an export from a pre-D-GOV-21 staging. Root
`execution/` remains outside the export allowlist (packet §4).
