# Guidance: Construction Work Package

## Purpose

The Construction Work Package turns the accepted `PKG-081` Flare KO Drum (High Pressure) 3-25 basis into construction-facing instructions, checks, and turnover evidence. Its purpose is to show how the vendor-supplied two HP flare KO drums (V-4100-2 in the compressor area; V-4150-2 in the tank farm) and their dedicated transfer pumps (P-4100-2 and P-4150-2) will be physically installed, built, inspected, turned over, and tied into the 03-25 facility flare, piping, drain, electrical, EHT, grounding, lighting, controls, structural, and maintenance-access systems.

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-081-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-081`; `INTERFACE_REGISTER.csv` rows for `PKG-081`.

## Principles

- Keep package identity and source basis visible. The construction package should carry `PKG-081`, workbook row 54, WBS 02, CoA tracking number `26020-02-17-001`, Mechanical discipline, and source references forward into the workface plan.
- Treat the Gate 7 registers as accepted decomposition truth for package identity, deliverable intent, artifacts, objectives, and interface labels.
- Treat the DBM source slices (`3-25_Comp_and_Liquids_DBM.md` Flare and Blowdown; Construction Scope Summary; SEC-02; SEC-08; SEC-15) as authority for facility-level flare-system context, ambient/geotechnical conditions, and standards constraints.
- Preserve the vendor-vs-EPC responsibility split. Package engineering, package design, vendor documentation, and physical equipment are Package Vendor scope; integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) is EPC Integrator scope.
- Preserve uncertainty. KO drum and pump detailed mechanical data, final flare relief/blowdown loads, staggered-blowdown sequence, shared HP/Cryo flare-stack service split, final geotechnical parameters, and detailed mechanical/piping specifications should remain `TBD` until accepted source material closes them.

## Considerations

The most important package-specific construction controls are the ten declared interface types for `PKG-081`: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports. These are dense for a vendor-supplied mechanical package and reflect the integration of a flare-relief subsystem with multiple facility systems.

The DBM Flare and Blowdown section names the in-scope equipment precisely: HP headers route to KO drums V-4100-2 (compressor area) and V-4150-2 (tank farm); both manifold to the shared HP/Cryo flare stack. KO drum pumps P-4100-2 and P-4150-2 truck-out or transfer liquids to slop. HP and LP relief headers are 508 mm (20 inch) in the current basis, and the sonic HP/Cryo flare stack is 660 mm OD by 60,957 mm tall. The CWP should anchor on these named tags and use them in the workface plan, the interface checklist, and the turnover records rather than generic equipment references.

Staggered blowdown is required to limit maximum relief, but the external Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 is a required detailed source for the final sequencing and was not read in this run. The CWP should carry a verification hold for the final blowdown loads and sequence rather than closing relief criteria from currently-available sources.

The HP/Cryo flare stack and the incinerator are shared between 03-25 and 04-25, and the current source basis explicitly notes that the exact service split and owner interface remain open. The CWP should carry this as an open interface item against the Relief / Flare / Vent interface, not as a closed scope boundary.

Construction planning should account for the broader 03-25 construction scope (module setting, mechanical hookups, ISBL/OSBL interconnecting piping, pipe supports, home-run cabling, terminations, area lighting, fencing, security, and tie-ins). Only the portions that affect the HP KO drum package, its dedicated transfer pumps, or the declared interfaces should be carried into this deliverable as requirements.

Geotechnical data and detailed mechanical/piping specifications are not fully closed. The DBM requires the final geotechnical report before foundation design closure; foundation, anchorage, and structural support criteria for the two drums and two pumps should remain readiness-gated until that report and vendor equipment loads are accepted.

The -40 deg C minimum ambient basis governs exposed drums, package piping, control panels, instrumentation, and field devices. EHT is a declared interface for `PKG-081`; cold-weather installation, handling, and commissioning provisions for the drums, low-point piping, drains, and transfer pumps should be explicitly verified before energization and before the first relief event.

Standards and regulatory references are not fully available in the current source set. The CWP should carry verification requirements for project mechanical/piping specifications, flare-system relief and blowdown studies, and the controlling shutdown-and-blowdown philosophy rather than claiming final compliance from unavailable citations.

## Trade-offs

| Topic | Trade-off | Guidance |
|---|---|---|
| Early CWP planning vs. vendor design certainty | Early CWP drafting helps define workface controls, but vendor drum and pump ratings, dimensions, weights, nozzle schedules, and termination details may evolve. | Use `TBD` readiness gates and re-align with the vendor engineered equipment package (`DEL-081-04`) before IFC release. |
| Flare-system relief loads vs. construction schedule | Final blowdown loads and staggered-blowdown sequencing may not be closed when civil/structural and piping work begins. | Keep relief/blowdown criteria as verification holds; do not pour foundations or close pressure-test boundaries prematurely. |
| Package-local focus vs. facility integration | The HP KO drums are vendor scope, but they function only when manifolded to the shared HP/Cryo flare stack and routed to facility drains/slop. | Keep interface signoffs explicit, including the open shared-system items with 04-25. |
| Source-limited standards vs. construction readiness | The DBM references standards, external philosophy documents, and Word-source detail that are not fully available. | Require verification of current project specifications, flare studies, the W242510-PRC-REP-000003-001 philosophy, and the 26020-Package_Requirements.docx package heading 34 before IFC/field release. |
| EPC vs. Vendor scope at the boundary | Some construction-adjacent tasks (factory-fitted internals, vendor pressure tests, vendor commissioning) belong to the vendor. | Document the EPC/Vendor boundary at each interface in the checklist and turnover record. |
| Cold-weather readiness vs. early energization | EHT, drainage, and insulation must be complete before any cold-weather operation of drums and transfer pumps. | Treat cold-weather readiness as a witness point on the turnover checklist. |

## Examples

TBD - no source-provided HP KO drum installation example, vendor equipment data, or completed turnover checklist is available in the current deliverable source set.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-081-03-001 | Detailed HP KO drum mechanical data (dimensions, MAWP, MDMT, nozzle schedule, internals, materials, weights, lifting lugs) and transfer-pump data (type, capacity, head, NPSH, driver, sealing, materials) are not present in accessible source slices. | `PACKAGE_REGISTER.csv` row `PKG-081`; `_REFERENCES.md` Missing/Deferred References | Missing Word source slice (26020-Package_Requirements.docx package heading 34) and vendor data | `Datasheet.md` Construction; `Specification.md` Requirements, Verification; `Procedure.md` Steps, Verification | Carry detailed drum and pump characteristics as `TBD` until vendor engineered equipment package (`DEL-081-04`), package datasheet (`DEL-081-02`), and the Word source slice are accepted. | TBD |
| HRR-081-03-002 | Final flare relief and blowdown loads and the staggered-blowdown sequence are referenced by the DBM but are governed by the external Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001, which is not accessible in the current deliverable source set. | `3-25_Comp_and_Liquids_DBM.md` Flare and Blowdown (line 501) | Missing external philosophy document | `Datasheet.md` Conditions; `Specification.md` Requirements, Standards, Verification; `Procedure.md` Steps, Verification | Carry blowdown sequence and final relief loads as verification holds; do not close pressure-test or relief boundaries until the external philosophy is accepted. | TBD |
| HRR-081-03-003 | The HP/Cryo flare stack and incinerator are shared between 03-25 and 04-25, and the exact service split and owner interface are explicitly carried as open by the DBM. | `3-25_Comp_and_Liquids_DBM.md` Commercial and Facility Interfaces (line 56); SEC-08 emissions/incinerator note | Cross-facility allocation not closed in source set | `Specification.md` Scope, Requirements; `Guidance.md` Considerations; `Procedure.md` Steps | Carry the HP/Cryo flare-stack tie-in and incinerator service split as an open interface item against the Relief / Flare / Vent interface; do not close the scope boundary until a source ruling is recorded. | TBD |
| HRR-081-03-004 | Responsibility for the deliverable is EPC Integrator, but the package responsibility model splits package engineering/design/equipment to the Package Vendor and facility integration to the EPC Integrator. | `_CONTEXT.md` Identity; `DELIVERABLE_REGISTER.csv` row `DEL-081-03` | `PACKAGE_REGISTER.csv` row `PKG-081` ResponsibilityModel | `Specification.md` Scope; `Procedure.md` Prerequisites, Steps | Treat EPC Integrator as deliverable owner; require human/project assignment for the EPC/Vendor construction-task split (field commissioning, vendor pressure tests, witness points) before work release. | TBD |
