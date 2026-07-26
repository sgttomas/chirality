---
amendment_id: SCA-002
doc_kind: scope_change.amendment_preview
decomp_variant: SOFTWARE
gate: 3
version: v2 (revised under round R-2b-g3; 26 findings ACCEPTED)
created: 2026-07-25
status: awaiting_gate_3_approval
scope_width: O-A
authority: D-PEC-64
basis: SOFTWARE_DECOMP.md revision 1.1 (current_basis)
basis_pins: SOFTWARE_DECOMP.md ad944a2bfa7784778afa8558d8f81762; Deliverables.csv 6d2b290b0c869fc1d51d626a1714abec; ScopeLedger.csv 49e0cff9af647e41966b7a3334641919
---

# SCA-002 — Amendment Preview (Gate 3) · v2

> **v2 revision note.** v1 was refuted by two independent refuters
> (round R-2b-g3). The byte-level mechanics were confirmed sound — one
> refuter applied the whole amendment in scratch and reproduced every
> old-text pair, the union invariant at 0, the 20+17/two-column containment,
> the §3 arithmetic, and wave-unmapped 17→0. **The defects were framing and
> calibration**, and they were mine: a false authority claim for A008, exact
> text presented as unconditional when it is contingent on the Q1/Q2 answers,
> a tautological precedent, and a warrant quote truncated at exactly the
> clause that pointed elsewhere. This version corrects all of them. Rewritten
> in place rather than appended, because no part of v1 was owner-ruled.
> Corrections logged in Part 7.

Basis pins re-verified unchanged at this revision (all three md5s match).

---

## Part 0 — Read this before approving

**The exact text in Part 2 is contingent.** A001, A002, A003b and A003d are
written for the **recommended** answers to Q1 and Q2. Any non-recommended
ruling **voids the affected exact text** — the mapping, the §3 arithmetic and
the simulation must be re-derived, re-simulated and re-presented before Gate 5
can apply anything.

Concretely: under Q1.2(b) or Q1.2(c), or under any Q1 answer introducing
`OBJ-003`/`OBJ-006`, the statement "`OBJ-003` and `OBJ-006` rows are
unchanged" becomes **false** and those §3 rows gain edits. Under Q2-N2 the
entire `OBJ-002` §3 edit **disappears** and A003d's sentence about the carried
derivation becomes false.

So: **Q1 and Q2 first, then Q5.** Q5 reads "approve as drafted, *conditional on
the Q1/Q2 recommended answers*". Any other ruling returns a revised Gate 3
package rather than proceeding to Gate 4.

---

## Part 1 — Attribution development

Method per `D-PEC-64` / intake §4: ledger `SourceRef` → the actual PRD row →
the §3 objective whose stated outcome that function serves. Every warrant is
quoted from my own read of `projects/pec/docs/PRD.md`.

### The six objectives

`OBJ-001` sub-second cited orientation · `OBJ-002` structural staleness by SHA ·
`OBJ-003` declared presence/write-scope surface · `OBJ-004` owner's one live
view · `OBJ-005` deletable at any moment without blocking · `OBJ-006`
measurable/falsifiable thesis.

### A convention that constrains the whole exercise

`OBJ-005`'s existing §3 col4 reads "SOW-010, SOW-055; **bound by C1/C2 across
all items**". The document already distinguishes *items that serve* OBJ-005
from the file-wide constraint binding that touches everything. **A posture
being constraint-like is therefore not grounds for an OBJ-005 mapping** — the
decomposition has an established place for that, and it is not the
`ObjectiveIDs` column. This cuts against several zero-dependency / locality
candidates below, and I have weighted them down rather than leaning on the
kinship.

### Register precedents (measured) — and one I withdraw

| Precedent | Mapping | Status |
|---|---|---|
| `SOW-041`, `SOW-043` → `DEL-08-03/04` | `OBJ-001` | **Valid** — PKG-08 transport members serve the orientation outcome |
| `SOW-018`, `SOW-019` (PEC-RCN-003/004) | `OBJ-002` | **Valid** — OBJ-002's register locus is the reconciler layer |
| `SOW-010` (PEC-RCN-001) | `OBJ-005` | **Valid but narrow** — about rebuild + store locality specifically |
| ~~`SOW-055` kill test → `DEL-10-02` → `OBJ-005`~~ | — | **WITHDRAWN.** `SOW-055` reads "delete the store, run representative governed workflows, nothing blocks"; `OBJ-005` reads "Everything PEC holds can be deleted at any moment without blocking any governed act". The scope item is a near-verbatim restatement of the objective, so its mapping is a tautology. It explains nothing about `SOW-025` and cannot select between candidates. Using it to give `DEL-10-03` HIGH confidence was wrong |

### Per-row attributions

| # | DEL | SOW | SourceRef | Recommended | Confidence | Ruling |
|---|---|---|---|---|---|---|
| 1 | DEL-00-01 | 088 | §13 | `OBJ-005` | **MEDIUM** | **Q1.1** |
| 2 | DEL-00-03 | 089 | §13 | `OBJ-001` | **LOW** | **Q1.2** |
| 3 | DEL-01-03 | 056 | PEC-SVC-005 | `OBJ-005` | HIGH | Q5 |
| 4 | DEL-01-05 | 052, 053 | PEC-SVC-001/002 | `OBJ-005` | **MEDIUM** | **Q1.3** |
| 5 | DEL-01-06 | 094 | §12 P2, PEC-DSH-002 | `OBJ-004` | HIGH | Q5 |
| 6 | DEL-03-06 | 054 | PEC-SVC-003 | `OBJ-005` | **MEDIUM-LOW** | **Q1.4** |
| 7 | DEL-08-01 | 003, 040 | §8, PEC-API-001 | `OBJ-001` | **MEDIUM-HIGH** | **Q1.5** |
| 8 | DEL-08-02 | 042 | PEC-API-003 | `OBJ-001` | **MEDIUM** | **Q1.6** |
| 9 | DEL-10-03 | 025 | PEC-GAT-004 | `OBJ-005` | **LOW-MEDIUM** | **Q1.7** |

