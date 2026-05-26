# Specification — EPC Vendor Package Review and Acceptance (DEL-106-06)

> Normative document. Requirements the EPC Integrator review and acceptance evidence shall satisfy for the PKG-106 Yard Lighting vendor package.

## Scope

This specification governs the EPC Integrator review, integration acceptance, and handoff-readiness evidence for the Yard Lighting vendor package, against:

- the EPC Scope of Work (DEL-106-01),
- the EPC Package Datasheet (DEL-106-02),
- the EPC Construction Work Package (DEL-106-03),
- the Vendor Engineered Equipment Package (DEL-106-04), and
- the Vendor Document Turnover Package (DEL-106-05).

It covers SOW-0011 (`_CONTEXT.md`).

**Excluded:** original vendor design (DEL-106-04 scope); original vendor documentation set (DEL-106-05 scope); construction execution by the construction contractor (DEL-106-03 scope); building-interior lighting where governed by separate building/HVAC packages (ASSUMPTION: scope boundary; not literally documented in available sources); receptacles and convenience power (covered by other packages, ASSUMPTION).

## Requirements

| ReqID | Requirement | Source | Verification (see §Verification) |
|---|---|---|---|
| REQ-1 | The acceptance evidence shall confirm that all yard lighting luminaires supplied are **LED** type. | DBM `4-25_Deepcut_DBM.md` "Lighting and Receptacles" (line 3027); reinforced at line 3031 ("Process area and outdoor lighting shall use LED fixtures") | V-1 |
| REQ-2 | The acceptance evidence shall confirm that general-purpose lighting circuits operate at **120/208 V** and are fed from the nearest power distribution centre, unless deviations are explicitly documented. | DBM `4-25_Deepcut_DBM.md` (line 3027) | V-1, V-2 |
| REQ-3 | The acceptance evidence shall confirm that each luminaire is **suitable for the area classification** of its installed location, with hazardous-area certification documentation included for fixtures installed in classified areas. | DBM `4-25_Deepcut_DBM.md` (line 3027) | V-2, V-3 |
| REQ-4 | The acceptance evidence shall confirm that emergency lighting (where buildings fall within yard package scope) is LED with battery backup, with at least two emergency fixtures per building. | DBM `4-25_Deepcut_DBM.md` (line 3031) | V-2 |
| REQ-5 | The acceptance evidence shall confirm light-pollution control measures: downward illumination (downcast floodlights), no horizontally aimed floodlights, photocell or switch control, selective minimization of exterior lighting to working areas, and mast poles located away from pad edge where mast poles are used. | DBM `4-25_Deepcut_DBM.md` (line 3035) | V-2, V-4 |
| REQ-6 | The acceptance evidence shall confirm that luminaires, drivers, controls, and field wiring are rated for the site ambient envelope (**-40 deg C to +35 deg C**, with -40 deg C minimum ambient governing exposed equipment). | DBM `3-25_Comp_and_Liquids_DBM.md` SEC-04 (lines 96, 145) | V-2 |
| REQ-7 | The acceptance evidence shall confirm that wiring methods, conduit selection, and area-classification sealing comply with the **Canadian Electrical Code** (CEC) as called out in the DBM cable/conduit basis. | DBM `4-25_Deepcut_DBM.md` "Cable, Conduit and Lighting" prose preceding the lighting section (CEC reference) | V-3 |
| REQ-8 | The acceptance evidence shall confirm grounding and bonding continuity for the yard lighting system (poles, fixtures, panels) consistent with the package's declared Grounding/Bonding interface (workbook row 12). | `_Sources/26020-Packages_Interfaces_4_export.xlsx` sheet `Packages` row 12 (Grounding/Bonding = X) | V-3 |
| REQ-9 | The acceptance evidence shall include a vendor document review log recording the disposition of each document required by the Vendor Document Turnover Package (DEL-106-05) against the EPC SOW (DEL-106-01) and Package Datasheet (DEL-106-02). | `_CONTEXT.md` Anticipated Artifacts | V-5 |
| REQ-10 | The acceptance evidence shall include a package acceptance checklist covering: scope conformance to DEL-106-01; technical conformance to DEL-106-02; constructability/turnover conformance to DEL-106-03; integration interface conformance (Electrical Power, Grounding/Bonding, Area/Exterior Lighting). | `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER.csv PKG-106 rows; workbook row 12 | V-5 |
| REQ-11 | Test and inspection evidence shall be collected, indexed, and traceable to the responsible test plan, including (as applicable): factory photometric reports; area-classification certification; grounding/bonding continuity tests; field illumination/uniformity measurements; energization checks; photocell and lighting-control verification. | `_CONTEXT.md` Anticipated Artifacts; DBM lighting section (lines 3027, 3031, 3035) | V-2, V-5, V-6 |
| REQ-12 | Turnover evidence shall record Mechanical Completion, Pre-Commissioning, and Commissioning/Operational Acceptance status for the yard lighting system. | `_CONTEXT.md` Anticipated Artifacts | V-6 |
| REQ-13 | All acceptance and approval signatures shall be performed by humans; the EPC Integrator and the Owner are the authoritative approvers. Agents may draft, summarize, or check, but shall not certify. | Chirality `docs/CONTRACT.md` K-AUTH-1 | V-7 |
| REQ-14 | Items unresolved at the time of acceptance shall be carried as explicit punchlist items with owner and target-resolution date. | ASSUMPTION (industry-standard EPC acceptance practice; not literally quoted in available sources) | V-5 |
| REQ-15 | Regulatory light-pollution compliance shall be evidenced against the governing jurisdictional regulation (regulation citation TBD; not enumerated in available sources). | DBM `4-25_Deepcut_DBM.md` (line 3035) "Regulatory light-pollution requirements"; specific regulation TBD (location TBD) | V-4 |

## Standards

Standards explicitly cited by source materials available locally:

- **Canadian Electrical Code (CEC)** — wiring methods, area-classification compliance, conduit sealing at area-class transitions (DBM `4-25_Deepcut_DBM.md`, cable/conduit prose preceding "Lighting and Receptacles").
- **Project DBMs** — DBM `4-25_Deepcut_DBM.md` "Lighting and Receptacles" section (lines 3027, 3031, 3035); DBM `3-25_Comp_and_Liquids_DBM.md` SEC-04 site basis.

Standards likely applicable but not locally accessible or not enumerated (location TBD):

- 26020-Package_Requirements.docx package heading for PKG-106 — package-level EPC requirements (ASSUMPTION: likely applicable; not text-accessible in this run).
- Workbook Packages row 12 detail beyond interface flags — package-level scope/interface attributes beyond what the exported sheet exposes (ASSUMPTION: likely applicable).
- Hazardous-area certification basis (e.g., CSA C22.2 No. 137 series, IEC 60079 series, or equivalent) — specific standards TBD; selection per CEC and area-classification documents.
- Photometric / illumination design standards (e.g., IES RP-7 for industrial outdoor lighting, or equivalent) — TBD; not enumerated in available sources for this deliverable.
- BC light-pollution / dark-sky regulatory citation — TBD; DBM cites the obligation but not a specific clause.

## Verification

| VID | Method | Applies to |
|---|---|---|
| V-1 | Document review of vendor submittals (datasheets, cut sheets, BoM) | REQ-1, REQ-2 |
| V-2 | Document review against DBM provisions (LED/area-class/emergency/light-pollution/ambient) and field photometric/illumination measurement records | REQ-1, REQ-2, REQ-3, REQ-4, REQ-5, REQ-6, REQ-11 |
| V-3 | Compliance review against CEC, area-classification drawings, grounding/bonding test records | REQ-3, REQ-7, REQ-8 |
| V-4 | Compliance review against jurisdictional light-pollution regulation (citation TBD) and as-built lighting layout/aiming records | REQ-5, REQ-15 |
| V-5 | Audit of review log, acceptance checklist, and punchlist register | REQ-9, REQ-10, REQ-11, REQ-14 |
| V-6 | Audit of test/inspection records and turnover certificates (MC, PC, Commissioning/OA) | REQ-11, REQ-12 |
| V-7 | Audit of acceptance signature records (human signatories) | REQ-13 |

## Documentation

Required artifacts produced under this deliverable (consistent with `_CONTEXT.md` Anticipated Artifacts):

- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence index (factory photometric, area-class certification, grounding continuity, field illumination/uniformity, energization, lighting-controls verification)
- Turnover evidence (MC, PC, Commissioning/OA)
- Punchlist register (open items with owner and target date)
- Acceptance signature record
