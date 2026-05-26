# Guidance: DEL-051-01_scope-of-work — Scope of Work

> Directional guidance for drafting and reviewing the EPC Scope of Work for PKG-051 Process Heat Medium Unit. The Scope of Work is an EPC Integrator anchor deliverable: it defines the package boundary that all downstream package deliverables (datasheet, CWP, vendor engineering, vendor document turnover, EPC review) inherit. Where the workbook scope and the Deepcut DBM disagree, this document does not silently reconcile them; instead, it surfaces conflicts for human ruling.

## Purpose

This deliverable exists to give the Package Vendor and the EPC Integrator a single, source-grounded statement of what PKG-051 is, what it does, where its boundary sits, who is responsible for which engineering and integration tasks, and which design-basis values and open items it inherits from the Deepcut DBM. It is the binding scope reference for DEL-051-02 (Package Datasheet), DEL-051-03 (Construction Work Package), DEL-051-04 (Vendor Engineered Equipment Package), DEL-051-05 (Vendor Document Turnover), and DEL-051-06 (EPC Vendor Package Review and Acceptance).

## Principles

- **Source-grounded.** Every claim in the SoW must trace to a workbook row, scope-ledger SOW item, package register row, or DBM source slice. Inferences are labeled `ASSUMPTION`; unknowns are labeled `TBD`. [Authority hierarchy in skill SKILL.md]
- **Vendor/EPC split is binding.** Package engineering, design, vendor documentation, and physical equipment supply are Package Vendor; integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration are EPC Integrator. The SoW must not assign vendor design work to the EPC Integrator. [OBJ-004; `PACKAGE_REGISTER.csv` PKG-051 responsibility model]
- **Single source of truth per parameter.** When the workbook (SOW-0165..0168) and the DBM disagree, the SoW shall state both, mark the value `TBD pending human ruling`, and add a Conflict Table row — it shall not pick a value silently. The DBM and the workbook are both authoritative for what they were written for (DBM: facility-side basis; workbook: package-vendor scope), so the conflict is real and requires a ruling.
- **Shared utility framing.** The Heat Medium Unit is a shared 04-25 utility serving stabilizer/TEG/amine/deethanizer reboilers, MPFF HCL heaters, and lateral users, not a one-off package. The SoW must keep the integration narrative consistent with `4-25_Deepcut_DBM.md` SEC-08 (Utilities) and the `## Heat Medium Basis` slice.
- **Carry open items forward.** The DBM `## Heat Medium Basis` slice lists multiple TBD/TBC items (circulation rate, sparing, heater resize, fluid rating, pop-tank SG, sour tube-rupture venting). The SoW shall list them; it shall not pretend they are resolved.

## Considerations

- **Architecture conflict (single-loop vs. hot/cold loop).** The workbook scope describes a hot/cold loop with mixing for optimum supply temperature. The DBM explicitly retires the cold/hot segregation, the separate hot expansion tank, and the separate hot pumps, and consolidates to a single 220 °C/428 °F loop. The SoW must record both and defer to human ruling. The downstream effect of this ruling is large: pump count, sparing, mixing-valve scope, and lateral-bypass scope all change.
- **Maximum bulk fluid temperature conflict.** DBM: 599 °F (315 °C); Workbook: 500 °F (260 °C). Petrotherm fluid rating confirmation will likely resolve this, but until vendor confirmation is in hand the SoW must not pick a value.
- **Expansion-tank operating pressure conflict.** Two workbook lines disagree (SOW-0167 vs. SOW-0168). The 18–35 psig range is consistent with a low-pressure surge/expansion device; 100 psig is the pump-discharge operating pressure. The likely resolution is that 100 psig was carried over from pump operating pressure in error, but the SoW must not assume that.
- **Pop tank ownership.** The DBM identifies a ~600 bbl pop tank for heater PSV discharge as part of the heat medium system. The workbook SoW for the package does not enumerate it. Whether the pop tank is in the vendor package boundary or in EPC scope is a boundary-ownership decision that must be recorded explicitly in the SoW.
- **Mole sieve regeneration gas heating removal.** The DBM removes mole sieve regen gas heating from the heat medium loop and serves it from a separate direct-fired heater. The SoW must not reintroduce that user.
- **Objective association is heuristic.** `_CONTEXT.md` lists eight objectives. Per the package-grouping heuristic and `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`, this set is directional context, not a hard requirement. Treat it as such.
- **Standards access.** API-560 and ASME Section I are referenced, but the actual standard texts are not in the local source set. Clause-level claims that need them must be marked `location TBD`.

## Trade-offs

