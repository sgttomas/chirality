# DEL-08-01 — forward-pass notes (RUN_D128_CONCORDANCE_2026-09-21_1614Z, R2 PKG-08)

Epistemic status: worker evidence at frozen basis `00115c719`. Nothing here is a ruling.

## 1. Census

- **Rows:** 50 data rows. They cover the 30 indexed units (SEC-1..3, CLM-001..026, REM-1), plus
  6 `REGISTER-n` rows and 1 `STATE-n` row.
- **By ClaimType:** REQUIREMENT 20 · CONTEXT_CLAIM 13 · REGISTER_DEFECT 6 · STATE_ASSERTION 5 ·
  ACCEPTANCE 4 · EXCLUSION 1 · REMAINING_WORK 1.
- **By Disposition:** STALE_SPECIFICATION 13 · PARTIALLY_IMPLEMENTED 10 · NOT_AUDITABLE 9 ·
  IMPLEMENTED_DIFFERENTLY 6 · ALIGNED 5 · REMAINING_STATE_MISMATCH 4 · DOCUMENTED_UNIMPLEMENTED 1 ·
  STALE_ASSESSMENT 1 · AUTHORITY_CONFLICT 1.
- **ClaimType × Disposition (main cells):**
  - REQUIREMENT: PARTIALLY_IMPLEMENTED 7, IMPLEMENTED_DIFFERENTLY 6, ALIGNED 4,
    STALE_SPECIFICATION 2, DOCUMENTED_UNIMPLEMENTED 1.
  - CONTEXT_CLAIM: NOT_AUDITABLE 9, STALE_SPECIFICATION 4.
  - STATE_ASSERTION: STALE_SPECIFICATION 4, AUTHORITY_CONFLICT 1.
  - REGISTER_DEFECT: REMAINING_STATE_MISMATCH 4, STALE_SPECIFICATION 2.
  - ACCEPTANCE: PARTIALLY_IMPLEMENTED 3, STALE_ASSESSMENT 1.
  - EXCLUSION: ALIGNED 1.
  - REMAINING_WORK: STALE_SPECIFICATION 1.
- **Split rate:** 1 of 30 units was split (3.3%). CLM-009, the requirements table
  DEL0801-REQ001..014, became `.1`–`.14`, so 14 of 50 rows are split rows.
  - No unit lists k ≥ 2 SubItems. CLM-012 (AC-001) and CLM-018 (VER-001) each hold one item and are
    not split.
- **SEE rows (counted separately):** 3. CLM-010, CLM-024 and CLM-026 each point to
  `SEE:DEL-08-01#CLM-004`, which anchors the repeated statement "PRD current under D-APP-38 /
  REF-006 MATCH".
- **HumanDecisionNeeded ≠ NO:** 17 rows in total: `R4; R4-Q1` 9 · `R4-Q1` 5 · `R4` 3.
- **Errata:** none. This is the forward pass, so the sealed and errata-applied figures are the same.

## 2. Least-confident rows

- **`CLM-009.9` (DEL0801-REQ009, section markers), LOW, DOCUMENTED_UNIMPLEMENTED.**
  - Why this reading: the validator module is LEGACY_ONLY and only tests call it. The packaged v3
    role files use `## PROTOCOL` headings without `[[BEGIN:…]]` markers, and no live or packaging
    check validates sections. §2.3 says to judge on the live path, which gives this disposition.
  - Alternative: DEL-08-01 is a TEST_SUITE deliverable, so the fixture suite may itself be the
    obligation. That would make the row PARTIALLY_IMPLEMENTED: the validator and fixtures exist, but
    nothing applies them to the real files.
- **`CLM-009.14` (DEL0801-REQ014, unknown option keys), LOW, PARTIALLY_IMPLEMENTED.**
  - Why this reading: the live registry loader ignores unknown keys but gives no warning.
  - Alternative: App SPEC §7.4 concerns frontmatter, and v3 role files no longer have any. On that
    reading the row is NOT_AUDITABLE on the live path.
