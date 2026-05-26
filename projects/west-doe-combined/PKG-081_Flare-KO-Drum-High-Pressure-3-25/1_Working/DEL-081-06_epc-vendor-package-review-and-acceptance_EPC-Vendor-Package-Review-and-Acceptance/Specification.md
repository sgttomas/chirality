# Specification: DEL-081-06 — EPC Vendor Package Review and Acceptance

## Scope

### In Scope

The EPC Integrator shall perform vendor package review, integration acceptance, and handoff readiness against:

- the EPC Scope of Work for PKG-081 (DEL-081-01),
- the EPC Package Datasheet for PKG-081 (DEL-081-02), and
- the EPC Construction Work Package for PKG-081 (DEL-081-03).

The vendor scope under review is the Package Vendor's engineering, design, vendor documentation, and physical equipment package for the Flare KO Drum (High Pressure) 3-25 package, comprising two HP flare KO drums (V-4100-2, V-4150-2), two dedicated transfer pumps (P-4100-2, P-4150-2), liquid transfer to the condensate slop tank, truck-out provision, and the package interfaces. (Sources: `DELIVERABLE_REGISTER.csv` DEL-081-06; `SCOPE_LEDGER.csv` SOW-0072, SOW-0073; `PACKAGE_REGISTER.csv` PKG-081.)

The deliverable covers SOW-0071, SOW-0072, SOW-0073, and SOW-0074, and supports OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010. (Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` DEL-081-06.)

### Exclusions

- Vendor-internal engineering and design decisions, vendor document authoring, and physical equipment fabrication remain owned by the Package Vendor; they are reviewed, not produced, by this deliverable. (Source: `PACKAGE_REGISTER.csv` PKG-081 Responsibility Model; `OBJECTIVE_REGISTER.csv` OBJ-004.)
- No package-specific exclusions stated in source materials beyond the scope-conflict open item at SOW-0074. (Source: `PACKAGE_REGISTER.csv` PKG-081 Exclusions field: "TBD; no package-specific exclusions stated in source materials.")

## Requirements

### R-1 — Review against EPC acceptance basis (mandatory)

The EPC Integrator shall verify that the vendor package satisfies the EPC SOW (DEL-081-01), Package Datasheet (DEL-081-02), and Construction Work Package (DEL-081-03), and shall record evidence in a Package Acceptance Checklist. (Source: `DELIVERABLE_REGISTER.csv` DEL-081-06 description; `_CONTEXT.md` Scope.)

### R-2 — Responsibility split preserved

Acceptance shall preserve the documented responsibility split: Package Vendor owns engineering, design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. (Source: `PACKAGE_REGISTER.csv` PKG-081 Responsibility Model; `OBJECTIVE_REGISTER.csv` OBJ-004.)

### R-3 — Interface review coverage

Acceptance shall review and record evidence for every interface category declared for PKG-081:

- Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports.

(Source: `INTERFACE_REGISTER.csv` PKG-081 rows; `PACKAGE_REGISTER.csv` PKG-081 Applicable Interface Types.)

### R-4 — Vendor document register review

The EPC Integrator shall review the Vendor Document Turnover Package (DEL-081-05) for completeness, comment resolution, and turnover readiness, and shall maintain a Vendor Document Review Log. (Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` DEL-081-06; `OBJECTIVE_REGISTER.csv` OBJ-010.)

### R-5 — Vendor engineered equipment package review

The EPC Integrator shall review the Vendor Engineered Equipment Package (DEL-081-04) for conformance to the EPC acceptance basis (R-1) and capture inspection/test evidence. (Source: `DELIVERABLE_REGISTER.csv` DEL-081-04, DEL-081-06.)

### R-6 — Safety, sour-service, and regulatory carry-through

Acceptance shall confirm that sour-service, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, emissions, regulatory, codes, and standards requirements have been carried into the vendor package and its interfaces. (Source: `OBJECTIVE_REGISTER.csv` OBJ-009.)

