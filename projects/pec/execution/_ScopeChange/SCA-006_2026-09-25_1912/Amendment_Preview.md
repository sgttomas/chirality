---
amendment_id: SCA-006
doc_kind: scope_change.amendment_preview
decomp_variant: SOFTWARE
checkpoint_group: 2
created: 2026-09-25
status: candidate_awaiting_checkpoint_2_acceptance
accepted_impact_assessment_sha256: 93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691
accepted_intake_sha256: c5f90801989ee9948ccdd375917ba052fdb5838183e387ed373d8c7c2b824891
---

# SCA-006 — checkpoint-group-2 exact amendment preview

## Approval unit and boundary

This is the exact, diff-style amendment of PEC's SOFTWARE decomposition (revision 1.5 → 1.6) proposed for checkpoint group 2. It is a preview only: no live decomposition, register, PRD, `projects/pec/AGENTS.md`, SOW, `_CONTEXT.md`, `_STATUS.md`, `Dependencies.csv`, pointer or `v2/**` byte has changed. Every diff below is computed from the live preimages and the candidate postimages under `CP2_CANDIDATE/_Decomposition/`, and every changed byte of the five decomposition files is shown under the action that drives it. The hunks are a reading aid and also mechanically exact: each markdown hunk is an exact string replacement (its `-` lines are the old text and its `+` lines the new text; some start or end mid-line, and inserted rows carry their anchor row as context), and applying them in document order to the live `SOFTWARE_DECOMP.md` yields the candidate byte-for-byte. Register rows are shown as replaced or inserted rows with their stated insertion point; every register row not shown is byte-identical, with physical row order preserved. The candidate files and their SHA-256 values below are what the owner accepts.

Basis consumed: the accepted group-1 snapshot `checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/` (owner act "SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded"), and the accepted Impact Assessment and intake at the hashes above. This preview realizes the D group (intake Seq 18–43) with the texts of the manager's shared checkpoint-2 drafting canon for B5; the K group (Seq 1–13) and the I group (Seq 14–17) are in their own diff documents (§8), and the derivative advisories (Seq 44–54) are listed in §12. Section anchors `A-NN` are the `ActionSeq` of the intake.

## Byte preconditions and postimages

| Surface | Preimage SHA-256 (live, revision 1.5 / PRD v2.3) | Candidate postimage SHA-256 |
|---|---|---|
| `_Decomposition/SOFTWARE_DECOMP.md` | `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` | `4eed1247de47d1921e5526ef5027c12d504bffd4b8393b59645bb973fac62d71` |
| `_Decomposition/ScopeLedger.csv` | `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df` | `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e` |
| `_Decomposition/Deliverables.csv` | `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a` | `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805` |
| `_Decomposition/ContextBudgetQA.csv` | `2a1941050d06e5e07f6cde629d0abf0c2d80acde1983139e6c1918cfca9eb0df` | `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c` |
| `_Decomposition/Companion_Inventory.csv` | `7c8a24a868ff03415c4440055dc099aaf7e2d87cca8dc0267e77d1a676976ef8` | `1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662` |
| `docs/PRD.md` | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` | `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` |
| `projects/pec/AGENTS.md` | `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` | `49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d` (`CP2_CANDIDATE/AGENTS.candidate.md`, with the I1 corrections; recommended) or `a8b8d906f7df22f35fc8489a04fcb5476700e919af896c8256c0b713bf961188` (`CP2_CANDIDATE/AGENTS.candidate_without_I1.md`), per owner question Q-CP2-1; applied only through the checkpoint-3 instruction tranche |
| `_Decomposition/_LATEST.md` — not in the approval unit; rewritten only after checkpoint-3 acceptance (A-43) | `626feaafa213c3fe4995640a42a0a7606a1bd89a200ebf2e588afd4209a212dd` | none |

Any preimage mismatch before application invalidates this preview and returns the package to checkpoint 2.

### Acceptance-bound tokens and the pre-acceptance application state

The candidate carries its final accepted-state text (SCA-004 and SCA-005 precedent). The tokens below are acceptance-bound slots that take the actual checkpoint-3 acceptance date; no other byte may change. **Hash rule:** the SHA-256 values in this package are computed with every slot at its default `2026-09-25`. When a slot takes a different actual value, the verifier substitutes the actual value at exactly these loci, recomputes SHA-256, compares it with the written file, and records both the accepted hash and the slot-substituted hash. The PRD and `projects/pec/AGENTS.md` slots (including the group-2 folder token `SCA-006_GROUP-2_2026-09-25`) are listed in their own diff documents (§8); the decomposition candidate carries no group-2 folder token.

| File | Location | Token |
|---|---|---|
| `SOFTWARE_DECOMP.md` | front matter `date:` | `2026-09-25` (checkpoint-3 acceptance date; byte-identical to revision 1.5 at the default, so no hunk) |
| `SOFTWARE_DECOMP.md` | front matter `accepted:` | `2026-09-25` (checkpoint-3 acceptance date) |
| `SOFTWARE_DECOMP.md` | §7 `Revision` row | `2026-09-25` |
| `SOFTWARE_DECOMP.md` | §11 DL-21 date cell | `2026-09-25` |

Dates inside DL-21 prose ("the owner's R-A ruling and direct-query answer of 2026-09-25", "accepted at checkpoint 1 on 2026-09-25") and the "revision 1.5 (accepted 2026-09-25)" clause below record acts that have occurred; they are not slots.

Application during checkpoint-3 preparation writes the decomposition postimage with exactly two front-matter lines in their pre-acceptance form; the owner's checkpoint-3 acceptance restores them to the postimage values above:

```text
status: candidate_pending_checkpoint_3
accepted: not yet accepted — revision 1.6 applied during SCA-006 checkpoint-3 preparation; revision 1.5 (accepted 2026-09-25) remains the accepted basis until the owner's checkpoint-3 acceptance
```

Pre-acceptance variant SHA-256: `3ad0de686616f895c5fc63cceccef15dca3cd45ba1ca154d9797c2b9551f8a8b` (differs from the candidate in those two lines only).

### Mechanical proof

- Preview proof: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/B5/decomp/prove_preview.py` (SHA-256 `739834a2b19611f29a9abaf1e38bd6aa6293efae956b2a3c982deeb6219145bc`), run from `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/B5/decomp` as `python3 /private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/B5/decomp/prove_preview.py` (interpreter Python 3.13.7). It applies every `SOFTWARE_DECOMP.md` hunk of this file as an exact string replacement, in document order, to the live preimage (asserting each old text occurs exactly once) and asserts the candidate byte-for-byte; rebuilds each register from its live preimage using only the rows shown here (replace / insert after the stated row) and asserts the candidate CSV byte-for-byte; checks the preimage and candidate SHA-256 values in the table above and the pre-acceptance variant hash; and checks that each of A-18..A-43 appears exactly once. Result: exit code 0; 43 markdown hunks and 17 register rows verified.
- Counts and mirrors: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/B5/decomp/prove_counts.py` (SHA-256 `1876deaa319260c0c1e187cabc81653cbe1b5478b4e0abd52f77f756271652c6`), `python3 prove_counts.py <dir> --label L [--baseline counts_live.json]`; exit 0 on the candidate against the live baseline (no mirror disagreement that revision 1.5 does not already carry; the ten pre-existing SSOW-vs-ledger notes/order differences are listed in §11).
- Candidate builder: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/B5/decomp/build_candidate.py` (SHA-256 `5043f06b9e125bd13058040554fa2a71e5de07315279649b1a1573bf693460f0`). The scratchpad is session-local; the manager may preserve these scripts with the package.

## Final action set

`Amendment_Actions_CP2.csv` holds **54 actions: 12 ADD / 42 MODIFY** (0 REMOVE / RECLASSIFY / MERGE / SPLIT). It is the accepted intake exactly: every intake Seq 1–54 is carried with the same ActionSeq, ActionType, EntityType and EntityID, and nothing is dropped or added. The owner's selections (DQ-a, ENV-a, BUD-a, GATE-a, INS-a; R-C excluded) are the intake's recommended set, so no option delta of Impact Assessment §13 applies. Each row's Description states its scope, cites its intake Seq and points to its exact text (the candidate text itself for the ADDed scope items and vocabulary rows).

Differences from the intake rows, all within their accepted scope:

- **Seq 54 narrowed.** The exact candidate breaks exactly two EvidenceQuote cells, DEP-09-06-003 and DEP-10-03-003 (both quote the DEL-08-01 description). The canon keeps the DEL-08-03 first sentence and the PKG-08 charter as byte-identical prefixes, so DEP-09-06-004 and DEP-10-12-004 stay verbatim. The DEL-10-12 register leaves `AffectedFiles`.
- **Seq 49, 51, 52, 53 routing.** Their `DownstreamReruns` name graph node S4 (Seq 49, 51) or D1 (Seq 52, 53), each held until checkpoint 3, following the work graph's more conservative hold (`Propagation_Plan.md` §B4).
- **`SupersessionBindingPresent`.** 16 rows are `YES` (Seq 1, 2, 3, 5–12, 14, 18, 20–22), matching the 16 rows of `Supersession_Delta.csv` (`Propagation_Plan.md` §"Supersession binding policy").
- **Pure mirrors attributed to their action** (listed by the drafter; no new action): the §1.2 validation-obligations sentence and the P3 build-shape line (A-19, mirroring Seq 8/27 and Seq 9); the §3 intro instrument sentence (A-36); the vocabulary row `orientation` (PEC-ORI-001..007, A-39); the §2 intro sentence on SOW-097..100 (A-24, SCA-005 A-08 precedent); the DEL-08-03 envelope note that records the S → M re-assessment (A-32); and DEL-08-06's ContextBudgetQA risk `MEDIUM` / "Hold envelope; re-assess on the linked OI's ruling" (A-28, the DL-14 rule for deliverables coupled to an open issue, here OI-006).

## 1. Change Register (Decision Log, Revision History, front matter, references)

### A-43 — MODIFY OTHER `SCA-006`

