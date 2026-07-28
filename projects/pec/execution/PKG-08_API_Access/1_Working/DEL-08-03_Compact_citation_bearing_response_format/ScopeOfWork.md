---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-08-03
package_id: PKG-08
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@11a494e9a
project_scope_refs: [SOW-043]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-08-03 Compact citation-bearing response format

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-08-03` — "Compact
citation-bearing response format" — in `PKG-08` API & Access of the PEC v2
build. It covers project scope item `SOW-043` in service of package objective
`OBJ-001`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.3** (`current_basis`, SCA-003 successor), pinned at merge
`11a494e9a`. The deliverable-local `_REFERENCES.md` now cites that current
basis under the reference-parity integration at `af62343d3`. `_CONTEXT.md`
retains the revision-1.1 to revision-1.2 supersession trace; SCA-003 in turn
establishes revision 1.3 as the current successor. This contract cites
revision 1.3.

**Objective warrant (register-direct, pre-SCA-002).** The mapping
`SOW-043` → `OBJ-001` is the register's own and is unchanged by the SCA-002
amendment. Three independent tests in the SCA-002 record agree, each checked
against the record rather than inherited.

First, `SOW-043` is not among the twenty ledger rows whose empty `ObjectiveIDs`
cell action `A001` populated:

> | A001 | `MODIFY` | `OBJECTIVE` | `ScopeLedger.csv` `ObjectiveIDs` — **20 IN rows** (`SOW-001, 003, 011..017, 021, 025, 040, 042, 052, 053, 054, 056, 088, 089, 094`) | Populate `ObjectiveIDs` with bare `;`-separated `OBJ-NNN` tokens, derived by the intake §4 attribution method. **Binding constraint: `SOW-021` ⊆ `{OBJ-005}`** (see F-2) | Unit Ledger (§6 + `ScopeLedger.csv`) |
>
> (`_ScopeChange/SCA-002_2026-07-25_1042/Brief.md`, action-register row `A001`,
> quoted in full across all six cells. The `..` range is the source's own
> notation, not an elision. ID-shaped text inside this quotation is upstream
> source context, not a local definition or reference.)

Second, `DEL-08-03` is not among the seventeen deliverable rows whose empty
`SupportsObjectives` cell action `A002` populated:

> | A002 | `MODIFY` | `DELIVERABLE` | `Deliverables.csv` `SupportsObjectives` — **17 deliverable rows** (`DEL-00-01, 00-03, 01-01, 01-03, 01-05, 01-06, 02-01..07, 03-06, 08-01, 08-02, 10-03`) | Populate `SupportsObjectives` so the §3 union invariant holds file-wide | Secondary Entities (§5 + `Deliverables.csv`) |
>
> (`Brief.md`, action-register row `A002`, quoted in full across all six cells.
> The `..` range is the source's own notation. ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference.)

Third, the objective side says the same directly. The recorded old and new text
of the `OBJ-001` §3 row names both this scope item and this deliverable on the
**old** side, before the amendment touched anything:

> ```
> OLD col4: SOW-004..009, SOW-041, SOW-043; instruments: SOW-058, SOW-059
> NEW col4: SOW-001, SOW-003, SOW-004..009, SOW-011..017, SOW-040..043, SOW-089; instruments: SOW-058, SOW-059
> OLD col5: DEL-04-01..05, DEL-08-03, DEL-08-04, DEL-10-01, DEL-10-04
> NEW col5: DEL-00-03, DEL-01-01, DEL-02-01..07, DEL-04-01..05, DEL-08-01..04, DEL-10-01, DEL-10-04
> ```
>
> (`Amendment_Preview.md`, action `A003b`, "Line 320 · `OBJ-001`"; all four
> lines of the block quoted in full, none elided. The `..` ranges are the
> source's own notation. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

`SOW-043` is named literally in the `OLD col4` text and `DEL-08-03` literally in
the `OLD col5` text. The mapping is therefore register-direct at both levels and
predates SCA-002. This contract records it rather than deriving it, asserts no
confidence label for it because the record assigns none, and creates no
owner-confirmation acceptance criterion for it.

One further appearance in the same record corroborates the mapping at its
actual strength, which is that of a **measured register precedent, not a
ruling**:

> | D-15 | Four **register precedents** measured and used as attribution anchors | `SOW-010`→`OBJ-005` (rebuild/store cluster), ~~`SOW-055`/`DEL-10-02`→`OBJ-005`~~ **withdrawn by C-18 as tautological** — `SOW-055` restates OBJ-005 nearly verbatim and selects nothing for `SOW-025`, `DEL-08-03/04`→`OBJ-001` (PKG-08 transport), `SOW-018/019`→`OBJ-002` (reconciler layer). Anchoring to accepted register facts beats inventing a fresh rationale per row. |
>
> (`Decision_Log.md`, row `D-15`, quoted in full across all three cells. The
> strikethrough and the withdrawal note are the source's own. ID-shaped text
> inside this quotation is upstream source context, not a local definition or
> reference.)

That row uses this deliverable's pre-existing attribution as an anchor for
*other* rows' attributions. It is evidence that the attribution was measured and
relied upon in the amendment, not an act that created or re-ruled it.

Source chain, in order of authority for this contract:

1. `execution/_Decomposition/ScopeLedger.csv`, row `SOW-043` (CLM-002).
2. `docs/PRD.md` §9.6, requirement `PEC-API-004`, the ledger row's `SourceRef`
   (CLM-002).
3. `execution/_Decomposition/SOFTWARE_DECOMP.md` §5 `PKG-08` row and
   `Deliverables.csv` row `DEL-08-03` (CLM-001), with the §4 package charter
   (CLM-002) and the §3 `OBJ-001` row (CLM-003).
4. Deliverable-local control files: `_CONTEXT.md`, `_REFERENCES.md`,
   `_DEPENDENCIES.md`, `Dependencies.csv`, `_STATUS.md` (CLM-004, CLM-005).
5. The two upstream `INITIALIZED` contracts, `DEL-08-02` and `DEL-04-03`
   (CLM-006, CLM-007).

## Deliverable Definition — Ontology

- **CLM-001** — The register identity of record. `Deliverables.csv` holds one row for this deliverable, under the columns `DeliverableID,PackageID,Name,Description,Type,ResponsibleParty,AnticipatedArtifacts,CoversScopeItems,SupportsObjectives,ContextEnvelope,ContextEnvelopeNotes,PhaseHint`:

> ```
> DEL-08-03,PKG-08,Compact citation-bearing response format,Machine-first response envelope carrying citations.,API_CONTRACT,TBD,Format spec + serializer + tests,SOW-043,OBJ-001,S,,P1
> ```
>
> (`Deliverables.csv`, row `DEL-08-03`, quoted in full. `ResponsibleParty` is
> the literal token `TBD`; `ContextEnvelopeNotes` is empty. ID-shaped text
> inside this quotation is upstream source context, not a local definition or
> reference.)

  The `SOFTWARE_DECOMP.md` §5 `PKG-08` table repeats the compact control fields: "| DEL-08-03 | Compact citation-bearing response format | API_CONTRACT | S | P1 | SOW-043 |". `ContextEnvelopeNotes` being empty is why `_CONTEXT.md` records "(none)" under envelope notes: there are none to carry. `ContextBudgetQA.csv` records this deliverable, under the columns `DeliverableID,PackageID,ContextEnvelope,Risk,RecommendedAction,Notes`, as "DEL-08-03,PKG-08,S,LOW,None," — envelope `S`, risk `LOW`, recommended action `None`, `Notes` empty. `ResponsibleParty` is `TBD` throughout the register by the §5 preamble convention recorded at `DL-13`(c): assignment happens at WORKING_ITEMS activation, not here (TBD-001).

- **CLM-002** — The covered scope item and its cited source. `ScopeLedger.csv` holds one row for `SOW-043`, under the columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`:

