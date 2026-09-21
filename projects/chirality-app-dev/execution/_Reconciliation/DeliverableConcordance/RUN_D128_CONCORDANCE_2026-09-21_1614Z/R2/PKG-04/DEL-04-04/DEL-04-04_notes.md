# DEL-04-04 PersonaComposer from Instruction Root — forward-pass notes

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, R2 wave 1, PKG-04. Forward pass only.
Sealed ledger `DEL-04-04_claims.csv`: SHA-256
`d077fd3845dd72f192ad773113ca9d0cbc491cc6e29ae5a89213d89c0e5bba85`. The validator reports
`RULES errors none | warnings none` and `RESULT PASS errors=0 warnings=0`.

## 1. Census

- **Rows:** 50 data rows covering all 34 indexed units (SEC-1..3, CLM-001..030, REM-1).
  There are also 3 run-local rows: STATE-1, REGISTER-1 and REGISTER-2.
- **By ClaimType:**

  | ClaimType | Rows |
  |---|---|
  | REQUIREMENT | 23 |
  | STATE_ASSERTION | 12 |
  | CONTEXT_CLAIM | 7 |
  | ACCEPTANCE | 5 |
  | REGISTER_DEFECT | 2 |
  | REMAINING_WORK | 1 |

- **By Disposition:**

  | Disposition | Rows |
  |---|---|
  | IMPLEMENTED_DIFFERENTLY | 11 |
  | STALE_SPECIFICATION | 10 |
  | ALIGNED | 9 |
  | PARTIALLY_IMPLEMENTED | 7 |
  | REMAINING_STATE_MISMATCH | 6 |
  | NOT_AUDITABLE | 4 |
  | DOCUMENTED_UNIMPLEMENTED | 2 |
  | STALE_VERIFICATION | 1 |

- **Split rate:** 3 of 34 units were split.
  - CLM-010 has 12 rows, one for each PC-REQ-001..012. The requirements take different
    dispositions, and each row names its PC-REQ ID in Notes.
  - CLM-014 has a base row plus `.1` for AC-001.
  - CLM-021 has a base row plus `.1` for VER-001.
  - For CLM-014 and CLM-021, the base row carries the repeated P45 note as a SEE row.
- **SEE rows (MR-4), counted separately: 10.**

  | SEE target | SEE rows |
  |---|---|
  | CLM-001 (the repeated D-APP-56 P40 "REF-006 MATCH" note) | CLM-008, CLM-015, CLM-022, CLM-029 |
  | CLM-007 (the repeated P45 note) | CLM-014, CLM-021, CLM-030 |
  | CLM-009 (scope/purpose) | CLM-016, CLM-023 |
  | CLM-012 (verification) | CLM-019 |

  Without the SEE rows there are 40 distinct dispositioned rows.
- **HumanDecisionNeeded other than NO: 21 rows.**

  | Value | Rows |
  |---|---|
  | R4-Q1 | 16 |
  | D-APP-119; R4-Q1 | 2 |
  | R4 | 2 |
  | D-APP-119 | 1 |

- There is no errata file yet, so only the sealed figures are reported.

## 2. Least-confident rows

- **CLM-010.7 (PC-REQ-007, professional-boundary reminders), PARTIALLY_IMPLEMENTED / LOW.**
  - The live Runtime path injects the user-editable product `AGENTS.md` and the role file.
  - The composer adds no fixed reminder of its own. The explicit reminder exists only in the
    LEGACY_ONLY `persona-manager.ts:93`.
  - Alternative reading: the role files under `agents/` may carry an equivalent reminder,
    which would make this row ALIGNED in substance. The CauseTag could also be read as
    CODEX_SOLE_ENGINE rather than UNRECORDED_JUDGMENT.
- **CLM-010.11 (PC-REQ-011, unknown option keys warn), IMPLEMENTED_DIFFERENTLY / LOW.**
  - The live Codex turn envelope rejects unknown keys (`delegated-runtime.ts:103-107`).
  - Warn-and-ignore exists only in the LEGACY_ONLY `options.ts`.
  - Alternative reading: the envelope is internal, not user runtime options. A live
    user-option normaliser elsewhere may warn and ignore, which would make this ALIGNED.