Traceability: front matter revision 1.6 (date and accepted acceptance-bound; pre-acceptance lines per this preview), session_authorization, source_corpus and §1.5 R1 → PRD v2.4, R6 + D-PEC-90, DL-21, revision 1.6 row, §7 Revision, Companion_Inventory row counts; `_Decomposition/_LATEST.md` and `_ScopeChange/_LATEST.md` move only after checkpoint-3 acceptance; the §1.4 Gate-1 intake posture stays as history. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — FM revision (Seq 43):

```diff
-revision: "1.5"
+revision: "1.6"
```

`SOFTWARE_DECOMP.md` — FM accepted (Seq 43):

```diff
-accepted: 2026-09-25 (original Gate 7 owner ruling under D-PEC-60; revision 1.5 successor accepted through SCA-005 under the owner's checkpoint-group-3 audited-poststate acceptance)
+accepted: 2026-09-25 (original Gate 7 owner ruling under D-PEC-60; revision 1.6 successor accepted through SCA-006 under the owner's checkpoint-group-3 audited-poststate acceptance)
```

`SOFTWARE_DECOMP.md` — FM session_authorization (Seq 43):

```diff
-then by SCA-005 under D-PEC-86 and the owner's SCA-005 checkpoint acceptances
+by SCA-005 under D-PEC-86 and the owner's SCA-005 checkpoint acceptances, then by SCA-006 under D-PEC-90 R-A and the owner's SCA-006 checkpoint acceptances
```

`SOFTWARE_DECOMP.md` — FM source_corpus (Seq 43):

```diff
-source_corpus: projects/pec/docs/PRD.md (v2.3; v2.0 adopted by D-PEC-58, directed-bootstrap clarification adopted by D-PEC-61, exact PEC-K-03/-11 rows adopted by D-PEC-67, surrounding consumer-interface concordance adopted by D-PEC-68, v2.3 successor accepted through SCA-005 carrying the D-PEC-79 §16.3 loop-registry concordance with the SCA-005 feed-model and Runtime-topology concordance)
+source_corpus: projects/pec/docs/PRD.md (v2.4; v2.0 adopted by D-PEC-58, directed-bootstrap clarification adopted by D-PEC-61, exact PEC-K-03/-11 rows adopted by D-PEC-67, surrounding consumer-interface concordance adopted by D-PEC-68, v2.3 successor accepted through SCA-005 carrying the D-PEC-79 §16.3 loop-registry concordance with the SCA-005 feed-model and Runtime-topology concordance, the v2.4 successor accepted through SCA-006 carrying the D-PEC-90 operational-reliance direction)
```

`SOFTWARE_DECOMP.md` — §7 Revision (Seq 43):

```diff
-| Revision | 1.5, 2026-09-25 (SCA-005) |
+| Revision | 1.6, 2026-09-25 (SCA-006) |
```

`SOFTWARE_DECOMP.md` — §11 ADD DL-21 (Seq 43):

```diff
-| DL-20 | 2026-09-25 | SCA-005, requested by owner Ryan Tufts and opened by D-PEC-86, accepted at checkpoint 1 on 2026-09-24 with amendment 1 (TM-PEC-023 selections; cmux deferral) and amendment 2 (SOW-033 → OBJ-003), re-bases the feed model on the shared development-loop method and the application-owned Runtime topology (D-GOV-43 A2): it adds SOW-095/096 and DEL-02-08/09 (work-graph and MEMORY run-index parsers, P1, OBJ-001;OBJ-002); re-sources SOW-001/004/013..017 and DEL-01-01, DEL-02-03..07, DEL-03-03 and DEL-04-01; declares closed, PEC-versioned feed profiles on registry rows (SOW-077/094, DEL-01-06; a strict schema v2 by a later D-PEC source packet within D-PEC-78 O-A) and makes `adapter.yaml` a parity-peer input; moves SOW-029, SOW-035 and SOW-087 (trigger T-RT) and SOW-037 (later owner direction) to Deferred OUT and retires DEL-06-04, DEL-07-02, DEL-07-04 and DEL-07-05 non-destructively; records the owner's TM-PEC-023 selections and the SOW-033 mapping, so no IN item lacks an objective (SOW-063's mapping supersedes DL-14's objective-free rationale); and re-expresses C5, C13, R4, SOW-026/034/049/074/076/080/082/083/092, OI-002/006/008/009, PKG-00/02/06/07, the telemetry and the vocabulary. The source corpus moves to PRD v2.3 | Invariants preserved: 11 packages and 6 objectives; every stable ID, name and path retained (CP1-N) and the new IDs append-only; retired rows kept for register integrity; no IN item without package, deliverable or objective; the union invariant holds; the §16 decisions stay open (Q6); C3, C15 and SOW-058 unchanged. Dependency registers, `_CONTEXT.md` and `_REFERENCES.md` metadata, Scope of Work contracts, lifecycle and source remain downstream of this amendment |
+| DL-20 | 2026-09-25 | SCA-005, requested by owner Ryan Tufts and opened by D-PEC-86, accepted at checkpoint 1 on 2026-09-24 with amendment 1 (TM-PEC-023 selections; cmux deferral) and amendment 2 (SOW-033 → OBJ-003), re-bases the feed model on the shared development-loop method and the application-owned Runtime topology (D-GOV-43 A2): it adds SOW-095/096 and DEL-02-08/09 (work-graph and MEMORY run-index parsers, P1, OBJ-001;OBJ-002); re-sources SOW-001/004/013..017 and DEL-01-01, DEL-02-03..07, DEL-03-03 and DEL-04-01; declares closed, PEC-versioned feed profiles on registry rows (SOW-077/094, DEL-01-06; a strict schema v2 by a later D-PEC source packet within D-PEC-78 O-A) and makes `adapter.yaml` a parity-peer input; moves SOW-029, SOW-035 and SOW-087 (trigger T-RT) and SOW-037 (later owner direction) to Deferred OUT and retires DEL-06-04, DEL-07-02, DEL-07-04 and DEL-07-05 non-destructively; records the owner's TM-PEC-023 selections and the SOW-033 mapping, so no IN item lacks an objective (SOW-063's mapping supersedes DL-14's objective-free rationale); and re-expresses C5, C13, R4, SOW-026/034/049/074/076/080/082/083/092, OI-002/006/008/009, PKG-00/02/06/07, the telemetry and the vocabulary. The source corpus moves to PRD v2.3 | Invariants preserved: 11 packages and 6 objectives; every stable ID, name and path retained (CP1-N) and the new IDs append-only; retired rows kept for register integrity; no IN item without package, deliverable or objective; the union invariant holds; the §16 decisions stay open (Q6); C3, C15 and SOW-058 unchanged. Dependency registers, `_CONTEXT.md` and `_REFERENCES.md` metadata, Scope of Work contracts, lifecycle and source remain downstream of this amendment |
+| DL-21 | 2026-09-25 | SCA-006, opened under `D-PEC-90` R-A grant item 3 (the owner's R-A ruling and direct-query answer of 2026-09-25) and accepted at checkpoint 1 on 2026-09-25 with DQ-a, ENV-a, BUD-a, GATE-a and INS-a (R-C excluded), writes operational reliance on PEC data into the decomposition: C3 is re-expressed (a consumer may act on a record-tier claim within the pin, coverage and tier the response declares, with file fallback, only from a release that has passed the §12 reliance-advertisement gate; non-authoritative is kept in the authority sense); it adds SOW-097 (reliance envelope, PEC-ORI-007 → DEL-04-03), SOW-098 (response-size budgets, PEC-API-006 → DEL-08-03), SOW-099 (agent tool-call query surface, PEC-API-007 → new DEL-08-06, P3) and SOW-100 (the standing reliance-advertisement gate, §12 → new DEL-10-13, P1), all mapped to OBJ-001 and SOW-097 also to OBJ-002; adds the read-only `agent` access class to SOW-003 and DEL-08-01, enabled agent tool-call surfaces to SOW-060, and `agent` credentials to the open SOW-080 / OI-006 premise; re-envelopes DEL-08-03 S → M; and re-expresses §1.2, PKG-04/08/10, the OBJ-001/OBJ-002 views, the telemetry and the vocabulary (+operational reliance, reliance envelope, response budget; `harness` modified). The source corpus moves to PRD v2.4 | Invariants preserved: 11 packages and 6 objectives with unchanged statements; every stable ID, name and path retained and the new IDs append-only; no IN item without package, deliverable or objective; the union invariant holds; C1, C2 and C15 (PEC-K-01, PEC-K-02, PEC-K-11) unchanged and PEC output stays never citable as authority (R-C not selected); the token mechanism stays open (OI-006); the §12 P1 row is not edited (GATE-a). Dependency registers, `_CONTEXT.md` and `_REFERENCES.md` metadata, Scope of Work contracts, lifecycle and source remain downstream of this amendment |
```

`SOFTWARE_DECOMP.md` — §12 ADD revision 1.6 (Seq 43):

```diff
-| 1.5 | SCA-005 | Feed-model and Runtime-topology rebaseline under D-PEC-86: +SOW-095/096 and +DEL-02-08/09; SOW-029/035/037/087 IN→OUT Deferred and DEL-06-04/07-02/07-04/07-05 retired non-destructively; registry feed profiles; `adapter.yaml` parity-peer only; TM-PEC-023 selections and the SOW-033 mapping (0 IN items without objective); C5/C13, R4, SSOW rows, PKG-00/02/06/07, deliverable descriptions, §16 premises, vocabulary (26 terms), telemetry and envelope posture (S 28 / M 32 / L 2) reconciled; PRD v2.3 source; stable IDs, names and paths retained |
+| 1.5 | SCA-005 | Feed-model and Runtime-topology rebaseline under D-PEC-86: +SOW-095/096 and +DEL-02-08/09; SOW-029/035/037/087 IN→OUT Deferred and DEL-06-04/07-02/07-04/07-05 retired non-destructively; registry feed profiles; `adapter.yaml` parity-peer only; TM-PEC-023 selections and the SOW-033 mapping (0 IN items without objective); C5/C13, R4, SSOW rows, PKG-00/02/06/07, deliverable descriptions, §16 premises, vocabulary (26 terms), telemetry and envelope posture (S 28 / M 32 / L 2) reconciled; PRD v2.3 source; stable IDs, names and paths retained |
+| 1.6 | SCA-006 | Operational reliance on PEC data under D-PEC-90 R-A: C3 re-expressed; +SOW-097..100 and +DEL-08-06/10-13 (reliance envelope, response-size budgets, agent tool-call query surface, reliance-advertisement gate); read-only agent access class (SOW-003, DEL-08-01); SOW-060/080 and OI-006 extended; DEL-04-03/08-03 descriptions and coverage, DEL-08-03 S→M; PKG-04/08/10, OBJ-001/002 views, §1.2, vocabulary (29 terms), telemetry and envelope posture (S 28 / M 34 / L 2) reconciled; PRD v2.4 source; stable IDs, names and paths retained |
```

