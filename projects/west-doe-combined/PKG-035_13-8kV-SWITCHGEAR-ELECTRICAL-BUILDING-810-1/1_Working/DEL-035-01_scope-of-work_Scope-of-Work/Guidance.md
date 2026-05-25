# Guidance: DEL-035-01 Scope of Work

## Purpose

This Scope of Work exists to give the EPC Integrator a bounded, source-traceable package integration basis for PKG-035 (the 810-1 13.8 kV Switchgear Electrical Building) before downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance work proceeds.

The source basis is narrow but materially richer than for many other packages: workbook row 37 establishes package identity and interface flags; Gate 7 establishes the mandatory EPC anchor deliverable and the Package Vendor / EPC Integrator responsibility split; the DBM-Deepcut electrical narrative establishes the 13.8 kV switchgear function as the plant main distribution center, the utility supply basis, the downstream radial distribution targets, the medium-voltage system parameters, and the 810-1 building identity; the DBM-Comp_and_Liquids narrative establishes the housed-equipment scope and coordination requirements. Package-specific switchgear ratings, building dimensions, structural loads, HVAC heat load, and fire & gas device counts remain `TBD` until vendor or source data is available.

## Principles

- Treat the Scope of Work as an EPC integration document, not a vendor design document.
- Keep Package Vendor responsibilities (package engineering, design, vendor documentation, equipment supply) separate from EPC Integrator responsibilities (facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, acceptance).
- Include all twelve source-supported package interfaces from workbook row 37; do not silently drop interface categories.
- Use the DBM-Deepcut 13.8 kV switchgear narrative as the authoritative facility-level function basis; preserve its statements about utility supply, transformer step-down, bus sizing, radial distribution, downstream targets, and 03-25 / 04-25 shared scope.
- Preserve the building identifier `810-1` and the Shop-delivered building convention.
- Prefer `TBD` over inferred technical values where accessible sources do not provide package-specific detail (ratings, dimensions, loads, device counts).
- Surface the 03-25 / 04-25 shared distribution scope as an integration concern requiring later detailed-engineering confirmation; do not silently allocate split shares.

## Considerations

The 810-1 building is identified in the DBM-Deepcut Electrical Buildings table as a Shop-delivered pre-engineered building, and the 13.8 kV switchgear it houses is described as the plant main power distribution center for the facility. This supports stating the building's facility-level role and the system architecture (utility feed, step-down transformer, radial outgoing feeders). It does not support stating switchgear short-circuit ratings, bus continuous current, breaker quantity, or lineup configuration; those remain `TBD`.

The package has the largest source-supported interface footprint of the Gate 7 EPC anchor packages (twelve interface categories). The Scope of Work should preserve the full interface list as the EPC integration boundary and identify each as requiring coordination, without expanding to design responsibilities.

The DBM explicitly states that incoming power metering, protection coordination, and the emergency / standby power scope split between 03-25 and 04-25 are to be confirmed during detailed engineering. The Scope of Work should mirror that posture and not pre-decide those splits.

## Trade-offs

| Topic | Conservative treatment | Risk if overstated |
|---|---|---|
| Switchgear function | Describe as the plant main 13.8 kV distribution center per DBM narrative; mark ratings, bus continuous current, and breaker count `TBD`. | The SOW could lock in unverified switchgear ratings before vendor data is available. |
| Utility supply / transformer | State the 25 kV BC Hydro feed and the 25 kV/13.8 kV, 50 MVA utility-supplied transformer per DBM; flag "25 kV (TBC)" carefully. | EPC scope could be sized against unverified utility-interface assumptions. |
| Downstream distribution | List the five downstream electrical buildings per DBM as radial feeder destinations. | Adding feeders not stated in source could misallocate procurement and construction scope. |
| EPC responsibility | State facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance review. | EPC scope could accidentally absorb vendor package design obligations. |
| Shared 03-25 / 04-25 scope | Flag as confirmed-during-detailed-engineering item per DBM. | Pre-deciding the split could conflict with future facility integration decisions. |
| Building basis | Identify 810-1 as a Shop-delivered electrical building housing the listed equipment classes; mark dimensions, structural loads, and HVAC heat load `TBD`. | Pre-declaring building size, weight, or HVAC capacity could break later vendor design and structural coordination. |

## Examples

- Acceptable SOW language: "PKG-035 is the workbook-defined Electrical package `13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1)`, WBS 01, tracking number `26020-01-30-026`; the Package Vendor owns package engineering/design/equipment and the EPC Integrator owns facility integration and interface coordination for the twelve source-supported interface categories."
- Acceptable SOW language: "The 13.8 kV switchgear housed in 810-1 functions as the plant main power distribution center, fed from a BC Hydro 25 kV supply via a 25 kV/13.8 kV, 50 MVA utility-supplied transformer, and distributes power radially through step-down transformers to the 6.9 kV, 4.16 kV, 600 V, and 4.16 kV/600 V downstream electrical buildings."
- Acceptable SOW language: "Switchgear ratings, bus continuous current, short-circuit rating, breaker count, building dimensions, structural loads, HVAC heat load, and fire & gas device list are TBD pending vendor / source data."
- Avoid: "The EPC Integrator shall design the 13.8 kV switchgear lineup." Gate 7 assigns package engineering and design to the Package Vendor.
- Avoid: Specific switchgear short-circuit ratings, breaker counts, or building dimensions. No accessible source slice supports those values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-035-01 | Incoming utility voltage is stated as "25 kV (TBC)" in the DBM; the value is explicitly To-Be-Confirmed at the source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` 13.8 kV switchgear narrative (line 2917) | None contradicting; no accepted updated source. | Datasheet Conditions, Specification Requirements, Procedure Steps. | Preserve "25 kV (TBC)" with explicit TBC flag in SOW; do not normalize to a confirmed value. | TBD |
| HR-035-02 | Package-specific switchgear ratings, building dimensions, structural loads, HVAC heat load, and fire & gas device list are not exposed in accessible sources. | Workbook row 37 gives identity and interface flags only. | DBM gives facility-level function and system voltages, but not package-specific design configuration. | Datasheet Conditions, Specification Requirements, Procedure Steps. | Treat DBM as facility context and keep package-specific technical values as `TBD` pending vendor / source data. | TBD |
| HR-035-03 | The 03-25 / 04-25 shared distribution scope, incoming power metering, protection coordination, and emergency / standby power scope split are stated as items to be confirmed during detailed engineering. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` 13.8 kV switchgear narrative (line 2927) | None contradicting. | Specification scope and verification; Procedure steps. | Carry forward as open items requiring detailed-engineering confirmation; do not pre-allocate splits. | TBD |
