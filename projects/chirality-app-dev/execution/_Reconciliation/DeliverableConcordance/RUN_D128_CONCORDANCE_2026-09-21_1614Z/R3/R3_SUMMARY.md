# R3 summary — RUN_D128_CONCORDANCE_2026-09-21_1614Z

Script-built sections by `R3/_scripts/r3_summary.py`; the last section is hand-written by the R3 manager. Evidence for HELP_HUMAN and the owner, not rulings.

## 1. Coverage QA verdicts

| Q1 CLAIM_INDEX units dispositioned | PASS | 1746 of 1746 (expected 1,746); missing 0 [] |
| Q2 EXTENSION_INDEX units dispositioned | PASS | 221 of 221 (expected 221); missing 0 [] |
| Q3 capabilities claimed or listed as unmapped (with reach and state) | PASS | 468 capability rows: 361 claimed/partial by >=1 deliverable, 107 in UNMAPPED_IMPLEMENTATION.csv; unmapped without stated reach/state: 0 []; reverse IDs not in any capability file: 0 [] |
| Q4 package summaries reproduce from the ledgers (sealed Disposition census) | PASS | 24 of 24 summaries reproduce |
| Q5 no duplicate keys | PASS | ClaimKey duplicates 0 []; reverse (CapabilityID, DeliverableID) duplicates 0 [] |
| Q6 REMAP_LOG reconciles the sealed census to the final census | PASS | 3568 rows replayed from sealed values through 1188 log lines; mismatches 0 [] |

Detail: `COVERAGE_AND_QA.md`.

## 2a. Disposition census — Deliverable ledgers (54): sealed → final

| Disposition | Sealed | Final | Delta |
|---|---:|---:|---:|
| ALIGNED | 698 | 695 | -3 |
| IMPLEMENTED_UNDOCUMENTED | 1 | 1 | +0 |
| DOCUMENTED_UNIMPLEMENTED | 110 | 104 | -6 |
| PARTIALLY_IMPLEMENTED | 415 | 411 | -4 |
| IMPLEMENTED_DIFFERENTLY | 183 | 179 | -4 |
| STALE_SPECIFICATION | 1032 | 1044 | +12 |
| STALE_ASSESSMENT | 8 | 8 | +0 |
| STALE_VERIFICATION | 34 | 34 | +0 |
| ACCEPTED_DIVERGENCE | 37 | 32 | -5 |
| RETIRED_BY_RULING | 40 | 40 | +0 |
| LIFECYCLE_REASSESSMENT_REQUIRED | 2 | 2 | +0 |
| REMAINING_STATE_MISMATCH | 124 | 112 | -12 |
| AUTHORITY_CONFLICT | 150 | 159 | +9 |
| UNKNOWN | 9 | 22 | +13 |
| NOT_AUDITABLE | 374 | 374 | +0 |
| **Total** | 3217 | 3217 | +0 |

## 2b. Disposition census — Extension ledgers (13): sealed → final

| Disposition | Sealed | Final | Delta |
|---|---:|---:|---:|
| ALIGNED | 195 | 195 | +0 |
| DOCUMENTED_UNIMPLEMENTED | 10 | 10 | +0 |
| PARTIALLY_IMPLEMENTED | 30 | 30 | +0 |
| IMPLEMENTED_DIFFERENTLY | 33 | 28 | -5 |
| STALE_SPECIFICATION | 45 | 45 | +0 |
| STALE_VERIFICATION | 1 | 1 | +0 |
| ACCEPTED_DIVERGENCE | 6 | 6 | +0 |
| RETIRED_BY_RULING | 9 | 9 | +0 |
| REMAINING_STATE_MISMATCH | 4 | 4 | +0 |
| DEFERRED_AGENT_WORKFLOW | 1 | 1 | +0 |
| AUTHORITY_CONFLICT | 5 | 10 | +5 |
| UNKNOWN | 1 | 1 | +0 |
| NOT_AUDITABLE | 11 | 11 | +0 |
| **Total** | 351 | 351 | +0 |

## 3. Sealed-to-final deltas by Source (REMAP_LOG)

