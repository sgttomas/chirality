# Guidance: DEL-061-03 — Construction Work Package (NGL Booster and Transfer Pumps Building)

## Purpose

This guidance explains why the Construction Work Package (CWP) exists for PKG-061 and how to use it when authoring or reviewing the deliverable. It is directional: it does not replace the Specification's normative requirements or the Procedure's operational steps.

The package itself is a Package-Vendor-engineered, EPC-Integrated production unit: two parallel LPG booster pumps (P-9570-1 / P-9580-1) supplied as a packaged building with skid, piping, instrumentation, electrical, HVAC/enclosure, and commissioning support. The CWP is the EPC Integrator's instrument for translating the vendor package into a built and turned-over part of the facility. (Source: SCOPE_LEDGER.csv SOW-0149/0150/0151; PACKAGE_REGISTER.csv row for PKG-061.)

## Principles

- **EPC owns integration, not equipment design.** The vendor package (DEL-061-04) provides equipment; the CWP defines how that equipment becomes part of the facility. Boundary explicitness is more important than redoing vendor design intent. (Source: PACKAGE_REGISTER.csv row for PKG-061 description.)
- **Source-anchored, register-keyed.** Each construction-relevant claim should trace either to the deliverable register, scope ledger, package register, interface register, or an extracted source slice (e.g., DBM-Deepcut). Where a clause is referenced but not extracted, mark `location TBD` rather than paraphrasing from memory.
- **TBDs are first-class.** Source materials explicitly leave TDH, materials-class details, and field environment values open; the CWP should carry these forward as resolution items rather than backfilling assumed values.
- **Interface completeness over interface depth.** The thirteen interface types in the PKG-061 package register should each appear in the CWP at least at the checklist level, even where the interface is trivial; missing an interface category creates turnover risk. (Source: PACKAGE_REGISTER.csv row for PKG-061.)
- **Modular delivery shapes the workface plan.** Because the vendor module ("950-1 LPG Booster and Transfer Pump Module") is shop-assembled, the workface plan is dominated by foundation readiness, set-and-tie-in sequencing, and utility connection logistics rather than in-field fabrication. (Source: DBM-Deepcut/4-25_Deepcut_DBM.md row 2818.)

## Considerations

- **LPG service.** The pumps move LPG to the LACT unit; hazardous-area classification, fire and gas detection, relief routing, and drain/containment design require specific attention even though the source slices accessible here do not provide clause-level requirements. The CWP should explicitly flag where it relies on the vendor's classified-area design vs. EPC scope. (Source: SCOPE_LEDGER.csv SOW-0150; PACKAGE_REGISTER.csv interface list for PKG-061; `location TBD` for clause-level hazardous area text.)
- **EHT and freeze protection.** EHT is a listed package interface but no PKG-061-specific freeze-protection requirements are stated in the accessible source slices; the CWP should preserve EHT as a designed interface with vendor/EPC boundary called out. (Source: PACKAGE_REGISTER.csv interface list for PKG-061.)
- **Foundations and MCC supply are EPC scope.** SOW-0152 is explicit that DCS integration, foundations, and electrical supply to MCC are "by others." The CWP should be the primary place this boundary is operationalized for construction. (Source: SCOPE_LEDGER.csv SOW-0152.)
- **API 610 receipt expectations.** The pumps are API 610 vertical multistage can-type with seal plan 13/52; the CWP should expect API 610 acceptance practices at receipt, even though the deliverable's local source slices do not extract API 610 clause text. (Source: SCOPE_LEDGER.csv SOW-0151; ASSUMPTION on clause-level applicability.)
- **Commissioning support is vendor-included.** Construction completion and commissioning are bridged by vendor-provided commissioning support called out in SOW-0151; the CWP commissioning hand-off planning should respect this. (Source: SCOPE_LEDGER.csv SOW-0151.)
- **Sparing pattern.** The DBM sparing table shows the C3/C4 LPG LACT Booster Pump as 2 x 100% (200% installed), which is consistent with the two-pump basic scope in SOW-0150. ASSUMPTION: this DBM row corresponds to the PKG-061 booster duty; if the human confirms otherwise, the implied "any-one-out" operability assumption in the CWP needs re-examination. (Source: DBM-Deepcut/4-25_Deepcut_DBM.md row 2338.)

## Trade-offs

- **Detail now vs. resolve-later.** The CWP can either populate provisional values for known TBDs (TDH, materials) or carry them as open items. Preferring `TBD` keeps the deliverable honest until DEL-061-02 (Package Datasheet) and DEL-061-04 (Vendor Engineered Equipment Package) supply authoritative values.
- **Workface plan granularity.** A heavier workface plan reduces field improvisation but increases authoring and review cost; for a vendor-modular pump building the natural granularity is interface-by-interface tie-in steps, not fabrication-step decomposition.
- **Interface checklist vs. interface design.** The CWP is a construction artifact, not a design artifact. Where an interface needs design rather than just installation, the CWP should reference the upstream design deliverable rather than embed design content.

## Examples

- *Foundation tie-in record entry.* "Foundation grout verified to 28-day strength; anchor bolt extension within tolerance; level confirmed before pump module set; reference: DEL-061-02 Package Datasheet weights and base plate drawing (TBD pending vendor data)."
- *Electrical interface entry.* "MCC feeder to package: cable size and termination per EPC electrical drawings; 575 V / 3 ph / 60 Hz verified at package terminal box prior to bump test. (Source: SCOPE_LEDGER.csv SOW-0151 drive basis; SOW-0152 supply-to-MCC ownership.)"
- *DCS integration interface entry.* "Package PLC / instrumentation signals mapped to facility DCS per I&C drawings; loop checks complete before commissioning support handoff. (Source: SCOPE_LEDGER.csv SOW-0152.)"

## Conflict Table (for human ruling)

No source conflicts requiring human ruling were identified in this drafting run. The DBM-Deepcut sparing-table reference to the "C3/C4 LPG LACT Booster Pump" is treated as the same duty as PKG-061 based on tag mapping (DBM-Deepcut row 2609 maps PKG-061 to tags P-9570-1/P-9580-1) and is recorded as an ASSUMPTION rather than a CONFLICT.
