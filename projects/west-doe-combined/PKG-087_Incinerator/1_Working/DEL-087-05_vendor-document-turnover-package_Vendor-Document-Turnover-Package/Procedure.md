# Procedure — DEL-087-05 Vendor Document Turnover Package

## Purpose

Operational steps to produce, control, review, and turn over the vendor document set for the Incinerator package (26020-Package_Requirements.docx heading 40), culminating in EPC Integrator acceptance.

## Prerequisites

| Item | Notes |
|---|---|
| DEL-087-01 Scope of Work (EPC) | Available and current — defines vendor scope contractually. |
| DEL-087-02 Package Datasheet (EPC) | Available and current — defines vendor design inputs and interface matrix, including supplemental fuel-gas rate, incinerator service split (per owner ruling), and KO drum design conditions. |
| DEL-087-03 Construction Work Package (EPC) | Available — defines installation/tie-in interfaces vendor docs must support. |
| DEL-087-04 Vendor Engineered Equipment Package | In progress — vendor must be under contract and engineering active. |
| Source package specification | 26020-Package_Requirements.docx heading 40 accessible to vendor and EPC reviewers (file present in `_Sources`; heading-40 slice not parsed this run — see Guidance Conflict Table C-04). |
| Vendor RFQ document | Vendor RFQ for Incinerator package — TBD; required for any RFQ-specific requirements not covered by package source. |
| Document control system | Vendor and EPC Integrator each operate an electronic document management system (TBD which platforms). |
| Owner emissions/permit basis | PRO-024 owner-side framework available before vendor freezes emissions basis (TBD — owner-driven). |

## Steps

### 1. Establish document control basis
1.1 Vendor issues DOC-008 Vendor Document Control Procedure for EPC review.
1.2 Vendor issues initial PRQ-009 Vendor Document Index listing every document required by Specification R-01..R-18 plus any additional RFQ-imposed items, plus any heading-40-specific items identified once that source slice is parsed (Conflict Table C-04).
1.3 EPC Integrator reviews DOC-008 and PRQ-009; aligns on status codes, transmittal numbering, revision conventions, and expected submittal schedule (target dates).
1.4 PRQ-009 becomes the live register; vendor updates it with every submittal/revision.

### 2. Engineering submittal cycle (iterative)
2.1 Vendor produces engineering documents per the index (MEC-001..MEC-025, MEC-011..MEC-013 fired-equipment, ELE-002..ELE-030 including BMS, PRO-008..PRO-024 including emissions, PIP-003..PIP-028, CIV-014, REG-022, ICA-xxx BMS/SIF, etc.).
2.2 Vendor issues each submittal under a transmittal with explicit revision and status code.
2.3 EPC Integrator routes each submittal to the responsible discipline reviewer; BMS/SIF documentation receives an independent functional-safety review.
2.4 Reviewer returns disposition: approved / approved-with-comments / not-approved / for-information.
2.5 Vendor re-issues as required; update PRQ-009 to reflect current status.
2.6 Verify discipline-level consistency at each revision (e.g., supplemental fuel-gas rate consistent across MEC-013, ELE-002 Load List indirectly via auxiliary loads, PRO-011 Utility Summary, and PRO-024 emissions calculation). Raise Conflict Table entries when disagreements appear.
2.7 Confirm GA/installation drawings (MEC-016, MEC-017) support EPC verification of OGAOM Sec. 9.6.15 spacing constraints (see Guidance "Considerations"); reject drawings that obstruct compliance verification.

### 3. Quality and inspection execution
3.1 Vendor issues QLT-006 Supplier Quality Plan and QLT-003 Inspection and Test Plan for EPC approval before manufacturing. ITP must include witness/hold points for the KO drum pressure test, burner assembly, BMS factory testing, and any refractory installation.
3.2 Witness and hold points executed per the approved ITP; EPC Integrator (or its inspection authority) witnesses as required.
3.3 Material Test Reports / Certificates (QLT-013) collected for pressure-retaining components (KO drum) and for high-temperature components (burner internals, stack liner if any).
3.4 Non-conformance reports (NCRs) raised and dispositioned per QLT-006.

### 4. Factory Acceptance Test
4.1 Vendor issues MEC-021 FAT / Performance Test Procedure and MEC-013 Fired Equipment Performance / Emissions Test Procedure for EPC approval prior to FAT.
4.2 FAT executed against the approved procedure to the extent representative-feed combustion can be performed in the shop; EPC Integrator attends per RFQ. Where shop emissions testing is not representative, the test plan defers emissions verification to site SAT (Conflict Table / Guidance trade-off).
4.3 Vendor issues MEC-022 FAT / Performance Test Report and addresses punch-list items.
4.4 Electrical/BMS FAT (ELE-029) executed analogously for ignition, burner management, and safety instrumented functions; functional-safety reviewer signs the BMS section.

