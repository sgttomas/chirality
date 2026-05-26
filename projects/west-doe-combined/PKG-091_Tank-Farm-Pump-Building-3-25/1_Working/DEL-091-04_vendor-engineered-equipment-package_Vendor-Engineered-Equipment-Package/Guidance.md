# Guidance — Vendor Engineered Equipment Package (DEL-091-04)

## Purpose

This deliverable exists so that the Package Vendor produces a coherent, integration-ready pump building package for the 3-25 Tank Farm — a vendor-engineered production unit grounded in the EPC Scope of Work (`DEL-091-01`) and EPC Package Datasheet (`DEL-091-02`), and accepted by the EPC Integrator under `DEL-091-06`. (Source: DELIVERABLE_REGISTER row 471; PACKAGE_REGISTER row 84.)

The vendor is the engineering authority for the package internals; the EPC Integrator is the integration authority for the facility-level interfaces.

## Principles

1. **Vendor owns package; EPC owns facility integration.** The vendor produces the package design basis, package datasheet, and physical equipment. The EPC Integrator does not redesign the vendor package, and the vendor does not redesign the facility around the package. (Source: PACKAGE_REGISTER row 84.)
2. **Source-grounded design basis.** Design values come from the EPC Package Datasheet (`DEL-091-02`) and the 3-25 DBM. Where source values are missing locally (e.g., site-specific seismic, area classification breakdown), the vendor shall request them from the EPC Integrator and not infer them silently.
3. **Single coordinated package boundary.** Each interface type listed in `Datasheet.md` Construction has one defined termination on the vendor package. Multiple termination points within one interface type require an explicit interface drawing.
4. **Do not reintroduce removed functions.** The SCA basis has removed local 3-25 stabilization, local SOC, condensate dehydration, local instrument-air compression, and local heat-medium. Vendor design shall not add these. (Source: DBM 3-25 lines 65–68, 366, 442.)
5. **Sour service discipline.** Streams handled (produced water, sour condensate, condensate-sweetening feed) require sour-service materials, seal selection, and venting/relief consistent with site sour gas/liquids basis. Specific NACE/MR0175 clause selection: `TBD` (vendor design basis).

## Considerations

- The pump building houses all pumps for the tank farm (PACKAGE_REGISTER row 84). Layout and maintenance access should be coordinated early with grading/spill-containment (interface type listed in PACKAGE_REGISTER row 84).
- The water transfer pumps draw through a bag filter — filter housing pressure drop, change-out access, and isolation must be reflected in the pump suction sizing.
- The sour condensate pumps feed the sweetening feed pumps, which feed the non-regenerative caustic mercaptan treating package. The sweetening feed pumps' duty point should be coordinated against the treating package's 20,000 bbl/d throughput (DBM 3-25 line 389) plus the upstream sour-condensate storage and recycle architecture (DBM 3-25 lines 406–417). ASSUMPTION: vendor will use the EPC Package Datasheet as the binding sizing source.
- VFD/soft-start vs. across-the-line motor starting impacts the Electrical Power interface and the Tank Farm Pump Building 3-25 electrical scope; defer to EPC Package Datasheet.

## Trade-offs

- **Vendor-standard pumps vs. fully custom-engineered pumps.** Vendor-standard equipment minimizes cost and schedule but may compromise interface optimization. The 3-25 DBM and PACKAGE_REGISTER do not prescribe a preference; defer to the EPC Scope of Work and Package Datasheet. (ASSUMPTION: preference unresolved.)
- **Local instrumentation/control on the package vs. routed back to facility DCS.** Tighter package autonomy improves vendor testability; tighter facility integration improves operability. Interface split is decided by the EPC Package Datasheet I&C interface section (location TBD).
- **Spare parts philosophy.** `2 x 100 percent` configurations on produced-water transfer and water transfer service (DBM 3-25 line 429) reduce required spare parts inventory but increase capital. The DBM basis is `2 x 100 percent`; do not reduce.

## Examples

`TBD` — no example vendor packages cited in locally accessible source slices. The Tank Farm Pump Building 4-25 (PKG-060) is a structurally similar deliverable and may be used as a reference for delivery shape but not for sizing values (different service basis).

## Conflict Table (for human ruling)

| ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-091-04-001 | Pneumatic vs. centrifugal drain pump | PACKAGE_REGISTER row 84: "1 Building Drain Pump, pneumatic diaphragm" | None observed; no conflicting source | Datasheet Attributes | PACKAGE_REGISTER row 84 governs (FACT). | TBD |
| C-091-04-002 | Standards list completeness | Specification §Standards (ASSUMPTION list) | `26020-Package_Requirements.docx` heading 44 (not locally accessible) | Specification §Standards | EPC Package Datasheet (`DEL-091-02`) shall govern once issued. | TBD |
| C-091-04-003 | Sweetening feed pump sizing basis | DBM line 389 (20,000 bbl/d treater throughput) | EPC Package Datasheet (`DEL-091-02`, not yet issued) | Specification R5; Datasheet Conditions | EPC Package Datasheet governs upon issuance. | TBD |