Only **two** rows carry a direct, unambiguous PRD warrant and are batched into
Q5. v1 claimed six were "HIGH or MEDIUM-HIGH" — false against my own
confidence labels, and withdrawn.

### The two Q5 rows

**Row 3 · DEL-01-03 / SOW-056 — HIGH, with one clause noted.**
PEC-SVC-005 (§10:317) in full: *"The store lives at a gitignored path; the
content-minimal rule (PEC-K-10) is enforced at ingest."* The **first** clause
is the warrant — a gitignored store is exactly PEC-K-02's "gitignored and safe
to delete", and `SOW-010` already carries store-gitignoring into `OBJ-005`.
The **second** clause serves **no §3 objective**: PEC-K-10 is a
privacy/footprint invariant with no objective-level statement. The mapping
rests on clause one alone; clause two is carried unmapped inside a mapped row,
which the ledger has no way to express.

**Row 5 · DEL-01-06 / SOW-094 — HIGH.** PEC-DSH-002 (§9.7:300): *"Lifecycle
census across all registered loops' packages/deliverables, with stuck-age and
workflow-completeness views."* The loop registry is what makes "all registered
loops" resolvable; §12:348 (P2) confirms *"All five loops; Overview, census,
registers, decision slate"*. Direct service to the owner's one live view.

### The seven rows needing a per-row ruling

**Q1.1 · DEL-00-01 / SOW-088 — `OBJ-005` vs `OBJ-003`. MEDIUM.**
§13:379: *"live postures (ADR-002, ADR-014) re-cited in v2's first ADRs."*
ADR-002 is the zero-dependency core; the OI-012 core-isolation seam the ADR
settles is schema-vs-persistence, and persistence separability underwrites
PEC-K-02's deletability → `OBJ-005`. **Against it:** by the C1/C2 convention,
"zero-dependency posture" is constraint-like, and the chain to a *product
outcome* runs through two inferential steps. **Alternative `OBJ-003`:**
ADR-014 is shared-runtime agent ownership — but its effect is to keep session
ownership *out* of PEC, so it argues for absence, not service. `OBJ-005`
recommended, weakly.

**Q1.2 · DEL-00-03 / SOW-089 — the weakest in the set. LOW.**
§13:379: *"v2 SPEC is born from the decomposition."* The SPEC specifies the
whole product and serves no single outcome; its PRD anchor is about prototype
disposition, not any outcome.
- **(a) `OBJ-001`** *(recommended)* — the SPEC's primary subject is the
  orientation product. Thin but non-arbitrary.
- **(b) `OBJ-001;OBJ-002;OBJ-003;OBJ-004;OBJ-005`** — honest about a document
  that specifies everything. **Edits the `OBJ-003` §3 row**, which the drafted
  A003b says is unchanged.
- **(c) `OBJ-006`** — the SPEC makes behaviour checkable. Weakest warrant; §13
  says nothing about measurement. **Edits the `OBJ-006` §3 row.**

**Q1.3 · DEL-01-05 / SOW-052+053 — `OBJ-005`. MEDIUM** *(recalibrated from
MEDIUM-HIGH to match Q1.1's identical ADR-002 chain).*
§10:313 *"The service core has zero third-party runtime dependencies (carries
ADR-002)"*; §10:314 *"Local, single-owner posture; no external network
egress."* Both are posture/constraint statements — precisely the class the
C1/C2 convention binds file-wide rather than objective-maps. The `OBJ-005`
reading is that no external entanglement is what makes deletion clean.
**Alternative:** `OBJ-003` (local single-owner as coordination posture) —
weak. There is no strong option here; the honest range is `OBJ-005` or a
judgment that this row is closer to the intentional class than to any
objective, which O-A does not permit for an in-wave row.

**Q1.4 · DEL-03-06 / SOW-054 — `OBJ-005` vs `OBJ-002` vs both. MEDIUM-LOW.**
PEC-SVC-003 (§10:315) **in full**: *"Full rebuild of the current corpus
completes within a bound confirmed at Phase 1 (target: minutes); incremental
reconcile within seconds."*

> v1 truncated this at "(target: minutes)" — cutting it at exactly the clause
> that points somewhere else. The most consequential quoting error in the
> package.

Two clauses pointing at different objectives:
- *full rebuild within a bound* → `OBJ-005` kinship (a fast rebuild is what
  makes deletion survivable), continuous with `SOW-010`;
- *incremental reconcile within seconds* → incremental reconcile is
  SHA-delta-keyed by PEC-RCN-003, which is `SOW-018` → **`OBJ-002`**.

Options: **`OBJ-005`** *(recommended, weakly — the row is a PKG-03 performance
bound on the rebuild path)*; **`OBJ-002`**; or **`OBJ-005;OBJ-002`**, the most
faithful to the two-clause text and defensible if you prefer completeness over
minimality. **`OBJ-002` or both edits the `OBJ-002` §3 row beyond the drafted
text.**

