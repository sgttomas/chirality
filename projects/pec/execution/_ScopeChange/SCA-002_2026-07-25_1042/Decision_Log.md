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

**Opened:** 2026-07-25 10:42 · **Ruled:** 2026-07-25 · **Status:** `CLOSED`
**Executing role:** SCOPE_CHANGE (Agent 1), dispatched by Agent 0 under the
`D-PEC-64` owner amendment §2.4 with a frozen launch brief at
`_Coordination/AgentRuns/RUN_2026-07-25_sca002/instances/SCOPECHANGE-SCA002/LAUNCH_BRIEF.md`
(amended to **v2** on the Gate 1 ruling relay).

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
| D-5 | Finding `W-1` recorded and escalated, **not** corrected | Gate 1 holds no write authority over decomposition truth (`D-PEC-64` §2.5, §5). ~~`W-1` is also outside SCA-002's declared `MODIFY` mapping change class~~ — **superseded by C-1 (C-13):** `W-1`/A007 is `MODIFY`, which *is* the declared class; it was excluded by the `D-PEC-64` §4.3 byte-identity **window** and the intake's **subject scope**, both owner-amended at Gate 1. The operative reason to escalate rather than correct was the Gate 1 write-authority boundary alone. |
| D-6 | `Supersession_Delta.csv` disposition **not** settled at Gate 1 | Intake §5.5 assigns it to Gate 2/3. Recording it here would pre-empt a later gate. |
| D-7 | Three spurious Check-7 `BLOCKER`s discarded after root-cause | §3's `MappedDeliverables` uses range notation (`DEL-04-01..05`, `DEL-06-01..06`, `DEL-09-01..07`). Literal ID scanning undercounts. After range expansion, §3 and `Deliverables.csv` agree exactly for all six objectives. Recorded so the discarded findings are auditable rather than invisible. |
| D-8 | `AMENDMENT_ID = SCA-002` confirmed by directory scan **before** workspace creation | `_ScopeChange/` held only `SCA-001_2026-07-24_2206`, making `SCA-002` next-available and consistent with `D-PEC-64`. Note: `tools/query/scan_next_amendment_id.sh` now returns `SCA-003` **because this session's workspace exists** — that is the expected post-creation reading, not a conflict. |

### New facts found at Gate 1 (not in the intake)

| Ref | Finding | Disposition |
|---|---|---|
| `W-1` | `SOFTWARE_DECOMP.md` §5 line 376 states "29 S / 33 M / 2 L / 0 XL"; `Deliverables.csv` and §7 both yield "28 S / 34 M / 2 L / 0 XL". SCA-001 re-enveloped `DEL-10-10` `S`→`M` and reconciled the registers, `ContextBudgetQA.csv`, and §7 — but not the §5 prose. A residual reconciliation miss inside accepted revision 1.1. | Escalated to the owner as a Gate 1 open item. Documentation-consistency only; no topology impact; `D-PEC-64` §4.1's invariant agrees with the registers, not §5. ~~Outside SCA-002's change class.~~ **Superseded by C-1 (C-13):** `MODIFY`-legal; excluded by the §4.3 window and the intake's subject scope, not by change class. Ruled **"Fix now: add A007"**. |
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

### Gate 1 owner ruling — RULED 2026-07-25

Owner (Ryan Tufts) in-session; relayed by Agent 0. Verbatim options selected:

| # | Question | Owner's verbatim selection |
|---|---|---|
| 1 | Six-action list A001–A006 as parsed | **"Confirmed"** |
| 2 | Scope width | **"O-A wave-minimum"** |
| 3 | `W-1` disposition | **"Fix now: add A007"** |

**Effects, as executed by this session:**

| Ref | Effect |
|---|---|
| R-1 | **Scope width O-A** is final: 20 `IN` ledger rows (`SOW-001, 003, 011..017, 021, 025, 040, 042, 052, 053, 054, 056, 088, 089, 094`) and 17 deliverable rows (`DEL-00-01, 00-03, 01-01, 01-03, 01-05, 01-06, 02-01..07, 03-06, 08-01, 08-02, 10-03`). Both sets re-derived from the pinned registers in this session, not copied from the ruling. |
| R-2 | **`SOW-021` ⊆ `{OBJ-005}` is now a binding constraint**, not an observation. It originates in this session's F-2 finding and is written into `D-PEC-64` §4.3 by the owner's same-day amendment. Violating it forces `DEL-03-01`'s cell by the union invariant and breaks the 17-row window. |
| R-3 | **A007 added** to the action register: §5 line 376 `29 S / 33 M / 2 L / 0 XL` → `28 S / 34 M / 2 L / 0 XL`. `D-PEC-64` §4.3's byte-identity window amended the same day to admit exactly that one line. Re-validated `PASS` post-ruling. |
| R-4 | **Residue protection restated:** the 11 residue `IN` rows and 9 residue deliverables must remain byte-identical. `D-PEC-64` §4.3: "an unauthorized mapping of the intentional class is a verification failure, not a bonus." |
| R-5 | Gate 1 closed; Gate 2 released with write scope unchanged (Gates 1–2 surfaces only). |

### Corrections to this session's own Gate 1 return (round R-2b-g1)

| Ref | What was wrong | Correction |
|---|---|---|
| C-1 | The Gate 1 return characterized `W-1` as **"outside SCA-002's declared change class"** | **Wrong.** A007 is `MODIFY` — an attribute edit on an existing section — and `MODIFY` is precisely the declared class. What actually excluded it was the `D-PEC-64` §4.3 byte-identity **window** and the intake's **subject scope** (deliverable→objective mapping). Both were owner-amended at Gate 1. Change class was never the barrier, and saying so understated how cheaply the fix could be admitted. |
| C-2 | The Gate 1 return listed the intake §6.5 derivative-package table as a Gate 2 item among others | It is a **mandatory** Gate 2 output under `D-PEC-64` §4.5 and `AGENT_SCOPE_CHANGE.md` Gate 2 ("Produce `Impact_Assessment.md` with … Derivative-package status table"). Delivered in `Impact_Assessment.md` §4. |

### Snapshot-artifact deferrals (recorded per R-2b-g1)

The `AGENT_SCOPE_CHANGE.md` STRUCTURE snapshot layout is populated across
gates, not all at Gate 1. Current state of this snapshot:

