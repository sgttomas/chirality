# Sealed launch/coordination brief v1

{
  "id": "/root/v3_decisions",
  "role": "bounded Agent2 decision assessment",
  "state": "PLANNED",
  "depends": [
    "/root/resume_change",
    "graph_v1_frozen",
    "fresh_preflight"
  ],
  "write_scope": [
    "this run decisions/**"
  ],
  "objective": "Read-only App contract/capability mapping and independent D121 packet review; return decision readiness/evidence, not rulings. No delegation."
}

## Common execution and return contract

Resolve REPO_ROOT with git rev-parse --show-toplevel; WORKING_ROOT={REPO_ROOT}/projects/chirality-app-dev. Read actual root role instructions and App AGENTS/LOOP_INIT. Re-derive live Remaining, accepted scope/dependency snapshots and exact synchronized APP-HOLD checks before reliance/dispatch. Historical plans are context, not a standing queue. Product source is frozen for this first increment; no feature edits. Require fresh independent review of the complete frozen product diff before final check acceptance/publication. Preserve historical failures. Any frontend change invalidates earlier A1 staging for a new login claim; fresh exact staging and owner proof are required, not implied by build success. D122/D123 feature effects remain held until their recorded main observability requirements are met. No Root/Runtime source writes, decision rulings, supplier acceptance, merges, signing, release or distribution. Significant contract/lifecycle changes return to Agent0 for the owner slate. Return claim status, identities, artifacts, checks, blockers, reruns and next owner. Native delegation is instruction-asserted; exact served model unavailable unless separately exposed, and no attribution is invented.

Basis: 28a8ed32ba83c5514ae2e65e9260833c1d46b7ef; graph WORK_GRAPH_v1.json. Planned IDs are not evidence of execution. Runtime is an independent user task, not an App child.
