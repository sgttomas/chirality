# Specification — DEL-065-06 EPC Vendor Package Review and Acceptance

EpistemicStatus: DRAFT (Pass 1/Pass 2)

## Scope

This specification governs the EPC Integrator's review and acceptance of the Package Vendor's deliverables for `PKG-065` (Tanks, Caustic API 650, 4-25). It covers vendor document review, integration acceptance against the EPC Scope of Work (DEL-065-01), Package Datasheet (DEL-065-02), and Construction Work Package (DEL-065-03), and handoff readiness to construction, commissioning, and operations. (`_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv row 491.)

**In scope:** vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence (`_CONTEXT.md` Anticipated Artifacts).

**Out of scope:** vendor-side detailed engineering content production (Vendor Engineered Equipment Package — DEL-065-04); vendor document register and submittals authoring (Vendor Document Turnover Package — DEL-065-05); other-package acceptance.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-06-01 | The EPC Integrator shall maintain a vendor document review log covering all submittals listed in the Vendor Document Turnover Package (DEL-065-05). | `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER.csv row 490 |
| REQ-06-02 | The EPC Integrator shall verify that the Vendor Engineered Equipment Package (DEL-065-04) meets the EPC Scope of Work (DEL-065-01) and Package Datasheet (DEL-065-02). | `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv rows 486, 487, 489 |
| REQ-06-03 | The EPC Integrator shall verify caustic tank conformance to API 650 as the governing tank specification. | PACKAGE_REGISTER.csv / package name "Tanks, Caustic (API 650) 4-25"; API 650 clause references — location TBD |
| REQ-06-04 | The acceptance checklist shall confirm fresh caustic tank: 1 x 400 bbl, atmospheric, heated, insulated, truck-in capable, fuel-gas blanketed, not connected to VRU header. | DBM-Deepcut lines 1528, 1562 |
| REQ-06-05 | The acceptance checklist shall confirm spent caustic tank: 1 x 400 bbl, atmospheric, heated, insulated, truck-out capable, incinerator-header connected, flame-arrestor protected, low-pressure fuel-gas blanketed. | DBM-Deepcut lines 1529, 1562 |
| REQ-06-06 | The acceptance checklist shall confirm the fresh caustic tank design specific gravity basis of 1.75 (TBC). | DBM-Deepcut line 1562 |
| REQ-06-07 | Material acceptance shall confirm absence of aluminum in the caustic building; stainless steel insulation cladding/straps in caustic exposure areas; caustic-compatible (polymer or equivalent) tank materials. | DBM-Deepcut line 1566 |
| REQ-06-08 | Installation acceptance shall confirm indoor placement within the Mercaptan Treating Unit building or immediately adjacent area. | DBM-Deepcut line 1552 |
| REQ-06-09 | Acceptance shall confirm safety-shower provision in the caustic building with discrete control-room alert on activation. Shower quantity and location: TBD (carry as open item until detailed engineering closes). | DBM-Deepcut line 1552 |
| REQ-06-10 | The EPC Integrator shall verify that the Construction Work Package (DEL-065-03) tie-ins, turnover checklist, and installation plan are satisfied by vendor-supplied documentation. | DELIVERABLE_REGISTER.csv row 488 |
| REQ-06-11 | Acceptance evidence shall include test/inspection records demonstrating vessel pressure tests, weld inspections, and any code-stamp/certification artifacts required by API 650 (specific test list TBD). | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION — specific tests not yet extracted from sources |
| REQ-06-12 | Turnover evidence shall be sufficient to support handoff to commissioning and operations. Format TBD. | `_CONTEXT.md` Anticipated Artifacts |

## Standards

| Standard | Applicability | Source / Location |
|---|---|---|
| API 650 | Welded tanks for oil storage — governing tank specification for this package. | Package name; clause references — location TBD (standard not locally accessible) |
| `26020-Package_Requirements.docx` package heading 20 | Project package requirements basis | Local binary file in `_Sources/`; slice not extracted — location TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-06-01 | Review of vendor document review log against DEL-065-05 submittal index. |
| REQ-06-02 | Cross-reference matrix: DEL-065-04 deliverables vs. DEL-065-01 SOW and DEL-065-02 Datasheet line items. |
| REQ-06-03 | Inspection of API 650 code-stamp / nameplate and supporting calculations / weld records. |
| REQ-06-04 / 05 / 06 / 07 / 08 | Acceptance checklist sign-off against DBM-cited values; deviations recorded with disposition. |
| REQ-06-09 | Construction walkdown; alert-loop functional test. |
| REQ-06-10 | Construction Work Package alignment check; tie-in verification matrix. |
| REQ-06-11 | Review of vendor inspection and test records (ITRs); witness/hold point closure log. |
| REQ-06-12 | Turnover dossier completeness check against the to-be-defined turnover artifact list (TBD). |

## Documentation

Required artifacts (from `_CONTEXT.md` Anticipated Artifacts):

- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence
- Turnover evidence

Inputs consumed:

- EPC Scope of Work (DEL-065-01)
- EPC Package Datasheet (DEL-065-02)
- EPC Construction Work Package (DEL-065-03)
- Vendor Engineered Equipment Package (DEL-065-04)
- Vendor Document Turnover Package (DEL-065-05)
