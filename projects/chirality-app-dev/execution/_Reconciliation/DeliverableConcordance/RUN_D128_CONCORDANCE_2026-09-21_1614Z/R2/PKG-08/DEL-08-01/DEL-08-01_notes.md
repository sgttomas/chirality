# DEL-08-01 — forward notes (RUN_D128 R2 PKG-08, rerun)

Independent rerun worker. The earlier ledger, `_verify/**`, `_ORIGINAL/**` and `R0_CALIBRATION/**` were not read. No PREGATHER existed.
Basis: frozen tree at `00115c719`. Git use: read-only `log`/`show` against the frozen tree only (no touched path was cited, so no `blame` was needed; see PostReleaseBasis below).

## 1. Census

Rows: **54** (30 indexed units plus 5 `REGISTER-n` and 1 `STATE-n`). SEE rows: **0** (counted separately; none used, see §5).

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 27 |
| CONTEXT_CLAIM | 14 |
| REGISTER_DEFECT | 5 |
| ACCEPTANCE | 4 |
| STATE_ASSERTION | 2 |
| EXCLUSION | 1 |
| REMAINING_WORK | 1 |

| Disposition | Rows |
|---|---:|
| PARTIALLY_IMPLEMENTED | 14 |
| STALE_SPECIFICATION | 11 |
| NOT_AUDITABLE | 11 |
| ALIGNED | 8 |
| IMPLEMENTED_DIFFERENTLY | 6 |
| REMAINING_STATE_MISMATCH | 2 |
| DOCUMENTED_UNIMPLEMENTED | 1 |
| STALE_ASSESSMENT | 1 |

- **Split rate:** 4 of 30 indexed units split, 13.3%. The splits are CLM-005 (4-row construction table), CLM-009 (14-row requirements table, DEL0801-REQ001..014), CLM-012 (records and AC-001) and CLM-018 (records and VER-001). The SubItems in the index are AC-001 (CLM-012) and VER-001 (CLM-018), each with k = 1, and each has its own row.
- **HumanDecisionNeeded:** NO 35; `R4-Q1` 9; `R4-Q1; R4` 9; `R4` 1.
- **Confidence:** HIGH 19, MEDIUM 32, LOW 3.
- **PostReleaseBasis:** `NO` on every row. No cited file appears in `TOUCHED_PATHS.csv`. The only touched paths are a Root tranche manifest and `projects/chirality-runtime/docs/APPLICATION_TOOLS.md`, and neither is cited.
- **Errata (reverse pass):** 2 rows, both `ImplementationEvidence` (CLM-009.12 and CLM-009.14, REACH re-tag of `native-role-config.ts`). Sealed and errata-applied figures are identical in every census column: rows, ClaimType, Disposition, CauseTag, Confidence and HumanDecisionNeeded. No Disposition, ClaimType or HumanDecisionNeeded field changed. See `DEL-08-01_reverse_notes.md`.

## 2. Least-confident rows

- **CLM-009.9 (REQ009, section markers): DOCUMENTED_UNIMPLEMENTED, LOW.**
  - Alternative: PARTIALLY_IMPLEMENTED. The marker validator and its fixture exist, and the requirement names the check, not its use on shipped files.
  - I judged on what packaging and the product actually execute (lesson 4). Nothing on the packaging or live path checks the section structure of the four shipped role files.
- **CLM-009.14 (REQ014, unknown frontmatter keys): IMPLEMENTED_DIFFERENTLY, LOW.**
  - Alternative 1: DOCUMENTED_UNIMPLEMENTED, because the live path has no warning behaviour.
  - Alternative 2: ALIGNED by absence, because the live path consumes no instruction-file frontmatter at all and role options come only from the strict `agents/registry.json` schema.
- **REM-1: REMAINING_STATE_MISMATCH, LOW.**
  - Alternative: ALIGNED. The item is correctly recorded as open.
  - I chose mismatch because its write locus and checks name surfaces that no longer exist at the frozen basis:
    - Root `skills/` has become `.agents/skills/`;
    - Root `AGENTS.md` no longer has an agent-index change-notice rule.
  - MechanicallyUnblocked is `NO` under either reading. The dependencies DEL-06-03-V3-01 and DEL-07-01-V3-01 are still Remaining, and no owner write-scope grant is recorded.
  - The gate "DEL-02-02-V3-04 selected" is itself ambiguous. V3-04 is still Remaining with its own NOT_SELECTABLE gate, yet a bounded read-only V3-04 slice was implemented on 2026-09-06.
