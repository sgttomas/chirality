# REPORT B — Reviewer B, horizontal lens (architecture, boundaries, adversarial concordance)

Run: TANDEM-REVIEW-20260726 · Pass 1 (independent) · Reviewer B
Dispatcher: HELP_HUMAN (Agent 0) as supervising review manager
Date of return: 2026-07-26

> Manager filing note (not reviewer content): Reviewer B's harness blocked the report-file
> write required by brief §8; the reviewer returned this report in its terminal response
> with an explicit deviation disclosure (§1.5 below). The supervising manager persisted the
> returned content verbatim to this path and froze it by hash on receipt, before reading
> any other reviewer's return. Three HTML entity escapes introduced by the return channel
> (&lt; &gt; &amp;) were normalized to their literal characters; no other change.

---

## 1. Reviewed-basis statement

### 1.1 Identity and verification

| Item | Value | Verification |
|---|---|---|
| Review freeze commit | `da31c19b5656dd74615e308c4215688971d33dc9` | `git rev-parse HEAD` in the assigned worktree returned exactly this SHA |
| Product-basis commit | `aeadf5304435e1a4d8b4a26306da9ad4d4519eb6` | Present in `git log` of the freeze (2 commits back) |
| Worktree used | `…/scratchpad/frozen-da31c19b5` (detached, read-only) | Confirmed; `git status --porcelain` empty at start and at every checkpoint |
| Charter | `plans/chirality_program_architecture_and_tandem_review_2026-07-25.html` | SHA-256 `1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f` — recomputed, matches brief §2 |
| My sealed brief | `…/briefs/REVIEWER_B_BRIEF.md` | SHA-256 `ede4724d80fa4c3ecf784821f3807f4a56aecb9cec90d1189abeafaa09daf274` — recomputed, matches dispatch |
| Frozen-basis manifest | `…/FROZEN_BASIS_MANIFEST.md` (521 lines) | **Read in full** before any finding |
| Charter | 1449 lines | **Read in full** before any finding, as non-governing reviewer guidance |

### 1.2 Independent SHA-256 verification of the six product instruments

All six manifest SHA-256 prefixes were recomputed at the freeze and **match exactly**:

| Instrument | Manifest prefix | Recomputed |
|---|---|---|
| `docs/PRD_ROOT.md` | `82f7ea2944e7` | `82f7ea2944e791f12de3a191cbe209a8e8ed90420b82af25ccb5df43d4cc94b3` |
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `14067a7d97c9` | `14067a7d97c94a43f5db0c2c1116206482504f260363de5ff6fa401a4df94cf7` |
| `projects/chirality-app-dev/docs/PRD.md` | `ef638f43ccae` | `ef638f43ccae1cd78b26b1ae078a33770cf64cc36c247c5d7da04b35196a4010` |
| `…/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | `952d3cbf81b0` | `952d3cbf81b0cea014a1c3f1bd3f62fbc0b23b96bfa1fd1913961731c925b08b` |
| `projects/pec/docs/PRD.md` | `de0a969cad15` | `de0a969cad1519dda61e871ab4bf14be34dce995049c042746f08e1c82d14684` |
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` | `3e5be4e453ed` | `3e5be4e453ed48d7fbfa48ecc486156124bb197798b47f57aa5284698346dd58` |

### 1.3 Tool basis (every tool run, with basis stated)

All tools were executed from the frozen tree at the freeze commit. The worktree was verified clean (`git status --porcelain` → 0 lines) after every tool run; **no tool wrote into the worktree**.

| Tool / method | Path (at freeze `da31c19b5`) | Use | Result relied on |
|---|---|---|---|
| `validate_scope_of_work.py` | `tools/scope_of_work/validate_scope_of_work.py` | Root 45 SOWs, PEC 32 SOWs | Root **45 PASS / 0 FAIL**; PEC **32 PASS / 0 FAIL** |
| `validate_harness_contract_pull.py` | `tools/coordination/validate_harness_contract_pull.py` | D-APP-48 pull contract; Piping D-30 consumption | pull contract alone: `harness contract pull validation passed` (exit 0); with consumption: `ERROR: consumption source.commitSha mismatch` (exit 1) |
| `git show <commit>:<path>` + `shasum -a 256` | git | Compare pinned basis vs freeze content | See B-011, B-013 |
| Python `hashlib.sha256` recompute | ad hoc, stdout only | Source-manifest and corpus pin recompute | See §1.4 |
| `grep` / `find` / `csv` counts | ad hoc, stdout only | Corpus-wide sweeps | Counts stated per finding |

**Version-skew note (manifest §4, condition 15) is respected.** Root's 45 SOWs were accepted under the pre-v6 method; I ran the *current* validator only to test whether skew manifests as a current-tool failure. It does not (45/45 PASS). I therefore report no tool-drift finding against Root's SOWs and do not treat the historical acceptance as impeached.

### 1.4 Deterministic recomputations that validate my method against the manifest

- `domains/chirality/_Sources/Source_Manifest.csv` (225 rows, repo-root-relative paths): **126 CLEAN / 93 DRIFT / 6 MISSING** — matches the manifest exactly.
- `domains/chirality-app-dev/_Sources/Source_Manifest.csv` (467 rows, paths relative to `projects/chirality-app-dev/`): **119 CLEAN / 129 DRIFT / 219 MISSING** — matches the manifest exactly once the correct path base is used.

Both matches give me confidence that subsequent recomputations in this report are sound.

### 1.5 Deviations from the brief

**One, forced and external:** the harness blocked writing the report file, so this report is returned as the response body rather than at the brief §8 path. No content was reduced as a result.

Otherwise none. Specifically: I read the charter in full and then the manifest in full before forming findings; I formed my own account of each product from the frozen records before using the charter as a challenge set; I did not read, `cd` into, or cite `/Users/ryan/dev/chirality` or any other worktree; I altered no Git state; I did not delegate (brief §1); I made no attempt to discover or anticipate the other reviewer's work.

One scope note: an early sweep of mine returned 43 Root SOWs because my exclusion filter `-not -path "*Evaluation*"` wrongly excluded two deliverables whose *names* contain "Evaluation". Corrected count is **45**, confirmed per package (8/5/6/10/8/8). I record the error because the corrected figure is load-bearing for coverage.

---

## 2. Product accounts (formed from the frozen records, before charter challenge)

### 2.1 Chirality Root

**What it is.** Root is the repository-root product: the ratified normative corpus, the shared instruction surface, the developmental (governance) machinery, the evidence conventions, and — since D-GOV-20 — the generic executable runtime under `runtime/`. Its adopted PRD (`docs/PRD_ROOT.md`, Rev 5, adopted by D-GOV-22) states a two-level ruled genus (ID-0): a "canonical human-governed application environment and generative operating form" that *contains* a filesystem-native agent operating system.

**Authority chain.** `docs/DIRECTIVE.md` → `docs/CONTRACT.md` → `docs/SPEC.md` → `docs/TYPES.md`, with `AGENTS.md` + `agents/` as the live instruction surface (PRD N-6; K-AGENTS-1 makes the live registry govern over narrative). Rulings live in `docs/governance_harness/_DECISIONS/` (D-GOV-01..D-GOV-27); the register is navigational and the per-decision records govern (PRD D-1). The PRD itself confers no authority — D-GOV-22 does, bound to exact bytes (K-AUTH-2).

**Governed state at the freeze.** PRD Rev 5 carries **42 stable commitments** (N-1..N-9 = 9; O-1..O-10 = 10; D-1, D-2, D-4..D-16 = 15 with D-3 retired; E-1..E-8 = 8), **7 objectives** (OBJ-1..OBJ-7), 6 falsifiers (F1..F6), 5 ruled owner decisions (RD-1..RD-5) with 3 concordance obligations, and 4 surfaced conflicts (C-1..C-4). The accepted decomposition (v1.0, D-GOV-25) is 6 packages / 45 deliverables / 103 scope items / 7 objectives, with six authoritative companion registers; I verified row counts of all five CSVs (45 / 7 / 84 / 103 / 51) against the manifest — all match. 45 ScopeOfWork contracts exist under `execution/PKG-0*/1_Working/`, all INITIALIZED, all pinning `…SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8…`. Guards G1–G4 are registered and passing (`execution/_harness/root_guards.yaml`); all six work-graph nodes are `pending` (`execution/_harness/work_graph.yaml`, `accepted_basis: 31b8dc94a…`). Materialization beyond initialization remains behind the D-GOV-21 §5.3 gate (OI-008, `OPEN_STANDING`).

**Distinctive strength.** The decomposition's discipline is genuinely high: a single declared scope source (DEC-001), explicit refusal to partition by the four PRD categories (DEC-003, §4.3), bidirectional F4 registers that close (84 forward / 51 reverse, 0 uncovered), recorded framing strains kept on the record after acceptance rather than deleted (OI-003, OI-004), and a reasoned, machine-visible deferral rather than a silent gap (OI-013 / §12.1, forward register `COVERED_WITH_RECORDED_DEFERRAL`).

**Distinctive weakness (my lens).** Because the PRD is the sole scope source and the PRD carries the runtime only as an authority-boundary statement (O-2(c), O-10), the accepted decomposition contains **no deliverable that owns the shared runtime's contract, conformance, compatibility, migration, security, or release evidence** — even though D-GOV-20 (accepted, 2026-07-22) rules ten substantive architectural items and names "Daemon/client/CLI, Desktop migration, PEC migration, security review, and regression review" as separately bounded implementation gates. This is lawful decomposition behaviour producing a real program-level gap (B-002).

### 2.2 Chirality App

**What it is.** A registered project loop at `projects/chirality-app-dev/` (registered through `chirality.project.json`), not a domain engine. Its PRD is titled **"PRD - Chirality Desktop Harness"** (dated 2026-05-20) — "a desktop harness for running governed AI agents against a user-selected local filesystem workspace", packaging a release-managed instruction root and keeping mutable state in a user-selected working root.

**Authority chain.** A synchronized six-document corpus (DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, PRD) *local to the project*, whose identity of record is its pin in `execution/_Reconciliation/References/AUTHORITY_CORPUS.json` v17 (D-APP-38 model). There is no single adopting PRD ruling; authority is accumulated across 74 RULED D-APP rows, the register describing itself as non-governing tracking. I verified all **8 of 8 v17 pins CLEAN** at the freeze.

**Governed state at the freeze.** Decomposition v3.2 (2026-05-20): 10 packages / 51 deliverables / 78 scope items / 10 objectives, gates "PASSED by implicit human approval per user instruction" (DEC-002), amended in place by SCA-APP-001/003/004 with topology preserved. 53 ScopeOfWork.md and 53 `_STATUS.md` (51 + 2 PKG-00 control); I confirmed **all 53 read `Current State: IN_PROGRESS`**, none ISSUED, consistent with D-APP-54. Open work is expressed in each contract's `Remaining` section.

**Distinctive weakness (my lens).** App is the product where boundary discipline is weakest, and the weakness is structural rather than incidental: (i) the decomposition directory contains **only the markdown file** — no companion registers at all, so no machine-checkable scope/deliverable/coverage truth exists; (ii) the decomposition references **zero FR-\* and zero NFR-\* identifiers**, so the only requirement-ID map is the PRD's own §16 table, which is coarse, overlapping and incomplete (B-020); (iii) the decomposition's Downstream Execution Notes assert that root `runtime/` ownership is merely "an implementation-location change" and that "app-dev deliverables retain semantic ownership" (B-001) — a direct contradiction of D-GOV-20, D-T0-23, `AGENTS.md`, and the App PRD's own §17 amendment.

### 2.3 PEC

**What it is.** The optional Chirality **coordination plane** at `projects/pec/`: a deterministic, rebuildable projection of governed file truth (record tier) plus an ephemeral presence registry (presence tier). PRD v2.1 (adopted v2.0 by D-PEC-58; v2.1 clarification by D-PEC-61) states the thesis plainly: "the coordination plane that **does not need to exist**: every consumer has a file-native fallback, and deleting PEC degrades throughput, never correctness."

**Authority chain.** PRD v2.1 → 11 product invariants PEC-K-01..PEC-K-11 → requirement families `PEC-{ORI,RCN,GAT,PRS,STR,API,DSH,SVC}-NNN`; rulings in `execution/_Coordination/_DECISIONS/` (D-PEC-57..D-PEC-66); fences F-PEC-1..F-PEC-4 in force (D-T0-15), with F-PEC-1 requiring an owner-ruled packet per build tranche.

