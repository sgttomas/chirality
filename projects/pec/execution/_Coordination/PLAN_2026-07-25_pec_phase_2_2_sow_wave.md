# PLAN 2026-07-25 — PEC Phase 2.2: SCA-002 objective mapping, then the SOW initialization wave (D-PEC-63)

**Author:** PROJECT_SETUP (Agent 1), session of 2026-07-25 (post-D-PEC-62)
**Status:** ACTIVE — compaction-survival execution plan; the single
timestamped session plan (Issue-Plan rule). R1-refuted and revised before
the pause (see §6).
**Position marker (update at every stage/batch; §6 must be current before
any pause):**
`STEP 2 COMPLETE — SCA-002 CLOSED 2026-07-25: revision 1.2 accepted
("Accept revision 1.2 (Recommended)", Gate 5). All 32 wave members carry
non-empty SupportsObjectives (wave-unmapped 17→0); O-A residue 11 IN
rows / 9 deliverables untouched. Evidence:
_ScopeChange/SCA-002_2026-07-25_1042/ + Receipt 109; refutation rounds
R-2a, R-2b-g1..g5 in §6. PROJECT_SETUP RESUMED (closure commit per
D-PEC-64 §3.6b performed). Next: STEP 3 — D-PEC-63 draft v2 re-pins
(§7: three pins to rev 1.2 + DAG-exhibit §1 annotation), refutation,
owner ruling with Q1/Q2; then STEP 4 wave B1–B8.`

---

## §0 Resume instructions (for a cold agent)

You are PROJECT_SETUP for `{WORKING_ROOT}` = `{REPO_ROOT}/projects/pec`
(`REPO_ROOT` via `git rev-parse --show-toplevel`). Read in order:
1. This file, fully.
2. `{REPO_ROOT}/agents/AGENT_PROJECT_SETUP.md` — Phase 2.2 + invariants.
3. `{REPO_ROOT}/agents/AGENT_SCOPE_CHANGE.md` — for STEP 2 (SCA-002).
4. `{REPO_ROOT}/skills/scope-of-work/SKILL.md` + `BRIEF_SCHEMA.md` +
   `TOOL_POLICY.md` + `QA_CHECKS.md` — the INIT authoring contract.
5. `{WORKING_ROOT}/execution/_Coordination/_DECISIONS/D-PEC-63_pec_phase_2_2_scope_of_work_initialization_wave.md`
   (DRAFT — conditioned on SCA-002).
6. `{WORKING_ROOT}/execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`
   — the accepted-DAG gate exhibit (rev-1.1 frozen provenance; see §7 note).

Standing owner steers (this arc): **opus-5 for every Agent 1/2 instance**;
**adversarial refutation of your own fan-in before every owner gate and
every closure** (ephemeral refutation-briefed Agent 2s, findings
dispositioned at fan-in, logged in §6 BEFORE any pause).

**Stage sequence:** STEP 2a — PROJECT_SETUP drafts the SCA-002 **opening
packet** (next free D-PEC ID; expected D-PEC-64 — ID order ≠ execution
order here) + intake package; owner rules it → STEP 2b — **owner invokes
SCOPE_CHANGE** (human entry; PROJECT_SETUP must NOT dispatch it — Agent 1
→ Agent 1 delegation is not an allowed edge; PROJECT_SETUP yields while
`_ScopeChange/_LATEST.md` is active and resumes from its handoff state) →
STEP 3 — D-PEC-63 draft v2 (re-pins per §7) + refutation + owner ruling →
STEP 4 — wave B1–B8 → STEP 5 — closure. Mandatory owner gates: the
opening-packet ruling; every SCA gate 1–5; the D-PEC-63 ruling; post-B1
and post-B2 reviews; wave closure.

## §1 Wave scope (frozen; owner-accepted)

32 deliverables = 3 pre-P1 + 29 P1 (PhaseHint, `Deliverables.csv`). P2–P4
deferred to later packets. Batches by DAG tier over **raw** in-wave
EXECUTION/UPSTREAM/ACTIVE edges from the deliverable-local registers.

**Tiering convention (load-bearing):** tiering uses ALL in-wave
EXECUTION/UPSTREAM/ACTIVE edges — the C-08 standing-target exclusion
applies to **blocker arithmetic only** and must NOT be applied to tiering.
The single divergence node is DEL-10-11 (sole upstream DEL-03-04 is C-08):
it is tier 5 / B6 for batching yet UNBLOCKED at baseline in the blocker
report. Applying the exclusion to tiering would wrongly move it to B1 and
yield the ladder 10,13,19,20,26,29,31,32. Recompute at execution: tier 0
must reproduce B1 exactly under the raw-edge convention.

| Batch | n | Deliverables |
|---|---|---|
| B1 pilot (roots) | 9 | DEL-00-01, DEL-00-03, DEL-01-03, DEL-01-04, DEL-01-05, DEL-01-06, DEL-08-01, DEL-08-02, DEL-10-01 |
| B2 | 3 | DEL-01-01, DEL-02-07, DEL-10-03 |
| B3 | 6 | DEL-02-01, DEL-02-02, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06 |
| B4 | 1 | DEL-03-01 |
| B5 | 6 | DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-01, DEL-10-02, DEL-10-10 |
| B6 | 4 | DEL-03-06, DEL-04-02, DEL-04-03, DEL-10-11 |
| B7 | 2 | DEL-04-05, DEL-08-03 |
| B8 | 1 | DEL-08-04 |

The wave is upward-closed (zero out-of-wave upstream edges; R1b-verified).
B1 runs a canary fan-out of 3 first — DEL-01-06 (simple S), DEL-08-02
(contract-heavy API_CONTRACT), DEL-00-01 (carries OI-012) — full contract
read + brief-template fixes before the remaining 6. Owner halts after B1
and B2 (first upstream-citing batch); relax to internal fan-in for B3–B8
only if both clean. Any FAIL/CONFLICT/scope violation re-arms per-batch
halts. Authoring concurrency ≤ 4.

