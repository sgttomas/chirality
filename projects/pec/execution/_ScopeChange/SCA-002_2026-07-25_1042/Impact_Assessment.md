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
corrections_round: R-2b-g2 (14 findings, all ACCEPTED; C-2..C-13 applied)
---

# SCA-002 — Impact Assessment (Gate 2)

> **Corrections applied.** This document was adversarially refuted
> (round R-2b-g2) after its first presentation. Fourteen findings were
> accepted and applied as corrections **C-2 … C-13**; each is logged in §10
> with its in-place effect, and each affected passage is marked inline. Prior
> claims are annotated as superseded rather than deleted, matching the C-1
> convention established at Gate 1.

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
| A001 | `ObjectiveIDs` populated for 20 unmapped `IN` rows | `ScopeLedger.csv` only **(C-12)** | 20 of 94 | `AUDIT_DECOMP`, `PROJECT_SETUP`, `CHANGE` |
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
- **§3, §5 (control view + A007 line), §7, §11, §12** narrative and table
  text. **(C-12: §6 Scope Ledger removed — it is an 8-line pointer to
  `ScopeLedger.csv` carrying no per-row mapping and no objective count;
  nothing in it changes.)**
- **`_Decomposition/_LATEST.md`** — revision pointer and handoff state.

### What must NOT change (verification failure if it does)

- The **11 residue `IN` rows**: `SOW-022, 023, 033, 034, 035, 036, 037, 038,
  044, 063, 087`.
- The **9 residue deliverables**: `DEL-00-02, 03-05, 05-01, 07-02, 07-03,
  07-04, 07-05, 08-05, 10-08`.
- All 14 `OUT` and 9 `TBD` ledger rows (unmapped by design).

**(C-7)** `ContextBudgetQA.csv` and `Companion_Inventory.csv` are **not** in
this "verification failure if changed" list. Both are **in-fence writable**
(`D-PEC-64` §3.2 names `ContextBudgetQA.csv` explicitly; `Companion_Inventory.csv`
is writable under the conditional D-PEC-61 clause). Both are **expected
unchanged** because no envelope or package-role change is in scope, and either
may be edited only via Gate-3-approved exact text. An unexplained diff is a
finding to investigate, not an automatic verification failure — unlike the
residue rows above, where any diff *is* a failure. §2 and §3 now state one
post-check contract.

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

**(C-6)** Every `Disposition` cell below is normalized to the contract enum
`DIRECT_EDIT | RECOMPUTE | NO_CHANGE`. Conditions, timing, and caveats moved
to a separate `Status / notes` column so Gate 5's `Handoff_State.md` table can
carry these values directly — it cannot carry non-enum prose.

| Surface | In `D-PEC-64` fence? | Package role | Disposition | Status / notes |
|---|---|---|---|---|
| `SOFTWARE_DECOMP.md` | yes §3.2 | working surface | `DIRECT_EDIT` | at Gate 5 per Gate-3 approved text |
| `ScopeLedger.csv` | yes §3.2 | authoritative companion register | `DIRECT_EDIT` | 20 cells, `ObjectiveIDs` column only |
| `Deliverables.csv` | yes §3.2 | authoritative companion register | `DIRECT_EDIT` | 17 cells, `SupportsObjectives` column only |
| `ContextBudgetQA.csv` | yes §3.2 | authoritative companion register | `NO_CHANGE` | expected unchanged; in-fence, editable only via Gate-3 text (C-7) |
| `Companion_Inventory.csv` | conditional (D-PEC-61 clause) | authoritative companion register | `NO_CHANGE` | expected unchanged (C-7) |
| `_Decomposition/_LATEST.md` | yes §3.2 | snapshot / handoff artifact | `DIRECT_EDIT` | at Gate 5 |
| `_ScopeChange/**` | yes §3.2 | snapshot / handoff artifact | `DIRECT_EDIT` | this session's own writes |
| `_Evaluation/DecompCoverage/**` | yes §3.2 | derived publication artifact | `RECOMPUTE` | pre-change baseline done; post-change regenerated at Gate 5 (C-6) |
| `Supersession_Map.csv` (this snapshot) | yes §3.2 | snapshot / handoff artifact | `RECOMPUTE` | generated at Gate 5 by the accumulator, never hand-merged; SCA-001 precedent (C-6) |
| **17× `_CONTEXT.md`** (`SupportsObjectives` line) | yes §3.2 line class (i) | derived publication artifact | `DIRECT_EDIT` | at Gate 5, pending Gate 4 approval |
| **64× `_CONTEXT.md`** (basis pointer) | yes §3.2 line class (ii) | derived publication artifact | `DIRECT_EDIT` | **conditional on the Gate 4 refresh-vs-deferral decision**; `NO_CHANGE` if deferral is recorded |
| `_STATUS.md` | **narrowed out** §3.2 | working surface | `NO_CHANGE` | no lifecycle state changes |
| `_REFERENCES.md` (64) | **excluded** §3.3 | derived publication artifact | `NO_CHANGE` | forced by the fence, not by parity — stale content persists; see §4 row 3 |
| `Dependencies.csv`, `_DEPENDENCIES.md` | excluded §3.3 | authoritative (dependency basis) | `NO_CHANGE` | see §4 row 2 |
| `projects/pec/docs/PRD.md` | excluded §3.3 | upstream source corpus | `NO_CHANGE` | mapping *consumes* PRD anchors |