**Governed state at the freeze.** Decomposition rev 1.2 (D-PEC-60, amended by SCA-001/D-PEC-61 and SCA-002/D-PEC-64): 11 packages (PKG-00..PKG-10), 64 deliverables, 94 scope-ledger rows, with four companion registers. 32 of 64 deliverables have validated SOWs at INITIALIZED; the other 32 remain OPEN by deliberate sequencing. I verified this exactly: **32 ScopeOfWork.md, 64 `_STATUS.md`, 32 INITIALIZED + 32 OPEN**. Dependency truth is deliverable-local and I recomputed it independently: **64 local `Dependencies.csv`, 254 rows, 135 ANCHOR / 119 EXECUTION, all Status=ACTIVE, and no central dependency register present** — matching the manifest exactly and conforming to Root O-8 / K-DEP-1/2.

**Distinctive strength.** PEC is the strongest boundary document in the corpus. Non-goals are stated as *permanent* and mechanically checkable (§4.2: not a system of record, not a ruling surface, not an orchestrator, not a lock manager, not a Git actor); PEC-K-01 makes graceful absence an invariant with a standing release gate (PEC-SVC-004 kill test); §16 records nine open product decisions rather than closing them by preference; and PEC-STR-002 explicitly declares that "writes into root `runtime/` are outside PEC's fences and require their own coordination." It also declares its own coverage residue in its own telemetry rather than concealing it (B-028).

---

## 3. Coverage matrices (one per product)

### 3.1 Root — full PRD-item coverage matrix (84 rows, complete)

**Grouping rule:** the population is the accepted forward register `chirality_root_prd_coverage_forward_v1_0.csv` (84 rows), which decomposition §3 designates authoritative for F4-forward. I enumerate every row. Dispositions are the register's own `CoverageStatus`, independently recomputed by me from the CSV: **83 COVERED, 1 COVERED_WITH_RECORDED_DEFERRAL, 0 UNCOVERED.** Item kinds: 42 commitment, 15 direction, 7 objective, 6 falsifier, 5 ruling, 4 obligation, 4 conflict, 1 non-goal.

| PRD item | Kind | Disposition | Carrying deliverable(s) (lead) |
|---|---|---|---|
| OBJ-1 | objective | COVERED | DEL-01-01, DEL-01-02, DEL-01-03, DEL-01-07, DEL-01-08, DEL-02-01, DEL-02-05, DEL-04-07, DEL-04-09 |
| OBJ-2 | objective | **COVERED_WITH_RECORDED_DEFERRAL** | DEL-01-04, DEL-01-06, DEL-02-02, DEL-02-03, DEL-03-02, DEL-03-06, DEL-04-02, DEL-04-06 — situated-working-root half deferred (§12.1, OI-013, owner decision 1 of D-GOV-25) |
| OBJ-3 | objective | COVERED | DEL-01-04, DEL-04-01/03/04/05/08/10, DEL-05-02/03/04/05/07/08, DEL-06-03 |
| OBJ-4 | objective | COVERED | DEL-02-04, DEL-03-01/04/05/06, DEL-05-06, DEL-06-01/07 |
| OBJ-5 | objective | COVERED | DEL-06-04, DEL-06-05, DEL-06-06, DEL-06-08 |
| OBJ-6 | objective | COVERED | DEL-03-03, DEL-05-01, DEL-06-02 |
| OBJ-7 | objective | COVERED | DEL-01-05, DEL-03-01 |
| N-1 | commitment | COVERED | DEL-01-05, DEL-06-05 |
| N-2 | commitment | COVERED | DEL-01-02 |
| N-3 | commitment | COVERED | DEL-01-04 |
| N-4 | commitment | COVERED | DEL-01-03 |
| N-5 | commitment | COVERED | DEL-02-04 (+ DEL-03-01, DEL-05-x per split DEC-005) |
| N-6 | commitment | COVERED | DEL-01-03 |
| N-7 | commitment | COVERED | DEL-01-06 |
| N-8 | commitment | COVERED | DEL-01-06 |
| N-9 | commitment | COVERED | DEL-01-02 |
| O-1 | commitment | COVERED | DEL-02-01 |
| O-2 | commitment | COVERED | **DEL-02-02 only** — see B-002 |
| O-3 | commitment | COVERED | DEL-02-03 |
| O-4 | commitment | COVERED | DEL-02-04 |
| O-5 | commitment | COVERED | DEL-02-05 |
| O-6 | commitment | COVERED | DEL-03-01 |
| O-7 | commitment | COVERED | DEL-03-02 |
| O-8 | commitment | COVERED | DEL-03-03 |
| O-9 | commitment | COVERED | DEL-03-04, DEL-03-05 |
| O-10 | commitment | COVERED | **DEL-02-02 only** — see B-002 |
| D-1 | commitment | COVERED | DEL-04-01 |
| D-2 | commitment | COVERED | DEL-04-01 |
| D-4 | commitment | COVERED | DEL-04-02 |
| D-5 | commitment | COVERED | DEL-04-03 |
| D-6 | commitment | COVERED | DEL-04-04 |
| D-7 | commitment | COVERED | DEL-04-05 |
| D-8 | commitment | COVERED | DEL-04-06 |
| D-9 | commitment | COVERED | DEL-04-10 |
| D-10 | commitment | COVERED | DEL-04-07 |
| D-11 | commitment | COVERED | DEL-04-04 |
| D-12 | commitment | COVERED | DEL-04-10 |
| D-13 | commitment | COVERED | DEL-04-08 |
| D-14 | commitment | COVERED | DEL-04-09 (capability unbuilt — OI-005 `OPEN`) |
| D-15 | commitment | COVERED | DEL-04-10 |
| D-16 | commitment | COVERED | DEL-04-08 |
| E-1 | commitment | COVERED | DEL-05-01 |
| E-2 | commitment | COVERED | DEL-05-02 |
| E-3 | commitment | COVERED | DEL-05-03 — **but E-3 is currently violated in fact; see B-011** |
| E-4 | commitment | COVERED | DEL-05-04 |
| E-5 | commitment | COVERED | DEL-05-05 |
| E-6 | commitment | COVERED | DEL-05-06 |
| E-7 | commitment | COVERED | DEL-05-07 |
| E-8 | commitment | COVERED | DEL-05-04 |
| v1-boundary | direction | COVERED | DEL-03-05, DEL-03-06 |
| obj-discipline | direction | COVERED | DEL-04-10 |
| cat-4.1 | direction | COVERED | DEL-04-10 |
| loop-4.2 | direction | COVERED | DEL-04-05, DEL-05-0x |
| judgments-4.2 | direction | COVERED | DEL-01-04 |
| cat-4.3 | direction | COVERED | DEL-04-10 |
| registry-discipline | direction | COVERED | DEL-02-05 |
| selfapp-6.1 | direction | COVERED | DEL-03-06 |
| selfapp-6.2 | direction | COVERED | DEL-03-04, DEL-06-01 |
| practice-6.2 | direction | COVERED | DEL-06-03 |
| concurrency-6.3 | direction | COVERED | DEL-06-02 |
| variants-7.1 | direction | COVERED | DEL-06-04 |
| promotion-7.2 | direction | COVERED | DEL-06-06 |
| nongoals-8.1 | non-goal | COVERED | DEL-01-08, DEL-0x |
| F1 | falsifier | COVERED | DEL-06-01 |
| F2 | falsifier | COVERED | DEL-06-01 |
| F3 | falsifier | COVERED | DEL-06-01 |
| F4 | falsifier | COVERED | DEL-04-10 |
| F5 | falsifier | COVERED | DEL-01-01 |
| F6 | falsifier | COVERED | DEL-04-08 |
| release-8.3 | direction | COVERED | DEL-06-07 |
| RD-1 | ruling | COVERED | DEL-01-01 |
| obl-a | obligation | COVERED | DEL-01-01 |
| obl-b | obligation | COVERED | DEL-01-01 |
| obl-c | obligation | COVERED | DEL-01-01 |
| RD-2 | ruling | COVERED | DEL-01-07 |
| RD-3 | ruling | COVERED | DEL-01-01 |
| RD-4 | ruling | COVERED | DEL-04-08 |
| RD-5 | ruling | COVERED | DEL-01-07 |
| annex-10.1 | obligation | COVERED | DEL-04-09 |
| C-1 | conflict | COVERED | DEL-01-01 |
| C-2 | conflict | COVERED | DEL-01-02 |
| C-3 | conflict | COVERED | DEL-01-08 |
| C-4 | conflict | COVERED | DEL-01-08 |
| adoption-10.3 | direction | COVERED | DEL-03-06 |

**Root coverage totals: 84/84 dispositioned; 0 GAP.** Reverse trace: 51/51 TRACED, 0 UNTRACED. Scope ledger: 103 rows (IN 94 / OUT 9 / TBD 0); 0 unassigned; every IN item maps to ≥1 deliverable.

**Reviewer note.** The register closes, and I do not dispute it. What the register cannot see is that O-2's runtime clause and O-10 are both carried by one `REQ_SLICE` deliverable whose own register entry says "no implementation change implied." Coverage at PRD-item granularity is satisfied; ownership of the runtime *work* is not established. That is B-002, and it is a gap at PRD level, not a decomposition defect.

### 3.2 App — coverage matrix (objectives complete; commitments by declared groups)

**Grouping rule (stated explicitly as brief §7.3 permits).** App's admitted commitments are too numerous to row-enumerate (128 FR + 31 NFR + 34 KG + 25 Goals + 30 Principles + non-goals = 248+ addressable items). I therefore (a) enumerate **all 10 objectives completely**, and (b) enumerate **all commitment groups completely** — where a "group" is a PRD requirement family or the package-level bands used by the PRD's own §16 traceability table, the only ID-level map that exists.

**Objectives (all 10, from decomposition §6):**

| Objective | Statement (abbrev.) | Mapped scope items | Disposition |
|---|---|---|---|
| OBJ-001 | Governed local desktop harness centred on human–agent dialogue | SOW-001–008, 023 | COVERED (PKG-02 + DEL-05-04, DEL-08-02/03) |
| OBJ-002 | Product-owned runtime contracts and thin route boundaries | SOW-009–018, 037–040 | COVERED **but semantically contested** — see B-001/B-025 |
| OBJ-003 | Auditable accepted turns / messages / outcomes / replay | SOW-014–015, 039–046, 059, 061 | COVERED (PKG-05) |
| OBJ-004 | Provider-adapter architecture, first governed replaceable adapter | SOW-016–021, 044–046, 051 | COVERED (PKG-04) |
| OBJ-005 | Tools only through deterministic capability policy | SOW-047–064, 076 | COVERED (PKG-06) |
| OBJ-006 | Filesystem project truth preserved | SOW-024–034, 075, 077 | COVERED (PKG-07) |
| OBJ-007 | Agent-suite integrity, governed subagent delegation | SOW-005–006, 017, 030–031, 063 | COVERED (PKG-08) |
| OBJ-008 | Validation, packaging, release, network, key checks | SOW-019–022, 035–036, 072–073, 078 | COVERED (PKG-09) |
| OBJ-009 | Professional boundary, product identity, reliance-boundary ownership | SOW-065, 071, 074, 076–077 | COVERED (PKG-01) |
| OBJ-010 | Future domain-engine compatibility without solver capture | SOW-066–071 | COVERED (PKG-10) |

**Objective totals: 10/10 COVERED, 0 unmapped.** Scope ledger: 78 rows (IN 74 / OUT 4 / TBD 1 — SOW-073); every IN row carries ≥1 deliverable.

**Commitment groups (complete enumeration):**

| Group | Population | ID-level trace instrument | Disposition |
|---|---|---|---|
| Product Goals 1–25 (§3.1) | 25 | PRD §16 (goal numbers only, for PKG-01/PKG-02) | **PARTIAL** — only Goals 4, 6, 9–11, 18, 21–25 named; Goals 1–3, 5, 7–8, 12–17, 19–20 have no ID-level home |
| Non-Goals (§3.2) | 26 bullets | DEL-01-04 + SOW-065/076/077/078 | COVERED as a group; no per-bullet trace |
| Product Principles 1–30 (§5) | 30 | none | **GAP at ID level** — no instrument maps principles to deliverables |
| FR-001..FR-128 (§8) | 128 | PRD §16 only (decomposition references **0** FR IDs) | **DEFECTIVE** — 50/128 claimed by ≥2 packages; 8/128 by none. See B-020 |
| NFR-001..NFR-031 (§11) | 31 | §16 names only NFR-028..031 | **PARTIAL** — 27/31 unassigned anywhere |
| KG-001..KG-034 (§15) | 34 | §16 names KG-016..020, KG-021..032 | PARTIAL |
| API requirements (§9.1–9.5) | 5 sub-sections | SOW-009–011, 037–040 → PKG-03 | COVERED |
| Data/file requirements (§10.1–10.10) | 10 sub-sections | SOW-024–029, 039–046 → PKG-05/07 | COVERED |
| Validation plan (§12.1–12.8) | 8 sub-sections | SOW-035–036 → PKG-09 | COVERED |
| Runtime sequence R0–R7 (§13) | 8 phases | §16 roadmap table | COVERED as sequencing overlay (DEC-012) |
| §17 Shared Runtime Amendment (second §17) | 1 block | **none** — carried by OI-007 + 16/53 `_STATUS.md` Remaining | **GAP** — see B-022 |
| §17 Approval and Change Control (first §17) | 1 | self-referential | COVERED |
| `contract_invariant_coverage_register.csv` | required-or-deferred | absent, no deferral ruling | **GAP** — see B-023 |

