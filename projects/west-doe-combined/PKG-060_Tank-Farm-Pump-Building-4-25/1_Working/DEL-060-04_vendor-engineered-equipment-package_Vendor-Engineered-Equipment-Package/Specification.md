# Specification — DEL-060-04 Vendor Engineered Equipment Package

## Scope

### In scope
- Engineering, design, fabrication/supply, and physical delivery of the Tank Farm Pump Building 4-25 vendor package by the Package Vendor.
- Vendor production unit elements: vendor engineered physical equipment package; vendor package design basis and datasheet set (per `_CONTEXT.md` anticipated artifacts).
- Equipment line items associated with PKG-060 in the DBM (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2618-2622): condensate transfer pumps, water transfer pumps, sour water treatment pumps, process water transfer pumps, fresh caustic transfer pumps, and the shop-built 920-1 Tank Farm Pump Module enclosure (line 2817).

### Out of scope
- EPC-Integrator anchor deliverables (Scope of Work DEL-060-01, Package Datasheet DEL-060-02, Construction Work Package DEL-060-03) — inputs, not outputs, of this deliverable.
- Tank-farm storage tanks themselves (separate PKG-060 line items 87-102, owned by separate vendor categories — DBM lines 2623-2628).
- Site civil, foundations, grading, retention pond, and roads (DBM SEC-11 scope).
- Tie-in piping outside the vendor package battery limits and EPC-integrator-led integration work (assigned to DEL-060-03 and DEL-060-06).

## Requirements

REQ-1. The vendor package shall be developed from the EPC Scope of Work (DEL-060-01) and Package Datasheet (DEL-060-02). Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 477.

REQ-2. Condensate transfer pumps (P-9210-1, P-9220-1) shall be configured 2 x 150% with both pumps capable of simultaneous operation, sized for >= 150% of facility design flow of combined condensate product. Source: DBM lines 1673-1675.

REQ-3. The condensate transfer pumping system shall provide 350 kPad (50 psid) differential to the liquids hub at design conditions. Source: DBM line 1673. Operating conditions remain TBC (per source).

REQ-4. Condensate transfer pump design NPSHR at design flow shall not exceed 0.75 m. If the vendor cannot meet this limit, a condensate booster pump plus downstream transfer pump arrangement shall be evaluated. Source: DBM line 1677.

REQ-5. Condensate transfer pump motors shall be sized for inlet stabilizer composition density at -40 deg C startup, including potential initial startup in JT mode. Source: DBM line 1679.

REQ-6. A minimum-flow control valve shall be provided to enable continuous pumping from condensate tanks to the downstream liquids hub. Gap-control pumping provision shall be included to allow settling time in the inlet condensate storage tanks. Source: DBM line 1679.

REQ-7. The product recycle pump shall be 1 x 100%, manually started, sized for 20 m3/h at 80 m TDH (TBC), and shall be capable of recycling condensate from any storage tank to the stabilizer flash feed separator. Located in the Tank Farm Pump Module. Source: DBM line 1671.

REQ-8. The condensate skim pump shall be 1 x 100%, automatically controlled from the produced-water tank interface level controller, sized for 20 m3/h at 80 m TDH (TBC), and shall recycle condensate from the produced-water skim system to the stabilizer flash feed separator. Located in the Tank Farm Pump Module. Source: DBM line 1672.

REQ-9. The fresh caustic transfer pumps (P-6760-1, P-6765-1) shall be radial centrifugal type. The sour water treatment pumps (P-9231-1, P-9232-1) shall be radial centrifugal. The process water transfer pumps (P-5317-1, P-5318-1) shall be radial centrifugal. Source: DBM lines 2620-2622 (Notes column).

REQ-10. Water transfer pumps (P-9290-1, P-9293-1) shall be radial centrifugal. Quantity: ASSUMPTION x2 from detailed table (DBM line 2619); summary indicates x4 (DBM line 2555). Resolution pending — see Conflict Table.

REQ-11. The pump module enclosure shall be shop-fabricated (Module 920-1 Tank Farm Pump Module). Source: DBM line 2817.

REQ-12. Module envelope painting and finishes shall conform to facility colors: Cloverdale # 2593 "Safety Green" flashing/doors/trim, pre-painted galvanized metal walls and roof, bright white QC8783 interior. Source: DBM lines 2824-2826.

REQ-13. Caustic-service materials shall comply with SEC-09 material rules: no aluminum in caustic exposure; insulation cladding and straps in caustic-exposure areas shall be stainless steel; caustic storage interfacing piping/tanks shall use polymer or other caustic-compatible materials. Source: DBM line 1566.

REQ-14. Vendor scope shall integrate with declared upstream/downstream interfaces of PKG-060 (storage tanks, VRU suction header, liquids hub transfer line, stabilizer flash feed return). Specific interface points: TBD pending Package Datasheet (DEL-060-02) issuance.

REQ-15. The vendor shall produce the vendor package design basis and datasheet set as the engineering artifact accompanying the physical equipment package. Source: `_CONTEXT.md` anticipated artifacts.

## Standards

| Standard / Code | Applicability | Locality |
|---|---|---|
| API 610 | Pump design (general centrifugal pumps; multi-stage horizontal) — ASSUMPTION: applied to condensate transfer pumps based on DBM precedent for NGL Booster pumps using "API 610, multi-stage can" (DBM line 2609). | location TBD |
| API 650 | Tank construction (interfacing tank classification used in DBM SEC-10 rows 87-102) | DBM lines 2623-2628 (referenced as classifier) |
| API 2000 | Tank blanket gas and vent rates (referenced in DBM line 1663) | location TBD |
| API 2510 | Pressurized LPG storage spacing | DBM line 258 (referenced for site spacing) |
| Facility design temperature basis | -40 deg C startup minimum | DBM line 1679 |

Additional code applicability remains TBD pending Package Datasheet (DEL-060-02) and Vendor design basis development.

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-2, REQ-3, REQ-4 | Vendor pump performance curves and NPSHR test report; pump test per API 610 acceptance criteria (ASSUMPTION) |
| REQ-5 | Motor sizing calculation reviewed against -40 deg C density basis |
| REQ-6 | P&ID review confirming minimum-flow valve and gap-control logic |
| REQ-7, REQ-8 | Pump curve, controls description, and FAT functional test |
| REQ-9, REQ-10 | Vendor data sheets and pump type confirmation |
| REQ-11, REQ-12 | Module FAT inspection; coating/paint inspection report |
| REQ-13 | Material test reports; insulation/cladding inspection |
| REQ-14, REQ-15 | EPC Integrator integration review (DEL-060-06) and Vendor Document Turnover (DEL-060-05) acceptance |

## Documentation

The vendor package shall deliver, at minimum:
- Vendor engineered physical equipment package (the supplied module). Source: `_CONTEXT.md`.
- Vendor package design basis and datasheet set. Source: `_CONTEXT.md`.
- Pump datasheets (per tag), pump curves, NPSHR data, motor data sheets.
- Module general arrangement drawings, P&IDs, electrical one-line, instrumentation index.
- Material certifications and weld procedures.
- FAT reports and inspection records.
- Operations and maintenance manuals.

Detailed vendor document register: TBD by DEL-060-05 Vendor Document Turnover Package.
