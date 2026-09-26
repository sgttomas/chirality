# Decomposition Coverage Report — SCA-006 post-change audit (checkpoint-3 preparation)

| Field | Value |
|---|---|
| Variant | `SOFTWARE` |
| Decomposition | revision **1.6**, pre-acceptance (`status: candidate_pending_checkpoint_3`), SHA-256 `3ef0412a99812885e247bc4e9726fe005ce3446372f609c47274b6ad25b29b59` |
| Audited tree | commit `5e0169f5e` on `claude/pec-sca006-cp3-execution` (Lane A1, A2, A4 applied; A5 in progress; A6 not done) |
| Scope | `ALL` |
| Status | **`WARNINGS`** (0 blockers / 3 warnings / 71 info; 12 expected consequences, counted separately) |
| Closure readiness | **`WARN`**, method-literal from the counts |
| Method edition | `audit-decomp` WORKFLOW `7ba6291c…246b`, contract `704929c7…4e75`, method `51a0c69b…8308827` |

**Expected source.** Candidate SCA-006
(`_ScopeChange/SCA-006_2026-09-25_1912/`, incomplete until A5) under the
accepted group-2 decision `checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`
(register row `D-PEC-97`) and its amendment 1
(`checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/`). The accepted
predecessor is SCA-005, which `_ScopeChange/_LATEST.md` still names (posture
`ACCEPTED_PREDECESSOR`). The four live registers and `docs/PRD.md` are
byte-identical to the accepted CP2 candidates. The live decomposition differs
from its CP2 candidate only in the pre-acceptance front-matter lines and the
acceptance-date slots (`Decision_Log.md` D-19). The three A2 mirrors equal
their plan postimages.

**Expected phase.** SCA-006 checkpoint-3 preparation, pre-acceptance poststate.
The `_Evaluation/DecompCoverage/_LATEST.md` decision belongs to the invoking
manager; this run did not touch it.

| # | Check | Verdict |
|---|---|---|
| 1 | Forward packages | `PASS`: 11/11. `INFO` ×2 from the structure tool (workspace SHOULD-subfolders and tool roots; pre-existing, first measured) |
| 2 | Forward deliverables | `PASS` (no counted blocker): 66/68 folders. DEL-08-06 and DEL-10-13 have no folder: `EXPECTED_CONSEQUENCE` ×2 (plan §B1, `D-PEC-97`) |
| 3 | Reverse coverage | `PASS`: no undeclared package or deliverable folder |
| 4 | ID consistency | `PASS`: every folder ID and parent package equals the declared value |
| 5 | Context fidelity | `PASS`: 66/66 `_CONTEXT.md` match `Deliverables.csv` on every compared field, including `ContextEnvelope` and the three A2 mirrors |
| 6 | Artifact presence / contract shape | `WARNING` ×3 (pre-existing) and `INFO` ×60. 3 anticipated sets found. 32 `SOW_V1`, 34 `NONE`, 0 ambiguous |
| 7 | Objective mapping | `PASS` for all six objectives. `INFO` ×5: OBJ-001's two folderless supporters, and the four retired rows by design |
| 8 | Ledger integrity | `PASS` (no counted warning): 100 rows (`74 IN / 18 OUT / 8 TBD`). Every IN row resolves at declaration level; SOW-099 and SOW-100 do not resolve to folders: `EXPECTED_CONSEQUENCE` ×2 (plan §B1) |
| 9 | Derivative parity | `SKIPPED`: not owned by the SOFTWARE variant. Other derivative-currency observations: `EXPECTED_CONSEQUENCE` ×6, `INFO` ×3 |
| 9b | Package-shape conformance | `PASS`: companion inventory present and mirrored by `Companion_Inventory.csv`; roles explicit; duplication justified (DL-15); §7 telemetry equals the registers |
| 10 | Active snapshot / handoff state | `PASS`: `_ScopeChange/_LATEST.md` names exactly one complete active snapshot (SCA-005); no handoff surface claims a later phase or cleaner closure than the evidence. `EXPECTED_CONSEQUENCE` ×2 (pre-acceptance pointers; mid-A5 candidate), `INFO` ×1 (SCA-005 residual) |
| 11 | Lifecycle distribution | `PASS`: 26 `INITIALIZED`, 30 `OPEN`, 4 `CHECKING`, 2 `IN_PROGRESS`, 4 `RETIRED` (66 folders); 2 declared units without folder (`UNKNOWN` in the matrix) |

## How to read the verdict

