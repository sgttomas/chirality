# Specification — DEL-083-01 Scope of Work (PKG-083 Inlet Separators 3-25)

## Scope

### In Scope

The EPC Integrator shall deliver a Scope of Work covering the PKG-083 Inlet Separators 3-25 package at the 03-25 West Doe Compressor Station, including:

1. **Tagged equipment and package identity list** for the two horizontal three-phase inlet separator packages V-1600-2 and V-1700-2, their inlet pressure-control valves, produced-water level-control valves, internals (manually adjustable weir, mist eliminators, de-sanding provisions, Devchem 253 internal coating), and associated heated self-framing building enclosure (extent TBD). [Source: DBM §SEC-04 "Inlet Separation"; `_CONTEXT.md` Anticipated Artifacts.]
2. **Package function and integration narrative** describing three-phase separation of sour gas, raw condensate, and produced water at 50% facility capacity per train, and outgoing stream routing to: inlet compression (gas), 04-25 MPFS/stabilization (raw condensate), and the liquids hub produced-water system (water). [Source: DBM §SEC-01 "Facility Overview", §SEC-04.]
3. **Source basis** explicitly citing the governed 03-25 DBM (current basis CAT-004; SCA-002 discharge pressure supersession noted in DBM §SEC-04 "Source and Governance Note") and the Package Requirements basis (`26020-Package_Requirements.docx` package heading 36 — **location TBD**, source not parsed locally).
4. **Boundaries** drawn at:
   - upstream: inlet ESDV and pig receiver isolation (pig receiver and ESDV are out-of-package; see Exclusions);
   - gas downstream: package outlet flange to inlet compressor suction (KM-2150 / KM-2250);
   - condensate downstream: package outlet to raw-condensate forwarding to 04-25;
   - produced-water downstream: package outlet to liquids-hub produced-water transfer;
   - utility: tie-in flanges for fuel gas, instrument air (supplied from 04-25 per SCA-006), electrical power, and controls;
   - flare/vent: tie-in to HP flare and sweet-gas purge system. [Source: DBM §SEC-04, §SEC-01 "Commercial and Facility Interfaces".]
5. **Whole-facility integration narrative** describing how the package fits within the 03-25 / 04-25 split (raw-condensate routing to 04-25, drive-gas recycle from downstream of inlet compressor aftercoolers per DBM §SEC-04 "Flow Distribution and Controls"). [Source: DBM §SEC-01, §SEC-04; Trace_Appendix.md KTY-04-02 KA-06.]
6. **Responsibility assignment record** identifying EPC Integrator scope versus owner-furnished, vendor-furnished, and third-party scope (e.g., NRM LACT scope is excluded except for facility-side tie-in). [Source: DBM §SEC-01 "Commercial and Facility Interfaces"; `_CONTEXT.md` Anticipated Artifacts.]

### Out of Scope (Exclusions)

- Detailed equipment datasheets, P&IDs, mechanical drawings (separate package deliverables — TBD which DEL IDs).
- Inlet compressor packages (KM-2150, KM-2250) and TEG dehydration package (separate packages per DBM §SEC-05).
- Pig receiver and inlet ESDV procurement (covered upstream of the separator package per DBM §SEC-04 "Pig Receiver" subsection; **ASSUMPTION** that these sit in a separate package — confirmation TBD via PACKAGE_REGISTER.csv).
- Local stabilization, local SOC, local heat-medium system, local instrument-air compressors — all removed/superseded per DBM §SEC-01 "Exclusions and Superseded Scope".
- Third-party LACT packages except facility-side power/tie-in.
- Stabilized condensate return handling at the Liquids Hub (separate package scope).

## Requirements

### R1 — Equipment identity completeness
The Scope of Work shall list every tagged item in the inlet separation packages, including vessels V-1600-2 and V-1700-2 and all in-package valves, internals, and instrumentation skids that constitute the package boundary. [Source: DBM §SEC-04; verification by cross-check against PACKAGE_REGISTER.csv.]

### R2 — Process duty consistency
The package duty statement shall match the per-separator basis: 40 MMSCFD gas, 556 m3/d condensate, 1,800 m3/d produced water, 4,963 kPag design pressure, ANSI 600# class, ~38 m3 slug handling per separator. [Source: DBM §SEC-04 "Inlet Separation".]

### R3 — Sour-service design basis
The Scope of Work shall require sour-service materials and inspection consistent with H2S design 0.3 mol% (license 2.0 mol%) and applicable codes for sour vessels (NACE MR0175 / ISO 15156 — **ASSUMPTION**: applicable code; explicit citation in DBM §SEC-08 vessel general was not extracted in this pass — **location TBD**). [Source: DBM §SEC-03 raw gas H2S; DBM §SEC-04 internal coating; NACE MR0175 ASSUMPTION.]

### R4 — Internal coating
Inlet separator vessels shall specify Devchem 253 internal coating; piping is not coated under the current basis. [Source: DBM §SEC-04 "Inlet Separation"; §SEC-08 vessels (location TBD).]

### R5 — Internals
Each separator shall include a manually adjustable weir, high-performance mesh/vane mist eliminators (vertical and horizontal), and de-sanding provisions. [Source: DBM §SEC-04 "Inlet Separation"; Trace_Appendix.md KA-10, KA-11, KA-12.]

### R6 — Inlet pressure-control valves
Each package shall provide at least two parallel inlet pressure-control valves using balanced globe hardened trim with a differential pressure limit of no more than 5 psid. [Source: DBM §SEC-04 "Flow Distribution and Controls"; Trace_Appendix.md KA-13.]

### R7 — Produced-water level-control valves
Each package shall provide at least two parallel produced-water level-control valves. [Source: DBM §SEC-04 "Flow Distribution and Controls"; Trace_Appendix.md KA-14.]

