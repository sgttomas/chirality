# Run Manifest — ROOT-HARNESS-46-PIN-20260726

## Identity

- Parent: `HELP_HUMAN` (Agent 0)
- Manager: `HELPS_HUMANS` (Agent 1)
- Specialist: one read-only ephemeral Agent 2 adversarial reviewer
- Accepted instruction basis:
  `ff04694afa709856a58f9f54a79ca2056b8e0b4e`
- Project Setup candidate:
  `dd28d201b8bc7c7fb534cf6ff75817da25023120`
- Worktree: `/Users/ryan/dev/chirality-root-project-setup-del0206`
- Branch: `codex/root-project-setup-del-02-06`
- Pull request: `#369`

## Objective and evidence

PR #369's governance-harness job
`https://github.com/sgttomas/chirality/actions/runs/30238988494/job/89892137423`
reported exactly three failures in
`tools/practitioner_harness/test_root_adoption.py`: the static live Root tests
still expected 45 status files after the candidate added DEL-02-06 and repinned
`execution/_harness/adapter.yaml` to 46/0.

The live candidate measurement is 46 status files, 46 matches, zero
mismatches, zero unparseable documents, and zero documents without a state
assertion. Status distribution is 45 `INITIALIZED` plus one `OPEN`. The Root
adapter continues to declare no DAG pointer.

## Runtime classification and work graph

This is an existing Agent 1 component-maintenance lane. The implementation is
deterministic static test maintenance; no new tool, skill, or dedicated
specialist is warranted. One read-only ephemeral Agent 2 adversarially reviews
scope, pins, SCC disposition, derivatives, and acceptance coverage.

1. HELPS_HUMANS reads the governing M2/G4 and live harness surfaces.
2. The read-only specialist reviews the bounded design and does not delegate.
3. HELPS_HUMANS updates only the three failing static live-root tests.
4. HELPS_HUMANS writes the G4 manifest and bounded evidence/handoff records.
5. HELPS_HUMANS validates the full harness and G0–G4 surfaces and returns to
   HELP_HUMAN for Git closeout.

There is one writer: HELPS_HUMANS. The specialist is read-only.

## Authorized writes

- `tools/practitioner_harness/test_root_adoption.py` — only the three failing
  live-root tests and their names/comments/assertions, plus the directly
  coupled module-level LIVE-tree pin summary
- `docs/governance_harness/tranche_manifests/ROOT-HARNESS-46-PIN-20260726.yaml`
- `execution/_Coordination/AgentRuns/ROOT-HARNESS-46-PIN-20260726/**`

## Prohibited changes

- Dynamic or self-updating assertions
- Practitioner-harness production behavior
- Project Setup, audit, scaffold, adapter-state, decomposition, runtime, or
  downstream-loop state
- Staging, commit, push, PR mutation, or merge

## Artifact classes

- Test change: candidate instruction-surface evidence under M2
- Tranche manifest: governed record of M2/G4 containment and dispositions
- Run records: factual execution evidence and handoff, not authority
- Existing Project Setup state: validated predecessor candidate, not authored
  or modified by this run

## Brief amendment

Agent 0 amended the sealed write boundary after the read-only adversarial
review identified the stale module-level LIVE-tree summary. The amendment
authorizes changing only that summary's stale 45/all-OPEN facts to 46 total,
45 `INITIALIZED` plus one `OPEN`, and zero mismatch. It does not authorize
production behavior or any adapter-state edit. See `BRIEF_AMENDMENT_01.md`.

## Atomic acceptance SCC

The PR #369 state and the conscious static pin are mutually coupled for
acceptance:

- `dd28d201b` without this pin fails the three live-root tests because the
  candidate measures 46 while the tests assert 45.
- This 46-file pin against `ff04694` cannot pass because that accepted base
  contains only the original 45 Root status files.

The pin must therefore be a separate commit within PR #369, while the PR is
the atomic human-gated acceptance vehicle. A standalone pin PR and a
state-only merge are both invalid.
