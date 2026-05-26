# Guidance — DEL-072-04 Vendor Engineered Equipment Package

## Purpose

DEL-072-04 is the **vendor production unit** for PKG-072 (Truck Product Loading Unit 4-25). It exists so that the Package Vendor's engineering, design, fabrication/supply, and the physical equipment package itself are tracked as a single coherent deliverable downstream of the EPC Integrator anchor deliverables (Scope of Work, DEL-072-01; Package Datasheet, DEL-072-02) and ahead of EPC review/acceptance (DEL-072-06).
Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv (DEL-072-04 row); PACKAGE_REGISTER.csv row 99 Notes.

## Principles

- **Vendor ownership, EPC integration.** The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration (PACKAGE_REGISTER.csv row 99 Notes). DEL-072-04 must respect that division and not silently absorb EPC-side scope.
- **Source-anchored over derived.** Equipment, conditions, and control choices come from the source basis (workbook row 99; 26020-Package_Requirements.docx heading 26; SOW-0247/0248). Where the source says "TBD" or "vendor to design", carry that forward — do not invent values.
- **Datasheet alignment.** The vendor package design basis and datasheet set (ART-071DC1CCEF) must be coherent with the EPC Package Datasheet (DEL-072-02). Divergences are conflicts, not refinements.
- **Interface discipline.** Package-side terminations only. Facility-side tie-ins are out of scope and live in DEL-072-03 (Construction Work Package).

## Considerations

- **Heater capacity is open.** SOW-0247 states "A fuel gas heater capacity TBD"; the design flow ( > 8.4 MMSCFD) and outlet temperature (95 F / 35 C) constrain the sizing problem, but the capacity value itself is vendor-derived and currently TBD.
- **MAWP is open.** Design Pressure is 150 psig but MAWP is explicitly TBD (SOW-0248). The vendor's pressure-equipment design must establish MAWP and may set MAWP > Design Pressure per applicable code; standard reference is TBD here.
- **Final Flow is open.** Design Flow is bounded ( > 8.4 MMSCFD) but Final Flow is TBD (SOW-0248); the vendor design point should be carried with both values until Final Flow is settled.
- **Scrubber sizing convention.** The k-factor convention (0.35 imperial max plus operating-pressure de-ration) is unusual to encounter pre-stated; treat it as a hard ceiling, not a target, and apply the de-ration factor on top of pressure-rating effects.
- **Control architecture.** SCR (600 V) heater control panels live in the electrical building, not on the skid; the vendor must coordinate field-to-building cabling boundaries with the EPC Integrator via the I&C / Control Cabling and Electrical Power interfaces.
- **Objective association.** This deliverable's listed objectives (OBJ-001, OBJ-003..OBJ-010) come from the package-grouping heuristic in OBJECTIVE_DELIVERABLE_MAP.csv (uniformly assigning all PKG-072 objectives to every PKG-072 deliverable). Treat the association as **ASSUMPTION (best-effort, package-grouping)** until a human confirms a deliverable-level objective mapping.

## Trade-offs

- **Vendor design freedom vs. EPC fit.** The source explicitly says "vendor to design" for the scrubber and leaves heater capacity TBD; vendor design choices that minimize equipment cost must still satisfy facility integration constraints carried by DEL-072-02 and DEL-072-03.
- **Carry-forward vs. resolve-now.** Several values are TBD in the source (heater capacity, MAWP, Final Flow). Resolving them mid-vendor-design saves rework; deferring them keeps the deliverable narrow but creates downstream contingency for DEL-072-06 acceptance.
- **Standards specificity.** Locally accessible registers do not enumerate the governing pressure, electrical, and area-classification standards. Listing them precisely here would invent authority the source does not establish; leaving them as `location TBD` preserves epistemic honesty but pushes the burden onto vendor submittals.

## Examples

Examples must come from accessible source slices. The current accessible source set does not contain worked examples for analogous vendor low-pressure fuel gas packages within `_Sources/`. **TBD — examples to be added when vendor submittals or DBM-Deepcut analogous package sections are read in a follow-on pass.**

## Conflict Table (for human ruling)

None at Pass 1/Pass 2. The four documents agree on terminology, equipment counts, conditions, and interface posture. Differences between DEL-072-04 (vendor production unit) and sibling DEL-072-02 (EPC Package Datasheet) are by design (production vs. handoff) and are not conflicts.