### R8 — Symmetrical inlet piping
Inlet piping arrangement shall distribute flow evenly between the two separator trains. [Source: DBM §SEC-04 "Flow Distribution and Controls".]

### R9 — Drive-gas recycle interface
The package shall accept drive-gas recycle from downstream of inlet compressor aftercoolers, with drive-gas pressure set above the 04-25 stabilizer flash feed separator pressure. [Source: DBM §SEC-04 "Flow Distribution and Controls"; Trace_Appendix.md KA-06.]

### R10 — Sweet-gas purge and HP flare vent
Sweet-gas purge and HP flare vent provisions shall be included on inlet separation package as continuous with the pig receiver / ESDV purge basis. **ASSUMPTION** that purge provisions are physically on the separator package boundary; DBM language ties them to the pig receiver. **Conflict surfaced — see Guidance Conflict Table CT-01.** [Source: DBM §SEC-04 "Pig Receiver" paragraph + KTY-04-02 KA-08 (Trace_Appendix.md).]

### R11 — Building and module configuration
Each package shall be modularized for shop assembly with instrumentation and one end of each package enclosed in a heated self-framing building. Exact building extent is TBD and shall be resolved during detailed design. [Source: DBM §SEC-04 "Inlet Separation"; Trace_Appendix.md KA-15.]

### R12 — Shutdown pressure setpoints
Inlet separator ESDV shutdown pressure shall be 635 psig (current basis); delivery-point ESDV shutdown is TBC. [Source: DBM §SEC-04 "Pig Receiver" paragraph (635 psig at inlet separator ESDV).]

### R13 — Methanol drain
The separator boot shall accommodate methanol that may appear infrequently; downstream methanol disposition remains TBD. [Source: DBM §SEC-04 methanol note.]

### R14 — Capacity language reconciliation
The Scope of Work shall use the current "2 x 50%" capacity basis; the older "2 x 100%" table language is superseded and shall be reconciled. [Source: DBM §SEC-04 "Inlet Separation" tables (older "2 x 100 percent table language requires reconciliation").]

### R15 — Inlet temperature reconciliation
The Scope of Work shall carry inlet design temperature as 8.3 deg C with a note that detailed design shall reconcile this against downstream excerpts before issuing final equipment datasheets. [Source: DBM §SEC-04 inlet conditions paragraph.]

### R16 — Whole-facility integration narrative
The narrative shall describe upstream Doe field interface, downstream routing to inlet compression, raw-condensate routing to 04-25 MPFS/stabilization, produced-water routing to the liquids hub, and shared utilities supplied from 04-25 (instrument air per SCA-006). [Source: DBM §SEC-01 "Facility Overview", "Commercial and Facility Interfaces", "Exclusions and Superseded Scope".]

### R17 — Responsibility matrix
The Scope of Work shall include a responsibility assignment record covering at minimum: EPC Integrator scope, owner-furnished equipment (if any — TBD), vendor-furnished packaging scope, NRM third-party scope (excluded except facility-side tie-in), and 04-25 plant scope at the package interfaces. [Source: DBM §SEC-01 "Commercial and Facility Interfaces"; `_CONTEXT.md` Anticipated Artifacts.]

## Standards

| Standard | Applicability | Location |
|---|---|---|
| CSA Z662 | Pipeline overpressure protection and pipeline design (referenced for sour-gas export) — relevance to package-boundary piping TBD | DBM §SEC-04 "Sour-Gas Export" |
| NACE MR0175 / ISO 15156 | Sour-service materials (ASSUMPTION — applicability for H2S 0.3 mol% / license 2.0 mol% service); explicit DBM citation **location TBD** | ASSUMPTION |
| ASME Section VIII (pressure vessels) | Vessel design for 4,963 kPag, ANSI 600#, sour service (ASSUMPTION pending DBM §SEC-08 extraction) | ASSUMPTION; location TBD |
| NEMA MG1, IEEE Std 841, IEC ratings | Applicable to motors on motor-operated valves and ancillary drives, where present (TBD) | TBD |
| 26020-Package_Requirements.docx, package heading 36 | Owner package requirement basis | location TBD (DOCX not parsed in this pass) |

## Verification

| Req | Verification Approach |
|---|---|
| R1 | Cross-check Scope of Work equipment list against PACKAGE_REGISTER.csv and ARTIFACT_REGISTER.csv (GATE-07 snapshot). |
| R2 | Compare duty statements with DBM §SEC-04 table; flag any deviation. |
| R3 | Materials review against accepted sour-service code (citation to be resolved before issue). |
| R4, R5 | Vendor data review against DBM §SEC-04 internals list. |
| R6, R7 | P&ID and instrument index review showing parallel valve sets per package. |
| R8 | Piping isometric review for symmetrical inlet manifold. |
| R9 | P&ID review for drive-gas recycle tie-in; pressure-setpoint review against 04-25 stabilizer flash feed separator pressure. |
| R10 | Resolution of Conflict Table CT-01 in `Guidance.md` to confirm boundary of purge/vent provisions. |
| R11 | Module general-arrangement review; building extent resolution log. |
| R12 | Cause-and-effect / SIL review of shutdown pressure setpoints. |
| R13 | P&ID review of separator boot drain to methanol disposition (downstream TBD). |
| R14, R15 | Reconciliation log signed by EPC Integrator before equipment datasheets issued. |
| R16 | Narrative review against DBM §SEC-01. |
| R17 | Responsibility matrix signed by all parties at SoW issue. |

## Documentation (Anticipated Artifacts)

- Package scope of work (this deliverable's principal artifact)
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record

(Per `_CONTEXT.md` Anticipated Artifacts.)
