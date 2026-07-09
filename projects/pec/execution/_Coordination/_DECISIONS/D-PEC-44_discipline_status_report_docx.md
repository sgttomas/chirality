# D-PEC-44 - PROPOSAL: Discipline status report (.docx) generation

**Status:** AWAITING_RULING
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-44
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-39/41/42 precedent.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> This is the second dependency decision the standing plan **explicitly
> reserves to its own ruling** (phase corollary: "the `.docx` generation
> approach … names its approach and any dependency, and where it runs
> (sidecar vs server), in its own packet"). Source execution remains
> prohibited unless and until the owner rules this packet.

## Why this row exists

The R1 `.docx` row is the owner's recurring deliverable: a template-conformant
Word draft of the weekly/aggregate discipline status report, PE-vetted and
issued **outside the app** (findings §3; workplan north star). Every
prerequisite has now landed or been resolved:

- D-PEC-36 standard reports (weekly status grouped by discipline) — landed.
- D-PEC-39 periods/coverage (issuances-this-period basis) — landed.
- D-PEC-41 contract v2 (PE-attested % complete; DISC-PCT rollup) — landed.
- Report-file placement — owner-ruled 2026-07-09 (Receipt 76, verbatim):
  gitignored `projects/pec/pilot-scratch/reports/` (created).
- Template exemplar — present in the tree (below).

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| The workplan reserves the `.docx` approach + dependency + placement to its own packet; zero-new-dependency posture governs pec runtime/web (ADR-002). | `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_reporting_product.md` (phase corollaries; R1 row) |
| A completed exemplar of the owner's report exists: `projects/pec/pilot-scratch/input/2026-07-08-Status_Report_completed.docx` (gitignored, owner-held). **Delta vs the findings:** the findings cite `2026-07-08-Disciplines_Status_Report.docx`, which is not in the tree; the live exemplar governs. | live tree; `_DomainEngines/proposals/pec/FINDINGS_2026-07-09_pec_product_interview.md` §3 |
| Exemplar structure: one `Heading1` per discipline; `Subtitle` sections Activities · Issuances this week · Needs · Risks; bullet `ListParagraph` items (narrative prose with inline % values); **no tables**. Section titles vary slightly (e.g. "Mechanical Needs", "Piping Needs"). | exemplar `word/document.xml` (structure inspected 2026-07-09) |
| Weekly report payloads, period figures, and DISC-PCT already exist server-side in the `Explain` shape with basis pointers. | `projects/pec/server/src/reports/standard.ts`; `projects/pec/server/src/services/periods.ts`; `projects/pec/server/src/services/views.ts`; `projects/pec/execution/_Coordination/REPORT_BASIS.md` |
| Reports are edited and issued outside the app; in-app storage is at most a convenience. | findings §2 (owner verbatim) |

## Decision to rule

Whether to authorize one source tranche adding a **draft-generation act** to
the agent sidecar:

1. A bound act (e.g. `report.draftDocx`) that composes a template-conformant
   `.docx` **draft** from the existing server read surfaces for a declared
   period: per discipline — Activities (in-work deliverables grouped by
   deliverable type, with attested % where present, DISC-PCT basis) ·
   Issuances this period (PER-ISSUED basis, coverage named) · Needs (open
   RAIL-borne needs; internal/client typing absent until its tranche) ·
   Risks (risk records + attested Risk-type v2 issues).
2. **Factual-or-absent in the draft**: a section with no supporting records
   renders "None recorded for this period (basis: <rule-id>)" — never
   invented narrative. The PE rewrites bullets into prose before issuing; the
   draft is a starting point, not the issued report (findings §2).
3. Output written to the owner-ruled gitignored folder
   `projects/pec/pilot-scratch/reports/` (never committed; F-PEC-3
   data-residency respected; report content never lands in this repo,
   D-PEC-01 convention). No in-app storage in this tranche.
4. Aggregate ("monthly") = the same act over a wider declared window
   (owner: any aggregate of >1 week).
5. Every figure in the draft carries its rule-id basis in a trailing
   basis note (strippable by the PE), satisfying REPORT_BASIS.
6. Tests: template-conformance (styles/sections per the exemplar structure),
   factual-or-absent rendering, period-basis naming, and a golden-file
   round-trip against a synthetic dataset. No real TWD content in fixtures.

**Approach options (the reserved decision):**

- **O-A (recommended): zero-dependency `.docx` writer in the sidecar.**
  `.docx` is ZIP + WordprocessingML; the exemplar needs only Heading1 /
  Subtitle / ListParagraph styles and plain runs. The D-PEC-42 tranche
  already proved the ZIP layer (a zero-dep reader in src, a zero-dep writer
  in test support) — the writer is promoted/extended to emit the document
  package. Runs sidecar-side only; server and web untouched.
- **O-B: vetted `.docx` dependency in the sidecar only** (the ruling names
  the exact package + version); breaches the zero-dep posture in the sidecar
  manifest and takes on supply-chain surface.
- **O-C: no `.docx` generation** — the agent drafts report text (D-PEC-36/37
  already support this); the PE pastes into the Word template manually.
- **O-D: defer.**

**Not in scope:** issuing/sending the report anywhere (PE act, outside the
app); in-app report storage (possible future convenience, its own decision);
snapshot-based week-over-week deltas; interfaces content (D-PEC-43);
template-file mutation.

## Fence (exact; STOP outside it)

O-A/O-B may touch only:

- `projects/pec/agent-sidecar/**` (writer, act, tests, synthetic fixtures)
- `projects/pec/execution/_Coordination/REPORT_BASIS.md` (draft-basis rows)

If O-B, the ruling also names the dependency admitted into the sidecar
manifest. Output files go only to gitignored `pilot-scratch/reports/`. No
`server/**`, `web/**`, `core/**` (the read surfaces it composes from already
exist), no tracked DB files, no report content in the repo.

## Verification plan (workplan step-4 bar)

Sidecar suite green incl. the new template-conformance and golden-file tests;
unchanged-surface belt-and-braces stays green; a generated draft opens clean
in Word/Pages (manual spot check recorded in the receipt); scope containment
⊆ fence; self-check / coord-check / `git diff --check`; adversarial review
(no invented narrative; every figure basis-named; absent-honest sections).

## Rollback

Single revert of the tranche commit(s); generated drafts are gitignored
working files.

## Human ruling

**OPEN — decision is the owner's (K-AUTH-1).** Rule O-A / O-B / O-C / O-D;
an O-B ruling names the dependency and version basis.
