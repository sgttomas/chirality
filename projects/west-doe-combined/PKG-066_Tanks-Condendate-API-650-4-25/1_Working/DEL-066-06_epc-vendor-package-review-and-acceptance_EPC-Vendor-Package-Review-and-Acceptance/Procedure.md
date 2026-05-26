# Procedure: DEL-066-06 — EPC Vendor Package Review and Acceptance (PKG-066)

> Operational procedure for producing the EPC Integrator review-and-acceptance evidence set for the PKG-066 Condensate Storage Tanks (4-25) vendor package. This procedure describes how to **produce** the acceptance deliverable. Where project-specific procedural conventions are not stated in the locally accessible sources, the step is marked `TBD`.

## Purpose

Produce the four-artifact acceptance evidence set (vendor document review log, package acceptance checklist, test/inspection evidence index, turnover evidence index) and a signed acceptance record disposition for the PKG-066 vendor package.

## Prerequisites

### Required upstream EPC anchor deliverables (no formal declaration in `_DEPENDENCIES.md`; informal precondition)
- DEL-066-01 — Scope of Work (PKG-066): issued
- DEL-066-02 — Package Datasheet (PKG-066): issued
- DEL-066-03 — Construction Work Package (PKG-066): issued

### Required vendor inputs
- DEL-066-04 — Vendor Engineered Equipment Package: vendor-issued documentation set available for review
- DEL-066-05 — Vendor Document Turnover Package: vendor-issued turnover set available

If any upstream EPC anchor deliverable is not yet issued or any vendor input is not yet available, the acceptance activity is on hold; record the hold in `MEMORY.md` and notify the EPC discipline lead.

