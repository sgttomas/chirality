# Dependencies: DEL-096-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill, UPDATE run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1 schema); this file is the human-readable view and index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Run produced **16 ACTIVE rows** across two passes (ANCHOR + EXECUTION). No rows retired. No prior register existed; all rows are new.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-096-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-096 | Tanks, Sour Condendate (API 650) | HIGH | ACTIVE |
| DEP-096-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0217 | Carry PKG-096 as distinct flat package WBS 03 | HIGH | ACTIVE |
| DEP-096-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0218 | Basic scope: 2×3800 bbl Sour Inlet Condensate Tanks | HIGH | ACTIVE |
| DEP-096-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0219 | Major included equipment incl. PVRV EPRV VRU connection | HIGH | ACTIVE |
| DEP-096-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0220 | Scope notes: foundations by others; design −40 °C / 60 °C | HIGH | ACTIVE |
| DEP-096-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Governed Liquids Hub DBM | HIGH | ACTIVE |
| DEP-096-02-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 PROJECT_DECOMP Snapshot | HIGH | ACTIVE |
| DEP-096-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | — | Final Tank Register (supersedes DBM count if issued) | HIGH | ACTIVE |
| DEP-096-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | 26020-Package_Requirements.docx heading 48 | HIGH | ACTIVE |
| DEP-096-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | VRU Header Design Basis | MEDIUM | ACTIVE |
| DEP-096-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | — | API 650 (Welded Tanks for Oil Storage) | HIGH | ACTIVE |
| DEP-096-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-096-01_scope-of-work | Scope of Work | MEDIUM | ACTIVE |
| DEP-096-02-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-096-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-096-02-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | UNKNOWN | — | VRU Suction Header (facility VRU equipment) | HIGH | ACTIVE |
| DEP-096-02-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | UNKNOWN | — | Sour Condensate Booster Pump Suction Header | HIGH | ACTIVE |
| DEP-096-02-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | UNKNOWN | — | Facility Receiving Piping from 04-25 and future third-party | HIGH | ACTIVE |

**Totals:** 16 ACTIVE, 0 RETIRED. ANCHOR rows: 5. EXECUTION rows: 11.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE | 16 |
| RETIRED | 0 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 4 |
| EXECUTION / UPSTREAM | 8 |
| EXECUTION / DOWNSTREAM | 3 |
| SatisfactionStatus = TBD | 12 |
| SatisfactionStatus = PENDING | 3 |
| SatisfactionStatus = SATISFIED | 1 |

## Run Notes

- **Run date:** 2026-05-26
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned all documents in deliverable folder: `Datasheet.md` (ANCHOR_DOC, matches `datasheet` heuristic), `Specification.md`, `Guidance.md`, `Procedure.md` (EXECUTION_DOCS). `_CONTEXT.md` and `_REFERENCES.md` read as read-only inputs per skill read boundary.
- **ANCHOR_DOC chosen:** `Datasheet.md` — highest-confidence ANCHOR_DOC match (`datasheet` in filename per DEFAULT DOC_ROLE_MAP heuristic).
- **EXECUTION_DOC_ORDER chosen:** `Procedure.md` (strongest workflow signal), `Specification.md`, `Guidance.md`, `Datasheet.md` (residual).
- **DECOMPOSITION_PATH resolved:** GATE-07_Final_Published_2026-05-24 provided path in brief did not exist at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/`. Resolved via `_REFERENCES.md` (line 5) to `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — confirmed present. Used `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `PACKAGE_REGISTER.csv` from this snapshot for anchor validation and label resolution.
- **Decomposition validation:** PKG-096 confirmed in PACKAGE_REGISTER.csv. DEL-096-02_package-datasheet confirmed in DELIVERABLE_REGISTER.csv. SOW-0217, SOW-0218, SOW-0219, SOW-0220 confirmed in SCOPE_LEDGER.csv.
- **Parent anchor (IMPLEMENTS_NODE):** PKG-096 is the confirmed parent package node. One IMPLEMENTS_NODE row emitted (DEP-096-02-001). No FLOATING_NODE warning; no AMBIGUOUS_ANCHOR warning.
- **Trace anchors:** 4 SOW items (SOW-0217 through SOW-0220) confirmed in SCOPE_LEDGER.csv and in `_CONTEXT.md § Covers Scope Items`. All emitted as TRACES_TO_REQUIREMENT rows.
- **Objectives not anchored separately:** OBJ-002 through OBJ-010 are listed in `_CONTEXT.md § Supports Objectives`. These are objective relationships, not deliverable-scope trace anchors; they are implicitly captured by the SOW trace anchors. CONSERVATIVE strictness applied — no additional ANCHOR rows emitted for objectives.
- **EXECUTION rows — scope note:** DEP-096-02-008 (Final Tank Register) has `SatisfactionStatus=PENDING` because the register has not yet been issued at draft time (per CT-03 and Procedure Step 2.2). DEP-096-02-009 (26020-Package_Requirements.docx) also PENDING because the source is inaccessible (CT-05).
- **Interface targets (TargetType=UNKNOWN):** VRU equipment, booster pumps, and receiving piping are facility equipment items and piping systems, not deliverables with stable IDs. Recorded as UNKNOWN per conservative resolution rule.
- **No extension columns populated:** CONSUMER_CONTEXT=NONE; EstimateImpactClass and ConsumerHint omitted.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. SOURCE_DOCS=AUTO. Decomposition resolved via _REFERENCES.md to GATE-07_Final_Published_2026-05-24. Produced 16 ACTIVE rows (5 ANCHOR, 11 EXECUTION). Schema validated. No warnings: parent anchor present, decomposition resolved.
