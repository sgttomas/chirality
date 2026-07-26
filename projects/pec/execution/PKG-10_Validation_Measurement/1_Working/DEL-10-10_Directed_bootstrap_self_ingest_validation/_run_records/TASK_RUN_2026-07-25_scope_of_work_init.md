# TASK RUN RECORD — scope-of-work INIT — DEL-10-10

| Field | Value |
|---|---|
| RunDate | 2026-07-25 |
| Agent | Agent 2 (TASK), sealed brief |
| RequestedBy | PROJECT_SETUP |
| Decision | D-PEC-63 (SOW initialization wave, batch B5) |
| Phase | PROJECT_SETUP_PHASE_2_2 |
| TaskSkill | `scope-of-work` |
| ResolvedSkillVersion | `chirality-skill-version: "1"`, `chirality-task-profile: NONE` |
| MODE | INIT |
| ScopePath | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation` |
| DECOMPOSITION_BASIS | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b` (revision 1.2, `current_basis`, SCA-002 successor accepted under D-PEC-64) |
| PROJECT_SCOPE_REFS | SOW-064 |
| PACKAGE_OBJECTIVE_REFS | OBJ-006 |
| SOURCE_STATE | OPEN (unchanged; STATUS_POLICY `NO_STATUS_TOUCH`) |
| DECOMP_VARIANT | SOFTWARE |
| RENDER_HTML | false (no derivative produced) |
| RUN_STATUS | COMPLETE |

## Companion files read

- `skills/scope-of-work/SKILL.md`
- `skills/scope-of-work/BRIEF_SCHEMA.md`
- `skills/scope-of-work/TOOL_POLICY.md`
- `skills/scope-of-work/QA_CHECKS.md`
- `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` (governing standard, read-only)

## Grounding sources read

