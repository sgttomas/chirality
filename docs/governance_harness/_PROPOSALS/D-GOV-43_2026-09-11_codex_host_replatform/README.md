# D-GOV-43 Proposal Packet — Codex Host Re-platform

Status: `PROPOSED — AWAITING OWNER RULING` (revision 2)

Date: `2026-09-11`

Prepared by: `HELP_HUMAN`, Chirality v3 Codex-only MVP trial session

Accepted preparation basis: `main@a75adecf13f055c092ffa92809f66e7817c44242`

This is a candidate governed record. It does not amend `AGENTS.md`, the
ratified standards, Runtime or App governance, product source, packaging,
installations, trial evidence, or any downstream loop. Nothing becomes active
through this packet's authorship, validation, commit, push, or review. Only an
owner ruling can adopt the decision; the coordinated application tranche it
authorizes performs the propagation.

## Packet inventory

- `D-GOV-43.proposed.md` — the decision: findings, fourteen ruling items,
  three unresolved choices, surfaces touched, gates.
- `AGENTS.proposed.patch` — the exact inactive delta to `AGENTS.md`, verified
  with `git apply --check`.
- `IMPACT.md` — affected Root, Runtime, App and PEC surfaces, the purpose test
  for every affected check and gate, trial-chat preservation, notices.
- `REVIEW_FEEDBACK_R1.md` — the round-1 independent review, verbatim, with
  each point's disposition in revision 2.
- `docs/governance_harness/tranche_manifests/ROOT-DGOV43-PROPOSAL-20260911.yaml`
  — the proposal-candidate tranche manifest.

Packet integrity is the branch's Git history. No hash table or self-hash is
maintained (review point 3).

## Owner direction of record

The owner's verbatim direction to prepare and iterate this packet is
transcribed in
`plans/steers/chirality_app_v3_codex_host_replatform_direction_2026-09-11.md`
and quoted in `D-GOV-43.proposed.md`.

## Validation posture

- The inactive patch applies cleanly with the literal command
  `git apply --check`.
- The tranche manifest validates in candidate-range mode; the agent-
  instruction and instruction-entrypoint validators pass.
- The candidate whitespace guard still runs in CI at this basis and passes;
  ruling item 11 proposes retiring it as a gate. The patch keeps its hunks
  anchored on non-blank lines only so the packet passes CI meanwhile.

Structural validation is evidence only. It is not semantic acceptance or an
owner ruling.

## What the owner is asked to rule on

Fourteen ruling items and three unresolved choices in `D-GOV-43.proposed.md`:
stock pinned App Server owned by the App host; faithful transport; a
Chirality effective Codex home with separated authentication; user-chosen
policy; continuity from Codex; Codex-native authentication; daemon
retirement; role and workflow instructions through supported mechanisms;
evidence from the full stream; roles, skills, workflows and Plan Mode;
governance simplification as a primary deliverable; the eight-check measure
of done; local models deferred; exclusions. Choices: one coordinated tranche
across loops; daemon-era trial chats read-only; residency requirements
retired.
