# Guidance — DEL-064-01 Scope of Work (Tanks, Water (API 650) 4-25)

> Directional guidance for authoring and reviewing the EPC Scope of Work for PKG-064.
> Pass 1/Pass 2 draft. Rationale is drawn from the locally accessible DBM source; conservative inferences are labeled `ASSUMPTION`.

## Purpose

The Process Water Storage tanks (TK-5317-1, TK-5318-1) exist to hold an atmospheric inventory of utility-quality process water at the 04-25 Deep Cut Gas Plant tank farm. The DBM identifies two specific consumers explicitly: make-up water to the caustic NGL contactor water-wash system during upset operation (DBM-Deepcut §SEC-07) and the process-water storage and transfer service associated with the Module 530 amine regeneration module/building (DBM-Deepcut §SEC-05). The EPC Scope of Work is the EPC Integrator's anchor deliverable that bounds package identity, function, source basis, and whole-facility integration so that downstream EPC Integrator deliverables (Datasheet, Construction Work Package, Vendor Acceptance) and the Package Vendor's engineered tank package (DEL-064-04) and turnover documentation (DEL-064-05) share a single, source-anchored definition. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-05, §SEC-07, §SEC-10, §SEC-16; `_CONTEXT.md` Scope; GATE-07 PKG-064 deliverable family.

## Principles

- **Source-anchored boundaries.** The DBM is the authoritative source for package identity, tagged equipment, code basis, freeze protection, and tank-farm siting. Where the DBM does not state a value (e.g., tank capacity, internal coating, PVRV sizing, drain routing), the EPC SOW carries `TBD` rather than synthesize a value. Source: DBM-Deepcut §SEC-05, §SEC-07, §SEC-10, §SEC-16.
- **Atmospheric API 650 service discipline.** The package class "Tanks, Water (API 650) 2" anchors the tanks to API 650 design and its companion atmospheric-tank conventions (venting, foundations, inspection). SOW review should resist drift toward pressure-vessel (ASME VIII) conventions that are not warranted for atmospheric water service. Source: DBM-Deepcut §SEC-16 row 102.
- **Winter-freeze priority.** The DBM is unambiguous that water tanks shall be insulated to prevent winter freezing. Insulation, and any heat tracing if required, must be carried as scope and not deferred to vendor optional pricing. Source: DBM-Deepcut §SEC-10.
- **Two consumers, one inventory.** Both confirmed consumers — caustic NGL water-wash make-up and Module 530 process-water service — draw on the same storage inventory. SOW should make the multi-consumer character explicit so capacity sizing in DEL-064-02 (Package Datasheet) cannot be done against a single demand. Source: DBM-Deepcut §SEC-05 Module 530, §SEC-07 NGL caustic treating.
- **Package-boundary discipline.** The Process Water Transfer Pumps (P-5317-1, P-5318-1) are physically and contractually in Tank Farm Pump Building 2 (a separate package). Containment berms are in PKG-006. The SOW should keep these interfaces visible so they are not silently absorbed into the tank vendor's scope. Source: DBM-Deepcut §SEC-16 deliverable row 83; GATE-07 PACKAGE_REGISTER (PKG-006).
- **Tank-farm siting governance.** Tank spacing rules are facility-wide (NFPA 30, OGAOM, API 2510) and govern plot-plan freeze, not package vendor scope. The SOW should reference §SEC-02 directly rather than reinvent the basis. Source: DBM-Deepcut §SEC-02 Atmospheric Tank and General Plant Spacing.

## Considerations