`SOFTWARE_DECOMP.md` — §1.5 R1 source reference (Seq 43):

```diff
-| R1 | `projects/pec/docs/PRD.md` (v2.3; lineage ruled through `D-PEC-58`, `D-PEC-61`, `D-PEC-67`, and `D-PEC-68`, with the `D-PEC-79` §16.3 concordance carried into the v2.3 successor accepted through SCA-005) | Source corpus |
+| R1 | `projects/pec/docs/PRD.md` (v2.4; lineage ruled through `D-PEC-58`, `D-PEC-61`, `D-PEC-67`, and `D-PEC-68`, with the `D-PEC-79` §16.3 concordance carried into the v2.3 successor accepted through SCA-005 and the `D-PEC-90` operational-reliance direction carried into the v2.4 successor accepted through SCA-006) | Source corpus |
```

`SOFTWARE_DECOMP.md` — §1.5 R6 decision references (Seq 43):

```diff
-| R6 | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-57..68` | Pivot, adoption, decomposition, directed bootstrap, exact consumer rows, and v2.2 concordance |
+| R6 | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-57..68`, `D-PEC-90` | Pivot, adoption, decomposition, directed bootstrap, exact consumer rows, v2.2 concordance, and operational reliance on PEC data (`D-PEC-90` R-A) |
```

`Companion_Inventory.csv` row `ScopeLedger.csv` (replace):

```diff
-ScopeLedger.csv,authoritative companion register,96-row SOW->PKG->DEL->OBJ ledger with DecisionRef and OpenIssue columns; authoritative for assignments
+ScopeLedger.csv,authoritative companion register,100-row SOW->PKG->DEL->OBJ ledger with DecisionRef and OpenIssue columns; authoritative for assignments
```

`Companion_Inventory.csv` row `Deliverables.csv` (replace):

```diff
-Deliverables.csv,authoritative companion register,"66-row deliverable register: descriptions, types, artifacts, Context Envelopes + notes, PhaseHint"
+Deliverables.csv,authoritative companion register,"68-row deliverable register: descriptions, types, artifacts, Context Envelopes + notes, PhaseHint"
```

## 2. Primary partitions — Packages

### A-33 — MODIFY PACKAGE `PKG-04`

PKG-04 charter adds the reliance envelope; assigned SOW-004..009, 097 (6 → 7). Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §4 PKG-04 (Seq 33):

```diff
-| PKG-04 | Orientation Services | Derivation and serving of orientation: per-loop returns, deltas since SHA, SHA/freshness stamping, per-claim citations, scope parameterization, explicit measurement limits | SOW-004..009 (6) | Transport (PKG-08); rendering (PKG-09) |
+| PKG-04 | Orientation Services | Derivation and serving of orientation: per-loop returns, deltas since SHA, SHA/freshness stamping, per-claim citations, scope parameterization, explicit measurement limits, and the reliance envelope | SOW-004..009, 097 (7) | Transport (PKG-08); rendering (PKG-09) |
```

### A-34 — MODIFY PACKAGE `PKG-08`

PKG-08 charter keeps its current text byte-for-byte as prefix and adds response-size budgets and the agent tool-call query surface; assigned SOW-003, 040..044, 098, 099 (6 → 8); §5 PKG-08 table gains DEL-08-06 (A-28). Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §4 PKG-08 (Seq 34):

```diff
-| PKG-08 | API & Access | The machine-consumer surface: Unix-socket binding, token-scoped access classes, p95 latency, versioned additive schema, compact citation-bearing responses, SSE subscription | SOW-003, 040..044 (6) | Dashboard rendering (PKG-09) |
+| PKG-08 | API & Access | The machine-consumer surface: Unix-socket binding, token-scoped access classes, p95 latency, versioned additive schema, compact citation-bearing responses, SSE subscription, response-size budgets, and the agent tool-call query surface | SOW-003, 040..044, 098, 099 (8) | Dashboard rendering (PKG-09) |
```

### A-35 — MODIFY PACKAGE `PKG-10`

PKG-10 charter adds the reliance-advertisement gate; assigned + SOW-100 (12 → 13); §5 PKG-10 table gains DEL-10-13 (A-29). Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §4 PKG-10 (Seq 35):

```diff
-| PKG-10 | Validation & Measurement | Release-gating proof and metrics: kill test, no-ruling-write verification, Step-0 baseline, defect/adoption/collision/parity measurement, seeded-conflict, TTL-honesty and stream-loss tests, usage observability, directed bootstrap progression evidence | SOW-025, 055, 058..064, 084, 085, 093 (12) | The behaviors under test (their home packages) |
+| PKG-10 | Validation & Measurement | Release-gating proof and metrics: kill test, no-ruling-write verification, Step-0 baseline, defect/adoption/collision/parity measurement, seeded-conflict, TTL-honesty and stream-loss tests, usage observability, directed bootstrap progression evidence, and the reliance-advertisement gate | SOW-025, 055, 058..064, 084, 085, 093, 100 (13) | The behaviors under test (their home packages) |
```

## 3. Secondary entities — Deliverables (additions and modifications)

### A-28 — ADD DELIVERABLE `DEL-08-06`

ADD DEL-08-06 'Agent tool-call query surface' (PKG-08, BACKEND_FEATURE_SLICE, M, P3, covers SOW-099, OBJ-001) plus ContextBudgetQA row (M / MEDIUM), inserted after DEL-08-05; §5 PKG-08 mirror. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §5 PKG-08 ADD DEL-08-06 (Seq 28):

```diff
-| DEL-08-05 | SSE delta/presence subscription | BACKEND_FEATURE_SLICE | M | P4 | SOW-044 |
+| DEL-08-05 | SSE delta/presence subscription | BACKEND_FEATURE_SLICE | M | P4 | SOW-044 |
+| DEL-08-06 | Agent tool-call query surface | BACKEND_FEATURE_SLICE | M | P3 | SOW-099 |
```

`Deliverables.csv` row `DEL-08-06` (insert after `DEL-08-05`):

```diff
+DEL-08-06,PKG-08,Agent tool-call query surface,"Read-only query interface packaged for agent tool calls over the versioned API and responses, bound to the read-only agent access class; enabling it is consumer-owned; writes nothing.",BACKEND_FEATURE_SLICE,TBD,Tool definitions over the read API + access-class binding + tests,SOW-099,OBJ-001,M,Token mechanism follows OI-006; the tier-0 profile is amended before any tool is declared or invoked,P3
```

`ContextBudgetQA.csv` row `DEL-08-06` (insert after `DEL-08-05`):

```diff
+DEL-08-06,PKG-08,M,MEDIUM,Hold envelope; re-assess on the linked OI's ruling,Token mechanism follows OI-006; the tier-0 profile is amended before any tool is declared or invoked
```

### A-29 — ADD DELIVERABLE `DEL-10-13`

ADD DEL-10-13 'Reliance-advertisement gate' (PKG-10, TEST_SUITE, S, P1, covers SOW-100, OBJ-001) plus ContextBudgetQA row (S / LOW), inserted after DEL-10-12; §5 PKG-10 mirror. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §5 PKG-10 ADD DEL-10-13 (Seq 29):

```diff
-| DEL-10-12 | Poll-adoption measurement | MEASUREMENT | S | P3 | SOW-060 |
+| DEL-10-12 | Poll-adoption measurement | MEASUREMENT | S | P3 | SOW-060 |
+| DEL-10-13 | Reliance-advertisement gate | TEST_SUITE | S | P1 | SOW-100 |
```

`Deliverables.csv` row `DEL-10-13` (insert after `DEL-10-12`):

```diff
+DEL-10-13,PKG-10,Reliance-advertisement gate,"Standing gate for any release that advertises operational reliance: composes DEL-03-04 parity, DEL-04-05 coverage honesty under seeded feed failures, the DEL-04-03 reliance envelope, the PKG-02 parser fixture suites and the DEL-10-02 kill test into one gate record; re-proved at each such release.",TEST_SUITE,TBD,Gate harness + gate record,SOW-100,OBJ-001,S,Binds the first release that advertises operational reliance; composes other packages' evidence and consumes no internals (as DEL-10-02),P1
```

`ContextBudgetQA.csv` row `DEL-10-13` (insert after `DEL-10-12`):

```diff
+DEL-10-13,PKG-10,S,LOW,None,Binds the first release that advertises operational reliance; composes other packages' evidence and consumes no internals (as DEL-10-02)
```

### A-30 — MODIFY DELIVERABLE `DEL-04-03`

DEL-04-03 description adds the reliance envelope; CoversScopeItems + SOW-097; envelope M and SupportsObjectives `OBJ-001;OBJ-002` unchanged; §5 mirror. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §5 DEL-04-03 (Seq 30):

```diff
-| DEL-04-03 | Citation & freshness stamping | BACKEND_FEATURE_SLICE | M | P1 | SOW-006, 007 |
+| DEL-04-03 | Citation & freshness stamping | BACKEND_FEATURE_SLICE | M | P1 | SOW-006, 007, 097 |
```

