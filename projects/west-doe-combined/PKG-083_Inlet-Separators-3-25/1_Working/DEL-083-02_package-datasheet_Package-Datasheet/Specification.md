# Specification — DEL-083-02 Package Datasheet (PKG-083 Inlet Separators 3-25)

Status: INITIALIZED (P1_P2 draft). Normative content grounded in DBM-Comp_and_Liquids SEC-04 and PACKAGE_REGISTER row 67. Inferred items labeled ASSUMPTION; missing values TBD.

## Scope

### In Scope

- Technical handoff datasheet content sufficient for third-party vendor or discipline package engineering and design of the PKG-083 Inlet Separator package, comprising two horizontal three-phase separators (V-1600-2, V-1700-2) at 03-25 West Doe Compressor Station. Source: `_CONTEXT.md` Scope; DBM SEC-04 "Inlet Separation".
- EPC Integrator interface and integration requirements for the eleven applicable interface types in INTERFACE_REGISTER.csv for PKG-083.
- Source-anchored equipment design criteria, operating conditions, and construction requirements (Datasheet.md tables are the carrier).

### Out of Scope (Exclusions)

- Package vendor engineering, design, fabrication, and physical equipment package — covered by DEL-083-04. Source: DELIVERABLE_REGISTER.csv.
- Construction installation and tie-in workface planning — covered by DEL-083-03. Source: DELIVERABLE_REGISTER.csv.
- Vendor document register and submittals — covered by DEL-083-05. Source: DELIVERABLE_REGISTER.csv.
- Inlet pipeline scope upstream of the first aboveground flange within the lease boundary (Doe field pipeline contractor scope). Source: DBM SEC-04 "Inlet Pipeline Interface and Pigging" line 228.
- Downstream stabilization at 03-25 (consolidated to 04-25 under SCA-002). Source: DBM SEC-03 "Scope Removals/Supersessions".

## Requirements

Each requirement is a normative claim grounded in an accessible source. Items without an accessible source basis are marked TBD or ASSUMPTION, never asserted.

### R-1 Equipment Count and Configuration

- R-1.1: The package shall comprise two (2) identical horizontal three-phase inlet separator packages, tagged V-1600-2 and V-1700-2. Source: DBM SEC-04 "Inlet Separation".
- R-1.2: Each separator shall be sized for one half of facility capacity. Source: DBM SEC-04.

### R-2 Per-Separator Process Design Basis

- R-2.1: Gas flow capacity shall be 40 MMSCFD per unit. Source: DBM SEC-04 design table.
- R-2.2: Condensate flow capacity shall be 556 m3/d (3,494 bbl/d) per unit. Source: DBM SEC-04.
- R-2.3: Produced-water flow capacity shall be 1,800 m3/d (11,322 bbl/d) per unit. Source: DBM SEC-04.
- R-2.4: Separator vessel diameter shall be 2,743 mm (9 ft); straight-side length shall be 12,191 mm (40 ft). Source: DBM SEC-04.
- R-2.5: Pressure class shall be ANSI 600#; design pressure shall be 4,963 kPag. Source: DBM SEC-04.
- R-2.6: Slug handling capacity shall be approximately 38 m3. Source: DBM SEC-04.

### R-3 Operating Conditions

- R-3.1: Inlet operating-pressure envelope shall accommodate low 125 psig, design 200 psig, and maximum 572 psig. Source: DBM SEC-04. Normal-high value is TBC.
- R-3.2: Inlet ESDV shutdown pressure setpoint shall be 635 psig. Source: DBM SEC-04 "Inlet Pipeline / Pigging" line 230.
- R-3.3: Inlet design temperature is 8.3 deg C (current feed basis). Source: DBM SEC-04. (CONFLICT — see Guidance Conflict Table CF-01.)

### R-4 Internals and Coating

- R-4.1: Internal coating shall be Devchem 253. Source: DBM SEC-04.
- R-4.2: Internals shall include a manually adjustable weir, vertical and horizontal high-performance mesh/vane mist eliminators, and de-sanding provisions. Source: DBM SEC-04.
- R-4.3: Piping is not required to be coated under the current separator basis. Source: DBM SEC-04.

### R-5 Pressure and Level Control

