# Chirality Root Decomposition — Coverage and Telemetry

**Package Role:** `authoritative companion register`
**Belongs to:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` (working surface)
**Revision:** v1.0 · **Date:** 2026-07-25
**Status:** CANDIDATE — every gate is `PENDING_OWNER_RULING`; nothing here is accepted.

This register is authoritative for the decomposition's counts, coverage
results, and the D-15 four-category demonstration. The working surface
summarizes; this file holds the machine truth.

---

## 1. Base telemetry (SOFTWARE_DECOMP schema)

| Metric | Value |
|---|---:|
| Revision | v1.0 (candidate) |
| Date | 2026-07-25 |
| ScopeItemCount | 103 |
| ScopeItemsIN | 94 |
| ScopeItemsOUT | 9 |
| ScopeItemsTBD | 0 |
| PackageCount | 6 |
| DeliverableCount | 45 |
| ObjectiveCount | 7 |
| UnassignedScopeItems | 0 |
| ScopeItemsWithoutDeliverableMapping | 0 |
| UnmappedObjectives | 0 |
| ContextEnvelopeCounts | S=14, M=30, L=1, XL=0 |
| PRDForwardItemCount | 84 |
| PRDItemsUncovered | 0 |
| PRDItemsDeferred | 0 |
| UnitsUntracedInReverseRegister | 0 |
| OpenIssueCount | 13 |
| ScopeLedgerRowsFlaggedOpenIssue | 12 |

`UnassignedScopeItems` is 0 as the standard requires for acceptance. `TBD`
scope items are 0 because no PRD statement in the enumerated source scope was
left unclassifiable; unresolved *content* inside classified items (for example
the unresolved referent recorded at SOW-094) is carried as an open issue on
that item, not as a `TBD` classification.

## 2. Deliverables per package

| PackageID | Deliverables |
|---|---:|
| PKG-01_Product_Definition_Normative_Basis_and_Authority | 8 |
| PKG-02_Operative_Instruction_Surface_and_Runtime_Layers | 5 |
| PKG-03_Governed_Execution_Structure_and_Root_Containment | 6 |
| PKG-04_Developmental_Machinery_and_Change_Control | 10 |
| PKG-05_Evidence_Provenance_and_Audit | 8 |
| PKG-06_Self_Application_Variants_and_Release | 8 |

## 3. Context Budget QA

| Envelope | Deliverables | QA result |
|---|---|---|
| S | DEL-01-05, DEL-01-06, DEL-01-07, DEL-01-08, DEL-02-05, DEL-03-03, DEL-04-02, DEL-04-06, DEL-04-07, DEL-05-03, DEL-05-05, DEL-05-07, DEL-06-03, DEL-06-05 | Acceptable small slices. |
| M | All deliverables not listed as S or L | Acceptable bounded Agent 2 work; each is single-package and single artifact-shape. |
| L | DEL-04-09_PRD_Source_Currency_Check_Capability | Proposed as large-but-single-domain, for owner acceptance at Gate 5/6: one checker plus one regenerable derivative package. Splittable by check class (five mechanical, four semantic) if implementation review finds churn. Recorded at OI-010. |
| XL | none | No XL deliverable is proposed. |

## 4. D-15 four-category coverage demonstration

D-15 requires the first root decomposition to demonstrate coverage across all
four §4.1 categories, each having coverage or a recorded reasoned deferral.
Categories are non-exclusive (§4.3), so a scope item may carry more than one.
Counts below are ledger-derived (`Categories` column).

| §4.1 category | Scope items carrying it | Packages participating | Deliverables participating | Coverage status |
|---|---:|---|---:|---|
| Normative basis | 41 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-05, PKG-06 | 21 | COVERED |
| Operative product | 26 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-06 | 18 | COVERED |
| Developmental machinery | 59 | PKG-01, PKG-03, PKG-04, PKG-05, PKG-06 | 25 | COVERED |
| Evidence | 18 | PKG-01, PKG-04, PKG-05, PKG-06 | 16 | COVERED |

**No category is deferred.** No reasoned deferral is therefore recorded, and
none is claimed.

**The categories are not the partition.** Every category spans four or more of
the six packages, and no package is coextensive with any category —
participation ranges from two categories (PKG-02: normative basis and
operative product) to all four (PKG-01, PKG-04, PKG-06); PKG-03 and PKG-05
participate in three each. That is the intended reading of §4.3: the
categories classify functions and authority relationships, and the partition
is a separate, work-domain judgment (DEC-003).

Per-category deliverable membership:

- **Normative basis** — DEL-01-01, DEL-01-02, DEL-01-03, DEL-01-04, DEL-01-05, DEL-01-06, DEL-01-07, DEL-01-08, DEL-02-02, DEL-02-04, DEL-02-05, DEL-03-01, DEL-03-04, DEL-04-08, DEL-04-10, DEL-05-02, DEL-05-04, DEL-06-04, DEL-06-05, DEL-06-06, DEL-06-07
- **Operative product** — DEL-01-08, DEL-02-01, DEL-02-02, DEL-02-03, DEL-02-04, DEL-02-05, DEL-03-01, DEL-03-02, DEL-03-03, DEL-03-04, DEL-03-05, DEL-03-06, DEL-04-07, DEL-04-10, DEL-06-02, DEL-06-04, DEL-06-05, DEL-06-08
- **Developmental machinery** — DEL-01-01, DEL-01-04, DEL-01-08, DEL-03-04, DEL-03-05, DEL-03-06, DEL-04-01, DEL-04-02, DEL-04-03, DEL-04-04, DEL-04-05, DEL-04-06, DEL-04-07, DEL-04-08, DEL-04-09, DEL-04-10, DEL-05-06, DEL-05-07, DEL-05-08, DEL-06-01, DEL-06-02, DEL-06-03, DEL-06-04, DEL-06-06, DEL-06-07
- **Evidence** — DEL-01-03, DEL-01-08, DEL-04-05, DEL-04-08, DEL-04-09, DEL-04-10, DEL-05-01, DEL-05-02, DEL-05-03, DEL-05-04, DEL-05-05, DEL-05-06, DEL-05-07, DEL-05-08, DEL-06-02, DEL-06-06

D-15 itself carries the source label **PROPOSED**; it is applied here as the
PRD's only coverage obligation, and its status is visible wherever it is
relied on (SOW-050).

## 5. F4 bidirectional traceability result

F4 (PROPOSED) is tripped when an accepted scope unit cannot be traced to a PRD
requirement or objective, or when a PRD requirement or objective has neither
coverage nor a recorded deferral. Both directions are computed, not asserted.

| Direction | Register | Population | Result |
|---|---|---:|---|
| PRD item → decomposition | `chirality_root_prd_coverage_forward_v1_0.csv` | 84 | 84 COVERED, 0 DEFERRED, 0 UNCOVERED |
| decomposition unit → PRD | `chirality_root_trace_reverse_v1_0.csv` | 51 (6 packages + 45 deliverables) | 51 TRACED, 0 UNTRACED |

Forward population (84 items): OBJ-1..OBJ-7 (7); N-1..N-9 (9); O-1..O-10 (10);
D-1, D-2, D-4..D-16 (15); E-1..E-8 (8); the §3 v1 boundary and objective
discipline (2); §4.1 categories, §4.2 loop, §4.2 three judgments, §4.3
non-prescription (4); §5 registry discipline (1); §6.1, §6.2 discipline, §6.2
practice statement, §6.3 concurrency (4); §7.1 downward, §7.2 promotion (2);
§8.1 non-goals (1); F1..F6 (6); §8.3 release authority (1); RD-1..RD-5 (5);
§9.1 obligations (a), (b), (c) (3); §10.1 annex (1); C-1..C-4 (4); §10.3
adoption mechanics (1). `D-3` is deliberately absent and never reassigned
(PRD §5.3).

Reverse trace resolves through scope items where a deliverable covers them and
through `SupportsObjectives` where a deliverable exists to satisfy an
objective's success condition — the F4 wording is "a PRD requirement **or**
objective". `DEL-05-08_Evidence_Linkage_Completeness_and_Retrieval_Evaluation`
is the one deliverable that is objective-derived first (OBJ-3); it also covers
SOW-009 (DEC-010).

**This is a candidate result over a candidate decomposition.** F4 speaks to
*accepted* scope units; nothing here is accepted, so the result is evidence
offered to the gate, not a closure claim.

## 6. Open issues by type

| Type | Count | IDs |
|---|---:|---|
| SOURCE_CURRENCY | 2 | OI-001, OI-002 |
| FRAMING_STRAIN | 3 | OI-003, OI-004, OI-012 |
| UNBUILT_CAPABILITY | 1 | OI-005 |
| OWNER_RULING_PENDING | 1 | OI-006 |
| PARTITION_BOUNDARY | 1 | OI-007 |
| GATE_SEQUENCING | 1 | OI-008 |
| SCOPE_TBD | 1 | OI-009 |
| CONTEXT_ENVELOPE | 1 | OI-010 |
| RESPONSIBILITY_UNASSIGNED | 1 | OI-011 |
| OBJECTIVE_GRANULARITY | 1 | OI-013 |

Twelve ledger rows carry `OpenIssue = TRUE`, and they partition as follows:
OI-001 (source currency of the discharged obligations and conflicts) — SOW-060,
SOW-089, SOW-090, SOW-091, SOW-098, SOW-099, SOW-100, SOW-101 (8); OI-002
(PROPOSED label status) — SOW-085, SOW-102 (2); OI-005 (unbuilt currency
check) — SOW-049 (1); OI-009 (unresolved referent) — SOW-094 (1). The
remaining open issues are package-level rather than row-level and carry no
ledger flag; **OI-013 is objective-level** — it concerns a condition inside
OBJ-2 for which no scope item exists, which is precisely why it has no ledger
row to flag. Full per-row flags are the `OpenIssue` column of the scope
ledger.

## 7. Companion register inventory

| File | Package role | Authoritative for |
|---|---|---|
| `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | working surface | Control surface: gates, references, partition, deliverable topology, decisions, open issues |
| `chirality_root_scope_ledger_v1_0.csv` | authoritative companion register | Scope item rows: statement, status, source ref, package, deliverables, objectives, PRD item, categories |
| `chirality_root_deliverable_register_v1_0.csv` | authoritative companion register | Full deliverable fields including descriptions, artifacts, covered scope items, envelope notes, write locus |
| `chirality_root_objective_register_v1_0.csv` | authoritative companion register | Objective rows and their deliverable/scope-item mappings |
| `chirality_root_prd_coverage_forward_v1_0.csv` | authoritative companion register | F4 forward direction: every PRD item's coverage or deferral |
| `chirality_root_trace_reverse_v1_0.csv` | authoritative companion register | F4 reverse direction: every package and deliverable's PRD trace |
| `chirality_root_coverage_telemetry_v1_0.md` | authoritative companion register | This file: counts, context budget QA, D-15 demonstration, F4 result, open-issue taxonomy |

No derived publication artifact is produced by this run.