`overall_status = WARNINGS` and `closure_readiness = WARN` follow the count
rule: 0 blockers and 3 warnings. The three warnings are the pre-existing
Check-6 artifact-location findings (DEL-01-03, DEL-01-05, DEL-08-02), carried
unchanged since before SCA-005 and unrelated to SCA-006. The 12
`EXPECTED_CONSEQUENCE` findings are each a condition that would otherwise be a
BLOCKER or WARNING and that `D-PEC-97` (the accepted SCA-006 plan) explains;
the contract excludes them from the verdict. Without that classification the
two missing folders would read `BLOCKERS` / `FAIL`. `closure_readiness` is the
method's three-way verdict only; it is not a lifecycle, readiness, acceptance
or reliance judgement.

## Baseline findings COV-068, COV-069, COV-072, COV-073

These four baseline INFO findings (in `COV_SCA005_POSTSETUP_2026-09-25_1606`)
predate SCA-006 Lane A. The `D-PEC-95` act (PR #924, merge `abfd0897b`, an
ancestor of the audited commit; run root
`_Coordination/CURRENCY_REV15_D95_2026-09-25/`) changed exactly 42
`_CONTEXT.md`, 64 `_REFERENCES.md`, 10 `Dependencies.csv` and both `_LATEST.md`
pointers (`git diff --name-only abfd0897b^1 abfd0897b`). Since that merge no
`_REFERENCES.md` or `Dependencies.csv` changed, and only the three A2
`_CONTEXT.md` did. None of these resolutions is an SCA-006 effect.

| Baseline | Condition then | Observed now | Disposition | Attributed to |
|---|---|---|---|---|
| COV-068 | 42 `_CONTEXT.md` provenance blocks end at revision 1.4 | 0 end at 1.4; 63 end at 1.5, 3 (the A2 mirrors) at 1.6 | **RESOLVED** | `D-PEC-95` N2 (re-pin to 1.5) |
| COV-069 | 64 of 66 `_REFERENCES.md` name revision 1.4 | 0 at 1.4; 66 at 1.5 (all naming PRD v2.3) | **RESOLVED** | `D-PEC-95` N2 |
| COV-072 | 19 ACTIVE EXECUTION rows with non-verbatim EvidenceQuotes | All 19 verbatim; each row's Notes cite D-PEC-95; `LastSeen` 2026-09-25 | **RESOLVED** | `D-PEC-95` N3 |
| COV-073 | Stale-conservative SCA-005 `Handoff_State.md` / `RUN_SUMMARY.md` and both pointers | Pointers current for revision 1.5 and the D-PEC-93/95 acts. The two SCA-005 snapshot files are byte-identical to the baseline and still say DEL-02-08/09 `NOT_CREATED`, registers pre-B3, `AuditState BLOCKED` | **PARTIALLY RESOLVED**: pointer part resolved; snapshot-file part carried as COV-086 (`INFO`) | `D-PEC-95` N1 (pointers). The ruling selected option P, which keeps the two snapshot files byte-identical; `_COORDINATION.md` item 14 records them as superseded for current state, by hash |

What is new since then belongs to SCA-006 and is reported separately. The 63
contexts and 66 references now lag revision 1.6 and PRD v2.4 (COV-077,
COV-078), and two different EvidenceQuotes are now stale (COV-075, COV-076).
These are not re-openings of the baseline findings.

## Expected SCA-006 consequences (`EXPECTED_CONSEQUENCE`)

Every row cites `D-PEC-97` and the governing section of the accepted SCA-006
`Propagation_Plan.md`. Each matches the plan's stated prediction exactly.

