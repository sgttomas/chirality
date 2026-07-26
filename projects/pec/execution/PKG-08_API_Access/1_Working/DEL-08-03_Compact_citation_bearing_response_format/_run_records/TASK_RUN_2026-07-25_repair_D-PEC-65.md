# TASK run record — D-PEC-65 register evidence repair (DEL-08-03)

| Field | Value |
|---|---|
| Date | 2026-07-25 |
| Instrument | `D-PEC-65` (RULED 2026-07-25), §2 defect basis / §3.1 repair method |
| Agent | Sealed ephemeral Agent 2 repair dispatch (file-tool-only; no Bash) |
| Package | `PKG-08_API_Access` |
| Deliverable | `DEL-08-03` Compact citation-bearing response format |
| File touched | `Dependencies.csv` (EXECUTION rows only) |

## Rows dispositioned

Register holds 4 rows: 2 ANCHOR (`DEP-08-03-001`, `DEP-08-03-002`) — read-only,
untouched — and 2 EXECUTION rows, both defect-bearing and both repaired.

| DependencyID | Class found | Disposition |
|---|---|---|
| `DEP-08-03-003` | DUP (EVQ-001) | REPAIRED |
| `DEP-08-03-004` | EMPTY (EVQ-003 + EVQ-004) | REPAIRED |

## Cells changed

### `DEP-08-03-003` (→ `DEL-08-02`, EdgeID `E-N11`)

Before: `EvidenceFile` = the frozen D-PEC-62 PLAN exhibit; `SourceRef` and
`EvidenceQuote` both carried the identical exhibit `BasisCitation` text
"SOW-042 additive versioned schema governs the response surface".

After:

- `EvidenceFile` → `execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/ScopeOfWork.md`
- `SourceRef` → `Epistemology section REQ-003` (locus only; no quoted span)
- `EvidenceQuote` → verbatim `REQ-003` sentence: "OUT-001 shall define the
  machine-consumer surface of PKG-08 so that the orientation reads OBJ-001
  describes can be issued and interpreted against a named schema version
  rather than against an undeclared shape."

Warrant: the upstream target's own accepted contract states that its schema
governs how the PKG-08 machine-consumer surface is issued and interpreted,
which is the dependency the `Statement` asserts ("envelope is schema-governed").

### `DEP-08-03-004` (→ `DEL-04-03`, EdgeID `E-P53`)

Before: `EvidenceFile` = the frozen exhibit; `SourceRef` = `location TBD`;
`EvidenceQuote` empty (the exhibit row's `BasisCitation` was empty).

After:

- `EvidenceFile` → `execution/_Decomposition/SOFTWARE_DECOMP.md` (rev 1.2
  `current_basis`)
- `SourceRef` → `§2.1 SSOW row SOW-007`
- `EvidenceQuote` → verbatim: "Attach a citation (file path, anchor, and/or
  SHA) to every claim in an orientation response"

Warrant: `SOW-007` is the scope item `DEL-04-03` covers, and its accepted
statement puts the produced citations inside the orientation response this
deliverable's envelope serializes — the dependency the `Statement` asserts.

## Statement edits

**None.** Both `Statement` cells carry the exhibit `Rationale`, but each states
the dependency claim intelligibly (`DEP-08-03-003`'s "R3-F4:" prefix is
refutation-round provenance attached to a stated claim, not a claim-free note).
No cell met the §3.1 misstatement threshold, so none was rewritten.

## Waivers declared

**None.** No `Dependencies_EvidenceWaivers.csv` was created for this
deliverable: real, verbatim, apt source text exists for both rows.

## Integrity

No rows added, deleted, or reordered; no schema change; 29 columns preserved on
every row; ANCHOR rows byte-unchanged; all other EXECUTION cells (IDs, classes,
targets, maturities, `SatisfactionStatus`, `Confidence`, `Origin`,
`FirstSeen`/`LastSeen`, `Status`, `Notes`) untouched. Both edited rows re-read
after editing and confirmed column-intact.
