# Guidance — DEL-089-05 Vendor Document Turnover Package (PKG-089)

> Directional. Explains why this deliverable exists, the principles that should guide assembly and review of the vendor document set, and the trade-offs encountered. Closes with a Conflict Table for items needing human ruling.

## Purpose

This deliverable is the **single source of truth for vendor documentation** on the PKG-089 Pig Receivers (Inlet) 3-25 package. Its role in the project is to:

- Concentrate the 109 source-listed vendor documents (ARTIFACT_REGISTER.csv DEL-089-05 rows) into one register so that EPC Integrator review (DEL-089-06) and downstream construction (DEL-089-03) consume a single, traceable submittal stream.
- Carry source vendor-document rows as artifacts — not as standalone deliverables — to keep the project's decomposition flat and the package boundary intact (DELIVERABLE_REGISTER.csv row 430 Notes).
- Produce the turnover record set (Vendor Data Book / Final Supplier Documentation) that closes out the vendor's documentation obligation before acceptance.

Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 430; PACKAGE_REGISTER.csv row 77.

## Principles

1. **Source-rooted register.** Every register row traces back to either (a) the `Vendor Engineering Deliverables` table in `26020-Package_Requirements.docx` heading 42, or (b) another accepted decomposition source. No invented documents.
2. **Package boundary is the unit of accountability.** Vendor produces; EPC Integrator reviews. Acceptance evidence belongs to DEL-089-06; this deliverable owns *production* of the submittals.
3. **Artifacts, not nested deliverables.** A vendor document line item is an artifact row, not a sub-deliverable. This preserves the project's flat package-deliverable hierarchy (K-HIER-1).
4. **Interface documentation is integration evidence.** The 10 source categories include interface disciplines (process piping, relief/flare/vent, drainage, electrical, I&C, structural, pipeline/pigging). These exist so EPC Integrator can verify integration without re-engineering. Treat their level-of-detail as "sufficient for integration review," not "sufficient to re-design."
5. **Identical-twin transparency.** PR-1010-2 and PR-1020-2 are an identical pair (SOW-0159). The register should describe them as one unit unless real deltas exist; deltas, if present, are itemized.
6. **Sour-service is non-trivial.** The 0.1 mol% sour design condition (SOW-0159) propagates into MTRs/certificates, ITP, and the Pressure Equipment Registration Package. The vendor document set should make sour-service compliance visible, not implicit.
7. **Sequencing matters even when not explicitly stated.** The Vendor Document Control Procedure is the earliest-submitted document by role (it governs every other submittal's flow). FAT Procedure precedes FAT Report. Pressure Equipment Registration precedes shipment. These sequencing inferences are labeled `ASSUMPTION` in the Specification because the source text does not state the sequence explicitly.
8. **Decomposition routes; sources govern.** The decomposition (DELIVERABLE_REGISTER.csv, ARTIFACT_REGISTER.csv) identifies *which* documents and categories apply. The source slices (`26020-Package_Requirements.docx` heading 42, `3-25_Comp_and_Liquids_DBM.md`) govern *what* those documents must contain. Where decomposition prose appears to add detail not in source, the source wins.

## Considerations

- **Two `.docx` source files (`26020-Package_Requirements.docx` and `26020-02-PT-RFQ-35-001-Pig_Recv_1.docx`) are binary and were not opened directly.** Their content reaches this draft only through the decomposition snapshot (registers and SCOPE_LEDGER). Any requirement that depends on language inside those `.docx` files but is not reflected in the registers is `location TBD`. Consider extracting these to markdown if more granular sourcing is required.
- **Objective association is heuristic.** OBJ-002 through OBJ-010 are associated to this deliverable via the package-grouping heuristic (PACKAGE_HEURISTIC default) since OBJECTIVE_DELIVERABLE_MAP is package-grouped at PKG-089, not deliverable-row-tied. This is labeled `ASSUMPTION` and a human ruling can re-scope.
- **EPC review interface is owned elsewhere.** Do not draft acceptance criteria, comment-resolution workflows, or rejection paths here — those belong to DEL-089-06. This deliverable produces submittals; DEL-089-06 evaluates them.
- **No declared upstream/downstream dependencies** at PREPARATION time (`_DEPENDENCIES.md`). The natural informational upstream is DEL-089-02 (Package Datasheet) and DEL-089-04 (Vendor Engineered Equipment Package); the natural downstream is DEL-089-06 (EPC Vendor Package Review and Acceptance). These relationships are not formally declared and should not be treated as gating without a `TASK + dependency-extract` run.
- **Code citations are absent from source slices.** ASME BPVC Section VIII, NACE MR0175/ISO 15156, and the jurisdictional pressure equipment authority (ABSA for Alberta) are *typical* references for the equipment class, but none are explicitly cited in accessible source. They appear in Specification.md Standards table as `ASSUMPTION`.

## Trade-offs

| Trade-off | Position taken | Rationale |
|---|---|---|
| Comprehensive register vs. compact register | Comprehensive (all 109 rows) | The decomposition source already chose comprehensiveness; this deliverable inherits that choice. |
| Promote each vendor document to a deliverable vs. carry as artifact | Carry as artifact | Decomposition explicitly chose this (DELIVERABLE_REGISTER.csv row 430 Notes); preserves flat hierarchy. |
| Define submittal lifecycle here vs. defer to DEL-089-06 | Define a minimal lifecycle here (REQ-004), defer acceptance gating to DEL-089-06 | Vendor needs a lifecycle to submit against; EPC owns the gate. |
| State sequencing as requirement vs. observation | State as requirement and label `ASSUMPTION` where source is silent | Sequence matters operationally; transparency about inference preserves auditability. |
| Treat interface documents as integration evidence vs. as design re-issuance | Integration evidence | EPC Integrator owns facility-level integration; vendor describes the interface, not the facility. |

## Examples

- **Register row example (representative shape):** `Vendor Document Control Procedure | Core vendor documents | ART-F156006A5E | Source: 26020-Package_Requirements.docx heading 42`. The register row carries the artifact ID and source. The actual document content is the vendor's submittal.
- **Lifecycle example (informative):** `planned -> submitted (Rev A) -> under EPC review -> returned with comments -> resubmitted (Rev B) -> accepted -> incorporated into Vendor Data Book`.
- **Sour-service traceability example:** MTRs cite material grade -> ITP cites the qualification tests for that grade against sour-service criteria -> Pressure Equipment Registration Package cites the MTRs and ITP -> Final Vendor Data Book aggregates the chain.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-001 | Submittal lifecycle states not explicitly defined in accessible source slice | `26020-Package_Requirements.docx` heading 42 (binary, not opened) | Project documentation control convention (not locally accessible) | Specification REQ-DEL-089-05-004; Procedure Steps; Guidance Examples | PROPOSAL: Adopt `planned -> submitted -> under EPC review -> accepted/returned -> incorporated` until vendor document control procedure is finalized | TBD |
| HRR-002 | Pressure equipment jurisdictional authority not explicitly named | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (does not name regulator) | Project location implicit (Alberta -> ABSA assumed) | Specification Standards table; REQ-005 | PROPOSAL: Adopt ABSA (Alberta) as jurisdictional pressure equipment authority pending project confirmation | TBD |
| HRR-003 | Sour-service material code not explicitly cited | SCOPE_LEDGER.csv SOW-0159 (states 0.1 mol% sour) | No explicit NACE MR0175 / ISO 15156 citation in accessible source | Specification Standards table; REQ-006 | PROPOSAL: Adopt NACE MR0175 / ISO 15156 as the governing sour-service material standard | TBD |
| HRR-004 | Pressure vessel design code not explicitly cited | PACKAGE_REGISTER.csv row 77 (cites equipment class) | No explicit ASME BPVC citation in accessible source | Specification Standards table; REQ-005 | PROPOSAL: Adopt ASME BPVC Section VIII (Div 1) as default for the receiver pressure vessels unless vendor specifies otherwise | TBD |
| HRR-005 | FAT-before-shipment sequencing not explicitly stated | ARTIFACT_REGISTER.csv DEL-089-05 (lists FAT Procedure and Report rows) | No explicit "before shipment" gating language in accessible source | Specification REQ-009; Procedure Steps | PROPOSAL: FAT Procedure submitted-and-accepted before FAT execution; FAT Report submitted before shipment release | TBD |
| HRR-006 | Vendor Document Control Procedure "earliest-submitted" sequencing inferred | ARTIFACT_REGISTER.csv DEL-089-05 (ART-F156006A5E) | No explicit sequencing in accessible source | Specification REQ-013; Procedure Steps | PROPOSAL: Vendor Document Control Procedure is submitted-and-accepted before any other submittal is logged into the register | TBD |
| HRR-007 | Objective association is package-grouped, not deliverable-row-tied | OBJECTIVE_DELIVERABLE_MAP.csv (PKG-089 grouping) | DELIVERABLE_REGISTER.csv row 430 (no explicit per-deliverable objective set) | Datasheet Identification (Supports Objectives); _CONTEXT.md | PROPOSAL: Maintain OBJ-002..OBJ-010 association as PACKAGE_HEURISTIC `ASSUMPTION` until human re-scopes | TBD |
| HRR-008 | Submittal medium, language, and review-cycle counts not in accessible source | Datasheet Conditions (`TBD`) | No accessible source slice | Datasheet Conditions; Procedure Prerequisites | PROPOSAL: Defer until project-level documentation control standard is referenced or finalized | TBD |
| HRR-009 | `26020-02-PT-RFQ-35-001-Pig_Recv_1.docx` (Bid Doc Word Source Basis) not opened directly (binary) | `_REFERENCES.md` (cites the file) | File not extracted to markdown | All sections that might cite RFQ-specific clauses | PROPOSAL: Extract RFQ to markdown if any clause-level requirement is contested; otherwise defer | TBD |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `Datasheet.md` (this folder)
- `Specification.md` (this folder)
- `Procedure.md` (this folder)
- GATE-07 PROJECT_DECOMP snapshot — DELIVERABLE_REGISTER.csv row 430; PACKAGE_REGISTER.csv row 77; SCOPE_LEDGER.csv SOW-0157..0160; ARTIFACT_REGISTER.csv DEL-089-05 rows; OBJECTIVE_DELIVERABLE_MAP.csv PKG-089 rows
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 226-239
