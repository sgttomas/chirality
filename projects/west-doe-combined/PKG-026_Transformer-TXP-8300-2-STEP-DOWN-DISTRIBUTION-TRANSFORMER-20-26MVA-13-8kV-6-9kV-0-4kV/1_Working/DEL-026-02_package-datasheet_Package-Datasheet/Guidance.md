# Guidance: DEL-026-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-026` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the TXP-8300-2 20/26 MVA 13.8 kV / 6.9 kV / 0.4 kV step-down distribution transformer while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name carries the full "TXP-8300-2 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV" string because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work (vector group, impedance, tap range, BIL, cooling class, monitoring) with the Package Vendor and facility-level integration (feeder routing, grounding tie-in, foundation, area classification) with the EPC Integrator.
- Use `TBD` for cooling class, ambient basis, impedance, vector group, BIL, tap range, sound levels, monitoring detail, foundation type, exact physical location, and tertiary winding service until a source-supported package-specific basis is available.
- Use DBM electrical basis only at the level it supports: medium-voltage class (13.8 kV, 6.9 kV), 3-phase/60 Hz/LRG, neutral grounding via 100 A 10 s NGR on the 6.9 kV side, oil-filled transformer convention, CEC spacing, two-point ground-grid connection, and shielded TECK cable basis.

## Considerations

The DBM electrical design basis supports the medium-voltage side of TXP-8300-2: 13.8 kV facility backbone radially distributed through step-down transformers, with a 6.9 kV bus dedicated to AC inverter-drive process motors rated 5,500 hp and above (the inlet/sales compressor drive class served by the 820-1 6.9 kV Inlet/Sales Compressor Electrical Building). It also supports the 6.9 kV neutral grounding basis (100 A, 10 s NGR, tripping system) and the oil-filled transformer convention (with CEC spacing and containment review).

The DBM does **not** identify a 0.4 kV facility service class. The transformer name nevertheless declares a 0.4 kV winding. This is a real source ambiguity: it could be a tertiary auxiliary winding (e.g., for transformer cooling fans, monitoring, station service, or harmonic mitigation), or it could indicate a different intended use not described in the accessible DBM slice. Vendor-facing datasheet content for the 0.4 kV winding should remain conservative (`TBD`) until source-supported allocation is available, and the open question should be carried into the conflict table.

The dual 20/26 MVA rating implies a two-stage cooling design (e.g., ONAN/ONAF), but the cooling-class code and ambient design basis are not stated in accessible sources. These should be left to vendor data within CEC and project-electrical-specification limits.

Grounding and bonding are applicable interface topics. The DBM source supports two-point connection of major electrical equipment to the ground grid, ground wells at power transformers, and CEC-sized separate copper ground conductors for distribution transformers. The datasheet should require coordination with this basis while avoiding unsupported package-specific conductor sizing.

Maintenance access, area/exterior lighting, I&C / control cabling, and communications / network are explicit workbook interface facts. The datasheet should require facility-side provisions consistent with the DBM convention (bottom-entry cable, TECK/ACIC wiring, climate-controlled electrical buildings) while leaving package-side monitoring protocol bindings to vendor data.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Tertiary 0.4 kV winding | Mark service, loading, and grounding `TBD`; document as a human-ruling item. | DBM voltage/service table does not list a 0.4 kV facility service class. |
| Cooling class / ambient | Note dual rating 20/26 MVA as `ASSUMPTION` of stage-cooled design; leave class code `TBD`. | Source does not state cooling-class designation or ambient basis. |
| Insulating medium | Treat as oil-filled by ASSUMPTION; confirm against vendor selection. | DBM convention is large oil-filled transformers; the specific medium for TXP-8300-2 is not confirmed in source. |
| Physical location | Identify proximity to 820-1 6.9 kV Inlet/Sales Compressor Electrical Building as ASSUMPTION. | DBM lists step-down transformer destinations but does not assign the specific transformer to a pad. |
| Standards | List CEC, area classification, and project electrical specifications as governing bases with locations `TBD`. | DBM references these bases but detailed clauses / specification documents are not available in the deliverable folder. |
| Impedance / vector group / BIL / tap range | Defer to vendor data within project-specification limits. | Source does not establish these values. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 28 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Cooling class: TBD. Dual rating 20/26 MVA implies a stage-cooled design (ASSUMPTION); class code (e.g., ONAN/ONAF) not stated in accessible source."
- Acceptable grounding entry: "Secondary (6.9 kV) neutral grounded via 100 A, 10 s NGR operating as a tripping system. Source: DBM-Deepcut, grounding paragraph."
- Not acceptable without new source: "Impedance 8.5%; vector group YNyn0d1; BIL 110 kV; tap range +/-2x2.5%." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-026-02-001 | Package name declares a 0.4 kV winding, but the DBM voltage/service table does not list a 0.4 kV facility service class; tertiary winding service, loading, and grounding are unconfirmed. | Workbook Packages row 28 (package name); `PACKAGE_REGISTER.csv` row `PKG-026`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table; grounding paragraph. | Datasheet Attributes/Conditions; Specification REQ-026-02-006; Procedure Steps. | Treat 0.4 kV as a vendor-defined tertiary winding; carry service, loading, vector-group, and grounding basis as `TBD` until source-supported allocation is established. | TBD |
| HRR-026-02-002 | Dual rating 20/26 MVA implies a stage-cooled design, but the cooling-class designation (e.g., ONAN/ONAF) and ambient design basis are not stated in accessible sources. | Workbook Packages row 28 (package name dual rating). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph (no cooling-class designation). | Datasheet Attributes; Specification Standards/Verification. | Defer cooling-class code and ambient basis to vendor data within CEC and project-electrical-specification limits; record as ASSUMPTION pending vendor confirmation. | TBD |
| HRR-026-02-003 | The QAS line item `ELC-QAS-000011-001` lists "Oil-Filled Transformers" quantity 2, but explicit allocation to `PKG-026` (vs. the companion PKG-015 TXP-8300-1 12/15 MVA package or other oil-filled units) is not confirmed in accessible sources. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, QAS table. | `PACKAGE_REGISTER.csv` rows `PKG-015` and `PKG-026`. | Datasheet Attributes/Construction; Specification Standards. | Do not assign QAS quantity to `PKG-026`; cite the QAS line item as ASSUMPTION until allocation is confirmed. | TBD |
