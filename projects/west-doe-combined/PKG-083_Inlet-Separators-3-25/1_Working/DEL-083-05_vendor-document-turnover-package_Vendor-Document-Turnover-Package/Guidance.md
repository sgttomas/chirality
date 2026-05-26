# Guidance — DEL-083-05 Vendor Document Turnover Package

## Purpose

This deliverable exists because PKG-083 (Inlet Separators 3-25) is a vendor-supplied package whose engineering and operating intent live in vendor-authored documents rather than in EPC-Integrator-authored drawings. Without a controlled turnover of those documents — registered, revision-controlled, accepted, and handed over — the EPC Integrator cannot integrate the package into the 3-25 West Doe Compressor Station, the operator cannot operate or maintain it, and the regulator cannot accept the pressure equipment. The turnover package is the durable bridge between vendor knowledge and facility-owner knowledge.

It supports the project objectives associated with the PKG-083 deliverable row (`OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010` — ASSUMPTION: package-grouping heuristic per `_CONTEXT.md` and per the four-documents skill's `OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC`).

## Principles

1. **Source is the vendor's deliverable list.** The composition of the turnover package is not negotiable downward from the vendor engineering deliverables table issued for PKG-083 in `26020-Package_Requirements.docx` heading 36. Adding rows is permissible when warranted; deleting rows requires a documented ruling.
2. **One register of record.** PRQ-009 (Vendor Document Index) is the single source of truth for what is in, and what is missing from, the turnover package. The folder of files is evidence; PRQ-009 is the ledger.
3. **Identity is preserved end-to-end.** A submittal that loses its source deliverable ID (`MEC-009`, `QLT-021`, etc.) is harder to audit, harder to integrate, and harder to retrieve at the operating end of life. Names and metadata SHOULD carry the ID.
4. **Vendor authors; integrator reviews.** The Package Vendor produces these documents; the EPC Integrator reviews them at interface and integration boundaries (per `_CONTEXT.md` ResponsibleParty). Neither party can substitute for the other.
5. **Acceptance is final and human.** Per K-AUTH-1, no agent or automated tool can sign off the turnover package. Acceptance records carry human authority signatures.
6. **Artifacts are evidence, not deliverables.** Raw vendor document rows that arrive as artifacts (per `_CONTEXT.md`) are attached to register rows; they do not multiply into separate deliverables (Gate 5 ruling in decomposition notes).

## Considerations

- **Sour service implications for documentation.** Inlet separators in 3-25 service handle sour gas, sour condensate, and sour water (`26020-Package_Requirements.docx` heading 36, Basic Scope). This raises the importance of material test reports (`QLT-013`), pressure equipment registration (`REG-022`), and the FAT/inspection record stack (`MEC-021/022`, `QLT-003/020/021`). Treat those rows as critical-path submittals rather than routine.
- **Interface breadth.** Eleven interface types apply to PKG-083 (see `Datasheet.md` Attributes). Each interface type maps to a discipline family inside the vendor engineering deliverables table (e.g., Fire & Gas → TSF rows; Structural → STR rows). The EPC Integrator review should be organized by interface family rather than by single document.
- **Pressure equipment registration.** `REG-022` is jurisdiction-bound. ASSUMPTION: ABSA (Alberta) is the registration authority for West Doe; confirm at executing-project mobilization.
- **Two-of-a-kind sparing.** Two identical separators are supplied (2 x 50%). The turnover package should make clear whether each row applies to both units, only one, or differs by serial number (relevant especially for `MEC-009`, `QLT-013`, `QLT-020`).
- **Inaccessible source detail.** The vendor RFQ (`26020-02-PT-RFQ-17-003_Inlet Separators 1_R0.docx`) is referenced by 26020 but was not opened locally during this draft. Detail beyond what 26020 captures is `TBD` until the RFQ is read directly. Do not invent requirements from the RFQ that 26020 does not echo.
- **Status-vs-content separation.** PRQ-009 tracks status (rev, transmittal, acceptance); the individual submittal carries content. Use both. Do not conflate "the latest submitted PDF" with "the accepted revision" until DOC-008 routing records confirm acceptance.

## Trade-offs

- **Granularity of register rows vs. ease of maintenance.** A finer-grained register (e.g., per data sheet per tag number) is more auditable but costlier to maintain. A coarser register (e.g., one row covering "Pressure Vessel Data Sheets" for both units) is cheaper but loses tag-level traceability. The PKG-083 default should follow whatever DOC-008 defines; deviate only with vendor agreement.
- **Early-issue vs. final-issue acceptance.** Some rows (e.g., `MEC-016` General Arrangement) are needed at IFR/IFA early in execution for integration; others (e.g., `MEC-022` FAT Report, `MEC-023` Final Vendor Data Book) only exist at the end. Plan the turnover package as a flowing register, not a single end-of-job dump.
- **Coverage vs. duplication.** Some rows overlap (e.g., `MEC-023 Vendor Data Book / Mechanical Final Documentation` vs. `PRQ-016 Vendor Data Book / Final Supplier Documentation` vs. `QLT-021 Manufacturing Record Book / Vendor Data Book`). Decide one canonical "data book" hierarchy with the vendor and reflect that in PRQ-009; otherwise the EPC Integrator will receive overlapping content.

## Examples

- **A row at full lifecycle:** `MEC-009 Pressure Vessel Data Sheets` arrives at IFR, IFA, IFC, then As-Built revisions; PRQ-009 carries the rev history; the As-Built rev is the one referenced by `REG-022` for ABSA registration; the As-Built data sheet is the version included in the final Vendor Data Book (`MEC-023` / `PRQ-016`). All four rev artifacts are evidence; the As-Built is the authoritative content for operations.
- **A composite turnover row:** `QLT-021 Manufacturing Record Book` may itself contain MTRs (`QLT-013`), inspection releases (`QLT-020`), and weld maps. PRQ-009 should still carry `QLT-013` and `QLT-020` as separate register rows pointing to their location inside `QLT-021`, to keep traceability.

## Conflict Table (for human ruling)

_None recorded at Pass 2._ No source-source contradictions surfaced during drafting; the only unresolved item is the local inaccessibility of the RFQ source, which is recorded as `TBD`/`location TBD` in the relevant sections rather than as a conflict.
