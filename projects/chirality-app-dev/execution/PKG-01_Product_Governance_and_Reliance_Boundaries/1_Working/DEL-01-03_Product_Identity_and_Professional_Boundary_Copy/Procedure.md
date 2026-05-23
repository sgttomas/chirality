# Procedure: DEL-01-03 Product Identity and Professional Boundary Copy

## Purpose

This procedure describes how to produce and use product-identity and professional-boundary copy for DEL-01-03 without inventing unsupported claims or weakening Chirality's governance posture.

## Prerequisites

- Read `_CONTEXT.md` for deliverable identity, scope, artifacts, and `ResponsibleParty: TBD`.
- Read `_REFERENCES.md` for the authoritative source corpus and hash status.
- Read `_DEPENDENCIES.md`; dependency extraction remains deferred and declared upstream/downstream dependencies are TBD.
- Read relevant source slices from:
  - `docs/DIRECTIVE.md`
  - `docs/CONTRACT.md`
  - `docs/SPEC.md`
  - `docs/TYPES.md`
  - `docs/PLAN.md`
  - `docs/PRD.md` with hash mismatch warning
  - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`

## Steps

1. Confirm stable identity.
   - Use `DEL-01-03`, `PKG-01`, and the canonical deliverable name from `_CONTEXT.md`.
   - Keep `ResponsibleParty` as `TBD` until a human assigns ownership.

2. Establish source authority.
   - Use `docs/DIRECTIVE.md` for intent, product identity, professional responsibility, evidence posture, and source hierarchy.
   - Use `docs/CONTRACT.md` for binding invariants.
   - Use `docs/PRD.md` for accepted vNext product requirements, while preserving the recorded hash-mismatch warning.

3. Draft or review product identity copy.
   - Confirm the surface names Chirality as the product.
   - Confirm SDK/provider references are implementation detail, not product identity.
   - Remove or flag copy that makes Chirality appear to be Claude Code, Anthropic, a vendor CLI, or a feature-parity target.

4. Draft or review professional-boundary copy.
   - State that agent outputs are drafts, proposals, or decision support until accepted by an accountable human.
   - Reserve approval, certification, signature, seal, issue, transmittal, release for reliance, residual-risk acceptance, and professional judgment for humans.
   - Flag copy that conflates runtime events, transcripts, validators, or generated artifacts with approval records.

5. Draft or review reliance-boundary copy.
   - Confirm product-critical boundaries are described as Chirality-owned or verified through concrete enforcement surfaces.
   - Flag statements that rely on prompt text, model behavior, or opaque SDK defaults alone for safety or authority.

6. Draft or review future domain-engine notices.
   - State that domain engines own authoritative domain truth where applicable.
   - State that Chirality governs interaction, proposals, records, and human gates.
   - State that domain-engine outputs are not Chirality-owned solver truth, code compliance, external validation, or professional approval.

7. Preserve uncertainty.
   - Mark missing target paths, owner assignments, and unsupported implementation details as `TBD`.
   - Mark inferred guidance as `ASSUMPTION`.
   - Add conflicts requiring judgment to the Conflict Table in `Guidance.md`.

8. Prepare release review evidence.
   - Record the surfaces checked.
   - Record source sections used.
   - Record any `TBD`, `ASSUMPTION`, or human-ruling-needed item.

## Verification

| Check | Pass condition |
|---|---|
| Identity check | Product-facing copy names Chirality and does not present the app as Claude Code, Anthropic, or a vendor CLI. |
| SDK framing check | SDK references are implementation/provider detail behind Chirality-owned contracts. |
| Human authority check | No copy claims automated approval, certification, issue, signature, seal, external validation, code compliance, or release for reliance. |
| Binding-record check | Drafts, proposals, summaries, transcripts, runtime events, and validator results are not described as approval records. |
| Reliance-boundary check | Product-critical boundaries are not described as prompt-only or SDK-default-only. |
| Domain-boundary check | Domain-engine notices preserve human acceptance and do not assign solver truth or professional approval to Chirality. |
| Uncertainty check | Unsupported facts remain `TBD`, `ASSUMPTION`, `PROPOSAL`, conflict, or human-ruling-needed. |

## Records

Create or maintain these records as applicable:

- UI copy guidelines: target path TBD.
- Release review checklist: target path TBD.
- Boundary notice examples: target path TBD.
- Review notes with checked surfaces and source sections: target path TBD.
- Human rulings for Conflict Table entries: TBD.

