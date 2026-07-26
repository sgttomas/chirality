# TASK RUN — D-PEC-65 register evidence repair (DEL-00-02)

- **Date:** 2026-07-25
- **Actor:** sealed ephemeral Agent 2 (bounded generalist, file-tool-only), dispatched under
  owner-ruled packet `D-PEC-65 §3.1`; model `opus-5`.
- **Package scope of dispatch:** `execution/PKG-00_Architecture_Runway_Contracts/1_Working/`
- **Write scope (as sealed):** EXECUTION-row `SourceRef` / `EvidenceQuote` / `EvidenceFile` /
  flagged-`Statement` cells of deliverable-local `Dependencies.csv`; optional
  `Dependencies_EvidenceWaivers.csv`; this `_run_records/` file. No Bash, no git, no scripts.

## Package census

| Deliverable | Register rows | ANCHOR (read-only) | EXECUTION | Rows touched |
|---|---|---|---|---|
| DEL-00-01 (v2 first ADRs) | 2 | 2 | 0 | 0 — file untouched |
| DEL-00-02 (Event-contract schema v1) | 3 | 2 | 1 | 1 |
| DEL-00-03 (v2 SPEC seed) | 2 | 2 | 0 | 0 — file untouched |

PKG-00 carries exactly **one** EXECUTION row corpus-wide (`DEP-00-02-003`, edge `E-N18`).
DEL-00-01 and DEL-00-03 are DAG roots — the D-PEC-62 exhibit records no incoming edge for
either — so their registers hold ANCHOR rows only and were opened read-only.

## Row disposition

### `DEP-00-02-003` — class (a) locus/quote duplication → **REPAIRED**

Defect as seeded: `SourceRef` and `EvidenceQuote` both carried the exhibit's `BasisCitation`
byte-identically (EVQ-001), and that text embeds two quoted spans, so a naive EVQ-001 repair
would have unmasked EVQ-002. `EvidenceFile` pointed at the frozen D-PEC-62 PLAN exhibit,
which D-PEC-62 §3.3 rules is history-only provenance and never a cited evidence source.

Cells changed (4 of 29; all other cells byte-identical; no row added, deleted, or reordered):

| Cell | Before | After |
|---|---|---|
| `EvidenceFile` | `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` | `execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `SourceRef` | `OI-012 basis: "driving edges: PKG-07/08/09"; DEL-00-02 envelope tied to OI-009` | `§10 Open Issues — OI-012 row (Issue column)` |
| `EvidenceQuote` | (identical to the `SourceRef` value above) | verbatim contiguous span from `SOFTWARE_DECOMP.md` §10, OI-012 row — see below |
| `Statement` | `R3-F15: owner may prefer PKG-00 unordered` | see the flagged-edit section below |

Quote now cited (verbatim, contiguous, character-for-character; no reflow, no ellipsis):

> the package partition is congruent with a hexagonal grain (core: PKG-03/04/05 + PKG-01
> entities; driven edges: PKG-02/06 + store; driving edges: PKG-07/08/09); nearly all §16 open
> decisions are adapter-level, so core isolation keeps them open cheaply

Grounding and aptness. The accepted basis is `SOFTWARE_DECOMP.md` rev 1.2 (`current_basis`),
first in the packet's grounding order. §10's OI-012 row is the recorded basis of the
core-isolation question, and its own closure column states that it is *"Decided in DEL-00-01's
ADR"* — DEL-00-01 is the predecessor of this edge. The cited span carries both halves of what
the D-PEC-62 seeder was gesturing at, in one contiguous run of source text: (i) the isolation
grain places the event contracts at the **driving edges (PKG-07/08/09)** — §4 records PKG-07 as
"implementing the PKG-00 event contracts", and DEL-00-02 is that contract; and (ii) the same
ruling is what keeps the §16 adapter-level decisions cheaply open, of which **OI-009** is
DEL-00-02's own (its `ContextEnvelopeNotes` read "OI-009 keeps the contract home open"; §8
lists DEL-00-02 as an OI-coupled MEDIUM risk on exactly that ground). File, locus, and quote
name one coherent document. `SourceRef` embeds no quoted span, so EVQ-002 does not fire.

The frozen exhibit (`SEED_D-PEC-62/edges_v02.csv`, row `E-N18`) was read as provenance only,
to establish what the seeder intended; it is neither the cited `EvidenceFile` nor the source of
the quote.

## Statement edits (flagged individually, per §3.1)

**One** `Statement` edit in this package, on `DEP-00-02-003`.

- **Before:** `R3-F15: owner may prefer PKG-00 unordered`
- **After:** `DEL-00-02 depends on DEL-00-01: the ADR closing OI-012 fixes the core-isolation
  grain in which the event contracts sit at the driving edges (PKG-07/08/09), and which keeps
  DEL-00-02's open contract-home question (OI-009) adapter-level.`
