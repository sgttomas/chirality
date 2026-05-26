# Procedure — DEL-060-04 Vendor Engineered Equipment Package

This procedure describes the steps to **produce** the Vendor Engineered Equipment Package deliverable (the vendor production unit for PKG-060). It assumes that DEL-060-01 (Scope of Work) and DEL-060-02 (Package Datasheet) have been issued by the EPC Integrator, since those are the anchoring inputs (`_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 477).

## Prerequisites

- EPC Scope of Work (DEL-060-01) issued.
- EPC Package Datasheet (DEL-060-02) issued with package equipment list, design conditions, and interface requirements.
- Access to applicable DBM source slice: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (sections SEC-09 Product Pumps, SEC-10 Package Line-Items, SEC-11 Civil/Buildings).
- Vendor agreement and commercial scope alignment with the EPC Integrator.
- Open `_STATUS.md` state is `OPEN` or `INITIALIZED` at start of vendor execution.
- Upstream dependencies: none declared in `_DEPENDENCIES.md`; treat DEL-060-01 and DEL-060-02 as logical prerequisites (ASSUMPTION).

## Steps

### Step 1 — Receive and validate EPC inputs
1.1. Receive DEL-060-01 (Scope of Work) and DEL-060-02 (Package Datasheet) from the EPC Integrator.
1.2. Validate that the package datasheet covers all SOW items SOW-0189 through SOW-0192.
1.3. Log any TBD or conflicting items against the DBM source slice. Record findings in vendor design-basis register.

### Step 2 — Develop vendor design basis
2.1. Establish vendor design basis document covering pump services, sparing philosophy, materials, motor sizing, controls, and module envelope, traceable to DBM SEC-09 (lines 1667-1679) and SEC-10 (lines 2618-2622).
2.2. Confirm pump configurations per Specification REQ-2 through REQ-10.
2.3. Resolve or document the WATER TRANSFER PUMP quantity (Guidance Conflict CONF-01).
2.4. Document caustic-compatibility material plan (Specification REQ-13).
2.5. Document -40 deg C startup motor sizing (Specification REQ-5).

### Step 3 — Produce vendor datasheets and design documents
3.1. Produce pump datasheets per tag (P-9210-1, P-9220-1, P-9290-1, P-9293-1, P-9231-1, P-9232-1, P-5317-1, P-5318-1, P-6760-1, P-6765-1) plus product recycle and condensate skim pumps.
3.2. Produce module general arrangement, P&IDs, electrical one-line, instrumentation index, and HVAC/ventilation arrangement.
3.3. Produce vendor package design basis document.
3.4. Produce calculation packs: hydraulic, NPSHA/NPSHR, motor sizing, line sizing within module battery limits.

### Step 4 — Procure long-lead items
4.1. Issue purchase orders for pumps, motors, vessels (if any), and the module structural envelope.
4.2. Confirm shop fabrication slot for Module 920-1 (DBM line 2817).

### Step 5 — Fabricate, assemble, and test
5.1. Shop-build the module to drawings.
5.2. Apply coatings/finishes per Specification REQ-12 (Safety Green trim, galvanized walls, white interior).
5.3. Conduct FAT including pump performance, NPSHR verification, motor cold-start verification (proxy if -40 deg C bath not feasible — note as ASSUMPTION), and instrumentation/control loop checks.
5.4. Conduct mechanical run tests per applicable API standards (REQ-14 verification list).

### Step 6 — Package and ship
6.1. Package module for transport to LSD 04-25-80-15W6 (DBM line 17).
6.2. Provide shipping documentation, lifting plans, and offload instructions.
6.3. Transfer module and accompanying documentation to site.

### Step 7 — Support EPC integration review
7.1. Submit vendor documentation to DEL-060-05 Vendor Document Turnover Package per the EPC document register.
7.2. Support DEL-060-06 EPC Vendor Package Review and Acceptance.
7.3. Resolve and close any review comments via documented change control.

## Verification

| Item | Verification |
|---|---|
| Pump performance | FAT performance curves matching vendor datasheet within tolerance |
| NPSHR | NPSHR test report, <= 0.75 m at design flow (Spec REQ-4) |
| Motor sizing | Independent motor calculation against -40 deg C density basis (Spec REQ-5) |
| Minimum-flow control | Functional loop test of minimum-flow valve (Spec REQ-6) |
| Materials (caustic) | Material test reports; visual inspection of insulation cladding and tank-interfacing piping (Spec REQ-13) |
| Module envelope | Visual inspection vs coating and finish requirements (Spec REQ-12) |
| Document completeness | Cross-check against vendor document register (DEL-060-05 receiving check) |
| EPC acceptance | DEL-060-06 acceptance log entry indicating "Accepted" or "Accepted with conditions" |

## Records

The following records shall result from the procedure:
- Vendor design basis document.
- Pump datasheets and performance curves (per tag).
- Motor sizing calculations.
- NPSHR test reports.
- FAT inspection records.
- Material test reports and weld procedure qualifications.
- Module GA drawings and P&IDs at issued-for-construction status.
- Shipping and offload documentation.
- Vendor document index (handed to DEL-060-05).
- Open punch-list and resolution log feeding DEL-060-06.

Storage location for records: vendor document repository, mirrored to the EPC document control system. Specific location TBD by Package Datasheet (DEL-060-02) and EPC document control plan.
