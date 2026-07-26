# D-PEC-62 — DRAFT: Project Setup build tranche 1 — scaffolding + deliverable-local dependency registers

**Status:** RULED 2026-07-25 — owner selected "RULED as drafted" at the
in-session gate: the proposed §7 ruling text applies verbatim, including
the flags-as-flags reading and the C-08 standing-node exclusion.
(Drafted 2026-07-25 by PROJECT_SETUP at owner direction; engine/model of
drafting run: claude-fable-5; draft v1 adversarially refuted — 25 findings
— and revised; refuter session a6c21e82ca668384c)
**Decision ID:** D-PEC-62
**Structure precedent:** `D-PEC-60`/`D-PEC-61` (human-gated session packets);
`docs/STATUS.md` gate 1 ("Each tranche requires its own owner-ruled `D-PEC`
packet")

## 1. Owner direction of record (2026-07-25, in-session gate answers)

1. Landing instrument: a `D-PEC-62` packet (this document).
2. Phase 1.3 dependency maturity threshold: **`INITIALIZED`**.
3. Register storage: **deliverable-local**, not central — verbatim: "I think
   we've tried central dependency registries before and not found that
   desirable because it creates another surface for authority, while the
   deliverable local dependencies can be queried to construct a full
   accounting of all dependencies if needed."
4. DAG candidate v0.2 (120 edges: 19 DECLARED / 19 DERIVED / 82 PROPOSAL;
   10 constraint rows; 5 STANDING nodes): **accepted, all strata as
   presented** — exhibit and basis hashes in
   `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`.
   This packet reads "as presented" as accepting the exhibit **flags as
   flags** — E-A11 (AMBIGUOUS_BASIS), E-P69/E-N02 (PHASE_TENSION),
   E-N13/E-N18 (LOW_CONFIDENCE), C-02 direction, C-08 standing-node set
   remain recorded-but-unresolved, non-gating annotations; each flag is
   carried verbatim into the seeded rows' `Notes`. The ruling text below
   lets the owner confirm or override this reading.

**Not yet owner-directed (newly proposed by this packet):** the scaffolding
act itself (§3.1) and the seeding act (§3.2). PLAN §6 Q1 offered scaffolding
only conditionally; the ruling on this packet is what authorizes them.

## 2. Storage-precedent evidence (owner-directed check)

- `projects/chirality-app-dev`: deliverable-local `Dependencies.csv` v3.1
  per deliverable folder, no standing central register — matches the ruling.
- `projects/chirality-piping/execution/_DAG/DAG-001..008`: the central
  aggregate pattern the owner declined for PEC.
- Repo support for local-first: `skills/dependency-extract/SKILL.md`
  (deliverable-local v3.1 + `_DEPENDENCIES.md`),
  `tools/coordination/analyze_dep_closure.py` (on-demand full-graph
  accounting over an execution root),
  `tools/validation/validate_dependencies_schema.py` (v3.1 contract).
- `tools/coordination/materialize_local_dependencies.py` is **not used**:
  it requires the central `execution/_DAG` aggregate this packet forbids,
  and it hardcodes a PKG-00 exclusion (a repo-tool default this packet
  deliberately departs from — PEC's PKG-00 deliverables are accepted work
  units and receive registers like all others; divergence recorded as a
  tool-owner follow-on).

## 3. Ruled behavior (proposed)

### 3.1 Scaffolding (actor: PREPARATION under PROJECT_SETUP)

From accepted revision 1.1 registers: 11 package folders
`execution/{PKG-ID}_{PkgLabel}/` with **all 9 subfolders per
`tools/scaffolding/scaffold_package.sh`** (`0_References/` + `_Archive`,
`1_Working/` + `_Archive`, `2_Checking/From`, `2_Checking/To`, `3_Issued/`
+ `_Archive`), and 64 deliverable folders
`{pkg}/1_Working/{DEL-ID}_{DelLabel}/` with the 5-file minimum viable
fileset per `tools/validation/check_min_viable_fileset.sh`.

- **Exact status act** (refuter-verified tool-sequence defect): after
  `scaffold_deliverable.sh` creates the folder and stubs, the empty
  `_STATUS.md` stub is deleted and `tools/scaffolding/write_status.sh
  {folder} OPEN PREPARATION` recreates it — `write_status.sh` cannot parse
  the empty stub in place (exits 2). Lifecycle authority is unchanged:
  PREPARATION may set `OPEN` on creation.
- **Label sanitization rule:** `{ID}_{Label}` where Label = deliverable/
  package name with non-alphanumerics mapped to `_`, runs collapsed, no
  leading/trailing `_`. IDs come only from `Deliverables.csv` (I5; no
  invented IDs).
- **Metadata population:** PREPARATION populates `_CONTEXT.md` and
  `_REFERENCES.md` from the decomposition registers (IDs, names,
  descriptions, covered scope items, envelope notes, PhaseHint) per
  AGENT_PROJECT_SETUP Phase 2.1 — folders are not left as empty stubs.
  `_SEMANTIC.md` remains a stub (semantic pipeline is a later phase).

### 3.2 Deliverable-local dependency registers (actor: one PROJECT_SETUP-dispatched ephemeral Agent 2 executing the deterministic seeding script)

Each deliverable folder receives `Dependencies.csv` (v3.1, 29 columns) and
a populated `_DEPENDENCIES.md`, seeded **deterministically** from the
owner-accepted exhibit by a one-off script preserved with its run log at
`execution/_Coordination/SEED_D-PEC-62/` (in-fence packet evidence). This
one-time DAG materialization is outside the `dependency-extract` extraction
lifecycle (that skill extracts from deliverable source documents, which do
not exist yet); later refreshes use `TASK + dependency-extract`.

Row template (per incoming edge; this deliverable depends on Target):

| v3.1 field | Value |
|---|---|
| RegisterSchemaVersion | `v3.1` |
| DependencyID | `DEP-{PP}-{LL}-{NNN}` (2-digit segments matching PEC IDs; the 3-digit `validate_id_format.sh` DEP pattern mismatch is a recorded accepted deviation / tool follow-on) |
| DependencyClass / AnchorType / Direction / DependencyType / TargetType | `EXECUTION` / `NOT_APPLICABLE` / `UPSTREAM` / `PREREQUISITE` / `DELIVERABLE` |
| Target\* | predecessor's IDs/name; TargetLocation = its folder path |
| Statement | exhibit Rationale |
| EvidenceFile / SourceRef / EvidenceQuote | `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1 + exhibit BasisCitation; for the 33 PROPOSAL edges with blank BasisCitation: `SourceRef=location TBD` per the skill's evidence fallback |
| Explicitness / Origin / Confidence | DECLARED → `EXPLICIT`/`DECLARED`/`HIGH`; DERIVED → `EXPLICIT`/`EXTRACTED`/`MEDIUM`; PROPOSAL → `IMPLICIT`/`EXTRACTED`/`MEDIUM` (`LOW` when flagged LOW_CONFIDENCE) |
| RequiredMaturity / ProposedMaturity | `INITIALIZED` (ruled threshold) / `TBD` |
| SatisfactionStatus / Status | `PENDING` / `ACTIVE` |
| FirstSeen / LastSeen | seeding date |
| Notes | stratum name + exhibit Flag verbatim + EdgeID |

Additionally per deliverable: one `ANCHOR`/`IMPLEMENTS_NODE` row targeting
its parent package and `ANCHOR`/`TRACES_TO_REQUIREMENT` rows from
`Deliverables.csv` `CoversScopeItems` (v3.1 Tree-anchor contract; avoids 64
FLOATING_NODE warnings). The **9 root nodes** (DEL-00-01, DEL-00-03,
DEL-01-03, DEL-01-04, DEL-01-05, DEL-01-06, DEL-08-01, DEL-08-02,
DEL-10-01) receive anchor rows but zero EXECUTION rows — expected and
valid; their `_DEPENDENCIES.md` states "no upstream predecessors (root
node)". Constraint rows C-01..C-10 are recorded in the affected
deliverables' `_DEPENDENCIES.md` prose (non-gating; excluded from blocker
arithmetic); STANDING nodes (C-08) annotated in their own
`_DEPENDENCIES.md`, exclusion from one-shot arithmetic pending the flag
confirmation in the ruling.

### 3.3 No standing central register; exhibit freeze

No `execution/_DAG/` aggregate is created. After landing, **the
deliverable-local registers are the sole live dependency basis**; the PLAN
exhibit is frozen gate provenance consulted only as history; the §5
graph-reproduction check is a **one-time landing check**, not a standing
invariant. Any future regeneration traces to the accepted decomposition
snapshot (revision 1.1 via `SCA-001_2026-07-24_2206/`), not to the exhibit.
Full accounting is reconstructed on demand with `analyze_dep_closure.py`
(stdout-only inside the checkout; `--output-dir` may target only paths
outside the checkout or the session scratchpad). This supersedes PLAN §4.3's
`audit_dag.py` landing note, which presupposed the central aggregate the
owner declined (owner ruling 3).

### 3.4 Blocker computation

Activates after landing, from deliverable-local registers only, at
threshold `INITIALIZED` (FULL_GRAPH per `_COORDINATION.md`). Per
PROJECT_SETUP's own invariants (no work assignment; no forced false
precision), blocker output is advisory visibility for the human — reporting
only, never assignment or dispatch (also consistent with the spirit of
PEC-K-06, though that invariant binds the PEC product, not this workflow).
Note on tool semantics: `analyze_dep_closure.py`'s internal graph runs
consumer→predecessor (UPSTREAM rows), the reverse of the exhibit's
`A → B = B consumes A`; acyclicity/SCC/counts are direction-invariant, but
its `hubs.csv` in/out degrees are inverted relative to the exhibit — recorded
here so it is not rediscovered as a defect.

### 3.5 Receipt and pointers

- One loop receipt appended to `_DomainEngines/pec/LOOP_RECEIPTS.md`
  covering the DAG gate + this tranche (per-tranche opening of that
  surface).
- One-line amendment to `docs/STATUS.md` "What's next" item 1 recording
  that deliverable-local storage co-lands materialization **with**
  scaffolding (the item's "before scaffolding" ordering is impossible under
  the ruled storage: registers cannot exist before folders) and that
  D-PEC-62 is the authorizing packet.
- On ruling: update `_COORDINATION.md` (remove "scaffolding is not yet
  authorized"; add ruling item 5 naming D-PEC-62) and add the D-PEC-62 row
  to `_DECISIONS/_REGISTER.md`.

## 4. Exact fence (writes authorized by this packet when RULED)

- `projects/pec/execution/{PKG-*}/**` — creation of the 11 package trees
  (9 subfolders each) and 64 deliverable folders with the 5-file minimum
  viable fileset, plus `Dependencies.csv`, populated `_CONTEXT.md`,
  `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_run_records/` — creation
  only; no edits to any pre-existing path.
- `projects/pec/execution/_Coordination/SEED_D-PEC-62/**` — seeding script,
  inputs manifest, run log (also covered by the default fence; named for
  precision).
- `_DomainEngines/pec/LOOP_RECEIPTS.md` — append one receipt.
- `projects/pec/docs/STATUS.md` — the one-line item-1 amendment of §3.5
  only.
- `projects/pec/execution/_Coordination/_COORDINATION.md`, `.../_DECISIONS/
  D-PEC-62_*.md`, `.../_DECISIONS/_REGISTER.md` — ruling-time updates.

No source tree, manifest, estimate, schedule, frozen-corpus, database, PRD,
or other `docs/` write. F-PEC-1..4 otherwise unchanged.

## 5. Verification (expected values empirically calibrated against a simulated end-state)

1. `check_min_viable_fileset.sh` looped over all 64 deliverable folders:
   **64/64 exit 0**.
2. `validate_dependencies_schema.py` looped over all 64 `Dependencies.csv`:
   **64/64 `VALID`** (header-only EXECUTION content valid for the 9 roots).
3. `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution`
   — expected output: `Found 64 Dependencies.csv files`; `Loaded ≥184 total
   dependency rows` (120 EXECUTION + anchor rows); `Schema: 64 valid, 0
   invalid`; `Graph: 62 nodes, 120 edges`; `Orphans: 2` (**expected** —
   DEL-00-03, DEL-01-05 are the deliberate zero-edge nodes per PLAN §4.3;
   the tool's node set is edge-derived); `SCCs (size > 1): 0` (acyclicity
   witness).
4. `tools/query/count_workspace_state.sh projects/pec/execution` — 11
   packages / 64 deliverables / `OPEN | 64`.
5. Decomposition basis md5s at execution time match PLAN §1; on mismatch,
   halt and resurface.

## 6. Rollback

The tranche lands as one scoped commit (via CHANGE under project closeout
rules). Rollback = revert that commit, **plus** a follow-on commit
annotating the LOOP_RECEIPTS line as superseded (a revert alone would
delete the receipt line), **plus** manual removal of any untracked
`_run_records/` residue that revert does not touch.

## 7. Human ruling

**PENDING.** Proposed ruling text: "D-PEC-62 is RULED as drafted: scaffold
tranche 1 (11 packages / 64 deliverables) and the local-register seeding
may execute; the flags-as-flags reading of ruling 4 is confirmed, including
the C-08 standing-node exclusion from one-shot blocker arithmetic."
(Strike or amend any clause to override.)