Each REMAP_LOG line is one step; `SealedValue` is the value before that step. Net Disposition moves are counted per step (a row moved twice counts twice).

| Source | Lines | Rows touched | Disposition steps | HumanDecisionNeeded steps | Other fields |
|---|---:|---:|---:|---:|---:|
| ERRATA | 116 | 85 | 6 | 4 | 106 |
| CORRECTION | 116 | 107 | 0 | 6 | 110 |
| R3_RULE | 386 | 335 | 41 | 218 | 127 |
| R3_RUNWIDE | 495 | 351 | 28 | 37 | 430 |
| OWNER_CHECK | 75 | 63 | 2 | 0 | 73 |

Disposition moves (Source: from → to × n):

- ERRATA: PARTIALLY_IMPLEMENTED → IMPLEMENTED_DIFFERENTLY × 2
- ERRATA: ALIGNED → PARTIALLY_IMPLEMENTED × 2
- ERRATA: IMPLEMENTED_DIFFERENTLY → PARTIALLY_IMPLEMENTED × 1
- ERRATA: DOCUMENTED_UNIMPLEMENTED → PARTIALLY_IMPLEMENTED × 1
- OWNER_CHECK: UNKNOWN → PARTIALLY_IMPLEMENTED × 2
- R3_RULE: REMAINING_STATE_MISMATCH → STALE_SPECIFICATION × 21
- R3_RULE: STALE_SPECIFICATION → REMAINING_STATE_MISMATCH × 9
- R3_RULE: DOCUMENTED_UNIMPLEMENTED → UNKNOWN × 7
- R3_RULE: PARTIALLY_IMPLEMENTED → UNKNOWN × 4
- R3_RUNWIDE: IMPLEMENTED_DIFFERENTLY → AUTHORITY_CONFLICT × 14
- R3_RUNWIDE: PARTIALLY_IMPLEMENTED → UNKNOWN × 4
- R3_RUNWIDE: ACCEPTED_DIVERGENCE → IMPLEMENTED_DIFFERENTLY × 3
- R3_RUNWIDE: UNKNOWN → ALIGNED × 2
- R3_RUNWIDE: ALIGNED → UNKNOWN × 2
- R3_RUNWIDE: ACCEPTED_DIVERGENCE → DOCUMENTED_UNIMPLEMENTED × 2
- R3_RUNWIDE: ALIGNED → IMPLEMENTED_DIFFERENTLY × 1

Errata rejected by CORRECTIONS (sealed value kept): 2. Spot-check reverts (second pass): 0.

## 4. HumanDecisionNeeded by token (rows citing the token; all rows)

| Token | Sealed | Final | Delta |
|---|---:|---:|---:|
| R4 | 153 | 48 | -105 |
| R4-Q1 | 622 | 727 | +105 |
| R4-Q2 | 32 | 32 | +0 |
| R4-Q3 | 13 | 13 | +0 |
| R4-Q4 | 59 | 102 | +43 |
| R4-Q5 | 44 | 65 | +21 |
| R4-Q6 | 3 | 86 | +83 |
| NO | 2703 | 2601 | -102 |
| D-APP-116 | 4 | 4 | +0 |
| D-APP-117 | 5 | 5 | +0 |
| D-APP-118 | 2 | 2 | +0 |
| D-APP-119 | 7 | 7 | +0 |
| D-APP-121 | 3 | 3 | +0 |
| D-APP-127 | 4 | 4 | +0 |
| D-APP-43 | 1 | 1 | +0 |
| D-APP-73 | 14 | 14 | +0 |
| D-GOV-43 | 1 | 1 | +0 |

## 5. Clusters (candidate R4 packets)

