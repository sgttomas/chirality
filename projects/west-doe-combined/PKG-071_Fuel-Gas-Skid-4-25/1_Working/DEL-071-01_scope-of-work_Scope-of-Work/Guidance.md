# Guidance: DEL-071-01 — Scope of Work (PKG-071 Fuel Gas Skid 4-25)

## Purpose

DEL-071-01 is the mandatory Gate 5 EPC anchor deliverable for PKG-071. It establishes the authoritative integrator-side narrative of what the package is, what it does, where its boundaries lie, who is responsible for what, and how it integrates into the whole 04-25 Deep Cut facility. Source: `_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv.

It is the integrator's articulation of the source-given package definition (Workbook Packages row 61; 26020-Package_Requirements.docx package heading 25), and it grounds the rest of the package deliverable chain (Datasheet, CWP, vendor-engineered equipment, vendor doc turnover, EPC-vendor review).

## Principles

- **Source fidelity.** The package identity, function, equipment, and conditions are fixed by the workbook row and the Word package heading. The SOW articulates them; it does not redefine them. Source: PACKAGE_REGISTER.csv; SCOPE_LEDGER SOW-0099..0102.
- **Responsibility separation.** Per OBJ-004 and the package row, the Package Vendor owns engineering/design/documentation/equipment and the EPC Integrator owns facility integration. The SOW must not transfer vendor scope to the EPC, or vice versa.
- **Boundary clarity.** The source explicitly lists "By others" items (shipping, installation, tie-in piping, electrical tie-in). The SOW must surface these so downstream construction-work and procurement deliverables can route them correctly.
- **Interface visibility.** PKG-071 carries twelve applicable interface types (PACKAGE_REGISTER.csv). The SOW must list them so OBJ-005..009 integration deliverables can pick them up. None should be silently dropped.
- **TBD discipline.** Final flow and MAWP are explicit TBDs in source (SCOPE_LEDGER SOW-0102). Heater capacity is TBD (SOW-0101). These must remain TBD until vendor inputs close them — they must not be invented.

## Considerations

- **Capacity differs from sister package.** PKG-084 (Fuel Gas Skid 3-25) has Design Flow > 1.5 MMSCFD (SOW-0098). PKG-071 has Design Flow > 8.4 MMSCFD (SOW-0102). Conditions look otherwise similar but must be quoted from the PKG-071 row, not the PKG-084 row.
- **Heating value not stated for PKG-071.** SOW-0098 cites 1040 BTU/SCF for the 3-25 sister package; SOW-0102 does not restate it for 4-25. The SOW should not propagate the 3-25 heating value to PKG-071 without explicit source.
- **Heater control architecture.** SCR control panels are 600 V and physically located in the electrical building (SOW-0102); the heater itself carries a skin-temperature thermocouple override (SOW-0101). The EPC integration narrative should make clear that I&C, electrical power, and electrical building scopes will touch this package (interfaces I&C / Control Cabling, Electrical Power, Building HVAC / Services).
- **Scrubber sizing is a vendor exercise.** k = 0.35 imperial max + de-ration is a sizing constraint, not a sized result. The SOW should preserve the constraint and let the vendor produce the sized vessel via DEL-071-02 / DEL-071-04.
- **Objective coverage.** OBJ-001 (04-25 facility outcome), OBJ-004 (vendor/EPC split), OBJ-005..010 (electrical, controls, utilities, civil/structural, safety/regulatory, operability/handoff) are all marked as supported by this deliverable (DELIVERABLE_REGISTER.csv). Treat OBJ-005..010 as PACKAGE_HEURISTIC associations — they are directionally relevant because PKG-071 carries the corresponding interface types, but they are not turned into PKG-071-internal requirements here. (ASSUMPTION: best-effort mapping per OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC.)

## Trade-offs

- **Narrative vs. tabular.** A pure tabular SOW is easier to audit against the registers but harder to integrate into procurement and construction packages. A narrative-only SOW is harder to verify. The artifact split (ART-AC01900208 SOW + ART-31BC19483F equipment list + ART-5369838D71 integration narrative + ART-451A242BFC responsibility record) intentionally produces both, so this Specification's requirements split tabular identity from narrative integration text.
- **Tightening vs. preserving source.** Some source items (Capacity TBD, MAWP TBD, Final Flow TBD) could be tightened with engineering judgment. The skill's non-negotiable is to preserve them as TBD until vendor input arrives. Tightening prematurely risks contractually binding values that the vendor has not yet committed to.
- **By-others list scope.** The source by-others list (shipping, installation, tie-in piping, electrical tie-in) is unusually broad for a "package scope" — it implies the package is FOB-style supply with EPC doing physical placement and connection. The SOW must surface this clearly so estimating and procurement do not assume otherwise.

## Examples

- Identity sentence: "PKG-071 Fuel Gas Skid 4-25 (Workbook ID 71, WBS 01, Mechanical) is a single skid-mounted Low Pressure Fuel Gas Package comprising one low-pressure fuel gas heater (SCR-controlled, 600 V) and one low-pressure fuel gas scrubber (k = 0.35 imperial max plus operating-pressure de-ration; vendor-designed), serving the low-pressure fuel gas system for the West Doe Deep Cut Facility." Source: SCOPE_LEDGER SOW-0100, SOW-0101.
- Responsibility sentence: "Package Vendor is responsible for package engineering, package design, vendor documentation, and physical equipment supply. EPC Integrator is responsible for facility-level integration: interfaces, tie-ins, constructability, procurement/construction coordination, and facility integration." Source: PACKAGE_REGISTER.csv.
- By-others sentence: "By others: shipping packages to site, installation, tie-in piping, electrical tie-in." Source: SCOPE_LEDGER SOW-0102.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CF-071-01-01 | Heating value: 1040 BTU/SCF cited only on PKG-084 row (SOW-0098), not on PKG-071 row (SOW-0102). Should PKG-071 inherit this value? | SCOPE_LEDGER SOW-0098 (PKG-084) | SCOPE_LEDGER SOW-0102 (PKG-071, no heating value stated) | Datasheet.md Conditions; Specification.md REQ-071-01-07/08 | Do not propagate; mark heating value TBD for PKG-071; ask vendor / refer to 26020-Package_Requirements.docx | TBD |
| CF-071-01-02 | Pass-through of OBJ-005..010 as "supported" by DEL-071-01. The deliverable carries no internal requirements for electrical, controls, utility, civil, safety, or operability scope — those live in sibling/other packages. Should the SOW restate them or only cross-reference? | DELIVERABLE_REGISTER.csv (SupportsObjectives) | OBJ-005..010 register rows scoped to discipline packages, not this SOW | Specification.md REQ-071-01-13; Guidance Considerations | Treat as cross-reference only; do not introduce derivative requirements into this SOW. (ASSUMPTION: PACKAGE_HEURISTIC association.) | TBD |
| CF-071-01-03 | Source clause-level rereads not possible: 26020-Package_Requirements.docx is binary and not directly readable in this run. Pre-extracted SCOPE_LEDGER slices were used. Acceptable? | `_REFERENCES.md` (lists .docx); SCOPE_LEDGER (extracted slices) | Skill authority hierarchy (rank 1 = authoritative source materials) | All four documents | Accept extracted slices as proxy for this initialization pass; perform source-clause reread during Pass 3 / human review when a converter or human-readable extract is available | TBD |
