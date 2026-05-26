# Guidance — Construction Work Package (DEL-054-03)

## Purpose

This Guidance explains the rationale, principles, and trade-offs behind the Construction Work Package (CWP) for **PKG-054 Flare KO Drum (High Pressure) 4-25**. It complements the normative Specification by giving construction planners and the EPC Integrator the design intent and the supporting reasoning so that field decisions during installation and tie-in stay aligned with the DBM and the Gate 5 turnover expectations.

The CWP exists because the 04-25 Deepcut HP flare KO drum (V-4100-1) and transfer pump (P-4100-1) are delivered to site as a shop-fabricated module (410-1) per the DBM's Modularization table, and the EPC Integrator must convert that shipped module plus surrounding civil, electrical, instrumentation, and piping interfaces into an operating, inspected, and turned-over installation.

## Principles

1. **Vendor-EPC split (OBJ-004).** The Package Vendor owns shop fabrication of Module 410-1; the EPC Integrator owns site placement, tie-ins, inspection, and turnover. Construction decisions should preserve, not redo, vendor design intent. When in doubt, escalate to the EPC interface review, not to field modification.
2. **DBM is the authority for flare-system constraints.** Spacing (10 m to vegetation/fire hazards), heat tracing, header sizes, materials, and backpressure ceilings are set by the DBM. Construction field-fits must not erode these envelopes.
3. **Modular shop fabrication preserves quality.** Whenever a Module 410-1 sub-assembly can be tested in-shop, do so; site work should focus on the few tie-ins that cannot be pre-tested.
4. **Sour-service safety carries through (OBJ-009).** Hydrocarbon and sour-service relief paths must remain intact at all times during turnover; bypasses, blinds, and isolation states must be tracked in writing.
5. **Turnover evidence is the deliverable (OBJ-010).** A complete and well-organized turnover package is the construction product, not just a built asset. Treat documentation as part of the workface plan, not an afterthought.

## Considerations

- **Sequencing relative to civil packages.** Foundation acceptance from the relevant earthworks/grading package must precede module set. Coordinate hand-off with the civil deliverable schedule (DBM External Dependencies section flags civil inputs as required).
- **Header heat tracing.** HP flare headers outside heated buildings require electric heat trace and insulation; PSV outlets that free-drain into the header are explicitly exempted (DBM). Construction should confirm the exemption per line before omitting heat trace, not by inference.
- **Backpressure preservation.** The estimated peak HP/cryo built-up backpressure is 695 kPag (100 psig), with PSV flange maximum kept below 1172 kPag (170 psig). Field-routing changes (extra elbows, rerouting around obstructions) can erode this margin and should be reviewed by process engineering before execution.
- **Spacing at site.** OGAOM Sec. 9.6.15 distances apply to the entire flare/KO drum complex; the CWP should verify that the as-installed module location, not just the planned location, meets the 10 m clearance to vegetation and other fire hazards.
- **Common HP/cryo stack ownership.** The HP/cryo stack is at 03-25 and shared. Tie-ins from V-4100-1 outlet into the combined HP/cryo header pass a facility boundary; ownership and inspection responsibility across the boundary should be explicit on the construction interface checklist.

## Trade-offs

- **Field tie-in count vs. module size.** Larger shop modules reduce field work but increase transport and lift complexity. Module 410-1 is designated Shop per DBM; the CWP should not redesign that scope, but lift planning (R-054-03-11) is a meaningful trade-off zone.
- **Hydrostatic vs. pneumatic testing.** Hydrostatic test is standard but introduces water in a service where water is intentionally minimized. Construction may negotiate test approach with process engineering and code requirements; record the chosen approach and rationale (TBD per project).
- **Pre-commissioning energization sequence.** Heat trace, instrumentation power, and pump electrical loads have different readiness gates. Sequencing these so each can be loop-checked without interfering with others is a workface planning trade-off.

## Examples

The DBM identifies parallel HP/LP/cryo KO drum modules at 4-25:
- Module 390-1 (LP Flare KO Drum, V-3900-1, P-3900-1) — Shop
- Module 410-1 (HP / Cryo Flare KO Drum, V-4100-1, P-4100-1) — Shop (this package)
- Module 691-1 (Incinerator KO Drum) — Shop

These share installation patterns (shop module + site tie-ins + truck-out + heat trace + radiation envelope), and lessons learned from one should be available to construction planning for the others. Cross-reference is informational; this CWP governs PKG-054 only.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-054-03-01 | Detailed package heading 9 of 26020-Package_Requirements.docx is cited as a basis but its text was not accessible to this run; some construction-specific document expectations may therefore be missing. | _CONTEXT.md "Source Reference" | Available DBM text slice | Specification.Documentation; Datasheet.References | PROPOSAL: confirm/parse the .docx heading 9 in a follow-up source-slice extraction pass and merge into Specification.Documentation before Gate 5. | TBD |
| C-054-03-02 | "Construction work package" appears as both a package-level concept and as an anticipated artifact label, which can confuse whether this deliverable IS the CWP or merely produces it. | _CONTEXT.md anticipated artifacts | Decomposition row 55 narrative | Datasheet/Specification framing | PROPOSAL: treat this deliverable AS the CWP; the "installation and tie-in workface plan" and "construction interface and turnover checklist" are sub-artifacts captured under Procedure and Specification.Documentation. | TBD |
