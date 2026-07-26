# TASK RUN 2026-07-26 — DEL-10-10 `ScopeOfWork.md` REQ-011 boundary-owner repair

**Packet:** `D-PEC-66` act 2 (`execution/_Coordination/_DECISIONS/D-PEC-66_post_repair_followons.md`)
**Form:** sealed Agent 2 revision dispatch, file-tool-only (Read/Write/Edit; no Bash, no git, no probes)
**Target:** `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md`
**Write set:** that `ScopeOfWork.md` (one line changed) and this run record. `_STATUS.md` untouched.

## 1. The defect

`REQ-011` excludes ten adjacent acts and, for the parsing/rebuild family, cites
the owning deliverables inline:

> it shall implement no rebuild, no incremental reconcile, no drift
> classification, and no parity diff (`DEL-03-01`, `DEL-03-02`, `DEL-03-03`,
> `DEL-03-04`)

and closes its exclusion enumeration with `(CLM-018)`, plus a `DL-11` boundary
sentence citing `CLM-017`.

Neither cited claim named the owners of two of those excluded acts:

- **CLM-018** (the adjacent-acts enumeration) named `DEL-02-05`, `DEL-03-01`,
  `DEL-10-02`, `DEL-10-03`, `DEL-01-05`, `DEL-03-04`, `DEL-10-11`, `DEL-03-06`,
  `DEL-10-01`, `DEL-01-04`, and `PROJECT_SETUP` — **not** `DEL-03-02` and
  **not** `DEL-03-03`.
- **CLM-017** (the `DecisionRef` claim) names only `DEL-03-01`, as the
  counterparty of the `DL-11` "not a reconciler feature" boundary.

The contract's only other mention of `DEL-03-02`/`DEL-03-03` is **CLM-015**, a
phase-staging claim that assigns no ownership (it records both as `P1` in the
`PhaseHint` column and nothing more).

So two acts excluded by a boundary requirement — incremental reconcile and
drift classification — resolved to no named owner in the claim(s) `REQ-011`
cites. That breaks the convention upheld across the `D-PEC-63` wave and now
machine-checked as QA item 21 (`check_boundary_owner_resolution.py`, which
binds owners from the cited claim's text).

## 2. Option chosen: **Option A** — extend `CLM-018`'s enumeration

### Register-truth verification (done before the edit)

Read `projects/pec/execution/_Decomposition/Deliverables.csv` rows:

| Row | Name | Description | `CoversScopeItems` |
|---|---|---|---|
| `DEL-03-02` | Incremental reconcile on Git delta | "Reconciliation keyed on Git delta since last examined SHA." | `SOW-018` |
| `DEL-03-03` | Drift classification | "Classified drift between successive snapshots, reported as DriftFindings; sources never modified." | `SOW-019` |

Both are `PKG-03`, `BACKEND_FEATURE_SLICE`, `P1`. The two deliverables own
**exactly** the two acts `REQ-011` excludes — the extension is true to register
truth, not an approximation.

### Why Option A over Option B

1. `CLM-018`'s own framing already is this list: "The acts adjacent to this
   validation are owned elsewhere and are cited here, never discharged," followed
   by an act → owner → scope-item enumeration. Two more adjacent acts fit the
   framing exactly; nothing about the claim had to be re-purposed.
2. `CLM-018` is already the claim `REQ-011` cites for this enumeration, and the
   Output and Evaluation Matrix row for `REQ-011` already cites `CLM-018`. No
   citation, no matrix row, and no `REQ-011` text needed to change.
3. Option B would have required either widening `CLM-017` — a claim whose
   subject is the `SOW-064` ledger `DecisionRef` cell (`DL-10`, `DL-11`,
   `SCA-001`), which carries no statement about incremental reconcile or drift
   classification and could not have truthfully absorbed them — or minting a new
   claim ID. Both are larger and less honest diffs than Option A.
4. `CLM-015` already names `DEL-03-02` and `DEL-03-03` in this contract's own
   voice as `P1` neighbours, so no new deliverable is introduced to the contract
   by this edit and `CLM-015`'s enumeration remains true unchanged.

### Evidence-citation consistency

The new sentence cites scope items only (`SOW-018`, `SOW-019`), matching the
style of `CLM-018`'s later entries (`DEL-10-02` (`SOW-055`), `DEL-10-03`
(`SOW-025`), `DEL-03-04` (`SOW-020`), …). Its first two entries additionally
cite `CLM-010`/`CLM-011` because those upstream contracts are quoted in this
document; `DEL-03-02` and `DEL-03-03` are not quoted here, so no claim
back-reference is asserted. Naming style is the contract's existing plain
backticked deliverable ID form used throughout `CLM-018`.

