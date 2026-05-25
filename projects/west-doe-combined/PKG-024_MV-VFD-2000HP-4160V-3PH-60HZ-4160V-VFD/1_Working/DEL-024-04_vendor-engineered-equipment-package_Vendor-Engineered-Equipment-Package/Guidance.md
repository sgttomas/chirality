# Guidance: DEL-024-04_vendor-engineered-equipment-package

## Purpose

This guidance frames how the **Vendor Engineered Equipment Package** for `PKG-024` (MV VFD - 2000HP, 4160V, 3PH, 60HZ) should be interpreted and developed by the Package Vendor and reviewed by the EPC Integrator. The deliverable is a Gate 5 Vendor Package Production Unit, anchored downstream of the EPC Scope of Work (`DEL-024-01`) and EPC Package Datasheet (`DEL-024-02`). Per `_CONTEXT.md`, it covers engineering, design, fabrication / supply, and the physical equipment package.

## Principles

- **Vendor authority over package design.** The Package Vendor is the design authority for the MV VFD package. The EPC Integrator does not redesign the package; it sets the technical handoff envelope (Scope of Work, Package Datasheet) and reviews integration.
- **Source-grounded technical claims only.** The accessible facility design basis (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) explicitly leaves "VFD and soft-starter requirements for 4.16 kV motors" as TBD. Any clause-level requirement asserted by the Package Vendor must trace to either the EPC Package Datasheet, a project-specific package requirements slice, or a vendor design choice flagged as a vendor-originated proposal.
- **Interface facts are the integration contract.** The six declared `PKG-024` interfaces (`IFC-68C5E24846`, `IFC-F8A6E25E1C`, `IFC-8062D6F881`, `IFC-22E88310C9`, `IFC-DD889EF8E3`, `IFC-850A8082BB`) are the contractually surfaced integration surfaces. Anything outside these interfaces is not assumed to be in scope unless added to `DEL-024-02`.
- **Package vs. facility scope discipline.** Facility-level decisions (electrical building layout, ground grid, plant PLC architecture, area classification drawings) are EPC scope and inputs to the vendor, not outputs of the vendor.

## Considerations

- **2,000 HP at 4,160 V is squarely within the "larger motors on this facility shall be 4,000 V or 13.2 kV" envelope** (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`). The package rating is internally consistent with the facility motor voltage policy.
- **Driven motor identity not asserted.** The decomposition records a 2,000 HP MV VFD without naming a specific driven motor tag or process service. The vendor cannot size load-dependent VFD characteristics (overload duty, harmonic interaction with downstream motor, output filter) without that information. Treat driven-load type as a required input from the EPC Package Datasheet.
- **Housing decision is upstream.** The DBM allows MV VFDs to be housed in prefabricated electrical buildings, but does not commit `PKG-024` to a building, room, skid, or outdoor location. The vendor's mechanical / cooling design depends on this decision.
- **Plant PLC and protective relay integration.** The facility 4.16 kV MCC convention is mechanically latched fused contactors with motor protection relays plus an Ethernet port to the plant PLC. The MV VFD package will likely need to expose a compatible interface; the EPC Package Datasheet must confirm this.

## Trade-offs

- **Topology choice (multilevel cascaded H-bridge vs. NPC three-level vs. transformerless)** drives harmonic performance, footprint, cooling, and cost. Source materials do not specify; vendor proposal needed.
- **Integrated input transformer vs. separate matching transformer** affects building / skid layout and the boundary with EPC-supplied feeders.
- **Sine-wave output filter** can extend motor cable length tolerance and reduce dV/dt stress at the motor, at cost and footprint expense. Necessity depends on driven motor and cable run, both currently TBD.
- **Bypass / second-source arrangement** trades availability against cost; not asserted by source. The DBM notes "Starting VFDs" are used on certain sales-gas compressor motors with synchronous transfer; whether `PKG-024` is a starting-only or continuous-duty drive is not asserted.

## Examples

No package-specific example or analog from accessible source materials. Sibling Vendor Engineered Equipment Package deliverables for other MV VFD packages (`DEL-017-04`, `DEL-018-04`, `DEL-019-04`, `DEL-023-04`) share the same boilerplate text and the same `Vendor engineered physical equipment package; vendor package design basis and datasheet set` artifact list, indicating a deliberately shared deliverable shape across MV VFD packages. They do not provide additional source-grounded technical content.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-024-04-001 | Driven motor tag, service, and load type for the 2,000 HP MV VFD are not identified by source. The vendor cannot finalize overload duty, cable / filter sizing, or harmonic study without it. | Workbook Packages row 26 (only states "MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD") | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (no PKG-024 motor tag assertion) | Datasheet/Attributes; Specification REQ-3, REQ-4; Procedure prerequisites | Treat driven-motor identification as a required input from `DEL-024-02` (EPC Package Datasheet) before vendor engineering proceeds. | TBD |
| HRR-024-04-002 | Drive topology, output filter, harmonic mitigation, and bypass arrangement are TBD by source ("VFD and soft-starter requirements for 4.16 kV motors are TBD"). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2957, 3088 | `_Sources/26020-Package_Requirements.docx` (no accessible PKG-024 slice) | Specification REQ-4; Datasheet/Attributes | Defer to vendor proposal grounded in driven-load characteristics once HRR-024-04-001 is resolved; EPC Integrator reviews against IEEE 519 facility limits if confirmed in `DEL-024-02`. | TBD |
| HRR-024-04-003 | Housing decision (prefabricated electrical building vs. outdoor / skid-mounted) is not asserted for `PKG-024`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph | `_CONTEXT.md` (silent on installation location) | Datasheet/Construction; Specification REQ-10 | EPC Integrator to assert housing decision in `DEL-024-02` before vendor mechanical / cooling design proceeds. | TBD |
| HRR-024-04-004 | Applicability of "Low-voltage power cable fed from VFDs shall be Copper TECK cable" to the 4,160 V output side of `PKG-024` is not clear. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 3013 | (no contrary slice) | Specification REQ-7; Procedure verification | Treat the rule as applicable only to LV power cabling fed from VFDs; MV output cabling rules to be confirmed against `_Sources/26020-Package_Requirements.docx` once accessible. | TBD |
| HRR-024-04-005 | The package-specific match in `_Sources/26020-Package_Requirements.docx` for `PKG-024` has not been extracted to accessible markdown. Clause-level package requirements may exist that this draft does not reflect. | `_REFERENCES.md` (DOCX listed at shared source root) | This deliverable's draft (no extracted slice cited) | All four documents | Extract the PKG-024 package-specific slice (or confirm no match) before Pass 2/3 acceptance. | TBD |
