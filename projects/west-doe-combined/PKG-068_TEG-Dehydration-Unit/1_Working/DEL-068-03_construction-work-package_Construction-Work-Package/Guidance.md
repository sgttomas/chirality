# Guidance: DEL-068-03 — Construction Work Package (TEG Dehydration Unit)

## Purpose

This Construction Work Package (CWP) is the **EPC Integrator's controlling document** for how the vendor-supplied TEG Dehydration Unit (PKG-068) is physically installed into the 04-25 Deepcut facility and turned over for commissioning. The decomposition explicitly identifies it as a **mandatory Gate 5 EPC anchor deliverable**. [Source: DELIVERABLE_REGISTER.csv row 548 Notes; `_CONTEXT.md`]

It exists because the workbook + 26020 package requirements split the TEG Dehydration Unit into a **vendor-owned package** plus **EPC-owned facility integration**: the vendor cannot install the package into the facility, and the EPC must explicitly own all "by others" construction scope (foundations, interconnecting piping, electrical to the burner control panel, etc.) plus all 13 facility-level interfaces flagged YES for PKG-068. [Source: PACKAGE_REGISTER.csv row 97; SOW-0240; INTERFACE_REGISTER.csv PKG-068 rows; OBJ-004]

## Principles

1. **Vendor scope is sacrosanct.** The CWP must not redesign or re-engineer the vendor package. EPC actions are receipt, set, tie-in, test, and turnover — not package internals. [Source: OBJ-004; PACKAGE_REGISTER.csv row 97]
2. **All declared interfaces must appear as work.** Every `YES` interface row in INTERFACE_REGISTER.csv for PKG-068 must show up as identifiable construction scope in the CWP. Missing interfaces lead to commissioning gaps. [Source: INTERFACE_REGISTER.csv PKG-068 rows; OBJ-006, OBJ-007]
3. **By-others items must be explicitly claimed.** The source instruction names interconnecting piping, foundations, and burner-control-panel electrical supply as "by others" from the vendor side. These are EPC obligations and must be unambiguous in the CWP. [Source: SOW-0240]
4. **Treat the TEG unit as common equipment.** Construction provisions must support safe isolation, drain, blind, and maintenance access because a single train serves the facility. [Source: `4-25_Deepcut_DBM.md` line 2429]
5. **Source over decomposition.** Where the DBM or 26020 package document gives a value (e.g., 425 °F heat-medium supply, 1,480 psig design pressure, 150 °F design temperature, Module 520/570 contents), the source wins over decomposition summaries. [Source: `4-25_Deepcut_DBM.md` lines 1214, 1375; SOW-0240; DBM module table]
6. **Sour-service safety is integral.** Flare, drain/containment, F&G, and shutdown integration are part of construction acceptance, not afterthoughts. [Source: OBJ-009; `4-25_Deepcut_DBM.md` SEC-09, SEC-14]

## Considerations

| Consideration | Rationale |
|---|---|
| **Module fabrication is shop-based for Module 570.** The DBM module fabrication table lists "570-1 TEG Dehydration Module" as Shop. Site work is therefore primarily set, tie-in, and integration rather than stick-built construction. [Source: `4-25_Deepcut_DBM.md` line 2795] | Drives planning toward heavy-lift, alignment, and tie-in workfronts rather than field fabrication. |
| **Module 520 mixes vendor and non-vendor equipment.** Module 520 contains TEG dehy equipment (TEG inlet air cooler, filter coalescer, contactor, cooler, level pot) alongside amine equipment. [Source: `4-25_Deepcut_DBM.md` line 1131] | Construction interfaces between PKG-068 and amine-treating packages within a shared module require interface coordination. |
| **High temperature heat medium (425 °F) at the TEG reboiler.** [Source: `4-25_Deepcut_DBM.md` lines 1214, 1375] | Drives heat-medium piping spec, EHT, supports, and personnel-protection requirements at tie-ins. |
| **Multiple flare/vent destinations.** TEG contactor blowdown → HP flare; TEG flash drum LP blowdown and still overheads (recovered to VRU with LP flare backup) → LP flare. [Source: `4-25_Deepcut_DBM.md` lines 1360, 2029] | CWP must clearly identify which package nozzles tie into HP vs. LP flare headers and to VRU suction. |
| **Contactor sparing/configuration TBD.** The DBM keeps TEG contactor configuration open between 1 × 100% and 2 × 50%. [Source: `4-25_Deepcut_DBM.md` lines 1222, 1237, 1386] | Foundation, structural, and piping designs handed to construction must reflect the configuration locked in detailed engineering — CWP should not freeze ahead of that decision. |
| **Burner control panel power source.** Explicitly excluded from vendor supply. [Source: SOW-0240] | EPC must size and route a dedicated supply; not assume vendor terminations. |

