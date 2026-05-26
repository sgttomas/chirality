# Specification — DEL-089-06 EPC Vendor Package Review and Acceptance (PKG-089 Pig Receivers, Inlet 3-25)

## Scope

This specification governs the EPC Integrator's review and acceptance of the vendor-supplied pig-receiver package for the 03-25 facility inlet pipeline interface, against the EPC Scope of Work, Package Datasheet, and Construction Work Package. It covers:

- Vendor document review and disposition
- Integration acceptance against site interfaces (purge, flare vent, ESDV, structural skid tie-in)
- Test and inspection evidence verification
- Turnover/handoff readiness

Excluded: Inlet separator packages (PKG separate), inlet pipeline construction upstream of the lease-boundary first flange (Doe field pipeline contractor scope per DBM 3-25 SEC-04), and downstream sales/export systems.

Covers SOW items: `SOW-0157`, `SOW-0158`, `SOW-0159`, `SOW-0160` (per `_CONTEXT.md`; SOW slice not locally accessible — `location TBD`).

## Requirements

### R-1 Vendor Document Review

- R-1.1: EPC Integrator shall maintain a vendor document review log covering all vendor-issued documents for the pig-receiver package (drawings, datasheets, calculations, test plans, ITP, MTRs, certifications). Source: `_CONTEXT.md` anticipated artifacts.
- R-1.2: Each vendor document shall be dispositioned (Approved / Approved with Comments / Revise and Resubmit / Rejected) with a documented review record. **ASSUMPTION**: standard EPC review classes; specific class names per project QA plan — `location TBD`.

### R-2 Package Configuration Acceptance

- R-2.1: The accepted package shall implement a **single combined three-phase pig receiver** mounted on a **structural steel, non-enclosed skid**. Source: DBM 3-25 SEC-04 (Inlet Pipeline Interface and Pigging).
- R-2.2: The package shall include **sweet-gas purge** and **HP flare vent** provisions. Source: DBM 3-25 SEC-04.
- R-2.3: The inlet ESDV associated with the receiver shall be **full-port, piggable, and equipped with position transmitters**. Source: DBM 3-25 SEC-04.
- R-2.4: Receiver size shall be confirmed during detailed engineering. Source DBM value: TBD — carry as **TBD** until detailed design confirms.
- R-2.5: Delivery-point ESDV shutdown pressure shall be confirmed. Source DBM value: **TBC**. Inlet separator ESDV shutdown is 635 psig (governing related value). Source: DBM 3-25 SEC-04.

### R-3 Interface and Integration

- R-3.1: The package shall integrate at the **first aboveground flange within the lease boundary**, the defined plant inlet boundary. Source: DBM 3-25 SEC-04.
- R-3.2: Vendor scope shall integrate with the EPC-installed sweet-gas purge header and HP flare header tie-in points. Tie-in flange ratings and locations: **location TBD** (vendor general arrangement to confirm).
- R-3.3: Vendor scope shall integrate with operator pigging/flowback management practices; no additional pigging slug volume is provided beyond separator slug handling. Source: DBM 3-25 "Slug and Flowback Basis".

### R-4 Test and Inspection Evidence

- R-4.1: EPC Integrator shall verify pressure-test records (hydrotest/pneumatic) per applicable code. **ASSUMPTION**: CSA Z662 governs sour-service inlet piping (DBM 3-25 SEC-04 cites CSA Z662 for outlet pipeline; applicability to receiver inlet **location TBD**).
- R-4.2: EPC Integrator shall verify NDE/NDT records (RT/UT/MT/PT as applicable), MTR traceability, weld maps, and PMI where sour service requires. Specific NDE acceptance criteria: `location TBD`.
- R-4.3: ESDV functional test records, including position-transmitter calibration, shall be reviewed and accepted. Source: DBM 3-25 SEC-04 (ESDV requirements).

### R-5 Turnover Readiness

- R-5.1: EPC Integrator shall confirm completeness of the turnover package (as-built drawings, redlines, vendor manuals, spare parts list, lubrication schedule, training records, punch-list closure). **ASSUMPTION**: standard EPC turnover content — specific list `location TBD`.
- R-5.2: Acceptance checklist shall be signed by the EPC Integrator and countersigned by the responsible operating authority. Final approval is reserved for the human authority (K-AUTH-1).

## Standards

| Standard | Applicability | Status |
|---|---|---|
| CSA Z662 | Pipeline/sour-service piping design | Cited in DBM 3-25 SEC-04 for outlet pipeline; receiver-side applicability **ASSUMPTION: likely applicable**; clause-level `location TBD` |
| ASME B31.3 / B31.4 / B31.8 | Process/piping code for skid piping | **ASSUMPTION**, `location TBD` |
| ASME Section VIII Div 1 | Pig-receiver barrel as pressure vessel | **ASSUMPTION**, `location TBD` |
| Project QA/QC plan and EPC SOW | Procedural and review-disposition class definitions | `location TBD` |

## Verification

| Requirement | Verification Method |
|---|---|
| R-1.x | Review of vendor document control log; sample audits of dispositions |
| R-2.1, R-2.2, R-2.3 | Visual inspection vs. accepted GA drawings and P&ID, plus vendor datasheet review against DBM 3-25 SEC-04 |
| R-2.4, R-2.5 | Hold-point sign-off when TBD/TBC values are resolved by detailed design |
| R-3.x | Interface walk-down; tie-in dimensional check; alignment with EPC isometrics |
| R-4.1 | Witness/review of hydrotest packages; certificate review |
| R-4.2 | NDE film/report review; MTR cross-check vs. specified materials |
| R-4.3 | ESDV stroke test; position-transmitter signal verification |
| R-5.1 | Turnover-binder completeness audit |
| R-5.2 | Signature audit on acceptance checklist |

## Documentation

Anticipated artifacts (per `_CONTEXT.md`):

- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence binder
- Turnover evidence package