1. `execution/_Decomposition/ScopeLedger.csv` row `SOW-064` (verified against
   the brief's verbatim copy, field by field)
2. `docs/PRD.md` v2.1 — §12 release strategy (both closing paragraphs and the
   `P1` row), §11 success metrics and falsification clause, §3 product
   outcomes, §4.2 non-goals, §6 product invariants (`PEC-K-01`, `PEC-K-02`,
   `PEC-K-06`)
3. `execution/_Coordination/_DECISIONS/D-PEC-61_directed_full_dag_self_bootstrap.md`
   (ruled behavior items 1–2, exact fence, SCA-001 closure)
4. `execution/_Decomposition/SOFTWARE_DECOMP.md` — §1.3 `C16`, §2 preamble,
   §2.1 `SOW-064` SSOW row, §3 `OBJ-006`, §4 `PKG-10`, §5 `PKG-10` table,
   §10 `OI-010`, §11 `DL-10`/`DL-11`/`DL-16`/`DL-17`, §12 revision history
5. `execution/_Decomposition/Deliverables.csv` row `DEL-10-10` and the
   `PhaseHint` column for every deliverable named in this contract's own voice
6. Deliverable-local control files: `_CONTEXT.md`, `_REFERENCES.md`,
   `_DEPENDENCIES.md`, `Dependencies.csv`, `_STATUS.md`
7. `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` — §3
   validation summary, §4 node classes, edge-register rows `E-P73`/`E-P74`,
   constraint register row `C-08`;
   `execution/_Coordination/_DECISIONS/D-PEC-62_*.md` §1(3) and §1(4)
8. `execution/_ScopeChange/SCA-002_2026-07-25_1042/` — `Gate3_Simulation.json`,
   `Decision_Log.md` (`C-54`, the SOW-064 incident narrative), `Brief.md`,
   `Post_Change_Coverage.json`, `Handoff_State.md` — read to verify the
   objective warrant's pre-SCA-002 provenance
9. Git object `04a5efbf6` (`ScopeLedger.csv`, `Deliverables.csv` at accepted
   revision 1.1) — read-only verification of the pre-SCA-002 register values
10. Upstream contracts (tier ≥1 reads):
    `PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/ScopeOfWork.md`
    and
    `PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/ScopeOfWork.md`
11. Accepted standing-node pattern precedents (read-only):
    `PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/ScopeOfWork.md`
    and
    `PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/ScopeOfWork.md`

## Objective-warrant verification (performed before authoring)

`SOW-064` → `OBJ-006` is **register-direct** and pre-SCA-002. Three independent
checks, all agreeing:

1. `git show 04a5efbf6:projects/pec/execution/_Decomposition/ScopeLedger.csv`
   (the accepted revision 1.1 state, SCA-001 successor) already carries
   `ObjectiveIDs` `OBJ-006` on `SOW-064`, and that row is byte-identical to the
   row at the current accepted basis `3623b958b`.
2. `SOW-064` is not in SCA-002 action `A001`'s twenty `IN` rows and `DEL-10-10`
   is not in `A002`'s seventeen deliverable rows. SCA-002 `Decision_Log.md`
   control `C-54` records "`ScopeLedger.csv` SOW-064 quoting — restored
   byte-identical to HEAD" after an incidental writer renormalisation, with
   "no non-`ObjectiveIDs` field change" across the approved rows.
3. `SOFTWARE_DECOMP.md` §3 `OBJ-006` at revision 1.2 names both `SOW-064` and
   `DEL-10-10` in its mapped cells; `DL-16` records SCA-001 as the amendment
   that "maps both to OBJ-006".

Stated at record strength in Purpose and Objective Traceability. **No
confidence label is asserted and no owner-confirmation acceptance criterion is
created for the warrant**, per the brief's binding instruction and because no
accepted record rates or qualifies this mapping.

## Tool invocations

1. `python3 tools/scope_of_work/validate_scope_of_work.py "projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation"`

   Verbatim result (first and only run — no rerun required):

   ```
   PASS format=SOW_V1 target=projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation
   ```

2. `python3 tools/scope_of_work/derive_review_checklist.py "projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation"` — stdout only, not persisted.

   - `schema`: `chirality-review-checklist/v1`, `tool_version`: 1
   - `item_count`: **16** (`AC-001` … `AC-016`, source order, each exactly once)
   - bound production `sha256`:
     `a038cb5bd30286e5d6d06a2966eb72224f981778be527cea2d2048774ecd6109`
   - `AC-001`…`AC-014` each carry exactly one matrix-linked `VER-*` method
     (1:1 AC↔VER, no unioned rows); `AC-015` and `AC-016` carry explicit
     `HUMAN_REVIEW` methods
   - repeated derivation byte-identical (stdout sha256
     `cc0aa9facf202ea58997cfdbaa1560e9b79879ceba2b201e778490b1392128b9` on two
     consecutive runs; `cmp` reports no difference)

Tool-policy note: `TOOL_POLICY.md` steps 2–5 and 8 (converter, evidence-candidate
refinement with source markers, claim map, parity, finalizer, HTML render) are
CONVERT/derivative-shaped and inert for `MODE=INIT` — no legacy four-document
kit, no evidence candidate, and no requested derivative exist, and the
conversion tools are structurally CONVERT-only. Per the skill-contract
pre-ruling (D-PEC-63 §3.1) the applicable steps are source-grounded authoring,
validation, and checklist derivation, executed in that order. No `--force`, no
converter, no finalizer, no HTML.

## Production artifact

| Artifact | sha256 |
|---|---|
| `ScopeOfWork.md` | `a038cb5bd30286e5d6d06a2966eb72224f981778be527cea2d2048774ecd6109` |

## Contract shape

| Prefix | Count | Range |
|---|---|---|
| `OUT` | 1 | OUT-001 |
| `CLM` | 20 | CLM-001 … CLM-020 |
| `REQ` | 14 | REQ-001 … REQ-014 |
| `AC` | 16 | AC-001 … AC-016 |
| `VER` | 14 | VER-001 … VER-014 |
| `AX` | 11 | AX-001 … AX-011 |
| `TBD` | 5 | TBD-001 … TBD-005 |
| `CON` | 5 | CON-001 … CON-005 |

86 local definitions, no duplicates, no `REM-*`, every referenced ID defined.
Matrix: 16 rows, all `OUT-001` (the register names one cohesive record and
`ContextEnvelopeNotes` directs "keep one cohesive validation record"); 14 rows
carry one AC and one VER, 2 rows carry `HUMAN_REVIEW` methods.

## Read-only control files — before/after (byte-identical)

| File | sha256 before | sha256 after |
|---|---|---|
| `_STATUS.md` | `e45eebb3b3af3a95b28a7ccb25137bb98e9e4ed8b51d775468a88f42ecaab60c` | `e45eebb3b3af3a95b28a7ccb25137bb98e9e4ed8b51d775468a88f42ecaab60c` |
| `_CONTEXT.md` | `c3cba40f31e866c86985af81c5c8d6879af880ee566cc6369da98750eee49d95` | `c3cba40f31e866c86985af81c5c8d6879af880ee566cc6369da98750eee49d95` |
| `_REFERENCES.md` | `43ff727a153f0545fb3439b6dcc6c1326d031450a0c2bfefa2ef626515a7761c` | `43ff727a153f0545fb3439b6dcc6c1326d031450a0c2bfefa2ef626515a7761c` |
| `_DEPENDENCIES.md` | `0e6ff8d728d70cd05d4a9087cd8af43387d4f6eb02c8b10df925687d0ea3cb22` | `0e6ff8d728d70cd05d4a9087cd8af43387d4f6eb02c8b10df925687d0ea3cb22` |
| `Dependencies.csv` | `2ccdd71a6b9530722a3552ec81d6a477fed353fd25b28218c8a5b5105ad1e81d` | `2ccdd71a6b9530722a3552ec81d6a477fed353fd25b28218c8a5b5105ad1e81d` |
| `_SEMANTIC.md` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

`_STATUS.md` lifecycle state is `OPEN` before and after this run. The
`OPEN` → `INITIALIZED` advancement is a separate deterministic act under
D-PEC-63 §3.2 and was not performed here.

## Standing-node handling (C-08)

Authored as a STANDING assertion per the brief's directing sentence, quoted
verbatim in the Purpose section and attributed to its durable carrier
`execution/_Coordination/WAVE_D-PEC-63/BATCH_B5_FANIN.md` (PROJECT_SETUP's
batch fan-in record; not written by this run). The accepted DEL-01-05 /
DEL-10-03 pattern was applied:

- **Settled and stated as settled:** the arithmetic exclusion — `C-08` is a
  non-gating constraint row and this deliverable is excluded from one-shot
  `COMPLETE`/`UNBLOCKED` counting (CLM-008).
- **Unresolved and routed, not resolved:** the classification's force as a
  release gate — `Notes` "owner confirmation requested"; D-PEC-62 §1(4)
  accepted the standing-node set as a recorded-but-unresolved, non-gating
  annotation. Carried at **CON-001**, routed at **AC-015**, with a dedicated
  `HUMAN_REVIEW` matrix row. **This run did not resolve the gating-force
  question.**
- The `C-08` evidence phrase for this member is "standing validation" — the
  deliverable's own `Description` wording — and the row's `Notes` sentence
  "DEL-10-10 is the bootstrap progression record itself" is carried as the
  register states it: the standing obligation and its artifact are the same
  object (CLM-008, CON-002).
- `_DEPENDENCIES.md`'s compression "(owner-confirmed at D-PEC-62 ruling)" is
  accurate as to the arithmetic exclusion and overstates the rest; the contract
  cites the D-PEC-62 text over the local paraphrase.

## Upstream contracts read and elements bound

| Edge | Upstream | Maturity | Elements bound in this contract |
|---|---|---|---|
| `[E-P73]` (`DEP-10-10-003`) | DEL-02-05 Dependency register parser | INITIALIZED (contract only) | Its `OUT-001` and `REQ-001` (the DAG's file form is read and emitted as DependencyEdge records; both file forms in scope) and `REQ-006` (absent/unreadable/malformed/unrecognized feeds reported explicitly, coverage of a read itself reportable) — quoted in a §4-provision blockquote at CLM-010 with the ID carve-out. Consumed by REQ-012, AC-012, VER-012. Its `CON-004` corpus observation (the `projects/pec` tree holds 64 `Dependencies.csv` and **zero** `WORK_GRAPH.json`) is quoted in full at CLM-013 and attributed to that contract as **its** recorded observation, never asserted here; carried at CON-005. |
| `[E-P74]` (`DEP-10-10-004`) | DEL-03-01 Full-rebuild reconciler (one command) | INITIALIZED (contract only) | Its `OUT-001`, `REQ-001` (one command, full rebuild, no operator step) and `REQ-009` (upstream-reported feed limitations carried through, silent omission prohibited) — quoted in full at CLM-011. Its `CON-005` ("in full" vs limitation-bearing rebuilds) quoted in full and its `CON-001` (instance-level generated-views gap) quoted at its two governing sentences at CLM-012. The conditioning is carried, not smoothed: REQ-012, CON-004, AC-012, VER-012. |

No upstream artifact is asserted to exist. CLM-010 states explicitly that
`INITIALIZED` means the upstream **contract** is the reliable input and that no
parser, reconciler, store, or rebuilt record tier does. Both edges are
`PROPOSAL` stratum with `Flag` empty and are cited flags-as-flags by EdgeID per
D-PEC-62 §1(4) (AX-008). Edge direction is held: consuming both contracts
imposes no obligation on either upstream, and this deliverable's having no
accepted consumer (CLM-014, verified against the exhibit's edge register and
every `Dependencies.csv` in the project) is the `C-08` shape.

## Quotation record

Six omissions are made by this contract, each ellipsis-marked and enumerated in
full in the contract's own quotation-record trailer: two in the `DEL-02-05`
`REQ-006` quotation (CLM-010), two in the `DEL-03-01` `CON-001` quotation
(CLM-012), and two in the `DL-11` Decision-cell clause extract (CLM-017). One
further ellipsis inside the `DEL-02-05` `CON-004` quotation (CLM-013) is that
upstream contract's own omission of the `OI-010` text it quotes, not an
omission by this contract, which quotes `CON-004` in full. All upstream
contract quotations sit in §4-provision blockquotes carrying the carve-out
sentence "ID-shaped text inside this quotation is upstream source context, not a
local definition or reference."

## CONFLICT / TBD / CON roll-up

- **CONFLICT records: none.** No substantive ambiguity required a `CONFLICT`
  marking; the authority question encountered is carried as `CON-001` with a
  routed owner-confirmation acceptance criterion.
- **TBD-001** — `ResponsibleParty` unassigned (register `TBD`; assignment at
  WORKING_ITEMS activation).
- **TBD-002** — What mechanism runs this standing validation, on what
  occasions, and in what form is fixed by no accepted source.
- **TBD-003** — Where the progression record lives — path, format, single file
  vs dated entries — is fixed by no accepted source.
- **TBD-004** — What constitutes "acceptance" of a predecessor for a capability
  cutover is not fixed at this deliverable's level.
- **TBD-005** — The "structurally different loop" against which generality is
  validated is named by no accepted source.
- **CON-001** — Release-gating force of the `C-08` standing classification
  unconfirmed. Routed at **AC-015** with a dedicated HUMAN_REVIEW matrix row.
  Not resolved by this run.
- **CON-002** — The standing obligation and its artifact are the same object
  (`C-08` `Notes`), the register types the deliverable `TEST_SUITE` while
  naming a record as its artifact, and no accepted source states a runner
  (TBD-002) or a location (TBD-003).
- **CON-003** — Reflexivity: this deliverable is a node of the same accepted
  DAG whose ingestion it records, and observes friction arising in its own
  production. The consequence is bound (an observation grants no authority
  whatever its subject); the mechanism is not resolved.
- **CON-004** — DAG-ingestion evidence is conditioned by `DEL-03-01`/CON-005's
  open "in full" question; REQ-012 obliges the record to carry the conditioning
  rather than answer it by phrasing.
- **CON-005** — The self-ingestion corpus is not uniform across the upstream
  parser's feeds, per `DEL-02-05`'s own recorded census; recorded as that
  contract's observation, with REQ-012 requiring the upstream limitation report
  to appear in the record.

## Boundary discipline (brief-specific)

- **One artifact, not six.** `AnticipatedArtifacts` names one record with six
  facets and `ContextEnvelopeNotes` directs "keep one cohesive validation
  record". The contract declares exactly one `OUT-001`; the six facets are
  components, bound by REQ-009 and checked at AC-009/VER-009. The declared
  maintenance-and-rerun statement is a component of OUT-001 (precedent:
  `DEL-03-01`'s declared-view record), not a second artifact.
- **SOW-064's three Notes constraints all bound** (CLM-016): no-authority
  (REQ-006, AX-002 — a governing value, with CLM-019 stating the consequence
  for cutovers), fallback operability (REQ-005, AX-004), generality against a
  structurally different loop (REQ-010, TBD-005).
- **DL-10 / DL-11 / SCA-001** are cited as the ledger's own `DecisionRef`
  cross-references with their actual basis (CLM-017), not as register edges.
- **No sibling scope absorbed.** DAG parsing is `DEL-02-05`'s, reconciliation
  is `DEL-03-01`'s, edge materialization and blocker computation are
  `PROJECT_SETUP`'s under D-PEC-62; REQ-011 states the boundary as a checkable
  requirement, `DL-11`'s "a validation act, not a reconciler feature" is quoted
  as its accepted statement, and AC-016 puts it in front of REVIEW.
- **"Capability cutovers only after predecessor acceptance"** is stated as a
  property the record **evidences** (REQ-002), with CLM-019 recording
  explicitly that this deliverable holds no scheduling or authorizing power
  over cutovers and AC-002/VER-002 checking for authorizing language.
- **Basis-revision note (OI-B) applied**: `_REFERENCES.md`'s "revision 1.1"
  phrase is treated as superseded provenance and the contract cites revision
  1.2 with the divergence stated visibly in Purpose, not normalized away.

## Findings by class

- **Schema findings:** none. Validation passed on the first run; frontmatter
  uses inline list syntax, no duplicate keys, `decomposition_basis` binds with
  `@`, six required L2 headings in order, 3-digit local IDs, no `REM-*`, every
  referenced ID defined, every `OUT`/`AC`/`VER` present in the matrix, matrix
  header verbatim.
- **Project-content findings:** one recorded authority gap (CON-001, the `C-08`
  gating force) and four recorded gaps in accepted truth (CON-002 through
  CON-005). One basis-pointer divergence — `_REFERENCES.md` names revision 1.1
  while the accepted basis is revision 1.2 (deferred pointer sweep, SCA-002
  `Handoff_State.md` §6) — carried visibly rather than normalized.
  `_DEPENDENCIES.md`'s "(owner-confirmed at D-PEC-62 ruling)" overstates what
  §1(4) settled; the contract cites the D-PEC-62 text over the local paraphrase
  (CLM-008).
- **Execution-substrate findings:** the `scope-of-work` companion files
  (TOOL_POLICY steps 2–5/8, QA_CHECKS items 1–3 and 5–15) are CONVERT-shaped
  and largely inert for `MODE=INIT`; the run followed the D-PEC-63 §3.1
  pre-ruling and the INIT-applicable QA subset (4, 8, 9, 13, 16, 18). The INIT
  restatement of QA item 3 — `_STATUS.md` byte-identical with state unchanged
  at `OPEN` — holds, evidenced by the before/after table above.

## Write authorization

`ApplyEdits: true`. Files written by this run, both inside
`AllowedWriteTargets`:

1. `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md`
2. `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/_run_records/TASK_RUN_2026-07-25_scope_of_work_init.md`

No other file inside or outside `{ScopePath}` was created, modified, or deleted.
The derived REVIEW checklist JSON was emitted to stdout and inspected in a
session scratchpad outside the repository; it was not persisted to the
deliverable.