| Cluster | Title | PRIMARY | ALSO/CONTEXT | Packages | AuthorityTier mix |
|---|---|---:|---:|---|---|
| CL-01 | Owner-deferred DEL-06-02 keys (Addendum 5) | 2 | 0 | PKG-06 | GOVERNANCE_INVARIANT 1; LOCAL_DESIGN 1 |
| CL-02 | Owner check: off-code events known only by absence of a record (Addendum 10) | 63 | 0 | EXT, PKG-00, PKG-01, PKG-02, PKG-03, PKG-05, PKG-09, PKG-10 | LOCAL_DESIGN 36; GOVERNANCE_INVARIANT 22; NOT_APPLICABLE 3; PRD 2 |
| CL-03 | Release signing posture and G6a (run-wide call f) | 22 | 5 | EXT, PKG-09 | GOVERNANCE_INVARIANT 20; LOCAL_DESIGN 5; NOT_APPLICABLE 2 |
| CL-04 | R4-Q6: unamended App DIRECTIVE and K-PERM-1/6 versus D-GOV-43 | 86 | 0 | EXT, PKG-01, PKG-02, PKG-03, PKG-04, PKG-06, PKG-09, PKG-10 | GOVERNANCE_INVARIANT 76; PRD 5; LOCAL_DESIGN 4; NOT_APPLICABLE 1 |
| CL-05 | R4-Q5: Codex event payloads stored as received or translated | 53 | 12 | EXT, PKG-01, PKG-02, PKG-03, PKG-04, PKG-05, PKG-09 | GOVERNANCE_INVARIANT 57; PRD 5; NOT_APPLICABLE 2; LOCAL_DESIGN 1 |
| CL-06 | R4-Q4: the 2026-09-09 four-role adoption | 102 | 0 | EXT, PKG-02, PKG-04, PKG-08, PKG-10 | GOVERNANCE_INVARIANT 53; LOCAL_DESIGN 29; PRD 17; NOT_APPLICABLE 3 |
| CL-07 | R4-Q3: actor check on the legacy status_transition tool | 13 | 0 | EXT, PKG-06, PKG-07 | GOVERNANCE_INVARIANT 13 |
| CL-08 | R4-Q2: Codex engine never run through the K-ENGINE-2 conformance suite | 24 | 8 | EXT, PKG-01, PKG-03, PKG-04, PKG-06, PKG-09 | GOVERNANCE_INVARIANT 25; PRD 5; LOCAL_DESIGN 2 |
| CL-09 | R4-Q1: retained legacy in-process harness versus the live Codex path | 630 | 97 | EXT, PKG-01, PKG-02, PKG-03, PKG-04, PKG-05, PKG-06, PKG-07, PKG-08, PKG-09, PKG-10 | GOVERNANCE_INVARIANT 442; LOCAL_DESIGN 185; PRD 59; NOT_APPLICABLE 41 |
| CL-10 | Rows held on existing or awaiting decisions (D-APP-nn / D-GOV-nn tokens) | 18 | 23 | EXT, PKG-02, PKG-03, PKG-04, PKG-05, PKG-06, PKG-07, PKG-08, PKG-09, PKG-10 | GOVERNANCE_INVARIANT 18; LOCAL_DESIGN 17; NOT_APPLICABLE 5; PRD 1 |
| CL-11 | Unframed owner questions (plain R4) | 26 | 22 | EXT, PKG-02, PKG-03, PKG-04, PKG-05, PKG-06, PKG-08, PKG-09, PKG-10 | GOVERNANCE_INVARIANT 27; LOCAL_DESIGN 20; NOT_APPLICABLE 1 |
| CL-12 | Live path: unredacted event storage (K-EVENT-6) | 25 | 32 | EXT, PKG-01, PKG-02, PKG-03, PKG-04, PKG-05, PKG-06, PKG-08 | GOVERNANCE_INVARIANT 52; PRD 3; LOCAL_DESIGN 1; NOT_APPLICABLE 1 |
| CL-13 | Live path: protected paths, instruction root and hooks (K-DOMAIN-2; PKG-06 path/hook rows) | 25 | 51 | PKG-06, PKG-07, PKG-10 | GOVERNANCE_INVARIANT 69; NOT_APPLICABLE 6; PRD 1 |
| CL-14 | Live path: human gate and status transition | 13 | 44 | EXT, PKG-01, PKG-04, PKG-06, PKG-07, PKG-08, PKG-10 | GOVERNANCE_INVARIANT 46; NOT_APPLICABLE 5; LOCAL_DESIGN 4; PRD 2 |
| CL-15 | Live path: execution-root scaffolding returns 501 | 28 | 8 | EXT, PKG-02, PKG-04, PKG-06, PKG-07, PKG-09 | GOVERNANCE_INVARIANT 28; PRD 5; NOT_APPLICABLE 2; LOCAL_DESIGN 1 |
| CL-16 | Live path: legacy-session migration inert | 8 | 6 | PKG-01, PKG-03, PKG-05 | GOVERNANCE_INVARIANT 8; LOCAL_DESIGN 4; NOT_APPLICABLE 2 |
| CL-17 | Carrier propagation: D-APP-127 / D-GOV-43 not carried into deliverable text | 118 | 43 | EXT, PKG-00, PKG-01, PKG-02, PKG-03, PKG-04, PKG-05, PKG-06, PKG-07, PKG-08, PKG-09, PKG-10 | NOT_APPLICABLE 84; LOCAL_DESIGN 42; GOVERNANCE_INVARIANT 34; PRD 1 |
| CL-18 | Document hygiene: reference hashes, registers and metadata | 513 | 29 | EXT, PKG-00, PKG-01, PKG-02, PKG-03, PKG-04, PKG-05, PKG-06, PKG-07, PKG-08, PKG-09, PKG-10 | NOT_APPLICABLE 456; LOCAL_DESIGN 64; GOVERNANCE_INVARIANT 19; PRD 3 |
| CL-19 | Pre-v3 drift | 260 | 118 | EXT, PKG-00, PKG-01, PKG-02, PKG-03, PKG-04, PKG-05, PKG-06, PKG-07, PKG-08, PKG-09, PKG-10 | GOVERNANCE_INVARIANT 134; NOT_APPLICABLE 123; LOCAL_DESIGN 103; PRD 18 |
| CL-20 | Codex sole engine and credential custody | 117 | 517 | EXT, PKG-01, PKG-02, PKG-03, PKG-04, PKG-05, PKG-06, PKG-07, PKG-08, PKG-09, PKG-10 | GOVERNANCE_INVARIANT 419; LOCAL_DESIGN 122; PRD 61; NOT_APPLICABLE 32 |
| CL-21 | A2 topology, Runtime extraction and facade deprecation | 139 | 172 | EXT, PKG-01, PKG-02, PKG-03, PKG-04, PKG-05, PKG-06, PKG-07, PKG-08, PKG-09, PKG-10 | GOVERNANCE_INVARIANT 172; LOCAL_DESIGN 90; NOT_APPLICABLE 37; PRD 12 |
| CL-22 | Shell redesign and role adoption (not otherwise framed) | 75 | 73 | EXT, PKG-01, PKG-02, PKG-05, PKG-07, PKG-08, PKG-09 | LOCAL_DESIGN 55; GOVERNANCE_INVARIANT 52; PRD 30; NOT_APPLICABLE 11 |
| CL-23 | Open lifecycle gates and v3 release scope | 38 | 72 | EXT, PKG-02, PKG-03, PKG-04, PKG-05, PKG-06, PKG-07, PKG-08, PKG-09, PKG-10 | GOVERNANCE_INVARIANT 52; LOCAL_DESIGN 43; PRD 8; NOT_APPLICABLE 7 |
| CL-24 | Done-declaration questions Q-01..Q-13 (CONTEXT) | 0 | 34 | PKG-09 | GOVERNANCE_INVARIANT 26; LOCAL_DESIGN 6; NOT_APPLICABLE 2 |
| CL-EX | Exceptions | 3 | 0 | EXT | LOCAL_DESIGN 1; PRD 1; NOT_APPLICABLE 1 |

