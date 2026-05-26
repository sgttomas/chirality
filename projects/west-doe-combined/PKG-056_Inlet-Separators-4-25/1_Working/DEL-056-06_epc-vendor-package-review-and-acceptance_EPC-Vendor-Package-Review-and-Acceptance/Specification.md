# Specification: EPC Vendor Package Review and Acceptance

## Scope

This specification governs the DEL-056-06 EPC Vendor Package Review and Acceptance deliverable for PKG-056 Inlet Separators 4-25. The deliverable is the EPC Integrator's review-and-acceptance evidence set against the vendor package supplied for two installed horizontal three-phase HP inlet separators (plus future plot provision).

In scope: vendor document review log, vendor package acceptance and turnover checklist, factory/shop test and inspection evidence, and integration acceptance against the EPC Scope of Work (DEL-056-01), Package Datasheet (DEL-056-02), and Construction Work Package (DEL-056-03).

Out of scope: vendor package engineering, design, fabrication, and vendor documentation production itself (carried by DEL-056-04 and DEL-056-05); detailed civil/structural/electrical discipline production (carried by separate discipline production-package deliverables, if any); and any final values that depend on inputs unresolved in the current source set.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-056-06-001 | The acceptance evidence set shall identify DEL-056-06 against PKG-056 (Inlet Separators 4-25), WBS 01, CoA 26020-01-17-004, Mechanical discipline. | PACKAGE_REGISTER.csv, PKG-056; DELIVERABLE_REGISTER.csv, DEL-056-06 | Check identity table against Gate 7 registers. |
| REQ-056-06-002 | The EPC Integrator shall produce a vendor document review and comment log covering vendor package submittals against the EPC Scope of Work, Package Datasheet, and Construction Work Package. | ARTIFACT_REGISTER.csv, ART-C28CAEBE71; DELIVERABLE_REGISTER.csv, DEL-056-06 | Review log exists, references vendor submittals, and traces comments to source basis. |
| REQ-056-06-003 | The EPC Integrator shall produce a vendor package acceptance and turnover checklist that records integration acceptance and handoff readiness. | ARTIFACT_REGISTER.csv, ART-DBC56EA416 | Acceptance checklist exists; each item has accept/reject status and traceable evidence. |
| REQ-056-06-004 | The acceptance evidence shall include factory/shop test and inspection evidence for the supplied separators. | ARTIFACT_REGISTER.csv, ART-95970470BB | Test/inspection reports captured; deviations resolved or flagged. |
| REQ-056-06-005 | Review shall cover the eleven applicable workbook interface types for PKG-056: Process Piping, Utility Piping, Relief / Flare / Vent, Drain / Containment, EHT, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Fire & Gas / Safety Systems, Maintenance Access, and Structural / Foundations / Supports. | INTERFACE_REGISTER.csv, PKG-056 rows | Interface matrix in acceptance package lists all eleven interfaces with vendor-EPC resolution status. |
| REQ-056-06-006 | Vendor package equipment quantity shall be verified as two (2) installed horizontal three-phase HP inlet separators, each 9 ft ID x 40 ft S/S, with plot space reserved for a third separator; the legacy four-package reference shall be preserved as unresolved unless a human ruling closes it. | 4-25_Deepcut_DBM.md, Inlet Separator Design Parameters | Quantity verification record and open-conflict log. |
| REQ-056-06-007 | Vendor mechanical design pressure shall be verified at 9,377 kPag per separator. | 4-25_Deepcut_DBM.md, Inlet Separator Design Parameters | Design pressure check against vendor data sheet. |
| REQ-056-06-008 | Vendor capacity submittal shall be reviewed against per-separator gas design rate of 125 to 150 MMSCFD with facility total carried as unresolved between 300 MMSCFD and approximately 225 MMSCFD until human ruling. | 4-25_Deepcut_DBM.md, Inlet Separator Design Parameters | Capacity review entry in review log; conflict carried to ruling list. |
| REQ-056-06-009 | Vendor slug capacity submittal shall be reviewed against the unresolved per-separator slug capacity of 31.8 m3 or 33.9 m3 and shall flag the open ruling. | 4-25_Deepcut_DBM.md, Inlet Separator Design Parameters | Slug capacity verification entry and open-ruling reference. |
| REQ-056-06-010 | Vendor internal coating submittal shall be verified as Devchem 253 on each separator; associated piping shall not be internally coated. | 4-25_Deepcut_DBM.md, Inlet Separator construction | Coating data sheet review entry. |
| REQ-056-06-011 | Vendor internals submittal shall include a manually adjustable weir and a vertical high-performance mesh/vane mist eliminator; mist eliminator selection shall be subject to operations review. | 4-25_Deepcut_DBM.md, Inlet Separator construction | Internals review entry; operations review record. |
| REQ-056-06-012 | Inlet pressure control valve submittal shall verify at minimum two parallel balanced-globe inlet PCVs per separator with hardened trim recommended and design dP <= 5 psid at design inlet pressure. | 4-25_Deepcut_DBM.md, Inlet Separator construction | PCV data sheet review entry. |
| REQ-056-06-013 | Maintenance isolation submittal shall verify outlet manual isolation that permits PCV maintenance without full separator blowdown and skid-edge inlet isolation for inlet PCV maintenance. | 4-25_Deepcut_DBM.md, Inlet Separator construction | Isolation philosophy review entry. |
| REQ-056-06-014 | Liquid outlet heater submittal shall be reviewed with target outlet temperature, heat duty, and heating medium carried as TBD pending process simulation and medium selection. | 4-25_Deepcut_DBM.md, Inlet Separator narrative | Heater submittal review entry; TBD log. |
| REQ-056-06-015 | Inlet piping/distribution submittal shall be reviewed for accounting for normal gas/liquid distribution to each separator and minimization of uneven distribution, with detailed distribution review carried to detailed engineering. | 4-25_Deepcut_DBM.md, Inlet Separator narrative | Inlet piping review entry. |
| REQ-056-06-016 | Hydrate-suppression methanol injection upstream of the inlet separators shall be considered during winter/shutdown cooling and line-pack start-up review. | 4-25_Deepcut_DBM.md, Inlet Separator narrative | Methanol provisions review entry. |
| REQ-056-06-017 | Spacing acceptance shall confirm separator-to-flare and separator-to-fired-heater distances of 25 m (82 ft) per OGAOM Sec. 9.6.15. | 4-25_Deepcut_DBM.md, OGAOM Sec. 9.6.15 | Spacing acceptance entry. |
| REQ-056-06-018 | Detailed vendor package requirements from 26020-Package_Requirements.docx heading 11 shall be carried as TBD content (location cited; text not locally accessible) until the source slice is brought into the deliverable's accessible source set. | _REFERENCES.md, Source Materials Referenced By Decomposition Row | Open source-input log lists this gap. |
| REQ-056-06-019 | The acceptance evidence set shall not infer requirements, design values, or test/inspection acceptance criteria from decomposition prose when the actual source text is not locally accessible. | SKILL.md (four-documents) non-negotiable constraints; _REFERENCES.md, Missing / Deferred References | Reviewer confirms no inferred requirements lack source citations. |
| REQ-056-06-020 | Status promotion beyond INITIALIZED shall require accepted upstream evidence from DEL-056-01..05 and human ruling closure of the unresolved conflicts listed in Guidance.md. | _STATUS.md; Guidance.md Conflict Table | Status change record. |

