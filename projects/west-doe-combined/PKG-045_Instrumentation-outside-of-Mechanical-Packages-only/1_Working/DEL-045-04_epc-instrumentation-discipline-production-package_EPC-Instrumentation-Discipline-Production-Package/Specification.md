# Specification: DEL-045-04 — EPC / Instrumentation Discipline Production Package

## Scope

### Covers

- Production-unit basis for the **Instrumentation (outside of Mechanical Packages only)** package (`PKG-045`, Workbook row 47, WBS 03).
- Carrying scope item `SOW-0046` ("Carry the workbook-defined Instrumentation package … as a distinct flat project package for WBS 03").
- The EPC/Discipline production unit responsible for execution of non-vendor instrumentation scope, including production package basis, a TBD discipline deliverable register, and a source-limited requirements closure record. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-045-04.)

### Excludes

- Instrumentation scope embedded inside vendor Mechanical Packages — by definition of `PKG-045`. (Source: Workbook row 47; package name.)
- Field supports, power, and comms scope unless explicitly confirmed by package scope. (Source: `PACKAGE_REGISTER.csv` row PKG-045 — Exclusions/Notes.)
- Vendor-package ownership constructs not supported by source. (Source: `PACKAGE_REGISTER.csv` row PKG-045 — Notes.)

## Requirements

| Req ID | Requirement | Source / Status |
|---|---|---|
| R-1 | The production unit MUST carry `PKG-045` as a distinct flat project package under WBS 03. | `SCOPE_LEDGER.csv` SOW-0046 |
| R-2 | The production unit MUST treat the package as Instrumentation discipline scope explicitly outside any Mechanical Package. | Workbook row 47 (package name); `PACKAGE_REGISTER.csv` PKG-045 |
| R-3 | The production unit MUST plan for the physical interface types recorded for PKG-045: Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network. | `PACKAGE_REGISTER.csv` PKG-045 (Applicable Interface Types) |
| R-4 | The production unit MUST NOT include field supports, power, or comms scope unless confirmed by package scope. | `PACKAGE_REGISTER.csv` PKG-045 (Exclusions/Notes) |
| R-5 | The production unit MUST produce: (a) a discipline production package basis, (b) a discipline deliverable register (TBD content), and (c) a source-limited requirements closure record. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` DEL-045-04 |
| R-6 | The production unit MUST record items unresolved at Gate 7 and surface them for Gate 5 disposition. | `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` DEL-045-04 (Notes) |
| R-7 | The production unit MUST coordinate with companion PKG-045 deliverables: `DEL-045-01` (Scope of Work), `DEL-045-02` (Package Datasheet), `DEL-045-03` (Construction Work Package). | `SCOPE_LEDGER.csv` SOW-0046 |
| R-8 (ASSUMPTION) | Should support objectives `OBJ-002`, `OBJ-003`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-010` per package-heuristic association. | `OBJECTIVE_DELIVERABLE_MAP.csv`; package heuristic — confirmation TBD |
| R-9 (TBD) | Detailed instrumentation requirements (instrument lists, loop counts, signal types, I/O quantities, control system interfaces, hazardous-area classification, calibration scope, FAT/SAT scope, etc.) — TBD; source slices not locally available. | `_REFERENCES.md` Missing/Deferred References |

## Standards

| Standard / Code | Applicability | Status |
|---|---|---|
| TBD | Standards governing instrumentation design, installation, and test for this scope are not enumerated in the locally accessible source set. | `location TBD` — Workbook row 47 section text not locally accessible; DBM Comp_and_Liquids reference not copied locally |
| Project-internal decomposition standards | This deliverable conforms to the PROJECT_DECOMP Gate 7 snapshot. | `_REFERENCES.md` |

## Verification

| Req ID | Verification Method | Evidence |
|---|---|---|
| R-1 | Inspection — package presence as a distinct flat project package | Project register entry for PKG-045 |
| R-2 | Inspection — production-unit boundary statement excludes Mechanical Package scope | Boundary clause in production package basis |
| R-3 | Inspection — interface list in production package basis matches PKG-045 row | Cross-check against `PACKAGE_REGISTER.csv` |
| R-4 | Inspection — exclusions statement present and matches PKG-045 notes | Production package basis exclusions section |
| R-5 | Inspection — three artifacts produced and stored under the deliverable folder | Artifact presence in 1_Working/2_Review/3_Published |
| R-6 | Review — open-issues list surfaced for Gate 5 | Closure record entries + `OPEN_ISSUES.csv` cross-reference |
| R-7 | Review — coordination notes reference DEL-045-01/02/03 | Production package basis cross-reference section |
| R-8 | Human ruling — confirm or refute objective mapping | Decision record referencing OBJECTIVE_DELIVERABLE_MAP |
| R-9 | TBD — verification methods cannot be specified until requirements are sourced | TBD |

## Documentation

- `Datasheet.md` — descriptive identification and conditions
- `Specification.md` — this document (normative)
- `Guidance.md` — interpretive guidance and trade-offs
- `Procedure.md` — how to produce/operate this production unit
- Discipline production package basis (anticipated)
- Discipline deliverable register (TBD content)
- Source-limited requirements closure record