| Artifact | State | When |
|---|---|---|
| `Brief.md` | present | Gate 1 (updated with the ruling) |
| `Decision_Log.md` | present, appended per gate | Gates 1–5 |
| `Impact_Assessment.md` | present | Gate 2 |
| `Amendment_Actions.csv` | **DEFERRED** | Gate 3 — written when the action register finalizes against approved exact text, so `AffectedFiles` and per-row `ActionSeq` are accurate rather than provisional |
| `Pre_Change_Coverage.json` | **DEFERRED** | copied into this snapshot from `COV_SCA002_PRECHANGE_2026-07-25_1040/coverage_summary.json` **before Gate 5**, so the snapshot is self-contained per the active-snapshot integrity rule |
| `Propagation_Plan.md` | present (**v2**) | Gate 4 |
| `Post_Change_Coverage.json`, `RUN_SUMMARY.md`, `Handoff_State.md` | not started | Gate 5 |
| `Supersession_Delta.csv` / `Supersession_Map.csv` | pending ruling | Gate 2/3 — see `Impact_Assessment.md` §5 |

Neither deferral is a gap in Gate 1 or Gate 2 evidence: both artifacts depend
on decisions those gates have not yet made.

---

## Gate 2 — Impact Assessment

**Opened:** 2026-07-25 · **Ruled:** 2026-07-25 · **Status:** `CLOSED` (ACCEPTED)
**Output:** `Impact_Assessment.md` (this snapshot)

### Agent-side resolutions

| Ref | Decision | Rationale |
|---|---|---|
| D-9 | Impact traced for **seven** actions under O-A, with A007 assessed separately from A001–A006 | A007 has a different consumer profile: it touches no register, no mapping, and no `_CONTEXT.md`, so folding it into the mapping impact would overstate its blast radius. |
| D-10 | `Supersession_Delta.csv` analysed and a recommendation given, but **not written** | The intake §5.5 assigns the owed-or-not question to Gate 2/3 as an owner ruling. Writing the file would pre-empt it; recommending without writing preserves the gate. Analysis in `Impact_Assessment.md` §5. |
| D-11 | `_REFERENCES.md` recorded as an **out-of-fence** stale surface rather than a propagation target | All 64 pin "revision 1.1" (measured), but `D-PEC-64` §3.3 **explicitly excludes** `_REFERENCES.md`. It cannot be refreshed by this session under any gate. Recorded as a `DEFERRED_BY_FENCE` derivative row with a named downstream owner — see `Impact_Assessment.md` §4 row 3 and open item `OI-B`. |
| D-12 | `Dependencies.csv` verdict is **conditional `NO_CHANGE`**, not flat `NO_CHANGE` | One row (`DEP-02-01-003`) quotes the §3 parser clause verbatim as both `SourceRef` and `EvidenceQuote` — the exact text A003 may rewrite. The verdict holds only if A003 preserves that sentence. See `Impact_Assessment.md` §4 row 2 and §6 `F-4`. |
| D-13 | ~~Expected closure verdict recorded as **`OPEN_PENDING_DERIVATIVE_CLOSURE`**~~ — **SUPERSEDED BY C-2.** Corrected to **`CLOSED_FOR_SCOPE_CHANGE_ONLY`** with obligations in `DownstreamRerunState = FROZEN`; the final call is a Gate 5 fact | ~~Four derivative rows leave live obligations outside this fence; SCA-001 could claim the cleaner verdict, SCA-002 cannot.~~ **Wrong, and refuted by the precedent quoted in §5 of the same document:** SCA-001's `Handoff_State.md` records `DownstreamRerunState: FROZEN` **together with** `ClosureVerdict: CLOSED_FOR_SCOPE_CHANGE_ONLY` (lines 19, 23) — out-of-fence obligations and the clean verdict coexist by design. `AGENT_SCOPE_CHANGE.md`:685 scopes `DerivativePackageState` to *decomposition-local* surfaces; of the four rows invoked, three are coordination surfaces and the fourth (`_REFERENCES.md`) is fence-excluded. |

### New findings at Gate 2 (not in the intake)

| Ref | Finding | Disposition |
|---|---|---|
| `F-4` | `DEP-02-01-003` in `DEL-02-01`'s `Dependencies.csv` quotes the §3 parser clause verbatim in both `SourceRef` and `EvidenceQuote` — the exact sentence A003 may amend. 1 of 255 dependency rows repo-wide. | Gate 3 drafting guidance: preserve the sentence verbatim (O-A *applies* it per `F-3`), keeping all 64 `Dependencies.csv` `NO_CHANGE`. Otherwise `dependency-extract` owes a `DEL-02-01` rerun. Owner question 3 at Gate 2. |
| `OI-B` | **All 64 `_REFERENCES.md` pin "revision 1.1"** — a basis-pointer surface the intake §6.5 table did not enumerate. `D-PEC-64` §3.3 explicitly excludes `_REFERENCES.md`, so this session cannot refresh it at any gate. | Recorded as `STALE_DEFERRED_BY_FENCE`; must appear in `Handoff_State.md` as an obligation owned by resumed `PROJECT_SETUP`. Owner question 2 at Gate 2. |
| `F-5` | The four-doc→SOW converter's `--package-objective-ref` is `required=True` (line 202). ~~An empty mapping means the converter **cannot be invoked at all**~~ — **superseded by C-11:** argparse requires the **flag**, not a valid value, so invocation is mechanically possible; what the caller lacks is any legal value to pass. The wall is the same, reached one step earlier than the validator's non-emptiness check. | Strengthens the wave-blocker warrant; no action needed. |

### Open items carried out of Gate 2

| Ref | Item | Owner |
|---|---|---|
| `OI-B` | 64 × `_REFERENCES.md` rev-1.1 basis pointers, out of fence | Owner to confirm deferral; resumed `PROJECT_SETUP` to execute |
| `F-4` | Parser-clause verbatim preservation vs `dependency-extract` rerun | Owner at Gate 2; drafting at Gate 3 |
| — | `Supersession_Delta.csv` owed-or-not | **Owner at Gate 2** — recommendation: not owed |
| — | `_CONTEXT.md` basis-pointer refresh vs deferral | **Gate 4**, deliberately not asked at Gate 2 |
| — | 9 `NEEDS ATTRIBUTION` candidate mappings with per-row warrant quotes | Gate 3 |
| `OI-A` | Binding-table drift in `AGENT_SCOPE_CHANGE.md` / `AGENT_AUDIT_DECOMP.md` | HELPS_HUMANS, outside this project fence |
| `OI-013` | No durable repo-native register validator | Pre-existing; Gate 5 deterministic post-checks |

