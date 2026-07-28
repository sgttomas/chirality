# Decomposition Coverage Report — SCA-003 post-change interim

**Variant:** `SOFTWARE` · **Decomposition:** revision **1.3**
(`current_basis`) · **Scope:** `ALL` · **Status:** `OK`
(0 blockers / 0 warnings / 73 info)

**Expected source:** accepted decomposition working state being assembled into
SCA-003. **Expected phase:** Gate 5 pre-snapshot.

| # | Check | Verdict |
|---|---|---|
| 1 | Forward packages | `PASS` — 11/11; `SOFTWARE_DECOMP.md` Packages + `execution/PKG-??_*` |
| 2 | Forward deliverables | `PASS` — 64/64; `Deliverables.csv` + package `1_Working/DEL-??-??_*` folders |
| 3 | Reverse coverage | `PASS` — no reverse-only package or exact deliverable folder |
| 4 | ID consistency | `PASS` — all folder IDs equal their declared IDs |
| 5 | Context fidelity | `PASS` — 64/64; `Deliverables.csv` and each matching `_CONTEXT.md` |
| 6 | Artifact presence / contract shape | `INFO` ×64 for absent pre-production artifact sets; 32 valid `SOW_V1`, 32 absent at `OPEN`, 0 ambiguous |
| 7 | Objective mapping | `PASS` for all six objectives; `INFO` ×9 for accepted unmapped-deliverable residue |
| 8 | Ledger integrity | `PASS` — 94 rows; all 71 `IN` package/deliverable references resolve |
| 9 | Derivative parity | `SKIPPED` — not variant-owned by SOFTWARE |
| 9b | Package-shape conformance | `PASS` — explicit companion inventory and role labels; canonical working/register surfaces are discoverable |
| 10 | Active snapshot / handoff state | `PASS` — `_ScopeChange/_LATEST.md` names exactly complete SCA-002; its closure claims match its evidence |
| 11 | Lifecycle distribution | `PASS` — 32 `INITIALIZED`, 32 `OPEN` |

Optional comparison mode was not requested and is `SKIPPED`.

## Evidence and findings

Forward and reverse scans found all 11 declared packages and all 64 declared
deliverables. Every current context exactly matches its register identity,
package, type, Context Envelope, canonical name, and description, including
the three SCA-003 mirrors `DEL-00-01`, `DEL-10-05`, and `DEL-10-12`.
`DEL-10-12` remains under its canonical `Poll-adoption measurement` label and
existing folder path.

Objective support counts agree with `Deliverables.csv`: OBJ-001 20, OBJ-002
12, OBJ-003 12, OBJ-004 10, OBJ-005 7, OBJ-006 9. Nine deliverables and 11
`IN` ledger rows remain intentionally unmapped residue from SCA-002; none of
the six objectives lacks active filesystem-backed support.

The 64 artifact findings and nine unmapped-deliverable findings are
informational. They appear with concrete decomposition and filesystem
references in `Decomp_Coverage_IssueLog.csv`. No blocker or warning was found.

## Active snapshot boundary

At this interim boundary, `_ScopeChange/_LATEST.md` correctly identifies
`SCA-002_2026-07-25_1042/` as the one active snapshot. Its required SCOPE_CHANGE
artifact set is complete, and its `RUN_SUMMARY.md` / `Handoff_State.md` claims
do not outrun the evidence. SCA-003 has not yet published its immutable
snapshot, so this run does not validate SCA-003 snapshot completeness. The
recommended next action is to assemble and point SCA-003, then run the final
post-snapshot AUDIT_DECOMP check.

## What to fix for a cleaner rerun

No structural remediation is required. Produce anticipated artifacts only
through their governed work lifecycle; do not treat the 64 pre-production
`INFO` rows as authorization. Preserve the accepted nine-deliverable mapping
residue unless a separate ruled scope change amends it.
