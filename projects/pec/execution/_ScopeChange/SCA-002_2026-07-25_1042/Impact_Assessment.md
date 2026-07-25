---
amendment_id: SCA-002
doc_kind: scope_change.impact_assessment
decomp_variant: SOFTWARE
gate: 2
created: 2026-07-25
status: awaiting_gate_2_acceptance
scope_width: O-A
authority: D-PEC-64
basis: SOFTWARE_DECOMP.md revision 1.1 (current_basis)
---

# SCA-002 — Impact Assessment (Gate 2)

Seven Gate-1-ruled actions under scope width **O-A wave-minimum**. All change
classes are `MODIFY`. No topology primitive is added, removed, reclassified,
merged, split, or renumbered.

Every claim below was measured in this session against the pinned registers
(`SOFTWARE_DECOMP.md` `ad944a2b…`, `Deliverables.csv` `6d2b290b…`,
`ScopeLedger.csv` `49e0cff9…`, re-verified unchanged at Gate 2 open).

---

## 1. Impact summary

| Action | Change | Sections / files | Rows | Workflows notified |
|---|---|---|---|---|
| A001 | `ObjectiveIDs` populated for 20 unmapped `IN` rows | §6 Scope Ledger (summary only) + `ScopeLedger.csv` | 20 of 94 | `AUDIT_DECOMP`, `PROJECT_SETUP`, `CHANGE` |
| A002 | `SupportsObjectives` populated for 17 deliverables | §5 Deliverables (control view) + `Deliverables.csv` | 17 of 64 | `AUDIT_DECOMP`, `PROJECT_SETUP`, `CHANGE` |
| A003 | §3 objective-side view + mapping notes reconciled | §3 Objectives | 6 objective rows + notes block (lines 332–338) | `AUDIT_DECOMP` |
| A004 | §7 metric + revision row updated | §7 Coverage & Telemetry | 2 metric rows | `AUDIT_DECOMP` |
| A005 | Change Register entry | §11 Decision Log (`DL-17`) + §12 Revision History (row `1.2`) | 2 rows | `CHANGE` |
| A006 | Handoff pointer repointed to revision 1.2 | `_Decomposition/_LATEST.md` | whole file | `PROJECT_SETUP`, `CHANGE` |
| A007 | §5 envelope-posture prose corrected | §5 Deliverables, line 376 | **1 line** | none (defect correction to already-accepted register truth) |

**Packages touched** (identical from both the ledger and deliverable sides —
a coherence check that passed): `PKG-00`, `PKG-01`, `PKG-02`, `PKG-03`,
`PKG-08`, `PKG-10`. Six of eleven. `PKG-04`, `PKG-05`, `PKG-06`, `PKG-07`,
`PKG-09` are untouched.

---

## 2. Lens 1 — Decomposition structure

### What changes

- **`ScopeLedger.csv`**, `ObjectiveIDs` column only, on exactly these 20 rows:
  `SOW-001, 003, 011, 012, 013, 014, 015, 016, 017, 021, 025, 040, 042, 052,
  053, 054, 056, 088, 089, 094`. No other column on those rows; no other row.
- **`Deliverables.csv`**, `SupportsObjectives` column only, on exactly these
  17 rows: `DEL-00-01, 00-03, 01-01, 01-03, 01-05, 01-06, 02-01, 02-02, 02-03,
  02-04, 02-05, 02-06, 02-07, 03-06, 08-01, 08-02, 10-03`.
- **§3, §5 (control view + A007 line), §6 summary, §7, §11, §12** narrative
  and table text.
- **`_Decomposition/_LATEST.md`** — revision pointer and handoff state.

### What must NOT change (verification failure if it does)

- The **11 residue `IN` rows**: `SOW-022, 023, 033, 034, 035, 036, 037, 038,
  044, 063, 087`.
- The **9 residue deliverables**: `DEL-00-02, 03-05, 05-01, 07-02, 07-03,
  07-04, 07-05, 08-05, 10-08`.
