---
amendment_id: SCA-002
doc_kind: scope_change.amendment_preview
decomp_variant: SOFTWARE
gate: 3
created: 2026-07-25
status: awaiting_gate_3_approval
scope_width: O-A
authority: D-PEC-64
basis: SOFTWARE_DECOMP.md revision 1.1 (current_basis)
basis_pins: SOFTWARE_DECOMP.md ad944a2bfa7784778afa8558d8f81762; Deliverables.csv 6d2b290b0c869fc1d51d626a1714abec; ScopeLedger.csv 49e0cff9af647e41966b7a3334641919
---

# SCA-002 — Amendment Preview (Gate 3)

Exact text for all seven ruled actions, plus one **newly surfaced gap
(A008)** the register does not currently cover. Nothing here is applied:
decomposition truth is untouched until the Gate 3 approval and the Gate 4
propagation plan are both relayed back.

Basis pins re-verified unchanged at Gate 3 open (all three md5s match).

---

## Part 1 — Attribution development (the 9 NEEDS-ATTRIBUTION rows)

Method per `D-PEC-64` / intake §4: ledger `SourceRef` → the actual PRD row in
`projects/pec/docs/PRD.md` → the §3 objective whose stated outcome that
function serves. **Every warrant below is quoted verbatim from my own read of
the PRD**, with its line anchor.

### The six objectives (SOFTWARE_DECOMP §3, derived from PRD §3 / §11)

`OBJ-001` sub-second cited orientation · `OBJ-002` structural staleness by SHA ·
`OBJ-003` declared presence/write-scope surface · `OBJ-004` owner's one live
view · `OBJ-005` deletable at any moment without blocking · `OBJ-006`
measurable/falsifiable thesis.

### Register precedents used as anchors (measured, not assumed)

| Precedent | Mapping | Why it anchors |
|---|---|---|
| `SOW-010` PEC-RCN-001 "rebuildable… store gitignored" | `OBJ-005` | Rebuild/store-locality cluster → deletability |
| `SOW-055` PEC-SVC-004 kill test → `DEL-10-02` | `OBJ-005` | A PKG-10 **verification** deliverable maps to the objective its invariant serves, **not** to OBJ-006 |
| `SOW-041` PEC-API-002, `SOW-043` → `DEL-08-03/04` | `OBJ-001` | PKG-08 API members serve the orientation outcome |
| `SOW-018`/`SOW-019` PEC-RCN-003/004 | `OBJ-002` | OBJ-002's register locus is the reconciler layer |

### Per-row attributions

| # | DEL | SOW | SourceRef | Recommended | Warrant (verbatim, PRD) | Confidence |
|---|---|---|---|---|---|---|
| 1 | DEL-00-01 | SOW-088 | §13 | `OBJ-005` | §13:379 "live postures (ADR-002, ADR-014) re-cited in v2's first ADRs" — ADR-002 is the zero-dependency core (PEC-SVC-001); the OI-012 core-isolation seam it settles is what lets the store be "gitignored and safe to delete" (PEC-K-02, §6:157) | **MEDIUM** — enabling artifact; see alternatives |
| 2 | DEL-00-03 | SOW-089 | §13 | `OBJ-001` | §13:379 "v2 SPEC is born from the decomposition" | **LOW — genuinely ambiguous; owner should rule** |
| 3 | DEL-01-03 | SOW-056 | PEC-SVC-005 | `OBJ-005` | §10:317 "The store lives at a gitignored path; the content-minimal rule (PEC-K-10) is enforced at ingest" | **HIGH** |
| 4 | DEL-01-05 | SOW-052, SOW-053 | PEC-SVC-001/002 | `OBJ-005` | §10:313 "zero third-party runtime dependencies (carries ADR-002)"; §10:314 "Local, single-owner posture; no external network egress" | **MEDIUM-HIGH** |
| 5 | DEL-01-06 | SOW-094 | §12 P2, PEC-DSH-002 | `OBJ-004` | §9.7:300 "Lifecycle census across all **registered loops'** packages/deliverables"; §12:348 P2 "All five loops; Overview, census, registers, decision slate" | **HIGH** |
| 6 | DEL-03-06 | SOW-054 | PEC-SVC-003 | `OBJ-005` | §10:315 "Full rebuild of the current corpus completes within a bound confirmed at Phase 1" — the performance bound on the same rebuild `SOW-010` maps to `OBJ-005` | **MEDIUM-HIGH** |
| 7 | DEL-08-01 | SOW-003, SOW-040 | §8, PEC-API-001 | `OBJ-001` | §9.6:289 "The service binds local-only, Unix socket by default, with token-scoped access"; §8:218 harnesses are "machine consumers of the API on behalf of agent sessions" | **MEDIUM-HIGH** — see alternative |
| 8 | DEL-08-02 | SOW-042 | PEC-API-003 | `OBJ-001` | §9.6:291 "The API schema is versioned; evolution is additive" | **MEDIUM** |
| 9 | DEL-10-03 | SOW-025 | PEC-GAT-004 | `OBJ-005` | §9.3:261 "PEC shall provide no write path that records adoption, ruling, or direction (PEC-K-02; K-AUTH-1)" — exact analogue of `DEL-10-02`/`SOW-055` → `OBJ-005` | **HIGH** |

