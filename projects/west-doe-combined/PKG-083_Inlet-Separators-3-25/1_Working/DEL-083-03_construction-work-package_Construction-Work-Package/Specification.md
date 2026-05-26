# Specification — DEL-083-03 Construction Work Package (PKG-083 Inlet Separators 3-25)

## Scope

### Covered

This Construction Work Package (CWP) defines the EPC Integrator's plan to receive, install, integrate, inspect, and turn over the PKG-083 Inlet Separators 3-25 package (V-1600-2, V-1700-2) into the 03-25 West Doe Compressor Station and Liquids Hub. It covers:

- Site receipt, rigging, setting, and anchoring of the two horizontal three-phase separator packages on prepared foundations.
- Tie-in to upstream pig receiver / inlet ESDV piping.
- Tie-in to downstream gas, raw condensate, and produced-water routing.
- Connection of EPC-scope interface types listed in PACKAGE_REGISTER.csv row PKG-083: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.
- Pre-commissioning, mechanical completion verification, and turnover.

### Excluded

- Package vendor engineering, package design, vendor documentation, and physical equipment package supply (Package Vendor scope per PACKAGE_REGISTER.csv row PKG-083).
- Electrical Power and Building HVAC / Services interface types — not listed against PKG-083 in PACKAGE_REGISTER.csv. ASSUMPTION: these are either inside the vendor package boundary or scoped to a different package; confirmation TBD.
- Operations and process commissioning beyond mechanical turnover (CWP scope ends at handoff per `_CONTEXT.md`).
- Stabilization, MPFS, and downstream 04-25 facility scope (DBM §SEC-03; routed to 04-25).

## Requirements

### R1 — Foundations, Setting, and Anchoring

R1.1 Foundations shall be designed and constructed to accept two horizontal three-phase separator packages with vessel diameter 2,743 mm (9 ft) and straight-side length 12,191 mm (40 ft). [Source: DBM §SEC-04 separator parameter table]
R1.2 Setting tolerances, anchor-bolt patterns, and saddle loads shall match the vendor package general arrangement and certified loads. ASSUMPTION: detailed values from vendor data; location TBD until vendor GAs are received against 26020-02-PT-RFQ-17-003.
R1.3 The CWP shall identify rigging study, crane plan, and lift envelope for setting V-1600-2 and V-1700-2 within the heated self-framing building footprint (DBM §SEC-04: instrumentation and one end of each package enclosed in a heated self-framing building; exact extent TBD).

### R2 — Process Piping Tie-ins

R2.1 Inlet piping arrangement shall be symmetrical to distribute flow evenly between the two separator trains. [Source: DBM §Flow Distribution and Controls]
R2.2 Tie-in to inlet ESDV shall accept full-port, piggable ESDV with position transmitters; current shutdown-pressure value at the inlet separator ESDV is 635 psig. [Source: DBM §Pig Receiver / ESDV]
R2.3 Inlet pressure-control valve manifold per package shall accommodate at least two parallel valves with balanced globe hardened trim and a differential pressure limit of <=5 psid. [Source: DBM §Flow Distribution and Controls]
R2.4 Produced-water level-control valve manifold per package shall accommodate at least two parallel valves. [Source: DBM §Flow Distribution and Controls]
R2.5 Drive-gas recycle return line from downstream of inlet compressor aftercoolers shall be tied into each separator at the vendor-defined nozzle. [Source: DBM §Flow Distribution and Controls]
R2.6 Pressure class for separator-package process piping at the tie-in flanges shall match the 600# rating of the vessels unless vendor data specifies otherwise. [Source: DBM §SEC-04 table — 600# pressure class]

### R3 — Utility Piping

R3.1 Instrument air, fuel gas, and other utility services shall be supplied per the facility utility plan; instrument air is supplied from 04-25 (no local compression at 03-25 under SCA-006). [Source: DBM §Facility Description]
R3.2 Methanol drain provisions shall be made at the inlet separator boot. Downstream methanol disposition is TBD per source. [Source: DBM §SEC-03 line 218]

### R4 — Relief / Flare / Vent

R4.1 PSV outlet headers and flare/vent connections shall tie into the shared HP/Cryo and LP flare and incinerator system per the current 03-25/04-25 allocation. [Source: DBM §Facility Description]
R4.2 Sweet-gas purge and HP flare vent provisions shall be carried at the upstream pig receiver interface as needed for the inlet system. [Source: DBM §Pig Receiver / ESDV]