**Q1.5 · DEL-08-01 / SOW-003+040 — `OBJ-001` vs `OBJ-001;OBJ-004`. MEDIUM-HIGH.**
§9.6:289 *"The service binds local-only, Unix socket by default, with
token-scoped access"* → `OBJ-001` via the PKG-08 transport precedent.
§8:217–219 lists *"Human owner — dashboards, decision slate, presence board.
Full read"* and *"Harnesses … machine consumers of the API on behalf of agent
sessions"*. `SOW-003`'s three access classes include **owner**, giving an
`OBJ-004` reading. `OBJ-001` alone recommended — the dashboards serving
OBJ-004 are PKG-09 deliverables that already carry it, and this row gates the
API rather than providing the view. **`OBJ-001;OBJ-004` edits the `OBJ-004`
§3 row beyond the drafted text.**

**Q1.6 · DEL-08-02 / SOW-042 — `OBJ-001` vs broader. MEDIUM.**
PEC-API-003 (§9.6:291): *"The API schema is versioned; evolution is
additive."* The textual link to any single outcome is weak: additive schema
evolution serves **every** API consumer — orientation reads (`OBJ-001`),
dashboard/census reads (`OBJ-004`) and presence subscriptions (`OBJ-003`).
`OBJ-001` is recommended only because orientation is the API's primary
consumer in §12's P1 sequencing, not because the text selects it.
Alternatives: `OBJ-001;OBJ-004`, or the full consumer set.

**Q1.7 · DEL-10-03 / SOW-025 — `OBJ-005` vs `OBJ-003` vs `OBJ-006`. LOW-MEDIUM.**
PEC-GAT-004 (§9.3:261): *"PEC shall provide no write path that records
adoption, ruling, or direction (PEC-K-02; K-AUTH-1)."*

**The honest position, now that the `SOW-055` precedent is withdrawn:** the
authority boundary K-AUTH-1 states is **not stated by any §3 objective** —
exactly the condition `DL-14` invoked to leave `SOW-063` intentionally
unmapped. If this row were out-of-wave, "intentionally unmapped" would be the
defensible answer. It is in-wave, so O-A requires a mapping, and you are
choosing the **least-wrong** objective as an explicit act rather than
discovering a warrant that exists.

- **`OBJ-005`** *(recommended)* — a system that captures no authority holds
  nothing whose deletion could block a governed act.
- **`OBJ-003`** — the declared-surface objective is the one about what PEC *is*
  to concurrent governed work.
- **`OBJ-006`** — `DEL-10-03` is a PKG-10 verification deliverable and OBJ-006
  is the measurable/falsifiable objective; against it, §11's metric list does
  not include no-ruling-write.

### The INDIRECT-8 (`DEL-01-01` + `DEL-02-01..07`) — Q2

§3's mapping notes state a positive derivation: *"parser items (SOW-011..017)
underlie OBJ-001/OBJ-002 through the record tier (SOW-001)."*

**Recommended — AFFIRM** `[OBJ-001, OBJ-002]` for all eight: it applies the
accepted §3 rationale rather than superseding it.

**Narrow options, defined precisely** (v1 said "narrow" without specifying):

| Variant | SOW-001 | SOW-011..017 | §3 `OBJ-002` col4 | §3 `OBJ-002` col5 | OBJ-002 dels |
|---|---|---|---|---|---|
| **AFFIRM** *(rec.)* | `OBJ-001;OBJ-002` | `OBJ-001;OBJ-002` | `SOW-001, SOW-006, SOW-011..019; supported by SOW-005` | `DEL-01-01, DEL-02-01..07, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03` | 12 |
| **N1** | `OBJ-001;OBJ-002` | `OBJ-001` | `SOW-001, SOW-006, SOW-018, SOW-019; supported by SOW-005` | `DEL-01-01, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03` | 5 |
| **N2** | `OBJ-001` | `OBJ-001` | *(unchanged from revision 1.1)* | *(unchanged)* | 4 |

**Consequences.** Under **N1**, seven A002 cells become `OBJ-001` and the
`OBJ-002` §3 edit shrinks. Under **N2** the `OBJ-002` §3 row is **not edited at
all** — the drafted A003b `OBJ-002` block is deleted and A003d's carried-
derivation sentence becomes false and must be rewritten. Both change
A001/A002/A003b and require re-simulation.

**Evidence for narrowing, stated because it is real:** OBJ-002's register locus
is the reconciler layer — `SOW-018` (incremental, Git-delta-keyed), `SOW-019`
(drift classification), `SOW-006` (SHA stamping). The parsers produce facts the
SHA comparison operates over; they do not perform it. N1 would arguably
describe the system more precisely than the §3 sentence does.

---

## Part 2 — Exact amendment text

**Contingent on the Q1/Q2 recommended answers** (Part 0).

### A001 — `ScopeLedger.csv`, `ObjectiveIDs`, 20 rows

All cells currently empty; only this column changes on these rows.

| SOW | new | SOW | new |
|---|---|---|---|
| 001 | `OBJ-001;OBJ-002` | 042 | `OBJ-001` |
| 003 | `OBJ-001` | 052 | `OBJ-005` |
| 011 | `OBJ-001;OBJ-002` | 053 | `OBJ-005` |
| 012 | `OBJ-001;OBJ-002` | 054 | `OBJ-005` |
| 013 | `OBJ-001;OBJ-002` | 056 | `OBJ-005` |
| 014 | `OBJ-001;OBJ-002` | 088 | `OBJ-005` |
| 015 | `OBJ-001;OBJ-002` | 089 | `OBJ-001` |
| 016 | `OBJ-001;OBJ-002` | 094 | `OBJ-004` |
| 017 | `OBJ-001;OBJ-002` | 021 | `OBJ-005` |
| 025 | `OBJ-005` | 040 | `OBJ-001` |

### A002 — `Deliverables.csv`, `SupportsObjectives`, 17 rows