- **Also worth a verifier's look (MEDIUM):**
  - CLM-024 and CLM-026 are NOT_AUDITABLE. Their REF-006 MATCH content is treated as snapshot-true under MR-8 (iv) and carried by REGISTER-3. The alternative is STALE_SPECIFICATION for the present-tense "are current".
  - CLM-002 is STALE_SPECIFICATION. The SoW's own Gate-5 proviso makes earlier clauses dated history, which argues for NOT_AUDITABLE.

## 3. Register-defect summary

| Key | Defect | Disposition |
|---|---|---|
| REGISTER-1 | `_REFERENCES.md` REF-002 CONTRACT MATCH does not reproduce (`REFERENCE_HASHES.csv` Match=NO) | STALE_SPECIFICATION |
| REGISTER-2 | REF-003 SPEC MATCH does not reproduce; SPEC was amended under D-GOV-43 | STALE_SPECIFICATION |
| REGISTER-3 | REF-006 PRD MATCH does not reproduce; restated by 9 SoW units | STALE_SPECIFICATION |
| REGISTER-4 | REF-009 and REF-010 each name two different sources (duplicate RefIDs across the two tables) | REMAINING_STATE_MISMATCH |
| REGISTER-5 | Dependencies.csv DEP-08-01-013 points, by a machine-absolute path, to `agents/AGENT_SOFTWARE_DECOMP.md`, which was deleted by `d1166698d` (2026-09-09); `_DEPENDENCIES.md` L52 still calls it byte-identical | STALE_SPECIFICATION |

The other recorded hashes reproduce: DIRECTIVE, TYPES and PLAN (App docs), and the three `workflows/software-decomp` files (recomputed with `shasum -a 256` on the frozen tree).

Two other hygiene notes are carried in rows rather than registers:
- SoW CLM-006 carries a machine-specific absolute path.
- `_CONTEXT.md` package scope still names daemon-client dispatch (STATE-1).

## 4. Direction and cause

**Main finding.**
- On 2026-09-09 Root replaced its specialized agents with four v3 role files (`d1166698d`), and the App adopted the v3 role/skill/workflow bundle (`9b005c23a`).
- The v3 role files use level-two `## PROTOCOL/SPEC/STRUCTURE/RATIONALE` headings (Root SPEC §9.1, D-GOV-41, prospective). Role type, tools and write scope live in `agents/registry.json`. The files carry no `[[DOC:AGENT_INSTRUCTIONS]]` header, no Agent Type table and no `[[BEGIN:]]` markers.
- App SPEC §7 and CONTRACT K-WRITE-1 are unamended.
- The DEL-08-01 conformance validator (`frontend/src/lib/harness/agent-instruction.ts`) is LEGACY_ONLY. Its `validateAgentInstructionConformance` has no non-test caller. It therefore checks only synthetic fixtures, and would fail every shipped role file.

**Authority (lesson 1).**
- App DIRECTIVE §0 ranks SPEC (3) and CONTRACT (2) above `agents/AGENT_*.md` (7).
- Root SPEC §9 is prospective, with an adoption hold (Root CONTRACT K-AGENTS-1), and App SPEC §7 does not defer to it.
- The order therefore resolves the disagreement, and **no AUTHORITY_CONFLICT** is raised.
- The divergence is still consequential. Rows that turn on it carry `R4` (App SPEC §7 unamended for the adopted v3 format), plus `R4-Q1` because the only checks live in retained harness code.

**CauseTags.**
- `OTHER:V3_ROLE_ADOPTION` (18 rows): **new OTHER token, for the manager to report.** It names the Root/App v3 role-format and bundle adoption of 2026-09-09. No vocabulary tag names this mechanism:
  - CODEX_SOLE_ENGINE and NATIVE_DELEGATION concern the engine and delegation, not the instruction-file format;
  - V3_RELEASE_SCOPE concerns scope inclusion, not a mechanism.
- `DOC_HYGIENE` (5), `PRE_V3_DRIFT` (4: TBD statements overtaken by ADQ-12 on 2026-06-21), `LIFECYCLE_GATE_PENDING` (2), `CODEX_SOLE_ENGINE` (2), and one each of `CARRIER_PROPAGATION`, `SHELL_REDESIGN`, `NATIVE_DELEGATION` and `A2_TOPOLOGY`.
- `CAUSE2:` secondaries: CARRIER_PROPAGATION, CODEX_SOLE_ENGINE, NATIVE_DELEGATION, A2_TOPOLOGY, DOC_HYGIENE, PRE_V3_DRIFT, LIFECYCLE_GATE_PENDING and OTHER:V3_ROLE_ADOPTION.