- **REM-1 (DEL-04-04-V3-01), DOCUMENTED_UNIMPLEMENTED / LOW, MechanicallyUnblocked NO.**
  - Gate status:
    - DEL-07-03-V3-01 has landed (PR #733, recorded on the DEL-07-03 `_STATUS` on 2026-09-06).
    - DEL-07-01-V3-01 was "selection evaluated" on 2026-09-05, then held on D-APP-119
      (AWAITING_RULING).
  - Alternative reading 1: the literal gate "DEL-07-01-V3-01 selected" is met, which would
    make the gate YES. The NO rests on the pending pins named in `Depends`.
  - Alternative reading 2: the seated write locus (`persona-manager.ts`) became LEGACY_ONLY
    under D-GOV-43, so REMAINING_STATE_MISMATCH would also fit.

## 3. Register-defect summary

- **REGISTER-1.** In `_REFERENCES.md`, REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD)
  record MATCH, but none reproduces at `00115c719` (`REFERENCE_HASHES.csv`, Match=NO).
  - I recomputed DIRECTIVE, TYPES and PLAN myself; they still match their recorded hashes.
  - The following SoW rows restate the MATCH claim and cite REGISTER-1: CLM-001/008/015/022/029
    (the P40 note), CLM-006 (the references table) and CLM-028 (conflict table CT-001).
- **REGISTER-2.** Two defects in the reference records:
  - In `_REFERENCES.md`, REF-009 and REF-010 are each used twice: once for the corpus rows
    (lines 14-15) and once for the SCA-APP-010 authority rows (lines 22-23).
  - SoW CLM-006 names REF-007 as `AGENT_SOFTWARE_DECOMP.md`, but `_REFERENCES.md` gives
    `workflows/software-decomp/WORKFLOW.md`.
- **STATE-1 (a carrier finding, not a register row).** `_CONTEXT.md` still says Claude Agent
  SDK / Anthropic is the current path.
  - It still lists packaged-daemon credential-boundary participation in the package scope.
  - All five DEL-04-04 carriers show `Revised=NO` in the D-APP-127 application map.

## 4. Direction and cause

- **Main CauseTags:**

  | CauseTag | Rows |
  |---|---|
  | CODEX_SOLE_ENGINE | 14 |
  | DOC_HYGIENE | 9 |
  | CARRIER_PROPAGATION | 4 |
  | LIFECYCLE_GATE_PENDING | 3 |
  | RUNTIME_EXTRACTION | 3 |
  | PRE_V3_DRIFT | 2 |
  | V3_RELEASE_SCOPE | 1 |
  | UNRECORDED_JUDGMENT | 1 |

- **Secondary causes:**
  - `CAUSE2:RUNTIME_EXTRACTION` and `CAUSE2:CODEX_SOLE_ENGINE` pair up across the
    composition rows.
  - `CAUSE2:PRE_V3_DRIFT` on CLM-004.
  - `CAUSE2:CARRIER_PROPAGATION` on STATE-1.
- **Core finding.**
  - The SoW's PersonaComposer (`frontend/src/lib/harness/persona-manager.ts`) is LEGACY_ONLY.
  - Live prompt composition is the Runtime selected-context / instruction-basis path. It
    starts at `runtime-method-service.ts:532-620`. It supplies root `AGENTS.md`, project
    `AGENTS.md`, role, product library and method bodies, with a sha256 for each entry.
  - Those entries are rendered into Codex `developerInstructions` by
    `delegated-engine-adapter.ts:37` and passed through `codex-supervisor.ts`.
  - The live boot fingerprint (`runtime-service.ts:331`) hashes the manifest, persona, mode
    and runtime fingerprint. It does not include persona or governance content hashes;
    content identity is carried by the instruction-basis hash instead.
  - There is no organisation layer and no delimited roadmap block on any path. The
    governed-workflow file contract is TEST_ONLY.
- **R4-Q1 applies** because the seated write locus and the verification targets still name
  the legacy module.
- **Persona default conflict (CLM-004, R4).** SPEC §13.1 (GOVERNING) says the default persona
  is `WORKING_ITEMS`. Both the SoW and the live resolver use `HELP_HUMAN`. I found no
  amendment.