### Corrections to this session's own Gate 2 return (round R-2b-g2)

Fourteen findings, all `ACCEPTED` at fan-in, applied as **C-2 … C-13**. Each
was independently re-verified against repo state in this session before
application. Full log with per-correction detail: `Impact_Assessment.md` §10.

| C | Content | Where |
|---|---|---|
| C-2 | Closure verdict → `CLOSED_FOR_SCOPE_CHANGE_ONLY` + `DownstreamRerunState = FROZEN`; Gate 5 decides | IA §7 |
| C-3 | `projects/pec/AGENTS.md` has no revision pin → `CURRENT`; only `_COORDINATION.md` is stale-on-acceptance | IA §4 rows 10 / 10b |
| C-4 | Owner question 3 withdrawn; `F-4` WITHDRAWN (wrong anchor, mandate conflict, wrong gate); `Dependencies.csv` unconditional `CURRENT` | IA §4/§6/§8/§9 |
| C-5 | Supersession recommendation made conditional on PRD-consumptive attributions; re-affirmed at Gate 3 | IA §5, §7 |
| C-6 | §3 dispositions normalized to `DIRECT_EDIT \| RECOMPUTE \| NO_CHANGE` + notes column | IA §3 |
| C-7 | `ContextBudgetQA.csv` is in-fence writable; removed from the failure-if-changed list | IA §2 |
| C-8 | Wave plan §7 = three re-pin points + one annotation; phantom "point 4" removed | IA §4 rows 4, 9 |
| C-9 | DAG-exhibit annotation partly extant (lines 347, 362); scheduled act targets §1 pins only | IA §4 row 4 |
| C-10 | v3.1 dependency schema has no objective column at all; phrasing corrected | IA §4 row 2 |
| C-11 | Converter "cannot be invoked" softened — argparse requires the flag, not a valid value | IA §6 |
| C-12 | §6 Scope Ledger removed from A001's affected sections | IA §1, §2 |
| C-13 | D-5 and the `W-1` finding row annotated in place as superseded by C-1 | this file, above |

**Pattern worth carrying forward.** Ten of the fourteen were overstatement
toward more alarm, more coupling, more staleness, and more owner questions
than the evidence supported — including a pessimistic closure verdict
contradicted by precedent I had quoted in the same document, and an
`AGENTS.md` staleness claim presented under a "measured" label without having
been measured. Gate 3 must measure every claim, cite the measurement, and
check evidence already in hand for contradiction before presenting.

### Gate 2 owner ruling — ACCEPTED 2026-07-25

Owner (Ryan Tufts) in-session; relayed by Agent 0. Impact assessment
**ACCEPTED**, both questions as recommended:

| Q | Question | Owner's verbatim selection | Effect |
|---|---|---|---|
| 1 | Supersession — no `Supersession_Delta.csv` binding owed under O-A, conditional on Gate 3 attributions remaining PRD-consumptive | **"Accept"** | Condition discharged at Gate 3 — see `Amendment_Preview.md` Part 4. Gate 5 carries SCA-001's header-only map forward via `accumulate_supersession_map.py --allow-empty` |
| 2 | `OI-B` — 64 `_REFERENCES.md` rev-1.1 pointers, fence-excluded | **"Record as deferred"** | Recorded in `Handoff_State.md` at Gate 5 as a deferred obligation owned by resumed `PROJECT_SETUP`. **No fence change** |

Gate 2 closed. Gate 3 released; write scope still `_ScopeChange/**` only.

---

## Gate 3 — Amendment Approval

**Opened:** 2026-07-25 · **Status:** drafted (preview **v2**), awaiting owner approval
**Outputs:** `Amendment_Preview.md` (v2), `Amendment_Actions.csv` (14 rows),
`Gate3_Simulation.json` (all in this snapshot)

### Agent-side resolutions

| Ref | Decision | Rationale |
|---|---|---|
| D-14 | Attributions derived from **my own read of `projects/pec/docs/PRD.md`**, every warrant quoted verbatim with a line anchor | The ruled method is `SourceRef` → PRD row → objective. Paraphrasing the PRD would make the warrant unauditable; the owner must be able to check each quote against the source. |
| D-15 | Four **register precedents** measured and used as attribution anchors | `SOW-010`→`OBJ-005` (rebuild/store cluster), ~~`SOW-055`/`DEL-10-02`→`OBJ-005`~~ **withdrawn by C-18 as tautological** — `SOW-055` restates OBJ-005 nearly verbatim and selects nothing for `SOW-025`, `DEL-08-03/04`→`OBJ-001` (PKG-08 transport), `SOW-018/019`→`OBJ-002` (reconciler layer). Anchoring to accepted register facts beats inventing a fresh rationale per row. |
| D-16 | Three rows presented as **genuinely ambiguous** with alternatives rather than given a confident single answer | `DEL-00-03` (LOW), `DEL-00-01` (MEDIUM), `DEL-08-01`/`SOW-003` (MEDIUM-HIGH). The PRD does not settle what an *authoring* deliverable "serves"; presenting a confident mapping would manufacture certainty the source does not support. |
| D-17 | INDIRECT-8 recommended at the full `[OBJ-001, OBJ-002]` set, **with the narrower alternative stated and evidenced** | §3's derivation is explicit about the set, and applying it is faithful to accepted rationale. But my own measurement shows OBJ-002's register locus is the reconciler layer (`SOW-006/018/019`), which genuinely supports a parsers-are-`OBJ-001`-only reading. The owner should choose knowingly rather than inherit my preference. |
| D-18 | A002 cells **derived** from A001 by the union invariant, never authored independently | Authoring both sides invites divergence. Deriving one from the other makes the invariant structurally true rather than checked after the fact. |
| D-19 | `_LATEST.md` handoff-state **body** drafted only as shape, values deferred to Gate 5 | The body states measured facts (closure verdict, audit state, verification results). Those measurements do not exist until Gate 5. Drafting plausible values now would be invention. |
| D-20 | Simulation run **in memory**, artifact written only inside the session workspace | Verifies the post-state without touching decomposition truth, honouring the Gate 3 write boundary. |

