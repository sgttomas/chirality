# Specification — Construction Work Package (VRU 4-25)

DeliverableID: `DEL-047-03_construction-work-package`
ParentPackageID: `PKG-047`

## Scope

### In scope
- Define the EPC Integrator's construction execution scope to physically install, inspect, mechanically complete, turn over, and tie in the Vapour Recovery Unit (VRU) packages for the West Doe 04-25 expansion into the surrounding facility systems.
- Cover the construction interfaces explicitly flagged "By others" in the vendor package: shipping compressor packages to site, installation on piles, tie-in piping, electrical connections, and mounting platform and stairs. (SOW-0256)
- Capture pre-commissioning, mechanical-completion, and turnover handover from EPC Integrator construction to commissioning and operations.

### Out of scope
- Vendor package engineering, design, equipment supply, fabrication, and vendor documentation: owned by the Package Vendor per SOW-0253 / OBJ-004.
- VRU process design basis: governed by the 4-25 DBM and DEL-047-02 (Package Datasheet).
- Vendor document turnover content: governed by DEL-047-05.
- EPC review and acceptance of the vendor package: governed by DEL-047-06.

## Requirements

### R1. Service classification and material compatibility
- R1.1 All construction work touching the VRU process envelope SHALL treat the VRU as sour service (H2S 0.3557 mol%, CO2 0.9434 mol%) and apply the NACE designation called out in SOW-0255. **Source:** SOW-0255; 4-25_Deepcut_DBM.md VRU Inlet Composition.
- R1.2 Construction welds, weld procedures, NDE coverage, and PWHT decisions on tie-in piping SHALL comply with the NACE designation referenced in R1.1. Specific NACE document edition: **location TBD** in accessible sources for this deliverable. **ASSUMPTION:** NACE MR0175 / ISO 15156 is the governing standard; confirm via DBM SEC-15 (regulatory/codes/standards) which is referenced but not extracted locally for this deliverable.

### R2. Foundation and setting
- R2.1 VRU compressor packages SHALL be installed on piles as defined by the EPC civil/structural design. **Source:** SOW-0256 ("installation on piles").
- R2.2 Pile design parameters (count, diameter, embedment, lateral and uplift capacity) — **TBD**; not present in accessible sources for this deliverable.
- R2.3 Mounting platforms, stairs, and access steel SHALL be supplied and installed by the EPC Integrator. **Source:** SOW-0256 ("Mounting platform and stairs etc." listed under "By others").

### R3. Piping tie-ins
- R3.1 EPC construction SHALL install tie-in piping between the VRU package skid limits and the upstream low-pressure vapour sources and the downstream Stabilizer Overheads Compressor (SOC) first-stage suction. **Source:** SOW-0256; DBM VRU section (lines 1683, 1688).
- R3.2 The VRU discharge tie-in SHALL terminate at the 04-25 SOC first-stage suction header; both 04-25 and 03-25 VRU discharges route to this same header. **Source:** DBM VRU section.
- R3.3 The primary seal vent tie-in SHALL terminate at the LP flare header. **Source:** DBM VRU table (Primary seal vent: LP flare); SOW-0255.
- R3.4 Tie-in line classes, insulation, heat tracing, and slope requirements — **TBD** until P&ID and line list are issued by the EPC mechanical/piping discipline package.

### R4. Electrical connections
- R4.1 EPC construction SHALL terminate motor and cooler-motor power to VFD-ready 600 V, 3-phase, 60 Hz drives per SOW-0256.
  - **CONFLICT (carry forward):** DBM VRU table specifies motor voltage 4,000 V, 3-phase, and motor power TBD with a 200 hp / 300 hp conflict; SOW-0256 specifies 600 V, 200 HP. Resolution required before electrical detail engineering — see Guidance Conflict Table CFL-1.
- R4.2 Grounding, bonding, area-classification compliance, and cable routing SHALL follow the EPC electrical package basis (DBM SEC-12). Specific values: **location TBD** for this deliverable.

### R5. Building and HVAC
- R5.1 Each VRU is to be installed within a building with associated utilities. **Source:** DBM VRU Configuration paragraph.
  - **CONFLICT (carry forward):** SOW-0254 states "both housed in one building"; DBM states "Each VRU is installed in an individual building with associated utilities." Construction cannot proceed on building scope until resolved — see Guidance Conflict Table CFL-2.
- R5.2 Building ventilation, gas detection, and heat tracing requirements — **TBD** for this deliverable; governed by HVAC, fire-and-gas, and EHT packages.

### R6. Mechanical completion and turnover
- R6.1 Construction SHALL produce a turnover checklist demonstrating, at a minimum:
  - Foundation and anchor-bolt acceptance.
  - Skid setting and levelling within vendor tolerance (vendor tolerance: **TBD**, from DEL-047-04 vendor-engineered equipment package).
  - Bolt-up, alignment, and torque records for inlet, discharge, vent, drain, and seal-supply tie-ins.
  - Hydrostatic/pneumatic test records per applicable line class.
  - Electrical termination, megger, and continuity records.
  - Loop checks against package control narrative supplied by the vendor (DEL-047-05).
  - Pre-commissioning sign-off prior to handover to commissioning.
- R6.2 Construction interface and turnover checklist SHALL be an explicit anticipated artifact per `_CONTEXT.md`.

### R7. Sour-service safety during construction
- R7.1 Pre-commissioning inerting, purging, and first-fill of sour-service equipment SHALL follow facility sour-service entry/work procedures. Procedure references: **location TBD**; governed by DBM SEC-14 (Instrumented Protection) and SEC-15 (Regulatory) — not extracted locally for this deliverable.

## Standards

| Standard | Use | Status |
|---|---|---|
| NACE MR0175 / ISO 15156 (ASSUMPTION) | Sour-service material compliance | Cited as "NACE designation applies" in SOW-0255; specific document edition: **location TBD** |
| API 6 series / ASME B31.3 (ASSUMPTION) | Tie-in piping construction and pressure testing | **TBD** — not in accessible sources for this deliverable |
| CSA Z662 (ASSUMPTION; Canadian sour-service) | Tie-in piping where regulated | **TBD** — not in accessible sources for this deliverable |
| AESO/BCER provincial codes | Site/electrical compliance (facility in BC per DBM SEC-01) | **TBD** — not extracted locally |
| Vendor installation and field-service manual (DEL-047-05) | Vendor-prescribed installation and torque | Required prerequisite |

## Verification

| Requirement | Verification approach |
|---|---|
| R1 (Sour service / NACE) | Material certificates and weld map review; NDE per accepted procedure |
| R2 (Foundations) | Pile load test / driving records; survey acceptance |
| R3 (Tie-in piping) | Line walkdowns; pressure test records; isometric markup |
| R4 (Electrical) | Megger, continuity, motor rotation bumps, VFD parameter check |
| R5 (Building/HVAC) | Building functional test; gas detection commissioning |
| R6 (Mechanical completion) | Signed turnover checklist; punch-list close-out evidence |
| R7 (Sour-service work) | Permits, gas-test logs, purge/inert records |

## Documentation

The construction work package SHALL produce, at minimum, the anticipated artifacts identified in `_CONTEXT.md`:

- Construction work package narrative (this document set, finalized).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.

Plus supporting records implied by the requirements above (pile records, weld map and NDE reports, hydrotest packages, electrical commissioning records, punch list).
