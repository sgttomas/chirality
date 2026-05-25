# Guidance — DEL-026-01 Scope of Work (PKG-026)

## Purpose

This Guidance explains the *why* and the interpretive frame for the EPC Integrator Scope of Work for PKG-026 Transformer TXP-8300-2. The Scope of Work is the Gate 5 EPC anchor deliverable: it tells downstream readers what the package is, why it exists in the facility, who owns which slice, and how the EPC Integrator will integrate the vendor-supplied transformer package into 03-25.

## Principles

1. **Vendor-owned engineering, EPC-owned integration.** The package boundary is set by `PACKAGE_REGISTER.csv` and is non-negotiable at the SoW level: design, fabrication, and vendor documentation belong to the Package Vendor; integration (interfaces, tie-ins, constructability, facility-level coordination) belongs to the EPC Integrator. (Source: PACKAGE_REGISTER.csv row PKG-026.)
2. **Source-anchored identity.** The package's identity (`TXP-8300-2`, 20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV) comes from Workbook row 28. Where the accessible DBM does not corroborate a detail (e.g., 6.9 kV and 0.4 kV services, 20/26 MVA rating), the Scope of Work documents the workbook fact and flags the verification gap rather than inventing supporting prose.
3. **Interface-centric integration narrative.** The seven applicable interface types named in PACKAGE_REGISTER.csv (Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports) provide the spine of the integration narrative.
4. **Do not pre-empt downstream deliverables.** The SoW frames; it does not duplicate. Datasheet detail belongs in DEL-026-02; construction execution detail belongs in DEL-026-03; vendor package engineering in DEL-026-04; vendor document control in DEL-026-05; review/acceptance evidence in DEL-026-06.
5. **Conservative on quantitative claims.** Where source slices do not give a value, the SoW marks `TBD` and lets the Package Datasheet (DEL-026-02) resolve it during EPC handoff to vendor.

## Considerations

- **Identity not directly corroborated in DBM.** The accessible 3-25 DBM (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) describes a 12 MVA 13.8/4.16 kV transformer at L744; it does not enumerate a 20/26 MVA 13.8/6.9/0.4 kV transformer. Treat the workbook row as authoritative for package identity per K-PROV-1 conventions but surface the gap as a verification item — the 03-25 DBM slice may simply be incomplete with respect to all transformers, or TXP-8300-2 may serve a different process load not detailed in the accessible DBM text.
- **Two-secondary configuration (6.9 kV and 0.4 kV).** The 6.9 kV and 0.4 kV (400 V) secondaries are named in the package title but not described in the accessible DBM. Treat both legs as `ASSUMPTION: per package title` and surface them as verification items to the Package Datasheet.
- **Dual rating (20/26 MVA).** Conventionally, dual MVA ratings denote ONAN/ONAF cooling stages. This is `ASSUMPTION` until vendor data confirms; do not write cooling-class statements as fact in the SoW.
- **Standby/emergency power.** Per DBM L505 and L762, the project's emergency-power basis has moved to LV standby generators on the 600 V MCC; the accessible DBM does not identify an MV emergency feed through TXP-8300-2. The SoW should note this so that downstream readers do not assume an emergency duty for the transformer.
- **Sub-feed from 04-25 (facility convention).** Facility incoming power for 03-25 is sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building (DBM L740). Whether TXP-8300-2 is fed directly from a 03-25 bus, a 04-25 feeder, or via an intermediate switchgear is not stated in the accessible source set; record as `TBD`.
- **Area classification.** General-facility classification is Class I, Zone 2, Gas Groups IIA/IIB (DBM L720–L726). Transformers sited in general-purpose areas may carry a different local classification — the SoW should reference the general policy and defer site-specific classification to detailed engineering.
- **0.4 kV (400 V) is unusual on a Canadian/North American 60 Hz site.** The package title shows a 0.4 kV secondary, which is an IEC-standard LV value rather than the 600 V / 480 V / 347 V values used elsewhere in the 03-25 DBM (L734). This may indicate a packaged-vendor convention or an IEC-spec piece of process equipment. Flag this for detailed engineering and the Package Datasheet; do not assume a 600 V or 480 V substitution.