### New finding at Gate 3

| Ref | Finding | Disposition |
|---|---|---|
| `F-6` | **The ruled action register A001–A007 does not cover the document's own front matter.** Lines 6–8 and 11 carry `revision: "1.1"`, `date: 2026-07-24`, an `accepted:` line naming the SCA-001 successor, and `session_authorization` naming only SCA-001/D-PEC-61. If unamended, revision 1.2 ships **declaring itself revision 1.1**, contradicting both the amended §7 Revision row (A004) and `_LATEST.md` (A006). | Surfaced as proposed action **A008** with exact text, marked `PROPOSED - NOT YET RULED` in `Amendment_Actions.csv`. `MODIFY`-class and mechanically entailed by A004/A006, but **not** in the ruled register — **and, per C-14, not inside the §4.3 byte-window either**, so it needs a dated owner amendment of that window — so it is asked explicitly (Gate 3 Q4) rather than folded silently into A005. |

### Supersession condition — discharged

The Gate 2 acceptance was conditional on the Gate 3 attributions remaining
PRD-consumptive. Tested against all drafted attributions: none asserts a fact
absent from the PRD, contradicts a PRD statement, or changes a PRD authority
fact; A007 corrects toward register truth; A003 **applies** the §3 parser
derivation and retains the ingest/bridge and `SOW-063` clauses verbatim.
**Re-affirmed: no binding owed.** Full analysis in `Amendment_Preview.md`
Part 4. The re-affirmation holds under every alternative on the Gate 3 table.

### Simulation — six checks, all pass

Union invariant 0 violations file-wide · residue (11 IN + 9 deliverables)
untouched and still unmapped, `OUT`/`TBD` byte-identical · all changed tokens
match `^OBJ-[0-9]{3}$` after `;`-split · topology unchanged (94/71-14-9/64/11/6,
S 28 M 34 L 2) · §4.3 window exactly 20 + 17 with `DEL-03-01` unchanged and
`SOW-021` ⊆ `{OBJ-005}` · no column other than `ObjectiveIDs` /
`SupportsObjectives` changed. Evidence: `Gate3_Simulation.json`.

### Snapshot-artifact deferral discharged

`Amendment_Actions.csv` was deferred at Gate 1 "until the action register
finalizes". It is now written (SCA-001 schema; 10 rows at Gate 3, extended to 14 at Gate 4), with A008 flagged
`PROPOSED - NOT YET RULED` at the time of writing so the file never implied
approval the owner had not given (**resolved to approved at the Gate 3
ruling**). `Pre_Change_Coverage.json` remains deferred to pre-Gate-5.

### Gate 3 owner ruling

> _Pending. Five questions in `Amendment_Preview.md` **Part 8** — Q1 (**seven**
> per-row attribution rulings), Q2 (INDIRECT-8 breadth: AFFIRM / N1 / N2),
> Q3 (§3 header qualifier), Q4 (A008 **plus** the dated §4.3 window
> amendment), Q5 (everything else, **conditional on Q1/Q2 recommended**)._

### Corrections to this session's own Gate 3 package (round R-2b-g3)

26 findings, all `ACCEPTED`, applied as **C-14 … C-33** with the
`SOW-038`/`DL-11` note below. Full per-correction log:
`Amendment_Preview.md` Part 7. The refuters confirmed the **byte-level
mechanics sound** — one applied the whole amendment in scratch and reproduced
every old-text pair, the union invariant at 0, the 20+17/two-column
containment, the §3 arithmetic and wave-unmapped 17→0. Every defect was
framing or calibration.

