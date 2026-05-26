# Datasheet: EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-083-06_epc-vendor-package-review-and-acceptance |
| Deliverable name | EPC Vendor Package Review and Acceptance |
| Parent package | PKG-083 - Inlet Separators 3-25 |
| Workbook ID / row | 83 / row 67 |
| WBS | 02 |
| CoA tracking number | 26020-02-17-003 |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| Responsible party | EPC Integrator (lead) with Package Vendor input |
| Covers scope items | SOW-0123; SOW-0124; SOW-0125; SOW-0126 |
| Supports objectives | OBJ-002; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: package-grouped objective mapping) |

## Attributes

| Attribute | Current basis | Source |
|---|---|---|
| Deliverable intent | EPC Integrator review, integration acceptance, and handoff readiness evidence for the Inlet Separators vendor package against the EPC Scope of Work, Package Datasheet, and Construction Work Package. | DELIVERABLE_REGISTER.csv, DEL-083-06 |
| Acceptance evidence type | EPC review and acceptance evidence framed as a Gate 5 additional deliverable. | DELIVERABLE_REGISTER.csv, DEL-083-06 notes |
| Vendor scope under review | Package engineering, package design, vendor documentation, and the physical equipment package for two identical horizontal three-phase inlet separators. | PACKAGE_REGISTER.csv, PKG-083 |
| EPC scope under acceptance | Integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | PACKAGE_REGISTER.csv, PKG-083 |
| Equipment tags in scope | V-1600-2 and V-1700-2 (two identical horizontal three-phase inlet separator packages, each 50% of facility capacity). | 3-25_Comp_and_Liquids_DBM.md, Inlet Separation |
| Anticipated artifact - review log | Vendor document review and comment log (ART-AE2840AE44). | ARTIFACT_REGISTER.csv, DEL-083-06 |
| Anticipated artifact - acceptance checklist | Vendor package acceptance and turnover checklist (ART-27FC8B869F). | ARTIFACT_REGISTER.csv, DEL-083-06 |
| Anticipated artifact - test/inspection evidence | Factory/shop test and inspection evidence (ART-30486BD773). | ARTIFACT_REGISTER.csv, DEL-083-06 |
| Anticipated artifact - turnover evidence | Turnover evidence captured within the acceptance/turnover checklist set. | _CONTEXT.md, Anticipated Artifacts |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Site ambient minimum | -40 deg C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe process or vendor condition applies; acceptance must verify vendor package compliance with the site cold-climate basis. | 3-25_Comp_and_Liquids_DBM.md, Site Basis |
| Service classification | Sour service: sour natural gas, sour raw condensate, sour water. | PACKAGE_REGISTER.csv, PKG-083; 3-25_Comp_and_Liquids_DBM.md, Inlet Separation |
| Separator design basis (per separator) | Gas flow 40 MMSCFD; condensate flow 556 m3/d (3,494 bbl/d); produced water 1,800 m3/d (11,322 bbl/d); diameter 2,743 mm (9 ft); straight-side length 12,191 mm (40 ft); pressure class 600#; design pressure 4,963 kPag; slug handling approximately 38 m3; internal coating Devchem 253. | 3-25_Comp_and_Liquids_DBM.md, Inlet Separation |
| Inlet pressure envelope | Low operating 125 psig; design operating 200 psig; maximum 572 psig; normal high TBC. | 3-25_Comp_and_Liquids_DBM.md, Inlet Separation |
| Inlet design temperature | 8.3 deg C per current feed data; downstream excerpts require confirmation; detailed design shall reconcile inlet temperature basis before final datasheet issuance. | 3-25_Comp_and_Liquids_DBM.md, Inlet Separation |
| Inlet ESDV shutdown pressure | 635 psig at the inlet separator ESDV (current basis). | 3-25_Comp_and_Liquids_DBM.md, Pig Receiver and ESDV |
| Building enclosure | Instrumentation and one end of each package enclosed in a heated self-framing building; exact building extent TBD by vendor design. | 3-25_Comp_and_Liquids_DBM.md, Inlet Separation |

## Construction

| Item | Current basis | Source |
|---|---|---|
| Package boundary | Vendor delivers a self-contained mechanical package; EPC integrates into the facility at defined interface boundaries. | PACKAGE_REGISTER.csv, PKG-083 |
| Applicable interface types | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | PACKAGE_REGISTER.csv, PKG-083 |
| Required package deliverables | Datasheets; cause-and-effect inputs; utility load summaries; relief/load data; field tie-in lists; operating and design envelopes; sparing philosophy; materials and coating basis; maintenance access; shipped-loose item lists; vendor document registers. | 3-25_Comp_and_Liquids_DBM.md, Mechanical Packages |
| Internals/equipment features to verify | Devchem 253 coating; manually adjustable weir; vertical/horizontal high-performance mesh/vane mist eliminators; de-sanding provisions; piping not coated under current basis. | 3-25_Comp_and_Liquids_DBM.md, Inlet Separation |
| Flow distribution and controls | Symmetric inlet piping; drive-gas recycle from downstream inlet compressor aftercoolers returns to separators; at least two parallel inlet pressure-control valves per package with balanced globe hardened trim and dP limit <= 5 psid; at least two parallel produced-water level-control valves per package. | 3-25_Comp_and_Liquids_DBM.md, Flow Distribution and Controls |
| Slug/flowback acceptance basis | Slug handling 38 m3 per separator; frac flowback governs transient liquid case; operator shall manage pigging/flowback to remain within downstream 04-25 stabilization capacity (approximately 6 hours processing). | 3-25_Comp_and_Liquids_DBM.md, Slug and Flowback Basis |
| Methanol disposition | Methanol expected to drain at inlet separator boot; downstream methanol disposition remains TBD. | 3-25_Comp_and_Liquids_DBM.md, Inlet Separation |
| Test and inspection evidence scope | TBD — detailed FAT/inspection requirements not located in current accessible sources; to be defined by the Vendor Engineered Equipment Package (DEL-083-04) and Package Datasheet (DEL-083-02). | TBD |
| Turnover evidence scope | TBD — to be defined relative to the Vendor Document Turnover Package (DEL-083-05) at handoff. | TBD |

## References

- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md
- 26020-Package_Requirements.docx, package heading 36 (location TBD; .docx not locally readable as text)
