# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

| Field | Value |
|---|---|
| Deliverable | DEL-07-05 Shared-runtime client seam (v2) |
| Package | PKG-07 Event Ingest & Bridges |
| Instrument | `execution/_Coordination/_DECISIONS/D-PEC-65_register_evidence_repair.md` (RULED 2026-07-25) |
| Agent | sealed ephemeral Agent 2 (file-tool-only), `TASK-repair/D-PEC-65` |
| Files written | `Dependencies.csv` (EXECUTION evidence cells only), `Dependencies_EvidenceWaivers.csv` (created), this run record |

## Rows dispositioned

3 EXECUTION rows (all defect-bearing); 2 ANCHOR rows read-only and untouched.

| DependencyID | Class found | Disposition | EvidenceFile after |
|---|---|---|---|
| DEP-07-05-003 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/SOFTWARE_DECOMP.md` |
| DEP-07-05-004 | EMPTY (EVQ-003/-004) | WAIVED | `execution/_Decomposition/Deliverables.csv` |
| DEP-07-05-005 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/ScopeLedger.csv` |

## Cells changed

**DEP-07-05-003** (→ DEL-00-02 Event-contract schema v1)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/SOFTWARE_DECOMP.md`
- `SourceRef`: → `SOFTWARE_DECOMP.md §4 Packages table row PKG-07 (Scope Description)`
- `EvidenceQuote`: → `the shared-runtime client seam — implementing the PKG-00 event contracts`
- `Statement`: **EDITED — FLAGGED** (see below)
- Aptness: the §4 PKG-07 scope description's em-dash clause places the shared-runtime client seam among the surfaces implementing the PKG-00 event contracts, which DEL-00-02 publishes. The seeded value carried this same clause as a paraphrase-with-ellipsis in both locus and quote columns; the quote is now a verbatim contiguous span and the locus is quote-free.

**DEP-07-05-004** (→ DEL-08-02 Versioned additive API schema) — **WAIVED**
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/Deliverables.csv` (the frozen exhibit may not remain cited per D-PEC-62 §3.3; the register holding both endpoint rows is named as the document searched)
- `SourceRef`: unchanged (`location TBD`) — waived under EVQ-004
- `EvidenceQuote`: unchanged (empty) — waived under EVQ-003
- `Statement`: unchanged. It is prefixed with refutation provenance (`R3-F5:`) but does state the claim and its owner-declinable status, so it does not misstate the edge and was not rewritten.

**DEP-07-05-005** (→ DEL-01-01 Record-tier schema & entity model)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: → `ScopeLedger.csv row SOW-087 (ScopeItemStatement)`
- `EvidenceQuote`: → `Reimplement the shared-runtime client seam concept against v2 entities`
- Aptness: SOW-087 is the scope item DEL-07-05 covers; its statement is the source of the "against v2 entities" obligation, and the v2 record-tier entity model is DEL-01-01 (`Deliverables.csv` DEL-01-01, `ScopeLedger.csv` SOW-001). Explicitness stays IMPLICIT / confidence MEDIUM because the entity-model resolution is register-evident rather than stated in the quoted span.

## Statement edits (flagged)

| DependencyID | Before | After | Why |
|---|---|---|---|
| DEP-07-05-003 | `R1-F4/R3-F5: em-dash clause covers the client seam` | `DEL-07-05's client seam implements the PKG-00 event contracts published by DEL-00-02` | Seeded text was a D-PEC-62 refutation-round provenance note about which clause of §4 was read; it asserted no dependency claim at all, so it misstated the edge per D-PEC-65 §3.1. |

## Waivers declared

`Dependencies_EvidenceWaivers.csv` created with 2 rows (one dependency fully waived):

| DependencyID | WaivedCheck | Rationale summary |
|---|---|---|
| DEP-07-05-004 | EVQ-003 | No accepted source text warrants a DEL-07-05 → DEL-08-02 edge. SOW-087 and PRD §13 describe the seam only as the D-PEC-56 concept reimplemented against v2 entities; DL-11 assigns it to PKG-07 as daemon-facing integration, not as a consumer of PEC's own versioned API schema. Any quote would fabricate the link. |
| DEP-07-05-004 | EVQ-004 | No citable locus exists. Searched: SOFTWARE_DECOMP.md §4 (PKG-07/PKG-08) and §11 DL-11; ScopeLedger.csv SOW-087 and SOW-042; Deliverables.csv DEL-07-05 and DEL-08-02; PRD v2.1 §9.6 and §13; DEL-07-05/_CONTEXT.md. The row is Flag=LOW_CONFIDENCE and its Statement records that the owner may decline it. |

## Notes

- All three rows previously cited the frozen D-PEC-62 PLAN exhibit as `EvidenceFile`; all three are re-pointed away from it.
- No rows added, deleted, or reordered; 29-column schema preserved; all non-evidence cells untouched.

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MIN-3** exactly as specified. No other cell in
either file changed.

