# Dependencies: DEL-073-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` on 2026-05-25.

**Total ACTIVE rows: 16**
- ANCHOR rows: 5 (1 × IMPLEMENTS_NODE, 4 × TRACES_TO_REQUIREMENT)
- EXECUTION rows: 11 (2 × PREREQUISITE upstream deliverables, 1 × PREREQUISITE document, 2 × HANDOVER downstream, 2 × CONSTRAINT upstream external, 4 × INTERFACE)

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetName | Confidence |
|---|---|---|---|---|---|---|---|
| DEP-073-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-073 — Amine Treating Unit | HIGH |
| DEP-073-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0051 | HIGH |
| DEP-073-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0052 | HIGH |
| DEP-073-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0053 | HIGH |
| DEP-073-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0054 | HIGH |
| DEP-073-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-073-01 Scope of Work | HIGH |
| DEP-073-04-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-073-02 Package Datasheet | HIGH |
| DEP-073-04-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM SEC-06 — Amine Treating Basis | HIGH |
| DEP-073-04-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-073-05 Vendor Document Turnover Package | HIGH |
| DEP-073-04-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-073-06 EPC Vendor Package Review and Acceptance | HIGH |
| DEP-073-04-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | Inlet HP sour gas from inlet-service compressor aftercooler (R-4.1) | HIGH |
| DEP-073-04-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | EXTERNAL | Sweet gas outlet to TEG inlet (R-4.2) | HIGH |
| DEP-073-04-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | EXTERNAL | Amine flash gas to SOC first-stage suction (R-4.3) | HIGH |
| DEP-073-04-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | EXTERNAL | Acid gas overheads to acid-gas compressor first-stage suction scrubber (R-4.4) | HIGH |
| DEP-073-04-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | Heat medium supply 350 °F hot oil to amine reboiler (R-4.6) | HIGH |
| DEP-073-04-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | LP fuel gas supply — surge tank blanket / regenerator blanket / sour-filter purge (R-4.7) | HIGH |

## Run Notes

**Run date:** 2026-05-25
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Consumer context:** NONE

**Defaults applied:**
- `SOURCE_DOCS=AUTO` — scanned deliverable folder: Datasheet.md, Procedure.md, Specification.md, Guidance.md, _CONTEXT.md, _REFERENCES.md
- `ANCHOR_DOC=AUTO` — Datasheet.md selected as highest-confidence anchor doc (contains "datasheet" in name; explicit DeliverableID and ParentPackageID fields)
- `EXECUTION_DOC_ORDER=AUTO` — Procedure.md (primary execution signal), Specification.md (R-4 interfaces), Guidance.md (conflict table; supporting context)
- `DECOMPOSITION_PATH` — resolved to `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` per `_CONTEXT.md` Decomposition Reference

**Anchor validation:** PKG-073 confirmed in PACKAGE_REGISTER.csv (GATE-07 snapshot). SOW-0051–SOW-0054 confirmed in SCOPE_LEDGER.csv with explicit mapping to DEL-073-04.

**Decomposition confirmation:** DELIVERABLE_REGISTER row confirms DEL-073-04_vendor-engineered-equipment-package with ParentPackageID=PKG-073.

**Unresolved targets (TargetType=EXTERNAL):** Interface targets R-4.1 (inlet-service compressor), R-4.2 (TEG dehydration package), R-4.3 (SOC compressor package), R-4.4 (acid-gas compressor package), R-4.6 (heat-medium generation package), R-4.7 (LP fuel gas source) — upstream package DEL IDs not resolved from accessible sources. Recorded as EXTERNAL per CONSERVATIVE strictness.

**Document not parseable:** `26020-Package_Requirements.docx` heading 27 referenced by `_CONTEXT.md` and decomposition row but is a binary file not locally accessible. Source for R-4 interfaces, Standards table, and some scope items was DBM-Deepcut SEC-06 and SCOPE_LEDGER. Items requiring heading-27 confirmation remain marked `location TBD` in source documents.

**[WARNING] MISSING_DECOMPOSITION_DOC:** `DECOMPOSITION_PATH` resolves to the snapshot folder. `PROJECT_DECOMP.md` and CSV registers were read from snapshot; no single markdown decomposition file was unavailable — warning not applicable. PACKAGE_REGISTER and DELIVERABLE_REGISTER confirmed.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 16 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 16 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (confirmed). Source docs: Datasheet.md, Procedure.md, Specification.md, Guidance.md. 16 ACTIVE rows created (5 ANCHOR, 11 EXECUTION). Schema validated VALID. No prior rows retired (first extraction run).
