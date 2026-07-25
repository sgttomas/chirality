---
amendment_id: SCA-002
doc_kind: scope_change.brief
decomp_variant: SOFTWARE
gate: 2
created: 2026-07-25
updated: 2026-07-25
status: gate_1_ruled_awaiting_gate_2
scope_width: O-A
authority: D-PEC-64
---

# SCA-002 — Deliverable→Objective Mapping Amendment

## Human initiation

SCOPE_CHANGE is human-initiated only. The owner direction of record is
`D-PEC-64`, RULED 2026-07-25, which records the owner (Ryan Tufts) selecting
verbatim:

> "RULED as drafted (Recommended)"

carrying the ruling text: "D-PEC-64 is RULED as drafted: I adopt the intake §1
change request as my own; SCA-002 may open at Gate 1 under the stated fence,
entry mechanics, and git-acts clause; Gates 1–5 remain distinct in-session
owner acts; scope width is ruled at Gate 1 from the intake §7 options."

The adopted change request is `_Coordination/SCA-002_INTAKE_2026-07-25.md` §1:

> Complete the deliverable→objective mapping in decomposition truth so that
> every Phase 2.2 wave deliverable carries a non-empty objective reference set,
> superseding revision 1.1's recorded best-effort mapping posture to the extent
> the owner approves at Gate 3.

On the advisory scope-width question the owner selected **"Decide at Gate 1"** —
no pre-indication. The intake §7 options are presented fresh below.

## Normalized session parameters

| Parameter | Value |
|---|---|
| `DECOMP_VARIANT` | `SOFTWARE` |
| `CONTEXT_ROOT` | `projects/pec/execution/` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `SCOPE_CHANGE_ROOT` | `projects/pec/execution/_ScopeChange/` |
| `AMENDMENT_ID` | `SCA-002` |
| `ALLOW_RENUMBERING` | `false` |
| `ALLOWED_PROPAGATION_WRITES` | Narrowed from the `SOFTWARE` default: `_CONTEXT.md` **in**, `_STATUS.md` **out** (`D-PEC-64` §3.2 — a mapping amendment changes no lifecycle state) |
| Owner packet | `D-PEC-64` |
| Requested successor | revision **1.2** as `current_basis` on Gate 5 acceptance |
| Current gate | Gate 1 — change intake and validation |
| Executing role | SCOPE_CHANGE (Agent 1), dispatched by Agent 0 under `D-PEC-64` owner amendment §2.4 |

`AMENDMENT_ID` assignment: `_ScopeChange/` contained exactly one prior
snapshot (`SCA-001_2026-07-24_2206`) at session open, making `SCA-002` the next
available ID — consistent with the ID `D-PEC-64` names.

## Accepted basis resolved and verified

`_Decomposition/_LATEST.md` names `SOFTWARE_DECOMP.md` revision **1.1** as
`current_basis` (SCA-001 successor, accepted 2026-07-24 under `D-PEC-61`).
Document front matter agrees (`revision: "1.1"`, `status: current_basis`).

Basis pins re-measured at session open with `md5 -q`:

| File | Measured | `D-PEC-64` / intake §2 pin | Result |
|---|---|---|---|
| `SOFTWARE_DECOMP.md` | `ad944a2bfa7784778afa8558d8f81762` | same | `MATCH` |
| `Deliverables.csv` | `6d2b290b0c869fc1d51d626a1714abec` | same | `MATCH` |
| `ScopeLedger.csv` | `49e0cff9af647e41966b7a3334641919` | same | `MATCH` |

Accepted topology confirmed against the registers: **94 scope items
(71 IN / 14 OUT / 9 TBD), 11 packages, 64 deliverables, 6 objectives**,
Context Envelope **S 28 / M 34 / L 2 / XL 0**.

## Semantic section binding (resolved by heading text)

`AGENT_SCOPE_CHANGE.md`'s `SOFTWARE_DECOMP` binding table carries hard-coded
section numbers that do not match this document. The protocol directs binding
by heading text when section numbers are absent; that is what was done.