Derived from A001 by the union invariant, not authored independently.

| DEL | Covers | new | DEL | Covers | new |
|---|---|---|---|---|---|
| 00-01 | 088 | `OBJ-005` | 02-03 | 013 | `OBJ-001;OBJ-002` |
| 00-03 | 089 | `OBJ-001` | 02-04 | 014 | `OBJ-001;OBJ-002` |
| 01-01 | 001 | `OBJ-001;OBJ-002` | 02-05 | 015 | `OBJ-001;OBJ-002` |
| 01-03 | 056 | `OBJ-005` | 02-06 | 016 | `OBJ-001;OBJ-002` |
| 01-05 | 052;053 | `OBJ-005` | 02-07 | 017 | `OBJ-001;OBJ-002` |
| 01-06 | 094 | `OBJ-004` | 03-06 | 054 | `OBJ-005` |
| 02-01 | 011 | `OBJ-001;OBJ-002` | 08-01 | 003;040 | `OBJ-001` |
| 02-02 | 012 | `OBJ-001;OBJ-002` | 08-02 | 042 | `OBJ-001` |
| | | | 10-03 | 025 | `OBJ-005` |

`DEL-03-01` is **not** in this set — `SOW-021` maps within its existing
`OBJ-005`, so its cell is unchanged.

### A003a — §3 table header, line 318 · **conditional on Q3** (`ActionSeq 3b`)

```
OLD: | ObjectiveID | Statement | SourceRef | Mapped Scope Items (best-effort) | MappedDeliverables |
NEW: | ObjectiveID | Statement | SourceRef | Mapped Scope Items | MappedDeliverables |
```

Carried as its own action row so approving A003 does not silently carry this.

### A003b — §3 objective rows (cols 4 and 5 only)

Under the recommended answers, `OBJ-003` (line 322) and `OBJ-006` (line 325)
are unchanged. **This holds only under those answers** — see Part 0.

Line 320 · `OBJ-001`:
```
OLD col4: SOW-004..009, SOW-041, SOW-043; instruments: SOW-058, SOW-059
NEW col4: SOW-001, SOW-003, SOW-004..009, SOW-011..017, SOW-040..043, SOW-089; instruments: SOW-058, SOW-059
OLD col5: DEL-04-01..05, DEL-08-03, DEL-08-04, DEL-10-01, DEL-10-04
NEW col5: DEL-00-03, DEL-01-01, DEL-02-01..07, DEL-04-01..05, DEL-08-01..04, DEL-10-01, DEL-10-04
```

Line 321 · `OBJ-002`:
```
OLD col4: SOW-006, SOW-018, SOW-019; supported by SOW-005
NEW col4: SOW-001, SOW-006, SOW-011..019; supported by SOW-005
OLD col5: DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03
NEW col5: DEL-01-01, DEL-02-01..07, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03
```

Line 323 · `OBJ-004`:
```
OLD col4: SOW-024, SOW-045..051; instrument: SOW-085
NEW col4: SOW-024, SOW-045..051, SOW-094; instrument: SOW-085
OLD col5: DEL-05-02, DEL-09-01..07, DEL-10-05
NEW col5: DEL-01-06, DEL-05-02, DEL-09-01..07, DEL-10-05
```

Line 324 · `OBJ-005`:
```
OLD col4: SOW-010, SOW-055; bound by C1/C2 across all items
NEW col4: SOW-010, SOW-021, SOW-025, SOW-052..056, SOW-088; bound by C1/C2 across all items
OLD col5: DEL-03-01, DEL-10-02
NEW col5: DEL-00-01, DEL-01-03, DEL-01-05, DEL-03-01, DEL-03-06, DEL-10-02, DEL-10-03
```

Every range is contiguous and fully mapped (verified in simulation).

### A003c — post-table note, lines 327–330

```
OLD:
No objective is unmapped at either level (scope items or deliverables);
SOW-062 was mapped to OBJ-003 at Phase 6 (TTL honesty is a presence-surface
instrument); SOW-063 remains intentionally unmapped — it instruments
PEC-K-07, which no §3-derived objective states directly (DL-14).

NEW:
No objective is unmapped at either level (scope items or deliverables);
SOW-062 was mapped to OBJ-003 at Phase 6 (TTL honesty is a presence-surface
instrument); SOW-063 remains intentionally unmapped — it instruments
PEC-K-07, which no §3-derived objective states directly (DL-14). SCA-002
mapped the Phase 2.2 wave scope at revision 1.2 (DL-17); the residue below
is deliberate, not pending.
```

The `SOW-063`/`DL-14` sentence is retained **verbatim**.

### A003d — mapping-notes block, lines 332–338

```
OLD:
**Mapping notes:** no unmapped objectives. Ingest/bridge items
(SOW-033..039) serve OBJ-001/OBJ-003 freshness indirectly through
PEC-K-07 and are intentionally not force-mapped; parser items
(SOW-011..017) underlie OBJ-001/OBJ-002 through the record tier
(SOW-001). Deferred/OUT and TBD items map to no objective by design.
Full ScopeItem→Objective assignments land in `ScopeLedger.csv` at
Phase 4–5; this table is the objective-side view.

NEW:
**Mapping notes:** no unmapped objectives. Ingest/bridge items
(SOW-033..039) serve OBJ-001/OBJ-003 freshness indirectly through
PEC-K-07 and are intentionally not force-mapped; parser items
(SOW-011..017) underlie OBJ-001/OBJ-002 through the record tier
(SOW-001) — SCA-002 carried that derivation into the ledger at
revision 1.2, mapping SOW-001 and SOW-011..017 to OBJ-001/OBJ-002
rather than superseding the rationale. Deferred/OUT and TBD items map
to no objective by design. Eleven IN items remain unmapped after
SCA-002's O-A wave-minimum scope: the unmapped members of the
ingest/bridge class above (SOW-033..038), SOW-063 (intentional per
DL-14), and SOW-022, SOW-023, SOW-044, SOW-087, which are out-of-wave
and left to the packet that authors their deliverables. Full
ScopeItem→Objective assignments land in `ScopeLedger.csv` at Phase 4–5;
this table is the objective-side view.
```

