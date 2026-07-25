---
amendment_id: SCA-002
doc_kind: scope_change.decision_log
decomp_variant: SOFTWARE
created: 2026-07-25
authority: D-PEC-64
---

# SCA-002 — Decision Log

Records every human decision and every agent-side resolution at each gate.
Owner decisions are made in chat; this file records them, it does not make
them.

---

## Gate 1 — Change Intake and Validation

**Opened:** 2026-07-25 10:42
**Executing role:** SCOPE_CHANGE (Agent 1), dispatched by Agent 0 under the
`D-PEC-64` owner amendment §2.4 with a frozen launch brief at
`_Coordination/AgentRuns/RUN_2026-07-25_sca002/instances/SCOPECHANGE-SCA002/LAUNCH_BRIEF.md`.
**Owner ruling status:** `PENDING` — the Gate 1 decision package is presented;
no gate is ruled by this agent.

### What was validated

| # | Item | Result |
|---|---|---|
| 1 | Basis md5 pins (3 files) vs `D-PEC-64` / intake §2 | `MATCH` ×3 |
| 2 | `_Decomposition/_LATEST.md` revision parity vs front matter | `MATCH` (revision 1.1, `current_basis`) |
| 3 | Accepted topology (94 / 71-14-9 / 11 / 64 / 6; S 28 M 34 L 2 XL 0) | `MATCH` |
| 4 | Semantic section binding by heading text | resolved — see D-1 |
| 5 | Intake completeness (session params, gap inventory, warrant evidence, constraints, endpoint, options, repro commands) | `COMPLETE` |
| 6 | Intake coherence with parsed state | `COHERENT` — all 11 measured claims match |
| 7 | Change-class legality (`MODIFY`-only, no topology) | `PASS` |
| 8 | Parent-closure rule | not triggered (no `REMOVE`/`RECLASSIFY`/`MERGE`/`SPLIT`) |
| 9 | Stable-ID preservation / `ALLOW_RENUMBERING=false` / I5 append-only | preserved |
| 10 | Pre-change `AUDIT_DECOMP` baseline | `WARNINGS` — 0 blockers |

### Independent re-verification of the intake's central numbers

Recomputed from the pinned registers in this session; the intake's assertions
were **not** trusted.

| Claim | Intake | Measured | Result |
|---|---|---|---|
| Unmapped `IN` rows | 31 | 31 (identical ID set) | `MATCH` |
| Unmapped deliverables | 26 | 26 (identical ID set) | `MATCH` |
| In-wave unmapped | 17 | 17 | `MATCH` |
| Out-of-wave unmapped | 9 | 9 | `MATCH` |
| Pilot roots unmapped | 7 of 9 | 7 | `MATCH` |
| `SOW-021` in-wave ledger exception | 1 | 1 (verified `DEL-03-01` ← `OBJ-005` via `SOW-010`) | `MATCH` |
| Union-invariant violations | 0 | 0 | `MATCH` |
| O-A / O-C / O-B `IN`-row widths | 20 / 24 / 31 | 20 / 24 / 31 | `MATCH` |
| Wave membership | 32 | 32 (B1–B8 sum, all unique) | `MATCH` |
| §3 mapping-notes quote and line span | 333–336 | verified verbatim within 332–338 | `MATCH` |
| `DL-14` `SOW-063` rationale | quoted | verified verbatim (line 623) | `MATCH` |
| SOW-validator mechanics | `common.py:213-215`, `:251-253`, `:266-267` | all three verified | `MATCH` |

**Verdict: no discrepancy found in the intake.** Every load-bearing number,
quote, and line citation reproduces.

### Agent-side resolutions

