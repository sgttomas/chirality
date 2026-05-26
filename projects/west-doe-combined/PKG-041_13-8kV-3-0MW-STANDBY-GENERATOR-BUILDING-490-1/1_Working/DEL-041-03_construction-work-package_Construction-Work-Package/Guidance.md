# Guidance — DEL-041-03 Construction Work Package

## Purpose

The Construction Work Package translates the EPC Integrator's Scope of Work (DEL-041-01) and Package Datasheet (DEL-041-02) into a constructible plan for the vendor-furnished 13.8 kV, 3.0 MW standby generator building (PKG-041, building 490-1). It explains how the package is physically installed, built, inspected, turned over, and tied into the larger facility systems (`_CONTEXT.md` Scope; GATE-07 `DELIVERABLE_REGISTER.csv`). Without this deliverable the workbook-declared interfaces on PKG-041 have no field execution plan or turnover evidence trail.

## Principles

1. **Integrator-led; vendor-fed.** Package engineering, design, vendor documentation, and the physical equipment package are vendor-owned (DEL-041-04 / DEL-041-05). Construction integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination — is EPC Integrator-owned (GATE-07 `PACKAGE_REGISTER.csv` responsibility narrative).
2. **Interface-driven execution.** Every workbook-declared interface on PKG-041 is a construction obligation. The twelve interfaces in GATE-07 `INTERFACE_REGISTER.csv` are the spine of the workface plan and the turnover checklist.
3. **Evidence over assertion.** The Package Datasheet (DEL-041-02) carries interface fact evidence as artifacts (ART-* "Interface fact -" rows). The Construction Work Package consumes those facts; it does not restate them.
4. **Source-grounded values.** Construction-affecting values come from Workbook Packages row 43, the Design Basis Memorandum (`_Sources/DBM-Deepcut`), or accepted vendor documentation. Unsupported values are `TBD`, never invented.
5. **No silent reconciliation of upstream conflict.** If DEL-041-01, DEL-041-02, or the vendor package on DEL-041-04 disagree, log the conflict against the originating deliverable rather than papering over it in the construction work package.

## Considerations

- **High-voltage life-safety:** 13.8 kV electrical work and standby generator commissioning involve significant arc-flash and grounding hazards. Site safety planning, lock-out/tag-out, and energized-work procedures are essential. Specific procedures: TBD (not derivable from registers; resolve from facility safety standards and `_Sources/DBM-Deepcut`).
- **Standby reliability function:** The package is a standby generator (package name, GATE-07 `PACKAGE_REGISTER.csv`). Construction sequencing should avoid loss-of-standby windows during tie-in to the existing electrical system. (ASSUMPTION pending verification against facility operating philosophy.)
- **Vendor-furnished building:** "Generator building" suggests a packaged, vendor-furnished enclosure delivered to site. Site preparation (foundation, grading, drainage) typically precedes setting. (ASSUMPTION; vendor design on DEL-041-04 is authoritative when available.)
- **Twelve interface domains** span mechanical (utility piping, drain/containment, HVAC), electrical (power, grounding, lighting), I&C/communications, safety (fire & gas), site civil (grading, structural), and operability (maintenance access). The construction plan must reach into multiple disciplines despite the package being classified Electrical.
- **Objective alignment:** Eight objectives (OBJ-001, OBJ-004 through OBJ-010) are mapped to this deliverable, but objective acceptance criteria were not opened in this run. Traceability is required (REQ-CWP-06) and content is `TBD` until objective text is consulted.

## Trade-offs

| Trade-off | Considerations |
|---|---|
| Pre-set vs. post-set tie-ins | Setting the vendor-furnished building before completing foundations and underground tie-ins simplifies vendor delivery but may complicate access for buried utility and grounding work. Sequencing decision: TBD (depends on vendor design and site logistics). |
| Single combined turnover vs. discipline-by-discipline turnover | A single combined turnover reduces administrative overhead; discipline-by-discipline turnover gives earlier visibility into latent defects. The `_CONTEXT.md` anticipated artifact is a single turnover checklist, suggesting the combined approach; sub-discipline sign-offs can be rows within it (ASSUMPTION). |
| EPC self-perform vs. vendor field services | Some interface tie-ins (notably I&C / Control Cabling and Fire & Gas / Safety Systems) may be most efficiently executed by vendor field services under EPC Integrator coordination. Allocation: TBD. |

## Examples

No worked examples are available from the accessible source set. Concrete tie-in narratives, installation sequences, and turnover acceptance criteria are TBD until the Design Basis Memorandum slices and any vendor-furnished installation manuals on DEL-041-04 are opened.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none open) | No source-vs-source conflicts identified in this run. Most "missing" content is absent rather than contested. | — | — | — | — | TBD |