| Issue | Check | Entity | Plan | Would otherwise be | Evidence |
|---|---|---|---|---|---|
| COV-003 | 2 | DEL-08-06 | §B1 | BLOCKER | No `PKG-08_*/1_Working/DEL-08-06_*` folder. Strict validator DRB-008 [DEL-08-06]. `audit_structure.py` unit FAIL "declared production-unit directory is missing" |
| COV-004 | 2 | DEL-10-13 | §B1 | BLOCKER | Same, for `PKG-10_*/1_Working/DEL-10-13_*` |
| COV-073 | 8 | SOW-099 → DEL-08-06 | §B1 | WARNING | Declaration resolves; folder does not |
| COV-074 | 8 | SOW-100 → DEL-10-13 | §B1 | WARNING | Same |
| COV-075 | 9 | DEP-09-06-003 | §B3 | WARNING | Quotes the revision-1.5 DEL-08-01 description ("owner, harness, admin"); not verbatim in `Deliverables.csv` |
| COV-076 | 9 | DEP-10-03-003 | §B3 | WARNING | Same quote and file |
| COV-077 | 9 | 63 `_CONTEXT.md` | §B7 | WARNING | Provenance ends at revision 1.5 `current_basis`; semantic fields current (Check 5 66/66) |
| COV-078 | 9 | 66 `_REFERENCES.md` | §B7 | WARNING | All name revision 1.5 and PRD v2.3 |
| COV-079 | 9 | DEL-04-03, DEL-08-01, DEL-08-03 `_CONTEXT.md` | §A2 | WARNING | Provenance anticipates "revision 1.6 (`current_basis` …)" before acceptance; exact accepted postimages |
| COV-080 | 9 | DEL-04-03, DEL-08-03 registers | §B2 | WARNING | No register traces SOW-097..100; DEL-04-03 anchors only SOW-006/007, DEL-08-03 only SOW-043 |
| COV-084 | 10 | both pointers + front matter | §A6, §A1 | WARNING | Pointers name revision 1.5 / SCA-005 with revision-1.5 hashes (recoverable at `94e9255b6`); the working surface is revision 1.6 pre-acceptance |
| COV-085 | 10 | SCA-006 candidate snapshot | §A5, §C5 | WARNING | `Supersession_Map.csv` present (45 rows); `Post_Change_Coverage.json` and `RUN_SUMMARY.md` absent; `Handoff_State.md` and `Decision_Log.md` not yet updated for Lane A |

**B3 check, exactly as the plan states.** Of the 111 ACTIVE EXECUTION rows,
exactly two quotes are not verbatim: DEP-09-06-003 and DEP-10-03-003, both
citing `Deliverables.csv` row DEL-08-01 Description. DEP-09-06-004 ("Machine-first
response envelope carrying citations.") and DEP-10-12-004 (the PKG-08 charter
prefix in `SOFTWARE_DECOMP.md`) remain verbatim. No `_DEPENDENCIES.md` contains
either broken quote. The 11 ACTIVE rows that cite a `ScopeOfWork.md` (the
`D-PEC-95` carry-forward) are verbatim.

**B7 counts, exactly as the plan states.** 63 `_CONTEXT.md` end at revision
1.5; the three A2 mirrors end at 1.6. All 66 `_REFERENCES.md` name revision 1.5
and PRD v2.3; none names 1.6 or v2.4. Before checkpoint 3 the revision-1.5
statements remain literally true of the accepted basis; the staleness is
against the candidate poststate this audit evaluates, and is version-only.

**COV-080 is outside the brief's list, not outside the plan.** Accepted plan
§B2 lists these TRACES rows (A-24, A-25, A-30, A-32) as open dependency-extract
work. The workflow directs classifying findings explained by an accepted
decision as `EXPECTED_CONSEQUENCE` (`Decision_Log.md` D-17).

## Coverage and context evidence

- **Packages.** All 11 declared packages (§4) have exact folders, each
  containing only `1_Working/`. §4 "Assigned (count)" equals the ledger's
  per-package IN counts for 11/11 (3/8/9/7/7/3/6/3/8/7/13).
- **Deliverables.** 68 declared rows (64 active, 4 retired); 66 folders. The
  §5 compact view and `ContextBudgetQA.csv` match `Deliverables.csv` for 68/68
  rows; the four retired rows are marked in both.
- **Reverse coverage.** No undeclared folder exists.
- **Context fidelity.** 66/66 match on DeliverableID, name, package, type,
  `ContextEnvelope`, `PhaseHint`, covered items, objectives, responsible
  party, description, anticipated artifacts and envelope notes. The A2 mirrors
  carry the revision-1.6 fields (DEL-04-03 +SOW-097 and reliance envelope;
  DEL-08-01 agent class; DEL-08-03 M, +SOW-098, budget text).

## Objective evidence (Check 7)

| Objective | IN scope items (ledger) | Supporting deliverables | Folder-backed |
|---|---|---|---|
| OBJ-001 | 31 | 27 | 25 (DEL-08-06, DEL-10-13 folderless; COV-068 `INFO`) |
| OBJ-002 | 15 | 14 | 14 |
| OBJ-003 | 16 | 14 | 14 |
| OBJ-004 | 13 | 11 | 11 |
| OBJ-005 | 9 | 7 | 7 |
| OBJ-006 | 9 | 9 | 9 |

For every objective, four sets are equal: the ledger IN set, the
`SupportsObjectives` set, the ledger-reached deliverables and the §3
objective-side view. No IN row lacks an objective; no active deliverable lacks
one. The union rule holds on all 64 active rows, and reciprocity holds on
68/68. The four retired deliverables support no objective by design (COV-069
to COV-072, `INFO`).

## Ledger integrity (Check 8)

