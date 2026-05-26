# Guidance: Construction Work Package

## Purpose

This Guidance document explains why the Construction Work Package (CWP) for `PKG-078` Pig Receivers (Inlet) 4-25 exists and the rationale behind its scope and major requirements. The CWP is the mandatory EPC Integrator deliverable describing how the package will be physically installed, built, inspected, turned over, and tied into the larger 04-25 facility (`_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-078-03_construction-work-package`). It is one of six deliverables that, together, frame the EPC Integrator / Package Vendor split for `PKG-078` (`SCOPE_LEDGER.csv` `SOW-0161`).

## Principles

- **Vendor-owns-package; EPC-owns-integration.** The Package Vendor owns engineering, design, vendor documentation, and physical equipment package for the receivers and HIPPS skids; the EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, and procurement/construction coordination (`PACKAGE_REGISTER.csv` row `PKG-078`; `SCOPE_LEDGER.csv` `SOW-0161`). The CWP is the EPC Integrator's anchor for that integration.
- **Pigging safety is a first-class concern.** Full-port upstream isolation, barred tees that prevent pigs from entering facility piping, sweet-gas purge before barrel opening, and routing of vents to HP flare are intrinsic features of pig-receiver construction at this facility (`4-25_Deepcut_DBM.md` line 585; `SCOPE_LEDGER.csv` `SOW-0163`). The CWP must verify each of these features.
- **Overpressure protection is an integrated function, not a skid accessory.** The HIPPS package on each receiver skid is the means by which the plant inlet protects downstream inlet separators when inlet pipeline pressure could exceed facility inlet design pressure (`4-25_Deepcut_DBM.md` line 809; `SCOPE_LEDGER.csv` `SOW-0163`). HIPPS installation, loop testing, and proof testing therefore sit at the centre of the turnover plan.
- **Sour-service discipline applies throughout.** Design H2S of 1.0 mol% means materials, welding, hardness, and inspection records must satisfy project sour-service requirements; this is a quality-and-safety discipline, not just a metallurgical choice (`4-25_Deepcut_DBM.md` Inlet Contaminant table line 419; `SCOPE_LEDGER.csv` `SOW-0163`, `SOW-0164`).
- **Construction sequencing follows the inlet-process flow.** Plant inlet pipeline gas enters via the pig receivers and moves on into the inlet separators (`SCOPE_LEDGER.csv` `SOW-0162`); turnover sequencing should preserve the ability to introduce inlet gas to the facility in a controlled fashion.

## Considerations

- The Package Vendor delivers receivers and HIPPS skids; "by others" in SOW-0164 explicitly assigns interconnecting piping, DCS integration, foundations, and electrical supply to MCC outside the vendor package - the CWP must coordinate these interfaces and not assume vendor-provided coverage.
- The DBM section text describes one 610 mm OD inlet pig receiver (`4-25_Deepcut_DBM.md` line 585), while the package basic scope and equipment line items describe three identical receivers (PR-1010-1 / PR-1020-1 / PR-1030-1) (`SCOPE_LEDGER.csv` `SOW-0162`, `SOW-0163`; `4-25_Deepcut_DBM.md` Package Line-Item Requirements row 61). The governing package-level basis for this deliverable is three receivers; the DBM narrative describes a single-receiver functional case and is not a contradiction with the equipment count, but the CWP author should be aware of the narrative gap. See Conflict Table.
- HIPPS configuration, setpoints, SIL allocation, and proof-test intervals are explicitly deferred to detailed engineering (`4-25_Deepcut_DBM.md` line 809). The CWP cannot fix HIPPS test acceptance criteria until those engineering outputs land; placeholder TBDs in Specification R-07 and R-09 are intentional.
- EHT scope on receiver-skid piping is package-by-package detail; CWP should not assume universal trace coverage.
- DCS integration is by others (SOW-0164); the CWP's I&C tie-in obligation ends at the facility marshalling termination, with sign-off by the DCS-integration party.
- Pipeline / pigging interface (`INTERFACE_REGISTER.csv` `IFC-65EDB92369`) means there is at least one upstream pipeline party whose pigging operations interact with the receivers; CWP turnover should coordinate the first pig receipt operationally (timing TBD).

