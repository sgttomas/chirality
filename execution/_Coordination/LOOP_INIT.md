# Root Governance Work Loop — session init

You are resuming the root governance work loop that lives in this directory.
Its goal and recorded owner intent are selected by `CURRENT_WORKPLAN.md`.
Read that pointer and then the exact target it names. Pursue the widest lawful
tranche allowed by live authority, and stop at every human gate.

This file is orientation, not authority. Standards, decisions, accepted
snapshots, live Git state, and current human direction govern on disagreement.
Plans, receipts, and run records are derivative coordination surfaces only.

## 1. Bootstrap

- Resolve `REPO_ROOT` with `git rev-parse --show-toplevel` and work from it.
- Read root `AGENTS.md` and the instruction package for the role selected by
  the standing workplan and current human direction.
- Resolve this loop directory as `{REPO_ROOT}/execution/_Coordination`.
- Root `execution/` is the root product's execution root (D-GOV-21): the
  repository root is the root product's working root. Root `execution/` is
  **eligible** to acquire `PKG-*`/`DEL-*` structure only from an accepted root
  decomposition derived from an adopted root PRD, and only while guards G0–G4
  are registered and passing (D-GOV-21 §5.3 gate; G0 is the materialization
  fence in governance-harness CI). Until that gate closes, confirm it still
  contains control-plane records only.

## 2. Hand off to the standing plan

Read `{REPO_ROOT}/execution/_Coordination/CURRENT_WORKPLAN.md`. Resolve its
`Target` relative to `{REPO_ROOT}`, read that exact workplan, and run its Step
0 before selecting or dispatching work. Then read the newest entry in
`LOOP_RECEIPTS.md`, if any.

Do not select a workplan by filesystem modification time, directory order, or
the phrase "newest workplan" in an older derivative surface. If the pointer is
missing, malformed, escapes the repository, or names a missing file, stop and
return the defect to the human.

The standing plan records intent, protocol, constraints, gates, and source
pointers. It carries no authority merely because it exists. A receipt records
handoff context and check outcomes; it does not update governed truth.

## 3. First return

The first substantive return must state:

- current branch, worktree, clean/dirty state, and divergence from its remote;
- newest applicable root receipt and relevant App Dev/Piping loop receipts;
- live governance decisions and human directions that open or close work;
- the widest lawful lane or lanes now available;
- parked lanes and the exact owner action or accepted predecessor needed to
  release each one.

If only human decisions remain, present a decision slate and stop.

## 4. Authority and evidence discipline

- Human adoption, ruling, acceptance, and consequential direction remain human
  acts. Never manufacture or infer them.
- Re-open every cited live source before relying on a derivative claim. When a
  plan or receipt disagrees with the live source, the live source wins and the
  delta is recorded in the next receipt.
- Preserve ratified source text and historical evidence. Amend governed canon
  only through its recorded authority path.
- A commit, branch, push, PR, receipt, or generated report does not constitute
  semantic acceptance.

## 5. Multi-agent orchestration

Root `AGENTS.md` governs delegation. HELP_HUMAN is the cross-manager
supervisor; HELPS_HUMANS owns workflow-component design and implementation;
WORKING_ITEMS owns only an activated project package; RECONCILIATION owns
claim-preservation audit and corpus fan-in; SCOPE_CHANGE, REVIEW, and CHANGE
enter only at their declared gates.

Before dispatch, record the actual work graph under:

```text
execution/_Coordination/AgentRuns/<RunID>/
```

The runtime creates `<RunID>` only when a real run begins. Do not create
placeholder runs or represent briefs as executed children. Records must include
selection authority, posture, nodes, dependencies, read/write ownership,
expected returns, fan-in gates, notices, amendments, acknowledgments, child
returns, and terminal handoff state as applicable.

Use the platform's native hierarchical agent mechanism only when it preserves
sealed briefs, scopes, parentage, returns, and durable evidence equivalent to
the root doctrine. Otherwise defer the multi-agent stage or use a specifically
authorized sequential fallback. Children never bypass their parent.

Project-local child records remain in the owning project's
`execution/_Coordination/AgentRuns/`; the root run stores cross-project notices,
dispositions, and final fan-in.

## 6. Stops and write fences

The standing workplan defines the tranche-specific fences. Always stop for:

- a new or amended human ruling;
- scope expansion or substantive content change;
- lifecycle acceptance or issuance;
- unresolved authority, ownership, or shared-write conflict;
- Stage-2 authorization;
- any uncertainty about whether a change is consequential.

Root control-plane records never authorize writes to any *other* working
root's content (`projects/*`, `domains/*`). Project pilots run through their
project loops with an explicit accepted variance and path-bounded activation.
Root-product work runs through root `execution/` under D-GOV-21 and its
replacement containment contract (M1–M7, G0–G4); root-product instruction-
surface changes additionally require independent owner authorization through
a human-gated repo-wide change tranche (D-GOV-21 M2).

## 7. Closeout

After a lawful tranche:

- run the checks required by the standing workplan and affected project
  profiles;
- append one minimal receipt to `LOOP_RECEIPTS.md` containing only owner
  directions not recorded elsewhere, artifact pointers, gate outcomes, check
  summaries, and unresolved blockers;
- emit an explicit handoff naming accepted upstream state, derivative status,
  closure verdict, rerun requirements, and remaining blockers;
- use CHANGE for Git closeout; human-gated PRs are the standing default, and
  beyond that default the owner may direct merge execution — directly or by
  agent proxy — recorded in the loop's ordinary closeout evidence per PRD
  annex §5.3.1, preserving K-MERGE-1.

Any per-run steer supplied with the launcher applies on top of this protocol
but cannot override human gates or ratified governance.
