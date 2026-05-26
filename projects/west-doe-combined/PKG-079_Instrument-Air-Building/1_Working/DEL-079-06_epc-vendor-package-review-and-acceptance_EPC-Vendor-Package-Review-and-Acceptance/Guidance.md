# Guidance — DEL-079-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable closes the EPC Integrator's review loop on the PKG-079 Instrument Air Building vendor package. It is the auditable evidence layer that connects (a) the EPC-authored basis (DEL-079-01 Scope of Work, DEL-079-02 Package Datasheet, DEL-079-03 Construction Work Package) to (b) the vendor-owned outputs (DEL-079-04 Vendor Engineered Equipment Package, DEL-079-05 Vendor Document Turnover Package). It exists so that handoff readiness is demonstrated, not assumed. Source: DELIVERABLE_REGISTER PKG-079; `_CONTEXT.md` Scope and Notes.

## Principles

- **Acceptance is traceable, not narrative.** Every accepted item points back to a SOW-0131..SOW-0134 row, a Package Datasheet requirement, an interface ID, or an explicitly listed vendor document. Source: SCOPE_LEDGER; INTERFACE_REGISTER PKG-079; ARTIFACT_REGISTER PKG-079.
- **The EPC owns integration; the Vendor owns the package.** The acceptance lens here is *fitness for integration into the process facility*, not redesign of the vendor's package. Source: PACKAGE_REGISTER PKG-079 ownership note; SCOPE_LEDGER SOW-0131.
- **Interfaces are first-class acceptance objects.** Because PKG-079 declares ten interface types as YES in the workbook, no acceptance is complete until each interface has a closure disposition. Source: INTERFACE_REGISTER IFC-E7D3353482 .. IFC-0EC9E5E722.
- **Source slices govern; decomposition narrative routes.** Acceptance criteria that touch design values (pressures, dew point, equipment counts) are derived from the SOW/source rows, not paraphrased from the decomposition. Source: SCOPE_LEDGER SOW-0132..SOW-0134.

## Considerations

- **By-others items are not vendor failures.** SOW-0134 expressly carves out shipping, installation on piles, tie-in piping, electrical connections, mounting platform, and stairs as "by others." Reviewers should not flag absence of these on the vendor's side; instead, confirm they appear in the EPC Construction Work Package (DEL-079-03). Source: SCOPE_LEDGER SOW-0134.
- **Dryer sizing and dry-receiver topology are vendor-degree-of-freedom.** SOW-0133 explicitly defers dryer size/capacity and allows the dry receiver to be 1 vessel or 2 x 50%. Acceptance should confirm the vendor's chosen topology matches the as-issued Package Datasheet revision and is internally consistent with compressor turn-down and downstream flow. Source: SCOPE_LEDGER SOW-0133.
- **Driver speed is vendor-determined.** Acceptance should not assert a target motor RPM unless the EPC Package Datasheet has fixed one. Source: SCOPE_LEDGER SOW-0134.
- **PSV setting (948 kPag / 137.5 psig) is a hard-coded source value.** Any vendor PSV nameplate differing from this must be raised as a non-conformance, not silently accepted. Source: SCOPE_LEDGER SOW-0133.

## Trade-offs

- **Acceptance breadth vs. timeline.** Exhaustive line-by-line review of every vendor document extends schedule; minimal review increases turnover risk. Recommended bias: deep review on safety-relevant items (PSV, dew point, electrical classification, F&G interface) and lighter review on commercial/administrative documents. Rationale TBD against any project-specific risk policy (not in accessible sources).
- **Pre-shipment vs. site acceptance.** FAT findings can be resolved at the vendor's shop; SAT findings are remedied with construction crews on-critical-path. Push verification of PSV setting and dryer dew-point performance into FAT where vendor scope permits. ASSUMPTION: project allows FAT witness; no explicit FAT/SAT split is stated in accessible source slices.
- **Open vs. closed comment loops.** Accepting vendor documents "with comments" preserves schedule but creates a comment-resolution debt that must be tracked through turnover; rejecting forces rework but yields a cleaner turnover package.

## Examples

(Drawn from the accessible source set; no fabricated examples.)

- Acceptance row: "PSV setpoint of each package PSV verified as 948 kPag (137.5 psig) — source: SOW-0133; evidence: Vendor PSV data sheet rev __, item __ — disposition: ACCEPTED / ACCEPTED WITH COMMENTS / REJECTED."
- Interface closure row: "IFC-47DC520AA2 Electrical Power — closure evidence: vendor electrical termination drawing rev __ matches DEL-079-02 electrical interface requirement; closure status: CLOSED."
- Vendor document row: "Vendor Document Index (ART-F8BF3DB9AA / source ID PRQ-009) — received rev __; review disposition: ACCEPTED; comments: none."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|

No conflicts identified at Pass 1/Pass 2 between accessible source slices (SCOPE_LEDGER SOW-0131..SOW-0134, INTERFACE_REGISTER PKG-079, ARTIFACT_REGISTER PKG-079, PACKAGE_REGISTER PKG-079) and `_CONTEXT.md` / decomposition narrative.