### Required reference materials
- `_REFERENCES.md` (deliverable-local)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (DBM)
- `_Sources/26020-Package_Requirements.docx` (package requirements, heading `26020-01-PT-19-004 - Tanks, Condensate`, 4-25, extracted-text line 5004 onward)
- Gate 7 snapshot registers: `DELIVERABLE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `OBJECTIVE_SCOPE_MAP.csv`

### Required tools / governance
- Project document control procedure (DOC-008) — exact location `TBD`
- EPC Integrator signature roster — `TBD`
- Acceptance disposition vocabulary — `TBD` (default placeholder per Specification REQ-066-06-10)

## Steps

### Step 1 — Receive and inventory vendor submissions
1. Confirm receipt of every vendor deliverable enumerated for `26020-01-PT-19-004 - Tanks, Condensate` (see Specification REQ-066-06-03 for the full list).
2. Log each submission in the Vendor Document Review Log with: document ID, vendor revision, date received.
3. Cross-check against the vendor's Vendor Document Index (PRQ-009). Flag missing or unexpected items.

### Step 2 — Establish the acceptance checklist
1. Build the checklist scaffold from:
   - the EPC SoW (DEL-066-01) sections,
   - the EPC Package Datasheet (DEL-066-02) parameters,
   - the EPC CWP (DEL-066-03) installation / tie-in items,
   - the interface applicability table (Datasheet, "Interface Applicability"; source `26020-Package_Requirements.docx` lines 5014-5055).
2. For each interface marked `Yes` (Process Piping, Relief/Flare/Vent, Drain/Containment, Area Lighting, Grounding/Bonding, Cathodic Protection, I&C/Control Cabling, Grading/Drainage/Containment, Structural/Foundations/Supports), add at least one acceptance line item.
3. For each interface marked `No`, add a single line item: "Not applicable per `26020-Package_Requirements.docx` line `<n>`".

### Step 3 — Review core vendor documents
1. Review each Core vendor document (PRQ-009, DOC-008, QLT-006, QLT-003, QLT-013, QLT-020, QLT-021, PRQ-013, PRQ-015, PRQ-016) for conformance with the EPC SoW and project document control procedure.
2. Disposition each per the disposition vocabulary (Specification REQ-066-06-10): ACCEPT, ACCEPT-WITH-CONDITIONS, REJECT, DEFER.
3. Record disposition and citations in the Vendor Document Review Log.

### Step 4 — Review core package engineering documents
1. Review MEC-001 (Mechanical Design Basis): verify alignment with DBM tank-design clauses (`4-25_Deepcut_DBM.md` lines 518-520, 1646-1648).
2. Review MEC-002 (Mechanical Equipment List): confirm tag set TK-9110-1, TK-9120-1, TK-9130-1, TK-9140-1, TK-9150-1 matches the package register (`4-25_Deepcut_DBM.md` line 2625). Reconcile any deviation against CONF-066-06-02 (Guidance Conflict Table).
3. Review MEC-003 / MEC-011 (Equipment Data Sheets / Storage Tank Data Sheets): verify modified API 650 basis, 16 oz test pressure, 90% maximum fill, blanket-gas system per API 2000, non-insulated product tanks.
4. Review MEC-014 (Mechanical Calculation Package): verify tank shell, roof, anchorage, and seismic / wind calculations are present and conform to the cited code basis.
5. Review MEC-016 / MEC-017 (Equipment GA / Installation Drawings): verify the inlet/outlet cascade philosophy with internal pipe stand (`4-25_Deepcut_DBM.md` line 1661) is represented, common truck-out connection is shown, and VRU header tie-in is shown.
6. Review MEC-018 (Lifting / Handling Study): confirm site lift access is feasible.
7. Review MEC-021 / MEC-022 (FAT Procedure / Report): confirm FAT scope includes the verifications listed in Specification REQ-066-06-07.

### Step 5 — Review storage-tank-specific and relief documents
1. Review MEC-005 (Static Equipment Specifications) and MEC-011 (Storage Tank Data Sheets) per Step 4.3 detail.
2. Review PRO-014 (Relief and Flare Design Basis), PRO-015 (PSV / Pressure Relief Sizing Calculations), PRO-016 (Relief Valve Data Sheets) for: EPRV sizing, blanket-gas sizing per API 2000, off-spec overhead vent sizing, tank isolation philosophy with possible sour vapours, thermal expansion. These are explicitly DBM open items (`4-25_Deepcut_DBM.md` line 1663) and must not be accepted silently.

### Step 6 — Compile DBM-open-items disposition annex
1. Enumerate each DBM open item relevant to the condensate-tank package (Specification REQ-066-06-06; source `4-25_Deepcut_DBM.md` lines 1663, 1815).
2. For each item, record: Resolved (with cite), Deferred to detailed engineering (with owner), or Open (with owner and target date).

### Step 7 — Assemble test / inspection evidence index
1. Index: executed ITP (QLT-003), MTRs / certificates (QLT-013), NDE reports, FAT Report (MEC-022), Inspection Release Certificate (QLT-020).
2. Each indexed item must be cross-referenced to the acceptance checklist line(s) it supports.

### Step 8 — Assemble turnover evidence index
1. Index: Manufacturing Record Book / Vendor Data Book (QLT-021), Final Supplier Documentation (PRQ-016), Mechanical Final Documentation (MEC-023), IOM Manual (MEC-025), Spares / Special Tools (MEC-024), SPIR (PRQ-015), Logistics / Shipping Plan (PRQ-013).
2. Each indexed item must be cross-referenced to the acceptance checklist line(s) it supports.

### Step 9 — Roll up overall acceptance disposition
1. Roll up checklist line dispositions:
   - All ACCEPT → package-level ACCEPT.
   - One or more ACCEPT-WITH-CONDITIONS, no REJECT → package-level ACCEPT-WITH-CONDITIONS; conditions enumerated.
   - One or more REJECT → package-level REJECT or HOLD (per EPC discipline lead judgment); rejection rationale recorded.
   - One or more DEFER on items affecting safety / integration → package-level HOLD until deferred items are closed.
2. Draft the signed acceptance record summarizing the disposition and citing the supporting evidence indexes.

### Step 10 — Acceptance signature and issuance
1. Route the signed acceptance record to the EPC Integrator's mechanical discipline lead (or designee) for signature. (Signatory roster `TBD`.)
2. Issue the acceptance record into project document control. (Issuance route `TBD`.)
3. Update `_STATUS.md` per the project state model — outside the scope of this skill run.

## Verification

| Verification check | Method |
|---|---|
| All enumerated vendor deliverables logged | Inventory comparison vs. Specification REQ-066-06-03 list |
| Every "Yes" interface has at least one checklist line | Audit checklist against Datasheet Interface Applicability table |
| Tank design conformance evidenced | Inspection of MEC-011, MEC-014 review notes |
| DBM open items dispositioned | Inspection of DBM-open-items annex |
| Test/inspection evidence complete | Inventory check vs. Specification REQ-066-06-07 list |
| Turnover evidence complete | Inventory check vs. Specification REQ-066-06-08 list |
| Disposition vocabulary applied consistently | Spot-check checklist disposition column |
| Acceptance signed by authorized signatory | Inspection of signature block vs. signatory roster (roster `TBD`) |

## Records

The records produced and retained by this procedure:

- Vendor Document Review Log (working artifact, retained through project life)
- Package Acceptance Checklist (signed)
- Test / Inspection Evidence Index (signed)
- Turnover Evidence Index (signed)
- DBM-Open-Items Disposition Annex
- Signed Acceptance Record (the final disposition artifact)
- Procedural run-record entries in `_run_records/` (when produced by subsequent TASK runs)

All records are stored within `DELIVERABLE_PATH` or routed to the project's document control repository per DOC-008. Record-retention duration per project records policy — `TBD`.
