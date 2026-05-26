# Procedure — DEL-057-06 EPC Vendor Package Review and Acceptance

This procedure describes how the EPC Integrator produces and uses the review-and-acceptance artifacts that constitute this deliverable.

## Prerequisites

- EPC Scope of Work (`DEL-057-01`) issued. Source: DELIVERABLE_REGISTER row `DEL-057-01`.
- EPC Package Datasheet (`DEL-057-02`) issued. Source: DELIVERABLE_REGISTER row `DEL-057-02`.
- EPC Construction Work Package (`DEL-057-03`) issued. Source: DELIVERABLE_REGISTER row `DEL-057-03`.
- Vendor Engineered Equipment Package (`DEL-057-04`) submitted by Package Vendor. Source: DELIVERABLE_REGISTER row `DEL-057-04`.
- Vendor Document Turnover Package (`DEL-057-05`) being assembled by Package Vendor with EPC Integrator review. Source: DELIVERABLE_REGISTER row `DEL-057-05`.
- Access to source materials in `_REFERENCES.md` (acceptance-criteria slice — location TBD).
- Note: no upstream/downstream dependencies are declared in `_DEPENDENCIES.md` at PREPARATION; the deliverables above are de facto upstreams. ASSUMPTION.

## Steps

1. **Open the review record.** Initialize the vendor document review log with reference to PKG-057 anchor deliverables (`DEL-057-01`/`-02`/`-03`) and vendor inputs (`DEL-057-04`/`-05`). Source: `_CONTEXT.md` Anticipated Artifacts.
2. **Receive vendor submittals.** Log each vendor document received under `DEL-057-05` into the review log with date, revision, and originating vendor reference. Source: DELIVERABLE_REGISTER row `DEL-057-05` (Anticipated Artifacts: vendor document register; submittals).
3. **Review against EPC Scope of Work.** For each `SOW-0177`..`SOW-0180` line covered by PKG-057, confirm vendor package content addresses the scope item; record disposition in the package acceptance checklist. Source: `_CONTEXT.md` Covers Scope Items; DELIVERABLE_REGISTER scope text for `DEL-057-06`.
4. **Review against Package Datasheet.** Compare vendor-engineered attributes (equipment list, design criteria, interface requirements) to the EPC Package Datasheet (`DEL-057-02`); record matches, deltas, and required vendor responses. Source: DELIVERABLE_REGISTER scope text for `DEL-057-06`; row for `DEL-057-02`.
5. **Review against Construction Work Package.** Verify that vendor-supplied installation/tie-in inputs align with the Construction Work Package (`DEL-057-03`) installation plan, tie-in list, and turnover checklist. Source: DELIVERABLE_REGISTER scope text for `DEL-057-06`; row for `DEL-057-03`.
6. **Disposition comments and re-submittals.** Issue review comments to the Package Vendor and update the review log on each cycle until each document reaches "accepted" or "accepted with comments closed." Source: `_CONTEXT.md` Anticipated Artifacts (vendor document review log). ASSUMPTION: standard EPC review-cycle convention; specific cycle limits are `TBD` pending `26020-Package_Requirements.docx` heading 12.
7. **Collect test/inspection evidence.** Gather records for required tests/inspections on the vendor package (factory acceptance, source inspection, etc.). Specific required tests: `TBD` (location TBD — `26020-Package_Requirements.docx` heading 12). Source: `_CONTEXT.md` Anticipated Artifacts.
8. **Collect turnover evidence.** Gather turnover records demonstrating handoff readiness, including residual punch items. Source: `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER scope text ("handoff readiness").
9. **Finalize integration acceptance.** Close the package acceptance checklist with an integrated disposition referencing the review log, test/inspection evidence, and turnover evidence. Source: DELIVERABLE_REGISTER scope text ("integration acceptance"); R-08 ASSUMPTION in `Specification.md`.
10. **Archive evidence.** Retain the four artifacts in the deliverable folder per project records convention. ASSUMPTION; specific retention rules are `TBD`.

## Verification

| Check | Expected Outcome |
|---|---|
| Review log exists and covers all vendor submittals from `DEL-057-05` | Pass when each submittal has a logged disposition |
| Acceptance checklist covers `SOW-0177`..`SOW-0180` | Pass when all four SOW items are dispositioned |
| Acceptance checklist traces to `DEL-057-01`/`-02`/`-03` | Pass when each acceptance row cites at least one anchor deliverable |
| Test/inspection evidence exists for each required test | Pass when each test in the (TBD) required-tests list has a record; TBD until source slice imported |
| Turnover evidence exists and residual punch items are listed | Pass when turnover records and a punch list (possibly empty) are present |
| Cross-document consistency with `Specification.md` requirements R-01..R-08 | Pass when each requirement has a corresponding step/verification artifact |

## Records

- Vendor document review log — see `Datasheet.md` Construction table.
- Package acceptance checklist — see `Datasheet.md` Construction table.
- Test/inspection evidence — see `Datasheet.md` Construction table.
- Turnover evidence — see `Datasheet.md` Construction table.

All four are produced and retained within this deliverable folder once execution begins; this PREPARATION-to-INITIALIZED pass establishes the structure, not the content of the records themselves.