25 clusters (including the exceptions list); 2401 rows with a PRIMARY cluster. Full populations: `CLUSTERS.md`, `CLUSTER_INDEX.csv`.

## 6. Owner check

`OWNER_CHECK.md`: 20 questions over 63 rows, grouped by event (release act; build and signing; notarization; publication; CI and release jobs; attestation, SBOM and build matrix; packaged proofs; manual reviews). It includes the owner-reported fact that v3.0.1 was notarized, as a statement to confirm (not applied). HELP_HUMAN puts it to the owner before any R4 packet is drafted.

## 7. Independent spot check

- Items checked: 338 over 271 row-samples — S1 178 rows (5.0% of 3,568, stratified by package × Disposition); S2 65 of 194 AUTHORITY_CONFLICT/UNKNOWN rows (all 40 mandatory + 25 in order; at least 20 required); S3 28 REMAP_LOG entries.
- Totals: CONFIRMED 315, REFUTED 12, UNDECIDED 11, UNVERIFIABLE 0.
- S3 re-mappings: CONFIRMED 29, REFUTED 0, UNDECIDED 1. Refuted items whose checked value came from an R3 re-mapping: 0 → second REMAP_LOG pass reverts 0.
- 12 refutations hit sealed (or errata/corrected) values that R3 did not re-map; they are not changed by R3 and are carried to R4 as contested items (table below).

