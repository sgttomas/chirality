# Specification — DEL-049-02 Package Datasheet (Sales Gas Booster Compressor, PKG-049)

> Normative requirements for the EPC Package Datasheet artifact that supports
> third-party Package Vendor engineering of the Sales Gas Booster Compressor
> package. Requirements are source-grounded; inferred or convention-based
> requirements are labeled `ASSUMPTION`. Unresolved values are `TBD`.

## 1. Scope

### 1.1 In Scope

This datasheet defines the package data the EPC Integrator hands off to the
Package Vendor for engineering, design, and vendor documentation of the Sales
Gas Booster Compressor package (`PKG-049`, tag `26020-01-PT-12-004`), as
described in PACKAGE_REGISTER row 80 (GATE-07 snapshot).

Coverage:

- Package identification and configuration basis (one x 100% sweet sales gas
  booster, single-stage reciprocating, induction-motor driven). Source: DBM
  Deepcut §932-§936.
- Process design conditions (suction/discharge pressure and temperature,
  capacity, MAWP, inlet composition). Source: DBM Deepcut §938-§961.
- Package sub-system requirements (suction scrubber, suction PCV, aftercooler,
  blowdown, recycle, lube oil, packing drains, automated sequences, downstream
  filter/coalescer F-3500-1). Source: DBM Deepcut §963-§969, §1469-§1483.
- Package interface requirements matrix (carried as evidence in this
  deliverable per `_CONTEXT.md` Notes). Source: PACKAGE_REGISTER
  Applicable_Interfaces.

Scope items covered: `SOW-0169`, `SOW-0170`, `SOW-0171`, `SOW-0172`
(`_CONTEXT.md`).

### 1.2 Out of Scope

- Package vendor internal engineering deliverables (vendor drawings,
  calculations, factory QA records) — owned by Package Vendor per
  PACKAGE_REGISTER Scope_Split.
- Detailed cryogenic recovery, product treating, product storage, plant-wide
  utility design — addressed only at interface boundaries (DBM Deepcut §868).
- Sweet gas purge supply (manual sweet gas purge is explicitly external; DBM
  Deepcut §967).
- Acid gas injection compression, inlet/sales multi-service compression — separate packages.

## 2. Requirements

### 2.1 Identification Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-049-02-ID-1 | The datasheet shall identify the package as `PKG-049 / 26020-01-PT-12-004 — Sales Gas Booster Compressor`, Workbook row 80. | PACKAGE_REGISTER.csv |
| REQ-049-02-ID-2 | The datasheet shall declare ownership split: Package Vendor owns package engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility-level integration and interfaces. | PACKAGE_REGISTER.csv (Scope_Split) |

### 2.2 Configuration Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-049-02-CFG-1 | The package shall consist of one (1) x 100% sweet sales gas booster compressor with no installed spare. | DBM Deepcut §942, §877, §951 |
| REQ-049-02-CFG-2 | The compressor shall be a separable reciprocating compressor, single stage. | DBM Deepcut §934, §943 |
| REQ-049-02-CFG-3 | The compressor frame shall be Ariel KBK/4, with all cylinders dedicated to the single booster stage. ASSUMPTION: equivalent or vendor-proposed alternative is permitted only with EPC approval. | DBM Deepcut §936 |
| REQ-049-02-CFG-4 | A larger high-efficiency cylinder on a two-throw design shall be evaluated during detailed engineering due to the low compression ratio; final cylinder selection is `TBD`. | DBM Deepcut §936 |
| REQ-049-02-CFG-5 | Clearance pocket configuration (automated continuously variable, automated fixed-volume, or manual variable volume) shall be evaluated during detailed engineering; selection is `TBD`. | DBM Deepcut §930, §969 |

### 2.3 Driver Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-049-02-DRV-1 | The driver shall be an electric induction motor rated 6,700 hp, 4,000 V, 3-phase, 60 Hz. | DBM Deepcut §936 |
| REQ-049-02-DRV-2 | The motor shall be tested and labeled per NEMA MG 1. | DBM Deepcut §936 |
| REQ-049-02-DRV-3 | Insulation class shall be F; temperature-rise class shall be B. | DBM Deepcut §936 |
| REQ-049-02-DRV-4 | Cooling fans shall be non-sparking and bidirectional. | DBM Deepcut §936 |
| REQ-049-02-DRV-5 | The motor enclosure shall be TEFC or WPII. | DBM Deepcut §936 |
| REQ-049-02-DRV-6 | Starting basis shall be DOL with soft-start; no driver speed turndown is required (mapped basis). | DBM Deepcut §936 |

