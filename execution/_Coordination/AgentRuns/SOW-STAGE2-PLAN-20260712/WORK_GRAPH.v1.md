# D-GOV-16 Stage-2 Work Graph v1

Status: `PROPOSED — NOT DISPATCHED`
Graph basis: `main@c9af689118e4e87f329e1ab4c6e71fea331b2674`

## Graph conventions

- `H` is a human gate; `B` a basis/manifest node; `C` canon/consumer
  activation; `P` pilot replacement; `W` ordinary conversion wave; `I` ISSUED
  handling; `X` cross-wave closure; `R` retirement request.
- Every node consumes only accepted predecessor snapshots.
- `R/O` means read-only. A write scope is exhaustive, not illustrative.
- CHANGE is the sole Git integration owner. Candidate workspaces are
  derivative until integrated through CHANGE.
- Every terminal return is `PASS`, `PARTIAL`, or `BLOCKED`; partial or invalid
  returns do not satisfy fan-in.

## Top-level dependency graph

```text
H0
 └─ B0 ─ C1 ─ C1V ─ C1G
                    ├─ C2R ─┐
                    └─ C2A ─┴─ C2F ─ C2G ─ B1
                                            ├─ P-A ─┐
                                            └─ P-P ─┴─ P-F ─ P-G
                                                              └─ W-A1 ─ W-A2 ─ W-A3 ─ W-P1 ─ W-P2 ─ W-P3 ─ W-P4
                                                                                         └───────────────┬──────────────┘
                                                                                                         I0 ─ H1 ─ I1
                                                                                                                 └─ X0 ─ X1 ─ R0 ─ H2
```

`I0` depends specifically on `W-P1` because both touch Piping PKG-01. `X0`
depends on all ordinary waves and, if H1 approves, I1. If H1 defers, X0 may
produce an honest partial/blocked closure package but cannot claim 154-member
conversion closure.

## Node contracts

