# Package Datasheet — Guidance — PKG-075 Cryogenic Unit ("Deepcut")

DeliverableID: DEL-075-02_package-datasheet
DecompositionRef: GATE-07_Final_Published_2026-05-24

## Purpose

The Package Datasheet for PKG-075 is the mandatory EPC Integrator technical-handoff deliverable that carries the package data required for third-party Package Vendor engineering and design of the UltraTEF cryogenic recovery unit (DELIVERABLE_REGISTER.csv DEL-075-02). It is the single point at which the West Doe Deepcut DBM design basis is consolidated for the cryogenic package and presented to the Vendor with the EPC Integrator's interface and integration constraints attached. Interface facts are intentionally carried here as evidence rather than as separate deliverables (DELIVERABLE_REGISTER.csv DEL-075-02 notes; _CONTEXT.md Notes).

## Principles

- **Source-anchored, not narrative-anchored.** All design values must trace to the DBM (primary) or to the package register / interface register (secondary). Decomposition prose is routing, not authority. (Authority hierarchy, four-documents SKILL.md.)
- **Single design point for cryogenic core equipment.** BAHX and turbo-expander/compressor are designed to summer/expander-mode conditions; winter operation is *expected* performance and must be hydraulically verified for towers, pumps, and reboiler (DBM SEC-06).
- **Two-mode operability.** Expander mode is the normal high-recovery mode; J-T mode is the start-up / off-design mode. The package must remain operable, safe, and sufficient for sales-gas total-sulphur compliance in J-T mode, even though several J-T parameters remain TBC (DBM SEC-06).
- **Hydrate and freeze management by methanol injection.** Methanol injection is the primary defense against hydrate formation and ice plugging in cryogenic service; the system is designed for single-point injection at any moment, which constrains operating procedure (DBM SEC-06).
- **MDMT protection is non-negotiable.** The E-pass bypass exists to keep the deethanizer condenser reflux system below its MDMT during transients; this protective function must remain available across all operating modes.
- **Flare-protective J-T valve stroke limit.** A mechanical or stroke limit on the J-T valve is a protective design feature, not a tuning convenience; it caps the worst-case flare flow into the propane absorber.
- **Mercury, particulate, and water are upstream problems with cryogenic consequences.** The mol-sieve dehydration system, MRU, and dust filtration are not in package scope, but the package's tolerance assumptions (water dewpoint < −75 °C; mercury-tolerant BAHX features) define the upstream interface.
- **EPC Integrator owns facility integration.** The Package Vendor owns package engineering and physical equipment; the EPC Integrator owns interfaces, tie-ins, constructability, and facility-level integration (PACKAGE_REGISTER.csv PKG-075). The Datasheet is the place where EPC integration constraints get pushed into the vendor scope.

## Considerations

- **Winter operation may govern hydraulics even though it does not govern thermal design.** Higher operating pressures and increased liquid flows in winter can stress tower flooding, pump NPSH, and reboiler approach. Vendor model must publish a winter case (DBM SEC-06 "Process Description").
- **Mercaptan concentration in C3+ liquids.** Cryogenic liquids may concentrate mercaptans (DBM SEC-06 reports design summer expander-mode C3+ deethanizer bottoms can contain methyl mercaptan ~1,373 ppmv and ethyl mercaptan ~2,640 ppmv). This conditions the downstream NGL mercaptan treating scope and the metallurgy of cryogenic-package piping touching deethanizer bottoms.
- **BAHX is a sole-source long-lead item.** Six-pass BAHX with ALPEMA / ASME / BC CRN and mercury-tolerant features requires early vendor engagement; treat as critical-path on the package schedule.
- **Mercury-tolerant features remain to be developed.** This is an explicit DBM-flagged TBD; the Datasheet should require Vendor to propose mercury-tolerant features rather than presume them.
- **Future NGL bottoms exchanger/cooler provisions.** Future NGL treating is downstream and out-of-scope for the package now, but the package must be physically and hydraulically prepared (nozzle and provision) for the future NEN exchanger and air cooler (DBM SEC-06 "Future deethanizer bottoms exchanger" / "cooler").
- **Sales-gas total-sulphur compliance during start-up.** Plant strategy is internal recycle and cooldown to meet specification before flowing into the sales pipeline; whether spec can be met before flowing is a TBC at the facility level (DBM SEC-05) and conditions cryogenic dry-out and J-T mode duration.
- **External package-requirements documents (26020-Package_Requirements.docx; Interfaces export .xlsx) are not parsed locally** — Datasheet content depending on them is `location TBD`. The Vendor handoff package must reconcile against these documents before final issue.