| Semantic section | Binding table | This document | Bound to |
|---|---|---|---|
| Change Register | `Change Log` §8 | §8 is *Context Budget QA*; no "Change Log" heading | **§11 Decision Log** + **§12 Revision History** |
| Unit Ledger | `Scope Ledger` §5 | §5 is *Deliverables* | **§6 Scope Ledger** + `ScopeLedger.csv` (authoritative) |
| Objectives | via Scope Ledger §5 | both views exist | **§3 Objectives** (objective-side) + `ScopeLedger.csv` `ObjectiveIDs` (item-side, authoritative) |
| Primary Partitions | `Packages` §3 | §3 is *Objectives* | **§4 Packages** |
| Secondary Entities | `Deliverables` §4 | §4 is *Packages* | **§5 Deliverables** + `Deliverables.csv` (authoritative) |
| Coverage Basis | `AUDIT_DECOMP` output | — | **§7 Coverage & Telemetry** + this session's baseline |

## Parsed atomic actions (Gate-1-ruled, O-A)

The owner ruled **O-A wave-minimum** and confirmed A001–A006, adding **A007**.
Row-set widths below are now concrete, not conditional. Exact per-row text
remains Gate 3 work.

| Ref | ActionType | EntityType | EntityID | Requested change | Affected semantic sections |
|---|---|---|---|---|---|
| A001 | `MODIFY` | `OBJECTIVE` | `ScopeLedger.csv` `ObjectiveIDs` — **20 IN rows** (`SOW-001, 003, 011..017, 021, 025, 040, 042, 052, 053, 054, 056, 088, 089, 094`) | Populate `ObjectiveIDs` with bare `;`-separated `OBJ-NNN` tokens, derived by the intake §4 attribution method. **Binding constraint: `SOW-021` ⊆ `{OBJ-005}`** (see F-2) | Unit Ledger (§6 + `ScopeLedger.csv`) |
| A002 | `MODIFY` | `DELIVERABLE` | `Deliverables.csv` `SupportsObjectives` — **17 deliverable rows** (`DEL-00-01, 00-03, 01-01, 01-03, 01-05, 01-06, 02-01..07, 03-06, 08-01, 08-02, 10-03`) | Populate `SupportsObjectives` so the §3 union invariant holds file-wide | Secondary Entities (§5 + `Deliverables.csv`) |
| A003 | `MODIFY` | `OTHER` | §3 Objectives — `Mapped Scope Items` / `MappedDeliverables` columns and mapping notes | Reconcile the objective-side view to the amended ledger/register truth; amend or explicitly retain the "intentionally not force-mapped" and best-effort clauses per the Gate 1 scope ruling | Objectives (§3) |
| A004 | `MODIFY` | `OTHER` | §7 Coverage & Telemetry — `IN items without objective mapping` metric row; `Revision` row | Update the metric from 31 to the post-amendment residue; restate the posture; set revision 1.2 | Coverage Basis (§7) |
| A005 | `MODIFY` | `OTHER` | Change Register — §11 Decision Log + §12 Revision History | Add the SCA-002 decision-log entry and the revision-1.2 history row; requested by owner Ryan Tufts under `D-PEC-64` | Change Register (§11, §12) |
| A006 | `MODIFY` | `OTHER` | `_Decomposition/_LATEST.md` | Repoint to revision 1.2 with the SCA-002 handoff state on Gate 5 acceptance | Handoff pointer |
| **A007** | `MODIFY` | `OTHER` | §5 Deliverables — envelope-posture prose line (line 376) | Correct `29 S / 33 M / 2 L / 0 XL` → `28 S / 34 M / 2 L / 0 XL`, reconciling the residual SCA-001 miss (finding `W-1`) to `Deliverables.csv` and §7. **Exactly one line; no other §5 content changes.** | Secondary Entities (§5 prose) |

**A007 provenance.** Added by owner ruling at Gate 1 ("Fix now: add A007")
after this session's Gate 1 validation surfaced `W-1`. The owner amended
`D-PEC-64` §4.3 the same day so the byte-identity window admits exactly that
one §5 prose line. A007 is `MODIFY`-legal on its own terms — it edits an
attribute of an existing section — and was previously out of scope by the
**§4.3 window and the intake's subject scope**, not by change class.

No action adds, removes, reclassifies, merges, splits, or renumbers a package,
deliverable, objective, scope item, product function, dependency edge, or
stable ID. `ALLOW_RENUMBERING=false` holds; I5 append-only is preserved. The
**parent-closure rule is not triggered**. `ContextBudgetQA.csv` and
`Companion_Inventory.csv` are expected **unchanged** (no envelope or package-
role change is in scope).

