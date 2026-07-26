# Run Summary

**RUN_STATUS:** `WARNINGS`

**Requested by:** `SCOPE_CHANGE` (SCA-002, Gate 1)
**Expected handoff phase:** `SCOPE_CHANGE_GATE_1`
**Authoritative input pointer:** `projects/pec/execution/_Decomposition/_LATEST.md`
**Expected source snapshot:** `SOFTWARE_DECOMP.md` revision **1.1** (`current_basis`)
**Scope:** `ALL` (11 packages / 64 deliverables)

## Headline

This is the **first `AUDIT_DECOMP` run against PEC that could measure
filesystem coverage.** SCA-001's Gate 1 and Gate 5 baselines both returned
the contract-required `FAILED_INPUTS` because zero deliverable folders
existed before Project Setup. The `D-PEC-62` scaffold has since landed
**11 package folders and 64 deliverable folders**, so Step 0's precondition
now passes and all 12 checks executed.

| Metric | Value |
|---|---|
| Packages declared / found | 11 / 11 (100.0%) |
| Deliverables declared / found | 64 / 64 (100.0%) |
| Reverse coverage | 100.0% (no orphan folders) |
| Context fidelity | 100.0% (64/64 `_CONTEXT.md` match `Deliverables.csv`) |
| Objective coverage | 100.0% (6/6 objectives have active supporting deliverables) |
| Lifecycle distribution | `OPEN` 64 |
| Blockers / Warnings / Info | **0 / 1 / 90** |
| Overall status | `WARNINGS` |
| Closure readiness | `WARN` |

## Check results

| # | Check | Verdict | Note |
|---|---|---|---|
| 1 | Forward coverage — Packages | `PASS` | 11/11 declared packages have folders |
| 2 | Forward coverage — Deliverables | `PASS` | 64/64 declared deliverables have folders |
| 3 | Reverse coverage — Folders | `PASS` | every folder traces to a §5 declaration |
| 4 | ID consistency | `PASS` | `DEL-XX-YY` prefix couples to parent `PKG-XX` for all 64 |
| 5 | Context fidelity | `PASS` | Name / PackageID / Type / ResponsibleParty / ContextEnvelope / CoversScopeItems / SupportsObjectives all match the register for 64/64 |
| 6 | Artifact presence | `INFO` (64) | Expected: all 64 are `OPEN`; no production artifacts exist yet |
| 7 | Objective mapping | `PASS` + `INFO` (26) | No objective is unsupported; 26 deliverables carry no `SupportsObjectives` — SCA-002's subject matter |
| 8 | Ledger integrity | `PASS` | every `IN` row's `PackageID` and `DeliverableIDs` resolve |
| 9 | Derivative package parity | `SKIPPED` | not variant-owned by this audit (`DECOMP_VARIANT != DOMAIN`) |
| 9b | Package-shape conformance | `WARN` | one stale duplicated count — see Finding W-1 |
| 10 | Active snapshot / handoff state | `PASS` | `_ScopeChange/_LATEST.md` names exactly one snapshot (`SCA-001_2026-07-24_2206`), which carries the full required artifact set |
| 11 | Lifecycle distribution | `PASS` (informational) | 64 `OPEN`; no unrecognized state |
| 12 | Comparison mode | `PARTIAL` | see §Comparison |

## Findings

### W-1 (`WARNING`, Check 9b.2) — stale duplicated envelope count in §5

`SOFTWARE_DECOMP.md` §5 (line 376) states:

> Context Envelope posture: **29 S / 33 M / 2 L / 0 XL.**

`Deliverables.csv` yields **28 S / 34 M / 2 L / 0 XL**, and §7 Coverage &
Telemetry (`ContextEnvelopeCounts`) states **S 28 / M 34 / L 2 / XL 0**.

`SCA-001` action seq 3 re-enveloped `DEL-10-10` from `S` to `M`
(`Amendment_Actions.csv`; `DL-16`; revision-history row 1.1). It reconciled
`Deliverables.csv`, `ContextBudgetQA.csv`, and the §7 telemetry table, but
**did not update the §5 prose count**, which still carries the pre-SCA-001
value. `D-PEC-64` §4.1's stated invariant (`S 28 / M 34 / L 2 / XL 0`)
agrees with the registers and §7, not with §5.

This is a residual reconciliation miss inside accepted revision 1.1. It is a
**documentation-consistency defect, not a topology defect** — no count of
packages, deliverables, scope items, or objectives is affected, and the
authoritative register is correct. It is **outside SCA-002's declared
change class** (`MODIFY`, deliverable→objective mapping). It is recorded
here and escalated to the owner rather than corrected, because Gate 1 has no
write authority over decomposition truth.

### Expected `INFO` classes (not defects)

- **Check 6 (64 rows).** Every deliverable declares an `AnticipatedArtifacts`
  set and none has produced it. All 64 are `OPEN`; production begins with the
  D-PEC-63 wave. `artifact_presence_pct = 0.0` is the correct pre-production
  reading, not a coverage regression.
- **Check 7 (26 rows).** The 26 deliverables with empty `SupportsObjectives`
  are precisely SCA-002's subject matter. They are logged as `INFO` so the
  post-change baseline can measure the delta directly.

## Deliverable-contract resolution (Check 6 detail)

All 64 deliverable folders resolve uniformly to the transitional
**`LEGACY_FOUR_DOC`** contract: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`,
`_DEPENDENCIES.md` present in 64/64, plus `Dependencies.csv` and `_SEMANTIC.md`.
Zero folders carry `ScopeOfWork.md`. There is **no `MIGRATION_DUAL` ambiguity**
and no fail-closed state — the SOW_V1 contract arrives with the D-PEC-63 wave,
which is exactly what SCA-002 unblocks.

## Comparison (Check 12)

| Metric | `COV_SCA001_PRECHANGE` | `COV_SCA001_POSTCHANGE` | This run |
|---|---|---|---|
| `RUN_STATUS` | `FAILED_INPUTS` | `FAILED_INPUTS` | `WARNINGS` |
| Deliverable folders discoverable | 0 | 0 | 64 |
| Checks executed | 0 (Step 0 return) | 0 (Step 0 return) | 12 |

No per-check delta is computable: the prior runs produced no
`coverage_summary.json` (the precondition-failure branch suppresses it). This
run is therefore a **new baseline**, not a regression comparison. The
improvement — filesystem coverage becoming measurable at 100% forward and
reverse — is attributable to `D-PEC-62`, not to any SCA-002 act.

## Assessment for SCA-002 Gate 1: expected vs anomalous

- **Expected.** The transition from `FAILED_INPUTS` to a fully-executing
  12-check run; 100% forward/reverse coverage; 64 `OPEN`; `artifact_presence`
  at 0%; 26 unmapped deliverables and 31 unmapped `IN` ledger rows.
- **Anomalous.** Exactly one item — Finding **W-1**. It predates SCA-002 and
  belongs to revision 1.1's reconciliation, not to this amendment.

**No blocker prevents SCA-002 from proceeding to the Gate 1 owner ruling.**

## Write discipline

No decomposition document, companion register, `_CONTEXT.md`, `_STATUS.md`,
`Dependencies.csv`, coordination surface, or deliverable file was modified.
Writes are confined to this snapshot folder and
`_Evaluation/DecompCoverage/_LATEST.md` (pointer-only overwrite, permitted by
the `AUDIT_DECOMP` contract and in-fence under `D-PEC-64` §3.2).