## Trade-offs

| Trade-off | Discussion |
|---|---|
| **Pre-set tie-in piping vs. measured field fits.** | Shop-modular packages benefit from pre-fab tie-in spools, but field-measured spools reduce fit-up rework. Choose by tie-in tolerance band against vendor module dimensional tolerance. TBD — no DBM guidance found. |
| **Sequence: set TEG modules before or after adjacent amine modules.** | Module 520 mixing of amine and TEG equipment may force a coordinated set sequence; preserves access for crane swings and tie-in. ASSUMPTION: amine modules set first because process flow is upstream-to-downstream; confirm during heavy-lift planning. |
| **Common-equipment maintenance bypass provisions.** | Single-train architecture means future maintenance requires facility outage. Construction can over-provide tie-in isolation valves and spool-piece points now; cost vs. future outage exposure. [Source: `4-25_Deepcut_DBM.md` line 2429] |
| **Burner control panel electrical source: dedicated feeder vs. shared MCC.** | Vendor exclusion silent on origin. ASSUMPTION: source from local MCC with dedicated breaker; confirm electrical SLD. |

## Examples

- **Tie-in example — TEG contactor blowdown to HP flare.** The DBM states "TEG contactor automated blowdown to HP flare". CWP work pack: route blowdown line from vendor-supplied package nozzle to the HP flare header, install isolation and check valves per piping class, hydrotest with the HP flare lateral, F&G loop check on shutdown. [Source: `4-25_Deepcut_DBM.md` line 1360]
- **Tie-in example — TEG reboiler heat medium.** Heat medium at 425 °F supply via mixing valves; install lateral with mixing valve, control valve, isolation, and EHT/insulation; align with heat-medium loop heater minimum-flow basis. [Source: `4-25_Deepcut_DBM.md` lines 1214, 1375, 1961]
- **By-others example — burner control panel power.** Pull and terminate a dedicated power circuit to the vendor-supplied burner control panel; vendor provides termination details. [Source: SOW-0240]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CFL-068-03-01 | Decomposition narrative says "physically installed, built, inspected, turned over, and tied into the larger facility systems," which can be read to include site fabrication; DBM module table assigns the TEG Dehydration Module to Shop fabrication. | DELIVERABLE_REGISTER.csv row 548 description | `4-25_Deepcut_DBM.md` line 2795 (570-1 = Shop) | Datasheet "Module fabrication location"; Specification R-CWP-068-03-04; Procedure Steps | DBM is authoritative for fabrication location; CWP plans for shop-built receipt + site set/tie-in, not site fabrication. | TBD |
| CFL-068-03-02 | TEG contactor sparing/configuration TBD in DBM; affects foundations, piping, supports the CWP must reflect. | `4-25_Deepcut_DBM.md` lines 1222, 1237, 1386 | n/a — open item | Specification R-CWP-068-03-04, R-CWP-068-03-07; Procedure | Hold CWP-final issue until detailed engineering closes the sparing basis; issue CWP for construction only after configuration confirmed. | TBD |
| CFL-068-03-03 | Process piping classification for TEG package internals/tie-ins is not stated in extracted DBM (only heat-medium loop is given ASME Cat D). | `4-25_Deepcut_DBM.md` line 1933 (heat medium only) | None found for TEG process piping | Specification Standards table; R-CWP-068-03-07 | Adopt ASME B31.3 with piping class set from project piping spec; mark `location TBD` until project piping spec confirms. | TBD |

## TBD / Open Items

- ASME and CSA standard citations are listed as ASSUMPTION; confirm against project specifications. [Spec Standards table]
- TEG contactor sparing/configuration (1 × 100% vs. 2 × 50%) pending detailed engineering. [`4-25_Deepcut_DBM.md` lines 1222, 1237, 1386]
- Vendor-document tables in `26020-Package_Requirements.docx` package heading 23 not extracted to markdown; specific vendor document IDs called out by source remain `location TBD` until the source is extracted.
- Strategic ESD pushbutton locations for large modules without buildings (TEG dehy not explicitly identified, but cryogenic and molecular sieve modules are). [`4-25_Deepcut_DBM.md` lines 3270, 3303, 3314]
