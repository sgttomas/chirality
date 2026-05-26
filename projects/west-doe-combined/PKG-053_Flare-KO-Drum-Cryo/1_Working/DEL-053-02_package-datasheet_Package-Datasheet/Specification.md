# Specification — DEL-053-02 Package Datasheet — Flare KO Drum (Cryo)

> Normative content. Clause-level requirements that depend on the binary `26020-Package_Requirements.docx` heading 8 slice are marked `TBD` (location TBD). ASSUMPTION labels surface inferences.

## Scope

This specification governs the **EPC Package Datasheet** for the Flare KO Drum (Cryo) package (PKG-053). It defines the technical data the EPC Integrator must hand off to a third-party Package Vendor for engineering and design of the cryogenic flare knock-out drum (V-4110-1) and its associated electric immersion heater (H-4112-1), supplied as a single equipment package (SOW-0068).

In scope:
- Identification, tagged equipment, service conditions, materials and mechanical basis, and interface battery-limit data required for vendor engineering handoff (per `ARTIFACT_REGISTER.csv` artifacts ART-4D31E29362, ART-D9D27FE028, ART-92CCADAD89, ART-6BD88EA2DC).
- Carriage of the nine PKG-053 interface facts (Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports) as datasheet evidence.

Out of scope:
- Vendor engineering and design execution (carried in DEL-053-04 Vendor Engineered Equipment Package).
- Construction work package and tie-in workface planning (DEL-053-03).
- Vendor document submittals and turnover records (DEL-053-05).
- EPC vendor package review and acceptance (DEL-053-06).
- Package-level exclusions: TBD; no package-specific exclusions stated in source materials (`PACKAGE_REGISTER.csv` row PKG-053).

## Requirements

### R-DS-01 — Package Identification (source-grounded)
The datasheet shall identify the package as Flare KO Drum (Cryo), PKG-053, CoA tracking number `26020-01-PT-17-001 - Flare KO Drum (Cryo)`, WBS 01, Discipline Mechanical.
Source: `PACKAGE_REGISTER.csv` row PKG-053; `_CONTEXT.md`.

### R-DS-02 — Tagged Equipment (source-grounded)
The datasheet shall list V-4110-1 (Cryogenic Flare KO Drum) and H-4112-1 (Electric Immersion Heater) as the major included equipment supplied as a single package.
Source: `26020-Package_Requirements.docx` heading 8 — Major included equipment (location TBD as binary); corroborated by `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Tagged-Equipment table; SOW-0068, SOW-0069.

### R-DS-03 — Service Basis (source-grounded)
The datasheet shall state the drum serves cryogenic-unit reliefs and molecular-sieve-dehydrated systems with PSVs relieving below -45.5 deg C, and shall classify the service as non-sour per the project brief.
Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Flare Systems table; SOW-0070.

### R-DS-04 — Relief Header and Downstream Routing (source-grounded)
The datasheet shall note the associated 610 mm (24 in) cryogenic relief header inlet and the downstream routing in which the cryogenic header combines with the HP flare header downstream of both KO drums before discharge to the common HP/cryo flare stack.
Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Flare Systems table.

### R-DS-05 — Design Conditions
The datasheet shall publish drum design pressure, drum design temperature (min/max), orientation, geometry, internals (demister, vortex breaker, baffles), and nozzle schedule.
Source: `26020-Package_Requirements.docx` heading 8 — design conditions (location TBD; binary). Values TBD pending source slice.

### R-DS-06 — Pressure-Vessel Code and Materials
The datasheet shall identify the governing pressure-vessel design code and material classes appropriate for cryogenic service.
ASSUMPTION: ASME BPVC Section VIII (Division 1 or 2) and low-temperature impact-tested materials (e.g., low-temperature carbon steel, 3.5 Ni, 9 Ni, or austenitic stainless) are likely applicable given the < -45.5 deg C duty. Values and code edition TBD pending source slice.

### R-DS-07 — Electric Immersion Heater Basis
The datasheet shall publish the duty (kW), sheath material, electrical class, area classification, and control philosophy for H-4112-1.
Source: `26020-Package_Requirements.docx` heading 8 (location TBD; binary). Values TBD.

### R-DS-08 — Interface Battery Limits (carried as evidence)
The datasheet shall carry, for each of the nine declared interfaces below, the battery-limit data required for third-party engineering and design handoff:
- Process Piping (IFC-705A2F4958)
- Relief / Flare / Vent (IFC-389D987465)
- Drain / Containment (IFC-2D41AA86C9)
- Electrical Power (IFC-2EA8D3CAE2)
- EHT (IFC-198E1B696B)
- Grounding / Bonding (IFC-19B7425129)
- I&C / Control Cabling (IFC-4CD44C8D3A)
- Maintenance Access (IFC-3AD0CD340A)
- Structural / Foundations / Supports (IFC-A0F9C88368)

Per-interface detail (nozzle sizes, ratings, set points, cable schedules, foundation reactions, access envelopes) is TBD pending source slice (`26020-Package_Requirements.docx` heading 8 and `26020-Packages_Interfaces_4_export.xlsx`).

### R-DS-09 — Modularization Form
The datasheet shall record the package's planned form as a shop-fabricated module: "410-1 HP / Cryo Flare KO Drum Module — Shop".
Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Modularization table.

### R-DS-10 — Responsibility Boundary
The datasheet shall reflect the responsibility split: Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration, tie-ins, constructability, and procurement/construction coordination.
Source: `PACKAGE_REGISTER.csv` row PKG-053; ART-FC3EEE4D5E.

## Standards

| Standard | Applicability | Status |
|---|---|---|
| ASME BPVC Section VIII | Pressure vessel design code (drum V-4110-1) | ASSUMPTION; location TBD |
| ASME B16.5 / B16.47 | Nozzle flange ratings | ASSUMPTION; location TBD |
| API 521 | Pressure-relieving and depressuring systems (flare system context) | ASSUMPTION; location TBD |
| API 526 / 527 | PSV selection / seat tightness (system context) | ASSUMPTION; location TBD |
| API 537 / 521 | Flare details (system context, not in PKG-053 scope) | Context only |
| NACE MR0175 / ISO 15156 | Sour service materials | Not applicable per SOW-0070 (non-sour) |
| Project EHT specification | Heat tracing on insulated cryogenic surfaces | Location TBD |
| Project electrical area classification | H-4112-1 electrical class | Location TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-DS-01 / R-DS-02 / R-DS-10 | Document review against `PACKAGE_REGISTER.csv` and `_CONTEXT.md` |
| R-DS-03 / R-DS-04 / R-DS-09 | Document review against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| R-DS-05 / R-DS-06 / R-DS-07 | Vendor-returned datasheet completeness check; clause-by-clause source reread against `26020-Package_Requirements.docx` heading 8 when slice is accessible |
| R-DS-08 | Interface matrix completeness check against `INTERFACE_REGISTER.csv` (9 of 9 PKG-053 rows); per-interface attribute completeness check |

## Documentation

Expected EPC datasheet artifact set per `ARTIFACT_REGISTER.csv` (DEL-053-02):
- ART-4D31E29362 Package technical datasheet
- ART-D9D27FE028 Vendor engineering handoff basis
- ART-92CCADAD89 Package interface requirements matrix
- ART-6BD88EA2DC Major included equipment evidence
- ART-C990BE80EE / ART-F1E566161F / ART-F70A5F3C35 / ART-055AE18021 / ART-AFB9D70FCD / ART-16C4579DB2 / ART-F9CB2FE63B / ART-EEB15A33C3 / ART-4B8E08B832 (nine interface-fact evidence rows)
