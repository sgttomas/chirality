# DEL-10-01 — R2 forward-pass notes (RUN_D128, PKG-10)

Frozen basis `00115c719`. Forward pass only; the reverse pass has not been run. RUN_BASIS Addenda 4 (R4-Q4)
and 5 (STALE_SPECIFICATION / REMAINING_STATE_MISMATCH tie-break) were applied before sealing, as the
manager directed mid-run.

## 1. Census

- **Rows:** 56. That is 52 indexed-unit rows covering all 32 indexed units (30 CLM, 2 REM), plus 4 run-local
  rows (REGISTER-1..3, STATE-1).
- **Split rate:** 6 of 32 units split (19%), into 26 rows: CLM-003 (2), CLM-004 (6, table rows), CLM-012 (11,
  REQ-001..011), CLM-016 (2, ownership + AC-001), CLM-022 (2, records + VER-001) and CLM-025 (3, table rows).
  Both SubItems units are covered: CLM-016 AC-001 → .2 and CLM-022 VER-001 → .2.
- **SEE rows (MR-4), counted separately:** 11. They are CLM-004.2, CLM-012.2/.3/.4/.7/.10/.11, CLM-013 (→ REGISTER-1),
  CLM-025.2/.3 and CLM-030.

| Disposition | All rows | Excluding SEE |
|---|---:|---:|
| ALIGNED | 21 | 17 |
| STALE_SPECIFICATION | 14 | 13 |
| NOT_AUDITABLE | 9 | 9 |
| ACCEPTED_DIVERGENCE | 6 | 2 |
| PARTIALLY_IMPLEMENTED | 3 | 1 |
| IMPLEMENTED_DIFFERENTLY | 1 | 1 |
| AUTHORITY_CONFLICT | 1 | 1 |
| REMAINING_STATE_MISMATCH | 1 | 1 |

| ClaimType | Dispositions |
|---|---|
| REQUIREMENT (29) | ALIGNED 16, ACCEPTED_DIVERGENCE 6, STALE_SPECIFICATION 5, PARTIALLY_IMPLEMENTED 1, IMPLEMENTED_DIFFERENTLY 1 |
| CONTEXT_CLAIM (11) | NOT_AUDITABLE 9, STALE_SPECIFICATION 2 |
| STATE_ASSERTION (9) | STALE_SPECIFICATION 5, ALIGNED 2, PARTIALLY_IMPLEMENTED 2 |
| REGISTER_DEFECT (3) | STALE_SPECIFICATION 2, REMAINING_STATE_MISMATCH 1 |
| ACCEPTANCE (2) | ALIGNED 2 |
| REMAINING_WORK (2) | ALIGNED 1, AUTHORITY_CONFLICT 1 |

- **Confidence:** 32 HIGH, 23 MEDIUM, 1 LOW.
- **HumanDecisionNeeded:** 49 NO; R4-Q1 ×5 (one combined as `D-APP-118; R4-Q1`); R4-Q4 ×1; R4 ×1.
- No errata file exists yet.

## 2. Least-confident rows

- **CLM-022.2 (VER-001), LOW, ALIGNED.**
  - The deliverable folder has no source-marker map or parity report.
  - Parity evidence (30/30 checks) exists in the Root SoW-migration run:
    `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/.../VERIFY-DEL-10-01/CHECKS.md:6`.
    I read it while searching for the report. It is outside the brief's reading boundary ("any other project's
    execution tree"); see §5.
  - **Alternative reading:** judged on App surfaces only, VER-001 would be `DOCUMENTED_UNIMPLEMENTED`
    (PRE_V3_DRIFT). The finalize commit `2282a535b` also rewrote the SoW after that check.
- **CLM-004.1 / CLM-004.2 / CLM-012.2, MEDIUM, PARTIALLY_IMPLEMENTED.**
  - These rows turn on R4-Q1. Judged on the live Codex path, only the inert type module is present; the registry
    and every domain MCP tool are LEGACY_ONLY.
  - **Alternative reading:** if R4-Q1 treats the retained path as live compatibility, the "live" claims are
    ALIGNED.
  - I did not raise AUTHORITY_CONFLICT. CONTRACT's Codex-only MVP preamble outranks SPEC §18 and PLAN R7 in the
    DIRECTIVE §0 authority order, and it reads Claude/Pi descriptions as compatibility history, so the order
    resolves the conflict.
