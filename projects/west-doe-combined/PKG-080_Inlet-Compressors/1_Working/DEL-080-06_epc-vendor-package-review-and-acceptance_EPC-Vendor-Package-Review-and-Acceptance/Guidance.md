# Guidance — DEL-080-06 EPC Vendor Package Review and Acceptance

## Purpose

DEL-080-06 exists to make the EPC Integrator's review-and-acceptance of the vendor-engineered Inlet Compressors package (PKG-080) visible, auditable, and traceable to the EPC Scope of Work, Package Datasheet, and Construction Work Package. Per OBJ-004, electrical and mechanical packages are vendor-engineered and vendor-supplied; the EPC Integrator does not redo that work — it reviews and accepts it, and integrates it into the facility. This deliverable is the evidence record that the EPC has done that review and accepted (or conditionally accepted, or rejected) the vendor's package.

## Principles

- **Vendor/EPC split is non-negotiable.** Per OBJ-004 and the PKG-080 register row, the Package Vendor owns engineering, design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination. This deliverable evidences the integration-side acceptance, not vendor engineering rework.
- **Source authority over convention.** Acceptance dispositions cite the EPC Scope of Work, Package Datasheet, Construction Work Package, and DBM sources (where locally accessible). When source location is not locally accessible, the citation is preserved with `location TBD` rather than substituted with generic convention.
- **Interface-completeness.** Every interface type declared for PKG-080 in `PACKAGE_REGISTER.csv` is in scope for verification. Silence on an interface is not acceptance.
- **OBJ-010 closure mindset.** Acceptance is not just "documents received" — it is open-item closure, sparing/isolation/access posture, vendor-document completeness, commissioning/turnover readiness, and controlled handoff evidence.
- **Conservative inference.** Where source detail is unavailable, mark `TBD` or `ASSUMPTION` rather than filling with plausible-sounding values.

## Considerations

- **Sour service.** SOW-0122 makes NACE-compliant materials and seals an explicit requirement. Acceptance review should not waive or interpret this — the vendor's material and seal selection records must support the requirement explicitly.
- **No dedicated spare.** The 2 x 50% configuration with no dedicated spare elevates the importance of reliability evidence, maintenance access, and isolation provisions for one-train-out operation. Maintenance Access is one of the declared interface types and warrants explicit attention.
- **Approximate operating envelope.** Suction ~1275 kPag, discharge ~6550 kPag, and combined ~80 MMSCFD are *approximate* values per SOW-0122; the acceptance record should reference the vendor's as-engineered values (TBD against vendor documentation) rather than restating the approximate workbook figures as performance commitments.
- **Multi-objective coverage.** PKG-080 carries OBJ-002, -003, -004, -005, -006, -007, -008, -009, -010 per `OBJECTIVE_DELIVERABLE_MAP.csv`. The acceptance evidence set should be structured so each of these objectives can be cited as substantively addressed — typically through the interface verification matrix (OBJ-005..008), the safety/regulatory review (OBJ-009), and the open-item/turnover record (OBJ-010). ASSUMPTION: package-heuristic objective association per brief (`OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC`).
- **Reciprocating compressor specifics.** Ariel KBZ/6 reciprocating compressors with intercooling/aftercooling have specific vibration, pulsation, and PSV/PRV/blowdown design considerations. These should be reviewed against the vendor's package engineering and the relevant DBM section (location TBD — local DBM slice not copied for this deliverable).
- **Modular self-framing buildings.** The package supplies its own building enclosures; this drives Building HVAC / Services, Fire & Gas / Safety Systems, Area / Exterior Lighting, and Structural / Foundations / Supports interface scope that must be coordinated with EPC facility-level systems rather than duplicated.

## Trade-offs

- **Depth of review vs. schedule.** Comprehensive vendor-document review is the strongest acceptance evidence but is time-consuming; risk-prioritized review (sour-service materials, safety/relief, controls cause-and-effect) is a common compromise. Both approaches should make their basis explicit in the acceptance checklist.
- **Conditional acceptance vs. NCR.** Outstanding items can be carried as conditional-acceptance open items or as NCRs against the vendor; choice affects who owns closure. The acceptance record should make the disposition basis explicit.
- **Single composite acceptance vs. per-artifact acceptance.** PKG-080 has two identical parallel packages; per-unit acceptance preserves per-asset traceability while composite acceptance is lighter. Per-unit traceability is generally preferred for OBJ-010 handoff evidence.

## Examples

Source-grounded examples cannot be drawn from local artifacts at this draft pass because no deliverable-specific source slices have been copied to this deliverable (`_REFERENCES.md` Missing / Deferred References). Worked examples are deferred — `TBD` until source slices or vendor turnover materials are available locally.
