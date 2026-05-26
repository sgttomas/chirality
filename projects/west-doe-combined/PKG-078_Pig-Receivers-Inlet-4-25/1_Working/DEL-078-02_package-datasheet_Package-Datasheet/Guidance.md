# Guidance — DEL-078-02 Package Datasheet (Pig Receivers (Inlet) 4-25)

Directional guidance for authoring, using, and consuming the PKG-078 Package Datasheet. Guidance is grounded in accessible sources; speculative material is marked `TBD` or `ASSUMPTION`.

## Purpose

The Package Datasheet is the EPC Integrator's source-supported technical handoff to the Package Vendor and to downstream disciplines. It carries the data needed to engineer, design, fabricate, and integrate three identical 24-inch inlet pig receivers with HIPPS at the 04-25 facility, expressed as values traceable to the workbook row 78 entry, the `26020-Package_Requirements.docx` package heading 31 extraction (SCOPE_LEDGER `SOW-0161` to `SOW-0164`), and the DBM-Deepcut basis document (SEC-04).

Per `_CONTEXT.md`, this is a "Mandatory Gate 5 EPC anchor deliverable; interface facts are intentionally carried here as evidence rather than standalone deliverables."

## Principles

1. **Source fidelity over convention.** Where decomposition prose and accessible source text both speak, use the source text. The decomposition tells you which package this is and where it sits in the WBS; it does not invent design values.
2. **Interfaces are first-class on this datasheet.** PKG-078 carries ten declared interface types (see Datasheet). The matrix is intended to be exhaustive at the interface-type level even when per-interface engineering remains TBD.
3. **Sour service is non-negotiable.** All MOC, vent routing, purge, and HIPPS arrangements interpret in the context of sour-service classification (H2S design 1.0 mol%; ref `SOW-0163` and DBM SEC-04).
4. **HIPPS arrangement is prescribed, not optional.** `SOW-0163` requires both a primary pneumatic hi-low shutdown and a redundant pneumatic hi-low shutdown. Vendor proposals that reduce redundancy require an explicit human ruling.
5. **By Others is explicit.** Interconnecting piping, DCS integration, foundations, and electrical supply to MCC are explicitly outside vendor scope per `SOW-0164`; the datasheet must restate them on the vendor side of the boundary so they are not silently absorbed.
6. **TBD over invention.** Several quantities (normal flowrate per receiver, MOC class, relief sizing basis, EHT extent) are not stated in accessible sources and remain TBD pending vendor or detailed-engineering resolution.

## Considerations

- **Pressure-envelope coherence.** The DBM lease-boundary basis is 1100 psig (with detailed-engineering confirmation pending) while the package operating window per `SOW-0164` is 653-725 psig with MAOP 1300 psig. The pressure transition between lease boundary and receiver inlet is governed by upstream facility piping and the HIPPS arrangement itself; the Package Datasheet should document the receiver-side envelope, not the upstream pressure reduction.
- **Pig-launcher pairing.** PKG-078 receives pigs sent from upstream launchers. Pipeline/Pigging interface (`IFC-65EDB92369`) needs to be reconciled with the actual launcher location and pig type during detailed engineering; not stated in available sources.
- **Comparison with 3-25 receivers (PKG-089).** The sister package PKG-089 (Pig Receivers Inlet 3-25) uses 2 receivers with ESDV (no HIPPS) at much lower pressures (MAOP 572 psig per `SOW-0160`). Treat any reuse of PKG-089 datasheet content as `ASSUMPTION` until confirmed against PKG-078 sources; the two packages share an interface-type set but diverge in sizing, redundancy strategy, and pressure class.
- **HP flare routing.** The vent line from each receiver enters the HP flare system (`SOW-0163`). Coordination with the facility flare header sizing belongs in the flare deliverable; the datasheet only declares the tie-in and load on a "per-receiver vent" basis.
- **Drain and containment.** Drain/Containment is a declared interface (`IFC-17309B535C`); sour drain compatibility and spill containment grading must be coordinated with facility civil/process design.
- **Maintenance access.** Pig handling requires a maintenance access envelope (`IFC-A553991A6E`); the datasheet should record any vendor-required clear zones for door opening, pig handling equipment, and operator access even though specific dimensions are TBD.

## Trade-offs

- **Vendor flexibility vs. interface determinism.** Tight datasheet language reduces vendor optionality but reduces interface rework. For a sour-service HIPPS-protected high-pressure inlet, lean toward interface determinism.
- **Carrying TBDs vs. inventing values.** Carrying a small number of explicit TBDs is preferable to populating defaults that may misalign with vendor design; downstream review (DEL-078-06) is the correct place to close them.
- **Single datasheet vs. multiple vendor-side datasheets.** EPC-side datasheet remains a single artifact per `_CONTEXT.md`; vendor will produce their own internal datasheet set inside DEL-078-04 / DEL-078-05.

## Examples

- **Interface row pattern.** Each PKG-078 interface row carries InterfaceID (from INTERFACE_REGISTER), interface type, counterparty boundary description, and source. Example: `IFC-49A2026DAA | Process Piping | Facility process piping at receiver inlet and outlet flanges | INTERFACE_REGISTER row 647`.
- **Operating envelope row pattern.** `Normal operating pressure | 653 to 725 psig | SOW-0164`.
- **TBD with provenance pattern.** `Materials of construction | TBD by Package Vendor for stated sour service (1.0 mol% H2S) | SOW-0163; specific MOC class not stated in available sources`.

## Conflict Table (for human ruling)

No fact-level conflicts were detected between the four documents in Pass 2. The package operating window vs. lease-boundary pressure relationship is noted as `ASSUMPTION` rather than `CONFLICT` because both values come from different scopes (package boundary vs. lease boundary) and are not strictly contradictory.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none) | No fact-level conflicts detected in Pass 2 | — | — | — | — | TBD |