- **CLM-016.1, MEDIUM, IMPLEMENTED_DIFFERENTLY.**
  - The mirror moved to the Runtime contracts package (D-APP-73). The App keeps only a deprecated facade
    (D-APP-89; retirement is D-APP-118, AWAITING_RULING).
  - **Alternative reading:** ALIGNED at module level, if ownership simply follows the file through the facade.
- **CLM-004.4 / CLM-004.5 (and their SEE rows), MEDIUM, ACCEPTED_DIVERGENCE.**
  - K-DOMAIN-2 and K-DOMAIN-3 are present-tense in CONTRACT §1.10, but the section is headed "Future Scope".
    D-APP-49 ruled "no protected-path hooks" and D-APP-50 excluded apply outright.
  - **Alternative reading:** DOCUMENTED_UNIMPLEMENTED, if a present-tense invariant under a future-scope heading
    must be enforced now. In particular, nothing on the Codex path stops an agent writing `_DomainEngines/**`.
- **REM-1, MEDIUM, AUTHORITY_CONFLICT (R4).**
  - DIRECTIVE §8 and decomposition DEC-019 (both unamended) keep the shared per-user daemon with project clients.
  - D-GOV-43 retired the daemon path "on the App MVP Codex path" without naming DEC-019 or this item.
  - **Alternative reading:** ALIGNED as an open cross-project item, with MechanicallyUnblocked UNKNOWN, if PEC
    client registration is read as outside the App MVP path.
- **REM-2, MEDIUM, ALIGNED.**
  - The item is correctly open: no register row after D-APP-58 widens the domain surface.
  - Its "read-only" gloss understates D-APP-52's write-graded pec propose/refresh.
  - **Alternative reading:** STALE_SPECIFICATION on that gloss.
- **CLM-012.5 / CLM-012.6, MEDIUM, ALIGNED.**
  - "Integrated workflows require ADOPTED" and "do not skip levels" are not enforced in code. They hold only
    because no integrated workflow runs on the live path.
  - The legacy registry gates on ruled registration (D-APP-51), not on `profile_status`.

## 3. Register-defect summary

- **REGISTER-1 (STALE_SPECIFICATION):** `_REFERENCES.md` REF-002, REF-003 and REF-006 are recorded as MATCH, but
  CONTRACT, SPEC and PRD all fail HASH-RECOMPUTE@00115c719. All three changed again on 2026-09-12, after the
  `23b3879b3` v23 re-hash. DIRECTIVE, TYPES, PLAN and the REF-007..012 workflow hashes do reproduce (I recomputed
  them). CLM-013 restates "reconciled by D-APP-38" and points here with SEE.
- **REGISTER-2 (REMAINING_STATE_MISMATCH; ALSO:STALE_SPECIFICATION):** two `_STATUS.md` header fields lag.
  - The "P06 Record" line still says the concordance Remaining item stays open for R6; R6 removed it (line 30).
  - "Authorization Basis: D-APP-19 Option D" predates D-APP-54's supersession.
- **REGISTER-3 (STALE_SPECIFICATION; ALSO:REMAINING_STATE_MISMATCH):** `_DEPENDENCIES.md` still says "TBD - no
  accepted dependency edges have been extracted yet" and "do not compute … until Dependencies.csv exists", while
  the register holds 3 SATISFIED anchors.
- **Also noted, not raised as a row:** Dependencies.csv DEP-10-01-003 cites the App `harness-contract` path as the
  "inert type mirror"; that path is now a deprecated facade. The note is dated 2026-07-10 and is left as history.
- **Stale references in SoW text:**
  - REF-008 has been `workflows/domain-engine/WORKFLOW.md` since `9b005c23a` (2026-09-09). The profile shape now
    sits in REF-011. The SoW still equates REF-008 with `agents/AGENT_DOMAIN_ENGINE.md` throughout; this is
    disposed once, at CLM-019 (R4-Q4).
  - The deleted four-document set (`d19ee4d30`, 2026-07-13) is still cited as present in CLM-014, CLM-015,
    CLM-020, CLM-021 and CLM-022.1. D-APP-68 item 2 directs annotating such citations, but that repair was not
    applied to this deliverable.

## 4. Direction and cause

- **CauseTags:** PRE_V3_DRIFT 9, LIFECYCLE_GATE_PENDING 6, CODEX_SOLE_ENGINE 4, DOC_HYGIENE 4,
  RUNTIME_EXTRACTION 1, CARRIER_PROPAGATION 1, A2_TOPOLOGY 1. No UNRECORDED_JUDGMENT and no OTHER tags.
- **CAUSE2 secondaries:**
  - CARRIER_PROPAGATION on CLM-004.1, CLM-013, CLM-020 and STATE-1;
  - DOC_HYGIENE on CLM-019;
  - CODEX_SOLE_ENGINE on CLM-016.1.
