# Specification — DEL-055-04 Vendor Engineered Equipment Package (LP Flare KO Drum, 4-25)

> Normative specification for the vendor-supplied LP flare knock-out drum
> package (drum V-3900-1, transfer pump P-3900-1, and associated module 390-1
> deliverables). Requirements derive from the accepted PROJECT_DECOMP Gate 7
> snapshot, the deliverable's `_CONTEXT.md`, and the 4-25 Deepcut DBM source
> slices. Requirements that cannot be grounded in accessible source slices are
> marked `TBD` or labelled `ASSUMPTION` per the source-grounding rule.

## Scope

### In scope (Package Vendor)
- Engineering, design, and supply of the LP flare KO drum (tag `V-3900-1`) and the LP flare KO drum transfer pump (tag `P-3900-1`), including associated module 390-1. [`4-25_Deepcut_DBM.md` lines 2029, 2581-2582, 2783]
- Vendor package design basis and datasheet set (one of the two anticipated artifacts for this deliverable). [`_CONTEXT.md` "Anticipated Artifacts"]
- Vendor documentation supporting fabrication, inspection, and turnover (see Documentation section; turnover artifacts owned by DEL-055-05).
- Shop-fabricated module assembly (390-1 LP Flare KO Drum Module). [`4-25_Deepcut_DBM.md` line 2783]
- Coordination with EPC Integrator on interface types declared in PACKAGE_REGISTER row PKG-055. [PACKAGE_REGISTER.csv]

### Out of scope (handled by EPC Integrator or other deliverables)
- Integration into the process facility, facility-level tie-ins, constructability planning, and procurement/construction coordination. [PACKAGE_REGISTER.csv row PKG-055]
- LP flare stack element and HP/cryo common flare stack design. [`4-25_Deepcut_DBM.md` lines 2030-2031]
- Flare header sizing/backpressure analysis at the facility scale (LP header sizing basis defined in DBM §"Flare Header and Backpressure Basis"). [`4-25_Deepcut_DBM.md` lines 2035-2046]
- Acceptance / review of the vendor package (covered by DEL-055-06). [PROJECT_DECOMP package siblings]
- Construction Work Package preparation (DEL-055-03). [PROJECT_DECOMP package siblings]

## Requirements

> Requirement IDs use `REQ-055-04-NN`. Each requirement cites the authoritative
> source slice or is labelled `ASSUMPTION` / `TBD` per the four-documents skill.

### Functional

| ID | Requirement | Source / Label |
|---|---|---|
| REQ-055-04-01 | The drum shall provide knock-out separation of entrained liquids from LP flare relief and blowdown vapours sourced from amine regeneration, TEG regeneration, VRU, reciprocating compressor seal pot, VRU package blowdown, VRU suction header bypass, primary seal vent, and contaminated mole-sieve regen gas blowdown, before vapours enter the LP flare stack element. | `4-25_Deepcut_DBM.md` lines 2029, 1781, 1787, 1801, 1702 |
| REQ-055-04-02 | The drum shall be sized using the LP flare relief volumes determined in detailed engineering; preliminary header sizing supported by Aspen Flare System Analyzer is consistent with a 508 mm (20 in) LP relief header. | `4-25_Deepcut_DBM.md` lines 2021, 2029 |
| REQ-055-04-03 | The transfer pump `P-3900-1` shall provide truck-out of collected liquids from the LP flare KO drum. | `4-25_Deepcut_DBM.md` line 2029 |
| REQ-055-04-04 | The package shall accommodate routing of low-pressure header sources from the drum pump to the condensate slop tank low-pressure pump header, consistent with the slop tank low-pressure header source list. | `4-25_Deepcut_DBM.md` line 1665 |

### Mechanical / Pressure

| ID | Requirement | Source / Label |
|---|---|---|
| REQ-055-04-05 | The drum design pressure shall be `TBD`, set by relief case analysis and LP header built-up backpressure determined during detailed engineering. | TBD; framing from `4-25_Deepcut_DBM.md` lines 2021, 2044 |
| REQ-055-04-06 | Typical PSV maximum total backpressure at the PSV flange shall remain below 1172 kPag (170 psig) under 150# flange rating; the drum and pump inlet shall be compatible with this header backpressure basis. | `4-25_Deepcut_DBM.md` line 2044 |
| REQ-055-04-07 | The drum shall be designed for sour-service exposure consistent with the 04-25 sour gas processing facility envelope; specific NACE MR0175 / ISO 15156 compliance and material grades — `ASSUMPTION` pending vendor metallurgy proposal. | `4-25_Deepcut_DBM.md` lines 5, 7, 2029 (ASSUMPTION) |
| REQ-055-04-08 | The drum shall be designed and registered to the governing pressure-vessel code applicable in British Columbia (ASME Section VIII Div. 1 with BC CRN registration — `ASSUMPTION`; not stated in accessible source slice). | ASSUMPTION; location TBD |
| REQ-055-04-09 | The drum minimum design metal temperature (MDMT) shall be `TBD`, set by ambient design minimums and depressurization case analysis. | TBD |

### Piping / Process Interfaces

