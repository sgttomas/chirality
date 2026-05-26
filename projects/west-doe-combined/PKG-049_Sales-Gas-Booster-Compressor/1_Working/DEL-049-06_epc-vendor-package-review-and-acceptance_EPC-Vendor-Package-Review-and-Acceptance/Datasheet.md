# Datasheet — DEL-049-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-049-06_epc-vendor-package-review-and-acceptance |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | PKG-049 |
| PackageName | Sales Gas Booster Compressor |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| CoversScopeItems | SOW-0169; SOW-0170; SOW-0171; SOW-0172 |
| SupportsObjectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC association) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Review subject | Vendor-supplied Sales Gas Booster Compressor package (motor-driven separable reciprocating gas compressor + filter coalescer) | SOW-0170 (SCOPE_LEDGER) |
| Major equipment in review scope | Ariel KBX/X reciprocating compressor; 8-pole induction motor 4000V/3PH/60Hz, 891 RPM; per-stage air cooler (API 661); per-stage suction scrubber; packing vent/drain pot; seal-pot waste oil transfer pump; 0.3 micron @ 99.97% filter coalescer (100 MMSCFD) | SOW-0171 (SCOPE_LEDGER) |
| Process function | Compress sweet sales gas from sales gas booster header to sales gas coalescer and on to sales gas splitter | SOW-0170 |
| Design throughput | 140 MMSCFD (3962 e3m3/day); no turndown | SOW-0172 |
| Driver | Electric induction motor, 8-pole, 1000 kW (1340 HP), 4000V/3PH/60Hz @ 891 rpm fixed speed; TEFC or WPII; NEMA MG 1 | SOW-0172 |
| Suction design pressure | 6137 kPag (890 psig) | SOW-0172 |
| Discharge design pressure | 12866 kPag (1866 psig) | SOW-0172 |
| Inlet operating temperature | 110 F (43.3 C) summer | SOW-0172 |
| Inlet liquid density assumption | 0.61 SG (suction scrubber design basis) | SOW-0172 |
| EPC by-others scope (review boundary) | Shipping to site; pile installation; tie-in piping; electrical connections; mounting platform and stairs | SOW-0172 |
| Ownership split | Package Vendor owns engineering/design/equipment; EPC Integrator owns facility integration | SOW-0169 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sweet sales gas | SOW-0170 |
| Operating mode | Fixed-speed (no turndown) | SOW-0172 |
| Soft start | DOL driver with soft-start | SOW-0171 |
| Cooling | Forced air intercooler after each cylinder, horizontal air-flow, single fan, automated louvers | SOW-0171 |

## Construction

| Item | Value | Source |
|---|---|---|
| Compressor frame | Ariel KBX/X reciprocating, all cylinders dedicated | SOW-0171 |
| Air cooler standard | API 661 | SOW-0171 |
| Scrubbers | Two-phase, vertical-flow mesh/vane (per cylinder stage); vendor-designed size/capacity | SOW-0171 |
| Packing vent/drain pot | Two-phase, DP 101 kPag; vendor-designed | SOW-0171 |
| Filter coalescer | 0.3 micron @ 99.97%, bandlock-type QOC, 100 MMSCFD design flow | SOW-0171 |
| Motor enclosure | TEFC or WPII, non-sparking bidirectional cooling fan | SOW-0172 |

## References

- Gate 7 PROJECT_DECOMP snapshot SCOPE_LEDGER.csv rows SOW-0169..SOW-0172 (locally accessible)
- Gate 7 PROJECT_DECOMP DELIVERABLE_REGISTER.csv (DEL-049-06 row)
- Gate 7 PROJECT_DECOMP ARTIFACT_REGISTER.csv (ART-A1F5908C64; ART-6439AA1852; ART-F7E6330088)
- Workbook Packages row 80 (binary; not directly read in this run — TBD location for clause-level slices)
- 26020-Package_Requirements.docx package heading 4 (binary; not directly read in this run — TBD location for clause-level slices)
