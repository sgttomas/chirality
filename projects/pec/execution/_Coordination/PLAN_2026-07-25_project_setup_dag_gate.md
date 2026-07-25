# PLAN 2026-07-25 — PROJECT_SETUP: full-DAG materialization gate (candidate v0.2)

**Author:** PROJECT_SETUP (Agent 1), session of 2026-07-25
**Status:** AWAITING_OWNER_RULING — this is a gate exhibit and issue record,
not a landed dependency register.
**Session-plan rule:** this is the single timestamped plan for this session
(project `AGENTS.md` Issue-Plan Rule).

---

## 1. Derivative-package citation (upstream basis)

This candidate is a **derivative package** (root `AGENTS.md`
derivative-package rule): it cites accepted upstream truth and is never a
substitute for decomposition truth.

- Accepted basis: `execution/_Decomposition/SOFTWARE_DECOMP.md` **revision
  1.1** (`current_basis`), accepted 2026-07-24 under `D-PEC-61` as the
  SCA-001 successor.
- Immutable acceptance evidence: `execution/_ScopeChange/SCA-001_2026-07-24_2206/`.
- Basis integrity (md5 at read time, 2026-07-25):

```
ad944a2bfa7784778afa8558d8f81762  SOFTWARE_DECOMP.md
49e0cff9af647e41966b7a3334641919  ScopeLedger.csv
6d2b290b0c869fc1d51d626a1714abec  Deliverables.csv
05654b41b019a48dad97bfb5af09cd04  ContextBudgetQA.csv
6daf36b94b226e92f6348acc2bc15fc7  Companion_Inventory.csv
ecfb737936bf0e5e82d5408e2889b4ff  _LATEST.md
```

**Objective and edge semantics** (declared before edges, per
`docs/CYCLE_DRIVEN_RESOLUTION.md`): build-order capability-consumption
precedence for PEC v2's directed self-bootstrap under C16 — an edge
`A → B` means *B consumes a capability or artifact produced by A; B's start
or acceptance is gated on A reaching the (owner-ruled) maturity threshold*.
Non-precedence relations (co-landing, co-obligation, package-level,
phase-precedence, standing obligations) are in the constraints register,
**not** encoded as blocking edges.

## 2. Why this exists and why it was gated before landing

The accepted decomposition deliberately contains no dependency-edge register
(DL-16: "dependency-edge materialization stays with PROJECT_SETUP").
`execution/_Decomposition/_LATEST.md` directs: "Project Setup must
materialize the complete accepted dependency graph and blocker computation
from revision 1.1."

**Surfaced authority contradiction (not silently reconciled, per
`AGENT_PROJECT_SETUP.md` precedence rule):**

- *Permissive:* D-PEC-61 closure — "`PROJECT_SETUP` is released as the next
  owning workflow ... Project Setup still owns dependency-edge
  materialization, blocker computation, scaffolding, and its normal Phase
  1.3 ... gate." F-PEC-1 leaves `execution/_Coordination/**` writable by
  default.
- *Restrictive:* D-PEC-61 exact fence — "No implementation, scaffolding,
  `Dependencies.csv`, estimate, schedule, ... dependency, or external-system
  write is authorized"; `docs/STATUS.md` — "**Each tranche requires its own
  owner-ruled `D-PEC` packet** — nothing is authorized yet; `F-PEC-1`
  remains the outer fence."

Consequently this session **prepared and validated** the DAG candidate and
recorded it here as a gate exhibit (in-fence coordination surface), but
**landed no dependency register** at any storage path. Landing format, home,
and instrument are owner rulings (Section 6).

## 3. Method and adversarial fan-in (this session)

1. Extraction of candidate edges from revision 1.1 by PROJECT_SETUP, strata
   by provenance (Section 4).
2. Deterministic validation (session validator): 64/64 node coverage,
   acyclicity over all edges (Kahn 64/64), no duplicates/self-loops,
   phase-consistency with flagged exceptions, transitive satisfaction of the
   DEL-01-01 package-level constraint (13/13 PKG-03/04/05 members
   reachable). Result: PASS.