- **Detail now vs. detail in DEL-051-02.** The SoW is intentionally narrower than the Package Datasheet. Detailed design values belong in the datasheet; the SoW carries only the values required to define the package boundary and the design envelope. Avoid duplicating the full DBM `## Heat Medium Basis` table here.
- **Workbook fidelity vs. DBM fidelity.** Pure workbook fidelity would describe a hot/cold loop with mixing — superseded by the DBM. Pure DBM fidelity would treat the workbook scope as overridden. The conservative middle is to record both and defer to ruling. This may slow vendor RFQ, but it avoids issuing a package scope against retired architecture.
- **Heater sparing options.** 1 × 125 %, 2 × 62.5 %, or 3 × 41.7 % all appear in the DBM. The SoW should record the 1 × 125 % current basis with the alternatives explicitly listed as open trade-offs rather than silently picking one.
- **Vendor-confirmed values vs. project assumptions.** Several parameters (fluid rating, circulation rate, pump sparing, heater minimum flow, pop-tank SG) are explicitly TBC/TBD pending vendor input. The SoW must not pre-empt the vendor; it must define the questions the vendor must answer.

## Examples

- Example tagged-equipment row in the SoW: `H-5170-1 — Heat Medium Heater — API-560 natural-draft cabin-style direct-fired thermal-fluid heater; design duty 1.25 × winter steady-state; current sparing basis 1 × 125 %; resize TBD per single-loop 220 °C basis.` [Source: `4-25_Deepcut_DBM.md` lines 1977, 1998-1999]
- Example user-list row: `E-5360-1 — Amine reboiler — Design duty 10,257 kW (35.0 MM BTU/h); supply 220 °C, return 135 °C.` [Source: `4-25_Deepcut_DBM.md` line 1972]
- Example responsibility statement: `Package Vendor supplies the heat medium pump module (expansion tank and 3 vertical inline circulation pumps) and the medium heater module (heater, blower, air intake pre-heater) including engineering, design, vendor documentation, and physical equipment. EPC Integrator supplies interconnecting piping, foundations, mounting, electrical supply from MCC, platforms and stairs, and DCS integration, and is responsible for facility-level integration and tie-ins.` [Sources: SOW-0166, SOW-0167, SOW-0168]
- Example open-item statement: `Single-loop circulation rate is TBD pending detailed engineering simulation; minimum circulation basis is assumed 85 % of design flow, TBC by heater vendor.` [Source: `4-25_Deepcut_DBM.md` lines 1961, 2000]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Maximum bulk fluid temperature: 599 °F (315 °C) vs. 500 °F (260 °C). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` `## Heat Medium Basis` line 1958 | `SCOPE_LEDGER.csv` SOW-0167 (Major included equipment) | Datasheet Conditions; Specification REQ-08 | PROPOSAL: DBM authoritative for facility-side bulk-temperature envelope; vendor to confirm Petrotherm rating to that maximum. | TBD |
| C-02 | Expansion-tank operating pressure: 125–240 kPag (18–35 psig) vs. 695 kPag (100 psig). | `SCOPE_LEDGER.csv` SOW-0167 | `SCOPE_LEDGER.csv` SOW-0168 | Datasheet Conditions; Specification REQ-12 | PROPOSAL: SOW-0167 (18–35 psig) is the expansion-tank operating range; SOW-0168 100 psig appears to be the pump-discharge operating pressure mis-applied to the tank. | TBD |
| C-03 | Loop architecture: single unified loop at 220 °C (DBM) vs. hot/cold loop with mixing for optimum supply (Workbook). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1945-1947 | `SCOPE_LEDGER.csv` SOW-0166 (Basic scope) | Datasheet Attributes; Specification REQ-03; Procedure step "Define architecture" | PROPOSAL: DBM authoritative (post-value-engineering supersedes pre-VE workbook scope); vendor RFQ should be issued against single-loop basis. | TBD |
| C-04 | Heat medium fluid vendor identity: "Brenntag Petrotherm" (DBM) vs. "Petro Canada Petrotherm" (Workbook). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1951 | `SCOPE_LEDGER.csv` SOW-0167 | Datasheet Attributes; Specification REQ-09 | PROPOSAL: Both reference Petrotherm; treat as same product family with supplier TBC during procurement. | TBD |
| C-05 | Pop-tank scope boundary: included in heat medium system per DBM line 2002; not enumerated in Workbook SoW package scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2002 | `SCOPE_LEDGER.csv` SOW-0166, SOW-0167 (absence) | Datasheet Construction; Specification REQ-04 (Pop tank entry) | PROPOSAL: Pop tank is part of the heat medium system; assignment to vendor package vs. EPC scope is a boundary-ownership decision requiring ruling. | TBD |
