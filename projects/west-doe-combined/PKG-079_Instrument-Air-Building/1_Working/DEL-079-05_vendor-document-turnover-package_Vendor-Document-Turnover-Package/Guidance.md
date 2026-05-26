# Guidance: DEL-079-05_vendor-document-turnover-package

## Purpose

The Vendor Document Turnover Package exists to assemble and turn over the vendor-produced documentation for `PKG-079`, the Instrument Air Building package, in a controlled, register-tracked form that supports EPC Integrator interface/integration review and downstream operations handover. It should let operations, construction, and EPC integration verify that the vendor has produced and delivered the documents needed to design, fabricate, ship, install, commission, operate, and maintain the package as specified at heading 32 of `_Sources/26020-Package_Requirements.docx`.

## Principles

- Preserve source spelling and identity. The package name is carried as "Instrument Air Building" because that is the workbook and Gate 7 register spelling; the CoA tracking number `26020-01-39-001` is preserved as written.
- Treat workbook interface `X` facts as evidence for what the vendor documentation must address; do not promote interfaces to separate deliverables.
- Keep vendor-owned documentation production with the Package Vendor and interface/integration review with the EPC Integrator.
- Enumerate vendor documents by source-listed code. The Package Requirements source provides a complete Vendor Engineering Deliverables table for this package; use those codes verbatim rather than inventing equivalents.
- Use `TBD` for items the accessible source does not state (submittal stages, hold/issue codes, transmittal numbering, acceptance criteria, Interface Coordination Notes).
- Treat individual vendor-document rows from source as artifacts/evidence, not as separate deliverables, consistent with `_CONTEXT.md` notes and `ARTIFACT_REGISTER.csv` row structure.

## Considerations

The Comp & Liquids DBM source establishes vendor document registers as a required package deliverable for mechanical/equipment packages alongside datasheets, cause-and-effect inputs, utility load summaries, relief/load data, tie-in lists, operating envelopes, sparing, materials/coating basis, maintenance access, and shipped-loose item lists (line 617). That basis supports requiring a vendor document register here. Unlike most packages, the Package Requirements source already enumerates a detailed Vendor Engineering Deliverables table for heading 32 (Instrument Air Building), so the register schema is richer than a typical source-gap case.

The source Basic Scope and Major Included Equipment slices describe an oil-injected rotary screw compressed air package with definite ratings: 2 x 1113 SCFM at 861 kPag (125 psig) compressors driven by 2 x 250 HP motors, a wet air receiver, two dryer pre-filters, a regenerative desiccant air dryer (100% capacity, two tanks/towers), a common after-filter, and one or two dry air receivers. All PSVs are set at 948 kPag (137.5 psig) and the delivered instrument air dew point is -73.3 °C at 1000 kPag. These values are source-anchored design conditions that vendor data sheets must preserve.

The source Physical Interface Summary applies to ten interface types (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports), matching the ten `INTERFACE_REGISTER.csv` rows for PKG-079. Three interface types listed in some peer packages (Process Piping, Relief / Flare / Vent, EHT, Cathodic Protection, Communications / Network, Grading / Site Drainage / Spill Containment, Product Loading, Pipeline / Pigging) are explicitly marked "No" in the source for this package.

The source Scope Notes / Open Items explicitly designate as "by others": shipping compressor packages to site, installation on piles, tie-in piping, electrical connections, and mounting platform and stairs. Vendor turnover documentation should not assume those scope items.

The artifact register confirms that one `ARTIFACT_REGISTER.csv` row exists per source vendor-document code (plus per-category evidence rows), reinforcing the "rows-as-artifacts" pattern of `_CONTEXT.md`.

The source Interface Coordination Notes record "TBD"; this is an explicit source-acknowledged gap that vendor or EPC coordination must close.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Vendor document register schema | Require the full enumerated source list (Core vendor documents, Core package engineering, Rotating equipment / compressors, Static pressure equipment, Utility piping interfaces, Drainage / containment interfaces, Electrical/lighting/EHT/grounding, Instrumentation and controls interfaces, Building / HVAC / code interfaces, Fire and gas / technical safety interfaces, Structural/foundations/supports/access), carrying each by its source code (e.g., `MEC-008` Compressor Data Sheets, `INS-018` Instrument I/O List). Mark register columns (document number, title, revision, status, transmittal, hold/issue code) as `TBD`. | `_Sources/26020-Package_Requirements.docx` heading 32 enumerates the codes; column-level metadata is not stated in the accessible source set. |
| Submittal stages and hold/issue codes | List as `TBD` and require vendor or EPC procedure to define under `DOC-008` Vendor Document Control Procedure. | No accessible source defines stages or hold codes for this package. |
| Pressure equipment registration | List `REG-022` (Pressure Equipment Registration Package) as a required vendor deliverable; jurisdictional code references are `TBD`. | Source lists `REG-022` but does not state jurisdiction or registration authority. |
| Fire code / building code compliance | List `REG-021` as required; specific codes/editions are `TBD`. | Source lists `REG-021` but does not state code edition. |
| SIL determination scope | Require `TSF-009` (SIL Determination Report), `TSF-011` (SRS), and `TSF-013` (Supplier SIL Documentation / Safety Manual) as vendor deliverables; SIF list and target SIL are `TBD`. | Source lists the documents but not the SIF inventory or targets. |
| Dry air receiver count | Carry "one dry air receiver (or two 50% capacity receivers)" as a vendor-determined choice. | Source explicitly states the disjunction. |
| Dryer sizing | Carry "size and capacity TBD by vendor" with the constraint that the dryer is sized for 2 compressors. | Source explicitly states "size and capacity TBD by vendor." |
| Interface Coordination Notes | Carry as `TBD`. | Source explicitly records "TBD." |
| By-others scope | Treat shipping, installation on piles, tie-in piping, electrical connections, and mounting platform/stairs as outside vendor turnover scope. | Source explicitly designates these as by-others. |
| Standards | List vendor RFQ (`26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx`), DBM mechanical-package-deliverables basis, and source-listed registration/code deliverables (`REG-022`, `REG-021`) with detailed clauses `TBD`. | DBM and source reference these bases but specific clauses/specifications are not accessible. |