- **MEDIUM rows most worth a verifier look:**
  - **`CLM-009.7`, `.8` and `.10` (IMPLEMENTED_DIFFERENTLY):**
    - App SPEC §7.1/§7.2 and CONTRACT K-WRITE-1 are unamended. The packaged Root role files carry
      type and write scope in `agents/registry.json` instead (Root SPEC §9.2 under the D-GOV-41
      candidate).
    - I applied DIRECTIVE §0: App SPEC ranks above `agents/AGENT_*.md`, and D-GOV-41 is not in the
      App GOVERNING map. I therefore did **not** use AUTHORITY_CONFLICT; the rows are routed `R4`.
    - Alternative: a verifier could treat D-GOV-41 as Root GOVERNING. The rows would then be
      AUTHORITY_CONFLICT.
  - **`STATE-1` (AUTHORITY_CONFLICT):**
    - `_CONTEXT.md` restates the PKG-08 decomposition scope, including "daemon-client dispatch".
      D-GOV-43/D-APP-127 retired the daemon without naming this carrier.
    - Alternative: STALE_SPECIFICATION with CARRIER_PROPAGATION, if D-APP-127's topology facts are
      read as addressing all daemon wording.

## 3. Register-defect summary

- **REGISTER-1..3:** the `_REFERENCES.md` MATCH hashes for CONTRACT, SPEC and PRD do not
  reproduce at `00115c719` (pack `REFERENCE_HASHES.csv`, all `Match=NO`).
  - Disposition: REMAINING_STATE_MISMATCH, because each MATCH is snapshot-true (MR-8 iv).
  - All three documents carry the 2026-09-12 D-GOV-43 amendment header.
  - Rows that restate REF-006 MATCH cite REGISTER-3: CLM-004, CLM-009.4, CLM-010, CLM-016,
    CLM-021, CLM-024 and CLM-026.
- **REGISTER-4:** `_REFERENCES.md` reuses REF-009 and REF-010 for two different documents each.
  REF-008 appears only in the SCA table.
- **REGISTER-5:** `_STATUS.md` says Last Updated 2026-09-04, but it has a 2026-09-05 history entry.
- **REGISTER-6:** `Dependencies.csv` DEP-08-01-013 is still an ACTIVE upstream to
  `AGENT_SOFTWARE_DECOMP.md`.
  - That file is absent at the frozen basis, and `_REFERENCES.md` REF-007 now names
    `workflows/software-decomp/WORKFLOW.md`.
  - `_DEPENDENCIES.md` already flags this row as NEEDS_HUMAN_GRAPH_DECISION (2).
- **Not raised as rows:**
  - `_DEPENDENCIES.md` "Declared Upstream/Downstream: TBD": the deliverable does not state whether
    the D-APP-109 edges count as "accepted".
  - MEMORY.md dated evidence entries: these are snapshot records.

## 4. Direction and cause

- **Main CauseTags:**
  - **V3_RELEASE_SCOPE (14).** The App packages the Root v3 four-role bundle, and the SPEC §7
    validator is not applied to it.
    - CONTEXT: `CHIRALITY_V3_APP_ADOPTION_20260909/CORPUS_V21_CANDIDATE.md` and `HANDOFF_STATE.md`.
  - **CARRIER_PROPAGATION (9).** D-APP-109 re-extraction and later corpus changes were not carried
    into the SoW text.
  - **DOC_HYGIENE (6).**
  - **LIFECYCLE_GATE_PENDING (2).** SEC-1 and SEC-2, held in REM-1.
  - **NATIVE_DELEGATION (2).** REQ011 and REQ012.
  - One each: SHELL_REDESIGN, CODEX_SOLE_ENGINE and A2_TOPOLOGY.
- **CAUSE2 secondaries:** V3_RELEASE_SCOPE, CODEX_SOLE_ENGINE, CARRIER_PROPAGATION and
  DOC_HYGIENE, as marked in Notes.