**App coverage totals: 10/10 objectives COVERED; 13 commitment groups — 6 COVERED, 4 PARTIAL, 3 GAP/DEFECTIVE.**

### 3.3 PEC — coverage matrix (objectives and requirement families complete)

**Grouping rule:** PEC's admitted commitments are its 11 product invariants and 8 requirement families; authoritative populations are `ScopeLedger.csv` (94 rows) and `Deliverables.csv` (64 rows).

**Objectives (all 6), recomputed deliverable counts:**

| Objective | Deliverables supporting | Disposition |
|---|---|---|
| OBJ-001 | 20 | COVERED |
| OBJ-002 | 12 | COVERED |
| OBJ-003 | 12 | COVERED |
| OBJ-004 | 10 | COVERED |
| OBJ-005 | 7 | COVERED |
| OBJ-006 | 9 | COVERED |

**UnmappedObjectives = 0** (independently confirmed).

**Requirement families (all 8 complete):**

| Family | Requirements | Disposition |
|---|---|---|
| PEC-ORI (orientation) | 001–006 | COVERED |
| PEC-RCN (reconciliation) | 001–006 | COVERED |
| PEC-GAT (gate/slate) | 001–004 | COVERED (SOW-022, 023 objective-unmapped) |
| PEC-PRS (presence) | 001–007 | COVERED |
| PEC-STR (streams/ingest) | 001–005 | COVERED; **all objective-unmapped** |
| PEC-API | 001–005 | COVERED; SOW-044 objective-unmapped |
| PEC-DSH (dashboards) | 001–007 | COVERED |
| PEC-SVC (service) | 001–006 | COVERED |
| PEC-K-01..K-11 (invariants) | 11 | carried as constraints C1–C15 (DL-7), except SOW-025/055/056 | COVERED by declared convention |

**Scope ledger totals (recomputed): 94 rows — IN 71 / OUT 14 / TBD 9; 0 IN rows without a deliverable mapping.**

**Recorded residue (disclosed by PEC itself, confirmed by me):** 11 IN scope items and 9 deliverables carry no ObjectiveID — my independent recompute returns exactly 11 IN rows (SOW-022, 023, 033–038, 044, 063, 087) and 9 deliverables (DEL-00-02, 03-05, 05-01, 07-02, 07-03, 07-04, 07-05, 08-05, 10-08). See B-028.

**PEC coverage totals: 6/6 objectives COVERED; 8/8 requirement families COVERED; 11 invariants dispositioned; 32/64 deliverables contracted by deliberate sequencing (not a gap).**

---

## 4. Boundary and ownership matrix (cross-product)

Every cell is evidenced at the freeze or marked **UNKNOWN**.

### 4.1 Shared runtime (protocol, daemon, client, CLI, sessions, credentials, engines, residency)

| Aspect | Finding |
|---|---|
| Semantic owner | **Root** — D-GOV-20 item 1 ("root-owned `runtime/` workspace"); `AGENTS.md` §Shared Runtime Doctrine; `runtime/README.md` ("The daemon is the sole owner of engines, credentials, sessions, delegation, turn locks, interruption, tools, and local-model residency") |
| **Contested by** | **App decomposition v3.2 §13 line 611**: "Root `runtime/` ownership is an implementation-location change; app-dev deliverables retain semantic ownership" — an accepted instrument asserting the opposite. **Divided ownership on the record (B-001).** |
| Producers | Root `runtime/packages/{contracts,core,daemon,client,cli,engine-claude,engine-pi-omlx}` (7 packages, verified present) |
| Consumers | App (`frontend/src/lib/runtime-client/{daemon-harness-port.ts,runtime-daemon-harness-port.ts}`, `frontend/electron/runtime-host.ts`); PEC (prospective: DEL-07-02, DEL-07-05); CLI |
| Authoritative record | D-GOV-20 + D-T0-23 for architecture; `runtime/README.md` for package roles. **No Root PRD commitment, scope item, or deliverable states the runtime contract's content** beyond O-2(c)/O-10 |
| Compatibility obligation | **UNKNOWN / not established.** `@chirality/runtime-contracts` declares `version: 0.1.0` while the governed identity is `FLOW_A_CONTRACT_VERSION = 'flow-a.contract.v0.1.0'` (D-T0-09). No instrument states the rule between them, nor who may bump either (B-003) |
| Fallback / degraded mode | **UNKNOWN for App.** D-T0-23 §Failure boundary specifies fail-closed **for PEC agent execution** only. No accepted record states what App does when the daemon is absent |
| Routed change path | Root M2 tranche + D-11 routed notice. **Exercised inconsistently**: D-GOV-20 itself shipped 0 routed notices (B-007) |

### 4.2 Work surface / UI (reusable human–agent surface)

| Aspect | Finding |
|---|---|
| Semantic owner | **None established.** App PRD owns the *App's* Woven Dialogue shell (Goals 4, 23–25; PKG-02). No accepted instrument assigns ownership of a *reusable* work surface |
| Producers | App PKG-02 (5 deliverables) |
| Consumers | App only. PEC §16 open decision 5 (PEC UI placement) undecided |
| Authoritative record | App decomposition PKG-02; charter's "reusable work surface" is **clarified framing / open question**, not accepted basis |
| Compatibility obligation / Fallback | N/A — no reuse contract exists |
| Routed change path | App SCA / D-APP |
| Verdict | **Not a conformance gap** (charter §7 holds this open; brief §5 forbids counting candidate absence as a gap). Routed as owner-decision request (B-010) |

### 4.3 Coordination projection