### Constraint conformance

No new scope; no new `REQ-*`/`CLM-*`/`AC-*`/`VER-*`/`TBD-*`/`CON-*`/`AX-*` ID;
no built-state claim; six L2 headings preserved; inline-YAML frontmatter
untouched; ID grammar preserved; all other bytes identical. Exactly one line of
the contract changed.

## 3. Exact before/after diff

One line changed — `CLM-018` (line 317). The change is the insertion of one
sentence between the existing `DEL-03-01` sentence and the existing
`DEL-10-02` clause; the rest of the line is byte-identical.

**Before (excerpt of line 317, at the insertion point):**

```
... The one-command full rebuild through which self-ingestion runs is `DEL-03-01` (`SOW-010`, `SOW-021`, CLM-011). The standing kill test is `DEL-10-02` (`SOW-055`); ...
```

**After (same excerpt):**

```
... The one-command full rebuild through which self-ingestion runs is `DEL-03-01` (`SOW-010`, `SOW-021`, CLM-011). Incremental reconcile keyed on Git delta is `DEL-03-02` (`SOW-018`), and drift classification between successive snapshots is `DEL-03-03` (`SOW-019`). The standing kill test is `DEL-10-02` (`SOW-055`); ...
```

**Inserted text, verbatim:**

```
Incremental reconcile keyed on Git delta is `DEL-03-02` (`SOW-018`), and drift classification between successive snapshots is `DEL-03-03` (`SOW-019`).
```

No other line of `ScopeOfWork.md` was added, removed, or modified. `REQ-011`,
`CLM-017`, `CLM-015`, and the Output and Evaluation Matrix are unchanged.

## 4. Manual re-check (by inspection; no tools available to this dispatch)

Every act enumerated in `REQ-011`'s exclusion, resolved against the claims
`REQ-011` cites (`CLM-018` as amended, and `CLM-017`):

| `REQ-011` excluded act | Owner named in `REQ-011` | Named in cited claim? |
|---|---|---|
| define register/work-graph grammar; parse dependency register or work graph | `DEL-02-05` | `CLM-018` ✓ ("Reading the DAG's file form … is `DEL-02-05`") |
| implement rebuild | `DEL-03-01` | `CLM-018` ✓; also `CLM-017` ✓ |
| implement incremental reconcile | `DEL-03-02` | `CLM-018` ✓ **(added by this repair)** |
| implement drift classification | `DEL-03-03` | `CLM-018` ✓ **(added by this repair)** |
| implement parity diff | `DEL-03-04` | `CLM-018` ✓ ("harness parity diffing is `DEL-03-04`") |
| run kill test | `DEL-10-02` | `CLM-018` ✓ |
| run no-ruling-write verification | `DEL-10-03` | `CLM-018` ✓ |
| assert rebuild bound | `DEL-03-06` | `CLM-018` ✓ |
| materialize dependency edge; compute blocker state; scaffold | `PROJECT_SETUP` under `D-PEC-62` | `CLM-018` ✓ (final sentences) |
| create/modify/delete register, decomposition, ledger, decision, or lifecycle file | — (`CLM-018`) | `CLM-018` ✓ ("Amending decomposition truth is the scope-change workflow's.") |

**Verification statement:** after this edit, every act excluded by `REQ-011`
resolves to a named owner in the claim(s) `REQ-011` cites. The two previously
unresolved owners, `DEL-03-02` and `DEL-03-03`, now appear verbatim in
`CLM-018`'s text, which is the text `check_boundary_owner_resolution.py` binds
owners from.

## 5. Anomalies

None material. Two notes for the dispatcher:

1. `CLM-018` also names `DEL-10-11` (parity metric, `SOW-093`), `DEL-01-05`,
   `DEL-10-01`, and `DEL-01-04` — adjacent acts that `REQ-011` does not
   enumerate. That direction (claim names more than the requirement excludes) is
   not a defect under the convention and was left untouched.
2. This dispatch is file-tool-only, so `validate_scope_of_work.py` and
   `check_boundary_owner_resolution.py` were **not** run here. Section 4 is a
   manual inspection result. Machine verification is the dispatcher's at fan-in,
   along with the new contract `sha256`.
