# Decomposition Coverage Report — SCA-002 pre-change baseline

**Variant:** `SOFTWARE` · **Basis:** `SOFTWARE_DECOMP.md` revision 1.1
(`current_basis`) · **Scope:** `ALL` · **Status:** `WARNINGS`
(0 blockers / 1 warning / 90 info)

---

## 1. Forward Coverage — Packages · `PASS`

All 11 declared packages (`PKG-00`..`PKG-10`, §4) have matching folders under
`projects/pec/execution/`. Forward coverage **100.0%**.

## 2. Forward Coverage — Deliverables · `PASS`

All 64 declared deliverables (§5, across 11 `### PKG-XX` subsections) have
matching folders at `PKG-XX_*/1_Working/DEL-XX-YY_*/`. Forward coverage
**100.0%**.

This is the first PEC run where this check produced a number. SCA-001's two
baselines returned `FAILED_INPUTS` at Step 0 with zero discoverable folders.

## 3. Reverse Coverage — Folders · `PASS`

All 64 discovered deliverable folders and all 11 package folders trace to a
declaration. No orphan folder exists. Reverse coverage **100.0%**.

## 4. ID Consistency · `PASS`

For all 64 matched pairs, the folder-derived `PKG-XX` parent equals the
decomposition's declared `PackageID`, and each `DEL-XX-YY` prefix couples to
its parent package. `SOFTWARE_DECOMP` IDs carry no descriptive suffix in the
register, so comparison is direct against the folder-name prefix.

## 5. Context Fidelity · `PASS`

64/64 `_CONTEXT.md` files present and field-consistent with `Deliverables.csv`
across all seven compared fields: `Canonical name`, `PackageID`, `Type`,
`ResponsibleParty`, `ContextEnvelope` (the `SOFTWARE`-specific field),
`CoversScopeItems`, and `SupportsObjectives`. Context fidelity **100.0%**.

Note for SCA-002 Gate 2: the 26 deliverables with empty register
`SupportsObjectives` carry the literal placeholder
`(none mapped — see §3 mapping notes)` in `_CONTEXT.md`, which the comparison
correctly reads as the empty objective set. Any Gate 3 mapping change makes
those lines stale — they are the `_CONTEXT.md` line class (i) named in
`D-PEC-64` §3.2.

## 6. Artifact Presence · `INFO` ×64

No deliverable has produced its anticipated artifacts. All 64 are `OPEN`;
production has not begun. The protocol escalates to `WARNING` only at
`IN_PROGRESS` or later, so this remains informational.

**Deliverable-contract resolution:** 64/64 resolve uniformly to the
transitional `LEGACY_FOUR_DOC` contract (`_CONTEXT.md`, `_STATUS.md`,
`_REFERENCES.md`, `_DEPENDENCIES.md`, plus `Dependencies.csv` and
`_SEMANTIC.md`). Zero `ScopeOfWork.md`. No `MIGRATION_DUAL` ambiguity, no
fail-closed invalid state.

## 7. Objective Mapping · `PASS` + `INFO` ×26

All 6 objectives (`OBJ-001`..`OBJ-006`, resolved from the ledger
`ObjectiveIDs` column per the `SOFTWARE` binding) have at least one supporting
deliverable whose folder exists. No objective is supported only by `RETIRED`
units. Objective coverage **100.0%**.

**Objective-evidence integrity: `PASS`.** The §3 objective-side view
(`MappedDeliverables`) and the `Deliverables.csv` deliverable-side view agree
exactly for all six objectives once §3's range notation is expanded
(Decision_Log D-5):

| Objective | §3 view | Register-derived | Agreement |
|---|---|---|---|
| OBJ-001 | 9 | 9 | `MATCH` |
| OBJ-002 | 4 | 4 | `MATCH` |
| OBJ-003 | 12 | 12 | `MATCH` |
| OBJ-004 | 9 | 9 | `MATCH` |
| OBJ-005 | 2 | 2 | `MATCH` |
| OBJ-006 | 9 | 9 | `MATCH` |

**26 `INFO` rows** record deliverables with no `SupportsObjectives` mapping.
This is SCA-002's subject matter, logged so the post-change baseline measures
the delta directly. It is *not* an unmapped-objective condition — every
objective is supported; it is unmapped **deliverables**, which this check
surfaces but does not fail on.

## 8. Ledger Integrity · `PASS`

