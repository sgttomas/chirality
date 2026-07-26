# TASK run record — D-PEC-65 register evidence repair (DEL-08-04)

| Field | Value |
|---|---|
| Date | 2026-07-25 |
| Instrument | `D-PEC-65` (RULED 2026-07-25), §2 defect basis / §3.1 repair method |
| Agent | Sealed ephemeral Agent 2 repair dispatch (file-tool-only; no Bash) |
| Package | `PKG-08_API_Access` |
| Deliverable | `DEL-08-04` Orientation latency budget (p95 ≤ 100 ms) |
| File touched | `Dependencies.csv` (EXECUTION rows only) |

## Rows dispositioned

Register holds 6 rows: 2 ANCHOR (`DEP-08-04-001`, `DEP-08-04-002`) — read-only,
untouched — and 4 EXECUTION rows, all defect-bearing and all repaired.

| DependencyID | Class found | Disposition |
|---|---|---|
| `DEP-08-04-003` | DUP (EVQ-001) | REPAIRED |
| `DEP-08-04-004` | EMPTY (EVQ-003 + EVQ-004) | REPAIRED |
| `DEP-08-04-005` | EMPTY (EVQ-003 + EVQ-004) | REPAIRED |
| `DEP-08-04-006` | EMPTY (EVQ-003 + EVQ-004) | REPAIRED |

## Cells changed

### `DEP-08-04-003` (→ `DEL-10-01`, EdgeID `E-A28`, DECLARED stratum)

Before: `EvidenceFile` = the frozen D-PEC-62 PLAN exhibit; `SourceRef` and
`EvidenceQuote` both carried the identical exhibit `BasisCitation`
`SOW-058 note: "baselines SOW-004/041"` — a quote-shaped locus that would have
tripped EVQ-002 had EVQ-001 been repaired naively.

After:

- `EvidenceFile` → `execution/_Decomposition/SOFTWARE_DECOMP.md` (rev 1.2)
- `SourceRef` → `§2.1 SSOW row SOW-058 Notes` (locus only; no quoted span)
- `EvidenceQuote` → verbatim from that row's `Notes` cell:
  "Sequencing obligation, pre-P1; baselines SOW-004/041"

Warrant: the accepted SSOW row for `SOW-058` (the scope item `DEL-10-01`
covers) records the pre-P1 sequencing obligation and names `SOW-041` — this
deliverable's scope item — as a baselined target. That is precisely the
`Statement`'s claim, and it is the live accepted source the exhibit's
`BasisCitation` was itself pointing at.

### `DEP-08-04-004` (→ `DEL-08-03`, EdgeID `E-N12`)

Before: exhibit `EvidenceFile`; `SourceRef` = `location TBD`; `EvidenceQuote`
empty.

After:

- `EvidenceFile` → `execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md`
- `SourceRef` → `Ontology section OUT-002`
- `EvidenceQuote` → verbatim: "The serializer: the component that renders a
  composed orientation response into an instance of the OUT-001 envelope"

Warrant: the upstream target's accepted contract defines its serializer as the
component every composed orientation response passes through. An orientation
read — the act this deliverable times under `SOW-041` — therefore traverses it,
which is the `Statement`'s "sits on the measured p95 latency path". Note the
upstream contract's own `CON-001` records that no accepted source *allocates*
any part of the budget to it; this repair cites the adjacency only and asserts
no allocation.

### `DEP-08-04-005` (→ `DEL-04-01`, EdgeID `E-P51`)

Before: exhibit `EvidenceFile`; `SourceRef` = `location TBD`; `EvidenceQuote`
empty.

After:

- `EvidenceFile` → `execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md`
- `SourceRef` → `Axiology section AX-009`
- `EvidenceQuote` → verbatim: "least of all the latency budget, which tests
  this deliverable from outside under `SOW-041`"

Warrant: the upstream target's accepted contract names, in its own voice, the
`SOW-041` latency budget as testing it from outside — the strongest available
non-exhibit statement of exactly this edge.

### `DEP-08-04-006` (→ `DEL-08-01`, EdgeID `E-P52`)

Before: exhibit `EvidenceFile`; `SourceRef` = `location TBD`; `EvidenceQuote`
empty.

After:

- `EvidenceFile` → `execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md`
- `SourceRef` → `Ontology section OUT-001`
- `EvidenceQuote` → verbatim: "The PEC Unix-socket server: the listener and its
  binding configuration, which expose the PKG-08 API surface on a local Unix
  domain socket as the default transport."

Warrant: the upstream target's accepted contract defines its output as the
thing that exposes the PKG-08 API surface. "Latency measured through the API
surface" is therefore a measurement over `DEL-08-01`'s output.

## Statement edits

**None.** All four `Statement` cells carry the exhibit `Rationale`, but each
states its dependency claim intelligibly; `DEP-08-04-004`'s "R3-F4:" prefix is
refutation-round provenance attached to a stated claim, not a claim-free note.
No cell met the §3.1 misstatement threshold.

## Waivers declared

**None.** No `Dependencies_EvidenceWaivers.csv` was created for this
deliverable: real, verbatim, apt source text exists for all four rows,
including the three that were honest-empty at seeding.

## Integrity

No rows added, deleted, or reordered; no schema change; 29 columns preserved on
every row; ANCHOR rows byte-unchanged; all other EXECUTION cells untouched. All
four edited rows re-read after editing and confirmed column-intact.

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MAJ-1** exactly as specified. No other cell in
this file changed.

| DependencyID | Cell | Before | After |
|---|---|---|---|
| `DEP-08-04-005` | `EvidenceFile` | `execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md` | `docs/PRD.md` |
| `DEP-08-04-005` | `SourceRef` | `Axiology section AX-009` | `PRD.md §9.6 requirement PEC-API-002` |
| `DEP-08-04-005` | `EvidenceQuote` | `least of all the latency budget, which tests this deliverable from outside under ``SOW-041``` | `Orientation reads shall complete in ≤100 ms at p95 against the current corpus (session-start critical path).` |

Why: the superseded quote lifted a subordinate clause out of a scope-boundary
disclaimer in the upstream `ScopeOfWork.md` — a negation context, in which the
sentence's force is that the latency budget is *not* this deliverable's own work.
The replacement is the affirmative requirement of record. `Statement`,
`Explicitness`, `Confidence`, and every other cell are byte-unchanged.

**Verbatim check:** the new quote is a contiguous single-line substring of
`projects/pec/docs/PRD.md`, §9.6 API table, row `PEC-API-002`. `SourceRef` carries
no quoted span (EVQ-002 cannot fire). `EvidenceFile` / `SourceRef` /
`EvidenceQuote` name one coherent document. Row re-read post-edit: 29 columns intact.
