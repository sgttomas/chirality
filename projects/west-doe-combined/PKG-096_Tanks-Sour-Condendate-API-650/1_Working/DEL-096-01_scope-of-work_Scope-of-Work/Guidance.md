# Guidance — DEL-096-01 Scope of Work (PKG-096 Tanks, Sour Condendate (API 650))

## Purpose

This document explains the intent, principles, and judgement calls behind the EPC Scope of Work for PKG-096. The Scope of Work is the EPC Integrator's anchor for handing the Sour Condensate tank package across the EPC/Package Vendor boundary while keeping facility integration explicit. It exists to:

- name and bound the package (tags, function, source basis);
- assign responsibility between EPC Integrator and Package Vendor;
- preserve safety, code, and interface constraints from the source so they are not lost when the package is procured.

Source: `_CONTEXT.md` Scope; OBJ-004; SOW-0217..SOW-0220.

## Principles

1. **Source fidelity over convention.** Equipment counts, capacities, codes, and "by others" assignments come from the package source text (`26020-Package_Requirements.docx` package heading 48), not from typical tank-farm conventions.
2. **Vendor/EPC split is non-negotiable.** Per OBJ-004, the Package Vendor owns engineering, design, fabrication, and supply; the EPC Integrator owns facility integration and the explicit "by others" items.
3. **Sour service is a primary design driver.** API 650 (modified), API 2000 venting, NACE compliance, internal coating, PVRV/EPRV, and VRU header connection are all consequences of sour-service H2S handling and must propagate to every downstream deliverable.
4. **Conflicts are surfaced, not resolved silently.** Where source slices disagree, this guidance flags them in the Conflict Table below for human ruling, rather than picking a value.
5. **Decomposition narrative routes; sources determine values.** The decomposition register and SCOPE_LEDGER rows map this deliverable to objectives and downstream deliverables, but design values come only from the package source text.

## Considerations

- **Source basis (RFQ) is not locally accessible.** The package source text cites `Bid Docs/Budgetary/26020-03-PT-RFQ-19-005 - Sour Conde Tanks.docx` as the basis for tank scope. That RFQ is not in the locally accessible `_Sources` tree. Clause-level requirements (e.g., specific API 650 modifications, exact NACE document) cannot be reproduced here and remain `TBD` or `ASSUMPTION` until the RFQ is read.
- **"Sour Condendate" vs "Sour Condensate" spelling.** The package name in the decomposition uses "Condendate" (sic). The source document and the tank tag context use "Condensate". This is treated as a register-side typo, not a scope split.
- **Item No. 2 values appear in source row text but not in basic scope.** SOW-0220 includes design flow and operating temperature for "Item No. 2" although the Major Included Equipment lists only Item No. 1 (two 3800 bbl tanks). Recorded as CFL-001.
- **Building Item No. 1 has "Ambient" operating temperature.** No numeric operating temperature was provided for Item No. 1; ambient site temperature conditions are an `ASSUMPTION`.

## Trade-offs

- **Tighter scope vs. interface coverage.** This SoW intentionally restates the package interface applicability matrix because PKG-096 is a tank package — sour-service relief/vent, secondary containment, grounding/bonding, and cathodic protection are operationally as important as the tank shells themselves.
- **Carrying companion-deliverable references.** Listing DEL-096-02..06 inside Specification REQ-9 risks scope creep, but the alternative (silent ownership) would let the EPC/Package Vendor boundary slip. The reference is anchor-only, not authoring.
- **Conflict avoidance vs. completeness.** Where source rows disagree (e.g., CFL-001), the Specification carries only the Item No. 1 values and the Conflict Table preserves the Item No. 2 strings as evidence pending ruling.

## Examples

- **Sour-service venting chain.** A change to the VRU header connection on either tank propagates from this SoW (REQ-4) into DEL-096-02 (Package Datasheet relief schedule) and into the Relief/Flare/Vent interface artifacts produced by adjacent packages.
- **By-others foundations.** Because SOW-0220 puts foundations "By others", the Construction Work Package (DEL-096-03) — owned by the EPC Integrator — must include foundation design and installation as facility scope rather than expecting the Package Vendor to deliver them.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-001 | "Item No. 2" design flow (94,940 kg/h / 3187 Am3/d) and operating temperature (5 °C / 40 °C) appear in package "Scope Notes / Open Items" text, but the package "Basic Scope" and "Major Included Equipment" enumerate only Item No. 1 (two 3800 bbl Sour Condensate tanks, TK-9110-2 / TK-9120-2). | SCOPE_LEDGER SOW-0220 + 26020-Package_Requirements.docx heading 48 / Scope Notes & Open Items | 26020-Package_Requirements.docx heading 48 / Basic Scope and Major Included Equipment | Datasheet (Conditions); Specification REQ-6 | PROPOSAL: treat "Item No. 2" text as RFQ template carryover from an adjacent condensate package; carry only Item No. 1 values in PKG-096 until the underlying RFQ is read. | TBD |
| CFL-002 | Package decomposition name "Tanks, Sour Condendate (API 650)" vs. source-document spelling "Tanks, Sour Condensate". | Decomposition: PACKAGE_REGISTER / DELIVERABLE_REGISTER name field | `26020-Package_Requirements.docx` heading "26020-03-PT-19-005 - Tanks, Sour Condensate" | Datasheet (Identification); all docs referring to package name | PROPOSAL: treat "Condendate" as a register-side typo; production documents may use the source spelling "Condensate" when describing the physical package, while preserving the register-side name verbatim in identity blocks. | TBD |
| CFL-003 | Specific NACE standard (e.g., MR0175) is not named in source slice; "NACE compliant" is stated without document identifier. | 26020-Package_Requirements.docx heading 48 / Major Included Equipment | (none — not stated locally) | Specification Standards table; Datasheet Construction | PROPOSAL: cite "NACE compliance" as required, with the specific document (NACE MR0175 ASSUMPTION) deferred to the RFQ (`26020-03-PT-RFQ-19-005`) when accessible. | TBD |
| CFL-004 | DCS integration ownership is asserted from analogous PKG-019 text ("By others: DCS integration ...") and not stated for PKG-096. | Specification Out of Scope (analogy from `26020-Package_Requirements.docx` PKG-019 Scope Notes) | `26020-Package_Requirements.docx` heading 48 / Scope Notes & Open Items (does not state DCS integration) | Specification Out of Scope | PROPOSAL: keep DCS integration as EPC Integrator scope by ASSUMPTION until confirmed in the RFQ or controls deliverable. | TBD |
