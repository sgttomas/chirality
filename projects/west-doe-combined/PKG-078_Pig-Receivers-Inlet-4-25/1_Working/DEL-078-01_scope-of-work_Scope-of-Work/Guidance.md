# Guidance — DEL-078-01 Scope of Work (PKG-078 Pig Receivers (Inlet) 4-25)

> Directional guidance for authors and reviewers of the EPC Integrator Scope of Work for `PKG-078`. Rationale is grounded in `PACKAGE_REGISTER.csv` PKG-078, `SCOPE_LEDGER.csv` rows SOW-0161–0164, and the `OBJECTIVE_REGISTER.csv` rows OBJ-001 / OBJ-003 / OBJ-004 / OBJ-005 / OBJ-006 / OBJ-007 / OBJ-008 / OBJ-009 / OBJ-010 in the GATE-07 snapshot.

## Purpose

The Scope of Work for `PKG-078` is the package anchor for all downstream EPC and vendor deliverables in `PKG-078_Pig-Receivers-Inlet-4-25`. Its existence is mandated by user instruction as a "Gate 5 EPC anchor deliverable" (`DELIVERABLE_REGISTER.csv` DEL-078-01 Notes). It is the only document in the package that simultaneously states (i) what is being purchased and built, (ii) what the EPC must integrate around it, and (iii) who owns what — supporting OBJ-004's vendor/EPC split as a first-class outcome rather than a buried convention.

## Principles

1. **Source-anchored.** Every requirement, equipment tag, design number, and boundary statement must trace to either (a) `26020-Package_Requirements.docx` package heading 31, (b) Workbook Packages row 78, or (c) the GATE-07 register rows that extracted from those sources. (Source: `PACKAGE_REGISTER.csv` PKG-078 SourceBasis; `SCOPE_LEDGER.csv` source columns.)
2. **Workbook row authoritative.** When package identity, tracking number, or discipline assignment is in tension, the workbook row (row 78) is authoritative. (Source: `SCOPE_LEDGER.csv` SOW-0161 Notes: "Workbook package row is authoritative.")
3. **Vendor/EPC split preserved.** Package engineering, design, vendor documentation, and the physical equipment package belong to the Package Vendor; everything connecting the package to the facility belongs to the EPC Integrator. (Source: `PACKAGE_REGISTER.csv` PKG-078 ResponsibilityModel; `OBJ-004`.)
4. **By-Others list is binding.** Items listed in `SOW-0164` "By others" — interconnecting piping, DCS integration, foundations, electrical supply to MCC — are not part of `PKG-078`. The SoW must say so explicitly so vendor pricing and EPC integration scope agree.
5. **Sour-service and HP-flare risks surfaced.** Sour-service (1.0 mol% H2S) and HP-flare venting drive material selection, relief-system tie-ins, and operability provisions. The SoW must flag these as integration-critical concerns so OBJ-009 (safety/regulatory) is visibly carried into package execution.
6. **HIPPS architecture preserved.** The redundant pneumatic hi-low shutoff topology in `SOW-0163` is a safety architecture, not a convenience feature. Do not simplify it in the SoW narrative.
7. **Open items remain open.** Where the source says "TBC" (e.g., normal flowrate per receiver) or omits a numerical value (e.g., HIPPS setpoint), the SoW must carry the gap forward as `TBD`, not silently fill it. This supports OBJ-010 (open-item closure evidence).

## Considerations