| Ref | Decision | Rationale |
|---|---|---|
| D-1 | Semantic sections bound by **heading text**, not by the binding table's section numbers | `AGENT_SCOPE_CHANGE.md`'s `SOFTWARE_DECOMP` column names `Change Log` §8, `Scope Ledger` §5, `Packages` §3, `Deliverables` §4. The live document has §3 Objectives, §4 Packages, §5 Deliverables, §6 Scope Ledger, §8 Context Budget QA, and **no** "Change Log" heading. The protocol directs "Bind by heading text when section numbers are absent". Resolution table is in `Brief.md`. Flagged as agent-file drift (open item OI-A). |
| D-2 | `AUDIT_DECOMP` executed **inline** rather than dispatched | Agent 2 dispatch is unavailable in this harness. Launch brief: "run the deterministic audit tooling inline and record that substitution". Root `AGENTS.md` single-agent fallback. Read-only invariants preserved; writes confined to the COV snapshot + its pointer. |
| D-3 | Coverage baseline scoped `ALL`, not to affected packages/deliverables | The affected set is undetermined until the owner rules scope width. `ALL` is the strict superset of O-A/O-C/O-B and the only scoping that keeps the Gate 5 post-change baseline comparable under any ruling. |
| D-4 | Actions parsed as **six** `MODIFY` actions with conditional row-set width | The change request is one class over a row set the owner sizes at Gate 1. Stating A001/A002 conditionally avoids pre-empting the ruling while keeping the action register complete. Exact per-row text is Gate 3 work. |
| D-5 | Finding `W-1` recorded and escalated, **not** corrected | Gate 1 holds no write authority over decomposition truth (`D-PEC-64` §2.5, §5). `W-1` is also outside SCA-002's declared `MODIFY` mapping change class, so bringing it in scope requires an explicit owner act. |
| D-6 | `Supersession_Delta.csv` disposition **not** settled at Gate 1 | Intake §5.5 assigns it to Gate 2/3. Recording it here would pre-empt a later gate. |
| D-7 | Three spurious Check-7 `BLOCKER`s discarded after root-cause | §3's `MappedDeliverables` uses range notation (`DEL-04-01..05`, `DEL-06-01..06`, `DEL-09-01..07`). Literal ID scanning undercounts. After range expansion, §3 and `Deliverables.csv` agree exactly for all six objectives. Recorded so the discarded findings are auditable rather than invisible. |
| D-8 | `AMENDMENT_ID = SCA-002` confirmed by directory scan **before** workspace creation | `_ScopeChange/` held only `SCA-001_2026-07-24_2206`, making `SCA-002` next-available and consistent with `D-PEC-64`. Note: `tools/query/scan_next_amendment_id.sh` now returns `SCA-003` **because this session's workspace exists** — that is the expected post-creation reading, not a conflict. |

### New facts found at Gate 1 (not in the intake)

| Ref | Finding | Disposition |
|---|---|---|
| `W-1` | `SOFTWARE_DECOMP.md` §5 line 376 states "29 S / 33 M / 2 L / 0 XL"; `Deliverables.csv` and §7 both yield "28 S / 34 M / 2 L / 0 XL". SCA-001 re-enveloped `DEL-10-10` `S`→`M` and reconciled the registers, `ContextBudgetQA.csv`, and §7 — but not the §5 prose. A residual reconciliation miss inside accepted revision 1.1. | Escalated to the owner as a Gate 1 open item. Documentation-consistency only; no topology impact; `D-PEC-64` §4.1's invariant agrees with the registers, not §5. Outside SCA-002's change class. |
| `F-2` | The union invariant makes the **deliverable**-row change count conditional on token choice. `D-PEC-64` §4.3's O-A window of "17 deliverable rows" holds only if `SOW-021` maps to a subset of `{OBJ-005}`. Any other assignment forces `DEL-03-01` to change, widening the window to 18 and breaching the pinned bound. The symmetric case is `SOW-033`/`DEL-07-01` under O-B/O-C. | Carried to Gate 3 as a drafting constraint. Not a Gate 1 blocker. |
| `F-3` | The §3 parser clause (`SOW-011..017` "underlie OBJ-001/OBJ-002 through the record tier") is a **positive derivation**, whereas the ingest/bridge and `SOW-063` clauses are **abstentions**. Mapping the parser rows *applies* recorded rationale; mapping the ingest/bridge or `SOW-063` rows *supersedes* it. | Sharpens the O-A/O-C/O-B supersession comparison presented at Gate 1. |

### Substitutions recorded

- **`AUDIT_DECOMP` Agent 2 dispatch → inline execution** by this Agent 1
  instance (D-2). The `AGENT_AUDIT_DECOMP.md` v2.1 protocol was executed as a
  deterministic read-only script; all 12 checks ran; outputs conform to the
  contract's required artifact set.

### Open items carried out of Gate 1

| Ref | Item | Owner |
|---|---|---|
| `OI-A` | Binding-table drift: `SOFTWARE_DECOMP` section numbers hard-coded in `AGENT_SCOPE_CHANGE.md` and `AGENT_AUDIT_DECOMP.md` do not match the live document | HELPS_HUMANS (agent-file scope, outside this project fence) |
| `OI-013` | No durable repo-native register validator; `W-1` is exactly the defect class it predicts | Pre-existing; Gate 5 must rerun equivalent deterministic checks |
| `W-1` | §5 envelope-count staleness in revision 1.1 | Owner — decide whether it rides along under a Gate 3 approval that names it, or waits for a separate amendment |
| — | Scope width O-A / O-B / O-C | **Owner — this is the Gate 1 ruling** |
| — | 9 `NEEDS ATTRIBUTION` candidate mappings with per-row warrant | Gate 2/3 |
| — | `Supersession_Delta.csv` owed-or-not | Gate 2/3 |

### Gate 1 owner ruling

> _Pending. To be recorded verbatim here when the owner rules in chat._

**Required to close Gate 1:** (a) confirmation that the parsed action list is
what the owner intends, and (b) the scope-width ruling (O-A / O-B / O-C), and
(c) optionally, a disposition for `W-1`.

---

## Gate 2 — Impact Assessment

> _Not opened._

## Gate 3 — Amendment Approval

> _Not opened._

## Gate 4 — Propagation Plan Approval

> _Not opened._

## Gate 5 — Execute and Validate

> _Not opened._