## 8. Manager's notes (hand-written)

**How the final values were built.** Precedence is applied by script (`_scripts/r3_build.py`) in this order:
1. the sealed ledger of record;
2. errata. Two DEL-09-03 errata were rejected by CORRECTIONS, so their sealed values stand;
3. CORRECTIONS;
4. R3 re-mappings, in order:
   - run-wide reach calls (a) and (b);
   - R4-Q1 re-derivation under Addendum 6 rule 3 and Addendum 8 (91 rows by script, the rest by T2);
   - plain R4 mapped to R4-Q4, R4-Q5 or R4-Q6 (T1);
   - the Addendum 5 tie-break (T5);
   - Addendum 10 owner checks (T3);
   - run-wide disposition calls (c) to (f) (T4B, T6, T2B, and three manager consistency fixes).

Every step is a REMAP_LOG line. The QA replay rebuilds the final census from the sealed census.

Some CORRECTIONS values are prose rather than a field value. For evidence cells, that prose is appended to the sealed cell instead of replacing it, so no sealed citation is lost. T2 flagged three cells where an earlier build had lost citations. The rule was fixed before the final build.

**Open contested items (carried to R4; R3 did not resolve them).**
- **Owner-deferred:** DEL-06-02#CLM-005 and #CLM-032. Both workers' verdicts are in `AltReading` (CL-01).
- **Sealed AUTHORITY_CONFLICT rows the verifiers read as needing no owner decision:** DEL-09-04#CLM-022, #CLM-023.3 and DEL-06-04#STATE-2. R3 kept the Disposition and restored `R4` for MR-11 consistency (CL-03 and CL-04 notes).
- **"Claude/Anthropic default" statement:** AUTHORITY_CONFLICT on 11 rows and STALE_SPECIFICATION on 23. Both readings are in Notes (call d, ED).
- **R4-Q6 scope, narrow or broad:**
  - Narrow means the listed clauses. Broad means DIRECTIVE versus D-GOV-43 generally, including K-PERM-3/4/5, K-NET-1 and DIRECTIVE §8.
  - About 13 T1 rows and about 70 T4B "adjacent" rows depend on which reading applies.
  - The spot check found 4 Full-access rows that lack R4-Q6.
- **Spot check:** 12 sealed values were refuted and 11 items were left UNDECIDED (`R3_SPOT_CHECK.md`). None of those values came from an R3 re-mapping, so R3 reverted nothing.
- **Items the R3 tasks left undecided:**
  - DEL-09-05#CLM-010.8: Addendum 10 (OC-05);
  - DEL-04-01#CLM-004.2 and DEL-06-06#STATE-2: tie-break;
  - DEL-06-03#CLM-010.4: subject test;
  - DEL-04-04#CLM-024 and DEL-04-05#CLM-024: R4-Q1.
  - Current values stand, and both readings are in the task files.
- **Rule 2b reading behind 9 tie-break moves:** T5 read rule 2b as covering text that is false only about the register itself. Nine moves to REMAINING_STATE_MISMATCH rest on that reading. The manager accepted it; the owner may reverse it.