`ScopeLedger.csv`: 100 rows, `74 IN / 18 OUT / 8 TBD`, equal to §2.1/§2.2/§2.3
and §7. Every IN row names a declared package and declared, non-retired
deliverables with matching package prefix. 72 of the 74 resolve to folders; the
two that do not are COV-073 and COV-074.

## Artifact and lifecycle evidence (Checks 6 and 11)

The three deliverable-local anticipated sets are unchanged: DEL-00-01, DEL-00-03
and DEL-10-01. No `_STATUS.md`, `ScopeOfWork.md` or `artifacts/` file changed
since the baseline's audited commit (`git diff --name-only 995af4f36 HEAD` over
those paths is empty). SCA-006 has no REMOVE action and wrote no `_STATUS.md`
(plan §A3).

| Issue | DEL | State | Note |
|---|---|---|---|
| COV-008 | DEL-01-03 | `IN_PROGRESS` | bytes under `projects/pec/v2/`; sibling `MEMORY.md` read (non-authoritative) is consistent |
| COV-010 | DEL-01-05 | `IN_PROGRESS` | bytes under `projects/pec/v2/` |
| COV-046 | DEL-08-02 | `CHECKING` | accepted source-tree bytes outside the folder |

The other 60 absences are `INFO`: 56 at `OPEN`/`INITIALIZED` (including
DEL-02-08/09) and 4 at `RETIRED`.

## Dependency evidence (supplementary)

- **Strict register validator:** 66 registers, 263 rows (ANCHOR 140, EXECUTION
  123), 68 deliverables declared. **0 errors / 2 warnings**, both DRB-008, for
  DEL-08-06 and DEL-10-13. Exit 1 by design of `--strict`. This is exactly
  plan §C2's prediction.
- **Closure tool:** 111 edges over 66 nodes, 0 SCCs, 0 bidirectional pairs, 0
  orphans; isolated DEL-00-03, DEL-01-05, DEL-06-04, DEL-07-02, DEL-07-04,
  DEL-07-05 (COV-082, `INFO`); hub DEL-03-01 (25). `closure_summary.json` is
  byte-identical to the baseline's and to the D-PEC-95 run root's
  `checks/closure_post.out` (`bd73806c…187a`).
- **Rows:** 243 ACTIVE (132 ANCHOR, 111 EXECUTION), 20 RETIRED; 0 ACTIVE rows
  target or sit in a retired register; ACTIVE `IMPLEMENTS_NODE` missing only
  for the four retired deliverables. No row names DEL-08-06, DEL-10-13 or
  SOW-097..100.
- **Anchors:** 132/132 ACTIVE anchor assertions true (62 `PackageID`, 70
  `DeliverableIDs include`), covering the 70 pre-SCA-006 IN rows (see COV-080).
- **Mirrors:** the 12 fully retired EdgeIDs have no unstruck row mention; no
  ACTIVE EdgeID is struck; E-P79..E-P82 remain mirrored.

## Active snapshot and handoff evidence (Check 10)

`_ScopeChange/_LATEST.md` (`e92b3b16…7d24`, equal to the checkpoint-3
precondition) names exactly one snapshot, SCA-005, which exists and holds all
15 items the baseline listed, byte-identical. `_Decomposition/_LATEST.md`
(`626feaaf…12dd`, equal to the precondition) names revision 1.5
`current_basis`. Neither pointer, nor the SCA-005 `RUN_SUMMARY.md` or
`Handoff_State.md`, nor the SCA-006 candidate's `Handoff_State.md`, claims a
later phase or a cleaner closure state than the evidence. All state
`ReadyForNextPhase = NO`. The SCA-006 `_AUTHORIZED` pointers are
amendment-qualified and say they do not replace `_LATEST.md`. Check 10 passes;
COV-084, COV-085 and COV-086 record the designed pre-acceptance state and the
stale-conservative residue.

## Other derivative-currency observations (Check 9)

- COV-075, COV-076 (B3), COV-077, COV-078 (B7), COV-079 (A2 anticipatory
  provenance), COV-080 (B2): above, `EXPECTED_CONSEQUENCE`.
- **COV-081 (`INFO`).** All 32 Scope of Work contracts are byte-unchanged. The
  accepted SCA-005 §B4 classes remain open, and SCA-006 §B4 adds its
  nine-contract set. SOW text was not audited.