**Correction from v1:** the phrase "both intentional per DL-14" is removed.
`DL-14` records **only** `SOW-063`; the ingest/bridge intentionality lives in
the retained §3 sentence above it. v1's wording attributed to `DL-14` a
rationale it does not contain.

### A004 — §7 Coverage & Telemetry

Line 528:
```
OLD: | IN items without objective mapping | 31 (intentional best-effort posture, §3 mapping notes — parsers/mechanics serve objectives through the record tier) |
NEW: | IN items without objective mapping | 11 (SCA-002 O-A residue, §3 mapping notes — the ingest/bridge class SOW-033..038; SOW-063, intentional per DL-14; and out-of-wave SOW-022, SOW-023, SOW-044, SOW-087) |
```

The `DL-14` attribution is scoped to `SOW-063` by semicolon separation, so the
parenthetical cannot be read as covering the ingest/bridge class.

Line 532:
```
OLD: | Revision | 1.1, 2026-07-24 (SCA-001) |
NEW: | Revision | 1.2, 2026-07-25 (SCA-002) |
```

`ContextEnvelopeCounts` (line 529) is **unchanged**.

### A005a — §11 Decision Log, new row after `DL-16` · **authority: Part 3**

```
NEW:
| DL-17 | 2026-07-25 | SCA-002, requested by owner Ryan Tufts and opened by D-PEC-64, completes the deliverable→objective mapping for the Phase 2.2 scope-of-work wave scope (O-A wave-minimum): 20 IN ledger rows gain ObjectiveIDs and 17 deliverables gain SupportsObjectives, with §3's parser derivation carried into the ledger rather than superseded and the ingest/bridge and SOW-063 intentional rationale retained verbatim for the 11-row residue; §5's stale envelope-posture line is corrected to the register value; no package, deliverable, objective, scope item, product function, stable ID, or dependency edge is added or removed | The wave's SOW briefs require non-empty package_objective_refs from register truth; completing the mapping in decomposition truth (rather than by a SOW-local convention, which the owner declined) keeps objective attribution auditable at its source, and confining the amendment to wave scope leaves the recorded intentional-unmapped rationale standing rather than force-mapping it |
```

### A005b — §12 Revision History, new row after `1.1`

```
NEW:
| 1.2 | SCA-002 | Deliverable→objective mapping for the Phase 2.2 wave scope under D-PEC-64 (O-A): +ObjectiveIDs on 20 IN rows, +SupportsObjectives on 17 deliverables, §3 objective-side view and mapping notes reconciled, §7 metric 31→11, §5 envelope-posture line corrected (SCA-001 residual); topology unchanged |
```

### A006 — `_Decomposition/_LATEST.md` · complete successor text

SCA-001's precedent is **full-file replacement**, so the complete successor is
previewed. `{SLOT}` values are measured at Gate 5 and filled then; you approve
the **shape** now.

```markdown
# Latest — revision pointer and handoff state

Latest: `execution/_Decomposition/SOFTWARE_DECOMP.md` **revision 1.2**
(**`current_basis`** — accepted {CLOSURE_DATE} as the SCA-002 successor under
`D-PEC-64`).

## Handoff state

- **Basis:** D-PEC-60 SOFTWARE_DECOMP revision 1.0 over PRD v2.0, amended by
  SCA-001 (PRD v2.1 directed-bootstrap reconciliation, D-PEC-61) and by
  SCA-002 (deliverable→objective mapping for the Phase 2.2 wave scope,
  D-PEC-64). SCOPE_CHANGE Gates 1–5 were separately owner-confirmed.
- **Package:** working surface + `ScopeLedger.csv` (94 rows) +
  `Deliverables.csv` (64) + `ContextBudgetQA.csv` (unchanged) +
  `Companion_Inventory.csv` (unchanged).
- **Basis integrity (md5, post-amendment):** `SOFTWARE_DECOMP.md`
  {POST_MD5_DECOMP}; `Deliverables.csv` {POST_MD5_DELIVERABLES};
  `ScopeLedger.csv` {POST_MD5_LEDGER}.
- **Closure verdict: `CLOSED_FOR_SCOPE_CHANGE_ONLY`.** Revision 1.2 is the
  accepted decomposition basis. No package, deliverable, objective, scope
  item, product function, stable ID, or dependency edge was added or removed.
- **Verification:** deterministic pre/post register comparison confirms
  topology unchanged (94 scope items — 71 IN / 14 OUT / 9 TBD; 11 packages;
  64 deliverables; 6 objectives; Context Envelope S 28 / M 34 / L 2 / XL 0);
  union invariant 0 violations; exactly 20 ledger rows and 17 deliverable
  rows changed, in the `ObjectiveIDs` / `SupportsObjectives` columns only;
  the 11 residue IN rows and 9 residue deliverables byte-identical.
- **Mapping state:** IN items without objective mapping 31 → 11; deliverables
  without objective mapping 26 → 9. All 32 Phase 2.2 wave members carry a
  non-empty `SupportsObjectives` set.
- **AuditState: `{AUDIT_STATE}`.** Pre-change baseline
  `_Evaluation/DecompCoverage/COV_SCA002_PRECHANGE_2026-07-25_1040/`;
  post-change baseline `{POST_COV_SNAPSHOT}`. OI-013 remains the durable
  register-validator follow-on.
- **Supersession:** no `Supersession_Delta.csv` binding owed (attributions
  consume PRD anchors; no upstream authority fact is overridden).
  `Supersession_Map.csv` carries SCA-001's accepted rows forward unchanged.
- **Blockers / open issues:** OI-B — all 64 deliverable `_REFERENCES.md` still
  pin "revision 1.1"; that surface is excluded by `D-PEC-64` §3.3 and the
  refresh is a deferred obligation owned by resumed `PROJECT_SETUP`.
  `_CONTEXT.md` basis pointers: {CONTEXT_POINTER_DISPOSITION}. OI-001..009
  remain the §16 owner decisions; OI-012 the core-isolation ADR; OI-013 the
  validator follow-on.
- **DownstreamRerunState: `FROZEN`** — released, not executed by SCOPE_CHANGE.
- **ReadyForNextPhase: `REGEN_ONLY`.** `PROJECT_SETUP` is the next owner and
  resumes per `D-PEC-64` §2.4: SCA-002 receipt, closure commit, the D-PEC-63
  re-pins (three points + the DAG-exhibit §1 annotation), and the
  `projects/pec/AGENTS.md` pointer refresh.
- **Fallback and authority:** unchanged from revision 1.1 — the full DAG is
  PEC's initial file-native self-ingestion corpus; observed friction may
  generate evidence-linked candidates or amendment requests but changes no
  accepted scope and grants no authority. File-native fallback remains
  operable.
```

