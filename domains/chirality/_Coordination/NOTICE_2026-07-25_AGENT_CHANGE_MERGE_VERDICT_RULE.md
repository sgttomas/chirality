# Routed Change Notice — `agents/AGENT_CHANGE.md` merge-verdict standing rule (ROOT-CLOSEOUT-20260725)

Routed by: root loop (Agent 0, `HELP_HUMAN` posture), 2026-07-25, per the
`AGENTS.md` agent-index change-notice rule and D-GOV-21 M6. This notice is
coordination, not authority: this loop adopts, amends, or declines under its
own instruments and cadence.

## What changed

`agents/AGENT_CHANGE.md` — one sentence appended to the **Integration
coordinator** bullet (Type-1 duties): before executing any merge, CHANGE
must inspect the source branch's check verdicts explicitly (a completed
checks listing showing pass/fail per check) and must never chain a merge
behind a watch command whose final verdicts were not read.

Tranche: `ROOT-CLOSEOUT-20260725` (manifest at
`docs/governance_harness/tranche_manifests/ROOT-CLOSEOUT-20260725.yaml`;
human-gated PR; authorization = owner closeout direction 2026-07-25). The
rule was a parked follow-on pre-specified in
`execution/_Coordination/WORKPLAN_2026-07-25_root_product_development.md`
(§Standing follow-ons carried forward from Receipts 31–32).

## Why this loop is notified

The chirality domain pack pins `agents/AGENT_CHANGE.md` as source
`SRC-AGENTS-AGENT-CHANGE` (sha256-pinned in
`domains/chirality/_Sources/Source_Manifest.csv` row 37) and atomizes it by
line anchor + content hash in
`domains/chirality/_Decomposition/Domain_Ledger_Gate3_Category_Draft.csv`.
The file's sha256 changes with this tranche; line anchors at and below the
edited bullet may shift. Corpus-drift checks remain the deterministic
detection path; this notice exists so detection does not depend on them
alone.

## Follow-on for this loop (its own act, on its own cadence)

Re-pin or re-atomize `SRC-AGENTS-AGENT-CHANGE` when this loop next
processes source drift. No other `agents/` file changed in this tranche.
