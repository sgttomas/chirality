# Guidance — DEL-015-01 Scope of Work (PKG-015)

## Purpose

This Guidance explains the *why* and the interpretive frame for the EPC Integrator Scope of Work for PKG-015 Transformer TXP-8300-1. The Scope of Work is the Gate 5 EPC anchor deliverable: it tells downstream readers what the package is, why it exists in the facility, who owns which slice, and how the EPC Integrator will integrate the vendor-supplied transformer package into 03-25.

## Principles

1. **Vendor-owned engineering, EPC-owned integration.** The package boundary is set by `PACKAGE_REGISTER.csv` and is non-negotiable at the SoW level: design, fabrication, and vendor documentation belong to the Package Vendor; integration (interfaces, tie-ins, constructability, facility-level coordination) belongs to the EPC Integrator. (Source: PACKAGE_REGISTER.csv row PKG-015.)
2. **Source-anchored identity.** The package's identity (`TXP-8300-1`, 12/15 MVA, 13.8 kV / 4,160 / 2,400 V) comes from Workbook row 17. Where the accessible DBM does not corroborate a detail (e.g., 2,400 V service), the Scope of Work documents the workbook fact and flags the verification gap rather than inventing supporting prose.
3. **Interface-centric integration narrative.** The seven applicable interface types named in PACKAGE_REGISTER.csv (Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports) provide the spine of the integration narrative.
4. **Do not pre-empt downstream deliverables.** The SoW frames; it does not duplicate. Datasheet detail belongs in DEL-015-02; construction execution detail belongs in DEL-015-03; vendor document control belongs in DEL-015-05; review/acceptance evidence belongs in DEL-015-06.
5. **Conservative on quantitative claims.** Where source slices do not give a value, the SoW marks `TBD` and lets the Package Datasheet (DEL-015-02) resolve it during EPC handoff to vendor.

## Considerations

- **Two-secondary configuration (4,160 V and 2,400 V).** The DBM at 3-25 documents 4,160 V service and a 12 MVA 13.8/4.16 kV transformer (DBM L744). The 2,400 V secondary is named in the package title but not directly described in the accessible DBM slice. Treat the 2,400 V leg as an `ASSUMPTION: per package title` and surface it as a verification item to the Package Datasheet.
- **Dual rating (12/15 MVA).** Conventionally, dual MVA ratings denote ONAN/ONAF cooling stages. This is `ASSUMPTION` until vendor data confirms; do not write cooling-class statements as fact in the SoW.
- **Standby/emergency power.** Per DBM L505 and L762, the project's emergency-power basis has moved to LV standby generators on the 600 V MCC; there is no MV emergency feed planned through TXP-8300-1. The SoW should note this so that downstream readers do not assume an emergency duty for the transformer.
- **Sub-feed from 04-25.** TXP-8300-1 is fed from the 04-25 13.8 kV Main Switchgear Electrical Building (DBM L740). The cross-facility electrical interface to 04-25 is a first-class integration item.
- **Area classification.** General-facility classification is Class I, Zone 2, Gas Groups IIA/IIB (DBM L722). Transformers sited in general-purpose areas may carry a different local classification — the SoW should reference the general policy and defer site-specific classification to detailed engineering.

## Trade-offs

- **Specifying vs. deferring.** The EPC SoW could pre-specify transformer parameters (impedance, BIL, vector group, taps). Recommendation: defer to the Package Datasheet (DEL-015-02) so that the SoW remains a stable EPC anchor and vendor pre-bid issues are concentrated in one technical handoff document.
- **Tag-level enumeration vs. package-level abstraction.** Enumerating every package-bundled auxiliary (cooler fans, OLTC controls, monitoring devices) duplicates vendor scope. Recommendation: list the principal tag (`TXP-8300-1`) and reference the vendor package as the source of the complete tag list.

## Examples (drawn from source)

- Package function statement (source-grounded): "TXP-8300-1 is the 12 MVA step-down distribution transformer described in the 03-25 DBM (L744) that feeds the 4,160 V MCC serving 4,000 V class process motors (e.g., KM-2150, KM-2250)." (Source: DBM L744, L754.)
- Upstream source statement (source-grounded): "Power to TXP-8300-1 is sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building." (Source: DBM L740.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-015-01-01 | Package title states secondary voltages "4160/2400 V". Accessible DBM (3-25 L738–L750) describes only the 4.16 kV secondary; no 2,400 V service appears in the accessible DBM slices. | Workbook row 17 (package title) | DBM L738–L750 | Datasheet (secondary voltages), Specification REQ-015-01-02, Guidance principle 2 | Carry both secondaries per workbook title; flag 2,400 V as `verify-against-detailed-electrical` until single-line diagrams or vendor data confirm. | TBD |
| CFL-015-01-02 | Package title states "12/15 MVA". Accessible DBM names "12 MVA transformer" only (L744). | Workbook row 17 | DBM L744 | Datasheet (rating), Specification REQ-015-01-02 | Treat 12/15 MVA as ONAN/ONAF dual rating consistent with DBM 12 MVA self-cooled basis; confirm cooling class with vendor. | TBD |
| CFL-015-01-03 | Package-spec number `26020-02-30-006` listed in PACKAGE_REGISTER.csv but underlying spec text not in accessible source set. | PACKAGE_REGISTER.csv | (absent in `_Sources`) | Specification §3 | Cite by number; mark clause-level requirements `location TBD`. | TBD |