### A007 — §5 envelope-posture line (W-1 fix)

Line 376:
```
OLD: Context Envelope posture: **29 S / 33 M / 2 L / 0 XL.** Both L
NEW: Context Envelope posture: **28 S / 34 M / 2 L / 0 XL.** Both L
```

Lines 377–379 continue unchanged; the two `L` deliverables named
(`DEL-02-03`, `DEL-01-01`) remain correct.

### A008 — front-matter revision block · **requires a §4.3 amendment (Part 3)**

```
Line 6  OLD: revision: "1.1"
        NEW: revision: "1.2"
Line 7  OLD: date: 2026-07-24
        NEW: date: 2026-07-25
Line 8  OLD: accepted: 2026-07-24 (original Gate 7 owner ruling under D-PEC-60; revision 1.1 successor accepted through SCA-001 under D-PEC-61)
        NEW: accepted: 2026-07-25 (original Gate 7 owner ruling under D-PEC-60; revision 1.2 successor accepted through SCA-002 under D-PEC-64)
Line 11 OLD: session_authorization: D-PEC-60; amended by SCA-001 under D-PEC-61
        NEW: session_authorization: D-PEC-60; amended by SCA-001 under D-PEC-61, then by SCA-002 under D-PEC-64
```

`source_corpus` (line 12) and `status: current_basis` (line 5) unchanged.

---

## Part 3 — Window authority · **corrects a false claim in v1**

`D-PEC-64` §4.3 enumerates the allowed-change window as: *"20 IN rows, 17
deliverable rows, the §3/§7/revision-history/mapping-notes text, and the
in-fence `_CONTEXT.md` line classes"*, plus the Gate 1 owner amendment
admitting the one §5 prose line.

**v1 claimed A008 was "inside the window's revision-history text". That is
false.** Front-matter lines 6–8 and 11 are not §3, not §7, not §12 Revision
History, and not the mapping notes. I asserted an authority basis the packet
does not contain — the same class of error as the `AGENTS.md` "measured" claim
at Gate 2, and the one I had said I would not repeat.

**One consistent reading, applied to all three edge cases:**

| Action | Target | In the §4.3 byte-window? | Authority |
|---|---|---|---|
| A005b | §12 Revision History | **Yes** — "revision-history text" | §4.3 as written |
| **A005a** | §11 **Decision Log** | **No**, strict reading — §11 and §12 are distinct sections and the window names revision-history only | **Needs the §4.3 amendment** |
| **A008** | Front matter, lines 6–8, 11 | **No** | **Needs the §4.3 amendment** |
| A006 | `_Decomposition/_LATEST.md` | **Not applicable** — a separate file, not text inside the decomposition document | `D-PEC-64` §3.2 names it a writable amendment target (line 131) and §2.3 names the `_LATEST.md` update in the requested endpoint. Outside the byte-window enumeration **by construction**, not as a silent exception |

I take the **strict** reading deliberately. A loose reading ("revision history"
loosely covers the Decision Log too) would let A005a through — but that same
looseness produced v1's false A008 claim. Being strict costs one line in an
owner amendment and removes the ambiguity permanently.

The instrument already exists and was used once today: the owner amended §4.3
at Gate 1 to admit the A007 line. **Q4 asks for the same instrument covering
(i) the front-matter revision block and (ii) the §11 Decision Log append.**

---

## Part 4 — Explicit unchanged surfaces (Gate 3 determinations)

`D-PEC-64` assigns two determinations to this gate. Both are demonstrated, not
asserted.

**`ContextBudgetQA.csv` — no edit required.** It carries per-deliverable
envelope/risk/action QA. SCA-002 changes no `ContextEnvelope` value: the
simulation confirms envelope counts S 28 / M 34 / L 2 / XL 0 pre and post, and
check 6 confirms no column other than `ObjectiveIDs` / `SupportsObjectives`
changes on any row. The file has no objective column. **`NO_CHANGE`.**

