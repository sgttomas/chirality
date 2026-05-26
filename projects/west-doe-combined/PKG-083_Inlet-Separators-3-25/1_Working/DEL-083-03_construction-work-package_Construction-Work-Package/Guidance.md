# Guidance — DEL-083-03 Construction Work Package (PKG-083 Inlet Separators 3-25)

## Purpose

This Construction Work Package (CWP) exists to capture how the EPC Integrator physically installs, ties in, inspects, and turns over the PKG-083 Inlet Separators 3-25 package (two identical horizontal three-phase separators V-1600-2 and V-1700-2) into the 03-25 West Doe Compressor Station and Liquids Hub. It is the Gate-5 EPC anchor deliverable for this package and the basis for downstream Vendor Package Review and Acceptance (DEL-083-06 type), pre-commissioning, and operations turnover. [Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row DEL-083-03_construction-work-package]

## Principles

1. **Package-vs-Integration split is non-negotiable.** The vendor owns package engineering and physical equipment supply; the EPC Integrator owns facility integration and the interfaces listed for PKG-083. CWP content must stay on the EPC-Integration side of that line. [Source: PACKAGE_REGISTER.csv row PKG-083]
2. **Symmetry of inlet trains drives constructability.** Two 50% separators rely on symmetrical inlet piping for even flow distribution. Field installation that compromises symmetry (run length, fittings, elevation) is a constructability risk to be flagged early. [Source: DBM §Flow Distribution and Controls]
3. **Sour service governs material, weld, and inspection regime.** Process and produced-water sides are sour. Material certifications, NACE compliance, hardness testing, and PWHT requirements (per vessel/piping classes) must be carried through receiving inspection and field welds. [Source basis: DBM §SEC-03/04 sour service references; clause-level NACE/MR0175 mapping: location TBD]
4. **Coatings discipline matters.** Vessels are internally coated with Devchem 253; field damage during rigging, setting, and tie-in must be avoided and inspected. Piping is not coated under the current separator basis. [Source: DBM §SEC-04]
5. **Building extent is partly defined.** Instrumentation and one end of each package are enclosed in a heated self-framing building, but the exact extent is TBD in the source. CWP planning must flag this as a coordination item with the package vendor and the building scope owner. [Source: DBM §SEC-04]

## Considerations

- **Interface-type coverage check.** Compare the PACKAGE_REGISTER.csv PKG-083 interface list against this CWP's tie-in tasks. Note: Electrical Power and Building HVAC / Services are not in the PKG-083 interface list; before writing the workface plan, confirm whether power and HVAC are inside the vendor scope or owned by another package. (See Conflict Table CT-1.)
- **Methanol drain at the boot.** Methanol may appear at the inlet separator boot but downstream methanol disposition is TBD in the source. The CWP cannot resolve disposition; flag the drain tie-in as a coordination item with the facility utility/drain plan. [Source: DBM §SEC-03 line 218]
- **Inlet temperature reconciliation.** The DBM states an inlet design temperature of 8.3 deg C but notes downstream excerpts require confirmation. Construction-stage decisions (EHT extent, insulation specifications at tie-ins) should defer to the latest issued process datasheet, not be locked from the DBM alone. [Source: DBM §SEC-04]
- **ESDV shutdown pressure (635 psig) and delivery-point ESDV (TBC).** Construction interface to ESDV instrumentation must accept the current basis pressure but should track the open delivery-point value. [Source: DBM §Pig Receiver / ESDV]
- **Capacity-basis language reconciliation.** DBM §SEC-10 (Equipment Sizing Basis) notes inlet separators as "two identical packages, each 50 percent of facility capacity; older 2 x 100 percent table language requires reconciliation." Construction should follow the 2 x 50% basis. (See Conflict Table CT-2.)
- **Modularization and transport.** Inlet compressor packages are noted to disassemble into three pieces for transport; the source does not explicitly state separator-package modularization. ASSUMPTION: separator packages arrive on a single skid each, but rigging plan should be confirmed against vendor GA.

## Trade-offs

- **Field-weld vs flanged tie-ins.** Field welds reduce leak points but require sour-service qualified procedures, NDE, and PWHT planning; flanged tie-ins simplify make-up and future maintenance. Choice should be driven by isolation/maintenance philosophy and the vendor's nozzle list.
- **Pre-set vs set-and-align sequencing.** Pre-setting before building envelope completion preserves crane access but exposes the package to weather; setting after building completion protects the package but requires careful lift planning inside or through partial building walls. The "heated self-framing building; exact extent TBD" wording in the DBM means this trade-off cannot be finalized until building scope is clarified.
- **Symmetry vs site congestion.** Strict pipe symmetry between the two trains may conflict with site congestion and existing utility runs; deviations from symmetry that affect flow distribution must be reviewed with process engineering.

## Examples

- **Example A — Inlet pressure-control manifold installation.** Source requires at least two parallel inlet PCVs per package with balanced globe hardened trim and dP <=5 psid. A valid CWP step: pre-fabricate the parallel PCV manifold as a sub-spool, hydrotest off-skid, then field weld/flange to the inlet header symmetric tee. [Source: DBM §Flow Distribution and Controls]
- **Example B — Mist eliminator preservation.** Source identifies vertical/horizontal high-performance mesh/vane mist eliminators with manway access. A valid CWP step: confirm vendor-installed mist eliminators are bagged or capped before site receipt; verify presence and orientation before sealing the vessel after any internals access. [Source: DBM §SEC-04]
- **Example C — Devchem 253 coating inspection.** Visual + DFT check of internal coating after transport and after any field-weld nozzle work; coordinate with vendor for repair procedure if damage is found. [Source: DBM §SEC-04, §SEC-06]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-1 | PKG-083 interface list in PACKAGE_REGISTER.csv omits Electrical Power and Building HVAC / Services, but the package is enclosed in a heated self-framing building per DBM §SEC-04, which would normally require both. | PACKAGE_REGISTER.csv row PKG-083 (interfaces field) | DBM-Comp_and_Liquids §SEC-04 (heated self-framing building wording) | Specification R3, R8; this Guidance | PROPOSAL: treat Electrical Power and Building HVAC / Services as out-of-PKG-083 EPC scope for tie-in purposes but coordinated through the building/utility package; explicitly flag in the workface plan as a cross-package interface | TBD |
| CT-2 | Inlet separator capacity basis: current basis is 2 x 50%, but older DBM table language said 2 x 100% and "requires reconciliation". | DBM §SEC-04 (table: 40 MMSCFD per separator; 2 x 50%) | DBM §SEC-10 note ("older 2 x 100 percent table language requires reconciliation") | Datasheet capacity rows; Specification R1, R2 | PROPOSAL: follow the current 2 x 50% basis everywhere in the CWP | TBD |
| CT-3 | Inlet design temperature stated as 8.3 deg C, with the source noting that "some downstream excerpts require confirmation". | DBM §SEC-04 narrative | DBM §SEC-04 reconciliation note | Specification R6 (EHT scope) | PROPOSAL: defer EHT extent decisions to the latest issued process datasheet; do not lock from DBM alone | TBD |