## Examples

- Acceptable register entry: "Vendor document register row: source code `MEC-008` Compressor Data Sheets; document number `TBD`; revision `TBD`; transmittal `TBD`; hold/issue code `TBD`. Source basis: `_Sources/26020-Package_Requirements.docx`, heading 32, Vendor Engineering Deliverables table; `ARTIFACT_REGISTER.csv` row `ART-5DDAE82D5E`."
- Acceptable interface treatment: "Vendor grounding interface drawings and bonding details shall be included via `ELE-012` Grounding / Earthing Study and `ELE-019` Earthing / Bonding Layout Drawings. Source: `INTERFACE_REGISTER.csv` row `IFC-CD84DBE736`; `_Sources/26020-Package_Requirements.docx`, heading 32, Electrical/lighting/EHT/grounding."
- Acceptable design-condition statement: "Vendor data sheets shall reflect PSV set 948 kPag (137.5 psig) and delivered air dew point -73.3 °C at 1000 kPag. Source: `_Sources/26020-Package_Requirements.docx`, heading 32, Major Included Equipment."
- Not acceptable without new source: "Submittal stage 1 (for-review) shall be due 4 weeks ARO and stage 3 (as-built) shall be due 60 days after mechanical completion." The accessible source set does not establish these stages or durations for this package.
- Not acceptable without new source: assigning a SIL target to a specific SIF without `TSF-009`/`TSF-011` content.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-079-05-001 | Source enumerates a full Vendor Engineering Deliverables table by code, but states no package-specific submittal stages, hold/issue review codes, transmittal numbering, or turnover acceptance criteria; the source also records "Interface Coordination Notes: TBD." | `_Sources/26020-Package_Requirements.docx`, heading 32, Vendor Engineering Deliverables table | `_Sources/26020-Package_Requirements.docx`, heading 32, Interface Coordination Notes (TBD) | Datasheet Construction; Specification Requirements; Procedure Steps | Require all source-listed Vendor Engineering Deliverables codes and `DOC-008`/`PRQ-009` for control/index; keep submittal stages, hold/issue codes, transmittal numbering, acceptance criteria, and Interface Coordination Notes `TBD` until source-supported. | TBD |
| HRR-079-05-002 | Source designates several scope items as "by others" (shipping to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs). It is therefore ambiguous whether vendor turnover documentation should include installation/transport documentation beyond `MEC-017` (Equipment Installation / Setting Drawings), `MEC-018` (Lifting / Handling Study), `PRQ-013` (Logistics / Shipping Plan), and `STR-014` (Lifting Lug / Transport Analysis). | `_Sources/26020-Package_Requirements.docx`, heading 32, Scope Notes / Open Items | `_Sources/26020-Package_Requirements.docx`, heading 32, Vendor Engineering Deliverables table | Specification Scope; Specification Requirements; Guidance Trade-offs | Limit vendor turnover documentation to the source-listed Vendor Engineering Deliverables codes; do not extend into by-others installation/tie-in/electrical/mounting scope. | TBD |
| HRR-079-05-003 | Dryer size and capacity are explicitly "TBD by vendor"; dry air receiver count is "one (or two 50% capacity)". These are intentional vendor-determined choices, but they create ambiguity for data-sheet completeness checks at turnover. | `_Sources/26020-Package_Requirements.docx`, heading 32, Major Included Equipment | None (single-source vendor-discretion statement) | Datasheet Attributes; Specification Requirements; Procedure Verification | Accept vendor selection at turnover as long as documented in `MEC-003` / `MEC-008` and supported by `MEC-014` (Mechanical Calculation Package); record the choice and rationale in the turnover record book. | TBD |
