# D-PEC-42 - PROPOSAL: XLSX upload follow-on (the D-PEC-35 rider)

**Status:** AWAITING_RULING
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-42
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20/D-PEC-39 precedent.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> This is the dependency decision the standing plan **explicitly reserves to
> its own ruling** (phase corollary: "the XLSX/workbook parsing approach …
> names its approach and any dependency, and where it runs (sidecar vs
> server), in its own packet"). Source execution remains prohibited unless
> and until the owner rules this packet.

## Why this row exists

The D-PEC-35 ruling's rider made the CSV/TSV lane interim, with an "XLSX
parsing expected follow-on only after revised MDL/RAIL templates." The
revised TWD templates arrived 2026-07-09 (Receipt 75) **as `.xlsx`
workbooks** — multi-sheet, with data validation, non-header title/metadata
rows, and date cells. The owner's fidelity direction ("importing all the
data I'm providing") includes sheets a CSV export flattens or drops (Rules of
Credit, Data Dictionary, Lists, the RAIL metadata block). Native workbook
parsing is what lets the upload lane take the owner's files as provided.

## Dependencies

- D-PEC-35 agent-adaptive upload lane: landed (delivery path this extends).
- D-PEC-41 MDL/RAIL contract v2: defines the mapping targets. Execution of
  this packet should sequence with/after D-PEC-41 so parsed workbooks map to
  the v2 contract rather than v1.
- Tier-P templates: present (owner-provided TWD workbooks, Receipt 75).

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| D-PEC-35 rider reserves XLSX parsing to a follow-on ruling after the revised templates. | `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` (D-PEC-35 row) |
| The standing plan reserves the parsing approach + any dependency + where it runs to this packet; pec runtime/web stays zero-new-dependency (ADR-002 posture). | `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_reporting_product.md` (phase corollaries; R1 row) |
| The upload lane is proposal-gated: agent maps and files import proposals; accept/apply are human acts. | `projects/pec/agent-sidecar/**`; `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/FILE_DROP_RUNBOOK.md` |
| The owner's revised templates are `.xlsx` workbooks with multi-sheet structure recorded in D-PEC-41. | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-41_mdl_rail_contract_v2.md` |

## Decision to rule

Whether to authorize workbook (`.xlsx`) intake on the agent-adaptive upload
lane, and by which approach. Common scope under any approach:

1. The lane accepts `.xlsx`; the parser extracts sheets/cells (shared
   strings, inline strings, numeric and date cells with the 1900 date
   system, header-row detection per the v2 contract) into the same tabular
   representation the CSV/TSV lane maps today.
2. Everything stays proposal-gated: parse → map → import proposal → human
   accept/apply. No direct writes; parse/mapping failures are reported with
   basis, never guessed through.
3. Non-tabular sheets are carried verbatim into the full-fidelity capture
   defined by D-PEC-41.
4. Tests against fixture workbooks exercising the TWD template shapes
   (multi-sheet, offset headers, date serials, blank/placeholder rows,
   validation-only vocabulary sheets).

**Approach options (the reserved decision):**

- **O-A (recommended): zero-dependency parser in the agent sidecar.**
  `.xlsx` is ZIP + XML; the sidecar implements a minimal read-only ZIP
  reader (`node:zlib` inflate) and SpreadsheetML extraction sufficient for
  the v2 contract's shapes. Runs in the sidecar only — the pec server/web
  runtime stays untouched by parsing. Honest cost: a bounded but real
  parser (~ZIP central directory + shared strings + sheet XML + date-serial
  handling); mitigated by fixture-driven tests and by refusing (with a
  reported basis) any workbook feature it cannot faithfully read.
- **O-B: vetted parsing dependency in the sidecar only** (e.g., a
  maintained `.xlsx` reader), never in pec server/web. Less parser risk;
  breaches the zero-dependency posture in the sidecar package and takes on
  supply-chain surface — the ruling would need to name the exact package and
  version basis.
- **O-C: no native parsing** — PE keeps exporting CSV/TSV per sheet (status
  quo; the fidelity direction is then met only via manual multi-sheet
  export discipline).
- **O-D: defer.**

**Not in scope:** contract semantics (D-PEC-41); `.docx` generation (its own
reserved packet); `.xlsm` macro execution (never — macros are ignored as
content, captured only as file provenance); any write path to pec outside
the existing proposal gate.

## Fence (exact; STOP outside it)

O-A/O-B may touch only:

- `projects/pec/agent-sidecar/**` (parser, lane wiring, tests, fixtures for
  the sidecar)
- `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/**` (runbook/docs)

If the ruling selects O-B, it must also name the dependency (package +
version) it admits into the sidecar manifest. No pec `server/**`, `web/**`,
`core/**`, no tracked DB files, no other manifests.

## Verification plan (workplan step-4 bar)

- Sidecar test suite green, including the new fixture workbooks; PEC
  belt-and-braces unchanged surfaces stay green.
- Round-trip check: parsing the TWD-shaped fixtures yields exactly the
  columns/sheets recorded in D-PEC-41 — nothing dropped (fidelity
  direction), nothing invented (K-INVENT-1).
- Scope containment: `git diff --name-only` ⊆ fence; repo checks
  (self-check, coord-check on branch diff, `git diff --check`).
- Adversarial review: unreadable/unsupported workbook features refuse with a
  reported basis rather than silently degrade.

## Rollback

Single revert of the tranche commit(s); O-B additionally reverts the sidecar
manifest change.

## Human ruling

**OPEN — decision is the owner's (K-AUTH-1).** Rule O-A / O-B / O-C / O-D;
an O-B ruling names the dependency and version basis.
