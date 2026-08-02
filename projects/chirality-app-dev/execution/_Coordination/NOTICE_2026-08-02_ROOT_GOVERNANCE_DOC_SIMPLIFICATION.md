# Routed Change Notice — Root governance-doc simplification

Routed by: Root loop, 2026-08-02, owner-directed governance-documentation
simplification tranche, in the spirit of the `AGENTS.md` agent-index
change-notice rule (no `agents/` files changed).

This notice is coordination, never authority. The App loop adopts,
acknowledges, amends, declines, or defers any local response through its own
instruments and cadence.

## What changed

The owner simplified the root governance-documentation surface:

- `PROFESSIONAL_ENGINEERING.md` is removed from the repository. The firm's
  professional practice standard, *Professional Engineering with Agentic AI
  in Regulated Practice*, is now maintained in the Chirality AI Ltd. quality
  management system outside this repository. The pre-relocation text remains
  in git history (last repo SHA-256
  `b07115e7933ff51280a78e3df4c16f186032aa2aa2c8433ed50ce066bcfa992b`).
  `LICENSE.md` reverted to a standard MIT license; the professional
  engineering clause was removed together with the standard it referenced.
- `CHIRALITY_FRAMEWORK.md` moved from the repository root to
  `docs/thesis/CHIRALITY_FRAMEWORK.md`, unmodified. Its operational content
  remains normatively owned by `docs/TYPES.md` §10, `docs/CONTRACT.md`, and
  `docs/DIRECTIVE.md`.
- `docs/SE_Design_Analysis.md` moved to `docs/thesis/SE_Design_Analysis.md`,
  unmodified; `docs/TYPES.md` §10.6 repoints to the new path.
- Root `README.md` was rewritten as a short orientation document (new
  SHA-256
  `cf467728c3cb3f5ca9d36b3f478a78394763820710504fcfb66da940c6d02dff`,
  superseding
  `e0a5e3e8c933e7f798e833288e52398085067d3a5e673888aa8e6fdc97014ca3`).
- `docs/thesis/bigger-picture/` moved to `plans/bigger-picture/`.
- The public export profile (`exports/chirality-app/export_public.py`) no
  longer lists `CHIRALITY_FRAMEWORK.md` or `PROFESSIONAL_ENGINEERING.md` as
  root files; the export manifest and report were regenerated with boundary
  checks passing.

## What did not change

`AGENTS.md`, all `agents/AGENT_*.md` instruction files, `skills/`, `tools/`
behavior, and all K-* invariants are untouched. The moved documents were not
edited. No lifecycle, reliance, release, or professional-judgment act is
performed by this notice or the root tranche.

## Follow-on for this loop

This loop's packaging pins root files that this tranche changed or removed:

- `frontend/package.json` `extraResources` filters
  `PROFESSIONAL_ENGINEERING.md` and `README.md` from the repository root
  into the app bundle; the former no longer exists and the latter's content
  changed.
- `frontend/src/__tests__/scripts/verify-instruction-root-integrity.test.ts`
  and any instruction-root packaging contract that asserts the presence of
  `PROFESSIONAL_ENGINEERING.md` will need amendment or a recorded decline.

Whether to drop the pin, repoint it to the firm QMS artifact, or bundle the
historical text remains an App-loop decision under its own instruments and
cadence.