### The three rows where the method strains — owner should rule explicitly

**Row 2 · DEL-00-03 (v2 SPEC) — LOW confidence, the weakest attribution in the set.**
The SPEC specifies the whole product; it does not serve one outcome more than
another. Its PRD anchor (§13) is about prototype disposition, not about any
product outcome. Three defensible answers:

- **(a) `OBJ-001`** *(recommended)* — the SPEC's primary subject is the
  orientation product; OBJ-001 is the thesis outcome. Thin but non-arbitrary.
- **(b) `OBJ-001;OBJ-002;OBJ-003;OBJ-004;OBJ-005`** — full-span, honest about
  a document that specifies everything. Cost: inflates five objectives'
  deliverable counts with an authoring artifact and weakens the signal in §3.
- **(c) `OBJ-006`** — the SPEC is what makes behavior checkable, and §11's
  falsification clause needs stated behavior to falsify. Weakest textual
  warrant; §13 says nothing about measurement.

I recommend **(a)** but hold it at LOW confidence: this is a judgment about
what an authoring deliverable "serves", and the PRD does not settle it.

**Row 1 · DEL-00-01 (v2 first ADRs) — MEDIUM.** Same enabling-artifact
problem, but with a concrete hook: OI-012's core-isolation seam is
schema-vs-persistence, and persistence separability is what PEC-K-02's
deletability rests on. Alternative: `OBJ-003` (ADR-014 shared-runtime agent
ownership touches the coordination surface) — I judge this weaker, since
ADR-014's effect is to keep session ownership *out* of PEC.

**Row 7 · DEL-08-01 (Unix socket + token-scoped access) — MEDIUM-HIGH.**
`SOW-040` → `OBJ-001` is solid (PKG-08 transport precedent). `SOW-003`'s three
access classes include **owner**, and §8:217 gives the owner "dashboards,
decision slate, presence board" — an `OBJ-004` reading. Alternative:
`SOW-003` → `OBJ-001;OBJ-004`, which would make `DEL-08-01` = `OBJ-001;OBJ-004`.
I recommend `OBJ-001` alone, because the dashboards that serve OBJ-004 are
PKG-09 deliverables and already carry it; the access-class row is about
gating the API, not about the owner's view.

### The INDIRECT-8 (`DEL-01-01` + `DEL-02-01..07`) — affirm both, with the alternative stated

§3's mapping notes state a **positive derivation**: "parser items
(SOW-011..017) underlie OBJ-001/OBJ-002 through the record tier (SOW-001)".