| Node | Manager / bounded children | Depends on | Read scope | Write scope | Required output and checks | Release/failure rule |
|---|---|---|---|---|---|---|
| H0 — plan acceptance | Human via HELP_HUMAN | presented plan | this plan package; D-GOV-16 | exact ruling/receipt surface selected by HELP_HUMAN | explicit accept/amend/defer/reject | No acceptance, no Stage-2 execution run or child dispatch |
| B0 — synchronized bootstrap | ORCHESTRATOR; no child needed | H0 | Git refs; D-GOV-16; proposal artifacts; two project trees; caller surfaces | fresh Stage-2 run `basis/` and `snapshots/P0_BASIS/` only | synchronized refs, ruled hashes, census 154/10/144, lifecycle 153+1, caller manifest, exact path digest | Any ref/census/lifecycle/caller delta returns decision request |
| C1 — exact canon preparation | HELPS_HUMANS; bounded deterministic patch worker if needed | B0 | P0 snapshot; ruled standard and patches; current `docs/{DELIVERABLE_SCOPE_OF_WORK_STANDARD,TYPES,SPEC}.md` | isolated canon worktree: exactly those three canonical files; run evidence | exact copy, exact patch application, before/after hashes; no interpretation edits | Patch mismatch or any extra path blocks C1V |
| C1V — canon validation | EVALUATION, read-only | C1 | canon worktree; ruled hashes; root standards | `snapshots/P1_CANON/validation/` only | exact bytes, normative consistency, path containment, applicable root checks | Any failed required check blocks integration |
| C1G — canon integration | CHANGE; no content child | C1V PASS | validated canon candidate and manifest | Git refs/commit plus `snapshots/P1_CANON/` | dedicated canon commit, clean synchronized post-commit basis, evidence binding | No merge/push outside approved CHANGE brief; failure preserves candidate handoff |
| C2R — root consumer activation | HELPS_HUMANS; bounded TASK/generalist children with disjoint root paths | C1G | P1 canon; active caller manifest; agents, skills, tools, live explanatory docs, export sources | only caller-manifest paths under `agents/`, `skills/`, `tools/`, current docs, governed exports; no `projects/**/execution/PKG-*` | active SOW/legacy resolver, INIT/CONVERT/VERIFY method, checklist boundary, registries, tests, exports; full changed-path manifest | New/unclassified caller or project-deliverable write blocks C2F |
| C2A — App runtime activation | App Dev WORKING_ITEMS; TASK software implementation + separate software review child | C1G | P1 canon; App runtime caller paths and tests | App frontend scanner/view/runtime/test paths named in sealed brief; no App deliverable folder | SOW and legacy selection, ambiguous/partial fail-closed, feature-flag retirement, typecheck/build/test/runtime evidence | Any project deliverable/control write or failing required App check blocks C2F |
| C2F — consumer fan-in | RECONCILIATION + EVALUATION; one REVIEW compatibility calibration | C2R PASS, C2A PASS | both returns; caller manifest; checks; diffs | `snapshots/P2_CONSUMERS/` only | 100% active caller disposition; legacy retained; deterministic checklist exact-consumer calibration; root/App/exports green | REVIEW does not re-extract ACs; unclassified/failed caller blocks C2G |
| C2G — consumer integration | CHANGE | C2F PASS | accepted root and App commits | serial Git integration and P2 snapshot binding only | root then App integration, synchronized clean main, final caller hashes | Shared-write/conflict returns to parent; no deliverable conversion starts |
| B1 — post-activation manifest freeze | ORCHESTRATOR; RECONCILIATION read-only verifier | C2G | synchronized post-C2 main; P0 census; P2 caller snapshot | `snapshots/P3_MANIFEST/` only | row-by-row source/status/census equality; final execution manifest; caller closure | Membership/lifecycle/caller delta returns to human; source drift requires scoped amendment |
| P-A — App pilot preparation | App PKG-07 WORKING_ITEMS; six TASK verify-only children | B1 | P3 manifest; App pilot commit `fb83ff...`; six current legacy sources and controls | App PKG-07 isolated replacement worktree plus run evidence; no accepted main | exact candidate extraction, current-base hash check, validation/map/parity/checklist/render/project checks, six replacement manifest rows | No conversion regeneration unless material-change rule invoked; failed member excluded and handed off |
| P-P — Piping pilot preparation | Piping PKG-13 WORKING_ITEMS; four TASK verify-only children | B1 | P3 manifest; Piping pilot commit `31c35e...`; four current legacy sources and controls | Piping PKG-13 isolated replacement worktree plus run evidence | same checks as P-A; four manifest rows | Same isolation as P-A |
| P-F — pilot fan-in | RECONCILIATION | P-A PASS, P-P PASS | ten candidates, Stage-1 inventory/evidence, P3 basis | `snapshots/P4_PILOTS/preintegration/` only | 325 rows, 3,466 lines, ten status hashes, current consumer/project checks, single-format manifest | A failed pilot blocks that member and P-G; unrelated evidence remains valid |
| P-G — pilot integration | CHANGE | P-F PASS | accepted ten-row manifest and candidate blobs | ten serial deliverable replacement commits; `snapshots/P4_PILOTS/` | each commit adds SOW/removes four docs atomically; no control change; post-commit no dual state | Never merge pilot branches; any commit/check failure stops remaining integration and preserves rollback evidence |
| W-A1 | App package WORKING_ITEMS instances for PKG-00–03; author/verifier TASK pairs | P-G | current synchronized main; P3 manifest rows for 15 members; accepted tools | isolated package worktrees; candidate/evidence paths; later exact 15 deliverable dirs through CHANGE | 15 conversions, independent returns, RECON wave audit, 15 atomic commits, immutable snapshot | Failed member/dependants held; accepted subset requires explicit closed release manifest |
| W-A2 | App WORKING_ITEMS for PKG-04–06; author/verifier TASK pairs | W-A1 accepted snapshot | 16 member rows | same pattern, disjoint three packages | 16 conversions and wave snapshot | same |
| W-A3 | App WORKING_ITEMS for PKG-08–10; author/verifier TASK pairs | W-A2 accepted snapshot | 16 member rows | same pattern, disjoint three packages | 16 conversions and wave snapshot; App ordinary population closed | same |
| W-P1 | Piping WORKING_ITEMS for PKG-00–04; exclude DEL-01-01; author/verifier TASK pairs | W-A3 accepted snapshot | 30 ordinary rows; Piping current checks | isolated five package scopes, with PKG-01 limited to three named IN_PROGRESS members | 30 conversions and wave snapshot | DEL-01-01 is read-only and excluded; any overlap blocks fan-in |
| W-P2 | Piping WORKING_ITEMS for PKG-05–09 | W-P1 accepted snapshot | 29 member rows | disjoint five package scopes | 29 conversions and wave snapshot | standard wave isolation |
| W-P3 | Piping WORKING_ITEMS for PKG-10–12 | W-P2 accepted snapshot | 15 member rows | disjoint three package scopes | 15 conversions and wave snapshot | standard wave isolation |
| W-P4 | Piping WORKING_ITEMS for PKG-14–17 | W-P3 accepted snapshot | 22 member rows | disjoint four package scopes | 22 conversions and wave snapshot; ordinary population closed | standard wave isolation |
| I0 — ISSUED preparation | Piping PKG-01 WORKING_ITEMS; separate author and verifier TASK | W-P1 accepted snapshot and B1 | DEL-01-01 source commit, four blobs, accepted basis, status, D-GOV-16 item 6 | isolated DEL-01-01 candidate/evidence workspace only | deterministic candidate, full preservation package, independent RECON verdict; no integration | Semantic delta, status drift, or missing accepted-basis evidence is CONFLICT/BLOCKED |
| H1 — ISSUED administrative gate | Human via HELP_HUMAN | I0 PASS | exact I0 preservation snapshot | ruled administrative approval record only | explicit approval citing snapshot, or defer/reject/amend | Plan approval is not H1; silence prohibits I1 |
| I1 — ISSUED integration | CHANGE | H1 APPROVED | approved I0 manifest | one atomic DEL-01-01 replacement commit; `snapshots/P6_ISSUED/` | post-state SOW only, status byte-identical, lifecycle still ISSUED, full checks | Failure uses human-authorized recovery; no automatic reissue/revert |
| X0 — corpus reconciliation | RECONCILIATION + EVALUATION | W-A1..W-P4 accepted; I1 if approved | all wave snapshots, current tree, caller manifest, historical evidence | `snapshots/P7_CLOSURE/` only | 154 SOW, zero legacy/dual/invalid; receipts, caller closure, containment, full checks, rollback manifest | Any unresolved member/caller/ISSUED gate yields PARTIAL/BLOCKED, never false closure |
| X1 — conversion closure handoff | HELP_HUMAN validates fan-in; CHANGE binds evidence | X0 PASS | P7 snapshot and Git history | root handoff/receipt and evidence-binding commit only | `CONVERSION_CLOSED — LEGACY_RETIREMENT_RULING_REQUIRED`; rollback obligations named | No compatibility deletion or deprecation |
| R0 — retirement proposal | RECONCILIATION evidence; HELPS_HUMANS exact proposal | X1 and satisfied rollback obligations | closure evidence, retained caller list, recovery requirements | proposal/evidence package only | exact retirement targets, effects, bytes, recovery; no implementation | Missing caller/rollback closure blocks proposal eligibility |
| H2 — later retirement ruling | Human | R0 | evidence-backed proposal | human decision surface | approve/amend/defer/reject | No explicit approval means legacy remains supported |

