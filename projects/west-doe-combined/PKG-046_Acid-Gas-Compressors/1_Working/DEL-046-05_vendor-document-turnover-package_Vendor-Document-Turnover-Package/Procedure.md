# Procedure: DEL-046-05 — Vendor Document Turnover Package (PKG-046 Acid Gas Compressors)

## Purpose

Define the operational steps the Package Vendor (with EPC Integrator interface/integration review) follows to assemble, transmit, and close out the Vendor Document Turnover Package for PKG-046 Acid Gas Compressors. This procedure addresses both producing the deliverable (VDR + submittals + turnover records) and using it during the integration/handover cycle.

## Prerequisites

- Declared upstream dependencies: none declared during PREPARATION (`_DEPENDENCIES.md`). Practical upstreams that should be available before VDR baseline is set (ASSUMPTION; treat as advisory until human confirms):
  - Engineering basis for the package (informed by DEL-046-04 Vendor Engineered Equipment Package).
  - Scope of Work (DEL-046-01) and Package Datasheet (DEL-046-02) sufficient to scope the document set.
- Reference materials available:
  - `26020-Package_Requirements.docx` package heading 1 (defines required vendor documents) — **location TBD** (file not text-accessible at run time).
  - `26020-Packages_Interfaces_4_export.xlsx` row 48 (workbook scope row) — **location TBD**.
  - DBM-Deepcut Acid Gas Compressor design basis sections (lines 878-1092 and equipment list lines 2529, 2572-2573, 2793-2794).
- VDR template approved by the Package Vendor and acceptable to the EPC Integrator (specific template **TBD** per source).

## Steps

### Step 1 — Initialize the VDR

1. Instantiate the Vendor Document Register using the template required by `26020-Package_Requirements.docx` (location TBD).
2. Populate the VDR with all required vendor documents identified in the Package Requirements vendor-document table. Specific line items are **TBD** pending source text access.
3. Tag each VDR row with discipline ownership (Process, Mechanical, Electrical, I&C, Quality, Operations) using the interface types from PACKAGE_REGISTER PKG-046 as the discipline frame.
4. Preserve the source vendor-document table rows as artifacts/evidence linked to the VDR (do not split into separate deliverables per `_CONTEXT.md` Notes).

### Step 2 — Schedule submittals

1. Establish the submittal milestone plan (e.g., kickoff, model review, IFA / IFR / IFC / AB — exact revision lexicon **TBD**) per Package Requirements.
2. Tie key submittals (datasheets, P&IDs, GAs, cause-and-effect, pulsation analysis) to the upstream EPC engineering milestones identified by the EPC Integrator.

### Step 3 — Produce engineering submittals

1. Generate the engineering documents required by REQ-046-05-R-03 (Specification.md). At minimum: process datasheets per unit; GA drawings for K-5450-1 and V-5530-1 plus spare; P&IDs; electrical one-line and schematics; instrument index; cause-and-effect; reciprocating compressor pulsation/vibration analysis.
2. Ensure consistency with the design basis: 5 stages of compression; cooler outlets at 110 deg F (43.33 deg C) for stages 1-4 and 150 deg F (65.56 deg C) for stage 5; 3:1 turndown VFD with cascading recycle; fail-open final discharge blowdown valve; no adjustable volume pockets; common forced-draft motor-driven air cooler per stage (DBM-Deepcut lines 1023, 1027, 1033, 1057).
3. Flag unresolved design-basis items in the submittal (compressor model KBT/6 vs KBK/6; discharge pressure 1,200 vs 1,500 psig; 2x100%+spare vs 3x50%) so the EPC Integrator can track resolution (Guidance.md Conflict Table entries C-046-05-02 through C-046-05-04).

### Step 4 — Produce quality, certification, and inspection records

1. Assemble material certifications (with NACE MR0175 / ISO 15156 conformance evidence for sour service — ASSUMPTION pending source confirmation).
2. Assemble NDE records, hydrotest records, ITP sign-offs, and code-stamp data reports (ASME U-1A or equivalent as applicable; specific codes **TBD** per source).
3. Assemble electrical area classification certifications (jurisdiction and code **TBD** per source).

### Step 5 — Produce O&M documentation

1. Assemble IOM manuals, lubrication and seal references, commissioning / two-year / capital spare parts lists, and special-tool lists.
2. Document the lube-oil injection-into-disposal-well philosophy and lube selection rationale (DBM-Deepcut line 1061).
3. Document the long two-compartment distance-piece purge philosophy and the check-valve arrangement preventing sour-gas backflow into the crankshaft (DBM-Deepcut line 2218).

### Step 6 — Transmit submittals through the VDR

1. Issue each document on its planned revision against the VDR; record transmittal number and date.
2. Route to EPC Integrator for interface/integration review per the agreed review cycle (cycle parameters **TBD** per source; DEL-046-06 is the formal acceptance disposition).
3. Manage review comments to closure; re-issue revisions per the controlled revision sequence.

### Step 7 — Compile turnover records

1. Produce the final turnover record set: transmittal letters, punch list (open and closed), mechanical completion certificate, and acceptance sign-offs.
2. Verify that every VDR row has reached its required final status (e.g., AB / certified) before mechanical completion is signed.
3. Hand over the closed VDR and the complete submittal record to the EPC Integrator and Owner/Operator (acceptance disposition is recorded under DEL-046-06).

## Verification

| Step | Verification |
|---|---|
| Step 1 | VDR template confirmed against Package Requirements; all required rows present |
| Step 2 | Submittal schedule integrated into EPC master schedule; milestone gates defined |
| Step 3 | Engineering submittals reviewed for design-basis consistency; unresolved items explicitly flagged |
| Step 4 | Quality records audit: material certs and code stamps present where required |
| Step 5 | O&M completeness check: IOM, lube, spares, tools all present |
| Step 6 | Transmittal log shows every VDR row transmitted with a recorded reviewer disposition |
| Step 7 | VDR closeout report shows 100% of required rows at final status; mechanical completion signed; turnover accepted |

Specific acceptance thresholds (e.g., percentage punch closure permitted at mechanical completion) are **TBD** pending source access to `26020-Package_Requirements.docx`.

## Records

The following evidence shall result from this procedure and shall be stored as deliverable artifacts:

- Final Vendor Document Register (closed status).
- All vendor document submittals at their final revision (engineering, quality, O&M, certifications).
- Transmittal log and review-comment closure log.
- Source vendor document table rows preserved as artifacts/evidence linked to the VDR.
- Turnover record set: transmittals, punch list (open/closed), mechanical completion certificate, acceptance sign-offs.
- Pointers to upstream design-basis sources used during drafting (DBM-Deepcut, Package Requirements).
