# DEL-08-02: forward-pass notes (RUN_D128, R2 PKG-08)

Sealed ledger `DEL-08-02_claims.csv`, SHA-256
`7d46d035b414d97f205f18b84a7a08e1cc8fd465db0330a95016ac3afafb0b1d`. The validator
reported `RULES errors none | warnings none` and `RESULT PASS errors=0 warnings=0`. All
reading was done at the frozen basis `00115c719`. The reverse pass produced no errata, so the
errata-applied figures are identical to the sealed figures below (see
`DEL-08-02_reverse_notes.md`).

## 1. Census

- **Rows:** 73 in total. 68 rows cover the 28 indexed units (CLM-001..026, REMTXT-1,
  REM-1). The other 5 are run-local: REGISTER-1..4 and STATE-1.
- **Split rate:** 7 of 28 indexed units are split (25%): CLM-003 (7 rows), CLM-004 (6),
  CLM-005 (6), CLM-009 (22, one per REQ-001..022), CLM-011 (2), CLM-012 (2: the
  documentation list and AC-001) and CLM-018 (2: the records list and VER-001). The
  index's `SubItems` lists one item each for CLM-012 (AC-001) and CLM-018 (VER-001).
  CLM-009 has no `SubItems` entry, but it holds 22 numbered REQ items, so it is split
  under §2.2.
- **SEE rows (counted separately):** 9. These are CLM-005.2, CLM-009.12, .13, .14, .16,
  .18, .19, .22 and CLM-022. Without them there are 64 rows.

| Disposition | Rows | Of which SEE |
|---|---:|---:|
| STALE_SPECIFICATION | 16 | 0 |
| IMPLEMENTED_DIFFERENTLY | 15 | 7 |
| ALIGNED | 12 | 1 |
| PARTIALLY_IMPLEMENTED | 11 | 0 |
| NOT_AUDITABLE | 9 | 0 |
| DOCUMENTED_UNIMPLEMENTED | 8 | 1 |
| REMAINING_STATE_MISMATCH | 2 | 0 |

| ClaimType | Rows | Dispositions |
|---|---:|---|
| REQUIREMENT | 44 | IMPLEMENTED_DIFFERENTLY 15, ALIGNED 11, PARTIALLY_IMPLEMENTED 10, DOCUMENTED_UNIMPLEMENTED 8 |
| CONTEXT_CLAIM | 16 | NOT_AUDITABLE 9, STALE_SPECIFICATION 7 |
| STATE_ASSERTION | 7 | STALE_SPECIFICATION 6, ALIGNED 1 |
| REGISTER_DEFECT | 4 | STALE_SPECIFICATION 3, REMAINING_STATE_MISMATCH 1 |
| ACCEPTANCE | 1 | PARTIALLY_IMPLEMENTED 1 |
| REMAINING_WORK | 1 | REMAINING_STATE_MISMATCH 1 |

- **HumanDecisionNeeded other than NO:** 34 rows. `R4` 28, `R4-Q1; R4` 4, `R4-Q1` 1,
  `D-APP-127` 1.
- **Confidence:** HIGH 32, MEDIUM 41, LOW 0.
- **PostReleaseBasis:** `NO` on every row. None of the cited files is in
  `TOUCHED_PATHS.csv`: its frontend entries do not include any DEL-08-02 module, and the
  cited Runtime files (`core/src/runtime-service.ts`, `method-catalog.ts`,
  `contracts/src/v3.ts`) are not listed. No blame was needed.