> ```
> SOW-043,IN,"Return compact, machine-first, citation-bearing responses",PEC-API-004,PKG-08,DEL-08-03,OBJ-001,,FALSE,
> ```
>
> (`ScopeLedger.csv`, row `SOW-043`, quoted in full. `DecisionRef` empty;
> `OpenIssue` `FALSE`; `Notes` empty — this item carries no forced-assignment
> decision, no open issue, and no ledger note. ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference.)

  The `SourceRef` cell names one `PRD.md` §9.6 requirement, which reads in full: "| PEC-API-004 | Responses are compact, machine-first, and citation-bearing. |". The `SOFTWARE_DECOMP.md` §2 SSOW row for the same item repeats the statement without the register-only columns and carries an empty note cell: "| SOW-043 | IN | Return compact, machine-first, citation-bearing responses | PEC-API-004 | |". The `PKG-08` charter (`SOFTWARE_DECOMP.md` §4) places the item: "| PKG-08 | API & Access | The machine-consumer surface: Unix-socket binding, token-scoped access classes, p95 latency, versioned additive schema, compact citation-bearing responses, SSE subscription | SOW-003, 040..044 (6) | Dashboard rendering (PKG-09) |". Of that six-item charter this deliverable covers exactly one, and the charter's stated exclusion — dashboard rendering — binds it directly (REQ-010). The reciprocal exclusion is recorded on the other side: the `PKG-04` charter lists "Transport (PKG-08); rendering (PKG-09)" as outside its own scope, so the wire surface is `PKG-08`'s by both charters.

- **CLM-003** — The objective and what this deliverable contributes to it. `OBJ-001` reads, under the §3 columns `ObjectiveID,Statement,SourceRef,Mapped Scope Items,MappedDeliverables`:

> | OBJ-001 | Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation | §3.1 | SOW-001, SOW-003, SOW-004..009, SOW-011..017, SOW-040..043, SOW-089; instruments: SOW-058, SOW-059 | DEL-00-03, DEL-01-01, DEL-02-01..07, DEL-04-01..05, DEL-08-01..04, DEL-10-01, DEL-10-04 |
>
> (`SOFTWARE_DECOMP.md` §3, row `OBJ-001`, quoted in full across all five cells.
> The `..` ranges are the source's own notation. ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference.)

  The objective is a cross-package outcome whose deliverable set is the whole `MappedDeliverables` cell; no single deliverable discharges it. This deliverable is the wire limb: the objective's "per-claim citations" clause is produced by the citation layer (CLM-007) and reaches a machine consumer only if the response envelope carries it, which is the act `SOW-043` names.

- **CLM-004** — Placement in the accepted work graph. This deliverable's `Dependencies.csv` holds four rows at `RegisterSchemaVersion` `v3.1`. Two are `ANCHOR` rows — `DEP-08-03-001` (`AnchorType` `IMPLEMENTS_NODE`, package-local to `PKG-08`) and `DEP-08-03-002` (`AnchorType` `TRACES_TO_REQUIREMENT`, the `SOW-043` requirement trace) — both `SatisfactionStatus` `SATISFIED`, `Confidence` `HIGH`, `Origin` `DECLARED`. Two are `EXECUTION` rows, both `Direction` `UPSTREAM`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, `Status` `ACTIVE`:
    - `DEP-08-03-003` — `TargetDeliverableID` `DEL-08-02`, `TargetName` "Versioned additive API schema", `Statement` "R3-F4: envelope is schema-governed", `SourceRef` and `EvidenceQuote` both "SOW-042 additive versioned schema governs the response surface", `Notes` "PROPOSAL; Flag=none; EdgeID=E-N11".
    - `DEP-08-03-004` — `TargetDeliverableID` `DEL-04-03`, `TargetName` "Citation & freshness stamping", `Statement` "Response format carries citations produced by the citation layer", `SourceRef` "location TBD", `EvidenceQuote` **empty**, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P53".

  Both edges are legible independently from the accepted gate exhibit, whose §4.1 columns are `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`:

> ```
> E-P53,DEL-04-03,DEL-08-03,PROPOSAL,CONSUMES,,,Response format carries citations produced by the citation layer
> E-N11,DEL-08-02,DEL-08-03,PROPOSAL,CONSUMES,,SOW-042 additive versioned schema governs the response surface,R3-F4: envelope is schema-governed
> ```
>
> (`PLAN_2026-07-25_project_setup_dag_gate.md` §4.1, both rows quoted in full.
> `[E-P53]`'s `Flag` and `BasisCitation` cells are both empty; `[E-N11]`'s
> `Flag` cell is empty and its `BasisCitation` cell is populated. ID-shaped text
> inside this quotation is upstream source context, not a local definition or
> reference.)

  **Two register observations are recorded here rather than smoothed over.** First, `DEP-08-03-004` cites its evidence file without an in-file locus and without a quoted span: its `SourceRef` reads "location TBD" and its `EvidenceQuote` is empty. The exhibit row explains why — `[E-P53]` has an empty `BasisCitation` cell, so there was no basis text to carry — but that is an explanation, not a substitute; the register row remains one that names no locus. This contract neither supplies a locus nor invents a quotation for it. Second, the local register's mapping of `[E-N11]`'s exhibit cells is asymmetric: the exhibit's `BasisCitation` text lands in **both** the `SourceRef` and the `EvidenceQuote` columns of `DEP-08-03-003`, and the exhibit's `Rationale` text lands in its `Statement` column. Both observations are of the class `OI-013` records — that no durable register validator exists, the coverage and coupling assertions having run in a session-local generator that "is not part of this package and enforces nothing after acceptance" — and neither is a defect this contract is authorized to repair (AX-007).

  Two register-wide non-gating constraints apply, as `_DEPENDENCIES.md` records them: **C-04 (PHASE_PRECEDENCE)** — "Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling" — and **C-10 (STRATUM_RULE)**, whose text ends "All strata require owner acceptance; strata are provenance not authority". No constraint in the exhibit's §4.2 register names this deliverable as a party.

- **CLM-005** — Two downstream consumer relations are recorded in `_DEPENDENCIES.md` and marked informational; neither holds a row in this deliverable's `Dependencies.csv`, because downstream rows live in each consumer's own local register per the deliverable-local storage ruling of `D-PEC-62`. The exhibit rows read:

> ```
> E-N07,DEL-08-03,DEL-09-06,PROPOSAL,CONSUMES,,as E-N06,R3-F1: views consume the citation-bearing envelope
> E-N12,DEL-08-03,DEL-08-04,PROPOSAL,TESTS,,,R3-F4: serializer sits on the measured p95 latency path
> ```
>
> (`PLAN_2026-07-25_project_setup_dag_gate.md` §4.1, both rows quoted in full.
> Both are `PROPOSAL`; both `Flag` cells are empty. ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference.)

  Both run *from* this deliverable outward. Being consumed by the universal drill-down component and sitting on the path a latency test measures transfers none of their scope into this contract and imposes no obligation on them (AX-006). In particular, `[E-N12]`'s rationale states an adjacency, not an obligation: the latency budget is `SOW-041` → `DEL-08-04`, whose accepted contract remains separate, and no latency threshold, budget, or measurement enters here (REQ-010, CON-001).

- **CLM-006** — Upstream `[E-N11]`: the envelope is schema-governed. `DEL-08-02` is at lifecycle state `INITIALIZED`, which is the maturity the edge requires. `INITIALIZED` means the upstream **contract** is the reliable input: an accepted `ScopeOfWork.md` exists, and no schema artifact, version identifier, or compatibility check does. Nothing in this contract asserts that any upstream artifact exists. What that contract obliges, and what it hands to this one, it states in its own voice:

> - **REQ-001** — The API schema shall be versioned: OUT-001 shall carry an explicit, machine-readable version identifier that a consumer can bind to.
> - **REQ-003** — OUT-001 shall define the machine-consumer surface of PKG-08 so that the orientation reads OBJ-001 describes can be issued and interpreted against a named schema version rather than against an undeclared shape.
> - **CLM-004** — Transport binding, token-scoped access classes, latency budget, response compactness and citation-bearing form, and SSE subscription belong to sibling PKG-08 deliverables (`DEL-08-01`, `DEL-08-03`, `DEL-08-04`, `DEL-08-05`) per the accepted §5 package table; they are out of scope for `DEL-08-02`.
> - **AX-005** — Additive-only evolution is a constraint on this deliverable's own artifacts. It does not authorize `DEL-08-02` to constrain, define, or pre-empt the scope of the consuming deliverables named in CLM-002.
>
> (`DEL-08-02/ScopeOfWork.md`, Epistemology, Ontology, and Axiology sections;
> all four records quoted in full, none elided. ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference —
> this contract's own `REQ-*`, `CLM-*`, and `AX-*` records are separate and
> differently worded.)

  Three consequences bind this contract. The envelope's shapes are members of a schema whose definition and version identifier the upstream contract owns, so this contract's format specification names the version it belongs to rather than declaring a second schema (REQ-004). The upstream contract disclaims response compactness and citation-bearing form in explicit terms, which is the accepted basis on which this contract takes those properties. And its axiology limits what its additive posture may do to a consumer: the additive floor constrains the schema artifact, and this contract adopts it as a constraint on its own envelope evolution rather than receiving it as an imposed obligation.

- **CLM-007** — Upstream `[E-P53]`: the citations the envelope carries are produced elsewhere. `DEL-04-03` is at `INITIALIZED` — again, contract, not artifact. Its accepted contract names this deliverable as the owner of the wire envelope and its serialization:

> … the compact, machine-first, citation-bearing response envelope and serializer are `DEL-08-03` (`SOW-043`, `PEC-API-004`) …
>
> (`DEL-04-03/ScopeOfWork.md`, Ontology section, `CLM-016`. **Elided:** this is
> one clause lifted from a long semicolon-separated enumeration of adjacent
> acts; the leading and trailing ellipses are this contract's, marking text
> elided before and after the clause. Both elisions are enumerated in the
> quotation record. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  What that contract obliges, and what it hands over, it states in its own voice:

> - **REQ-002** — Every claim in a stamped orientation response shall carry a citation that resolves to its live source as file path, anchor, and/or SHA, per `SOW-007` and `PEC-ORI-004`, with no claim class exempted (CLM-002, CLM-003, CLM-008, CON-004).
> - **REQ-008** — Where a claim's provenance is absent or does not resolve, or where a stamp field's value is not carried, the layer shall neither emit the claim or field with a fabricated or approximate value nor drop it silently: the absence shall be stated against the affected claim or field and recorded so that it is available to the deliverable that renders measurement limitations. Silent omission is prohibited (`PEC-ORI-006`), and the posture is `PRD.md` §7.3's coverage honesty — "a figure the records don't support is absent and said to be absent". Rendering such a limitation into an orientation response is `DEL-04-05`'s act under `SOW-009` (CLM-016); this layer makes it available to that act.
> - **REQ-010** — The layer shall perform no act owned by another deliverable. In particular it shall compose no orientation return, serve no delta since a caller-supplied SHA, parameterize no response by scope, render no measurement limitation, define or emit no wire envelope or serialization format, implement no socket binding, token check, or subscription, render no dashboard or drill-down view, evaluate no pressure or staleness rule, perform no rebuild, incremental reconcile, or drift classification, enforce no presence-store TTL or guard, and measure no defect rate, latency, or adoption; each is cited to its owner in CLM-016 and none is discharged here.
>
> (`DEL-04-03/ScopeOfWork.md`, Epistemology section; all three records quoted in
> full, none elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  Three consequences bind this contract. The citation values and the three stamp fields are produced upstream and are carried, never made, here (REQ-008). The upstream contract's explicit disclaimer of any wire envelope or serialization format is the accepted basis on which this contract defines one, and it is also the boundary: nothing this contract defines may re-perform the attaching or the stamping. And the absence semantics the upstream contract requires — a stated absence rather than a silent drop — arrive at the envelope as content that must survive serialization intact (REQ-009), while rendering a measurement limitation remains `DEL-04-05`'s act.

- **CLM-008** — Two upstream records condition what the envelope must be able to carry, and this contract carries the conditioning rather than resolving it. On what the envelope must carry per claim:

> - **CON-004** — What counts as a *claim* in an orientation response is not enumerated by any accepted source, so the granularity at which `PEC-ORI-004`'s universal quantifier bites is unsettled. The upstream return contract fixes the response's structure — six named components, each carrying its own provenance (CLM-011) — but whether a claim is a whole component, a field within a component, or a derived assertion about one is stated nowhere. The consequences differ: at component granularity, one citation per component satisfies the requirement; at field granularity, a component assembled from several entities needs several. The corpus pressure runs toward the finer reading — `PEC-K-08` requires that "Every status, verdict, and warning carries rule ID, threshold, and contributing cited sources. Drill-down never dead-ends", and `SOW-050` obliges drill-down "from every displayed value to its cited source" — but neither is this deliverable's scope item and neither states a claim granularity for `SOW-007`. This contract obliges full coverage at whatever granularity the response presents (REQ-002, REQ-012) and obliges the adopted granularity to be declared (REQ-014); it does not choose it here, and the choice is a production decision bounded by those requirements rather than a licence to exempt a claim class.
>
> (`DEL-04-03/ScopeOfWork.md`, Epistemology section; quoted in full, not elided.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

  And on what the stamp's SHA field carries:

> - **CON-002** — Which value the stamp's examined-through SHA carries, and where that value originates, is unsettled by the accepted sources on two axes. On representation, the upstream return contract's own `CON-003`, quoted at CLM-012, records that the SHA appears both as a component of the composed return and inside this deliverable's response stamp, and that "no accepted source states whether the two are the same field"; ownership of the stamping act is not in doubt, representation is. On origin, no accepted source states whether the stamped value is the reconcile-side examined-SHA baseline that keyed the reconcile — `SOW-018`, "Run reconciliation incrementally, keyed on Git delta since the last examined SHA" (`SourceRef` `PEC-RCN-003`, whose own `PRD.md` §9.2 wording differs), covered by `DEL-03-02` — or a value obtained per response. This contract does not close either axis: REQ-004 fixes that whatever value is stamped is obtained structurally and never judged, and REQ-013 obliges the production choice and its basis to be declared in the derivation record so the question stays visible to review and to any later scope change.
>
> (`DEL-04-03/ScopeOfWork.md`, Epistemology section; quoted in full, not elided.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

  Neither is resolved here, and neither may be resolved *by* an envelope decision. The envelope's per-claim citation carriage must accommodate whatever granularity the upstream layer adopts, without the format itself deciding it (CON-004); and the envelope's stamp carriage must accommodate the SHA value as the upstream layer presents it, without the format fixing a representation the accepted sources leave open (CON-002).

- **CLM-009** — The acts adjacent to this one are owned elsewhere and are cited here, never discharged. Composing the per-loop orientation return is `DEL-04-01` (`SOW-004`, `PEC-ORI-001`); serving deltas since a caller-supplied commit SHA is `DEL-04-02` (`SOW-005`, `PEC-ORI-002`); producing per-claim citations and the three-field response stamp is `DEL-04-03` (`SOW-006`, `SOW-007`, `PEC-ORI-003`, `PEC-ORI-004`); parameterizing orientation by scope is `DEL-04-04` (`SOW-008`, `PEC-ORI-005`); rendering a measurement limitation where a feed is unparseable or stale is `DEL-04-05` (`SOW-009`, `PEC-ORI-006`). Within `PKG-08`: binding the service local-only on a Unix socket and implementing the three token-scoped access classes is `DEL-08-01` (`SOW-003`, `§8`; `SOW-040`, `PEC-API-001`); defining and versioning the API schema is `DEL-08-02` (`SOW-042`, `PEC-API-003`); the orientation latency budget and its measurement is `DEL-08-04` (`SOW-041`, `PEC-API-002`); the SSE delta and presence subscription is `DEL-08-05` (`SOW-044`, `PEC-API-005`). Outside both: the record-tier entity model whose provenance every citation resolves is `DEL-01-01` (`SOW-001`); the zero-dependency and no-egress posture is `DEL-01-05` (`SOW-052`, `SOW-053`); the presence-store TTL machinery and the presence-side limb of the citation-exclusion guard is `DEL-06-05` (`SOW-030`, `SOW-032`); dashboard rendering is `DEL-09-01` through `DEL-09-05` (`SOW-045` through `SOW-049`); resolving a citation to its source in the universal drill-down component is `DEL-09-06` (`SOW-050`, `PEC-DSH-006`). This contract produces only the format specification, the serializer, and their tests.
- **CLM-010** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: this deliverable is `P1`; both upstream predecessors are `P1` (`DEL-08-02`, `DEL-04-03`). Its two recorded consumers are `P1` (`DEL-08-04`) and `P2` (`DEL-09-06`). Other deliverables named as owners of adjacent scope are `P1` (`DEL-01-01`, `DEL-01-05`, `DEL-04-01`, `DEL-04-02`, `DEL-04-05`, `DEL-08-01`), `P2` (`DEL-04-04`, `DEL-09-01`, `DEL-09-02`, `DEL-09-03`, `DEL-09-04`), `P3` (`DEL-06-05`, `DEL-09-05`), and `P4` (`DEL-08-05`). No consumer precedes this deliverable's phase, and no claim in this contract stages any named deliverable into a different phase.
- **CLM-011** — The deliverable is at lifecycle state `INITIALIZED` with no implementation present: `_STATUS.md` records "**Current State:** INITIALIZED". No format specification, no serializer, no envelope, and no test exists. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.

The outputs are bounded by the register's `AnticipatedArtifacts` naming,
"Format spec + serializer + tests" (CLM-001) — three artifacts, and no fourth.

- **OUT-001** — The response-format specification: the document that defines the compact, machine-first, citation-bearing response envelope for the `PKG-08` API surface — its field set, the place and shape in which a per-claim citation is carried, the place and shape in which the three-field response stamp is carried, the schema version its shapes belong to, and the declarations REQ-012 requires. Its **format declaration record** — the section in which the specification states its operative reading of compactness and of machine-first form, the wire representation it selects, and the upstream open readings it accommodates without resolving — is a component of this output rather than a fourth artifact: it is the specification's own self-declaration, so the register's naming of exactly three artifacts is preserved.
- **OUT-002** — The serializer: the component that renders a composed orientation response into an instance of the OUT-001 envelope, carrying through every citation, stamp field, and stated absence the composed response presents, and adding nothing.
- **OUT-003** — An automated test suite covering carry-through fidelity, citation and stamp carriage, schema-version conformance and additive envelope evolution, machine-first parse, the declared compactness rule, content-minimality, the no-synthesis boundary, absence carriage, and the adjacent-act boundary, implementing the verification methods declared in this contract.

Unresolved information carried forward, not invented:

- **TBD-001** — `ResponsibleParty` is unassigned; the register records the literal token `TBD` in both `Deliverables.csv` and `_CONTEXT.md`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble convention, `DL-13`(c)).
- **TBD-002** — The concrete wire representation of the envelope (for example a JSON encoding versus a binary encoding), the language and location of the OUT-001 specification document, and the module location and entry point of OUT-002 are fixed by no accepted source. The one adjacent open decision in the corpus is a *transport* question, not a representation one: the `SOW-083` scope-item statement reads "Event-contract home (shared runtime contracts vs PEC-local schema + pinned mirror) and API transport (Unix socket only vs additional loopback listener)" with `SourceRef` `§16.9`, and that surface is `DEL-08-01`'s. Neither the `PRD.md` §16 list nor `PEC-API-004` states a wire representation for a response body. The choice is production work bounded by REQ-004 through REQ-006 and declared under REQ-012.
- **TBD-003** — The envelope's full field set is not enumerated by any accepted source. What the accepted corpus fixes is that the envelope carries per-claim citations (`SOW-007`, `PEC-ORI-004`), the three stamp fields (`SOW-006`, `PEC-ORI-003`, `PEC-K-04`), and a schema version binding (`SOW-042`, `PEC-API-003`). Whether any further field exists, and what it is, is a production decision bounded by REQ-006 and declared under REQ-012; no field may be added on this contract's authority.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a specification, a serializer, an envelope, an
orientation response, a citation layer, a schema, or a test exists.

- **REQ-001** — The serializer shall carry through, into the envelope instance, every citation, every stamp field, and every stated absence the composed orientation response presents, altering none of their values and dropping none of them; and it shall add no claim, citation, stamp field, or value the composed response does not present. Serialization is a representation act, not a content act.
- **REQ-002** — The envelope shall define the place and shape in which a per-claim citation is carried, such that each citation's constituents as the citation layer produces them — file path, anchor, and/or SHA — survive serialization individually and remain individually addressable by a machine consumer. The envelope shall place no ceiling on the number of citations carried and shall exempt no claim class from carrying one; the granularity at which claims are counted is the upstream layer's adopted granularity and is not decided by the envelope (CON-004).
- **REQ-003** — The envelope shall define the place and shape in which the response-level stamp is carried, providing for all three fields `PEC-ORI-003` names — the examined-through SHA, the generation time, and per-feed freshness — with per-feed freshness carried per feed rather than collapsed into a single aggregate value, so that a consumer detects staleness structurally from the response as `PEC-K-04` requires: "**Staleness is a comparison.** Every response carries the examined-through commit SHA and per-feed freshness; consumers detect staleness structurally." The envelope shall fix no representation for the examined-through SHA field beyond what carrying the upstream value requires, because the accepted sources leave its representation and origin open (CON-002).
- **REQ-004** — The envelope's shapes shall be defined as members of the versioned API schema `DEL-08-02` owns, and every envelope instance shall resolve, from the artifact alone, which schema version it belongs to. This contract defines no second schema and no independent version identifier scheme. Successor envelope shapes shall satisfy the additive floor that upstream contract states — a successor adds to its predecessor without removing any element the predecessor published and without changing the meaning of any element the predecessor published — as a constraint this contract adopts for its own artifacts. This places no obligation on schema versions authored after this deliverable closes and asserts no standing enforcement mandate over them.
- **REQ-005** — The envelope shall be machine-first: an instance shall be parseable deterministically by a machine consumer without human-oriented layout, prose framing, or presentation markup, and shall carry no field whose only purpose is human display. The accepted sources identify explicitly PEC-enabled harnesses as possible machine consumers of the API on behalf of agent sessions. Under `PEC-K-03`, any such consumer chooses whether and when to request orientation and whether to inject labeled non-authoritative data; no polling, cadence, contact, or injection duty is asserted. The sources state no machine-first format criterion, so the operative reading shall be declared under REQ-012 rather than assumed (CON-003).
- **REQ-006** — The envelope shall be compact in a sense the specification declares and applies: the specification shall state the operative reading of compactness, the rule by which it is applied to field naming, structure, and repetition, and the evidence by which conformance to that rule is checked. No accepted source states a size metric, threshold, or budget for compactness (CON-001), so the declared rule is a production decision; it shall not be stated as, or presented as derived from, an accepted threshold, and it shall never be applied by dropping a citation, a stamp field, or a stated absence, which REQ-001 forbids.
- **REQ-007** — No envelope field shall carry file content or diff content, per `PEC-K-10`: "**Content-minimal.** Paths, counts, SHAs, states, hashes — never file or diff content." A citation carried in the envelope shall carry locating identity only and shall not reproduce, excerpt, summarize, or paraphrase the text it locates. Every citation carried shall resolve to the live governed source the upstream layer bound it to and none to a PEC artifact, store record, or generated view, per `PEC-K-02`: "PEC output is never citable as authority".
- **REQ-008** — The serializer shall synthesize, derive, infer, default, reformat, or recompute no citation constituent, no stamp field value, and no freshness value; it shall classify no value's trust tier and shall admit no presence-tier value into a citation position, per `PEC-K-05` ("Presence facts never enter record-tier citations"). Producing these values, and enforcing the citation-production limb of that exclusion, is `DEL-04-03`'s act; the presence-store guard limb is `DEL-06-05`'s (CLM-009). This deliverable's obligation is that serialization introduce no new value and no new classification of its own.
- **REQ-009** — Where the composed response states an absence — an unresolvable citation, an uncarried stamp field, or an unknown per-feed freshness value — the envelope shall provide for that stated absence to be carried and distinguishable from a value, and the serializer shall carry it rather than omitting the affected claim or field, substituting a default, or emitting an empty value indistinguishable from a real one. Deciding what a measurement limitation says and rendering it into a response is `DEL-04-05`'s act under `SOW-009` (CLM-009); this contract defines no limitation semantics and only obliges that the wire form not destroy what the response states.
- **REQ-010** — This deliverable shall perform no act owned by another deliverable. In particular it shall compose no orientation return, serve no delta since a caller-supplied SHA, produce no citation and stamp no response, parameterize no response by scope, render no measurement limitation, define or version no API schema, implement no socket binding, token check, or access class, define, measure, or assert no latency budget, implement no subscription, render no dashboard view, resolve no citation to its source in a drill-down component, define no record-tier entity type or provenance field, enforce no presence-store TTL or guard, and enforce no dependency or egress policy. Each of those acts is cited to a named owner in CLM-009 and none is discharged here.
- **REQ-011** — This deliverable and its tests shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053` and is not discharged here.
- **REQ-012** — The format declaration record — a component of OUT-001 required here — shall state, in readable form: the operative reading of compactness and the rule applied under REQ-006; the operative reading of machine-first form under REQ-005; the wire representation selected under TBD-002 and the reason it was selected; the full field set under TBD-003, with each field traced to the accepted source that requires it or marked as a production addition; the schema version binding under REQ-004; and, for each of the two upstream open readings, how the envelope accommodates it without resolving it — the per-claim citation granularity (CON-004) and the examined-through SHA representation and origin (CON-002). A field, a rule, or an accommodation produced by an undeclared reading is prohibited.
- **REQ-013** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria. Where a verification method cannot be executed because a counterpart artifact does not yet exist — a schema version to bind, a citation layer to produce citations, or an orientation return to serialize — the test shall record that fact rather than assert a passing result.

Acceptance criteria. Each states a property the future implementation must
exhibit; none asserts a present state.

- **AC-001** — For fixture composed orientation responses, every citation, every stamp field, and every stated absence present in the composed response is present in the serialized envelope instance with its value unaltered, byte for byte where the value is a string; the serialized instance contains no claim, citation, stamp field, or value absent from the composed response; and the round-trip inventory of carried elements matches the composed response's inventory exactly in both directions.
- **AC-002** — The delivered specification defines a per-claim citation carriage in which file path, anchor, and SHA are each individually addressable by a machine consumer; for fixture responses spanning every claim class the fixture contains, and for fixtures presenting claims at more than one granularity, every claim's citation is carried with its constituents individually recoverable; and neither the specification nor the serializer imposes a count ceiling on citations or exempts any claim class.
- **AC-003** — The delivered specification defines a response-stamp carriage providing for the examined-through SHA, the generation time, and per-feed freshness, with freshness carried as one entry per feed; for a fixture whose composed response reports multiple feeds, the serialized instance carries one freshness entry per reported feed and no aggregate substitute; and the specification fixes no representation for the examined-through SHA field beyond carrying the value the composed response presents.
- **AC-004** — Every envelope instance produced in a fixture run resolves, from the artifact alone, the schema version its shapes belong to; the specification defines no schema and no version identifier scheme of its own, naming instead the version owned upstream; and a check run over a seeded successor envelope shape passes a purely additive successor and fails a successor that removes a published element or changes a published element's meaning.
- **AC-005** — Fixture envelope instances parse deterministically under the declared machine-first reading with no human-oriented layout, prose framing, or presentation markup; the specification's field set contains no field whose stated purpose is human display; and the declared reading of machine-first form is present in the format declaration record and is not presented as fixed by an accepted source.
- **AC-006** — The format declaration record states the operative reading of compactness, the rule applied to field naming, structure, and repetition, and the conformance evidence; fixture envelope instances conform to that stated rule; no compactness threshold is presented as derived from an accepted source; and no fixture case exists in which applying the compactness rule drops a citation, a stamp field, or a stated absence.
- **AC-007** — For a content-dense fixture corpus carrying long prose bodies, authored ruling text, and diff-shaped content, inspection of every field of every serialized envelope instance finds no file content and no diff content, and no carried citation reproduces, excerpts, summarizes, or paraphrases the text it locates; and no citation in any fixture instance resolves to a PEC artifact, store record, or generated view.
- **AC-008** — For a fixture carrying presence-tier records alongside the record tier, no value in any citation position of a serialized instance derives from or resolves to a presence-tier record; this deliverable's source contains no citation-, stamp-, or freshness-value synthesis, derivation, inference, default, reformatting, or recomputation path, and no trust-tier classification path; and every value in a fixture instance is traceable to the identical value in the composed response.
- **AC-009** — For fixture composed responses carrying an unresolvable citation, an uncarried stamp field, and an unknown per-feed freshness value, each stated absence is carried in the serialized instance and is distinguishable by a consumer from a real value; no affected claim or field is omitted; no default or empty value is substituted; and this deliverable's source contains no limitation-rendering path and no limitation semantics of its own.
- **AC-010** — This deliverable's source and call graph contain no orientation-composition path, no delta-since-SHA path, no citation-production or response-stamping path, no scope-parameterization path, no limitation-rendering path, no schema definition or version-scheme path, no socket binding, token check, or access-class path, no latency budget, measurement, or assertion, no subscription path, no dashboard-rendering or drill-down-resolution path, no record-tier entity or provenance definition, no presence-store TTL or guard path, and no dependency or egress enforcement path; and no test in this deliverable asserts a criterion belonging to any of them.
- **AC-011** — This deliverable and its tests add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact and undischarged here.
- **AC-012** — The format declaration record — the component of OUT-001 required by REQ-012 — states the compactness reading and rule, the machine-first reading, the selected wire representation with its reason, the full field set with each field traced to its requiring source or marked a production addition, the schema-version binding, and the two accommodations for the upstream open readings; every field and rule exercised in a fixture run is traceable to a declaration in that record; and neither upstream open reading is presented as resolved.
- **AC-013** — The test suite implements VER-001 through VER-012, executes in the `PKG-08` test run, passes or records a pending result where a verification cannot execute because a counterpart artifact does not exist, and introduces no acceptance criterion absent from this contract.
- **AC-014** — The REVIEW gate confirms this contract's traceability to `SOW-043` and `OBJ-001`; confirms the objective mapping is stated as register-direct and pre-SCA-002 with no confidence label the record does not carry and no owner-confirmation criterion attached to it; confirms both upstream edges and both downstream relations are stated at their recorded `PROPOSAL` stratum; confirms the two `Dependencies.csv` register-hygiene observations at CLM-004 are recorded as observations rather than repaired; confirms the four unresolved records CON-001 through CON-004 are carried rather than decided; and confirms that no `PKG-01`, `PKG-04`, `PKG-06`, sibling `PKG-08`, or `PKG-09` scope has been absorbed.

Unresolved conflicts, carried rather than decided:

- **CON-001** — "Compact" is stated as a property of responses by `PEC-API-004` and restated by `SOW-043`, and no accepted source defines it, measures it, or sets a threshold for it. The nearest measured budget in the corpus is `PEC-API-002` — "Orientation reads shall complete in ≤100 ms at p95 against the current corpus (latency-sensitive pull path; any session-start use requires a separately adopted consumer duty)" — which enters scope as `SOW-041` and is covered by `DEL-08-04`, a different deliverable with its own accepted contract. The gate exhibit records the adjacency and nothing stronger: `[E-N12]`'s rationale reads "R3-F4: serializer sits on the measured p95 latency path", a `PROPOSAL`-stratum `TESTS` edge running outward from this deliverable (CLM-005). Sitting on a measured path is not a budget allocated to this deliverable, and no accepted source allocates one. This contract therefore requires the operative reading of compactness to be declared and applied (REQ-006, REQ-012) and forbids it being presented as derived from an accepted threshold; it selects no metric, and none may be inferred from this document.
- **CON-002** — What the envelope's examined-through SHA field carries is conditioned by an unresolved upstream question and cannot be closed here. `DEL-04-03`'s own `CON-002`, quoted in full at CLM-008, records that the SHA's representation is unsettled — "no accepted source states whether the two are the same field" — and that its origin is unsettled on a second axis. Ownership of the stamping act is not in doubt and is not this deliverable's. An envelope that fixed one representation would settle by format choice a question the accepted sources leave open, and would do so in the wrong place: the value's identity is the citation layer's to declare under its own requirements. This contract therefore obliges the stamp carriage to accommodate the value as presented (REQ-003) and obliges the accommodation to be declared (REQ-012), and takes no position on either axis.
- **CON-003** — "Machine-first" is stated as a property by `PEC-API-004` and restated by `SOW-043`, and no accepted source defines what makes a format machine-first. The corpus identifies explicitly enabled consumers but leaves consumption to their own authority: the consumer owns whether and when to request, its mode mapping and cadence, and any optional injection; PEC never forces contact or injection, and pipeline and unscoped-conversation modes may remain zero-contact. None of those rules states a format criterion, and §7.1's record-tier entity list is an information model rather than a wire form. This contract states the floor the term plainly bears in context — deterministic machine parse, no human-display-only field (REQ-005) — and obliges the operative reading to be declared (REQ-012); it does not extend the term beyond that floor, and a production choice may not read into it a criterion the accepted sources do not state.
- **CON-004** — What the envelope must carry per claim is conditioned by an unresolved upstream question and cannot be closed here. `DEL-04-03`'s own `CON-004`, quoted in full at CLM-008, records that "What counts as a *claim* in an orientation response is not enumerated by any accepted source" and that the choice between component, field, and derived-assertion granularity is a production decision bounded by that contract's requirements. The envelope inherits the consequence: a format that fixed one citation per component would foreclose the finer reading, and a format that assumed the finer reading would impose a structure no accepted source requires. This contract therefore obliges the carriage to be granularity-neutral — individually addressable citation constituents, no count ceiling, no exempt claim class (REQ-002) — and obliges the accommodation to be declared (REQ-012). Choosing the granularity is not this deliverable's act.

## Production and Verification Method — Praxeology

Production proceeds in the order upstream-contract survey → field set and
carriage shapes → schema-version binding → declaration record → serializer
carry-through path → absence carriage → compactness and machine-first
conformance → tests. The upstream-contract survey comes first because both
predecessors are at `INITIALIZED` and supply obligations rather than artifacts,
so a field set written against an imagined citation shape or an assumed schema
would violate REQ-004 and REQ-008 before any code existed. The declaration
record is authored before the serializer rather than after it, because REQ-006
and REQ-012 make the compactness rule a declared premise of the format: a rule
reverse-engineered from a finished serializer would document the implementation
instead of governing it, and the two accommodations for the upstream open
readings would be settled by implementation accident. Absence carriage is built
before compactness conformance for the same reason, because a format tuned for
size over complete fixtures acquires exactly the omissions REQ-001 and REQ-009
forbid.

All work is bounded to this deliverable folder and the `PKG-08` source it names.
This contract authorizes no register, decomposition, PRD, or upstream-deliverable
edit; it neither defines nor reshapes the schema its shapes belong to, the
citation layer whose values it carries, the return it serializes, the transport
that carries it, or the surfaces that render, resolve, or measure it. Tests
implement the verification methods below and create no scope.

- **VER-001** — Carry-through exercise: serialize fixture composed orientation responses and compare, element by element, the inventory of citations, stamp fields, and stated absences in the composed response against the inventory in the serialized instance; assert equality of values, assert no element present in one is absent from the other, and assert no element appears in the instance that the composed response does not present.
- **VER-002** — Citation-carriage exercise: inspect the delivered specification for a per-claim citation carriage in which file path, anchor, and SHA are individually addressable; serialize fixture responses spanning every claim class the fixture contains and fixtures presenting claims at more than one granularity, asserting per claim that its citation is carried with constituents individually recoverable; and search the specification and serializer for a citation count ceiling or an exempt claim class, asserting none.
- **VER-003** — Stamp-carriage exercise: inspect the specification for a stamp carriage providing all three `PEC-ORI-003` fields with freshness per feed; serialize a fixture whose composed response reports multiple feeds and assert one freshness entry per reported feed with no aggregate substitute; and inspect the specification for any fixed representation of the examined-through SHA beyond carrying the presented value, asserting none.
- **VER-004** — Schema-binding exercise: serialize fixture responses and assert each instance resolves its schema version from the artifact alone; search the specification for an independent schema definition or version identifier scheme, asserting none and asserting the version named is the one owned upstream; and run the additive check over a seeded purely additive successor envelope shape, a seeded successor removing a published element, and a seeded successor changing a published element's meaning, asserting pass, fail, and fail respectively.
- **VER-005** — Machine-first exercise: parse fixture envelope instances under the declared reading and assert deterministic parse; inspect the specification's field set for any field whose stated purpose is human display, and the instances for human-oriented layout, prose framing, or presentation markup, asserting none; and read the format declaration record to confirm the machine-first reading is declared and not presented as fixed by an accepted source.
- **VER-006** — Compactness exercise: read the format declaration record's compactness reading, rule, and conformance evidence; check fixture envelope instances against that stated rule; search the specification and declaration record for any compactness threshold presented as derived from an accepted source, asserting none; and serialize fixtures under the compactness rule asserting no citation, stamp field, or stated absence is dropped by its application.
- **VER-007** — Content inspection: serialize over a content-dense fixture corpus carrying long prose bodies, authored ruling text, and diff-shaped content, then dump every field of every instance and assert none carries file or diff content and no carried citation reproduces, excerpts, summarizes, or paraphrases the located text; and assert no citation in any instance resolves to a PEC artifact, store record, or generated view.
- **VER-008** — No-synthesis exercise: serialize over a fixture carrying presence-tier records alongside the record tier and assert no value in any citation position derives from or resolves to a presence-tier record; inspect this deliverable's source for citation-, stamp-, and freshness-value synthesis, derivation, inference, default, reformatting, and recomputation paths and for any trust-tier classification path, asserting none; and trace every value in a fixture instance to the identical value in the composed response.
- **VER-009** — Absence-carriage exercise: serialize fixture composed responses carrying an unresolvable citation, an uncarried stamp field, and an unknown per-feed freshness value; assert per case that the stated absence is carried, that a consumer can distinguish it from a real value, that no affected claim or field is omitted, and that no default or empty substitute appears; and inspect this deliverable's source for limitation-rendering paths and limitation semantics, asserting none.
- **VER-010** — Adjacent-act inspection: inspect this deliverable's call graph and source for orientation-composition, delta-since-SHA, citation-production and response-stamping, scope-parameterization, limitation-rendering, schema-definition and version-scheme, socket, token and access-class, latency budget and measurement, subscription, dashboard-rendering and drill-down-resolution, record-tier entity and provenance definition, presence-store TTL and guard, and dependency and egress enforcement paths, asserting each absent; and review this deliverable's tests for any criterion belonging to another deliverable, asserting none.
- **VER-011** — Inspect the `PKG-08` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` zero-dependency and locality enforcement once that deliverable is available, without discharging it here.
- **VER-012** — Declaration-record exercise: read the format declaration record and assert it states the compactness reading and rule, the machine-first reading, the selected wire representation with its reason, the full field set with each field traced to its requiring source or marked a production addition, the schema-version binding, and the two accommodations for the upstream open readings; assert neither open reading is presented as resolved; then serialize fixtures and assert each field and rule exercised is traceable to a declaration in that record.
- **VER-013** — Run the `PKG-08` test suite and confirm that each of VER-001 through VER-012 has a corresponding automated test that either executes and passes or records a pending result where a counterpart artifact does not exist, and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-001` governs this deliverable's reason for existing: orientation is a sub-second query with per-claim citations, not a session-length prose derivation. The citation layer makes an orientation answer checkable; the envelope is where checkability either survives contact with a machine consumer or quietly does not. A citation that is produced correctly and then flattened, truncated, or aggregated on the wire is indistinguishable, at the point of use, from a citation that was never produced — which is why REQ-001 forbids alteration rather than merely discouraging it, and why REQ-002 requires constituents to remain individually addressable rather than merely present.
- **AX-002** — Compactness is the one property in `PEC-API-004` that can be satisfied by removing something, and the corpus supplies no threshold at which removing becomes correct. That asymmetry is why REQ-006 makes compactness a declared and checked rule rather than a design instinct, and why it is subordinated to REQ-001: a format optimized for size against complete fixtures acquires the habit of dropping what is rarely populated, and what is rarely populated here is precisely the stated absence that `PEC-ORI-006` prohibits omitting silently. The absence of a metric (CON-001) is a reason to declare the reading, not a licence to choose one and call it accepted.
- **AX-003** — `PEC-K-04` fixes what the stamp is for: "consumers detect staleness structurally". Structural detection is a property of the wire form, not only of the value — a consumer that cannot locate the examined-through SHA and the per-feed freshness entries in the response it received cannot compare anything, whatever the citation layer computed. REQ-003 therefore binds the carriage per feed rather than in aggregate, because an aggregate freshness value is a judgment about the feeds rather than a comparison surface for them, and making that judgment on the wire would relocate a determination the invariant assigns to the consumer.
- **AX-004** — `PEC-K-10` content-minimal and `PEC-K-02`'s "PEC output is never citable as authority" bound what may appear in the envelope. A serializer is the last place text could enter a response and the first place a reader meets it, so the temptation to inline an excerpt beside a path is strongest exactly here and most invisible downstream. The strongest enforcement is upstream at the ingest guard and the citation layer; REQ-007 binds the wire side directly rather than relying on that.
- **AX-005** — Serialization is a representation act and never a content act. Every requirement that looks like a prohibition — no synthesis, no derivation, no default, no reformatting, no tier classification (REQ-008) — is one statement of that single value. It is load-bearing because the failure mode is silent: a serializer that normalizes a SHA's case, pads a freshness value, or supplies an empty string for an absent field produces output that looks correct and destroys the property the upstream contracts were written to guarantee.
- **AX-006** — Edge direction is a constraint on this contract, not a licence. Upstream, `RequiredMaturity` `INITIALIZED` on `[E-N11]` and `[E-P53]` means the upstream *contracts* are the reliable input, not any upstream artifact; this contract is written against the obligations quoted at CLM-006 through CLM-008 and asserts nothing about upstream implementation state. Downstream, being consumed by the drill-down component and sitting on the path a latency test measures neither expands this contract's scope nor transfers any of theirs into it — least of all the latency budget, which is `SOW-041`'s and belongs to `DEL-08-04` under its own accepted contract.
- **AX-007** — Stratum is provenance, not authority. `C-10` `STRATUM_RULE` ends "strata are provenance not authority", and the `D-PEC-62` packet (`_Coordination/_DECISIONS/D-PEC-62_project_setup_scaffold_and_local_dependency_registers.md` §1, item 4) accepted the DAG candidate — "accepted, all strata as presented" — and reads that acceptance as taking the exhibit "flags as flags", listing the specific annotations that "remain recorded-but-unresolved, non-gating"; none of the annotations it names is an edge or constraint this contract cites. All four edges this contract cites — `[E-N11]`, `[E-P53]`, `[E-N07]`, `[E-N12]` — are `PROPOSAL` with empty `Flag` cells. Citation converts none of them into anything stronger. The same discipline governs the two register-hygiene observations at CLM-004: `OI-013` records that no durable register validator exists, so a missing locus and an asymmetric column mapping are exactly the gaps nothing catches after acceptance. Recording them is this contract's act; repairing the register is not.
- **AX-008** — Unknowns stay marked. TBD-001 through TBD-003 and CON-001 through CON-004 are recorded rather than resolved by authoring judgment. Two of the four unresolved records are not this deliverable's to resolve at all: the claim granularity and the examined-through SHA's representation belong to the citation layer's own open records, and settling either by a format decision would take a determination in the wrong place while making it look like an implementation detail. Where the accepted sources are silent — on compactness, on machine-first form, on the wire representation, on the field set — this contract requires the choice to be declared rather than making it.
- **AX-009** — Local identifiers in this contract are local. Where this document refers to an upstream record it does so in qualified form or inside a quotation; a number shared with an upstream record is coincidence, not identity. This contract's CON-002 and CON-004 carry the upstream records of the same numbers and are not those records.
- **AX-010** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by this reconciliation; the deliverable is at `INITIALIZED` and nothing has been built. No requirement, criterion, or verification method below implies that any artifact exists, and no test result is asserted.

**Quotation record.** Every quotation in this contract is verbatim from the
named source. **Exactly one quotation is elided, and it carries exactly two
marked elisions**: the upstream boundary-enumeration clause quoted at CLM-007,
naming this deliverable as the owner of the wire envelope, where a leading
ellipsis marks text elided before the clause and a trailing ellipsis marks text
elided after it, both ellipses being this contract's and both marking omission
from a long semicolon-separated enumeration of adjacent acts. No other
quotation in this contract omits text from the span it presents, and no
ellipsis of this contract's making appears anywhere else — the document
contains exactly two ellipsis characters, both in that one quotation. Several
quotations present a contiguous fragment of a longer sentence or row rather
than the whole of it; those are partial quotations, not elided ones, because
the span each presents is complete and unbroken, and each is attributed to its
source where it appears. Two further points are noted so they are not mistaken
for elisions: every `..` range appearing inside a quotation in this contract —
in the `A001`, `A002`, and `A003b` quotations of the objective warrant, in the
`OBJ-001` §3 row at CLM-003, and in the `PKG-08` charter row at CLM-002 — is
the source's own range notation; and the strikethrough inside the `D-15` row is
that source's own. No annotation of this contract's making appears inside any
quotation.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-002 | SOW-043 OBJ-001 | REQ-001, CLM-007, AX-001, AX-005 | AC-001 | VER-001 | Element-by-element carry-through inventories for fixture composed responses and their serialized instances, matching in both directions with values unaltered |
| OUT-001 | SOW-043 OBJ-001 | REQ-002, CLM-007, CLM-008, CON-004 | AC-002 | VER-002 | Specification extract showing individually addressable citation constituents, per-claim carriage results across every fixture claim class and more than one granularity, and the search record showing no count ceiling and no exempt class |
| OUT-001 | SOW-043 OBJ-001 | REQ-003, CLM-007, CON-002, AX-003 | AC-003 | VER-003 | Specification extract showing the three-field stamp carriage with per-feed freshness entries, a multi-feed fixture instance carrying one entry per reported feed, and the inspection record showing no fixed SHA representation |
| OUT-001 | SOW-043 OBJ-001 | REQ-004, CLM-006, TBD-002 | AC-004 | VER-004 | Fixture instances resolving their schema version from the artifact alone, the search record showing no independent schema or version scheme, and additive-check outcomes over one additive, one element-removal, and one meaning-change successor shape |
| OUT-002 | SOW-043 OBJ-001 | REQ-005, CON-003 | AC-005 | VER-005 | Deterministic parse results over fixture instances, the field-set and instance inspection showing no human-display-only field or presentation markup, and the declaration record's machine-first reading |
| OUT-001 | SOW-043 OBJ-001 | REQ-006, CON-001, AX-002 | AC-006 | VER-006 | The declared compactness reading, rule, and conformance evidence with fixture instances checked against it, the search record showing no threshold presented as accepted, and the drop-free result under rule application |
| OUT-002 | SOW-043 OBJ-001 | REQ-007, AX-004 | AC-007 | VER-007 | Field-by-field dumps of fixture instances over a content-dense corpus showing no file or diff content, no reproduction of located text, and no citation resolving to a PEC artifact, store record, or generated view |
| OUT-002 | SOW-043 OBJ-001 | REQ-008, CLM-009, AX-005 | AC-008 | VER-008 | Presence-alongside-record fixture results showing no presence-derived citation value, the source inspection for synthesis, default, reformatting, and tier-classification paths, and per-value traces to the composed response |
| OUT-002 | SOW-043 OBJ-001 | REQ-009, CLM-007 | AC-009 | VER-009 | Per-case serialized instances for an unresolvable citation, an uncarried stamp field, and an unknown freshness value, each carrying a distinguishable stated absence, plus the source inspection showing no limitation semantics |
| OUT-002 | SOW-043 OBJ-001 | REQ-010, CLM-002, CLM-005, CLM-009, CLM-010, AX-006 | AC-010 | VER-010 | Call-graph and source inspection records showing each named adjacent path absent, plus a review of this deliverable's tests confirming no criterion belonging to another deliverable |
| OUT-002 | SOW-043 OBJ-001 | REQ-011 | AC-011 | VER-011 | Dependency-manifest and import-graph inspection records, plus the DEL-01-05 enforcement result once that deliverable is available |
| OUT-001 | SOW-043 OBJ-001 | REQ-012, TBD-003, CON-001, CON-002, CON-003, CON-004 | AC-012 | VER-012 | The format declaration record with its compactness and machine-first readings, selected wire representation and reason, traced field set, schema-version binding, and the two upstream accommodations, with fixture fields and rules traced to declarations |
| OUT-003 | SOW-043 OBJ-001 | REQ-013, CLM-011 | AC-013 | VER-013 | PKG-08 test-run output mapping each executed test to its declared verification method, with pending results recorded as pending, and no criterion asserted that this contract does not state |
| OUT-001 | SOW-043 OBJ-001 | CLM-001, CLM-003, CLM-004, TBD-001, AX-007, AX-008, AX-009, AX-010 | AC-014 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-043 and OBJ-001, confirms the objective mapping is stated as register-direct and pre-SCA-002 with no unrecorded confidence label and no owner-confirmation criterion, confirms both upstream edges and both downstream relations are stated at their recorded PROPOSAL stratum, confirms the two Dependencies.csv register-hygiene observations are recorded rather than repaired, confirms CON-001 through CON-004 are carried rather than decided, and confirms no cross-package or sibling scope absorption | Review record citing the SOW-043 ledger row, the A001/A002/A003b evidence for the pre-existing objective mapping, the four local register rows with their strata and recorded evidence-cell gaps, the two exhibit edge rows, and the two upstream contracts' quoted obligations |