**`Companion_Inventory.csv` — no edit required.** Its six rows carry
`Filename`, `PackageRole`, `Description`. SCA-002 changes no filename, no
package role, and no count cited in a description — the ledger remains
"94-row", the deliverable register remains "64-row". The D-PEC-61 conditional
clause (edit only if Gate 3 demonstrates one is required) is **not triggered**.
**`NO_CHANGE`.**

**Also explicitly unchanged:** all 14 `OUT` and 9 `TBD` ledger rows; the 11
residue IN rows and 9 residue deliverables; `DEL-03-01`; §7
`ContextEnvelopeCounts`; §3 rows `OBJ-003` and `OBJ-006` *(under the
recommended Q1/Q2 answers only)*; `source_corpus` and `status` in the front
matter; every deliverable-local `Dependencies.csv`; `projects/pec/docs/PRD.md`.

---

## Part 5 — Deterministic post-state simulation

Simulated in memory from the pinned registers; evidence at
`Gate3_Simulation.json` (now carrying basis-md5, date and method provenance).
**All six checks pass** — for the **recommended** Q1/Q2 answers only.

| # | Check | Result |
|---|---|---|
| 1 | Union invariant, file-wide | **0 violations** across all 64 deliverables |
| 2 | Residue untouched | 11 residue IN rows and 9 residue deliverables unchanged and still unmapped; 14 `OUT` + 9 `TBD` byte-identical |
| 3 | Token grammar | every changed cell matches `^OBJ-[0-9]{3}$` after `;`-split; no commas, spaces or qualifiers |
| 4 | Topology unchanged | 94 (71/14/9), 64 deliverables, 11 packages, 6 objectives, S 28 / M 34 / L 2 |
| 5 | §4.3 window | exactly **20** ledger + **17** deliverable rows; `DEL-03-01` unchanged; `SOW-021` ⊆ `{OBJ-005}` |
| 6 | Column containment | no column other than the two target columns changed |

Post-state: unmapped IN **31 → 11**; unmapped deliverables **26 → 9**; wave
members unmapped **17 → 0**.

| Objective | Items | Dels | Δ dels |
|---|---|---|---|
| OBJ-001 | 22 | 20 | +11 |
| OBJ-002 | 12 | 12 | +8 |
| OBJ-003 | 13 | 12 | — |
| OBJ-004 | 10 | 10 | +1 |
| OBJ-005 | 9 | 7 | +5 |
| OBJ-006 | 9 | 9 | — |

---

## Part 6 — Supersession re-affirmation (Gate 2 condition discharged)

Gate 2 accepted "no binding owed" **conditional on the Gate 3 attributions
remaining consumptive of the PRD**. Tested against every drafted attribution:

| Test | Result |
|---|---|
| Any attribution asserting a fact **not** in the PRD? | **No** — each maps a scope item to an objective whose PRD-stated outcome the quoted requirement serves |
| Any attribution **contradicting** a PRD statement? | **No** — no requirement is restated, narrowed or overridden |
| Any change to a PRD **authority fact**? | **No** — the PRD is read-only here and excluded by `D-PEC-64` §3.3 |
| Does A007 supersede anything? | **No** — corrects a stale restatement toward accepted register truth |
| Does A003 supersede the §3 rationale? | **No** — the parser derivation is applied; ingest/bridge and `SOW-063` retained verbatim |
| Does A008 supersede anything? | **No** — front-matter metadata follows the amendment it describes |

**Re-affirmed: no `Supersession_Delta.csv` binding is owed.** This holds under
**every** alternative on the Q1/Q2 table — each is a reading of PRD text, not a
contradiction of it. Weak warrants make an attribution *debatable*, not
*superseding*. Gate 5 carries SCA-001's header-only map forward:

```bash
python3 tools/coordination/accumulate_supersession_map.py \
  --prior-map projects/pec/execution/_ScopeChange/SCA-001_2026-07-24_2206/Supersession_Map.csv \
  --output-map projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Supersession_Map.csv \
  --allow-empty
```

---

## Part 7 — v2 correction log (round R-2b-g3)

26 findings, all `ACCEPTED`. Verified against repo state before applying.