**Canary-failure routing (R1a-F7):** `MODE=INIT` has no precedent run in
this repo, and the skill's companion files are partly CONVERT-shaped
(`QA_CHECKS.md` items 2/3/5–7/10–12/14/17 are conversion-only;
`BRIEF_SCHEMA.md` write-boundary list enumerates conversion artifacts;
`TOOL_POLICY.md` steps 4–5 have no INIT branch). A canary failure
traceable to those companion contracts is a **skill-contract defect**:
halt the wave and route an AGENT_HELPS_HUMANS request for INIT-mode
branches. PROJECT_SETUP may not edit `skills/**` (outside every PEC
writable surface). Fold into gate question Q2.

## §2 SCA-002 input inventory (STEP 2)

**Owner ruling (2026-07-25, verbatim choice):** "SCA-002 first" — the
deliverable→objective mapping is completed in **decomposition truth**
before any SOW authoring; a SOW-local attribution convention was declined.

**STEP 2a — opening packet required (R1a-F1).** SCA-002's writes
(`execution/_Decomposition/SOFTWARE_DECOMP.md`, `ScopeLedger.csv`,
`Deliverables.csv`, `_LATEST.md`, `execution/_ScopeChange/SCA-002_*/`,
affected `_CONTEXT.md`) are all outside the default writable surface, and
`AGENT_SCOPE_CHANGE.md`'s SOFTWARE default `ALLOWED_PROPAGATION_WRITES`
does not reach the companion CSVs. PROJECT_SETUP drafts an owner-ruled
opening packet (D-PEC-61 is the exact precedent shape: session
authorization + enumerated SCOPE_CHANGE fence released gate-by-gate,
explicitly including the companion registers and `_CONTEXT.md`
propagation) plus this intake package; the owner rules it, then **the
owner invokes SCOPE_CHANGE** (STEP 2b). PROJECT_SETUP yields while the SCA
is active and resumes from `_ScopeChange/_LATEST.md` + `Handoff_State`.

