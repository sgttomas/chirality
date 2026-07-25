---
amendment_id: SCA-002
doc_kind: scope_change.propagation_plan
decomp_variant: SOFTWARE
gate: 4
created: 2026-07-25
status: awaiting_gate_4_approval
scope_width: O-A
authority: D-PEC-64 (+ §4.3 owner amendments #1 and #2)
basis: SOFTWARE_DECOMP.md revision 1.1 (current_basis)
basis_pins: SOFTWARE_DECOMP.md ad944a2bfa7784778afa8558d8f81762; Deliverables.csv 6d2b290b0c869fc1d51d626a1714abec; ScopeLedger.csv 49e0cff9af647e41966b7a3334641919
---

# SCA-002 — Propagation Plan (Gate 4)

Planning only. Nothing is applied: decomposition truth is untouched until this
plan is approved and Gate 5 is released. Basis pins re-verified unchanged at
Gate 4 open (all three md5s match).

The Gate 3 approved text is **final and is the only text Gate 5 may apply**
(`D-PEC-64` §4.3 amendment #2 record). This plan adds no amendment content; it
sequences the write pass, carries the one remaining owner decision
(`_CONTEXT.md` basis pointers), and makes the post-check mechanical.

---

## 1. Propagation manifest

Contract enum: `DIRECT_EDIT` / `RECOMPUTE` / `NO_CHANGE`.

### 1a. Authoritative truth (applied per the Gate-3-approved exact text)

| Surface | Class | Action | Count |
|---|---|---|---|
| `_Decomposition/ScopeLedger.csv` | `DIRECT_EDIT` | A001 — set `ObjectiveIDs` on 20 IN rows; no other column, no other row | 20 cells |
| `_Decomposition/Deliverables.csv` | `DIRECT_EDIT` | A002 — set `SupportsObjectives` on 17 rows; `DEL-03-01` untouched | 17 cells |
| `_Decomposition/SOFTWARE_DECOMP.md` | `DIRECT_EDIT` | A003a header · A003b 4 objective rows · A003c post-table note · A003d mapping-notes block · A004 2 metric rows · A005a DL-17 append · A005b revision row 1.2 · A007 §5 line 376 · A008 front matter | 9 edit sites |
| `_Decomposition/_LATEST.md` | `DIRECT_EDIT` | A006 — full-file replacement per the approved successor text, Gate-5 slots filled from measurement | 1 file |
| `_Decomposition/ContextBudgetQA.csv` | `NO_CHANGE` | Gate 3 determination — no envelope change in scope | 0 |
| `_Decomposition/Companion_Inventory.csv` | `NO_CHANGE` | Gate 3 determination — no filename, role or cited count changes | 0 |

### 1b. Variant-local metadata (propagation writes)

| Surface | Class | Action | Count |
|---|---|---|---|
| 17 × `_CONTEXT.md` — `SupportsObjectives` line | `DIRECT_EDIT` | Restate the register value; **propagation default, confirmed** — leaving these would contradict the register the file exists to restate | 17 lines |
| 64 × `_CONTEXT.md` — basis-pointer lines | *(pending)* | **§2 owner decision — option (i), (ii) or (iii)** | 0 / 17 / 64 |
| 64 × `_STATUS.md` | `NO_CHANGE` | Narrowed out of the fence at §3.2 — a mapping amendment changes no lifecycle state | 0 |
| 64 × `_REFERENCES.md` | `NO_CHANGE` | Fence-excluded (§3.3). Stale rev-1.1 pin persists — `OI-B`, deferred at Gate 2 | 0 |
| 64 × `Dependencies.csv`, `_DEPENDENCIES.md` | `NO_CHANGE` | Fence-excluded; the v3.1 schema has no objective column | 0 |

### 1c. Snapshot artifacts (SCOPE_CHANGE-owned)

| Artifact | Class | Action |
|---|---|---|
| `Pre_Change_Coverage.json` | `DIRECT_EDIT` | Copy from `COV_SCA002_PRECHANGE_2026-07-25_1040/coverage_summary.json` — discharges the Gate 1 deferral and makes the snapshot self-contained |
| `Amendment_Actions.csv` | `DIRECT_EDIT` | Finalise: row 3b conditional → firm (Q3 ruled), A008 `PROPOSED - NOT YET RULED` → approved, contingency notes resolved |
| `Supersession_Map.csv` | `RECOMPUTE` | `accumulate_supersession_map.py --prior-map <SCA-001 map> --allow-empty`, **no `--delta`** — never hand-merged |
| `Post_Change_Coverage.json` | `RECOMPUTE` | Copy from the post-change AUDIT_DECOMP snapshot |
| `Handoff_State.md` | `DIRECT_EDIT` | New — closure verdict, derivative table, deferrals, next owners |
| `RUN_SUMMARY.md` | `DIRECT_EDIT` | New — actions taken, pre/post comparison, state fields, CHANGE handoff |
| `_ScopeChange/_LATEST.md` | `DIRECT_EDIT` | Repoint SCA-001 → SCA-002 (the Gate 5 act; it names SCA-001 until then by design) |

### 1d. Derivative evidence

| Surface | Class | Action |
|---|---|---|
| `_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_*` | `RECOMPUTE` | Post-change AUDIT_DECOMP, run **inline** (Agent 2 dispatch unavailable), scope `ALL`, compared against the pre-change baseline |
| `_Evaluation/DecompCoverage/_LATEST.md` | `DIRECT_EDIT` | Pointer update per the tool contract |

**Manifest totals:** `DIRECT_EDIT` 20 + 17 cells, 9 doc edit sites, 17 (or 34 /
81) `_CONTEXT.md` lines, 7 snapshot artifacts, 2 pointers · `RECOMPUTE` 3 ·
`NO_CHANGE` 6 surface classes (192 deliverable-local files untouched).

---

## 2. The `_CONTEXT.md` basis-pointer decision — Gate 4's owner question

### What is stale, exactly

All 64 `_CONTEXT.md` carry a byte-identical provenance block at lines 29–33
(measured; one occurrence per file, zero variants):

```
29: Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
30: `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (`current_basis`,
31: SCA-001 successor). Fields templated deterministically from
32: `Deliverables.csv`; this file restates register truth and is not an
33: independent authority.
```

After Gate 5 the stale claim is specifically **"revision 1.1 (`current_basis`)"**
— revision 1.1 stops being `current_basis` the moment 1.2 is accepted.

### A subtlety worth deciding deliberately

The sentence conflates two different facts: *what the file was scaffolded
from* (historically revision 1.1 — **true, and it stays true**) and *what
basis is current* (revision 1.2 after Gate 5). A naive swap of "1.1"→"1.2" and
"SCA-001"→"SCA-002" fixes the `current_basis` label but makes the
scaffolded-from claim **false** — the files were not scaffolded from 1.2.

Two deterministic variants, both identical across every touched file:

**P-swap** (2 lines changed):
```
30: `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.2 (`current_basis`,
31: SCA-002 successor). Fields templated deterministically from
```
Simplest. Manufactures a false historical claim.

**P-supersede** *(recommended)* (lines 30–31 → 3 lines):
```
30: `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (SCA-001
31: successor), superseded by revision 1.2 (`current_basis`, SCA-002
32: successor). Fields templated deterministically from
```
Keeps the scaffold history true, removes the false `current_basis` claim, and
records the lineage. Costs one line per file.

Both stay inside the §3.2 line class (ii) — "the decomposition
basis/provenance pointer". Neither touches any other content.

### Method (whichever option is chosen)

**Surgical line replacement, not regeneration.** The exact old string is
byte-identical across all 64, so the edit is a literal two-line match-and-
replace with no templating, no re-derivation from `Deliverables.csv`, and no
risk of collateral field drift. Line 29 (`Scaffolded under D-PEC-62`) is
**never** touched — the scaffold provenance is a true historical fact.
Verification: post-edit, grep for `revision 1.1 (\`current_basis\`` must return
0 hits in the touched set, and every untouched file must be byte-identical.

### The three options, with honest costs

| | Scope | Benefit | Cost |
|---|---|---|---|
| **(i) Refresh all 64** | 64 pointer lines (+17 mapping lines) | **Zero stale pointers.** No follow-on obligation for this surface | Touches **47 files whose mapping content is unchanged** — a larger Gate 5 diff, and 47 files whose only change is a pointer line. Larger blast radius for the post-check to bound |
| **(ii) Refresh only the 17 touched** *(recommended)* | 17 pointer lines (+17 mapping lines) | Minimal diff; each touched file is internally consistent; the 17 are being edited anyway so the marginal cost is ~zero | **Leaves 47 stale pointers** with a recorded rerun obligation in `Handoff_State.md` |
| **(iii) Defer all 64** | 0 pointer lines | Smallest possible diff | **Leaves 64 stale pointers**, including in the 17 files SCA-002 *is* editing — those would restate a new mapping while pointing at the superseded basis. Internally incoherent |

### Recommendation: **(ii)**, with reasoning

Option (iii) is hard to defend: editing a file's mapping line while leaving its
basis pointer naming the superseded revision produces a file that contradicts
itself in the same edit. That leaves (i) versus (ii).

**(ii) is recommended because the residual obligation it creates is one this
project already owes and has already deferred.** `OI-B` — all 64
`_REFERENCES.md` pinning revision 1.1 — was deferred by owner ruling at Gate 2
and is fence-excluded (§3.3), so it *cannot* be closed by this session at any
option. A pointer sweep across deliverable-local metadata is therefore
happening later regardless. Option (ii) lets `OI-B` (64 `_REFERENCES.md`) and
the 47 residual `_CONTEXT.md` pointers land in **one PROJECT_SETUP
pointer-sweep packet**, where they can share a single deterministic method and
a single verification.

Option (i) is not wrong — it strictly reduces staleness and I would apply it
without objection. Its real cost is that it touches 47 files SCA-002 has no
substantive business editing, which widens the Gate 5 diff and the post-check
surface for a benefit that a later sweep delivers anyway. If you prefer zero
stale `_CONTEXT.md` pointers at closure and accept the wider diff, choose (i);
the method and verification are identical.

Under **(ii)** the `Handoff_State.md` obligation reads: *47 deliverable
`_CONTEXT.md` basis pointers remain at revision 1.1; owner resumed
PROJECT_SETUP; recommended to be executed together with `OI-B` in a single
pointer-sweep packet.*

---

## 3. Bounded post-check design (mechanical)

The `D-PEC-64` §4.3 window **as amended** — base + amendment #1 (§5 line) +
amendment #2 (front matter, DL-17). Gate 5 verification enforces exactly this
list; anything else differing is a **verification failure**.

### Complete allowed-change enumeration

**`_Decomposition/ScopeLedger.csv`** — `ObjectiveIDs` column only, on exactly
these 20 rows: `SOW-001, 003, 011, 012, 013, 014, 015, 016, 017, 021, 025,
040, 042, 052, 053, 054, 056, 088, 089, 094`. All other cells byte-identical.

**`_Decomposition/Deliverables.csv`** — `SupportsObjectives` column only, on
exactly these 17 rows: `DEL-00-01, 00-03, 01-01, 01-03, 01-05, 01-06, 02-01,
02-02, 02-03, 02-04, 02-05, 02-06, 02-07, 03-06, 08-01, 08-02, 10-03`. All
other cells byte-identical — **including `DEL-03-01`**.

**`_Decomposition/SOFTWARE_DECOMP.md`** — exactly these sites:

| Site | Lines | Authority |
|---|---|---|
| Front matter revision block | 6, 7, 8, 11 | §4.3 amendment **#2** |
| §3 table header | 318 | window (§3 text) |
| §3 rows `OBJ-001`, `OBJ-002`, `OBJ-004`, `OBJ-005` — cols 4–5 only | 320, 321, 323, 324 | window (§3 text) |
| §3 post-table note | 327–330 | window (§3 / mapping-notes) |
| §3 mapping-notes block | 332–338 | window (mapping-notes) |
| §5 envelope-posture line | 376 | §4.3 amendment **#1** |
| §7 metric row | 528 | window (§7 text) |
| §7 revision row | 532 | window (§7 text) |
| §11 Decision Log — DL-17 appended | after 625 | §4.3 amendment **#2** |
| §12 Revision History — row 1.2 appended | after 640 | window (revision-history) |

Explicitly **unchanged** in this file: §3 rows `OBJ-003` (322) and `OBJ-006`
(325); §7 `ContextEnvelopeCounts` (529); front-matter `status` (5) and
`source_corpus` (12); §5 lines 377–379; every other line.

**`_Decomposition/_LATEST.md`** — full-file replacement (authority: §3.2
writable target; outside the byte-window by construction).

**`_CONTEXT.md`** — line class (i) `SupportsObjectives` on the 17; line class
(ii) basis pointer on 0 / 17 / 64 per the §2 ruling. No other line in any of
the 64.

**Everything else byte-identical**, specifically: the 11 residue IN rows
(`SOW-022, 023, 033, 034, 035, 036, 037, 038, 044, 063, 087`); the 9 residue
deliverables (`DEL-00-02, 03-05, 05-01, 07-02, 07-03, 07-04, 07-05, 08-05,
10-08`); all 14 `OUT` and 9 `TBD` rows; `ContextBudgetQA.csv`;
`Companion_Inventory.csv`; all 64 `_STATUS.md`, `_REFERENCES.md`,
`_DEPENDENCIES.md`, `Dependencies.csv`, `_SEMANTIC.md`; `docs/PRD.md`.

### Post-check assertions (all six re-run against real files)

1. Union invariant — 0 violations across all 64 deliverables.
2. Residue — 11 IN rows and 9 deliverables byte-identical and still unmapped.
3. Token grammar — every changed cell matches `^OBJ-[0-9]{3}$` after `;`-split.
4. Topology — 94 (71/14/9), 64, 11, 6; envelopes S 28 / M 34 / L 2 / XL 0.
5. Window — exactly 20 + 17 changed rows; two columns only; `DEL-03-01`
   unchanged; `SOW-021` ⊆ `{OBJ-005}`.
6. `git status --porcelain` lists **only** paths in the §3.1/§3.2 enumeration.

Plus the collateral checks: `analyze_dep_closure.py` unchanged from the
D-PEC-62 values (64 files, 255 rows, 135/120, 62 nodes/120 edges, orphans 2,
SCCs 0) and the census still `64 OPEN` via the `grep` form — **never**
`count_workspace_state.sh` (`D-PEC-64` §4.4).

---

## 4. Downstream rerun / deferral table (for `Handoff_State.md`)

| Item | Owner | State | Required action |
|---|---|---|---|
| `AUDIT_DECOMP` post-change | SCOPE_CHANGE (inline, this session) | executed at Gate 5 | Scope `ALL`; compare to the pre-change baseline |
| `SCOPE_CHANGE_POSTCHECK` | SCOPE_CHANGE (this session) | executed at Gate 5 | The six assertions in §3 |
| **`OI-B`** — 64 `_REFERENCES.md` rev-1.1 pins | resumed `PROJECT_SETUP` | **`DEFERRED`** (Gate 2 owner ruling) | Fence-excluded (§3.3); pointer sweep |
| **47 (or 0) residual `_CONTEXT.md` pointers** | resumed `PROJECT_SETUP` | **per the §2 ruling** | Under (ii): same sweep as `OI-B` — recommended as one packet |
| DAG-exhibit §1-pins annotation | resumed `PROJECT_SETUP` | `SCHEDULED` | Wave plan §7's one annotation (lines 347/362 already carry provenance) |
| D-PEC-63 re-pins (3 points) | resumed `PROJECT_SETUP` | `SCHEDULED` | md5s + rev-1.2 SHA; `{REV_1_2_COMMIT}` in §3; confirm bare `OBJ-NNN` survived |
| `_COORDINATION.md` rev-1.1 citations | resumed `PROJECT_SETUP` | `STALE_ON_ACCEPTANCE` | §3.1 owner-governance refresh at closure |
| `projects/pec/AGENTS.md` pointer refresh | resumed `PROJECT_SETUP` | `CURRENT` (no revision pin) | A chosen governance act per §2.4, not staleness repair |
| `_DomainEngines/pec/LOOP_RECEIPTS.md` receipt | resumed `PROJECT_SETUP` | `SCHEDULED` | §2.4 resumption step (a) |
| Closure commit | resumed `PROJECT_SETUP` | `SCHEDULED` | §3.6(b), from this session's handoff file list |
| `dependency-extract` | — | `NOT_REQUIRED` | No topology change; no objective column in the v3.1 schema |
| Estimates / schedules | — | `NOT_APPLICABLE` | No such surface exists |

---

## 5. Gate 5 execution sequence

Each step carries its verification. **Abort and return on any failure** — do
not proceed to a later step.

| # | Step | Verification |
|---|---|---|
| 1 | Re-verify the three basis md5s against the pins | All three match, else halt (basis drifted since Gate 3) |
| 2 | Apply **A001** — 20 `ObjectiveIDs` cells | Row count 20; two-column containment; token grammar |
| 3 | Apply **A002** — 17 `SupportsObjectives` cells | Row count 17; `DEL-03-01` untouched; union invariant 0 violations |
| 4 | Apply **A003a/b/c/d, A004, A005a, A005b, A007, A008** to `SOFTWARE_DECOMP.md` | Each old-text pair matched exactly once before replacement; the §3 objective-side view agrees with the registers for all six objectives (with range expansion); no site outside §3's enumeration differs |
| 5 | Run the six post-check assertions (§3) | All pass |
| 6 | Run collateral checks — `analyze_dep_closure.py`, census `grep` | Unchanged from D-PEC-62 values; `64 OPEN` |
| 7 | Apply `_CONTEXT.md` propagation — 17 mapping lines + pointer lines per the §2 ruling | Exact-string match per file; no other line differs; grep for the stale pointer returns 0 in the touched set |
| 8 | Run post-change `AUDIT_DECOMP` **inline**, scope `ALL` | Snapshot written; `_LATEST.md` pointer updated; compared against the pre-change baseline |
| 9 | Copy `Pre_Change_Coverage.json` and `Post_Change_Coverage.json` into this snapshot | Both present; the snapshot is self-contained |
| 10 | Generate `Supersession_Map.csv` via `accumulate_supersession_map.py --prior-map <SCA-001> --allow-empty` (no `--delta`) | Header-only map carried forward; not hand-edited |
| 11 | Finalise `Amendment_Actions.csv` | 10 rows; 3b firm; A008 approved; no `PROPOSED` string remains |
| 12 | Apply **A006** — `_Decomposition/_LATEST.md` full replacement, slots filled from measurement | Every `{SLOT}` resolved; no literal `{` remains |
| 13 | Write `RUN_SUMMARY.md` and `Handoff_State.md` with the seven state fields | `DecompositionTruthState COMPLETE`; `DerivativePackageState COMPLETE`; `ContentRemediationState NOT_REQUIRED`; `DownstreamRerunState FROZEN`; `MetadataAlignmentState NOT_REQUIRED`; `AuditState` from step 8; `ReadyForNextPhase REGEN_ONLY`; `ClosureVerdict CLOSED_FOR_SCOPE_CHANGE_ONLY` |
| 14 | Repoint `_ScopeChange/_LATEST.md` to SCA-002 | Exactly one active snapshot named; artifact set complete |
| 15 | `git status --porcelain` scope check | Only §3.1/§3.2 paths listed |
| 16 | Return the handoff — file list + recommended commit message | **No commit performed** |

### Git posture — explicit

**SCOPE_CHANGE performs no git operation at any step.** No `add`, no `commit`,
no `push`. `AGENT_SCOPE_CHANGE.md` assigns git staging to CHANGE, and
`D-PEC-64` §3.6(b) assigns the SCA-002 closure commit to **resumed
`PROJECT_SETUP`**, working from this session's handoff file list. Step 16
produces that list and a recommended message; someone else runs it.

Recommended commit message (per the `AGENT_SCOPE_CHANGE.md` STRUCTURE format):

```text
scope: SCA-002 — deliverable→objective mapping for the Phase 2.2 wave scope

Variant: SOFTWARE
Actions: 10 (MODIFY:10)
Affected entities: ScopeLedger.csv (20 IN rows), Deliverables.csv (17
deliverables), SOFTWARE_DECOMP.md (§3/§5/§7/§11/§12 + front matter),
_Decomposition/_LATEST.md, _CONTEXT.md propagation, SCA-002 snapshot,
AUDIT_DECOMP pre/post baselines
```

---

## 6. Gate 4 approval question

**Two decisions.**

**Q1 — the `_CONTEXT.md` basis-pointer scope.** Choose **(i)** refresh all 64
pointer lines, **(ii)** *(recommended)* refresh only the 17 files already being
edited and record a deferral + rerun obligation for the other 47, or **(iii)**
defer all 64. Within (i) or (ii), the line-text variant is **P-supersede**
*(recommended — keeps the scaffold history true)* or **P-swap**.

The 17 `SupportsObjectives` restatement lines refresh under every option —
that is the propagation default and is confirmed, not in question.

**Q2 — Do you approve this propagation plan and release Gate 5?**
