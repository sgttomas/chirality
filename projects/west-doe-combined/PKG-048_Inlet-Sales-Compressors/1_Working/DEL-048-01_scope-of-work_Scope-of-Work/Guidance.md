# Guidance: DEL-048-01 — Scope of Work, PKG-048 Inlet / Sales Compressors

## Purpose

PKG-048 supplies the central gas-compression service for the 04-25 West Doe Deep Cut Gas Plant expansion. The five (5) multi-service reciprocating compressor packages combine sour inlet compression and sweet sales gas compression on a single frame per package. This arrangement is intended to:

- balance loading across the process plant,
- limit single-package downtime production loss to approximately 20%, and
- improve flow stability compared with a conventional split inlet/sales arrangement.

Source: DBM-Deepcut SEC-05 Compression Configuration; PACKAGE_REGISTER.csv Scope.

This deliverable (DEL-048-01) is the **EPC Integrator's Scope of Work record** for PKG-048. It documents what the EPC Integrator is contractually accountable for integrating into the facility, distinct from what the Package Vendor supplies inside the package boundary.

Source: _CONTEXT.md (Scope; ResponsibleParty); PACKAGE_REGISTER.csv Responsibility.

## Principles

1. **Two responsibility envelopes.** The Package Vendor owns the package envelope (engineering, design, vendor documentation, physical equipment). The EPC Integrator owns the facility envelope (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). The Scope of Work record shall not blur these envelopes.
   Source: PACKAGE_REGISTER.csv Responsibility.

2. **Five identical packages, no installed spare.** Production loss exposure per package is approximately 20%. Constructability, maintenance access, and tie-in arrangement shall preserve the option to isolate one package without forcing total plant shutdown.
   Source: DBM-Deepcut SEC-05 Compression Configuration.

3. **Common frame multi-service complexity.** A single compressor frame supports both sour inlet and sweet sales services. EPC integration shall recognize the shared utilities (lube oil, seal-pot drain/vent system, air-cooler frame, electrical and I&C interfaces) and the need to prevent sour gas backflow into sweet-service distance pieces.
   Source: DBM-Deepcut SEC-05 Inlet/Sales Compressor Basis.

4. **Source-grounded basis.** Design parameters are taken from DBM-Deepcut SEC-05 as the current authoritative source for compression services at 04-25. Workbook Packages row 65 and the RFQ (26020-01-PT-12-003) provide contracting context but several values in those sources have not been read as text in this initialization run — see Missing Sources.
   Source: _REFERENCES.md; PACKAGE_REGISTER.csv Source.

5. **Mandatory Gate 5 EPC anchor.** This deliverable is a mandatory Gate 5 EPC anchor deliverable defined by user instruction. Any later scope-change or substitution must traverse the governed change process; this document is not the authoritative engineering basis but the contractual scope record.
   Source: _CONTEXT.md Notes; DELIVERABLE_REGISTER.csv Notes.

## Considerations

- **Conflicts with binding contractual impact** (see Conflict Table) include frame model selection, motor horsepower rating, motor start method, and recycle-valve fail positions. The Scope of Work record shall capture these as unresolved items, not silently choose one side.
- **Cross-package interfaces.** Sales discharge flows to PKG-049 (Sales Gas Booster Compressor). Inlet feed includes 03-25 sour gas (DBM-Comp_and_Liquids SEC-05 export route). The Scope of Work integration narrative shall name both interfaces explicitly.
- **TBD propagation.** DBM-Deepcut SEC-05 carries several TBD/TBC items (J-T mode temperatures, second-stage discharge value at 1,500 vs 1,700 psig, design pressure drops, clearance pocket selection, recycle fail positions). These TBDs propagate forward to detailed engineering and shall not be silently resolved at Scope of Work stage.
- **Standards extraction depth.** Project standards beyond what is in DBM-Deepcut have not been extracted from 26020-Package_Requirements.docx in this run (file is .docx; no markdown conversion present). Detailed-engineering pass shall resolve standards list from that source.

## Trade-offs

- **Multi-service common-frame vs. split inlet/sales compressors.** The chosen multi-service arrangement reduces production loss per outage and improves flow stability, at the cost of greater package complexity and tighter integration between sour and sweet service domains within one frame (purge integrity, distance-piece sweep, shared cooler frame).
  Source: DBM-Deepcut SEC-05 Compression Configuration.
