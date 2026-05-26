# Guidance — DEL-053-06: EPC Vendor Package Review and Acceptance (Flare KO Drum (Cryo))

## Purpose

This deliverable exists so that the EPC Integrator can demonstrate, with evidence, that the Package Vendor's engineered Flare KO Drum (Cryo) package has been reviewed against the EPC source-of-truth deliverables (Scope of Work, Package Datasheet, Construction Work Package) and is ready for facility integration and downstream commissioning. Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` DEL-053-06.

The package is mechanical-discipline cryogenic service: the cryogenic flare KO drum V-4110-1 and its immersion heater H-4112-1 collect liquids dropping out of the cryogenic relief header and vaporize/maintain them as part of the flare system. The drum sees PSV reliefs from cryogenic-unit and molecular-sieve-dehydrated systems below -45.5 degC. Source: `4-25_Deepcut_DBM.md` §Flare Equipment and Routing; `SCOPE_LEDGER.csv` SOW-0070.

## Principles

1. **EPC documents are the acceptance datum.** Vendor documents are reviewed against the EPC Scope of Work (DEL-053-01), Package Datasheet (DEL-053-02), and Construction Work Package (DEL-053-03). Disagreements are resolved in favor of the EPC datum unless a formal change is processed. Source: `DELIVERABLE_REGISTER.csv` DEL-053-06.

2. **Acceptance does not transfer responsibility.** Acceptance evidence records EPC Integrator review and integration acceptance; it does not relieve the Package Vendor of engineering, design, fabrication, or documentation responsibility under PKG-053. Source: `PACKAGE_REGISTER.csv` PKG-053.

3. **Interface-by-interface acceptance.** Facility-level integration is acceptance-scope; each PKG-053 interface type (Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; I&C/Control Cabling; Maintenance Access; Structural/Foundations/Supports) receives a discrete acceptance line. Source: `PACKAGE_REGISTER.csv` PKG-053.

4. **Cryogenic service is the controlling design constraint.** The drum's low-temperature exposure (relief below -45.5 degC, non-sour) frames the review of materials, MDMT, impact testing, and interface design (e.g., no header heat trace, since water is not expected in the cryogenic flare system). Source: `4-25_Deepcut_DBM.md` §Flare Equipment and Routing.

5. **Traceability beats narrative.** Each acceptance checklist line traces to a source clause; narrative summaries without traceability do not constitute acceptance evidence.

## Considerations

### Reviewing the Vendor Engineered Equipment Package (DEL-053-04)

- Verify that vendor design conditions envelope the EPC Datasheet (DEL-053-02) and that MDMT, materials, and impact testing are consistent with cryogenic service.
- Verify equipment identity: V-4110-1 (KO drum) and H-4112-1 (immersion heater) appear with correct tag numbers, sizes, and ratings.
- Verify that the 610 mm (24 in) cryogenic relief header connection is accommodated and that the downstream tie-in to the combined HP/cryo header is consistent with project routing.

### Reviewing the Vendor Document Turnover Package (DEL-053-05)

- Confirm the vendor document register contains every required submittal and that submittals have been reviewed to a status that supports turnover (e.g., Code 1/Code 2 in typical EPC review codes — exact codes are governed by project document control; ASSUMPTION absent explicit source).
- Confirm MTRs, NDE reports, hydrotest/pressure test records, and welding records are present and signed.
- Confirm preservation, packing, and storage records exist for field receipt and pre-installation care.

### Reviewing Construction Work Package Readiness (DEL-053-03)

- Confirm rigging plan, foundation/support drawings, and tie-in isometrics are consistent with the as-fabricated vendor package.
- Confirm hot-work, lifting, and confined-space considerations are addressed for installation.
- Confirm the turnover checklist tied to mechanical completion is populated and ready to be executed at delivery.

### Cryogenic-specific review considerations

- Material toughness and MDMT verification (ASSUMPTION: ASME Section VIII impact-testing rules apply; verify via DEL-053-02).
- Avoidance of trapped water; confirm that internal coatings, drains, and dry-out provisions are appropriate to a service designated non-sour and not heat-traced. Source: `4-25_Deepcut_DBM.md` §Flare Equipment and Routing.
- Immersion heater H-4112-1: confirm electrical area classification, watt-density limits suitable for liquid hydrocarbon vaporization service, and interlocks. Specific values are `TBD` pending DEL-053-02 access.

### Backpressure and relief-system fit

- Verify that vendor inputs and outputs are consistent with the project HP/cryo flare backpressure envelope (preliminary built-up 695 kPag during peak coincident blowdown; PSV maximum total backpressure < 1172 kPag under 150# flange rating). Source: `4-25_Deepcut_DBM.md` §Flare Radiation Criteria preface.
- Detailed-engineering verification of actual built-up backpressure is a downstream activity; acceptance need only confirm vendor consistency with the project basis or document accepted deviations.

## Trade-offs

- **Strict-traceability vs. schedule:** A traceability-by-line acceptance is auditable but slower than a narrative acceptance memo. The traceability approach is preferred because acceptance evidence is the only durable proof of EPC integration review under PKG-053.
- **Accept with conditions vs. punchlist vs. reject:** Conditions allow integration to proceed with documented residual risk; punchlist defers items to resolution before turnover; reject requires vendor rework. Choose the lowest-impact disposition that still preserves the EPC source-of-truth datum.
- **Interface acceptance granularity:** Per-interface sign-off (PKG-053 lists nine interface types) is more durable than a single facility-integration sign-off but is heavier on review labor.

## Examples

Specific worked examples are not included in accessible sources and are not synthesized here. Representative line types (illustrative only, not asserted as project examples):

- "Material MDMT for V-4110-1 shell SHALL envelope -45.5 degC plus design margin per ASME BPVC Section VIII Div. 1 UCS-66 / UHA-51" — ASSUMPTION pending DEL-053-02 access.
- "Cryogenic relief header tie-in: 610 mm OD, 304SS material, no heat trace, per DBM §Flare Equipment and Routing."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-053-06-01 | `_REFERENCES.md` notes "No deliverable-specific source slices copied during PREPARATION." The skill requires locally accessible source slices for source fidelity. | `_REFERENCES.md` Missing/Deferred References | `skills/four-documents/SKILL.md` Step 1.5 | All four documents | Treat decomposition CSVs and `4-25_Deepcut_DBM.md` as the accessible mediated source set; mark docx/xlsx-only specifics as `TBD`. | TBD |
| C-053-06-02 | Objective association uses PACKAGE_HEURISTIC; `_CONTEXT.md` lists OBJ-001/004/005/006/007/008/009/010 but accessible OBJECTIVE_SCOPE_MAP rows verify only via package-grouped extraction. | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_SCOPE_MAP.csv` (package-grouped) | Datasheet Identification; Guidance Purpose | Retain `_CONTEXT.md` listing labeled ASSUMPTION (best-effort mapping). | TBD |
| C-053-06-03 | Detailed test/inspection list and immersion heater specifics are unavailable in accessible sources. | accessible source set | DEL-053-02 (not yet accessible to this draft) | Datasheet Conditions; Specification REQ-09; Procedure Steps 4 and 7 | Mark as `TBD` and resolve when DEL-053-02 is drafted. | TBD |