- **GOVERNING rulings cited as explanations:**
  - D-APP-49 (types only, no hooks), D-APP-50 (apply excluded), D-APP-51 (registration-as-gate) and D-APP-52;
  - D-APP-53 and D-APP-54;
  - D-APP-56 (P27 ownership; UPD-148);
  - D-APP-68 items 1–2 (migrated CLM blocks are live; annotate dangling four-document citations), with D-GOV-16;
  - D-APP-73 and D-APP-89 (extraction and facade);
  - D-GOV-43 (Codex sole engine, A2).
- **CONTEXT records used:**
  - `execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/CORPUS_V21_CANDIDATE.md` for the
    REF-008 remap (CLM-013, CLM-019);
  - the CONTRACT Codex-only MVP preamble. It is a GOVERNING text, cited in CLM-004.1 as `CTX:` alongside
    `GOV:D-GOV-43` for locator clarity.
- **Searches behind NONE_FOUND values:**
  - REGISTER-1 DirectionEvidence: grepped `_REGISTER.md` for corpus v23+/re-hash and checked the CONTEXT AgentRuns
    (CHIRALITY_V3_APP_ADOPTION_20260909, APP_V3_*). No post-v23 re-hash record exists.
  - ImplementationEvidence searches:
    - domain tools on the live path: grepped `domain_`, `mcp__chirality` and `api/domain` across
      `projects/chirality-runtime/packages/*/src`, `frontend/src/app` and `frontend/electron`;
    - path quarantine: grepped `protected_write_paths`, `agent_writable_paths` and `_DomainEngines`;
    - apply: no apply tool, route or descriptor exists;
    - PEC client: grepped `pec` in runtime packages;
    - later domain rulings: grepped the register for domain / PKG-10 / DEL-10 / pec rows after D-APP-58.
  - LatestDecision NONE_FOUND rows either restate no ruling (CONTEXT, verification-method and reference rows) or
    have none: REQ-001 ownership (D-APP-59 covers DEL-10-04 only) and CLM-019 (the v3 adoption is not a register
    row).
- **Reach basis:** every code citation uses `R2/PKG-10/EVIDENCE_PACK/REACHABILITY.csv`.
  - `frontend/packages/harness-contract/src/domain-profile.ts` is absent from the map. I tagged it TEST_ONLY
    because its only importer is `harness-contract-rollback.test.ts`.
- **PostReleaseBasis:** NO on every row. No cited file is in TOUCHED_PATHS.csv, and I deliberately did not cite
  `contracts/src/index.ts`, which is touched by `da95ec194`.

## 5. Method friction

- **Reading boundary (self-flag).** I checked VER-001's parity evidence in the Root `execution/` tree. I treated
  it as outside the App/Runtime evidence roots but not named in the prohibition list, so the brief's "any other
  project's execution tree" is ambiguous for Root's own tree.
  - **Proposed revision:** name Root `execution/**` explicitly, as either allowed read-only for migration
    evidence or forbidden.
- **Deferral versus present tense.** CONTRACT §1.10 states K-DOMAIN-2/3 in the present tense under a "Future
  Scope" heading. The rulebook has no guidance for invariants that are present-tense but scoped as future.
  - **Proposed revision:** add a line to §2.6 saying whether a section-level "future scope" heading counts as the
    GOVERNING permission for ACCEPTED_DIVERGENCE.
- **Module-level LIVE versus behaviour.** `domain-profile.ts` is LIVE only because the contracts index re-exports
  it; its guards have no product call site. Structural REQs were judged ALIGNED at module level, and behavioural
  ones on the live path.
  - **Proposed revision:** add a symbol-level "called from product" flag to REACHABILITY.

## 6. Effort

- **Read:** about 35 files or slices, in three groups:
  - the full deliverable set: SoW, _STATUS, _CONTEXT, MEMORY, _DEPENDENCIES, Dependencies.csv, _REFERENCES,
    INSP-03;
  - governing slices: CONTRACT §1.10 and preamble, SPEC §18, TYPES §11, PLAN R7, PRD §8.17, DIRECTIVE §0/§8, and
    the D-APP-127, D-GOV-43, D-APP-49/50/52/56/68 excerpts;
  - code: `domain-profile.ts`, the registry, the facade and the test case lists; plus evidence-pack filters and
    git log/show/blame for dating.
- **Not read:** `_SEMANTIC*.md` and `_run_records/**`.
- **Context budget:** adequate, not tight.
