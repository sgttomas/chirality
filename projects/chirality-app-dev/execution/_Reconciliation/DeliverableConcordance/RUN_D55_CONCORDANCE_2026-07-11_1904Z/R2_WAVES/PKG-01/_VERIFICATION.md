# PKG-01 — R2 Wave-5 fan-in verification record

Run: RUN_D55_CONCORDANCE_2026-07-11_1904Z · Wave: W5 · Package: PKG-01 (Product Governance and Reliance Boundaries)
Discovery: 4 fable agents (owner model steer, Receipt 18 — ALL W5 discovery on fable). Fan-in: fable, high effort.
Source state: frontend/ at fac46e33f, byte-identical through HEAD 242900ae9 = main (orchestrator re-verified at dispatch and at fan-in; verifier independently re-read live surfaces and recomputed all seven authority-doc hashes, reproducing `_REFERENCES.md` and corpus v6 values).

## 1. Recheck coverage

Recheck set = every self-flagged ClaimID ∪ every non-ALIGNED row, per wave protocol. Derived and audited:

- DEL-01-01: 6 rows (REQ-006, REQ-009, REQ-010, ACC-001, ACC-002, REGISTER-1) plus the doc-anchor method question and the cross-deliverable register handle.
- DEL-01-02: 18 rows (RBR-001/-002/-003/-005/-006/-007/-009/-014/-019/-020/-021/-022/-023/-024/-025, ACC-001, ACC-002, REGISTER-1).
- DEL-01-03: 9 rows (REQ-01, REQ-04, EXC-02, ACC-01, ACC-02, ACC-03, ACC-04 incl. the validator warning, ACC-05, REGISTER-1).
- DEL-01-04: 7 rows (REQ-008, REQ-011, EXC-002, ACC-001, ACC-002, ACC-003, ACC-004).

**Total rechecked: 40 of 89 rows. Verdicts: 37 CONFIRMED, 2 REFUTED, 1 CONTESTED.**

## 2. Refutations — routed to owning agents, both accepted

1. **DEL-01-03 ACC-02**: STALE_ASSESSMENT → **STALE_SPECIFICATION** (accepted). The false "D-APP-38 corpus v1 records matching hashes" wording lives on kit surfaces (Spec line 45, Datasheet 68, Procedure 18/30/102-103, Guidance 85-86), and corpus v1's recorded PRD hash (`33e00c82…`) no longer matches the live file — the kit flatly asserts a now-false state (MR-8 first branch). Owner independently re-verified `AUTHORITY_CORPUS.json` (v1 binding commit `8da930ae0`) before accepting; also corrected the row's ImplementationEvidence clause that carried the refuted "remaining hash-true" premise (owner judgment, recorded in owner notes). Makes the corpus-label class four-way consistent (§5).
2. **DEL-01-04 ACC-002**: ACCEPTED_DIVERGENCE → **STALE_SPECIFICATION** (accepted). Strict affirmative-permission test fails: D-APP-50/D-APP-52 affirmatively permit the tool surface but contain no text accepting or deferring the BR-005 register-wording divergence; the row's own repair-shaped RemainingWork concedes the MR-8 branch. A minority ALIGNED reading is preserved for R3 (BR-005's statement carve-in arguably covers the ruled propose/validate/read surface; pivot fact: whether the staged loopback tools count as "domain-engine integration as a shipping feature").

## 3. Contested rows

1. **DEL-01-02 RBR-014** (STALE_ASSESSMENT vs STALE_SPECIFICATION) — **RESOLVED by owner: STALE_SPECIFICATION**, no standing contest. The owner independently re-verified the deciding fact rather than deferring: `session-manager.ts` line 10 `DEFAULT_MODE = 'direct'` normalizes to `'ask'` via `permission-overlay.ts` lines 57-71 and workspaceWrite auto-allows Bash after hooks (lines 141-168), while register lines 50 and 110 flatly assert "Bash denied by default" as current handling — a live register surface carrying now-false wording, so the MR-1 live-surfaces-agree reservation for STALE_ASSESSMENT falls away. Row re-anchored (DeclaredState, ImplementationEvidence, RemainingWork naming register lines 50/110 + Spec line 42).

**W5 carries zero standing contested rows.**

## 4. Corrections and evidence recasts (owner-applied)

- DEL-01-02 RBR-021: repair enumeration extended to register lines 112 ("Current corpus is v1 and MATCH" — flatly false at v6) and 122 (cross-check "preserve D-APP-38 corpus v1") alongside line 9; no new row (verifier ruling).
- DEL-01-03 MR-10 recasts: EXC-01, EXC-03, ACC-04 (the validator-warned row) VerificationEvidence recast from free-text "Document/scope claim …" to `RUN-INSPECTION@242900ae9 (…)`; owner also recast REGISTER-1's same-class cell on own initiative. Dispositions unchanged; zero free-text residue (machine-checked).
- DEL-01-01 doc-anchor question: `RUN-INSPECTION@242900ae9` for doc-only rows ruled MR-10-conformant (vocabulary fixes the form, not the SHA; byte-identity makes both anchors equivalent). No correction.

## 5. Cross-deliverable consistency verified