## Trade-offs

| Trade-off | Tension | Current basis position |
|---|---|---|
| Single summer design point vs winter case sizing | Reduces vendor scope but pushes hydraulic risk to winter | DBM accepts the trade-off; requires winter hydraulic verification (DBM SEC-06). |
| Expander-mode recovery 99+% vs J-T mode capacity | High expander recovery means J-T mode is a fallback, not a parallel mode | DBM positions J-T as start-up / off-design only (DBM SEC-06 "Operating Modes"). |
| BAHX excess area 10% vs cost | Improves margin for fouling, mercury, and off-design | Required by DBM SEC-06 "BAHX" — no compromise. |
| Single-point methanol injection vs simultaneous multi-point | Simplifies header design, valving, control; constrains procedure | Adopted by DBM SEC-06 "Methanol injection". |
| Electric expander aftercooler control by fan speed vs winter recirculation | Winter operation below 95 °F outlet requires study | DBM SEC-06 leaves winter <95 °F operation as TBC. |
| Carrying interface facts inside the Datasheet vs separate interface deliverables | Reduces deliverable count, increases Datasheet density | DEL-075-02 _CONTEXT.md and decomposition note explicitly choose to consolidate here. |

## Examples

- **Cryogenic dry-out as a worked procedural example.** The dry-out header provides low-pressure dry sales gas recycle for cryogenic dry-out at approximately 250 psig initial assumption (DBM SEC-06 mol-sieve table). The package vendor's procedure must align with this header and with the J-T-mode cooldown strategy.
- **A-pass bypass control logic.** Cold-separator overhead temperature controls a 15–20% A-pass bypass (TBC), used to maintain propane absorber pressure/temperature at low inlet temperatures (DBM SEC-06 "BAHX A-pass bypass"). This is a vendor-implemented control with EPC interface to the plant PID network.
- **Anti-surge recycle.** Compressor anti-surge recycle is from discharge to inlet via FCV (DBM SEC-06 "Turbo-expander/compressor"); a worked example of a vendor-package control loop that consumes EPC-supplied utilities (instrument air; I&C interface IFC-A14DB88572).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CT-01 | Deethanizer bottoms C2/C3 "expected/operating target <=654 mol%" — value exceeds 100% and is internally inconsistent with the design "<=1.5 mol%" in the same row. | DBM SEC-06 "UltraTEF Design Values" — Deethanizer bottoms product row, design target text | DBM SEC-06 same row — design value "<=1.5 mol%" | Datasheet "Attributes"; Specification R1.4 | Read as `≤0.654 mol%` (typo for decimal point). Treat as ASSUMPTION pending DBM SEC-06 erratum or human ruling. | TBD |
| CT-02 | LACT scope and responsibility. DBM SEC-01 simultaneously identifies NGL product LACT and lists LACT units as excluded. | DBM SEC-01 "Process and Commercial Basis" | DBM SEC-01 "Scope Boundary" (excluded items) | Not directly in cryogenic package scope; affects downstream metering and product-disposition handoff that the cryogenic Datasheet must point to. | LACT inclusion, ownership, and design responsibility remain TBD; do not assume cryogenic package includes LACT-related metering. | TBD |
| CT-03 | 26020-Package_Requirements.docx heading 29 referenced as authoritative package basis, but the docx is a binary file and was not parsed for this draft. | _REFERENCES.md "Source Materials Referenced By Decomposition Row" | This Datasheet draft (no source slice cited) | Datasheet "References"; Specification "Standards"; any vendor-package addendum requirements | Treat 26020-Package_Requirements.docx requirements as `location TBD`; vendor handoff packet must reconcile before final issue. | TBD |
| CT-04 | 26020-Packages_Interfaces_4_export.xlsx not parsed locally; 12 interface types confirmed from INTERFACE_REGISTER.csv only (YES flag, no per-interface specifics). | _Sources/26020-Packages_Interfaces_4_export.xlsx | INTERFACE_REGISTER.csv (PKG-075) | Datasheet "Interfaces"; Specification R9 | Use INTERFACE_REGISTER.csv as the current authority for interface presence; defer per-interface specifics to the xlsx-derived matrix at vendor handoff. | TBD |
