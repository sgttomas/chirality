# DEL-10-02 Protected Path and Proposal Path Policy: forward-pass notes (R2, PKG-10)

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, frozen basis `00115c719`. Ledger:
`DEL-10-02_claims.csv`, forward pass only. Mid-run rules RUN_BASIS Addenda 4 and 5
(`R4-Q4` and the STALE_SPECIFICATION / REMAINING_STATE_MISMATCH tie-break) were applied
before sealing. No row turns on R4-Q4.

## 1. Census

- **Rows:** 49. That is 28 indexed units (27 CLM plus REM-1) and 5 run-local `REGISTER-n` rows. There are no `STATE-n` rows.
- **Split rate:** 4 of 28 units were split (14%), giving 20 rows:
  - CLM-003: 4 rows (Attributes table rows);
  - CLM-010: 12 rows, one per REQ-001..REQ-012 (the index lists no SubItems for this unit, so this split was a choice);
  - CLM-013: 2 rows (the gap list and AC-001);
  - CLM-019: 2 rows (the records list and VER-001).
- **V-SUBITEMS:** satisfied for AC-001 and VER-001.

| Disposition | All rows | SEE rows | Non-SEE rows |
|---|---:|---:|---:|
| STALE_SPECIFICATION | 24 | 7 | 17 |
| ALIGNED | 10 | 5 | 5 |
| ACCEPTED_DIVERGENCE | 7 | 4 | 3 |
| STALE_VERIFICATION | 3 | 1 | 2 |
| NOT_AUDITABLE | 3 | 0 | 3 |
| AUTHORITY_CONFLICT | 2 | 1 | 1 |
| **Total** | **49** | **18** | **31** |

| ClaimType | Rows | Dispositions |
|---|---:|---|
| REQUIREMENT | 20 | ACCEPTED_DIVERGENCE 7, STALE_SPECIFICATION 6, ALIGNED 5, AUTHORITY_CONFLICT 2 |
| STATE_ASSERTION | 11 | STALE_SPECIFICATION 9, ALIGNED 2 |
| CONTEXT_CLAIM | 7 | STALE_SPECIFICATION 4, NOT_AUDITABLE 3 |
| REGISTER_DEFECT | 5 | STALE_SPECIFICATION 5 |
| ACCEPTANCE | 4 | STALE_VERIFICATION 3, ALIGNED 1 |
| EXCLUSION | 1 | ALIGNED 1 |
| REMAINING_WORK | 1 | ALIGNED 1 |

- **Confidence:** HIGH 24, MEDIUM 23, LOW 2.
- **HumanDecisionNeeded:** NO on 45 rows, R4-Q1 on 4 (CLM-010.9, CLM-010.11, CLM-024, REM-1).
- **Errata:** none yet (forward pass).

## 2. Least-confident rows (with alternative reading)

- **CLM-006 (LOW), STALE_SPECIFICATION.** The References list still says "source warning per REF-006". Alternative reading: the D-APP-56 P40 note (CLM-001) says any older warning wording "is dated drafting history", which would cover this bullet. The row would then be NOT_AUDITABLE.
- **CLM-019.2 VER-001 (LOW), STALE_VERIFICATION.**
  - Why stale: no finalization or parity report was found in the frozen tree. The source markers were removed by design at finalization (`33a29ba8c`), and the production bytes changed afterwards (`0410a15df`, frontmatter pin).
  - Alternative reading: if an external `chirality-sow-finalization/v1` report exists and the frontmatter edit is acceptable, the row is ALIGNED. Run inspection confirms line-content parity (CLM-013.2).
- **CLM-010.9 and CLM-024 (MEDIUM), AUTHORITY_CONFLICT with R4-Q1.**
  - The conflict: App CONTRACT K-DOMAIN-2 (`docs/CONTRACT.md:150`, unamended since 2026-06-21) names "path hooks" as the enforcement surface, and the reliance register's RB-HOOKS row still assigns domain-action fail-closed to legacy `chirality-hooks.ts`. D-GOV-43 bars Chirality from pinning approval or sandbox policy on the live Codex path, and names neither text.
  - Alternative reading: App CONTRACT §1.10 is titled "Future Scope", and Root CONTRACT classes K-DOMAIN-2 as design-time governance (`docs/CONTRACT.md:208`). On that reading there is no present conflict: ACCEPTED_DIVERGENCE with the hook mechanism simply unchosen.