## Standards

| Standard / basis | Application | Source |
|---|---|---|
| OGAOM Sec. 9.6.15 | Spacing of separators from flare and fired heaters. | 4-25_Deepcut_DBM.md, plant spacing |
| 26020-Package_Requirements.docx package heading 11 | Detailed vendor package requirements specific to Inlet Separators (location TBD; not locally accessible as text). | _REFERENCES.md; PACKAGE_REGISTER.csv, PKG-056 |
| Project DBM (Deepcut 4-25) Inlet Separator section | Mechanical/process basis for the inlet separator scope. | 4-25_Deepcut_DBM.md |

## Verification

| Verification item | Acceptance basis |
|---|---|
| Identity verification | Matches Gate 7 PACKAGE_REGISTER.csv and DELIVERABLE_REGISTER.csv entries for PKG-056 / DEL-056-06. |
| Vendor document review log check | Log exists, references vendor submittals, and traces comments to source-grounded basis. |
| Acceptance checklist check | Acceptance and turnover checklist captures every applicable interface and source-grounded requirement; each item has status and evidence. |
| Test/inspection evidence check | Factory/shop test and inspection records cover supplied separators and resolve or flag deviations. |
| Interface coverage check | All eleven PKG-056 interface types are addressed in the acceptance package. |
| Conflict closure check | Open quantity, capacity, and slug-capacity conflicts are carried to the Conflict Table and not silently closed. |
| Source-grounding check | Each non-trivial requirement cites a register row or a DBM source slice; items dependent on the inaccessible docx are marked TBD. |
| Cross-document consistency check | Datasheet, Specification, Guidance, and Procedure use consistent identifiers, interface labels, and source basis. |

## Documentation

The acceptance evidence set should include, at minimum:

- Vendor document review and comment log (ART-C28CAEBE71).
- Vendor package acceptance and turnover checklist (ART-DBC56EA416).
- Factory/shop test and inspection evidence (ART-95970470BB).
- Interface matrix covering the eleven PKG-056 interface types with vendor-EPC resolution status.
- Open-conflict log for the quantity, capacity, and slug-capacity conflicts carried from the Deepcut DBM.
- Source-input log identifying the inaccessible 26020-Package_Requirements.docx heading 11 slice and any other deferred references.
- Integration acceptance record linking review evidence to DEL-056-01..05.
