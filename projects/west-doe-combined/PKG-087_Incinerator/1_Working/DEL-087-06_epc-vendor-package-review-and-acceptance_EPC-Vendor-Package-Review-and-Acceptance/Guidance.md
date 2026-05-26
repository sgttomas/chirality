# Guidance — DEL-087-06 EPC Vendor Package Review and Acceptance

> Directional document. Explains why this deliverable exists, the principles that should govern the EPC Integrator's review and acceptance of the PKG-087 Incinerator vendor package, key trade-offs, and pointers to examples. Source-grounded; rationale beyond the available sources is marked ASSUMPTION or TBD.

## Purpose

PKG-087 (Incinerator) is one of the Gate-5 EPC anchor packages in the West Doe PROJECT_DECOMP. The EPC Integrator is responsible for assembling a defensible evidence base that the vendor's engineered equipment package (DEL-087-04) and vendor document turnover package (DEL-087-05) meet the EPC scope of work (DEL-087-01), package datasheet (DEL-087-02), and construction work package (DEL-087-03). DEL-087-06 is the deliverable in which that evidence is consolidated and a human acceptance disposition is recorded. (Source: DELIVERABLE_REGISTER.csv row 353, GATE-07 snapshot; _CONTEXT.md.)

The incinerator package itself is safety-significant: it terminates spent caustic and DSO off-gas streams from the NGL mercaptan treating system and is sited adjacent to the flare stacks. Acceptance defects can become safety, environmental, or schedule defects.

## Principles

1. **Acceptance is a human authority decision.** The EPC Integrator's authority signs the acceptance disposition (R-AC-10). Reviewers may propose, agents may compile, but only humans accept. (Cross-ref: K-AUTH-1.)
2. **Evidence must be traceable.** Every checklist line item should point at a specific vendor document, test report, or inspection record, and every requirement should be traceable to its source (SOW row, Datasheet attribute, CWP step, or applicable standard).
3. **Source over narrative.** If a vendor narrative summary disagrees with the source (workbook row 64, 26020 heading 40, DBM-Deepcut), the source governs. Record the disagreement in the Conflict Table rather than silently reconciling.
4. **Safety-critical features are not waivable on review.** Spacing (R-AC-07), backflash protection (R-AC-08), and the upstream knock-out drum (R-AC-08) are derived from the design-basis manual; deviations require engineering disposition, not reviewer judgement.
5. **Open design parameters are not implicit acceptance.** R-AC-09 makes the DBM TBCs (supplemental fuel gas rate, incinerator flow basis, dilution gas, 03-25/04-25 operational responsibility) explicit acceptance gates with closure paths.
6. **Acceptance is a snapshot.** When acceptance is granted, freeze the evidence set. Later changes ride a new revision or scope-change packet (K-SNAP-1).

## Considerations

- The incinerator described in DBM-Deepcut is physically at 03-25 and services the 04-25 NGL mercaptan treating system (lines ~1568-1570). PKG-087 is listed as the "Incinerator" package in PROJECT_DECOMP. Whether DEL-087-06 accepts a *new* 04-25 incinerator, a *shared-facility* 03-25 incinerator modification, or a vendor scope inside an existing 03-25 asset is not directly stated in the decomposition row and is **NEEDS_HUMAN_RULING**.
- The 26020 source set defines package scope and interfaces but is held as binary documents (.docx, .xlsx) at the shared source root. Acceptance criteria that depend on those slices are intentionally carried as TBD with `location TBD` until extracted.
- Objectives OBJ-002, OBJ-004..OBJ-010 are associated by package-grouping heuristic, not by direct deliverable-ID mapping; treat as directionally relevant, not as binding acceptance criteria (per skill Step 1.3 default).
- Vendor document turnover (DEL-087-05) and vendor engineered equipment (DEL-087-04) are upstream evidence sources. If their accepted-snapshot state is `OPEN` or `INITIALIZED`, acceptance evidence for DEL-087-06 cannot be considered complete; coordinate via the package-level register.
- Emissions values for the incinerator are flagged in DBM-Deepcut as "future addition; current non-regenerative-caustic emissions basis TBD" (lines ~2244-2246). Treat emissions-related acceptance items as conditional pending confirmed basis.

## Trade-offs

- **Comprehensive vs. timely review.** A complete dossier (every NCR resolved, every TBC closed) maximizes confidence but can delay mechanical completion. The acceptance disposition allows "Accepted with Conditions" for non-safety items provided a closure path is documented (R-AC-09).
- **Reliance on vendor evidence vs. independent verification.** Where vendor FAT/SAT reports are authoritative, EPC review may be a paper review; for safety-critical interfaces (KO drum, flame arrestor, spacing, thermal radiation), independent walk-down is preferred over paper-only review.
- **Snapshotting vs. living dossier.** Snapshotting acceptance evidence at the moment of disposition is cleaner for audit; a "living" dossier risks blurring what was actually accepted. This deliverable should snapshot.
- **Package-grouped objective association vs. explicit mapping.** Using the package-heuristic keeps work moving; carrying it as ASSUMPTION makes future explicit-mapping reconciliation cheap.

## Examples

Concrete examples (sample checklist rows, sample NCR templates, sample acceptance disposition language) require either prior project-specific templates or a worked vendor submittal. None are present in the deliverable folder or the locally accessible sources.

- Sample acceptance checklist row: **TBD** (location TBD)
- Sample NCR disposition language: **TBD** (location TBD)
- Sample acceptance disposition statement: **TBD** (location TBD)

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Incinerator location and scope ownership: DBM-Deepcut places the incinerator at facility 03-25 servicing 04-25; PROJECT_DECOMP lists PKG-087 "Incinerator" without explicit location | DBM-Deepcut `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines ~1568-1572 | PROJECT_DECOMP DELIVERABLE_REGISTER.csv rows 348-353 (PKG-087) | Datasheet Conditions, Specification R-AC-06/07/08, Procedure prerequisites | PROPOSAL: confirm via 26020-Package_Requirements.docx heading 40 once extracted | TBD |
| C-02 | Emissions basis: DBM-Deepcut marks the incinerator emissions rows as "future addition; current non-regenerative-caustic emissions basis TBD"; objective-grouping suggests OBJ-006..OBJ-010 (which may include environmental/emissions) apply now | DBM-Deepcut `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines ~2244-2246 | OBJECTIVE_DELIVERABLE_MAP.csv (package-grouped) | Specification R-AC-12, Datasheet Conditions (Emission basis) | PROPOSAL: defer emissions-related acceptance items pending confirmed non-regen-caustic emissions basis | TBD |
