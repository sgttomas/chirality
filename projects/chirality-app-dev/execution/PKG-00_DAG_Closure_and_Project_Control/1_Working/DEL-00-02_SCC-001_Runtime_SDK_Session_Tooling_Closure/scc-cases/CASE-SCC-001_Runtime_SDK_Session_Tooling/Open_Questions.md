# Open Questions: CASE-SCC-001

| QuestionID | Question | Needed From | Status |
| --- | --- | --- | --- |
| Q-SCC-001-001 | Which runtime/SDK reciprocal rows are true sequencing prerequisites, and which should become interface, conformance, or evidence-handoff requirements? | WORKING_ITEMS/TASK plus human ruling | OPEN |
| Q-SCC-001-002 | Which session, transcript, HarnessEvent, redaction, and logger impacts require product implementation only, and which require decomposition or scope amendment? | WORKING_ITEMS/TASK plus human ruling | OPEN |
| Q-SCC-001-003 | Which tooling, permission, MCP, write/edit, hook, and compaction mirror impacts should remain deferred versus enter a governed owner workflow? | WORKING_ITEMS/TASK plus human ruling | OPEN |
| Q-SCC-001-004 | What exact downstream rerun sequence is required after any owner workflow changes land? | RECONCILIATION/DepClosure handoff | OPEN |
| Q-SCC-001-005 | For the runtime/SDK core pairs indexed in `FIND-SCC-001-004` through `FIND-SCC-001-008`, should dependency workflow classify reciprocal rows directly or should any row first require SCOPE_CHANGE/decomposition amendment? | Human ruling plus owner workflow | OPEN |
| Q-SCC-001-006 | For the session/audit pairs indexed in `FIND-SCC-001-009` through `FIND-SCC-001-011`, should dependency workflow classify reciprocal rows directly or should terminal taxonomy, redaction-helper paths, or storage/linkage TBDs first require human or SCOPE_CHANGE rulings? | Human ruling plus owner workflow | OPEN |
| Q-SCC-001-007 | For the tooling/permissions/MCP pairs indexed in `FIND-SCC-001-012` through `FIND-SCC-001-015`, should dependency workflow classify reciprocal rows directly or should event writer, status lifecycle API, hook mapper, validation fixture, or REF-006 hash-mismatch TBDs first require human or SCOPE_CHANGE rulings? | Human ruling plus owner workflow | OPEN |
| Q-SCC-001-008 | Consolidation ruling: may dependency workflow proceed first on the dependency-workflow-ready bucket while the human-ruling-needed bucket remains open? | Human ruling plus dependency workflow | OPEN |
| Q-SCC-001-009 | Should RECONCILIATION use `SCC-001_Ruling_Workbook.csv` as the decision surface for the next CHANGE handoff, with `SCC-001_Dispatch_Plan.md` controlling sequential versus parallel owner-workflow work? | Human ruling plus RECONCILIATION | OPEN |

## Notes

The imported packets are seed evidence. They provide useful grouping and citations, but they are not enough by themselves to decide dependency treatment, scope impact, or closure. Runtime/SDK core, session/audit, and tooling/permissions/MCP row evidence have now been indexed into the case and normalized into `SCC-001_Ruling_Workbook.csv`. Candidate remedies are bucketed for owner workflow handoff; row classifications remain provisional until accepted by the appropriate owner workflow.
