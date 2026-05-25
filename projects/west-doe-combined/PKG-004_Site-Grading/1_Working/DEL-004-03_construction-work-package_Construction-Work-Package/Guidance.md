# Guidance: DEL-004-03 Construction Work Package

## Purpose

The DEL-004-03 construction work package exists to convert the accepted PKG-004 Site Grading decomposition basis into a construction-facing package that can be installed, inspected, tied into adjacent systems, and turned over without losing the declared drainage, containment, grading, access, hydrology, and geotechnical constraints.

## Principles

- Use Gate 7 accepted snapshot rows as the package identity and deliverable boundary. Do not merge PKG-004 with the parallel Site Grading packages for WBS 01 or WBS 03.
- Treat the 3-25 DBM civil and construction sections as the source-grounded design basis for WBS 02 Site Grading until superseded by accepted later-phase documents.
- Keep Drain / Containment and Grading / Site Drainage / Spill Containment visible in the construction interface checklist; these are declared interfaces, not optional drafting detail.
- Treat hydrology and geotechnical inputs as maturity constraints. The current source set identifies proxy rainfall data and preliminary geotechnical basis, so IFC-ready construction closure requires later confirmation.
- Prefer explicit `TBD` over invented field quantities, elevations, slopes, drawing numbers, hold points, or sequence logic.

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| Package separation | PKG-004 is the Site Grading package for WBS 02 and must remain distinct from PKG-003 and PKG-005. | SCOPE_LEDGER.csv, SOW-0004 row; PACKAGE_REGISTER.csv, PKG-004 row |
| Workface planning | The workface plan should organize construction activities around grading, drainage, containment tie-ins, access, and turnover evidence, but detailed construction sequencing remains TBD without IFC inputs. | ARTIFACT_REGISTER.csv, DEL-004-03 rows; DBM Construction Scope Summary |
| Surface water | Surface-water controls should be checked for offsite discharge prevention, process-area protection, and construction/operations access. | DBM SEC-11 Surface Water and Drainage |
| Process-contaminated drainage | Do not allow process-contaminated drainage to be treated as ordinary surface-water discharge in the CWP checklist. | DBM SEC-11 Surface Water and Drainage |
| Roads and access | Grading work should preserve construction, module delivery, operations, maintenance, emergency response, and truck-loading access needs, including winter operation. | DBM SEC-11 Roads and Access |
| Hydrology maturity | Drainage and surface-water management should carry the proxy IDF basis as an assumption/open item until final hydrology is confirmed. | DBM SEC-02 Site-Specific Design Data |
| Geotechnical maturity | Final geotechnical report acceptance is a prerequisite for closed foundation-related grading criteria. | DBM SEC-02 Geotechnical and Seismic Basis; DBM SEC-11 Site and Civil Conditions |

## Trade-offs

| Trade-off | Guidance |
|---|---|
| Early CWP readiness vs. source fidelity | Issue a structured CWP shell with TBDs rather than delaying all package definition, but do not convert TBDs into construction criteria without accepted source evidence. |
| Workface detail vs. package boundary | Include enough workface structure to support installation and turnover, while keeping detailed crew means/methods, dates, and quantities TBD until construction planning inputs are available. |
| Drainage routing vs. surface-water simplicity | Preserve segregation of process-contaminated drainage from surface-water discharge even if routing details are not yet available. |
| Access optimization vs. winter design basis | Keep winter operation and -40 deg C basis visible when grading affects roads/access, even where final road geometry is TBD. |

## Examples

| Example item | Treatment |
|---|---|
| Interface checklist row for `Drain / Containment` | Include row with status, source `INTERFACE_REGISTER.csv IFC-FA26BF6895`, construction tie-in owner/status TBD, and turnover evidence required. |
| Interface checklist row for `Grading / Site Drainage / Spill Containment` | Include row with status, source `INTERFACE_REGISTER.csv IFC-D2D12F4CA2`, drainage/containment tie-in evidence required, and hydrology/geotechnical open items linked. |
| Unsupported grading quantity | Mark `TBD - no issued grading quantity in accessible Gate 7/DBM source set`. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-004-03-001 | `_CONTEXT.md` lists OBJ-010 as supported, while Gate 7 package/scope mapping for PKG-004/SOW-0004 lists OBJ-002, OBJ-007, OBJ-008, and OBJ-009; OBJECTIVE_DELIVERABLE_MAP also lists DEL-004-03 under OBJ-010. | `_CONTEXT.md`, Supports Objectives; OBJECTIVE_DELIVERABLE_MAP.csv row for OBJ-010 and DEL-004-03 | PACKAGE_REGISTER.csv PKG-004 row and SCOPE_LEDGER.csv SOW-0004 row | Datasheet Identification, Specification Scope/Documentation, Procedure Records | Treat OBJ-010 as deliverable-level handoff context for the construction work package, not as package-scope design authority, until PROJECT_DECOMP ownership clarifies objective granularity. | TBD |

