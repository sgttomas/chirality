# Guidance — DEL-017-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable produces the EPC Integrator's evidence of having reviewed the PKG-017 vendor package and accepted it as ready for integration handoff. It exists because PKG-017 is a vendor-owned Electrical package whose engineering, design, fabrication, and physical equipment are produced by the Package Vendor (see DEL-017-04 and DEL-017-05), while integration into the functional process facility is owned by the EPC Integrator. (Source: Gate 7 `PACKAGE_REGISTER.csv` row PKG-017.)

## Principles

- **Acceptance is evidence, not certification.** This deliverable records EPC Integrator review and acceptance disposition. It does not constitute binding approval; binding approval is a separate human action. (Source: governance principle stated in the parent repo's CONTRACT; agent shells may not certify.)
- **Acceptance is anchored to accepted upstream snapshots.** Each review item cites the accepted revision of the EPC SOW (DEL-017-01), Package Datasheet (DEL-017-02), Construction Work Package (DEL-017-03), and the vendor production unit (DEL-017-04) and turnover package (DEL-017-05). (Source: `_CONTEXT.md` Scope.)
- **Coverage tracks the declared interface surface.** The acceptance checklist works through each PKG-017 interface type: Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports. (Source: Gate 7 `PACKAGE_REGISTER.csv` row PKG-017.)

## Considerations

- The PKG-017 source basis (3-25 DBM) explicitly defers VFD sizing, harmonics, and reactive-power mitigation to detailed electrical studies (SCA-001 VE #34, #37). EPC acceptance should confirm that vendor evidence either incorporates or properly defers these studies, not re-perform them. (Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.)
- The 3-25 DBM slice describes inlet compressor motors at 4,000 V / 5,200 hp with starting VFDs, and separately discusses 600 V VFDs built into 600 V MCC lineups. The PKG-017 identity ("MV VFD - 600HP, 4160V") does not directly match either passage. See Conflict Table item CT-017-06-01. Acceptance language should remain at the package-identity level until the technical basis is reconciled.
- Declared dependencies are empty; coordination mode is DECLARED. Sibling DEL-017-01 through DEL-017-05 are de-facto upstream inputs for the acceptance basis, but they are not currently asserted in `_DEPENDENCIES.md`. EPC Integrator should track this as an undeclared-but-relied-upon coordination edge. (Source: `_DEPENDENCIES.md`.)

## Trade-offs

- **Depth of evidence vs. handoff schedule.** Heavy clause-by-clause traceability slows acceptance but reduces integration risk; a checklist-with-exceptions model is lighter but pushes residual risk into commissioning. The right balance depends on accepted Datasheet criticality categories (`TBD` until DEL-017-02 is accepted).
- **Strict acceptance vs. carried holds.** Closing every open item before acceptance is cleanest but rarely feasible; carrying holds preserves schedule but requires explicit tracking through commissioning.
- **Vendor-led vs. EPC-led test witnessing.** Vendor-led with EPC sampling is cost-efficient; EPC-led witnessing across all hold points raises assurance but is more expensive. Balance should follow DEL-017-02 Verification section once accepted.

## Examples

No project-local example acceptance records were located in `_REFERENCES.md` or the deliverable folder. Examples are deferred to a later revision once at least one PKG-017 sibling deliverable (DEL-017-01..05) is past `INITIALIZED` and produces concrete clause content to cite.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CT-017-06-01 | Package identity "MV VFD - 600HP, 4160V, 3PH, 60HZ" does not directly match the accessible 3-25 DBM source slice, which describes 4,000 V / 5,200 hp inlet compressor motors with starting VFDs and separately 600 V VFDs in 600 V MCC lineups. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-017 (Workbook Packages row 19; `26020-02-30-008`) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (compressor-motor and MCC sections) | Datasheet Construction "Quantities/Ratings"; Specification Standards row referencing SCA-001 VEs | PROPOSAL: treat the Gate 7 package register row as authoritative for package identity until a corroborating equipment-list source slice is presented; hold detailed VFD ratings as TBD. | TBD |
| CT-017-06-02 | `_DEPENDENCIES.md` declares no upstream dependencies, but acceptance content cannot be assembled without DEL-017-01, DEL-017-02, DEL-017-03, DEL-017-04, and DEL-017-05 reaching accepted snapshots. | `_DEPENDENCIES.md` (no declared edges) | `_CONTEXT.md` Scope (acceptance basis enumerates sibling deliverables) | All Specification requirements that depend on accepted sibling snapshots | PROPOSAL: declare DEL-017-01..05 as upstream dependencies of DEL-017-06 in a follow-up `dependency-extract` pass. | TBD |
