# Guidance: DEL-040-06_epc-vendor-package-review-and-acceptance

## Purpose

This deliverable exists to provide the EPC Integrator's review-and-acceptance evidence for the Package Vendor's engineered 600 V electrical building (`PKG-040`, building 860-1). It is the closure record demonstrating that the vendor-delivered package can be integrated into the West Doe facility against the EPC Scope of Work, Package Datasheet, and Construction Work Package, and that all applicable interface and document obligations are met or formally tracked. It supports objectives OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, and OBJ-010 (`OBJECTIVE_DELIVERABLE_MAP.csv`).

## Principles

- **Two-party authorship, one-party acceptance.** The Package Vendor produces the engineered package and its document set; the EPC Integrator decides acceptance. This split is set in `PACKAGE_REGISTER.csv` for `PKG-040` and is binding for this deliverable.
- **Source-grounded review.** EPC review of vendor submittals shall trace requirements to the Package Datasheet and to the facility electrical design basis (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`). Where source detail is not available, mark `TBD` rather than infer values.
- **Interface-by-interface coverage.** All twelve `PKG-040` interface types are reviewed individually so that no interface is silently waived. (`INTERFACE_REGISTER.csv` for `PKG-040`.)
- **Conditional acceptance is the default tolerance valve.** When integration risk is low but a small number of open vendor items remain, prefer conditional acceptance with named owners and closure dates over hard rejection that interrupts construction sequencing.
- **No facility re-engineering through acceptance.** Acceptance does not change the Package Datasheet; if vendor submittals deviate, route through the Package Datasheet change path, not through silent acceptance.

## Considerations

- **600 V building scope.** Building 860-1 is the 600 V General Area / Tank Farm electrical building (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2816). Reviewers should expect 600 V MCC, 600 V SCR heater-control panels, 600 V to 208/120 V step-downs and panelboards, UPS systems, PLC control panels, and network racks — not the 13.8 kV switchgear lineup, which belongs in the main switchgear electrical building (line 2811).
- **Bottom-entry / pile-elevated construction.** Cable routing under the building drives the construction interface; reviewers should confirm that civil/structural turnover (`DEL-040-03` outputs) align with vendor pile/elevation drawings.
- **HVAC n+1.** N+1 is explicit in the DBM (line 2975); a vendor providing a single HVAC unit is a hard finding, not a comment.
- **Grounding architecture.** 5 A continuous HRG with ground/resistor fault detection on the 600 V MCC and alarm-only ground-fault protection (line 2985) is a facility safety/availability tradeoff. Do not accept vendor deviations to trip-on-fault without an explicit Package Datasheet change.
- **Standby-power applicability.** TOU standby generators connect at the 600 V MCC level via transfer switches (line 2943). Confirm whether 860-1 participates; this is a known `TBD` on the Datasheet (REQ-040-06-10 / Conditional).
- **F&G device list `TBD`.** Pending Package Datasheet; do not invent.
- **Vendor document register gap.** `ARTIFACT_REGISTER.csv` notes that detailed vendor-document requirements are not present in current source material for sibling vendor packages (`ART-EF224E6F34` family). The review log shall not assume completeness of the register; treat absence as an open item.

## Trade-offs

- **Speed vs. evidence depth.** A thorough document-by-document log can stall construction sequencing; conditional acceptance with tracked open items is preferred when risk is contained to commissioning rather than installation.
- **Reject-and-resubmit vs. comment-and-resolve.** Reject only on safety, code, or hard interface conflicts; otherwise comment-and-resolve preserves the vendor schedule.
- **Single checklist vs. per-interface checklist.** A single-record checklist (`ART-F627B8462B`) is preferred for traceability and gate sign-off; per-interface working sheets may be used during review but reconcile to the single record at acceptance.

## Examples

Examples cannot be drawn directly from accessible source for `PKG-040`. Sibling-package `DEL-031-06` Datasheet/Specification (PKG-031 step-down transformer) provides a useful pattern for interface-by-interface checklists; this is context only and is not authority for `PKG-040` acceptance.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-040-06-01 | The vendor-document detail base for sibling Electrical packages is flagged in `ARTIFACT_REGISTER.csv` as `TBD vendor document register` (e.g., `ART-EF224E6F34`). For `PKG-040` it is unclear whether `_Sources/26020-Package_Requirements.docx` contains a `PKG-040`-specific section. | `ARTIFACT_REGISTER.csv` row `ART-EF224E6F34` (sibling pattern) | `_Sources/26020-Package_Requirements.docx` (not yet sliced for `PKG-040`) | Datasheet / Vendor document set basis; Specification / REQ-040-06-01 | PROPOSAL: treat the source document as authoritative for register completeness; open a deliverable-local slice request for the `PKG-040` section. | TBD |
| CONF-040-06-02 | Acceptance closure rule (REQ-040-06-13) is an `ASSUMPTION` not stated in accessible source. | This Specification (assumed) | No source slice | Specification / REQ-040-06-13; Guidance / Principles | PROPOSAL: confirm the two-gate rule through EPC project procedure (out of accessible scope here). | TBD |
| CONF-040-06-03 | Standby-power applicability for 860-1 is unstated (REQ-040-06-10). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2943 (general policy) | `PACKAGE_REGISTER.csv` row `PKG-040` (silent on 860-1 specifically) | Datasheet / Standby-power interface; Specification / REQ-040-06-10 | PROPOSAL: confirm by Package Datasheet (`DEL-040-02`) single-line review. | TBD |
