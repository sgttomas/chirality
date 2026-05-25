# Specification — DEL-014-06 EPC Vendor Package Review and Acceptance

## Scope

This specification defines the EPC Integrator's review and acceptance work for the PKG-014 vendor-engineered Contactor Panels (Lighting / Exhaust Fan) Low-Voltage package. Deliverable scope includes vendor document review, integration acceptance against EPC basis documents, and handoff readiness against the EPC Scope of Work (DEL-014-01), Package Datasheet (DEL-014-02), and Construction Work Package (DEL-014-03). [Source: DELIVERABLE_REGISTER.csv row DEL-014-06; `_CONTEXT.md`]

Excluded: original generation of the Package Vendor's engineered equipment package (covered by DEL-014-04) and the vendor document turnover content itself (covered by DEL-014-05). EPC review of those artifacts is in scope; their authorship is not. [Source: DELIVERABLE_REGISTER.csv rows DEL-014-04, DEL-014-05]

## Requirements

| ReqID | Requirement | Source / Basis |
|---|---|---|
| REQ-014-06-01 | A vendor document review log shall be maintained, recording each vendor-submitted document, revision, review disposition, and resolution status. | `_CONTEXT.md` anticipated artifact; DELIVERABLE_REGISTER.csv row DEL-014-06 |
| REQ-014-06-02 | A package acceptance checklist shall be produced and signed-off, traceable to the EPC SOW (DEL-014-01), Package Datasheet (DEL-014-02), and Construction Work Package (DEL-014-03). | DELIVERABLE_REGISTER.csv rows DEL-014-01/02/03/06 |
| REQ-014-06-03 | Test and inspection evidence shall be collected and retained for vendor-furnished equipment acceptance. | `_CONTEXT.md` anticipated artifact |
| REQ-014-06-04 | Turnover evidence shall be assembled covering vendor document turnover (DEL-014-05) completeness and integration acceptance. | DELIVERABLE_REGISTER.csv row DEL-014-05; `_CONTEXT.md` |
| REQ-014-06-05 | Integration interfaces shall be verified against the package's declared interface set: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | PACKAGE_REGISTER.csv row PKG-014 (Interface Types) |
| REQ-014-06-06 | Vendor LV equipment subject to acceptance shall be verified consistent with the project LV system: 600 V, 3 phase, 3 wire, 60 Hz HRG with 5A continuous resistor, with lighting/utility loads at 120/208 V, 3 phase, 4 wire, 60 Hz solid grounded. | DBM 3-25, lines 734-735 |
| REQ-014-06-07 | Vendor-supplied exhaust-fan/heater controls integration shall be verified consistent with the project RIO architecture, which states RIO nodes may support building exhaust fan and heater controls via Allen-Bradley Flex5000. | DBM 3-25, line 804 |
| REQ-014-06-08 | Standby/emergency power continuity for accepted vendor loads shall be confirmed consistent with the LV standby generator basis on the LV MCC with transfer switch. | DBM 3-25, line 505 |
| REQ-014-06-09 | Environmental fitness of accepted vendor equipment shall be verified against the project low-temperature basis (-40 deg C minimum ambient) where exposed. | DBM 3-25, line 145 |
| REQ-014-06-10 | Acceptance shall not be issued before the EPC-side basis deliverables (DEL-014-01, DEL-014-02, DEL-014-03) reach a state permitting reliance. Specific maturity gate: TBD (no explicit gate stated in source). | ASSUMPTION; default maturity threshold from `_DEPENDENCIES.md` is `INITIALIZED` |

## Standards

| Standard / Reference | Applicability | Source |
|---|---|---|
| Project electrical specifications | Governs LV equipment acceptance criteria. | DBM 3-25, line 893 |
| CEC and area classification standards | Governs electrical safety and area-classification fitness checks. | DBM 3-25, line 893 |
| Voltage / MCC / grounding basis (DBM 3-25) | Governs vendor-equipment electrical compatibility checks. | DBM 3-25, line 893 |
| Code/standard clause-level requirements | location TBD; not extracted from accessible sources. | TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-014-06-01 | Review log inspection: completeness against vendor document register (DEL-014-05). |
| REQ-014-06-02 | Checklist traceability audit against DEL-014-01/02/03 entries. |
| REQ-014-06-03 | Examination of factory and site test/inspection records. |
| REQ-014-06-04 | Turnover dossier completeness review against DEL-014-05 register. |
| REQ-014-06-05 | Interface-by-interface verification against package interface matrix (DEL-014-02 evidence). |
| REQ-014-06-06 | Document review: voltage class, grounding scheme, and load category alignment with DBM electrical basis. |
| REQ-014-06-07 | I&C drawings/architecture check: vendor controls tie-in to Flex5000 RIO where applicable. |
| REQ-014-06-08 | Power continuity check: load attribution to LV MCC + standby generator scheme. |
| REQ-014-06-09 | Vendor environmental ratings review against -40 deg C minimum ambient. |
| REQ-014-06-10 | Status check of upstream EPC deliverables before acceptance issuance. |

## Documentation

Acceptance deliverable artifacts (per `_CONTEXT.md`):

- Vendor document review log.
- Package acceptance checklist (signed).
- Test/inspection evidence file.
- Turnover evidence file.

Supporting working records (recommended; ASSUMPTION):

- Review meeting minutes.
- Non-conformance / open-item log with disposition.
- Cross-reference matrix linking vendor documents to acceptance criteria.
