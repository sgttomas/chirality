# Procedure: DEL-085-06 — EPC Vendor Package Review and Acceptance

## Purpose

Operational procedure the EPC Integrator follows to review the High Pressure flare stack vendor package, integrate the acceptance evidence, resolve open interface items where authorized, and produce the four anticipated artifacts (vendor document review log, package acceptance checklist, test/inspection evidence, turnover evidence) for handoff. Source basis: `_CONTEXT.md`, `Specification.md`, `Guidance.md`, and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Flare and Blowdown section.

## Prerequisites

- `DEL-085-01` Scope of Work — accepted version available.
- `DEL-085-02` Package Datasheet — accepted version available.
- `DEL-085-03` Construction Work Package — accepted version available.
- `DEL-085-04` Vendor Engineered Equipment Package — delivered.
- `DEL-085-05` Vendor Document Turnover Package — delivered.
- Accessible source slices: `3-25_Comp_and_Liquids_DBM.md` Flare and Blowdown (L497-L499); package-specific source slice from `26020-Package_Requirements.docx` heading 38 (currently **location TBD**, extraction required).
- Geotechnical/foundation as-built records.
- Interface ruling on 03-25 / 04-25 HP/LP service split (per Spec R-04). If absent, the acceptance proceeds with R-04 as a gating open item.
- No declared upstream/downstream dependencies in `_DEPENDENCIES.md` at PREPARATION; sibling acceptance ordering (DEL-085-01..05) is implicit not declared. TBD whether a declared dependency entry is required.

## Steps

1. **Open acceptance record.** Initialize the vendor document review log, package acceptance checklist (templated against R-01 through R-09 in `Specification.md`), evidence index, and turnover index.
2. **Document review (R-01, R-10).** For each vendor document in `DEL-085-05`, record document ID, revision, reviewer, disposition (Accept / Accept-with-comment / Reject), and link to comment file. Reconcile coverage against `DEL-085-02` index.
3. **Geometric and sizing checks (R-02, R-03).** Compare as-delivered stack OD (660 mm), height (60,957 mm), and 508 mm relief headers against vendor as-built drawings and field measurement records. Capture LP stack OD value once vendor data is available (current source value is TBD — DBM L499).
4. **Interface ruling resolution (R-04).** Attach the 03-25 / 04-25 service split ruling to the acceptance record. If unresolved, record R-04 as an open gating item and notify the project interface authority.
5. **Cold-weather qualification (R-05).** Verify vendor-supplied qualification certificates and heat-tracing/winterization provisions for -40 °C to +35 °C envelope (DBM L96, L145).
6. **Foundation reconciliation (R-06).** Verify civil/structural sign-off reconciles vendor anchor loads against the as-built foundation per the geotechnical basis (DBM L700).
7. **KO drum and pump evidence (R-07).** Within the agreed scope envelope, collect FAT, inspection, and field-test evidence for V-4100-2, V-4150-2, V-3900-2 and pumps P-4100-2, P-4150-2, P-3900-2. Confirm scope split with compressor / tank-farm packages before applying this step (Guidance Considerations).
8. **Test/inspection evidence completeness (R-08).** Walk the FAT, weld, NDE, pressure-test, burner functional, and loop-check evidence against the package acceptance checklist. Flag absent records.
9. **Flare-study condition (R-09).** Add a statement to the acceptance record that permit/operations-final acceptance is conditional on completion of final flare studies and permit-final emissions tabulation (DBM L548, L555).
10. **Compile turnover evidence (R-10).** Produce the four artifacts and a single acceptance summary that lists: accepted items, accept-with-comment items, rejected items, open gating items (notably R-04), and conditional items (notably R-09).
11. **Acceptance disposition.** EPC Integrator records acceptance disposition: ACCEPTED, ACCEPTED-WITH-CONDITIONS, or REJECTED. Disposition is a human decision; this procedure produces only the evidence supporting the decision.

## Verification

| Check | Pass criterion |
|---|---|
| Review log completeness | Every vendor document in `DEL-085-05` has a log entry with disposition |
| Checklist coverage | Every requirement R-01..R-09 has a checklist row with evidence pointer or open-item note |
| Geometric conformance | Stack OD, height, header sizing recorded with deviation status (DBM L497, L499) |
| Interface ruling | R-04 status explicitly recorded (resolved or gating) |
| Cold-weather evidence | Vendor qualification certificates present in evidence set |
| Foundation acceptance | Civil/structural sign-off attached |
| Open and conditional items registered | R-09 (flare-study conditionality) and any unresolved interface items present in the acceptance summary |
| Four artifacts present | Review log, checklist, evidence package, turnover package all produced |

## Records

The following records result from this procedure (`_CONTEXT.md` anticipated artifacts):

- Vendor document review log (per-document disposition history).
- Package acceptance checklist (requirements traceability, R-01..R-09).
- Test/inspection evidence package (FAT, NDE, pressure test, functional test, loop checks).
- Turnover evidence package (operations handoff index: manuals, spares, certifications, as-built drawings, open and conditional items list).
- Acceptance disposition record (ACCEPTED / ACCEPTED-WITH-CONDITIONS / REJECTED) signed by EPC Integrator authority.