- **CLM-003.4 and its SEE rows (CLM-010.4/.5/.6, CLM-022) (MEDIUM), ACCEPTED_DIVERGENCE.**
  - Alternative reading: DOCUMENTED_UNIMPLEMENTED. Root `docs/CONTRACT.md:158` states K-DOMAIN-2 in the present tense in a non-future section, and two ADOPTED profiles (pec, open_pipe_stress) already declare protected repo paths that no live runtime guard protects.
  - Why I chose ACCEPTED_DIVERGENCE: App PRD §8.17 (`PRD.md:835`) and SPEC §18 (`SPEC.md:1121`) keep "direct protected-path writes/hooks" future and gated, and D-APP-37 rules PKG-10 doc-only.
- **CLM-003.1 / CLM-010.3 (MEDIUM), STALE_SPECIFICATION.** TYPES §11.3 renamed "Proposal path" to "Agent-writable path" and widened it. PRD FR-111 (`PRD.md:844`) still uses the narrower wording. A reader who takes PRD as the controlling source could call the SoW wording ALIGNED with a citation defect only.

## 3. Register-defect summary

- **REGISTER-1: reference hashes.** `_REFERENCES.md` REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD) are recorded MATCH, and none reproduces at `00115c719` (HASH-RECOMPUTE; evidence-pack `REFERENCE_HASHES.csv`). REF-001/004/005/007/009/010 do reproduce. The values were last rewritten by the D-GOV-43 tranche (`23b3879b3`, 2026-09-12).
  - Restated as current by CLM-001/008/014/020 (the P40 notes) and CLM-016; these are SEE rows under tie-break rule 3.
  - Also restated by CLM-011, CLM-019.1 and CLM-023; those rows are dispositioned on other grounds, and the restatement is noted.
- **REGISTER-2: MEMORY.md:7.** The entry still gives "active code implementation is underway" as the 2026-06-16 rationale. D-APP-37 ruled that wording false, but only `_STATUS.md:16` was repaired.
- **REGISTER-3: `_CONTEXT.md:48,52`.** Still reads "Claude Agent SDK / Anthropic remains the first concrete/current path", and cites review of four kit files that no longer exist. Its CauseTag is CODEX_SOLE_ENGINE. No PKG-10 carrier cites D-APP-127 or D-GOV-43 (application map: all NO).
- **REGISTER-4: stale facade path.** `Dependencies.csv:4` (DEP-10-02-003 Notes) and `_DEPENDENCIES.md:33` cite `frontend/packages/harness-contract/src/domain-profile.ts` lines 120-121. That file is now a 2-line deprecated re-export; the declarations live in `projects/chirality-runtime/packages/contracts/src/harness/domain-profile.ts:120-121`. CauseTag FACADE_DEPRECATION, CAUSE2 RUNTIME_EXTRACTION.
- **REGISTER-5: dependency evidence points to deleted files.** `Dependencies.csv` EvidenceFile/SourceRef and `_DEPENDENCIES.md:41-45` point to Datasheet/Specification/Procedure.md, which were deleted by the ScopeOfWork migration (`5ced1fc86`).
- **Stale SoW-internal conflict table:** CLM-026. CT-001/003/004 keep the REF-006 warning conflict open ("Human ruling TBD") while also saying "reconciled under D-APP-38".
- **Examined and not raised:**
  - The `_STATUS.md` header's D-APP-19 authorization basis and Checking Approval SHA are preserved as historical evidence by D-APP-54's own text.
  - The `_DEPENDENCIES.md` Declared Upstream/Downstream sections are TBD by design.
  - MEMORY's REF-007 path entry is a dated log line.

## 4. Direction and cause

- **CauseTags:**

  | CauseTag | Rows |
  |---|---:|
  | PRE_V3_DRIFT | 19 |
  | NONE | 13 |
  | LIFECYCLE_GATE_PENDING | 7 |
  | DOC_HYGIENE | 6 |
  | CODEX_SOLE_ENGINE | 3 |
  | FACADE_DEPRECATION | 1 |

  Secondaries: CAUSE2 CARRIER_PROPAGATION on 11 rows, DOC_HYGIENE on 4, RUNTIME_EXTRACTION on 1.
