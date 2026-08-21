# Owner direction transcript — PR #602 repair and carrier rulings

Date: `2026-08-21`

Classification: `CHAT_TRANSCRIPTION — EVIDENCE, NOT A SUBSTITUTE FOR THE OWNER ACTS IT QUOTES`

```text
OWNER DIRECTION — PR #602 repair, TM-ROOT-117 ruling, DEL-02-06 ruling (2026-08-21)

Context: PR #602 Desktop E2E has since completed success; all required checks on b2f9f1cdc are green. HELP_HUMAN byte-verification of the tranche found one defect (item 1). Review and merge remain owner acts.

1. BASIS-SHA REPAIR (BEFORE MERGE). Four committed files cite nonexistent
   commit e3e18d277a4b902e2a3347235239e90e946b91f4. The true run basis is
   e3e18d27740018efd12e73193c02395a9eca93c2. Replace every occurrence in:

   - docs/governance_harness/tranche_manifests/ROOT-TM125-AGENT0-A2-VALIDATOR-ALIGN-20260821.yaml (basis:)
   - execution/_Coordination/AgentRuns/ROOT_CROSS_LOOP_CARRIERS_2026-08-21/ORCHESTRATION_PLAN.md
   - execution/_Coordination/AgentRuns/ROOT_CROSS_LOOP_CARRIERS_2026-08-21/instances/H1-HELPS-TMROOT125/LAUNCH_BRIEF.md
   - execution/_Coordination/AgentRuns/ROOT_CROSS_LOOP_CARRIERS_2026-08-21/instances/T1-TASKMGMT-CARRIERS/LAUNCH_BRIEF.md
     Repair by ordinary commit(s) on the existing branch; no rebase, no force
     push. Re-run your required gates and bind the repair in the receipt per
     your protocol.

2. TM-ROOT-117 RULING (OWNER ACT):
   TM-ROOT-117 — APPROVE OPTION R (RE-SCOPE). CLOSE TM-ROOT-117
   RESOLVED_BY_DECISION. ROUTE A RECIPROCAL NOTICE DIRECTING APP TO REPLACE
   TM-APP-032'S TRIGGER WITH THE EXACT TEXT IN THE T1 RETURN; NO SUCCESSOR
   IDENTITY IS ACCEPTED BY THIS RULING.
   Apply on the existing branch as your protocol permits.

3. DEL-02-06 RULING (OWNER ACT):
   DEL-02-06 — SUPPLY INITIAL ROOT COMPATIBILITY EPOCH `1`, YIELDING
   CANDIDATE IDENTITY `root-runtime-1`, AND AUTHORIZE ONE SEALED
   WORKING_ITEMS ACTIVATION TO PREPARE AND VALIDATE THE EXACT
   COMPATIBILITY-COMPLETION PACKAGE AGAINST ACCEPTED SNAPSHOT
   `3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`.
   PREPARATION ONLY: DO NOT ACCEPT THE RESULTING BYTES BY INFERENCE; DO NOT
   IMPLEMENT, CHANGE LIFECYCLE, RELEASE, PUBLISH, ASSERT RELIANCE, OR WRITE
   A FOREIGN LOOP.
   Sequencing: record this ruling and update the handoff state in this
   tranche. The sealed preparation activation itself is separate work — run
   it as its own tranche/PR (this session if your protocol and remaining
   scope permit, otherwise the next Root session). Do not attach preparation
   output to PR #602. The prepared exact bytes and their SHA-256 return to
   the owner for a separate acceptance decision.

4. CLOSEOUT. Transcribe this direction as CHAT_TRANSCRIPTION. Bind the
   repair and both rulings in the receipt, then return PR #602 for owner
   review. Merge remains an owner act; no artifact-proof label; no rebase,
   force push, or branch deletion.
```

This transcript records the owner's exact direction. It does not itself
create compatibility-package bytes, accept such bytes, merge PR #602, or
grant any foreign-loop disposition.
