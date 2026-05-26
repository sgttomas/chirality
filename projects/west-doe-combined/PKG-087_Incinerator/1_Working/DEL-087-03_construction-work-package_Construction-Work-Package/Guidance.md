# Guidance — DEL-087-03 Construction Work Package (PKG-087 Incinerator)

## Purpose

The Construction Work Package (CWP) for PKG-087 Incinerator exists so that the EPC Integrator can take a vendor-engineered incinerator package (knockout drum, knockout drum transfer pump, low-pressure flare stack, blower) and physically install, inspect, tie in, and turn it over as an integrated part of the wider process facility (`_CONTEXT.md` Scope; PACKAGE_REGISTER.csv PKG-087 split-of-responsibility). It is a Gate 5 EPC-anchor deliverable (`_CONTEXT.md` Notes).

## Principles

1. **Vendor / EPC boundary is the load-bearing axis of this CWP.** The Package Vendor owns engineering, design, and physical equipment supply; the EPC Integrator owns facility-level integration, interfaces, constructability, and procurement/construction coordination (PACKAGE_REGISTER.csv PKG-087). CWP content must respect that boundary and not redo vendor engineering.
2. **Source over summary.** Where DBM source language is available locally (`3-25_Comp_and_Liquids_DBM.md`), use it directly for connected-system constraints (e.g., the spent-caustic flame-arrestor vent path to the incinerator header — line 402).
3. **Treat the incinerator as a shared-interface system.** The DBM explicitly characterizes the LP flare stack and incinerator as shared between 03-25 and 04-25, with the exact service split open (DBM lines 56, 547). Construction sequencing must accommodate a pending allocation ruling.
4. **No invention on permit values.** The DBM expressly defers permit-final emissions values (line 555). Do not generate permit-final emission, flare load, or blowdown numbers in this CWP.
5. **Twelve interfaces are first-class objects.** The INTERFACE_REGISTER lists twelve YES interfaces for PKG-087; the workface plan should treat each as a distinct workstream with its own tie-in package.

## Considerations

- **Material restrictions in caustic-impacted service.** The DBM states aluminum shall not be used in the caustic building (line 402). For the incinerator package, this may apply to vent header materials and any package equipment exposed to caustic-laden vapor — ASSUMPTION; confirmation required against the package vendor's material selection.
- **Cross-facility utility supply.** Fuel gas, instrument air, and electrical power are shared with the 04-25 gas plant; instrument air compression is supplied from 04-25 (DBM line 56). Tie-in sequencing must coordinate with 04-25 construction.
- **Open interface items are not blockers but are risks.** Service allocation and emissions-summary inputs (DBM lines 547, 555) are listed as open. The CWP can be progressed in parallel as long as it carries those items explicitly.
- **DEL-087-02 Package Datasheet is the engineering hand-off.** Construction parameters (loads, anchor patterns, utility consumption, hazardous-area classification) flow from the datasheet; the CWP consumes them rather than originates them.

## Trade-offs

| Trade-off | Discussion | Source |
|---|---|---|
| Sequence: install package then tie in interfaces vs. lay tie-ins first | Source materials do not state a preference; conventional EPC practice would defer to vendor erection requirements. ASSUMPTION; final sequence is TBD. | TBD |
| Owner of LP flare stack physical installation | Shared-interface status (DBM lines 56, 547) creates ambiguity between 03-25 and 04-25 scope; CWP must record the ruling once made. | DBM lines 56, 547 |
| Permit-final emissions vs. DBM scoping | The DBM is explicit that current numbers are DBM-scoping not permit-final (line 555); the CWP should not pull DBM numbers into permit-binding form. | DBM line 555 |

## Examples

(Examples grounded in source slices; otherwise omitted.)

- Spent caustic vent example: the spent-caustic storage tank vents through a flame arrestor to the incinerator header and supports truck-out (DBM line 402) — the CWP's Relief / Flare / Vent workface scope must preserve this path during tie-in.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-01 | Incinerator service allocation between 03-25 and 04-25 not resolved | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md line 56 | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md lines 547, 555 | Specification §Scope, R-087-03-05; Datasheet §Conditions | Carry as open interface item until human/source ruling; PROPOSAL: treat 03-25 as installation-host facility unless ruled otherwise | TBD |
| C-02 | Aluminum-exclusion clause stated for the caustic building; applicability to incinerator package equipment not explicit | DBM line 402 (clause stated for caustic building) | Package equipment list (PACKAGE_REGISTER.csv PKG-087) does not specify materials | Specification R-087-03-07; Datasheet §Construction | PROPOSAL: apply aluminum-exclusion to any incinerator-package component in direct caustic-vapor service; confirm with vendor MTR | TBD |
| C-03 | `26020-01-PT-RFQ-25-003_Incinerator.docx` referenced by PACKAGE_REGISTER but not locally accessible | PACKAGE_REGISTER.csv PKG-087 Word Source Basis | (no local copy) | All Specification requirements lacking source citations (R-087-03-08..11); Standards | PROPOSAL: stage source slice locally before progressing CWP past Gate-5 preparation | TBD |
| C-04 | `26020-Package_Requirements.docx` heading 40 cited as source but not locally readable as text | `_REFERENCES.md`; `_CONTEXT.md` Source Reference | (binary .docx; not extracted) | Specification §Standards; Datasheet §References | PROPOSAL: extract heading-40 slice to markdown before next pass | TBD |
