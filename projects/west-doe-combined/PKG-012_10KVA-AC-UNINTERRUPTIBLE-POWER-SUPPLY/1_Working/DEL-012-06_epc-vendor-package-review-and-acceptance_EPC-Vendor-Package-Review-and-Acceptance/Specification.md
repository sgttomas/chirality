# Specification: EPC Vendor Package Review and Acceptance

## Scope

This specification covers the EPC Integrator deliverable for review, acceptance, and handoff readiness of the PKG-012 10KVA AC UNINTERRUPTIBLE POWER SUPPLY vendor package.

The deliverable covers:

- EPC review evidence for vendor documentation and integration requirements.
- Acceptance and turnover evidence for facility integration.
- Factory/shop test and inspection evidence where available.
- Confirmation that declared electrical, grounding/bonding, maintenance access, and structural/foundation/support interfaces have been addressed or carried as open items.

The deliverable excludes:

- Vendor-owned package engineering, package design, vendor documentation generation, and physical equipment supply except as reviewed by the EPC Integrator.
- Package-specific exclusions not stated in Gate 7; these remain TBD.

Sources: DELIVERABLE_REGISTER.csv row DEL-012-06; PACKAGE_REGISTER.csv row PKG-012; ARTIFACT_REGISTER.csv rows for DEL-012-06; INTERFACE_REGISTER.csv rows for PKG-012.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-012-06-001 | The deliverable shall identify PKG-012 as a vendor-responsible Electrical package for the 10KVA AC UNINTERRUPTIBLE POWER SUPPLY under WBS 02. | Check package identity against PACKAGE_REGISTER.csv row PKG-012 and SCOPE_LEDGER.csv row SOW-0013. |
| REQ-012-06-002 | The deliverable shall preserve the responsibility split: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment; EPC Integrator owns facility integration and interfaces. | Review responsibility statements against PACKAGE_REGISTER.csv row PKG-012 and SCOPE_LEDGER.csv row SOW-0013. |
| REQ-012-06-003 | The deliverable shall include or reference a vendor document review and comment log. | Confirm artifact corresponding to ART-627ADF1B97 is present or explicitly marked TBD/open. |
| REQ-012-06-004 | The deliverable shall include or reference a vendor package acceptance and turnover checklist. | Confirm artifact corresponding to ART-4925F002F5 is present or explicitly marked TBD/open. |
| REQ-012-06-005 | The deliverable shall include or reference factory/shop test and inspection evidence when available. | Confirm artifact corresponding to ART-2736623A0D is present or explicitly marked TBD/open. |
| REQ-012-06-006 | The deliverable shall address the accepted interface types for PKG-012: Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports. | Cross-check against INTERFACE_REGISTER.csv rows IFC-AA089340E0, IFC-2F50872E45, IFC-52E7E27E87, IFC-1D40B1F072. |
| REQ-012-06-007 | The deliverable shall document open acceptance items, missing evidence, and unresolved interface issues instead of implying closure without evidence. | Review checklist, log, and turnover sections for open-item disposition. |
| REQ-012-06-008 | The deliverable shall remain aligned to objectives OBJ-002, OBJ-004, OBJ-005, OBJ-008, OBJ-009, and OBJ-010 as directional context, not as substitute source criteria. | Confirm objective IDs match OBJECTIVE_DELIVERABLE_MAP.csv rows for DEL-012-06. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Gate 7 final published PROJECT_DECOMP snapshot | Accepted upstream decomposition truth for package identity, responsibility split, artifacts, interfaces, and objectives. | Available locally. |
| EPC Scope of Work | Acceptance basis named for this deliverable. | Detailed source slice TBD. |
| Package Datasheet | Acceptance basis named for this deliverable. | Detailed source slice TBD. |
| Construction Work Package | Acceptance basis named for this deliverable. | Detailed source slice TBD. |
| Project electrical codes/standards | Likely relevant to electrical package acceptance. | ASSUMPTION; clause-level requirements TBD because no deliverable-specific code source slice was copied into the assigned folder. |

## Verification

Verification shall confirm:

1. The review package identifies the correct package, WBS, scope item, deliverable ID, responsible parties, and accepted Gate 7 snapshot.
2. Vendor documents have been reviewed with comments, holds, and dispositions recorded.
3. Acceptance checklist items are either accepted, rejected, open, not applicable, or TBD with a named basis.
4. Test and inspection evidence is present or explicitly missing/open.
5. Each declared interface type is reviewed for integration acceptance or carried as an open item.
6. Turnover evidence supports facility handoff readiness and does not close unresolved items by implication.

## Documentation

Required or expected records:

- Vendor document review and comment log.
- Vendor package acceptance and turnover checklist.
- Factory/shop test and inspection evidence.
- Open-item and exception register, if not embedded in the acceptance checklist.
- Interface acceptance notes for Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports.
- Turnover evidence for EPC facility integration.
