# Specification — DEL-096-06 EPC Vendor Package Review and Acceptance (PKG-096 Tanks, Sour Condendate (API 650))

## Scope

### In Scope

This deliverable is the EPC Integrator's vendor-package review-and-acceptance evidence set for PKG-096 (Tanks, Sour Condendate (API 650)). It comprises:

- Review of the Package Vendor's engineered equipment package (DEL-096-04) and Vendor Document Turnover Package (DEL-096-05) against the EPC Scope of Work (DEL-096-01), Package Datasheet (DEL-096-02), and Construction Work Package (DEL-096-03).
- Integration acceptance: confirmation that the vendor package satisfies the "Yes" interfaces declared in the package heading's Physical Interface Summary, and that "By Others" boundary items are handled by the EPC Integrator (not the vendor).
- Handoff readiness: confirmation that test/inspection evidence and turnover documentation are complete and traceable.

Source: `_CONTEXT.md` Scope; SOW-0217..SOW-0220 (per `_CONTEXT.md` Covers Scope Items).

### Out of Scope (By Others, per source)

- Foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase — declared "By others" in package source. These belong to the EPC Integrator's discipline production packages, not the vendor package under review. Source: `26020-Package_Requirements.docx` package heading "Tanks, Sour Condensate" — Scope Notes / Open Items.
- Vendor authoring of the engineered equipment package and the vendor document turnover package themselves (those are DEL-096-04 and DEL-096-05).
- Authoring of the SOW, Package Datasheet, and Construction Work Package (those are DEL-096-01, DEL-096-02, DEL-096-03).
- Final human approval / certification of the vendor package for reliance — this deliverable produces review-and-acceptance evidence; binding approval is recorded by a human per K-AUTH-1.

## Requirements

### REQ-1 — Acceptance basis identified

The review-and-acceptance dossier SHALL identify the acceptance basis as the EPC Scope of Work (DEL-096-01), the Package Datasheet (DEL-096-02), and the Construction Work Package (DEL-096-03).

- Source: `_CONTEXT.md` Scope ("integration acceptance, and handoff readiness against the EPC Scope of Work, Package Datasheet, and Construction Work Package").

### REQ-2 — Vendor inputs identified

The dossier SHALL identify the vendor inputs under review, comprising the Vendor Engineered Equipment Package (DEL-096-04) and the Vendor Document Turnover Package (DEL-096-05).

- Source: `_CONTEXT.md` Scope; sibling deliverable IDs within `PKG-096`. **ASSUMPTION (best-effort mapping)**: identifiers inferred from sibling deliverable folders; not explicitly named in the package heading.

### REQ-3 — Vendor-document review log

The dossier SHALL include a vendor document review log that records, for each vendor-submitted document, at minimum: document ID and title, vendor revision, date received, reviewer, review status (e.g., Accepted, Accepted with Comments, Rejected — exact code-set TBD; align with project document control procedure), review comments, comment-disposition status, and re-submittal reference where applicable.

- Source: `_CONTEXT.md` Anticipated Artifacts ("Vendor document review log"); package heading — Vendor Engineering Deliverables list (`DOC-008` Vendor Document Control Procedure as basis).
- Status code-set: location TBD (refer to project document control procedure).

### REQ-4 — Package acceptance checklist tied to source-derived attributes

The dossier SHALL include a package acceptance checklist that verifies, item-by-item, the vendor package against source-declared attributes for PKG-096:

- Quantity and tags: Two (2) 3800 bbl Sour Inlet Condensate Storage Tanks, TK-9110-2 and TK-9120-2.
- Code/fabrication: Modified API 650.
- Service: Sour (H2S); NACE compliant.
- Blanket gas: per API 2000.
- Internal coating: Devchem 253 on floors, walls, roofs.
- Insulation: Non-insulated.
- Pressure relief: PVRV and EPRV provided; VRU header connection provided.
- Fill protection: Maximum fill 90% shutdown; nozzles sized so plant design capacity can fill a single tank.
- Design conditions: 32 oz test pressure; -40 °C / 60 °C; design flow 27,606 kg/h / 919 Am3/d (Item No. 1).

- Source: `26020-Package_Requirements.docx` package heading "Tanks, Sour Condensate" — Basic Scope, Major Included Equipment, Scope Notes / Open Items.

### REQ-5 — Interface integration acceptance

The dossier SHALL verify that the vendor package addresses, or is correctly bounded against, each interface in the package heading's Physical Interface Summary. Applicable ("Yes") interfaces for this package include: Process Piping; Relief / Flare / Vent; Drain / Containment; Area / Exterior Lighting; Grounding / Bonding; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Non-applicable ("No") interfaces SHALL be confirmed not present in vendor scope.

- Source: `26020-Package_Requirements.docx` package heading "Tanks, Sour Condensate" — Physical Interface Summary.

### REQ-6 — Vendor engineering deliverable completeness

