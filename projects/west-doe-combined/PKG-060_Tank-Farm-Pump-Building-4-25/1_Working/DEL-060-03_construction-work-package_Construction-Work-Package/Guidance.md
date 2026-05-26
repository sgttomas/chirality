# Guidance — DEL-060-03 Construction Work Package

## Purpose

The Construction Work Package exists so the EPC Integrator can carry PKG-060 (Tank Farm Pump Building 4-25) from a vendor-supplied package into a built, inspected, tied-in, and turned-over asset within the West Doe Deepcut facility (SourcePath: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` PKG-060). It bridges vendor engineering/design/equipment scope and Owner field-construction execution authority defined in the DBM (SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SectionRef: SEC-01 Construction Responsibility).

## Principles

- **Source-anchored construction basis.** Construction planning derives from the DBM construction-responsibility basis and the package decomposition. Where the source basis is silent, items are `TBD` rather than invented.
- **Vendor / Integrator / Owner boundary discipline.** The Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility-level integration and interfaces; Tourmaline owns field construction execution. The CWP must never silently shift these scopes (`PACKAGE_REGISTER.csv` PKG-060; DBM SEC-01).
- **Interface-first turnover.** Turnover is structured around the PKG-060 interface set (`INTERFACE_REGISTER.csv`) so every applicable interface type is explicitly closed out.
- **Independent metering preservation.** Any cross-facility tie-in (e.g., shared fuel gas / instrument air with 03-25; existing-facility connections) must keep facility mass balances accurate (DBM SEC-01 Existing-Facility Interfaces and Metering).
- **Cold-climate construction.** Design ambient is -40 °C / +35 °C with extreme -49.2 °C / +38.9 °C (DBM SEC-02.2). Construction methods, materials, and schedule must accommodate sustained cold and short cold-weather work windows.

## Considerations

- **By-others coordination.** SOW-0192 declares DCS integration, foundations, and electrical supply to the MCC as "by others" relative to the package vendor. The CWP must explicitly own coordination of those scopes through the EPC Integrator and Owner.
- **ISBL/OSBL tie-in responsibility.** The DBM marks interconnecting piping to ISBL/OSBL tie-in points as an external interface "responsibility to be confirmed for each tie-in." Workface planning should not assume Tourmaline (or any party) by default; each tie-in needs a documented responsibility decision.
- **Material conformance for caustic service.** Caustic transfer pumps are corrosive service with "no aluminium" (SOW-0191). Installed gaskets, supports, and incidental contact materials at tie-ins should be checked for the same constraint.
- **Motor and starter basis.** All pumps are 575 V / 3 ph / 60 Hz, DOL or VFD start, fed from 600 V MCC with local H-O-A or On-Off control (SOW-0192). Construction hookup and pre-commissioning checks should validate this configuration in the field.
- **Self-framing building erection.** The pump building is site-erected, self-framing (SOW-0191). Erection schedule should reflect Dawson Creek wind (mean 14 km/h; max 138 km/h TBC, DBM SEC-02.2) and cold-weather constraints.
- **Permitting.** Construction is conducted under the BC Energy Regulator permit amendment for the 300 MMSCFD deep cut train, subject to a Section 12.4 site alteration permit (DBM SEC-01). CWP planning should reference and respect the permit conditions when they are made available.

## Trade-offs

- **Field-erected vs modularized build.** The package is field-erected (self-framing building) per source. Trading toward more modularization would require source change and is out of scope for this CWP.
- **Tourmaline field construction vs EPC subcontracted execution.** DBM SEC-01 assigns the bulk of field construction to Tourmaline. Any EPC subcontracted alternative would require explicit human ruling and is `TBD`.
- **DOL vs VFD starting.** Either is allowed by SOW-0192; selection affects MCC bucket sizing, harmonic mitigation, and starting torque verification. CWP should record the selection used by the vendor package and flow it into hookup checks.

## Examples

Concrete construction-sequence examples are not derivable from the locally accessible source slices; populate from project-specific workface plan once developed (`TBD`).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CWP-CFL-01 | Tie-in responsibility for interconnecting piping to ISBL/OSBL is assigned by DBM as an "external interface responsibility marker, to be confirmed per tie-in," yet PKG-060 carries 14 declared interface types implying default integrator action. | DBM-Deepcut SEC-01 Construction Responsibility (interconnecting piping line) | `INTERFACE_REGISTER.csv` PKG-060 rows (14 interface types YES) | Specification REQ-CWP-04, REQ-CWP-06; Datasheet Construction table; Procedure tie-in steps | DBM line governs default; each tie-in receives a documented responsibility confirmation in the workface plan. | TBD |
| CWP-CFL-02 | Foundations are "Tourmaline field construction scope" per DBM, but SOW-0192 lists foundations under "by others" relative to the vendor. | DBM-Deepcut SEC-01 (Tourmaline scope: foundations) | `SCOPE_LEDGER.csv` SOW-0192 ("By others: ... foundations ...") | Specification REQ-CWP-03, REQ-CWP-09; Datasheet Construction table | The two statements are consistent at the package boundary (foundations are by others *to the vendor* and are *by Tourmaline* in the field); CWP should restate this explicitly to avoid ambiguity. | TBD |
| CWP-CFL-03 | DCS integration is "by others" per SOW-0192; the CWP must still document who performs DCS hookup and pre-commissioning loops for PKG-060. | `SCOPE_LEDGER.csv` SOW-0192 | DBM-Deepcut SEC-01 (does not name a DCS integrator for this package) | Specification REQ-CWP-09; Procedure pre-commissioning | EPC Integrator coordinates DCS integration with the controls discipline; exact executing party `TBD`. | TBD |
| CWP-CFL-04 | The 26020 Word and Excel source materials referenced by the decomposition are not locally accessible as text; clause-level statements ascribed to them cannot be cited at section granularity. | `_REFERENCES.md` Missing/Deferred References | `DELIVERABLE_REGISTER.csv` DEL-060-03 Source Reference | All four documents | Mark unsupported clause-level claims `location TBD`; expand `_REFERENCES.md` with accessible slices in a later run. | TBD |

## TBD / Open Items

- Owner construction safety standards and turnover acceptance criteria (`TBD`).
- Discipline-level construction standards (civil/mechanical/electrical/I&C) not in accessible sources (`TBD`).
- Final tie-in responsibility per interface (`TBD` per CWP-CFL-01).
- Threshold ambient temperature for cold-weather construction restrictions (`TBD`).