| DependencyID | File / Cell | Before | After |
|---|---|---|---|
| `DEP-07-05-004` | `Dependencies.csv` · `EvidenceFile` | `execution/_Decomposition/Deliverables.csv` | `execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `DEP-07-05-004` | `Dependencies_EvidenceWaivers.csv` · `Rationale` (`WaivedCheck=EVQ-004`) | `…naming a locus would misrepresent an unsourced inference as cited.` | `…naming a locus would misrepresent an unsourced inference as cited. EvidenceFile names SOFTWARE_DECOMP.md as the primary searched document whose DL-11 line records the counter-evidence; it is not a warranting source.` |

`SourceRef` stays `location TBD` and `EvidenceQuote` stays empty — both remain
waived under EVQ-004 / EVQ-003 respectively. The `EVQ-003` waiver row is
untouched.

Why: the waived row pointed `EvidenceFile` at `Deliverables.csv` while the EVQ-003
rationale states that file contains nothing relevant to the edge — an internal
contradiction between the cited file and the recorded reason for waiving. The
file now names `SOFTWARE_DECOMP.md`, whose DL-11 line is the actual recorded
counter-evidence (it assigns SOW-087 to PKG-07 as daemon-facing integration, not
as a consumer of the versioned API schema), and the EVQ-004 rationale states
explicitly that this is the primary searched document, not a warranting source —
so no reader can mistake the pointer for evidence of the dependency.

**Integrity:** waiver sidecar still holds exactly 2 rows for the one fully-waived
dependency (`EVQ-003` + `EVQ-004`), `DeclaredBy` = `TASK-repair/D-PEC-65`,
`DeclaredOn` = `2026-07-25`, both rationales well over the EVQ-008 length floor.
Both files re-read post-edit: 29 columns on every `Dependencies.csv` row, 5 on
every waiver row.

## E-N13 decline (D-PEC-66, 2026-07-26)

Sealed Agent 2 dispatch (file-tool-only) under
`execution/_Coordination/_DECISIONS/D-PEC-66_post_repair_followons.md` act 1
(RULED 2026-07-26). Recorded here rather than in a new run-record file so that
the full lifecycle of `DEP-07-05-004` — seeded (D-PEC-62), waived (D-PEC-65),
declined (D-PEC-66) — reads in one place. Files written: `Dependencies.csv`,
`Dependencies_EvidenceWaivers.csv`, `_DEPENDENCIES.md`, this record.

**Ruling basis:** repair-time evidence search under `D-PEC-65` found no
warranting source text for the DEL-07-05 → DEL-08-02 edge, and
SOFTWARE_DECOMP `DL-11` supplies counter-evidence (SOW-087 assigned to PKG-07
as daemon-facing integration, not as a consumer of PEC's own versioned API
schema). The row was seeded PROPOSAL / LOW_CONFIDENCE and its own `Statement`
recorded that the owner may decline.

### 1. `Dependencies.csv` — row deleted

Row `DEP-07-05-004` (EXECUTION, edge `E-N13`) removed. Former content, verbatim
and complete, for rollback readability:

```csv
v3.1,DEP-07-05-004,PKG-07,DEL-07-05,Shared-runtime client seam (v2),EXECUTION,NOT_APPLICABLE,UPSTREAM,PREREQUISITE,DELIVERABLE,PKG-08,DEL-08-02,DEL-08-02,Versioned additive API schema,execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema,R3-F5: a client seam is a client of the versioned API surface; owner may decline,execution/_Decomposition/SOFTWARE_DECOMP.md,location TBD,,IMPLICIT,INITIALIZED,TBD,PENDING,LOW,EXTRACTED,2026-07-25,2026-07-25,ACTIVE,PROPOSAL; Flag=LOW_CONFIDENCE; EdgeID=E-N13
```

Post-state: 4 data rows (2 ANCHOR `DEP-07-05-001/-002`, 2 EXECUTION
`DEP-07-05-003/-005`) plus header; no other row, cell, or byte changed; no
reordering; no renumbering of the surviving IDs (the `-004` identifier is
retired, not reused). Re-read post-edit: 29 columns on every remaining row.

### 2. `Dependencies_EvidenceWaivers.csv` — waivers retired

Both `DEP-07-05-004` waiver rows (`EVQ-003`, `EVQ-004`, declared by
`TASK-repair/D-PEC-65` on 2026-07-25 and revised the same day) are retired with
the edge they justified. The file now holds the header line only:

```csv
DependencyID,WaivedCheck,Rationale,DeclaredBy,DeclaredOn
```

The rationale text remains preserved above in this record's *Waivers declared*
and *Revision* sections. Removal of the now-empty sidecar file is the
dispatcher's recorded act at fan-in (this dispatch cannot delete files).

### 3. `_DEPENDENCIES.md` — derivative restatement annotated

The upstream table's `E-N13` row was removed from the live rows and replaced by
an explicit declined marker below the table (annotated, never silently dropped).

Before (table rows, in order):

```markdown
| DEL-00-02 (Event-contract schema v1) | DERIVED | CONSUMES |  | E-N01 |
| DEL-08-02 (Versioned additive API schema) | PROPOSAL | CONSUMES | LOW_CONFIDENCE | E-N13 |
| DEL-01-01 (Record-tier schema & entity model) | PROPOSAL | CONSUMES |  | E-P14 |
```

After:

```markdown
| DEL-00-02 (Event-contract schema v1) | DERIVED | CONSUMES |  | E-N01 |
| DEL-01-01 (Record-tier schema & entity model) | PROPOSAL | CONSUMES |  | E-P14 |

**DECLINED 2026-07-26 by owner ruling (D-PEC-66 act 1)** — DEL-08-02
(Versioned additive API schema), edge `E-N13`, register row `DEP-07-05-004`
(seeded PROPOSAL / LOW_CONFIDENCE): repair-time evidence search (`D-PEC-65`)
found no warranting source text and SOFTWARE_DECOMP `DL-11` supplies
counter-evidence (the client seam is daemon-facing integration, not a consumer
of PEC's own versioned API schema). Register row `DEP-07-05-004` removed and
its two evidence waivers retired.
```

Sections *Non-gating constraints and register-wide rules* and *Blocker
semantics* untouched.

### Rollback

Restoring the edge means re-inserting the verbatim CSV row above between
`DEP-07-05-003` and `DEP-07-05-005`, restoring the two waiver rows from the
*Waivers declared* / *Revision* sections above, and reverting the
`_DEPENDENCIES.md` table to the *Before* block.
