# Dependencies: DEL-034-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

Produced by `dependency-extract` run on 2026-05-25 (MODE=UPDATE, STRICTNESS=CONSERVATIVE).

**Total rows: 9 | ACTIVE: 9 | RETIRED: 0**

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetName | SatisfactionStatus | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-034-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-034 — 600V ELECTRICAL BUILDING (820-2) | TBD | HIGH |
| DEP-034-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0035 | TBD | HIGH |
| DEP-034-04-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-034-01_scope-of-work | PENDING | HIGH |
| DEP-034-04-004 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-034-02_package-datasheet | PENDING | HIGH |
| DEP-034-04-005 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Accepted electrical studies (load-flow; short-circuit; relay coordination; arc-flash) | PENDING | MEDIUM |
| DEP-034-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 26020-Package_Requirements.docx | PENDING | MEDIUM |
| DEP-034-04-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-034-05_vendor-document-turnover-package | TBD | HIGH |
| DEP-034-04-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-034-06_epc-vendor-package-review-and-acceptance | TBD | HIGH |
| DEP-034-04-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-034-03_construction-work-package | TBD | HIGH |

---

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents used: `Datasheet.md` (ANCHOR_DOC), `Procedure.md`, `Specification.md`, `Guidance.md`, `_CONTEXT.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — USED for anchor validation and label resolution
- **Anchor validation:** DEP-034-04-001 (PKG-034) confirmed in PACKAGE_REGISTER.csv row 36. DEP-034-04-002 (SOW-0035) stated in DELIVERABLE_REGISTER.csv row 189.
- **Pass 1 (ANCHOR):** One parent anchor (IMPLEMENTS_NODE to PKG-034) and one trace anchor (TRACES_TO_REQUIREMENT to SOW-0035) emitted. No WARNING FLOATING_NODE or AMBIGUOUS_ANCHOR.
- **Pass 2 (EXECUTION):** Four UPSTREAM edges extracted (DEL-034-01, DEL-034-02, electrical studies, 26020-Package_Requirements.docx) and three DOWNSTREAM edges (DEL-034-05, DEL-034-06, DEL-034-03).
- **Open items carried forward:** HRR-034-04-001 (Building 820-2 designator TBD), HRR-034-04-002 (LV equipment quantity allocation TBD), HRR-034-04-003 (code editions TBD pending 26020-Package_Requirements.docx extraction), HRR-034-04-004 (DEL-034-01 and DEL-034-02 not yet drafted).
- **Assumption on electrical studies:** No stable document ID available; recorded as TargetType=DOCUMENT with TargetRefID=TBD per conservative policy.
- **No CONSUMER_CONTEXT** — `EstimateImpactClass` and `ConsumerHint` extension columns not populated this run.

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 9 |
| RETIRED | 0 |
| **Total** | **9** |

**SatisfactionStatus breakdown (ACTIVE rows):**

| SatisfactionStatus | Count |
|---|---|
| PENDING | 4 |
| TBD | 5 |

**DependencyClass breakdown:**

| Class | Count |
|---|---|
| ANCHOR | 2 |
| EXECUTION | 7 |

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition used: GATE-07_Final_Published_2026-05-24. 9 rows written (9 ACTIVE, 0 RETIRED). Schema validation: VALID. No FLOATING_NODE, no AMBIGUOUS_ANCHOR warnings.
