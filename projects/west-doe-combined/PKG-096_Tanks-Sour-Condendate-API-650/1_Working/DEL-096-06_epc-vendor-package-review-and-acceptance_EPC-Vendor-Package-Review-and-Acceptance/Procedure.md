# Procedure — DEL-096-06 EPC Vendor Package Review and Acceptance (PKG-096 Tanks, Sour Condendate (API 650))

## Purpose

Operational procedure for producing the EPC vendor-package review-and-acceptance dossier for PKG-096 (Tanks, Sour Condendate (API 650)). Steps are derived from Specification REQ-1..REQ-10 (see `Specification.md`) and from the package heading "Tanks, Sour Condensate" in `26020-Package_Requirements.docx`.

## Prerequisites

- Acceptance basis available and accepted:
  - DEL-096-01 Scope of Work
  - DEL-096-02 Package Datasheet
  - DEL-096-03 Construction Work Package
- Vendor inputs received for review:
  - DEL-096-04 Vendor Engineered Equipment Package
  - DEL-096-05 Vendor Document Turnover Package
  - (Sibling identifiers per `PKG-096/1_Working/` folder layout — **ASSUMPTION (best-effort mapping)**.)
- Source materials accessible:
  - `26020-Package_Requirements.docx` heading "Tanks, Sour Condensate"
  - `_CONTEXT.md` and `_REFERENCES.md` (this deliverable folder)