- All 14 `OUT` and 9 `TBD` ledger rows (unmapped by design).
- `ContextBudgetQA.csv`, `Companion_Inventory.csv` — no envelope or
  package-role change is in scope.

### The `SOW-021` constraint (binding)

`DEL-03-01` currently carries `OBJ-005`, sourced from `SOW-010`
(`PEC-RCN-001`). `SOW-021` (`PEC-RCN-006`) also covers `DEL-03-01`. Because
the union invariant defines `SupportsObjectives` as the union over covered
`IN` rows, mapping `SOW-021` to anything outside `{OBJ-005}` **forces**
`DEL-03-01`'s cell to change — making 18 deliverable rows, not 17, and
breaching the `D-PEC-64` §4.3 window. The owner made `SOW-021 ⊆ {OBJ-005}`
binding at Gate 1. `DEL-03-01` is therefore **not** in the A002 row set and
must remain byte-identical.

The symmetric case, `SOW-033` / `DEL-07-01` (`OBJ-003` via `SOW-039`), does
not arise under O-A: `SOW-033` is residue.

---

## 3. Lens 2 — Variant-local metadata (write scope)

| Surface | In `D-PEC-64` fence? | Package role | Disposition |
|---|---|---|---|
| `SOFTWARE_DECOMP.md` | yes §3.2 | working surface | `DIRECT_EDIT` at Gate 5 per Gate-3 text |
| `ScopeLedger.csv` | yes §3.2 | authoritative companion register | `DIRECT_EDIT`, 20 cells |
| `Deliverables.csv` | yes §3.2 | authoritative companion register | `DIRECT_EDIT`, 17 cells |
| `ContextBudgetQA.csv` | yes §3.2 | authoritative companion register | `NO_CHANGE` expected |
| `Companion_Inventory.csv` | conditional (D-PEC-61 clause) | authoritative companion register | `NO_CHANGE` |
| `_Decomposition/_LATEST.md` | yes §3.2 | snapshot / handoff artifact | `DIRECT_EDIT` at Gate 5 |
| `_ScopeChange/**` | yes §3.2 | snapshot / handoff artifact | this session's own writes |
| `_Evaluation/DecompCoverage/**` | yes §3.2 | derived publication artifact | pre-change done; post-change at Gate 5 |
| **17× `_CONTEXT.md`** (`SupportsObjectives` line) | yes §3.2 line class (i) | derived publication artifact | `DIRECT_EDIT` at Gate 5, Gate 4 approval |
| **64× `_CONTEXT.md`** (basis pointer) | yes §3.2 line class (ii) | derived publication artifact | **Gate 4 decision: refresh vs recorded deferral** |
| `_STATUS.md` | **narrowed out** §3.2 | working surface | `NO_CHANGE` — no lifecycle state changes |
| `_REFERENCES.md` | **excluded** §3.3 | derived publication artifact | **stale but unreachable** — see §4 row 3 |
| `Dependencies.csv`, `_DEPENDENCIES.md` | excluded §3.3 | authoritative (dependency basis) | `NO_CHANGE`, conditional — see §4 row 2 |
| `projects/pec/docs/PRD.md` | excluded §3.3 | upstream source corpus | `NO_CHANGE` — mapping *consumes* PRD anchors |

---

## 4. Derivative-package status table (mandatory, intake §6.5)