### R5 — Drain / Containment

R5.1 Closed and open drain tie-ins shall be installed per the facility drain plan, accommodating sour service and sour produced water.
R5.2 Containment provisions shall match the package skid drain points. ASSUMPTION: specific routing per facility plan; location TBD.

### R6 — EHT (Electric Heat Tracing)

R6.1 EHT shall be installed on lines and instrumentation requiring freeze protection or process-temperature maintenance per the EHT line list. ASSUMPTION: EHT line list is a downstream input; location TBD.

### R7 — Grounding / Bonding

R7.1 Each separator package and associated piping shall be grounded and bonded per facility grounding standard. ASSUMPTION: standard reference TBD.

### R8 — Area / Exterior Lighting

R8.1 Area lighting in the separator skid vicinity and within the enclosed building portion shall be installed per facility lighting plan.

### R9 — I&C / Control Cabling

R9.1 Field instrumentation provided on the vendor package shall be cabled back to the facility control system per the I&C tie-in schedule. Specific instrument list, location TBD.

### R10 — Fire & Gas / Safety Systems

R10.1 Fire and gas detection coverage for the separator skid and enclosing building shall be installed per the facility F&G layout.
R10.2 Inlet ESDV interlocks shall be terminated and tested.

### R11 — Maintenance Access

R11.1 Maintenance access for manway, mist eliminator removal, weir adjustment, and de-sanding provisions shall be preserved during permanent installation. [Source: DBM §SEC-04 — manually adjustable weir; vertical/horizontal high-performance mesh/vane mist eliminators; de-sanding provisions]

### R12 — Structural / Foundations / Supports

R12.1 Supports for tie-in piping, building, and access platforms shall be designed and erected per facility structural standards.

### R13 — Inspection and Turnover

R13.1 Construction interface and turnover checklist shall be executed and signed per `_CONTEXT.md` anticipated artifacts.
R13.2 Pre-commissioning shall verify mechanical completion of all tie-ins enumerated in R2 through R12.

## Standards

The following are governing or invoked by the source materials read; clause-level extraction is deferred until source-clause text is accessible:

- CSA Z662 — overpressure protection and pipeline design applies to outlet pipeline systems referenced in DBM §Sour-Gas Export (clause set: location TBD for separator-package tie-ins).
- NEMA MG1 — invoked for inlet compressor motors, not for separators (DBM §SEC-05). Listed for awareness; not a CWP requirement here.
- Other applicable codes (ASME B31.3 for process piping, ASME Section VIII for vessels, etc.) are presumed applicable to project execution but are not explicitly cited in the accessed DBM slices. location TBD.

## Verification

| Requirement set | Verification approach |
|---|---|
| R1 (foundations/setting) | Survey of anchor patterns and elevations against vendor GA; record in turnover checklist |
| R2 (process piping) | Hydrotest / pneumatic test per piping line list; flange make-up records; ESDV stroke and position-transmitter functional test |
| R3 (utility piping) | Continuity and pressure tests; instrument-air pressure verification at delivery point |
| R4 (relief/flare/vent) | Walk-down against PSV outlet schedule; flare header tie-in inspection |
| R5 (drains) | Drain-system walk-down; slope and routing inspection |
| R6 (EHT) | Megger / continuity test per EHT circuit; commissioning energization |
| R7 (grounding/bonding) | Ground-resistance measurement; bonding visual + continuity |
| R8 (lighting) | Lux verification per area; functional test |
| R9 (I&C cabling) | Loop checks per loop sheet; signal continuity |
| R10 (F&G) | Detector calibration and functional test; ESDV interlock test |
| R11 (access) | Walk-down against maintenance-access criteria |
| R12 (structural) | Bolt-up and weld inspection; load-path verification per structural drawings |
| R13 (turnover) | Signed construction interface and turnover checklist |

## Documentation

Per `_CONTEXT.md` anticipated artifacts and the requirements above, this CWP shall produce:

- Construction Work Package document (this Specification + plan attachments)
- Installation and tie-in workface plan (FIWP-level steps and sequencing)
- Construction interface and turnover checklist
- Test/inspection evidence (hydrotest reports, loop check sheets, ESDV stroke tests, F&G test records)
- Punch list and turnover certificate
