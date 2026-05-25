# Guidance: DEL-036-03_construction-work-package

## Purpose

The Construction Work Package is the EPC Integrator's operational bridge between the vendor-supplied 6.9kV switchgear electrical building (`PKG-036` / building 830-1) and the running facility. It exists to ensure that a shop-prefabricated electrical-building module is physically installed, tied in, inspected, and turned over with full coverage of every facility interface the package declares (`PACKAGE_REGISTER.csv` row `PKG-036`; `DELIVERABLE_REGISTER.csv`). It does not replace, restate, or override the vendor's engineering deliverables; those belong to `DEL-036-04`.

## Principles

- **Responsibility split is fixed.** Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. The Construction Work Package operates strictly within the EPC Integrator side of this split. (`PACKAGE_REGISTER.csv` row `PKG-036`.)
- **Construction follows the building basis.** Electrical buildings in this facility are shop-prefabricated, modular, elevated on piles for bottom cable entry, climate-controlled with n+1 HVAC, and internally wired with TECK/ACIC cables and EMT for adjacent equipment. The Construction Work Package shall mirror these construction realities rather than re-deriving them. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph.)
- **Grounding is non-negotiable.** Two-point ground-grid connection per major equipment, building ground wells with bolted test points, compression-type connections, and PVC-protected above-grade green-insulated grounding conductors are baseline requirements rather than design choices. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding paragraph.)
- **Every declared interface earns a workface section.** The package declares 12 interface types in the Gate 7 interface register; the workface plan shall have an explicit section per interface so that no tie-in is omitted in construction sequencing. (`INTERFACE_REGISTER.csv` `PKG-036`.)
- **Turnover is the gate.** The construction-interface and turnover checklist is the artifact that transfers responsibility downstream; nothing leaves construction without it. (`ARTIFACT_REGISTER.csv` `ART-A5CFBCEAB9`.)

## Considerations

- The 6.9 kV class places the building in the medium-voltage population fed from the 13.8 kV main switchgear; bottom-entry cable management and ground-well access are the dominant construction constraints. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Plant Power Distribution and Electrical Buildings paragraphs.)
- The DBM electrical-building-type table assigns this class of building to "Shop" prefabrication; site work concentrates on foundation, set, cable pulls, terminations, grounding, HVAC commissioning, and tie-in walkdowns rather than on-site assembly. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-building-type table.)
- A package-specific slice for `PKG-036` was not located in `26020-Package_Requirements.docx`; detailed construction specifics (e.g., ITP content, specific test procedures, contractor qualifications) must be sourced from the detailed-design package, not invented here.

## Trade-offs

- **Workface plan depth vs. vendor scope encroachment.** A deeper workface plan reduces field rework but risks re-deriving vendor-owned work. Keep workface plan content scoped to integration, tie-ins, and turnover — not to package internal engineering.
- **Inspection coverage vs. schedule.** Full per-interface walkdowns provide highest assurance; partial sampling accelerates turnover but increases turnover-checklist exception load.

## Examples

- The `PACKAGE_REGISTER.csv` "Applicable interface types" list (12 types) maps directly to 12 workface plan sections.
- The "elevated on piles" construction reality determines that cable-pull sequencing precedes building set on some sites and follows it on others; the workface plan resolves that order before mobilization.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-036-03-001 | Building number "830-1" in `PACKAGE_REGISTER.csv` row `PKG-036` is labeled "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)" while `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical-building-type table lists "830-1" as the 4.16 kV Acid Gas / Overheads Compressor Electrical Building and "820-1" as the 6.9 kV Inlet / Sales Compressor Electrical Building. | `PACKAGE_REGISTER.csv` row `PKG-036`; `_CONTEXT.md` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-building-type table | Datasheet → Identification; Specification → Scope and Standards; Guidance → Purpose | Treat `PACKAGE_REGISTER.csv` (Gate 7 authoritative companion register) as governing identity for the deliverable. Surface the DBM mismatch to the human for ruling without altering the deliverable identity. | TBD |
| HRR-036-03-002 | Detailed inspection, test, and acceptance criteria for installed equipment are not present in accessible source slices; REQ-036-03-010 is currently ASSUMPTION-grade only. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (no detail) | `_Sources/26020-Package_Requirements.docx` (no `PKG-036` slice accessible) | Specification → Requirements (REQ-036-03-010), Verification | Defer to detailed-design ITP for `PKG-036` once accessible; mark REQ-036-03-010 ASSUMPTION until then. | TBD |
| HRR-036-03-003 | Objectives OBJ-001/004/005/006/007/008/009/010 are mapped to `DEL-036-03` by package-grouped `OBJECTIVE_DELIVERABLE_MAP.csv` rows; mapping is package-heuristic in nature. | `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-036-03` | `_CONTEXT.md` (records same eight objectives) | Datasheet → Identification; Guidance → Purpose | Carry as ASSUMPTION (best-effort mapping) until human confirms or refines per-objective applicability. | TBD |