- **Why the seeded text misstated the dependency claim:** the seeder wrote the exhibit's
  `Rationale` column into `Statement` (`seed_local_dependencies.py:130`). For `E-N18` that
  column held a Phase-3 refutation-round annotation — a finding ID plus a caveat *against* the
  edge — not a statement of what DEL-00-02 depends on DEL-00-01 for. It asserted no dependency
  at all, so no quote could have warranted it. The replacement states the dependency the
  accepted DAG carries. Edge strength metadata is untouched: the row remains
  `IMPLICIT` / `EXTRACTED` / `Confidence=LOW`, and `Notes` still records
  `PROPOSAL; Flag=LOW_CONFIDENCE; EdgeID=E-N18`, so the owner's open option to drop the edge
  stays visible in the register.

## Waivers declared

**None.** No `Dependencies_EvidenceWaivers.csv` was created anywhere in PKG-00: the package has
no class (b) row (empty `EvidenceQuote` with `SourceRef` = "location TBD"), and class (a) rows
are never waivable.

## Integrity checks performed

- Post-edit re-read of `DEL-00-02_Event_contract_schema_v1/Dependencies.csv`: 29 columns on
  every row; the two `EXECUTION`-row cells containing commas are double-quoted, no embedded
  double quotes required doubling; header and the two ANCHOR rows byte-unchanged.
- Row counts unchanged: 3 / 2 / 2 across the package (7 rows, 6 ANCHOR + 1 EXECUTION).
- `EvidenceFile` resolves under the validator's evidence root (`projects/pec`) to
  `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`, a regular file.
- Topology untouched: no `DependencyID`, class, target, maturity, satisfaction, confidence,
  origin, first/last-seen, status, or notes cell was modified in any file.

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MAJ-7** exactly as specified. No other cell in
this file changed.

| DependencyID | Cell | Before | After |
|---|---|---|---|
| `DEP-00-02-003` | `Statement` | `DEL-00-02 depends on DEL-00-01: the ADR closing OI-012 fixes the core-isolation grain in which the event contracts sit at the driving edges (PKG-07/08/09), and which keeps DEL-00-02's open contract-home question (OI-009) adapter-level.` | `…adapter-level.; owner may prefer PKG-00 unordered` (the string `; owner may prefer PKG-00 unordered` appended verbatim to the prior text) |

`EvidenceFile`, `SourceRef`, and `EvidenceQuote` are untouched; the evidence
repair recorded above stands unchanged.

Why: the earlier flagged `Statement` rewrite dropped the seeded routing language
(`owner may prefer PKG-00 unordered`), which records the owner's live option on
this edge's ordering. The disposition restores it by append, so both the stated
dependency claim and the routing note now stand in the same cell. The row's
`Confidence=LOW` and `Flag=LOW_CONFIDENCE` remain untouched.

**Anomaly flagged for the dispatcher:** the disposition specified a literal
append, and the prior text ends in a full stop, so the result contains the
sequence `.;`. This was applied as instructed rather than silently normalised
(removing the period would edit text the disposition did not authorise). If the
loop wants `adapter-level; owner may prefer PKG-00 unordered`, that is a
one-character follow-on act.