## Trade-offs

- **Pressure-test medium (hydrostatic vs. pneumatic).** Hydrostatic is safer and conventional; pneumatic may be required in cold weather or where dehydration after wetting is impractical. The CWP defers to the project piping specification; if both are options, schedule and sour-service drying constraints govern the choice.
- **Single-stage vs. staged turnover.** Three receivers permit either a single mechanical-completion event or staged turnover of one receiver while the others are completed. Operations preference for early gas-in capability may favour staged turnover; constructability and HIPPS validation continuity may favour a single completion. Trade-off should be decided jointly with operations during workface planning.
- **Sour-service hardness verification scope.** Higher coverage (e.g., every field weld) reduces the risk of in-service sulphide stress cracking but lengthens the construction schedule. The CWP author should propose a coverage rate consistent with the project piping spec and seek a human ruling if the project spec is silent.

## Examples

Concrete examples from the source set:
- **Equipment tag list:** PR-1010-1, PR-1020-1, PR-1030-1 (`4-25_Deepcut_DBM.md` Package Line-Item Requirements row 61) - three receivers, each on its own dedicated structural-steel non-enclosed skid.
- **Pressure framing:** Normal operating pressure 653-725 psig, MAOP 1300 psig (`SCOPE_LEDGER.csv` `SOW-0164`; `4-25_Deepcut_DBM.md` Inlet Pipeline Pressure table line 626). Receiver/skid MAWP 1440 psig (TBC at plant gate).
- **Pigging-functional features:** Full-port upstream isolation, barred tees, low-pressure sweet fuel-gas purge downstream of the manual isolation valve, HP flare vent (`4-25_Deepcut_DBM.md` line 585; `SCOPE_LEDGER.csv` `SOW-0163`).

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | DBM narrative refers to a single 610 mm OD inlet pig receiver while the package basic scope and equipment line items describe three identical 24" receivers on dedicated skids. | `4-25_Deepcut_DBM.md` line 585 ("one 610 mm OD (24 in.) pig receiver on a dedicated structural steel non-enclosed skid") | `SCOPE_LEDGER.csv` `SOW-0162`, `SOW-0163`; `4-25_Deepcut_DBM.md` Package Line-Item Requirements row 61 (PR-1010-1, PR-1020-1, PR-1030-1; equipment count 3) | Datasheet.Attributes (equipment identity), Datasheet.Construction (work package boundary), Specification.Scope, Specification.R-01, Guidance.Examples | PROPOSAL: package-level scope (three receivers) governs CWP equipment count; DBM line 585 describes the functional case of an inlet receiver and is not necessarily contradictory. Confirm intended count. | TBD |
| C-02 | Receiver / inlet skid MAWP 1440 psig is stated with "TBC" at plant gate; HIPPS requirements are explicitly deferred to detailed engineering. | `4-25_Deepcut_DBM.md` Inlet Pipeline Pressure table (line 626) and line 809 (HIPPS to be confirmed) | `SCOPE_LEDGER.csv` `SOW-0164` (MAWP = 1440 psig) | Datasheet.Conditions (Design pressure / Inlet ESDV / HIPPS interaction), Specification.R-07, Specification.Standards, Procedure (HIPPS test) | PROPOSAL: hold HIPPS final design parameters as TBD pending detailed engineering; do not freeze HIPPS test acceptance criteria in this CWP. | TBD |
| C-03 | Equipment-roster line item is labelled "Pig Receivers (Inlet) 2" in the DBM roster while the package is `PKG-078` "Pig Receivers (Inlet) 4-25"; the "2" appears to be a roster line-item suffix, not a quantity. | `4-25_Deepcut_DBM.md` Package Line-Item Requirements row 61 ("Pig Receivers (Inlet) 2", equipment count 3) | `PACKAGE_REGISTER.csv` row `PKG-078` (package name "Pig Receivers (Inlet) 4-25") | Datasheet.Identification, Datasheet.Attributes, Specification.Scope | PROPOSAL: treat package name from `PACKAGE_REGISTER.csv` as authoritative; "Pig Receivers (Inlet) 2" is a DBM roster line-item suffix. | TBD |
