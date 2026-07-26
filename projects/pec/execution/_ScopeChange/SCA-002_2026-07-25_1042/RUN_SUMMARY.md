---
amendment_id: SCA-002
doc_kind: scope_change.run_summary
decomp_variant: SOFTWARE
gate: 5
created: 2026-07-25
authority: D-PEC-64 (+ §4.3 owner amendments #1 and #2; plan amendment v2.1)
---

# SCA-002 — Run Summary

## Amendment

Complete the deliverable→objective mapping in decomposition truth for the
Phase 2.2 scope-of-work wave scope, so every wave deliverable carries a
non-empty objective reference set. Scope width **O-A wave-minimum** (owner
ruling, Gate 1). Change class **MODIFY only** — no topology change.

`SOFTWARE_DECOMP.md` **revision 1.1 → 1.2**.

## State fields

| Field | Value |
|---|---|
| `DecompositionTruthState` | `COMPLETE` |
| `DerivativePackageState` | `COMPLETE` |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` |
| `MetadataAlignmentState` | `NOT_REQUIRED` |
| `AuditState` | `NON_BLOCKING_PASS` |
| `ReadyForNextPhase` | `REGEN_ONLY` |
| `ClosureVerdict` | `CLOSED_FOR_SCOPE_CHANGE_ONLY` |

## Actions taken

| Action | Target | Result |
|---|---|---|
| A001 | `_Decomposition/ScopeLedger.csv` | 20 `ObjectiveIDs` cells populated |
| A002 | `_Decomposition/Deliverables.csv` | 17 `SupportsObjectives` cells populated |
| A003a–d | `SOFTWARE_DECOMP.md` §3 | Header qualifier dropped; 4 objective rows reconciled; post-table note and mapping-notes block rewritten with the ingest/bridge and `SOW-063` rationale retained verbatim |
| A004 | `SOFTWARE_DECOMP.md` §7 | Metric 31 → 11; Revision → 1.2 |
| A005a/b | `SOFTWARE_DECOMP.md` §11/§12 | `DL-17` appended; revision row 1.2 appended |
| A006 | `_Decomposition/_LATEST.md` | Full replacement — revision 1.2 pointer + handoff state |
| A007 | `SOFTWARE_DECOMP.md` §5 | Envelope-posture prose `29 S / 33 M` → `28 S / 34 M` (W-1) |
| A008 | `SOFTWARE_DECOMP.md` front matter | revision/date/accepted/session_authorization → 1.2 |
| P1 | 17 × `_CONTEXT.md` | `SupportsObjectives` restated from the register |
| P2 | 64 × `_CONTEXT.md` | Basis pointer refreshed (Gate 4 ruling (i), P-supersede) |

## Pre / post comparison

| Metric | Pre (1.1) | Post (1.2) |
|---|---|---|
| Scope items | 94 (71 IN / 14 OUT / 9 TBD) | **unchanged** |
| Packages / deliverables / objectives | 11 / 64 / 6 | **unchanged** |
| Context Envelopes | S 28 / M 34 / L 2 / XL 0 | **unchanged** |
| IN items without objective mapping | 31 | **11** |
| Deliverables without objective mapping | 26 | **9** |
| Wave members without objective mapping | 17 | **0** |
| Union-invariant violations | 0 | **0** |
| `_CONTEXT.md` pointers asserting revision 1.1 as `current_basis` | 64 | **0** |

Residue held: the 11 intentional/out-of-wave IN rows and 9 residue
deliverables are byte-identical and still unmapped, as `D-PEC-64` §4.3
requires.

## Verification

All post-check assertions pass **under the corrected assertion 9** (see
`Propagation_Plan.md` §3d, dated correction 2026-07-25) — union invariant 0 file-wide; residue
untouched; token grammar `^OBJ-[0-9]{3}$` on every changed cell; topology
unchanged; window exactly 20 + 17 rows in two columns with `DEL-03-01`
unchanged and `SOW-021` ⊆ `{OBJ-005}`; revision-1.2 parity across front
matter, §7 and `_LATEST.md`; `analyze_dep_closure.py` unchanged from the
D-PEC-62 landing values; census `64 OPEN`. Evidence:
`Post_Change_Coverage.json`.

## Audit

Run **inline** by this SCOPE_CHANGE instance — Agent 2 dispatch is unavailable
in this harness (root `AGENTS.md` single-agent fallback), recorded as a
substitution at Gate 1.

Two passes, per plan amendment **v2.1**:

| Pass | Snapshot | Result |
|---|---|---|
| Interim | `COV_SCA002_POSTCHANGE_2026-07-25_1252` | `BLOCKERS` — 1 blocker (Check 10: snapshot artifacts not yet written). Known ordering circularity; all other checks clean |
| **Final** | `COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257` | **`OK`** — 0 blockers, 0 warnings, 73 info; Check 10 `PASS` against the completed snapshot; forward/reverse coverage 100%, context fidelity 100%, objective coverage 100%, objective-evidence integrity `PASS`, package-shape `PASS` |

Pre-change baseline: `COV_SCA002_PRECHANGE_2026-07-25_1040` (`WARNINGS`;
its single warning was **W-1**, which A007 resolves).

## Recommended downstream reruns (not executed)

See `Handoff_State.md` §6. Principally: the D-PEC-63 re-pins, the
`_COORDINATION.md` / register-row / packet / wave-plan updates, the
`LOOP_RECEIPTS.md` receipt, and the closure commit — all owned by resumed
`PROJECT_SETUP`. `OI-B`, `OI-A` and `OI-013` remain open.

## Handoff to CHANGE / PROJECT_SETUP

**SCOPE_CHANGE performed no git operation.** `D-PEC-64` §3.6(b) assigns the
closure commit to resumed `PROJECT_SETUP`, working from the file list in the
Gate 5 return. Recommended message:

```text
scope: SCA-002 — deliverable→objective mapping for the Phase 2.2 wave scope

Variant: SOFTWARE
Actions: 10 (MODIFY:10)
Affected entities: ScopeLedger.csv (20 IN rows), Deliverables.csv (17
deliverables), SOFTWARE_DECOMP.md (front matter + §3/§5/§7/§11/§12),
_Decomposition/_LATEST.md, _CONTEXT.md propagation, SCA-002 snapshot,
AUDIT_DECOMP pre/post baselines
```