**Gap (measured against rev 1.1; R1b-corrected framing):** **31 of 71 IN**
ledger rows have empty ObjectiveIDs (the accepted basis's own §7 metric:
"IN items without objective mapping | 31 (intentional best-effort
posture)"); **26 of 64 deliverables** have empty SupportsObjectives —
**17 of the 32 wave members, including 7 of 9 pilot roots**. The 14 OUT +
9 TBD ledger rows are unmapped **by design** ("Deferred/OUT and TBD items
map to no objective by design", §3) and are **out of SCA-002's scope**.
The wave blocker is the deliverable-side gap (SupportsObjectives), which
feeds SOW frontmatter.

**Why it blocks:** the SOW validator hard-requires non-empty
`package_objective_refs` (`tools/scope_of_work/common.py:213-215`); matrix
rows can satisfy the per-OUT objective check with `SOW-*` refs via the
union rule (`common.py:251-253` builds the union; `:266-267` consumes it),
so the frontmatter field is the binding constraint.

**Warrant evidence for the session (all R1b-verified):**
- DIRECT (15 wave members, register-mapped, no SCA action needed):
  DEL-01-04, DEL-03-01..04, DEL-04-01, DEL-04-02, DEL-04-03, DEL-04-05,
  DEL-08-03, DEL-08-04, DEL-10-01, DEL-10-02, DEL-10-10, DEL-10-11.
- INDIRECT-§3 (8): DEL-01-01, DEL-02-01..07 — §3 states a **positive
  derivation**: "parser items (SOW-011..017) underlie OBJ-001/OBJ-002
  through the record tier (SOW-001)" → candidate [OBJ-001, OBJ-002].
- NEEDS ATTRIBUTION (9): DEL-00-01 (SOW-088, §13), DEL-00-03 (SOW-089,
  §13), DEL-01-03 (SOW-056, PEC-SVC-005), DEL-01-05 (SOW-052/053,
  PEC-SVC-001/002), DEL-01-06 (SOW-094, "§12 P2, PEC-DSH-002" → evident
  candidate OBJ-004), DEL-03-06 (SOW-054, PEC-SVC-003), DEL-08-01
  (SOW-003/040, §8 + PEC-API-001), DEL-08-02 (SOW-042, PEC-API-003),
  DEL-10-03 (SOW-025, PEC-GAT-004/K-AUTH-1). Method: ledger SourceRef →
  PRD function row → the §3 objective whose outcome that function serves;
  candidates developed in-session, owner-ruled at Gate 3.
- **Tension for Gate 3 (narrowed per R1b-F9):** §3's "intentionally not
  force-mapped" clause applies only to ingest/bridge items SOW-033..039 —
  none in the wave. The session therefore debates only the register
  **representation** of the mappings (direct vs qualified/indirect form),
  not whether §3 forbids them. **Hard constraint to present at Gate 3
  (R1a-F8):** whatever representation is chosen, `ObjectiveIDs` /
  `SupportsObjectives` must keep **bare `OBJ-NNN` tokens** — any qualifier
  lives in a separate column or §3 notes, never inside the token: the SOW
  validator token-splits frontmatter lists and matrix cells, and qualified
  tokens break both.

**SCA-002 endpoint:** `SOFTWARE_DECOMP.md` revision 1.2 `current_basis`
with every **deliverable** (at minimum every wave deliverable) carrying a
non-empty objective reference set across `ScopeLedger.csv` ObjectiveIDs
(IN rows only), `Deliverables.csv` SupportsObjectives, §3
MappedDeliverables + mapping-notes reconciliation, **plus** (R1a-F12) the
§8 Change Log amendment entry and a Gate-2/3 ruling on whether a
`Supersession_Delta.csv` binding is owed for the superseded best-effort
posture. **Gate 4/5 propagation includes the affected scaffolded
`_CONTEXT.md` files** (their SupportsObjectives lines restate rev 1.1) —
that is the SCOPE_CHANGE protocol default for MODIFY and belongs in the
SCA fence; it must NOT be deferred to D-PEC-63, whose fence excludes
`_CONTEXT.md` (R1a-F4). No topology change of any kind. Immutable
evidence under `execution/_ScopeChange/SCA-002_*/`; pre/post
register-integrity comparison bounded to the IN-row + deliverable gap
(so Gate 5 does not spuriously fail on the by-design OUT/TBD rows).

**R-2a corrections to this section (2026-07-25, STEP 2a; the intake file
is now the authoritative statement):** (1) **SOW-021** (PEC-RCN-006 →
DEL-03-01, B4) is an in-wave unmapped IN row on an already-mapped
deliverable — the only one outside the 17; O-A includes it (20 IN rows
total; residue 11 rows, all out-of-wave). (2) The intentional-unmapped
clause lives in **§3 Mapping notes** (not DL-14, which covers only
SOW-063), and its unmapped members are **SOW-033..038** (SOW-039 is
mapped to OBJ-003). (3) The operative consistency rule is the **union
invariant**: deliverable `SupportsObjectives` = union of covered IN
rows' `ObjectiveIDs` (0 violations at baseline; checker in intake §8).
(4) Token-mechanism correction: no frontmatter format regex exists; the
matrix check splits on comma/whitespace only; registers are
`;`-separated — the binding rule is **brief construction** (split `;`,
emit inline YAML list of bare tokens); a `;`-joined cell copied verbatim
into `PACKAGE_OBJECTIVE_REFS` becomes one unusable token. (5) The SCA
fence must include `execution/_Evaluation/DecompCoverage/**` (AUDIT_DECOMP
Gate 1/5 baselines) and `ContextBudgetQA.csv`; `_CONTEXT.md` in-fence for
all 64 with a two-line-class constraint (mapping restatement + rev
pointer, refresh-or-deferred at Gate 4).

## §3 Canonical authoring TASK brief (STEP 4; template)

Concrete sample (root DEL-01-06); per-deliverable substitutions:
`ScopePath`, `PROJECT_SCOPE_REFS` (from CoversScopeItems),
`PACKAGE_OBJECTIVE_REFS` (bare OBJ-NNN tokens from post-SCA registers),
PRD anchors in CustomInstructions, upstream-SOW read list for tiers ≥ 1.

```markdown
PURPOSE: Initialize the SOW_V1 production contract for one PEC deliverable (MODE=INIT).
RequestedBy: PROJECT_SETUP
WorkingRoot: {REPO_ROOT}/projects/pec
ScopePath: {REPO_ROOT}/projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default
TaskSkill: scope-of-work

Tasks:
  - Load skills/scope-of-work/SKILL.md + BRIEF_SCHEMA.md + TOOL_POLICY.md + QA_CHECKS.md.
  - Read the deliverable-local truth set (_CONTEXT.md, _REFERENCES.md, _DEPENDENCIES.md,
    Dependencies.csv, _STATUS.md) and the grounding sources in CustomInstructions.
  - Author {ScopePath}/ScopeOfWork.md as a source-grounded SOW_V1 contract.
  - Run `python3 tools/scope_of_work/validate_scope_of_work.py "{ScopePath}"` until PASS.
  - Run `python3 tools/scope_of_work/derive_review_checklist.py "{ScopePath}"` to stdout;
    report item_count + production sha256 in the run record; do not persist the JSON.

ApplyEdits: true
AllowedWriteTargets:
  - {ScopePath}/ScopeOfWork.md
  - {ScopePath}/_run_records/

RuntimeOverrides:
  MODE: INIT
  DELIVERABLE_PATH: {ScopePath}
  DECOMPOSITION_BASIS: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
  PROJECT_SCOPE_REFS: [SOW-094]
  PACKAGE_OBJECTIVE_REFS: [{bare OBJ-NNN tokens from post-SCA registers}]
  SOURCE_STATE: OPEN
  RENDER_HTML: false
  DECOMP_VARIANT: SOFTWARE
  PHASE: PROJECT_SETUP_PHASE_2_2
  STATUS_POLICY: NO_STATUS_TOUCH

CustomInstructions:
  - Lifecycle: this run never touches _STATUS.md (skill constraint honored); the
    OPEN→INITIALIZED advancement is a separate deterministic act under D-PEC-63 §3.2.
  - Grounding order (no invention; unknowns stay TBD): (1) ScopeLedger.csv row(s) and their
    SourceRef into projects/pec/docs/PRD.md; (2) SOFTWARE_DECOMP.md §5 row + ContextEnvelopeNotes;
    (3) deliverable-local control files; (4) tiers ≥1 only: the INITIALIZED ScopeOfWork.md of each
    upstream deliverable in Dependencies.csv.
  - Do not modify _STATUS.md, _CONTEXT.md, _REFERENCES.md, _DEPENDENCIES.md, Dependencies.csv,
    _SEMANTIC.md, or anything outside {ScopePath}.
  - Frontmatter uses INLINE list syntax ([SOW-094]); YAML block lists fail the parser; no duplicate
    keys; decomposition_basis must contain "@".
  - Exactly these six L2 headings in order: Purpose and Objective Traceability; Deliverable
    Definition — Ontology; Completion and Reliance Basis — Epistemology; Production and
    Verification Method — Praxeology; Governing Values and Decisions — Axiology; Output and
    Evaluation Matrix.
  - 3-digit local IDs (OUT-001…); never define REM-*; every referenced ID defined; every defined
    OUT/AC/VER appears in the matrix. Matrix header verbatim:
    | Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
    Objective-refs cells cite the SOW-* items (and OBJ-* additively, bare tokens).
  - State the objective warrant explicitly in Purpose and Objective Traceability (register-direct
    vs SCA-002-qualified, per the amended registers).
  - The deliverable is at OPEN with no implementation: acceptance criteria state the contract the
    future implementation must satisfy — never assert anything is built. Open issues become CON-*
    records, not resolutions (OI-012 in DEL-00-01; OI-006 in DEL-08-01; OI-003 in DEL-01-06).
    DEL-01-05 is a standing assertion (C-08) — author it as such, not as a one-shot artifact.
  - Tests may implement a verification method; they may never create scope or acceptance criteria.

ExpectedOutputs:
  - {ScopePath}/ScopeOfWork.md (PASS format=SOW_V1)
  - {ScopePath}/_run_records/TASK_RUN_*.md
  - Structured return: RUN_STATUS, ResolvedSkillVersion, CompanionFiles, validation result,
    production sha256, checklist item_count, CONFLICT/TBD/CON roll-up
```

Notes: `FORMAT_AUTHORITY_REF` is deliberately omitted (CONVERT-only).
`STATUS_POLICY: NO_STATUS_TOUCH` is the only defined vocabulary value that
matches the design (the scope-of-work skill itself has no STATUS_POLICY
handler — the field is PROJECT_SETUP-mandated brief metadata; the contract
gap is routed with Q1/Q2).

**Status act (per batch, after fan-in; R1a-F5/F11 shape):** one
generic-shell TASK (no skill), opus-5:
- `ScopePath: {WORKING_ROOT}/execution/_Coordination/WAVE_D-PEC-63`
- `AllowedWriteTargets`: the batch's explicit `<DEL_PATH>/_STATUS.md`
  list **plus `{ScopePath}/_run_records/`** (TASK hard-requires the
  run-record enclosure).
- Per deliverable: re-run `python3 tools/scope_of_work/validate_scope_of_work.py "<DEL_PATH>"`;
  only on `PASS format=SOW_V1` run
  `tools/scaffolding/write_status.sh "<DEL_PATH>" INITIALIZED "TASK+status-advance"`
  (`write_status.sh` takes a **path**, not an ID; forward-only guard). On
  any FAIL: skip, do not advance, report.
The scope-of-work skill's `_STATUS.md` prohibition is honored, never
overridden (its `allowed-tools` frontmatter + TASK's intersection rule
foreclose in-run status writes). Warrant:
`docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` §8 under D-GOV-16 (RULED
APPROVED 2026-07-12, `docs/governance_harness/_DECISIONS/_REGISTER.md:29`).

## §4 Verification commands + calibrated values (run everything from {REPO_ROOT})

- Per-deliverable: `python3 tools/scope_of_work/validate_scope_of_work.py "<DEL_PATH>"`
  → `PASS format=SOW_V1`, exit 0 (independent re-run at fan-in — never
  trust self-report). `derive_review_checklist.py` per deliverable, exit 0.
- Census (NEVER `count_workspace_state.sh` after the first transition —
  history-substring defect):
  `grep -h '^\*\*Current State:\*\*' projects/pec/execution/PKG-*/1_Working/DEL-*/_STATUS.md | sort | uniq -c`
  INITIALIZED ladder after B1→B8: **9, 12, 18, 19, 25, 29, 31, 32**.
- Scope per batch (R1a-F16 formula): `git status --porcelain` shows
  exactly n new `ScopeOfWork.md`, n modified `_STATUS.md`, **n+1**
  run-record additions (n authoring + 1 status act), plus
  `WAVE_D-PEC-63/BATCH_B{n}_FANIN.md` and `BLOCKER_STATE_*_B{n}.md` and
  the plan's position-marker edit. Zero other paths.
- Blocker snapshot per batch:
  `python3 projects/pec/execution/_Coordination/WAVE_D-PEC-63/report_blocker_state.py projects/pec/execution --output projects/pec/execution/_Coordination/WAVE_D-PEC-63/BLOCKER_STATE_<date>_B{n}.md`
  Exit 0 = completed report; exit 2 = IO/parse failure → halt (never a
  blocker verdict). Baseline (verified twice, pre/post script patch):
  **54 BLOCKED / 10 UNBLOCKED** (9 roots + DEL-10-11 standing-edge
  divergence, expected and named); rows 255 = ANCHOR 135 + EXECUTION 120 +
  other 0. Closure: **40 UNBLOCKED / 24 BLOCKED, all 32 wave members
  UNBLOCKED** (R1b-simulated; the 8 non-wave beneficiaries: DEL-00-02,
  DEL-01-02, DEL-03-05, DEL-04-04, DEL-05-01, DEL-05-02, DEL-09-06,
  DEL-10-04).
- Structural invariant at every batch:
  `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution`
  unchanged from D-PEC-62 landing (64 files, 255 rows, 135 ANCHOR /
  120 EXECUTION, 62 nodes / 120 edges, orphans 2, SCCs 0).
- Basis md5s (§7 rev-1.2 pins) re-checked pre-batch; mismatch → halt.
- `scan_deliverable_consistency.py` output is advisory reading only.
- Failure rules: single FAIL → deliverable stays OPEN, fresh sealed
  re-dispatch (never repair inline); two consecutive FAILs on one
  deliverable, or any CONFLICT return → owner halt.
- Skill-version freeze: `chirality-skill-version: "1"`; drift mid-wave halts.

## §5 Owner-gate questions (present at the D-PEC-63 ruling, STEP 3)

- **Q1 — semantic-phase posture.** SOFTWARE protocol runs Phases 2.3/2.4/
  2.5 after 2.2, but Phase 2.5 for SOW_V1 has a contract gap (the
  scope-of-work skill has no P3/enrichment mode; also no STATUS_POLICY
  handler — see §3 note). Options: (a) run 2.3+2.4 after the wave, hold
  2.5 pending a skill-contract fix routed to HELPS_HUMANS; (b) declare the
  semantic pipeline unused for PEC → straight to WORKING_ITEMS activation;
  (c) full chain after the skill fix lands.
- **Q2 — tooling/skill-contract consolidation packet** (candidate ID after
  the SCA opening packet): OI-013 register validator; the
  `count_workspace_state.sh` history-substring defect; the missing
  `validate_semantic_pipeline_scope.py --step init` guard; the
  scope-of-work INIT-mode companion-file branches (R1a-F7) — vs
  review-based verification standing.

## §6 Refutation log

**R1 (2026-07-25, pre-compaction; refuters a60b41fb6c667e676 [R1a
governance/contract] and af97aca8e66acebd8 [R1b arithmetic/graph], both
opus-5, on this plan + the D-PEC-63 draft + the blocker script).**
26 findings; all dispositioned ACCEPTED and applied 2026-07-25 before the
pause:

- R1a-F1 (CRIT): SCA-002 writes exceed default surface; no packet → STEP
  2a opening packet added (§0/§2). R1a-F2 (CRIT): Agent1→Agent1 dispatch
  forbidden → owner invokes SCOPE_CHANGE; PROJECT_SETUP yields (§0/§2).
- R1a-F3 = R1b-F1 (MAJ): tiering convention pinned raw-edges; DEL-10-11
  divergence named (§1). R1a-F4 (MAJ): `_CONTEXT.md` refresh belongs to
  the SCA fence, not D-PEC-63 (§2). R1a-F5 (MAJ): status-act ScopePath +
  run-record enclosure fixed (§3). R1a-F6 (MAJ): STATUS_POLICY →
  NO_STATUS_TOUCH (§3). R1a-F7 (MAJ): canary-failure routing to
  HELPS_HUMANS; skills/ unwritable (§1, Q2). R1a-F8 (MAJ): third re-pin —
  bare OBJ-NNN tokens (§2, §7). R1a-F9 (MAJ): this log filled pre-pause.
- R1a-F10 = R1b-F2 (MAJ/MIN): blocker command repo-root-relative (§4).
  R1a-F11 (MIN): `<DEL_PATH>` + actor `TASK+status-advance` (§3).
  R1a-F12 (MIN): SCA endpoint adds §8 Change Log + supersession ruling
  (§2). R1a-F13 (MIN): exit-code semantics corrected (§4 + packet §3.4).
  R1a-F14 (MIN): path anchors in §0; packet §3.2 cross-ref fixed.
  R1a-F15 (MIN): batch-commit actor named — D-PEC-63 §3.6 clause
  authorizes PROJECT_SETUP scoped batch commits under project closeout
  discipline (owner rules it with the packet). R1a-F16 (MIN): scope
  formula n+1 (§4). R1a-F17 (MIN): DAG-exhibit staleness annotation (§7).
- R1b-F3 (MAJ): gap reframed 31-IN / 26-deliverables; OUT/TBD by-design
  out of scope (§2). R1b-F4 (MAJ): script prints full row accounting +
  asserts closure (patched; baseline regenerated, identical verdicts).
  R1b-F5 (MIN): out-of-vocabulary RequiredMaturity → exit 2 (patched).
  R1b-F6 (MIN): dead `--threshold` flag removed (patched). R1b-F7 (MIN):
  IO paths wrapped → exit 2 (patched). R1b-F8 (MIN): union-rule citation
  corrected to `common.py:251-253` + `:266-267` (§2). R1b-F9 (MIN):
  Gate-3 tension narrowed to representation only (§2).

Clean categories confirmed by R1b (independent recomputation): wave
membership 32; tier table B1–B8 exact; ladder 9/12/18/19/25/29/31/32;
baseline 54/10 with the exact UNBLOCKED set; closure 40/24 all-wave-
unblocked; DIRECT-15/INDIRECT-8/ATTRIB-9 partition; structural invariant;
basis md5s; C-08 set; state regex safety; union rule real.

**R-2a (2026-07-25, STEP 2a; refuters a68bdbe6ad25a3551 [governance/
contract] and abf0b1bf486fc9a2c [data/arithmetic], both opus-5, on the
D-PEC-64 opening packet + SCA-002 intake).** 25 findings (17 gov + 8
data, 3 overlapping); all dispositioned ACCEPTED and applied 2026-07-25
via full rewrites of both artifacts before presentation:

- Gov-1 (CRIT): fence omitted `_Evaluation/DecompCoverage/**`
  (AUDIT_DECOMP Gate 1/5 baselines — SCA-001 provably wrote it; session
  would stall at Gate 1) → added to §3.2. Gov-3 (MAJ): yield trigger was
  keyed to `_ScopeChange/_LATEST.md`, which the protocol writes only at
  Gate 5 → yield now keyed to the ruling act itself (packet §2.4).
  Gov-2 (MAJ): all 64 `_CONTEXT.md` pin rev 1.1; ~47 would be left
  stale → all 64 in-fence with two constrained line classes,
  refresh-or-recorded-deferral at Gate 4. Gov-4 (MAJ): ContextBudgetQA
  caveat misquoted (D-PEC-61 has it IN the fence; SCA-001 edited it) →
  in-fence, expected-unchanged clause; Companion_Inventory caveat kept
  to that file alone. Gov-5 (MAJ): rollback claim "nothing outside
  _ScopeChange/** before Gate 5" false → rewritten accurately. Gov-6
  (MAJ): bounded comparison exempted exactly the rows that must prove
  unchanged → window now = Gate-1-ruled scope only; residue rows must
  be byte-identical. Gov-7 (MAJ): no commit actor → §3.6 git-acts
  clause (opening + closure commits by PROJECT_SETUP; protocol hands
  off a file list). Gov-8=Data-4 (MAJ): "DL-14" misattribution; range
  is SOW-033..038 (SOW-039 mapped) → corrected. Gov-9+Data-1 (MAJ):
  "consistent ObjectiveIDs" undefined / SOW-021 hidden in DIRECT class
  → union invariant stated + SOW-021 named, O-A includes it. Gov-10
  (MAJ): CSVs are AUTHORITATIVE_TRUTH not propagation;
  ALLOWED_PROPAGATION_WRITES narrows only → fence rationale + gate
  sequencing rewritten. Gov-11 (MAJ): derivative-package classification
  obligations absent → intake §6.5 + packet §4.5. Gov-12 (MIN):
  Supersession_Delta.csv (not Map) → fixed. Gov-13=Data-2/3 (MAJ/MIN):
  claimed token-breakage mechanism false; real hazard is the `;`
  separator vs comma/whitespace-splitting brief construction →
  intake §5.1 rewritten with accurate mechanics + conversion rule.
  Gov-14 (MIN): parser-shapes-truth inversion now surfaced. Gov-15
  (MIN): ruling text now adopts intake §1 as the owner's own change
  request. Gov-16+Data-6 (MIN): verification checks made runnable
  (per-token regex after `;`-split; census command named; git status
  vs enumerated allowlist; `git diff --check` demoted; scope-
  conditional endpoint). Gov-17 (MIN): `projects/pec/docs/STATUS.md`
  exclusion qualified; `_COORDINATION.md` ruling item added; AGENTS.md
  pointer refresh scheduled; receipt append moved into the resumption
  sequence. Data-5 (MIN): §7 metric quoted in full. Data-7 (MIN):
  K-AUTH-1 is Notes, not SourceRef → reworded. Data-8 (MIN):
  "fed from register truth" restated as a brief-construction
  convention, not a pipeline.

Clean categories (R-2b independent recomputation): all three md5 pins;
94=71/14/9; the 31-row block character-exact; 26 = 17+9 partition;
DIRECT-15 all mapped; 7-of-9 pilot roots; envelope S28/M34/L2; §3/DL-14
quotes verbatim (location corrected); common.py citations 213-215/
251-253/266-267 accurate; analyze_dep_closure landing values exact;
census 64 OPEN; 11 packages / 6 objectives; O-C straggler triples;
intake §8 commands run verbatim. R-2a-gov clean categories: `_STATUS.md`
narrowing legitimate and correct; Agent1→Agent1 prohibition correctly
stated; `_CONTEXT.md` claimed by exactly one packet.

**R-2b-g1 (2026-07-25, STEP 2b; refuter aa51d56df4267951b, opus-5, on
the SCOPECHANGE-SCA002 Gate 1 return before presentation).** 10 findings
(4 MAJ), dispositions applied at Agent 0 fan-in:
F1+F2 (MAJ, ACCEPTED): W-1 "ride along at Gate 3" unlawful as offered —
Gate 3 admits no unparsed action, and the §5-prose fix breaches D-PEC-64
§4.3's byte-identity window; corrected owner options = Gate 1 correction
(add A007 + dated owner amendment of §4.3 window) or separate future
amendment. F3 (MAJ, ACCEPTED): intake §6.5 derivative-package table
obligation dropped from carried open items → relayed into the Gate 2
dispatch brief. F4 (MAJ, ACCEPTED-AS-RECORDED): the sole WARNING row in
the coverage IssueLog has invalid CheckNumber=96 (schema says 1–11;
AUDIT_DECOMP contract itself inconsistent: schema 1–11 vs 12 checks) —
routed to Q2 tooling consolidation. F5 (MIN): W-1 is MODIFY-legal;
excluded by §4.3 window/subject scope, not change class — presentation
corrected. F6 (MIN): child's F-3 (applies-vs-supersedes) is interpretive
(§7:528 folds parser rows into the intentional posture) — presented as
interpretation. F7 (MIN): Pre_Change_Coverage.json +
Amendment_Actions.csv missing from snapshot vs precedent → deferral
recorded; produce at Gate 3/pre-Gate-5 (relayed). F8/F9/F10 (MIN,
ACCEPTED-AS-RECORDED): coverage SCOPE=ALL over-broad but conservative;
two additive JSON fields beyond schema (→ Q2); baseline timestamp 2 min
before gate-open, md5s stable across interval. Clean under attack: fence
(11 paths, all in-fence; DecompCoverage/_LATEST.md pointer-overwrite
authorized), all md5s, option widths 20/17, 24/20, 31/26 + residues,
F-2 union-window constraint (and its symmetric DEL-07-01 case), W-1
substance real (§5:376 "29 S / 33 M" vs registers 28/34), six-action
list faithful+complete vs intake and reproduced owner-facing, every
cited line number, coverage numbers vs disk, dep-closure values,
_ScopeChange/_LATEST.md untouched.

**R-2b-g2 (2026-07-25, STEP 2b; refuter a19cf58230e2eac7c, opus-5, on
the SCOPECHANGE-SCA002 Gate 2 return before presentation).** 14 findings
(8 MAJ / 6 MIN), dispositions applied at Agent 0 fan-in — all relayed to
the instance as required corrections before the Gate 2 owner
presentation:
F1 (MAJ, ACCEPTED): OPEN_PENDING_DERIVATIVE_CLOSURE reasoning refuted by
SCA-001 precedent (CLOSED_FOR_SCOPE_CHANGE_ONLY coexists with
DownstreamRerunState=FROZEN out-of-fence obligations; DerivativePackage-
State scoped to decomposition-local surfaces) → expected verdict
corrected to CLOSED_FOR_SCOPE_CHANGE_ONLY + FROZEN obligations, final
call at Gate 5. F2 (MAJ, ACCEPTED): projects/pec/AGENTS.md carries no
revision pin (deliberately revision-agnostic) — row-10
STALE_ON_ACCEPTANCE claim false for that file; corrected (the D-PEC-64
closure pointer refresh is a chosen act, not staleness repair).
F3+F4+F5 (MAJ, ACCEPTED): owner question 3 withdrawn from Gate 2 —
DEP-02-01-003's declared EvidenceFile is the frozen DAG exhibit (not
SOFTWARE_DECOMP.md), so A003 does not break the row's anchor;
preserve-verbatim conflicts with A003/A004's reconciliation mandate and
§7:528's changed in-document function; parser-sentence handling routed
to Gate 3 drafting + its refutation pass. F6 (MAJ, ACCEPTED):
no-binding supersession recommendation is lawful (refuter-verified:
self-description is not upstream admitted authority; SCA-001 precedent
exact) but made CONDITIONAL on Gate 3 attributions remaining
consumptive of PRD (re-affirmed at Gate 3). F7 (MAJ, ACCEPTED): §3
classification normalized to the contract enum
(DIRECT_EDIT|RECOMPUTE|NO_CHANGE) so Gate 5 Handoff_State can carry it.
F8 (MAJ, ACCEPTED): §2 ContextBudgetQA "must not change" contradiction
with §3/D-PEC-64 §3.2 corrected to expected-unchanged/Gate-3-text-only.
F9–F13 (MIN, ACCEPTED): "§7 re-pin point 4" cite fixed (annotation is
enumerated as not-a-point); DAG-exhibit annotation partly extant (2 of
8 refs are the annotation); "0 of 255 rows carry SupportsObjectives"
rephrased (no such column); converter "cannot be invoked" softened
(argparse requires the flag, not a legal value); §6 removed from A001's
affected list. F14 (MIN, ACCEPTED): stale W-1 characterization at D-5
annotated as superseded by C-1 in place. Clean under attack: A001/A002
sets exact (incl. DEL-03-01 exclusion structurally safe — no A001 row
touches residue deliverables); package set PKG-00/01/02/03/08/10 both
sides; union invariant 0; OI-B real (64 _REFERENCES.md, fence-excluded,
absent from intake §6.5); DEP-02-01-003 1-of-255 verbatim; A007 exact
incl. the two L deliverables surviving; supersession tooling
(--allow-empty, no --delta) precedent-exact; both closure-verdict
values legal; Gate 2 contract outputs complete; fence 3 paths; md5s
unchanged; §3/register agreement 9/4/12/9/2/9 and 10/4/13/9/2/9.

**R-2b-g3 (2026-07-25, STEP 2b; refuters aecdbaa2131e10179
[governance/warrants] and a2d9b9cd8c49b6c9e [arithmetic/simulation —
independently applied the full amendment in scratch], both opus-5, on
the Gate 3 drafting package).** 26 distinct findings (2 CRIT / 10 MAJ /
14 MIN), all ACCEPTED at fan-in; revision relayed before presentation:
G1 (CRIT): A008's "inside the window" claim false — front matter is not
§3/§7/rev-history/mapping-notes; needs a dated §4.3 amendment (A007
precedent); Q4 must carry that rider. G2=A-M1 (CRIT): exact text valid
only under recommended Q1/Q2 answers ("OBJ-003/OBJ-006 unchanged" false
under 3 of 5 alternatives; Q2-narrow erases the OBJ-002 edit); package
must state non-recommended rulings force re-derivation + re-simulation
+ re-presentation. G3 (MAJ): DEL-10-03 HIGH unwarranted — SOW-055
precedent tautological; K-AUTH-1 boundary stated by no §3 objective
(the DL-14 abstention condition) → escalated to per-row ruling with
honest framing. G4 (MAJ): DEL-08-02 is MEDIUM (Part-5 "six are
HIGH/MEDIUM-HIGH" false on its face) and weakest on merits →
escalated. G5 (MAJ): DEL-01-05 calibration inconsistent with row 1
(same ADR-002 chain, different treatment) → aligned. G6=A-M2 (MAJ):
A003d writes a false DL-14 citation into decomposition truth
(ingest/bridge intentionality lives in §3 notes, not DL-14) → text
fix. G7 (MAJ): Companion_Inventory/ContextBudgetQA Gate-3
determinations absent (D-PEC-64 assigns them to Gate 3; SCA-001 had
explicit sections) → added. G8 (MAJ): A006 defers _LATEST.md body past
the approval gate vs SCA-001 full-text precedent → full successor text
with marked to-be-measured slots. G9 (MAJ): Q2-narrow ambiguous on
SOW-001 → both variants defined. G10 (MAJ): SOW-054 warrant truncated
at the clause pointing to OBJ-002 ("incremental reconcile within
seconds") → full quote + alternatives, escalated. G11 (MAJ): A005a
(§11 Decision Log) outside the narrow §4.3 reading — one consistent
reading applied; the Q4 dated amendment admits A005a + A008 together;
A006's authority (§2.3/§3.2, outside byte-window) stated. MINs
(G12–G18, A-M2..M8): duplicate Gate 3 heading; stale Gate 2 header;
CSV row 3 non-deterministic ("optionally") → resolved post-Q3;
DownstreamReruns SCOPE_CHANGE_POSTCHECK restored + NONE replaced;
"retained verbatim" precision (substring survives, sentence edited);
Explicit-unchanged-surfaces section added; simulation JSON provenance
(md5 pins) added; Part-4/Part-5 cross-ref; §8:218 soft-wrap and
§9.7:300 inserted-bold quote nits; SOW-038/DL-11 tension recorded;
A008 DownstreamReruns aligned. Clean under attack (arithmetic refuter
applied the amendment end-to-end): all 16 single-line + 2 multi-line
old-text pairs byte-exact; union invariant 0 post; residue sets exact;
20+17 rows only, two columns only; §3 per-objective sets exact
(22/12/13/10/9/9 items, 20/12/12/10/7/9 dels); §7 metric 11 under
every alternative; purpose test — wave unmapped 17→0, residue∩wave=∅;
all 13 PRD warrants verbatim at anchor; I5 append-only held; CSV
schema byte-identical to SCA-001; fence clean; md5s unchanged.

**R-2b-g4 (2026-07-25, STEP 2b; refuter ab4a462ff0371098e, opus-5, on
the Gate 4 Propagation Plan).** 22 findings (2 CRIT / 12 MAJ / 8 MIN),
all ACCEPTED; plan revision ordered before presentation:
C1: Gate 5 never wrote Decision_Log.md (contract + SCA-001 require it)
→ added to sequence/manifest. C2: the 17 _CONTEXT.md mapping-line edits
had no approved/planned exact text (Gate 5 would invent values) → exact
old→new per file added, derived from the approved A002 cells. M3+M4:
post-change AUDIT_DECOMP sequenced before the _LATEST writes it
validates, and without EXPECTED_SOURCE_SNAPSHOT/handoff-phase params →
re-sequenced post-repoint with rev-1.2 citation params. M5: ambiguous
pre/post line coordinates on four net-insertion sites → pre-change
coordinates + post-change anchor map declared. M6: "192 files" wrong
(row-count arithmetic; correct 256) + _SEMANTIC.md unclassified →
fixed. M7: CURRENT/STALE_REBUILD_REQUIRED/DEFERRED_BY_HUMAN
classifications lost between Gates 2 and 4 → restored for
Handoff_State. M8 (load-bearing): option-(i) cost claim inverted —
full refresh COLLAPSES the post-check (zero stale pointers repo-wide)
while partial refresh carries a permanent 47-file exception. M9
(load-bearing): the OI-B equivalence doesn't hold (OI-B is
fence-forced; the 47 is elective despite authority) and a 17/47
partial refresh is a third posture D-PEC-64 §3.2 never contemplated →
recommendation FLIPPED to (i) full 64-pointer refresh with P-supersede
text; (ii) presented as alternative requiring an explicit owner
authorization of the partial posture. M10: Amendment_Actions.csv
lacked the propagation writes → extended. M11: "finalize CSV" step
already discharged at Gate 3 → dropped; SCA-001 snapshot-immutability
posture adopted. M12: Handoff_State scope completed to the contract's
four sections; seven state fields relocated to RUN_SUMMARY. M13:
post-change front-matter↔_LATEST parity assertion added. M14:
register-integrity baseline JSONs restored to SCA-001 schema (citing
the audit) instead of raw copies. MINs m15–m22: two-line/three-line
arithmetic (51/145 not 17/64+17); --output-map required arg; 10 not 9
edit sites; Decision_Log stale rows; CSV DownstreamReruns normalized +
CHANGE-vs-PROJECT_SETUP owner inconsistency resolved; §4 table gains
the dropped items (register row, packet update, wave-plan updates,
OI-A, OI-013, and the plan's entire point: D-PEC-63 BLOCKED→UNBLOCKED
effect); _REFERENCES.md class corrected to Gate 2's
STALE_DEFERRED_BY_FENCE; P-swap "false claim" softened (status: field
reading is defensible; P-supersede still preferred as unambiguous).
Clean under attack: the 64-file basis-block byte-identity measurement
(md5-verified 64/64), every §3 line anchor, postcheck↔approved-text
bijection (no creep, no omission), git posture (no SCOPE_CHANGE
commits; PROJECT_SETUP closure commit per §3.6(b)), fence, md5s,
coverage-run naming parity, wave-plan §7 obligations fully carried,
supersession chain, option-(iii) incoherence, D-21.

**Future rounds:** R2 post-B1 (contract quality), R3 post-B2 (upstream
citation), R4 pre-closure (numbers/receipt/pointer audit) — plus a
refutation pass on D-PEC-63 draft v2 (STEP 3). Log all here.

## §7 Basis freeze + git anchors + re-pin list

- Accepted basis now (**RE-PINNED 2026-07-25 post-SCA-002**):
  `SOFTWARE_DECOMP.md` **rev 1.2** md5
  `961e8e959b7d1965cd1d4153c69a9c43`; `Deliverables.csv`
  `3f807d502df3ed1f35326baed890832a`; `ScopeLedger.csv`
  `9ece6f49fb5fc7f83f72fa897d01a325`; rev-1.2 commit **`3623b958b`**
  (the SCA-002 closure commit). Historical rev-1.1 md5s are preserved in
  the DAG gate exhibit §1 and in `_ScopeChange/SCA-002_*/Brief.md`.
- **Re-pin after SCA-002 — EXECUTED 2026-07-25:** (1) md5s + commit SHA
  above; (2) `{REV_1_2_COMMIT}` in §3's `DECOMPOSITION_BASIS` =
  `3623b958b`; (3) bare `OBJ-NNN` tokens confirmed in the amended
  registers (post-state token scan: 0 non-`^OBJ-[0-9]{3}$` tokens after
  `;`-split); DAG-exhibit §1 pins annotated as rev-1.1 historical
  provenance (topology unchanged by SCA-002).
- D-PEC-62 closeout commit: `c5e3a6ebd` (branch
  `claude/project-setup-agent-config-5c0d34`, fast-forwarded to local
  `main` 2026-07-25; not pushed). Owner note of record: "merge but it may
  be revised again before being put to use."
- Wave commits: one scoped commit per batch (rollback granularity;
  `write_status.sh` blocks backward transitions — revert is the only
  walk-back), performed by PROJECT_SETUP under the D-PEC-63 §3.6 clause.
- Receipt/rollback lesson (D-PEC-62): revert deletes the receipt line —
  rollback = revert + follow-on commit annotating the receipt superseded +
  manual removal of untracked `_run_records/` residue.