### R-7 — Operability, maintainability, sparing, turnover

Acceptance shall confirm operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, and controlled open-item closure evidence are present and adequate for downstream facility handoff. (Source: `OBJECTIVE_REGISTER.csv` OBJ-010.)

### R-8 — Scope-conflict open-item disposition

The scope conflict identified at SOW-0074 (flare-system equipment technically described but listed as excluded in the DBM scope table; final in/out boundary requires owner/engineering ruling) shall be tracked as an open item through acceptance and closed by owner/engineering ruling before turnover sign-off. (Source: `SCOPE_LEDGER.csv` SOW-0074.)

### R-9 — Detailed acceptance criteria (clause-level)

Detailed acceptance criteria specific to HP flare KO drum process mechanical scope (design pressure, temperature, material class, sizing, relief sizing, nozzle/connection schedule, vendor-document table line items, etc.) **location TBD** — these reside in `26020-Package_Requirements.docx` package heading 34, which is not locally accessible as text. Acceptance shall apply those clauses once the source slice is available. (Source: `SCOPE_LEDGER.csv` SOW-0073 source reference; `PACKAGE_REGISTER.csv` PKG-081 Source References.)

## Standards

| Standard / Authority | Applicability | Source / Location |
|---|---|---|
| 26020-Package_Requirements.docx package heading 34 | Authoritative process mechanical package requirements for PKG-081, including vendor-document tables | location TBD (binary not text-accessible) |
| DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md | Facility-level design basis referenced by PKG-081 (companion context for sour-service, utilities, interfaces) | `PACKAGE_REGISTER.csv` PKG-081 Source References; locally accessible |
| Applicable codes and standards for sour-service flare KO drums (pressure vessel code, relief, materials) | ASSUMPTION: governing codes for HP flare KO drums apply; specific code list is in source materials | location TBD (in `26020-Package_Requirements.docx` and DBM SEC-15) |

## Verification

| Requirement | Verification Approach | Evidence Artifact |
|---|---|---|
| R-1 | Side-by-side review of vendor package against DEL-081-01 / DEL-081-02 / DEL-081-03 | Package Acceptance Checklist |
| R-2 | Responsibility map review; no EPC encroachment on vendor design, no vendor encroachment on facility integration | Package Acceptance Checklist (responsibility section) |
| R-3 | Per-interface review of vendor outputs vs. EPC interface definitions in DEL-081-02 / DEL-081-03 | Package Acceptance Checklist (interface section); Vendor Document Review Log entries per interface |
| R-4 | Document-by-document review against vendor document register from DEL-081-05 | Vendor Document Review Log |
| R-5 | Inspection releases, FAT/SAT, NDE, pressure-test review | Test / Inspection Evidence file set |
| R-6 | Trace OBJ-009 carry-through into vendor outputs (relief, fire/gas, shutdown, environmental, sour-service) | Package Acceptance Checklist (safety/regulatory section) |
| R-7 | Trace OBJ-010 carry-through (sparing, isolation, winterization, commissioning, turnover, open-item closure) | Turnover evidence; open-item register entries |
| R-8 | Document the SOW-0074 open item; require owner/engineering ruling before sign-off | Open-item register entry referencing SOW-0074; ruling record |
| R-9 | Apply 26020 package-requirements clauses once locally accessible | TBD pending source-slice access |

## Documentation

Required artifacts produced by this deliverable (per `_CONTEXT.md` Anticipated Artifacts and `DELIVERABLE_REGISTER.csv` DEL-081-06):

- Vendor document review log
- Package acceptance checklist
- Test / inspection evidence
- Turnover evidence

These artifacts shall cite their basis documents (DEL-081-01, DEL-081-02, DEL-081-03 for the acceptance basis; DEL-081-04, DEL-081-05 for the vendor inputs) and the GATE-07 PROJECT_DECOMP snapshot used as the decomposition reference.
