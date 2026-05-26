# Guidance: DEL-090-03 — Construction Work Package (Vapour Recovery Unit 3-25)

## Purpose

This document gives the EPC Integrator construction team the rationale behind the requirements in `Specification.md` and the directional considerations needed to plan and execute the VRU 3-25 installation safely, in the right sequence, and consistent with the accepted upstream basis (Gate 7 PROJECT_DECOMP snapshot, the 26020 package requirements section for the VRU, and the 3-25 Compressors and Liquids DBM).

The VRU is a small but safety- and emissions-critical sub-system on the 03-25 site: it sweeps tank vapours and selected process vents into a compressed stream that is routed off-site to the 04-25 SOC suction (under SCA-002). Construction quality and sequencing directly affect leak-tightness, flare/relief integrity, and the ability to start up the rest of the liquids hub vapour-handling network.

## Principles

1. Honour the vendor / EPC split. `PACKAGE_REGISTER.csv` PKG-090 makes the split explicit: vendor owns package engineering, design, vendor docs, and physical equipment package. EPC owns integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Construction work outside that split is out of scope, and vendor work shall not be silently absorbed.
2. Construct to the source slice, not to convention. Where the 26020 package requirements and the 3-25 DBM are explicit (lead-lag two trains, 200 HP VFD per train, Plan-53 seal buffer to LP flare, discharge to 04-25 SOC suction), construct exactly to those. Inferred or "industry-standard" detail must be labelled ASSUMPTION until vendor or standard text is on file.
3. Respect SCA reconciliations. The current basis explicitly removes a local 03-25 SOC and routes VRU discharge to 04-25 SOC suction (SCA-002). The CWP must not reintroduce a local SOC tie-in. Likewise, local instrument air, local condensate stabilization, and local heat-medium have been removed (SCA-006 etc.); construction shall not install foundations, supports, or tie-ins for those superseded systems.
4. Treat "by others" items as your scope. The vendor `26020-01-PT-12-002` package scope note lists shipping, installation on piles, tie-in piping, electrical, and instrumentation as "by others." Those items are EPC scope under PKG-090. Plan accordingly in the workface plan.
5. Tie-in checklist must be 1:1 with the `Yes` interfaces. Every `Yes` row in the PT-12-002 Physical Interface Summary should have a corresponding line in the construction interface and turnover checklist, traceable to its acceptance test.
6. Sour service first. The package operates at 0.3557 mol% H2S, 0.9434 mol% CO2, with NACE designation. Tie-in piping selection, weld/NDE practice, and material handling/QA must reflect sour service from day one.
7. Flare integrity is non-negotiable. The VRU is tied into the LP flare network for seal vent and for the LP flare bypass V-ball valve on the suction header. The suction header must free-drain to the flare KO interface; sag-pockets or back-grade are construction defects, not snag-list items.

## Considerations

- Constructability windows. Two trains in one building with shared utilities mean piping and electrical/I&C runs are dense. Sequence so that the building shell, EHT, lighting, fire and gas, and structural supports are sufficiently in place before high-density piping and cable tray installation, but not so early that vendor equipment cannot be set on its foundations.
- Lift planning. Specific lift weights and module split dimensions are not in the local source set (vendor MEC-018 is listed as a deliverable but not present here). Treat lift planning as TBD pending receipt of MEC-018; do not freeze the lift plan against assumed weights.
- Foundation interfaces. Anchor-bolt patterns, embedments, and grouting requirements come from vendor STR-005/006/013. Pour foundations only after these are received and reconciled with the civil scope already executed at 03-25.
- Shared utilities with 04-25. Fuel gas, instrument air, and electrical power are shared cross-facility utilities; instrument air specifically comes from 04-25 (SCA-006). The VRU tie-ins on those utilities depend on the 04-25 side being available — coordinate with the corresponding 04-25 packages in the EPC schedule.
- Flare KO interface. The exact service split and ownership at the HP/Cryo + LP dual flare stack and incinerator are flagged in the DBM as "open interface items where source language is not fully resolved" (DBM SEC-04). Treat the VRU's LP flare and KO connections as interface-controlled until the open items are closed.
- Recycle valve failure action. DBM SEC-05 notes that compressor recycle valves are expected to fail open but final failure action remains TBC. Construction shall install per vendor data sheet; if the valve action is not yet locked, plan for possible field rework.
- Pressure equipment registration. Provincial registration (REG-022) is a sequencing constraint — without an accepted registration package, the unit cannot be pressurized for commissioning. Bring vendor REG-022 into the construction window early.
- ASSUMPTION (best-effort objective mapping). `_CONTEXT.md` lists OBJ-002 through OBJ-010 as supported objectives using the PACKAGE_HEURISTIC association mode. These should be confirmed by the human owner; do not treat individual OBJ codes as testable construction requirements.