## Trade-offs

- **Specifying vs. deferring.** The EPC SoW could pre-specify transformer parameters (impedance, BIL, vector group, taps). Recommendation: defer to the Package Datasheet (DEL-026-02) so that the SoW remains a stable EPC anchor and vendor pre-bid issues are concentrated in one technical handoff document.
- **Tag-level enumeration vs. package-level abstraction.** Enumerating every package-bundled auxiliary (cooler fans, OLTC controls, monitoring devices) duplicates vendor scope. Recommendation: list the principal tag (`TXP-8300-2`) and reference the vendor package as the source of the complete tag list.

## Examples (drawn from source)

- Package-identity statement (workbook-grounded): "TXP-8300-2 is the 20/26 MVA step-down distribution transformer named in Workbook Packages row 28, stepping 13.8 kV to 6.9 kV and 0.4 kV services for the 03-25 facility." (Source: Workbook row 28 via PACKAGE_REGISTER.csv.)
- Boundary statement (register-grounded): "Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration." (Source: PACKAGE_REGISTER.csv `Vendor_EPC_Boundary` for PKG-026.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-026-01-01 | Workbook row 28 names a 20/26 MVA 13.8/6.9/0.4 kV transformer; the accessible 3-25 DBM describes only a 12 MVA 13.8/4.16 kV transformer (L744) and 600 V LV service (L734). No 6.9 kV or 0.4 kV service is enumerated in the accessible DBM slices. | Workbook Packages row 28 | DBM L728–L750 | Datasheet (attributes, secondary voltage), Specification REQ-026-01-02 / REQ-026-01-12, Guidance principles 2 and considerations | Carry workbook row 28 as authoritative for package identity; flag the DBM mismatch for resolution in DEL-026-02 (Package Datasheet) and detailed engineering. | TBD |
| CFL-026-01-02 | Package title states "20/26 MVA". Accessible DBM does not corroborate dual-rating cooling basis for this unit. | Workbook row 28 | DBM (silent on this unit) | Datasheet (rating, cooling), Specification REQ-026-01-02 | Treat 20/26 MVA as ONAN/ONAF dual rating consistent with industry convention; confirm cooling class with vendor in DEL-026-02. | TBD |
| CFL-026-01-03 | Package-spec number `26020-02-30-017` listed in PACKAGE_REGISTER.csv but underlying spec text not in accessible source set. | PACKAGE_REGISTER.csv | (absent in `_Sources` accessible text; `26020-Package_Requirements.docx` present as binary, not read) | Specification §3 | Cite by number; mark clause-level requirements `location TBD`; convert the binary `26020-Package_Requirements.docx` if needed by a separate extraction task. | TBD |
| CFL-026-01-04 | 0.4 kV (400 V) secondary in package title is an IEC voltage value not otherwise used in the 03-25 DBM, which standardizes on 600 V / 347 V LV (DBM L734). | Workbook row 28 | DBM L734 | Datasheet (secondary voltage), Specification REQ-026-01-02, Guidance considerations | Preserve 0.4 kV verbatim from workbook; do not substitute 600 V or 480 V. Flag for detailed engineering and the Package Datasheet. | TBD |

## NEEDS_HUMAN_RULING

- HRR-026-01-001: Reconcile the Workbook row 28 identity (20/26 MVA, 13.8/6.9/0.4 kV) against the 3-25 DBM (12 MVA, 13.8/4.16 kV at L744) — either the DBM is incomplete with respect to TXP-8300-2 or the workbook row carries an updated facility design. Proposed handling: treat workbook row 28 as authoritative for identity; resolve in DEL-026-02.
- HRR-026-01-002: Determine whether TXP-8300-2's 0.4 kV secondary is an IEC-spec packaged-equipment power feed or a typographical / unit-conversion artifact in the workbook. Proposed handling: preserve verbatim; flag for detailed engineering.