### 2.4 Process Design Requirements

| ID | Requirement | Value | Source |
|---|---|---|---|
| REQ-049-02-PROC-1 | Suction pressure | 6,137 kPag (890 psig); low suction pressure `TBD` | DBM Deepcut §944 |
| REQ-049-02-PROC-2 | Suction temperature | 43 deg C service basis (35 deg C winter / 43.3 deg C summer) | DBM Deepcut §945 |
| REQ-049-02-PROC-3 | Discharge pressure | 12,866 kPag (1,866 psig); normal discharge pressure TBC | DBM Deepcut §946 |
| REQ-049-02-PROC-4 | Capacity | 3,962 e3m3/d (140 MMSCFD) in both J-T and expander modes; high/excess capacity TBC | DBM Deepcut §934, §947 |
| REQ-049-02-PROC-5 | Minimum MAWP (suction and discharge) | 13,100 kPag (1,900 psig) | DBM Deepcut §948 |
| REQ-049-02-PROC-6 | Suction design temperature | 149 deg F (300 deg F alternate) | DBM Deepcut §949 |
| REQ-049-02-PROC-7 | Discharge design temperature | 177 deg F (350 deg F alternate) | DBM Deepcut §949 |
| REQ-049-02-PROC-8 | Inlet water content | <0.1 ppmv (upstream molecular sieve dehydration) | DBM Deepcut §950 |
| REQ-049-02-PROC-9 | Design compositions | Per Datasheet "Inlet Gas Composition" table (expander and J-T modes) | DBM Deepcut §955-§961 |

### 2.5 Sub-system Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-049-02-SUB-1 | A two-phase suction scrubber shall be provided upstream of compression; final need to be evaluated in detailed engineering due to very low inlet-gas dewpoint. Sizing per API-11P or vendor vane-style demister sizing; horizontal double-hook vane-style demister internals are acceptable; assumed inlet liquid density 0.61 SG. | DBM Deepcut §963 |
| REQ-049-02-SUB-2 | The suction pressure control valve shall be a full-port automated ball valve with upstream manual isolation, allow 5 psid differential pressure, and fail closed. | DBM Deepcut §963 |
| REQ-049-02-SUB-3 | The aftercooler shall be horizontal-airflow, single-fan, on-module; winter outlet 35.0 deg C; summer outlet 43.3 deg C; simulated first-stage gas-section dP 69.0 kPad; design dP `TBC`; automated pneumatic louver control required. | DBM Deepcut §965 |
| REQ-049-02-SUB-4 | The package shall include a blowdown valve that fails closed; designed to start from equalization pressure; equalization pressure shall not exceed system MAWP. | DBM Deepcut §967 |
| REQ-049-02-SUB-5 | The recycle valve shall be sized for 100% capacity at minimum pipeline operating pressure with high suction pressure (initial start-up case); fail position fail-closed (TBC in detailed engineering); a single full-port manual isolation valve shall be installed on the outlet of the recycle valve. | DBM Deepcut §969 |
| REQ-049-02-SUB-6 | If an additional automated bypass valve is required, the alternate option shall be to depressure back into the sales compressor discharge header. | DBM Deepcut §967 |
| REQ-049-02-SUB-7 | An electric circulating lube oil heater shall be included. | DBM Deepcut §967 |
| REQ-049-02-SUB-8 | Packing drains and vents shall be collected to a common seal pot; seal-pot vapour shall be routed to the VRU suction header; liquids shall be trucked out locally; distance-piece sweep purge shall be provided to prevent backflow from the VRU header. | DBM Deepcut §967 |
| REQ-049-02-SUB-9 | Manual sweet gas purge is NOT included in package scope and is an external-responsibility item. | DBM Deepcut §967 |
| REQ-049-02-SUB-10 | Isolation, purging, pressurization, depressurization, lubrication, start-up, loading, unloading, cooldown, and shutdown sequences shall be automated. | DBM Deepcut §967 |
| REQ-049-02-SUB-11 | The downstream Sales Gas Booster Filter/Coalescer F-3500-1 shall be sized as 1 x 100% with manual bypass and isolation for filter change-out, and clean dP <2 psid; design inlet flow remains `TBD` pending conflict resolution (see Guidance Conflict Table CONF-001). | DBM Deepcut §1471, §1474-§1483, §1808 |