For all 71 `IN` rows in `ScopeLedger.csv`: `PackageID` resolves to a declared
package, and every `DeliverableIDs` token resolves to a declared deliverable.
No dangling reference. 14 `OUT` + 9 `TBD` rows carry no package/deliverable by
design and are excluded per the protocol.

## 9. Derivative Package Parity · `SKIPPED`

Not variant-owned by this audit (`DECOMP_VARIANT != DOMAIN`).

## 9b. Package-Shape Conformance · `WARN`

1. **Package-role labeling — `PASS`.** The document carries an explicit
   `## Companion Inventory` section mirrored machine-readably in
   `Companion_Inventory.csv`; the front matter declares
   `package_role: working_surface` and a package-role note block.
2. **Monolithic duplication — `WARN`.** See Finding **W-1** below.
3. **Derived artifact authority confusion — `PASS`.** No derived monolithic
   render is being treated as the amendment surface. `D-PEC-64` §3.2 correctly
   targets the working surface plus authoritative companion registers.
4. **Package-role discoverability — `PASS`.** Every companion file carries an
   explicit `PackageRole` in both the inventory table and the CSV mirror.

### Finding W-1 — `WARNING`

`SOFTWARE_DECOMP.md` §5 (line 376) states **29 S / 33 M / 2 L / 0 XL**.
`Deliverables.csv` yields **28 S / 34 M / 2 L / 0 XL**; §7's
`ContextEnvelopeCounts` states **S 28 / M 34 / L 2 / XL 0**.

`SCA-001` action seq 3 re-enveloped `DEL-10-10` `S`→`M` and reconciled
`Deliverables.csv`, `ContextBudgetQA.csv`, and §7 — but not the §5 prose
count, which retains the pre-amendment value. `D-PEC-64` §4.1's invariant
agrees with the registers and §7.

Impact is documentation consistency only: the authoritative register is
correct, no topology count is affected, and the two `L` deliverables named in
the same §5 sentence (`DEL-02-03`, `DEL-01-01`) are still accurate. It is a
residual reconciliation miss inside accepted revision 1.1, outside SCA-002's
declared change class, escalated to the owner rather than corrected.

## 10. Active Snapshot and Handoff State · `PASS`

`_ScopeChange/_LATEST.md` names exactly one active snapshot,
`SCA-001_2026-07-24_2206`, which exists and carries the full required
artifact set (`Brief.md`, `Impact_Assessment.md`, `Propagation_Plan.md`,
`Amendment_Actions.csv`, `Pre_Change_Coverage.json`,
`Post_Change_Coverage.json`, `Decision_Log.md`, `Handoff_State.md`,
`RUN_SUMMARY.md`, plus `Amendment_Preview.md` and `Supersession_Map.csv`).

Its claimed state (`AuditState: WARNINGS`, `ReadyForNextPhase: REGEN_ONLY`,
`ClosureVerdict: CLOSED_FOR_SCOPE_CHANGE_ONLY`) does not overstate what the
evidence supports. The pointer still naming SCA-001 during SCA-002 Gates 1–4
is correct by design (`D-PEC-64` §2.4).

## 11. Lifecycle Distribution · `PASS` (informational)

| State | Count |
|---|---|
| `OPEN` | 64 |

No unrecognized state. Consistent with the `D-PEC-64` §4.4 census expectation
(`64 OPEN`).

## 12. Comparison Mode · `PARTIAL`

Neither SCA-001 baseline produced a `coverage_summary.json` (the
`FAILED_INPUTS` branch suppresses it), so no per-check delta is computable.
This run establishes a new baseline. The visible change — filesystem coverage
becoming measurable at 100% — is attributable to the `D-PEC-62` scaffold, not
to any SCA-002 act.

---

## What to fix for a cleaner rerun

1. **W-1** — reconcile §5's envelope-posture sentence to `28 S / 34 M / 2 L /
   0 XL`. Requires an explicit owner act: it is outside SCA-002's declared
   change class, so it either rides along under a Gate 3 approval that names
   it, or waits for a separate amendment.
2. **`OI-013`** — a durable repo-native register validator would let this
   consistency class be caught by a build gate instead of by an SCA-time
   audit. W-1 is exactly the defect `OI-013` predicts.
3. **Binding-table drift** (`QA_Report.md` §Section binding) — the
   `SOFTWARE_DECOMP` section numbers hard-coded in `AGENT_AUDIT_DECOMP.md` and
   `AGENT_SCOPE_CHANGE.md` do not match the live document. Semantic
   heading-text binding resolves it, but the stale numbers are a trap for
   future agents. Agent-file scope, not project scope.
