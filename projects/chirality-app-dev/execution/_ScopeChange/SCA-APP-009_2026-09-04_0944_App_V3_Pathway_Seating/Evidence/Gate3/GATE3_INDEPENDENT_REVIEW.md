# SCA-APP-009 Gate-3 Independent Review

**Verdict:** `PASS`
**Severity count:** `0 BLOCKER / 0 MAJOR / 1 MINOR`
**Review role:** fresh read-only Agent 2 independent reviewer
**Manager basis:** `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f`
**Reviewed freeze:** 2026-09-04 Gate-3 scratch package

The exact Gate-3 amendment preview is fit to present for owner approval and Gate-4 authorization. The one MINOR is a machine-schema delimiter mismatch in a Gate-4-freezable supporting register; it does not create semantic ambiguity, alter either exact authoritative candidate, or mask a missing supersession binding.

## Finding

### MINOR-001 — `DownstreamReruns` uses the wrong list delimiter

`agents/AGENT_SCOPE_CHANGE.md:731` defines `Amendment_Actions.csv` `DownstreamReruns` as a **comma-separated** list. All multi-value entries in `gate3/Amendment_Actions.csv` instead use semicolons, for example ActionSeq 1 (`AUDIT_DECOMP;RECONCILIATION;WORKING_ITEMS`) and ActionSeq 8 (`AUDIT_DECOMP;RECONCILIATION;PREPARATION;WORKING_ITEMS;dependency-extract`). The cells are already CSV-quoted, so the specified comma delimiter can be represented without changing row structure.

Required correction: before Gate 4 freezes `Amendment_Actions.csv`, replace the within-cell semicolons in `DownstreamReruns` with commas, reparse the CSV, and refresh any recorded hash of that register. Do not alter the authoritative decomposition or companion candidates for this correction.

This is MINOR because every rerun token is present and unambiguous, the current schema does not make the register an applied Gate-3 authority surface, and `SNAPSHOT_CONTRACT_PREVIEW.md:16` expressly freezes it only after Gate 4. It is not a reason to reject the exact Gate-3 decomposition/companion bytes.

## Independent checks