**Recommendation: affirm the full set `[OBJ-001, OBJ-002]` for all eight**,
uniformly. Reasons: it is the accepted §3 rationale applied rather than
superseded; it is what the source text says about the set as a whole; and
deviating per-parser would substitute my judgment for accepted truth.

**The genuine alternative, stated because the register supports it.** My own
measurement shows OBJ-002's register locus is the *reconciler* layer, not the
parsers: `SOW-018` (incremental, keyed on Git delta) and `SOW-019` (drift
classification) carry `OBJ-002`; `SOW-006` (SHA stamping) carries
`OBJ-001;OBJ-002`. A narrower reading would give the seven parsers `OBJ-001`
only and leave OBJ-002 to the layer that actually performs SHA comparison —
reducing OBJ-002's deliverable count from 12 to 4.

I do not recommend the narrow reading, but it is not a strawman: it would
arguably describe the system more precisely. The owner should pick knowingly.

### `SOW-021` — constraint satisfied

`SOW-021` (PEC-RCN-006, §9.2:252 "The reconciler writes only its own store and
generated views") → **`OBJ-005`**, a subset of the binding `{OBJ-005}`.
`DEL-03-01` already carries `OBJ-005` via `SOW-010`, so its cell is
**unchanged** and the 17-row window holds. Verified in simulation.

---

## Part 2 — Exact amendment text

All edits are old→new pairs with line anchors against revision 1.1.

### A001 — `ScopeLedger.csv`, `ObjectiveIDs` column, 20 rows

Every cell is currently empty (`""`). Only this column changes on these rows.

| ScopeItemID | old | new |
|---|---|---|
| SOW-001 | *(empty)* | `OBJ-001;OBJ-002` |
| SOW-003 | *(empty)* | `OBJ-001` |
| SOW-011 | *(empty)* | `OBJ-001;OBJ-002` |
| SOW-012 | *(empty)* | `OBJ-001;OBJ-002` |
| SOW-013 | *(empty)* | `OBJ-001;OBJ-002` |
| SOW-014 | *(empty)* | `OBJ-001;OBJ-002` |
| SOW-015 | *(empty)* | `OBJ-001;OBJ-002` |
| SOW-016 | *(empty)* | `OBJ-001;OBJ-002` |
| SOW-017 | *(empty)* | `OBJ-001;OBJ-002` |
| SOW-021 | *(empty)* | `OBJ-005` |
| SOW-025 | *(empty)* | `OBJ-005` |
| SOW-040 | *(empty)* | `OBJ-001` |
| SOW-042 | *(empty)* | `OBJ-001` |
| SOW-052 | *(empty)* | `OBJ-005` |
| SOW-053 | *(empty)* | `OBJ-005` |
| SOW-054 | *(empty)* | `OBJ-005` |
| SOW-056 | *(empty)* | `OBJ-005` |
| SOW-088 | *(empty)* | `OBJ-005` |
| SOW-089 | *(empty)* | `OBJ-001` |
| SOW-094 | *(empty)* | `OBJ-004` |

### A002 — `Deliverables.csv`, `SupportsObjectives` column, 17 rows

Derived from A001 by the union invariant, not authored independently.

| DeliverableID | Covers | old | new |
|---|---|---|---|
| DEL-00-01 | SOW-088 | *(empty)* | `OBJ-005` |
| DEL-00-03 | SOW-089 | *(empty)* | `OBJ-001` |
| DEL-01-01 | SOW-001 | *(empty)* | `OBJ-001;OBJ-002` |
| DEL-01-03 | SOW-056 | *(empty)* | `OBJ-005` |
| DEL-01-05 | SOW-052;SOW-053 | *(empty)* | `OBJ-005` |
| DEL-01-06 | SOW-094 | *(empty)* | `OBJ-004` |
| DEL-02-01 | SOW-011 | *(empty)* | `OBJ-001;OBJ-002` |
| DEL-02-02 | SOW-012 | *(empty)* | `OBJ-001;OBJ-002` |
| DEL-02-03 | SOW-013 | *(empty)* | `OBJ-001;OBJ-002` |
| DEL-02-04 | SOW-014 | *(empty)* | `OBJ-001;OBJ-002` |
| DEL-02-05 | SOW-015 | *(empty)* | `OBJ-001;OBJ-002` |
| DEL-02-06 | SOW-016 | *(empty)* | `OBJ-001;OBJ-002` |
| DEL-02-07 | SOW-017 | *(empty)* | `OBJ-001;OBJ-002` |
| DEL-03-06 | SOW-054 | *(empty)* | `OBJ-005` |
| DEL-08-01 | SOW-003;SOW-040 | *(empty)* | `OBJ-001` |
| DEL-08-02 | SOW-042 | *(empty)* | `OBJ-001` |
| DEL-10-03 | SOW-025 | *(empty)* | `OBJ-005` |

`DEL-03-01` is **not** in this set — confirmed unchanged.

### A003 — §3 Objectives (table columns + mapping notes)

**A003a — table header, line 318.** Optional sub-decision; see Part 4 Q3.

```
OLD: | ObjectiveID | Statement | SourceRef | Mapped Scope Items (best-effort) | MappedDeliverables |
NEW: | ObjectiveID | Statement | SourceRef | Mapped Scope Items | MappedDeliverables |
```

**A003b — objective rows.** Only columns 4 and 5 change. `OBJ-003` (line 322)
and `OBJ-006` (line 325) are **unchanged** — O-A maps nothing they cover.

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

Range notation follows the document's existing convention; every range is
contiguous and fully mapped (verified in simulation).

**A003c — post-table note, lines 327–330:**
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

The `SOW-063` sentence is retained **verbatim**.

**A003d — mapping-notes block, lines 332–338:**
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
SCA-002's O-A wave-minimum scope: the ingest/bridge class above
(SOW-033..038, its unmapped members) and SOW-063, both intentional per
DL-14; and SOW-022, SOW-023, SOW-044, SOW-087, which are out-of-wave
and left to the packet that authors their deliverables. Full
ScopeItem→Objective assignments land in `ScopeLedger.csv` at Phase 4–5;
this table is the objective-side view.
```

The ingest/bridge clause is retained **verbatim**; the parser clause is
retained verbatim and extended with what SCA-002 did to it.

### A004 — §7 Coverage & Telemetry

Line 528:
```
OLD: | IN items without objective mapping | 31 (intentional best-effort posture, §3 mapping notes — parsers/mechanics serve objectives through the record tier) |
NEW: | IN items without objective mapping | 11 (SCA-002 O-A residue, §3 mapping notes — the intentional ingest/bridge class SOW-033..038 and SOW-063 (DL-14), plus out-of-wave SOW-022, SOW-023, SOW-044, SOW-087) |
```

Line 532:
```
OLD: | Revision | 1.1, 2026-07-24 (SCA-001) |
NEW: | Revision | 1.2, 2026-07-25 (SCA-002) |
```

`ContextEnvelopeCounts` (line 529) is **unchanged** — A007 makes §5 agree
with it, not the reverse.

### A005 — Change Register

**A005a — §11 Decision Log, new row after `DL-16` (line 625):**
```
NEW:
| DL-17 | 2026-07-25 | SCA-002, requested by owner Ryan Tufts and opened by D-PEC-64, completes the deliverable→objective mapping for the Phase 2.2 scope-of-work wave scope (O-A wave-minimum): 20 IN ledger rows gain ObjectiveIDs and 17 deliverables gain SupportsObjectives, with §3's parser derivation carried into the ledger rather than superseded and the ingest/bridge + SOW-063 intentional rationale retained verbatim for the 11-row residue; §5's stale envelope-posture line is corrected to the register value; no package, deliverable, objective, scope item, product function, stable ID, or dependency edge is added or removed | The wave's SOW briefs require non-empty package_objective_refs from register truth; completing the mapping in decomposition truth (rather than by a SOW-local convention, which the owner declined) keeps objective attribution auditable at its source, and confining the amendment to wave scope leaves the recorded intentional-unmapped rationale standing rather than force-mapping it |
```

**A005b — §12 Revision History, new row after `1.1` (line 640):**
```
NEW:
| 1.2 | SCA-002 | Deliverable→objective mapping for the Phase 2.2 wave scope under D-PEC-64 (O-A): +ObjectiveIDs on 20 IN rows, +SupportsObjectives on 17 deliverables, §3 objective-side view and mapping notes reconciled, §7 metric 31→11, §5 envelope-posture line corrected (SCA-001 residual); topology unchanged |
```

### A006 — `_Decomposition/_LATEST.md`

Lines 3–5:
```
OLD:
Latest: `execution/_Decomposition/SOFTWARE_DECOMP.md` **revision 1.1**
(**`current_basis`** — accepted 2026-07-24 as the SCA-001 successor under
`D-PEC-61`).

NEW:
Latest: `execution/_Decomposition/SOFTWARE_DECOMP.md` **revision 1.2**
(**`current_basis`** — accepted 2026-07-25 as the SCA-002 successor under
`D-PEC-64`).
```

The handoff-state body (basis, package, closure verdict, verification,
audit state, blockers, ReadyForNextPhase) is rewritten at **Gate 5** from
actual post-change evidence, not drafted here — it must state measured facts,
and the measurements do not exist yet. Gate 4 approves the shape; Gate 5
writes the values.

### A007 — §5 envelope-posture line (the W-1 fix)

Line 376:
```
OLD: Context Envelope posture: **29 S / 33 M / 2 L / 0 XL.** Both L
NEW: Context Envelope posture: **28 S / 34 M / 2 L / 0 XL.** Both L
```

Single line; the sentence continues unchanged on lines 377–379, and the two
`L` deliverables it names (`DEL-02-03`, `DEL-01-01`) remain correct.

### A008 — front-matter revision block · **NEWLY SURFACED — not in the ruled register**

A001–A007 do not cover the document's own front matter. If it is not amended,
revision 1.2 ships declaring `revision: "1.1"` and contradicts both §7 and
`_LATEST.md`. Proposed exact text:

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

`source_corpus` (line 12) is **unchanged** — SCA-002 consumes PRD v2.1, it
does not re-baseline it. `status: current_basis` (line 5) is unchanged.

**This is a gap in the ruled action register, not a scope expansion.** It is
`MODIFY`-class, mechanically entailed by A004/A006, and inside the §4.3
window's "revision-history text". I surface it as a discrete action rather
than folding it silently into A005 so the owner approves it explicitly.

---

## Part 3 — Deterministic post-state simulation

Simulated in memory from the pinned registers; evidence at
`Gate3_Simulation.json` in this snapshot. **All six checks pass.**

| # | Check | Result |
|---|---|---|
| 1 | Union invariant, file-wide | **0 violations** across all 64 deliverables |
| 2 | Residue untouched | 11 residue IN rows unchanged and still unmapped; 9 residue deliverables unchanged and still unmapped; 14 `OUT` + 9 `TBD` rows byte-identical |
| 3 | Token grammar | every changed cell matches `^OBJ-[0-9]{3}$` after `;`-split; no commas, spaces, or qualifiers |
| 4 | Topology unchanged | 94 scope items (71 IN / 14 OUT / 9 TBD), 64 deliverables, 11 packages, 6 objectives, envelopes S 28 / M 34 / L 2 |
| 5 | `D-PEC-64` §4.3 window | exactly **20** ledger rows and **17** deliverable rows changed; `DEL-03-01` unchanged; `SOW-021` ⊆ `{OBJ-005}` satisfied |
| 6 | Column containment | **no column other than `ObjectiveIDs` / `SupportsObjectives` changed** on any row |

Derived post-state: unmapped IN **31 → 11**; unmapped deliverables
**26 → 9**. Both match the §7 and mapping-notes text drafted above.

Per-objective counts after the amendment (drives the A003b lists):

| Objective | Items | Deliverables | Δ deliverables |
|---|---|---|---|
| OBJ-001 | 22 | 20 | +11 |
| OBJ-002 | 12 | 12 | +8 |
| OBJ-003 | 13 | 12 | — |
| OBJ-004 | 10 | 10 | +1 |
| OBJ-005 | 9 | 7 | +5 |
| OBJ-006 | 9 | 9 | — |

---

## Part 4 — Supersession re-affirmation (Gate 2 condition discharged)

The Gate 2 acceptance was **conditional**: no `Supersession_Delta.csv` binding
is owed *provided the Gate 3 attributions remain consumptive of the PRD*.
Tested against the nine drafted attributions plus the INDIRECT-8:

| Test | Result |
|---|---|
| Does any attribution assert a fact **not** present in the PRD? | **No.** Each maps a scope item to an objective whose PRD-stated outcome the quoted requirement serves. Every warrant is a verbatim PRD quote |
| Does any attribution **contradict** a PRD statement? | **No.** No requirement is restated, narrowed, or overridden |
| Does any attribution change a PRD **authority fact**? | **No.** `projects/pec/docs/PRD.md` is read-only here and excluded by `D-PEC-64` §3.3 |
| Does A007 supersede anything? | **No.** It corrects a stale restatement toward already-accepted register truth |
| Does A003 supersede the §3 rationale? | **No.** The parser derivation is **applied**; the ingest/bridge and `SOW-063` clauses are retained **verbatim** |

**Re-affirmed: no `Supersession_Delta.csv` binding is owed.** Gate 5 carries
SCA-001's header-only map forward:

```bash
python3 tools/coordination/accumulate_supersession_map.py \
  --prior-map projects/pec/execution/_ScopeChange/SCA-001_2026-07-24_2206/Supersession_Map.csv \
  --output-map projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Supersession_Map.csv \
  --allow-empty
```

**One caveat, stated rather than buried.** This re-affirmation is only as
strong as the attributions the owner actually approves. If the owner selects
alternative **(c)** for `DEL-00-03` (`OBJ-006`, the measurement objective) the
conclusion still holds — it remains a reading of PRD text, not a contradiction
of it. No option on the table creates a binding.

---

## Part 5 — Gate 3 approval question

**Do you approve these amendments to the decomposition document?**

Structured so most of it can be approved at once:

**Q1 — the three genuinely ambiguous attributions** (rule per row):
1. `DEL-00-03` / `SOW-089` — **(a)** `OBJ-001` *(recommended)*, **(b)**
   full-span five-objective set, or **(c)** `OBJ-006`?
2. `DEL-00-01` / `SOW-088` — `OBJ-005` *(recommended)* or `OBJ-003`?
3. `DEL-08-01` / `SOW-003` — `OBJ-001` *(recommended)* or `OBJ-001;OBJ-004`?

**Q2 — the INDIRECT-8 breadth:** affirm `[OBJ-001, OBJ-002]` for all eight
*(recommended, faithful to §3)*, or narrow the seven parsers to `OBJ-001`
only and leave OBJ-002 to the reconciler layer?

**Q3 — §3 table header (A003a):** drop "(best-effort)" from the
`Mapped Scope Items` column *(recommended — the qualifier described the
posture A004 is retiring)*, or retain it since 11 residue rows remain?

**Q4 — A008:** approve the front-matter revision block as an eighth action?
Declining leaves revision 1.2 self-contradictory, so a decline should come
with direction on how else to reconcile it.

**Q5 — everything else:** approve A001, A002, A003b–d, A004, A005, A006, A007
as drafted?

The six remaining attributions (rows 3, 4, 5, 6, 8, 9) are HIGH or
MEDIUM-HIGH with direct PRD warrants and are folded into Q5 rather than asked
individually.