**What R3 could not resolve.**
- **Rule 3 on mixed evidence:** a claim can be judged whole or part by part when live code meets part of it. 428 rows carry both LIVE and LEGACY_ONLY tags and keep their sealed R4-Q1.
- **Reach, two readings:** the evidence pack reads module-level; R3 call (a) reads symbol-level. R3 applied symbol-level. REACHABILITY.csv is unchanged.
- **Call (c):** the D-GOV-16 conversion records sit in Root `execution/`, outside the evidence roots. So 16 VER-001 rows stay UNKNOWN pending the owner (OC-20). Nine AC-001 ALIGNED rows had no parity recompute.
- **Call (g):** the RUN_BASIS §5 flags for D-APP-104, 107, 122 and 123 are stale, because their effects landed. This is recorded as a finding; RUN_BASIS belongs to HELP_HUMAN. D-APP-125 item 3 and D-APP-126 are retired by D-APP-127, not pending.
- **Regex-built key lists:** XPF-020, -022, -048 and -050 list keys found by regex. They are candidates, not reviewed row by row.
- **Validator scope:** `_scripts/validate_ledger.py` validates per-deliverable ledger files. It does not apply to the merged concordance, which has 5 extra columns. Its checks are covered in `COVERAGE_AND_QA.md`.

**Owner check applied (R4 step 1).** The owner's answers (RUN_BASIS Addendum 13) were applied through `_work/DEC_OWNERCHECK.csv` (Source `OWNER_CHECK`, appended after all R3 lines in `REMAP_LOG.csv`). Two decided rows moved from `UNKNOWN`; every listed row carries an `OWNER_TESTIMONY`, `OWNER_BELIEF` or OC-08 note; `don't know` rows stay `UNKNOWN`. Row-by-row changes, noted rows for R4 attention and checks: `OWNER_CHECK_APPLIED.md`.

## Output hashes (SHA-256)

- `CLAIM_CONCORDANCE.csv` `a6f6cdda685173cac3aa8ab75d8dd823143feadbde2c44a755571337936dd852`
- `EXTENSION_CONCORDANCE.csv` `eeaaf27fcba05f2b8a16c6429a95be220b071c2b8938c41a3d5ff959854dbb37`
- `REVERSE_CONCORDANCE.csv` `2f07bfd122d88375c138d5a4ee86ef0023ebc06c9ada164ab41962e1f6648022`
- `REMAP_LOG.csv` `e53c0122d6c70c4ec91dde72232f4660e8475799ba2bbf7b0bdffe66e9150cd9`
- `INPUT_MANIFEST.md` `9f7f1b2755d89c3315a0959bb8c85ea197a907228a722bcc3407ed5dbc0037b9`
- `RUNWIDE_CALLS.md` `8c6108448332d677a0ee9b915100f56d0449c317fb17f8da3c20278dfc1a9546`
- `COVERAGE_AND_QA.md` `ccc03c6317babc0ad7a25723de72c8cd1fdb95e73ea41d91029e3da17d8c1cfa`
- `UNMAPPED_IMPLEMENTATION.csv` `be3af4989fb9fb6f06593122a2c715d25f1bc2fcf8838c48aa76ce872c18a833`
- `COVERAGE_GAPS.csv` `8250a77a0968006bd80a4c87aa8b32f7d437c3f9f515ae6cc576f183c43bc5c4`
- `CROSS_PACKAGE_FINDINGS.csv` `2aec4e02ae8c8fad1459213940ffb2be11f04b2cf015a88b21c92fd9f82c4113`
- `CLUSTERS.md` `13c14004d201e20560c1283176a56894d0754ef7675a5555448767350d5141be`
- `CLUSTER_INDEX.csv` `9efe82c66a7173af17ba14087d539544d13d24fee1563c3ab7506740c977c046`
- `OWNER_CHECK.md` `1a4f4e43ccd442b755e824a852fcd8283902a6fdf28fb2f3e532d13aed2dbc86`
- `R3_SPOT_CHECK.md` `002886987f564f57b3943c6f1d9c593c5283f60878c01e8f61ca398b72074e98`
