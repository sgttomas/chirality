# Guidance: DEL-003-04_epc-civil-discipline-production-package

## Purpose

The EPC / Civil Discipline Production Package turns the accepted Site Grading decomposition basis into a Civil discipline production package for non-vendor scope. Its main job is to hold the source-supported grading, drainage, containment, retention pond, and civil quantity-takeoff basis while clearly separating accepted facts from `TBD` design-development inputs.

## Principles

- Use Gate 7 as accepted decomposition truth for deliverable identity, parent package, objectives, and artifact expectations.
- Use accessible source materials for technical requirements. The workbook establishes this package as Civil Site Grading with Drain / Containment and Grading / Site Drainage / Spill Containment interfaces.
- Keep geotechnical, topographical, drainage, and retention pond closure open until the named external inputs are received.
- Do not convert preliminary assumptions into final design values.
- Keep the production package auditable by tying each requirement or open item to a source location or marking it `TBD`.

## Considerations

The DBM civil basis supports a conservative production package, but it does not close all detailed engineering inputs. The geotechnical assessment report, topographical survey and grade surface file, plot plan/retention pond reference, and detailed engineering drainage design are external dependencies for final design closure.

The workbook row 4 interface marks only two active interface columns: Drain / Containment and Grading / Site Drainage / Spill Containment. Other workbook interface columns are not marked for this row and should not be added as active interfaces without a source update or human ruling.

Civil deliverable codes from the package requirements document are useful as a candidate discipline deliverable register, but the source excerpt does not by itself prove final package-specific document numbering for `DEL-003-04`. Treat these entries as an **ASSUMPTION** until the discipline deliverable register is approved.

## Trade-offs

| Topic | Conservative Treatment |
|---|---|
| Current rainfall basis | Use the stated proxy basis and carry uncertainty until hydrology is updated. |
| Facility pad slope | Carry 1.5% down from pipe racks and the allowed 1.0% reduction as source-supported; require engineering justification for reductions. |
| Maximum grade slope | Use 3H:1V maximum unless a specific engineered exception or geotechnical requirement supersedes it. |
| Retention pond | Track location and capacity as `TBD` pending plot plan coordination and detailed engineering. |
| Civil production package contents | Include the candidate civil deliverable set, but mark final register approval as `TBD`. |

## Examples

| Source-Supported Item | How to Use It |
|---|---|
| Workbook row 4 marks Drain / Containment and Grading / Site Drainage / Spill Containment | Include those as active package interfaces; do not add unmarked interfaces without evidence. |
| DBM SEC-11 states ditch slope 0.2% minimum | Use it as a check criterion for drainage drawings/calculations. |
| DBM SEC-11 lists the topographical survey and grade surface file as required for grading/drainage design | Record missing survey/grade-surface information as an open input, not as a design-complete condition. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-001 | Final Civil discipline deliverable register for `DEL-003-04` is not approved in the local truth set. | `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv` list "TBD discipline deliverable register". | `_Sources/26020-Package_Requirements.docx` lists candidate civil items `CIV-003`, `CIV-004`, `CIV-015`, `CIV-019` under civil grading / spill containment interfaces. | Datasheet Attributes; Specification Requirements; Procedure Steps | Use the package requirements entries as candidate artifacts only; require human or discipline approval before treating them as the final register. | TBD |
