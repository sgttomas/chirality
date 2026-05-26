# Specification: DEL-051-06 — EPC Vendor Package Review and Acceptance

> Normative requirements the EPC Integrator must satisfy to declare the PKG-051 Process Heat Medium Unit vendor package "accepted" and ready for handoff.

## Scope

### In scope
- EPC Integrator review of the Package Vendor's engineered equipment package (DEL-051-04) against the EPC Scope of Work (DEL-051-01), EPC Package Datasheet (DEL-051-02), and EPC Construction Work Package (DEL-051-03).
- Vendor document review (interlocked with DEL-051-05 Vendor Document Turnover Package).
- Package acceptance checklist closure.
- Test/inspection evidence aggregation (shop and field).
- Turnover evidence aggregation.
- Issuance of an acceptance disposition (accept / accept with conditions / reject) recorded as a human-approved decision.

### Out of scope
- Vendor engineering execution (belongs to DEL-051-04).
- Vendor document production (belongs to DEL-051-05).
- Construction execution detail (belongs to DEL-051-03).
- Whole-facility integration scope outside the PKG-051 boundary.
- Final authorization to operate (separate human/regulatory decision).

## Requirements

> Requirements are tagged REQ-051-06-### for cross-document traceability. Source-grounded requirements cite the source slice; inferences are labelled ASSUMPTION.

### Document review

- **REQ-051-06-001** — The acceptance package SHALL include a vendor document review log enumerating each vendor document received, its revision, review status, and comment-resolution state. *(Source: `_CONTEXT.md` Anticipated Artifacts.)*
- **REQ-051-06-002** — The review log SHALL link to the Vendor Document Turnover Package (DEL-051-05) for document provenance. *(ASSUMPTION: cross-deliverable interlock implied by decomposition narrative.)*
- **REQ-051-06-003** — Each acceptance-critical vendor document SHALL be reviewed against DEL-051-01 (Scope of Work) and DEL-051-02 (Package Datasheet) before acceptance. *(Source: `_CONTEXT.md` Scope.)*

### Technical conformance

- **REQ-051-06-010** — Vendor-supplied heat medium heater SHALL be confirmed as API-560 natural-draft cabin-style direct-fired thermal-fluid heater. *(Source: DBM-Deepcut line 1998.)*
- **REQ-051-06-011** — Vendor SHALL confirm fluid suitability (Brenntag Petrotherm) to maximum bulk temperature 599 deg F / 315 deg C. *(Source: DBM-Deepcut line 1951.)*
- **REQ-051-06-012** — All vendor-supplied heat-medium-containing components SHALL be designed for at least 350 psig / 2413 kPag. *(Source: DBM-Deepcut line 1983.)*
- **REQ-051-06-013** — Heater design duty SHALL be at least 1.25 x winter steady-state design duty (winter total ~21,913 kW). *(Source: DBM-Deepcut lines 1976, 1998.)*
- **REQ-051-06-014** — Heater minimum-flow capability SHALL be confirmed by the vendor; the 85% of design flow assumption SHALL be either validated or revised in writing by the heater vendor. *(Source: DBM-Deepcut line 2000.)*
- **REQ-051-06-015** — Burner-management SHALL provide at minimum 4:1 turndown, with the option to shut individual burners for deeper turndown. *(Source: DBM-Deepcut line 1998.)*
- **REQ-051-06-016** — Heater PSV SHALL discharge to a pop tank sized at approximately 600 bbl with level-switch validating "normally empty" during operation. *(Source: DBM-Deepcut line 2002.)*
- **REQ-051-06-017** — Sour tube-rupture venting to the pop tank, including dispersion modeling if required, SHALL be reviewed and dispositioned by the EPC Integrator before acceptance. *(Source: DBM-Deepcut line 2002.)*
- **REQ-051-06-018** — Heater area classification confirmation SHALL be recorded as General Purpose. *(Source: DBM-Deepcut line 2000.)*
- **REQ-051-06-019** — Circulation pumps SHALL be single-stage vertical inline; consolidated pump sparing basis SHALL be selected and recorded prior to acceptance. *(Source: DBM-Deepcut line 1996.)*
- **REQ-051-06-020** — Pump motors SHALL be capable of starting under cold-start 15 deg C conditions. *(Source: DBM-Deepcut line 1996.)*
- **REQ-051-06-021** — Vendor pressure-relief valves SHALL be acceptance-tested against API STD 527 seat-tightness criteria. *(Source: DBM-Deepcut line 3388.)*

### Inspection and test