Whether a `Supersession_Delta.csv` binding is owed for the superseded
best-effort posture is a Gate 2/3 ruling (intake §5.5), not settled here.

## Gate 1 validation

| Action | Validation result | Evidence (independently measured, not taken from the intake) |
|---|---|---|
| A001 | `PASS` | 31 `IN` rows have empty `ObjectiveIDs`; all exist, all are `InOutStatus=IN`, all carry a resolving `PackageID` and `DeliverableIDs`. `ObjectiveIDs` is a valid existing ledger column. All 6 objective tokens `OBJ-001`..`OBJ-006` exist. |
| A002 | `PASS` | 26 of 64 deliverables have empty `SupportsObjectives`; all exist in `Deliverables.csv` and §5 with resolving `PackageID`. `SupportsObjectives` is a valid existing register column. |
| A003 | `PASS` | §3 exists with `Mapped Scope Items (best-effort)` and `MappedDeliverables` columns plus a `**Mapping notes:**` block (lines 332–338); all are amendment-capable narrative/table surfaces. |
| A004 | `PASS` | §7 exists; the `IN items without objective mapping` metric row (line 528) reads `31`, matching the measured ledger value; the `Revision` row reads `1.1, 2026-07-24 (SCA-001)`. |
| A005 | `PASS` | §11 Decision Log ends at `DL-16`; §12 Revision History ends at row `1.1`. Both are append-capable. |
| A006 | `PASS` | `_Decomposition/_LATEST.md` exists and names revision 1.1 as `current_basis`. |
| **A007** | `PASS` (re-validated post-ruling) | §5 line 376 reads verbatim "Context Envelope posture: **29 S / 33 M / 2 L / 0 XL.**". `Deliverables.csv` yields S 28 / M 34 / L 2 / XL 0; §7 `ContextEnvelopeCounts` reads "S 28 / M 34 / L 2 / XL 0". The replacement value is therefore already-accepted register truth, not a new fact. The two `L` deliverables named in the same sentence (`DEL-02-03`, `DEL-01-01`) remain correct and are untouched. |

**Change-class legality: `PASS`.** Every action is `MODIFY` over an existing
field, column, or narrative section of an existing entity. No topology
primitive changes. This is the smallest amendment that achieves the requested
endpoint, satisfying the type-level change preference; it is **not** a
contract-level change to the decomposition ontology, canonical vocabulary, or
section contract.

## Independently re-verified gap inventory

Every number below was recomputed from the pinned registers in this session.
All match the intake.

| Claim | Intake | Measured | Result |
|---|---|---|---|
| Ledger rows | 94 (71 IN / 14 OUT / 9 TBD) | 94 (71/14/9) | `MATCH` |
| Deliverables | 64 | 64 | `MATCH` |
| Unmapped `IN` rows | 31 | 31 | `MATCH` |
| The 31 row IDs | intake §3 list | identical set | `MATCH` |
| Unmapped deliverables | 26 | 26 | `MATCH` |
| Unmapped in-wave | 17 | 17 | `MATCH` |
| Unmapped out-of-wave | 9 | 9 | `MATCH` |
| Pilot roots unmapped | 7 of 9 | 7 | `MATCH` |
| Union-invariant violations | 0 | 0 | `MATCH` |
| Context Envelope | S 28 / M 34 / L 2 | S 28 / M 34 / L 2 | `MATCH` |
| Objective tokens | 6 | `OBJ-001`..`OBJ-006` | `MATCH` |

Wave partition verified against the frozen 32-member B1–B8 table in
`_Coordination/PLAN_2026-07-25_pec_phase_2_2_sow_wave.md` (9+3+6+1+6+4+2+1 = 32,
32 unique).

Derived option widths:

| Option | `IN` rows | Deliverable rows | Residue `IN` / deliverables |
|---|---|---|---|
| **O-A** wave-minimum | **20** | **17** | 11 / 9 |
| **O-C** wave + easy residue | **24** | **20** | 7 / 6 |
| **O-B** full closure | **31** | **26** | 0 / 0 |