- **Alias conflict (CLM-010.5, R4).** TYPES §3.4 still maps `ORCHESTRATE->PROJECT_SETUP` and
  `DEPENDENCIES->EVALUATION`. The live resolver is bounded to the four-role registry and maps
  only `HELP` and `AGENTS`.
- **CONTEXT and GOV records used:**
  - GOV:
    - D-GOV-43 / D-APP-127: the App PRD Codex-only preamble and the Root `AGENTS.md`
      additive-instruction clause.
    - D-APP-108: seating.
    - D-APP-109: dependency re-extraction.
    - D-APP-38: the reference model.
  - CTX:
    - `AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md:215-218`:
      `developerInstructions` carry the role plus selected workflow context.
    - `AgentRuns/APP_V3_INTEGRATION_2026-09-06/decisions/APP_CAPABILITY_DEPENDENCIES.md:16`:
      layered-root composition is unproven; D119 is pending.
    - `AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/CUSTODY_SUPPLEMENT_APP_GOVERNANCE_v1.md:17-24`:
      the four-role, three-direct-entry model.
- **Searches behind each NONE_FOUND DirectionEvidence** (rows CLM-003, CLM-010.7, CLM-010.11,
  CLM-013 and REGISTER-2).
  - I grepped `_DECISIONS/_REGISTER.md` and the §5 CONTEXT sources (`AgentRuns/APP_V3_*`,
    `CHIRALITY_V3_APP_ADOPTION_20260909`, `APPDEV_V3_NODE_*`, `plans/steers/chirality_app_v3_*`).
  - Terms searched:
    - DEL-04-04, PersonaComposer, persona-manager, organisation layer, Q14;
    - ORCHESTRATOR, professional-boundary, "unknown option" / FR-024;
    - SOW-017, REF-009 / REF-010, "integration note".
  - The only hits were copies of this deliverable's own SoW and Dependencies inside the
    integration run's decision sources, plus the D-APP-55 register row. None explains the
    divergence.
  - In the pack's DECISION_HITS, the only register or ruling hit for DEL-04-04 is D-APP-63,
    which is about a DEP-04-01-012 referral and does not bear on these claims.

## 5. Method friction

- **Split parents.** When a unit holds a single sub-item (CLM-014 AC-001, CLM-021 VER-001) and
  also repeats a note that another unit already dispositioned, the rules do not say whether to
  write a base SEE row plus `.1`, or one combined row. I used base + `.1`.
  - Proposal: state that a base row and its `.n` rows may coexist.
- **Gate literalism.** `NOT_SELECTABLE_UNTIL: … DEL-07-01-V3-01 selected` can be read literally
  as met, since the item was selected and evaluated, even though its output (the pins) is
  held. That makes the result depend on the reading.
  - Proposal: judge MR-2 / MR-6 on the gate text together with the `Depends` line, and name
    that pairing explicitly.
- **Live-path judgment for AssessmentEvidence.** INSP-03 PASS rows that rested on the
  now-LEGACY_ONLY module are marked OVERTAKEN where the live path diverges. They are marked
  STILL CURRENT where the live path independently holds (PC-REQ-002, -003, -008, -009, -012).
  - Proposal: confirm that this per-row split is the intended reading of MR-1.

## 6. Effort

- **Files read:** about 30.
  - Deliverable: SoW, `_STATUS`, `_CONTEXT`, MEMORY, `_REFERENCES`, the Assessment, and
    Dependencies (by script).
  - Code, in ranges: `persona-manager`, `persona-resolution`, `product-instructions`,
    `governed-workflow`, `runtime-method-service`, `product-native-role-config`,
    `delegated-engine-adapter`, `delegated-runtime`, `runtime-service`, and
    `codex-supervisor` (one line).
  - Governing and decision sources: sections of SPEC, TYPES, PRD and DIRECTIVE; register rows;
    two CONTEXT records; and the DEL-07-01 and DEL-07-03 `_STATUS` files.
- I did not read `_SEMANTIC*.md`, `_DEPENDENCIES.md` or `_run_records`, and I did not open
  PREGATHER, which does not exist for this deliverable.
- The context budget was adequate, not tight.
