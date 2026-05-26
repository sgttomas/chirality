# Guidance — DEL-104-03 Construction Work Package

## Purpose

The Construction Work Package exists so that the structural-steel-outside-of-modules scope (PKG-104) is physically installed, inspected, tied in, and turned over in a way that preserves the project's civil/structural design basis, satisfies the project Construction Responsibility model, and produces the handoff evidence required for facility commissioning and operations.

It bridges the package's design intent (PKG-104 datasheet and discipline production package) with field execution by Tourmaline Oil Corporation, and it captures the construction-side interface and turnover evidence needed by `OBJ-001` (Deepcut facility scope delivery), `OBJ-008` (civil/structural/site/construction support scope), and `OBJ-010` (operability/maintainability/turnover/closure evidence).

Sources: `OBJECTIVE_REGISTER.csv`; `4-25_Deepcut_DBM.md` Construction Responsibility; `_CONTEXT.md`.

## Principles

- **Source-anchored construction basis.** All material grades, design codes, foundation defaults, and grading criteria carried into the work package are taken from the project DBM (Section: Governing Civil and Structural Basis; Piles and Foundations; Site Grading and Surface Water Management). Where the geotechnical report or detailed engineering refines these, the refined values govern.
- **Construction Responsibility honoured at the interface.** Tourmaline performs field construction (`4-25_Deepcut_DBM.md` Construction Responsibility); the EPC Integrator's Construction Work Package coordinates with — but does not redefine — that field execution model.
- **Joint planning at every tie-in.** Tie-ins to existing or related facilities, and ISBL/OSBL interconnecting piping, are explicitly called out in the DBM as requiring joint planning and per-tie-in responsibility confirmation. Treat these as planned, evidenced events, not implicit completions.
- **Preserve access and future plot provisions.** Layout decisions (access routes, maintainability envelopes, modular erection access, emergency response, hazardous-area separation, future plot provision) shall not be foreclosed by construction sequencing or temporary works.
- **Evidence over assertion.** Turnover relies on documented checklist closure (`ART-8131641C3B`); open items are reconciled, not declared closed.

## Considerations

- **Geotechnical timing.** Bearing capacity, LPILE curves, dynamic design criteria, and road pavement design are TBD pending the geotechnical report. Construction sequencing must accommodate this dependency before pile and foundation work for affected scope begins.
- **Compressor and dynamic-load foundations.** Compressor foundation arrangement and dynamic analysis are TBD per DBM; if PKG-104 steel ties into compressor support steel, dynamic-load coordination is required.
- **Pipe-rack interface.** Although pipe racks are a distinct workbook package, the grading basis (high ridges at main pipe racks; 1.5% pad slope from pipe racks) constrains where and how outside-of-module structural steel can be installed.
- **Interface facts.** The two PKG-104 interface facts (`IFC-CCDE4B56CA` Grading/Site Drainage/Spill Containment; `IFC-ECDD4D3A15` Structural/Foundations/Supports) are the primary construction-coordination touchpoints.
- **Modular-vs-field boundary.** "Outside of modules" implies steel is field-erected; sequencing must permit module setting, mechanical hookup, and miscellaneous structural support installation per the DBM Construction Responsibility table.

## Trade-offs

- **Pile design conservatism vs. geotechnical timing.** Conservative driven-steel-pile default (DBM) enables early procurement and sequencing planning, but final pile lengths/spacing remain TBD pending geotechnical report. Trade-off: order long-lead steel against geotechnical risk.
- **Field-erection density vs. access.** Adding field-erected steel improves structural performance but can crowd access envelopes mandated by the DBM layout basis. Resolve via layout walk-downs before fabrication is released.
- **Inspection rigour vs. schedule.** A code-compliant ITP (CAN/CSA-S16 fabrication and erection) supports turnover evidence (OBJ-010) but adds hold/witness time; under-rigorous inspection risks rework and turnover deferral. ASSUMPTION: an ITP is included; this is not explicitly mandated at package scope in accessible sources.

## Examples

- **Foundation default applied (DBM source).** Driven steel piles are the default foundation basis for "other buildings, equipment, towers, tanks, modules, pipe racks, and similar structures" — applicable to outside-of-module structural steel supports unless detailed engineering justifies otherwise (`4-25_Deepcut_DBM.md` Piles and Foundations).
- **Grading-interface example (DBM source).** Pad slope from pipe racks at 1.5% per side, reducible to 1.0% to maintain reasonable top-of-pile-cap elevations — the Construction Work Package's pile-cap and column-base elevations must be coordinated with this grading basis (`4-25_Deepcut_DBM.md` Site Grading and Surface Water Management).
- Additional package-specific examples (e.g., specific column-line erection sequencing, specific tie-in scopes): TBD — not present in accessible source slices.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-104-03-01 | Responsible Party is `EPC Integrator` per `_CONTEXT.md`, but `4-25_Deepcut_DBM.md` Construction Responsibility assigns field construction (including installation of miscellaneous structural supports) to Tourmaline Oil Corporation. The Construction Work Package therefore has two parties: EPC Integrator authors and owns the package; Tourmaline executes the field work. | `_CONTEXT.md` ResponsibleParty | `4-25_Deepcut_DBM.md` Construction Responsibility | Datasheet Identification; Specification REQ-104-03-01; Procedure Prerequisites/Steps | PROPOSAL: Treat EPC Integrator as deliverable author/owner and Tourmaline as field execution authority; reflect both in the Construction Work Package responsibility matrix. | TBD |
| CONF-104-03-02 | Anticipated artifact list in `_CONTEXT.md` enumerates three artifacts (work package, workface plan, turnover checklist), but no source slice defines the package-specific ITP, MTR set, or NDE plan typically expected for a structural-steel construction work package. Specification REQ-104-03-12 marks this an ASSUMPTION. | `_CONTEXT.md` Anticipated Artifacts; `ARTIFACT_REGISTER.csv` PKG-104 rows | EPC convention / no source slice | Specification Documentation; Procedure Records | PROPOSAL: Either expand the artifact register to include ITP/inspection records or confirm that they are sub-records within the three named artifacts. | TBD |
| CONF-104-03-03 | `_REFERENCES.md` lists `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` under the shared source root, but these were not opened as source slices during this run. Several DEL-104-03 attributes (vendor-document register expectations, package-interface matrix detail, package-level turnover document list) may be more fully defined there. | `_REFERENCES.md` Shared Source Root | (file present, not opened) | Datasheet Construction (turnover acceptance basis); Specification Documentation | PROPOSAL: Open the two `.docx`/`.xlsx` sources in a subsequent pass (e.g., during semantic-lensing P3 or a targeted enrichment) and reconcile TBDs. | TBD |
