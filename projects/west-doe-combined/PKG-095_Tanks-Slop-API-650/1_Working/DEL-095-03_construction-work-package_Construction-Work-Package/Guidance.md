# Guidance — Construction Work Package (DEL-095-03)

## Purpose

This Guidance explains the rationale, principles, and trade-offs behind the Construction Work Package (CWP) for **PKG-095 Tanks, Slop (API 650)**. It complements the normative `Specification.md` by giving construction planners and the EPC Integrator the design intent, the responsibility split, and the supporting reasoning so that field decisions during installation and tie-in stay aligned with the Package Vendor's certified design and the Gate 5 turnover expectations.

The CWP exists because the Slop Tank package is delivered as a Package Vendor scope (engineering/design/equipment) but is installed and integrated into the facility by the EPC Integrator. The EPC Integrator must convert the vendor-engineered tank, its appurtenances, and its declared interfaces into an operating, inspected, and turned-over installation.

## Principles

1. **Vendor-EPC split is the spine of the package.** Per the PKG-095 PACKAGE_REGISTER row, the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Construction decisions should preserve, not redo, vendor design intent. When in doubt, escalate to the EPC interface review, not to field modification.
2. **Service segregation is the safety and operability point of the tank.** The slop tank exists to segregate off-spec or contaminated hydrocarbon liquids from on-spec condensate product (SCOPE_LEDGER SOW-0214). Construction must never bypass that segregation — particularly during tie-ins where temporary jumpers, blinds, or hose connections might cross-contaminate on-spec systems.
3. **Process disposition is open; carry it as TBD, not as invented routing.** The slop source list, disposition path, and tank design basis are explicitly flagged as requiring process confirmation (SOW-0216). The CWP must not assume which sources route where; certified P&IDs from process engineering are the only authority for routing.
4. **API 650 is the tank construction authority.** Tank-specific weld, NDE, hydrotest, settlement, and acceptance criteria come from API 650 as modified by the Package Vendor's certified design. The CWP follows that authority; field-fit deviations require vendor concurrence.
5. **Turnover evidence is the deliverable.** A complete and well-organized turnover package (vendor data book, foundation acceptance, weld/NDE, hydrotest, settlement survey, CP commissioning, loop checks, punch list, as-builts) is the construction product, not just a built tank.
6. **Interface coverage is checklist-driven.** PKG-095 has nine declared interface types (INTERFACE_REGISTER). Each appears as a row on the construction interface and turnover checklist with sign-off; missing rows are missing turnover, not just missing documentation.

## Considerations

- **Foundation type and civil hand-off.** API 650 slop tanks typically sit on a ringwall or pad foundation provided by a civil/earthworks package. The CWP needs explicit foundation acceptance (anchor bolt template, ringwall elevation/level/flatness, underpad readiness) before erection begins. The civil package linkage is not declared in `_DEPENDENCIES.md` (declared upstreams are "None"); treat the linkage as an open coordination point.
- **Field erection vs. shop modularity.** API 650 atmospheric tanks are field-erected in the general case. The accessible source slices do not state a module/shop assembly; treat any modular sub-assembly (e.g., shop-rolled shell courses) as a vendor design choice rather than an assumption.
- **Spill containment and drainage.** PKG-095 includes the "Grading / Site Drainage / Spill Containment" and "Drain / Containment" interface types. Secondary containment (dike, liner, sump) and routing of contained drainage to a slop-compatible destination are construction-critical; the CWP should verify dike geometry and drain routing as part of pre-hydrotest readiness.
- **Cathodic protection sequencing.** CP commissioning typically follows backfill/grounding completion but precedes long-term service. Plan CP energization to align with hydrotest and pre-commissioning windows so that protection is active before slop is introduced.
- **Overfill and high-level protection.** SOW-0215 lists "standard tank instrumentation" but does not specify trip levels. Overfill protection (independent high-level switch or equivalent) is standard tank-farm practice; treat its specifics as TBD per process design but plan its loop check explicitly.
- **Truck-out interface logistics.** SOW-0215 explicitly includes truck-out connections. Site access, load-out spotting, drainage of the load-out area, and grounding for vacuum/tanker trucks are construction-coordination items that should appear in the workface plan.
- **Declared dependencies are empty.** `_DEPENDENCIES.md` lists no declared upstreams or downstreams as of PREPARATION. The CWP should treat civil, electrical, instrumentation, vendor data, and process P&IDs as ASSUMPTION-level coordination items until declared in a dependency-extract pass.

