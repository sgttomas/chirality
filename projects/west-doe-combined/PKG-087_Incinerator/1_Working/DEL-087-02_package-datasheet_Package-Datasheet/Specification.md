# Specification: DEL-087-02 — PKG-087 Incinerator Package Datasheet

## Scope

This specification governs the production and content of the **PKG-087 Incinerator Package Datasheet** — the mandatory EPC Integrator technical handoff document containing the package data required for third-party vendor or discipline package engineering and design (per `_CONTEXT.md`).

**In scope:**
- Identification, attribute, condition, and construction fields for the single Incinerator package consisting of incinerator stack `FL-6920-1`, knockout drum `V-6900-1`, transfer pump `P-6900-1`, and blower `B-6920-1`.
- Package interface requirements matrix (interface types from PACKAGE_REGISTER.csv row PKG-087, corroborated by `26020-Package_Requirements.docx` heading 40).
- Source-supported equipment and design criteria traceable to `26020-Package_Requirements.docx` heading 40 and DBM cross-facility allocation language.
- Vendor engineering handoff basis.

**Out of scope:**
- Detailed mechanical design of vendor-supplied internals (burner, refractory, demister, instrumentation hookups).
- Detailed electrical design beyond motor ratings and MCC interface declaration (by EPC per source).
- Process simulation and emissions modelling (vendor and EPC detailed design; final allocation per DBM Emissions section is not permit-final).
- Construction work package content (DEL-087-03), vendor-engineered-equipment package content (DEL-087-04), vendor-document-turnover (DEL-087-05), and EPC vendor package review and acceptance (DEL-087-06) — these are separate sibling deliverables.

## Requirements

### R1 — Source-grounded identification
The datasheet MUST populate Identification fields from `_CONTEXT.md` and the PROJECT_DECOMP `PACKAGE_REGISTER.csv` row PKG-087.
Source: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-087.

### R2 — Single-train (1 x 100 percent) architecture
The datasheet MUST represent the package as a single train consisting of one stack, one KO drum, one transfer pump, and one blower. No installed spare is identified in the source slice.
Source: `26020-Package_Requirements.docx` heading 40, Basic Scope and Major Included Equipment. (Spare philosophy labelled ASSUMPTION in Datasheet pending RFQ slice.)

### R3 — Process function statement
The datasheet MUST state the process function as receiving vapours from the spent caustic storage tank and the caustic regeneration column overheads.
Source: `26020-Package_Requirements.docx` heading 40, Basic Scope; corroborated in `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` caustic treating section (spent caustic tank flame-arrestor vent to incinerator header; incinerator overhead / dilution / enrichment-gas interfaces).

### R4 — Equipment tag fidelity
The datasheet MUST carry equipment tags verbatim from source: `V-6900-1` (KO drum), `P-6900-1` (KO drum transfer pump), `FL-6920-1` (incinerator stack), `B-6920-1` (incinerator blower).
Source: `26020-Package_Requirements.docx` heading 40, Major Included Equipment.

### R5 — Design conditions verbatim
The datasheet MUST carry the following design conditions verbatim from source:
- Design ambient temperature: -40 / +35 deg C.
- KO drum design pressure: 345 kPag (50 psig).
- KO drum design temperature: -45.5 to +260 deg C.
- KO drum corrosion allowance: 1.59 mm.
- Incinerator operating pressure: 1 psig (7 kPag).
- Preliminary design throughput: 0.6 MMSCFD (17 E3M3D) for the incinerator and KO drum.
- Transfer pump design throughput: 70 USGPM.
Source: `26020-Package_Requirements.docx` heading 40, Major Included Equipment and Scope Notes.

### R6 — Motor starting basis
The datasheet MUST record that VFD or soft start is required for motors >= 100 hp, applicable to `B-6920-1` (100 hp).
Source: `26020-Package_Requirements.docx` heading 40, Scope Notes (Driver).

### R7 — "By others" boundary statements
The datasheet MUST record the following as EPC scope (by others):
- DCS integration.
- Foundations.
- Electrical supply to MCC.
Source: `26020-Package_Requirements.docx` heading 40, Scope Notes.