| ID | Requirement | Source / Label |
|---|---|---|
| REQ-055-04-10 | The LP relief header connection at the drum shall be sized consistent with the 508 mm (20 in) LP flare header basis. | `4-25_Deepcut_DBM.md` line 2029 |
| REQ-055-04-11 | LP flare header material at and immediately adjacent to the drum shall be consistent with SA-106 piping per the LP flare header basis (vendor scope of supply battery limit per package datasheet). | `4-25_Deepcut_DBM.md` line 2042 |
| REQ-055-04-12 | Drum vapour outlet header shall free-drain toward the LP flare without traps or pockets, consistent with the VRU-to-LP-flare slope rule applied at the LP flare KO. | `4-25_Deepcut_DBM.md` line 1787 |
| REQ-055-04-13 | All declared interface types — Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports — shall have defined terminating connections on the package skid for EPC integration. | PACKAGE_REGISTER.csv row PKG-055 |

### Electrical / Heat Tracing / I&C

| ID | Requirement | Source / Label |
|---|---|---|
| REQ-055-04-14 | LP flare headers and instrumentation lines on the package that are routed outside heated buildings shall be electrically heat-traced and insulated for freeze protection, consistent with the LP flare-header freeze-protection rule (`ASSUMPTION`: HP rule explicit; LP rule applied because LP system can carry water and condensable liquids). PSV outlets that free-drain into the flare header are exempt. | `4-25_Deepcut_DBM.md` line 2033 (HP rule); ASSUMPTION for LP |
| REQ-055-04-15 | Area classification, hazardous area equipment ratings, grounding/bonding, and area/exterior lighting on the package skid shall match the EPC Integrator area classification basis (basis TBD). | `_CONTEXT.md`; TBD |
| REQ-055-04-16 | I&C and control cabling terminations shall be presented at vendor-marked junction boxes on the skid for EPC tie-in. | PACKAGE_REGISTER.csv interface types |

### Safety / Radiation

| ID | Requirement | Source / Label |
|---|---|---|
| REQ-055-04-17 | The drum installation shall be located such that the distance from the flare tank / KO drum to vegetation or other fire hazards is at least 10 m (32 ft), per OGAOM §9.6.15. Final siting controlled by EPC Integrator plot plan; the vendor package shall not preclude this clearance. | `4-25_Deepcut_DBM.md` line 287 |
| REQ-055-04-18 | The drum and pump package shall not impair the LP flare radiation-criteria envelope defined by BCER Oil and Gas Processing Facility Regulation App. 1, Sch. 1, §7(4), including the 0.7888 kW/m2 solar allowance. | `4-25_Deepcut_DBM.md` lines 2050-2057 |

## Standards

> Locally accessible standards / regulations referenced by the source slice:

- **BCER Oil and Gas Processing Facility Regulation, Appendix 1, Schedule 1, §7(4)** — flare radiation criteria at grade. Source: `4-25_Deepcut_DBM.md` line 2050. Location TBD (text not in accessible source slice).
- **BC OGAOM §9.6.15** — distance between flare tanks (including KO drums) and vegetation / fire hazards. Source: `4-25_Deepcut_DBM.md` line 287. Location TBD.
- **ASME Section VIII Div. 1** (governing pressure-vessel construction code — `ASSUMPTION`; not stated in accessible source slice).
- **BC Safety Authority CRN registration** (`ASSUMPTION`; not stated in accessible source slice).
- **NACE MR0175 / ISO 15156** (`ASSUMPTION`; sour service applicability per 04-25 facility envelope).
- **API 521** (relief and depressurization, governing standard for flare KO drum sizing — `ASSUMPTION`; not stated in accessible source slice).

## Verification

| Requirement ID | Verification Approach |
|---|---|
| REQ-055-04-01, REQ-055-04-02, REQ-055-04-10, REQ-055-04-12 | Vendor process datasheet review against accepted relief-volume data and LP header sizing. |
| REQ-055-04-03, REQ-055-04-04 | Vendor pump datasheet review; demonstration of pump duty against truck-out and slop-header routing cases. |
| REQ-055-04-05, REQ-055-04-06, REQ-055-04-08, REQ-055-04-09 | Vendor pressure-vessel calculation set; design registration (CRN) certificate. |
| REQ-055-04-07, REQ-055-04-11 | Material certificates, NACE MR0175/ISO 15156 compliance documentation, mill test reports. |
| REQ-055-04-13, REQ-055-04-15, REQ-055-04-16 | Interface drawing review by EPC Integrator (DEL-055-06 acceptance). |
| REQ-055-04-14 | EHT design package and insulation specification review; field walkdown at construction. |
| REQ-055-04-17, REQ-055-04-18 | EPC Integrator plot-plan / radiation analysis confirming integration compatibility (out of vendor's authority, but vendor package must not preclude). |

## Documentation

The vendor shall produce the following documentation set; specific document
list and acceptance routing are owned by DEL-055-05 (Vendor Document Turnover
Package) and DEL-055-06 (EPC Vendor Package Review and Acceptance):

- Package design basis. [`_CONTEXT.md` anticipated artifacts]
- Package datasheet set (drum + pump). [`_CONTEXT.md` anticipated artifacts]
- Pressure-vessel mechanical calculations and CRN registration.
- General arrangement and skid layout drawings.
- P&ID extract for the package battery limit.
- Material certificates and NACE compliance documentation.
- EHT design package (if EHT included in vendor scope).
- I&C loop diagrams, junction-box termination schedules.
- Inspection and test plan (ITP).
- Operations and maintenance manuals (turnover content — owned by DEL-055-05).
- Spare parts list and recommended commissioning spares.

Document content and acceptance criteria specific to turnover are `TBD` here
(owned by DEL-055-05 / DEL-055-06).
