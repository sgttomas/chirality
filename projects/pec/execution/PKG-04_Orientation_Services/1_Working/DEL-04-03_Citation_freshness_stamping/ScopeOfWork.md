---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-03
package_id: PKG-04
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@11a494e9a
project_scope_refs: [SOW-006, SOW-007]
package_objective_refs: [OBJ-001, OBJ-002]
---

# Scope of Work — DEL-04-03 Citation & freshness stamping

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-04-03` — "Citation &
freshness stamping" — in `PKG-04` Orientation Services of the PEC v2 build. It
covers project scope items `SOW-006` and `SOW-007` in service of package
objectives `OBJ-001` and `OBJ-002`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.3** (`current_basis`, SCA-003 successor; accepted 2026-07-28 at
merge `11a494e9a`). The deliverable-local `_REFERENCES.md` now cites that
current basis under the reference-parity integration at `af62343d3`.
`_CONTEXT.md` retains the revision-1.1 to revision-1.2 supersession trace;
SCA-003 in turn establishes revision 1.3 as the current successor. This
contract cites revision 1.3.

**Objective warrant (register-direct, pre-SCA-002).** Both mappings are the
register's own and are unchanged by the scope-change amendment. Two independent
tests in the SCA-002 record agree, and each was checked against the record
rather than inherited. First, neither `SOW-006` nor `SOW-007` is among the
twenty ledger rows whose empty `ObjectiveIDs` cell action `A001` populated:

> `ScopeLedger.csv` `ObjectiveIDs` — **20 IN rows** (`SOW-001, 003, 011..017,
> 021, 025, 040, 042, 052, 053, 054, 056, 088, 089, 094`)
>
> (`Brief.md`, action-register row `A001`, target cell; the `..` range is the
> source's own notation, not an elision. ID-shaped text inside this quotation is
> upstream source context, not a local definition or reference.)

Second, `DEL-04-03` is not among the seventeen deliverable rows whose empty
`SupportsObjectives` cell action `A002` populated:

> `Deliverables.csv` `SupportsObjectives` — **17 deliverable rows** (`DEL-00-01,
> 00-03, 01-01, 01-03, 01-05, 01-06, 02-01..07, 03-06, 08-01, 08-02, 10-03`)
>
> (`Brief.md`, action-register row `A002`, target cell; the `..` range is the
> source's own notation. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

The §3 objective rows confirm the same from the objective side. The recorded
old and new text of the two objective rows this deliverable is mapped to reads:

> ```
> OLD col4: SOW-004..009, SOW-041, SOW-043; instruments: SOW-058, SOW-059
> NEW col4: SOW-001, SOW-003, SOW-004..009, SOW-011..017, SOW-040..043, SOW-089; instruments: SOW-058, SOW-059
> OLD col5: DEL-04-01..05, DEL-08-03, DEL-08-04, DEL-10-01, DEL-10-04
> NEW col5: DEL-00-03, DEL-01-01, DEL-02-01..07, DEL-04-01..05, DEL-08-01..04, DEL-10-01, DEL-10-04
> ```
>
> (`Amendment_Preview.md`, action `A003b`, "Line 320 · `OBJ-001`"; all four lines
> quoted in full, none elided. The `..` ranges are the source's own notation.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

> ```
> OLD col4: SOW-006, SOW-018, SOW-019; supported by SOW-005
> NEW col4: SOW-001, SOW-006, SOW-011..019; supported by SOW-005
> OLD col5: DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03
> NEW col5: DEL-01-01, DEL-02-01..07, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03
> ```
>
> (`Amendment_Preview.md`, action `A003b`, "Line 321 · `OBJ-002`"; all four lines
> quoted in full, none elided. The `..` ranges are the source's own notation.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

`SOW-006` and `SOW-007` both stand inside `OBJ-001`'s mapped scope items on
both sides of the amendment (`SOW-004..009` in the `OLD col4` text), `SOW-006`
stands inside `OBJ-002`'s on both sides (named literally in the `OLD col4`
text), and `DEL-04-03` stands inside both objectives' mapped deliverables on
both sides. The mappings are therefore register-direct at both levels and
predate SCA-002: this contract records them rather than deriving them, asserts
no confidence label for them because the record assigns none, and creates no
owner-confirmation acceptance criterion for them.

One appearance of `SOW-006` in the SCA-002 record is noted so it is not
misread. The Q2 `INDIRECT-8` decision table's `AFFIRM` row carries the cell
"`SOW-001, SOW-006, SOW-011..019; supported by SOW-005`", which is verbatim the
`NEW col4` text of the `OBJ-002` §3 row quoted above. `SOW-006` is present in
that cell because it was already present in the `OLD col4` text; the Q2 row
describes the §3 objective-row membership affected by the eight parser
deliverables' affirmation and re-attributes nothing about `SOW-006`, whose
ledger mapping predates the amendment. This contract's own reading of the
record agrees with that on inspection of both the `OLD`/`NEW` block and the Q2
table.

**Per-item mapping discipline.** The frontmatter objective union is
`[OBJ-001, OBJ-002]`, matching `Deliverables.csv`'s `SupportsObjectives` cell
for this deliverable. The two scope items do not carry that union equally:
`SOW-006`'s ledger `ObjectiveIDs` cell reads `OBJ-001;OBJ-002` and `SOW-007`'s
reads `OBJ-001` alone. Every matrix row and every warrant statement in this
contract respects each item's own mapping; no output, requirement, or
acceptance criterion anchored on `SOW-007` is attributed to `OBJ-002`
(AX-008).

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-006` reads in full (columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`):

> `SOW-006,IN,"Stamp every orientation response with examined-through SHA, generation time, and per-feed freshness",PEC-ORI-003,PKG-04,DEL-04-03,OBJ-001;OBJ-002,,FALSE,Carries PEC-K-04`
>
> (`DecisionRef` empty; `OpenIssue` `FALSE`; `Notes` "Carries PEC-K-04" —
> an invariant carry, not an open issue or boundary decision. ID-shaped text
> inside this quotation is upstream source context, not a local definition or
> reference.)

  The `SOFTWARE_DECOMP.md` §2 SSOW row for the same item repeats the statement without the register-only columns and carries the same note: "| SOW-006 | IN | Stamp every orientation response with examined-through SHA, generation time, and per-feed freshness | PEC-ORI-003 | Carries PEC-K-04 |".

- **CLM-002** — The accepted `ScopeLedger.csv` row for `SOW-007` reads in full, under the same columns:

> `SOW-007,IN,"Attach a citation (file path, anchor, and/or SHA) to every claim in an orientation response",PEC-ORI-004,PKG-04,DEL-04-03,OBJ-001,,FALSE,`
>
> (`ObjectiveIDs` `OBJ-001` alone; `DecisionRef` empty; `OpenIssue` `FALSE`;
> `Notes` empty. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  The `SOFTWARE_DECOMP.md` §2 SSOW row reads "| SOW-007 | IN | Attach a citation (file path, anchor, and/or SHA) to every claim in an orientation response | PEC-ORI-004 | |", with an empty note cell.

- **CLM-003** — The two `SourceRef` cells name two `PRD.md` §9.1 requirements, quoted here in full as they read. `PEC-ORI-003`: "Every orientation response shall carry the examined-through SHA, generation time, and per-feed freshness." `PEC-ORI-004`: "Every claim in an orientation response shall carry a citation (file path, anchor, and/or SHA) to its live source." `PEC-ORI-003` enumerates exactly three stamp fields — (i) the examined-through SHA, (ii) generation time, (iii) per-feed freshness — and `PEC-ORI-004` names three admissible citation constituents — file path, anchor, and/or SHA — resolving to the *live source*, not to PEC. Both requirements are universally quantified over responses and claims respectively; neither admits an exception class. Those quantifiers are register truth and are carried here exactly.
- **CLM-004** — `SOW-006`'s ledger `Notes` cell reads "Carries PEC-K-04", and that product invariant reads in full: "**Staleness is a comparison.** Every response carries the examined-through commit SHA and per-feed freshness; consumers detect staleness structurally." The invariant states *why* the stamp exists: the consumer, not this deliverable, performs the staleness determination, and it can only do so if the stamp is a structural value it may compare against its own state. `PEC-K-02` bounds what a citation may claim in the same register: "PEC output is never citable as authority". A citation produced here therefore points at a live governed source, never at a PEC artifact (AX-006).
- **CLM-005** — `OBJ-001` states "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation" (`SourceRef` `§3.1`), and `OBJ-002` states "Staleness is detected structurally by SHA comparison, never by judgment" (`SourceRef` `§3.2`). This deliverable is the buildable form of `OBJ-001`'s "per-claim citations" clause — the upstream return contract states as much in its own voice (CLM-010) — and one of `OBJ-002`'s two `PKG-04` limbs, the response-stamp limb, the other being `DEL-04-02`'s delta service under `SOW-005`. Neither objective is discharged by this contract alone; each is a cross-package outcome whose deliverable set is the `MappedDeliverables` cell quoted in the warrant above.

## Deliverable Definition — Ontology

`DEL-04-03` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `M` with
`PhaseHint` `P1`. `Deliverables.csv` records its `AnticipatedArtifacts` as
"Citation layer + tests" and leaves `ContextEnvelopeNotes` empty, so there are
no envelope notes to carry forward and `_CONTEXT.md` records "(none)". The
outputs of this contract are bounded by that artifact naming: exactly the
citation layer and its tests, and nothing beyond those two artifacts and the
components each of them declares as part of itself.

- **OUT-001** — A citation-and-stamping layer in the PEC service core, discharging both covered scope items over an orientation response: it attaches to every claim in the response a citation resolving to the live source (file path, anchor, and/or SHA) carried through from that claim's record-tier provenance, and it stamps the response with the examined-through SHA, the generation time, and per-feed freshness. The layer's **stamp-and-citation derivation record** — the readable artifact in which it declares, per stamp field and per claim class, the source it draws from, the rule it applies, and its absence semantics (REQ-014) — is a component of this output rather than a third artifact: it is the layer's own self-declaration, so the register's `AnticipatedArtifacts` naming of exactly two artifacts is preserved.
- **OUT-002** — An automated test suite covering citation attachment, stamp composition, the tier-exclusion boundary, absence and non-resolution behaviour, and the adjacent-act boundary, implementing the verification methods declared in this contract.

### Identity of record

- **CLM-006** — `DEL-04-03` is named "Citation & freshness stamping", Type `BACKEND_FEATURE_SLICE`, Context Envelope `M`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `AnticipatedArtifacts` "Citation layer + tests", `CoversScopeItems` `SOW-006;SOW-007`, `SupportsObjectives` `OBJ-001;OBJ-002`, `ContextEnvelopeNotes` empty, with the register `Description` field reading "Per-claim citations (path/anchor/SHA) and response stamping (examined-through SHA, generation time, per-feed freshness)." Sources: `Deliverables.csv` row `DEL-04-03` and the `SOFTWARE_DECOMP.md` §5 PKG-04 table row "| DEL-04-03 | Citation & freshness stamping | BACKEND_FEATURE_SLICE | M | P1 | SOW-006, 007 |". `ResponsibleParty` is `TBD` throughout the register by the §5 preamble — assignment happens at WORKING_ITEMS activation, not here (TBD-001). This deliverable is one of the eight two-item merges recorded at `DL-13`(d) and re-audited at Phase 6; §8 Context Budget QA records that of those merges "the other six merges hold as one shape each" after `DEL-10-05` was split and `DEL-06-05`'s cross-package enforcement edge to this deliverable was declared, so the two scope items remain one deliverable shape by accepted ruling and are not separable here.
- **CLM-007** — The `PKG-04` package charter (`SOFTWARE_DECOMP.md` §4) is "Derivation and serving of orientation: per-loop returns, deltas since SHA, SHA/freshness stamping, per-claim citations, scope parameterization, explicit measurement limits", covering "SOW-004..009 (6)", with "Transport (PKG-08); rendering (PKG-09)" recorded as explicitly out of package scope. Of those six items this deliverable covers exactly two — the stamping limb and the per-claim-citation limb — and the package's two exclusions bind it directly: no transport surface and no rendering surface is produced here (REQ-010).
- **CLM-008** — What "every claim in an orientation response" ranges over is fixed by the accepted corpus only at the level of the response's structure, and this contract states that rather than settling the granularity. `PEC-ORI-001` through `PEC-ORI-006` are the six requirements the §9 Vocabulary Map calls "the per-loop/scope serve", and the response this layer acts on is the return the sibling contracts compose: the per-loop return of `DEL-04-01` under `SOW-004`, the delta return of `DEL-04-02` under `SOW-005`, and the scope-parameterized returns of `DEL-04-04` under `SOW-008`. The upstream return contract enumerates its own components, and its enumeration is what claims in that response are composed from (CLM-010). Whether a claim is a whole component, a field within one, or a derived assertion about one is stated by no accepted source (CON-004).
- **CLM-009** — Every value the layer may cite is provenance the record tier is obliged to hold, and holding it is another deliverable's obligation. The upstream return contract quotes the entity-model contract's requirement in its own voice, and this contract reaches that text transitively through that quotation rather than through any register edge of its own — this deliverable's `Dependencies.csv` records no edge to `DEL-01-01`:

> - **REQ-003** — Every record-tier entity type shall carry provenance
>   sufficient for a per-claim citation to its live source — file path, anchor,
>   and/or SHA, per `PEC-ORI-004` — because §7.1 defines the tier as "citable
>   with sources". The act of attaching citations to an orientation response is
>   `DEL-04-03`'s under `SOW-007` (CLM-012); this requirement obliges the model
>   to hold what that act needs, and no more.
>
> (`DEL-01-01/ScopeOfWork.md`, Epistemology section, as quoted verbatim inside
> `DEL-04-01/ScopeOfWork.md` CLM-011; quoted in full, not elided. ID-shaped text
> inside this quotation is upstream source context, not a local definition or
> reference — this contract's own `REQ-*` records are separate and differently
> worded.)

  Two consequences bind this contract. The provenance a citation resolves is carried, not invented: this deliverable defines no record-tier entity type and no provenance field, and attaches nothing a source entity does not already carry (REQ-003). And the naming runs the other way as well — that requirement names this deliverable as the owner of the attaching act, which is the accepted basis on which this contract takes the act rather than deriving ownership from its own scope items alone.

### Placement in the work graph

- **CLM-010** — This deliverable has one accepted `EXECUTION` upstream edge and three `ANCHOR` rows, held as `Dependencies.csv` register rows `DEP-04-03-001` through `DEP-04-03-004` at `RegisterSchemaVersion` `v3.1`. The three anchors are `DEP-04-03-001` (package-local to `PKG-04`), `DEP-04-03-002` (`SOW-006` requirement trace), and `DEP-04-03-003` (`SOW-007` requirement trace). The single `EXECUTION` row is `DEP-04-03-004`: `TargetDeliverableID` `DEL-04-01`, `TargetName` "Loop orientation return", `DependencyClass` `EXECUTION`, `AnchorType` `NOT_APPLICABLE`, `Direction` `UPSTREAM`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `Statement` "Citation/freshness stamping applies to orientation responses", `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `FirstSeen` and `LastSeen` `2026-07-25`, `Status` `ACTIVE`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P34". **Two cells of that row are recorded here as observed rather than smoothed over:** its `SourceRef` reads "location TBD" and its `EvidenceQuote` is empty, so the row cites its evidence file without an in-file locus or quoted span. That is a register-hygiene observation of the class `OI-013` records — "No durable register validator exists: the coverage/coupling assertions ran in a session-local generator, which is not part of this package and enforces nothing after acceptance" — and this contract neither supplies a locus nor invents a quotation for it. The edge's own basis is legible independently from the exhibit row, which reads, under the exhibit's columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`:

> ```
> E-P34,DEL-04-01,DEL-04-03,PROPOSAL,CONSUMES,,,Citation/freshness stamping applies to orientation responses
> ```
>
> (`PLAN_2026-07-25_project_setup_dag_gate.md` §4.1, row quoted in full. The
> `Flag` and `BasisCitation` cells are both empty, so this edge carries no
> annotation and no cited basis beyond its `Rationale`. ID-shaped text inside
> this quotation is upstream source context, not a local definition or
> reference.)

- **CLM-011** — The upstream predecessor is at lifecycle state `INITIALIZED`, which is the maturity the edge requires. `INITIALIZED` means the upstream **contract** is the reliable input: an accepted `ScopeOfWork.md` exists, and no orientation builder, no return, and no record tier does. Nothing in this contract asserts that any upstream artifact exists or has been produced. What that contract obliges, and hands to this one, it states in its own voice:

> - **REQ-001** — The builder shall compose, for a named loop, a return carrying all six components enumerated at `SOW-004` and `PEC-ORI-001` (CLM-001, CLM-002): the newest applicable receipt, the examined-through SHA, gate states, owner directions of record, open tranches and candidate briefs, and parked lanes each with the owner action that would unpark it. No component shall be dropped, merged away, or silently substituted, and no seventh component shall be added.
> - **REQ-005** — Each component value shall carry through the citation provenance the upstream model is obliged to hold — file path, anchor, and/or SHA to the live source — so that the stamping-and-citation deliverable can attach it. This deliverable shall attach no citation to a response, shall stamp no response with generation time or per-feed freshness, and shall compute no freshness value; those acts are `DEL-04-03`'s under `SOW-006` and `SOW-007` (CLM-011, CLM-015, CON-003).
> - **REQ-009** — The examined-through SHA component shall be the value the record tier carries for the loop's examined state, obtained structurally and never re-derived, inferred, or judged by this builder, so that staleness remains a comparison rather than a judgment (`PEC-K-04`). Where the record tier carries no examined-through SHA for the loop, REQ-006 governs and no substitute value is presented.
>
> (`DEL-04-01/ScopeOfWork.md`, Epistemology section; all three records quoted in
> full, none elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference — this contract's own `REQ-*`,
> `AC-*`, and `CON-*` records are separate and differently worded.)

  Three consequences bind this contract. The six components of that return, each carrying its own provenance, are what the attaching act operates on, so this contract's claim-coverage obligation ranges over the response's structure as that contract fixes it (REQ-002, CON-004). The upstream contract disclaims the stamping and the attaching in explicit terms, so neither act is performed twice and neither is left unowned. And the structural-not-judged discipline the upstream contract applies to its own SHA component is the same discipline this contract applies to the SHA it stamps (REQ-004).

- **CLM-012** — The upstream contract also records an unsettled representation question about the SHA, in its own voice, and this contract carries the conditioning rather than resolving it:

> - **CON-003** — The examined-through SHA appears twice in the accepted scope, once as a component of this deliverable's return (`SOW-004`, `PEC-ORI-001`) and once inside the response-level stamp of another (`SOW-006`, `PEC-ORI-003`: "Every orientation response shall carry the examined-through SHA, generation time, and per-feed freshness"), and no accepted source states whether the two are the same field. The register is unambiguous about ownership — the stamping act is `DEL-04-03`'s, and the upstream entity model names that deliverable as the owner of citation attachment in its own voice (CLM-011) — but not about representation. This contract takes the narrow reading that its own row supports: the SHA is composed as a content component of the return, obtained structurally from the record tier (REQ-009), while the response-level stamp of SHA, generation time, and per-feed freshness, and the attachment of per-claim citations, are performed elsewhere and are not duplicated here (REQ-005). Whether the consuming deliverable reads this component or stamps an independently obtained value is left open by the accepted sources and is not settled here.
>
> (`DEL-04-01/ScopeOfWork.md`, Epistemology section; quoted in full, not elided.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

  Ownership is settled and representation is not. The stamping act is this deliverable's on both sides of the record; which value the stamp carries, and whether it is the same field as the upstream return component, is CON-002 here as it is `CON-003` there.

- **CLM-013** — Five downstream consumer relations are recorded against this deliverable in `_DEPENDENCIES.md` and marked informational: `DEL-10-04` `[E-A21]` (`MEASURES`), `DEL-09-07` `[E-N04]` (`CONSUMES`), `DEL-04-05` `[E-N17]` (`CONSUMES`), `DEL-08-03` `[E-P53]` (`CONSUMES`), and `DEL-09-06` `[E-P70]` (`CONSUMES`). **None of the five holds a row in this deliverable's `Dependencies.csv`**, which contains only the two requirement anchors, the package anchor, and the single upstream `EXECUTION` row; the downstream rows live in each consumer's own local register, per the deliverable-local storage ruling of `D-PEC-62`. Their strata are not uniform and this contract does not flatten them: `[E-A21]` is `DECLARED` (exhibit basis the `SOW-059` note "Method + any needed instrumentation; measures SOW-007", rationale "SOW-007 is covered by DEL-04-03"); `[E-N04]` is `DERIVED` (basis `SOW-051` "staleness" plus the Vocabulary Map entry making examined-through SHA "The staleness comparator (PEC-K-04)"); and `[E-N17]`, `[E-P53]`, and `[E-P70]` are `PROPOSAL`. All five carry an empty `Flag` column. Every one runs *from* this deliverable outward: being measured by the orientation defect-rate spot-check, consumed by the pressure rules, the limitation renderer, the response format, and the drill-down component transfers none of their scope into this contract and imposes no obligation on them (AX-009).
- **CLM-014** — One register-wide constraint names this deliverable directly, and it is unresolved. `_DEPENDENCIES.md` records it as "**C-02 (CO_OBLIGATION)** — One PEC-K-05/C4 enforcement obligation split across two write scopes; direction not declared". The exhibit's constraint register states it in full, under the columns `ConstraintID,Kind,Parties,Provenance,Statement,Notes`:

> ```
> C-02,CO_OBLIGATION,"DEL-04-03, DEL-06-05","DECLARED — DEL-06-05: ""The exclusion is two-sided: the presence-store guard lands here; the citation-production side is asserted in DEL-04-03's tests (declared dependency edge, DL-14)""",One PEC-K-05/C4 enforcement obligation split across two write scopes; direction not declared,Was edge E-A05. R1-F1/R3-F7: a P1 test cannot assert exclusion of a tier first existing at P3 — DEL-04-03 carries a P3-reopened acceptance obligation. PHASE_TENSION; owner ruling requested
> ```
>
> (`PLAN_2026-07-25_project_setup_dag_gate.md` §4.2 constraints register, row
> quoted in full; the doubled quotation marks are the source's own CSV escaping.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

  `D-PEC-62` §1(4) accepted the exhibit "accepted, all strata as presented" and that packet reads "as presented" as accepting the exhibit's flags as flags, leaving a specific annotated set recorded-but-unresolved: "E-A11 (AMBIGUOUS_BASIS), E-P69/E-N02 (PHASE_TENSION), E-N13/E-N18 (LOW_CONFIDENCE), C-02 direction, C-08 standing-node set remain recorded-but-unresolved, non-gating annotations". The `C-02` direction is one of them, and it names this deliverable. That is CON-001; this contract states the exclusion obligation as a requirement and records the phase tension rather than deciding either.
- **CLM-015** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: this deliverable is `P1`; its upstream `DEL-04-01` is `P1`. Its recorded consumers are `P1` (`DEL-04-05`, `DEL-08-03`) and `P2` (`DEL-09-06`, `DEL-09-07`, `DEL-10-04`). The `C-02` co-obligation partner `DEL-06-05` is `P3`, which is the phase tension the constraint's own `Notes` cell records. Other deliverables named as owners of adjacent scope are `P1` (`DEL-01-01`, `DEL-01-03`, `DEL-01-05`, `DEL-03-01`, `DEL-03-02`, `DEL-04-02`, `DEL-08-01`, `DEL-08-04`), `P2` (`DEL-04-04`), `P3` (`DEL-10-12`), and `P4` (`DEL-08-05`). No consumer precedes this deliverable's phase, and no claim in this contract stages any named deliverable into a different phase.

### Boundaries

- **CLM-016** — The acts adjacent to this one are owned elsewhere and are cited here, never discharged. Within `PKG-04`: composing the per-loop orientation return is `DEL-04-01` (`SOW-004`, `PEC-ORI-001`); serving deltas since a caller-supplied commit SHA is `DEL-04-02` (`SOW-005`, `PEC-ORI-002`); scope parameterization by loop / project / package per the modes ladder is `DEL-04-04` (`SOW-008`, `PEC-ORI-005`, `P2`); rendering a measurement limitation into an orientation response where a feed is unparseable or stale is `DEL-04-05` (`SOW-009`, `PEC-ORI-006`) — the upstream return contract states that division in its own voice at `DEL-04-01`/CLM-015. Outside it: the record-tier schema and entity model, including the provenance every citation resolves, are `DEL-01-01` (`SOW-001`); the one-command full rebuild that populates the record tier is `DEL-03-01` (`SOW-010`); incremental reconcile keyed on Git delta since the last examined SHA is `DEL-03-02` (`SOW-018`, `PEC-RCN-003`) and drift classification is `DEL-03-03` (`SOW-019`); the ingest-boundary content-minimal guard is `DEL-01-03` (`SOW-056`) and the zero-dependency, no-egress posture is `DEL-01-05` (`SOW-052`, `SOW-053`); the presence-store TTL machinery and the presence-side limb of the citation-exclusion guard are `DEL-06-05` (`SOW-030`, `SOW-032`, `P3`); the compact, machine-first, citation-bearing response envelope and serializer are `DEL-08-03` (`SOW-043`, `PEC-API-004`) and the orientation latency budget is `DEL-08-04` (`SOW-041`); the local-only Unix-socket binding and its token-scoped access classes are `DEL-08-01` (`SOW-003`, `SOW-040`) and the SSE delta/presence subscription is `DEL-08-05` (`SOW-044`, `P4`); the universal drill-down component that resolves a citation to its source is `DEL-09-06` (`SOW-050`, `PEC-DSH-006`, `P2`) and the Explain-shaped pressure rules that consume the staleness comparator are `DEL-09-07` (`SOW-051`, `P2`); the orientation defect-rate spot-check that measures `SOW-007` is `DEL-10-04` (`SOW-059`, `P2`); and candidate-consumer enablement plus enabled-consumer orientation use against contact opportunities defined by each consumer's own adopted mode/cadence rules are measured by `DEL-10-12` (`SOW-060`, `P3`). `DEL-10-12` retains its canonical “Poll-adoption measurement” label/path, but no harness polling or receiving-loop conformance criterion is implied. This contract produces only the citation layer and its tests.
- **CLM-017** — The deliverable is at lifecycle state `INITIALIZED` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The layer's concrete in-process shape — whether it is applied as a decoration of a composed response, as a construction-time obligation of the composer, or as a separate pass, and its entry-point name and parameters — is fixed by no accepted source beyond the register phrase "Citation layer". It is chosen during production within REQ-010, which bounds it to a service-core surface carrying no transport, serialization, or rendering concern.
- **TBD-003** — The representation of "generation time" — its precision, its timezone or offset convention, its clock source, and its serialized form — is stated by no accepted source; `PEC-ORI-003` names the field and nothing more. It is chosen during production, and REQ-014 obliges the choice to be declared rather than left implicit. The serialized form in a wire response is `DEL-08-03`'s envelope concern (CLM-016).
- **TBD-004** — Where the stamp-and-citation derivation record of OUT-001 lives and in what form it is published are fixed by no accepted source; they are chosen during production within REQ-014, which fixes what it must declare rather than where it sits.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a citation layer, an orientation return, a record
tier, a reconciler, or a test exists.

- **REQ-001** — Every orientation response the layer stamps shall carry all three fields `SOW-006` and `PEC-ORI-003` require — the examined-through SHA, the generation time, and per-feed freshness — with none dropped, merged away, or silently substituted, and no fourth stamp field added (CLM-001, CLM-003).
- **REQ-002** — Every claim in a stamped orientation response shall carry a citation that resolves to its live source as file path, anchor, and/or SHA, per `SOW-007` and `PEC-ORI-004`, with no claim class exempted (CLM-002, CLM-003, CLM-008, CON-004).
- **REQ-003** — Each citation shall be carried through from the provenance the record-tier entity behind the claim is obliged to hold (CLM-009); the layer shall synthesize, infer, reconstruct, or default no path, anchor, or SHA, shall define no record-tier entity type and no provenance field, and shall not depend on any upstream artifact existing. Every citation shall point at the live governed source and none at a PEC artifact, store record, or generated view, per `PEC-K-02` ("PEC output is never citable as authority").
- **REQ-004** — The examined-through SHA in the stamp shall be the value the record tier carries for the response's examined state, obtained structurally and never re-derived, recomputed, inferred, or judged by this layer, so that staleness remains a comparison performed by the consumer rather than a judgment made here (`PEC-K-04`, `OBJ-002`). Where no such value is carried, REQ-008 governs and no substitute value is stamped (CON-002).
- **REQ-005** — Per-feed freshness shall be stated per feed rather than as a single aggregate, over the feed set the reconcile reports for the response, and the freshness value for each feed shall be a value the record tier carries rather than one this layer computes about the feed's underlying file. Where a feed's freshness is not carried, the stamp shall state that it is unknown for that feed and shall present no derived, defaulted, inferred, or carried-forward value in its place (CON-003).
- **REQ-006** — No presence-tier value shall appear in any citation this layer attaches, and no citation shall resolve to a presence-tier record, per `PEC-K-05` ("Presence facts never enter record-tier citations"), `PEC-PRS-007` ("Presence data is operational only and shall never appear in record-tier citations (PEC-K-05)"), and `SOW-032`. This is the citation-production limb of the two-sided exclusion recorded at `C-02`; the presence-store guard limb is `DEL-06-05`'s and is not discharged here (CLM-014, CON-001).
- **REQ-007** — No citation and no stamp field shall carry file content or diff content, per `PEC-K-10` ("Paths, counts, SHAs, states, hashes — never file or diff content"). A citation shall carry locating identity — path, anchor, and/or SHA — and shall not reproduce, excerpt, summarize, or paraphrase the text it locates.
- **REQ-008** — Where a claim's provenance is absent or does not resolve, or where a stamp field's value is not carried, the layer shall neither emit the claim or field with a fabricated or approximate value nor drop it silently: the absence shall be stated against the affected claim or field and recorded so that it is available to the deliverable that renders measurement limitations. Silent omission is prohibited (`PEC-ORI-006`), and the posture is `PRD.md` §7.3's coverage honesty — "a figure the records don't support is absent and said to be absent". Rendering such a limitation into an orientation response is `DEL-04-05`'s act under `SOW-009` (CLM-016); this layer makes it available to that act.
- **REQ-009** — The layer shall be read-only over the record tier, over the presence tier, and over Git: it shall create, modify, or delete no source file, governed file, register, lifecycle file, or store record, and shall provide no path that records an adoption, a ruling, or a direction, per `PEC-GAT-004` ("PEC shall provide no write path that records adoption, ruling, or direction") and `PEC-K-06` observation-not-participation. Stamping a response shall not mutate the record tier the response was derived from.
- **REQ-010** — The layer shall perform no act owned by another deliverable. In particular it shall compose no orientation return, serve no delta since a caller-supplied SHA, parameterize no response by scope, render no measurement limitation, define or emit no wire envelope or serialization format, implement no socket binding, token check, or subscription, render no dashboard or drill-down view, evaluate no pressure or staleness rule, perform no rebuild, incremental reconcile, or drift classification, enforce no presence-store TTL or guard, and measure no defect rate, latency, or adoption; each is cited to its owner in CLM-016 and none is discharged here.
- **REQ-011** — The layer and its tests shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-012** — The stamp and citation obligations shall hold for every orientation response without exception of scope, caller, or response kind, because `PEC-ORI-003` and `PEC-ORI-004` are universally quantified (CLM-003): a delta return, a scope-parameterized return, and a return carrying stated absences are each an orientation response and shall each be stamped and cited. Selecting or parameterizing which response is produced remains the siblings' act (REQ-010).
- **REQ-013** — The layer shall declare, in the derivation record, which value it stamps as the examined-through SHA and on what basis — whether the value carried as a component of the composed return, or a value obtained independently from the record tier — and shall not present the choice as settled by an accepted source, because none settles it (CLM-012, CON-002).
- **REQ-014** — The layer shall declare, in the stamp-and-citation derivation record — a readable component of OUT-001 — for each of the three stamp fields and for each claim class it cites: the source it draws the value or provenance from, the rule it applies (including the feed set and freshness source for REQ-005, the claim granularity adopted under CON-004, and the generation-time representation of TBD-003), and its absence semantics. A stamp field or citation produced by an undeclared source or an undeclared rule is prohibited.
- **REQ-015** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria. Where a verification method cannot be executed at `P1` because its counterpart tier or artifact does not yet exist, the test shall record that fact rather than assert a passing result (CON-001).

- **AC-001** — For fixture orientation responses, every stamped response carries the examined-through SHA, the generation time, and per-feed freshness, each identifiable in the stamp by name; no stamp is emitted with a missing field; and no stamp carries a fourth field.
- **AC-002** — For fixture orientation responses spanning every claim class the fixture return contains, every claim in each stamped response carries a citation, and each citation resolves to a file path, anchor, and/or SHA identifying a live governed source; no claim in any fixture response is uncited.
- **AC-003** — Every citation attached in a fixture run is traceable to the provenance held by the record-tier entity behind its claim, with byte equality between the entity's provenance values and the citation's; this deliverable's source contains no path-, anchor-, or SHA-synthesis, reconstruction, or default path, no record-tier entity type or provenance field definition, and no assumption that an upstream schema, entity model, reconciler, store, or orientation builder artifact exists; and no citation in a fixture run resolves to a PEC artifact, store record, or generated view.
- **AC-004** — The examined-through SHA in a stamped fixture response equals the value the fixture record tier carries for that response's examined state, byte for byte; this deliverable's source contains no SHA derivation, recomputation, inference, or comparison path; and where the fixture record tier carries no examined-through SHA, the stamp states the absence per AC-008 rather than supplying a value.
- **AC-005** — For a fixture whose reconcile reports multiple feeds, the stamp carries a freshness entry per reported feed rather than one aggregate; each entry's value equals the value the fixture record tier carries for that feed; and for a fixture feed carrying no freshness value, the stamp states it as unknown for that feed and presents no derived, defaulted, inferred, or carried-forward value.
- **AC-006** — For a fixture carrying presence-tier records alongside the record tier, no citation attached in a stamped response derives from or resolves to a presence-tier record; this deliverable's source contains no presence-tier read on any citation path; and the test record states, for the enforcement that depends on a presence tier first existing at `P3`, whether it was executed or recorded as pending under CON-001 rather than reported as passing.
- **AC-007** — For a content-dense fixture corpus carrying long prose bodies, authored ruling text, and diff-shaped content, inspection of every citation and every stamp field in a stamped response finds no file content and no diff content, and no citation reproduces, excerpts, summarizes, or paraphrases the text it locates.
- **AC-008** — For fixture cases in which a claim's provenance is absent, a claim's provenance does not resolve, and each stamp field's value is in turn not carried, the stamped response states the absence against the affected claim or field, presents no fabricated or approximate value, drops no affected claim silently, and records the absence in a form a consuming deliverable can read.
- **AC-009** — A stamping run leaves the fixture source corpus, the fixture record tier, and the fixture store byte-identical; the captured filesystem and store write inventory for a stamping run is empty; and this deliverable's source contains no write, create, or delete call against any source file, governed file, register, lifecycle file, or store record, and no path that records an adoption, ruling, or direction.
- **AC-010** — This deliverable's source and call graph contain no orientation-composition path, no delta-since-SHA path, no scope-parameterization path, no limitation-rendering path, no wire envelope or serialization format, no socket binding, token check, or subscription, no dashboard or drill-down rendering, no pressure- or staleness-rule evaluation, no rebuild, incremental-reconcile, or drift-classification path, no presence-store TTL or guard path, and no defect-rate, latency, or adoption measurement; and no test in this deliverable asserts a criterion belonging to any of them.
- **AC-011** — The layer and its tests add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact.
- **AC-012** — For fixture responses of each kind the accepted sources name — a per-loop return, a delta return, a scope-parameterized return, and a return carrying stated absences — each is stamped per AC-001 and cited per AC-002, and this deliverable's source contains no response kind, scope, or caller for which the stamp or citation obligation is conditional or skipped.
- **AC-013** — The stamp-and-citation derivation record — the component of OUT-001 required by REQ-014 — names, for each of the three stamp fields and each cited claim class, its source, its applied rule including the feed set and freshness source, the claim granularity adopted, and the generation-time representation, and its absence semantics; it states which value is stamped as the examined-through SHA and on what basis, without presenting that choice as settled by an accepted source; and every stamp field and citation produced in a fixture run is traceable to the rule the record declares for it.
- **AC-014** — The test suite implements VER-001 through VER-013, executes in the `PKG-04` test run, passes or records a pending result under CON-001 where a verification cannot execute at `P1`, and introduces no acceptance criterion absent from this contract.
- **AC-015** — The REVIEW gate confirms this contract's traceability to `SOW-006`, `SOW-007`, `OBJ-001`, and `OBJ-002`; confirms that the objective mappings are stated as register-direct and pre-SCA-002 with no confidence label the record does not carry, and that no `SOW-007`-anchored output is attributed to `OBJ-002`; confirms that the single upstream edge and the five downstream relations are each stated at their own stratum; confirms that the `C-02` direction and its `P1`/`P3` phase tension are recorded as unresolved rather than decided here; and confirms that no `PKG-01`, `PKG-03`, sibling `PKG-04`, `PKG-06`, `PKG-08`, `PKG-09`, or `PKG-10` scope has been absorbed.

- **CON-001** — The presence-exclusion obligation this deliverable carries is one half of a split obligation whose direction the accepted record explicitly leaves undeclared, and whose two halves sit in different phases. `C-02` names both parties, states "One PEC-K-05/C4 enforcement obligation split across two write scopes; direction not declared", and records in its `Notes` that "a P1 test cannot assert exclusion of a tier first existing at P3 — DEL-04-03 carries a P3-reopened acceptance obligation. PHASE_TENSION; owner ruling requested" (CLM-014). The `D-PEC-62` §1(4) ruling accepted the exhibit's flags as flags and lists "C-02 direction" among the annotations that "remain recorded-but-unresolved, non-gating". The exhibit's own §7 erratum candidates repeat it as a PhaseHint tension: "C-02's P1-vs-P3 assertion obligation on DEL-04-03". This contract therefore states the exclusion as a requirement that binds this layer's own production (REQ-006), states what is checkable at `P1` and what must be recorded as pending rather than asserted (AC-006, REQ-015), and settles neither the direction of the obligation nor the phase in which its full assertion lands. Deciding either here would take an owner ruling in the wrong place; treating the requirement as discharged by a `P1` test over a tier that does not yet exist would assert a result the record says cannot be obtained.
- **CON-002** — Which value the stamp's examined-through SHA carries, and where that value originates, is unsettled by the accepted sources on two axes. On representation, the upstream return contract's own `CON-003`, quoted at CLM-012, records that the SHA appears both as a component of the composed return and inside this deliverable's response stamp, and that "no accepted source states whether the two are the same field"; ownership of the stamping act is not in doubt, representation is. On origin, no accepted source states whether the stamped value is the reconcile-side examined-SHA baseline that keyed the reconcile — `SOW-018`, "Run reconciliation incrementally, keyed on Git delta since the last examined SHA" (`SourceRef` `PEC-RCN-003`, whose own `PRD.md` §9.2 wording differs), covered by `DEL-03-02` — or a value obtained per response. This contract does not close either axis: REQ-004 fixes that whatever value is stamped is obtained structurally and never judged, and REQ-013 obliges the production choice and its basis to be declared in the derivation record so the question stays visible to review and to any later scope change.
- **CON-003** — "Per-feed freshness" carries two undefined terms. No accepted source defines what constitutes a *feed* for stamping purposes: the nearest is `PEC-RCN-002`'s minimum ingest list — "`_STATUS.md` (declared parser dialect), decision registers and packets, `LOOP_RECEIPTS.md` (per-loop grammar; the D-APP-57 contract where a ledger has adopted it), `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`, dependency registers, workplans/LOOP_INIT, and per-project `_harness/adapter.yaml` as the feed manifest" — which names what is ingested and designates a manifest, without stating that the stamp's feed set is that list, the manifest's contents, or the feeds actually read for a given response. And no accepted source defines what *freshness* is measured as: a last-read timestamp, an age, the feed's own SHA, or a staleness classification. `PEC-K-04` fixes only that the consumer detects staleness structurally from what the stamp carries. This contract requires the freshness value to be one the record tier carries rather than one computed here (REQ-005), requires the feed set and the freshness source to be declared (REQ-014), and requires an uncarried value to be stated as unknown rather than guessed (REQ-005, REQ-008); it selects no definition, and none may be inferred from this document.
- **CON-004** — What counts as a *claim* in an orientation response is not enumerated by any accepted source, so the granularity at which `PEC-ORI-004`'s universal quantifier bites is unsettled. The upstream return contract fixes the response's structure — six named components, each carrying its own provenance (CLM-011) — but whether a claim is a whole component, a field within a component, or a derived assertion about one is stated nowhere. The consequences differ: at component granularity, one citation per component satisfies the requirement; at field granularity, a component assembled from several entities needs several. The corpus pressure runs toward the finer reading — `PEC-K-08` requires that "Every status, verdict, and warning carries rule ID, threshold, and contributing cited sources. Drill-down never dead-ends", and `SOW-050` obliges drill-down "from every displayed value to its cited source" — but neither is this deliverable's scope item and neither states a claim granularity for `SOW-007`. This contract obliges full coverage at whatever granularity the response presents (REQ-002, REQ-012) and obliges the adopted granularity to be declared (REQ-014); it does not choose it here, and the choice is a production decision bounded by those requirements rather than a licence to exempt a claim class.

## Production and Verification Method — Praxeology

Production proceeds in the order upstream-contract survey → provenance
carry-through path → claim-coverage path → stamp composition → absence and
non-resolution handling → tier-exclusion enforcement → tests, because the
carry-through path is the acceptance surface of everything after it: a citation
that is synthesized rather than carried cannot be made correct later by
coverage or by stamping. The upstream-contract survey comes first because the
sole predecessor is at `INITIALIZED` and supplies obligations rather than
artifacts, so a citation path written against an imagined return shape or an
assumed populated store would violate REQ-003 before any code existed. Absence
and non-resolution handling is built before tier exclusion rather than after
it, because a layer that only ever runs over complete fixtures acquires
fallbacks that REQ-008 forbids and that would then be the first place a
presence-tier value could leak in. All work is bounded to this deliverable
folder and the `PKG-04` service-core source it names; this contract authorizes
no register, decomposition, PRD, or upstream-deliverable edit, and it neither
defines nor reshapes the entity model whose provenance it carries, the
reconcile that populates it, the return it stamps, the transport that serializes
it, or the surfaces that render, resolve, or measure it. Tests implement the
verification methods below and create no scope.

- **VER-001** — Stamp-completeness exercise: stamp fixture orientation responses and assert, field by field, that the examined-through SHA, the generation time, and per-feed freshness are each present and identifiable by name, that no stamp is emitted with a missing field, and that no stamp carries a fourth field.
- **VER-002** — Claim-coverage exercise: enumerate every claim in each fixture orientation response across every claim class the fixture contains, assert each carries a citation, and assert each citation resolves to a file path, anchor, and/or SHA identifying a live governed source; assert the enumeration finds no uncited claim.
- **VER-003** — Carry-through trace: for each citation in a stamped fixture response, trace it back to the provenance held by the record-tier entity behind its claim and assert byte equality; search this deliverable's source for path, anchor, or SHA synthesis, reconstruction, and default paths, for record-tier entity type and provenance field definitions, and for assumptions that an upstream schema, entity model, reconciler, store, or orientation builder artifact exists, asserting none; and assert no citation resolves to a PEC artifact, store record, or generated view.
- **VER-004** — SHA-stamp check: compare the stamped examined-through SHA against the value the fixture record tier carries for that response's examined state and assert byte equality; inspect this deliverable's source for SHA derivation, recomputation, inference, and comparison logic and assert none; and stamp over a fixture carrying no examined-through SHA, asserting the absence is stated rather than filled.
- **VER-005** — Per-feed freshness exercise: stamp over a fixture whose reconcile reports multiple feeds and assert one freshness entry per reported feed rather than an aggregate; compare each entry against the value the fixture record tier carries for that feed; and stamp over a fixture feed carrying no freshness value, asserting the entry is stated as unknown with no derived, defaulted, inferred, or carried-forward substitute.
- **VER-006** — Tier-exclusion exercise: stamp over a fixture carrying presence-tier records alongside the record tier and assert that no citation derives from or resolves to a presence-tier record; inspect this deliverable's source for presence-tier reads on any citation path, asserting none; and record explicitly, for the enforcement that depends on a presence tier first existing at `P3`, whether it was executed or is pending under CON-001, without reporting a pending enforcement as passing.
- **VER-007** — Content inspection: stamp over a content-dense fixture corpus carrying long prose bodies, authored ruling text, and diff-shaped content, then dump every citation and every stamp field and assert none carries file or diff content and none reproduces, excerpts, summarizes, or paraphrases the located text.
- **VER-008** — Absence and non-resolution exercise: stamp over fixture cases in which a claim's provenance is absent, a claim's provenance does not resolve, and each stamp field's value is in turn not carried; assert per case that the absence is stated against the affected claim or field, that no fabricated or approximate value is presented, that no affected claim is dropped silently, and that the recorded absence is readable by a consuming deliverable.
- **VER-009** — Write-boundary exercise: hash the fixture source corpus, record tier, and store before and after a stamping run and assert byte-identity; capture every filesystem and store write performed during the run and assert the inventory is empty; and inspect this deliverable's source for write, create, or delete calls against source, governed, register, lifecycle, or store targets and for any adoption-, ruling-, or direction-recording path, asserting none.
- **VER-010** — Adjacent-act inspection: inspect this deliverable's call graph and source for orientation-composition, delta-since-SHA, scope-parameterization, limitation-rendering, wire-envelope and serialization, socket, token, subscription, dashboard and drill-down rendering, pressure- and staleness-rule, rebuild, incremental-reconcile, drift-classification, presence-store TTL and guard, and defect-rate, latency, and adoption measurement paths, asserting each absent; and review this deliverable's tests for any criterion belonging to another deliverable, asserting none.
- **VER-011** — Inspect the `PKG-04` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` zero-dependency and locality enforcement once that deliverable is available, without discharging it here.
- **VER-012** — Universality exercise: stamp fixture responses of each kind the accepted sources name — a per-loop return, a delta return, a scope-parameterized return, and a return carrying stated absences — asserting per kind that VER-001's stamp completeness and VER-002's claim coverage both hold; and search this deliverable's source for any response kind, scope, or caller under which the stamp or citation obligation is conditional or skipped, asserting none.
- **VER-013** — Derivation-record exercise: read the stamp-and-citation derivation record (the component of OUT-001 required by REQ-014) and assert it declares, per stamp field and per cited claim class, its source, its applied rule including the feed set, freshness source, claim granularity, and generation-time representation, and its absence semantics, and that it states which value is stamped as the examined-through SHA and on what basis without presenting the choice as settled by an accepted source; then stamp over fixtures and assert each produced stamp field and citation follows the rule the record declares for it.
- **VER-014** — Run the `PKG-04` test suite and confirm that each of VER-001 through VER-013 has a corresponding automated test that either executes and passes or records a pending result under CON-001, and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-001` governs the citation limb: orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation. The citation is what makes an orientation answer checkable at all — without it a return is a set of assertions a reader must re-derive, which is the very cost the objective exists to remove. A claim emitted without a citation does not merely miss a field; it silently restores the prose-derivation burden for that claim while looking like a cited answer, which is why REQ-002 admits no exempt claim class.
- **AX-002** — `OBJ-002` and `PEC-K-04` govern the stamp limb: "Every response carries the examined-through commit SHA and per-feed freshness; consumers detect staleness structurally." The stamp exists so that judgment is unnecessary downstream. A SHA this layer computed, chose, or inferred would occupy the same field and look identical to a consumer while meaning nothing they could compare against, which is why REQ-004 forbids derivation rather than merely preferring carry-through — the failure mode is invisible at the point of use.
- **AX-003** — `PEC-K-05` two trust tiers, never blurred, is the invariant behind REQ-006, and this deliverable is one of the two places it is enforced. Presence data is fresher and would often look like the better citation — who is working where, what is live right now — and `PEC-PRS-007` forbids it entering record-tier citations. A citation is a promise about which tier a fact came from; blurring it here would make the record tier's guarantee unverifiable everywhere downstream, because a consumer inspects citations, not the layer that produced them.
- **AX-004** — `PEC-K-08` explainability and the drill-down obligation are the standard the citation shape is answerable to from outside: "Every status, verdict, and warning carries rule ID, threshold, and contributing cited sources. Drill-down never dead-ends", and `SOW-050` requires drill-down "from every displayed value to its cited source". Those are `DEL-09-06`'s and `DEL-09-07`'s scope items, not this contract's, and this contract asserts no drill-down behaviour; but a citation that does not resolve is exactly the dead end that obligation forbids, which is why REQ-002 requires resolution rather than mere presence and REQ-008 forbids emitting a non-resolving citation to preserve appearances.
- **AX-005** — `PEC-K-10` content-minimal is a residency posture, and a citation layer is where copying source text is most tempting: an excerpt beside a path would make a response more readable at a stroke. The strongest enforcement is upstream at the schema and the ingest guard, but this layer assembles located references into a response and is the last place text could enter, so REQ-007 binds the citation side directly.
- **AX-006** — `PEC-K-02` fixes what a citation may point at: "PEC output is never citable as authority". A citation resolving to a PEC store record or generated view would be circular — it would cite the projection rather than the file truth the projection was reconciled from — and would make the record tier's own claim of citability self-referential. REQ-003 states that as a checkable boundary.
- **AX-007** — Stratum is provenance, not authority, and this deliverable's graph position spans three strata, so the distinction is load-bearing rather than decorative. Register-wide constraint `C-10` `STRATUM_RULE` ends "strata are provenance not authority". The sole upstream edge `[E-P34]` is `PROPOSAL`, one downstream relation `[E-A21]` is `DECLARED`, one `[E-N04]` is `DERIVED`, and three are `PROPOSAL`; `D-PEC-62` §1(4) accepted all of them "all strata as presented", read in that packet as taking the exhibit's flags as flags. Every edge cited in this contract carries an empty `Flag` column. Citation converts no `PROPOSAL` into a `DECLARED` and weakens no `DECLARED` into a `PROPOSAL`.
- **AX-008** — The two scope items are mapped to objectives separately in the register and are kept separate here. `SOW-006` carries `OBJ-001;OBJ-002`; `SOW-007` carries `OBJ-001` alone. The frontmatter union matches `Deliverables.csv`'s `SupportsObjectives` cell, which the §3 union invariant produces from the item-level cells; it is not a licence to attribute `OBJ-002` to the citation limb. Every matrix row cites the objectives its own anchoring item carries. The distinction is not pedantry: `OBJ-002` is the structural-staleness outcome, and reading the citation limb into it would misplace where staleness detection is tested.
- **AX-009** — Edge direction is a constraint on this contract, not a licence. Upstream, `RequiredMaturity` `INITIALIZED` on `[E-P34]` means the upstream *contract* is the reliable input, not any upstream artifact; this contract is written against the obligations quoted in CLM-011 and CLM-012 and asserts nothing about upstream implementation state. Downstream, being measured by the orientation defect-rate spot-check and consumed by the pressure rules, the limitation renderer, the response format, and the drill-down component neither expands this contract's scope nor transfers any of theirs into it — least of all the defect-rate measurement, which tests `SOW-007` from outside under `SOW-059`.
- **AX-010** — Unknowns stay marked. TBD-001 through TBD-004 and CON-001 through CON-004 are recorded rather than resolved by inference. `C-02`'s direction is an open owner ruling and `OI-013` records that no durable register validator exists to catch register-hygiene gaps like the empty `EvidenceQuote` and "location TBD" `SourceRef` on this deliverable's own upstream row (CLM-010); a production choice that settled the first, or a quotation invented to fill the second, would be a decision taken in the wrong place. Where the accepted sources are silent — on claim granularity, on feed identity, on freshness units, on generation-time representation — this contract requires the choice to be declared rather than making it.
- **AX-011** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by this reconciliation; the deliverable is at `INITIALIZED` and nothing has been built.

**Quotation record.** Every quotation in this contract is verbatim from the
named source. **No quotation in this contract is elided**: there are zero
elisions, and no ellipsis of this contract's making appears inside any quoted
span. Three points are noted so they are not mistaken for elisions. The `..`
ranges inside the `A001`, `A002`, and `A003b` quotations in the objective
warrant are the sources' own range notation. The doubled quotation marks inside
the `C-02` constraint row quoted in CLM-014 are that CSV source's own escaping.
The `DEL-01-01` `REQ-003` record quoted in CLM-009 is reproduced from inside
`DEL-04-01`'s own blockquote of it, and is quoted in full as it appears there.
No annotation of this contract's making appears inside any quotation, and no
quotation omits text from the span it presents.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-006 OBJ-001 OBJ-002 | REQ-001, CLM-001, CLM-003, CLM-004 | AC-001 | VER-001 | Stamped fixture responses with a field-by-field completeness table showing all three PEC-ORI-003 fields present and no fourth |
| OUT-001 | SOW-007 OBJ-001 | REQ-002, CLM-002, CLM-003, CLM-008, CON-004 | AC-002 | VER-002 | Per-response claim enumerations with a citation and its resolution recorded against every claim, and a stated claim-class inventory showing none exempted |
| OUT-001 | SOW-007 OBJ-001 | REQ-003, CLM-009, AX-006 | AC-003 | VER-003 | Per-citation carry-through traces with byte equality against source-entity provenance, plus recorded searches for synthesis, default, and entity-definition paths and for upstream-artifact assumptions |
| OUT-001 | SOW-006 OBJ-001 OBJ-002 | REQ-004, CLM-011, CLM-012, CON-002, AX-002 | AC-004 | VER-004 | Byte comparison of the stamped examined-through SHA against the fixture record-tier value, the search record showing no derivation or comparison logic, and the no-SHA fixture stamp stating absence |
| OUT-001 | SOW-006 OBJ-001 OBJ-002 | REQ-005, CON-003 | AC-005 | VER-005 | Per-feed freshness entries matched against fixture record-tier values for a multi-feed reconcile, plus the unknown-freshness fixture stamp showing no substitute value |
| OUT-001 | SOW-007 OBJ-001 | REQ-006, CLM-014, CON-001, AX-003 | AC-006 | VER-006 | Presence-alongside-record fixture run showing no presence-derived or presence-resolving citation, the source inspection for presence reads, and the explicit executed-or-pending record for the P3-dependent enforcement |
| OUT-001 | SOW-007 OBJ-001 | REQ-007, AX-005 | AC-007 | VER-007 | Field-by-field dumps of citations and stamps over a content-dense fixture corpus showing no file or diff content and no reproduction of located text |
| OUT-001 | SOW-007 OBJ-001 | REQ-008, AX-004 | AC-008 | VER-008 | Per-case stamped responses for absent provenance, non-resolving provenance, and each uncarried stamp field, each stating the absence and presenting no substitute, with the recorded absence readable downstream |
| OUT-001 | SOW-006 SOW-007 OBJ-001 OBJ-002 | REQ-009, CLM-017 | AC-009 | VER-009 | Before/after hashes of the fixture corpus, record tier, and store, the empty write inventory for a stamping run, and the source inspection showing no write path and no adoption-, ruling-, or direction-recording path |
| OUT-001 | SOW-006 SOW-007 OBJ-001 OBJ-002 | REQ-010, CLM-007, CLM-013, CLM-016, TBD-002, AX-009 | AC-010 | VER-010 | Call-graph and source inspection records showing each named adjacent path absent, plus a review of this deliverable's tests confirming no criterion belonging to another deliverable |
| OUT-001 | SOW-006 SOW-007 OBJ-001 OBJ-002 | REQ-011 | AC-011 | VER-011 | Dependency-manifest and import-graph inspection records, plus the DEL-01-05 enforcement result once that deliverable is available |
| OUT-001 | SOW-006 SOW-007 OBJ-001 OBJ-002 | REQ-012, CLM-015, AX-001 | AC-012 | VER-012 | Stamped fixture responses of each named kind with stamp-completeness and claim-coverage results per kind, plus the source search showing no conditional or skipped obligation |
| OUT-001 | SOW-006 SOW-007 OBJ-001 OBJ-002 | REQ-013, REQ-014, TBD-003, TBD-004 | AC-013 | VER-013 | The stamp-and-citation derivation record (a component of OUT-001) with per-field and per-claim-class sources, rules, and absence semantics, the declared SHA basis, and fixture values traced to the declared rules |
| OUT-002 | SOW-006 SOW-007 OBJ-001 OBJ-002 | REQ-015, CLM-017 | AC-014 | VER-014 | PKG-04 test-run output mapping each executed test to its declared verification method, with pending results recorded as pending, and no criterion asserted that this contract does not state |
| OUT-001 | SOW-006 SOW-007 OBJ-001 OBJ-002 | CLM-005, CLM-006, CLM-010, TBD-001, AX-007, AX-008, AX-010, AX-011 | AC-015 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-006, SOW-007, OBJ-001, and OBJ-002, confirms the objective mappings are stated as register-direct and pre-SCA-002 with no unrecorded confidence label and no SOW-007-anchored attribution to OBJ-002, confirms the upstream and downstream edges are each stated at their own stratum, confirms the C-02 direction and its P1/P3 phase tension are recorded unresolved, and confirms no cross-package or sibling scope absorption | Review record citing the two ledger rows, the A001/A002/A003b evidence for the pre-existing objective mappings, the upstream register row with its stratum and its recorded evidence-cell gap, the five downstream relations with their strata, and the C-02 constraint row |