- **Cross-deliverable handle adjudicated**: DEL-01-01's notes claim (register line 112 says "Current corpus is v1 and MATCH", flatly false at v6; defect belongs to DEL-01-02) verified accurate; DEL-01-02 carries it on RBR-021, now with the full line enumeration (9/112/122).
- **Corpus v1→v6 label class four-way consistent** after the ACC-02 refutation: DEL-01-01 ACC-001 + REGISTER-1; DEL-01-02 RBR-021; DEL-01-03 ACC-02 + DEP-01-03-011 register note; DEL-01-04 ACC-004 — all STALE_SPECIFICATION under MR-8; substantive MATCH claims true everywhere (hashes verified by recompute). One run-wide harmonization/repair tranche.
- **CHECKING-lifecycle class fully consistent**: DEL-01-01 REQ-009, DEL-01-02 ACC-001, DEL-01-03 ACC-03, DEL-01-04 ACC-001 all STALE_SPECIFICATION under D-APP-54; one repair pattern (lifecycle-neutral wording reading from `_STATUS.md`).
- **No intra-package surface conflicts**: copy-absence claims (DEL-01-02 RBR-018 vs DEL-01-03 REQ-02/05) agree and assign copy ownership to DEL-01-03; domain-boundary claims (DEL-01-04 REQ-008/ACC-002 vs DEL-01-03 EXC-04) agree on the ruled propose-only surface; REMAINING-1 rows identical and MR-2-conformant across all four.
- **Enforcement-truth axis (this package's special duty)**: every OUT boundary and copy MUST checked against the live frontend; no register row asserts an enforcement the implementation lacks, and no boundary is crossed live without a ruling. Exception class: the reliance register's four stale enforcement-surface path citations (§6 item 3).

## 6. Items escalated to R3 (not resolved here)

1. DEL-01-04 ACC-002 minority ALIGNED reading (BR-005 carve-in vs "shipping feature" pivot fact) — recorded with the accepted STALE_SPECIFICATION row.
2. MR-1 application rule worth run-wide ratification: assessment-only staleness → STALE_ASSESSMENT; any kit/register surface carrying the stale wording → STALE_SPECIFICATION (would have mechanically decided RBR-014; consistent with all W5 outcomes).
3. Register enforcement-surface path drift: RBR-001's four stale paths (files live at `frontend/packages/harness-contract/src/`); RBR-025's proposal to add a cited-path-existence assertion to `reliance-boundary-register.test.ts` (verified absent) is sound.
4. REF-007 machine-absolute-path wart recurs in all four deliverables' `_REFERENCES.md` — run-wide R3 candidate, not per-deliverable rows.
5. Corpus v1→v6 label harmonization tranche (§5) — likely joins the REF-006-class R5 repair tranche from earlier waves.
6. DEL-01-04 ACC-003's proposed provider-expansion BR row must be worded against the post-D-APP-44 F1 posture (interacts with DEL-04-02 ownership).
7. PKG-01's live verification of the reliance register's enforcement claims retro-confirms PKG-03..09 waves' citations of the register as enforcement truth, except the four stale path pointers (item 3).
8. R1 REQUIREMENT_INDEX parser gap confirmed for DEL-01-02 (zero rows; 25 claims re-derived from Specification.md lines 29-53).

## 7. Method compliance

Deterministic validator: 0 errors / 0 warnings across all four CSVs post-correction (89 rows; the single pre-fan-in warning on DEL-01-03 ACC-04 resolved by the MR-10 recast). MR-1/MR-2 machine-checked by owners post-edit. All verdicts routed to owning agents; no orchestrator or verifier edits to any CSV; owner deviations from verdict framing (DEL-01-03's ImplementationEvidence clause correction) recorded in owner notes. Notes-file factual-error audit: none found (register line 112 text, parser-gap claim, four-path drift, hash prefixes, and all four censuses reproduced). F-APP-3 respected; no tests executed; no secret values in any cell.

## 8. Final tally

| Deliverable | Rows | ALIGNED | STALE_SPEC | STALE_ASSESS | PARTIAL | REM_STATE_MM | DOC_UNIMPL |
|---|---|---|---|---|---|---|---|
| DEL-01-01 | 15 | 9 | 2 | 2 | 0 | 1 | 1 |
| DEL-01-02 | 33 | 15 | 6 | 9 | 2 | 1 | 0 |
| DEL-01-03 | 21 | 15 | 3 | 1 | 1 | 1 | 0 |
| DEL-01-04 | 20 | 15 | 4 | 0 | 0 | 0 | 1 |
| **PKG-01** | **89** | **54** | **15** | **12** | **3** | **3** | **2** |

Zero AUTHORITY_CONFLICT, UNKNOWN, DEFERRED_AGENT_WORKFLOW, ACCEPTED_DIVERGENCE, IMPLEMENTED_DIFFERENTLY, IMPLEMENTED_UNDOCUMENTED, STALE_VERIFICATION. Register defects: 2 (DEL-01-01 REGISTER-1 corpus-v1 pin; DEL-01-02 REGISTER-1 REF-007 absolute path) plus DEL-01-03 REGISTER-1 (DEP-01-03-011 metadata lag).
PKG-01: 40 rechecked, 37 confirmed, 2 refuted (both accepted), 1 contested (owner-resolved). Standing contests: 0.
