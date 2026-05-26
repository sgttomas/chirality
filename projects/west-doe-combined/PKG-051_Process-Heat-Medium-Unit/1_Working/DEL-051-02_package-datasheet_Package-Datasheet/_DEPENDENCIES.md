# Dependencies: DEL-051-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` (v3.1) is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Extracted from source documents on 2026-05-25. Total ACTIVE rows: 11.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-051-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-051 — Process Heat Medium Unit | HIGH | ACTIVE |
| DEP-051-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0165 | HIGH | ACTIVE |
| DEP-051-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0166 | HIGH | ACTIVE |
| DEP-051-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0167 | HIGH | ACTIVE |
| DEP-051-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0168 | HIGH | ACTIVE |
| DEP-051-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 26020-Package_Requirements.docx | HIGH | ACTIVE |
| DEP-051-02-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 26020-Packages_Interfaces_4_export.xlsx | HIGH | ACTIVE |
| DEP-051-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07 decomposition snapshot | HIGH | ACTIVE |
| DEP-051-02-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-051-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-051-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-051-06_epc-vendor-package-review-and-acceptance | MEDIUM | ACTIVE |
| DEP-051-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-051-01_scope-of-work | MEDIUM | ACTIVE |

**Counts:** ANCHOR = 5 (1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT) | EXECUTION = 6 (3 UPSTREAM, 2 DOWNSTREAM HANDOVER, 1 UPSTREAM INTERFACE) | RETIRED = 0

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents found: `Datasheet.md`, `Specification.md`, `Procedure.md`, `Guidance.md`, `_CONTEXT.md`, `_REFERENCES.md`.
- **ANCHOR_DOC:** `Datasheet.md` (filename contains "datasheet" — highest confidence ANCHOR_DOC per DEFAULT heuristic).
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary; contains "procedure"), `Specification.md` (secondary), `Guidance.md` (tertiary).
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — auto-discovered from `_CONTEXT.md` and `_REFERENCES.md`; GATE-07 snapshot confirmed present. (Note: invoker provided `DECOMPOSITION_PATH: /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` which does not exist; resolved to correct path from `_CONTEXT.md`.)
- **Anchor validation:** PKG-051 confirmed in PACKAGE_REGISTER.csv. DEL-051-02_package-datasheet confirmed in DELIVERABLE_REGISTER.csv. SOW-0165, SOW-0166, SOW-0167, SOW-0168 confirmed in SCOPE_LEDGER.csv with DEL-051-02_package-datasheet listed as covered deliverable.
- **Target resolution:** DEL-051-01, DEL-051-04, DEL-051-06 confirmed in DELIVERABLE_REGISTER.csv.
- **Parent anchor count:** 1 (DEP-051-02-001 — IMPLEMENTS_NODE to PKG-051). No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- **Interface scope note (CONSERVATIVE):** The 10 interface types declared applicable in the xlsx row (Utility Piping, Drain/Containment, Electrical Power, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Building HVAC/Services, Fire & Gas/Safety Systems, Maintenance Access, Structural/Foundations/Supports) are recorded in Datasheet.md as package interface declarations. Under CONSERVATIVE strictness, no EXECUTION dependency rows are emitted for these interfaces because the source does not name specific target deliverables or packages for information/artifact transfer — only declares the interface types as applicable. A future AGGRESSIVE run or explicit interface coordination effort may produce EXECUTION rows referencing specific discipline packages once target deliverables are identified.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 11 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 11 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07 snapshot (auto-resolved). Source docs: AUTO. 11 ACTIVE rows extracted (5 ANCHOR, 6 EXECUTION). Schema validated VALID. Row count: 11.
