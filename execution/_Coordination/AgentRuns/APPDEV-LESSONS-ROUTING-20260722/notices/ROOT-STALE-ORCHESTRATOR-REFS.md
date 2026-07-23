# Coordination Notice — root-surface references to the deleted AGENT_ORCHESTRATOR.md

Issued by: HELP_HUMAN, app-dev loop iteration of 2026-07-22 (Receipts 86–88)
Basis: owner in-session adoption 2026-07-22 (Ryan Tufts) routing this item to the root loop
Status: OPEN — owned by the root loop
Priority: normal

## What already happened (no root action requested here beyond the ask below)

- The root D-GOV-18 re-disposition renamed ORCHESTRATOR to PROJECT_SETUP:
  `agents/AGENT_ORCHESTRATOR.md` was deleted and `agents/AGENT_PROJECT_SETUP.md`
  now holds the charter (root PR #305). The file no longer exists on disk.
- The app-dev loop closed its follow-on iteration (LOOP_RECEIPTS Receipts
  86–88; PR #314, merge commit 92dd3c97b) and updated its own doc surfaces.
- During that iteration the practitioner-harness self-check surfaced two
  root-surface references that still name the deleted file. They land as
  `WARN | UNRESOLVED_SOURCE_REF | provenance` findings under K-PROV-1, because
  the cited path `agents/AGENT_ORCHESTRATOR.md` no longer resolves.

## This notice's ask

Two live root-surface references remain and are outside the app-dev loop's
write scope. The app-dev loop does not edit root governance files; it routes
them here.

1. `docs/governance_harness/FOUR_DOCUMENT_CONSUMER_INVENTORY.md:46` — a LIVE
   consumer inventory. The current row reads:

   > `| `agents/AGENT_ORCHESTRATOR.md` | Dispatches four-documents passes and ties Pass 3 to semantic readiness | Add feature-gated candidate support; legacy remains authoritative |`

   Because this is a live inventory of active consumers, the reference should
   be updated to point at `agents/AGENT_PROJECT_SETUP.md` (the file that now
   carries that charter). This is the straightforward repair.

2. `docs/governance_harness/_DECISIONS/D-GOV-18_agent_index_redisposition.md:28`
   — a ruled decision packet. The current line reads:

   > `Rename ORCHESTRATOR to PROJECT_SETUP (`agents/AGENT_ORCHESTRATOR.md` →`

   Here the mention of the old filename is historically correct: it records
   the rename that was ruled. Rewriting a ruled decision to erase the name of
   the file it retired would falsify the history it exists to preserve. The
   disposition of this second reference — leave it as written (accepting the
   WARN as an artifact of accurate history), annotate it without rewriting the
   ruled text, or teach the self-check to treat historical rename records as
   resolved — is the root loop's call under its own decision instruments, not
   something the app-dev loop prescribes.

## Why this matters until repaired

Until both references are dispositioned, the two WARNs persist in every
practitioner-harness self-check run. Each project loop that runs the self-check
must re-recognize them as external, root-owned noise rather than a defect in
its own package — recurring friction that the app-dev loop absorbed this
iteration and that will recur for every loop until the root loop acts.

## Authority

This is a coordination notice, not an instruction. The root loop adopts,
amends, or declines it under its own decision and review instruments.