**Main finding.** DEL-08-02 describes a contract that the live App no longer implements.
On 2026-09-09, commit `9b005c23a` ("Adopt conversational roles, skills, and workflows for
Chirality v3") changed four things:

- it replaced the four-alias map and the `WORKING_ITEMS` default with a two-alias map, a
  `HELP_HUMAN` default and a fallback to `HELP_HUMAN` for unknown labels;
- it retired the 3x4 matrix, keeping a role directory in its place;
- it removed the legacy branch in `WovenDialogueRoute`, so `/pipeline` now shows the
  dialogue shell;
- it let a selected recorded conversation be resumed as the primary conversation.

None of this is transcribed into App `TYPES.md` §3.4/§4, `SPEC.md` §13.1/§17.6/§17.9 or
`PRD.md` FR-007/008/011/023/025/026. Those texts stay governing. Root D-GOV-42 is an
owner-directed candidate whose App adoption is "separately owned", so it is not treated
as governing here, and I do not read these rows as AUTHORITY_CONFLICT.

## 2. Least-confident rows

No row is LOW. These MEDIUM rows are the ones most open to another reading:

- **CLM-003.4, CLM-009.10, CLM-004.3 / CLM-009.16 (Pipeline routing and coming-soon
  visibility).** I judged these on the live path. `REACHABILITY.csv` tags `pipeline-surface.tsx`
  as LIVE, but at runtime it is only passed as the `legacy` prop, and
  `woven-dialogue-route.tsx:18` discards it (`void legacy`).
  - Alternative reading: D-APP-108 Q3 ("routes stay reachable by URL, unmounted from the
    active shell") is a governing ruling that addresses the `/pipeline` route. It could
    be read as undercutting TYPES §4.1 ("OPERATIVE → PIPELINE") and PRD FR-011 without
    naming them. That would make these rows AUTHORITY_CONFLICT.
  - Why I did not: Q3 kept the routes reachable, and at `03e61f38f` (2026-09-05) they
    still rendered the legacy shells. The later removal (2026-09-09) is explained only by
    CONTEXT, so I cite `GOV:D-APP-108` as partial direction.
- **CLM-009.8 / .9 (NORMATIVE and EVALUATIVE routing).** Every cell still lands on a
  Type 0/1 role, which could be read as ALIGNED. I read "canonical Type 0/1 persona" as
  the cell's own persona, which the code does not route to, so I used
  IMPLEMENTED_DIFFERENTLY.
- **CLM-009.4.** I set it ALIGNED on the MUST NOT. The explanatory clause says the
  EVALUATIVE/REVIEWING cell uses RESEARCH, which is now false. A stricter reading gives
  PARTIALLY_IMPLEMENTED.
- **CLM-009.17.** I set it ALIGNED because App code invents no alias, row or column.
  - Alternative reading: the catch-all fallback to `HELP_HUMAN` is an unsourced mapping,
    and the three v3 role names lack an App-corpus source. Either would make it
    IMPLEMENTED_DIFFERENTLY.
- **CLM-009.11.** I set it PARTIALLY_IMPLEMENTED because continuation hands interaction
  authority to the selected recorded session.
  - Alternative reading: continuation is a deliberate user act, so no authority is
    "transferred", which would make it ALIGNED.
- **CLM-009.15.** I set it OVERTAKEN / DOCUMENTED_UNIMPLEMENTED.
  - Alternative reading: the legacy `options.ts` still warns, so the INSP-03 PASS still
    reproduces on that module, and the row would then turn wholly on R4-Q1.
- **STATE-1 (MEMORY.md 2026-08-02).** This is a dated entry written in the present tense.
  I read it as a current-state claim that is now false.
  - Alternative reading: it is history that was true when written, and not auditable.
- **CLM-004.6.** I set it PARTIALLY_IMPLEMENTED because the SoW did not surface the
  ORCHESTRATE-target conflict.
  - Alternative reading: this is a documentation defect, which would make it
    STALE_SPECIFICATION.

## 3. Register-defect summary

- **REGISTER-1..3 (STALE_SPECIFICATION, DOC_HYGIENE).** `_REFERENCES.md` records MATCH
  for CONTRACT, SPEC and PRD at the 2026-09-12 hashes (`fa8fc9dc…`, `01e1c75c…`,
  `8649ccba…`). The recomputed values at `00115c719` differ (`57411f8d…`, `8b0d805b…`,
  `17ca3f3c…`; pack `REFERENCE_HASHES.csv`, all `Match=NO`). All three documents changed
  in later commits on 2026-09-12. The restating rows cite these keys: CLM-004.1, CLM-006,
  CLM-010, CLM-011.2, CLM-015, CLM-023, CLM-025 and CLM-026. I recomputed TYPES,
  DIRECTIVE, PLAN and the software-decomp workflow files myself, and all of them still
  match.
- **REGISTER-4 (REMAINING_STATE_MISMATCH).** `_REFERENCES.md:31-32` still says the hashes
  are "reconciled to authority corpus v16", but the rows were re-hashed on 2026-09-10 and
  2026-09-12.
- **Other document-hygiene defects on SoW rows:**
  - REF-007 points to `agents/AGENT_SOFTWARE_DECOMP.md`, which is absent (CLM-006).
  - The records list still names Datasheet/Specification/Guidance/Procedure, which were
    deleted on 2026-07-13 (CLM-018.1).
  - The F-001/D-001 slots are still "TBD" although the same SoW records D-001 as
    resolved (CLM-005.6).
- **D-APP-127 carriers.** `D-APP-127_APPLICATION_MAP.csv` shows all five carriers `NO`.
  REM-1's gate ("accepted and landed D-APP-88 distinct-helper implementation") has a
  premise that D-APP-127 retired. The row therefore has MechanicallyUnblocked `NO` and
  carries `MOOT:D-APP-127`.

## 4. Direction and cause

**Primary CauseTags.**

- V3_RELEASE_SCOPE: 32 rows. This is the v3 role/skill/workflow adoption: the four-role
  registry, the `HELP_HUMAN` default, the matrix retirement and session continuation.
- DOC_HYGIENE: 9.
- SHELL_REDESIGN: 4. This covers Pipeline unmounting and the legacy-branch removal.
- PRE_V3_DRIFT: 3.
- CARRIER_PROPAGATION: 3 (REMTXT-1, REM-1, STATE-1).
- CODEX_SOLE_ENGINE: 1 (the unknown-option warning exists only on the legacy harness
  path).

I chose V3_RELEASE_SCOPE over an `OTHER:` token because the CONTEXT adoption record puts
the role model in v3 scope explicitly. The mechanism itself is the D-GOV-42 four-role
adoption.

**Secondary tags (`CAUSE2:`).** SHELL_REDESIGN 11, V3_RELEASE_SCOPE 7, DOC_HYGIENE 6,
PRE_V3_DRIFT 4, CODEX_SOLE_ENGINE 4, A2_TOPOLOGY 2.

**Records used.**

- CONTEXT:
  - `execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/MANAGER_RETURN.md:6-13`:
    one role-based conversation, `HELP_HUMAN` default, three direct-entry roles, and
    "compatible v3 sessions resume".
  - `CORPUS_V21_CANDIDATE.md:45-60`: retired role-file aliases migrated in `_REFERENCES`
    only; the corpus is still a candidate.
- GOVERNING:
  - D-APP-108 Q3: `/workbench` and `/pipeline` stay reachable by URL, unmounted from the
    active shell.
  - D-APP-127 §D-APP-88: the helper bundle is superseded; the routes become thin
    adapters.
- Root D-GOV-42 was consulted and is cited only as `(context)`. Its status line reads
  "exact review, merge, and effective adoption pending", and its application boundary
  leaves App adoption to the App loop. Root `docs/TYPES.md` §4 likewise says incompatible
  consumers stay on their accepted basis until the owning loop adopts.

**Searches behind each NONE_FOUND.** I grepped `_DECISIONS/_REGISTER.md` for
`DEL-08-02|persona|alias|matrix|four-role|role registry|direct-entry|ORCHESTRATOR|resume|continu`
and `D-GOV-4[12]`. I also grepped the whole `_DECISIONS/` folder for `D-GOV-4[12]`, which
returned no hits, and grepped the App PRD/SPEC/DIRECTIVE/CONTRACT for `D-GOV-4[12]` and
`four-role`. On the CONTEXT side, I grepped `plans/steers/chirality_app_v3_*` and the
adoption AgentRun for alias, matrix and persona terms. None of these found an App ruling
that:

- adopts the four-role registry, the `HELP_HUMAN` default or resume-on-selection into the
  App corpus;
- retires the legacy matrix; or
- records the SoW's ORCHESTRATE→ORCHESTRATOR wording. `TYPES.md` has said PROJECT_SETUP
  since `3b6852548` on 2026-07-22.

These searches are named in the Notes of the NONE_FOUND rows (CLM-004.6, CLM-005.6,
CLM-015, CLM-018.1, CLM-026, REGISTER-1..4). There are no UNRECORDED_JUDGMENT rows.

**Named R4 questions.** R4-Q1 appears on the rows where the only conforming code is the
retained harness: PERSONA_NOT_FOUND and name-derived `AGENT_<name>.md` lookup in
`lib/harness/agent-instruction.ts`, and unknown-option warnings in
`lib/harness/options.ts`, both LEGACY_ONLY. The rows are CLM-003.6, CLM-005.2,
CLM-009.12, .13 and .15. R4-Q2 and R4-Q3 do not apply.

**Candidate R4 framing.** One owner question would settle most of the 28 `R4` rows. It
is whether the App corpus (TYPES §3.4/§4, SPEC §13.1/§17.6/§17.9, PRD FR-007/008/023/026)
adopts the v3 role model and the continuation behaviour that shipped in `9b005c23a`, or
whether code must return to the corpus.

## 5. Method friction

- **REACHABILITY versus runtime-discarded props.** The static map tags `loop-shell`,
  `loop-tertiary-shell`, `tertiary-sidebar-tabs`, `pipeline-surface` and similar modules
  as LIVE, because they are imported by `app/**/page.tsx`. Since 2026-09-09, however,
  `WovenDialogueRoute` voids its `legacy` prop, so these modules never render.
  - Proposal: add a `LIVE_IMPORT_ONLY` note, or have the map builder treat a prop passed
    to a component that discards it as unreached.
  - Workers who trust the map would read Pipeline/matrix clauses as live-implemented.
- **SEE direction.** MR-4 disposes a statement on the earliest indexed unit. In SoWs of
  this template, the Datasheet attribute table (CLM-003) comes before the numbered
  requirements (CLM-009), so the REQ rows would SEE a less precise Datasheet row.
  - What I did: I used SEE only where the statement is materially identical, and gave
    the REQ rows their own disposition otherwise.
  - Proposal: allow SEE toward the numbered REQ when the earlier unit is a summary table.
- **CLM-009 `SubItems` is empty** even though the unit holds 22 numbered REQ items. The
  index emitted AC/VER bullets but not table-form REQ rows. I split it by the §2.2 text.
- **REMAINING_WORK with a mooted gate.** When a gate's premise is retired by a ruling
  that does not name the deliverable, the choice between REMAINING_STATE_MISMATCH and
  STALE_SPECIFICATION is not specified. I used REMAINING_STATE_MISMATCH.

## 6. Effort

I read about 45 files or line ranges:

- the deliverable folder: SoW, `_STATUS`, `_CONTEXT`, `MEMORY`, `_REFERENCES`,
  `_DEPENDENCIES`, `Dependencies.csv` and the INSP-03 assessment;
- about 20 frontend and Runtime source and test files;
- `_REGISTER.md` plus the D-APP-108 and D-APP-127 rulings and D-GOV-42;
- App TYPES/SPEC/PRD/DIRECTIVE excerpts and Root TYPES §4;
- the adoption AgentRun return and corpus files;
- the evidence pack and the APP gate transcript.

Git use was read-only `log`/`show` against the frozen tree. The context budget was
adequate but not loose; I did not open `_SEMANTIC*.md` (83 KB) or most `_run_records`,
because the SoW and `_STATUS` carried the claims.