**Records used.**
- CONTEXT:
  - `execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/HANDOFF_STATE.md` (App v3 adoption; "KG-001 source completeness: remediation required");
  - `execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway` (class-aware managed/native delegation; unaccepted).
- GOVERNING:
  - D-APP-108 (seating);
  - D-APP-109 (dependency re-extraction);
  - D-APP-127 (A2; names `instruction-root:integrity` as the packaged-root check, ruling record L126-138);
  - D-APP-38 (reference-integrity model).

**Searches behind each `NONE_FOUND`.**
- `_REGISTER.md` grep for D-GOV-41, registry.json, instruction-root, bundle, WHAT-IS, PLAN.md, KG-001, Q14 and agent-index. There is no App ruling adopting D-GOV-41 and no record dropping `docs/PLAN.md` from the bundle.
- CONTEXT grep, in the v3 adoption run, `APP_V3_CODEX_HOST_REPLATFORM_20260912` and the other `APP_V3_*` runs, for documentationClosure, PLAN.md and a validator implementation decision record. Nothing specific was found. REQ003 therefore cites the adoption CTX only for the adoption as a whole.
- REGISTER-4: register and seating CONTEXT searched for acceptance of RefID reuse; none.
- CLM-012.1 and CLM-018.1: no validator implementation decision record anywhere.
- No `UNRECORDED_JUDGMENT` rows.

**Reach determination (lesson 5).**
- `frontend/scripts/prepare-packaged-instruction-root.mjs` and `verify-instruction-root-integrity.mjs` are outside `REACHABILITY.csv`.
- I tagged them `REACH=LIVE` (build-time) for three reasons:
  - `frontend/package.json` runs them in `desktop:prepare`, `desktop:pack` and `desktop:dist`;
  - `.github/workflows/harness-premerge.yml` L117-133 runs both;
  - D-APP-127 names the integrity script as the packaged-root check.
- Every row using them states this in Notes.

## 5. Method friction

- **MR-4 vs CLM-003.** The Attributes table (CLM-003, earliest unit) restates the same SPEC rules that DEL0801-REQ001..014 (CLM-009) turn into test-suite MUSTs.
  - Read literally, MR-4 would make CLM-009.x SEE rows of CLM-003.
  - I treated them as different statements (definition vs test obligation) and dispositioned both.
  - Proposed revision: MR-4 applies only when the later unit adds no obligation, such as a verification demand.
- **CONTEXT_CLAIM vs lesson 2.** Several units mix normative restatement with stale state (CLM-004). CONTEXT_CLAIM forces NOT_APPLICABLE, while lesson 2 forces GOVERNANCE_INVARIANT for restatements.
  - I typed CLM-004 as REQUIREMENT with STALE_SPECIFICATION.
  - Proposed revision: allow STATE_ASSERTION to carry the restated tier explicitly for such mixed units.
- **Build-time scripts.** Neither `REACHABILITY.csv` nor the vocabulary has a BUILD reach. `REACH=LIVE` plus a Notes basis works, but a `REACH=BUILD` value would be clearer.
- **Snapshot claims restated in SoW prose.** MR-8 (iv) plus §2.7 route these to a REGISTER key. Pure source-state units (CLM-024, CLM-026) then have no natural disposition except NOT_AUDITABLE. A "SEE-REGISTER" convention would make this explicit.

## 6. Effort

- **Files read:** about 45, fully or in ranges. The deliverable set was ScopeOfWork, _STATUS, _CONTEXT, MEMORY, _REFERENCES, Assessment and _DEPENDENCIES extracts. Beyond that:
  - 4 frontend scripts and modules, and 6 test files (case lists);
  - 4 runtime modules;
  - App SPEC, PRD, CONTRACT and DIRECTIVE, plus Root SPEC and AGENT_WORKFLOW_RUNTIME extracts;
  - the register, and the D-APP-108 and D-APP-127 records;
  - the DEL-02-02 status extract;
  - the pack and inventories.
- **Git:** 5 read-only log/show calls.
- **Context budget:** adequate, not tight. The 30 KB and 54 KB semantic files and the `_run_records` were not needed.
