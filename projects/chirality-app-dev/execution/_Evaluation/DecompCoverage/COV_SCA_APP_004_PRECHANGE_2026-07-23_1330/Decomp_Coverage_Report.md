# Decomposition Coverage — SCA-APP-004 Pre-change

**Status:** `WARNINGS`  
**Authoritative input:** accepted v3.2 decomposition at
`3c9ff297a4037d509bc930d1f607daf56769804d`  
**Derivative purpose:** SCA-APP-004 Gate-1 baseline

## Check summary

| Check | Verdict | Evidence |
|---|---|---|
| 1 Package forward coverage | PASS | PKG-02, PKG-05, and PKG-08 declarations and folders |
| 2 Deliverable forward coverage | PASS | All 15 declared package deliverables have folders |
| 3 Reverse folder coverage | PASS | No undeclared folder in the three packages |
| 4 ID consistency | PASS | Package/deliverable prefixes match declarations |
| 5 Context fidelity | PASS | 15 contexts match name, package, type, responsible party, description, and envelope |
| 6 Artifact presence | WARNING | Valid SOW_V1 in every folder; named implementation artifacts are not matching folder-local files |
| 7 Objective mapping | PASS | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, and OBJ-008 have existing mapped deliverables |
| 8 Ledger integrity | PASS | In-scope ledger rows reference declared packages and deliverables |
| 9 Derivative parity | SKIPPED | Not variant-owned for SOFTWARE |
| 9b Package shape | PASS | Main file labels itself authoritative and §2.2 identifies companion-register role |
| 10 Active snapshot/handoff | PASS | SCA-APP-003 pointer resolves uniquely to a complete, accepted closure state |
| 11 Lifecycle distribution | PASS | All 15 scoped deliverables are `IN_PROGRESS` |

## Affected baseline

The eight named deliverables are structurally present and faithfully described.
Their accepted semantics explicitly bind the current shell/matrix,
Workbench/Pipeline presentation, local state, runtime replay, persona/matrix
routing, and pipeline dispatch. Any semantic replacement therefore requires
SCOPE_CHANGE; this audit does not authorize or design that amendment.

## What to fix for a cleaner rerun

Decide whether software implementation evidence outside deliverable folders
should be linked through explicit deliverable-local artifact indexes. Until
then, retain Check-6 warnings rather than inferring artifact ownership.
