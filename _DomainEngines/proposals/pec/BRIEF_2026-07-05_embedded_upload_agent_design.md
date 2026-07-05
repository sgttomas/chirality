# CANDIDATE design brief — PEC embedded upload agent (D-PEC-07 O-C, design-only track)

> **Epistemic status: CANDIDATE — not adopted, authorizes nothing.** Prepared
> under the D-PEC-07 O-C ruling (2026-07-05). Implementation requires owner
> adoption of this brief AND a tranche authorization opening the pec source
> fence (F-PEC-1). The §16 contracts, profile
> `operation_proposal_contract`, and ADR-002 zero-dependency posture govern.

## Goal (owner's words, D-PEC-07)

"I want the embedded agent to accept a file upload from me and take action
accordingly to update things. That's one end goal."

## Design sketch

In-app flow mirroring the proven file-drop pathway, as first-class records:

1. **Upload** — new RBAC'd route (`config.manage`) accepting a spreadsheet/
   CSV upload; stored content-addressed (SHA-256) outside the DB; size-capped.
2. **Proposal record** — an `import_proposal` record per the profile's
   operation_proposal_contract lifecycle (`draft → ready_for_review →
   accepted → rejected → applied`): source file hash, detected/declared
   contract, agent-produced mapping (reusing `IMPORT_TEMPLATES/
   IMPORT_MAPPING.md` shapes), mapped-CSV preview, dry-run report
   (accepted/updated/conflict/reject counts + row detail) computed against a
   transaction that is rolled back.
3. **Agent seam** — the mapping/dry-run step is where the agent acts. v1 can
   be deterministic (known shapes from IMPORT_MAPPING.md); an LLM-backed
   mapper slots in behind the same proposal record later without changing the
   lifecycle. The agent NEVER applies.
4. **Human accept + apply** — accepting the proposal is an RBAC'd in-app act;
   apply executes the real `importContract` in a transaction, links the
   resulting import history to the proposal, and closes it `applied`.
   `force` remains a separate explicit control, default off.
5. **Audit** — proposal + apply land in history/audit like §16 imports today.

## Prerequisite repairs riding this tranche (from D-PEC-01 evidence)

- RAIL unanchored-row idempotency: match intake rows by imported `item_id`
  on re-import (evidence-03 seam finding) so re-drops update instead of
  duplicating.
- Multi-file schedule support: accept the schedule extractor shape (see
  evidence-04 mapping) natively or via stored mapping profiles.

## Out of scope

Auto-apply, agent-initiated imports, `force=true` defaults, non-import write
actions, SSO — all unchanged. No pilot-readiness or go-live implication.

## Adoption gate

Owner adopts this brief (or amends) → TOOLMAKER-style tranche packet with
exact file fence under `projects/pec/{server,web,core}/**` + tests → owner
authorizes → implementation PR(s) with the standing belt-and-braces checks.
