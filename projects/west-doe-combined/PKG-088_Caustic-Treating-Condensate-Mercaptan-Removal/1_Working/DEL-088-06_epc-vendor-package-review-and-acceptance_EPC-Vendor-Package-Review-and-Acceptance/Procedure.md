# Procedure — DEL-088-06 EPC Vendor Package Review and Acceptance

## Purpose

Operational steps the EPC Integrator follows to produce the DEL-088-06 acceptance deliverable: vendor document review log, package acceptance checklist, test/inspection evidence, and turnover evidence.

## Prerequisites

- DEL-088-01 (EPC Scope of Work) issued and accepted.
- DEL-088-02 (Package Datasheet) issued and accepted.
- DEL-088-03 (Construction Work Package) issued and accepted.
- DEL-088-04 (Vendor Engineered Equipment Package) submitted for review.
- DEL-088-05 (Vendor Document Turnover Package) submitted with at least the vendor document register populated.
- Access to the 03-25 DBM (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) and the package requirements source (26020-Package_Requirements.docx package heading 41 — location TBD).
- HAZOP outcome available where required (caustic drain pressure segregation). [Source: 3-25_Comp_and_Liquids_DBM.md §Drains]

## Steps

### Step 1 — Establish acceptance baseline
1. Lock the accepted versions of DEL-088-01, DEL-088-02, DEL-088-03 as the acceptance baseline.
2. Record baseline document IDs and revisions in the package acceptance checklist.

### Step 2 — Receive vendor submissions
1. Receive the DEL-088-04 vendor engineering package and DEL-088-05 vendor document turnover register.
2. Confirm vendor document register completeness against the source-required vendor documentation list. [Source: DELIVERABLE_REGISTER.csv row DEL-088-05]
3. Open the vendor document review log.

### Step 3 — Map vendor documents to requirements
1. Build the trace matrix that maps each requirement in Specification.md (R1-R11) to one or more vendor documents (or witness records).
2. Flag any requirement with no mapped evidence as an open item.

### Step 4 — Technology and capacity conformance review (R2-R5, R8)
1. Verify vendor PFD and process datasheet show non-regenerative caustic mercaptan treating (Merichem or equivalent) at 20,000 bbl/d C5+ capacity with no caustic regeneration. [Source: 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating]
2. Verify vendor process guarantees address DSO entrainment (30 ppmw S expected, 50 ppmw S design TBC) and extractable compounds (H2S, CO2, methyl/ethyl/propyl/butyl mercaptans).
3. Verify caustic solution basis (50 wt% NaOH/H2O, SG 1.75 TBC).
4. Verify package component completeness: caustic C5+ contactor, pre-heater, caustic outlet filter, water wash, DSO/spent/fresh-caustic/fresh-water tanks, incinerator overhead/dilution/enrichment-gas interfaces.

### Step 5 — Material and storage restrictions review (R6)
1. Verify aluminum is not used in the caustic building.
2. Verify fresh and spent caustic tanks are atmospheric 32 oz with LP fuel-gas blanket, heating, and insulation.
3. Verify spent caustic tank vents through a flame arrestor to the incinerator header and supports truck-out.
4. Verify fresh caustic is not connected to the VRU.
5. Verify tank material/coating selection has supporting compatibility evidence (or record as TBC and assign closure owner).

### Step 6 — Interface and drain review (R7)
1. Verify caustic drain minimum 300# ANSI rating and termination flange at spent-caustic tank.
2. Verify caustic drain maximum temperature handling (121 deg C / 250 deg F TBC).
3. Verify heat-tracing provisions and material selection considerations are addressed.
4. Confirm HAZOP outcome on pressure segregation has been incorporated, or surface the dependency.

### Step 7 — Turnover documentation conformance (R9)
1. Reconcile DEL-088-05 turnover artifacts against the vendor document register.
2. Confirm submittals, source-required vendor documentation, and turnover records are present and consistent with DEL-088-02.

### Step 8 — Construction and tie-in conformance (R10)
1. Confirm vendor scope statements are consistent with DEL-088-03 installation, tie-in, inspection, and turnover requirements.
2. Confirm the construction interface and turnover checklist items are coverable by vendor-supplied evidence.

### Step 9 — FAT and inspection evidence review
1. Review vendor FAT report and inspection records.
2. Where FAT evidence is incomplete, decide between re-FAT and integration witness at site (per Guidance.md trade-off).
3. Record disposition.

### Step 10 — Issue acceptance decision (R11)
1. Produce the documented acceptance decision: status (accept / accept-with-conditions / reject), open non-conformances, conditions and owners, handoff-readiness call.
2. Route for EPC Integrator authorized signature.
3. Issue to project records and notify Package Vendor.

### Step 11 — Closeout
1. Track conditional-acceptance items to closure under their assigned owners and deadlines.
2. Update the vendor document review log and package acceptance checklist as items close.
3. Archive the acceptance decision record and supporting evidence pack.

## Verification

- Trace matrix has 100% coverage of R1-R11 with mapped vendor documents or witness records (or explicit TBD with owner).
- Acceptance decision record is signed by the EPC Integrator and references the locked baseline document revisions.
- All conditional-acceptance items have an owner and a closure deadline.
- Open TBC items from the source basis are either closed by vendor evidence or carried forward with an explicit owner.

## Records

- Vendor document review log
- Package acceptance checklist
- FAT and inspection evidence pack
- Trace matrix (Specification.md R1-R11 → vendor documents)
- Acceptance decision record (signed)
- Punch list and conditional-acceptance closure log
- Turnover evidence pack (consolidated for facility turnover)