`Deliverables.csv` row `DEL-04-03` (replace):

```diff
-DEL-04-03,PKG-04,Citation & freshness stamping,"Per-claim citations (path/anchor/SHA) and response stamping (examined-through SHA, generation time, per-feed freshness).",BACKEND_FEATURE_SLICE,TBD,Citation layer + tests,SOW-006;SOW-007,OBJ-001;OBJ-002,M,,P1
+DEL-04-03,PKG-04,Citation & freshness stamping,"Per-claim citations (path/anchor/SHA) and response stamping (examined-through SHA, generation time, per-feed freshness), with the reliance envelope (pin, per-feed coverage and limitations, per-claim trust tier, file-fallback signal).",BACKEND_FEATURE_SLICE,TBD,Citation layer + tests,SOW-006;SOW-007;SOW-097,OBJ-001;OBJ-002,M,,P1
```

### A-31 — MODIFY DELIVERABLE `DEL-08-01`

DEL-08-01 description: access classes owner, harness, agent, admin (agent is read-only query for tool calls); envelope, notes and ContextBudgetQA row unchanged. Supersession binding: **NO**.

`Deliverables.csv` row `DEL-08-01` (replace):

```diff
-DEL-08-01,PKG-08,Unix-socket server + token-scoped access,"Local-only Unix-socket binding with token-scoped access classes (owner, harness, admin); auth-reuse choice tracked by OI-006.",SECURITY_CONTROL,TBD,Socket server + auth + tests,SOW-003;SOW-040,OBJ-001,M,"OI-006 determines the PEC-local token mechanism (Runtime token registries are private to each application's Runtime instance, so no shared registry exists to reuse); the socket+access-class core is stable either way, but the auth half may be reworked on ruling",P1
+DEL-08-01,PKG-08,Unix-socket server + token-scoped access,"Local-only Unix-socket binding with token-scoped access classes (owner, harness, agent, admin; agent is read-only query for tool calls); auth-reuse choice tracked by OI-006.",SECURITY_CONTROL,TBD,Socket server + auth + tests,SOW-003;SOW-040,OBJ-001,M,"OI-006 determines the PEC-local token mechanism (Runtime token registries are private to each application's Runtime instance, so no shared registry exists to reuse); the socket+access-class core is stable either way, but the auth half may be reworked on ruling",P1
```

### A-32 — MODIFY DELIVERABLE `DEL-08-03`

DEL-08-03 description appends the response-size budget sentence, keeping the current sentence byte-for-byte as its prefix; CoversScopeItems + SOW-098; envelope S → M, risk LOW kept (ContextBudgetQA re-assessed; the re-assessment note is written in both registers); §5 mirror. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §5 DEL-08-03 (Seq 32):

```diff
-| DEL-08-03 | Compact citation-bearing response format | API_CONTRACT | S | P1 | SOW-043 |
+| DEL-08-03 | Compact citation-bearing response format | API_CONTRACT | M | P1 | SOW-043, 098 |
```

`Deliverables.csv` row `DEL-08-03` (replace):

```diff
-DEL-08-03,PKG-08,Compact citation-bearing response format,Machine-first response envelope carrying citations.,API_CONTRACT,TBD,Format spec + serializer + tests,SOW-043,OBJ-001,S,,P1
+DEL-08-03,PKG-08,Compact citation-bearing response format,"Machine-first response envelope carrying citations. Responses are bounded by declared size budgets met by pagination or continuation, with any truncation stated.",API_CONTRACT,TBD,Format spec + serializer + tests,SOW-043;SOW-098,OBJ-001,M,"M under SCA-006: declared response-size budgets met by pagination or continuation, with stated truncation, join the compact citation-bearing format (SOW-043, SOW-098); kept one cohesive format slice",P1
```

`ContextBudgetQA.csv` row `DEL-08-03` (replace):

```diff
-DEL-08-03,PKG-08,S,LOW,None,
+DEL-08-03,PKG-08,M,LOW,None; single cohesive slice,"M under SCA-006: declared response-size budgets met by pagination or continuation, with stated truncation, join the compact citation-bearing format (SOW-043, SOW-098); kept one cohesive format slice"
```

## 4. Unit Ledger — Scope Ledger (statements and additions)

### A-20 — MODIFY OTHER `SOW-003`

SOW-003: three → four access classes (owner, harness, agent (read-only query for tool calls), admin); ledger DecisionRef `DL-11` → `DL-11; SCA-006`; §2.1 mirror. Supersession binding: **YES (D-020 in `Supersession_Delta.csv`)**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-003 (Seq 20):

```diff
-| SOW-003 | IN | Implement token-scoped access with three access classes: owner, harness, admin |
+| SOW-003 | IN | Implement token-scoped access with four access classes: owner, harness, agent (read-only query for tool calls), admin |
```

`ScopeLedger.csv` row `SOW-003` (replace):

```diff
-SOW-003,IN,"Implement token-scoped access with three access classes: owner, harness, admin",§8,PKG-08,DEL-08-01,OBJ-001,DL-11,FALSE,v1.0/prototype role ontologies retired
+SOW-003,IN,"Implement token-scoped access with four access classes: owner, harness, agent (read-only query for tool calls), admin",§8,PKG-08,DEL-08-01,OBJ-001,DL-11; SCA-006,FALSE,v1.0/prototype role ontologies retired
```

### A-21 — MODIFY OTHER `SOW-060`

SOW-060: candidate-consumer enablement names registered loops, harnesses and enabled agent tool-call surfaces (mirrors PRD §11 metric 4); ledger DecisionRef blank → `SCA-006`; Notes unchanged; §2.1 mirror. Supersession binding: **YES (D-021 in `Supersession_Delta.csv`)**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-060 (Seq 21):

```diff
-| SOW-060 | IN | Measure consumer uptake: candidate-consumer enablement and, among enabled consumers, orientation use against contact opportunities defined by their own adopted mode/cadence rules |
+| SOW-060 | IN | Measure consumer uptake: candidate-consumer enablement (registered loops, harnesses and enabled agent tool-call surfaces) and, among enabled consumers, orientation use against contact opportunities defined by their own adopted mode/cadence rules |
```

`ScopeLedger.csv` row `SOW-060` (replace):

```diff
-SOW-060,IN,"Measure consumer uptake: candidate-consumer enablement and, among enabled consumers, orientation use against contact opportunities defined by their own adopted mode/cadence rules","§11.4, §12 P3",PKG-10,DEL-10-12,OBJ-006,,FALSE,Measures uptake of SOW-004; no receiving-loop conformance criterion; supports the §11 falsification clause together with SOW-085
+SOW-060,IN,"Measure consumer uptake: candidate-consumer enablement (registered loops, harnesses and enabled agent tool-call surfaces) and, among enabled consumers, orientation use against contact opportunities defined by their own adopted mode/cadence rules","§11.4, §12 P3",PKG-10,DEL-10-12,OBJ-006,SCA-006,FALSE,Measures uptake of SOW-004; no receiving-loop conformance criterion; supports the §11 falsification clause together with SOW-085
```

### A-22 — MODIFY OTHER `SOW-080`

SOW-080 (TBD, OI-006): the open PEC-local token mechanism includes credentials for the agent access class; stays TBD; ledger DecisionRef `SCA-005` → `SCA-005; SCA-006`; §2.3 mirror. Supersession binding: **YES (D-022 in `Supersession_Delta.csv`)**.

`SOFTWARE_DECOMP.md` — §2.3 SOW-080 (Seq 22):

```diff
-| SOW-080 | TBD | Auth reuse: which PEC-local token mechanism PEC uses (premise: Runtime token registries are private to each application's Runtime instance, and reuse of an App registry is foreclosed by the Runtime consumer guide) |
+| SOW-080 | TBD | Auth reuse: which PEC-local token mechanism PEC uses, including credentials for the agent access class (premise: Runtime token registries are private to each application's Runtime instance, and reuse of an App registry is foreclosed by the Runtime consumer guide) |
```

`ScopeLedger.csv` row `SOW-080` (replace):

```diff
-SOW-080,TBD,"Auth reuse: which PEC-local token mechanism PEC uses (premise: Runtime token registries are private to each application's Runtime instance, and reuse of an App registry is foreclosed by the Runtime consumer guide)",§16.6,,,,SCA-005,TRUE,OI-006. Affects SOW-003 implementation choice
+SOW-080,TBD,"Auth reuse: which PEC-local token mechanism PEC uses, including credentials for the agent access class (premise: Runtime token registries are private to each application's Runtime instance, and reuse of an App registry is foreclosed by the Runtime consumer guide)",§16.6,,,,SCA-005; SCA-006,TRUE,OI-006. Affects SOW-003 implementation choice
```

### A-24 — ADD OTHER `SOW-097`

ADD SOW-097 (IN; PEC-ORI-007; PKG-04 / DEL-04-03 / OBJ-001;OBJ-002): declare the reliance envelope on every orientation response; appended after SOW-096; §2 intro and §2.1 mirrors. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §2 intro (SOW-097..100 appended) (Seq 24):

```diff
-SOW-095..096 were appended under SCA-005 from the PRD v2.3 feed list
-(DL-20). IDs are append-only, so family ordering is not semantic.
+SOW-095..096 were appended under SCA-005 from the PRD v2.3 feed list
+(DL-20), and SOW-097..100 under SCA-006 from PRD v2.4 (DL-21). IDs are
+append-only, so family ordering is not semantic.
```

`SOFTWARE_DECOMP.md` — §2.1 ADD SOW-097..100 (Seq 24-27) (Seq 24):