| # | Correction |
|---|---|
| C-14 | **A008 authority claim was false** — front matter is not §3/§7/§12/mapping-notes. Requires a dated §4.3 amendment. Part 3 |
| C-15 | **A005a (§11 Decision Log) is also outside the window** on the strict reading. One consistent reading adopted; folded into Q4 |
| C-16 | **A006's authority stated explicitly** — `D-PEC-64` §3.2 line 131 + §2.3; outside the byte-window by construction, not a silent exception |
| C-17 | **Alternative-contingency surfaced to Part 0** and into Q5's wording; the unconditional "OBJ-003/OBJ-006 unchanged" sentence is now conditioned |
| C-18 | **`SOW-055` precedent withdrawn as tautological** — it restates OBJ-005 nearly verbatim and selects nothing for `SOW-025` |
| C-19 | **DEL-10-03 recalibrated HIGH → LOW-MEDIUM** and reframed: no §3 objective states K-AUTH-1's boundary (the `DL-14` condition); O-A forces a least-wrong choice. Per-row ruling, three candidates |
| C-20 | **DEL-03-06 warrant quote was truncated at exactly the clause pointing elsewhere.** Full PEC-SVC-003 quoted; `OBJ-002` and both-objectives alternatives presented; escalated to per-row |
| C-21 | **DEL-08-02 escalated** to per-row; weak textual link stated (additive schema serves all API consumers) |
| C-22 | **DEL-01-05 recalibrated to MEDIUM** to match DEL-00-01's identical ADR-002 chain; both now per-row |
| C-23 | **OBJ-005's "bound by C1/C2 across all items" convention engaged** — constraint-like posture is not itself grounds for an OBJ-005 mapping; zero-dependency candidates weighted down |
| C-24 | **DEL-01-03 reasoned from the full requirement** — the content-minimal clause maps to no objective; the mapping rests on the gitignored-path clause alone |
| C-25 | **A003d: "both intentional per DL-14" removed** — `DL-14` covers `SOW-063` only. A004's parenthetical rescoped so it cannot read as covering the ingest/bridge class |
| C-26 | **A006 previewed as complete successor file** with marked Gate-5 slots, per SCA-001's full-replacement precedent |
| C-27 | **Q2 narrow options defined** as N1 / N2 with exact A001/A002/A003 consequences |
| C-28 | **Part 4 added** — `ContextBudgetQA.csv` and `Companion_Inventory.csv` determinations demonstrated; explicit-unchanged-surfaces section in the SCA-001 style |
| C-29 | **"Six are HIGH/MEDIUM-HIGH" withdrawn** — false against my own labels; only two rows batch into Q5 |
| C-30 | **A003a split into its own action row** (`ActionSeq 3b`, conditional on Q3) |
| C-31 | **`SCOPE_CHANGE_POSTCHECK` restored** to `DownstreamReruns` on every row (SCA-001 precedent; v1 dropped it with no rationale). `NONE` replaced with named owners |
| C-32 | **`Gate3_Simulation.json` provenance added** — basis md5s, run date, method |
| C-33 | **Citation hygiene** — §8 anchor corrected to `:217–219` (soft-wrap), inserted bold removed from the §9.7:300 quote, Part-4/Part-5 cross-references fixed |

### Decision-log note recorded at Gate 3

**`SOW-038` / `DL-11` tension.** §3's mapping notes call `SOW-033..039`
"ingest/bridge items", but `SOW-038` (PEC-STR-004, stream loss recovered by
reconciliation) is assigned to **PKG-03 Reconciliation & Parity** in §4, not to
PKG-07 Event Ingest & Bridges — it is a reconciliation-side guarantee, not
ingest mechanics. The §3 grouping label is therefore loose with respect to the
package assignment (`DL-11` records the forced boundary decisions). SCA-002
**does not resolve this**: `SOW-038` is residue under O-A and its row is
untouched. Recorded so the next amendment touching the ingest/bridge class
inherits the observation rather than rediscovering it.

### What v1 got wrong, in one line

The mechanics were right and the framing oversold them: a false authority
claim, contingent text presented as settled, a tautological precedent dressed
as evidence, and a quote cut at the clause that disagreed with me. Three of
those four make the package *look* more decided than the evidence supports —
the same overstatement pattern recorded at Gate 2, in a new form.

---

## Part 8 — Gate 3 approval question

**Do you approve these amendments to the decomposition document?**

**Q1 — per-row attribution rulings (7).** Each is `MODIFY` on one ledger cell;
non-recommended answers void the drafted A002/A003b text for that row.

| # | Row | Recommended | Alternatives | Conf. |
|---|---|---|---|---|
| Q1.1 | DEL-00-01 / SOW-088 | `OBJ-005` | `OBJ-003` | MED |
| Q1.2 | DEL-00-03 / SOW-089 | `OBJ-001` | full-span five-objective set · `OBJ-006` | **LOW** |
| Q1.3 | DEL-01-05 / SOW-052+053 | `OBJ-005` | `OBJ-003` | MED |
| Q1.4 | DEL-03-06 / SOW-054 | `OBJ-005` | `OBJ-002` · `OBJ-005;OBJ-002` | MED-LOW |
| Q1.5 | DEL-08-01 / SOW-003+040 | `OBJ-001` | `OBJ-001;OBJ-004` | MED-HIGH |
| Q1.6 | DEL-08-02 / SOW-042 | `OBJ-001` | `OBJ-001;OBJ-004` · full consumer set | MED |
| Q1.7 | DEL-10-03 / SOW-025 | `OBJ-005` | `OBJ-003` · `OBJ-006` | **LOW-MED** |

**Q2 — INDIRECT-8 breadth.** **AFFIRM** `[OBJ-001, OBJ-002]` for all eight
*(recommended)*, or **N1** (seven parsers → `OBJ-001`; `SOW-001` keeps both),
or **N2** (all eight → `OBJ-001`). N1 and N2 change A001/A002/A003b and force
re-simulation; N2 deletes the `OBJ-002` §3 edit entirely.

**Q3 — §3 table header (A003a, `ActionSeq 3b`).** Drop "(best-effort)" from
`Mapped Scope Items` *(recommended — the qualifier described the posture A004
retires)*, or retain it since 11 residue rows remain?

**Q4 — A008 plus the window amendment.** Approve **A008 (front-matter revision
block)** *and* a dated `D-PEC-64` §4.3 owner amendment admitting (i) the
front-matter revision block, lines 6–8 and 11, and (ii) the §11 Decision Log
append (A005a) — the same instrument used at Gate 1 for the A007 line?
Declining A008 leaves revision 1.2 declaring itself revision 1.1; declining the
§4.3 amendment leaves A005a and A008 without an authority basis.

**Q5 — everything else, conditional on Q1/Q2 recommended.** Approve A001,
A002, A003b, A003c, A003d, A004, A005a, A005b, A006 and A007 as drafted —
**valid only if Q1 and Q2 are ruled as recommended**. Any other answer returns
a revised Gate 3 package rather than proceeding to Gate 4.

Batched into Q5: the two attributions with direct unambiguous warrants —
`DEL-01-03` (HIGH) and `DEL-01-06` (HIGH).
