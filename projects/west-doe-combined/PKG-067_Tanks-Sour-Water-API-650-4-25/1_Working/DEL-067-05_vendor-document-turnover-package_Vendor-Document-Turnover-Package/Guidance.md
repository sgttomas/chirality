# Guidance — DEL-067-05 Vendor Document Turnover Package (PKG-067 Tanks, Sour Water (API 650) 4-25)

## Purpose

This deliverable establishes a single, controlled, EPC-accepted body of vendor documentation for the PKG-067 sour-water / produced-water tank package so that operations, maintenance, regulatory, integrity-management, and inspection functions can rely on it after package turnover. Per `DELIVERABLE_REGISTER.csv` (DEL-067-05 row), the Package Vendor owns the documentation, and the EPC Integrator performs interface/integration review.

## Principles

- **Document ownership is unambiguous.** The Package Vendor is the document author and owner; the EPC Integrator reviews for interface/integration fit (foundation interface, tie-ins, drainage/containment, grounding, cathodic protection, lighting, I&C), not for vendor internal design correctness (which the vendor warrants).
- **Source vendor document table rows are artifacts, not separate deliverables.** Individual vendor documents listed in Workbook Packages row 94 (location TBD) are evidence supporting this deliverable; they do not create their own decomposition entries. Source: `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` Notes.
- **The register is the truth set.** Status and acceptance derive from the controlled Vendor Document Register, not from ad-hoc transmittals or email.
- **Turnover is the close-out event.** The deliverable is not complete until a final transmittal/manifest is issued and EPC-accepted; absence of explicit acceptance leaves the package documentation open.
- **Source fidelity over convention.** Document categories, codes, and timing required by `26020-Package_Requirements.docx` package heading 22 (location TBD) govern; do not substitute generic vendor-document conventions for the project's stated requirements.
- **Analog use is conservative.** The 3-25 sour water tanks RFQ (`26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx`) is recorded as an analog basis only; analog documentation expectations may inform planning but do not substitute for the 4-25 project-stated requirements.

## Considerations

- The authoritative source for vendor-documentation requirements (`26020-Package_Requirements.docx` package heading 22) and the vendor-doc columns of Workbook Packages row 94 are binary source files (`.docx` / `.xlsx`) listed in `_REFERENCES.md` but not converted to locally readable text in `_Sources`. Substantive category/timing requirements remain `TBD` until source slices are extracted.
- The package covers two atmospheric storage tanks of the same nominal service. Their per-tank documentation must be tracked distinctly on the register (each tag gets its own data report, weld records, hydrostatic test record, etc.).
- Sour-water service raises material, coating/lining, and weld-qualification questions (e.g., NACE MR0175 applicability) — applicability is ASSUMPTION pending source confirmation; if applicable, the turnover set must include qualification and certification evidence.
- Tank vendor documentation typically includes both shop-fabricated and field-erection elements depending on tank size; the register and turnover sequencing must accommodate the chosen fabrication path (ASSUMPTION; specific fabrication path TBD).
- Vendor-document turnover interacts with DEL-067-06 (EPC Vendor Package Review and Acceptance); completeness here is a precondition for acceptance there.
- Interface types declared for PKG-067 (Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports) imply specific documentation that the EPC must receive at clear interface points (e.g., foundation loads, nozzle schedule, grounding lugs, CP coupon locations).
- Supported objectives include OBJ-001/003/004/005/006/007/008/009/010 (per `_CONTEXT.md` package-heuristic association — ASSUMPTION). Documentation completeness is a key input to integrity, operability, maintainability, sparing, isolation, winterization, commissioning, turnover, and open-item closure (per OBJ-010 phrasing in the decomposition).

## Trade-offs

- **Submittal granularity vs. review burden.** Listing every minor vendor document on the register increases EPC review effort but improves traceability. Project document control procedure (location TBD) governs the threshold.
- **Early vs. late submittal of as-builts.** Final as-built drawings can only be issued after fabrication / field erection and hydrostatic testing, but holding back the rest of the package until then delays turnover. Standard practice (ASSUMPTION) is staged submittal with a final as-built revision at turnover.
- **Paper turnover vs. electronic-only.** Electronic data books are typical for current EPC practice (ASSUMPTION); paper turnover may still be specified for jurisdictional records (e.g., API-650 Manufacturer's data report originals where required) — location TBD per project doc-control procedure.
- **Coating/lining documentation depth.** Sour-water service may justify detailed interior-coating QA records (DFT readings, holiday testing, cure records); the register must explicitly track these if required (TBD pending source confirmation).

## Examples

Examples of register line items that would be expected for this package (illustrative only — not extracted from authoritative source; all subject to confirmation against `26020-Package_Requirements.docx` package heading 22, location TBD):

- API-650 Manufacturer's Data Report for `TK-9010-1` and `TK-9020-1`
- General arrangement / fabrication / erection drawings as-built (including foundation interface, nozzle schedule, ladder/platform/handrail)
- Materials test reports (MTRs) for shell, bottom, and roof plate
- Weld Procedure Specifications and Procedure Qualification Records
- NDE records (shell vertical/horizontal weld inspection, bottom weld vacuum-box test, magnetic particle / penetrant inspection as applicable)
- Hydrostatic test record
- Interior coating / lining records (surface prep, DFT, holiday test, cure log) — if specified for sour-water service
- Cathodic protection installation and commissioning records — if part of vendor scope (TBD interface boundary)
- OEM operating and maintenance manual(s)
- Recommended spare-parts list
- Final QA dossier and turnover transmittal

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-067-05-01 | Package name in `PACKAGE_REGISTER.csv` row 94 reads "Tanks, Sour Water (API 650) 4-25" but the 4-25 Deepcut DBM tank list row reads "Tanks, Sour Water (API 650) 2 | PRODUCED WATER STORAGE TANK (x2)" with tags `TK-9010-1`, `TK-9020-1`. The same physical equipment is plausibly referenced under both names ("Sour Water" vs "Produced Water"). Tank tag mapping treated as ASSUMPTION until confirmed. | `PACKAGE_REGISTER.csv` row 94 (Name, ScopeDescription) | `4-25_Deepcut_DBM.md` tank-list rows (line/section TBD) | Datasheet Attributes (Equipment Documented, Tank Specification Basis); Specification REQ-05; Procedure Step 1 | PROPOSAL: treat as same equipment; use tags `TK-9010-1`, `TK-9020-1`; confirm under sour-water service naming in turnover documentation. | TBD |
| CONF-067-05-02 | Sour-service material/weld qualification applicability (NACE MR0175 / ISO 15156) is asserted as ASSUMPTION; no locally accessible source slice confirms or denies applicability for atmospheric produced-water tanks. | `4-25_Deepcut_DBM.md` (sour-service references — section TBD) | `26020-Package_Requirements.docx` package heading 22 (location TBD; binary) | Datasheet Conditions (Sour service considerations); Specification REQ-09 / Standards | PROPOSAL: defer applicability to confirmed source slice; do not require NACE certifications in turnover until confirmed. | TBD |