- Project document control procedure (governs review-status codes): **location TBD**.
- Project quality procedure (governs acceptance-disposition codes): **location TBD**.
- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md` at PREPARATION (review treats DEL-096-01..05 as logical inputs by package context).

## Steps

### Step 1 — Establish acceptance basis and vendor input set (verifies REQ-1, REQ-2)

1. Open a new dossier index.
2. Record acceptance basis: DEL-096-01, DEL-096-02, DEL-096-03 (with revisions and dates).
3. Record vendor inputs under review: DEL-096-04, DEL-096-05 (with vendor revisions and dates).
4. Cite the source for vendor-package identity (`26020-Package_Requirements.docx` heading "Tanks, Sour Condensate").

### Step 2 — Build/maintain the Vendor Document Review Log (verifies REQ-3)

1. Enumerate vendor documents received under DEL-096-04 and DEL-096-05.
2. For each document, record: document ID and title; vendor revision; date received; reviewer; review status; review comments; comment-disposition status; re-submittal reference.
3. Cross-check the enumerated list against the package heading's "Vendor Engineering Deliverables" list. Missing IDs become open items (feeds Step 5).

### Step 3 — Execute Package Acceptance Checklist for source-derived attributes (verifies REQ-4)

For each line below, compare vendor evidence to the source attribute and record Pass / Open / Fail with reference to vendor document and section:

1. Quantity and tags: two (2) 3800 bbl, TK-9110-2 and TK-9120-2.
2. Code/fabrication: Modified API 650 (note: enumerate "Modified" deltas per Conflict Table C-3 in `Guidance.md`).
3. Service: sour (H2S); NACE compliant (note specific NACE doc per Conflict Table C-4).
4. Blanket gas: per API 2000.
5. Internal coating: Devchem 253 on floors, walls, roofs.
6. Insulation: non-insulated.
7. Relief: PVRV (vacuum / modulating pressure relief), EPRV (emergency relief), VRU header connection.
8. Fill protection: maximum fill 90% shutdown; nozzles sized so plant design capacity can fill a single tank.
9. Design conditions: 32 oz test pressure (clarify per Conflict Table C-1); -40 °C / 60 °C; design flow 27,606 kg/h / 919 Am3/d (Item No. 1).

### Step 4 — Interface integration acceptance (verifies REQ-5)

1. For each "Yes" interface in the package heading's Physical Interface Summary (Process Piping; Relief / Flare / Vent; Drain / Containment; Area / Exterior Lighting; Grounding / Bonding; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports), record vendor evidence (drawing / spec / calc) or accepted interface handoff to an EPC discipline package.
2. For each "No" interface (Utility Piping; Electrical Power; EHT; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Product Loading; Pipeline / Pigging), confirm absence from vendor scope.
3. Apply Conflict Table C-5 (`Guidance.md`) re: blanket gas / VRU routing — confirm they are routed under Process Piping and Relief / Flare / Vent rather than Utility Piping.

### Step 5 — Vendor engineering deliverable completeness (verifies REQ-6)

1. Reconcile vendor deliverable list against the package heading's "Vendor Engineering Deliverables".
2. List any missing IDs (relative to the applicable subset for tanks) as open items.

### Step 6 — Test / inspection evidence (verifies REQ-7)

1. Confirm presence and review status for: `MEC-021` (FAT/Performance Test Procedure), `MEC-022` (FAT/Performance Test Report), `QLT-003` (ITP), `QLT-013` (Material Test Reports / Certificates), `QLT-020` (Inspection Release Certificate).
2. Record FAT witness/review evidence (date, witness, status). Specific witness/hold-point convention: **TBD** (defer to ITP `QLT-003`).

### Step 7 — Turnover evidence (verifies REQ-8)

1. Confirm presence and review status for: `QLT-021` (Manufacturing Record Book / Vendor Data Book), `PRQ-016` (Vendor Data Book / Final Supplier Documentation), `MEC-023` (Vendor Data Book / Mechanical Final Documentation), `MEC-025` (Mechanical Equipment IOM Manual), `PRQ-015` (Spare Parts Interchangeability Record / SPIR), `PRQ-013` (Logistics / Shipping Plan).

### Step 8 — "By Others" boundary confirmation (verifies REQ-9)

1. For each "By Others" item — foundations; mounting tanks at site; electrical/instrumentation; platforms; staircase — record the EPC discipline production package or work-front that owns the item.
2. Confirm none are absorbed into vendor scope without an explicit change record.

### Step 9 — Acceptance status and disposition (verifies REQ-10)

1. Populate acceptance status per checklist item (status code-set per project document control procedure — location TBD).
2. Compile open-items list with source reference per item.
3. Record overall acceptance disposition (e.g., Accepted / Accepted with Open Items / Rejected — code-set TBD).
4. Route dossier to the human approver for binding acceptance (K-AUTH-1). This procedure does not itself certify the package.

## Verification

| Verification | What is checked | How |
|---|---|---|
| V-1 | Acceptance basis and vendor inputs identified | Dossier index lists DEL-096-01..03 and DEL-096-04..05 |
| V-2 | Vendor Document Review Log complete | Spot-check at least one entry per vendor document class; check required fields populated |
| V-3 | Source-derived attributes checklist complete | All Step 3 items have a status and a vendor reference (or a logged open item) |
| V-4 | Interface acceptance complete | All Yes interfaces have evidence; all No interfaces confirmed absent |
| V-5 | Vendor engineering deliverable reconciliation complete | No silently-missing IDs from the applicable subset |
| V-6 | Test/inspection evidence in place | All five MEC/QLT items in Step 6 present with status |
| V-7 | Turnover evidence in place | All six items in Step 7 present with status |
| V-8 | By-Others boundary confirmed | Each By-Others item mapped to an EPC owner |
| V-9 | Acceptance disposition recorded | Overall disposition + open-items list + reviewer name and date |

## Records

The procedure produces these records, which together constitute the deliverable artifact set per `_CONTEXT.md` Anticipated Artifacts:

- Vendor Document Review Log (per Step 2)
- Package Acceptance Checklist (per Steps 3, 4, 5, 8)
- Test / Inspection Evidence Index (per Step 6)
- Turnover Evidence Index (per Step 7)
- Acceptance Summary and Open Items (per Step 9)
- Cross-reference map: checklist items → source attribute (in `26020-Package_Requirements.docx` heading "Tanks, Sour Condensate") and acceptance basis (DEL-096-01, DEL-096-02, DEL-096-03)

Exact filenames, formats, storage locations, and approval-record format: **TBD** (defer to project document control and quality procedures — locations TBD).
