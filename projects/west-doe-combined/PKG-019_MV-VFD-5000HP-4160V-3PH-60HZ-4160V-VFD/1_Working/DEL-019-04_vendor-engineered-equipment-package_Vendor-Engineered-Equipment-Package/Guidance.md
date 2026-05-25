# Guidance — DEL-019-04 Vendor Engineered Equipment Package

Directional guidance for drafting, reviewing, and accepting the Package Vendor's engineered MV VFD equipment package under PKG-019.

## Purpose

This deliverable carries the Package Vendor's engineering, design, and physical equipment scope for the MV VFD package. It exists as a distinct production unit (separate from EPC-Integrator anchor deliverables `DEL-019-01` and `DEL-019-02`) to make vendor ownership and the boundary between vendor scope and EPC integration explicit (Gate 7 `PACKAGE_REGISTER.csv` `PKG-019` ResponsibilityNarrative).

## Principles

- **Vendor produces, EPC integrates.** The Package Vendor owns the package engineering, design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance review (`PKG-019` ResponsibilityNarrative).
- **Authority chain for content.** EPC Scope of Work (`DEL-019-01`) and Package Datasheet (`DEL-019-02`) are upstream inputs; the DBM (`3-25_Comp_and_Liquids_DBM.md`) is the design-basis source for the application (starting VFDs for KM-2150 / KM-2250); workbook row 21 is the registration basis.
- **Starting-VFD basis is non-negotiable.** SCA-001 VE #34 requires starting VFDs for `KM-2150` and `KM-2250`; soft-start substitution is not in the current basis (DBM §326, §756).
- **Detailed sizing is a downstream electrical exercise.** DBM §326 explicitly defers VFD sizing to detailed electrical design; vendor design proposals must show sizing substantiation against accepted motor and load data.

## Considerations

- **Title vs. source rating mismatch.** The workbook package title states 5000 HP / 4160 V; the DBM motor basis states 5,200 HP / 4,000 V driven motors fed from a 4160V MCC. Treat the workbook title as identity only; treat the DBM as the design basis until human ruling resolves the discrepancy (see Conflict Table).
- **Line-side topology.** The 4160V MCC is the upstream supply for the 4000V motors, with EtherNet to the plant PLC central control panel (DBM §752, §754). The vendor package must accept this as the line-side interface and communications path.
- **Harmonic and reactive-power treatment.** DBM §756 defers mitigation to detailed electrical studies and removes capacitor banks from the synchronous bus on `MCC-8200` where VFDs are present (SCA-001 VE #37). Vendor design must accept mitigation requirements as inputs rather than originate them unilaterally.
- **Interface coverage.** The PKG-019 InterfaceTypes list (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) frames the package-level interface scope; the vendor package must provide engineering provisions for each.

## Trade-offs

- **Vendor-standard product vs. custom-engineered package.** Vendor-standard products reduce cost and lead time but may not match exact motor basis or facility interface requirements; custom engineering increases substantiation effort but reduces interface risk. The decision depends on the resolved motor rating (Conflict Table).
- **Cabinet / topology selection (e.g., cell-based vs. transformerless MV drive).** Affects footprint, harmonic profile, maintenance access, and the line-side mitigation strategy. Trade-off resolution depends on the detailed electrical study outputs referenced in DBM §756. (`TBD` until those study results are available.)
- **Integral isolation / bypass provisions.** Whether to include integral isolation and bypass cabinets affects starting-VFD reliability strategy and EPC tie-in design; not stated in accessible source slices; `TBD`.

## Examples

Locally accessible source slices do not contain worked vendor-package examples; this section is intentionally limited to source-grounded illustrations.

- *Application illustration (from DBM):* "Each inlet compressor is driven by a 4,000 V, three-phase, 60 Hz electric motor rated 3,878 kW / 5,200 hp ... continuous inverter-duty service, and a starting VFD." (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §324)
- *Topology illustration (from DBM):* "The 4160V MCC provides field-fused contactors, motor protection relays, and an EtherNet communication port to the plant PLC central control panel for data acquisition. The MCC serves large 4000V motors, including inlet compressors KM-2150 and KM-2250." (DBM §754)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-019-04-001 | Workbook package title states 5000 HP / 4160 V, but the DBM motor basis states 5,200 HP / 4,000 V driven motors. | Workbook Packages row 21 (PackageName); Gate 7 `PACKAGE_REGISTER.csv` `PKG-019` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §324, §523, §533 | `Datasheet.md` Attributes (driven motor basis vs. package title); `Specification.md` REQ-019-04-04, REQ-019-04-11 | Accept the DBM motor basis (5,200 HP / 4,000 V) as the design basis and treat the workbook title as identity-only nomenclature for PKG-019; record the resolution in `_MEMORY.md` and the package datasheet. | TBD |
| HRR-019-04-002 | DBM allocates starting VFDs to two inlet compressor motors (`KM-2150`, `KM-2250`), but the PKG-019 vendor package quantity (1 vs. 2 VFD units) is not explicitly stated in the workbook row or DBM source slices. | DBM §326, §523, §756 | Workbook Packages row 21 (no explicit quantity) | `Datasheet.md` Attributes; `Specification.md` REQ-019-04-02; `Procedure.md` prerequisites | Record VFD quantity as `TBD` and confirm under EPC Package Datasheet (`DEL-019-02`); do not assume one-per-motor without confirmation. | TBD |
| HRR-019-04-003 | Vendor / EPC ownership for IEEE 519 / IEC 61800-series compliance evidence is not explicit in accessible sources. | Gate 7 `PACKAGE_REGISTER.csv` `PKG-019` (ResponsibilityNarrative) | DBM §756 (defers mitigation to detailed electrical studies) | `Specification.md` REQ-019-04-10, Standards table; `Procedure.md` verification | Treat vendor package as required to *accept* mitigation requirements derived by the EPC-led electrical studies; vendor supplies compliance evidence against final accepted inputs. | TBD |

## Cross-references

- `Datasheet.md` — identification, attributes, conditions, construction, references.
- `Specification.md` — scope, requirements, standards, verification, documentation.
- `Procedure.md` — prerequisites, steps, verification, records.
- Sibling deliverables: `DEL-019-01`, `DEL-019-02`, `DEL-019-03`, `DEL-019-05`, `DEL-019-06`.