### 2.6 Interface Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-049-02-IF-1 | The datasheet shall include an interface requirements matrix covering, at minimum, the applicable interface types listed in PACKAGE_REGISTER.csv: Process Piping, Utility Piping, Relief/Flare/Vent, Drain/Containment, Electrical Power, EHT, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Building HVAC/Services, Fire & Gas/Safety Systems, Maintenance Access, Structural/Foundations/Supports. | PACKAGE_REGISTER.csv (Applicable_Interfaces) |
| REQ-049-02-IF-2 | The matrix shall identify, for each interface, the EPC scope, the Package Vendor scope, and the battery-limit reference point. Detailed values are `TBD` pending access to Word source `26020-Package_Requirements.docx` heading 4 and Excel source `26020-Packages_Interfaces_4_export.xlsx`. | `_REFERENCES.md`; PACKAGE_REGISTER Source_Refs |
| REQ-049-02-IF-3 | Process piping interfaces shall reflect: suction tie-in from HP Sales Header 2 (~95 MMSCFD nominal); discharge through aftercooler to F-3500-1 then to sales gas splitter for TCPL delivery; bypass routing downstream of F-3500-1 toward the TC sales gas splitter meter on booster shutdown. | DBM Deepcut §1435-§1436, §1471 |

## 3. Standards

| Standard | Use | Locality |
|---|---|---|
| NEMA MG 1 | Motor testing/labeling | Cited in DBM Deepcut §936; standard text not locally accessible (`location TBD`) |
| API-11P (or vendor vane-style demister sizing) | Suction scrubber demister sizing | Cited in DBM Deepcut §963; standard text not locally accessible (`location TBD`) |
| Project Design Basis Memorandum (Deepcut) | Governing process design basis | `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Additional governing project standards (HAZOP/SIL, piping classes, electrical area classification, structural codes) | `TBD` — not enumerated in accessible source slices | `location TBD` |

## 4. Verification

| Requirement Group | Verification Approach |
|---|---|
| Identification (REQ-049-02-ID-*) | Document review against PACKAGE_REGISTER.csv and `_CONTEXT.md`. |
| Configuration (REQ-049-02-CFG-*) | Vendor proposal compliance review; EPC engineering review at detailed-engineering gate for cylinder and clearance-pocket evaluations. |
| Driver (REQ-049-02-DRV-*) | Motor data sheet review against NEMA MG 1; FAT/witness per project ITP (project ITP `TBD`). |
| Process design (REQ-049-02-PROC-*) | Heat-and-material balance review against DBM Deepcut §938-§961; vendor performance curves; capacity confirmation in J-T and expander modes. |
| Sub-system (REQ-049-02-SUB-*) | P&ID review; cause-and-effect review; SAT for automated sequences; aftercooler performance test (winter and summer outlet temperatures); F-3500-1 dP test. |
| Interface (REQ-049-02-IF-*) | Interface matrix walkdown; tie-in drawing review; integration HAZOP. |

## 5. Documentation

The datasheet, when complete, shall comprise the anticipated artifacts listed
in `_CONTEXT.md` and PACKAGE_REGISTER.csv:

- Package technical datasheet (this deliverable).
- Vendor engineering handoff basis (configuration, driver, process conditions, sub-systems sections of this deliverable).
- Package interface requirements matrix (Section 2.6 of this Specification; values `TBD` pending source access).
- Source-supported equipment and design criteria (this deliverable and the companion Guidance/Procedure).

Anticipated downstream artifacts (Package Vendor responsibility, outside this
deliverable scope): vendor general arrangement, P&IDs, motor data sheet,
cooler data sheet, vessel data sheets, ITP, FAT records.
