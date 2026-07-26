# TASK run record — D-PEC-65 register evidence repair (DEL-08-05)

| Field | Value |
|---|---|
| Date | 2026-07-25 |
| Instrument | `D-PEC-65` (RULED 2026-07-25), §2 defect basis / §3.1 repair method |
| Agent | Sealed ephemeral Agent 2 repair dispatch (file-tool-only; no Bash) |
| Package | `PKG-08_API_Access` |
| Deliverable | `DEL-08-05` SSE delta/presence subscription |
| File touched | `Dependencies.csv` (EXECUTION rows only) |

## Rows dispositioned

Register holds 5 rows: 2 ANCHOR (`DEP-08-05-001`, `DEP-08-05-002`) — read-only,
untouched — and 3 EXECUTION rows, all defect-bearing and all repaired.

| DependencyID | Class found | Disposition |
|---|---|---|
| `DEP-08-05-003` | DUP (EVQ-001) | REPAIRED |
| `DEP-08-05-004` | DUP (EVQ-001) | REPAIRED |
| `DEP-08-05-005` | EMPTY (EVQ-003 + EVQ-004) | REPAIRED |

Note: this deliverable has no accepted `ScopeOfWork.md` — it was not a
D-PEC-63 wave member (`PhaseHint` `P4`). Grounding for its rows therefore ran
against accepted decomposition truth and the accepted contract of the upstream
sibling `DEL-08-01`, never against the frozen exhibit.

## Cells changed

### `DEP-08-05-003` (→ `DEL-04-02`, EdgeID `E-P56`)

Before: `EvidenceFile` = the frozen D-PEC-62 PLAN exhibit; `SourceRef` and
`EvidenceQuote` both carried `SOW-044: "SSE subscription for deltas and
presence changes"` — a quote-shaped locus (latent EVQ-002).

After:

- `EvidenceFile` → `execution/_Decomposition/Deliverables.csv`
- `SourceRef` → `Deliverables.csv row DEL-04-02 Description`
- `EvidenceQuote` → verbatim: "Deltas since a caller-supplied commit SHA."

Warrant: the accepted deliverable register defines the upstream target as the
producer of deltas — the stream this subscription carries, which is the
`Statement`'s "Delta stream source". The seeded citation named only this
deliverable's own scope item (`SOW-044`) and so never identified the source;
the repair re-points to the source deliverable's own register row.

### `DEP-08-05-004` (→ `DEL-06-01`, EdgeID `E-P57`)

Before: exhibit `EvidenceFile`; `SourceRef` and `EvidenceQuote` both
`SOW-044 (as E-P56)` — a cross-reference to the sibling row, not a locus or a
quote.

After:

- `EvidenceFile` → `execution/_Decomposition/Deliverables.csv`
- `SourceRef` → `Deliverables.csv row DEL-06-01 Description`
- `EvidenceQuote` → verbatim: "Harness-reported session records (kind,
  engine/model attribution, role, loop/package binding, declared write
  scopes); identity/lifecycle stay daemon-owned."

Warrant: the accepted deliverable register defines the upstream target as the
producer of the session presence records whose changes this subscription
streams — the `Statement`'s "Presence-change stream source". The two seeded
rows shared one citation; the repair gives each its own distinct source
deliverable locus.

### `DEP-08-05-005` (→ `DEL-08-01`, EdgeID `E-P58`)

Before: exhibit `EvidenceFile`; `SourceRef` = `location TBD`; `EvidenceQuote`
empty.

After:

- `EvidenceFile` → `execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md`
- `SourceRef` → `Ontology section OUT-001`
- `EvidenceQuote` → verbatim: "The PEC Unix-socket server: the listener and its
  binding configuration, which expose the PKG-08 API surface on a local Unix
  domain socket as the default transport."

Warrant: the upstream target's accepted contract defines its output as the
listener exposing the PKG-08 API surface; an SSE endpoint on that surface
therefore rides it, which is the `Statement`'s claim. (The same contract's
`CLM-002` independently records `DEL-08-05` CONSUMES it via `[E-P58]`.)

## Statement edits

**None.** All three `Statement` cells carry the exhibit `Rationale` and each
states its dependency claim intelligibly; none met the §3.1 misstatement
threshold.

## Waivers declared

**None.** No `Dependencies_EvidenceWaivers.csv` was created for this
deliverable: real, verbatim, apt source text exists for all three rows.

## Integrity

No rows added, deleted, or reordered; no schema change; 29 columns preserved on
every row; ANCHOR rows byte-unchanged; all other EXECUTION cells untouched. All
three edited rows re-read after editing and confirmed column-intact.
