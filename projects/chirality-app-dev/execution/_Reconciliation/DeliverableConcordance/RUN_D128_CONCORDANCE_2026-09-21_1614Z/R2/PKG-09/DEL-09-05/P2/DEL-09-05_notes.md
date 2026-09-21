# DEL-09-05 — R2 forward pass notes, part P2

Part P2 covers CLM-017 to CLM-033 (SoW Praxeology and Axiology), REM-1 to REM-3 (`_STATUS.md` Remaining)
and the run-local rows REGISTER-51 to REGISTER-56 and STATE-51 to STATE-54. Frozen basis `00115c719`.
The ledger is `DEL-09-05_claims.csv`. Validator: `RESULT PASS errors=0 warnings=0`, run with
`--index _index_P2.csv`.

## 1. Census

32 rows: 20 indexed units written as 21 rows (CLM-023 split `.1`/`.2`/`.3`), plus 6 REGISTER rows and
4 STATE rows.

| Disposition | Rows | of which SEE |
|---|---:|---:|
| STALE_SPECIFICATION | 11 | 3 (CLM-024, CLM-031, REGISTER-56 → REGISTER-51) |
| REMAINING_STATE_MISMATCH | 6 | 1 (CLM-032 → CLM-019) |
| ALIGNED | 6 | 1 (CLM-033 → CLM-023.3) |
| NOT_AUDITABLE | 5 | 0 |
| PARTIALLY_IMPLEMENTED | 3 | 0 |
| AUTHORITY_CONFLICT | 1 | 0 |

| ClaimType | Rows |
|---|---:|
| STATE_ASSERTION | 10 |
| CONTEXT_CLAIM | 6 |
| REGISTER_DEFECT | 6 |
| REQUIREMENT | 4 |
| ACCEPTANCE | 3 |
| REMAINING_WORK | 3 |

- **SEE rows:** 5, counted separately (MR-4). Without them the census has 27 distinct dispositions.
- **Split rate:** 1 of 20 indexed units was split (CLM-023, which lists VER-001 and VER-002). `.1` is
  VER-001, `.2` is VER-002, and `.3` is the unit's dated D-APP-56 P45 reconciliation note.
- **HumanDecisionNeeded:** `R4` on 5 rows (CLM-020, CLM-023.2, CLM-026, CLM-027 and REM-2), all tied to
  the release-target and release-act question (K-RELEASE-1 and F-APP-2 against the D-GOV-43
  signed/notarized candidate; done-declaration Q-02). No row turns on R4-Q1 through R4-Q6. No cited code is
  LEGACY_ONLY, and R4-Q6's DIRECTIVE/K-PERM cluster is not in scope for these rows.
- **Confidence:** 16 HIGH, 16 MEDIUM, 0 LOW.
- No errata file (pass 1).

## 2. Least-confident rows

No row is LOW. The MEDIUM rows with the most plausible alternative readings are listed here.

- **CLM-026 (AUTHORITY_CONFLICT, R4).** Alternative reading: STALE_SPECIFICATION under MR-11. On this
  reading, CONTRACT:17 already reads K-RELEASE-1 with D-GOV-43 and names bundle signing and notarization;
  PRD §12.8 and SPEC §19.4 were amended; and D-APP-127 names DEL-09-05 as revised, which together would
  resolve the question. I kept AUTHORITY_CONFLICT for three reasons: the K-RELEASE-1 row itself is
  unamended; D-APP-97's F-APP-2 fence on signing, notarization and distribution is not named by D-APP-127;
  and D-APP-127's own Boundary authorizes no release (see Q-02).
- **CLM-020 (STALE_SPECIFICATION, R4).** Alternative: PARTIALLY_IMPLEMENTED, if the procedure is read as a
  requirement on the product, since the code covers steps 2 and 5 and the Codex-pin check. I chose the
  text repair because the missing Codex pin and S-6/S-8 checks and the signing posture are gaps in the
  SoW's wording against amended PRD §12.8 and SPEC §19.4. The code already has the surfaces.
- **REM-2 (REMAINING_STATE_MISMATCH, MechanicallyUnblocked YES).** Alternative: ALIGNED with
  MechanicallyUnblocked NO. On that reading the deliverable-local execution record the item asks for still
  does not exist, and "owner directs the consolidated signed build" is recorded only by agents. I chose the
  mismatch because the gate text ("NOT_SELECTABLE_UNTIL …") is contradicted: independent review PASS, the
  signed consolidated build (2026-09-12), and notarization plus publication of v3.0.0 (2026-09-13) are all
  recorded on App surfaces.