| Aspect | Finding |
|---|---|
| Semantic owner | **PEC** — PRD v2.1 §1.1, §4.1 |
| Producers | PEC record tier (reconciled) + presence tier (TTL'd) |
| Consumers | harnesses on behalf of agents (PEC-K-03); human owner via dashboards |
| Authoritative record | `projects/pec/docs/PRD.md` v2.1; PEC output **never citable as authority** (PEC-K-02) |
| Compatibility obligation | PEC-API-003 (versioned schema, additive evolution) |
| Fallback / degraded mode | **Explicit and strong** — PEC-K-01 graceful absence; PEC-SVC-004 kill test as standing release gate; §11 falsification clause |
| Routed change path | D-PEC ruling + F-PEC-1 per-tranche packet |
| Verdict | **Clean.** Best-specified boundary in the corpus. No accepted record makes a governed act require PEC |

### 4.4 Dependency truth

| Aspect | Finding |
|---|---|
| Semantic owner | **Each deliverable** (deliverable-local registers authoritative) |
| Authoritative record | Root PRD O-8 / K-DEP-1, K-DEP-2: "No central dependency graph is *authoritative*" |
| Producers/consumers | PEC: 64 local `Dependencies.csv` (254 rows, 135 ANCHOR / 119 EXECUTION) — recomputed, no central register. App: `Dependencies.csv` v3.1 (DEL-07-05). Root: DEL-03-03 |
| Compatibility obligation | Schema v3.1 (App); `RegisterSchemaVersion` column (PEC) |
| Fallback | Files are the substrate |
| Verdict | **Clean and consistent across all three products.** PEC's "no central register by owner decision" conforms to Root O-8 |

### 4.5 SOW method layer

| Aspect | Finding |
|---|---|
| Semantic owner | **Root** — `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` (D-GOV-16), `skills/scope-of-work/`, `tools/scope_of_work/` |
| Consumers | Root (45 SOWs), PEC (32 SOWs). **App does not use this method** — its 53 SOWs diverge |
| Compatibility obligation | Method amendments v1–v6.1; **no version field in SOW frontmatter** to record authoring era (B-016) |
| Verdict | Working. Current-tool rerun: Root 45/45 PASS, PEC 32/32 PASS |

### 4.6 Authority-corpus pinning

| Aspect | Finding |
|---|---|
| Semantic owner | **Each consuming loop** pins its own corpus |
| Producers/records | App: `AUTHORITY_CORPUS.json` v17 (8 refs; 8/8 CLEAN). Root: `domains/chirality/_Sources/Source_Manifest.csv` (126 CLEAN / 93 DRIFT / 6 MISSING). App-dev pack: 467 rows (119/129/219) |
| **Structural defect** | App's v17 pins `docs/SPEC.md` / `docs/CONTRACT.md` — but these resolve to **App's own** documents. Hash proof: v17 pin `eee520f78…` = App file; Root's `docs/SPEC.md` = `988c4b902…`, pinned nowhere in App's corpus. **App has no deterministic detector for Root doctrine drift** (B-006) |
| Fallback | Routed notices — the only path for App, and incomplete (B-007) |

### 4.7 Notice routing

| Aspect | Finding |
|---|---|
| Semantic owner | **Root** (D-11; `AGENTS.md` change-notice rule) |
| Consumers | App, PEC, Piping, domain packs |
| **Measured coverage at freeze** | Notices exist for **D-GOV-21, 23, 24, 26 only**. D-GOV-20, 22, 25, 27 shipped **zero**. Recipients: App 4/4; `domains/chirality` 3/4; **PEC 0/4**; **Piping 0/4**; all other packs 0 |
| Compatibility obligation | "same tranche" delivery — not met for D-GOV-20/22/25/27 |
| Fallback | Downstream deterministic corpus-drift checks — **absent at App for Root docs** (B-006), absent at PEC and Piping entirely |
| Verdict | **Specified but not reliably operating** (B-007) |

### 4.8 Domain-engine profiles

| Aspect | Finding |
|---|---|
| Semantic owner | **Tier-0 / `_DomainEngines`** — `profiles/pec.yaml`, D-T0-06, D-T0-12 |
| **Duplication** | `domain-profile.ts` / `operation-proposal.ts` now exist as **root runtime code** while App DEL-10-01 is the accepted owner of the "DomainEngineProfile Contract Draft" and FR-107/FR-108 assign it to App. Two claimed owners; no supersession (B-009) |
| Compatibility obligation | UNKNOWN |
| Domain truth boundary | **Held.** K-DOMAIN-1 exemption intact; PEC §13 retires its L3 lane; App non-goal on protected-path writes stands. No instance found of generic infrastructure absorbing domain truth |

### 4.9 Resource governance (candidate)

| Aspect | Finding |
|---|---|
| Semantic owner | **None — and correctly so.** Described only by the charter. Manifest: "not accepted Root, App, or PEC scope" |
| All other cells | N/A at the freeze |
| Verdict | **Absence is not a gap** (brief §5; charter candidate-architecture row). Owner-decision material only |

### 4.10 Human judgment as the hinge (cross-cutting)

| Aspect | Finding |
|---|---|
| Semantic owner | **The human** — K-AUTH-1, K-AUTH-2, PRD N-3, §4.2 three judgments, §8.3 |
| Machine gates observed | Root G1–G4 (registered, passing, "holds no authority and confers none"); PEC gate evaluation (advisory, PEC-GAT-002/004); App F-APP-4 fencing CHECKING→ISSUED |
| **Anomaly** | `validate_harness_contract_pull.py` reports "validation passed" while all 12 pinned SHAs are stale, because it validates against the pinned historical commit, not the working tree (B-004) |
| Verdict | **No machine gate has absorbed a human acceptance/issuance judgment.** The single anomaly is false *assurance*, not authority capture |

### 4.11 Self-authorization / circularity check

| Aspect | Finding |
|---|---|
| Root self-application | Contained: F3; OI-008 keeps materialization behind the §5.3 gate; work-graph nodes returned to `pending` between phases |
| PEC self-ingestion | PRD §12: first loop ingested is "its own build" — bounded by "no node depends on the capability it is creating… grants no authority and changes no accepted scope without human approval" |
| Verdict | **No self-authorizing loop found.** Both arrangements carry an explicit non-circularity rule — a genuine architectural strength |

---

## 5. Findings register

### 5.1 Declared observation boundary (stated once, governs every severity below)

- **BLOCK** — two or more *accepted* instruments assert incompatible facts about ownership, authority, or scope, such that a downstream executor cannot act correctly without an owner ruling. Bounded to the named instruments and files; **never** a claim that the product is unsafe, unfit, or globally defective (D-GOV-02).
- **REVIEW** — an owner decision or governed act is required to close the item; work may continue, but reliance on the affected surface is not warranted.
- **WARN** — a real defect with bounded consequence, correctable inside an existing instrument without an owner ruling on substance.
- **INFO** — an observation, including recorded conformance.

Severities describe **the reviewed basis at commit `da31c19b5`** and nothing outside it. A finding against a *derived* or *navigational* surface never impeaches the instrument it points to. Where the basis cannot decide, I state **UNKNOWN** and assign no severity above WARN.

**Counts: 34 findings — 1 BLOCK, 11 REVIEW, 14 WARN, 8 INFO.**

### 5.2 Cross-product findings

---

**B-001 · CROSS_PRODUCT (Root ↔ App) · Class: authority conflict · Severity: BLOCK · Confidence: HIGH**

**Assertion.** The accepted App decomposition asserts that app-dev deliverables retain *semantic ownership* of the shared runtime, contradicting four other accepted instruments that place semantic ownership at Root.

**EvidenceRefs.**
- `…/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §13, line 611: *"Shared runtime promotion preserves this decomposition's existing package/deliverable topology. Root `runtime/` ownership is an implementation-location change; app-dev deliverables retain semantic ownership and acceptance evidence through the SCA-APP-003 impact map."*
- `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md` item 1: "becomes a **root-owned** `runtime/` workspace"; item 2: daemon "**exclusively owns** runtime engines, credentials, sessions, delegation, tools, turn locks, interruption, and local-model residency."
- `_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_domain_convergence.md` item 2: "Runtime transport, sessions, credentials, engine execution, managed delegation, interruption, replay, and residency are **shared infrastructure**."
- `AGENTS.md` §Shared Runtime Doctrine (line 264ff).
- `projects/chirality-app-dev/docs/PRD.md` §17 (second, line 1692ff): the runtime is "a **root-owned product subsystem rather than a frontend-owned singleton**." — App's own PRD contradicts App's own decomposition.

**Consequence.** "Shared" has become divided ownership on the record. An executor of App PKG-03 (DEL-03-01 "AgentEnginePort and Engine Conformance Suite", DEL-03-02 "Thin TurnEngine" — exactly the migrated surfaces) has an accepted instrument saying it owns the semantics while Root's say Root does. Any runtime-contract change can be justified by one instrument and prohibited by another.

**SmallestAction / Owner.** App SCOPE_CHANGE amending §13's note to state App holds **client-integration and acceptance-evidence** ownership while semantic ownership sits with Root under D-GOV-20/D-T0-23; owner ruling recorded as a D-APP decision. No topology change required. If the owner instead intends App to retain semantic ownership, the correcting instrument is a Root governance act amending D-GOV-20 — not a decomposition note.

---

**B-002 · ROOT · Class: ownership gap · Severity: REVIEW · Confidence: HIGH**

**Assertion.** No Root package or deliverable owns the shared-runtime contract, conformance, compatibility, migration, security, or release evidence; the runtime substrate enters the accepted decomposition through exactly one conformance slice.

**EvidenceRefs.**
- Sweep of `chirality_root_scope_ledger_v1_0.csv`: **2 of 103** scope items mention "runtime" — SOW-027 (three-layer authority boundary) and SOW-028 (delegation hierarchy, where "runtime" is an adjective for the agent hierarchy).
- `chirality_root_deliverable_register_v1_0.csv`, DEL-02-02: `CoversScopeItems` = SOW-027;SOW-035; `Type` = REQ_SLICE; `ContextEnvelopeNotes` = "…**no implementation change implied**."
- Forward register: O-2 → DEL-02-02 only; O-10 → DEL-02-02 only.
- Against: D-GOV-20 §Ruled architecture (10 items), §Local residency boundary (6 rules), §Implementation gates ("Daemon/client/CLI, Desktop migration, PEC migration, security review, and regression review remain separately bounded"); `runtime/` contains 7 real packages.
- Cause (not a defect): DEC-001 makes the PRD the **sole** scope source; §2.3 lists incorporated documents as "non-source, generates no scope"; D-GOV-20 is not even listed as interpretive context.

**Consequence.** Root is the accepted semantic owner of a substantial executable subsystem its own decomposition schedules no work against. Continuing conformance, version/compatibility policy, credential and residency security review, and cross-client conformance proofs have no owning deliverable — which is also why B-001 could arise without tripping anything and why B-003 has no owner to correct it.

**SmallestAction / Owner.** This is a **PRD-level** gap, not decomposition repair (D-9 forbids inventing packages). Least expansive lawful route: a **Root PRD amendment** (M2 tranche under D-13/D-16) adding an operative commitment stating the runtime-contract obligation, then a SCOPE_CHANGE adding deliverables under PKG-02. Owner decision required on amend-vs-record-explicit-deferral (the OI-013/§12.1 mechanism already exists).

---

**B-003 · CROSS_PRODUCT (Root ↔ App ↔ Piping) · Class: semantic conflict · Severity: REVIEW · Confidence: HIGH**

**Assertion.** The governed contract identity `flow-a.contract.v0.1.0` no longer identifies the contract's content, owner, or location: content moved to Root, App files became deprecation shims, version string unchanged.

**EvidenceRefs.**
- `runtime/packages/contracts/src/harness/sdk-version.ts:1`: `export const FLOW_A_CONTRACT_VERSION = 'flow-a.contract.v0.1.0';` (now in **Root**).
- `projects/chirality-app-dev/frontend/packages/harness-contract/src/agent-engine-port.ts` (full content): `/** @deprecated Import from '@chirality/runtime-contracts/agent-engine-port'. */ export * from '@chirality/runtime-contracts/agent-engine-port';`
- SHA recompute of the D-APP-48 pull contract's 12 `exports[].sha256` against live files: **0 CLEAN / 12 DRIFT / 0 MISSING**.
- `D-T0-09_flow_a_contract_version_value.md` O-A: "The decision record, not the string alone, binds the referenced SDK version, tool-registry version, event-vocabulary source, **package path**, and eventual SHA pin" — the bound package path is now shims.
- `runtime/packages/contracts/package.json`: `"version": "0.1.0"` — a second, unreconciled version identity.
- D-T0-07 assigns contract-versioning ownership to Tier-0; no D-T0 record rules on the post-migration identity.

**Consequence.** Two consumers pin a version string that cannot detect the change it exists to detect. Version comparison — the cheapest compatibility check — is structurally blind here.

**SmallestAction / Owner.** A **Tier-0 decision (D-T0-\*)** under D-T0-07 that either bumps `FLOW_A_CONTRACT_VERSION` to a new generation and re-pins App and Piping, or records that the value is deliberately carried forward and states what it now binds.

---

**B-004 · CROSS_PRODUCT · Class: overreach (false assurance) · Severity: REVIEW · Confidence: HIGH**

**Assertion.** The validator cited as the enforcement mechanism for the D-APP-48 SHA-pinned pull contract cannot detect drift of the pinned files, and reports "passed" while all 12 pinned SHAs are stale.

**EvidenceRefs.**
- Tool basis: `tools/coordination/validate_harness_contract_pull.py` at freeze `da31c19b5`, invoked via the contract's own `validation.pullContractValidationCommand`. Result: `harness contract pull validation passed`, **exit 0**.
- My independent recompute of the same 12 values against the working tree: **12/12 DRIFT**.
- Root cause, lines 84–93: the validator reads each export target with `git_blob(repo_root, commit, target_path)` where `commit = source.commitSha` (`55a066fdff…`) and compares against `entry['sha256']`. **It compares the pinned commit to itself and never reads the working tree.**
- `D-APP-48_RULING_2026-07-04.md:36` describes the mechanism as binding "`flow-a.contract.v0.1.0`, export targets, and SHA-256 checksums".

**Consequence.** A reader who runs the ruled validation command and sees "passed" will reasonably conclude the mirror is current. It is not, and no execution of this tool can ever say otherwise. The clearest instance in the corpus of a machine gate offering assurance outside its real observation boundary.

**SmallestAction / Owner.** **Documentary, not code**: amend the D-APP-48 record (or a successor) to state the validator's actual observation boundary — "verifies the pinned snapshot's internal consistency at `source.commitSha`; does **not** verify currency against the working tree." A currency check is a separate, larger act and should be routed as its own proposal. Owner: App loop (D-APP), with Tier-0 notification since D-T0-09 relies on the same mechanism.

---

**B-005 · CROSS_PRODUCT (Piping exemplar) · Class: trace gap · Severity: REVIEW · Confidence: HIGH**

**Assertion.** Piping's harness-contract consumption record is stale, fails the repo's own validator, and Piping received no routed notice of any change that made it stale.

**EvidenceRefs.**
- `projects/chirality-piping/execution/_Coordination/_DECISIONS/D-30_HARNESS_CONTRACT_CONSUMPTION_2026-07-04.json`: `pullContractPath` → the D-APP-48 contract (12/12 stale); `package.path` = the now-shimmed App package; `constants.harnessToolRegistryVersion` = `harness-tools.v6.mutating-mcp`.
- The App pull contract it consumes declares `harness-tools.v14.headless-preview-live` — Piping is **eight tool-registry generations behind its own declared source**, while both declare the same `flowAContractVersion`.
- Tool basis `validate_harness_contract_pull.py` at `da31c19b5` with `--consumption-record`: `ERROR: consumption source.commitSha mismatch`, **exit 1**.
- Notice sweep: `projects/chirality-piping/` contains **zero** routed D-GOV notices.

**Consequence.** The situated-product exemplar behaving exactly as the notice architecture predicts when notices are not sent: the inherited pin decays silently, the validator fails on a record-to-record mismatch that does not describe the real problem, and nothing routes the real change to the party relying on it. The inheritance chain is two hops deep (Root → App → Piping) with no instrument owning the second hop.

**SmallestAction / Owner.** Piping loop re-pins D-30 against the current pull-contract generation once B-003 is ruled. Root/Tier-0 ships the notice D-11 already requires. Sequencing: B-003 first.

---

**B-006 · CROSS_PRODUCT (Root → App) · Class: ownership gap · Severity: REVIEW · Confidence: HIGH**

**Assertion.** App's authority corpus contains no Root governance document, so the "deterministic detection path" the notice architecture relies on as its backstop does not exist at App for Root doctrine changes — and a routed notice asserts that it does.

**EvidenceRefs.**
- `AUTHORITY_CORPUS.json`, `current_version: v17`, `refs`: `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, `docs/PRD.md`, `AGENT_SOFTWARE_DECOMP.md`, `AGENT_DOMAIN_ENGINE.md`. Only the last two are Root files.
- Hash proof the four `docs/*` refs are **App-local**: v17 pin for `docs/SPEC.md` = `eee520f783ce…`; App's file = `eee520f783ce…` (**MATCH**); Root's `docs/SPEC.md` = `988c4b902877…` (**differs**). Same for `docs/CONTRACT.md`: pin `6d3a082c5f08…` = App file; Root file `1a448a822084…`.
- Claim under test — `NOTICE_D-GOV-26_SPEC_CONTRACT_AMENDMENTS.md` §"Why this loop is notified": *"`AUTHORITY_CORPUS.json` pins both `docs/SPEC.md` and `docs/CONTRACT.md` by sha256; **both hashes change with this tranche**. Corpus-drift checks remain the deterministic detection path."*
- Fact: D-GOV-26 changed **Root's** SPEC/CONTRACT. App's v17 pins are **8/8 CLEAN**. No hash changed; no drift check could have fired.
- `AGENTS.md` change-notice rule: "Downstream loops still detect such changes through their own deterministic checks (corpus-drift status); this rule exists so detection does not depend on that alone." — the stated redundancy is absent.

**Consequence.** The manifest calls this "one notice that misidentifies its stale target." It is worse: the notice misidentifies the *detection architecture*. For Root doctrine changes at App there is exactly one channel, and B-007 shows it is used inconsistently.

**SmallestAction / Owner.** App loop: add the Root governance documents App inherits (`AGENTS.md`, root DIRECTIVE/CONTRACT/SPEC/TYPES) to `AUTHORITY_CORPUS.json` as a distinct ref namespace at the next bump, so path collisions cannot conflate them (B-008). Root loop: correct the D-GOV-26 notice's detection claim by superseding notice, not edit.

---

**B-007 · CROSS_PRODUCT · Class: omission · Severity: REVIEW · Confidence: HIGH**

**Assertion.** Routed coordination notices were shipped for only 4 of the 8 most recent Root governance decisions, and two declared downstream consumers (PEC, Piping) received none at all.

**EvidenceRefs.** Repo-wide sweep for `*NOTICE*D-GOV-<n>*` at the freeze:

| Decision | Notices | Recipients |
|---|---|---|
| D-GOV-20 (shared runtime — the ruling that created the seam) | **0** | — |
| D-GOV-21 | 2 | App, `domains/chirality` |
| D-GOV-22 (Root PRD adoption) | **0** | — |
| D-GOV-23 | 2 | App, `domains/chirality` |
| D-GOV-24 | 2 | App, `domains/chirality` |
| D-GOV-25 (decomposition acceptance) | **0** | — |
| D-GOV-26 | 1 | App only |
| D-GOV-27 (instruction-surface supersession; 45 lifecycle transitions) | **0** | — |

Recipient-side: `projects/pec/execution/_Coordination/` holds 2 notices, **neither a D-GOV doctrine notice**. `projects/chirality-piping/`, `domains/chirality-app-dev/`, `domains/chirality-piping/`, `domains/piping-design/`, `_DomainEngines/`: **zero** each.

**Consequence.** D-11 requires the notice "in the same tranche." D-GOV-27 is the most consequential omission: it superseded the instruction-surface enumeration (PRD §5.2 O-1 → `docs/SPEC.md` §0.2.1), exactly a surface downstream loops pin and mirror. D-GOV-20 is second: it created the cross-product runtime seam that B-001, B-003 and B-005 all descend from, with no consumer formally notified. PEC is a *declared distinct client* of the Root runtime (D-T0-23 item 1) and has never received a Root doctrine notice.

**SmallestAction / Owner.** Root loop: ship the outstanding notices for D-GOV-20, 22, 25, 27 to App, PEC, Piping and the domain packs as a single coordination tranche. Coordination only — each loop still adopts, amends, or declines under its own instruments. Root DEL-04-04 is the owning deliverable and already exists.

---

**B-008 · CROSS_PRODUCT · Class: semantic conflict · Severity: WARN · Confidence: HIGH**

**Assertion.** Three loops each maintain governance documents at identical relative paths, so a bare reference such as `docs/SPEC.md` is ambiguous — and at least one routed notice has already been misread because of it.

**EvidenceRefs.**
- `docs/` (Root): CONTRACT, DIRECTIVE, PLAN, PRD_ROOT, SPEC, TYPES. `projects/chirality-app-dev/docs/` and `projects/chirality-piping/docs/`: CONTRACT, DIRECTIVE, PLAN, PRD, SPEC, TYPES.
- Content differs: Root `docs/SPEC.md` = `988c4b902877…`; App = `eee520f783ce…`.
- Consequence realised in B-006's notice text, and in App PRD §16's source table which lists "`docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`" without qualifying which loop's copy.
- App decomposition REF-001..004 pin the App-local copies by SHA — correctly, but only because the SHA disambiguates what the path does not.

**Consequence.** Notices, pins, and prose cross-references cannot be resolved by path alone. A structural amplifier of B-006 and B-007.

**SmallestAction / Owner.** Documentary convention: require loop-qualified paths (`{REPO_ROOT}/docs/SPEC.md` vs `{WORKING_ROOT}/docs/SPEC.md`) in notices and cross-loop references. Root `docs/SPEC.md` §0.2–§0.3 already defines the `{*_ROOT}` token registry (PRD O-6); the mechanism exists and is unused for this. Owner: Root, via DEL-04-04.

---

**B-009 · CROSS_PRODUCT (Root ↔ App) · Class: ownership gap · Severity: WARN · Confidence: MEDIUM**

**Assertion.** Domain-engine contract shapes now exist in Root's generic runtime contracts package while App's accepted decomposition still names App as the owner, with no supersession recorded.

**EvidenceRefs.** `runtime/packages/contracts/src/harness/domain-profile.ts` and `operation-proposal.ts` exist; `package.json` exports `./domain-profile`, `./operation-proposal`. App decomposition §8 PKG-10 DEL-10-01 "DomainEngineProfile Contract Draft" (`API_CONTRACT`, IN_PROGRESS). App PRD FR-107/FR-108 assign the contract to PKG-10 via §16. No D-APP or D-T0 record transfers ownership.

**Consequence.** Two claimed owners for one contract shape. Lower severity than B-001: PKG-10 is explicitly future-boundary scope (OI-005) and the Root files are contract *shapes*, not domain truth — K-DOMAIN-1 is intact. But activating PKG-10 later means activating against a contract that already exists elsewhere.

**SmallestAction / Owner.** Record the disposition before PKG-10 activation: an App SCA noting DEL-10-01 is satisfied-in-part by the Root-hosted shape, or a Tier-0 record placing it with Root. No action needed while PKG-10 remains future-gated.

**UNKNOWN.** Whether the Root-hosted files were intended as the FR-107/FR-108 contract or an unrelated transport type cannot be decided from the frozen basis.

---

**B-010 · CROSS_PRODUCT · Class: observation (owner-decision request) · Severity: INFO · Confidence: HIGH**

**Assertion.** No accepted instrument assigns ownership of a reusable work-surface or application-integration contract; the corpus does not currently rely on one, so this is a preserved open question rather than a gap.

**EvidenceRefs.** §4.2 boundary matrix. Charter §04 records the application environment profile as **candidate requirement** and §07 holds "whether the reusable work surface is a Root requirement, an App capability, or both" open. PEC §16 item 5 leaves PEC UI placement undecided.

**Consequence.** None at the freeze — I found no scope item, deliverable, or SOW in any product depending on a reusable work-surface contract existing. Recorded so the absence is visibly a decision rather than an oversight.

**SmallestAction / Owner.** No action required. Routed as a decision request with criteria in §7.2. Per brief §5 and charter §5, absence of candidate architecture is **not** a scope gap and I do not count it as one.

---

### 5.3 Root findings

---

**B-011 · ROOT · Class: semantic conflict · Severity: REVIEW · Confidence: HIGH**

**Assertion.** PRD commitment E-3 ("the three SHA roles are distinct and recorded distinctly") is violated on the Root decomposition itself: the same commit carries two different role names across two accepted surfaces.

**EvidenceRefs.**
- `D-GOV-25_root_decomposition_acceptance.md` line 6 `CandidateMergeSHA: ea0ad7a566ddb51d89297bfcf491636f1fc5dd15 (merge of PR #347…)`; line 8 `EffectiveSHA: 653fabc9b3e8abf369f5e776a7d3ee24bf235e7a (merge of PR #348…)`.
- `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` line 9: `**EffectiveSHA:** ea0ad7a566ddb51d89297bfcf491636f1fc5dd15 (merge of PR #347)`.
- Therefore `ea0ad7a56…` is `CandidateMergeSHA` in the accepting decision and `EffectiveSHA` in the accepted artifact. PRD §5.4 E-3 requires roles be "recorded distinctly."

**Consequence.** A consumer resolving "the EffectiveSHA of the accepted root decomposition" gets two different commits depending on which accepted surface it reads. Not cosmetic: the 45 SOWs pin `653fabc9b…`, so the decomposition's own header disagrees with what its downstream contracts treat as the basis.

**SmallestAction / Owner.** Correct the decomposition header's label to `CandidateMergeSHA` (the decision record governs — PRD D-1). A working-surface correction under the decomposition's own §14 amendment rule, not a governance act. Owner: Root loop; DEL-05-03 (SHA Role Register) is the standing deliverable.

---

**B-012 · ROOT · Class: authority conflict · Severity: REVIEW · Confidence: HIGH**

**Assertion.** D-GOV-27's `EffectiveSHA` is unbound, leaving the largest single state change in the Root loop without a bound applied state under K-AUTH-2 — and simultaneously depriving the 45 SOW contracts of any SHA they could correctly re-pin to.

**EvidenceRefs.**
- `D-GOV-27_initialization_closing_rulings.md` line 6: `EffectiveSHA: (merge of the closing-tranche PR into 'main'; backfilled by a later tranche per precedent)` — a parenthetical, no SHA. Line 5 shows `PublicationSHA` **was** backfilled (`3ed51532751b…`), so the omission is specific.
- Lines 46–47: "approval binds at the merge SHA of the human-gated PR carrying it (the EffectiveSHA above, backfilled on merge)" — the record states its binding depends on the missing value.
- Contrast `D-GOV-26` line 6: `EffectiveSHA: 31b8dc94acca…` (bound).
- What D-GOV-27 carries: supersession of PRD §5.2 O-1 (per `docs/PRD_ROOT.md` pointer block lines 15–24); DEC-021 additive objective propagation; ResponsibleParty assignment across 45 deliverables; 45 OPEN→INITIALIZED transitions.
- PRD N-3 / K-AUTH-2: "approvals bind to a specific git SHA and are voided by content change."

**Consequence.** The instrument governing the current Root state is not bound to that state. Compounding: the 45 SOWs pin `653fabc9b…` and reflect post-D-GOV-27 content (B-013); there is no bound SHA representing the D-GOV-27 applied state to re-pin to. Manifest conditions 1 and 6 interact rather than merely coexist.

**SmallestAction / Owner.** Backfill D-GOV-27's `EffectiveSHA` following the precedent already used for D-GOV-26 and for D-GOV-27's own PublicationSHA. Owner: Root loop / CHANGE. Receipt 52 already records the debt.

---

**B-013 · ROOT · Class: trace gap · Severity: WARN · Confidence: HIGH**

**Assertion.** All 45 Root SOW contracts pin a decomposition basis whose content contradicts the contracts' own objective references for four deliverables; the pin no longer identifies the state each contract conforms to.

**EvidenceRefs.**
- All 45 carry, uniformly: `decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a` (`grep -h` over all 45 → 45 identical lines).
- Content at the pinned commit vs the freeze: decomposition `.md` `812e4484eec4…` → `14067a7d97c9…`; deliverable register `e97d2887dcbe…` → `699e99e7ac7e…`. **Both differ.**
- `SupportsObjectives` diff pinned→freeze: DEL-01-04 `OBJ-002`→`OBJ-002;OBJ-003`; DEL-03-01 `OBJ-007`→`OBJ-004;OBJ-007`; DEL-03-06 `OBJ-002`→`OBJ-002;OBJ-004`; DEL-06-04 `OBJ-005`→`OBJ-004;OBJ-005` (the four DEC-021 additions). `ResponsibleParty` changed for **45/45** (`TBD`→`Ryan Tufts`).
- The contracts' `package_objective_refs` match the **freeze** register: my comparison over all 45 returned **0 mismatches** — the contracts are substantively correct and the *pin* is what is wrong.

**Consequence.** Substance consistent; provenance not. A reader resolving `decomposition_basis` retrieves a register in which DEL-01-04 does not carry OBJ-003, while the contract asserts it does. Two surfaces with independent update paths, where the pin silently stopped tracking.

**SmallestAction / Owner.** Re-pin `decomposition_basis` across the 45 contracts to the D-GOV-27 applied state — **blocked on B-012**. Interim: record the dependency. Owner: Root loop.

---

**B-014 · ROOT · Class: semantic conflict · Severity: WARN · Confidence: HIGH**

**Assertion.** The accepted decomposition's working surface states in two places that `ResponsibleParty` is TBD for every deliverable, while its own authoritative register assigns a named party to all 45.

**EvidenceRefs.**
- §9 line 274: "`ResponsibleParty` is `TBD` for every deliverable — this run holds no assignment authority (OI-011)."
- §12 OI-011: Status `OPEN` — "Acceptance of the decomposition assigned no one to anything."
- §14: "Executors should… preserve `ResponsibleParty: TBD` until a human assigns it."
- Against, §13 Change Log: "`ResponsibleParty` was assigned (`Ryan Tufts`…) across the deliverable register and all 45 `_CONTEXT.md` files."
- Register fact: `ResponsibleParty` = `Ryan Tufts` for **45/45** rows (recomputed).

**Consequence.** §3 makes the register "authoritative for full deliverable fields," so the register governs and three prose passages are stale — including an instruction to executors to *preserve* a value that no longer exists. The manifest discloses OI-011 staleness; the §9 and §14 contradictions are additional surfaces not named there.

**SmallestAction / Owner.** Close OI-011 citing the D-GOV-27 assignment; correct §9 and §14 to point at the register. Working-surface update under §14's own amendment rule; no owner ruling on substance.

---

**B-015 · ROOT · Class: omission · Severity: WARN · Confidence: HIGH**

**Assertion.** `AGENTS.md` — the live index K-AGENTS-1 makes authoritative over narrative — contains no reference to the accepted decomposition's packages or deliverables.

**EvidenceRefs.** `grep -c -E "PKG-0[1-6]_|DEL-0[1-6]-" AGENTS.md` → **0**. `AGENTS.md` predates the decomposition (D-GOV-25, 2026-07-25). PRD O-5 / K-AGENTS-1: "the live registry is authoritative over any narrative list."

**Consequence.** An agent instantiated from `AGENTS.md` alone has no path to the six packages, 45 deliverables, or their contracts; discoverability (OBJ-1: "a reader can determine what governs, from the repository alone") is served only via `LOOP_INIT.md`. Bounded because that path works; recorded because OBJ-1 is tested rather than assumed and the B-stage trajectory (PRD §9.5) is exactly the reader who did not build it.

**SmallestAction / Owner.** Add a pointer (not an enumeration — registry discipline forbids a parallel list) from `AGENTS.md` to the accepted decomposition and `LOOP_INIT.md`. Instruction surface → M2 tranche. Owner: Root, DEL-02-01.

---

**B-016 · ROOT · Class: observation · Severity: WARN · Confidence: HIGH**

**Assertion.** The candidate status of every AC-\* and VER-\* statement across the 45 Root contracts is expressed only in prose; no machine-readable field carries it.

**EvidenceRefs.** Frontmatter key union across all 45 is exactly six keys — `schema`, `deliverable_id`, `package_id`, `decomposition_basis`, `project_scope_refs`, `package_objective_refs` (each 45×). Sweep for a status-bearing key (`claim_status|status|lifecycle|ac_status`) → **0 files**. Prose carrier, `DEL-02-02/ScopeOfWork.md`: "**Claim status.** Every `OUT-*`, `CLM-*`, `REQ-*`, `AC-*`, `VER-*`, and `AX-*` definition below is a *candidate* authored under `MODE=INIT`…"

**Consequence.** No deterministic check can answer "are any AC/VER statements still candidate?" across the loop. Also means the SOW method era (v1–v6.1) is unrecorded per contract — which is what would otherwise let a reader resolve the version-skew condition per file.

**SmallestAction / Owner.** Add one frontmatter field (e.g. `claim_status: CANDIDATE`) to the SOW schema. Owner: Root, `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` + `skills/scope-of-work/` (M2), applied to Root and PEC contracts on next touch.

---

**B-017 · ROOT · Class: observation · Severity: WARN · Confidence: HIGH**

**Assertion.** `domains/chirality`'s source manifest pins one agent contract as ACTIVE that does not exist — but only one, not the six the manifest describes.

**EvidenceRefs.** Recompute over the 225-row manifest: 6 MISSING paths, with states:

| Path | ArchiveState | IncludeInIndex |
|---|---|---|
| `agents/AGENT_CONTEXT_TRANSPOSE.md` | RETIRED | NO |
| `agents/AGENT_DECOMP_BASE.md` | RETIRED | NO |
| **`agents/AGENT_ORCHESTRATOR.md`** | **ACTIVE** | **YES** |
| `agents/AGENT_SCHEDULING.md` | RETIRED | NO |
| `agents/AGENT_SKILLMAKER.md` | RETIRED | NO |
| `agents/AGENT_TOOLMAKER.md` | RETIRED | NO |

`AGENT_ORCHESTRATOR` appears nowhere in the `AGENTS.md` index at the freeze.

**Consequence.** Five are correctly-recorded retirements (the row survives as history, which is intended). Exactly **one** ACTIVE pin is broken. This is *better* than the frozen-basis manifest describes ("six missing ACTIVE-pinned agent files"), and I record the correction because reviewers were directed to assess the condition as stated. The residual defect is real: an ACTIVE-pinned authority reference to a file retired by D-GOV-18 was never updated — a notice/inheritance miss inside Root's own domain pack.

**SmallestAction / Owner.** Set that row to RETIRED / IncludeInIndex NO at the next manifest refresh, citing D-GOV-18. Owner: `domains/chirality` pack maintenance.

---

**B-018 · ROOT · Class: observation · Severity: WARN · Confidence: HIGH**

**Assertion.** 93 of 225 pins (41%) in Root's own authority-reference corpus are drifted, so the corpus cannot presently serve as a drift detector for the surfaces it pins.

**EvidenceRefs.** Recompute at freeze: **126 CLEAN / 93 DRIFT / 6 MISSING** (matches the manifest exactly). Row composition: SKILL_CONTRACTS 153, AGENT_CONTRACTS 36, ROOT_GOVERNANCE_DOCS 22, ROOT_DOCS 5, WORK_SURFACE_REGISTRY 4, TOOL_REGISTRY_DOCS 3, HARNESS_EXPORT_DOCS 2.

**Consequence.** At 41% drift a *new* drift — e.g. the next Root doctrine change — is not distinguishable from the standing backlog. This is what makes B-007's notice omissions consequential rather than merely procedural: neither channel is reliable.

**SmallestAction / Owner.** A single re-pin refresh of ACTIVE rows, recorded as a maintenance act. Owner: `domains/chirality` pack. The pack is consulted-only context; I report the effect on Root's detection architecture, not on the pack's own governance.

---

**B-019 · ROOT · Class: observation · Severity: WARN · Confidence: HIGH**

**Assertion.** The deterministic standing-plan pointer marks a completed workplan ACTIVE, and no successor has opened.

**EvidenceRefs.** `execution/_Coordination/CURRENT_WORKPLAN.md`: `Status: 'ACTIVE — ROOT DELIVERABLE INITIALIZATION'`, Target `WORKPLAN_2026-07-25_root_initialization.md`. `execution/_harness/work_graph.yaml` — all six nodes `status: pending`, header noting the initialization phase "returned them `pending` at its closing tranche (D-GOV-27) — nothing is dispatched between phases." Receipt 52 is the handoff.

**Consequence.** PRD D-7 makes the pointer a *deterministic* standing-plan surface, and OBJ-6 requires interrupted/abandoned runs be "detectable as stale or orphaned rather than silently indistinguishable from live ones." A completed-but-ACTIVE plan is the same ambiguity one level up. Bounded: the work graph independently shows `pending`, so true state is recoverable.

**SmallestAction / Owner.** Set the pointer to a terminal status citing Receipt 52, or open the successor workplan. Owner: Root loop (coordination surface; PRD D-7: "Coordination surfaces carry no authority merely because they exist").

---

**B-020 · APP · Class: trace gap · Severity: REVIEW · Confidence: HIGH**

**Assertion.** App has no requirement-ID-level traceability instrument: the accepted decomposition references zero FR/NFR identifiers, and the only ID map (PRD §16) assigns 50 of 128 FRs to more than one package and 8 to none.

**EvidenceRefs.**
- ID inventory of `projects/chirality-app-dev/docs/PRD.md`: FR-001..FR-128 (128, no gaps), NFR-001..NFR-031 (31, no gaps), KG-001..KG-034 (34, no gaps).
- Reference sweep of the decomposition: **FR-\* referenced: 0. NFR-\* referenced: 0.** KG-\*: 10. The scope ledger's `SourceRef` uses section granularity ("REF-006 Section 8.12"), not requirement IDs.
- Computed from PRD §16's "PRD Coverage" column: **8 FRs owned by no package** — FR-036, 037, 038, 039, 040 (all P0 attachment requirements), FR-103, FR-104 (P1: in-process MCP tools must pass the same permission/hook overlay), FR-105. **50 FRs owned by ≥2 packages**, including FR-021..035 and FR-116 (PKG-03 + PKG-04), FR-071..077 (PKG-03 + PKG-04 + PKG-05), FR-076 (four packages), FR-083 (three), FR-098..100 (PKG-05 + PKG-06), and **FR-122..FR-128 (PKG-01 + PKG-03)**.
- NFR: §16 assigns only NFR-028..031; **27 of 31 NFRs have no package assignment anywhere**.

**Consequence.** No deterministic way to answer "which deliverable owns FR-125?" — and FR-122..FR-128 are precisely the runtime-engine-boundary requirements at the centre of the Root/App ownership question (B-001, B-025), double-claimed by PKG-01 and PKG-03. The trace also runs the wrong way: the map lives in the PRD (source) rather than the decomposition (derived), so amending the decomposition cannot correct it. Work coverage is asserted at section granularity and I do not claim the *work* is uncovered (FR-036..040 → SOW-022/023; FR-104 → SOW-048). The gap is ownership resolution, not effort.

**SmallestAction / Owner.** Add the FR/NFR→deliverable mapping as a companion register (the mechanism DEC-011 already contemplates for invariant coverage), resolving the 50 multi-owned FRs to one primary owner each and assigning the 8 unowned. App SCOPE_CHANGE; no topology change required.

---

**B-021 · APP · Class: trace gap · Severity: REVIEW · Confidence: HIGH**

**Assertion.** The accepted App decomposition pins its primary scope source at a SHA that is not the current PRD, and the divergence spans the amendments most relevant to this review.

**EvidenceRefs.** Decomposition §2 REF-006: `docs/PRD.md` SHA-256 `d9bcdcb701de08942242425a085e39dad3cba07396cbcf64970a1c4433541485`. Live PRD at freeze: `ef638f43ccae…`. The decomposition is dated 2026-05-20; the PRD has since absorbed D-APP-72, D-APP-73/SCA-APP-003 (the §17 shared-runtime amendment) and D-APP-74/SCA-APP-004. The decomposition acknowledges these only in DEC-019/DEC-020 and the Change Log, without re-pinning REF-006.

**Consequence.** The decomposition's declared basis does not include the amendment that reassigns runtime ownership — a direct contributor to B-001: §13's ownership note was written against a PRD state predating §17. Any conformance check at the pinned SHA will not see the amendment.

**SmallestAction / Owner.** Re-pin REF-006 to the current PRD SHA in the next App SCA, recording which amendments are thereby admitted.

---

**B-022 · APP · Class: trace gap · Severity: REVIEW · Confidence: HIGH**

**Assertion.** The shared-runtime client migration — accepted work under D-APP-73/SCA-APP-003 — has no scope item and no deliverable in the accepted decomposition; it is carried only by one open issue and by prose in 16 deliverables' `_STATUS.md` "Remaining" sections.

**EvidenceRefs.**
- SSOW: 78 scope items, none stating the daemon/Unix-socket client migration (SOW-037/038 predate it and state the App-owned `AgentEnginePort`/`TurnEngine`).
- The only decomposition carrier is OI-007 (`SHARED_RUNTIME`, §11), whose "Required Resolution" is a sequencing instruction, not a scope assignment.
- §13 line 611 asserts topology preservation.
- Sweep of the 53 `## Remaining` blocks for daemon/Unix-socket/runtime-client terms: **16 of 53** — DEL-01-01, DEL-01-02, DEL-02-01, DEL-02-05, DEL-03-01, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-01, DEL-05-01, DEL-05-02, DEL-05-04, DEL-06-03, DEL-08-05, DEL-09-04, DEL-09-06.
- Example, `DEL-03-03/_STATUS.md`: "Add the versioned authenticated Unix-socket API and convert `/api/harness/*` into thin daemon proxies while preserving renderer routes, SSE names, and replay semantics (gated: daemon/client implementation)."

**Consequence.** The App loop's declared convention puts open work in `Remaining`, so this is not rule-breaking. But a cross-product architectural migration spanning 16 deliverables is visible only by reading 53 status files; it is not in the scope ledger, has no coverage telemetry, and no instrument states its completion criteria. This is the mechanism by which B-001's ownership contradiction stayed invisible.

**SmallestAction / Owner.** Add the migration as explicit scope items/deliverable mappings in the next App SCA (topology preserved by mapping to existing deliverables), so completion is checkable in one place. Sequence after B-001 is ruled.

---

**B-023 · APP · Class: omission · Severity: WARN · Confidence: HIGH**

**Assertion.** The required-or-deferred CONTRACT invariant coverage register is neither present nor explicitly deferred, and the decomposition's own acceptance checklist conditions REVIEW closure on it.

**EvidenceRefs.** Decomposition §2.2: "`contract_invariant_coverage_register.csv` — Planned authoritative companion register… **It must be created or explicitly deferred before REVIEW closure.**" §10B checklist row "CONTRACT invariant coverage". DEC-011, DEC-015 restate the obligation. Directory listing of `execution/_Decomposition/` at the freeze: **one file only**. No register; no deferral ruling found in the D-APP register.

**Consequence.** The self-declared closure precondition is unmet and undispositioned.

**SmallestAction / Owner.** Create the register or record an explicit deferral ruling. Owner: App loop, D-APP decision.

---

**B-024 · APP · Class: observation · Severity: WARN · Confidence: HIGH**

**Assertion.** The App decomposition has no companion registers of any kind, so none of its scope, deliverable, coverage, or context-budget assertions is machine-checkable.

**EvidenceRefs.** `ls projects/chirality-app-dev/execution/_Decomposition/` → a single `.md` file. Compare Root (6 companion registers) and PEC (4: `Deliverables.csv`, `ScopeLedger.csv`, `Companion_Inventory.csv`, `ContextBudgetQA.csv`). All of App's SSOW, deliverables, scope ledger and checklist live as markdown tables inside the working surface.

**Consequence.** Every count and coverage claim is verifiable only by hand. This is the enabling condition for B-020, B-023, and the general asymmetry in evidence quality between App and the other two products. It also means the App loop cannot run the deterministic register validation Root and PEC have.

**SmallestAction / Owner.** No immediate act beyond B-023; recorded as the structural reason several App findings exist. Acting on B-020 and B-023 together, one companion-register introduction addresses both.

---

**B-025 · APP · Class: semantic conflict · Severity: REVIEW · Confidence: HIGH**

**Assertion.** The App PRD contains two section 17s and asserts App ownership of the runtime contract in requirements the later §17 amendment contradicts, with no supersession recorded.

**EvidenceRefs.**
- Two headings numbered §17: line 1676 "Approval and Change Control"; line 1692 "Shared Runtime and Local-Agent Pilot Amendment".
- Unsuperseded App-ownership assertions: Principle 8 (§5): "Chirality owns the runtime contract exposed to the app and to project governance"; Goal 10 (§3.1); **FR-122 (§8.16, P0)**: "Chirality shall define an `AgentEnginePort` / `RuntimeEngineContract` separate from provider/SDK APIs"; FR-124, FR-126, FR-128 similarly.
- Second §17: "make the provider-neutral runtime a **root-owned product subsystem rather than a frontend-owned singleton**."
- The amendment names no superseded requirement IDs; §16 still routes FR-122..128 to PKG-01/PKG-03 (B-020).

**Consequence.** "Chirality" does double duty — the App product in FR-122/Principle 8, the program in §17 — and the two readings assign the same contract to different owners. With B-001 this makes App's ownership posture indeterminate in its PRD, its decomposition, and the Root instruments simultaneously. Duplicate §17 numbering additionally makes a citation to "PRD §17" ambiguous.

**SmallestAction / Owner.** In the next App PRD amendment: renumber the second §17 to §18, and add one sentence naming which FR/Goal/Principle statements it reinterprets and how (App owns the *client-facing* contract; Root owns the shared runtime contract). Governed PRD change per its own §17 change-control clause.

---

**B-026 · APP · Class: observation · Severity: WARN · Confidence: HIGH**

**Assertion.** The App project agent-index overlay operates as an active governance surface while declaring itself draft.

**EvidenceRefs.** `projects/chirality-app-dev/AGENTS.md` frontmatter: `doc_id: APP-AGENTS`, `doc_kind: governance.agent_index`, **`status: draft`**, `created: 2026-06-15`.

**Consequence.** A surface typed as governance authority carries a status denying it. Under PRD N-4 / K-CONFLICT-1 this should be surfaced rather than left implicit. Bounded — no observed reliance failure.

**SmallestAction / Owner.** Promote the status or record why draft is correct for an operating overlay.

---

**B-027 · APP · Class: observation · Severity: INFO · Confidence: HIGH**

**Assertion.** Materialized deliverable folder names diverge from the accepted decomposition's names after SCA-APP-004.

**EvidenceRefs.** Decomposition §8 PKG-02: DEL-02-01 "Woven Dialogue Shell and Compatibility Navigation". Filesystem: `…/DEL-02-01_Desktop_Shell_and_Matrix_Navigation/`.

**Consequence.** Navigational only — the stable ID governs (I5/K-ID-1), and renaming folders would break paths and pins for no benefit. Recorded so it is not mistaken for a topology change.

**SmallestAction / Owner.** None recommended. Optionally note the intentional divergence in the Downstream Execution Notes.

---

### 5.4 PEC findings

---

**B-028 · PEC · Class: observation · Severity: WARN · Confidence: HIGH**

**Assertion.** PEC's 11 objective-unmapped IN scope items and 9 objective-unmapped deliverables cluster almost entirely on the shared-runtime and stream-ingest seam — the surface where PEC's boundary with Root is least settled.

**EvidenceRefs.**
- Recomputed from `Deliverables.csv`: 9 of 64 deliverables have empty `SupportsObjectives` — DEL-00-02 (Event-contract schema v1), DEL-03-05, DEL-05-01, **DEL-07-02 (Daemon SSE subscriber bridge), DEL-07-03 (Hooks CLI bridge), DEL-07-04 (cmux socket adapter), DEL-07-05 (Shared-runtime client seam v2)**, DEL-08-05, DEL-10-08. PKG-07 is 4/5 unmapped.
- Recomputed from `ScopeLedger.csv`: 11 IN rows — SOW-022, 023, **033–038** (the entire PEC-STR ingest/bridge family), 044, 063, **087** ("Reimplement the shared-runtime client seam concept against v2 entities").
- **PEC disclosed this itself**: `SOFTWARE_DECOMP.md` §7 telemetry row "IN items without objective mapping | 11 (SCA-002 O-A residue… the ingest/bridge class SOW-033..038; SOW-063, intentional per DL-14; and out-of-wave SOW-022, SOW-023, SOW-044, SOW-087)"; DL-17 records the wave-scope rationale and that the residue was deliberately left rather than force-mapped.
- `UnmappedObjectives` = 0 (the reverse direction is complete).

**Consequence.** I credit the transparency: this is disclosed telemetry with a recorded rationale, not a hidden gap, and the owner explicitly declined a SOW-local convention in favour of fixing mapping at its source. The finding is about *where* the residue sits. Deliverables with no objective backing are the ones implementing PEC's coupling to the Root runtime — and also the ones PEC's own §16 item 9 says have an undecided contract home (B-029). A deliverable with no objective has no success criterion; here that coincides with the seam whose counterpart already shipped in Root.

**SmallestAction / Owner.** Complete the objective mapping for the 11 residual rows at the next scope-of-work wave (the SCA-002 mechanism), prioritising SOW-033..038 and SOW-087. PEC loop under D-PEC; no new instrument required.

---

**B-029 · PEC · Class: ownership gap · Severity: REVIEW · Confidence: HIGH**

**Assertion.** PEC's event-contract home is an open owner decision, while the Root-side artifact it would either adopt or mirror already exists and is in use.

**EvidenceRefs.**
- PRD §16 item 9: "Event-contract home (shared `runtime/packages/contracts` vs a PEC-local schema with a pinned mirror) and API transport (Unix socket only vs an additional loopback listener, given D-GOV-20's no-TCP-control-listener posture)."
- PEC-STR-002: "their home… is a cross-loop placement decision (§16) — **writes into root `runtime/` are outside PEC's fences and require their own coordination**."
- Root side already exists: `runtime/packages/contracts/src/events.ts`, `protocol.ts`, `session.ts`, `residency.ts`, and the package's `exports` map (verified present).
- PEC's dependent deliverables — DEL-00-02, DEL-07-02, DEL-07-05 — are among the objective-unmapped set (B-028).
- D-T0-23 item 1 makes PEC a distinct registered client; B-007 shows PEC received no routed notice of D-GOV-20 or any later Root doctrine change.

**Consequence.** PEC has correctly declined to write into Root's fences and correctly held the decision open — but the counterpart artifact has been built and adopted by another client (App) meanwhile, and no coordination reached PEC. The risk is the decision being effectively foreclosed by facts on the ground rather than ruled.

**SmallestAction / Owner.** Owner decision on §16 item 9, taken with knowledge of the existing `runtime/packages/contracts` shape. Criteria in §7.2. Route: D-PEC ruling with a D-T0 coordination record, since the placement crosses loops. **Preserved open design question — I do not recommend an answer.**

---

**B-030 · PEC · Class: observation · Severity: WARN · Confidence: HIGH**

**Assertion.** The PEC domain-engine profile names an adopted product version the live PRD has already superseded.

**EvidenceRefs.** `_DomainEngines/profiles/pec.yaml` header: "the adopted product is **PRD v2.0** (coordination plane) at `projects/pec/docs/PRD.md`"; `profile_version: "0.2"`. Live PRD: **Version 2.1**, "directed-bootstrap clarification adopted as v2.1 by `D-PEC-61`".

**Consequence.** Minor and disclosed; recorded with the added precision that the profile names v2.0 specifically, so the gap is one adopted amendment (D-PEC-61) rather than unbounded staleness. The profile is not relied on for v2 behaviour (the bound application is the frozen v0.4 corpus), which bounds consequence.

**SmallestAction / Owner.** Update the version reference at the next profile amendment. Owner: Tier-0 under D-T0-12's profile lifecycle.

---

**B-031 · PEC · Class: observation · Severity: INFO · Confidence: HIGH**

**Assertion.** PEC's optionality claim is not contradicted by any dependency I could find in the frozen basis.

**EvidenceRefs.** PEC-K-01 + PEC-SVC-004 + §11 falsification clause. Cross-checks: no Root scope item, deliverable, SOW, or guard references PEC as a precondition (grep over the scope ledger and `_harness/*.yaml`); Root PRD §9.2 holds the PEC-mediated attribution path "expressly not current scope"; App's 78 scope items contain no PEC dependency; D-T0-23 §Failure boundary specifies fail-closed with "no agent fallback starts the retired independent loop."

**Consequence.** The charter's test "Can governed work remain intelligible and recoverable without PEC?" is satisfied on the frozen basis. Recorded as positive conformance so the fan-in has an evidenced answer rather than an absence of findings.

**SmallestAction / Owner.** None.

---

### 5.5 Positive conformance findings

---

**B-032 · ROOT · Class: observation · Severity: INFO · Confidence: HIGH**

Root's F4 bidirectional traceability closes under independent recomputation: forward register 84 rows (83 COVERED + 1 COVERED_WITH_RECORDED_DEFERRAL, 0 UNCOVERED); reverse register 51 rows (51 TRACED, 0 UNTRACED); scope ledger 103 rows with 0 unassigned and 0 IN items lacking a deliverable mapping. The OBJ-2 deferral is recorded in the register schema (`CoverageStatus`/`DeferralReason`), not only in prose — the distinction F4 is designed to draw. I could not falsify any of these figures.

---

**B-033 · CROSS_PRODUCT · Class: observation · Severity: INFO · Confidence: HIGH**

The shared SOW method layer is functioning across both loops that use it. Tool basis: `tools/scope_of_work/validate_scope_of_work.py` at freeze `da31c19b5` — **Root 45/45 PASS, PEC 32/32 PASS**. The disclosed version-skew condition does not manifest as a current-tool failure, so I raise no tool-drift finding and do not treat Root's historical pre-v6 validation as impeached.

---

**B-034 · CROSS_PRODUCT · Class: observation · Severity: INFO · Confidence: HIGH**

The human-judgment hinge and the domain-truth boundary both hold. Every machine gate inspected disclaims authority in its own text (`root_guards.yaml`: "Registration records that a guard is wired and observed passing; it holds no authority and confers none (K-AUTH-1)"; PEC-GAT-002/004: advisory, no write path records adoption or ruling). No validator, runtime state, coordination projection, or UI control was found substituting for an acceptance, reliance, or release judgment. K-DOMAIN-1's engine-owned-truth exemption is intact in all three products. The single anomaly is B-004, which is false *assurance*, not captured *authority*.

---

## 6. Disclosed-conditions assessment

### 6.1 Basis-wide conditions (manifest §5, all 20)

| # | Condition | Verdict | Consequence assessment |
|---|---|---|---|
| 1 | D-GOV-27 EffectiveSHA unbound | **Worse than described** | Not merely a backfill debt: it is the binding SHA for the instruction-surface supersession, DEC-021, ResponsibleParty assignment and 45 lifecycle transitions, and it **blocks** correction of condition 13's SOW pins. B-012, B-013. Compounding, not isolated. |
| 2 | Decomposition SHA-role language conflicts | **As described** | Concretely: `ea0ad7a56…` is `CandidateMergeSHA` in D-GOV-25 and `EffectiveSHA` in the decomposition header. Violates PRD **E-3** on its own primary artifact. B-011. One-label correction. |
| 3 | Accepted amendments without one supplied verifying diff | **Better than described** | I reconstructed the diff from `git show 653fabc9b…` vs freeze: confined to 4 `SupportsObjectives` additions and 45 `ResponsibleParty` assignments, exactly as DEC-021 states. Nothing undisclosed. Missing artifact is convenience, not integrity. |
| 4 | Handoff is Receipt 52, not a HANDOFF_STATE file | **Immaterial** | `AGENTS.md`'s handoff-state rule requires an explicit handoff state naming snapshots, closure verdict, rerun requirements and blockers — not a filename. Receipt 52 discharges it. |
| 5 | Current workplan complete but ACTIVE | **As described** | Bounded: `work_graph.yaml` independently shows all six nodes `pending`. Interacts mildly with OBJ-6's staleness-detectability condition. B-019. |
| 6 | AC/VER candidate status not deterministically represented | **As described** | Confirmed: 6 frontmatter keys across 45/45, 0 status-bearing. Also blocks per-file resolution of condition 15. B-016. |
| 7 | App PRD identity depends on corpus v17 | **Better than described** | v17 pins verified **8/8 CLEAN**. The mechanism works for what it covers. The real defect is what it does *not* cover (B-006). |
| 8 | App decomposition acceptance provenance weaker | **As described** | "Gates 1-7 accepted by implicit human approval" (DEC-002) with no separate ruling file, against Root's exact-candidate-SHA ruling and PEC's D-PEC-60 gate confirmations. Consequence: App has no SHA-bound acceptance to re-verify against — which is why B-021's stale REF-006 pin has no corrective trigger. |
| 9 | App lacks the invariant-coverage register | **Worse than described** | Not one missing register: App has **no companion registers at all** (B-024). The named register is the visible instance of a general absence of machine-checkable decomposition truth. |
| 10 | D-APP-48 mirror entirely stale | **Worse than described** | Confirmed 12/12 — but the significant finding is that the ruled validator **passes** on it and structurally cannot detect it (B-004), that the staleness propagates to Piping (B-005), and that it orphans the governed contract identity (B-003). |
| 11 | App domain source manifest heavily drifted | **As described** | Recomputed 119/129/219. Consulted-only surface; effect on App's own governance indirect. |
| 12 | Root Chirality manifest drift + six missing ACTIVE pins | **Better than described (with a correction)** | Drift confirmed exactly (126/93/6). But **only one** missing row is ACTIVE/IncludeInIndex=YES (`AGENT_ORCHESTRATOR.md`); the other five are RETIRED/NO. The manifest's "six missing ACTIVE-pinned agent files" overstates it. B-017, B-018. |
| 13 | Root-doctrine notices inconsistently routed | **Worse than described** | Measured: notices for only 4 of 8 recent D-GOV records; **D-GOV-20, 22, 25, 27 shipped none**; PEC 0/4 and Piping 0/4 as recipients. And the stated deterministic backstop does not exist at App for Root docs (B-006). Both channels of a two-channel architecture impaired simultaneously. |
| 14 | PEC's 32 absent P2–P4 SOWs are deliberate | **As described** | Verified 32 INITIALIZED + 32 OPEN across 64 `_STATUS.md`. Not a coverage gap; F-PEC-1 gates each build tranche. |
| 15 | Root and PEC different SOW validation eras | **Immaterial (at the freeze)** | Current-tool rerun: Root 45/45 PASS, PEC 32/32 PASS. Note the era is unrecorded per contract (B-016), so this could not have been resolved by inspection. |
| 16 | Domain packs consulted-only but carry drift evidence | **As described** | Used exactly this way: supplied B-017, B-018 and corroborated B-006/B-007. No pack treated as a reviewed product. |
| 17 | Piping is a consulted-only situated exemplar | **As described** | Piping supplied the sharpest inheritance evidence in the review (B-005). Not reviewed as a product. |
| 18 | App semantic-parity change not an accepted instrument | **As described** | No repository instrument establishes it; treated as not-basis throughout. Appears nowhere in my findings as scope. |
| 19 | Resource governance is candidate architecture | **As described** | Treated strictly per brief §5: absence never counted as a gap. Appears only as an owner-decision item. |
| 20 | The charter is guidance to challenge, not evidence | **As described** | Cited only to identify questions and classify assertion status. **No finding rests on the charter as evidence.** Divergences reported at §6.3. |

### 6.2 Per-product condition lists

**Root (10):** #1 → worse, B-012. #2 → as described, B-011. #3 → better, reconstructed. #4 (OI-011 stale) → **worse**: §9 and §14 prose also contradict the register (B-014). #5 → immaterial. #6 → as described, B-019. #7 → as described, confirmed with a zero count, B-015. #8 → as described, B-016. #9 (AGENT_TASK absolute-path fields, `validate_id_format.sh`, SOW validator prefix set, `tools/REGISTRY.md`) → **UNKNOWN**: not reached within my sweep budget; I make no claim and flag it in §7.1. #10 → as described; the pointer mechanism is sound but depends on D-GOV-27, whose EffectiveSHA is unbound (#1).

**App (12):** #1 → as described. #2 → **worse**: the duplicate §17 hosts an unreconciled ownership reversal (B-025). #3 → as described. #4 → worse, B-023/B-024. #5 → worse, B-003/B-004. #6 (D-APP-49 mirror obligations may not describe the rehomed architecture) → **as described, and confirmed**: the harness-contract files are now deprecation shims re-exporting `@chirality/runtime-contracts`, so D-APP-49's described package home no longer holds. #7 → as described; treated as not-basis. #8 (51 vs 53) → **immaterial**: verified 53 = 51 + 2 PKG-00 control, exactly as explained. #9 → as described. #10 → **worse**: the notice misidentifies the detection *architecture*, not just a target (B-006). #11 → as described, B-026. #12 → as described; navigational, bounded.

**PEC (5):** #1 → as described, with the precision that the profile names v2.0 while the PRD is v2.1 (B-030). #2 → as described and verified. #3 (three recorded REVIEW residuals) → **assessed in context, not re-discovered**: all three are claim-internal consistency issues inside initialized contracts, none touches a cross-product boundary, D-PEC-66 records dispositions; consequence bounded to those three contracts' review closure. #4 → respected; I present none as new. #5 → **as described and verified**: my recompute of the live local registers returns 254 rows / 135 ANCHOR / 119 EXECUTION, confirming the live state governs and the exhibit is frozen provenance only.

### 6.3 Where the charter's expectation and the governed record diverge

- The charter's callout "**Root runtime ownership is not optional… The Root decomposition must assign its contract and continuing conformance work to a Root package and deliverables**" states as a requirement something the accepted basis does not contain. The governed record controls: the Root PRD carries the runtime only as O-2(c)/O-10, and the decomposition faithfully covered exactly that. I therefore report B-002 as a **PRD-level gap routed as an owner decision**, not a decomposition conformance failure — the charter's framing would have produced the wrong owner and the wrong instrument.
- The charter's ownership table places "runtime-client integration" with App and protocol/daemon/clients/sessions with the shared runtime. The accepted App decomposition (§13 line 611) asserts the opposite for semantics. The record — not the charter — is what makes B-001 a finding.

---

## 7. Open questions, UNKNOWNs, and owner-decision requests

### 7.1 Declared UNKNOWNs

1. **Root condition #9's four instrument conflicts** (AGENT_TASK absolute-path fields, `validate_id_format.sh`, the SOW validator's prefix set, `tools/REGISTRY.md`). Not examined within my sweep budget; I assert nothing. My report should not be read as clearing them.
2. **App's degraded-mode behaviour when the runtime daemon is absent.** No accepted record states it. D-T0-23's failure boundary covers PEC only. Material, because App is the packaged product that supplies daemon mode (D-GOV-20 item 3).
3. **The compatibility relationship between `@chirality/runtime-contracts@0.1.0` and `flow-a.contract.v0.1.0`.** Two version identities for one artifact, no reconciling record.
4. **Whether `runtime/packages/contracts/src/harness/domain-profile.ts` is intended as the FR-107/FR-108 contract** or an unrelated transport type (B-009).
5. **Whether any Root doctrine change since D-GOV-21 has been *dispositioned* by App**, as opposed to received. Notices exist; I found no disposition records. I state receipt, not disposition.

### 7.2 Owner-decision requests (a review may expose a candidate requirement; it cannot create one)

**ODR-1 — Runtime ownership (B-001/B-002).** (a) *Semantic ownership*: confirm Root owns the shared-runtime contract per D-GOV-20/D-T0-23 and direct correction of the App decomposition's contrary note; or rule otherwise and amend D-GOV-20. (b) *Scheduling*: decide whether the Root PRD is amended to carry a runtime-contract commitment (enabling decomposition deliverables), or an explicit reasoned deferral is recorded. **Criteria:** who must be able to change the runtime contract without another loop's approval; where cross-client conformance proof lives; which loop's release judgment is gated by the runtime security review D-GOV-20 names as separately bounded with no owner.

**ODR-2 — Contract identity (B-003/B-005).** Rule under D-T0-07 whether `FLOW_A_CONTRACT_VERSION` is bumped for the Root-hosted contract (re-pinning App and Piping) or deliberately carried forward with a record of what it now binds. **Criteria:** whether downstream consumers should detect the migration by version comparison alone; cost of re-pinning two consumers versus a permanently non-discriminating version string.

**ODR-3 — Notice-architecture repair (B-006/B-007).** Decide whether (a) outstanding notices for D-GOV-20/22/25/27 are issued now as a coordination tranche, and (b) whether downstream loops are expected to pin the Root doctrine documents they inherit so the deterministic backstop actually exists. **Criteria:** whether notices are the sole channel or redundancy over pin-drift detection — the `AGENTS.md` rule says the latter; at App the former is what obtains.

**ODR-4 — PEC event-contract home (preserved open question, B-029).** PEC §16 item 9 remains open; I do not close it. **Alternatives and what each affects:** (i) *adopt shared `runtime/packages/contracts`* — removes duplication, but couples PEC's release cadence to Root's and requires a write path into Root's fences that PEC-STR-002 currently prohibits, so it needs a coordination instrument first; affects DEL-00-02, DEL-07-02, DEL-07-05. (ii) *PEC-local schema with a pinned mirror* — preserves fences and cadence, but creates exactly the mirror class B-003/B-004/B-005 show decaying undetected, so it should not be chosen without a currency check the D-APP-48 precedent lacks. (iii) *defer* — acceptable while PKG-07 is unstarted, but the counterpart exists and is in use by App, so deferral has a rising foreclosure cost. **Criteria:** which loop's release gates the event contract; whether a mirror can be given a currency check; whether PEC's fences should be amended or preserved.

**ODR-5 — Reusable work surface / application environment profile (B-010).** Held open per charter §07. **Criteria for eventually deciding:** whether a second consumer of the work surface actually appears (PEC §16 item 5 is the nearest candidate); whether any product's scope would rely on it. Until then, **absence is correctly not a gap** and no instrument should be created.

**ODR-6 — Resource governance.** Candidate architecture described only by the charter. Per brief §5 its absence is not a scope gap and I raise none. If the owner wishes to open it, §4.9 records that it currently has no owner, producer, consumer, record, compatibility obligation, or fallback — all seven would need defining before it enters product scope, which is what the charter's own status table already says.

### 7.3 Preserved open design questions (not closed by reviewer preference)

- **Physical bundling versus logical composition.** The frozen basis supplies one relevant fact and no answer: D-GOV-20 item 3 requires the packaged Electron app to supply daemon mode so credential ownership stays single-owner. That constrains but does not settle the question.
- **When PEC is available, recommended, or required by complexity.** PEC's §5 modes ladder supplies the shape ("essential for throughput (not for soundness)"); no instrument sets a threshold, and PEC-K-11 deliberately makes consumption mode-proportional rather than mandated.
- **Which cross-client conformance proofs are release requirements.** Unowned at the freeze (a consequence of B-002); noted rather than answered.

---

## 8. Reviewer's closing statement

This report is a pass-1 independent return. It rests solely on the frozen basis at `da31c19b5656dd74615e308c4215688971d33dc9`; every claim is anchored to a file, line, register row, recomputed hash, or named tool output at that commit. The charter was used only as a challenge set and is cited as evidence nowhere. I have not communicated with, sought, or seen any other reviewer's work.

Where the basis could not decide, I have said UNKNOWN rather than inferred. Where a condition was already disclosed, I have assessed its consequence rather than re-presented it as a discovery, and I have marked the three cases where my own recomputation found the disclosure inaccurate (condition 12, and per-product Root #4 and App #10). Two internal tensions between accepted records are reported as findings rather than averaged away (B-001, B-011).

**End of Report B.**