| Group | Corrections |
|---|---|
| **Authority (critical)** | C-14 A008's "inside the window's revision-history text" claim was **false** — front matter is not §3/§7/§12/mapping-notes; requires a dated §4.3 amendment. C-15 A005a (§11 Decision Log) is **also** outside the window on the strict reading; one consistent reading adopted. C-16 A006's basis stated explicitly (§3.2 line 131 + §2.3; outside the byte-window by construction) |
| **Contingency (critical)** | C-17 the drafted A001/A002/A003b/A003d text is valid **only** under the recommended Q1/Q2 answers; surfaced to Part 0 and into Q5's wording; the unconditional "OBJ-003/OBJ-006 unchanged" sentence conditioned |
| **Attribution recalibration** | C-18 `SOW-055` precedent **withdrawn as tautological**. C-19 DEL-10-03 HIGH → LOW-MEDIUM, reframed (no §3 objective states K-AUTH-1's boundary — the `DL-14` condition — so O-A forces a least-wrong choice). C-20 DEL-03-06's warrant quote was **truncated at exactly the clause pointing elsewhere**; full PEC-SVC-003 quoted, `OBJ-002` alternatives presented. C-21 DEL-08-02 escalated. C-22 DEL-01-05 aligned with DEL-00-01 at MEDIUM. C-23 the `bound by C1/C2 across all items` convention engaged — constraint-like posture is not itself grounds for an OBJ-005 mapping. C-24 DEL-01-03 reasoned from the full requirement. C-29 the "six are HIGH/MEDIUM-HIGH" sentence withdrawn as false against my own labels |
| **Text** | C-25 "both intentional per DL-14" removed (`DL-14` covers `SOW-063` only); A004's parenthetical rescoped. C-26 A006 previewed as the complete successor file with marked Gate-5 slots. C-27 Q2's narrow options defined as N1/N2 with exact consequences. C-28 Part 4 added — `ContextBudgetQA.csv` and `Companion_Inventory.csv` determinations demonstrated |
| **Mechanical** | C-30 A003a split to `ActionSeq 3b`, conditional on Q3. C-31 `SCOPE_CHANGE_POSTCHECK` restored on every row (SCA-001 precedent; v1 dropped it with no rationale) and `NONE` replaced with named owners. C-32 `Gate3_Simulation.json` provenance added. C-33 citation hygiene — §8 anchor `:217–219` (soft-wrap), inserted bold removed from the §9.7:300 quote, Part-4/Part-5 cross-reference fixed |

**Note recorded per the relay — `SOW-038` / `DL-11` tension.** §3's mapping
notes call `SOW-033..039` "ingest/bridge items", but `SOW-038` (PEC-STR-004,
stream loss recovered by reconciliation) is assigned to **PKG-03 Reconciliation
& Parity** in §4, not PKG-07 — it is a reconciliation-side guarantee, not
ingest mechanics. The §3 grouping label is loose with respect to the package
assignment (`DL-11` records the forced boundary decisions). SCA-002 does **not**
resolve it: `SOW-038` is residue under O-A and its row is untouched. Recorded
so the next amendment touching that class inherits the observation.

**Pattern, third occurrence.** Gate 2's overstatement recurred here in a new
form: a false authority claim, contingent text presented as settled, a
tautological precedent dressed as evidence, and a quote cut at the clause that
disagreed with me. The mechanics have been sound at every gate; the framing has
consistently oversold them. For Gate 4: quote sources to their sentence end,
state an authority basis only after locating it in the packet text, and label
contingent work contingent.

### Gate 3 owner ruling — APPROVED 2026-07-25

Owner (Ryan Tufts) in-session; relayed by Agent 0. **Every question ruled as
recommended.**

| Q | Question | Ruling |
|---|---|---|
| Q1 | Seven per-row attributions | **All seven as recommended** — `OBJ-005`: DEL-00-01, DEL-01-05, DEL-03-06, DEL-10-03; `OBJ-001`: DEL-00-03, DEL-08-01, DEL-08-02 |
| Q2 | INDIRECT-8 breadth | **AFFIRM** `OBJ-001;OBJ-002` for all eight (not N1, not N2) |
| Q3 | §3 table header | **Drop "(best-effort)"** — `ActionSeq 3b` included |
| Q4 | A008 + window amendment | **Approved**, and `D-PEC-64` §4.3 **amendment #2** is recorded in the packet |
| Q5 | Complete exact text | **Approved as drafted** |

**Contingency condition satisfied.** Because Q1 and Q2 were ruled as
recommended, the Part 0 contingency does not fire: the drafted A001/A002/A003b/
A003d text is **final**, `OBJ-003` and `OBJ-006` §3 rows are confirmed
unchanged, and no re-derivation or re-simulation is owed. The Gate 3 text is
the **only** text Gate 5 may apply.

**§4.3 amendment #2, verified in the packet** (lines 202–213) rather than taken
from the relay. Recorded wording admits (i) the `SOFTWARE_DECOMP.md`
front-matter revision block, lines 6–8 and 11 (A008) and (ii) the §11 Decision
Log appended entry DL-17 (A005a), by the same instrument as the A007
amendment. Both authority gaps raised at Gate 3 are therefore **closed**, and
`Amendment_Actions.csv` rows 5 and 9 now read `AUTHORITY RESOLVED`.

`Amendment_Actions.csv` finalised: row `3b` conditional → **firm**; A008
`PROPOSED - NOT YET RULED` → **approved**; contingency notes resolved. No
`PROPOSED`, `CONTINGENT` or `AUTHORITY GAP` string remains in the register.
At Gate 4 it was **extended by appending** four propagation rows (`P1`–`P4`)
for the `_CONTEXT.md` line classes, snapshot-artifact completion, and the
`_LATEST.md` repoint + post-change audit — **14 rows total**. The ten
Gate-3-approved rows were left untouched (snapshot immutability).

Gate 3 closed. Gate 4 released; write scope still `_ScopeChange/**` only.

---

## Gate 4 — Propagation Plan Approval

**Opened:** 2026-07-25 · **Status:** planned, awaiting owner approval
**Output:** `Propagation_Plan.md` (this snapshot)

### Agent-side resolutions

| Ref | Decision | Rationale |
|---|---|---|
| D-21 | The 17 `SupportsObjectives` `_CONTEXT.md` lines refresh under **every** option — not presented as a question | A file whose stated purpose is to restate register truth cannot be left contradicting the register in the same edit. This is the propagation default; presenting it as a choice would manufacture a decision. |
| D-22 | `_CONTEXT.md` pointer refresh method is **surgical line replacement**, never regeneration | The provenance block is byte-identical across all 64 (measured: one occurrence per file, zero variants, lines 29–33). A literal match-and-replace has no templating step and therefore no risk of collateral field drift — regeneration from `Deliverables.csv` would re-derive fields the amendment has no authority to touch. |
| D-23 | Two pointer **text variants** offered (P-swap / P-supersede), P-supersede recommended | The existing sentence conflates *scaffolded-from* (historically revision 1.1, permanently true) with *current basis*. A naive 1.1→1.2 swap fixes the `current_basis` label by making the scaffold claim false. P-supersede keeps both facts true. Surfaced rather than silently choosing, because either is defensible and the owner may prefer the simpler diff. |
| D-24 | Recommended option **(ii)**, not (i) | (iii) is incoherent — it would leave the 17 edited files pointing at the superseded basis while restating the new mapping. Between (i) and (ii): `OI-B` (64 `_REFERENCES.md`) is fence-excluded and already deferred by owner ruling, so a pointer sweep is owed regardless. (ii) lets the 47 residual `_CONTEXT.md` pointers ride that same sweep. (i) is not wrong and I would apply it without objection; its cost is touching 47 files SCA-002 has no substantive business editing. |
| D-25 | Post-check enumerated to file + line-class granularity | `D-PEC-64` §4.3's window is prose. Gate 5's verification must be mechanical, so the plan converts it into an explicit allowed-change list including both owner amendments, with the unchanged sites (§3 `OBJ-003`/`OBJ-006`, §7 `ContextEnvelopeCounts`, front-matter `status`/`source_corpus`) named rather than implied. |
| D-26 | **No git operation at any Gate 5 step** | `AGENT_SCOPE_CHANGE.md` assigns staging to CHANGE; `D-PEC-64` §3.6(b) assigns the SCA-002 closure commit to resumed `PROJECT_SETUP` from this session's handoff file list. Gate 5 step 16 produces the list and a recommended message and stops. |
| D-27 | Gate 5 sequence is **abort-on-failure**, verification per step | Applying later edits over a failed earlier one would leave decomposition truth in a state neither the pre- nor post-condition describes, with no clean rollback short of revert. |

### Gate 4 owner ruling

> _Pending. Two questions in `Propagation_Plan.md` §6 — Q1 (`_CONTEXT.md`
> pointer scope: (i)/(ii)/(iii), plus the P-supersede/P-swap text variant),
> Q2 (approve the plan and release Gate 5)._

## Gate 5 — Execute and Validate

**Opened:** 2026-07-25 · **Status:** **`COMPLETED`** (resumed after an abort at
step 12 under plan amendment **v2.1**; final audit `OK`).

### Gate 4 owner ruling — APPROVED 2026-07-25

| Q | Ruling |
|---|---|
| Q1 | **"(i) All 64, P-supersede"** — full pointer refresh, supersession-note variant |
| Q2 | **"Approve and release"** — Gate 5 released; write scope widened to the full `D-PEC-64` §3.2 fence |

### Per-step execution record

| Step | Action | Result |
|---|---|---|
| 1 | Re-verify basis md5s | **PASS** — all three match the pins |
| 2 | A001 — 20 `ObjectiveIDs` cells | **PASS** — 20 applied, 20 rows changed, 0 other-column changes |
| 3 | A002 — 17 `SupportsObjectives` cells | **PASS** — 17 applied, 0 other-column changes, `DEL-03-01` unchanged, union invariant 0 |
| 4 | 10 `SOFTWARE_DECOMP.md` sites | **PASS** — 12 exact-string replacements each matched exactly once + 2 anchored appends (DL-17, revision row 1.2) |
| 4v | §3 ↔ register parity | **PASS** — all six objectives MATCH (20/12/12/10/7/9); `OBJ-003` and `OBJ-006` rows untouched; §7 `ContextEnvelopeCounts` unchanged; `status` and `source_corpus` unchanged |
| 4v | Post-change anchor map | **PASS** — §5→385, §7→537/541, DL-16→634 all as predicted; DL-17 landed at 635 and revision row 1.2 at 651 (the plan's "640→650" anchor was for the *existing* 1.1 row, which is at 650 — correct; my first probe was mislabelled) |
| 5 | A006 — `_Decomposition/_LATEST.md` | **PASS with a recorded plan gap** — see D-28 |
| 6 | 17 `_CONTEXT.md` mapping lines | **PASS** — pre-flight matched all 17 exactly once; 17 applied |
| 7 | 64 `_CONTEXT.md` pointer blocks (P-supersede) | **PASS** — pre-flight matched all 64 exactly once; 64 applied; 0 stale `current_basis` pointers remain; line 29 scaffold provenance untouched in all 64 |
| 8 | Post-check assertions 1–5, 7 | **PASS** — union 0; residue 11 IN + 9 deliverables still unmapped; `OUT`/`TBD` unmapped; 0 bad tokens; topology 94 (71/14/9), 64, 11, 6, S 28 / M 34 / L 2; 20 changed ledger rows; `DEL-03-01` = `OBJ-005`; `SOW-021` ⊆ `{OBJ-005}`; revision-1.2 parity across front matter, §7 and `_LATEST.md` |
| 8 | Collateral (assertion 8) | **PASS** — dep-closure 64 files / 255 rows / 135 ANCHOR / 120 EXECUTION / 62 nodes / 120 edges / orphans 2 / SCCs 0, matching D-PEC-62; census `64 OPEN` |
| 8 | Assertion 9 (option (i) grep) | **PASS** — 0 stale pointers repo-wide |
| 9 | `Pre_Change_Coverage.json` | **PASS** — `pec-software-register-baseline-v1`; pre-state reconstructed from `git show HEAD:` so the baseline is measured, not asserted; confirms pre 31 IN / 26 deliverables unmapped |
| 10 | `Supersession_Map.csv` | **PASS** — accumulator, `--allow-empty`, no `--delta`; 0 rows, 0 blocking findings |
| 11 | Repoint `_ScopeChange/_LATEST.md` → SCA-002 | **PASS** — 0 SCA-001 references remain |
| **12** | **Post-change `AUDIT_DECOMP`** | **BLOCKER — ABORTED** |
| 13 | `Post_Change_Coverage.json` (baseline schema) | **PASS** — all register-integrity checks and the six SCA-002 assertions recorded inside; post 11 IN / 9 deliverables unmapped |
| 13 | `Handoff_State.md` | **PASS** — four contract sections + closure verdict + FROZEN obligations table |
| 13 | `RUN_SUMMARY.md` | **PASS** — seven state fields |
| **12b** | **Final `AUDIT_DECOMP` pass** (amendment v2.1) | **PASS** — `COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257`, `overall_status OK`, **0 blockers / 0 warnings / 73 info**, Check 10 `active_snapshot_status PASS`, closure_readiness `PASS` |
| 14 | Fill A006 + `RUN_SUMMARY` slots; add `audit_decomp_final` citation | **PASS** — 0 literal slots remain in any artifact |
| 15 | `Decision_Log.md` Gate 5 record | **PASS** — this section |
| 16 | Git scope check | **PASS** — see below |
| 17 | Handoff file list + recommended commit message | **PASS** — returned; **no git operation performed** |

### The abort — step 12

`COV_SCA002_POSTCHANGE_2026-07-25_1252` returned `RUN_STATUS = BLOCKERS`,
`closure_readiness = FAIL`, 1 blocker:

```
COV-074,10,BLOCKER,SNAPSHOT,SCA-002_2026-07-25_1042,
"Active snapshot contract failed: missing ['Post_Change_Coverage.json',
 'Handoff_State.md', 'RUN_SUMMARY.md']"
```

Everything else in that run is clean: forward coverage 11/11 and 64/64,
reverse 100%, context fidelity 100% (the 64 amended `_CONTEXT.md` all still
match the registers), objective coverage 100%, objective-evidence integrity
`PASS`, package-shape `PASS` (**W-1 is gone** — A007 fixed it), 0 warnings,
73 info, lifecycle `64 OPEN`.

### Root cause — an unsatisfiable ordering in my own Gate 4 plan

This is **not** a defect in the amendment. It is a circular dependency I
introduced at Gate 4:

- Correction **C-36** moved the audit *after* the `_ScopeChange/_LATEST.md`
  repoint so Check 10 would validate **SCA-002's** snapshot rather than
  SCA-001's. That fixed a real problem.
- But Check 10 requires the **complete** artifact set, and three of those
  artifacts — `Post_Change_Coverage.json`, `Handoff_State.md`,
  `RUN_SUMMARY.md` — are written at steps 13–14, *after* the audit.
- `Post_Change_Coverage.json` cannot be written before the audit because it
  must cite the audit's output.

So at step 12 the audit can **never** pass Check 10. The plan as written is
unexecutable at this step, whichever order is chosen, without either running
the audit twice or accepting a known-incomplete Check 10.

I did **not** improvise a fix. Resolving it meant amending the approved
propagation plan — an Agent 0 / owner decision. The two candidate resolutions
put to Agent 0:

1. **Two-pass audit** — keep this run as the coverage//register evidence,
   complete steps 13–14, then re-run `AUDIT_DECOMP` so Check 10 sees the
   finished snapshot. Costs one extra immutable COV snapshot; yields a clean
   final audit.
2. **Accept Check 10 as expected-incomplete at step 12** — record the blocker
   as a known sequencing artifact in `RUN_SUMMARY.md`/`Handoff_State.md` and
   cap `AuditState` accordingly. Cheaper, but ships a `BLOCKERS` audit as the
   closure evidence, which `AGENT_SCOPE_CHANGE.md` treats as blocking.

I recommended **(1)**: the SCA-001 precedent is a clean post-change baseline,
and option (2) would leave the active snapshot's own audit asserting failure.

### Agent 0 disposition — plan amendment v2.1 (2026-07-25)

**Abort ruled correct; recommendation (1) ACCEPTED** as propagation-plan
amendment **v2.1: two-pass audit.** Procedural only — no new write surface
(the second COV snapshot lands inside the same `D-PEC-64` §3.2
`_Evaluation/DecompCoverage/**` grant), no amendment-text change, no window
change. Dispositioned at Agent 0 level and **disclosed to the owner at Gate 5
acceptance, where the final ruling remains theirs**. Nothing rolled back;
steps 2–11 stand as verified. Recorded in `Propagation_Plan.md` (v2.1 note).

**Outcome:** the final pass returned `OK` with **0 blockers and 0 warnings**,
Check 10 `PASS`. The two-pass structure is now the evidence: the interim run
is retained as first-pass register/coverage evidence and cited in
`Post_Change_Coverage.json.audit_decomp`; the final run is cited in
`audit_decomp_final` and is the closure evidence.

### Agent-side resolutions

| Ref | Decision | Rationale |
|---|---|---|
| D-28 | **A006 written in two phases** (plan gap recorded, not improvised around) | Step 5 must precede the audit so the audit sees revision 1.2 as `current_basis`, but `_LATEST.md` carries two audit-derived values (`{AUDIT_STATE}`, `{POST_COV_SNAPSHOT}`). Both remain as literal slots pending step 14. The plan's step-5 verification ("no literal `{` remains") is therefore **not yet satisfiable** and moves to step 14. This is a second instance of the same step-12 circularity. |
| D-29 | Aborted at step 12 rather than completing steps 13–17 and re-running the audit | The binding constraint is explicit: on an audit blocker, stop, write nothing further, report exact state. Re-running the audit after completing the artifacts would be the sensible engineering move **and** exactly the improvisation the rule forbids, because it silently amends the approved plan. |
| D-31 | Interim COV snapshot **retained**, not deleted | It is immutable evidence of a real run and of the ordering defect. Deleting it to tidy the record would erase the trace of a plan failure that the correction log depends on. Both passes are cited in `Post_Change_Coverage.json`. |
| D-30 | Decomposition truth left **applied**, not rolled back | The abort rule says stop and report, not revert. Steps 2–11 all passed their verifications; the amendment is internally consistent and validated. Rolling back would discard verified work on the strength of a sequencing artifact. State is reported precisely so Agent 0 can decide. |


---

## Gate 5 fix pass — round R-2b-g5 (2026-07-25)

Final refutation round on the executed state. The diff↔approved-text bijection
held on `SOFTWARE_DECOMP.md`, `Deliverables.csv` and all 64 `_CONTEXT.md`
(byte-identical to programmatic reconstruction); residue, `OUT`/`TBD` and
`DEL-03-01` byte-identical; all invariants reproduce; fence clean. **Eleven
findings** required a fix pass before owner acceptance. All fixes inside the
existing fence.

| # | Fix | Result |
|---|---|---|
| **C-54** | **`ScopeLedger.csv` SOW-064 quoting** — restored byte-identical to HEAD | Ledger diff **21 → 20 lines**; changed rows exactly the 20 approved; **no non-`ObjectiveIDs` field change**; 94 rows parsed |
| C-55 | Ledger md5 re-computed and **every citation reconciled** | `4bc5dace…` → **`9ece6f49fb5fc7f83f72fa897d01a325`** in `_Decomposition/_LATEST.md` and `Handoff_State.md` |
| **C-56** | `_ScopeChange/_LATEST.md` `AuditState` `WARNINGS` → **`NON_BLOCKING_PASS`** | Stale from the step-11 repoint, which ran *before* the final audit. Now consistent with `RUN_SUMMARY`, `_Decomposition/_LATEST.md` and `Post_Change_Coverage.json` |
| **C-57** | Same file pre-declared closure | `Status` → **`EXECUTED_AWAITING_OWNER_CONFIRMATION`**; "Gates 1–5 are owner-ruled" → "Gates 1–4 owner-ruled; Gate 5 executed and verified, awaiting owner confirmation"; `ClosureVerdict` → pending, with the value it takes on acceptance named |
| **C-58** | **Assertion 9 restated** in `Propagation_Plan.md` §3d with a dated correction note | The literal `grep 'revision 1.1'` returns **64 by design** under P-supersede — the string is retained deliberately. The satisfiable criterion is the **qualified** grep for ``revision 1.1 (`current_basis``, which returns 0. Gate 5 recorded PASS against the qualified form; the substitution is now explicit |
| C-59 | §2c option rationale qualified | "(i) collapses the post-check to one repo-wide grep" holds only in its **qualified** form. The recommendation stands — still one assertion, still no 47-file exception — but the rationale overstated it as a bare grep |
| C-60 | `RUN_SUMMARY.md` overstatement removed | "All post-check assertions pass" → "all pass **under the corrected assertion 9**"; the pre/post row reworded to "pointers asserting revision 1.1 as `current_basis`" |
| **C-61** | Interim COV snapshot marked honestly | `PARTIAL_RUN_NOTE.md` added stating it is the aborted step-12 first pass, **3 of 8 contract artifacts, incomplete by construction, superseded**. **No fake artifacts backfilled.** `Handoff_State` §3 row qualified |
| C-62 | Markdown defects | Orphaned double-backtick in `_Decomposition/_LATEST.md`; broken nested backticks in `RUN_SUMMARY.md` audit table |
| **C-63** | **Durable handoff file list** written into `Handoff_State.md` §9 | 90 paths, grouped (4 targets / 64 `_CONTEXT.md` / 9 snapshot / 13 COV) + commit message. §6 previously cited "§7's file list", which did not exist |
| C-64 | Derivative-**package** state table added (`Handoff_State` §3b) | The contract requires both the surface table and the package table; only the surface table existed |
| C-65 | `DerivativePackageState = COMPLETE` scoped explicitly | Clause added scoping it to **decomposition-local** surfaces per `AGENT_SCOPE_CHANGE.md`:685, so it cannot be misread as covering `_REFERENCES.md` |
| C-66 | `Propagation_Plan.md` front-matter status corrected | `awaiting_gate_4_approval` → `gate_4_approved; gate_5_executed_awaiting_owner_confirmation` |

### The SOW-064 incident — writer vs surgical edit

**What happened.** Steps 2–3 applied A001/A002 by parsing the CSVs with
`csv.DictReader`, mutating the target cells, and re-serialising the whole file
with `csv.DictWriter`. `DictWriter` applies `QUOTE_MINIMAL`, so it re-derived
quoting per field rather than preserving it. `SOW-064`'s `DecisionRef` value
`"DL-10; DL-11; SCA-001"` contains semicolons but no comma, so minimal quoting
dropped its quotes — a **2-byte change to a row outside the approved window**.

**Why the post-checks missed it.** Every assertion I ran was *semantic*: union
invariant, residue still unmapped, token grammar, topology, column containment.
All of those parse the CSV, and the parsed value is identical either way —
`DL-10; DL-11; SCA-001` reads the same quoted or bare. The one check that would
have caught it is the **byte-level** one `D-PEC-64` §4.3 actually specifies:
"everything else is byte-identical". I verified *containment* (which columns
changed) and never verified *byte-identity* of the untouched rows.

**The lesson, stated plainly.** I wrote the `_CONTEXT.md` propagation as exact
old→new string replacement precisely because the plan demanded byte-precision
there — and it came out clean, all 64 byte-identical to reconstruction. Then I
used a re-serialising writer on the registers, where the same requirement
applied and I did not carry it across. A round-trip through a parser is not a
surgical edit: it rewrites every byte it touches and silently renormalises
anything the writer's conventions disagree with.

**Rule for any future register edit in this project:** edit CSV rows by exact
line replacement, the same way `_CONTEXT.md` was edited — never by
parse-mutate-reserialise — and verify with a byte-level diff line count against
the approved row set, not only with parsed-field assertions.

### Fix-pass verification

- Ledger diff: **20 changed lines**, 20 changed rows, 0 non-`ObjectiveIDs`
  field changes, `SOW-064` byte-identical to HEAD.
- `Deliverables.csv` re-checked for the same defect class: **17 lines, 17 rows,
  0 non-`SupportsObjectives` changes** — clean (no quote-optional field was
  affected).
- `_CONTEXT.md`: 64 files, +209/−145 lines — exactly 64 pointer blocks (2→3
  lines) plus 17 mapping lines.
- No file outside the fix list changed.

---

## Gate 5 owner confirmation — ACCEPTED 2026-07-25

Owner (Ryan Tufts) in-session; relayed by Agent 0. Selected option, verbatim:

> **"Accept revision 1.2 (Recommended)"** — "Revision 1.2 becomes
> current_basis; SCA-002 closes CLOSED_FOR_SCOPE_CHANGE_ONLY with frozen
> downstream obligations; PROJECT_SETUP resumes for the closure commit and the
> D-PEC-63 re-pins. The three disclosures (two-pass audit, SOW-064 fix,
> assertion-9 restatement) are accepted as recorded."

**The three disclosures are accepted as recorded:**

| Disclosure | Where recorded |
|---|---|
| Two-pass audit (plan amendment v2.1, Agent 0 disposition) | `Propagation_Plan.md` v2.1 note; Gate 5 abort narrative + D-31 above; interim snapshot's `PARTIAL_RUN_NOTE.md` |
| SOW-064 quoting fix (writer renormalisation outside the approved window) | C-54/C-55 and the incident narrative above |
| Assertion-9 restatement (qualified grep) | C-58/C-59/C-60; `Propagation_Plan.md` §3d dated correction note |

## Five-gate record — closed

| Gate | Ruling | Date |
|---|---|---|
| 1 — Change Intake and Validation | RULED — O-A wave-minimum; A001–A006 confirmed + A007 added; `SOW-021` ⊆ `{OBJ-005}` | 2026-07-25 |
| 2 — Impact Assessment | ACCEPTED — no `Supersession_Delta.csv` owed (conditional, discharged at Gate 3); `OI-B` recorded as deferred | 2026-07-25 |
| 3 — Amendment Approval | APPROVED — all seven per-row attributions as recommended; INDIRECT-8 affirmed; header qualifier dropped; A008 + §4.3 amendment #2 | 2026-07-25 |
| 4 — Propagation Plan Approval | APPROVED — `_CONTEXT.md` option (i) all 64, P-supersede; Gate 5 released | 2026-07-25 |
| 5 — Execute and Validate | **CONFIRMED — `CLOSED_FOR_SCOPE_CHANGE_ONLY`** | 2026-07-25 |

**Final state.** `SOFTWARE_DECOMP.md` revision **1.2** is `current_basis`.
Topology unchanged (94 / 71-14-9 / 11 / 64 / 6; S 28 / M 34 / L 2 / XL 0). IN
items without objective mapping 31 → 11; deliverables without objective mapping
26 → 9; **Phase 2.2 wave members without objective mapping 17 → 0**. Final
audit `OK` — 0 blockers, 0 warnings.

**Next owner: `PROJECT_SETUP`**, resuming per `D-PEC-64` §2.4 — receipt,
closure commit from the `Handoff_State.md` §9 file list (90 paths), D-PEC-63
re-pins, `AGENTS.md` pointer refresh. Frozen obligations: `OI-B`, `OI-A`,
`OI-013`, the coordination-surface updates.

**SCOPE_CHANGE's role in SCA-002 is complete.** No git operation was performed
at any point in this session.
