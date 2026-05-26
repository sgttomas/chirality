# Procedure: DEL-090-06 — EPC Vendor Package Review and Acceptance

> Operational steps to produce the EPC Integrator's vendor package review-and-acceptance evidence (review log, acceptance checklist, test evidence) for PKG-090 VRU 3-25. Steps map back to the requirements in `Specification.md` and the rationale in `Guidance.md`.

## Purpose

Produce auditable evidence that the Package Vendor's submittals and the as-delivered VRU 3-25 package have been reviewed against the EPC Scope of Work (DEL-090-01), Package Datasheet (DEL-090-02), and Construction Work Package (DEL-090-03), and that acceptance and turnover are supported by recorded review comments, checklist sign-offs, and test/inspection records.

## Prerequisites

- DEL-090-01 (Scope of Work) is published and accessible. Source: `_CONTEXT.md` Scope.
- DEL-090-02 (Package Datasheet) is published and accessible. Source: `_CONTEXT.md` Scope.
- DEL-090-03 (Construction Work Package) is published and accessible. Source: `_CONTEXT.md` Scope.
- DEL-090-04 (Vendor Engineered Equipment Package) submittals are issued by the Package Vendor. Source: `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DEL-090-05 (Vendor Document Turnover Package) is being assembled or is complete. Source: `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Source `26020-Package_Requirements.docx package heading 43` is referenced for clause-level verification (location `TBD` for slice access at this run).
- Review templates (review log, acceptance checklist) are available. ASSUMPTION (templates not enumerated in accessible source slices).

## Steps

1. **Initialize review register.** Open the Vendor Document Review and Comment Log (ART-08602095B0); list every expected vendor submittal per the EPC vendor document list. (Detailed list `TBD` — depends on DEL-090-02 / DEL-090-03 outputs.)
2. **Triage each vendor document.** For every received submittal, record receipt, assign reviewer(s), and target disposition date. Source: REQ-090-06-001.
3. **Configuration verification.** Confirm the as-proposed configuration matches SOW-0250: two 100% capacity trains, lead-lag, sour service, single building. Source: REQ-090-06-002.
4. **Compressor make/model verification.** Confirm Ro-Flo 12S/212M two-stage rotary vane positive displacement, four stage units across two trains. Source: REQ-090-06-003.
5. **NACE / sour-service verification.** Review material certificates, welder qualifications, and NACE designation per SOW-0251. Source: REQ-090-06-004.
6. **Seal-system verification.** Verify Plan 53-type dual mechanical pressurized barrier seal using fuel gas, with alarms and primary vent to LP flare. Confirm interfaces to fuel-gas supply and LP flare. Source: REQ-090-06-005. Specific seal pressures/alarm setpoints: `TBD`.
7. **Driver and VFD verification.** Verify per train: one 200 HP, 600 V, 3-phase, 60 Hz, VFD-ready motor driving Stage 1 and Stage 2; cooler motors 600 V, VFD-ready. Source: REQ-090-06-006.
8. **Design / operating-condition verification.** Verify design conditions (0.9 kPag suction, 483 kPag discharge, 28 e3m³/d capacity, 102 °C design temperature) and operating temperatures and dewpoints from SOW-0252. Source: REQ-090-06-007 and REQ-090-06-008.
9. **Factory / shop test review.** Receive, witness or review test records (mechanical run, performance, hydrostatic, motor PI, etc.); file in ART-63586A61E0. Source: REQ-090-06-010. Test list detail: `TBD`.
10. **Turnover documentation gate.** Confirm DEL-090-05 closure: full vendor document turnover package received, indexed, and complete per the EPC document list. Source: REQ-090-06-009; REQ-090-06-012 (ASSUMPTION).
11. **Integration-readiness check.** Confirm "By others" items (shipping to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs) are ready or staged. Source: REQ-090-06-011 (SOW-0252).
12. **Acceptance decision.** Issue acceptance (or accept-with-comment / reject) on the Vendor Package Acceptance and Turnover Checklist (ART-2BE816FC33). Record residual items if conditional acceptance is granted.
13. **Close the review register.** Mark ART-08602095B0 closed; archive all evidence; transmit acceptance evidence to the package's final closure record.

## Verification

| Step Verified | How | Evidence Artifact |
|---|---|---|
| Steps 1–2 | Every expected vendor submittal has a logged disposition. | ART-08602095B0 |
| Steps 3–8 | Each configuration / requirement check has a recorded result with the source SOW citation. | ART-08602095B0; ART-2BE816FC33 |
| Step 9 | Each required test has either a witnessed-test record or a reviewed certified record. | ART-63586A61E0 |
| Step 10 | DEL-090-05 closure confirmed. | DEL-090-05 closure note; ART-2BE816FC33 |
| Step 11 | "By others" interface readiness signed. | ART-2BE816FC33 |
| Step 12 | Acceptance decision recorded and signed by EPC Integrator. | ART-2BE816FC33 |

## Records

The following records result from this procedure (per `_CONTEXT.md` anticipated artifacts and `ARTIFACT_REGISTER.csv`):

- Vendor Document Review and Comment Log — ART-08602095B0.
- Vendor Package Acceptance and Turnover Checklist — ART-2BE816FC33.
- Factory/Shop Test and Inspection Evidence — ART-63586A61E0.
- Turnover Evidence (cross-reference to DEL-090-05 outputs).
