# Datasheet: DEL-081-01 — Scope of Work (PKG-081 Flare KO Drum (High Pressure) 3-25)

> Descriptive datasheet for the EPC Integrator-authored Scope of Work for package PKG-081. Values are limited to those explicitly supported by accessible source materials and the Gate-7 PROJECT_DECOMP snapshot. Unsupported items are marked `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-081-01_scope-of-work` | `_CONTEXT.md` Identity table; `DELIVERABLE_REGISTER.csv` row for DEL-081-01 |
| Deliverable Name | Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent Package ID | `PKG-081` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Parent Workbook Row | 54 | `PACKAGE_REGISTER.csv` (workbook row column); `_CONTEXT.md` Source Reference |
| Package Name | Flare KO Drum (High Pressure) 3-25 | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| WBS | 02 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-02-17-001 | `PACKAGE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Items | `SOW-0071`, `SOW-0072`, `SOW-0073`, `SOW-0074` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (PACKAGE_HEURISTIC, ASSUMPTION) | `OBJECTIVE_DELIVERABLE_MAP.csv`; brief `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC` |

## Attributes

### Tagged Major Equipment (package basis)

| Tag | Description | Source |
|---|---|---|
| V-4100-2 | HP Flare KO Drum located in the 03-25 compressor area; receives HP relief header flow | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-07 (HP flare basis paragraph) |
| V-4150-2 | HP Flare KO Drum located in the 03-25 tank farm; receives HP relief header flow | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-07 |
| P-4100-2 | HP Flare KO Drum transfer pump dedicated to V-4100-2; truck-out / transfer to slop | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-07; SEC-09 sparing table |
| P-4150-2 | HP Flare KO Drum transfer pump dedicated to V-4150-2; truck-out / transfer to slop | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-07; SEC-09 sparing table |

### Package Function (descriptive)

| Attribute | Value | Source |
|---|---|---|
| Service | Sour HP flare relief liquid knockout and liquid transfer to slop | DBM SEC-07 (HP flare basis) |
| Service Class | Sour hydrocarbon (HP relief) | DBM SEC-07; SEC-09 isolation philosophy (sour-service text) |
| Quantity (KO drums) | 2 (V-4100-2, V-4150-2) | SCOPE_LEDGER `SOW-0073`; DBM SEC-07 |
| Quantity (transfer pumps) | 2, dedicated (one per drum), 1 x 100 percent each | SCOPE_LEDGER `SOW-0072`; DBM SEC-09 sparing row "HP flare KO drum transfer pumps" |
| Manifold | Both KO drums manifold to the HP flare | DBM SEC-07 |
| HP Relief Header Size | 508 mm / 20 inch (current source basis) | DBM SEC-07 |
| Flare Stack | HP/Cryo and LP dual flare stack; sonic HP/Cryo stack 660 mm OD x 60,957 mm tall; stack is shared with 04-25 | DBM SEC-07 |

### Conditions

| Attribute | Value | Source |
|---|---|---|
| Site location | LSD 03-25-80-15 W6M, north of Dawson Creek, BC | DBM SEC-02 |
| Site elevation | 673 m AMSL | DBM SEC-02 |
| Sour service applicability | YES (sour hydrocarbon relief) | DBM SEC-09 (sour-service isolation text); SEC-07 |
| Operating pressures, temperatures, relief loads (per-vessel) | TBD — not stated for V-4100-2 / V-4150-2 in accessible sources | location TBD; package-specific datasheet covered by DEL-081-02 |
| Blowdown sequencing | Staggered blowdown required; final sequencing relies on external Plant Shutdown and Blowdown Philosophy `W242510-PRC-REP-000003-001` (not locally accessible) | DBM SEC-07 |

### Construction (descriptive)

| Attribute | Value | Source |
|---|---|---|
| Procurement model | Vendor-engineered, vendor-designed, vendor-supplied package with EPC Integrator integration | `PACKAGE_REGISTER.csv` description; `OBJ-004` register entry |
| EPC scope (this deliverable) | Authored by EPC Integrator; describes package scope, function, tagged equipment, source basis, boundaries, and facility integration narrative | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row |
| Construction support scope | Civil/structural/site/grading/foundations/access supplied at facility level by EPC scope per `OBJ-008` (package-heuristic); package-local construction handled by DEL-081-03 | `OBJ-008` register row; `ARTIFACT_REGISTER.csv` mapping |
| Active facility-level interface types | Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` (10 rows for PKG-081) |

### Anticipated Artifacts (this deliverable)

| Artifact ID | Title | Source |
|---|---|---|
| ART-3A59CA7249 | Package scope of work | `ARTIFACT_REGISTER.csv` |
| ART-531950B8A7 | Tagged equipment and package identity list | `ARTIFACT_REGISTER.csv` |
| ART-8045E643FB | Package function and whole-facility integration narrative | `ARTIFACT_REGISTER.csv` |
| ART-00ABFE7374 | Package responsibility assignment record | `ARTIFACT_REGISTER.csv` |
| ART-F37B133BFD | Detailed mechanical package scope extraction evidence | `ARTIFACT_REGISTER.csv` |

## References

- `_CONTEXT.md` — deliverable identity and scope
- `_REFERENCES.md` — full reference set
- GATE-07 PROJECT_DECOMP snapshot registers: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `OBJECTIVE_REGISTER.csv`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-01 Exclusions; SEC-02 Site; SEC-07 HP flare basis; SEC-09 sparing/isolation)
- `_Sources/26020-Package_Requirements.docx` package heading 34 — referenced by registers; binary docx not converted to markdown in workspace, so clause-level extraction is `location TBD`
- External: `W242510-PRC-REP-000003-001` Plant Shutdown and Blowdown Philosophy — not locally accessible; `location TBD`