- R-5.1: Each package shall include at least two (2) parallel inlet pressure-control valves with balanced globe hardened trim and a differential-pressure limit of 5 psid or less. Source: DBM SEC-04 "Flow Distribution and Controls".
- R-5.2: Each package shall include at least two (2) parallel produced-water level-control valves. Source: DBM SEC-04.
- R-5.3: Inlet piping shall be arranged symmetrically to distribute flow evenly to the two separator trains. Source: DBM SEC-04.
- R-5.4: Drive-gas recycle from downstream of inlet-compressor aftercoolers shall return to the separators; drive-gas pressure shall be set above the 04-25 stabilizer flash-feed separator pressure. Source: DBM SEC-04.

### R-6 Building Enclosure and Winterization

- R-6.1: Instrumentation and one end of each package shall be enclosed in a heated self-framing building. Source: DBM SEC-04. Exact building extent is TBD.

### R-7 Methanol and Drainage

- R-7.1: The separator boot shall accept infrequent methanol drainage. Source: DBM SEC-03 line 218. Downstream methanol disposition is TBD.

### R-8 Interface Requirements

The package shall provide tie-ins and integration provisions for the eleven applicable interface types listed in INTERFACE_REGISTER.csv for PKG-083 (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports). Source: INTERFACE_REGISTER.csv. Interface clause-level requirements per type: TBD pending the EPC-issued interface specification (not present in the deliverable folder).

### R-9 Pressure-Vessel Code (ASSUMPTION)

- R-9.1: Vessels are expected to comply with ASME BPVC Section VIII Div. 1 — ASSUMPTION; not stated in the accessible DBM slice. Verify against 26020-Package_Requirements.docx heading 36 (location TBD).

## Standards

The DBM source slice for inlet separation does not enumerate vessel/code standards for PKG-083 explicitly. Candidate governing standards (treat as ASSUMPTION until verified against the binary source documents):

- ASME BPVC Section VIII Div. 1 — pressure-vessel design (ASSUMPTION; location TBD).
- CSA Z662 — sour-service pipeline and overpressure protection; named in DBM SEC-04 "Sour-Gas Export" for downstream pipeline; applicability to package piping is TBD.
- NACE MR0175 / ISO 15156 — sour-service materials; ASSUMPTION based on stated H2S service (DBM SEC-05 compressor inlet ~0.296 mol% H2S); location TBD.
- ASME B16.5 — flange dimensions (ANSI 600#); ASSUMPTION; location TBD.
- 26020-Package_Requirements.docx heading 36 — project-specific package requirements (location TBD; binary not text-accessible).
- 26020-02-PT-RFQ-17-003_Inlet Separators 1_R0.docx — package RFQ (location TBD; binary not text-accessible).

## Verification

| Requirement | Verification Approach | Verification Record |
|---|---|---|
| R-1.x | Vendor GA drawing and equipment list review (EPC integration acceptance) | Package acceptance checklist (DEL-083-06) |
| R-2.x | Vendor process datasheet review against this Specification's design table | Vendor document review log (DEL-083-06) |
| R-3.x | Operating-condition matrix cross-check vs PFD/P&ID at IFR/IFC | Design review record |
| R-4.x | Vendor internals drawing + coating spec review | Vendor document review log |
| R-5.x | Control-valve schedule and P&ID review | Design review record |
| R-6.x | Building/HVAC plan vendor submittal review | Vendor document review log |
| R-7.x | P&ID review of separator boot drain routing | Design review record |
| R-8.x | Interface specification cross-check (each IFC-* row from INTERFACE_REGISTER.csv) | Package interface requirements matrix |
| R-9.x | Vessel U-stamp data report (ASME) at FAT | FAT report; ASME data report |

## Documentation

Anticipated artifacts (from `_CONTEXT.md` "Anticipated Artifacts"):

- Package technical datasheet (this kit's Datasheet.md is the EPC-issued carrier; vendor will return a populated vessel datasheet).
- Vendor engineering handoff basis package.
- Package interface requirements matrix (per INTERFACE_REGISTER.csv set).
- Source-supported equipment and design criteria summary.

Document control: vendor submittals tracked through DEL-083-05 (Vendor Document Turnover Package); EPC review/acceptance through DEL-083-06.
