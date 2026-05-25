# Guidance: DEL-028-03_construction-work-package — Construction Work Package

## Purpose

The Construction Work Package (CWP) for PKG-028 exists to give the field organization a single, source-anchored construction reference for installing and tying in the TXP-8801-1 7.5 MVA 13.8 kV / 4160 / 2400 V step-down distribution transformer. It connects the EPC Integrator's scope and datasheet (DEL-028-01, DEL-028-02) to the vendor-engineered equipment package (DEL-028-04) and the downstream EPC review and acceptance work (DEL-028-06).

Source basis: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv (DEL-028-03); PACKAGE_REGISTER.csv (PKG-028).

## Principles

1. **EPC owns integration; vendor owns the package itself.** The CWP must not duplicate vendor package engineering or design content. It documents how the vendor-engineered package is physically integrated into the plant. (PACKAGE_REGISTER.csv responsibility narrative)
2. **Workface planning first.** Workface planning evidence is an explicit anticipated artifact (ART-D64770700D); plan the installation in sufficient detail that the field can execute against documented prerequisites and hold points.
3. **Interface-driven turnover.** All seven declared interface types for PKG-028 (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) must appear on the construction interface and turnover checklist. (INTERFACE_REGISTER.csv)
4. **Foundation discipline.** Transformers are generally supported on precast concrete bearing foundations; do not start setting work until the foundation is formally accepted. (DBM-Deepcut §2745)
5. **Grounding before energization.** Distribution transformers require a separately-run copper ground conductor in addition to wiring grounds, sized per CEC. (DBM-Deepcut §2991)

## Considerations

- The package title is the only source-supported statement of voltage and rating (13.8 kV / 4160 / 2400 V, 7.5 MVA). Winding configuration, cooling class, impedance, BIL, tap-changer arrangement, and insulating fluid are not stated in PREPARATION-accessible sources and remain `TBD` until vendor data is accepted under DEL-028-05/06.
- DBM-Deepcut §2985 gives the grounding scheme for 6.9 kV and 600 V transformers (100 A, 10 s NGR and 5 A continuous HRG respectively). The 4160 V and 2400 V secondaries of TXP-8801-1 are not directly named; the NGR/HRG sizing for these secondaries must be confirmed in detailed engineering rather than copied across by analogy.
- Adjacent-package coordination (who delivers the 13.8 kV feeder, who pulls the secondary feeders, who provides ground grid extension, who installs area lighting and comms) is real but not enumerated in PREPARATION-accessible sources. The CWP should reference these by interface type and leave specific package IDs `TBD` until interface management work is performed.
- The PROJECT_DECOMP authority-to-deliverable association is package-grouped (PACKAGE_HEURISTIC). The objectives recorded in `_CONTEXT.md` (OBJ-001/004/005/006/008/009/010) apply at the package level; this CWP supports them only insofar as construction integration enables the objectives — treat the association as directional context, not as binding requirements on this deliverable.

## Trade-offs

- **Detailed step-by-step procedures vs. vendor-IOM deference.** Writing detailed step-by-step transformer setting and termination procedures into the CWP before vendor IOM is in hand risks conflict with manufacturer requirements. The CWP should hold the structure and hold points but defer detailed mechanical and electrical steps to vendor IOM.
- **Pre-energization test scope.** Industry-standard pre-energization tests (insulation resistance, turns ratio, winding resistance, oil DGA where applicable) are likely required; specifying them here without vendor / ITP backing is an ASSUMPTION. Treat the listed tests as a planning baseline subject to ITP confirmation.
- **Workface granularity.** Workface plans that decompose to sub-shift increments give the field clearer control but cost more to maintain. The chosen granularity should match the project-wide workface planning standard, which is not enumerated in PREPARATION-accessible sources.

## Examples

- DBM-Deepcut §2919 illustrates the radial 13.8 kV distribution context that TXP-8801-1 participates in: power from the 13.8 kV switchgear is distributed radially through step-down transformers to downstream loads. The CWP narrative should reference this architecture when scoping the primary tie-in.
- DBM-Deepcut §2745 (`Transformers — Generally supported on precast concrete bearing foundations; None identified`) is the explicit foundation-type basis used in the Datasheet.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-028-03-001 | DBM-Deepcut §2985 specifies neutral grounding for 6.9 kV and 600 V transformer secondaries but not for 4160 V or 2400 V secondaries. Direct application by analogy may be inappropriate. | DBM-Deepcut §2985 | Package title (4160 V / 2400 V secondaries) | Datasheet (Neutral grounding), Specification REQ-028-03-004 | Treat DBM §2985 as analogous only; require detailed engineering to define the 4160 V and 2400 V grounding scheme; leave specific NGR/HRG ratings `TBD` here. | TBD |
| CONF-028-03-002 | OBJECTIVE_DELIVERABLE_MAP lists OBJ-001/004/005/006/008/009/010 against DEL-028-03 (package-grouped). Whether the construction-tie-in deliverable directly satisfies each objective or only contributes indirectly is unclear. | OBJECTIVE_DELIVERABLE_MAP.csv | `_CONTEXT.md` scope statement | Datasheet (Identification — Supports Objectives) | Treat associations as directional package-grouped context (ASSUMPTION) per PACKAGE_HEURISTIC; do not derive deliverable-level acceptance criteria from the objective list alone. | TBD |

## Needs Human Ruling

- **HRR-028-03-001:** Vendor data for TXP-8801-1 (winding configuration, cooling class, impedance, BIL, tap arrangement, insulating fluid, weight, dimensional envelope) is not present in PREPARATION-accessible sources. Proposed handling: keep all such fields `TBD` in the Datasheet and defer to DEL-028-04 / DEL-028-05.
- **HRR-028-03-002:** The 4160 V and 2400 V secondary grounding scheme (NGR vs. HRG; rating and duration) for TXP-8801-1 is not stated in accessible source material. Proposed handling: require detailed engineering to issue the grounding scheme before construction hold-point release; leave the Datasheet entry `TBD`.
- **HRR-028-03-003:** Adjacent-package owners for declared interface types (13.8 kV feeder, secondary feeders, ground grid extension, area lighting, I&C/control cabling, communications, structural supports) are not enumerated in accessible source material. Proposed handling: leave specific adjacent-package IDs `TBD` and reference interface types only.
