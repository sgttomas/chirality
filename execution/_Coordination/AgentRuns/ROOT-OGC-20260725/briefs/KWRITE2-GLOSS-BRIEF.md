# Sealed Brief — S2: K-WRITE-2 gloss amendment (ROOT-OGC-20260725)

Issued by: `HELP_HUMAN` (Agent 0), 2026-07-25. Executor: ephemeral bounded
Agent 2 generalist, `opus-5`. One objective; no delegation; terminal return.

## Authorization

Owner ruling 2026-07-25 (verbatim in
`docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md`,
authored this tranche): the four owner-gated issues close by following
Agent 0's recommendations. You execute R3 — the K-WRITE-2 gloss debt,
routed at D-GOV-21 packet §5.1 and carried since:

> the gloss inside the K-WRITE-2 entry of `docs/CONTRACT.md` ("confines a
> task's effects to its working root") overstates the invariant's
> mechanical reach in a monorepo.

## Work

1. Read the K-WRITE-2 entry in `docs/CONTRACT.md`, the D-GOV-21 packet
   §5.1 passage that routed the debt
   (`docs/governance_harness/_PROPOSALS/D-GOV-21_root-working-root-exception/PACKET.md`),
   and D-GOV-21's ruled containment reality (declared write scopes,
   M1 fine-grained ownership, the root working-root exception where
   WORKING_ROOT == REPO_ROOT).
2. Amend ONLY the gloss prose inside the K-WRITE-2 entry so it states what
   the invariant actually delivers: write scope is DECLARED and enforced
   by review, validation, and guard checks against the declaration — not
   mechanically confined by the filesystem; in a monorepo a task's
   effects are bounded by its declared write targets (M1) rather than by
   its working root's borders, and the root product's working root IS the
   repository root (D-GOV-21). Keep the invariant's normative sentence
   itself byte-identical — the debt is the GLOSS, not the invariant. Keep
   the amendment as short as honesty allows.
3. Add the supersession trace the CONTRACT's conventions use for amended
   entries (read how other amended entries record their amending act; if
   the convention is a parenthetical citation, cite D-GOV-26 and the
   D-GOV-21 §5.1 routing).

## Constraints

- Write scope: `docs/CONTRACT.md` (the K-WRITE-2 entry's gloss only) and
  your terminal return at
  `execution/_Coordination/AgentRuns/ROOT-OGC-20260725/returns/S2_RETURN_RAW.md`.
  A sibling agent is concurrently editing `docs/SPEC.md` and
  `tools/validation/` — touch neither. No commits.
- Do not change the invariant statement, the invariant ID, the index
  count line, or any other entry. If the CONTRACT index/summary would be
  falsified by your edit (it should not be — no entry is added or
  removed), STOP and report.
- Verification (verbatim): `python3 -m pytest tools/validation -q` all
  pass; `python3 tools/validation/validate_path_anchors.py` PASS; grep
  proves the old overstating phrase no longer appears and the invariant
  sentence is unchanged; `git status --porcelain` in scope.

## Terminal return (`S2_RETURN_RAW.md`, and return the same content)

Before/after fences of the entire K-WRITE-2 entry; rationale mapping each
changed phrase to the packet §5.1 debt; verification transcript; constraint
confirmations.
