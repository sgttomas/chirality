# Decomposition Coverage — SCA-APP-004 Post-change

**Status:** `WARNINGS`
**Authoritative input:** Gate-5 governance payload
`416b29033bbacb0bc3648d84033272b7ab4e6e11`
**Derivative purpose:** SCA-APP-004 post-change validation

## Check summary

| Check | Verdict | Evidence |
|---|---|---|
| 1 Package forward coverage | PASS | 10 declared packages; PKG-02, PKG-05, and PKG-08 declarations and folders checked |
| 2 Deliverable forward coverage | PASS | 51 unique deliverables; all 15 scoped package deliverables have folders |
| 3 Reverse folder coverage | PASS | No undeclared folder in the three scoped packages |
| 4 ID consistency | PASS | Stable package/deliverable IDs preserved; no renumbering |
| 5 Context fidelity | PASS | Six affected contexts match amended names/scope; nine scoped siblings remain aligned |
| 6 Artifact presence | WARNING | Valid SOW_V1 records exist; 15 carried folder-local anticipated-artifact warnings remain |
| 7 Objective mapping | PASS | 10 objectives; amended OBJ-001/OBJ-007 traceability resolves |
| 8 Ledger integrity | PASS | 78 SSOW rows and 78 matching Scope Ledger rows |
| 9 Derivative parity | PASS | Authority corpus v16 and six affected records reconciled |
| 9b Package shape | PASS | 10-package / 51-deliverable topology unchanged |
| 10 Active snapshot/handoff | PASS | SCA-APP-004 is the single active snapshot and contains closure artifacts |
| 11 Lifecycle distribution | PASS | All 15 scoped deliverables remain `IN_PROGRESS` |

## Amendment conformance

- The exact Woven Dialogue and Work/Agents amendment is present.
- The five supersession rows are prospective presentation supersessions only.
- `DEL-08-05` remains unchanged as the child-run record owner.
- No runtime, browser API, public SSE, dependency, lifecycle, release, or
  professional-reliance surface changed.

## Carried warnings

The 15 Check-6 warnings are identical in class and count to the Gate-1
baseline. They record that anticipated implementation artifacts are not
materialized as matching deliverable-folder files. They are expected before
the downstream implementation tranche and do not block governance closure.