- **Why PRE_V3_DRIFT dominates:** the stale content is the preserved 2026-05-20 four-document text. Its sources moved before 2026-08-22:
  - the TYPES rename, 2026-06-21 (`fbd8e29fd`, D-APP-45 canon conformance);
  - open_pipe_stress ADOPTED, 2026-06-21 (D-T0-06);
  - the pec registry, D-APP-51 (2026-07-06);
  - the D-APP-58 manifest path, 2026-07-16;
  - the migration and finalization, 2026-07-13/14.

  The D-APP-56 R5 P40/P45 notes (2026-07-12) acknowledged some of this without revising the tables, which is the CARRIER_PROPAGATION secondary.
- **GOVERNING records used in DirectionEvidence:** D-APP-37 (doc-only basis), D-APP-38 (reference model), D-APP-45, D-APP-50 (apply excluded), D-APP-56, D-APP-58, D-APP-89 (facade), D-GOV-16 (ScopeOfWork migration standard), D-GOV-43 and D-APP-127. CONTEXT sources were not needed.
- **NONE_FOUND DirectionEvidence:** none. Searches behind the AUTHORITY_CONFLICT and REM-1 gate readings:
  - `_REGISTER.md` grep for `hook`, `protected`, `DEL-10-02`, `PKG-10`, `ScopeOfWork`, `harness-contract`;
  - the decomposition grep for DEL-10-02, SOW-068 and DEC rows (DEC-006 keeps domain engines future-boundary);
  - `docs/harness/reliance_boundary_register.md` (RB-HOOKS, RB-FILESYSTEM);
  - App and Root CONTRACT K-DOMAIN rows;
  - Root `AGENTS.md` D-GOV-43 text.

  No ruling addresses domain path hooks under Codex, and no decision packet exists for glob syntax or a hook API.
- **Reachability measure (one rule for all rows):**
  - Definitional or "policy shall define/state" text is a documentary claim, judged against the governing text.
  - Behavioural statements about what agents or tools can do are judged on the live path.
  - **Live path:** no domain-profile write guard and no apply surface. `agent1-run-coordinator.ts` `protectedPaths` only excludes Runtime control roots from reads.
  - **Legacy path:** the domain registry and tools and `chirality-hooks.ts` are REACH=LEGACY_ONLY, and even they carry no protected-path rule.
  - **Contract types:** the contract types are REACH=LIVE but inert.
- **Cross-deliverable observations:**
  - PRD §8.17 (`PRD.md:835`) and SPEC §18 call the D-APP-49..52 surfaces "live", but the registry and tools are reachable only on the legacy in-process path.
  - The ADOPTED pec profile protects repo paths (`_DomainEngines/profiles/pec.yaml:34-39`) with no live runtime guard.
  - DEL-10-01, DEL-10-03 and DEL-10-04 will likely meet the same K-DOMAIN-2 / D-GOV-43 question.

## 5. Method friction

- **MR-4 on a four-document concatenation.**
  - **Problem:** the SoW repeats the same normative statements in Attributes, Conditions, Construction, Requirements, Steps, Principles and Trade-offs.
  - **What I did:** the earliest unit carrying the statement holds the disposition (CLM-003.x). Later wholly-restating units are SEE rows. Mixed units (CLM-004, CLM-005, CLM-017) are dispositioned on their distinctive content, with the overlaps named in Notes.
  - **Proposed revision:** allow SEE to point at the canonical numbered REQ row rather than the earliest unit when the earliest unit is a datasheet restatement.
- **Tie-break rule 3 against MR-8(iv).** SoW rows that restate the register MATCH as current now take STALE_SPECIFICATION with `SEE:` to REGISTER-1. The P40 notes cite D-APP-38 but no snapshot version, so rule 3 applied directly.
- **CONTEXT_CLAIM options.** A true, checkable CONTEXT_CLAIM (CLM-002, identification) can only take NOT_AUDITABLE. "Checked and true" and "nothing to check" become indistinguishable. Proposed revision: allow ALIGNED on CONTEXT_CLAIM rows that were actually checked.
- **REACH for the facade file.** `frontend/packages/**` is outside the REACHABILITY.csv roots. REGISTER-4 tags it by its LIVE re-export target, and says so in Notes.

## 6. Effort

- **Files read:** about 30.
  - The whole deliverable folder, except `_SEMANTIC*.md` and the pre-July run records.
  - Targeted line ranges of App PRD/CONTRACT/SPEC/TYPES/PLAN.
  - Root CONTRACT and AGENTS.
  - Six decision records (D-APP-37, 54, 58, 127, plus register rows).
  - Both domain profiles.
  - Six code modules.
  - The git history of the four legacy documents, used for the parity script.
- **Context budget:** adequate, not tight.