### 5. Pre-shipment release
5.1 All open NCRs closed or accepted with concession.
5.2 Manufacturing Record Book (QLT-021) assembled and reviewed.
5.3 Inspection Release Certificate (QLT-020) signed; package released for shipment.
5.4 PRQ-013 Logistics / Shipping Plan executed.
5.5 PRQ-015 SPIR submitted (commissioning and operating spares — pilot/igniter, refractory, burner tips, thermocouples as typical critical spares).
5.6 REG-022 Pressure Equipment Registration Package for the KO drum submitted to applicable jurisdictional authority (jurisdiction TBD — see Guidance Conflict Table C-02).

### 6. Site and commissioning records
6.1 Vendor supports installation and commissioning per IOM (MEC-025).
6.2 Electrical Test Records / Energization Package (ELE-030) completed at site, including BMS site validation and SIF proof testing.
6.3 Site emissions verification (per MEC-013 / PRO-024) performed under representative feed; report issued.
6.4 Piping As-Built Drawings (PIP-028) updated as installed, including incinerator-header tie-ins from the spent-caustic and DSO tank vent systems.
6.5 Punch-list items closed.

### 7. Final turnover
7.1 Vendor assembles PRQ-016 Vendor Data Book / Final Supplier Documentation and MEC-023 Mechanical Final Documentation Vendor Data Book using accepted final-revision documents from PRQ-009.
7.2 Vendor transmits Final VDB to EPC Integrator.
7.3 EPC Integrator performs completeness check against PRQ-009 and the source-required document list (once heading 40 is parsed and reconciled per Conflict Table C-04).
7.4 EPC Integrator records acceptance in DEL-087-06 (Vendor Document Review Log; Package Acceptance Checklist).
7.5 PRQ-009 closed at final revision; turnover record set frozen.

## Verification

| Check | Method | Acceptance |
|---|---|---|
| PRQ-009 completeness | Compare index entries against the Specification R-01..R-18 enumerated documents and against any additional RFQ items and heading-40 items | Every required document present, with current revision and status |
| Document status integrity | Random audit of 5 documents per submittal cycle | Status codes correct; transmittals reconcile |
| ITP execution | Inspection records vs ITP | Every hold/witness point signed |
| FAT acceptance | MEC-022, MEC-013 review | FAT report signed; punch list captured |
| BMS / SIF functional safety | ELE-029 + independent functional-safety review | Independent reviewer signature on file |
| Pre-shipment release | QLT-020 IRC signed | All NCRs closed or concessioned |
| Pressure equipment registration | REG-022 jurisdictional acceptance letter | Acceptance letter on file (jurisdiction per C-02 ruling) |
| Emissions basis reconciliation | PRO-024 vs MEC-013 vs site emissions report | Values consistent; deviations explained |
| Spacing compliance support | GA/installation drawings reviewed against OGAOM Sec. 9.6.15 | EPC verifies compliance using vendor drawings |
| Final VDB completeness | Completeness audit by EPC | 100% of PRQ-009 final-revision items present in VDB |
| EPC acceptance | DEL-087-06 acceptance log entry | Signed acceptance |

## Records

- PRQ-009 Vendor Document Index (final revision)
- All transmittals (incoming/outgoing)
- All vendor engineering submittals at final accepted revision
- Quality records: QLT-006, QLT-003, QLT-013, QLT-020, QLT-021
- FAT/performance records: MEC-021, MEC-022, MEC-013, ELE-029 (with independent SIF review)
- Site/commissioning records: ELE-030, PIP-028, site emissions verification report
- Spares: PRQ-015 (SPIR)
- Logistics: PRQ-013
- REG-022 Pressure Equipment Registration Package and jurisdictional acknowledgment
- PRO-024 Emissions Compliance Calculation / Permit Package (vendor engineering basis portion)
- Final VDBs: PRQ-016, MEC-023, plus electrical/controls volume (ASSUMPTION pending heading-40 confirmation)
- EPC acceptance log entry in DEL-087-06
- Conflict Table dispositions (from Guidance.md) — captured in `_MEMORY.md` if rulings are made (`_MEMORY.md` to be created when rulings are received)