| Check | Result | Evidence |
| --- | --- | --- |
| Basis and repository cleanliness | PASS | Manager worktree HEAD is exactly `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f`; `git status --short` returned empty. |
| Frozen identities | PASS | All manager-supplied freeze hashes re-derived, including decomposition candidate `e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97`, companion candidate `e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70`, decomposition diff `2fe0b2a1969100e8f11f6957e9015765f5c10318bebcfa047a0b8ac94648f48a`, companion diff `4da8820c0b16a1486218a0de52db518ac43a7f2832f6f75bd1734487dc8faa17`, actions `15031df73450efb315130160e6d0bcd8de501e90baad0e92859b824a9f8253da`, SCA-APP-008 backfill `ff0629982a02a50e91d5c3de2c7b145b2b5d3ace0527004fe463f6a46c614009`, delta `7c3b1899825ac3a208c6e0ca8fc5afacafdd02e1355ed8393bab042b949d9233`, cumulative map `851979228418303ce0aa6a6b51ef328b63bb57361402b67e5c3485e877dbce25`, and snapshot contract `aa43c2065ca43a1c9fde6706bb8ea0e9ade05a651a8f9f6fb3341d74ea4cd849`. |
| Full diffs and dry application | PASS | Independently regenerated diffs are byte-identical to both supplied full diffs; both pass `git apply --check` against the exact basis. |
| Candidate topology | PASS | 10 packages, 52 deliverables, 80 SSOW rows, 80 Scope Ledger rows, 75 IN / 4 OUT / 1 TBD, 10 objectives, and envelopes S9 / M41 / L2 / XL0. IDs are unique; SSOW and Scope Ledger ID sets match. |
| Stable IDs and coupling | PASS | SOW-079, SOW-080, DEL-09-07, and DEC-024 are the next unused IDs. Parent/package references are valid; all primary package assignments are represented by their deliverable mappings. |
| Scope Ledger / Deliverables reverse parity | PASS | Independently parsed 137 relations in each direction, with zero missing and zero extra relations. |
| Objective mappings | PASS | SOW-079 is mapped to exactly OBJ-002 and OBJ-004; SOW-080 is mapped to OBJ-008. The SOW-079 dual mapping is justified because the bounded probe tests both Root-runtime App-client conformance and provider/SDK client conformance while retaining Root App Server supply/download/generic-runtime authority. |
| Canonical type and granularity | PASS | `MIGRATION_SCRIPT` is a canonical SOFTWARE type. DEL-09-07/M is one bounded installer-transaction shape, while DEL-09-04/L remains byte-identical and retains its DMG/instruction-root/SDK-package shape. |
| Companion full-file recompute | PASS | 83 rows, 83 unique invariant IDs, 50 families, and 18 columns remain stable; all 83 decomposition pins change to the exact candidate; all 83 contract pins and all IDs/owners/provenance classes remain unchanged. |
| Companion semantic-diff set | PASS | Beyond the global pin, only K-CONTROL-1, K-STORE-2, and K-VALIDATE-1 change, each in exactly `AppDeliverableIDs`, `EnforcementSurfaces`, `ValidationSurfaces`, and `RationaleEvidenceAnchor`. DEL-09-07 appropriately participates in control-IPC, store-preserving migration/rollback, and validation. K-PACKAGE-1 and K-RELEASE-1 correctly remain unchanged because the new slice does not alter instruction-root integrity, target/release identity, or authorize a release act. |
| Open-issue telemetry | PASS | OI-007 already existed as SHARED_RUNTIME but was omitted from the telemetry rollup. Recomputing it to one issue and 10 affected scope items is a necessary consequence of adding SOW-079/SOW-080, not unrelated scope expansion. OI-003 correctly gains SOW-080; no issue closes. |
| Action coverage and supersession binding | PASS, subject to MINOR-001 | All 16 atomic preview actions are represented. The four authority-bearing scope actions (ActionSeq 1/3/5/7) correctly carry `YES` and map to D-001/D-003/D-005/D-007. Their paired deliverable rows (2/4/6/8) are explicitly the reverse-view implementation of those same facts and correctly avoid duplicate bindings; other structural/telemetry/derivative/log actions remain `NO`. |
| Cumulative SCA-APP-008 reconstruction | PASS | The 14-row backfill exhaustively represents the accepted substantive SCA-APP-008 transaction: four deliverable extensions, seven modified invariants, two new invariants, and one six-row enforcement-map extension. K-CONTROL-1 and K-EVENT-4 are correctly classified as `SUPERSESSION`; the other 12 are `SUPPLEMENTARY_EXTENSION`. C-11/DEC-023 history is not a separate superseded authority fact. SCA-APP-008 bytes remain immutable. |
| Normative accumulator | PASS | Fresh run from the accepted SCA-APP-006 map plus the SCA-APP-008 backfill plus the SCA-APP-009 delta produced 34 rows, zero findings, exact `--check-map` parity, and SHA-256 `851979228418303ce0aa6a6b51ef328b63bb57361402b67e5c3485e877dbce25`. |
| Snapshot completeness contract | PASS | The preview enumerates every current SOFTWARE snapshot artifact, distinguishes prediction-only post-coverage from later executed evidence, requires a complete new snapshot before pointer movement, and preserves SCA-APP-008 as dated immutable history. |
| Boundary containment | PASS | Root retains App Server supply/download, supervisor/control/store, consent, and session-policy authority. F-APP-2/D-APP-97 remain explicit. S-6 and the nine-node SCC remain separate. No dependency, lifecycle, implementation, release, Gate-4, Gate-5, or `_LATEST.md` act appears. |
| Authority corpus | PASS | Independent status run reports v20 and no drift on the untouched live tree. |
| Pre-change evidence | PASS | `Pre_Change_Coverage.json` is SHA-identical to the accepted Gate-1 audit summary (`c1cfe859fbf714899f80dc91e8060949350e83e4dce45933cdce296bd2727968`). |

## Review conclusion

The package faithfully carries the accepted Gate-2 transaction, including the owner-approved 51→52 topology. The exact decomposition and companion candidates are internally coherent, dry-applicable, authority-bounded, and complete enough for the Gate-3 owner question. Post-application AUDIT_DECOMP, reconciliation, dependency extraction/closure, snapshot verification, and pointer parity correctly remain unrun until their later authorized gates.

No repository or project bytes changed during this review. The only written artifact is this review memo (plus reviewer-only temporary check outputs under `gate3/review/tmp/`).