- **CLM-019 / CLM-028 / CLM-032 (REMAINING_STATE_MISMATCH).** Alternative: STALE_SPECIFICATION. Stale TBDs
  for a value that is now known fit either verdict. I applied tie-break rule 2(b) literally ("a TBD
  placeholder") and recorded `ALSO:STALE_SPECIFICATION`.
- **CLM-023.3 / CLM-033 (ALIGNED).** The claim rests on repo-root workflow content, which is out of root. I
  judged it on the in-root contract pins (`contract-pins.manifest.ts:70-116`, which passed in the gate
  transcript). The artifact name `harness-validation-summaries` cannot be verified in root.
- **CLM-021 (PARTIALLY_IMPLEMENTED, PRE_V3_DRIFT).** Alternative CauseTag: LIFECYCLE_GATE_PENDING, which
  is recorded as `CAUSE2:`.

## 3. Register-defect summary

- **REGISTER-51:** the `_REFERENCES.md` hash drift. REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD)
  are recorded as MATCH, but none reproduces at the frozen basis (`HASH-RECOMPUTE@00115c719`,
  `REFERENCE_HASHES.csv`). By my own recompute, REF-001, REF-004 and REF-005 (DIRECTIVE, TYPES, PLAN) do
  reproduce. REF-007, REF-009 and REF-010 (Root workflows) were not recomputed. Three rows restate the
  drift with `SEE:`: CLM-024 (SoW P40 note), CLM-031 (the stale conflict table) and REGISTER-56
  (`_DEPENDENCIES.md:70,126`).
- **REGISTER-52:** `Dependencies.csv` DEP-09-05-015 keeps G6a as an ACTIVE constraint, and
  `_DEPENDENCIES.md` handoff notes tell consumers to treat it as a current factual row. G6a was retired
  under D-APP-127, so this is STALE_SPECIFICATION (`MOOT:D-APP-127`).
- **REGISTER-53:** DEP-09-05-011 still has CI workflow path TBD, and the UNRESOLVED_TBD warnings remain,
  although the executed workflow is recorded. This is bookkeeping lag (REMAINING_STATE_MISMATCH).
- **REGISTER-54:** the DEP-09-05-008 EvidenceQuote cites `frontend/dist/Chirality-0.1.0-arm64.dmg` as SoW
  text, but that text is no longer in the SoW.
- **REGISTER-55:** `_CONTEXT.md:48` still calls Claude Agent SDK/Anthropic "the first concrete/current
  path". Codex is the sole engine (CONTRACT:17), and `_CONTEXT.md` is a `NO` carrier in the D-APP-127 map.
- **Seen, not given a row:**
  - `_DEPENDENCIES.md` Run Notes (lines 61-62 and 81-82) carry machine-specific absolute paths as run
    provenance (hygiene only).
  - DEP-09-05-014 restates K-RELEASE-1. It is covered by the CLM-026 conflict and not recoded as stale.
  - `_STATUS.md` "Last Updated 2026-09-12" agrees with the file's last edit (STATE-51 ALIGNED). The lag
    comes from later release events, which REM-2 and REM-3 carry.

## 4. Direction and cause

- **CauseTags:** DOC_HYGIENE 9, CARRIER_PROPAGATION 6, CODEX_SOLE_ENGINE 2, LIFECYCLE_GATE_PENDING 2,
  PRE_V3_DRIFT 1, V3_RELEASE_SCOPE 1, NONE 11.
- **CAUSE2 secondaries:** CARRIER_PROPAGATION (CLM-019, CLM-022, CLM-023.1, CLM-026, REGISTER-55),
  CODEX_SOLE_ENGINE (CLM-020), LIFECYCLE_GATE_PENDING (CLM-021), V3_RELEASE_SCOPE (CLM-023.2), DOC_HYGIENE
  (CLM-027) and PRE_V3_DRIFT (CLM-028).
- **Main mechanism.** The D-APP-127 application (2026-09-12) revised only `_STATUS.md`. The D-APP-127 map
  shows ScopeOfWork, `_CONTEXT.md`, `Dependencies.csv` and `_REFERENCES.md` as `NO`. As a result:
  - the SoW still states the unsigned target and G6a;
  - the register keeps G6a active;
  - the Remaining gates were not advanced when the release acts happened on 2026-09-12 and 2026-09-13.
- **GOVERNING records used:**
  - D-APP-127 (application record);
  - D-APP-56 (R5 P45 UPD-146/147: executed CI moved to the repo root);
  - D-APP-38 (reference-integrity model);
  - D-APP-97 (F-APP-2 fence);
  - App CONTRACT:17 and :134/:138, PRD §12.8, SPEC §19.4, BUILD_AND_RELEASE §8.1.
- **CONTEXT records used:**
  - `AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/{PACKAGING_PROCEDURE,BUILD_EVIDENCE_20260912,INDEPENDENT_REVIEW,NATIVE_CHECKLIST}.md`;
  - `AgentRuns/APP_V3_USER_JOURNEYS_20260912/RUN_LOG.md`, the agent-recorded signed 3.0.0 builds (lines
    157-189), direct notarization on owner direction (231-244) and v3.0.0 publication (247-251);
  - `AgentRuns/APPDEV_V3_NODE_B_2026-09-03/instances/B2_REVIEWER/REVIEW_03_*`;
  - `AgentRuns/APPDEV_UNSIGNED_RELEASE_WORKFLOW_2026-08-19/MANAGER_RETURN.md`.
  - Done-declaration Q-02 is cited in Notes only.
