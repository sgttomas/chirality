# Guidance: DEL-076-01 — Scope of Work (Lube Oil Supply)

Pass: P1 (initial draft); Pass 2 consistency sweep applied.

## Purpose

This deliverable establishes the EPC Integrator's Scope of Work for PKG-076 (Lube Oil Supply): a Mechanical package supplying two electric-motor-driven lube oil transfer pumps and bulk heated storage that serves all compressor packages at the West Doe Deepcut facility Storage Tank Area [Source: `DELIVERABLE_REGISTER.csv` row 384; `PACKAGE_REGISTER.csv` row 70; `SCOPE_LEDGER.csv` SOW-0136].

The SoW is the Gate 5 EPC anchor deliverable that downstream PKG-076 deliverables (Package Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover, EPC Vendor Package Review and Acceptance) consume as their authoritative starting basis [`DELIVERABLE_REGISTER.csv` rows 384-389; `_CONTEXT.md` Notes].

## Principles

1. **Vendor owns the package; EPC owns the integration.** The package vendor delivers engineering, design, vendor documentation, and the physical equipment package. The EPC Integrator owns integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. The SoW must preserve this split verbatim [Source: `PACKAGE_REGISTER.csv` row 70 Responsibility text].

2. **Source basis carries.** The package's authoritative inputs are the workbook row (Packages row 70), the package requirements document (`26020-Package_Requirements.docx` heading 30), and the Deepcut DBM Lube Oil Storage and Pump Basis. The SoW shall cite these by section and shall not invent values [Source: `DELIVERABLE_REGISTER.csv` row 384; `4-25_Deepcut_DBM.md` Lube Oil Storage and Pump Basis].

3. **Interface set is fixed at workbook level.** Eight interface types are workbook-asserted (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports). The SoW shall surface them; the Package Datasheet (`DEL-076-02`) carries the interface requirements matrix detail [Source: `INTERFACE_REGISTER.csv` rows 557-564; `ARTIFACT_REGISTER.csv` row 4040].

4. **Sweet and sour service is a primary safety condition.** The package serves compressors handling sour gas. SoW language must preserve sweet/sour service classification because it drives downstream material, sealing, and hazardous-area decisions even though those are not specified in this SoW [Source: `SCOPE_LEDGER.csv` SOW-0137; OBJ-009 sour-service objective].

5. **"By others" items are real exclusions, not silent assumptions.** Shipping to site, installation on piles, tie-in piping, electrical connections, and mounting platform/stairs are explicitly outside vendor scope. The SoW shall enumerate these to prevent scope creep on the vendor side and silent scope gaps on the EPC side [Source: `SCOPE_LEDGER.csv` SOW-0138].

## Considerations

- **Tank arrangement ambiguity.** The workbook describes a "horizontal storage tank, split in the middle" carrying both cylinder and crankcase oils; the Deepcut DBM describes separate "400 bbl heated tank" for cylinder oil and "200 bbl heated tank" for crank-case oil. These are most plausibly the same physical asset described from two angles, but the vendor configuration could resolve as either one split tank or two tanks. The SoW should record both source statements and flag the resolution as `TBD` for vendor confirmation [Sources: `SCOPE_LEDGER.csv` SOW-0137; `4-25_Deepcut_DBM.md` Lube Oil Storage and Pump Basis].

- **Driver-make exclusion.** "No Toshiba motors" is the only stated driver constraint. The SoW must carry it without re-interpretation; downstream vendor scope can elaborate on acceptable motor manufacturers [`SCOPE_LEDGER.csv` SOW-0138].

- **Cylinder oil type is unresolved.** The DBM notes multiple cylinder oils may be required across compressor services (inlet, sales, stabilizer overheads, acid gas, sales booster) and that manufacturer-recommended types remain TBC during FEED. The SoW should not over-commit to a single cylinder oil specification [`4-25_Deepcut_DBM.md` Lube Oil Storage and Pump Basis].

- **Hazardous-material classification.** The DBM (Compressor and Liquids facility, Emergency Power / Lube Oil / Analyzers section) notes the project hazardous-material list governs lube-oil storage but was not available in the accessible workspace. The SoW should reference the project hazardous-material list with `location TBD` and not infer area classification or containment volumes [`3-25_Comp_and_Liquids_DBM.md` line 507].

- **Objective linkage is package-heuristic.** The eight OBJ rows carried by this deliverable are inherited via the package-grouping heuristic (`OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`), not from a deliverable-ID-specific objective map. Treat the linkage as directional ASSUMPTION until human-confirmed [Skill Step 1; `OBJECTIVE_REGISTER.csv`].

- **Distinction from the Package Datasheet.** The SoW says **what** is in scope, who is responsible, and **where** the boundaries are. It does not duplicate the datasheet's technical handoff data (pump curves, NPSH, motor sizing, materials, control philosophy). Those belong in `DEL-076-02`. The SoW should clearly point readers to the datasheet for technical handoff and to the Construction Work Package for installation execution [`DELIVERABLE_REGISTER.csv` rows 385-386; `ARTIFACT_REGISTER.csv` rows 4038-4042].

## Trade-offs

- **Verbatim source quotation vs. paraphrase.** Verbatim text preserves source fidelity but can read awkwardly. Paraphrase improves readability but risks scope drift. Prefer verbatim for responsibility split, by-others list, and service-classification statements; paraphrase is acceptable elsewhere if the source citation is preserved.

- **Listing interfaces in SoW vs. deferring to Datasheet.** Listing interface types in the SoW improves SoW completeness but partially duplicates `DEL-076-02`. The chosen approach (per R-08) is to list interface **types** in the SoW and point to `DEL-076-02` for the requirements matrix; this preserves scope visibility without duplicating engineering detail.

- **Strict source-only vs. directional inference.** Strict source-only leaves many TBDs visible (cylinder oil type, heated-tank set point, hazardous classification). Directional inference would fill them with conventional values but would violate source-grounding discipline. The SoW chooses strict source-only and surfaces `TBD`/`ASSUMPTION` labels so downstream deliverables (especially `DEL-076-02`) can resolve them with the right evidence.

## Examples

The Datasheet provides concrete examples of acceptable source citation format:

- Tagged equipment row citing both `SCOPE_LEDGER.csv` SOW-0137 and `4-25_Deepcut_DBM.md` Lube Oil Storage and Pump Basis.
- Operating-condition row citing `SCOPE_LEDGER.csv` SOW-0138 and marking heated-tank set point as `TBD`.
- Interface row citing the specific `IFC-*` ID from `INTERFACE_REGISTER.csv`.

## Conflict Table (for human ruling)

No source-vs-decomposition conflicts identified in Pass 2 sweep. The tank-arrangement ambiguity (split-tank vs. two tanks) is recorded as a `TBD`/ASSUMPTION in R-09 rather than a conflict; both source statements are consistent under the assumption of a single split storage system.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| — | (none captured this pass) | — | — | — | — | — |