## Trade-offs

- **Field erection sequence (bottom-up vs. jacked-roof).** API 650 erection method (conventional vs. jacked-roof) is a vendor/EPC contractor choice. The CWP should not prescribe a method but should ensure the chosen method's lift, weld, and inspection records are captured.
- **Hydrotest water sourcing and disposal.** Hydrotest water sourcing (fresh, treated, or borrowed) and post-test disposal (especially in a slop-tank context where any residual contamination matters less than for product tanks, but environmental compliance still applies) is a trade-off. Record sourcing and disposition.
- **Sequencing of interior coating / lining (if any).** If the vendor design includes an interior lining or coating for slop service, lining application sequencing relative to hydrotest must be reconciled (some linings require pre-hydrotest application, others post). This is a vendor-driven trade-off; the CWP records the chosen sequence.
- **Independent overfill protection vs. control-system level.** Overfill protection may be implemented as an independent level switch tied to inlet block valves or as a control-system function. Independent protection is more robust; integrated control is simpler. TBD per process design.

## Examples

PKG-095 is the sole "Tanks, Slop (API 650)" workbook package (row 91). Other tankage packages in the project decomposition (e.g., other API 650 atmospheric storage packages) share installation patterns (vendor-engineered tank + EPC site erection + civil foundation + CP + grounding + instrumentation + hydrotest + turnover), and lessons learned from those should be available to construction planning for this CWP. Cross-reference is informational; this CWP governs PKG-095 only.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-095-03-01 | Detailed package heading 47 of 26020-Package_Requirements.docx is cited as a basis (in `_CONTEXT.md`, `_REFERENCES.md`, and the decomposition source basis) but its text was not accessible to this run; construction-specific document expectations and process mechanical detail beyond the SCOPE_LEDGER excerpts may therefore be missing. | _CONTEXT.md "Source Reference" / `_REFERENCES.md` | Available SCOPE_LEDGER.csv excerpts (SOW-0213..0216) | Datasheet.Conditions/Construction; Specification.Standards/Documentation; Procedure.Prerequisites/Records | PROPOSAL: confirm/parse the .docx heading 47 in a follow-up source-slice extraction pass and merge into Specification.Documentation and Datasheet.Conditions before Gate 5. | TBD |
| C-095-03-02 | Major equipment tag is "likely TK-9130-2" per SOW-0215 but is not confirmed; PACKAGE_REGISTER lists a different identifier ("26020-03-PT-19-004 - Tanks, Slop") which is a package-equipment companion register tag, not a P&ID tag. Construction tagging risks ambiguity. | SCOPE_LEDGER.csv SOW-0215 ("likely TK-9130-2") | PACKAGE_REGISTER.csv PKG-095 (26020-03-PT-19-004) | Datasheet.Identification/Attributes; Procedure tag references | PROPOSAL: treat TK-9130-2 as the P&ID equipment tag (subject to vendor/process confirmation) and 26020-03-PT-19-004 as the package companion register identifier; resolve both into the construction interface checklist before Gate 5. | TBD |
| C-095-03-03 | Slop source list, disposition path, and tank design basis are explicitly open (SOW-0216 "require process confirmation"). Construction cannot finalize tie-in scope without these. | SCOPE_LEDGER.csv SOW-0216 (open items) | _CONTEXT.md anticipated artifacts (presume completability) | Specification.Requirements (R-095-03-03, R-095-03-04, R-095-03-11); Procedure.Phase-3 tie-ins | PROPOSAL: hold final tie-in counts and routing TBD until process engineering issues IFC P&IDs and a confirmed disposition path; do not invent routing in this CWP. | TBD |

### HRR items (Human Ruling Required)

The three Conflict Table entries above are the explicit HRR items for this CWP. Pass 2 surfaced no additional cross-document conflicts that exceed `TBD` resolution within the drafted documents; any resolution of the three HRR items above should be reflected back into `Specification.md`, `Datasheet.md`, and `Procedure.md` in the next pass.
