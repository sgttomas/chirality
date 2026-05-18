# Plan: Piping Design — DOMAIN_DECOMP Audit Remediation Execution

**Workspace:** `/Users/ryan/ai-env/projects/chirality-app-test/domain-test/domains/piping-design/`
**Originating session:** Session 11 wrap-up — 2026-05-02 (ORCHESTRATOR; user-directed handoff persistence)
**Source artifacts (read-only authority for the framing below):**
- `domain-test/domains/piping-design/_Coordination/DOMAIN_DECOMP_AUDIT_2026-05-02.md` — 18 findings across 8 lanes; "Open questions for the human" §lines 209–221.
- `domain-test/domains/piping-design/_Coordination/DOMAIN_DECOMP_REMEDIATION_PLAN_2026-05-02.md` — 5 remediation waves; sequencing summary §lines 197–222; routing table §lines 34–47.
- `domain-test/domains/piping-design/_Coordination/DOMAIN_DECOMP_HANDOFF_NOTE_2026-05-02.md` — discoverability note + cross-reference with post-Session-10 state + 6 open questions table.
- `domain-test/domains/piping-design/_Coordination/DOMAIN_DECOMP_OPEN_QUESTIONS_2026-05-02.md` — reply scaffold (the durable record once rulings land); status `AWAITING_HUMAN_RULINGS`.
- `domain-test/domains/piping-design/_Coordination/_COORDINATION.md` — AOP-01/02/03 + Acyclicity Filter Spec overlay block (template for AOP-04..AOP-09 to be appended at Step 1).
- `domain-test/domains/piping-design/_Coordination/NEXT_INSTANCE_STATE.md` — Session 12 block points at this plan.

**Status:** `CLOSED_FOR_DOMAIN_DECOMP_CASCADE` as of Session 24 (2026-05-06). Q1–Q7 were ruled, SCA-002→SCA-003→SCA-008→SCA-004→SCA-005→SCA-006→SCA-007 closed, and post-cascade AGG/HG re-aggregation completed. Remaining forward content work and optional threshold ruling are tracked in `_Coordination/NEXT_INSTANCE_STATE.md`, not by this execution plan.

**Key change vs predecessor plans.** `.Archive/PIPING_DESIGN_CROSS_CUTTING_REMEDIATION_PLAN.md` (archived/completed Session 3 driver) closed Items 1–6 of the prior cross-cutting findings cycle and deferred Items 7 + 8. `.Archive/PIPING_DESIGN_ITEMS_7_8_FOLLOWUP_PLAN.md` (archived/completed Session 4 driver) prepped the Item-7 trigger watch and resolved Item 8 in-practice. **This plan was the orthogonal DOMAIN_DECOMP lane** — it consumed a parallel DOMAIN_DECOMP audit (the canonical decomposition package itself, not the deliverable-content surface) and routed its 18 findings through human rulings on Q1–Q7 followed by SCOPE_CHANGE / TOOLMAKER / SKILLMAKER / DBM_PUBLISHER fan-out.

---

## Context

State at plan authoring time (post-Session 11):

- All 42 KTYs at lifecycle `IN_PROGRESS` (T0a..T0e all promoted; Sessions 3, 5, 6, 7, 8, 9, 10).
- DOMAIN_HYPERGRAPH snapshot: `_Aggregation/Hypergraph/HG_PIPING_DESIGN_F26_CROSS_CUTTING_REMEDIATION_2026-05-02_1114/` (9/9 PASS; 16,745 nodes / 16,937 hyperedges / 108,354 incidences). Unchanged through promotion phase.
- FULL_GRAPH dependency-register snapshot: `_Aggregation/AGG_Dependency_Register_FullGraph_2026-05-02_1106/` (7/7 PASS; 0 cycles; 470 rows; 29 RECIPROCAL_MISSING preserved by design).
- Item 7 reciprocity sweep: `WATCHING` (no triggers fired). Item 8 (`_CONTEXT.md` vs SKILL default): `RESOLVED-IN-PRACTICE`. Both continue to require zero session attention unless triggered.
- DOMAIN_DECOMP advisory landed Session 11 (commit `85d7e5b6`): 18 findings (1 BLOCKER, 10 DEFECT, 4 DRIFT, 3 OPPORTUNITY); Q1–Q6 awaiting rulings.
- Open-questions reply scaffold authored Session 11 (commit `e1a59186`).

**Of the 18 audit findings:**
- F1 / `ASYMMETRIC_OBJECTIVE_MAPPING` (audit ID `AUDIT-C01`) → already codified as AOP-01 in Session 3.
- F2 / `OBJECTIVE_TRACE_ASYMMETRY` (audit ID `AUDIT-C02`) → already codified as AOP-02 in Session 3.
- All other 16 findings are net-new and unaddressed.

**User-confirmed execution preferences (locked in at plan handoff):**

1. **Bundle Step-1 transcription as one coherent commit** — Session 13 block + AOP overlay edits + plan-file Pre-req flips + scaffold update.
2. **Parallelize Step 2** by spawning subagents with bounded init-task briefs where independence allows (up to 4 parallel dispatches; see fan-out graph).
3. **Corrigendum SCA = `SCA-002_PackageMetadataCorrigendum`** (project already has SCA-001 reserved/used).
4. **Wave 2 scope = piping-design only.** No survey of West_Doe / Pipe_Specs / other DOMAIN packages before tooling lands. Other packages adopt later if they want.
5. **SKILLMAKER + TOOLMAKER dispatched directly** when Q2/Q3/Q4 rulings call for new skills/tools. No `plans/SKILL_SCOPE_*.md` pre-scoping draft.

---

## Q1 — Package layout convention

**Question (verbatim from audit §Open questions / line 211):**
> Is the package layout (`_Decomposition/<versioned-snapshot-folder>/<annexes>`) the intended convention, with `--decomposition-root` overrides expected at SCA invocation? Or is the convention `_Decomposition/<annexes>` (annexes at root), in which case the current package layout is non-standard? *(Drives reading of AUDIT-A01 BLOCKER vs OPPORTUNITY.)*

**Gates:** Wave 2 (AUDIT-A01 — `BLOCKER · INCOHERENT`).
**Evidence pointers:**
- `tools/validation/validate_domain_decomposition_integrity.py:117` (non-recursive `decomposition_root.glob(pattern)`).
- `agents/AGENT_SCOPE_CHANGE.md` §253 / §535 / §545 (`--decomposition-root {CONTEXT_ROOT}/_Decomposition`).
- Running validator at `_Decomposition/`: 6 CRITICAL `MISSING_REQUIRED_FILE`. Running at the inner `MWK1956_..._FIXED/` subfolder: 0 findings.

**Illustrative answer-shapes (paraphrased from plan routing table; NOT pre-rulings):**
- **(a)** Nested versioned snapshots are canonical → R-SPEC update on `agents/AGENT_SCOPE_CHANGE.md` to teach tools the `--decomposition-root` override pattern.
- **(b)** Annexes-at-`_Decomposition`-root is canonical → R-SCA-RECONCILE: piping-design layout migration (per user preference, scoped to piping-design only; surface separate plan if so).
- **(c)** Both forms accepted → R-TOOL: extend validators to walk both shapes (recursive descend-one-level when a single subfolder exists, OR `--package-subfolder` flag); document in SPEC.

---

## Q2 — Decision-log granularity / per-unit assignment decisions

**Question (verbatim from audit §Open questions / line 213):**
> Was the 16,510-unit partition into 10 categories accomplished without any non-trivial unit-level assignment decisions (so the empty `DecisionRef` columns and policy-only Decision_Log are vacuously correct)? Or did such decisions occur and not get logged? *(Drives reading of AUDIT-C03 INCOMPLETE vs vacuous-PASS.)*

**Gates:** Wave 3 tail (AUDIT-C03 + AUDIT-C04).
**Evidence pointers:**
- `_Decomposition/.../Domain_Ledger.csv` `DecisionRef`: 0 of 16,510 rows populated.
- `_Decomposition/.../Section_Seed_Domain_Ledger.csv`: 458/472 with `DecisionRef`; only two distinct values (DEC-001, DEC-002).
- `_Decomposition/.../Decision_Log.csv`: 16 entries — all policy decisions; none are per-unit assignment decisions.
- `_Decomposition/.../Atomic_Domain_Ledger.csv`: lacks `DecisionRef` column entirely.

**Illustrative answer-shapes:**
- **(a)** "No non-trivial unit-level decisions occurred" → R-SPEC: amend `agents/AGENT_DOMAIN_DECOMP.md` to clarify `DecisionRef` is required only for non-trivial decisions; close C03/C04 as `RESOLVED-IN-PRACTICE`.
- **(b)** "Decisions occurred and weren't logged" → R-NEW-SKILL `decision-backfill` (SKILLMAKER + TOOLMAKER) + R-SCA-RECONCILE: re-read source against partition, propose retroactive `DEC-NNN` entries, ingest as ADD/MODIFY actions on `Decision_Log.csv` and `Domain_Ledger.csv`/`Atomic_Domain_Ledger.csv`. Substantial blast radius (could touch hundreds to thousands of ledger rows).
- **(c)** "Policy-only granularity is intentional" → R-SPEC only; refine SPEC text.

---

## Q3 — `IntendedUsers` / `WhenUsed` boilerplate intent

**Question (verbatim from audit §Open questions / line 215):**
> Are uniform `IntendedUsers` and `WhenUsed` boilerplates (AUDIT-E01, E02) acceptable, or were per-KTY discriminating values intended? If the former is acceptable, then leaving the fields as `TBD` would honestly reflect that; populating them with identical strings does not.