- **Starting VFD with synchronous transfer vs. DOL with soft-start.** DBM-Deepcut SEC-05 specifies the former; PACKAGE_REGISTER.csv Scope quotes "DOL driver with a soft-start." These imply different electrical-design and process start-up behavior. The Scope of Work shall record this as an open conflict — it cannot be silently reconciled because each option has different bus-impact and rate-of-loading consequences.
- **Sales-service suction scrubber inclusion.** Low inlet-gas dewpoint may make the sales-service scrubber unnecessary. DBM-Deepcut SEC-05 defers this to detailed engineering. Scope of Work shall preserve scrubber inclusion as the baseline pending detailed-engineering ruling.

## Examples

- *Worked example — production-loss exposure.* Five 5 x 20% packages mean a single-package trip removes approximately 60 MMSCFD inlet capacity and 57.6 MMSCFD sales capacity (about 20%). With no installed spare, this is the maintenance/outage planning baseline.
  Source: DBM-Deepcut SEC-05 Compression Configuration; design table.
- *Worked example — cooler outlet basis.* Summer 3rd-stage sales cooler outlet 43.3 deg C; winter 35.0 deg C. Both inform downstream sweet-gas dewpoint margin before the sales gas booster.
  Source: DBM-Deepcut SEC-05 cooler table.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-1 | Motor start method: Starting VFD with synchronous transfer vs DOL with soft-start | DBM-Deepcut SEC-05 "Inlet / Sales Compressor Basis" (Starting VFD) | PACKAGE_REGISTER.csv PKG-048 Scope (DOL driver with soft-start) | Spec R-5; Datasheet "Tagged Equipment / Package Identity"; Procedure step on commissioning electrical interface | PROPOSAL: DBM-Deepcut is later/derivative engineering basis — provisionally favor Starting VFD with synchronous transfer pending RFQ confirmation. | TBD |
| CT-2 | Sales-service second-stage discharge pressure: 1,500 psig vs 1,700 psig | DBM-Deepcut SEC-05 design-condition table (1,500 psig current supported basis) | DBM-Deepcut SEC-05 design-condition table (1,700 psig initial estimate for second-stage discharge — TBC) | Spec R-4; Datasheet Sales Service Conditions | PROPOSAL: 1,500 psig as current supported basis; treat 1,700 psig as superseded initial estimate. | TBD |
| CT-3 | Compressor frame: Ariel KBC/6 vs unresolved legacy frame reference | DBM-Deepcut SEC-05 (Ariel KBC/6, TBC) | DBM-Deepcut SEC-05 reference to unresolved legacy frame value | Spec R-5; Datasheet "Tagged Equipment / Package Identity" | PROPOSAL: Ariel KBC/6 preliminary; resolve legacy reference in detailed engineering. | TBD |
| CT-4 | Driver horsepower: 6,700 hp vs 7,000 hp legacy | DBM-Deepcut SEC-05 (6,700 hp current) | DBM-Deepcut SEC-05 (7,000 hp legacy) | Spec R-5; Datasheet "Tagged Equipment / Package Identity" | PROPOSAL: 6,700 hp current basis. | TBD |
| CT-5 | Per-package inlet capacity: 62.4 MMSCFD vs 60 MMSCFD | DBM-Deepcut SEC-05 (62.4 MMSCFD supported basis) | DBM-Deepcut SEC-05 (60 MMSCFD appears in detailed tables) | Spec R-3; Datasheet Inlet Service Conditions | PROPOSAL: 62.4 MMSCFD as supported basis; treat 60 MMSCFD as rounded/superseded. | TBD |
| CT-6 | Total inlet capacity: ~312 MMSCFD vs 300 MMSCFD TBC | DBM-Deepcut SEC-05 (current supported basis ~312 MMSCFD) | DBM-Deepcut SEC-05 (300 MMSCFD TBC in detailed table) | Spec R-3; Datasheet | PROPOSAL: ~312 MMSCFD current basis. | TBD |
| CT-7 | Recycle-valve fail positions: stated values vs TBD | DBM-Deepcut SEC-05 (inlet fail open, sales fail closed — both TBD) | None — single-source TBD flag | Spec R-9; Procedure verification steps | PROPOSAL: Carry stated values as baseline; mark TBD until ruling. | TBD |