- **COV-082 (`INFO`).** Closure-tool isolated units, above.
- **COV-083 (`INFO`, unforeseen).** Revision 1.6 carries unchanged from 1.5
  the statement that PEC's own `pec` registry row "declares the
  `remaining-loop` profile now". The statement appears in SOW-094 (§2.1 line
  259; `ScopeLedger.csv` line 72), the DEL-01-06 Description and the §9
  "feed profile" example list. The owner's 2026-09-26 amend direction on the
  unruled D-PEC-96 proposal says "revision 4: drop remaining-items and
  remaining-loop". Its record states the row's departure from
  SCA005-CP1-Q8 (a) still needs a ruling. Live `v2/config/loops.json`
  declares no feed profiles. No accepted decision has changed the basis, so
  this is not an SCA-006 defect. It is raised because checkpoint-3 acceptance
  would pin this text while the direction is pending.

## Package shape (Check 9b)

The main document carries a `Companion Inventory` section listing the same six
files as `Companion_Inventory.csv`. Its roles are labelled: working surface,
snapshot/handoff artifact, and four authoritative registers. The §2/§5
duplication of register fields is declared and justified (DL-15). The §7
telemetry (100 items, 74/18/8; 68 rows, 64/4; S 28 / M 34 / L 2 / XL 0; 10
open / 3 resolved issues; 68/68 single-package membership) equals the
registers, and §9 has 29 vocabulary rows. No derived publication artifact is
treated as authoritative.

## Workspace structure (Check 1 context)

`audit_structure.py` ran for the first time in this audit series. The current
method edition requires it. It returned `run_status COMPLETE`, `subject_status
FAIL`: 66 units pass, and the two folderless units fail (COV-003/004). It also
reports two workspace-level issues, both pre-existing and `INFO`:

- COV-001: all 11 package folders lack `0_References/`, `2_Checking/` and
  `3_Issued/` (docs/SPEC.md §12.2: SHOULD exist).
- COV-002: `_Aggregation/`, `_Estimates/` and `_Sources/` are absent.

## Comparison with `COV_SCA005_POSTSETUP_2026-09-25_1606`

Full detail is in `PrePost_Comparison.md`. Headlines:

- **Topology.** 96 → 100 scope items (70 → 74 IN), 66 → 68 deliverable rows
  (62 → 64 active), folders 66 → 66. Active envelopes S/M/L 28/32/2 →
  28/34/2.
- **Forward deliverable coverage.** 100 % → 97.06 % (66/66 → 66/68), from
  plan §B1 alone.
- **Issues (B/W/I/EC).** 0/3/70/— → 0/3/71/12.
- **Per-finding delta.** 68 carried, 2 changed, 3 resolved, 16 new. No new
  BLOCKER or WARNING. Of the 16 new findings, 12 are `EXPECTED_CONSEQUENCE`
  under `D-PEC-97`. The other four are `INFO`: one SCA-006 observation
  (OBJ-001's folderless supporters), two pre-existing conditions newly
  measured (COV-001/002), and one unforeseen observation (COV-083).
- **Validator.** 0/0 (exit 0) → 0/2 DRB-008 (exit 1), as plan §C2 predicts.
  **Closure** unchanged, byte for byte.

## What would clear the remaining findings

These are observations, not recommendations to act; each belongs to its own
owner and gate.

1. The three Check-6 warnings clear only if artifact-location practice or
   lifecycle state changes. They are unrelated to SCA-006.
2. A later owner-ruled PROJECT_SETUP packet (plan §B1) would clear COV-003,
   004, 068, 073 and 074, and the two DRB-008 warnings.
3. Dependency extraction (§B2, §B3) would clear COV-075, 076 and 080.
4. The revision-1.6 re-pin (§B7) would clear COV-077 and COV-078.
5. Checkpoint-3 acceptance with A6 would make COV-079's provenance true and
   move the pointers (COV-084). A5 completion would complete the candidate
   snapshot (COV-085).
6. SOW currency (§B4) would change COV-081.
7. COV-083 needs an owner decision on whether the revision-1.6 SOW-094 and
   DEL-01-06 text should stand while D-PEC-96 revision 4 is pending.

## Findings

The SCA-006 pre-acceptance poststate passes every structural check the method
owns. The audit found 11/11 packages, 66/66 existing folders with matching
contexts, consistent objective evidence and ledger integrity at declaration
level, and conformant package shape and lifecycle. Every structural gap it
found is one the accepted plan predicts: the two absent folders, the
folder-level ledger misses, two stale quotes, the re-pin lag, the
missing traces, and the pre-acceptance pointers and snapshot. Each is reported
as `EXPECTED_CONSEQUENCE` under `D-PEC-97`. The baseline's COV-068, 069 and
072, and the pointer part of COV-073, were resolved by `D-PEC-95`, not by
SCA-006. The remaining warnings are pre-existing and unrelated to SCA-006.

This derivative evidence accepts nothing and authorizes nothing. The audit
`_LATEST.md` pointer is unchanged.