---

## 4. Derivative-package status table (mandatory, intake §6.5)

| # | Derivative package | Owner | Status after amendment | Required rerun / closure action |
|---|---|---|---|---|
| 1 | **64 × `_CONTEXT.md`** — (a) `SupportsObjectives` lines; (b) rev-1.1 basis pointer | `SCOPE_CHANGE` (in-fence, line classes only) | (a) **17 `STALE_REBUILD_REQUIRED`**; (b) **64 `STALE_REBUILD_REQUIRED`** | (a) rewrite the 17 changed lines at Gate 5 per Gate-4 plan. (b) **Gate 4 owner decision**: refresh all 64 pointers to revision 1.2, or record an explicit deferral with a rerun obligation in `Handoff_State.md`. Measured: 64/64 contain the string "revision 1.1"; the 26 unmapped carry the literal placeholder `(none mapped — see §3 mapping notes)`, of which 17 are in the A002 set |
| 2 | **64 × deliverable-local `Dependencies.csv`** | `PROJECT_SETUP` / `dependency-extract` skill | **`CURRENT`** (unconditional — **C-4**) | `NO_CHANGE`: no topology change. **(C-10)** The v3.1 register schema has **no objective column at all** — the 29 columns are `RegisterSchemaVersion, DependencyID, From*, DependencyClass, AnchorType, Direction, DependencyType, Target*, Statement, EvidenceFile, SourceRef, EvidenceQuote, Explicitness, *Maturity, SatisfactionStatus, Confidence, Origin, FirstSeen, LastSeen, Status, Notes` — so objective mappings cannot propagate here by construction. My earlier phrasing ("0 of 255 rows carry a `SupportsObjectives` value") implied such a column exists and merely happened to be empty; it does not. **(C-4)** The `DEP-02-01-003` exception is **withdrawn**: that row's declared `EvidenceFile` is `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, **not** `SOFTWARE_DECOMP.md`, and the exhibit carries the sentence verbatim at its line 143 (edge `E-P03`). A003 rewriting §3 therefore does not break the row's declared anchor |
| 3 | **64 × `_REFERENCES.md`** | `PROJECT_SETUP` / `PREPARATION` | **`STALE_DEFERRED_BY_FENCE`** | Measured: **all 64 pin "revision 1.1"** in the line `` `execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.1, accepted working surface) ``. `D-PEC-64` §3.3 **explicitly excludes** `_REFERENCES.md` — this session cannot refresh it at any gate. Must be recorded in `Handoff_State.md` as an open rerun obligation owned by resumed `PROJECT_SETUP`. **Not previously enumerated in intake §6.5** — new at Gate 2 (`OI-B`) |
| 4 | **Frozen DAG-gate exhibit** `_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` | `PROJECT_SETUP` | **`STALE_ANNOTATION_SCHEDULED`** (partly extant) | 8 rev-1.1 references measured (lines 18, 47, 70, 91, 99, 108, 347, 362). **(C-9)** Two of those — lines 347 and 362 — are **already** the provenance annotation ("Accepted upstream snapshot: revision 1.1 via…"; "decomposition snapshot (rev 1.1 via SCA-001), not this exhibit"), so the exhibit is not un-annotated. The scheduled act targets the **§1 pins only** (line 18 region). Lines 47/70/91/99/108 are historical narrative about how the exhibit was built from rev 1.1 and are correct as written — they need no edit. Topology is unchanged by SCA-002, so the exhibit stays factually valid. **(C-8)** Scheduled by wave plan §7 as the **one annotation** accompanying three re-pin points — there is no "point 4" |
| 5 | **`COV_SCA002_PRECHANGE_2026-07-25_1040`** | `SCOPE_CHANGE` (this session) | `CURRENT` | None. Immutable pre-change evidence; correctly reflects revision 1.1 |
| 6 | **`COV_SCA001_*` (2 snapshots)** | `SCOPE_CHANGE` | `HISTORICAL_RESIDUE` | None. Both `FAILED_INPUTS`; never current truth |
| 7 | **Post-change coverage baseline** | `SCOPE_CHANGE` (this session) | `NOT_YET_CREATED` | Gate 5: rerun `AUDIT_DECOMP` inline, scope `ALL`, compare against snapshot #5 |
| 8 | **`SCA-001_2026-07-24_2206` snapshot** | `SCOPE_CHANGE` | `HISTORICAL` on Gate 5 | `_ScopeChange/_LATEST.md` repoints to SCA-002 at Gate 5; SCA-001 remains immutable historical evidence |
| 9 | **D-PEC-63 wave brief template** (`PLAN_…_sow_wave.md` §3) | `PROJECT_SETUP` | **`BLOCKED` → `UNBLOCKED`** | This is the amendment's purpose. **(C-8)** Re-pin per wave plan §7, stated exactly as that section does — **three re-pin points plus one annotation**: (1) the three md5s + rev-1.2 commit SHA in §7; (2) `{REV_1_2_COMMIT}` in §3 `DECOMPOSITION_BASIS`; (3) confirm the registers kept bare `OBJ-NNN` tokens; **and** the DAG-exhibit §1-pins annotation (row 4) |
| 10 | **`_Coordination/_COORDINATION.md`** | `PROJECT_SETUP` | `STALE_ON_ACCEPTANCE` | Cites revision 1.1 as accepted basis at lines 16 and 50 (measured). Refresh is `D-PEC-64` §3.1 owner-governance work by resumed `PROJECT_SETUP` at closure — not this session's fence |
| 10b | **`projects/pec/AGENTS.md`** | `PROJECT_SETUP` | **`CURRENT`** (**C-3** — correction) | **My earlier row 10 was wrong**, and wrong in the way that matters most: it asserted this file "cites revision 1.1" under a **"measured"** label when I had not measured it. Grep verification: `projects/pec/AGENTS.md` contains **no revision pin at all**. It is deliberately revision-agnostic — line 84 routes acceptance state to `execution/_Decomposition/_LATEST.md` and states "this table asserts no gate state"; line 148 says "`_LATEST.md` is the revision pointer and handoff state — read it first". Nothing in it goes stale when revision 1.2 is accepted. The `D-PEC-64` §2.4 pointer refresh naming revision 1.2 and D-PEC-64 is a **chosen governance act**, not staleness repair |
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

**No `Supersession_Delta.csv` binding is owed under O-A — conditional on the
Gate 3 attributions remaining consumptive of the PRD.** Every posture change
is intra-decomposition and is captured by the revision history plus the
`DL-17` Decision Log entry. Under O-B the answer would differ — superseding the
§3 ingest/bridge clause and `DL-14` would be genuine overrides of recorded
design rationale — but O-B was not ruled.

**(C-5) The condition, stated explicitly.** This recommendation holds only
while every Gate 3 attribution *reads* a PRD function row to derive a mapping.
If any attribution instead asserts something that **conflicts with a PRD
authority fact** — for example, mapping a deliverable to an objective whose
PRD-stated outcome that deliverable's function does not serve, or contradicting
a PRD §3 outcome statement — then that action does override an upstream
admitted authority and **does** owe a binding. The nine `NEEDS ATTRIBUTION`
rows are exactly where this could arise, and their exact text does not exist
yet. **This recommendation is therefore re-affirmed at Gate 3** once the
attributions are drafted; accepting it at Gate 2 accepts the analysis and its
condition, not a guarantee about text not yet written.

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
| **Four-doc→SOW converter** `convert_four_documents_to_scope_of_work.py` | `--package-objective-ref` is `required=True` and repeatable (line 202), emitted as an inline YAML list (line 140). **(C-11)** argparse requires the **flag**, not a *correct* value — so invocation is mechanically possible; what the caller lacks is any legal value to pass, since the register cell is empty. The practical effect is the same wall, reached one step earlier than the validator's non-emptiness check. My earlier "cannot be invoked at all" overstated it | None |
| **Brief construction** (D-PEC-63 §3 template) | `PROJECT_SETUP` splits register cells on `;` and emits bare tokens. **Bare `OBJ-NNN` tokens are mandatory** — a `;`-joined cell copied verbatim becomes one unusable token | Wave plan §7 re-pin point 3 verifies this post-amendment |
| **`dependency-extract` skill** | **No effect (C-4)** — see §4 row 2 | **None** |
| **`AUDIT_DECOMP`** | Post-change baseline at Gate 5 | Yes — Gate 5, scope `ALL` |
| **`PROJECT_SETUP`** | Yields until Gate 5 closure per `D-PEC-64` §2.4; then resumes at STEP 3 | Yes — resumption sequence in `D-PEC-64` §2.4 |
| **`CHANGE`** | Receives the Gate 5 file list + recommended commit message | Closure commit per `D-PEC-64` §3.6b, performed by resumed `PROJECT_SETUP` |
| **`estimate-snapshot`, scheduling** | `NOT_APPLICABLE` — no estimate or schedule surface exists | None |

### `F-4` — WITHDRAWN (C-4)

> **Superseded by C-4.** The original `F-4` claimed that
> `DEP-02-01-003` (in `DEL-02-01`'s `Dependencies.csv`) creates a coupling
> requiring A003 to preserve the §3 parser sentence verbatim, and it raised
> that to a Gate 2 owner acceptance condition. **All three moves were wrong.**

Three independent defects, each verified:

1. **Wrong anchor.** The row's declared `EvidenceFile` is
   `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` — the
   frozen DAG exhibit — **not** `SOFTWARE_DECOMP.md`. The exhibit carries the
   sentence verbatim at line 143 (edge `E-P03`). A003 rewriting §3 does not
   break the row's declared anchor, because §3 is not its anchor. The exhibit
   is frozen provenance and does not change.
2. **Preserve-verbatim conflicts with the amendment's own mandate.** §7 line
   528 currently reads the parser clause as *non-mapping* rationale: "31
   (intentional best-effort posture, §3 mapping notes — parsers/mechanics
   serve objectives through the record tier)". Once `SOW-011..017` **are**
   mapped, that clause's in-document function changes, and A003/A004 are
   specifically chartered to reconcile it. Demanding verbatim preservation
   would have pitted my guidance against the actions' own purpose.
3. **Wrong gate.** Elevating drafting guidance to a Gate 2 acceptance
   condition is precisely the category error I correctly refused one paragraph
   earlier when I withheld the `_CONTEXT.md` refresh question as Gate 4 work.
   I applied the principle in one place and violated it in another.

**Correct disposition:** parser-sentence handling is **Gate 3 drafting**,
where the exact text is drafted and refuted on its merits. The scheduled
DAG-exhibit annotation (§4 row 4) is what keeps the attribution correct. No
`dependency-extract` rerun is owed, and Gate 2 asks **two** questions, not
three.

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
| Gate 3 attribution conflicts with a PRD authority fact → binding owed after all | MEDIUM | `C-5` condition; recommendation re-affirmed at Gate 3 against the drafted attributions |
| Qualified tokens (`OBJ-001(indirect)`) reach a register | MEDIUM | §5.1 constraint; post-check `^OBJ-[0-9]{3}$` after `;` split |
| §3 / register divergence after A003 | MEDIUM | Post-check re-runs the six-objective agreement comparison **with range expansion** (`D-7`) |
| 64 `_REFERENCES.md` silently left stale | MEDIUM | `OI-B`; must appear in `Handoff_State.md` — this session cannot fix it |
| `_CONTEXT.md` basis pointers left stale | LOW | Gate 4 explicit refresh-or-deferral decision |
| No durable register validator (`OI-013`) | LOW | Gate 5 deterministic post-checks; `OI-013` stays open |

### Active snapshot / handoff-state impact

`_ScopeChange/_LATEST.md` still names `SCA-001` and will until Gate 5 — correct
per `D-PEC-64` §2.4. At Gate 5 it repoints to `SCA-002_2026-07-25_1042`, which
must by then carry the full artifact set (see the Decision_Log deferral table).

**(C-2) Expected closure verdict: `CLOSED_FOR_SCOPE_CHANGE_ONLY`**, with the
out-of-fence obligations carried in **`DownstreamRerunState = FROZEN`**.
`ReadyForNextPhase` expected `REGEN_ONLY`. The final call remains a **Gate 5
fact**, not a Gate 2 prediction.

> **Superseded.** My Gate 2 return predicted
> `OPEN_PENDING_DERIVATIVE_CLOSURE`, reasoning that §4 rows 3, 4, 9, and 10
> leave obligations with owners outside this fence. That reasoning is refuted
> **by the precedent I myself cited**:

- `SCA-001_2026-07-24_2206/Handoff_State.md` records
  `DerivativePackageState: COMPLETE`, `DownstreamRerunState: FROZEN — not
  executed by SCOPE_CHANGE; released to Project Setup`, and
  `ClosureVerdict: CLOSED_FOR_SCOPE_CHANGE_ONLY` — **simultaneously**. Live
  out-of-fence obligations and the clean verdict coexist by design; `FROZEN`
  is the field that carries them.
- `AGENT_SCOPE_CHANGE.md` line 685 scopes `DerivativePackageState` to
  "**decomposition-local** derivative surfaces". Of the four rows I invoked,
  the DAG exhibit, wave re-pins, and `_COORDINATION.md` are coordination
  surfaces, not decomposition-local ones. Only `_REFERENCES.md` is arguably
  close — and it is fence-*excluded*, so it cannot be a parity failure of a
  package this session owns.

I had the disconfirming evidence in hand — I quoted SCA-001's map in §5 of
this same document — and still reached for the more pessimistic verdict.
Pessimism is not conservatism when it misreports a contract field: an
unwarranted `OPEN_PENDING_DERIVATIVE_CLOSURE` would understate the amendment's
completeness and could stall `PROJECT_SETUP` resumption.

---

## 8. Recommended downstream reruns (not executed by SCOPE_CHANGE)

1. `AUDIT_DECOMP` post-change baseline — Gate 5, inline, scope `ALL`.
2. `analyze_dep_closure.py` — confirm the `D-PEC-62` values still hold
   (64 files, 255 rows, 135/120, 62 nodes/120 edges, orphans 2, SCCs 0).
3. Lifecycle census — `grep -h '^\*\*Current State:\*\*' …` still `64 OPEN`
   (never `count_workspace_state.sh`, per `D-PEC-64` §4.4).
4. **(C-4)** ~~`dependency-extract` for `DEL-02-01`~~ — **withdrawn**; no
   rerun is owed.
5. `PROJECT_SETUP` resumption — `D-PEC-64` §2.4 sequence: receipt, closure
   commit, D-PEC-63 re-pins, `projects/pec/AGENTS.md` pointer refresh
   (a chosen governance act, not staleness repair — C-3).
6. `_REFERENCES.md` basis-pointer refresh across 64 deliverables — owner-
   assigned; outside this fence.

---

## 9. Gate 2 acceptance question

**Do you accept this impact assessment?**

**(C-4)** Two items need an explicit owner answer to close Gate 2:

1. **Supersession (§5).** Accept that **no `Supersession_Delta.csv` binding is
   owed under O-A**, *conditional on the Gate 3 attributions remaining
   consumptive of the PRD* — no attribution asserting anything that conflicts
   with a PRD authority fact — with the recommendation **re-affirmed at Gate
   3** once those attributions exist, and Gate 5 carrying SCA-001's
   header-only map forward through `accumulate_supersession_map.py
   --allow-empty` (no `--delta`, never hand-merged)?

2. **`_REFERENCES.md` (`OI-B`, §4 row 3).** All 64 pin "revision 1.1"
   (measured), and `D-PEC-64` §3.3 explicitly excludes `_REFERENCES.md` from
   this session's fence, so it cannot be refreshed here at any gate. Confirm
   it is recorded in `Handoff_State.md` as a deferred obligation owned by
   resumed `PROJECT_SETUP` — rather than widening this SCA's fence to reach
   it?

Two questions are deliberately **not** asked here:

- the `_CONTEXT.md` basis-pointer **refresh-vs-deferral** decision — **Gate 4**
  work; and
- the §3 **parser-sentence handling** — **Gate 3** drafting work, where the
  exact text is drafted and refuted on its merits (**C-4**; it was wrongly
  raised to a Gate 2 condition in the first presentation).

---

## 10. Corrections log — round R-2b-g2

Fourteen findings, all `ACCEPTED` at fan-in. Every claim below was
independently re-verified against repo state in this session before the
correction was applied.

| C | Finding(s) | Correction |
|---|---|---|
| **C-2** | F1 (MAJ) | Expected closure verdict `OPEN_PENDING_DERIVATIVE_CLOSURE` → **`CLOSED_FOR_SCOPE_CHANGE_ONLY`**, obligations carried in `DownstreamRerunState = FROZEN`; final call is a Gate 5 fact. Refuted by my own cited precedent (SCA-001 `Handoff_State.md` lines 17/19/23) and by `AGENT_SCOPE_CHANGE.md`:685 scoping `DerivativePackageState` to decomposition-local surfaces. §7 |
| **C-3** | F2 (MAJ) | `projects/pec/AGENTS.md` has **no revision pin** (grep-verified; deliberately revision-agnostic per its own lines 84 and 148). Row 10 split: `_COORDINATION.md` alone is `STALE_ON_ACCEPTANCE`; AGENTS.md is `CURRENT` (new row 10b). **An unmeasured claim was presented under a "measured" label — the error I most need not to repeat.** §4 |
| **C-4** | F3, F4, F5 (MAJ) | **Owner question 3 withdrawn**; `F-4` marked WITHDRAWN with all three defects named — wrong anchor (`EvidenceFile` is the DAG exhibit, which carries the sentence at line 143, not `SOFTWARE_DECOMP.md`), preserve-verbatim conflicts with A003/A004's reconciliation mandate (§7:528 reads the clause as non-mapping rationale), and drafting guidance was wrongly raised to a Gate 2 condition. `Dependencies.csv` → unconditional `CURRENT`; `dependency-extract` rerun removed. §4 row 2, §6, §8, §9 |
| **C-5** | F6 (MIN) | No-binding recommendation confirmed lawful but made **explicitly conditional** on Gate 3 attributions remaining consumptive of the PRD; re-affirmed at Gate 3. New risk-register row. §5, §7 |
| **C-6** | F7 (MAJ) | §3 `Disposition` cells normalized to the contract enum `DIRECT_EDIT \| RECOMPUTE \| NO_CHANGE`, with conditions moved to a `Status / notes` column so Gate 5's `Handoff_State.md` can carry them. `_Evaluation/DecompCoverage` → `RECOMPUTE`; `Supersession_Map.csv` added as `RECOMPUTE`. §3 |
| **C-7** | F8 (MIN) | `ContextBudgetQA.csv` removed from the "verification failure if changed" list — it is **in-fence writable** per `D-PEC-64` §3.2 (expected unchanged; editable only via Gate-3 text). §2 and §3 now state one post-check contract. §2 |
| **C-8** | F9 (MIN) | Wave plan §7 is **three re-pin points + one annotation**; the phantom "re-pin point 4" removed and the three points enumerated as §7 states them. §4 rows 4, 9 |
| **C-9** | F10 (MIN) | DAG-exhibit annotation is **partly extant** — lines 347 and 362 already carry it; the scheduled act targets **§1 pins only**; lines 47/70/91/99/108 are correct historical narrative needing no edit. §4 row 4 |
| **C-10** | F11 (MIN) | "0 of 255 rows carry a `SupportsObjectives` value" rephrased — the v3.1 schema has **no objective column at all** (29 columns enumerated), so the mapping cannot propagate there by construction. My phrasing implied an empty column that exists. §4 row 2 |
| **C-11** | F12 (MIN) | "converter cannot be invoked at all" softened — argparse requires the **flag**, not a correct value; invocation is mechanically possible, the caller simply has no legal value to pass. §6 |
| **C-12** | F13 (MIN) | §6 Scope Ledger removed from A001's affected-sections list — it is an 8-line pointer to `ScopeLedger.csv` carrying no per-row mapping; nothing in it changes. §1, §2 |
| **C-13** | F14 (MIN) | The two stale "outside change class" statements (`Decision_Log.md` D-5 and the Gate 1 W-1 finding row) annotated in place as superseded by C-1. `Decision_Log.md` |

### What these corrections have in common

Ten of the fourteen are overstatement in the direction of **more alarm, more
coupling, more staleness, more owner questions** than the evidence supports:
a pessimistic closure verdict contradicted by precedent I had already quoted;
a stale-file claim I never measured; a dependency coupling whose anchor I did
not check before raising it to a gate condition; a converter failure mode
stated more absolutely than argparse behaves.

Caution that inflates findings is not conservative — it spends owner attention
on false positives and, in the `AGENTS.md` case, put an unverified assertion
behind the word "measured". The Gate 3 return must hold every claim to the
standard the Gate 1 return did meet: measure it, cite the measurement, and
check whether the evidence already in hand contradicts the conclusion before
presenting it.