| # | Derivative package | Owner | Status after amendment | Required rerun / closure action |
|---|---|---|---|---|
| 1 | **64 × `_CONTEXT.md`** — (a) `SupportsObjectives` lines; (b) rev-1.1 basis pointer | `SCOPE_CHANGE` (in-fence, line classes only) | (a) **17 `STALE_REBUILD_REQUIRED`**; (b) **64 `STALE_REBUILD_REQUIRED`** | (a) rewrite the 17 changed lines at Gate 5 per Gate-4 plan. (b) **Gate 4 owner decision**: refresh all 64 pointers to revision 1.2, or record an explicit deferral with a rerun obligation in `Handoff_State.md`. Measured: 64/64 contain the string "revision 1.1"; the 26 unmapped carry the literal placeholder `(none mapped — see §3 mapping notes)`, of which 17 are in the A002 set |
| 2 | **64 × deliverable-local `Dependencies.csv`** | `PROJECT_SETUP` / `dependency-extract` skill | **`CURRENT` — conditional** | Expected `NO_CHANGE`: no topology change, and 0 of 255 rows carry a `SupportsObjectives` value. **One exception:** `DEP-02-01-003` (in `DEL-02-01`) quotes the §3 parser clause verbatim in *both* `SourceRef` and `EvidenceQuote`. If A003 preserves that sentence, the verdict is `CURRENT`. If A003 rewrites it, that row's evidence goes stale and `dependency-extract` owes a rerun for `DEL-02-01`. See §6 `F-4` |
| 3 | **64 × `_REFERENCES.md`** | `PROJECT_SETUP` / `PREPARATION` | **`STALE_DEFERRED_BY_FENCE`** | Measured: **all 64 pin "revision 1.1"** in the line `` `execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.1, accepted working surface) ``. `D-PEC-64` §3.3 **explicitly excludes** `_REFERENCES.md` — this session cannot refresh it at any gate. Must be recorded in `Handoff_State.md` as an open rerun obligation owned by resumed `PROJECT_SETUP`. **Not previously enumerated in intake §6.5** — new at Gate 2 (`OI-B`) |
| 4 | **Frozen DAG-gate exhibit** `_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` | `PROJECT_SETUP` | **`STALE_ANNOTATION_SCHEDULED`** | 8 rev-1.1 references measured (lines 18, 47, 70, 91, 99, 108, 347, 362). Topology is unchanged by SCA-002, so the exhibit stays factually valid; it needs a historical-provenance annotation naming rev-1.1 as its basis. Already scheduled by wave plan §7 re-pin point 4. Out of this session's fence (§3.3) |
| 5 | **`COV_SCA002_PRECHANGE_2026-07-25_1040`** | `SCOPE_CHANGE` (this session) | `CURRENT` | None. Immutable pre-change evidence; correctly reflects revision 1.1 |
| 6 | **`COV_SCA001_*` (2 snapshots)** | `SCOPE_CHANGE` | `HISTORICAL_RESIDUE` | None. Both `FAILED_INPUTS`; never current truth |
| 7 | **Post-change coverage baseline** | `SCOPE_CHANGE` (this session) | `NOT_YET_CREATED` | Gate 5: rerun `AUDIT_DECOMP` inline, scope `ALL`, compare against snapshot #5 |
| 8 | **`SCA-001_2026-07-24_2206` snapshot** | `SCOPE_CHANGE` | `HISTORICAL` on Gate 5 | `_ScopeChange/_LATEST.md` repoints to SCA-002 at Gate 5; SCA-001 remains immutable historical evidence |
| 9 | **D-PEC-63 wave brief template** (`PLAN_…_sow_wave.md` §3) | `PROJECT_SETUP` | **`BLOCKED` → `UNBLOCKED`** | This is the amendment's purpose. Re-pin per wave plan §7: three md5s + rev-1.2 commit SHA; `{REV_1_2_COMMIT}` in §3 `DECOMPOSITION_BASIS`; confirm bare `OBJ-NNN` tokens survived |
| 10 | **`_Coordination/_COORDINATION.md`**, **`projects/pec/AGENTS.md`** | `PROJECT_SETUP` | `STALE_ON_ACCEPTANCE` | Both cite revision 1.1 as accepted basis (measured: `_COORDINATION.md` lines 16, 50). Refresh is `D-PEC-64` §3.1 owner-governance work by resumed `PROJECT_SETUP` at closure — not this session's fence |
| 11 | **Hypergraph / `_Aggregation` outputs** | — | `NOT_APPLICABLE` | No such surface exists under `projects/pec/execution/` (measured: only `PKG-*`, `_Coordination`, `_Decomposition`, `_Evaluation`, `_ScopeChange`) |
| 12 | **Estimates / schedules** | — | `NOT_APPLICABLE` | Neither `_Estimates/` nor `_Schedule/` exists. `ResponsibleParty` is `TBD` across all 64; no estimate basis exists to go stale |

---

## 5. Supersession analysis (intake §5.5 — Gate 2/3 ruling)

### The question

Does any O-A action change a fact that could conflict with an **upstream
admitted authority**, thereby owing a `Supersession_Delta.csv` row?

### Analysis

The only admitted upstream authority in this decomposition's lineage is the
source corpus `projects/pec/docs/PRD.md` v2.1 (front matter `source_corpus`).
Assessed against each candidate:

| Candidate superseded fact | Where recorded | Verdict |
|---|---|---|
| §7 metric "31 (intentional best-effort posture)" | `SOFTWARE_DECOMP.md` §7 line 528 | **Not an upstream authority fact.** It is the decomposition's own self-description of its prior state. Its change is recorded by the §12 revision-history row and the `DL-17` entry (A004/A005) — the protocol's normal mechanism for intra-document state change |
| §3 parser clause (`SOW-011..017` → `OBJ-001`/`OBJ-002`) | §3 mapping notes | **Applied, not superseded** (finding `F-3`). §3 states a *positive derivation*; A001 mapping those rows carries the recorded rationale into the register rather than overriding it |
| §3 ingest/bridge "intentionally not force-mapped" | §3 mapping notes | **Retained verbatim under O-A** — `SOW-033..038` are residue. Nothing superseded |
| `DL-14` `SOW-063` rationale | §11 line 623 | **Retained verbatim under O-A** — `SOW-063` is residue. Nothing superseded |
| A007 envelope count | §5 line 376 | **Defect correction, not supersession.** The replacement value (`28 S / 34 M / 2 L / 0 XL`) is already-accepted register truth; A007 makes a stale restatement agree with the authority it restates |
| PRD function rows used for attribution | `docs/PRD.md` | **Consumed, not changed.** `D-PEC-64` §3.3 excludes the PRD; the attribution method reads PRD anchors to derive mappings |

### Precedent

`SCA-001_2026-07-24_2206/Supersession_Map.csv` is **header-only** — zero
binding rows — despite SCA-001 expanding a scope-item statement, renaming a
deliverable, and re-enveloping `S`→`M`. The accepted precedent for a
`SOFTWARE` intra-decomposition amendment is therefore *no binding*.

### Recommendation (owner rules; this agent does not)

**No `Supersession_Delta.csv` binding is owed under O-A.** Every posture
change is intra-decomposition and is captured by the revision history plus the
`DL-17` Decision Log entry. Under O-B the answer would differ — superseding the
§3 ingest/bridge clause and `DL-14` would be genuine overrides of recorded
design rationale — but O-B was not ruled.

Gate 5 must still produce the cumulative map through the deterministic
accumulator, carrying SCA-001's header-only map forward:

```bash
python3 tools/coordination/accumulate_supersession_map.py \
  --prior-map projects/pec/execution/_ScopeChange/SCA-001_2026-07-24_2206/Supersession_Map.csv \
  --output-map projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Supersession_Map.csv \
  --allow-empty