The 19 rows covering the 17 in-wave unmapped deliverables plus `SOW-021` give
O-A's 20. The 11 residue rows under O-A are exactly
`SOW-022, 023, 033, 034, 035, 036, 037, 038, 044, 063, 087`.

## Ledger-side exceptions verified

Two unmapped `IN` rows land on deliverables that are **already** mapped — the
only two such cases in the file:

- **`SOW-021`** (`PEC-RCN-006` → `DEL-03-01`, wave batch B4). `DEL-03-01`
  carries `OBJ-005` via `SOW-010` (`PEC-RCN-001`, `OBJ-005`). In-wave;
  included in O-A.
- **`SOW-033`** (`PEC-STR-001` → `DEL-07-01`). `DEL-07-01` carries `OBJ-003`
  via `SOW-039`. Out-of-wave; member of the §5.4 intentional class.

**Consequence for the bounded-comparison window (new Gate 1 fact).** Because
the union invariant makes a deliverable's `SupportsObjectives` the union over
its covered `IN` rows, the deliverable-row change count is **conditional on
which token is assigned**:

- Under O-A, `D-PEC-64` §4.3's window of "17 deliverable rows" holds **only if
  `SOW-021` is mapped to a subset of `{OBJ-005}`** — i.e. the intake's evident
  candidate. Any other assignment forces `DEL-03-01` to change too, making the
  window 18 rows and putting the amendment outside the pinned window.
- The same holds for `SOW-033`/`DEL-07-01` under O-B/O-C variants that map it.

This is a Gate 3 drafting constraint, surfaced now so the window is not
breached by a defensible-looking attribution.

## Recorded rationale that each option supersedes

Verified verbatim in the document:

- **§3 mapping notes (lines 332–338):** "Ingest/bridge items (SOW-033..039)
  serve OBJ-001/OBJ-003 freshness indirectly through PEC-K-07 and are
  intentionally not force-mapped; parser items (SOW-011..017) underlie
  OBJ-001/OBJ-002 through the record tier (SOW-001)."
  Of the `SOW-033..039` range, `SOW-039` is already mapped to `OBJ-003`;
  `SOW-033..038` are the unmapped members. Confirmed.
- **`DL-14` (line 623) and §3 note (lines 327–330):** "SOW-063 left unmapped
  intentionally (instruments PEC-K-07, which no §3 objective states)."
  Confirmed.

The parser clause (`SOW-011..017`) is a **positive derivation**, not an
abstention — mapping those rows to `OBJ-001`/`OBJ-002` *applies* the recorded
rationale rather than superseding it. The ingest/bridge and `SOW-063` clauses
are **abstentions**; mapping those rows supersedes recorded design rationale
and requires an explicit owner act at Gate 3.

| Option | Supersedes | Applies |
|---|---|---|
| O-A | §7 best-effort metric posture only | §3 parser derivation (`SOW-011..017`) |
| O-C | §7 posture; the §3 best-effort framing for 3 non-intentional stragglers | same; intentional class retained verbatim |
| O-B | §7 posture; §3 ingest/bridge "intentionally not force-mapped" clause; `DL-14` `SOW-063` rationale | same |

## Pre-change evidence

### `AUDIT_DECOMP` baseline

`execution/_Evaluation/DecompCoverage/COV_SCA002_PRECHANGE_2026-07-25_1040/`
· `coverage_summary.json` · `RUN_STATUS = WARNINGS` · 0 blockers / 1 warning /
90 info.

First PEC run able to measure filesystem coverage (SCA-001's baselines returned
the contract-required `FAILED_INPUTS` pre-scaffold; `D-PEC-62` has since landed
11 package and 64 deliverable folders). Forward coverage 11/11 and 64/64,
reverse 100%, context fidelity 100%, objective coverage 100%, lifecycle 64
`OPEN`, active-snapshot check `PASS`, objective-evidence integrity `PASS`.

Executed **inline** by this SCOPE_CHANGE instance — Agent 2 dispatch is
unavailable in this harness (launch-brief substitution, root `AGENTS.md`
single-agent fallback). Read-only discipline preserved.

### Corroborating deterministic check