- **REQ-051-06-030** — The acceptance package SHALL contain shop-test evidence (MTRs, welder qualifications, NDE reports, hydrotest records, performance tests) for each vendor-supplied component within the package. *(ASSUMPTION: standard EPC vendor-package acceptance practice; specific scope confirmation TBD pending `26020-Package_Requirements.docx` heading 6 access.)*
- **REQ-051-06-031** — The acceptance package SHALL contain site receipt-inspection records for each shipped item. *(ASSUMPTION: standard EPC practice; TBD pending source.)*
- **REQ-051-06-032** — The acceptance package SHALL contain commissioning test evidence covering loop integrity (flushing, fill, sampling), burner-management functional test, pump-module start under cold-start condition, PSV pop test, and pop-tank level-switch test. *(Source: DBM-Deepcut Heat Medium Basis; ASSUMPTION on test sequence specificity.)*

### Turnover

- **REQ-051-06-040** — The acceptance package SHALL include a turnover package containing: final vendor document set, spare-parts list, warranty documentation, calibration records, and outstanding-items (punchlist) log. *(Source: `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION on item-level granularity.)*
- **REQ-051-06-041** — A handover certificate SHALL be issued and signed by both the EPC Integrator and the Package Vendor for the package as a whole. *(ASSUMPTION: standard practice; TBD pending source.)*
- **REQ-051-06-042** — Acceptance disposition (accept / accept with conditions / reject) SHALL be recorded with the names of the authorizing parties; agents SHALL NOT author the disposition. *(Source: governance invariant K-AUTH-1.)*

### Coverage

- **REQ-051-06-050** — The acceptance package SHALL demonstrate satisfaction of SOW-0165, SOW-0166, SOW-0167, SOW-0168 as enumerated in `_CONTEXT.md`. Detailed mapping rows TBD pending `26020-Package_Requirements.docx` heading 6 access.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| API STD 560 | Heat medium fired heater design | DBM-Deepcut line 1998 |
| API STD 527 (5th Edition) | PSV seat tightness — leakage acceptance basis | DBM-Deepcut line 3388 |
| BCER Oil and Gas Processing Facility Regulation, Appendix 1, Schedule 1, Section 7(4) | Facility-level flare radiation limits (only indirectly applicable to vendor PSV discharge routing review) | DBM-Deepcut line 2050 |
| EPC Scope of Work (DEL-051-01) | Internal scope basis | DELIVERABLE_REGISTER row 438 |
| EPC Package Datasheet (DEL-051-02) | Internal technical basis | DELIVERABLE_REGISTER row 439 |
| EPC Construction Work Package (DEL-051-03) | Internal installation/tie-in basis | DELIVERABLE_REGISTER row 440 |
| Other industry standards (e.g., ASME B31.3 for piping, ASME BPV) | location TBD — text not accessible from `26020-Package_Requirements.docx` heading 6 |

## Verification

| Requirement ID(s) | Verification approach | Acceptance evidence |
|---|---|---|
| REQ-051-06-001..003 | Document audit | Vendor document review log; cross-link to DEL-051-05 |
| REQ-051-06-010..013, 015, 018, 019, 021 | Design document review against EPC datasheet (DEL-051-02) | Reviewed and stamped vendor datasheets; comment-resolution closure |
| REQ-051-06-011 | Vendor written confirmation of fluid bulk-temperature rating | Vendor letter on file |
| REQ-051-06-014 | Vendor written confirmation of heater minimum-flow basis | Vendor letter on file |
| REQ-051-06-016, 017 | Design review + commissioning test | Pop-tank level-switch FAT/SAT; sour-rupture disposition memo |
| REQ-051-06-020 | Cold-start functional test | Test report at 15 deg C condition |
| REQ-051-06-021 | Shop seat-tightness test per API STD 527 | PSV test certificate |
| REQ-051-06-030..032 | Test record audit | MTRs, NDE, hydrotest, FAT, SAT, commissioning records |
| REQ-051-06-040..042 | Turnover package audit + signed handover certificate | Handover certificate + spare parts list + warranty + punchlist |
| REQ-051-06-050 | Traceability matrix audit | SOW-to-evidence mapping table (TBD pending source) |

## Documentation

The acceptance deliverable produces:

1. Vendor document review log (linked into DEL-051-05).
2. Package acceptance checklist (closed out).
3. Test/inspection evidence index.
4. Turnover evidence index (including handover certificate).
5. Acceptance disposition memo (human-authored).
6. Outstanding-items punchlist (carried forward to operations).