**Gates:** Wave 4 (AUDIT-E01 + AUDIT-E02; AUDIT-E03 bundles).
**Evidence pointers:**
- `Knowledge_Type_Register.csv` `IntendedUsers`: identical across all 42 KTYs (`"Plant layout designers; piping/mechanical engineers; reviewers"`).
- Same for `WhenUsed`: identical across all 42 KTYs (`"During domain decomposition and downstream artifact generation"`).
- `Knowledge_Subject_Register.csv` `Description`: 87/88 SUBs are 50–149 chars (one-sentence stubs); 0/88 ≥150-char substantive.

**Illustrative answer-shapes:**
- **(a)** Boilerplate acceptable as-is → R-NONE.
- **(b)** Honest fallback → R-SCA-RECONCILE alone: revert all 42 `IntendedUsers` + `WhenUsed` to `TBD` (allowed per SPEC). Hours of work. E03 has no equivalent fallback (empty `Description` would fail downstream consumers worse than thin).
- **(c)** Per-KTY discrimination intended → R-NEW-SKILL `kty-metadata-discriminate` (SKILLMAKER + TOOLMAKER) + R-SCA-RECONCILE: read each KTY's Scoping.md + KAs, propose per-KTY values, human acceptance pass, MODIFY actions on the two registers. ~1 week skill design + ~1 day per 10 KTYs reviewed.

---

## Q4 — Vocabulary Map target scope

**Question (verbatim from audit §Open questions / line 217):**
> Should the Vocabulary Map (AUDIT-D01) eventually grow to cover the full source-supported vocabulary (potentially 100+ canonical terms across all 10 categories), or is it intentionally bounded to layout-execution terms?

**Gates:** Wave 4 (AUDIT-D01).
**Evidence pointers:**
- `_Decomposition/.../Vocabulary_Map.csv`: 18 entries, layout/plot-plan-centric.
- Audit spot-check: 9/50 (18%) common piping-domain terms covered; entire mechanical-integrity / flexibility / supports / dynamic-control / codes / equipment vocabularies absent.
- `KTY-01-03_Terminology-and-Vocabulary` has 103 atomic units mapped (38 from Piping_Manual + 65 from MWK_1956).

**Illustrative answer-shapes:**
- **(a)** Bounded scope (layout terms only) → R-NONE; document boundary in SPEC.
- **(b)** Full source-supported vocabulary → R-NEW-SKILL `domain-vocabulary-extract` (SKILLMAKER + TOOLMAKER) + R-SCA-RECONCILE: read sources + KTY-01-03 atomic units, propose canonical-term + synonym candidates with source-line citations, human acceptance pass, MODIFY action on `Vocabulary_Map.csv`. ~1 week skill + ~1 day per 50 candidates.
- **(c)** Intermediate scope (e.g., all category-canonical terms but not exhaustive synonyms) → R-NEW-SKILL with bounded extraction parameters.

---

## Q5 — Zero-AU surfaces semantics