## Trade-offs

- Foundation cure vs. schedule. Holding the schedule for a longer foundation cure protects long-term integrity; compressing the cure to chase the install date risks anchor-pull-out and re-alignment work. The CWP should default to the conservative side and flag deviations.
- Pre-fab tie-in spools vs. field weld. Pre-fabricating tie-in spools reduces sour-service field welding (good for QA and NDE), but increases the dependency on accurate vendor as-built dimensions. Choice should follow vendor PIP-008/PIP-009 isometric maturity.
- Single-building HVAC. The PT-12-002 row marks Building HVAC/Services as "No" interface; `PACKAGE_REGISTER.csv` PKG-090 lists HVAC as applicable. Until ruled, conservatively plan as if HVAC ventilation interfaces are required (sour-gas building, classified area), and budget for connection scope. See Conflict Table.
- Compressor model mismatch. The package requirements section refers to Ro-Flo 17S/217M; `PACKAGE_REGISTER.csv` says Ro-Flo 12S/212M. Foundation, lift, and electrical loads can differ between frame sizes; the CWP must not commit to one frame until the discrepancy is ruled. See Conflict Table.

## Examples (from source)

- Two 200 HP electric-drive VRU compressor packages, 2 x 100 percent, routed to 04-25 SOC suction under SCA-002. (DBM SEC-06 "Vapour Recovery")
- VRU suction header includes an LP flare bypass V-ball valve operated by VRU suction pressure; header shall free-drain or slope toward the flare KO interface as defined by detailed design. (DBM SEC-06)
- Vendor scope note: "By others: Shipping compressor packages to site, installation on piles, tie-in piping, electrical, instrumentation." (`26020-01-PT-12-002` scope-notes table)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFLT-090-03-001 | Compressor frame size: 17S/217M vs 12S/212M | `_Sources/26020-Package_Requirements.docx` `26020-01-PT-12-002 / Basic Scope` (Ro-Flo 17S/217M) | `_Decomposition/.../PACKAGE_REGISTER.csv` row PKG-090 Description (Ro-Flo 12S/212M) | Datasheet Attributes; Specification R-CWP-090-001/002; lift, foundation, and electrical sizing | Treat the 26020 package requirements document as authority for vendor-driven physical attributes; the package register entry is descriptive and may be a transcription drift. PROPOSAL: adopt 17S/217M pending confirmation from the issued vendor RFQ (`Bid Docs/_Budgetary/26020-01-PT-RFQ-12-002_VRU_2_R0.docx` per package source-basis table). | TBD |
| CFLT-090-03-002 | Building HVAC/Services interface applicability | `_Sources/26020-Package_Requirements.docx` `26020-01-PT-12-002 / Physical Interface Summary` (Building HVAC/Services = No) | `_Decomposition/.../PACKAGE_REGISTER.csv` row PKG-090 "Applicable interface types" (includes Building HVAC / Services) | Datasheet Interface table; Specification R-CWP-090-009 | The VRU sits in a classified sour-gas building; ventilation is typically required. PROPOSAL: treat HVAC as applicable until the package requirements row is confirmed correct; carry HVAC interface scope conservatively. | TBD |
| CFLT-090-03-003 | Vendor RFQ source basis: PT-RFQ-12-002 (Word) vs PT-RFQ-12-001 (register) | `26020-01-PT-12-002` Source Basis table (`26020-01-PT-RFQ-12-002_VRU_2_R0.docx`) | `_Decomposition/.../PACKAGE_REGISTER.csv` row PKG-090 (`26020-03-PT-RFQ-12-001_VRU_1_R0.docx`) | Datasheet References; Specification standards/verification provenance | The two RFQ codes may refer to two VRU trains (lead vs lag) or to a numbering drift across SCA cycles. PROPOSAL: obtain both RFQ docs and confirm whether 3-25 VRU is sourced from PT-RFQ-12-001 or PT-RFQ-12-002. | TBD |