3. **Adversarial refutation fan-in** (three refutation-briefed ephemeral
   Agent 2 instances, opus-5, per this run's steer): R1 citation fidelity,
   R2 governance/fence compliance, R3 graph viability. 40 findings returned;
   all dispositioned by PROJECT_SETUP (Section 5). v0.1 → v0.2 changes:
   4 edges removed or reclassified as constraints, 18 edges added, 2-tier
   strata split into 3-tier (DECLARED / DERIVED / PROPOSAL), constraints
   register and STANDING node class introduced, §3-mapping citations
   populated, basis hashes added.
4. Re-validation of v0.2: PASS (120 edges; two PHASE_TENSION inversions,
   both deliberately flagged for owner ruling; two zero-edge nodes covered
   by constraint rows C-05/C-06 and C-08).

## 4. Gate exhibit — candidate DAG v0.2

**Node set:** the 64 accepted deliverables of revision 1.1 (`Deliverables.csv`
is node truth; no node invented). **Node classes:** `STANDING` (excluded from
one-shot COMPLETE/UNBLOCKED arithmetic; gate releases, not successors —
pending owner confirmation, constraint C-08): DEL-01-05, DEL-03-04,
DEL-10-02, DEL-10-03, DEL-10-10. All others `COMPLETABLE`.

**Strata (provenance, not authority — all strata require owner acceptance
for FULL_GRAPH use):**
- `DECLARED` (19): both endpoints ID-named in revision 1.1 with a
  dependency-bearing verb.
- `DERIVED` (19): dependency-bearing statement whose endpoints resolve
  uniquely via the Vocabulary Map or package structure.
- `PROPOSAL` (82): heuristic candidates under my instruction's
  candidate-proposal duty; require explicit owner acceptance.

**Flags:** `PHASE_TENSION` (E-P69, E-N02 — producer phased after consumer;
owner must rule staged-rule-set vs soft edge vs PhaseHint correction),
`AMBIGUOUS_BASIS` (E-A11 — revision 1.1 says "the other six views" while
DL-14 retyped DEL-09-07 non-UI; erratum candidate, see Section 7),
`LOW_CONFIDENCE` (E-N13, E-N18 — owner may decline).

### 4.1 Edge register (candidate)

```csv
EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale
E-A01,DEL-00-02,DEL-07-01,DECLARED,CONSUMES,,"Deliverables.csv DEL-00-02: ""Published one phase ahead of its P3 consumers (DEL-07-01/-03) per the PKG-00 publish/consume mechanic""",Named consumer of the event-contract schema
E-A02,DEL-00-02,DEL-07-03,DECLARED,CONSUMES,,"Deliverables.csv DEL-00-02: ""Published one phase ahead of its P3 consumers (DEL-07-01/-03)""",Named consumer of the event-contract schema
E-A03,DEL-00-02,DEL-07-02,DERIVED,CONSUMES,,"SOFTWARE_DECOMP.md §4 PKG-07: bridges ""implementing the PKG-00 event contracts""; DEL-00-02 description: ""consumable by daemon, hooks CLI, and adapters""",PKG-00's event contract resolves uniquely to DEL-00-02; daemon SSE bridge implements it
E-A04,DEL-00-02,DEL-07-04,DERIVED,CONSUMES,,"SOFTWARE_DECOMP.md §4 PKG-07: bridges ""implementing the PKG-00 event contracts""; DEL-00-02: ""consumable by daemon, hooks CLI, and adapters""",cmux adapter implements the same contract
E-A06,DEL-09-06,DEL-09-01,DERIVED,CONSUMES,,"Deliverables.csv DEL-09-06: ""built and sequenced first, consumed by the other six views as a declared dependency (DL-12 publish/consume mechanics, package-internal; DL-14)""",Shared drill-down component
E-A07,DEL-09-06,DEL-09-02,DERIVED,CONSUMES,,Deliverables.csv DEL-09-06 (as E-A06),Shared drill-down component
E-A08,DEL-09-06,DEL-09-03,DERIVED,CONSUMES,,Deliverables.csv DEL-09-06 (as E-A06),Shared drill-down component
E-A09,DEL-09-06,DEL-09-04,DERIVED,CONSUMES,,Deliverables.csv DEL-09-06 (as E-A06),Shared drill-down component
E-A10,DEL-09-06,DEL-09-05,DERIVED,CONSUMES,,Deliverables.csv DEL-09-06 (as E-A06),Shared drill-down component
E-A11,DEL-09-06,DEL-09-07,PROPOSAL,CONSUMES,AMBIGUOUS_BASIS,"Deliverables.csv DEL-09-06 (as E-A06): the text says ""six views""; DEL-09-07 is the sixth non-DEL-09-06 PKG-09 deliverable although DL-14 retyped it non-UI",Literal resolution of 'the other six views'; refuters recommend dropping; owner ruling requested
E-A12,DEL-09-07,DEL-09-01,DECLARED,CONSUMES,,"Deliverables.csv DEL-09-07: ""rendered by the DEL-09-01..05 views""",Views render the documented pressure rules; rules precede their renderers
E-A13,DEL-09-07,DEL-09-02,DECLARED,CONSUMES,,Deliverables.csv DEL-09-07 (as E-A12),Views render the pressure rules
E-A14,DEL-09-07,DEL-09-03,DECLARED,CONSUMES,,Deliverables.csv DEL-09-07 (as E-A12),Views render the pressure rules
E-A15,DEL-09-07,DEL-09-04,DECLARED,CONSUMES,,Deliverables.csv DEL-09-07 (as E-A12),Views render the pressure rules
E-A16,DEL-09-07,DEL-09-05,DECLARED,CONSUMES,,Deliverables.csv DEL-09-07 (as E-A12),Views render the pressure rules
E-A17,DEL-05-02,DEL-09-04,DECLARED,CONSUMES,,"Deliverables.csv DEL-09-04: ""Rendering of the PKG-05 slate""; ScopeLedger SOW-048 note: ""Renders SOW-024""",SOW-024 is covered by DEL-05-02
E-A18,DEL-03-04,DEL-10-11,DECLARED,MEASURES,,"Deliverables.csv DEL-10-11: ""sourced from DEL-03-04's output""; SOW-093 note: ""Measures the output of SOW-020 (DL-14)""",Parity metric reports DEL-03-04's DriftFindings
E-A20,DEL-03-05,DEL-10-08,DECLARED,TESTS,,"Deliverables.csv DEL-03-05: ""the P4 exit demonstration is DEL-10-08""; SOW-063 note: ""Tests SOW-038""",Exit demonstration of the recovery guarantee
E-A21,DEL-04-03,DEL-10-04,DECLARED,MEASURES,,"SOW-059 note: ""Method + any needed instrumentation; measures SOW-007""",SOW-007 is covered by DEL-04-03
E-A22,DEL-04-01,DEL-10-12,DECLARED,MEASURES,,"SOW-060 note: ""Measures uptake of SOW-004; arms limb 1 of the falsification clause""",SOW-004 is covered by DEL-04-01
E-A23,DEL-06-06,DEL-10-06,DECLARED,TESTS,,"SOW-061 note: ""Tests SOW-031""",SOW-031 is covered by DEL-06-06
E-A24,DEL-06-05,DEL-10-07,DECLARED,TESTS,,"SOW-062 note: ""Tests SOW-030""",SOW-030 is covered by DEL-06-05
E-A25,DEL-06-06,DEL-10-09,DECLARED,MEASURES,,"SOW-084 note: ""Measures effectiveness of SOW-031""",SOW-031 is covered by DEL-06-06
E-A26,DEL-01-04,DEL-10-05,DECLARED,CONSUMES,,"SOW-085 note: ""grounded in SOW-057 self-observability""",SOW-057 is covered by DEL-01-04
E-A27,DEL-10-01,DEL-04-01,DECLARED,SEQUENCING,,"SOW-058: ""Measure the Step-0 cost baseline ... before P1 begins""; note: ""baselines SOW-004/041""",Declared pre-P1 sequencing against SOW-004
E-A28,DEL-10-01,DEL-08-04,DECLARED,SEQUENCING,,"SOW-058 note: ""baselines SOW-004/041""",Declared pre-P1 sequencing against SOW-041
E-P01,DEL-00-01,DEL-01-01,PROPOSAL,CONSUMES,,"OI-012: core-isolation style ""Decided in DEL-00-01's ADR""; ""the one seam to keep crisp is entity schema (core) vs store persistence (adapter) inside PKG-01""",The ADR ruling shapes the PKG-01 schema/persistence seam
E-P03,DEL-01-01,DEL-02-01,PROPOSAL,CONSUMES,,"§3 mapping notes: ""parser items (SOW-011..017) underlie OBJ-001/OBJ-002 through the record tier (SOW-001)""",Parser emits record-tier entities defined by the entity model
E-P04,DEL-01-01,DEL-02-02,PROPOSAL,CONSUMES,,§3 mapping notes (as E-P03),Parser emits DecisionRow entities
E-P05,DEL-01-01,DEL-02-03,PROPOSAL,CONSUMES,,§3 mapping notes (as E-P03),Parser emits Receipt entities
E-P06,DEL-01-01,DEL-02-04,PROPOSAL,CONSUMES,,§3 mapping notes (as E-P03),Parser emits RunRecord entities
E-P07,DEL-01-01,DEL-02-05,PROPOSAL,CONSUMES,,§3 mapping notes (as E-P03),Parser emits DependencyEdge entities
E-P08,DEL-01-01,DEL-02-06,PROPOSAL,CONSUMES,,§3 mapping notes (as E-P03),Parser emits Workplan/Step/Gate entities
E-P10,DEL-01-01,DEL-03-01,PROPOSAL,CONSUMES,,"DEL-01-01 envelope note: ""the schema every derivation package depends on"" (package-level accepted; deliverable pairing proposed — constraint C-03)",Reconciler entry point of PKG-03
E-P11,DEL-01-01,DEL-04-01,PROPOSAL,CONSUMES,,DEL-01-01 envelope note (as E-P10),Orientation derivation entry point of PKG-04
E-P12,DEL-01-01,DEL-05-01,PROPOSAL,CONSUMES,,DEL-01-01 envelope note (as E-P10),Gate-evaluation derivation entry point of PKG-05
E-P13,DEL-01-01,DEL-05-02,PROPOSAL,CONSUMES,,DEL-01-01 envelope note (as E-P10),Slate derivation in PKG-05
E-P14,DEL-01-01,DEL-07-05,PROPOSAL,CONSUMES,,"SOW-087: ""Reimplement the shared-runtime client seam concept against v2 entities""",The v2 entities are DEL-01-01's model
E-P15,DEL-01-03,DEL-03-01,PROPOSAL,CONSUMES,,,Reconciler writes are restricted to the store; store lifecycle must exist
E-P16,DEL-01-03,DEL-07-01,PROPOSAL,CONSUMES,,,Durable message store lives in the gitignored store
E-P17,DEL-01-03,DEL-01-02,PROPOSAL,CONSUMES,,,Presence-tier schema is hosted by the same store lifecycle
E-P18,DEL-01-06,DEL-03-01,PROPOSAL,CONSUMES,,"SOW-094: configuration ""naming the loops PEC serves""",Reconciler needs the loop registry
E-P19,DEL-02-01,DEL-03-01,PROPOSAL,CONSUMES,,PEC-RCN-002 feed list (DL-4),Full rebuild ingests the _STATUS.md feed
E-P20,DEL-02-02,DEL-03-01,PROPOSAL,CONSUMES,,PEC-RCN-002 feed list (DL-4),Full rebuild ingests decision registers/packets
E-P21,DEL-02-03,DEL-03-01,PROPOSAL,CONSUMES,,PEC-RCN-002 feed list (DL-4),Full rebuild ingests receipts ledgers
E-P22,DEL-02-04,DEL-03-01,PROPOSAL,CONSUMES,,PEC-RCN-002 feed list (DL-4),Full rebuild ingests run-evidence JSON
E-P23,DEL-02-05,DEL-03-01,PROPOSAL,CONSUMES,,PEC-RCN-002 feed list (DL-4),Full rebuild ingests dependency registers
E-P24,DEL-02-06,DEL-03-01,PROPOSAL,CONSUMES,,PEC-RCN-002 feed list (DL-4),Full rebuild ingests workplans/LOOP_INIT
E-P25,DEL-02-07,DEL-03-01,PROPOSAL,CONSUMES,,"SOW-017: adapter.yaml ""as the feed manifest""",Manifest drives which feeds are read per loop
E-P26,DEL-03-01,DEL-03-02,PROPOSAL,CONSUMES,,,Incremental reconcile presupposes the full-rebuild path and examined-SHA baseline
E-P27,DEL-03-01,DEL-03-03,PROPOSAL,CONSUMES,,,Drift classification compares successive reconcile snapshots
E-P28,DEL-03-01,DEL-03-04,PROPOSAL,CONSUMES,,,Parity diff runs over PEC derivations produced by reconcile
E-P29,DEL-03-01,DEL-03-05,PROPOSAL,CONSUMES,,,Recovery guarantee is reconciliation supremacy; needs the reconcile path
E-P30,DEL-03-01,DEL-03-06,PROPOSAL,TESTS,,,Perf bounds test the full rebuild
E-P31,DEL-03-02,DEL-03-06,PROPOSAL,TESTS,,,Perf bounds test incremental reconcile
E-P32,DEL-03-01,DEL-04-01,PROPOSAL,CONSUMES,,,Orientation derives from a populated record tier
E-P33,DEL-03-02,DEL-04-02,PROPOSAL,CONSUMES,,,Deltas since SHA ride the incremental examined-SHA machinery
E-P34,DEL-04-01,DEL-04-03,PROPOSAL,CONSUMES,,,Citation/freshness stamping applies to orientation responses
E-P35,DEL-04-01,DEL-04-04,PROPOSAL,CONSUMES,,,Scope parameterization parameterizes the orientation return
E-P36,DEL-04-01,DEL-04-05,PROPOSAL,CONSUMES,,,Limitation honesty is a property of orientation responses
E-P37,DEL-03-01,DEL-05-01,PROPOSAL,CONSUMES,,,Gate preconditions evaluate record-tier and Git facts
E-P38,DEL-03-01,DEL-05-02,PROPOSAL,CONSUMES,,,Slate aggregates AWAITING_RULING rows from the record tier
E-P39,DEL-01-02,DEL-06-01,PROPOSAL,CONSUMES,,,Presence writer needs the presence-tier schema
E-P40,DEL-01-02,DEL-06-02,PROPOSAL,CONSUMES,,,Worktree scanner writes presence-tier entities
E-P41,DEL-06-01,DEL-06-03,PROPOSAL,CONSUMES,,,Correlation joins session records
E-P42,DEL-06-02,DEL-06-03,PROPOSAL,CONSUMES,,,Correlation joins worktree scan results
E-P43,DEL-06-03,DEL-06-06,PROPOSAL,CONSUMES,,,Overlap detection consumes the session×worktree×scope join
E-P44,DEL-06-01,DEL-06-05,PROPOSAL,CONSUMES,,,TTL/heartbeat machinery rides presence records
E-P45,DEL-07-03,DEL-06-01,PROPOSAL,CONSUMES,,"SOW-036: hooks CLI carries ""session start/stop, status, scope declaration""",Session presence facts arrive via the hooks CLI bridge
E-P46,DEL-07-02,DEL-06-04,DERIVED,CONSUMES,,"SOW-029: hierarchy edges ""from daemon and hook feeds""",Daemon feed input to hierarchy edges
E-P47,DEL-07-03,DEL-06-04,DERIVED,CONSUMES,,SOW-029 (as E-P46),Hook feed input to hierarchy edges
E-P48,DEL-07-01,DEL-07-02,PROPOSAL,CONSUMES,,,Bridge delivers into the ingest endpoint/message store
E-P49,DEL-07-01,DEL-07-03,PROPOSAL,CONSUMES,,,Bridge delivers into the ingest endpoint/message store
E-P50,DEL-07-01,DEL-07-04,PROPOSAL,CONSUMES,,,Adapter delivers into the ingest endpoint/message store
E-P51,DEL-04-01,DEL-08-04,PROPOSAL,TESTS,,,Latency budget tests orientation reads
E-P52,DEL-08-01,DEL-08-04,PROPOSAL,TESTS,,,Latency measured through the API surface
E-P53,DEL-04-03,DEL-08-03,PROPOSAL,CONSUMES,,,Response format carries citations produced by the citation layer
E-P54,DEL-08-01,DEL-10-03,PROPOSAL,TESTS,,"SOW-025: ""a tested property of the API surface""",The API surface under negative test is DEL-08-01's server
E-P55,DEL-08-02,DEL-10-03,PROPOSAL,TESTS,,SOW-025 (as E-P54),The schema defines the surface under negative test
E-P56,DEL-04-02,DEL-08-05,PROPOSAL,CONSUMES,,"SOW-044: ""SSE subscription for deltas and presence changes""",Delta stream source
E-P57,DEL-06-01,DEL-08-05,PROPOSAL,CONSUMES,,SOW-044 (as E-P56),Presence-change stream source
E-P58,DEL-08-01,DEL-08-05,PROPOSAL,CONSUMES,,,SSE endpoint rides the socket server
E-P59,DEL-04-01,DEL-09-01,DERIVED,CONSUMES,,"SOW-045: ""Dashboard — Overview: the orientation return per loop""",'The orientation return' is DEL-04-01's serve (Vocabulary Map)
E-P60,DEL-05-01,DEL-09-01,PROPOSAL,CONSUMES,,"SOW-045: overview shows ""gates that matter""",Gate states from the Explain-shaped evaluators
E-P61,DEL-03-01,DEL-09-02,PROPOSAL,CONSUMES,,,Lifecycle census reads record-tier Package/Deliverable entities
E-P62,DEL-01-06,DEL-09-02,PROPOSAL,CONSUMES,,"SOW-094 SourceRef ""§12 P2, PEC-DSH-002""; DEL-01-06: ""extended to all five registered loops at P2""",Census spans the registered loops
E-P63,DEL-03-01,DEL-09-03,PROPOSAL,CONSUMES,,,Register views read record-tier registers
E-P64,DEL-06-03,DEL-09-05,DERIVED,CONSUMES,,SOW-049: presence board renders sessions × worktrees × hierarchy,Correlation join feeds the board
E-P65,DEL-06-05,DEL-09-05,DERIVED,CONSUMES,,"SOW-049: ""heartbeat age""",Heartbeat-age facts feed the board
E-P66,DEL-06-06,DEL-09-05,DERIVED,CONSUMES,,"SOW-049: ""advisory overlap warnings""",Overlap warnings feed the board
E-P67,DEL-03-03,DEL-09-07,DERIVED,CONSUMES,,"SOW-051: pressure rules include ""drift density""",Drift classification output feeds the rule
E-P68,DEL-05-01,DEL-09-07,DERIVED,CONSUMES,,"SOW-051: pressure rules include ""gate-blocked""",Gate verdicts feed the rule
E-P69,DEL-06-06,DEL-09-07,DERIVED,CONSUMES,PHASE_TENSION,"SOW-051: pressure rules include ""collision risk""",P3 producer for a P2 consumer; staged rule set vs soft edge — owner classification requested
E-P70,DEL-04-03,DEL-09-06,PROPOSAL,CONSUMES,,"SOW-050: drill-down ""from every displayed value to its cited source""",Citation shapes resolved by drill-down are DEL-04-03's artifact
E-P71,DEL-01-03,DEL-10-02,PROPOSAL,TESTS,,"SOW-055: ""delete the store""",Kill test exercises store safe-delete semantics
E-P72,DEL-03-01,DEL-10-02,PROPOSAL,TESTS,,SOW-055 + PEC-K-02,Kill test proves rebuildability after deletion
E-P73,DEL-02-05,DEL-10-10,PROPOSAL,CONSUMES,,"SOW-064: P1 ""ingests PEC v2's accepted full dependency DAG""; SOW-015: dependency registers into DependencyEdge",The DAG's file form is read by the dependency register parser
E-P74,DEL-03-01,DEL-10-10,PROPOSAL,CONSUMES,,SOW-064 (as E-P73),Self-ingest runs through the reconciler
E-P75,DEL-04-01,DEL-10-05,PROPOSAL,MEASURES,,"DEL-10-05: ""Orientation-read ... logging""",Orientation reads are a logged consultation surface
E-P76,DEL-09-01,DEL-10-05,PROPOSAL,MEASURES,,"DEL-10-05: ""dashboard-consultation logging""",Dashboard consultation is the other logged surface
E-P77,DEL-07-03,DEL-10-12,PROPOSAL,MEASURES,,"SOW-060: ""eligible session starts / mode transitions consuming orientation""",Poll instrumentation observes session starts via the hooks bridge
E-P78,DEL-07-01,DEL-10-08,PROPOSAL,TESTS,,SOW-063: stream loss requires a live stream to lose,Demonstration needs live ingest to interrupt
E-N01,DEL-00-02,DEL-07-05,DERIVED,CONSUMES,,"§4 PKG-07: ""...the shared-runtime client seam — implementing the PKG-00 event contracts""",R1-F4/R3-F5: em-dash clause covers the client seam
E-N02,DEL-06-04,DEL-09-05,DERIVED,CONSUMES,PHASE_TENSION,"SOW-049 / DEL-09-05: ""sessions x worktrees x live hierarchy""; DEL-06-04 is ""Live hierarchy edges""",R1-F5/R3-F8: named input; P4 producer for a P3 view — owner classification requested
E-N03,DEL-02-03,DEL-04-05,DECLARED,CONSUMES,,"SOW-013 note: ""Per-loop coverage limits stated (SOW-009)""",R1-F7: ID-explicit cross-link
E-N04,DEL-04-03,DEL-09-07,DERIVED,CONSUMES,,"SOW-051 ""staleness"" + Vocabulary Map: examined-through SHA is ""the staleness comparator (PEC-K-04)""",R1-F10: staleness rule input
E-N05,DEL-03-01,DEL-09-07,PROPOSAL,CONSUMES,,"SOW-051 ""stuck-in-state age""",R1-F10: lifecycle-state age read from the record tier
E-N06,DEL-08-01,DEL-09-06,PROPOSAL,CONSUMES,,"DEL-08-05: ""P2/P3 dashboards poll""; PKG-09 exclusion ""New data classes"" bars direct store reads",R1-F12/R3-F1: dashboards consume the API transport via the shared component
E-N07,DEL-08-03,DEL-09-06,PROPOSAL,CONSUMES,,as E-N06,R3-F1: views consume the citation-bearing envelope
E-N08,DEL-08-01,DEL-10-12,PROPOSAL,MEASURES,,"SOW-060: sessions ""consuming orientation"" (served over the API)",R3-F1: adoption instrumentation observes API consumption
E-N09,DEL-01-02,DEL-06-04,PROPOSAL,CONSUMES,,DEL-01-02 defines HierarchyEdge,R3-F3: DEL-06-04 creates HierarchyEdge instances
E-N10,DEL-06-01,DEL-06-04,PROPOSAL,CONSUMES,,"DEL-06-04: ""Parent-to-child session edges""; sessions are DEL-06-01's records",R3-F3
E-N11,DEL-08-02,DEL-08-03,PROPOSAL,CONSUMES,,SOW-042 additive versioned schema governs the response surface,R3-F4: envelope is schema-governed
E-N12,DEL-08-03,DEL-08-04,PROPOSAL,TESTS,,,R3-F4: serializer sits on the measured p95 latency path
E-N13,DEL-08-02,DEL-07-05,PROPOSAL,CONSUMES,LOW_CONFIDENCE,,R3-F5: a client seam is a client of the versioned API surface; owner may decline
E-N14,DEL-01-04,DEL-03-01,PROPOSAL,CONSUMES,,"SOW-057: ""Log PEC's own reconcile runs""",R3-F6: facility-first — logging facility precedes its emitting subjects
E-N15,DEL-01-04,DEL-07-01,PROPOSAL,CONSUMES,,"SOW-057: ""...and ingest activity""",R3-F6: ingest-logging half is phase-staged to P3
E-N16,DEL-01-06,DEL-02-07,PROPOSAL,CONSUMES,,"DEL-01-06 names ""the loops PEC serves""; DEL-02-07 reads per-project manifests per loop",R3-F13: replaces removed E-P09
E-N17,DEL-04-03,DEL-04-05,PROPOSAL,CONSUMES,,"SOW-009 ""unparseable or stale""; staleness defined by DEL-04-03's per-feed freshness",R3-F14
E-N18,DEL-00-01,DEL-00-02,PROPOSAL,CONSUMES,LOW_CONFIDENCE,"OI-012 basis: ""driving edges: PKG-07/08/09""; DEL-00-02 envelope tied to OI-009",R3-F15: owner may prefer PKG-00 unordered
```

### 4.2 Constraints register (non-gating; not blocking edges)

```csv
ConstraintID,Kind,Parties,Provenance,Statement,Notes
C-01,CO_LANDING,"DEL-03-05, DEL-07-01","DECLARED — DEL-03-05: ""Lands with the first ingest (DEL-07-01, P3) so ingest is never live without its safety invariant""; DL-14",DEL-07-01 may not be accepted/live without DEL-03-05; simultaneity permitted,Was blocking edge E-A19; R1-F9/R3-F2: precedence encoding over-strengthened the text
C-02,CO_OBLIGATION,"DEL-04-03, DEL-06-05","DECLARED — DEL-06-05: ""The exclusion is two-sided: the presence-store guard lands here; the citation-production side is asserted in DEL-04-03's tests (declared dependency edge, DL-14)""",One PEC-K-05/C4 enforcement obligation split across two write scopes; direction not declared,Was edge E-A05. R1-F1/R3-F7: a P1 test cannot assert exclusion of a tier first existing at P3 — DEL-04-03 carries a P3-reopened acceptance obligation. PHASE_TENSION; owner ruling requested
C-03,PACKAGE_LEVEL,DEL-01-01 ⇐ all PKG-03/04/05 members,"DECLARED — DEL-01-01 envelope note: ""the schema every derivation package depends on""; derivation set per §2.4/OI-012",Every PKG-03/04/05 deliverable depends on DEL-01-01 directly or transitively,Deliverable-level entry edges (E-P10..13) are PROPOSAL; validator proves transitive closure 13/13
C-04,PHASE_PRECEDENCE,pre-P1 < P1 < P2 < P3 < P4,"PhaseHint metadata (DL-3/DL-13b: sequencing metadata, not authority)",Release-strategy ordering; hard-vs-soft classification is a Phase 1.3 owner ruling,Not materialized as pairwise edges; flagged exceptions: E-P69 E-N02 C-02
C-05,PRE_P1_OBLIGATION,"DEL-00-01, DEL-00-03, DEL-10-01","DECLARED — SOW-058 ""before P1 begins""; DEL-00-03 ""seeded before P1""; DEL-00-01 pre-P1",All three complete before any P1 node starts,E-A27/E-A28 carry the two ID-named baseline targets as edges
C-06,UNRESOLVED_CONSUMERS,DEL-00-03,"DECLARED publish/consume (DL-12, DL-14) without named consumers",The v2 SPEC seed has declared dependants; the accepted text names none at deliverable level,R1-F6: deliberate no-edge record; consumers resolvable at WORKING_ITEMS activation or by owner ruling
C-07,DEFERRED_CONSUMPTION,DEL-08-05 → PKG-09 views,"DECLARED — DEL-08-05: ""P2/P3 dashboards poll; live subscription arrives with the P4 streams tranche""",No P2/P3 edge by declaration; P4 SSE consumption recorded as deferred,R1-F12: deliberate exclusion record
C-08,STANDING_NODES,"DEL-01-05, DEL-03-04, DEL-10-02, DEL-10-03, DEL-10-10","Own text: ""Automated assertion"" / ""Permanent"" / ""Runs at every release"" / ""tested property"" / ""standing validation""",Standing obligations: excluded from one-shot COMPLETE/UNBLOCKED arithmetic; they gate releases not successors,R3-F9; owner confirmation requested. DEL-10-10 is the bootstrap progression record itself
C-09,DELIBERATE_EXCLUSION,DEL-10-05 ↔ DEL-10-12,"SOW-060 note ""(limb 2: SOW-085)""; DEL-10-05 ""Split from poll adoption (DEL-10-12)""",Co-arming/provenance cross-link not a dependency; no edge,R1-F14
C-10,STRATUM_RULE,register-wide,Fan-in ruling 2026-07-25,DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines); DERIVED = unique non-ID resolution; PROPOSAL = heuristic. All strata require owner acceptance; strata are provenance not authority,R1-F3/R1-F14/R2-F1: one rule applied register-wide
```

### 4.3 Validation evidence (v0.2)

- Node coverage 64/64 against `Deliverables.csv`; no invented IDs.
- Acyclicity over all 120 edges: PASS (Kahn, 64/64 sorted); every subgraph
  of an acyclic graph is acyclic, so both provenance strata are acyclic.
  No SCCs exist; no cycle-resolution move required
  (`docs/CYCLE_DRIVEN_RESOLUTION.md` posture noted for reruns).
- No duplicate pairs, no self-loops.
- Phase consistency: 118/120 forward; the 2 inversions are the flagged
  E-P69 and E-N02 owner questions.
- C-03 transitive closure: 13/13 PKG-03/04/05 members reachable from
  DEL-01-01.
- Roots (9): DEL-00-01, DEL-00-03, DEL-01-03, DEL-01-04, DEL-01-05,
  DEL-01-06, DEL-08-01, DEL-08-02, DEL-10-01. Zero-edge nodes: DEL-00-03
  (C-05/C-06), DEL-01-05 (C-08 standing CI gate — deliberate).
- At landing, the register is regenerated in the repo-canonical v3.1
  dependency-register schema and re-audited with
  `tools/coordination/audit_dag.py` + `tools/validation/validate_dependencies_schema.py`
  (R2-F6/F7 disposition); the session validator is session evidence only.
  *(Superseded 2026-07-25 by owner ruling 3 / D-PEC-62 §3.3: no central
  aggregate exists for `audit_dag.py` to read; `analyze_dep_closure.py`
  over deliverable-local registers is the substituted closure check.)*

## 5. Adversarial fan-in disposition summary

Three refutation-briefed ephemeral Agent 2 instances (opus-5). 40 findings;
dispositions by PROJECT_SETUP:

| Refuter | Accepted | Partially accepted | Declined | Material outcomes |
|---|---|---|---|---|
| R1 citation fidelity (14) | 11 | 3 (E-A11 kept as flagged PROPOSAL rather than dropped; E-A03/04 resolved by DERIVED tier rather than demotion to heuristic; verb list published as C-10) | 0 | Strata split; E-N01..N04 added; deliberate-exclusion records C-06/C-07/C-09 |
| R2 governance (11) | 8 | 3 (F1: declared stratum retained but disciplined, count now 19 not 28, all with verbatim quotes; F2/F3: register held as gate exhibit, not landed — materialization itself was owner-directed in `_LATEST.md`, so candidate authoring was not re-asked) | 0 | Authority contradiction surfaced (§2); no `_LATEST.md`/tool-root scaffold write; v3.1-schema landing plan; basis hashes; receipt authorization folded into packet question |
| R3 graph viability (15) | 13 | 2 (F9 standing-node exclusion pending owner confirmation C-08; F12 transitive-redundancy marking deferred to v3.1 landing) | 0 | E-P02/E-P09 removed; E-A19/E-A05 converted to C-01/C-02; E-N05..N18 added; PKG-08→PKG-09 boundary closed |

Refuter session IDs: a2b9d4acc058b8600 (R1), ad1dd1546670ea6cb (R2),
ae25229439004aa01 (R3); full returns in the session transcript.

**Fourth round (post-ruling):** the D-PEC-62 draft packet was itself
refutation-checked before presentation (R4, session a6c21e82ca668384c,
opus-5; 25 findings, several empirically tested against a simulated
end-state — including a fatal scaffold→status tool-sequence defect and
verification values the named tools never emit). All 25 dispositioned;
packet rewritten as DRAFT v2 with calibrated verification values, a pinned
v3.1 row template, anchor-row seeding, exhibit-freeze clause, and corrected
fence/rollback/pointer clauses.

## 6. Owner gate — decisions requested

> **RULED 2026-07-25 (in-session gate answers):** (1) landing instrument =
> `D-PEC-62` packet — drafted at
> `_DECISIONS/D-PEC-62_project_setup_scaffold_and_local_dependency_registers.md`,
> awaiting owner ruling; (2) threshold = `INITIALIZED`; (3) storage =
> deliverable-local `Dependencies.csv` v3.1 + `_DEPENDENCIES.md`, no
> standing central register (owner: central registries create "another
> surface for authority"; precedent: `chirality-app-dev` local pattern
> preferred over `chirality-piping`'s `execution/_DAG` aggregate);
> (4) candidate accepted, **all strata as presented**. The subsections
> below are preserved as the questions as asked.

1. **Landing instrument.** The clean instrument is a `D-PEC-62` packet
   naming exact paths/acts/verification/rollback for: the dependency
   register landing (recommended home `execution/_DAG/DAG-001/` in v3.1
   schema — outside the default writable fence), the `LOOP_RECEIPTS.md`
   receipt for this tranche, and (if desired now) scaffolding. Alternative:
   owner rules that the default `_Coordination/**` surface suffices for a
   coordination-plane register. PROJECT_SETUP does not resolve this
   contradiction itself (§2).
2. **Phase 1.3 maturity threshold** for blocker computation (recommended
   default `INITIALIZED`).
3. **Phase 1.3 register storage**: central v3.1 register (+
   deliverable-local `Dependencies.csv` materialized at scaffolding, which
   also serves SOW-015/SOW-064 self-ingest) vs deliverable-local only vs
   `_DEPENDENCIES.md`.
4. **Candidate content**: accept DECLARED+DERIVED as the accepted graph and
   rule on the 82 PROPOSAL edges (bulk or itemized); rule the flagged items
   (E-A11, E-P69, E-N02, C-02 direction, C-08 standing set, E-N13/E-N18).

Blocker computation remains inactive until folders exist (scaffolding
packet) and the threshold is ruled; no blocked/available reporting will be
made before then (no-false-precision invariant).

## 7. Erratum candidates for a future SCA (recorded, not actioned)

- `Deliverables.csv` DEL-09-06 "the other six views" vs DL-14's retyping of
  DEL-09-07 as non-UI (numeral/classification tension; drives E-A11).
- PhaseHint tensions: SOW-051's collision-risk input (P3) vs DEL-09-07
  (P2); DEL-09-05 (P3) vs DEL-06-04 (P4); C-02's P1-vs-P3 assertion
  obligation on DEL-04-03.
- OI-013 adjacency: this session again ran a session-local validator; the
  durable register validator remains an open follow-on.

## 8. Handoff state

- **Accepted upstream snapshot:** revision 1.1 via
  `execution/_ScopeChange/SCA-001_2026-07-24_2206/` (hashes §1).
- **Derivative-package status:** DAG candidate v0.2 — gate exhibit embedded
  here (frozen provenance); landed 2026-07-25 as 64 deliverable-local
  `Dependencies.csv` v3.1 registers under D-PEC-62.
- **Closure verdict:** TRANCHE EXECUTED 2026-07-25 — D-PEC-62 RULED as
  drafted and executed same session: 11 packages / 64 deliverables
  scaffolded `OPEN` (PREPARATION), 64 deliverable-local `Dependencies.csv`
  v3.1 + `_DEPENDENCIES.md` seeded (ephemeral Agent 2), all five packet
  verifications PASS (fileset 64/64; schema 64/64 VALID; closure analysis
  62 nodes / 120 edges / orphans 2 deliberate / SCCs 0; workspace 11/64/
  OPEN 64; basis hashes match §1). Evidence: `SEED_D-PEC-62/RUN_LOG.md`;
  Receipt 108. The exhibit in §4 is now **frozen gate provenance** — the
  deliverable-local registers are the sole live dependency basis.
- **Rerun requirements:** future regeneration traces to the accepted
  decomposition snapshot (rev 1.1 via SCA-001), not this exhibit; register
  refreshes go through `TASK + dependency-extract`.
- **Remaining blockers:** none for this tranche. Open next: Git closeout
  via CHANGE; per-tranche owner packets for the P1 build slice (F-PEC-1
  still fences source work); §7 erratum candidates await a future SCA.
