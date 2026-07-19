# Run Basis — SCOPED_D65_RULING_EXECUTION_2026-07-19

> **Epistemic status:** derivative execution package, not decomposition truth
> and not an independent authority. It freezes an execution graph derived
> from the owner ruling, the chronology frozen by HELP_HUMAN, and accepted
> upstream evidence. The concurrent R1A D-APP-68 transcription is not treated
> as an already-accepted upstream source.

- **Source basis:** `96563e8e09b89908e13e6b2f1f1139aca3283855`
- **Owner ruling:** “I approve recommendations 1–8.”
- **Pending governed transcription:**
  `execution/_Coordination/_DECISIONS/D-APP-68_PACKET_CONCORDANCE_RULINGS_2026-07-19.md`
- **R1A/R1B relationship:** the owner chat ruling and the chronology frozen in
  the orchestration plan are this derivative's authority. The D-APP-68 packet
  remains a concurrent R1A candidate until HELP_HUMAN accepts R1A.
- **Accepted upstream derivatives:**
  `RUN_D55_CONCORDANCE_2026-07-11_1904Z`,
  `R6_D55_BACKCHECK_2026-07-12_1903Z`, and
  `SCOPED_D65_CONCORDANCE_2026-07-19`.
- **Authority/evidence read for this freeze:** D-GOV-14 item 7; D-GOV-16;
  D-APP-56 R4-P09/P28/P32; D-APP-52 live-probe evidence; D-APP-65; D-APP-67;
  Receipt-74; the scoped package ledgers/verification; the live target
  `ScopeOfWork.md`, dependency, evidence, status, code, and test surfaces.
- **Lifecycle basis:** all affected deliverables remain `IN_PROGRESS`; no
  lifecycle transition or `Checking Approval SHA` mutation is authorized.

## Accepted source pointers

The exact accepted sources consumed by this derivative are:

- owner ruling and chronology: the 2026-07-19 owner chat act quoted above and
  `execution/_Coordination/AgentRuns/APPDEV_LOOP_2026-07-19_CONCORDANCE_RULINGS/ORCHESTRATION_PLAN.md`;
- conversion authority:
  `docs/governance_harness/_DECISIONS/D-GOV-16_deliverable_scope_of_work_stage2.md`;
- legacy-bridge retirement authority:
  `docs/governance_harness/_DECISIONS/D-GOV-14_pr188_review_closure.md`, item 7;
- already-ruled Pipeline and child-output parameters:
  `execution/_Coordination/_DECISIONS/D-APP-56_RULING_2026-07-12.md`
  and its ruled R4-P28/R4-P32 dispositions;
- PEC transport-envelope and taxonomy limits:
  `execution/_Coordination/_DECISIONS/D-APP-52_PACKET_PEC_TRANSPORT_PROPOSAL_TOOLS_2026-07-06.md`,
  `execution/_Coordination/_DECISIONS/D-APP-52_RULING_2026-07-06.md`, and
  `execution/_Coordination/_DECISIONS/D-APP-67_PACKET_SECRET_REGISTRY_REDACTION_TAXONOMY_2026-07-18.md`;
- adoption-verdict evidence: the live DEL-04-01 `ScopeOfWork.md`,
  `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md` and its two SHA-bound JSON
  summaries, plus `Evidence_CODEV-001_SDK_Probe_Record.md`;
- claim populations and proposed repair evidence:
  `SCOPED_D65_CONCORDANCE_2026-07-19/PKG_LEDGERS/PKG-{00,01,04,05,06,08}_SCOPED_LEDGER.csv`
  and `SCOPED_VERIFICATION.md`.

Repository-relative forms and the claim-to-path joins are frozen in
`REPAIR_MANIFEST.md`. Readable shorthand above does not widen or replace the
manifest's exact paths.

## Source-state rule

Every manager must re-read its listed target and cited evidence at the source
basis before writing. A material mismatch is `STALE_INPUT` and returns to
HELP_HUMAN; it is not repaired by widening the manifest. Prior scoped ledgers
and D-APP-55/R6 evidence are immutable.

## Ownership graph

`WI-PKG00-01`, `WI-PKG04`, `WI-PKG05`, `WI-PKG06`, and `WI-PKG08` have
disjoint governed targets in `REPAIR_MANIFEST.md`. Manager instance-control
files under the active AgentRuns directory are governed by their sealed
briefs and are not deliverable repairs. The package managers may execute in
parallel only after HELP_HUMAN accepts this package and seals each slice.