## Standard per-deliverable child contract

Every ordinary author/verifier pair is instantiated from a sealed package
manifest row.

### Author child

- Role: TASK + `scope-of-work`, `MODE=CONVERT`.
- Reads: one deliverable's four source files, control metadata needed for
  provenance, accepted decomposition refs, exact active standard/tools, and
  its manifest row.
- Writes: isolated `ScopeOfWork.md`, claim map, parity report, checklist JSON,
  optional untracked HTML, receipt, and terminal return for that deliverable.
- Prohibited: `_STATUS.md` or other control edit; source-file edit; semantic
  rewrite; lifecycle act; write outside the isolated deliverable/run targets.

### Verifier child

- Separate instance and return.
- Reads author output and the same bound sources.
- Reproduces validation, map, parity, checklist, source/status hashes, format
  state, and containment. It may write only verifier evidence/return.
- It does not repair the candidate. A discrepancy is FAILED.

### Package manager fan-in

WORKING_ITEMS validates schema, coverage, provenance, unique ownership,
disjoint paths, and all returns before passing the package to RECONCILIATION.
No partial return becomes PASS.

## Wave fan-in and atomic integration protocol

For each wave `W-*`, RECONCILIATION must produce:

1. accepted basis and manifest hash;
2. expected, returned, PASS, FAILED, and missing member counts;
3. per-member candidate/source/status hashes;
4. aggregate mapping and source-line closure;
5. consumer/project/containment results;
6. separate schema, content/authority, preservation, and substrate verdicts;
7. exact accepted release set and blocked dependants; and
8. single-format replacement and rollback manifests.

CHANGE integrates the accepted release set serially. Each deliverable commit
must have this tree delta and no other deliverable delta:

```text
A  ScopeOfWork.md
D  Datasheet.md
D  Specification.md
D  Guidance.md
D  Procedure.md
```

Control-file hashes are checked before and after. After each commit, the
format resolver must report `SOW_V1`, never dual. A wave snapshot is accepted
only after post-integration checks on synchronized main.

## Failure isolation and dynamic replanning

- A source/hash/parity/checklist failure blocks the affected deliverable and
  declared dependants, not disjoint packages.
- A caller/canon failure blocks every conversion node because it is upstream.
- A project-wide runtime failure blocks integration for that project until
  classified and resolved.
- A shared-write conflict blocks only the overlapping stage and must be
  serialized or assigned one integration owner.
- A changed objective, authority, risk, ownership, write scope, acceptance
  criterion, lifecycle rule, or ISSUED meaning requires a versioned amendment;
  consequential amendments return to the human.
- Every FAILED/PARTIAL node persists basis, evidence, blockers, accepted
  predecessors, and exact rerun requirements. Earlier accepted snapshots are
  not rewritten.

## Current graph state

All execution nodes are `PENDING`. H0 has not been released in this planning
run. Terminal state remains `PLAN_PRESENTED — NO_STAGE2_DISPATCH`.