- **GOVERNING rulings cited as explanation:**
  - D-APP-108: seating.
  - D-APP-109: dependency re-extraction.
  - D-APP-110: the SCC holding the mutual DEL-06-03 ↔ DEL-08-01 dependency.
  - D-APP-127: instruction-root:integrity named as the packaged-root check; the Codex/A2 path.
- **NONE_FOUND searches:**
  - REGISTER-4 is the only non-ALIGNED row with `DirectionEvidence = NONE_FOUND`. I searched
    `_DECISIONS/_REGISTER.md` for DEL-08-01, instruction root, registry, AGENT_TYPE and SPEC §7
    (hits only D-APP-55/88/100/127, none relevant). I also searched the CONTEXT run
    `CHIRALITY_V3_APP_ADOPTION_20260909`. There is no record of the duplicate RefIDs.
  - No row uses `UNRECORDED_JUDGMENT`.
- **Carrier map (pack item 5):** all five DEL-08-01 carriers show D-APP-127 `Revised=NO`. That
  supports CARRIER_PROPAGATION on STATE-1.
- **PostReleaseBasis:** NO on every row. None of the cited files appears in `TOUCHED_PATHS.csv`; its
  only runtime `core` path is `session-store.ts`, which no row cites. No blame was needed.
- **Cross-deliverable observations:**
  - DEL-06-03-V3-01 and DEL-08-01-V3-01 depend on each other (D-APP-110 SCC).
  - DEL-02-02-V3-04 (the REM-1 gate) had a read-only slice implemented on 2026-09-06, but there is
    no selection record, and its own gate still reads `NOT_SELECTABLE_UNTIL`.
  - REM-1's write locus names `skills/*/SKILL.md` and "each Agent 1 package". At the frozen basis the
    skills live in `.agents/skills/` and there are two Type 1 roles.

## 5. Method friction

- **Reach for release scripts.** `frontend/scripts/**` are not product entries, and
  `REACHABILITY.csv` has no rows for them. I tagged them `REACH=TEST_ONLY`, because only tests
  import them statically, and noted in Notes that `package.json` `desktop:pack`/`desktop:dist` runs
  them.
  - For a TEST_SUITE deliverable, "judge on the live path" is ambiguous: its obligations are
    test/packaging checks by nature.
  - **Proposal:** add a `REACH=BUILD` note convention, or state that packaging-pipeline scripts are
    the operative path for packaging obligations.
- **Unit-level versus symbol-level reach.** `agent-instruction.ts` is LEGACY_ONLY at module level
  (pack limit 1), and `validateAgentInstructionConformance` is called only from its test. I used the
  module tag and described the symbol reach in Notes.
- **Root governance not in the App map.** D-GOV-41 (the Root four-role format) is not an App
  GOVERNING source, yet the App packages its output. This forces an `R4` rather than an
  AUTHORITY_CONFLICT.
  - **Proposal:** R4 should frame a named question: "App SPEC §7 / K-WRITE-1 versus the D-GOV-41
    role format".

## 6. Effort

- **Files read:** about 30 files or ranges.
  - The deliverable's SoW, `_STATUS`, `_CONTEXT`, `_REFERENCES`, MEMORY, Assessment and the heads
    of `_DEPENDENCIES`/`Dependencies.csv`.
  - The run CONVENTIONS and RUN_BASIS, the pack manifest and the pack CSV rows.
  - App SPEC §1/§7, the CONTRACT K-rows and DIRECTIVE §0.
  - Root SPEC §9, AGENT_WORKFLOW_RUNTIME, K-AGENTS-1 and D-GOV-41 register lines.
  - The D-APP-127 ruling excerpt and the v3 adoption CONTEXT.
  - Code: `agent-instruction.ts`, the verify/prepare instruction-root scripts, `session-manager`,
    `method-catalog`, `native-role-config`, and test-name greps.
- **Not read:** `_SEMANTIC*.md` and `_run_records/**`. They have no indexed units.
- **Budget:** moderate, not tight.
