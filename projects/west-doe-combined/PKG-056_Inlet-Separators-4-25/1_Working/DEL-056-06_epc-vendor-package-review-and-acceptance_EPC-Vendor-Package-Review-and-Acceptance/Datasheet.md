# Datasheet: EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-056-06_epc-vendor-package-review-and-acceptance |
| Deliverable name | EPC Vendor Package Review and Acceptance |
| Parent package | PKG-056 - Inlet Separators 4-25 |
| Workbook ID / row | 56 / row 68 |
| WBS | 01 |
| CoA tracking number | 26020-01-17-004 |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| Responsible party | EPC Integrator (lead) with Package Vendor input |
| Covers scope items | SOW-0127; SOW-0128; SOW-0129; SOW-0130 |
| Supports objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 |

## Attributes

| Attribute | Current basis | Source |
|---|---|---|
| Deliverable role | EPC Integrator review and acceptance of the vendor package against the EPC Scope of Work, Package Datasheet, and Construction Work Package. | DELIVERABLE_REGISTER.csv, DEL-056-06 |
| Package description | Workbook-defined Mechanical package for Inlet Separators 4-25 under WBS 01, supplying two (2) identical horizontal three-phase separators. | PACKAGE_REGISTER.csv, PKG-056 |
| Responsibility split | Package Vendor owns package engineering, design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination. | PACKAGE_REGISTER.csv, PKG-056 |
| Vendor review evidence artifact | Vendor document review and comment log. | ARTIFACT_REGISTER.csv, ART-C28CAEBE71 |
| Acceptance evidence artifact | Vendor package acceptance and turnover checklist. | ARTIFACT_REGISTER.csv, ART-DBC56EA416 |
| Test/inspection evidence artifact | Factory/shop test and inspection evidence. | ARTIFACT_REGISTER.csv, ART-95970470BB |
| Source basis for review | EPC Scope of Work (DEL-056-01), Package Datasheet (DEL-056-02), Construction Work Package (DEL-056-03), Vendor Engineered Equipment Package (DEL-056-04), Vendor Document Turnover Package (DEL-056-05). | DELIVERABLE_REGISTER.csv, DEL-056-01..05 |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Equipment quantity | Two (2) installed horizontal three-phase HP inlet separators, each 9 ft ID x 40 ft S/S; plot space reserved for a third separator. Legacy four-package references preserved as unresolved. | 4-25_Deepcut_DBM.md, Inlet Separator Design Parameters |
| Process function | Receives raw inlet gas and separates into sour natural gas (vapour), sour raw condensate (light liquid), and sour water (heavy liquid). | PACKAGE_REGISTER.csv, PKG-056; 4-25_Deepcut_DBM.md, Inlet Separator narrative |
| Design pressure | 9,377 kPag per separator. | 4-25_Deepcut_DBM.md, Inlet Separator Design Parameters |
| Per-separator gas design rate | 125 to 150 MMSCFD; facility total unresolved between 300 MMSCFD and approximately 225 MMSCFD. | 4-25_Deepcut_DBM.md, Inlet Separator Design Parameters |
| Inlet design vapour total | 300 MMSCFD facility inlet design flow; inlet separator total design vapour flow 300 MMSCFD. | 4-25_Deepcut_DBM.md, Inlet Separator narrative |
| Slug capacity per separator | 31.8 m3 or 33.9 m3; human ruling required. | 4-25_Deepcut_DBM.md, Inlet Separator Design Parameters |
| Internal coating | Each inlet separator internally coated with Devchem 253; associated piping not internally coated. | 4-25_Deepcut_DBM.md, Inlet Separator construction |
| Internals | Manually adjustable weir; vertical high-performance mesh/vane mist eliminator (subject to operations review). | 4-25_Deepcut_DBM.md, Inlet Separator construction |
| Inlet PCV configuration | Minimum two parallel balanced-globe inlet PCVs per separator, hardened trim recommended, design dP <= 5 psid at design inlet pressure. | 4-25_Deepcut_DBM.md, Inlet Separator construction |
| Maintenance isolation | Outlet manual isolation permits PCV maintenance without full separator blowdown; skid-edge inlet isolation isolates inlet PCVs for maintenance. | 4-25_Deepcut_DBM.md, Inlet Separator construction |
| Liquid outlet heater | One liquid outlet heater per package; two HEX units at 04-25 under installed-separator basis; outlet temperature target and heat duty TBD pending process simulation; heating medium TBD. | 4-25_Deepcut_DBM.md, Inlet Separator narrative |
| Detailed vendor package requirements | TBD; 26020-Package_Requirements.docx heading 11 cited by decomposition but not locally accessible as text — location TBD. | _REFERENCES.md, Source Materials Referenced By Decomposition Row |

## Construction

| Item | Current basis | Source |
|---|---|---|
| Applicable interface — Process Piping | YES | INTERFACE_REGISTER.csv, IFC-C5833B2729 |
| Applicable interface — Utility Piping | YES | INTERFACE_REGISTER.csv, IFC-2E1ABE7C99 |
| Applicable interface — Relief / Flare / Vent | YES | INTERFACE_REGISTER.csv, IFC-A1023EBFAC |
| Applicable interface — Drain / Containment | YES | INTERFACE_REGISTER.csv, IFC-DE1036D554 |
| Applicable interface — EHT | YES | INTERFACE_REGISTER.csv, IFC-53DF92868E |
| Applicable interface — Grounding / Bonding | YES | INTERFACE_REGISTER.csv, IFC-70423EFFC2 |
| Applicable interface — Area / Exterior Lighting | YES | INTERFACE_REGISTER.csv, IFC-54942AAFDA |
| Applicable interface — I&C / Control Cabling | YES | INTERFACE_REGISTER.csv, IFC-C8EFDB103A |
| Applicable interface — Fire & Gas / Safety Systems | YES | INTERFACE_REGISTER.csv, IFC-666C085B26 |
| Applicable interface — Maintenance Access | YES | INTERFACE_REGISTER.csv, IFC-9626472DCC |
| Applicable interface — Structural / Foundations / Supports | YES | INTERFACE_REGISTER.csv, IFC-F7D66A2D0B |
| Inlet piping distribution | Inlet piping from rack to inlet separator packages shall account for normal gas/liquid distribution and minimize uneven distribution; piping symmetry; detailed distribution review during detailed engineering. | 4-25_Deepcut_DBM.md, Inlet Separator narrative |
| Methanol injection | May be required upstream of inlet separators for hydrate suppression during winter/shutdown cooling and line-pack start-up. | 4-25_Deepcut_DBM.md, Inlet Separator narrative |
| Spacing basis | Separators-to-flare 25 m (82 ft); separators-to-fired heater 25 m (82 ft). | 4-25_Deepcut_DBM.md, OGAOM Sec. 9.6.15 |

## References

- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx (heading 11; location TBD — not locally accessible as text)
