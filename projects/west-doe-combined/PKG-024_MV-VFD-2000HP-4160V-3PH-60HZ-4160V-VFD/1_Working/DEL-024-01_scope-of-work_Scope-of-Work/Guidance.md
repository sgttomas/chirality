# Guidance: DEL-024-01 Scope of Work

## Purpose

This Scope of Work exists to give the EPC Integrator a bounded, source-traceable package integration basis for PKG-024 (`MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD`) before downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance work proceeds.

The source basis is intentionally narrow. Workbook row 26 (carried via Gate 7 registers) establishes the package identity and interface flags; Gate 7 establishes the mandatory EPC anchor deliverable basis (DEC-001) and the Package Vendor / EPC Integrator responsibility split; the DBM-Deepcut provides facility-level medium-voltage VFD and 4.16 kV MCC context. Package-specific MV VFD design details remain `TBD` unless later source material provides them.

## Principles

- Preserve the source spelling `MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD` in identity fields because it is the accepted workbook/Gate 7 package name.
- Treat the Scope of Work as an EPC integration document, not a vendor design document.
- Keep Package Vendor responsibilities (package engineering, design, vendor documentation, physical equipment supply) separate from EPC Integrator responsibilities (facility integration, interfaces, constructability, procurement/construction coordination).
- Include only source-supported package interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
- Use the DBM-Deepcut MV/VFD basis as facility context only; do not infer specific VFD topology, harmonic mitigation, cooling, enclosure, control architecture, or driven motor identity from it.
- Prefer `TBD` over inferred technical values where accessible sources do not provide package-specific detail.

## Considerations

The package title indicates a 2,000 hp, 4,160 V, 3-phase, 60 Hz medium-voltage VFD with 4,160 V output. The DBM-Deepcut facility basis confirms that medium-voltage VFDs are a recognized equipment class housed in prefabricated electrical buildings, that the 4.16 kV MCC connects to the plant PLC over Ethernet, and that "VFD and soft-starter requirements for 4.16 kV motors are TBD" at the facility-basis level. This supports framing the package as a facility-aligned MV VFD; it does not support assuming a specific driven motor tag, process service, VFD topology, input cell count, output filter, bypass arrangement, harmonic mitigation strategy, cooling method, enclosure type, or control protocol.

The workbook and Gate 7 interface basis flags six interface categories. These interfaces should drive the SOW boundary narrative and later construction coordination. They should not be expanded to additional interface categories unless later accepted sources add them.

The objective-to-deliverable map associates DEL-024-01 with OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, and OBJ-010. These should be carried as accepted directional context; they should not be used to manufacture package-specific requirements not otherwise supported by source materials.

## Trade-offs

| Topic | Conservative treatment | Risk if overstated |
|---|---|---|
| Package function | Describe as an MV VFD package nominally rated 2,000 hp, 4,160 V, 3-phase, 60 Hz with 4,160 V output, integrating with the facility 4.16 kV MCC basis; mark detailed driven service and topology `TBD`. | The SOW could incorrectly bind the package to a specific driven motor, process service, or VFD topology before vendor and process data is available. |
| EPC responsibility | State facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance review. | EPC scope could accidentally absorb vendor package engineering, design, documentation, or equipment supply obligations. |
| Technical values | Use only source-supported values and `TBD` elsewhere. | Unsupported values (driven motor tag, harmonic mitigation strategy, cooling, enclosure rating, weights, control protocol, protection settings) could propagate into datasheets, procurement, or construction packages. |
| Interface list | Use exactly the six Gate 7 interface categories for PKG-024. | Adding or omitting interface categories would diverge from accepted upstream truth. |
| Source spelling | Preserve `MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD` as the accepted package name (noting the redundant `4160V` and `4160V VFD` phrasing in the source). | Normalizing the spelling could break register traceability or appear to alter accepted upstream truth. |

## Examples

- Acceptable SOW language: "PKG-024 is the workbook-defined Electrical package `MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD`, WBS 01, tracking number `26020-01-30-015`; the Package Vendor owns package engineering/design/equipment/vendor documentation and the EPC Integrator owns facility integration and interface coordination across Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports."
- Acceptable SOW language: "Driven motor tag and service, VFD topology, harmonic mitigation, cooling, enclosure, control protocol, and protection settings are TBD pending vendor/process data."
- Avoid: "The EPC Integrator shall design the MV VFD." Gate 7 assigns package engineering and design to the Package Vendor.
- Avoid: "The VFD shall be an N-cell cascaded H-bridge with active front end and integral output filter." No accessible source slice supports a specific topology.
- Avoid: "The VFD drives the [named compressor/pump motor]." No accessible source slice ties PKG-024 to a specific driven motor or process service.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-024-01-01 | Package name contains the apparently redundant phrasing `... - 4160V, 3PH, 60HZ - 4160V VFD`. Whether the trailing `4160V VFD` clause is an output-voltage qualifier or a source-row artifact is not stated. | Workbook Packages row 26 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-024 use `MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD`. | Engineering convention typically distinguishes input vs. output voltage; no accessible source clarifies this. | Identity fields and Specification SOW-024-05. | Preserve accepted source spelling for traceability; interpret as 4,160 V input and 4,160 V output for SOW framing while flagging for human confirmation. | TBD |
| HR-024-01-02 | The driven motor (process service, tag, manufacturer) for the 2,000 hp 4,160 V VFD is not identified in accessible sources. The DBM-Deepcut explicitly states that 4.16 kV VFD/soft-starter requirements are TBD at the facility-basis level. | Workbook Packages row 26; Gate 7 `PACKAGE_REGISTER.csv` row PKG-024. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2957, 3088. | Datasheet Attributes/Conditions, Specification SOW-024-05/06, Procedure Steps, downstream Datasheet/Construction Work Package. | Treat the package as a standalone MV VFD identity for SOW purposes; defer driven-motor assignment to vendor/process data and keep tag and service `TBD`. | TBD |
| HR-024-01-03 | The Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` lists seven objectives for DEL-024-01 using a package-grouped pattern; this is consistent across all PKG-024 deliverables. Whether each objective is individually binding on the Scope of Work or directional context is not stated. | Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` DEL-024-01 rows. | Gate 7 `PROJECT_DECOMP.md` (no per-deliverable per-objective requirement extraction). | Specification SOW-024-09; downstream objective traceability. | Treat objective associations as accepted directional context (ASSUMPTION: best-effort mapping per PACKAGE_HEURISTIC) and do not derive requirements solely from objective IDs. | TBD |