- **Make-up routing is open.** DBM-Deepcut §SEC-07 explicitly states that final make-up water routing remains to be confirmed during detailed engineering. The SOW should keep the make-up interface visible to the caustic-treating package owner so the resolution is captured at the interface, not silently inside PKG-064. Source: DBM-Deepcut §SEC-07.
- **Module 530 process-water service is summary-only.** The §SEC-05 Module 530 description names "process-water storage and transfer" without separating storage flow, transfer flow, or quality limits. SOW review should treat the Module 530 demand as a sizing input that must be pulled forward from the amine package owner. Source: DBM-Deepcut §SEC-05 Module 530.
- **Tank capacity is not source-stated.** The accessible DBM source slice does not give a process-water tank capacity (the storage summary table in §SEC-03 covers produced water, slop, and condensate). Capacity must come from confirmed consumer-demand basis at detailed engineering. Avoid carrying a placeholder volume that becomes a de facto requirement. Source: §SEC-03 storage summary (no process water row); `location TBD`.
- **PVRV/EPRV applicability by analogy is unsafe.** Produced water tanks have an explicit PVRV requirement in §SEC-03; copying that statement onto process water tanks without source basis would conflate sour and utility services. Note the analogy as ASSUMPTION and resolve in DEL-064-02. Source: §SEC-03 produced-water PVRV statement.
- **Internal coating is service-dependent.** Devchem 253 is specified for produced water (sour, hydrocarbon-bearing) service. Process water coating selection (if any) should be re-evaluated against actual service chemistry; do not carry Devchem 253 forward as a default. Source: §SEC-03 produced-water coating.
- **Flare-to-tank spacing analogy.** §SEC-02 cites 25 m (82 ft) for flare-to-atmospheric-produced-water-tank. Applicability to process water tanks should be ruled by the discipline team at plot freeze; do not adopt as a hard requirement without ruling. Source: §SEC-02; ASSUMPTION.
- **Tag-register dependency.** Confirmed tags are TK-5317-1, TK-5318-1. Ancillary instrument and valve tags will come from the facility tag register. SOW should name the tag-register dependency rather than leave the gap open at vendor PO. Source: §SEC-16 row 102.

## Trade-offs

- **Two-tank, no-spare configuration.** Two tanks provide some operational flexibility (one in service, one in cleaning/maintenance, or both in parallel for surge) but there is no explicit standby philosophy in the accessible source. SOW should keep the operational philosophy (parallel vs. swing) as a detailed-engineering question rather than infer a default. Source: §SEC-16 row 102 (count only).
- **Insulation vs. heat tracing.** §SEC-10 mandates insulation to prevent freezing. Whether insulation alone is sufficient or whether heat tracing/heating is also needed depends on confirmed winter design temperature and tank-volume thermal mass. SOW should flag this as scope-affecting rather than predetermine. Source: §SEC-10.
- **Vendor scope width (foundations and ringwall).** Whether foundations and ringwall are vendor scope or civil discipline scope affects DEL-064-02 (Package Datasheet) and DEL-064-03 (Construction Work Package). SOW should leave the split as an explicit decision rather than assume vendor or civil by default. Source: split not stated in accessible source.

## Examples

- **Make-up routing example.** DBM-Deepcut §SEC-07 line: "Make-up water, if required during upset operation, is supplied from the process water storage tank. Final make-up water routing remains to be confirmed by detailed engineering." This is the canonical SOW reference for the caustic NGL water-wash interface and the explicit open item to forward to detailed engineering.
- **Module 530 process-water example.** DBM-Deepcut §SEC-05 Module 530 module/building scope line includes "process-water storage and transfer" alongside the amine regenerator scope. This grounds the second confirmed consumer of PKG-064 inventory.
- **Tag-list example.** DBM-Deepcut §SEC-16 deliverable row 102 reads: "Tanks, Water (API 650) 2 / PROCESS WATER STORAGE TANK (x2, 4-25) / 4-25 (Deepcut) / 2 / TK-5317-1, TK-5318-1". These are the only confirmed PKG-064 tags in the accessible source.

## Conflict Table (for human ruling)

No source conflicts identified from the locally accessible DBM material in Pass 1 / Pass 2 cross-checks. The locally-not-accessible references (Workbook Packages row 96; `26020-Package_Requirements.docx` package heading 19) may introduce conflicts when extracted; surface them in the next pass when source slices become available.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none) | — | — | — | — | — | TBD |
