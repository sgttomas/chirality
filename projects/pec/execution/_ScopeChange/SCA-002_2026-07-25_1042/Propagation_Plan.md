---
amendment_id: SCA-002
doc_kind: scope_change.propagation_plan
decomp_variant: SOFTWARE
gate: 4
version: v2.1 (v2 + Agent 0 plan amendment: two-pass audit)
created: 2026-07-25
status: gate_4_approved; gate_5_executed_awaiting_owner_confirmation
scope_width: O-A
authority: D-PEC-64 (+ §4.3 owner amendments #1 and #2)
basis: SOFTWARE_DECOMP.md revision 1.1 (current_basis)
basis_pins: SOFTWARE_DECOMP.md ad944a2bfa7784778afa8558d8f81762; Deliverables.csv 6d2b290b0c869fc1d51d626a1714abec; ScopeLedger.csv 49e0cff9af647e41966b7a3334641919
line_coordinates: PRE-change (revision 1.1); post-change anchor map in §3c
---

# SCA-002 — Propagation Plan (Gate 4) · v2

> **v2 revision note.** v1 was refuted (round R-2b-g4); 22 findings accepted.
> The measurement work held — 64-file byte-identity, line anchors,
> postcheck↔text bijection, git posture. The defects were **executability**
> (Gate 5 could not have run this plan without inventing text: the
> `_CONTEXT.md` mapping lines had no exact pairs, `Decision_Log.md` was
> missing from the manifest entirely) and **an inverted option analysis** —
> my `_CONTEXT.md` recommendation is **flipped to (i)** in §2. Corrections
> logged in §7.

Planning only. Nothing is applied: decomposition truth is untouched until this
plan is approved and Gate 5 is released. Basis pins re-verified unchanged at
this revision.

The Gate 3 approved text is **final and the only text Gate 5 may apply**
(`D-PEC-64` §4.3 amendment #2 record). This plan adds no amendment content.

---

## 1. Propagation manifest

Contract enum: `DIRECT_EDIT` / `RECOMPUTE` / `NO_CHANGE`. Derivative-package
state per Gate 4 item 6: `CURRENT` / `STALE_REBUILD_REQUIRED` /
`DEFERRED_BY_HUMAN`, consistent with the Gate 2 corrected table.

### 1a. Authoritative truth (per the Gate-3-approved exact text)

| Surface | Class | State | Action | Count |
|---|---|---|---|---|
| `_Decomposition/ScopeLedger.csv` | `DIRECT_EDIT` | `CURRENT` after | A001 — `ObjectiveIDs` on 20 IN rows only | 20 cells |
| `_Decomposition/Deliverables.csv` | `DIRECT_EDIT` | `CURRENT` after | A002 — `SupportsObjectives` on 17 rows; `DEL-03-01` untouched | 17 cells |
| `_Decomposition/SOFTWARE_DECOMP.md` | `DIRECT_EDIT` | `CURRENT` after | A003a, A003b(×4 rows), A003c, A003d, A004(×2 rows), A005a, A005b, A007, A008 | **10 edit sites** |
| `_Decomposition/_LATEST.md` | `DIRECT_EDIT` | `CURRENT` after | A006 — full-file replacement, slots filled from measurement | 1 file |
| `_Decomposition/ContextBudgetQA.csv` | `NO_CHANGE` | `CURRENT` | Gate 3 determination | 0 |
| `_Decomposition/Companion_Inventory.csv` | `NO_CHANGE` | `CURRENT` | Gate 3 determination | 0 |

### 1b. Variant-local metadata (propagation writes)

| Surface | Class | State | Action | Count |
|---|---|---|---|---|
| 17 × `_CONTEXT.md` `SupportsObjectives` (line 12) | `DIRECT_EDIT` | `CURRENT` after | Exact pairs in §2a — **propagation default, confirmed** | 17 lines |
| 64 × `_CONTEXT.md` basis pointer (lines 30–31) | `DIRECT_EDIT` | *(per §2 ruling)* | Exact pair in §2b | 64 / 17 / 0 |
| 64 × `_STATUS.md` | `NO_CHANGE` | `CURRENT` | Narrowed out at §3.2 — no lifecycle state changes | 0 |
| 64 × `_REFERENCES.md` | `NO_CHANGE` | **`DEFERRED_BY_HUMAN`** | **`OI-B`** — fence-excluded (§3.3), stale rev-1.1 pin persists. Gate 2's `STALE_DEFERRED_BY_FENCE` | 0 |
| 64 × `Dependencies.csv` | `NO_CHANGE` | `CURRENT` | v3.1 schema has no objective column | 0 |
| 64 × `_DEPENDENCIES.md` | `NO_CHANGE` | `CURRENT` | Fence-excluded (§3.3) | 0 |
| 64 × `_SEMANTIC.md` | `NO_CHANGE` | `CURRENT` | Carries no objective mapping and no basis pointer (measured: 0 files with either) | 0 |

**Deliverable-local `NO_CHANGE` total: 256 files** (4 surfaces × 64:
`_STATUS.md`, `_REFERENCES.md`, `Dependencies.csv`, `_DEPENDENCIES.md`) **plus
64 `_SEMANTIC.md` = 320 files untouched.**

### 1c. Snapshot artifacts (SCOPE_CHANGE-owned)

| Artifact | Class | Action |
|---|---|---|
| `Decision_Log.md` | `DIRECT_EDIT` | **Gate 4 ruling record, Gate 5 execution/validation record, final owner confirmation.** SCA-001 precedent — a Gate 5 write target, omitted from v1's manifest |
| `Pre_Change_Coverage.json` | `DIRECT_EDIT` | Register-integrity baseline in `pec-software-register-baseline-v1`, discharging the Gate 1 deferral |
| `Post_Change_Coverage.json` | `RECOMPUTE` | **Same schema** — see §5. Not a raw `coverage_summary.json` copy |
| `Supersession_Map.csv` | `RECOMPUTE` | Accumulator, `--allow-empty`, no `--delta` |
| `Handoff_State.md` | `DIRECT_EDIT` | New — full contract scope, §6 |
| `RUN_SUMMARY.md` | `DIRECT_EDIT` | New — actions, pre/post comparison, **the seven state fields**, CHANGE handoff |
| `_ScopeChange/_LATEST.md` | `DIRECT_EDIT` | Repoint SCA-001 → SCA-002 |
| `Amendment_Preview.md`, `Amendment_Actions.csv`, `Gate3_Simulation.json`, `Impact_Assessment.md`, `Brief.md` | `NO_CHANGE` | **Snapshot immutability** (SCA-001 posture): Gate 5 does not rewrite the substance of approved historical artifacts |

### 1d. Derivative evidence

| Surface | Class | State | Action |
|---|---|---|---|
| `_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_*` | `RECOMPUTE` | new | Post-change AUDIT_DECOMP, **inline**, scope `ALL`, run at sequence step 12 |
| `_Evaluation/DecompCoverage/_LATEST.md` | `DIRECT_EDIT` | `CURRENT` after | Pointer update per the tool contract |

---

## 2. The `_CONTEXT.md` decision — Gate 4's owner question

### 2a. Line class (i) — the 17 mapping lines · **exact pairs, not a rule**

Old text is byte-identical in all 17 files at **line 12** (verified this
session, zero variants):

```
| SupportsObjectives | (none mapped — see §3 mapping notes) |
```

New text per file, restating the Gate-3-approved A002 cell in the same table
format. Paths are relative to `projects/pec/execution/`.

| Deliverable | Path | Line | New text |
|---|---|---|---|
| DEL-00-01 | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-005 |` |
| DEL-00-03 | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-001 |` |
| DEL-01-01 | `PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-001;OBJ-002 |` |
| DEL-01-03 | `PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-005 |` |
| DEL-01-05 | `PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-005 |` |
| DEL-01-06 | `PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-004 |` |
| DEL-02-01 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-001;OBJ-002 |` |
| DEL-02-02 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-001;OBJ-002 |` |
| DEL-02-03 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-001;OBJ-002 |` |
| DEL-02-04 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-001;OBJ-002 |` |
| DEL-02-05 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-001;OBJ-002 |` |
| DEL-02-06 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-001;OBJ-002 |` |
| DEL-02-07 | `PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-001;OBJ-002 |` |
| DEL-03-06 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-005 |` |
| DEL-08-01 | `PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-001 |` |
| DEL-08-02 | `PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-001 |` |
| DEL-10-03 | `PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/_CONTEXT.md` | 12 | `| SupportsObjectives | OBJ-005 |` |

These refresh under **every** option. A file whose stated purpose is to restate
register truth cannot be left contradicting the register in the same edit.

### 2b. Line class (ii) — the basis pointer · **the decision**

All 64 carry a byte-identical provenance block at lines 29–33 (measured: one
occurrence per file, zero variants):

```
29: Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
30: `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (`current_basis`,
31: SCA-001 successor). Fields templated deterministically from
32: `Deliverables.csv`; this file restates register truth and is not an
33: independent authority.
```

After Gate 5 the stale claim is **"revision 1.1 (`current_basis`)"** —
revision 1.1 stops being `current_basis` when 1.2 is accepted.

**P-supersede** *(recommended)* — lines 30–31 → 3 lines:
```
30: `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (SCA-001
31: successor), superseded by revision 1.2 (`current_basis`, SCA-002
32: successor). Fields templated deterministically from
```

**P-swap** — lines 30–31 in place:
```
30: `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.2 (`current_basis`,
31: SCA-002 successor). Fields templated deterministically from
```

**Honest note on P-swap.** v1 called P-swap's scaffolded-from claim "false".
That charge is **contestable**: the sentence's `status:` framing is
`current_basis`, and read as "the accepted decomposition this file restates"
rather than "the artifact this file was generated from", P-swap is defensible.
P-supersede is recommended because it is **unambiguous** — both facts stated
separately — not because P-swap is provably wrong.

**Method (either variant): surgical line replacement, never regeneration.**
The old string is byte-identical across all 64, so the edit is a literal
match-and-replace with no templating step and no risk of collateral field
drift. Line 29 is **never** touched.

### 2c. The three options — recommendation **flipped from v1**

| | Scope | Post-check effect | Authority posture |
|---|---|---|---|
| **(i) all 64** *(recommended)* | 64 pointer lines | **Collapses to one assertion**: `grep -rl 'revision 1.1' PKG-*/1_Working/DEL-*/_CONTEXT.md` returns **0**, repo-wide, permanently | The refresh branch `D-PEC-64` §3.2 names |
| **(ii) only the 17** | 17 pointer lines | Carries a **47-file exception list forever** — every future check must special-case which files legitimately differ | **A third posture §3.2 does not contemplate** — requires explicit owner authorization |
| **(iii) defer all 64** | 0 | Single deferral, but leaves the 17 edited files pointing at the superseded basis while restating the new mapping — self-contradictory | The deferral branch §3.2 names |

**Why v1's recommendation was wrong.** §3.2 reads: the pointer may be edited
*"only if Gate 4 approves the refresh **rather than** recording an explicit
deferral with rerun obligation in the Handoff_State."* That is **binary** —
refresh or defer. Option (ii) is a third posture the packet never
contemplated, so recommending it as the low-friction default was recommending
the one option that needs an authorization the packet does not supply.

**And my `OI-B` equivalence argument fails.** I claimed the 47 residual
pointers could ride `OI-B`'s later sweep at no extra cost. But `OI-B` is
**fence-forced** — `_REFERENCES.md` is excluded by §3.3 and cannot be touched
at any option. The 47 `_CONTEXT.md` pointers would be **elective**: in-fence,
authorized, and deliberately left stale. Those are not the same posture, and
treating them as equivalent was the same authority-before-assertion failure I
recorded at Gate 3 — reasoning from a resemblance instead of from what the
packet actually says.

**Recommendation: (i), full 64-pointer refresh, P-supersede text.**

**(i)'s real cost, stated plainly:** the Gate 5 diff touches **47 files whose
mapping content is unchanged**. That is a wider diff and a longer file list in
the closure commit. It buys a post-check that collapses to a single repo-wide
grep and leaves no standing exception.

**(ii) remains available** as the alternative, but it needs the owner to
authorize a partial-refresh posture beyond §3.2's two branches. **(iii)** is
incoherent for the 17 and not recommended.

---

## 3. Bounded post-check design

### 3a. Line coordinates are **PRE-change**

All line numbers in this plan and in `Amendment_Preview.md` are against
**revision 1.1**. Gate 5 applies edits top-to-bottom and must re-anchor by
**exact old-string match**, never by line number after the first insertion.

### 3b. Complete allowed-change enumeration

**`ScopeLedger.csv`** — `ObjectiveIDs` only, exactly: `SOW-001, 003, 011, 012,
013, 014, 015, 016, 017, 021, 025, 040, 042, 052, 053, 054, 056, 088, 089,
094`.

**`Deliverables.csv`** — `SupportsObjectives` only, exactly: `DEL-00-01, 00-03,
01-01, 01-03, 01-05, 01-06, 02-01..07, 03-06, 08-01, 08-02, 10-03`. All other
cells byte-identical, **including `DEL-03-01`**.

**`SOFTWARE_DECOMP.md`** — 10 sites:

| # | Site | Pre-change lines | Authority |
|---|---|---|---|
| 1 | Front-matter revision block | 6, 7, 8, 11 | §4.3 amendment **#2** |
| 2 | §3 table header | 318 | window (§3) |
| 3 | §3 rows `OBJ-001/002/004/005`, cols 4–5 | 320, 321, 323, 324 | window (§3) |
| 4 | §3 post-table note | 327–330 | window (§3) |
| 5 | §3 mapping-notes block | 332–338 | window (mapping-notes) |
| 6 | §5 envelope-posture line | 376 | §4.3 amendment **#1** |
| 7 | §7 metric row | 528 | window (§7) |
| 8 | §7 revision row | 532 | window (§7) |
| 9 | §11 DL-17 appended | after 625 | §4.3 amendment **#2** |
| 10 | §12 revision row 1.2 appended | after 640 | window (revision-history) |

Explicitly unchanged: §3 rows `OBJ-003` (322) and `OBJ-006` (325); §7
`ContextEnvelopeCounts` (529); front-matter `status` (5) and `source_corpus`
(12); §5 lines 377–379.

**`_Decomposition/_LATEST.md`** — full replacement (§3.2 target; outside the
byte-window by construction). **`_CONTEXT.md`** — line class (i) on 17, line
class (ii) per the §2 ruling. No other line in any of the 64.

**Byte-identical**: 11 residue IN rows (`SOW-022, 023, 033, 034, 035, 036,
037, 038, 044, 063, 087`); 9 residue deliverables (`DEL-00-02, 03-05, 05-01,
07-02, 07-03, 07-04, 07-05, 08-05, 10-08`); all 14 `OUT` + 9 `TBD`;
`ContextBudgetQA.csv`; `Companion_Inventory.csv`; the 320 deliverable-local
files in §1b; `docs/PRD.md`.

### 3c. Post-change anchor map (net insertions)

Four sites insert net lines, shifting everything below:

| Site | Net Δ | Cumulative Δ above | Post-change anchor |
|---|---|---|---|
| §3 post-table note (327–330 → 6 lines) | **+2** | — | 327–332 |
| §3 mapping-notes (332–338 → 14 lines) | **+7** | +2 | 334–347 |
| §5 line 376 | 0 | +9 | **385** |
| §7 metric 528 | 0 | +9 | **537** |
| §7 revision 532 | 0 | +9 | **541** |
| §11 DL-16 625 (DL-17 inserted after) | +1 | +9 | **634** |
| §12 revision row 640 (1.2 inserted after) | +1 | +10 | **650** |

In `_CONTEXT.md` under **P-supersede**, lines 30–31 → 3 lines (**+1**),
shifting lines 32+ in every touched file. Under **P-swap**, Δ = 0.

### 3d. Post-check assertions

1. Union invariant — 0 violations across all 64.
2. Residue — 11 IN rows + 9 deliverables byte-identical and still unmapped.
3. Token grammar — every changed cell `^OBJ-[0-9]{3}$` after `;`-split.
4. Topology — 94 (71/14/9), 64, 11, 6; envelopes S 28 / M 34 / L 2 / XL 0.
5. Window — exactly 20 + 17 rows, two columns; `DEL-03-01` unchanged;
   `SOW-021` ⊆ `{OBJ-005}`.
6. `git status --porcelain` lists only §3.1/§3.2 paths.
7. **Parity assertion (new):** front-matter `revision: "1.2"` ==
   `_Decomposition/_LATEST.md` "revision 1.2" == §7 Revision row "1.2" ==
   `_ScopeChange/` handoff `AcceptedBasis`. All four agree, or halt.
8. Collateral — `analyze_dep_closure.py` unchanged from D-PEC-62 values (64
   files, 255 rows, 135/120, 62 nodes/120 edges, orphans 2, SCCs 0); census
   `64 OPEN` via the `grep` form, **never** `count_workspace_state.sh`.
9. Under option (i): **[CORRECTED 2026-07-25]** the satisfiable criterion is
   `grep -rl 'revision 1.1 (\`current_basis\`' PKG-*/1_Working/DEL-*/_CONTEXT.md`
   returns **0**.

   > **Correction note.** As originally written, assertion 9 grepped for the
   > bare string `revision 1.1`. Under the ruled **P-supersede** variant that
   > string is *retained by design* — the new text reads "revision 1.1 (SCA-001
   > successor), superseded by revision 1.2 (`current_basis`, SCA-002
   > successor)" — so the literal grep returns **64**, not 0, and always would
   > have. The check that actually discriminates is the **qualified** one
   > above: no file may still assert revision 1.1 as `current_basis`. Gate 5
   > recorded assertion 9 as PASS against the qualified form; this note makes
   > that substitution explicit rather than leaving a silently changed
   > criterion in the record.
   >
   > **Consequence for the §2c option rationale.** "(i) collapses the
   > post-check to one repo-wide grep" holds only in its qualified form. The
   > check is still a single assertion and still leaves no 47-file exception
   > list, so the (i)-over-(ii) recommendation stands — but it is a *qualified*
   > grep, not the bare one the rationale implied.

---

## 4. Downstream rerun / deferral table

| Item | Owner | State | Action |
|---|---|---|---|
| Post-change `AUDIT_DECOMP` | SCOPE_CHANGE (inline) | executed Gate 5 | Step 12 |
| `SCOPE_CHANGE_POSTCHECK` | SCOPE_CHANGE | executed Gate 5 | §3d assertions |
| **`OI-B`** — 64 `_REFERENCES.md` | resumed `PROJECT_SETUP` | **`DEFERRED_BY_HUMAN`** | Fence-forced (§3.3); Gate 2 ruling |
| Residual `_CONTEXT.md` pointers | resumed `PROJECT_SETUP` | per §2 ruling — **none under (i)** | — |
| **D-PEC-63 draft** | `PROJECT_SETUP` | **`BLOCKED` → ready-for-re-pin** | **The plan's central effect.** All 32 wave members gain non-empty `SupportsObjectives`; wave-unmapped 17 → 0 |
| D-PEC-63 re-pins (3 points + 1 annotation) | resumed `PROJECT_SETUP` | `SCHEDULED` | md5s + rev-1.2 SHA; `{REV_1_2_COMMIT}`; bare-token confirmation; DAG-exhibit §1-pins annotation |
| `_COORDINATION.md` | resumed `PROJECT_SETUP` | `STALE_ON_ACCEPTANCE` | §3.1 refresh (lines 16, 50) |
| `_DECISIONS/_REGISTER.md` row | resumed `PROJECT_SETUP` | `SCHEDULED` | §3.1 — one row |
| `D-PEC-64` packet status | resumed `PROJECT_SETUP` | `SCHEDULED` | §3.1 — status update on closure |
| Wave-plan position/log | resumed `PROJECT_SETUP` | `SCHEDULED` | §3.1 |
| `projects/pec/AGENTS.md` | resumed `PROJECT_SETUP` | `CURRENT` (no revision pin) | Chosen governance act, not staleness repair |
| `LOOP_RECEIPTS.md` receipt | resumed `PROJECT_SETUP` | `SCHEDULED` | §2.4 step (a) |
| Closure commit | resumed `PROJECT_SETUP` | `SCHEDULED` | §3.6(b), from the handoff file list |
| **`OI-A`** binding-table drift | `HELPS_HUMANS` | `OPEN` | Outside the project fence |
| **`OI-013`** no register validator | downstream pipeline | `OPEN` | Gate 5's checks are session-local, not a build gate |
| `dependency-extract` | — | `NOT_REQUIRED` | No topology change; no objective column |
| Estimates / schedules | — | `NOT_APPLICABLE` | No such surface |

---

## 5. `Post_Change_Coverage.json` schema

**Not** a raw `coverage_summary.json` copy. It must match
`Pre_Change_Coverage.json`'s `pec-software-register-baseline-v1` schema so the
pre/post comparison is like-for-like: `schema_version`, `baseline_role`,
`captured_at`, `amendment_id`, `decomp_variant`, `accepted_basis`,
`audit_decomp` (citation sub-object: snapshot path, run status, declared vs
discovered counts, interpretation), `counts` (scope_items, scope_status,
packages, deliverables, objectives, context_envelopes), `objective_support`,
`checks`, `issues`, `file_sha256`, `overall_status`, `known_warnings`.

**The §3d assertion results — the six post-checks plus the parity assertion,
dep-closure and census — land inside this artifact's `checks` object**, not
only in prose.

---

## 6. `Handoff_State.md` contract scope

Four named sections per `AGENT_SCOPE_CHANGE.md` Gate 5 step 7: **accepted
amendment snapshot path**; **authoritative truth changed in this run**;
**active derivative-surface state table** (surface, classification, status,
evidence); **active snapshot state** (snapshot, artifact completeness,
`_LATEST.md` parity). Plus closure verdict, deferrals with rerun obligations,
remaining blockers, next owning workflows.

The **seven state fields** (`DecompositionTruthState`,
`DerivativePackageState`, `ContentRemediationState`, `DownstreamRerunState`,
`MetadataAlignmentState`, `AuditState`, `ReadyForNextPhase`) go in
**`RUN_SUMMARY.md`**.

---

## 7. Gate 5 execution sequence

Abort-on-failure. **Re-anchor every edit by exact old-string match**, not by
line number (§3a).

| # | Step | Verification |
|---|---|---|
| 1 | Re-verify the three basis md5s | All match, else halt (basis drifted) |
| 2 | Apply **A001** — 20 cells | 20 rows; two-column containment; token grammar |
| 3 | Apply **A002** — 17 cells | 17 rows; `DEL-03-01` untouched; union invariant 0 |
| 4 | Apply the **10 `SOFTWARE_DECOMP.md` sites** | Each old string matched exactly once; §3 objective-side view agrees with the registers for all six objectives (range-expanded); no site outside §3b differs |
| 5 | Apply **A006** — `_LATEST.md` full replacement, slots filled from measurement | No literal `{` remains |
| 6 | Apply `_CONTEXT.md` class (i) — the 17 exact pairs (§2a) | Per-file exact match; only line 12 differs |
| 7 | Apply `_CONTEXT.md` class (ii) per the §2 ruling | Per-file exact match; line 29 untouched; under (i) the §3d.9 grep returns 0 |
| 8 | Run §3d assertions 1–5 and 7 (parity) and 8 (collateral) | All pass |
| 9 | Write `Pre_Change_Coverage.json` (baseline schema) | Present; schema matches SCA-001's |
| 10 | Generate `Supersession_Map.csv` | `accumulate_supersession_map.py --prior-map projects/pec/execution/_ScopeChange/SCA-001_2026-07-24_2206/Supersession_Map.csv --output-map projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Supersession_Map.csv --output-findings projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Supersession_Findings.csv --allow-empty` — no `--delta`; header-only carried forward |
| 11 | Draft `Handoff_State.md` + `RUN_SUMMARY.md`; **repoint `_ScopeChange/_LATEST.md` to SCA-002** | Snapshot artifact set complete; exactly one active snapshot named |
| 12 | Run post-change `AUDIT_DECOMP` **inline** — `EXPECTED_SOURCE_SNAPSHOT` = `_Decomposition/_LATEST.md` (revision 1.2, `current_basis`), `EXPECTED_HANDOFF_PHASE` = `SCOPE_CHANGE_GATE_5`, `SCOPE` = `ALL` | Runs **after** step 11 so its Check 10 validates **SCA-002's** active snapshot, not SCA-001's; pointer updated |
| 13 | Write `Post_Change_Coverage.json` (§5 schema, carrying the §3d results) | Schema matches the pre-change baseline |
| 14 | Finalise `RUN_SUMMARY.md` + `Handoff_State.md` evidence fields **citing the step-12 audit output** | Seven state fields in `RUN_SUMMARY`; four sections in `Handoff_State`; no claim exceeds the evidence |
| 15 | Record the Gate 4 ruling, the Gate 5 execution/validation record, and the final owner confirmation in **`Decision_Log.md`** | Present; all five gates recorded |
| 16 | `git status --porcelain` scope check | Only §3.1/§3.2 paths |
| 17 | Return the handoff — exact file list + recommended commit message | **No commit performed** |

Step ordering note: **A006 (step 5) and the `_ScopeChange/_LATEST.md` repoint
(step 11) both precede the audit (step 12)** so the audit evaluates the
post-amendment basis pointer and the SCA-002 snapshot. v1 ran the audit before
both and would have validated SCA-001's snapshot while claiming to validate
SCA-002's.

### Git posture

**SCOPE_CHANGE performs no git operation at any step.** `AGENT_SCOPE_CHANGE.md`
assigns staging to CHANGE; `D-PEC-64` §3.6(b) assigns the SCA-002 closure
commit to **resumed `PROJECT_SETUP`** from this session's handoff file list.

```text
scope: SCA-002 — deliverable→objective mapping for the Phase 2.2 wave scope

Variant: SOFTWARE
Actions: 10 (MODIFY:10)
Affected entities: ScopeLedger.csv (20 IN rows), Deliverables.csv (17
deliverables), SOFTWARE_DECOMP.md (front matter + §3/§5/§7/§11/§12),
_Decomposition/_LATEST.md, _CONTEXT.md propagation, SCA-002 snapshot,
AUDIT_DECOMP pre/post baselines
```

---

## 8. v2 correction log (round R-2b-g4)

22 findings, all `ACCEPTED`.

| Group | Corrections |
|---|---|
| **Executability (critical)** | **C-34** `Decision_Log.md` added to the manifest (§1c) and sequence (step 15) — SCA-001 names it a Gate 5 `DIRECT_EDIT`; v1 omitted it entirely. **C-35** the 17 `_CONTEXT.md` mapping edits now carry **exact old→new text per file** (§2a) — v1 gave a rule, which would have required Gate 5 to invent text |
| **Sequencing / evidence** | **C-36** audit re-sequenced **after** A006 and after the `_ScopeChange/_LATEST.md` repoint, with explicit params, so Check 10 validates SCA-002's snapshot. **C-37** parity assertion added (§3d.7). **C-38** `Post_Change_Coverage.json` restored to the `pec-software-register-baseline-v1` schema with the §3d results inside (§5). **C-39** line coordinates declared PRE-change with a post-change anchor map (§3c) |
| **Option analysis — recommendation flipped** | **C-40** §2c rewritten: my cost claim was **inverted**. Under (i) the post-check collapses to one repo-wide grep; (ii) carries a 47-file exception forever. **C-41** §3.2's "refresh **rather than** deferral" is **binary** — (ii) is a third posture needing explicit authorization. **C-42** the `OI-B` equivalence **fails**: `OI-B` is fence-forced, the 47 would be elective — the Gate 3 authority-before-assertion failure class again. **C-43** P-swap's "false claim" charge softened to contestable (m22). **Recommendation now (i) + P-supersede** |
| **Manifest / tables** | **C-44** 256 deliverable-local `NO_CHANGE` files (4 × 64) + 64 `_SEMANTIC.md` classified = 320. **C-45** "9 edit sites" → **10**. **C-46** Gate 4 item-6 classifications restored; `_REFERENCES.md` = `DEFERRED_BY_HUMAN`, not `NO_CHANGE`-only. **C-47** §4 additions: `_REGISTER.md` row, D-PEC-64 packet status, wave-plan updates, `OI-A`, `OI-013`, and the plan's central effect (D-PEC-63 `BLOCKED` → ready-for-re-pin). **C-48** `Handoff_State` full contract scope (§6); seven state fields to `RUN_SUMMARY` |
| **Mechanical** | **C-49** step-10 command fixed — `--output-map` (required) + `--output-findings`. **C-50** "finalize `Amendment_Actions.csv`" step dropped; snapshot-immutability posture adopted (§1c). **C-51** `Amendment_Actions.csv` **extended by appending** propagation rows; Gate-3-approved rows untouched. **C-52** `DownstreamReruns` normalised; owner named **`PROJECT_SETUP`** per §3.6(b), not `CHANGE`. **C-53** `Decision_Log.md` stale rows fixed |

### The pattern, fourth occurrence

Gates 2 and 3 were overstatement. This one is different in kind and worth
naming separately: **v1 was not executable.** A Gate 5 agent following it
would have had to invent the `_CONTEXT.md` text and would have skipped
`Decision_Log.md` entirely. A plan whose job is to make the next step
mechanical must be checked by asking "could someone run this without asking me
a question?" — and I did not ask that.

The option analysis failed the *same* way as Gate 3's A008 claim: I reasoned
from a resemblance (`OI-B` looks like the 47) instead of from what §3.2
actually says. Twice now the fix has been to read the governing text before
asserting what it permits.

---

## 9. Gate 4 approval question

**Q1 — `_CONTEXT.md` basis-pointer scope.** **(i) refresh all 64**
*(recommended)*, **(ii)** refresh only the 17 and defer 47 — *requires
authorizing a partial-refresh posture beyond §3.2's two branches — or
**(iii)** defer all 64 *(not recommended; incoherent for the 17)*. Text
variant: **P-supersede** *(recommended)* or **P-swap**.

The 17 `SupportsObjectives` restatements refresh under every option — the
propagation default, confirmed, not in question.

**Q2 — Do you approve this propagation plan and release Gate 5?**
