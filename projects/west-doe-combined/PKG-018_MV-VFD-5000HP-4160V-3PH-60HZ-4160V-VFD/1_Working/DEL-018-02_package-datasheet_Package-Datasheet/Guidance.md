# Guidance: DEL-018-02_package-datasheet

## Purpose

This deliverable provides the EPC Integrator's technical handoff basis for the medium-voltage VFD package (`PKG-018`) so a third-party Package Vendor can perform package engineering and design under `DEL-018-04`, and so downstream construction (`DEL-018-03`) and acceptance (`DEL-018-06`) deliverables can integrate the package into the facility. It carries the workbook identity, source-supported drive/motor/MCC basis, and the six interface facts as evidence rather than as separate deliverables. (Source: `DELIVERABLE_REGISTER.csv` row `DEL-018-02_package-datasheet`; `_CONTEXT.md`.)

## Principles

- **Workbook identity governs nameplate class.** Workbook row 20 sets the package title and rating class; downstream documents must use this identity. Where source drive basis differs in detail (e.g., 4,000 V / 5,200 hp inlet compressor motor vs. workbook "5000HP, 4160V"), surface the discrepancy rather than silently reconcile.
- **Source-grounded drive basis.** The drive mode (Starting VFD with synchronous transfer), the capacitor-bank prohibition, and the Ethernet/PLC data-acquisition interface are stated by accessible source (Comp_and_Liquids DBM and Deepcut DBM). These are authoritative and carry through as requirements.
- **EPC owns integration, Vendor owns package.** Per `PACKAGE_REGISTER.csv` row `PKG-018`, package engineering and physical equipment are Package Vendor scope; integration, interfaces, constructability, and facility-level integration are EPC scope.
- **Interface facts as evidence, not deliverables.** All six interface rows for `PKG-018` are carried here as datasheet evidence (`ARTIFACT_REGISTER.csv` rows `ART-1BC92A41D7`, `ART-FD4CA08C81`, `ART-A29D7CC3B8`, `ART-30065EEFDA`, `ART-665A429160`, `ART-1471235A54`).
- **Conservative TBD discipline.** Where vendor-internal design (cooling, harmonic-filter topology, isolation/bypass scheme, semiconductor selection) or unconfirmed facility data (PKG-018 location, exact driven-load tag) is absent from accessible source, prefer `TBD` over invention.

## Considerations

- **Driven load is not named in workbook row 20.** The 5,000 HP / 4,160 V / 3-phase / 60 Hz package class is consistent with starting/driving an MV inlet/sales compressor motor (KM-2150 / KM-2250), but source does not explicitly assign PKG-018 to these tags. Treat the linkage as ASSUMPTION and confirm during vendor handoff.
- **Voltage and HP precision.** Comp_and_Liquids DBM (line 324) states the inlet compressor motor basis as 4,000 V / 5,200 hp. Workbook row 20 names "4160V" and "5000HP." Whether the package title reflects the MV bus / MCC class (4.16 kV) and a rounded HP, or whether the package is genuinely a 4,160 V / 5,000 HP product distinct from the cited motor basis, is not resolved by accessible source.
- **4.16 kV MCC VFD requirements are TBD per Deepcut DBM** (line 3088). The package must satisfy any forthcoming detailed-design output of that determination.
- **Capacitor-bank prohibition (SCA-001 VE #37)** affects facility single-line design near MCC-8200; relevant for both EPC and Vendor planning.
- **Hazardous-area marking.** Any VFD-fed motor in a Zone 2 area inherits the temperature-code marking constraint; verify against area-classification and fugitive-emissions drawings.
- **Electrical-buildings assumption.** DBM allows medium-voltage VFDs to be housed in prefabricated modular electrical buildings; PKG-018 location is not assigned. Vendor packaging (skid vs. building-resident) should align with EPC layout.

## Trade-offs

- **Conservative datasheet vs. complete datasheet.** This deliverable favors source-grounded conservatism. Adding inferred values (output filters, dV/dt limits, ride-through duration, redundancy of cells) without source backing would risk overspecifying the vendor package; leaving them `TBD` preserves vendor design freedom and Surface the gaps for human ruling.
- **Identity-vs-source precedence.** Workbook identity is the contractual nameplate, but source-stated motor/MCC basis is the engineering reality. Forcing one over the other before human ruling would either contradict the workbook or contradict the DBM. Both are surfaced; the Conflict Table records the dispute.
- **Interface-fact evidence vs. separate interface deliverables.** Carrying the six interface facts here keeps the package envelope compact and avoids deliverable proliferation, at the cost of a denser datasheet.

## Examples

- The "Starting VFD with synchronous transfer" pattern (Deepcut DBM line 893) is the canonical drive-mode example to apply for the KM-2150/2250 use case.
- The Ethernet/PLC data-acquisition interface pattern from the 4.16 kV MCC (Comp_and_Liquids DBM line 754) is the canonical I&C/Communications interface example for this package.
- The "no capacitor banks on the synchronous-transfer bus where VFDs are present" rule (SCA-001 VE #37; Comp_and_Liquids DBM line 756) is the canonical facility-side constraint example tied to this package's presence.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-018-02-01 | Package title says "5000HP, 4160V" / "4160V VFD" but accessible source motor basis is 4,000 V / 5,200 hp inlet compressor motor on a 4.16 kV MCC. | Workbook Packages row 20 (`PACKAGE_REGISTER.csv` row `PKG-018`) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 324; line 752 (4160V MCC for 4000V motors) | Datasheet Attributes; Specification REQ-018-02-02; Guidance Considerations | PROPOSAL: Treat workbook identity (5000HP / 4160V) as the contractual package nameplate class; treat the 4,000 V / 5,200 hp value as the served motor's nameplate. Reconcile output-voltage class (4,000 V vs. 4,160 V) and HP basis during vendor handoff. | TBD |
| CT-018-02-02 | PKG-018 driven-load assignment is not stated. The Starting VFD basis is explicitly cited for KM-2150 / KM-2250, but the workbook row does not name a driven tag. | Workbook Packages row 20 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 326, 752-756; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 893 | Datasheet Attributes (Driven load); Specification REQ-018-02-03; Procedure Prerequisites | PROPOSAL: Provisionally associate PKG-018 with KM-2150 / KM-2250 starting service pending confirmation; do not commit factory-test acceptance until the load assignment is confirmed by the EPC Integrator. | TBD |
| CT-018-02-03 | Deepcut DBM states 4.16 kV motor VFD and soft-starter requirements are TBD; this leaves the precise specification framework for PKG-018 undecided. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2957, 3088 | (none — open item) | Specification Standards; Specification Requirements | PROPOSAL: Carry through current requirements and revisit upon issuance of the detailed-design output that closes the TBD. | TBD |