```diff
-| SOW-096 | IN | Parse deliverable `MEMORY.md` run-index entries (run-ID tokens, dates, link targets) in the template `## Runs` table, the observed bullet form and the dated-heading form, as RunRecord join evidence | PEC-RCN-002 (PRD v2.3), §7.1 RunRecord | New feed kind under SCA-005 (DL-4, DL-20); absence is a stated coverage limit (SOW-009); objectives per the DL-17 parser precedent |
+| SOW-096 | IN | Parse deliverable `MEMORY.md` run-index entries (run-ID tokens, dates, link targets) in the template `## Runs` table, the observed bullet form and the dated-heading form, as RunRecord join evidence | PEC-RCN-002 (PRD v2.3), §7.1 RunRecord | New feed kind under SCA-005 (DL-4, DL-20); absence is a stated coverage limit (SOW-009); objectives per the DL-17 parser precedent |
+| SOW-097 | IN | Declare the reliance envelope on every orientation response: pin (examined-through SHA), per-feed coverage and freshness with stated limitations, per-claim trust tier, and the file-fallback signal | PEC-ORI-007 | New under SCA-006 (D-PEC-90 R-A; ENV-a); distinct from SOW-006 stamping; an input to the reliance-advertisement gate (SOW-100) |
+| SOW-098 | IN | Bound responses by declared size budgets met by pagination or continuation; state any truncation; never drop citations, stamps or stated limitations | PEC-API-006 | New under SCA-006 (D-PEC-91 carry-forward; BUD-a); numeric budgets confirmed at P1; distinct from the latency budget (SOW-041) |
+| SOW-099 | IN | Offer a read-only query interface for agent tool calls over the versioned API under the agent access class; enabling it is consumer-owned | PEC-API-007, §8 | New under SCA-006 (D-PEC-90 owner answer; DQ-a); token mechanism OI-006; tier-0 profile amendment before any tool is declared or invoked; P3 |
+| SOW-100 | IN | Maintain the reliance-advertisement gate: before any release advertises operational reliance, prove harness parity clean or explained, complete coverage statements under seeded feed failures, the reliance envelope on every response, passing parser fixture suites and the kill test | §12, PEC-RCN-005, PEC-ORI-006, PEC-ORI-007 | Instrument (DL-6): distinct from the behaviours it tests (SOW-020, SOW-009, SOW-097, SOW-055); re-proved at each release that advertises operational reliance; the §12 P1 row is not edited (GATE-a) |
```

`ScopeLedger.csv` row `SOW-097` (insert after `SOW-096`):

```diff
+SOW-097,IN,"Declare the reliance envelope on every orientation response: pin (examined-through SHA), per-feed coverage and freshness with stated limitations, per-claim trust tier, and the file-fallback signal",PEC-ORI-007,PKG-04,DEL-04-03,OBJ-001;OBJ-002,SCA-006,FALSE,New under SCA-006 (D-PEC-90 R-A; ENV-a); distinct from SOW-006 stamping; an input to the reliance-advertisement gate (SOW-100)
```

### A-25 — ADD OTHER `SOW-098`

ADD SOW-098 (IN; PEC-API-006; PKG-08 / DEL-08-03 / OBJ-001): response-size budgets met by pagination or continuation, truncation stated; appended after SOW-097. Supersession binding: **NO**.

`ScopeLedger.csv` row `SOW-098` (insert after `SOW-097`):

```diff
+SOW-098,IN,"Bound responses by declared size budgets met by pagination or continuation; state any truncation; never drop citations, stamps or stated limitations",PEC-API-006,PKG-08,DEL-08-03,OBJ-001,SCA-006,FALSE,New under SCA-006 (D-PEC-91 carry-forward; BUD-a); numeric budgets confirmed at P1; distinct from the latency budget (SOW-041)
```

The §2.1 row is in the single §2.1 insertion shown under A-24.

### A-26 — ADD OTHER `SOW-099`

ADD SOW-099 (IN; PEC-API-007, §8; PKG-08 / DEL-08-06 / OBJ-001): read-only query interface for agent tool calls under the agent access class; appended after SOW-098. Supersession binding: **NO**.

`ScopeLedger.csv` row `SOW-099` (insert after `SOW-098`):

```diff
+SOW-099,IN,Offer a read-only query interface for agent tool calls over the versioned API under the agent access class; enabling it is consumer-owned,"PEC-API-007, §8",PKG-08,DEL-08-06,OBJ-001,SCA-006,FALSE,New under SCA-006 (D-PEC-90 owner answer; DQ-a); token mechanism OI-006; tier-0 profile amendment before any tool is declared or invoked; P3
```

The §2.1 row is in the single §2.1 insertion shown under A-24.

### A-27 — ADD OTHER `SOW-100`

ADD SOW-100 (IN; §12, PEC-RCN-005, PEC-ORI-006, PEC-ORI-007; PKG-10 / DEL-10-13 / OBJ-001): the standing reliance-advertisement gate, an instrument under DL-6; appended after SOW-099. Supersession binding: **NO**.

`ScopeLedger.csv` row `SOW-100` (insert after `SOW-099`):

```diff
+SOW-100,IN,"Maintain the reliance-advertisement gate: before any release advertises operational reliance, prove harness parity clean or explained, complete coverage statements under seeded feed failures, the reliance envelope on every response, passing parser fixture suites and the kill test","§12, PEC-RCN-005, PEC-ORI-006, PEC-ORI-007",PKG-10,DEL-10-13,OBJ-001,SCA-006,FALSE,"Instrument (DL-6): distinct from the behaviours it tests (SOW-020, SOW-009, SOW-097, SOW-055); re-proved at each release that advertises operational reliance; the §12 P1 row is not edited (GATE-a)"
```

The §2.1 row is in the single §2.1 insertion shown under A-24.

## 5. Objectives — objective mappings (ledger and deliverable in lockstep) and objective-side views

### A-36 — MODIFY OBJECTIVE `OBJ-001`

OBJ-001 objective-side view: + SOW-097, SOW-098, SOW-099 and instrument SOW-100; + DEL-08-06, DEL-10-13; statement unchanged. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §3 OBJ-001 view (Seq 36):

```diff
-| OBJ-001 | Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation | §3.1 | SOW-001, SOW-003..009, SOW-011..017, SOW-038, SOW-040..044, SOW-089, SOW-095, SOW-096; instruments: SOW-058, SOW-059, SOW-063 | DEL-00-03, DEL-01-01, DEL-02-01..09, DEL-03-05, DEL-04-01..05, DEL-08-01..05, DEL-10-01, DEL-10-04, DEL-10-08 |
+| OBJ-001 | Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation | §3.1 | SOW-001, SOW-003..009, SOW-011..017, SOW-038, SOW-040..044, SOW-089, SOW-095..099; instruments: SOW-058, SOW-059, SOW-063, SOW-100 | DEL-00-03, DEL-01-01, DEL-02-01..09, DEL-03-05, DEL-04-01..05, DEL-08-01..06, DEL-10-01, DEL-10-04, DEL-10-08, DEL-10-13 |
```

`SOFTWARE_DECOMP.md` — §3 intro instruments sentence (mirror of Seq 36) (Seq 36) — mirror edit beyond the literal intake description (step-8 list):

```diff
-items; the §11/§12 measurement items (SOW-058..063, 084, 085) are the
-test instruments.
+items; the §11/§12 measurement items (SOW-058..063, 084, 085) and the §12
+reliance-advertisement gate (SOW-100) are the test instruments.
```

### A-37 — MODIFY OBJECTIVE `OBJ-002`

OBJ-002 objective-side view: + SOW-097; statement unchanged; deliverable side unchanged (DEL-04-03 already present). Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §3 OBJ-002 view (Seq 37):

```diff
-| OBJ-002 | Staleness is detected structurally by SHA comparison, never by judgment | §3.2 | SOW-001, SOW-006, SOW-011..019, SOW-095, SOW-096; supported by SOW-005 | DEL-01-01, DEL-02-01..09, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03 |
+| OBJ-002 | Staleness is detected structurally by SHA comparison, never by judgment | §3.2 | SOW-001, SOW-006, SOW-011..019, SOW-095..097; supported by SOW-005 | DEL-01-01, DEL-02-01..09, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03 |
```

### Objective lockstep (ledger `ObjectiveIDs` and `SupportsObjectives`)

| Scope item → deliverable | ObjectiveIDs | SupportsObjectives before → after | Union rule |
|---|---|---|---|
| SOW-097 → DEL-04-03 | new `OBJ-001;OBJ-002` (A-24) | `OBJ-001;OBJ-002` → unchanged (union of SOW-006, SOW-007, SOW-097) | holds |
| SOW-098 → DEL-08-03 | new `OBJ-001` (A-25) | `OBJ-001` → unchanged (union of SOW-043, SOW-098) | holds |
| SOW-099 → DEL-08-06 | new `OBJ-001` (A-26) | new `OBJ-001` (A-28) | holds |
| SOW-100 → DEL-10-13 | new `OBJ-001` (A-27) | new `OBJ-001` (A-29) | holds |

No existing ledger `ObjectiveIDs` or deliverable `SupportsObjectives` cell changes. Objective statements are byte-unchanged. OBJ-003..OBJ-006 views are unchanged.

## 6. Vocabulary Map

### A-38 — ADD VOCAB_TERM `operational reliance`

ADD vocabulary 'operational reliance' with its disambiguation from the L-A1 reliance-hold control, professional reliance (K-AUTH-1) and Root PRD N-1. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §9 ADD operational reliance, reliance envelope, response budget (Seq 38-40) (Seq 38):

```diff
-| declared activity | graph-declared node state | A record-tier graph-declared node state (e.g. "declared ACTIVE as of commit X, age N"); never a liveness assertion and never presence tier (SOW-049) |
+| declared activity | graph-declared node state | A record-tier graph-declared node state (e.g. "declared ACTIVE as of commit X, age N"); never a liveness assertion and never presence tier (SOW-049) |
+| operational reliance | operational reliance on PEC data | Acting on a PEC record-tier claim as true as of its examined-through SHA, within the coverage and tier the response declares, with file fallback; available only from a release that has passed the §12 reliance-advertisement gate; never authority. Distinct from the L-A1 reliance-hold control (`ACTIVE_RELIANCE_HOLDS.csv`, `pec_reliance_hold.py` `rely-for-production`), from professional reliance (K-AUTH-1), and from Root PRD N-1 'for purposes of reliance' |
+| reliance envelope | — | The per-response declaration of pin, coverage, trust tier and file-fallback signal that bounds operational reliance (PEC-ORI-007, SOW-097) |
+| response budget | response-size budget, size cap | A declared bound on response size met by pagination or continuation, with stated truncation (PEC-API-006, SOW-098); distinct from the latency budget (PEC-API-002) |
```

### A-39 — ADD VOCAB_TERM `reliance envelope`

ADD vocabulary 'reliance envelope' (PEC-ORI-007, SOW-097). Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §9 orientation (mirror of Seq 5/39) (Seq 39) — mirror edit beyond the literal intake description (step-8 list):

```diff
-| orientation | Step-0 return | The per-loop/scope serve of PEC-ORI-001..006 |
+| orientation | Step-0 return | The per-loop/scope serve of PEC-ORI-001..007 |
```

The term row itself is added in the single §9 insertion shown under A-38.

### A-40 — ADD VOCAB_TERM `response budget`

ADD vocabulary 'response budget' (PEC-API-006, SOW-098), distinct from the latency budget. Supersession binding: **NO**.

Added in the single §9 insertion shown under A-38.

### A-41 — MODIFY VOCAB_TERM `harness`

Vocabulary 'harness': current row kept; an agent may also query directly through tool calls under the agent access class, and that agent is not a harness. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §9 harness (Seq 41):

```diff
-| harness | practitioner harness / application-owned Runtime service (per application, D-GOV-43 A2) / hooks CLI | Disambiguate: "practitioner harness" = the parity-peer CLI checker; "harness" unqualified = a potential machine consumer that acts only when explicitly enabled under its own authority; no polling or injection duty is inferred |
+| harness | practitioner harness / application-owned Runtime service (per application, D-GOV-43 A2) / hooks CLI | Disambiguate: "practitioner harness" = the parity-peer CLI checker; "harness" unqualified = a potential machine consumer that acts only when explicitly enabled under its own authority; no polling or injection duty is inferred. An agent may also query directly through tool calls under the agent access class; that agent is not a harness |
```

## 7. Constraints, intake summary, open issues, coverage and telemetry

### A-18 — MODIFY OTHER `C3`

C3 re-expressed: a consumer may act on a record-tier claim within the pin, coverage and tier the response declares, with file fallback (operational reliance, PEC-ORI-007), only from a release that has passed the §12 reliance-advertisement gate; 'non-authoritative' kept in the authority sense; Source adds D-PEC-90. Supersession binding: **YES (D-018 in `Supersession_Delta.csv`)**.

`SOFTWARE_DECOMP.md` — §1.3 C3 (Seq 18):

```diff
-| C3 | Pull-oriented, consumer-owned use: PEC serves labeled, non-authoritative orientation on request; it never self-polls, schedules a consumer, injects into an agent, or claims an external cadence; an explicitly enabled consumer decides whether and when to consume, and any injection is optional and verify-before-rely | PEC-K-03, D-PEC-67, D-PEC-68 |
+| C3 | Pull-oriented, consumer-owned use: PEC serves labeled, non-authoritative orientation on request (non-authoritative in the authority sense: never citable as authority); it never self-polls, schedules a consumer, injects into an agent, or claims an external cadence; an explicitly enabled consumer decides whether and when to consume and any injection is optional; a consumer may act on a record-tier claim within the pin, coverage and tier the response declares, with file fallback (operational reliance, PEC-ORI-007), only from a release that has passed the §12 reliance-advertisement gate | PEC-K-03, D-PEC-67, D-PEC-68, D-PEC-90 |
```

### A-19 — MODIFY OTHER `S1.2-Intake`

§1.2 intake summary: PRD v2.4 (the SCA-005 'PRD v2.2' residue at L45 corrected in the same edit, IA §9.5); thesis adds agents querying directly through tool calls; orientation bullet PEC-ORI-001..007 with the reliance envelope; API bullet PEC-API-001..007 with response-size budgets and the tool-call surface. Two further §1.2 mirror edits are marked below (step-8 list). Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §1.2 opening (SCA-005 residue "PRD v2.2", IA §9.5) (Seq 19):

```diff
-The work is a greenfield software build of the product defined by PRD v2.2:
+The work is a greenfield software build of the product defined by PRD v2.4:
```

`SOFTWARE_DECOMP.md` — §1.2 thesis (Seq 19):

```diff
-decision-slate presentation). It is available to explicitly PEC-enabled
-consumers, including harnesses acting on behalf of agents, and to the human
-owner through dashboards. It must remain "the coordination plane that
-doesn't need to exist": deletable at any moment without blocking any governed
-act.
+decision-slate presentation). It is available to explicitly PEC-enabled
+consumers, including harnesses acting on behalf of agents and agents
+querying directly through tool calls, and to the human owner through
+dashboards. It must remain "the coordination plane that doesn't need to
+exist": deletable at any moment without blocking any governed act.
```

`SOFTWARE_DECOMP.md` — §1.2 orientation bullet (Seq 19):

```diff
-- **Orientation** (PEC-ORI-001..006): per-loop orientation serves and deltas
-  since a caller SHA, scope-parameterized per the modes ladder, every claim
-  cited, every response SHA-stamped, measurement limits stated explicitly.
+- **Orientation** (PEC-ORI-001..007): per-loop orientation serves and deltas
+  since a caller SHA, scope-parameterized per the modes ladder, every claim
+  cited, every response SHA-stamped, measurement limits stated explicitly,
+  and every response declaring its reliance envelope (pin, coverage, trust
+  tier, file-fallback signal).
```

`SOFTWARE_DECOMP.md` — §1.2 API bullet (Seq 19):

```diff
-- **API** (PEC-API-001..005): local-only Unix-socket service, token-scoped;
-  ≤100 ms p95 orientation reads; versioned additive schema; compact
-  citation-bearing responses; SSE delta/presence subscription.
+- **API** (PEC-API-001..007): local-only Unix-socket service, token-scoped;
+  ≤100 ms p95 orientation reads; versioned additive schema; compact
+  citation-bearing responses; SSE delta/presence subscription; declared
+  response-size budgets met by pagination or continuation, with stated
+  truncation; a read-only query interface for agent tool calls under the
+  `agent` access class.
```

`SOFTWARE_DECOMP.md` — §1.2 validation bullet (mirror of Seq 8/27) (Seq 19) — mirror edit beyond the literal intake description (step-8 list):

```diff
-  standing kill test, the P1–P4 exit tests, and directed full-DAG
-  self-bootstrap validation for PEC's own build. (P0 governance is complete
-  and is not scope for this decomposition.)
+  standing kill test, the P1–P4 exit tests, the standing
+  reliance-advertisement gate for any release that advertises
+  operational reliance, and directed full-DAG self-bootstrap validation
+  for PEC's own build. (P0 governance is complete and is not scope for
+  this decomposition.)
```

`SOFTWARE_DECOMP.md` — §1.2 anticipated build shape P3 (mirror of Seq 9) (Seq 19) — mirror edit beyond the literal intake description (step-8 list):

```diff
-PEC-side consumer interfaces/adapters, presence registry, Git/worktree
-scanner) → P4 (PEC-side streams and optional hook-push interfaces). Live
-P3/P4 use requires separate
+PEC-side consumer interfaces/adapters, the agent tool-call query surface,
+presence registry, Git/worktree scanner) → P4 (PEC-side streams and
+optional hook-push interfaces). Live P3/P4 use requires separate
```

### A-23 — MODIFY OTHER `OI-006`

OI-006 premise extended to credentials for the agent access class (tool-call query, SOW-099); still closed only by a §16 ruling. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §10 OI-006 (Seq 23):

```diff
-| OI-006 | SOW-080 | §16.6 auth reuse undecided; premise re-expressed under SCA-005: Runtime token registries are private to each application's Runtime instance and reuse of an App registry is foreclosed, so the open choice is the PEC-local token mechanism | §16 ruling |
+| OI-006 | SOW-080 | §16.6 auth reuse undecided; premise re-expressed under SCA-005: Runtime token registries are private to each application's Runtime instance and reuse of an App registry is foreclosed, so the open choice is the PEC-local token mechanism; the open choice also covers credentials for the agent access class (tool-call query, SOW-099; SCA-006) | §16 ruling |
```

### A-42 — MODIFY OTHER `S7-S8-telemetry`

§5 intro counts and envelope posture, §6 row count, §7 telemetry and §8 prose recomputed: 100 scope items (74 IN / 18 OUT / 8 TBD); 68 deliverable rows (64 active / 4 RETIRED); active envelopes S 28 / M 34 / L 2 / XL 0; 0 IN items and 0 active deliverables without objective. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §5 intro counts (Seq 42):

```diff
-66 deliverable rows across the 11 packages: 62 active and 4 retired under
+68 deliverable rows across the 11 packages: 64 active and 4 retired under
```

`SOFTWARE_DECOMP.md` — §5 envelope posture (Seq 42):

```diff
-Context Envelope posture (active deliverables): **28 S / 32 M / 2 L / 0 XL.**
+Context Envelope posture (active deliverables): **28 S / 34 M / 2 L / 0 XL.**
```

`SOFTWARE_DECOMP.md` — §6 row count (Seq 42):

```diff
-**Authoritative register: `ScopeLedger.csv`** — 96 rows tracing every
+**Authoritative register: `ScopeLedger.csv`** — 100 rows tracing every
```

`SOFTWARE_DECOMP.md` — §7 ScopeItemCount (Seq 42):

```diff
-| ScopeItemCount | 96 (70 IN / 18 OUT / 8 TBD) |
+| ScopeItemCount | 100 (74 IN / 18 OUT / 8 TBD) |
```

`SOFTWARE_DECOMP.md` — §7 DeliverableCount (Seq 42):

```diff
-| DeliverableCount | 66 rows (62 active / 4 RETIRED: DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05) |
+| DeliverableCount | 68 rows (64 active / 4 RETIRED: DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05) |
```

`SOFTWARE_DECOMP.md` — §7 ContextEnvelopeCounts (Seq 42):

```diff
-| ContextEnvelopeCounts | S 28 / M 32 / L 2 / XL 0 (active deliverables; the 4 retired rows are excluded) |
+| ContextEnvelopeCounts | S 28 / M 34 / L 2 / XL 0 (active deliverables; the 4 retired rows are excluded) |
```

`SOFTWARE_DECOMP.md` — §7 single-package membership (Seq 42):

```diff
-| Deliverable single-package membership | 66/66; every `DEL-XX-YY` prefix matched to its parent package |
+| Deliverable single-package membership | 68/68; every `DEL-XX-YY` prefix matched to its parent package |
```

`SOFTWARE_DECOMP.md` — §8 ADD SCA-006 additions and re-assessments (Seq 42):

```diff
-  narrowed to `LOOP_INIT.md` identity.
+  narrowed to `LOOP_INIT.md` identity.
+- **SCA-006 additions and re-assessments:** DEL-08-03 (compact response
+  format) is re-enveloped S → M with LOW risk kept — declared response-size
+  budgets met by pagination or continuation, with stated truncation, join
+  the citation-bearing format as one slice; DEL-08-06 (agent tool-call
+  query surface) is M with MEDIUM risk, coupled to OI-006 like DEL-08-01
+  and held at its envelope until that ruling; DEL-10-13
+  (reliance-advertisement gate) is S, LOW — it composes other packages'
+  evidence into one gate record.
```

## 8. Product authority and instructions outside the decomposition

- **K group (Seq 1–13), PRD v2.4 successor candidate:** exact text in `PRD_V2_4_SUCCESSOR_DIFF.md` (SHA-256 `a743a5273c66dc679a99888c4dc2b865a318dab64fcaaa7768ecb71f35696a4c`); candidate bytes `CP2_CANDIDATE/docs/PRD.md` (SHA-256 in the byte table above).
- **I group (Seq 14–17), `projects/pec/AGENTS.md` instruction candidate:** exact text in `AGENTS_MD_CANDIDATE_DIFF.md` (SHA-256 `7c57a1b2c02c872fae6f778beeddf7f812809d469b504e34d1e6f79bbb48a158`); applied at checkpoint 3 as an instruction tranche (INS-a).

The decomposition texts above use the same canonical wording as those documents for C3 (PEC-K-03), SOW-003 (the §8 access classes), SOW-060 (§11 metric 4), SOW-080 / OI-006 (§16.6), SOW-097 (PEC-ORI-007), SOW-098 (PEC-API-006), SOW-099 (PEC-API-007) and SOW-100 (the §12 reliance-advertisement gate). The §12 P1 row is not edited (GATE-a).

## 9. Child-closure set and authoritative ledger remaps

No package is removed, merged, split or reclassified; no objective is added or removed; no action is a REMOVE, so no retirement closure is open. The parent-entity changes are four scope-item additions and two deliverable additions, each closed in this same amendment.

### 9.1 Added scope items and deliverables (ADD)

| New ID | Parent package | Covering / covered deliverable | Objectives | Envelope / phase of the deliverable |
|---|---|---|---|---|
| SOW-097 (A-24) | PKG-04 | DEL-04-03 (existing; A-30 adds the coverage) | `OBJ-001;OBJ-002` | M / P1 (unchanged) |
| SOW-098 (A-25) | PKG-08 | DEL-08-03 (existing; A-32 adds the coverage) | `OBJ-001` | S → M / P1 |
| SOW-099 (A-26) ↔ DEL-08-06 Agent tool-call query surface (A-28) | PKG-08 | reciprocal | `OBJ-001` | M / P3 |
| SOW-100 (A-27) ↔ DEL-10-13 Reliance-advertisement gate (A-29) | PKG-10 | reciprocal | `OBJ-001` | S / P1 |

IDs are append-only: SOW-097..100 follow SOW-096 (the ledger's physical order places them after SOW-096, before the OUT rows); DEL-08-06 follows DEL-08-05 and DEL-10-13 follows DEL-10-12 in `Deliverables.csv`, `ContextBudgetQA.csv` and §5. None of these IDs occurs in the live decomposition, registers or `PKG-*` folders. Folders, metadata and dependency registers for DEL-08-06 and DEL-10-13 are created later by PROJECT_SETUP under its own D-PEC packet; the Impact Assessment (§9.1) expects, for extraction: DEL-08-06 on DEL-08-01, DEL-08-02, DEL-08-03 and DEL-04-01; DEL-10-13 on DEL-03-04, DEL-04-03, DEL-04-05, DEL-10-02 and the PKG-02 parser deliverables. The closure must stay acyclic.

### 9.2 Package assignment remaps

| Package | Assigned IN scope before | After | Active children before → after |
|---|---|---|---|
| PKG-04 | SOW-004..009 (6) | SOW-004..009, 097 (7) | 5 → 5 |
| PKG-08 | SOW-003, 040..044 (6) | SOW-003, 040..044, 098, 099 (8) | 5 → 6 (+DEL-08-06) |
| PKG-10 | SOW-025, 055, 058..064, 084, 085, 093 (12) | + SOW-100 (13) | 12 → 13 (+DEL-10-13) |

### 9.3 Objective remaps

See the lockstep table in §5: only new rows carry objectives; no existing mapping changes.

## 10. Invariants and counts

Recomputed from the files by `prove_counts.py` (live revision 1.5 and candidate revision 1.6).

| Metric | Revision 1.5 (live) | Revision 1.6 candidate |
|---|---:|---:|
| Scope items (IN / OUT / TBD) | 96 (70 / 18 / 8) | 100 (74 / 18 / 8) |
| Packages / objectives | 11 / 6 | 11 / 6 |
| Deliverable rows (active / RETIRED) | 66 (62 / 4) | 68 (64 / 4) |
| ContextBudgetQA rows | 66 | 68 |
| IN items without package / deliverable / objective | 0 / 0 / 0 | 0 / 0 / 0 |
| Active deliverables without SupportsObjectives | 0 | 0 |
| Active Context Envelopes S / M / L / XL | 28 / 32 / 2 / 0 | 28 / 34 / 2 / 0 |
| Active risk LOW / MEDIUM (ContextBudgetQA) | 56 / 6 | 57 / 7 |
| Union rule `SupportsObjectives = union(ObjectiveIDs of CoversScopeItems)` over active rows | 62/62 | 64/64 |
| Open / resolved issues | 10 / 3 | 10 / 3 |
| Vocabulary terms | 26 | 29 |
| Strict register validator (`validate_decomposition_registers.py --strict`) | 0 ERROR / 0 WARNING, exit 0 (live) | 0 ERROR / 2 WARNING (DRB-008 DEL-08-06, DEL-10-13), exit 1 (scratch overlay) |
| Execution dependency closure (`analyze_dep_closure.py`) | 111 edges, 66 nodes, 0 SCCs, 6 isolated, 1 hub | identical (dependency registers unchanged) |

Per package (IN scope assigned / active deliverables / retired rows / active S-M-L):

| Package | Revision 1.5 | Revision 1.6 |
|---|---|---|
| PKG-00 | 3 / 3 / 0 / 1-2-0 | 3 / 3 / 0 / 1-2-0 |
| PKG-01 | 8 / 6 / 0 / 4-1-1 | 8 / 6 / 0 / 4-1-1 |
| PKG-02 | 9 / 9 / 0 / 4-4-1 | 9 / 9 / 0 / 4-4-1 |
| PKG-03 | 7 / 6 / 0 / 2-4-0 | 7 / 6 / 0 / 2-4-0 |
| PKG-04 | 6 / 5 / 0 / 2-3-0 | 7 / 5 / 0 / 2-3-0 |
| PKG-05 | 3 / 2 / 0 / 0-2-0 | 3 / 2 / 0 / 0-2-0 |
| PKG-06 | 6 / 5 / 1 / 1-4-0 | 6 / 5 / 1 / 1-4-0 |
| PKG-07 | 3 / 2 / 3 / 0-2-0 | 3 / 2 / 3 / 0-2-0 |
| PKG-08 | 6 / 5 / 0 / 3-2-0 | 8 / 6 / 0 / 2-4-0 |
| PKG-09 | 7 / 7 / 0 / 1-6-0 | 7 / 7 / 0 / 1-6-0 |
| PKG-10 | 12 / 12 / 0 / 10-2-0 | 13 / 13 / 0 / 11-2-0 |

Validator evidence: from `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a2306177d1672e417`, Python 3.13.7, `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` → exit 0, 66 registers, 263 dependency rows, 66 deliverables declared, no finding; `python3 tools/validation/validate_decomposition_registers.py <scratch>/execution --strict` on a scratch copy of `projects/pec/execution` (with `projects/pec/docs` beside it for evidence resolution) overlaid with the five candidate files → exit 1 under `--strict`, 0 ERROR and exactly two WARNINGs, DRB-008 for DEL-08-06 and DEL-10-13, whose folders and `Dependencies.csv` do not exist until PROJECT_SETUP (expected, as SCA-005's DEL-02-08/09). `python3 tools/coordination/analyze_dep_closure.py <scratch>/execution --output-dir <closure>` → exit 0, run_status COMPLETE, subject_status PASS, 263 rows, 111 execution edges over 66 folder nodes, 0 SCCs, hub DEL-03-01 (in 13 / out 12), isolated DEL-00-03, DEL-01-05 and the four retired rows; identical to the live run.

Package-discipline isolation (DL-3, DL-12): DEL-08-06 is a read-side PKG-08 slice that writes nothing and consumes only the versioned API and its responses; DEL-10-13 is a PKG-10 validation deliverable that composes other packages' evidence (DEL-03-04, DEL-04-05, DEL-04-03, the PKG-02 fixture suites, DEL-10-02) into one gate record and consumes no internals, like DEL-10-02. Neither writes into another package. Artifact-kind granularity (DL-4, DL-13): each new deliverable holds one artifact kind (a tool-call query adapter; a gate test suite), and SOW-100 is an instrument distinct from the behaviours it tests (DL-6). Stable IDs: no ID is renumbered, reused or deleted; every existing name and folder path is retained; new IDs are append-only. C1, C2, C15, the Gate Log, the objective statements and the §12 P1 citation are byte-unchanged.

## 11. Residual stale text not driven by any accepted action

Found by reading the candidate against the D-group changes. It is **not** changed by this candidate (nothing unselected is added). The accepted Impact Assessment §9.5 corrects SCA-005 residue only where SCA-006 already edits the same text; the one decomposition locus it names (L45 "PRD v2.2") is corrected under A-19.

| Locus (candidate line) | Wording | Why it is residual |
|---|---|---|
| §1.4 posture 1 (L142) | "Requirement source = PRD v2.2 alone. The 46 PEC-\*-NNN requirements" | Kept as Gate-1 history by A-43 (intake Seq 43; SCA-005 precedent). PRD v2.4 holds 49 requirements. |
| §2 intro (L177) | "Atomic scope items normalized from PRD v2.2." | SCA-005 residue; A-24 edits a later sentence of the same paragraph, but IA §9.5 names only L45; intake-time basis. |
| §1.3 C16 (L138); SOW-064 SourceRef (§2.1, ledger) | "PRD v2.2 §12" | SCA-005 residue; the §12 P1 row stays unedited (GATE-a), so the citation still locates its origin. |
| §1.5 R6 (L168) | "D-PEC-57..68", now with D-PEC-90 | Intake-time range; later records (D-PEC-78, 86, 92, 94) are not listed. Pre-existing. |
| §2.4 domain signals | "Runtime surfaces: … a socket API server, a web dashboard UI, and a hooks CLI"; "Test surfaces: kill test, parity diff, seeded-conflict, TTL/crash, and measurement instrumentation" | Phase-2 partitioning signals; they name neither the agent tool-call surface (inside PKG-08 API) nor the reliance-advertisement gate. No action covers §2.4. |
| §8 bullet "Two OI-coupled MEDIUM risks at M envelope (DL-14)" | DEL-00-02 and DEL-08-01 | Accurate as DL-14 history; DEL-08-06 (third OI-coupled MEDIUM) is described in the new SCA-006 bullet (A-42). "Remaining S/M deliverables assessed LOW risk" also omits DEL-10-10 (MEDIUM since SCA-001; pre-existing). |
| `Deliverables.csv` / `ContextBudgetQA.csv` DEL-00-03 envelope note | "(46 requirements / 64 deliverables)" | PRD v2.4 has 49 requirements; the registers hold 68 rows (64 active). Seq 52/53 advise the DEL-00-03 SOW and SPEC, not this register note. |
| §7 intro; OI-013 | "no durable build gate exists yet" | Pre-existing (the repo validator exists); not SCA-006 drift. |
| SOW-067 Notes | "Daemon owns execution (C13)" | Pre-existing SCA-005 residue. |
| §1.2 presence bullet | "live parent→child hierarchy edges" | Pre-existing SCA-005 residue. |
| §11 DL-18 (historical) | "… release, and reliance remain downstream or excluded" | Bare "reliance" in an earlier sense inside a historical decision-log row; the terminology rule governs new text only. |
| DEL-10-12 name and description | "Poll-adoption measurement"; "Candidate-consumer enablement …" | Not contradicted by SOW-060's new parenthetical (generic over candidate consumers); name/path stable (SCA-003). Noted for consistency only. |
| §2 SSOW vs ledger (pre-existing, DL-15) | TBD rows: ledger Notes prefix "OI-00N. "; SOW-064 Notes wording; SOW-077 physically after the TBD block in the ledger | Pre-existing duplication conventions; `prove_counts.py` shows the same ten differences on revision 1.5 and 1.6 and no new one. |

## 12. Derivative advisories (Seq 44–54)

Not Lane A writes: no byte of these files changes through this amendment; each owning workflow amends its file under its own packet after checkpoint 3. Exact disposition in `Propagation_Plan.md`.

| Seq | Target file | Advisory | Disposition |
|---|---|---|---|
| 44 | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md` | DEL-04-01 SOW re-quotes amended PEC-K-03/§8 (CLM-016, AX-007) | exact disposition in `Propagation_Plan.md` |
| 45 | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/ScopeOfWork.md` | DEL-04-02 SOW CLM-016 / REQ-013 / L363 | exact disposition in `Propagation_Plan.md` |
| 46 | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md` | DEL-08-01 SOW class set and §8 quotations (+ SCA-005 residue L48, L127) | exact disposition in `Propagation_Plan.md` |
| 47 | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md` | DEL-08-03 SOW REQ-005/006, AC-006, CON-001, VER-006, CLM-009; scope + SOW-098 | exact disposition in `Propagation_Plan.md` |
| 48 | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/ScopeOfWork.md` | DEL-04-03 SOW extension for SOW-097 | exact disposition in `Propagation_Plan.md` |
| 49 | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/ScopeOfWork.md` | DEL-03-04 SOW CON-001/002, AC-016 (+ SCA-005 residue L105) | exact disposition in `Propagation_Plan.md` |
| 50 | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/ScopeOfWork.md` | DEL-08-04 SOW CLM-011 access-class count | exact disposition in `Propagation_Plan.md` |
| 51 | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/ScopeOfWork.md` | DEL-10-03 SOW CLM-008; agent class in the negative surface | exact disposition in `Propagation_Plan.md` |
| 52 | `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/ScopeOfWork.md` | DEL-00-03 SOW CLM-004/006 ("46 requirements", "PRD.md v2.2") | exact disposition in `Propagation_Plan.md` |
| 53 | `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/artifacts/v2/SPEC.md` | DEL-00-03 SPEC K-03 row, counts, API row, release-proof list | exact disposition in `Propagation_Plan.md` |
| 54 | `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-06_Universal_drill_down_to_cited_source/Dependencies.csv`; `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/Dependencies.csv`; (intake also named `…/DEL-10-12_Poll_adoption_measurement/Dependencies.csv`; dropped at checkpoint 2) | EvidenceQuote refresh; this preview's scan: DEP-09-06-003 and DEP-10-03-003 break (DEL-08-01 description); DEP-09-06-004 and DEP-10-12-004 stay verbatim | exact disposition in `Propagation_Plan.md` |

EvidenceQuote scan (Seq 54): `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/B5/decomp/evidence_quotes.py` (SHA-256 `14141e2d350fe0d203ea5189d615423a3fe1565077f2f21295144035486bcd91`) checks every ACTIVE row of every `PKG-*/1_Working/DEL-*/Dependencies.csv` (263 rows, 243 ACTIVE) against the candidate copy of its EvidenceFile when that is one of the five decomposition files, the `--prd` file for `docs/PRD.md` (default the live PRD), and the live file otherwise. Against the candidate and the live PRD: 109 text quotes stay verbatim, 132 ANCHOR structured loci hold, and exactly two quotes break — DEP-09-06-003 and DEP-10-03-003 (both quote the DEL-08-01 description). DEP-09-06-004 (DEL-08-03 sentence, kept as prefix) and DEP-10-12-004 (PKG-08 charter prefix) stay verbatim, as the canon intended. Rerun against the PRD candidate with `--prd <path>`.

## 13. Basis currency since checkpoint 1

The accepted Impact Assessment §2.1 states that the audited inputs of the reused pre-change baseline `COV_SCA005_POSTSETUP_2026-09-25_1606` equal the pre-change state byte for byte. **That statement no longer holds exactly.** The `D-PEC-95` act (PR #924, merge `abfd0897b`; run root `execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/`) changed 119 derivative paths after that audit: both `_LATEST.md` pointers, `_Coordination/_COORDINATION.md`, 42 `_CONTEXT.md`, 64 `_REFERENCES.md` and 10 `Dependencies.csv`.

Three of those paths are in SCA-006 `AffectedFiles`: the DEL-04-03 and DEL-08-03 `_CONTEXT.md` (Seq 30, 32) and the DEL-10-12 `Dependencies.csv` (Seq 54 intake). `git diff 13df8b795 4d5f7b911` on them shows one provenance clause ("then by revision 1.5 …") in each context and a change to the DEP-10-12-003 row only. No text SCA-006 amends changed, and DEP-10-12-004, the Seq 54 intake cell, is byte-identical. The decomposition, its four registers, `docs/PRD.md` and `projects/pec/AGENTS.md` are byte-identical to the Impact Assessment's pins. This candidate is computed from the current bytes at `4d5f7b911`, including the `D-PEC-95` provenance lines.

Consequence for checkpoint 3: the reused baseline still carries COV-068 (42 contexts at revision 1.4), COV-069 (64 references at revision 1.4), COV-072 (19 non-verbatim EvidenceQuotes) and COV-073 (stale-conservative SCA-005 handoff surfaces and pointers). The `D-PEC-95` act addressed them without a further audit (its ruling: "no re-audit"). The SCA-006 post-change audit is the first audit to observe the post-`D-PEC-95` state. Its pre/post comparison must attribute the resolution of COV-068/069/072/073 to `D-PEC-95`, not to SCA-006, and must not report them as SCA-006 effects (`Propagation_Plan.md` §C4).

## 14. Derivative and propagation boundary

Nothing in this preview writes `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `Dependencies.csv`, `_DEPENDENCIES.md`, any Scope of Work, the DEL-00-01 ADRs, the DEL-00-03 SPEC, `v2/**`, `loops.json`, `_DomainEngines/profiles/pec.yaml`, pointers, notices or foreign surfaces, and it creates no folder for DEL-08-06 or DEL-10-13. The exact `_CONTEXT.md` mirror postimages for DEL-04-03, DEL-08-01 and DEL-08-03 are prepared as propagation input. Their exact dispositions, owners and rerun obligations are in `Propagation_Plan.md`. No downstream package becomes current through acceptance of this preview, and nothing here makes operational reliance on PEC data available: it begins only at a PEC release that passes the §12 reliance-advertisement gate.
