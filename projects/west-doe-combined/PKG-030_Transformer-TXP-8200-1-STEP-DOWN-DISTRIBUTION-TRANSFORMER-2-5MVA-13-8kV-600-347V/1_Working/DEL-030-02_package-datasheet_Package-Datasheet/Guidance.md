# Guidance: DEL-030-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-030` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the Transformer TXP-8200-1 (2.5 MVA, 13.8 kV / 600 V / 347 V step-down distribution transformer) while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried verbatim as "Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work (transformer detailed engineering, construction type selection, nameplate parameters, protection settings) with the Package Vendor and facility-level integration (grounding tie-ins, cable routes, foundation/containment coordination, building/yard placement) with the EPC Integrator.
- Use `TBD` for transformer nameplate parameters, construction type, installation location, secondary containment dimensions, cable schedules, and protection settings until vendor data or a detailed-design source is available.
- Use the DBM-Deepcut electrical basis only at the level it supports: System Voltages, Transformers paragraph (CEC spacing, oil-filled vs. dry-type framing, containment review), Foundations table (precast concrete bearing foundations), grounding paragraphs (two-point ground grid, ground wells, separate copper conductor, 5 A HRG resistor), and the cable schedule (ACWU for 600 V secondary).

## Considerations

The DBM-Deepcut System Voltages table directly supports the primary 13.8 kV and secondary 600 V services associated with this transformer. The 347 V leg is best interpreted as the line-to-neutral value of a 600/347 V grounded-wye lighting/utility secondary, but the DBM does not state 347 V explicitly; this interpretation is recorded as an `ASSUMPTION` and not a confirmed nameplate value.

The DBM Transformers paragraph addresses "large oil-filled transformers" generally (CEC spacing, structural-steel bases, containment review) and a specific 480 V dry-type transformer at LACT. It does not assign oil-filled vs. dry-type to TXP-8200-1. At 2.5 MVA, both options are plausible in industry practice; the datasheet keeps construction type `TBD` rather than overstating the source.

The DBM grounding paragraphs supply a complete facility grounding basis that the transformer must conform to: two-point ground grid connection for major electrical equipment, ground wells at power transformers for maintenance testing, distribution transformers fed with a separate copper ground conductor sized per CEC, and 600 V secondary high-resistance grounding using a 5 A continuous resistor with alarm-only ground-fault protection at the 600 V MCC. These are applicable EPC-side requirements regardless of vendor construction choices.

Maintenance access is both a workbook interface fact and a DBM routing constraint (cable tray and conduit shall not interfere with maintenance access). The datasheet should require electrical routing and physical placement to preserve maintenance access and ground-well accessibility; detailed clearances remain `TBD` unless issued by detailed design or vendor data.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Construction type (oil-filled vs. dry-type) | Mark `TBD` pending vendor selection and containment review. | DBM addresses both forms generally but does not assign one to TXP-8200-1. |
| 347 V interpretation | Record as line-to-neutral of a 600/347 V grounded-wye secondary (ASSUMPTION). | Workbook and Gate 7 spelling includes "/347V" but DBM System Voltages table does not state 347 V; industry-standard wye interpretation is the most defensible reading. |
| Nameplate parameters (impedance, BIL, tap range, cooling, vector group) | Mark `TBD`. | No package-specific source slice provides these values; inventing them would be a fabrication. |
| Installation location | Identify as either outdoor pad or electrical-building proximity per detailed design. | DBM describes both possibilities but does not place TXP-8200-1. |
| Secondary containment | Require review per DBM; do not commit to a containment configuration. | DBM says "transformer selection shall avoid or limit containment requirements where practical" — this is a directional principle, not a design. |
| Standards | List CEC, area classification, and project electrical specifications as governing bases with clause/document locations TBD. | DBM references these bases but detailed clauses and specification documents are not in the deliverable folder. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 32 and `INTERFACE_REGISTER.csv`."
- Acceptable source-grounded entry: "600 V secondary high-resistance grounded with 5 A continuous resistor; ground-fault protection at 600 V MCC is alarm-only. Source: DBM-Deepcut grounding paragraphs."
- Acceptable source-gap entry: "Transformer impedance: TBD. No package-specific vendor source slice available."
- Not acceptable without new source: "TXP-8200-1 is an oil-filled, ONAN/ONAF transformer with 5.75% impedance and ±2×2.5% off-circuit taps." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-030-02-001 | Workbook/register names this package as "2.5MVA 13.8kV/600/347V", but the DBM System Voltages table does not list a 347 V service. The "/347V" leg is therefore unverified against the DBM. | Workbook Packages row 32; `PACKAGE_REGISTER.csv` row `PKG-030` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table | Datasheet Attributes; Specification Requirements | Treat 347 V as line-to-neutral of a 600/347 V grounded-wye secondary (industry-standard wye interpretation) until vendor data confirms; keep as ASSUMPTION. | TBD |
| HRR-030-02-002 | DBM Transformers paragraph addresses oil-filled and dry-type forms generally but does not assign a construction type to TXP-8200-1. Containment, spacing, and foundation detail depend on this choice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph | Workbook Packages row 32; `PACKAGE_REGISTER.csv` row `PKG-030` (silent on construction type) | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Keep construction type `TBD`; require vendor to declare construction type and containment basis as part of vendor data submission. | TBD |
| HRR-030-02-003 | Installation location (outdoor pad vs. electrical-building proximity) is not assigned for TXP-8200-1 in any accessible source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings and Transformers paragraphs | Workbook Packages row 32 | Datasheet Construction; Procedure Steps | Defer installation location to detailed-design plot plan; carry as `TBD` in the datasheet. | TBD |
