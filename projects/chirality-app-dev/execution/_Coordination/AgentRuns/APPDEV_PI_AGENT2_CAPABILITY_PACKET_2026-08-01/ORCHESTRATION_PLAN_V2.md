# Orchestration Plan V2 — D-APP-84 Proposal Amendment

RunID: `APPDEV_PI_AGENT2_CAPABILITY_PACKET_2026-08-01`
PlanVersion: `2`
SelectionAuthority: `HUMAN`, proposal-revision direction only
Posture: `MIXED`
AcceptedBasis: live uncommitted D-APP-84 proposal over `fc06b3388de17dcd5fc65eb29bf77c7f551a64cc`

ScopedDriftCheck: `origin/main@23d15899fd0acf5d1d0513f3fe396438375c9e25`
is four commits ahead of the accepted basis, but `git diff --quiet` proves no
intervening change under `AGENTS.md`, `agents/**`, `runtime/**`,
`projects/chirality-app-dev/**`, or the two governing workflow/decomposition
standards. No merge or rebase is part of proposal preparation.

1. HELPS_HUMANS rederives live Pi-native and sandbox/runtime seams.
2. Bounded read-only Agent 2 checks cover runtime capability, authority, and
   proposal-amendment convention.
3. HELPS_HUMANS revises only D-APP-84, its AWAITING_RULING row, and this RunID.
4. A fresh independent read-only adversarial review gates return.
5. HELP_HUMAN validates fan-in and presents the amended proposal to the owner.

The integration owner remains H1-HELPS_HUMANS. No child writes project content.