```

`--delta` is omitted precisely because no delta exists. Hand-merging is
forbidden by the protocol.

**If the owner instead rules a binding owed**, the defensible row shape is
`SupersededAuthorityRole = OTHER`, path `SOFTWARE_DECOMP.md`, ref `§7 metric
row`, `OverrideType = SUPERSESSION`, old `31 (intentional best-effort
posture)` → new `11 (residue; O-A wave-minimum)`. This agent does not
recommend it — it binds a document to itself, which the schema is not shaped
for — but it is coherent and cheap if the owner wants the posture change
formally traceable.

---

## 6. Lens 3 — Downstream consumers

| Consumer | Effect | Rerun owed |
|---|---|---|
| **SOW validator** `tools/scope_of_work/common.py` | The wave blocker clears. `:213-215` requires non-empty `package_objective_refs`; `:251-253` unions it with `project_scope_refs`; `:266-267` splits matrix cells on comma/whitespace | None — validated at wave authoring |
| **Four-doc→SOW converter** `convert_four_documents_to_scope_of_work.py` | `--package-objective-ref` is **`required=True`** and repeatable (line 202), emitted as an inline YAML list (line 140). An empty mapping means the converter **cannot be invoked at all** — a harder failure than the validator's non-emptiness check | None |
| **Brief construction** (D-PEC-63 §3 template) | `PROJECT_SETUP` splits register cells on `;` and emits bare tokens. **Bare `OBJ-NNN` tokens are mandatory** — a `;`-joined cell copied verbatim becomes one unusable token | Wave plan §7 re-pin point 3 verifies this post-amendment |
| **`dependency-extract` skill** | Conditional — see §4 row 2 / `F-4` | Only if A003 rewrites the parser clause |
| **`AUDIT_DECOMP`** | Post-change baseline at Gate 5 | Yes — Gate 5, scope `ALL` |
| **`PROJECT_SETUP`** | Yields until Gate 5 closure per `D-PEC-64` §2.4; then resumes at STEP 3 | Yes — resumption sequence in `D-PEC-64` §2.4 |
| **`CHANGE`** | Receives the Gate 5 file list + recommended commit message | Closure commit per `D-PEC-64` §3.6b, performed by resumed `PROJECT_SETUP` |
| **`estimate-snapshot`, scheduling** | `NOT_APPLICABLE` — no estimate or schedule surface exists | None |

### `F-4` — the one genuine `Dependencies.csv` coupling

`projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/Dependencies.csv`,
row `DEP-02-01-003`, carries in **both** `SourceRef` and `EvidenceQuote`:

> `§3 mapping notes: "parser items (SOW-011..017) underlie OBJ-001/OBJ-002 through the record tier (SOW-001)"`

This is the exact sentence A003 may amend. The dependency edge itself
(`DEL-02-01` → `DEL-01-01`, `PREREQUISITE`) is unaffected — no topology
changes. Only the cited evidence text is at risk.

**Gate 3 drafting guidance:** because O-A *applies* the parser clause rather
than superseding it (`F-3`), A003 can reconcile the surrounding best-effort
framing while **preserving that sentence verbatim**. Doing so keeps all 64
`Dependencies.csv` genuinely `NO_CHANGE` and avoids a rerun. This is a
recommendation on drafting, not a constraint on the owner.

---

## 7. Lens 4 — Invariant and telemetry risk

### Orphan-risk summary (`SOFTWARE` counts)

| Condition | Pre | Post (expected) | Risk |
|---|---|---|---|
| Packages without folders | 0 | 0 | none — no topology change |
| Deliverables without folders | 0 | 0 | none |
| `IN` rows without package | 0 | 0 | none |
| `IN` rows without deliverable | 0 | 0 | none |
| Objectives without support | 0 | 0 | none |
| Deliverables parentless | 0 | 0 | none |
| **`IN` rows without objective** | **31** | **11** | intended (−20) |
| **Deliverables without objective** | **26** | **9** | intended (−17) |
| Union-invariant violations | **0** | **0** | **must hold — primary post-check** |

No parent-partition or parent-entity change occurs, so the parent-closure rule
is not engaged and no child-closure set exists to enumerate.

### Telemetry consequences

- §7 `IN items without objective mapping`: `31` → `11`, with the posture
  restated as O-A residue rather than blanket best-effort.
- §7 `Revision`: `1.1, 2026-07-24 (SCA-001)` → `1.2, 2026-07-25 (SCA-002)`.
- §7 `ContextEnvelopeCounts` — **unchanged**; A007 makes §5 agree with it.
- §3 `Mapped Scope Items` / `MappedDeliverables` — grow for the objectives
  receiving newly mapped rows. Pre-change, §3 and `Deliverables.csv` agree
  exactly for all six objectives (9/4/12/9/2/9); **that agreement must survive**.

### Risk register

| Risk | Severity | Mitigation |
|---|---|---|
| `SOW-021` mapped outside `{OBJ-005}` → `DEL-03-01` forced, window breaks | **HIGH** | Binding constraint in `D-PEC-64` §4.3; Gate 3 text review; post-check asserts `DEL-03-01` byte-identical |
| A003 rewrites the parser clause → `DEP-02-01-003` evidence stale | MEDIUM | `F-4` guidance: preserve verbatim |
| Residue rows mapped "helpfully" | MEDIUM | `D-PEC-64` §4.3: "a verification failure, not a bonus"; post-check asserts all 11 + 9 byte-identical |
| Qualified tokens (`OBJ-001(indirect)`) reach a register | MEDIUM | §5.1 constraint; post-check `^OBJ-[0-9]{3}$` after `;` split |
| §3 / register divergence after A003 | MEDIUM | Post-check re-runs the six-objective agreement comparison **with range expansion** (`D-7`) |
| 64 `_REFERENCES.md` silently left stale | MEDIUM | `OI-B`; must appear in `Handoff_State.md` — this session cannot fix it |
| `_CONTEXT.md` basis pointers left stale | LOW | Gate 4 explicit refresh-or-deferral decision |
| No durable register validator (`OI-013`) | LOW | Gate 5 deterministic post-checks; `OI-013` stays open |

### Active snapshot / handoff-state impact

`_ScopeChange/_LATEST.md` still names `SCA-001` and will until Gate 5 — correct
per `D-PEC-64` §2.4. At Gate 5 it repoints to `SCA-002_2026-07-25_1042`, which
must by then carry the full artifact set (see the Decision_Log deferral table).
Expected closure verdict: **`OPEN_PENDING_DERIVATIVE_CLOSURE`** — not
`CLOSED_FOR_SCOPE_CHANGE_ONLY` — because rows 3, 4, 9, and 10 of §4 leave live
obligations with owners outside this session's fence. `ReadyForNextPhase`
expected `REGEN_ONLY`.

---

## 8. Recommended downstream reruns (not executed by SCOPE_CHANGE)

1. `AUDIT_DECOMP` post-change baseline — Gate 5, inline, scope `ALL`.
2. `analyze_dep_closure.py` — confirm the `D-PEC-62` values still hold
   (64 files, 255 rows, 135/120, 62 nodes/120 edges, orphans 2, SCCs 0).
3. Lifecycle census — `grep -h '^\*\*Current State:\*\*' …` still `64 OPEN`
   (never `count_workspace_state.sh`, per `D-PEC-64` §4.4).
4. `dependency-extract` for `DEL-02-01` — **only if** A003 rewrites the parser
   clause.
5. `PROJECT_SETUP` resumption — `D-PEC-64` §2.4 sequence: receipt, closure
   commit, D-PEC-63 re-pins, `projects/pec/AGENTS.md` refresh.
6. `_REFERENCES.md` basis-pointer refresh across 64 deliverables — owner-
   assigned; outside this fence.

---

## 9. Gate 2 acceptance question

**Do you accept this impact assessment?**

Three items need an explicit owner answer to close Gate 2:

1. **Supersession** — accept the recommendation that **no
   `Supersession_Delta.csv` binding is owed** under O-A (§5), with Gate 5
   carrying SCA-001's header-only map forward through the accumulator?
2. **`_REFERENCES.md` (`OI-B`)** — all 64 pin revision 1.1 and `D-PEC-64` §3.3
   excludes them from this session. Confirm they are recorded in
   `Handoff_State.md` as a deferred obligation owned by resumed
   `PROJECT_SETUP`, rather than pulled into this SCA's fence?
3. **`F-4` drafting guidance** — accept that A003 should preserve the §3 parser
   sentence verbatim (keeping all 64 `Dependencies.csv` `NO_CHANGE`), or accept
   a `dependency-extract` rerun for `DEL-02-01`?

The `_CONTEXT.md` basis-pointer refresh-vs-deferral question is **Gate 4**
work, not Gate 2, and is deliberately not asked here.