### R8 — Interface matrix fidelity
The datasheet MUST list the applicable interface types from `PACKAGE_REGISTER.csv` row PKG-087 and corroborate Yes/No applicability against `26020-Package_Requirements.docx` heading 40, Physical Interface Summary. Where the two registers disagree (e.g., Building HVAC / Services), the discrepancy MUST be captured in the Conflict Table (see `Guidance.md`).
Source: `PACKAGE_REGISTER.csv` row PKG-087; `26020-Package_Requirements.docx` heading 40.

### R9 — Shared-interface allocation visibility
The datasheet MUST surface that the incinerator is a shared-interface system under the current 03-25 / 04-25 allocation and that the exact service split is an open interface item (not closed by the datasheet).
Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Exclusions and Superseded Scope; Emissions; Inter-facility Interfaces).

### R10 — Self-framing building scope
The datasheet MUST record that a self-framing building is erected at site as part of the package scope.
Source: `26020-Package_Requirements.docx` heading 40, Major Included Equipment.

### R11 — Unknown values marked, not invented
Any value that depends solely on the inaccessible RFQ (`Bid Docs/Budgetary/26020-01-PT-RFQ-25-003_Incinerator.docx`), the source `Appendix A` fluid table, the PFD referenced for instrumentation, or unread cells in `26020-Packages_Interfaces.*.xlsx` MUST be marked `location TBD` or `TBD`. No invented metallurgy, refractory, burner, instrumentation, or emissions values are permitted.

## Standards

- No package-specific standards (NFPA, API 537, API 521, NFPA 86, etc.) are quoted in the accessible source slice. The datasheet does not assert standards compliance beyond what the source states.
- Sour service material requirements: not stated in heading 40 for this package; not asserted in the datasheet. (location TBD if applicable.)
- Pressure equipment registration (Alberta/CRN) for `V-6900-1`: governance is implied by `REG-022` in the package's Vendor Engineering Deliverables list (heading 40); the datasheet does not assert specific registration code beyond that deliverable's existence.

## Verification

| Requirement | Verification |
|---|---|
| R1 | Cross-check Identification table cells against `_CONTEXT.md` and `PACKAGE_REGISTER.csv` row PKG-087. |
| R2 | Confirm Datasheet Attributes table lists single counts and a "no installed spare" ASSUMPTION (pending RFQ slice). |
| R3 | Confirm Datasheet Attributes row "Process function" matches the source Basic Scope sentence. |
| R4 | Grep Datasheet for `V-6900-1`, `P-6900-1`, `FL-6920-1`, `B-6920-1`. |
| R5 | Compare Datasheet Conditions table to heading 40 Major Included Equipment and Scope Notes. |
| R6 | Confirm Datasheet Construction table records "VFD or soft start required for motors >= 100 hp". |
| R7 | Confirm Datasheet Construction table marks DCS integration, foundations, and MCC supply as "By others (EPC)". |
| R8 | Confirm Datasheet interface list matches PACKAGE_REGISTER.csv row PKG-087 and Conflict Table records the Building HVAC / Services discrepancy. |
| R9 | Confirm Datasheet "Facility allocation context" row cites DBM and labels the shared-interface incinerator as open. |
| R10 | Confirm Datasheet records the self-framing building as in-package scope. |
| R11 | Confirm `TBD` / `location TBD` markers appear for: Appendix A fluid table, PFD instrumentation, RFQ-derived metallurgy, xlsx row 64 details. |

## Documentation

Required artifacts (from `_CONTEXT.md` Anticipated Artifacts):

- Package technical datasheet (`Datasheet.md`) — this deliverable's primary artifact.
- Vendor engineering handoff basis — the four documents collectively constitute the handoff basis for PKG-087.
- Package interface requirements matrix — embedded in `Datasheet.md` (Applicable Interface Types).
- Source-supported equipment and design criteria — `Datasheet.md` Attributes/Conditions/Construction tables.

The companion vendor-engineering deliverables list (PRQ/DOC/QLT/MEC/PRO/PIP/INS/CTL/ELE/CIV/REG/TSF families) enumerated under heading 40 belongs to DEL-087-04 / DEL-087-05 governance, not this datasheet.
