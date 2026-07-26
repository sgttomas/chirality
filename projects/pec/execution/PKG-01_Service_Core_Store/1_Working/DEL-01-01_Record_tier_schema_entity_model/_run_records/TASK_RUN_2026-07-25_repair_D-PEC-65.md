# TASK_RUN 2026-07-25 — D-PEC-65 register evidence repair (DEL-01-01)

- **Packet:** `execution/_Coordination/_DECISIONS/D-PEC-65_register_evidence_repair.md` (RULED 2026-07-25, §3.1 repair method)
- **Actor:** sealed ephemeral Agent 2 (file-tool-only; no Bash, no git, no scripts), model `opus-5`
- **Write scope exercised:** `Dependencies.csv` (EXECUTION-row evidence cells only) + this run record
- **Rows in file:** 3 (2 ANCHOR read-only, 1 EXECUTION)

## Row dispositions

| DependencyID | Class | Defect class found | Disposition |
|---|---|---|---|
| DEP-01-01-001 | ANCHOR | n/a (read-only) | untouched |
| DEP-01-01-002 | ANCHOR | n/a (read-only) | untouched |
| DEP-01-01-003 | EXECUTION | EVQ-001 locus/quote duplication (quote-shaped text in **both** cells; the duplicated value embedded two quoted spans, so EVQ-002 was latent) | **REPAIRED** |

## DEP-01-01-003 — cells changed

Edge `E-P01`: DEL-00-01 (v2 first ADRs) → DEL-01-01 (Record-tier schema & entity model).

- `EvidenceFile`
  - before: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` (the D-PEC-62 frozen exhibit — history only per D-PEC-62 §3.3)
  - after: `execution/_Decomposition/SOFTWARE_DECOMP.md` (rev 1.2 `current_basis`)
- `SourceRef`
  - before: `OI-012: core-isolation style "Decided in DEL-00-01's ADR"; "the one seam to keep crisp is entity schema (core) vs store persistence (adapter) inside PKG-01"`
  - after: `SOFTWARE_DECOMP.md section 10 Open Issues - OI-012 row`
  - Quote-free: contains no paired double-quote span, so the EVQ-002 `QUOTE_SPAN` test cannot fire.
- `EvidenceQuote`
  - before: byte-identical to the old `SourceRef` (the EVQ-001 defect)
  - after: `the one seam to keep crisp is entity schema (core) vs store persistence (adapter) inside PKG-01 | Decided in DEL-00-01's ADR`
  - Verbatim, contiguous, character-for-character from `SOFTWARE_DECOMP.md` §10 Open Issues, row `OI-012` (single source line). No reflow, no ellipsis, no paraphrase.

### Note on the `|` inside the quote

The span deliberately crosses the markdown table-cell delimiter of the `OI-012`
row: the *Issue* cell states the seam is "entity schema (core) vs store
persistence (adapter) inside PKG-01", and the adjacent *Owner action that closes
it* cell states it is "Decided in DEL-00-01's ADR". Only a span covering both
cells warrants the full dependency claim in `Statement` (an ADR ruling that
shapes the PKG-01 schema/persistence seam). The `|` is the literal delimiter
character present in the source line, so the span remains a verbatim contiguous
substring of the evidence file and passes a `grep -F`-equivalent check. Quoting
two separated spans joined by punctuation was rejected as non-contiguous.

## Statement edits

**None.** The seeded `Statement` ("The ADR ruling shapes the PKG-01
schema/persistence seam") states the dependency claim correctly and was left
untouched.

## Waivers declared

**None.** No waiver sidecar was created for this deliverable; real quotable
evidence exists in accepted decomposition truth.

## Untouched

All other cells (IDs, classes, targets, maturities, `SatisfactionStatus`,
`Confidence`, `Origin`, `FirstSeen`/`LastSeen`, `Status`, `Notes`). No rows
added, deleted, or reordered; 29 columns preserved (re-read and verified after
the edit).

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MIN-1** exactly as specified. No other cell in
this file changed.

| DependencyID | Cell | Before | After |
|---|---|---|---|
| `DEP-01-01-003` | `EvidenceQuote` | `the one seam to keep crisp is entity schema (core) vs store persistence (adapter) inside PKG-01 \| Decided in DEL-00-01's ADR` | `the one seam to keep crisp is entity schema (core) vs store persistence (adapter) inside PKG-01` |

`EvidenceFile` and `SourceRef` unchanged
(`execution/_Decomposition/SOFTWARE_DECOMP.md`; `SOFTWARE_DECOMP.md section 10
Open Issues - OI-012 row`).

Why: the superseded span crossed a raw markdown table delimiter, splicing the
`Issue` cell to the `Owner action that closes it` cell and presenting two
independent cells as one run of prose. The "Note on the `|` inside the quote"
section above argued the crossing was warranted; the closure refutation ruled
otherwise, and that ruling governs. The quote is now confined to the `Issue`
cell, which by itself states the schema-vs-persistence seam the `Statement`
claims the ADR shapes.

**Verbatim check:** the new quote is a contiguous single-line substring of
`projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`, §10 Open Issues, row
`OI-012`, `Issue` column, and contains no `|`. `SourceRef` carries no quoted span.
Row re-read post-edit: 29 columns intact.