`python3 tools/coordination/analyze_dep_closure.py projects/pec/execution`
returns 64 files, 255 rows, 135 `ANCHOR` / 120 `EXECUTION`, 62 nodes / 120
edges, orphans 2, SCCs 0 — matching the `D-PEC-62` landing values pinned in
`D-PEC-64` §4.4 exactly.

## Warnings and unknowns

1. **`W-1` — stale duplicated count in accepted revision 1.1.** `RESOLVED AT
   GATE 1` — the owner ruled "Fix now: add A007". §5 line 376 states
   "Context Envelope posture: **29 S / 33 M / 2 L / 0 XL**", while
   `Deliverables.csv` and §7 both yield **28 S / 34 M / 2 L / 0 XL**. SCA-001
   re-enveloped `DEL-10-10` `S`→`M` and reconciled the registers,
   `ContextBudgetQA.csv`, and §7, but not the §5 prose.
   **Characterization corrected (R-2b-g1):** the Gate 1 return described W-1 as
   "outside SCA-002's declared change class". That was wrong. A007 is
   `MODIFY` — an attribute edit on an existing section — and `MODIFY` is
   exactly the declared class. What excluded it was the `D-PEC-64` §4.3
   byte-identity **window** and the intake's **subject scope**
   (deliverable→objective mapping), both of which the owner amended/extended
   at Gate 1. Change class was never the barrier.
2. **Downstream-parser-shapes-truth flag (intake §5.1) stands.** Bare
   `OBJ-NNN` tokens are required in the registers because brief construction
   splits the cell on `;`. Verified: `common.py:213-215` enforces only
   non-emptiness of `package_objective_refs`; `:251-253` unions
   `project_scope_refs | package_objective_refs`; `:266-267` splits matrix
   cells on comma/whitespace. The constraint coincides with the register-native
   convention already in use, so no representation change is forced — but a
   downstream consumer is shaping the representation of authoritative truth.
3. **Attribution candidates are deliberately undecided.** The intake does not
   pre-decide the 9 `NEEDS ATTRIBUTION` mappings. Candidate development with
   per-row warrant quotes is Gate 2/3 work under the intake §4 method
   (ledger `SourceRef` → PRD function row → §3 objective).
4. **`OI-013` remains open.** No durable repo-native register validator exists;
   §7's structural assertions came from a session-local generator not part of
   the package. `W-1` is exactly the defect class `OI-013` predicts. Gate 5
   must rerun equivalent deterministic checks.
5. **Binding-table drift.** The `SOFTWARE_DECOMP` section numbers hard-coded in
   `AGENT_SCOPE_CHANGE.md` and `AGENT_AUDIT_DECOMP.md` do not match the live
   document. Resolved here by heading-text binding; flagged as a trap for
   future agents. Agent-file scope, not project scope.
6. **Exact amendment prose is deferred to Gate 3**, per `D-PEC-64` §2.5.
7. **`_ScopeChange/_LATEST.md` still names SCA-001.** Correct by design —
   `D-PEC-64` §2.4 updates it only at Gate 5.

## Gate boundary

Gate 1 modified **no** decomposition document, companion register,
decomposition pointer, `_CONTEXT.md`, `_STATUS.md`, `Dependencies.csv`,
coordination surface, decision packet, PRD, estimate, schedule, or
frozen-reference-corpus file. Writes are confined to this session workspace and
the in-fence `_Evaluation/DecompCoverage/` baseline plus its own pointer.

## Gate 1 ruling (owner, 2026-07-25)

**RULED.** Verbatim selections: six-action list **"Confirmed"** (A001–A006 as
parsed); scope width **"O-A wave-minimum"**; W-1 **"Fix now: add A007"**.
Binding constraint carried from this session's F-2 finding: `SOW-021`'s
`ObjectiveIDs` ⊆ `{OBJ-005}`. `D-PEC-64` §4.3's byte-identity window was
amended the same day to admit the single §5 prose line.

**Ruled scope, final:** 20 `IN` ledger rows, 17 deliverable rows, §3/§7/
revision-history/mapping-notes text, the one §5 prose line (A007), and the
in-fence `_CONTEXT.md` line classes. The 11 residue `IN` rows and 9 residue
deliverables must remain **untouched** — an unauthorized mapping of the
intentional class is a verification failure, not a bonus.

Gate 1 is closed. Gate 2 (Impact Assessment) is released; see
`Impact_Assessment.md`.