The dossier SHALL record receipt and review status for each vendor engineering deliverable applicable to this package, including (non-exhaustive — full list per package heading): `MEC-001`, `MEC-002`, `MEC-003`, `MEC-005`, `MEC-006`, `MEC-011`, `MEC-014`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-021`, `MEC-022`, `MEC-023`, `MEC-024`, `MEC-025`, `PRO-008`, `PRO-014`, `PRO-015`, `PRO-016`, `PRO-017`, `PRO-018`, `PIP-003`, `PIP-004`, `PIP-006`, `PIP-007`, `PIP-008`, `PIP-009`, `PIP-017`, `PIP-018`, `PIP-024`, `PIP-025`, `PIP-028`, `PRQ-009`, `PRQ-013`, `PRQ-015`, `PRQ-016`, `DOC-008`, `QLT-003`, `QLT-006`, `QLT-013`, `QLT-020`, `QLT-021`.

- Source: `26020-Package_Requirements.docx` package heading "Tanks, Sour Condensate" — Vendor Engineering Deliverables.

### REQ-7 — Test/inspection evidence

The dossier SHALL capture evidence of FAT, ITP execution, NDE results, material certification (MTRs), and inspection release for the package, referencing the corresponding vendor deliverables: `MEC-021` FAT/Performance Test Procedure, `MEC-022` FAT/Performance Test Report, `QLT-003` ITP, `QLT-013` Material Test Reports / Certificates, `QLT-020` Inspection Release Certificate.

- Source: `_CONTEXT.md` Anticipated Artifacts ("test/inspection evidence"); package heading — Vendor Engineering Deliverables.

### REQ-8 — Turnover evidence and handoff readiness

The dossier SHALL evidence handoff readiness via the Manufacturing Record Book / Vendor Data Book (`QLT-021`, `PRQ-016`, `MEC-023`), the Mechanical Equipment IOM Manual (`MEC-025`), the Spare Parts Interchangeability Record (`PRQ-015`), and the Logistics / Shipping Plan (`PRQ-013`).

- Source: `_CONTEXT.md` Anticipated Artifacts ("turnover evidence"); package heading — Vendor Engineering Deliverables.

### REQ-9 — "By Others" boundary confirmation

The dossier SHALL explicitly confirm that the "By Others" items — foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase — are not in vendor scope and are tracked to EPC Integrator discipline production packages.

- Source: `26020-Package_Requirements.docx` package heading "Tanks, Sour Condensate" — Scope Notes / Open Items.

### REQ-10 — Acceptance status and disposition

The dossier SHALL conclude with an acceptance status per checklist item and an overall acceptance disposition (e.g., Accepted / Accepted with Open Items / Rejected — exact code-set TBD; align with project quality procedures), with traceable open-items list referencing the document and section that originated each open item.

- Source: ASSUMPTION — derived from standard EPC vendor-package acceptance practice and from the deliverable Type ("EPC Vendor Package Acceptance"). Status code-set: location TBD.

## Standards

- **API 650** (Modified) — design and fabrication code for the vendor's tanks under review. Citation source: package heading. Standard text: **location TBD** (standard not locally accessible).
- **API 2000** — blanket gas / venting basis for the vendor's tanks under review. Citation source: package heading. Standard text: **location TBD**.
- **NACE** — sour-service material compliance (specific NACE document, e.g., MR0175, not stated in package source). Citation source: package heading. Standard text: **location TBD**.
- **Modified API 650** specifically: "Modified" qualifier not defined in package heading — applicable modifications **TBD** (refer to the RFQ at `Bid Docs/Budgetary/26020-03-PT-RFQ-19-005 - Sour Conde Tanks.docx` — **location TBD**, not locally accessible).
- Project document control procedure (governs review status codes): **location TBD**.
- Project quality procedure (governs acceptance disposition codes): **location TBD**.

## Verification

| Requirement | Verification approach | Verification record (Procedure step) |
|---|---|---|
| REQ-1 | Documentary check that dossier cover/index names DEL-096-01, DEL-096-02, DEL-096-03 as acceptance basis | Procedure Step 1 |
| REQ-2 | Documentary check that dossier identifies DEL-096-04 and DEL-096-05 as inputs under review | Procedure Step 1 |
| REQ-3 | Inspect vendor-document review log for required fields; sample at least one entry per document class | Procedure Step 2 |
| REQ-4 | Compare each checklist item to the source attribute in the package heading; confirm value match or accepted deviation | Procedure Step 3 |
| REQ-5 | For each "Yes" interface, confirm vendor scope evidence or accepted interface handoff; for each "No" interface, confirm absence from vendor scope | Procedure Step 4 |
| REQ-6 | Reconcile vendor deliverable list against package heading "Vendor Engineering Deliverables"; list any missing IDs as open items | Procedure Step 5 |
| REQ-7 | Verify presence and review status of MEC-021, MEC-022, QLT-003, QLT-013, QLT-020 | Procedure Step 6 |
| REQ-8 | Verify presence and review status of QLT-021, PRQ-016, MEC-023, MEC-025, PRQ-015, PRQ-013 | Procedure Step 7 |
| REQ-9 | Cross-check the "By Others" list against EPC discipline production packages; confirm none assigned to vendor | Procedure Step 8 |
| REQ-10 | Confirm acceptance status field populated per checklist item and overall disposition recorded with open-items list | Procedure Step 9 |

## Documentation

Per `_CONTEXT.md` Anticipated Artifacts, the dossier comprises:

- `Vendor_Document_Review_Log` (per REQ-3) — recommended structure: tabular, one row per vendor document.
- `Package_Acceptance_Checklist` (per REQ-4..REQ-9) — recommended structure: one row per acceptance item with source reference.
- `Test_Inspection_Evidence_Index` (per REQ-7) — index pointing to FAT, ITP, MTR, inspection release records.
- `Turnover_Evidence_Index` (per REQ-8) — index pointing to MRB/VDB, IOM, SPIR, shipping documents.
- `Acceptance_Summary_and_Open_Items` (per REQ-10) — overall disposition and open-items list.

Exact filenames, formats, and storage locations: TBD (defer to project document control procedure).