- **NONE_FOUND:** one row, REGISTER-54. I searched `_REGISTER.md` (grep "0.1.0": 0 hits; DEL-09-05: 1 hit,
  the D-APP-55 row) and the CONTEXT AgentRuns (grep "0.1.0-arm64"). The only AgentRuns hits are the
  `CODEX_MVP_PACKAGING_20260910/{amendment-candidate,carrier-propagation}.patch` candidate patches and an
  APP_LOOP_SHELL cited-bytes file. None records a direction on the DEP-09-05-008 quote. The CauseTag is
  DOC_HYGIENE, not UNRECORDED_JUDGMENT, because a vocabulary mechanism fits. (The sealed row's Notes
  summarize this search more briefly.)
- **REACH.** Build and packaging scripts are tagged `REACH=LIVE` when a `package.json` script invokes them
  (`desktop:dist`, `validate:release-quality`, `sbom:generate`, `verify:version-identity`,
  `proof:network-policy`). Notes flag the scripts that are **not chained** from `desktop:dist` or CI (secret
  scan, network proof, SBOM). Signing in `pack-electron.mjs:79-94` is DISABLED_BY_DEFAULT: the build is
  unsigned unless `CHIRALITY_SIGNING_IDENTITY_SHA1` is set. Test-file pins are `REACH=TEST_ONLY`. The in-root
  workflow file is not code (no tag) and does not execute. PostReleaseBasis is `NO` on every row:
  `TOUCHED_PATHS.csv` lists no `projects/chirality-app-dev/**` path, and no Runtime path is cited.

## 5. Method friction

- **Composite SoW units.** CLM-020, CLM-026 and CLM-027 each mix elements that would take different
  dispositions: stale Codex checks, the release-target authority conflict, stale MATCH, and stale TBDs. The
  splitting rule allows a split only for REQ/AC/VER items or tables, so I dispositioned each unit by its
  operative element and named the others in Notes. Proposal: allow `.n` splits for a list of independently
  dispositionable procedure steps.
- **MR-4 across split parts.** CLM-024 restates the same P40 note that P1's CLM-001 carries. `SEE:` must
  resolve inside my part ledger, so CLM-024 points to REGISTER-51 (P2-owned) rather than CLM-001. The
  manager may harmonize at merge.
- **Out-of-root executed workflow.** The executed CI (`.github/workflows/harness-premerge.yml`) and the
  unsigned-artifact workflow (`desktop-release-template.yml`) are out of root. The in-root copy of
  `harness-premerge.yml` is non-executing and diverges: it has no instruction-root step, it injects
  `ANTHROPIC_API_KEY`, and it uploads the section8 summary only. Several rows can be judged only through
  the in-root contract-pin manifest. Proposal: a manager-built pin extract (pins → claimed workflow
  content) in the evidence pack.
- **Tie-break 2(b) with "TBD placeholder" in SoW text.** The rule names register bookkeeping but says the
  same rule applies to SoW text. I read stale SoW TBDs as 2(b). A one-line clarification would help.

## 6. Effort

About 40 files and file ranges read:
- all deliverable carriers;
- D-APP-127, D-APP-97 and the register rows;
- the CONTRACT/PRD/SPEC/BUILD_AND_RELEASE excerpts;
- about 12 frontend scripts and tests (line ranges);
- 6 AgentRuns records;
- the evidence pack, PREGATHER and the gate transcript.

The context budget was adequate, not tight. Nothing was read under Root `execution/`, repository-root
`.github/**`, `projects/chirality-runtime/execution/**`, `R0_CALIBRATION/**` or other R2 folders,
including P1.

## Coverage gaps

- **SoW `## Output and Evaluation Matrix` (ScopeOfWork.md:568-573)** is not an indexed unit and has no
  forward row in P2. It still says "WP-11 execution record only after G6a" for OUT-002, the same stale G6a
  premise as CLM-023.2 and REGISTER-52.
- **Work delivered but undocumented in the deliverable:**
  - the consolidated signed build (2026-09-12);
  - the signed 3.0.0 builds, notarization and stapling, and the public v3.0.0 release (2026-09-13);
  - the v3.0.1 maintenance version (`cf4653526`).
  All are recorded only in AgentRuns or Git, and no DEL-09-05 carrier or Remaining item records them. REM-2
  and REM-3 own the nearest rows. v3.0.1 has no release record on any App surface I searched.
- **Retired LaunchAgent proof steps in the out-of-root workflow.** `desktop-release-workflow.test.ts:16-19`
  states that the out-of-root `desktop-release-template.yml` still carries retired LaunchAgent RunAtLoad
  proof steps whose script is gone. No DEL-09-05 carrier or Remaining item owns that workflow edit. P1's
  SEC-1 ("existing CI qualification stop") may be the nearer owner.
