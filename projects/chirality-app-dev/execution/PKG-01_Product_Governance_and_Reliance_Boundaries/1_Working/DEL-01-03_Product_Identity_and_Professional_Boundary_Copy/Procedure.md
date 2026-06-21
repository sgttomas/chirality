# Procedure: DEL-01-03 Product Identity and Professional Boundary Copy

## Purpose

This procedure describes how to produce and use product-identity and professional-boundary copy for DEL-01-03 without inventing unsupported claims or weakening Chirality's governance posture.

## Prerequisites

- Read `_CONTEXT.md` for deliverable identity, scope, artifacts, and `ResponsibleParty: TBD`.
- Read `_REFERENCES.md` for the authoritative source corpus and hash status.
- Read `_DEPENDENCIES.md` and `Dependencies.csv`; dependency extraction has produced active rows, but satisfaction status remains `TBD` pending downstream FULL_GRAPH/cycle checks and human closure decisions.
- Read relevant source slices from:
  - `docs/DIRECTIVE.md`
  - `docs/CONTRACT.md`
  - `docs/SPEC.md`
  - `docs/TYPES.md`
  - `docs/PLAN.md`
  - `docs/PRD.md` under D-APP-38 corpus `v1`
  - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`

## Steps

1. Confirm stable identity.
   - Use `DEL-01-03`, `PKG-01`, and the canonical deliverable name from `_CONTEXT.md`.
   - Keep `ResponsibleParty` as `TBD` until a human assigns ownership.

2. Establish source authority.
   - Use `docs/DIRECTIVE.md` for intent, product identity, professional responsibility, evidence posture, and source hierarchy.
   - Use `docs/CONTRACT.md` for binding invariants.
   - Use `docs/PRD.md` for accepted vNext product requirements under the current D-APP-38 corpus `v1` reference state.

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
   - Record reviewer name or role, review date, pass/fail result, findings, proposed copy, and human ruling status.
   - Include authority-corpus status and Conflict Table status as explicit evidence checkpoints.

9. Route authority-sensitive wording.
   - If copy uses approve, certify, sign, seal, issue, transmit, release, externally validate, code-compliant, solver truth, or safe for reliance, record the exact phrase and route it to the accountable human or human review body.
   - If no accountable role has been assigned, record `TBD` rather than approving the wording.
   - Do not close the item until the human ruling or deferral is recorded.

## Verification

| Check | Pass condition | Evidence fields |
|---|---|---|
| Identity check | Product-facing copy names Chirality and does not present the app as Claude Code, Anthropic, or a vendor CLI. | Surface; copy excerpt; source section; pass/fail; finding ID |
| SDK framing check | SDK references are implementation/provider detail behind Chirality-owned contracts. | Surface; SDK phrase; source section; pass/fail; finding ID |
| Human authority check | No copy claims automated approval, certification, issue, signature, seal, external validation, code compliance, or release for reliance. | Surface; authority-sensitive phrase; routed-to human role; ruling status |
| Binding-record check | Drafts, proposals, summaries, transcripts, runtime events, and validator results are not described as approval records. | Record type; proposed label; source section; pass/fail |
| Reliance-boundary check | Product-critical boundaries are not described as prompt-only or SDK-default-only. | Boundary; enforcement surface if known; unsupported claims marked `TBD` |
| Domain-boundary check | Domain-engine notices preserve human acceptance and do not assign solver truth or professional approval to Chirality. | Domain surface; notice text; human-gate statement; pass/fail |
| Uncertainty check | Unsupported facts remain `TBD`, `ASSUMPTION`, `PROPOSAL`, conflict, or human-ruling-needed. | Item; label used; owner/ruling field; closure status |
| Source-status check | D-APP-38 corpus status and active Conflict Table status are visible in review evidence. | REF-006 corpus status; CT-001 status; human ruling status |

## Records

Create or maintain these records as applicable:

- UI copy guidelines: target path TBD.
- Release review checklist: target path TBD.
- Boundary notice examples: target path TBD.
- Review notes with checked surfaces and source sections: target path TBD.
- Human rulings for Conflict Table entries: TBD.
- `Dependencies.csv` satisfaction closure notes: TBD.

### Release Review Evidence Template

| Field | Value |
|---|---|
| Review ID | TBD |
| Reviewer / accountable role | TBD |
| Review date | TBD |
| Release or surface set | TBD |
| Surfaces checked | TBD |
| Source sections used | TBD |
| Authority-corpus treatment | REF-006 matches under D-APP-38 corpus `v1`; rerun reconciliation if authority docs change |
| Conflict Table status | CT-001 TBD; historical CT-002 closed by D-APP-38 corpus `v1` |
| Overall result | TBD |

### Review Note Record Template

| Field | Value |
|---|---|
| Checked surface | TBD |
| Source basis | TBD |
| Issue type | Identity / SDK framing / human authority / binding record / reliance boundary / domain boundary / uncertainty / source status |
| Current copy excerpt | TBD |
| Proposed copy | TBD |
| Finding | TBD |
| Human ruling | TBD |