- **04-25 facility context.** `PKG-078` is the WBS 01 package serving the 04-25 Deepcut facility (225 MMSCFD design throughput). It is structurally parallel to `PKG-089` (Pig Receivers (Inlet) 3-25, WBS 02, 80 MMSCFD, 2 receivers, no HIPPS — only ESDV). Authors should consult `PKG-089` for the comparable 3-25 SoW only after this SoW is grounded in PKG-078 sources, to avoid cross-contamination of design values. (Source: `PACKAGE_REGISTER.csv` PKG-089 vs PKG-078.)
- **Downstream consumer.** The pig receivers feed the inlet separators. The 3-25 separator package is `PKG-083`; the 04-25 separator package ID is not directly verified in this pass and is recorded as `TBD` in the Conflict Table.
- **Interface envelope.** `PKG-078` carries ten distinct interface types (Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; I&C / Control Cabling; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Pipeline / Pigging). Each interface must be named in the SoW even when the detailed interface fact is carried in `DEL-078-02 Package Datasheet`. (Source: `PACKAGE_REGISTER.csv` PKG-078 InterfaceTypes.)
- **Objective coverage.** This SoW supports OBJ-001 (04-25 facility scope), OBJ-003 (commercial/boundary), OBJ-004 (vendor/EPC split), OBJ-005 (electrical infrastructure tie-in), OBJ-006 (controls/I&C tie-in), OBJ-007 (utilities), OBJ-008 (civil/structural/site), OBJ-009 (safety/sour-service/regulatory), OBJ-010 (operability/handoff). The SoW narrative should make each connection visible at least once so traceability is auditable.

## Trade-offs

- **Narrative completeness vs. duplication with `DEL-078-02`.** The SoW should fully identify the package and its boundaries but should not duplicate the interface-fact matrix that lives in `DEL-078-02 Package Datasheet`. Prefer summary statements with explicit pointers to the Datasheet for interface details.
- **Equipment-level detail vs. vendor-design freedom.** The SoW must preserve source-stated equipment requirements (size, count, HIPPS, ESDV, vent routing, sour-service basis) without specifying vendor-design-level choices (e.g., specific valve makes, exact pneumatic supply pressures). The vendor's freedom is preserved by `OBJ-004` and the ResponsibilityModel.
- **By-Others clarity vs. EPC integration narrative.** "By others" boundaries (interconnecting piping, DCS, foundations, MCC supply) belong to the EPC Integrator's broader scope but not to `PKG-078`. The SoW should name them as boundaries here and refer to the relevant EPC scope packages (TBD: cross-package pointers not enumerated in this pass).

## Examples

- **Equipment identity example (from source):** "Three (3) identical 610 mm (24") OD pig receivers `PR-1010-1`, `PR-1020-1`, `PR-1030-1` on dedicated structural steel non-enclosed skids." (Source: `SCOPE_LEDGER.csv` SOW-0163.)
- **Boundary example (from source):** "By others: interconnecting piping, DCS integration, foundations, electrical supply to MCC." (Source: `SCOPE_LEDGER.csv` SOW-0164.)
- **Responsibility example (from source):** "Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration." (Source: `PACKAGE_REGISTER.csv` PKG-078 ResponsibilityModel.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-078-01-01 | Numerical HIPPS setpoint ("maintain inlet separator vessel operating pressure below applicable") not given in extracted source slice | `SCOPE_LEDGER.csv` SOW-0163 | (none — silent) | Specification R-3.2; Datasheet HIPPS row | PROPOSAL: defer to inlet-separator package (04-25 separator package ID TBD) MAOP/operating-pressure record | TBD |
| CONF-078-01-02 | Downstream separator package ID for 04-25 not directly verified | `PACKAGE_REGISTER.csv` PKG-078 (process-function text) | `PACKAGE_REGISTER.csv` PKG-083 is 3-25 (verified); 04-25 row not examined in this pass | Specification Scope; Guidance Considerations | PROPOSAL: confirm the 04-25 Inlet Separators package ID before publishing the SoW integration narrative | TBD |
| CONF-078-01-03 | Normal flowrate per receiver shown as "TBC" in source | `SCOPE_LEDGER.csv` SOW-0164 | (none — explicit TBC in source) | Specification R-6.5; Datasheet Conditions | PROPOSAL: carry `TBC` forward to `DEL-078-02 Package Datasheet` and to the vendor RFQ; close via vendor confirmation | TBD |
| CONF-078-01-04 | Sour-service codes/standards not enumerated in extracted source slice | (none in SCOPE_LEDGER extract) | NACE/ISO sour-service practice (ASSUMPTION) | Specification Standards | PROPOSAL: confirm applicable sour-service standard set in `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-15 (regulatory/codes) | TBD |