**Question (verbatim from audit §Open questions / line 219):**
> Are the 7 zero-AU KTYs and 27 zero-AU SUBs (AUDIT-F02) meant to be filled by future SCAs/content workflows, or are they durable empty surfaces that downstream production fills with non-source content (extending the decomposition's content beyond its source basis)? The latter interpretation makes the "no invention" invariant softer than its text suggests.

**Gates:** Wave 5 (AUDIT-F02 — SPEC reinterpretation).
**Evidence pointers:**
- `_Decomposition/.../Coverage_Gaps_Register.csv` GAP-003 (7 KTYs) + GAP-004 (27 SUBs); both `Status=ACCEPTED_BY_GATE5`.
- `_Decomposition/.../Decision_Log.csv` DEC-013 + DEC-015 (policy resolutions for zero-AU).
- `agents/AGENT_DOMAIN_DECOMP.md` "no invention" invariant text — does not yet record the project's accepted interpretation.

**Illustrative answer-shapes:**
- **(a)** Scaffold-for-fill (future SCAs/content workflows populate from `_Sources/`) → R-SPEC: amend SPEC to formalize scaffold-for-fill semantic; "no invention" invariant intact. Plan §177 calls this overwhelmingly more practical.
- **(b)** Durable-empty (extends decomposition beyond source basis) → R-SPEC: explicitly soften the invariant; document the new boundary.
- **(c)** Per-surface decision → enumerate per-KTY/SUB in `Coverage_Gaps_Register.csv` (SCOPE_CHANGE SCA) + SPEC update.

---

## Q6 — SUB cardinality discipline

**Question (verbatim from audit §Open questions / line 221):**
> Is the uniform 2-SUB pattern (AUDIT-F01) intentional (e.g., a project convention emitted by the decomposition skill) or did the partitioning intend to vary cardinality with content density? The former is fine if explicit; the latter would suggest the SUB layer was filled mechanically.

**Gates:** Deferred (re-evaluate after Wave 4 lands and 4–6 KTYs complete content production).
**Evidence pointers:**
- 38/42 KTYs have exactly 2 SUBs; 4/42 have 3 SUBs; 0 KTYs have 1 SUB or 4+ SUBs.
- AU/SUB ratio span 270× (KTY-06-02 = 1,218; KTY-01-02 = 4.5); top-5 high-AU KTYs all carry 2 SUBs each.

**Illustrative answer-shapes:**
- **(a)** Intentional convention → R-SPEC: document; F01 closes as `RESOLVED-IN-PRACTICE`.
- **(b)** Should have varied with content density → defer R-SCA-RECONCILE (high blast: SubjectID(s) remap across thousands of rows, KTY-folder reorg, hypergraph rerun) until after Wave 4 lands and 4–6 KTYs complete content production.
- **(c)** Mixed → keep current cardinality, treat SUBs as coarse aggregation, finer partitions live inside KAs → R-SPEC clarification only.

---

## Step 1 — Transcribe rulings into governing artifacts (single bundled commit)

Execute when at least one of Q1–Q6 has been ruled in `_Coordination/DOMAIN_DECOMP_OPEN_QUESTIONS_2026-05-02.md`. ORCHESTRATOR write-scope = `_Coordination/` only (this step does not touch closed artifacts or dispatch any owner-agent).

For each ruling provided (any subset):

1. **Edit `_Coordination/DOMAIN_DECOMP_OPEN_QUESTIONS_2026-05-02.md`:**
   - Fill in the `**Ruling:** / **Date:** / **Authority:** / **Notes:**` block under each ruled question.
   - Update top `**Status:**` to `RULED <YYYY-MM-DD>` (all six) or `PARTIALLY_RULED <YYYY-MM-DD>` (subset).

2. **Append overlay block(s) to `_Coordination/_COORDINATION.md`** mirroring the existing AOP-01/AOP-02/AOP-03 + Acyclicity Filter Spec pattern from Session 3. Each ruling becomes one named overlay. Suggested IDs (final naming chosen at write time to avoid collision):
   - **AOP-04** ← Q1 (package layout convention)
   - **AOP-05** ← Q2 (decision-log granularity)
   - **AOP-06** ← Q3 (KTY metadata boilerplate intent)
   - **AOP-07** ← Q4 (vocabulary map target scope)
   - **AOP-08** ← Q5 (zero-AU surfaces semantics)
   - **AOP-09** ← Q6 (SUB cardinality discipline)

   Each overlay block carries (verbatim shape from AOP-01 §66–§75):
   - `### AOP-NN — <one-line ruling summary>`
   - `**Source of truth:** <authoritative artifact + clause>`
   - `**Subordinate side:** <derived/advisory side, if any>`
   - `**Generalizes:** <audit finding ID + KTYs affected>`
   - `**Coverage:** <quantitative scope>`
   - `**Implication for downstream agents/tools:** <how dependency-extract / aggregator / hypergraph / SCA-runner should apply this>`

3. **Edit `_Coordination/DOMAIN_DECOMP_REMEDIATION_PLAN_2026-05-02.md`:**
   - For each ruled question, flip the corresponding `**Pre-req:** human ruling on Open question #N` line to `**Pre-req:** ruled <YYYY-MM-DD> → <chosen route name>` (e.g., `R-SPEC`, `R-TOOL`, `R-NEW-SKILL → R-SCA-RECONCILE`).

4. **Append a Session 13 block to `_Coordination/NEXT_INSTANCE_STATE.md`** per §7 update protocol. Use the Session 11 / Session 12 blocks as structural template. Required content:
   - Driver line (which question(s) were ruled, by whom, on what date).
   - "What advanced": list of overlay IDs added; list of waves now dispatchable; list of waves still gated (and on which open question).
   - Refreshed §5 immediate next actions: which dispatch fan-out is authorized; remaining Session-10 carryovers (forward content, threshold change).
   - Lifecycle / hypergraph / dependency-register state (unchanged unless Step 2's downstream verifications fire).
   - Item 7 / Item 8 status confirmation.

**Single coherent commit** wraps Steps 1.1–1.4. Suggested message: `piping-design: Session 13 — DOMAIN_DECOMP rulings ⟨Q-list⟩ codified (AOP-NN..); waves ⟨W-list⟩ dispatchable`.

---

## Step 2 — Parallelized dispatch fan-out (post-Step 1)

Each dispatch is a separate subagent invocation with a bounded init-task brief. Dispatches with no inter-dependency run **in parallel** — send them in a single message with multiple Agent tool calls.

### Parallelization graph

```
                 Step 1 (single bundled commit)
                              │
       ┌──────────────┬───────┼─────────────────────────────┐
       ▼              ▼       ▼                             ▼
  SCA-002         Wave 2    Wave 3 tail                Wave 4 (Q3 + Q4)
  SCOPE_CHANGE    A01+B01   (depends on Q2)            D01 + E01/E02/E03
   (Q-indep.)     TOOLMAKER    Q2=(a)/(c) → R-SPEC       Q3=(c) → SKILLMAKER
                  + DBM_PUB    Q2=(b)     → SKILLMAKER   Q3=(b) → SCOPE_CHANGE alone
                  (R-TOOL +                              Q4=(b)/(c) → SKILLMAKER
                   R-SPEC)                               Q4=(a) → R-NONE
                              │
                              ▼
                         Wave 2 B02
                         (R-TOOL on validation generator;
                          gated by A02 corrigendum landing)
                              │
                              ▼
                         Wave 5 (Q5)
                         DBM_PUBLISHER / SKILLMAKER
                         (R-SPEC text edit; can run
                          alongside any other wave)
```

**Up to 4 dispatches in parallel post-Step-1**: SCA-002 corrigendum, Wave 2 head (A01+B01), Wave 3 tail (text-only or new-skill scoping), Wave 4 (one or two skill scopings). Wave 2 B02 sequences after SCA-002 corrigendum lands. Wave 5 R-SPEC text edit can land any time once Q5 is ruled.

### Step 2A — Wave 1 corrigendum (SCA-002, Q-INDEPENDENT)

- **Trigger:** part of the post-Step-1 fan-out. No ruling required (Wave 1 is Q-independent).
- **Owner agent:** SCOPE_CHANGE.
- **Init-task brief contents:**
  - **Goal:** Author `_ScopeChange/SCA-002_PackageMetadataCorrigendum/` containing four MODIFY actions:
    - **AUDIT-A02 — Companion_Inventory.csv missing 41 entries:** ADD all 41 missing files in the snapshot folder, classified by `PackageRole` and `Description` per the agent's inventory completeness criterion (every `*.csv` / `*.json` / `*.md` file gets a row).
    - **AUDIT-A03 — `_Decomposition/_LATEST.md` says `Latest: (none)`:** UPDATE pointer to `MWK1956_PipingManual_DOMAIN_DECOMP_FINAL_ACCEPTED_v1_0_FIXED`. Alternative if pointer convention is unused at this surface: delete the file. Pre-clarify with human if uncertain.
    - **AUDIT-G01 — `DEC-016` Status stale:** UPDATE `Decision_Log.csv` row `DEC-016` Status from `DRAFT_FOR_GATE6_CONFIRMATION` to `ACCEPTED_GATE6_COVERAGE_VERIFIED` (or equivalent matching `HANDOFF_STATE.md` closed-gate state).
    - **AUDIT-G02 — `DEC-003` `ImpactedIDs` wildcard:** UPDATE `Decision_Log.csv` row `DEC-003` `ImpactedIDs` from `CAT-003;KTY-03-*` to explicit list (`KTY-03-01_...; KTY-03-02_...; KTY-03-03_...; KTY-03-04_...; KTY-03-05_...` with full slugs).
  - **Authority overlays to apply silently (do NOT re-flag):** AOP-01, AOP-02, AOP-03, Acyclicity Filter Spec; plus any AOP-04..AOP-09 codified in Step 1.
  - **Write-scope:** `_ScopeChange/SCA-002_PackageMetadataCorrigendum/` (per agent boundary). The actual annex file MODIFY actions land via SCOPE_CHANGE Gates 4–5 acceptance flow.
  - **Gates:** SCOPE_CHANGE Gates 1–5 per `agents/AGENT_SCOPE_CHANGE.md`.
  - **Effort:** 1–2 hours authoring + Gates.
- **Verification on landing:** `Companion_Inventory.csv` row count = 71 (was 30); `_Decomposition/_LATEST.md` resolves; `DEC-016` Status updated; `DEC-003` `ImpactedIDs` enumerated; validator at inner folder still 0 findings.

### Step 2B — Wave 2 head: A01 + B01 (gated by Q1)

- **Trigger:** Q1 has been ruled.
- **Owner agents:** TOOLMAKER (R-TOOL) + DBM_PUBLISHER or SKILLMAKER (R-SPEC).
- **Init-task brief contents (TOOLMAKER):**
  - **Goal — AUDIT-A01:** Update `tools/validation/validate_domain_decomposition_integrity.py` and `tools/reporting/synthesize_domain_coverage_json.py` to support whichever layout convention Q1 ruled canonical:
    - If **Q1 = (a) nested-snapshots**: tools should accept `--decomposition-root` pointing at the inner snapshot folder; SPEC documents this as the standard call.
    - If **Q1 = (c) both-forms**: tools recursively descend one level when a single subfolder exists, OR add `--package-subfolder` flag. Tests cover both shapes.
    - If **Q1 = (b) annexes-at-root**: tools unchanged; surface a separate plan for piping-design layout migration (per user preference, scoped to piping-design only).
  - **Goal — AUDIT-B01:** Modify `synthesize_domain_coverage_json.py` to (1) prefer `Coverage_Telemetry.json` (Phase 7 final) when present in the package, fall back to `Atomic_Coverage_Telemetry.json` only when absent; (2) stop stringifying numeric fields (preserve int-typed values); (3) document the source-of-truth precedence in `--help`.
  - **Tests:** existing `test_validate_domain_decomposition_integrity.py` + `test_synthesize_domain_coverage_json.py` cover regression. Add cases for the new behavior.
  - **Write-scope:** `tools/validation/`, `tools/reporting/`, plus the matching `tests/` paths.
- **Init-task brief contents (DBM_PUBLISHER / SKILLMAKER):**
  - **Goal — R-SPEC:** Update `agents/AGENT_SCOPE_CHANGE.md` §253 / §535 / §545 invocations to either (i) point at the inner accepted snapshot folder, (ii) document that the resolver auto-descends, or (iii) document the `--package-subfolder` flag — whichever Q1's ruling implies.
  - **Write-scope:** `agents/AGENT_SCOPE_CHANGE.md` only.
- **Effort:** 8–16 hours combined (TOOLMAKER) + hours (DBM_PUBLISHER).
- **Verification on landing:** `validate_domain_decomposition_integrity.py` against `_Decomposition/` (top level) returns 0 findings (or documented flag is required); `python -m pytest tools/...` passes; `synthesize_domain_coverage_json.py` output matches `Coverage_Telemetry.json` schema parity (FINAL-ACCEPTED-v1.0 revision; integer-typed numerics).

### Step 2C — Wave 2 tail: B02 (gated by SCA-002 landing)

- **Trigger:** SCA-002 corrigendum has landed (A02 fix complete) AND Q1 has been ruled.
- **Owner agent:** TOOLMAKER on the Phase-6/7 validation generator (the script that emits `Validation_Checks.csv`).
- **Init-task brief contents:**
  - **Goal — AUDIT-B02:** Extend VAL-018 from "Companion_Inventory present" to "Companion_Inventory enumerates every file in the package folder, classified by role." Same shape for VAL-017 (extend to schema parity check post-AUDIT-B01 fix).
  - **Constraint:** changes regression baselines; rerun must continue to PASS post-SCA-002 corrigendum.
  - **Write-scope:** the validation generator script + its tests; downstream regenerated `Validation_Checks.csv` lands as part of a future SCA, not directly here.
- **Effort:** 2–4 hours.

### Step 2D — Wave 3 head: C01 + C02 (verify-only)

- **Trigger:** part of Step-1 housekeeping (no separate dispatch needed).
- **Action:** ORCHESTRATOR reads `_Coordination/_COORDINATION.md` and confirms AOP-01 + AOP-02 are still present and current (Session 3 codification). If still current, mark C01 + C02 as `RESOLVED-IN-PRACTICE` in the Session 13 block. No edits.

### Step 2E — Wave 3 tail: C03 + C04 (gated by Q2)

- **Trigger:** Q2 has been ruled.
- **If Q2 = (a) "no decisions occurred"** OR **(c) "policy-only intentional":**
  - **Owner agent:** SKILLMAKER or DBM_PUBLISHER.
  - **Init-task brief:** Update `agents/AGENT_DOMAIN_DECOMP.md` SPEC text to clarify that `DecisionRef` is required only for non-trivial decisions; absence is acceptable when partitioning is unambiguous. Document the policy-only Decision_Log granularity. Close C03/C04 as `RESOLVED-IN-PRACTICE`.
  - **Write-scope:** `agents/AGENT_DOMAIN_DECOMP.md`.
  - **Effort:** hours.
- **If Q2 = (b) "decisions occurred and weren't logged":**
  - **Owner agents (sequential):** SKILLMAKER (skill design) → SCOPE_CHANGE (SCA ingestion).
  - **Init-task brief (SKILLMAKER):** Scope a `decision-backfill` skill that re-reads `_Sources/MWK_1956/MWK_1956.md` and `_Sources/Piping_Manual/Piping_Manual.md` against the `Domain_Ledger.csv` partition, surfaces non-trivial unit-level assignment decisions, and proposes retroactive `DEC-NNN` entries for human acceptance. Skill must enforce "no invention" — every proposed DEC must trace to source citations.
  - **Init-task brief (SCOPE_CHANGE):** Ingest accepted DEC entries as ADD actions on `Decision_Log.csv` plus MODIFY actions populating `DecisionRef` columns in `Domain_Ledger.csv` and (optionally, per C04 ruling) `Atomic_Domain_Ledger.csv` (which would also need a column-add MODIFY action).
  - **Blast radius:** could touch hundreds to thousands of ledger rows. Surface for separate human authorization on whether to commit before SCA dispatch.
  - **Effort:** ~1 week skill design + acceptance pass + SCA Gates 1–5.

### Step 2F — Wave 4: D01 + E01/E02/E03 (gated by Q3 + Q4)

These two sub-waves are independent and run in parallel via separate dispatches.

#### Sub-wave 2F.1 — Vocabulary Map (D01, gated by Q4)

- **If Q4 = (a) bounded scope:** R-NONE; close as `RESOLVED-IN-PRACTICE`; document boundary in SPEC if not already.
- **If Q4 = (b) full source-supported** OR **(c) intermediate:**
  - **Owner agents (sequential):** SKILLMAKER (skill design) → SCOPE_CHANGE (SCA ingestion).
  - **Init-task brief (SKILLMAKER + TOOLMAKER):** Scope `domain-vocabulary-extract` TASK skill that:
    - Reads `_Sources/MWK_1956/MWK_1956.md` and `_Sources/Piping_Manual/Piping_Manual.md`.
    - Reads the 103 atomic units mapped to `KTY-01-03_Terminology-and-Vocabulary` from `Atomic_Domain_Ledger.csv`.
    - Proposes canonical-term + synonym candidates with source-line citations.
    - Emits `Vocabulary_Map_Candidates.csv` for human acceptance (NOT a direct edit).
    - Enforces "no invention" — every candidate traces to source.
  - **Init-task brief (SCOPE_CHANGE):** SCA-N MODIFY action on `Vocabulary_Map.csv` ingesting accepted candidates.
  - **Effort:** ~1 week skill + ~1 day per 50 candidates + SCA Gates.

#### Sub-wave 2F.2 — KTY/SUB metadata enrichment (E01/E02/E03, gated by Q3)

- **If Q3 = (a) boilerplate acceptable:** R-NONE.
- **If Q3 = (b) honest fallback to TBD:**
  - **Owner agent:** SCOPE_CHANGE alone.
  - **Init-task brief:** SCA-N revert all 42 `Knowledge_Type_Register.csv` `IntendedUsers` + `WhenUsed` values to `TBD` (allowed per SPEC). E03 SUB Descriptions: no equivalent fallback; surface as separate action requiring authoring.
  - **Effort:** hours.
- **If Q3 = (c) per-KTY discrimination intended:**
  - **Owner agents (sequential):** SKILLMAKER (skill design) → SCOPE_CHANGE (SCA ingestion).
  - **Init-task brief (SKILLMAKER + TOOLMAKER):** Scope `kty-metadata-discriminate` TASK skill that:
    - Reads each KTY's `Scoping.md` and `KA-*.md` content (deliverable-local, already authored).
    - Reads `Knowledge_Type_Register.csv` and `Knowledge_Subject_Register.csv`.
    - Proposes per-KTY `IntendedUsers` and `WhenUsed` values; per-SUB enriched `Description`.
    - Emits proposals as candidate-CSVs for human acceptance.
  - **Init-task brief (SCOPE_CHANGE):** SCA-N MODIFY actions on the two registers.
  - **Blast radius:** registers only; no ID changes; no ledger changes.
  - **Effort:** ~1 week skill + ~1 day per 10 KTYs + SCA Gates.

### Step 2G — Wave 5: F02 SPEC text (gated by Q5)

- **Trigger:** Q5 has been ruled. Can run in parallel with any other wave (text-only).
- **Owner agent:** DBM_PUBLISHER or SKILLMAKER.
- **Init-task brief:**
  - **If Q5 = (a) scaffold-for-fill:** Edit `agents/AGENT_DOMAIN_DECOMP.md` §non-negotiable invariants to refine "no invention" to bound to atomic-unit content, explicitly permitting scaffold KTYs/SUBs that future content workflows fill from `_Sources/` evidence. Matches DEC-013/DEC-015 accepted interpretation.
  - **If Q5 = (b) durable-empty:** Edit SPEC to soften the invariant explicitly; document the new boundary.
  - **If Q5 = (c) per-surface decision:** Enumerate per-KTY/SUB in `Coverage_Gaps_Register.csv` (separate SCOPE_CHANGE SCA) + SPEC update.
  - **Write-scope:** `agents/AGENT_DOMAIN_DECOMP.md` (R-SPEC text only). Plus `Coverage_Gaps_Register.csv` SCA target if Q5 = (c).
- **Effort:** hours (text-only).
- *Plan recommends deferring Wave 5 SPEC text until Waves 1–4 outcomes have stabilized practice.*

### Step 2H — Deferred F01 (Q6 records intent only)

- **If Q6 = (a) intentional:** R-NONE; document the convention in SPEC; close F01 as `RESOLVED-IN-PRACTICE`.
- **If Q6 = (b) should vary** OR **(c) mixed:** defer R-SCA-RECONCILE until after Wave 4 lands and 4–6 KTYs complete content production. Re-evaluate then.
- **Why defer if (b)/(c):** SUB SPLIT is high-blast-radius (parent-closure on `Knowledge_Subject_Register`, `Atomic_Domain_Ledger.SubjectID(s)` remap across thousands of rows, KTY-folder reorg, hypergraph rerun, dependency-aggregation refresh). Don't pay that cost until cheaper remediations are tested for sufficiency.

---

## Step 3 — Cross-cutting verifications after dispatches land

Each dispatch is independent except for the explicit gates. After any wave's SCA / tool-fix / skill-output lands:

1. **Re-aggregate FULL_GRAPH if a register row count changes.** Wave 3 tail (Q2=b backfill) is the main risk — it touches the ledger. Refresh `_Aggregation/_Pipelines/piping-design-fullgraph-deps/_LATEST.md` via AGGREGATION agent only after a meaningful batch lands (≥5 ledger-touching changes), per the established gate.
2. **Re-run DOMAIN_HYPERGRAPH if Category/KTY/Subject/Artifact/AtomicUnit topology changes.** Topology-changing waves: Wave 3 tail R-NEW-SKILL backfill (touches ledger); Wave 4 D01 vocabulary expansion (touches `Vocabulary_Map.csv` — refresh advisable); Wave 6 (deferred F01) SUB resplit (heavy refresh required). Topology-INVARIANT waves: Wave 1 corrigendum (annex-only); Wave 2 (tooling-only); Wave 3 tail R-SPEC (text-only); Wave 4 metadata-discriminate (register columns only); Wave 5 R-SPEC (text-only).
3. **Re-validate `Validation_Checks.csv`** if VAL-015 / VAL-017 / VAL-018 were extended in Wave 2 — confirm the tightened checks still PASS post-Wave-1 corrigendum.
4. **Update `## Resolved findings` table in `_Coordination/NEXT_INSTANCE_STATE.md`** with each net-new finding ruled and remediated. New rows should follow the existing table shape (Finding / Ruling / Remediation).

---

## Critical files

| Step | File | Action | Owner |
|---|---|---|---|
| 1 | `_Coordination/DOMAIN_DECOMP_OPEN_QUESTIONS_2026-05-02.md` | Edit (fill Ruling/Date/Authority/Notes; flip Status) | ORCHESTRATOR |
| 1 | `_Coordination/_COORDINATION.md` | Append AOP-04..AOP-09 overlay block(s) | ORCHESTRATOR |
| 1 | `_Coordination/DOMAIN_DECOMP_REMEDIATION_PLAN_2026-05-02.md` | Edit Pre-req lines per ruled wave | ORCHESTRATOR |
| 1 | `_Coordination/NEXT_INSTANCE_STATE.md` | Append Session 13 block | ORCHESTRATOR |
| 2A | `_ScopeChange/SCA-002_PackageMetadataCorrigendum/` | NEW (authored by SCOPE_CHANGE) | SCOPE_CHANGE |
| 2B | `tools/validation/validate_domain_decomposition_integrity.py` | Edit | TOOLMAKER |
| 2B | `tools/reporting/synthesize_domain_coverage_json.py` | Edit | TOOLMAKER |
| 2B | `agents/AGENT_SCOPE_CHANGE.md` | Edit (R-SPEC) | DBM_PUBLISHER / SKILLMAKER |
| 2C | `tools/<validation-generator>` (Phase 6/7) | Edit | TOOLMAKER |
| 2E | `agents/AGENT_DOMAIN_DECOMP.md` | Edit (R-SPEC for Q2=a/c) | SKILLMAKER / DBM_PUBLISHER |
| 2E | `skills/decision-backfill/` | NEW (Q2=b only) | SKILLMAKER |
| 2E | `_Decomposition/.../Decision_Log.csv`, `Domain_Ledger.csv`, `Atomic_Domain_Ledger.csv` | Edit via SCA only (Q2=b) | SCOPE_CHANGE |
| 2F.1 | `skills/domain-vocabulary-extract/` | NEW (Q4=b/c only) | SKILLMAKER |
| 2F.1 | `_Decomposition/.../Vocabulary_Map.csv` | Edit via SCA only | SCOPE_CHANGE |
| 2F.2 | `skills/kty-metadata-discriminate/` | NEW (Q3=c only) | SKILLMAKER |
| 2F.2 | `_Decomposition/.../Knowledge_Type_Register.csv`, `Knowledge_Subject_Register.csv` | Edit via SCA only | SCOPE_CHANGE |
| 2G | `agents/AGENT_DOMAIN_DECOMP.md` | Edit (R-SPEC for F02) | DBM_PUBLISHER / SKILLMAKER |
| 2G | `_Decomposition/.../Coverage_Gaps_Register.csv` | Edit via SCA only (Q5=c) | SCOPE_CHANGE |
| 3 | `_Aggregation/_Pipelines/piping-design-fullgraph-deps/` | NEW snapshot | AGGREGATION |
| 3 | `_Aggregation/Hypergraph/HG_PIPING_DESIGN_F26_<MILESTONE>_<DATE>_<HHMM>/` | NEW snapshot | DOMAIN_HYPERGRAPH |

ORCHESTRATOR's WRITE_SCOPE during Step 1 is `_Coordination/` only. Step 2/3 dispatches are all human-gated; ORCHESTRATOR proposes the dispatch and the human authorizes before any owner-agent is invoked.

## Existing artifacts to reuse

- `_Coordination/_COORDINATION.md` AOP-01/AOP-02/AOP-03 + Acyclicity Filter Spec block — overlay-block shape (Source-of-truth / Subordinate side / Generalizes / Coverage / Implication for downstream). Reuse verbatim shape for AOP-04..AOP-09.
- `_Coordination/NEXT_INSTANCE_STATE.md` Session 11 / Session 12 blocks — structural template for Session 13 block.
- `_Coordination/DOMAIN_DECOMP_REMEDIATION_PLAN_2026-05-02.md` lines 197–222 — sequencing-summary diagram template.
- `tools/scaffolding/write_status.sh` — not needed (no lifecycle changes in Steps 1–3).
- `tools/validation/validate_dependencies_schema.py` — re-run after any dependency-extract refresh that lands in Wave 3 tail / Wave 4.
- `tools/validation/validate_domain_decomposition_integrity.py` + `tools/reporting/synthesize_domain_coverage_json.py` — Wave 2 fix targets; must be re-tested post-fix.
- `.Archive/PIPING_DESIGN_CROSS_CUTTING_REMEDIATION_PLAN.md` — archived/completed convention reference for project-plan structure.
- `.Archive/PIPING_DESIGN_ITEMS_7_8_FOLLOWUP_PLAN.md` — archived/completed convention reference; the Item-7 trigger watch artifact is now carried by `_Coordination/NEXT_INSTANCE_STATE.md`.

---

## Verification

End-to-end verification of the execution sequence:

1. **After Step 1 (rulings transcribed):**
   - `grep -c "^### AOP-" _Coordination/_COORDINATION.md` returns 3 + (number of new overlays). With all six rulings, expect 9.
   - `_Coordination/DOMAIN_DECOMP_OPEN_QUESTIONS_2026-05-02.md` `Status:` line is `RULED 2026-05-02` (or `PARTIALLY_RULED 2026-05-02`).
   - `grep "Pre-req: human ruling" _Coordination/DOMAIN_DECOMP_REMEDIATION_PLAN_2026-05-02.md` no longer hits any ruled question's wave; instead `Pre-req: ruled YYYY-MM-DD → <route name>`.
   - `grep -c "^## Session 13" _Coordination/NEXT_INSTANCE_STATE.md` returns 1.
   - `git diff --stat HEAD~1..HEAD` shows changes only inside `_Coordination/`.

2. **After Step 2A (Wave 1 SCA-002):**
   - `_ScopeChange/SCA-002_PackageMetadataCorrigendum/` folder exists with the four MODIFY actions documented.
   - `_Decomposition/.../Companion_Inventory.csv` row count = 71 (was 30).
   - `_Decomposition/_LATEST.md` resolves to the inner snapshot folder name.
   - `_Decomposition/.../Decision_Log.csv` `DEC-016` Status updated; `DEC-003` `ImpactedIDs` enumerated.
   - `tools/validation/validate_domain_decomposition_integrity.py` against the inner folder still returns 0 findings.

3. **After Step 2B/2C (Wave 2 tools/spec/B02):**
   - `tools/validation/validate_domain_decomposition_integrity.py` against `_Decomposition/` (top level) returns 0 findings (or documented `--package-subfolder` flag is required).
   - `python -m pytest tools/...` passes.
   - `tools/reporting/synthesize_domain_coverage_json.py` output matches `Coverage_Telemetry.json` schema parity (`FINAL-ACCEPTED-v1.0` revision; integer-typed numerics).
   - `Validation_Checks.csv` VAL-018 / VAL-017 now check completeness, not just presence; both still PASS post-Wave-1.

4. **After Step 2D–2H (waves whose dispatch is gated on Q2/Q3/Q4/Q5/Q6):**
   - Each wave's SCA lands cleanly through SCOPE_CHANGE Gates 1–5.
   - If any register row count changes: a fresh AGG snapshot is published under `_Aggregation/_Pipelines/piping-design-fullgraph-deps/`; `_LATEST.md` updated.
   - If any topology changes: a fresh DOMAIN_HYPERGRAPH snapshot under `_Aggregation/Hypergraph/HG_PIPING_DESIGN_F26_<MILESTONE>_<DATE>_<HHMM>/` with 9/9 QA PASS.

5. **Cross-cutting safety check (every step):**
   - `git status` after each step shows changes scoped to the file list above. No edits to `_Decomposition/.../FINAL_ACCEPTED_v1_0_FIXED/` outside an explicit SCA snapshot folder. No edits to `_Sources/`, `.archive/`. No `_LATEST.md` writes outside the explicit owner-agent dispatch.

6. **Handoff dry-run:** A reader who opens `NEXT_INSTANCE_STATE.md` cold can find: (a) where Q1–Q6 live (scaffold path), (b) which user preferences are locked in (Session 12 block + this plan), (c) where to find the executable plan (this file's path), (d) what the immediate next action is (rule on Q1–Q6, then resume from Step 1).

---

## Refined Sequence (Session 14, 2026-05-03)

**Status update:** `READY_TO_EXECUTE_AFTER_RULINGS` → `CASCADE_DISPATCHABLE` (Session 14) → `CASCADE_IN_PROGRESS` (Session 15, 2026-05-03) → continuing through Session 19 (2026-05-04). Precursor R-TOOL (commit `d88247a0`), SCA-002 corrigendum + AOP-03 retro Option A bundle (commit `7948d02d`), SCA-002 closure transitions (Session 16; 3 VERIFY_KTY dispatches all VERIFIED + manifest closure rollup; both validators 0/0; closure verdict `CLOSED_FOR_SCOPE_CHANGE_ONLY`), AOP-03 DISSOLVED overlay edit (Session 16), R-SPEC pass for Q2 + Q4 (Session 16; closes AUDIT-C03/C04/D01 as `RESOLVED-IN-PRACTICE`), SCA-003 layout migration (Session 17 commit `15220674`; closes AUDIT-A01 BLOCKER physically; Q1=RETIRE / Q2=RETAIN / Q3=ADD / Q4=hand to ORCHESTRATOR follow-up; closure verdict `CLOSED_FOR_SCOPE_CHANGE_ONLY`), R-SPEC dual-layout note + DEC-018 fix-up (Session 17 commit `d7d470e1`), AOP-04 APPLIED status flip (Session 17 handoff), Q7=(b) ruling + SCA-008 AOP-02 retro sync (Session 18 commit `d18b871f`; AOP-02 reciprocity invariant 42/42 established), and **SCA-004 Q5 zero-AU backfill ✅ CLOSED Session 19 (2026-05-04)** — 261 atomic units APPENDED + 17 HBK seeds + 19 KT-register MODIFYs + 4 reciprocity firings (DEC-049..DEC-052) + 27 SUB-register MODIFYs + GAP-003/GAP-004 closed; AOP-02 reciprocity 42/42 PASS post-closure; closure verdict `CLOSED_FOR_SCOPE_CHANGE_ONLY`; AOP-08 APPLIED status flip landed in this Session 19 handoff — have all landed. **R-SPEC Q5 (scaffold-for-fill text formalization) ✅ COMPLETE Session 20 (2026-05-04); R-TOOL #31 (validator path-resolution + foreign-key SourceActionRef) ✅ COMPLETE Session 20 — 60 MAJOR validator-noise findings eliminated; 19/19 pytest PASS; SCA-002/003/008 baselines preserved at 0/0. SCA-005 (Q6 SUB cardinality) ✅ CLOSED Session 21 (2026-05-05) — 42 KTYs re-partitioned; net active SUBs 88 → 97; Validator B patched in-cycle; all 4 validators clean; AOP-09 APPLIED. SCA-006 (Q3 TBD reissue) ✅ CLOSED Session 22 (2026-05-05) — 42 × IntendedUsers/WhenUsed → TBD; DEC-116..DEC-158; 42 Scoping.md Identity table rows updated; both validators 0/0; AOP-06 APPLIED. **SCA-007 (AOP-01 retro denormalization) ✅ CLOSED Session 23 (2026-05-06)** — 7 OBJ rows denormalized; Objective_to_KnowledgeType_Map.csv retired; DEC-159..DEC-167; OBJECTIVE_KTY_PARITY_MISMATCH validator; both validators 0/0; AOP-01 APPLIED. **Post-cascade re-aggregation ✅ CLOSED Session 24 (2026-05-06)** — `AGG_Dependency_Register_FullGraph_2026-05-06_0900` (470 rows; 7/7 PASS; 0 cycles) + `HG_PIPING_DESIGN_F26_POST_CASCADE_2026-05-06_1200` (9/9 PASS; bijection 97↔97; cascade-driven node/edge deltas exact) snapshots published; both pipeline `_LATEST.md` pointers flipped. Forward content work and optional threshold-change ruling remain open.** The conditional fan-out below (Steps 2A–2H) is superseded by the linear cascade in this section; the original detail is retained as historical record. Owner-agents and write-scopes per Steps 2A–2H still apply.

### Cascade progress (Sessions 15–20, 2026-05-03..2026-05-04)

| Step | Owner | Status | Commit | Notes |
|---|---|---|---|---|
| Step 1 transcription | ORCHESTRATOR | ✅ COMPLETE | `5232f68c` (Session 14) | Q1–Q6 rulings codified; AOP-04..09 appended |
| Precursor R-TOOL | TOOLMAKER | ✅ COMPLETE | `d88247a0` (Session 15) | Transitional dual-layout validator + synthesizer; 18/18 pytest pass |
| SCA-002 corrigendum + AOP-03 retro Option A bundle | SCOPE_CHANGE | ✅ COMPLETE (Gates 1–5) | `7948d02d` (Session 15) | Closes A02/A03/G01/G02; 6 KA renames applied |
| SCA-002 follow-ups (3× VERIFY_KTY + AOP-03 DISSOLVED edit) | ORCHESTRATOR + TASK | ✅ COMPLETE (Session 16) | `0c8ba315` (Session 16 handoff) | All 3 VERIFY_KTY = VERIFIED; manifest 3/3 VERIFIED; both validators 0/0; closure verdict `CLOSED_FOR_SCOPE_CHANGE_ONLY`; AOP-03 DISSOLVED in `_COORDINATION.md` |
| R-SPEC parallel (Q2 + Q4) | SKILLMAKER (subagent) | ✅ COMPLETE (Session 16) | `0c8ba315` (Session 16 handoff) | 4-line text-only edit to `agents/AGENT_DOMAIN_DECOMP.md` STRUCTURE §1 + §5; closes AUDIT-C03/C04/D01 as `RESOLVED-IN-PRACTICE` |
| SCA-003 Q1 layout migration | SCOPE_CHANGE | ✅ COMPLETE (Gates 1–5) | `15220674` (Session 17) | 71 annex files relocated to `_Decomposition/` canonical root; Q1=RETIRE / Q2=RETAIN / Q3=ADD / Q4=hand to ORCHESTRATOR follow-up; closes AUDIT-A01 BLOCKER physically; closure verdict `CLOSED_FOR_SCOPE_CHANGE_ONLY`; KTY remediation manifest = zero rows; both validators 0/0 against canonical layout; Pre/Post coverage byte-identical |
| SCA-003 follow-ups (R-SPEC dual-layout note + DEC-018 fix-up) | ORCHESTRATOR | ✅ COMPLETE (Session 17) | `d7d470e1` (Session 17) | `agents/AGENT_SCOPE_CHANGE.md` §"Deterministic Tool Contracts" extended with dual-layout note (`--decomposition-root` canonical default + `--package-subfolder` transitional); DEC-018 row append fix-up (RM-split silent omission caught + corrected) |
| AOP-04 APPLIED Coordination overlay edit | ORCHESTRATOR | ✅ COMPLETE (Session 17) | this Session 17 handoff | `_COORDINATION.md` § AOP-04 status header added: `Status (piping-design): APPLIED 2026-05-03`. Overlay remains in force as canonical convention for ALL DOMAIN packages going forward |
| SCA-004 Gate 1 | SCOPE_CHANGE | ✅ COMPLETE (Session 18, 2026-05-03) | — | Snapshot `_ScopeChange/SCA-004_2026-05-03_1800/`; 4 deliverables. Pre-change baseline: 16,510 AUs / 458 ParentSeed / 42 KTYs / 88 SUBs / 10 CATs / 7 OBJs / 18 vocabulary terms. Validation 0/0; parsed action = single composite MODIFY against GAP-003 (7 KTYs) + GAP-004 (27 SUBs). Human-confirmed. |
| SCA-004 Gate 2 (original) | SCOPE_CHANGE | ⏸ PAUSED at gate boundary 2026-05-03 (Session 18) — paused for Q7 ruling resolution | — | Gate 2 deliverables authored (Impact_Assessment.md 584 lines, 13 sections; Decision_Log.md and RUN_SUMMARY.md Gate 2 entries APPENDED). Five questions surfaced (Q1–Q5). Q4 = KT-register `SupportsObjectives` amendment scope — paused for Q7 ruling. |
| **SCA-008 AOP-02 retro sync** | SCOPE_CHANGE | ✅ **CLOSED Session 18 commit `d18b871f`** | `d18b871f` | Q7=(b) AOP-02 retro sync. 29 KT-register cell widenings + 29 Decision_Log APPENDs DEC-019..DEC-047. AOP-02 reciprocity invariant 42/42 PASS established post-closure. Coverage telemetry byte-identical pre/post (strong invariant verified). Cumulative supersession chain SCA-002 → SCA-003 → SCA-008. Closure verdict `CLOSED_FOR_SCOPE_CHANGE_ONLY`; `ReadyForNextPhase=YES`. |
| **SCA-004 Gate 2 REOPEN** | SCOPE_CHANGE | ✅ **CONFIRMED Session 18 (2026-05-03)** post-SCA-008 | — | Single SCOPE_CHANGE dispatch APPEND-only to existing snapshot files. Brief.md +68 lines (Addendum §§A–I); Impact_Assessment.md +144 lines (§15 addendum subsections §15.1–§15.14); Decision_Log.md +29 lines (REOPEN entry); RUN_SUMMARY.md +89 lines (§10 REOPEN supplement). Q4 disposition supersession by Q7=(b) reciprocal-extension rule documented; DEC-### binding shifted to DEC-048 onward; supersession-map predecessor shifted to SCA-008. Q-new-1 + Q-new-2 surfaced for Gate 3/4. Human-confirmed: "yes I do accept this impact assessment." |
| **SCA-004 Gate 3** | SCOPE_CHANGE | ✅ COMPLETE (Session 18, 2026-05-03) | — | Amendment Approval landed; Q1/Q2/Q3 ruled DEFAULT; Q4 ruled EXISTING-TERMS-MAPPING (preserve `Coverage_Gaps_Register.csv` Status enum {NONE, ACCEPTED_BY_GATE5, OPEN_CONDITIONAL}; no new enum values introduced). Decision_Log + RUN_SUMMARY APPEND. |
| **SCA-004 Gate 4** | SCOPE_CHANGE | ✅ COMPLETE (Session 18, 2026-05-03) | — | Propagation_Plan.md (677 lines, 12 sections + boundary) + Amendment_Actions.csv (78 data rows, 13 logical blocks A..M) + KTY_Remediation_Manifest.csv (20 anchor rows MR-001..MR-020) authored. Pass-3 dispatch brief skeleton with Q1/Q3 binding rules included in §5. |
| **SCA-004 Gate 5** | SCOPE_CHANGE | ✅ **CLOSED Session 19 (2026-05-04)** | (this Session 19 commit) | Phased waves (Option B): Wave 1 (7 Cohort A KTYs parallel) → Wave 2 (13 Cohort B KTYs parallel) → closure subagent. **261 atomic units** APPENDED (HBA-016511..HBA-016771) — 7 GAP-003 KTYs (123 rows) + 13 Cohort B parents (138 rows). **17 new HBK seeds** (HBK-0473..HBK-0489); reuses on HBK-0003/0015/0031/0209..0212/0214/0320/0366/0429. **19 KT-register MODIFYs**; **4 SupportsObjectives reciprocity widenings** (DEC-049..DEC-052: KTY-02-04 +OBJ-002, KTY-04-04 +OBJ-002, KTY-02-02 +OBJ-001 drift correction, KTY-04-01 +OBJ-001). **27 SUB-register MODIFYs**; GAP-003 + GAP-004 → Status=NONE (full backfill). **DEC-048** closure marker. **All 4 validators PASS**: A integrity 0 findings, B manifest VERIFIED (0 PENDING_ROW; 60 MAJOR pre-existing path/SourceActionRef framework noise), C AOP-02 reciprocity 42/42, D telemetry directional confirmed. Closure verdict `CLOSED_FOR_SCOPE_CHANGE_ONLY`; `ReadyForNextPhase=YES`. Anomalies: KTY-10-02 row count 18 vs envelope 21 (actual evidence governs); KTY-03-04 name correction applied; 6 cross-cutting findings flagged for future SCAs (Handoff_State.md §6). |
| **AOP-08 APPLIED Coordination overlay edit** | ORCHESTRATOR | ✅ COMPLETE (Session 19, 2026-05-04) | (this Session 19 commit) | `_COORDINATION.md` § AOP-08 status header added: `Status (piping-design): APPLIED 2026-05-04`. SCA-004 closure summary inlined; R-SPEC Q5 unlock noted; post-cascade R-TOOL ticket (`validate_kty_remediation_manifest.py`) logged. Overlay remains in force as canonical convention for ALL DOMAIN packages going forward; this status note records the piping-design backfill. |
| SCA-005 Q6 cardinality | SCOPE_CHANGE | ✅ **CLOSED Session 21 (2026-05-05)** | (Session 21 commits) | 42 KTYs re-partitioned per post-SCA-004 AU density tiers. Net active SUBs 88 → 97 (37 deprecated, 46 new; Q3 α = Status=DEPRECATED + DeprecationDecisionRef). KTY-03-04 AtomicUnitCount corrigendum (305 → 312) bundled. KTY-03-01/-02/-03 `SupportsObjectives` byte-normalization bundled. 3 Wave 3 stream-idle timeout recoveries (KTY-03-05 effective SUCCESS; KTY-02-04 + KTY-04-04 recovery subagents). Validator B patched in-cycle (97 → 0 findings; Gate 4 mis-declaration of TaskSkill on 17 β rebind rows corrected). All 4 validators clean. Closure verdict `CLOSED_FOR_SCOPE_CHANGE_ONLY`; `ReadyForNextPhase=YES`. AOP-09 APPLIED. |
| SCA-006 Q3 TBD reissue | SCOPE_CHANGE | ✅ **CLOSED Session 22 (2026-05-05)** | (Session 22 commit) | 42 × `IntendedUsers`/`WhenUsed` → `TBD` in `Knowledge_Type_Register.csv`; 43 Decision_Log APPENDs (DEC-116..DEC-158); 42 per-KTY `Scoping.md` Identity table rows updated (41 targeted metadata edits + 1 REGENERATE_CONTENT for KTY-05-03 sub-option B); both validators 0/0. Cumulative supersession chain SCA-002 → ... → SCA-006. Closure verdict `CLOSED_FOR_SCOPE_CHANGE_ONLY`; `ReadyForNextPhase=YES`. AOP-06 APPLIED. Closes AUDIT-E01 + AUDIT-E02. |
| R-SPEC Q5 scaffold-for-fill | ORCHESTRATOR (self-write) | ✅ **COMPLETE (Session 20, 2026-05-04)** | (this Session 20 commit) | Two text-only edits to `agents/AGENT_DOMAIN_DECOMP.md`: "No invention" non-negotiable extended with source-line-evidence requirement (per AOP-08); new "Scaffold-for-fill (per AOP-08)" paragraph appended to STRUCTURE §3 Coverage & Telemetry. Generic phrasing; AOP-08 cited; mirrors AOP-07 (line 419) + AOP-05 (line 458) R-SPEC patterns. File grew 480 → 482 lines. |
| Q7 ruling | Human | ✅ RULED 2026-05-03 (Session 18) = (b) Extend with reciprocal-author-worker mechanism | — | See revised AOP-02 overlay; SCA-008 dispatched pre-SCA-004 |
| SCA-007 AOP-01 retro | SCOPE_CHANGE | ✅ **CLOSED Session 23 (2026-05-06)** | (Session 23 commit) | 7 OBJ rows in `Objective_Register.csv.MappedKnowledgeTypes` denormalized from KT-register inversion (OBJ-001: 20→33 KTYs; OBJ-002: 16→15; OBJ-003: 22→25; OBJ-004: 17→18; OBJ-005: 17→22; OBJ-006: 17→19; OBJ-007: 12→24). `Objective_to_KnowledgeType_Map.csv` (124 rows) retired as `RETIRED_DERIVED_ARTIFACT` (git mv to `_Decomposition/_Archive/`). `Companion_Inventory.csv` PackageRole updated. DEC-159..DEC-167 (9 rows) appended (DEC-159 closure marker; DEC-160..DEC-166 per-OBJ MODIFY; DEC-167 map retirement + validator). `OBJECTIVE_KTY_PARITY_MISMATCH` check added to `validate_domain_decomposition_integrity.py`. Both validators 0/0. Closure verdict `CLOSED_FOR_SCOPE_CHANGE_ONLY`; `ReadyForNextPhase=YES`. AOP-01 APPLIED. |
| **R-TOOL #31: validate_kty_remediation_manifest.py patch** | TOOLMAKER (ORCHESTRATOR self-write) | ✅ **COMPLETE (Session 20, 2026-05-04)** | (this Session 20 commit) | Added `find_workspace_root()` helper walking up from manifest folder to nearest ancestor with `_Sources/` or `_Decomposition/` sibling; extended `resolve_path()` to accept workspace_root fallback; extended `index_actions()` to register `<AmendmentID>:<ActionSeq>` foreign-key form alongside existing keys; added `--workspace-root` CLI override. 3 new pytest cases; 19/19 pytest PASS. Live SCA-004 manifest now reports 20 MAJOR (down from 80) — the 60 targeted findings (40 EVIDENCE_PATH_MISSING + 20 ACTION_NOT_FOUND) eliminated; SCA-002/003/008 manifests preserved at 0/0 (non-regressive). `tools/REGISTRY.md` entry updated. **NEW finding #32 surfaced (CONTENT_ACTION_MISMATCH semantic gap for `MODIFY KNOWLEDGE_TYPE_REGISTER_ROW` + `REGENERATE_CONTENT`)** previously masked by the ACTION_NOT_FOUND short-circuit; logged as separate framework-hardening item. |
| Post-cascade re-aggregation | AGGREGATION + DOMAIN_HYPERGRAPH | ✅ **CLOSED Session 24 (2026-05-06)** | (Session 24 commit) | Phase 1: 3 parallel `TASK + dependency-extract` (KTY-01-03/08-03/10-02; MODE=UPDATE/STRICTNESS=CONSERVATIVE/CONSUMER_CONTEXT=AGGREGATION) cleared SCA-002 KA-rename + SCA-003 namespace stale `EvidenceFile`/`TargetLocation` strings. Phase 2 mechanical sweep on non-factual files (`_CONTEXT.md` ×42 + `_REFERENCES.md` ×42 + `_DEPENDENCIES.md` ×39 + `Dependencies.csv` ×32) — 390 path-string replacements across 154 files. Phase 3 pre-aggregation gate: `validate_domain_decomposition_integrity.py` 0/0; SCA-007 manifest validator unchanged from baseline. Phase 4 produced `_Aggregation/AGG_Dependency_Register_FullGraph_2026-05-06_0900/` (470 rows; 7/7 QA gates PASS; 3 acyclicity-filtered edges, 0 cycles; RECIPROCAL_MISSING=33 unidirectional pairs informational). Phase 5 produced `_Aggregation/Hypergraph/HG_PIPING_DESIGN_F26_POST_CASCADE_2026-05-06_1200/` (9/9 QA gates PASS; 17,024 nodes / 17,260 hyperedges / 110,119 incidences; SUB↔KA bijection 97↔97; comparison-mode deltas confirm cascade exactly: ATOMIC_UNIT +261, KNOWLEDGE_SUBJECT +9 active, KTY_SUPPORTS_OBJ +35). Pipeline pointers `_Aggregation/_Pipelines/piping-design-fullgraph-deps/_LATEST.md` + `_Aggregation/Hypergraph/_LATEST.md` flipped; `_Aggregation/_LATEST.md` not touched. Factual-layer staleness (33 `Scoping.md` + 47 `KA-*.md` + 1 `_MEMORY.md`) deferred to next `domain-documents` Pass 3 rerun under one-writer rule. |

### Findings surfaced during Session 15 SCA-002 execution (framework hardening backlog)

| # | Finding | Owner | Task |
|---|---|---|---|
| 1 | KTY rename lane not formally codified in `AGENT_SCOPE_CHANGE.md` (pure renames vs content writes) | SKILLMAKER + DBM_PUBLISHER | #27 |
| 2 | `validate_kty_remediation_manifest.py` `FACTUAL_GATE_MISMATCH` MAJOR for `ALLOW_FACTUAL_USE + PENDING` (briefing/validator enum gap) | TOOLMAKER + SKILLMAKER | #28 |
| 3 | `CONTENT_DISPOSITION_STATE` enum lacks `PENDING_DISPATCH` value (briefing convention drift) | TOOLMAKER + SKILLMAKER | #29 |
| 4 | Nested `TASK + skill` dispatch unsupported within a SCOPE_CHANGE subagent — Gate 5 must author dispatch briefs for ORCHESTRATOR follow-up | SKILLMAKER | #30 |

### Rulings table (Session 14)

| Q | Ruling | Route | Overlay | Closes |
|---|---|---|---|---|
| **Q1** | Annexes-at-`_Decomposition`-root canonical | R-SCA-RECONCILE (SCA-003) + R-TOOL precursor (transitional validator) | AOP-04 | AUDIT-A01 BLOCKER |
| **Q2** | Policy-only granularity intentional | R-SPEC text only | AOP-05 | AUDIT-C03 + C04 |
| **Q3** | Label `IntendedUsers`/`WhenUsed` as `TBD`; revise CSV | R-SCA-CORRIG (SCA-006; piping-design CSV only) | AOP-06 | AUDIT-E01 + E02 |
| **Q4** | Bounded scope (niche / novel / ambiguous terms only) | R-SPEC text only | AOP-07 | AUDIT-D01 |
| **Q5** | Scaffold-for-fill WITH `_Sources/`-driven backfill predecessor | R-SCA-RECONCILE (SCA-004 backfill) + R-SPEC (formalize after) | AOP-08 | AUDIT-F02 |
| **Q6** | Cardinality must vary with content density | R-SCA-RECONCILE (SCA-005; post-Q5 backfill) | AOP-09 | AUDIT-F01 |

### Sequencing graph (linear cascade)

```
                    Step 1: Transcription (Session 14, single bundled commit)
                                    │
                                    ▼
                    Precursor R-TOOL (TOOLMAKER)
                  (transitional layout recognition; resolves Gate 1
                   chicken-and-egg for SCA-003)
                                    │
                                    ▼
                    SCA-002: Q-independent corrigendum (SCOPE_CHANGE)
                  + (proposed) AOP-03 retro: 3 KA file renames
                                    │
                                    ▼
                    SCA-003: Q1 layout migration (SCOPE_CHANGE)
              (annexes from .../MWK1956_..._FIXED/ → _Decomposition/)
                                    │
                                    ▼
                    SCA-008: Q7=(b) AOP-02 retro sync (SCOPE_CHANGE)
              (extend KT-register `SupportsObjectives` for the 29 of 42 KTYs
               showing existing divergence; per-extension Decision_Log entries;
               pre-SCA-004 ordering per Session 18 ruling)
                                    │
                                    ▼
                    SCA-004: Q5 zero-AU backfill (SCOPE_CHANGE)
              (populate 7 KTYs + 27 SUBs from _Sources/ via
               domain-documents Pass-3 enrichment; reciprocal-extension
               rule applies — new atomic objectives extend KT-register
               `SupportsObjectives` at Gate 5)
                                    │
                                    ▼
                    SCA-005: Q6 SUB cardinality reconciliation (SCOPE_CHANGE)
              (re-partition SUBs given post-Q5 AU densities)
                                    │
                                    ▼
                    SCA-006: Q3 CSV TBD reissue (SCOPE_CHANGE)
              (revert IntendedUsers/WhenUsed to TBD; regenerate Scoping.md)
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
   R-SPEC (Q2)              R-SPEC (Q4)              R-SPEC (Q5 post-SCA-004)
   DBM_PUB / SKILLMAKER     DBM_PUB / SKILLMAKER     DBM_PUB / SKILLMAKER
   (text-only; can run anytime post-Step-1; not gated on SCA cascade)
                                    │
                                    ▼ (separate ruling required)
                    Q7: AOP-02 retro disposition (Q&A)
                                    │
                                    ▼ (if approved)
                    SCA-007: AOP-01 retro denormalization (proposed; SCOPE_CHANGE)
              (Objective_to_KnowledgeType_Map.csv → MappedKnowledgeTypes;
               validator rewrite; deterministic mechanical sync)
```

**Dispatch boundary:** Each SCA dispatches separately through `agents/AGENT_SCOPE_CHANGE.md` 5-gate workflow. Gates 1–5 each require explicit human approval. ORCHESTRATOR surfaces dispatch readiness; the human authorizes before each owner-agent invocation. R-SPEC dispatches are also human-gated; DBM_PUBLISHER / SKILLMAKER do not auto-edit `agents/AGENT_*.md` without authorization.

### Per-step refinement vs Steps 2A–2H

The refined cascade replaces the parallelization graph at lines 199–221. Per-step content from Steps 2A–2G is reused with the following overrides:

- **Step 2A (Wave 1 corrigendum SCA-002):** unchanged in scope — four MODIFY actions per AUDIT-A02/A03/G01/G02. Proposed addition: bundle AOP-03 retro renames (3 KA-SUB-form files in KTY-01-03, KTY-08-03, KTY-10-02 → `KA-NN_{Type}__{Slug}.md`) per Phase 1 ITEM8 audit (zero runtime impact; skills already form-agnostic). Final bundling decision at Gate 4 (Propagation Plan).

- **Step 2B (Wave 2 head A01+B01):** Q1 ruling = (b) annexes-at-root canonical. The R-TOOL update is **PRECURSOR** (transitional dual-layout recognition) — runs BEFORE SCA-003 to resolve the Gate 1 chicken-and-egg. The R-SPEC update on `agents/AGENT_SCOPE_CHANGE.md` lands as part of or after SCA-003 completion (SPEC text now describes annexes-at-root as the standard call, with no `--decomposition-root` override needed).

- **Step 2C (Wave 2 tail B02):** unchanged — gated by SCA-002 corrigendum landing. Validation generator extension from presence-only to completeness checks for VAL-017 / VAL-018.

- **Step 2D (Wave 3 head C01+C02 verify-only):** unchanged — verify AOP-01 + AOP-02 are still current after Step 1's AOP-04..09 append. AOP-01 + AOP-02 retro consideration is now separate (proposed SCA-007 + Q7).

- **Step 2E (Wave 3 tail C03+C04):** Q2 ruling = (c) policy-only granularity intentional. R-SPEC only; no skill scoping. DBM_PUBLISHER / SKILLMAKER edits `agents/AGENT_DOMAIN_DECOMP.md` to document the policy. Can run anytime post-Step-1.

- **Step 2F.1 (Wave 4 D01 vocabulary):** Q4 ruling = (a) bounded scope. R-SPEC only; no `domain-vocabulary-extract` skill scoped. DBM_PUBLISHER / SKILLMAKER documents the bounded scope (niche / novel / ambiguous terms only).

- **Step 2F.2 (Wave 4 E01/E02/E03 metadata):** Q3 ruling = new shape (d-local) — TBD reissue + CSV revision. SCOPE_CHANGE alone (SCA-006). No SPEC change; no skill scoping. AUDIT-E03 (SUB Description thinness) is separate and not addressed under this ruling.

- **Step 2G (Wave 5 F02 SPEC):** Q5 ruling = (a) WITH backfill predecessor. SCA-004 backfill lands first; R-SPEC formalization on `agents/AGENT_DOMAIN_DECOMP.md` happens after to describe post-backfill canonical state.

- **Step 2H (Deferred F01):** Q6 ruling = (b) cardinality must vary. **Promoted from deferred to active** as SCA-005, sequenced AFTER SCA-004 backfill (so densities are accurate) and BEFORE SCA-006 (so SUB changes settle before metadata reissue).

### Q7 — AOP-02 retro disposition — RULED Session 18 (2026-05-03) = (b) Extend with reciprocal-author-worker mechanism

Per the user's Session 14 meta-direction ("revising the previous AOP decisions to provide for consistency rather than exceptions to rules and overlays"), AOP-02 (Domain_Ledger ObjectiveID asymmetry vs KT-register `SupportsObjectives`) was flagged as a candidate for retro-conversion. **Ruled Session 18 (2026-05-03) = (b) Extend** with this operating mechanism:

- KT-register remains authoritative AS THE RECORD of what KTY-level objectives exist.
- Discoveries during KA authoring (Pass-3 enrichment, scope-driven SCA dispatch, or any future content pipeline) that surface objectives in atomic-ledger `ObjectiveID(s)` not yet in the parent KTY's `SupportsObjectives` propagate **backwards** into the KT-register, with each extension recorded as a `Decision_Log.csv` entry.
- Standing approval for the reciprocal mechanism granted by the human in-session 2026-05-03; per-extension Decision_Log entries are the audit trail, not per-extension authorization gates.

**Sequencing ruling (same session 2026-05-03):** retro sync via **SCA-008 with pre-SCA-004 ordering**. SCA-008 reconciles the 29 of 42 KTYs showing existing divergence by extending KT-register `SupportsObjectives` with all atomic-observed objectives. SCA-004 Pass-3 dispatch then operates against an already-consistent KT-register baseline.

See `_Coordination/_COORDINATION.md` § AOP-02 (REVISED Q7=(b) overlay block; original framing preserved); `_Coordination/DOMAIN_DECOMP_OPEN_QUESTIONS_2026-05-02.md` Q7 ruling block; `_Coordination/NEXT_INSTANCE_STATE.md` §3 ruling 25 + Session 18 block.

### AOP retro-conversion proposals (separable scope)

| AOP | Disposition | Blast | When |
|---|---|---|---|
| AOP-03 (KA naming forms) | **Proposed bundle into SCA-002 corrigendum** (3 file renames; skills already form-agnostic per `_Coordination/ITEM8_KA_FORM_AUDIT_2026-05-02.md`; no information loss). Final decision at SCA-002 Gate 4. | SMALL | SCA-002 |
| AOP-01 (Objective_Register asymmetry) | **Proposed SCA-007 post-cascade** (denormalize 124-row map back into `Objective_Register.csv.MappedKnowledgeTypes`; rewrite `validate_domain_decomposition_integrity.py`; deterministic mechanical sync). Awaits user authorization. | MEDIUM | post-SCA-006 |
| AOP-02 (Domain_Ledger ObjectiveID asymmetry) | **Q7 RULED 2026-05-03 = (b) Extend with reciprocal-author-worker mechanism.** SCA-008 retro pre-SCA-004 (mechanical KT-register `SupportsObjectives` extension across 29 of 42 KTYs; per-extension Decision_Log entries). Going-forward: any SCA or content-authoring session extending atomic-ledger `ObjectiveID(s)` simultaneously extends parent KT-register `SupportsObjectives`. | LARGE (existing-state retro) + STANDING (going-forward) | SCA-008 pre-SCA-004 |

### User-confirmed execution preferences from Session 14

These augment the Session 12 preferences locked at lines 35–41 above. They are durable assumptions for the cascade.

1. **AOP-03 retro proposed for SCA-002 bundling.** Final bundling decision deferred to SCA-002 Gate 4 / Propagation Plan.
2. **AOP-01 retro proposed for SCA-007.** Authorization deferred to post-SCA-006 landing.
3. **AOP-02 retro promoted to Q7.** Awaits separate human ruling; default = leave as overlay.
4. **R-SPEC parallel pass timing:** dispatch alongside the SCA cascade (text changes are independent); not held until post-SCA-006.
5. **Precursor R-TOOL retention post-SCA-003:** retain `--package-subfolder` flag as forward-compatible safety net (favors any future re-nesting); revert if/when policy spirit demands strict canonical-only validation.

---

## Out of scope for this plan

- **Forward content work** (lifecycle progression beyond `IN_PROGRESS`) — owned by WORKING_ITEMS + per-KTY pipeline agents (TASK + content skills); Session 10 carryover, awaits separate human direction.
- **Threshold change** above `INITIALIZED` — Session 10 carryover; would activate Item 7 trigger #1 per receiving KTY.
- **Item 7 reciprocity sweep** — `WATCHING` per `_Coordination/ITEM7_RECIPROCITY_PUNCHLIST_2026-05-02.md`. Independent of this plan; only re-engages if a trigger fires.
- **DOMAIN packages other than piping-design** — per user direction, Wave 2 tooling fix is scoped to piping-design only. Other DOMAIN packages (West_Doe, Pipe_Specs, etc.) adopt later if they want.
- **`_CONTEXT.md` template vs SKILL default reconciliation** — `RESOLVED-IN-PRACTICE` per Session 4 Item 8 audit; tooling tracker at `plans/RECONCILE_CONTEXT_TEMPLATE_VS_SKILL_NAMING.md` owned by tooling/skill maintainers.

---

## Boundary record

- ORCHESTRATOR write-scope at Step 1: `_Coordination/` + `plans/` only.
- Owner-agent write-scopes at Step 2: bounded by each agent's definition; SCOPE_CHANGE writes inside `_ScopeChange/SCA-NNN/...` and (after acceptance) the named annex CSV/JSON paths; TOOLMAKER writes `tools/...` + `tests/...`; SKILLMAKER writes `skills/<name>/`; DBM_PUBLISHER writes `agents/...`.
- No edits to `.archive/retired-decomposition-2026-04-30/` at any step.
- `_LATEST.md` writes only by owner-agents (DOMAIN_HYPERGRAPH, AGGREGATION) in Step 3; never by ORCHESTRATOR or by hand.

EOF
