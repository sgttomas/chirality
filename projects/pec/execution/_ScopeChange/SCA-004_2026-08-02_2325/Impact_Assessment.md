---
amendment_id: SCA-004
doc_kind: scope_change.impact_assessment
decomp_variant: SOFTWARE
gate: 2
created: 2026-08-02
status: awaiting_gate_2_acceptance
---

# SCA-004 — Gate 2 Impact Assessment

## Impact verdict

SCA-004 is a bounded semantic and mapping amendment with no new entity,
deliverable, package, source behavior, execution dependency, lifecycle act, or
foreign-loop effect. It promotes one existing scope item (`SOW-077`) from
`TBD` to `IN`, maps it to the existing registry deliverable and objective,
and closes one open issue (`OI-003`) on the exact D-PEC-78 O-A authority.

The decomposition-local amendment is low structural risk. Its meaningful cost
is derivative currency: the successor will stale current-basis pins across the
64 scaffolded metadata/reference packets, require one new non-gating
requirement anchor for DEL-01-06, and make present-tense OI-003-open prose false
in four active ScopeOfWork contracts and the accepted SPEC.

Gate 2 is **not accepted** by this document.

## Evidence basis

| Evidence | SHA-256 / result |
|---|---|
| D-PEC-78 packet | `426dba045d63136937eec25af6e4842188ac402486f400391f1f30e1f33e5d17` |
| D-PEC-78 exact decision | `3f91ea6a18360d950f3cecce755ee929cdc78c53651d0b2774a3c93aa290a565` |
| Confirmed Gate 1 intake return | `071a0bfcde6a56fdf5634bf73f9b0c928c42627d6c5150251e42f20cfdf99f14` |
| SOFTWARE_DECOMP revision 1.3 | `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` |
| ScopeLedger.csv | `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5` |
| Deliverables.csv | `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40` |
| ContextBudgetQA.csv | `5c8d30994a99611b7023f8ac0995ee9a8efa0d2992f3c1a2683f4d2f9e8e2bef` |
| Fresh AUDIT_DECOMP snapshot | `execution/_Evaluation/DecompCoverage/COV_SCA004_PRECHANGE_2026-08-02_2327/`; 0 blockers, 1 non-blocking warning, 69 info |
| Strict register validator | 64 registers / 254 rows / 0 errors / 0 warnings |
| Dependency closure | 119 execution edges / 0 SCCs / 0 bidirectional pairs; two existing zero-edge nodes (`DEL-00-03`, `DEL-01-05`) |

The audit warning is unrelated to SCA-004: DEL-08-02 is `CHECKING`, while its
accepted source-tree schema/test bytes are not located inside the deliverable
folder scanned by artifact-presence Check 6. Structural coverage remains
11/11 packages, 64/64 deliverables and contexts, and 100% forward, reverse and
objective coverage.

## Impact summary by action

| Action | Decomposition structure | Variant-local metadata | Downstream consumers | Risk / invariant effect |
|---|---|---|---|---|
| A001 — SOW-077 | Move the existing row from the TBD view to IN; assign PKG-01, DEL-01-06 and OBJ-004; OpenIssue FALSE | PKG-01 and OBJ-004 summary views gain SOW-077 | DEL-01-06 contract, references and requirement anchors must gain the accepted scope item | Reciprocal mapping must land atomically with A003; status telemetry changes by one row |
| A002 — SOW-094 | Notes/DecisionRef only; lineage and statement preserved | No deliverable identity change | DEL-01-06 contract's “temporary/open” basis becomes false | Risk is semantic drift only; no new work product is implied |
| A003 — DEL-01-06 | CoversScopeItems becomes SOW-077;SOW-094; description loses OI-003-open posture | Exact DEL-01-06 `_CONTEXT.md` fields and provenance become affected | Existing port consumers remain isolated; their contracts need authority-prose review | Name/path/type/envelope/phase/artifacts/objective remain stable; no folder move or estimate-class change |
| A004 — OI-003 | Row retained and marked resolved; open/resolved telemetry changes | No lifecycle or source metadata change | SPEC and four contracts containing present-tense “undecided/open” statements become stale | Non-destructive closure preserves issue identity and history |
| A005 — traceability | Package/objective summaries, decision/revision history, accepted pointers and audit evidence require parity | All current-basis pointer packets become revision-stale after successor acceptance | Project/loop orientation maps require ordinary pointer refresh | No accepted pointer may move before Gate 5 owner authority |

## Expected decomposition-state delta

| Metric | Pre-change | Expected post-change | Explanation |
|---|---:|---:|---|
| Scope items | 94 | 94 | Stable ID and row count preserved |
| IN / OUT / TBD | 71 / 14 / 9 | 72 / 14 / 8 | SOW-077 only |
| Packages | 11 | 11 | No partition change |
| Deliverables | 64 | 64 | DEL-01-06 modified in place |
| Objectives | 6 | 6 | OBJ-004 mapping extended, not added |
| PKG-01 covered scope items | 7 | 8 | Add SOW-077 |
| DEL-01-06 covered scope items | 1 | 2 | SOW-094 → SOW-077;SOW-094 |
| OBJ-004 mapped scope items | 10 | 11 | Add SOW-077; mapped deliverable population unchanged |
| IN rows without package / deliverable | 0 / 0 | 0 / 0 | Same-amendment reciprocal assignment |
| IN rows without objective mapping | 11 | 11 | SOW-077 enters IN already mapped to OBJ-004 |
| Open / resolved issues | 11 / 2 | 10 / 3 | OI-003 only |
| Context Envelope counts | S 28 / M 34 / L 2 | unchanged | DEL-01-06 stays S |
| Execution dependency edges / SCCs | 119 / 0 | unchanged | Requirement anchor is non-execution metadata |

## Package-role and derivative-surface classification

| Surface | Package role | Classification | Expected state after amendment | Authority / required action |
|---|---|---|---|---|
| `execution/_Decomposition/SOFTWARE_DECOMP.md` | working surface / decomposition truth | `DIRECT_EDIT` | `CURRENT` after Gate 5 | Exact Gate 3 postimage only |
| `execution/_Decomposition/ScopeLedger.csv` | authoritative companion register | `DIRECT_EDIT` | `CURRENT` after Gate 5 | Replace only SOW-077 and SOW-094 rows within approved cells |
| `execution/_Decomposition/Deliverables.csv` | authoritative companion register | `DIRECT_EDIT` | `CURRENT` after Gate 5 | Replace only DEL-01-06 row within approved fields |
| `ContextBudgetQA.csv`, `Companion_Inventory.csv` | authoritative companion registers | `NO_CHANGE` | `CURRENT_UNCHANGED` | Prove byte identity; no envelope/package-role change |
| DEL-01-06 `_CONTEXT.md` | variant-local derived metadata | `DIRECT_EDIT` | `CURRENT` after approved propagation | CoversScopeItems, Description and successor provenance only; `_STATUS.md` remains frozen |
| Remaining 63 `_CONTEXT.md` files | derived metadata | `NO_CHANGE` in SCA direct pass | `STALE_REPIN_REQUIRED` | PROJECT_SETUP/approved pointer-parity pass; semantic fields unchanged |
| All 64 `_REFERENCES.md` files | derived reference packets | `NO_CHANGE` in SCA direct pass | `STALE_REPIN_REQUIRED` | PROJECT_SETUP re-pin to the accepted successor |
| DEL-01-06 `Dependencies.csv` | downstream structured dependency truth | `NO_CHANGE` in SCA direct pass | `STALE_ANCHOR_REFRESH_REQUIRED` | dependency-extract / PROJECT_SETUP adds one `ANCHOR/TRACES_TO_REQUIREMENT` row for SOW-077; execution graph unchanged |
| Other 63 dependency registers | downstream structured dependency truth | `NO_CHANGE` | `CURRENT_UNCHANGED` | Preserve 119 execution edges and every existing row |
| SCA-004 evidence and accepted decomposition/SCA pointers | snapshot / handoff artifacts | `RECOMPUTE` | Interim until Gate 5; current only after owner acceptance | Never move `_LATEST.md` at Gate 2 |
| DecompCoverage pre/post snapshots | derivative audit evidence | `RECOMPUTE` | Pre-change current for this gate; post-change required later | AUDIT_DECOMP owns the read-only evidence |
| Four affected ScopeOfWork contracts | derived production contracts | `NO_CHANGE` in SCA direct pass | `STALE_REVIEW_REQUIRED` | WORKING_ITEMS / contract owner; exact population below |
| DEL-00-03 accepted SPEC | accepted derivative artifact | `NO_CHANGE` in SCA direct pass | `STALE_REVIEW_REQUIRED` | DEL-00-03 owning workflow and artifact gate |
| PRD v2.2 | accepted upstream product definition | `NO_CHANGE` | `CURRENT_WITH_SUPPLEMENT` | §16.3 retains the question; D-PEC-78 supplies the accepted answer |
| `projects/pec/v2/**` | source / configuration | `NO_CHANGE` | `CURRENT_UNCHANGED` | D-PEC-78 confirms existing bytes; no source act needed or authorized |
| Lifecycle files | downstream control truth | `NO_CHANGE` | `CURRENT_UNCHANGED` | No transition or status annotation inferred |
| Decisions, receipts, prior SCA/audit/reconciliation snapshots | authority/history/evidence | `NO_CHANGE` | `HISTORICAL_CURRENT` | Never rewrite prior truth as though it had always reflected D-PEC-78 |
| Root/App/Piping/Bridge surfaces | foreign-loop truth | `NO_CHANGE` | `CURRENT_UNCHANGED` | O-A creates no declaration or receiving-loop duty |

## Derivative packages and owning reruns

| Package / exact population | Owner | State after accepted amendment | Required rerun / closure action |
|---|---|---|---|
| DEL-01-06 ScopeOfWork (`7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a`) | WORKING_ITEMS + owner artifact gates | `STALE_REBUILD_REQUIRED` | Add SOW-077 trace and replace CLM-003, REQ-005, CON-001 and related future-ruling prose while preserving port isolation; rerun deterministic checklist and exact-hash fitness gates |
| DEL-02-07 ScopeOfWork (`ddc837ca8b87ad8af52cfc4ec8b06c8fef883bbc3eeca9eea9949fb6280b007b`) | WORKING_ITEMS | `STALE_REVIEW_REQUIRED` | Replace the OI-003-undecided premise with settled upstream authority; preserve the in-process interface boundary |
| DEL-03-01 ScopeOfWork (`756c5f2af726272645a3cee491862cf3ca1fb751becad39f82ff310128d5ba19`) | WORKING_ITEMS | `STALE_REVIEW_REQUIRED` | Same; retain separate TBD-005 loop→project uncertainty and existing dependency edges |
| DEL-04-01 ScopeOfWork (`0c38bee95ca99d8a3f1da8155055f84e3c704865f23dc05be44338570d38e53f`) | WORKING_ITEMS | `STALE_REVIEW_REQUIRED` | Replace OI-003-open assertions without inventing a DEL-01-06 dependency edge |
| DEL-00-03 SPEC (`8b25a0d1f7ec7451ed3d19839904ee0c5f9a69b94df50f2122d9065c59a02315`) | DEL-00-03 owning workflow + REVIEW/owner fitness | `STALE_REVIEW_REQUIRED` | Change only the §8 statement that all OI-001..009 remain open; byte acceptance remains historical and does not accept a successor |
| 64 deliverable `_REFERENCES.md` packets | PROJECT_SETUP / reference owner | `STALE_REPIN_REQUIRED` | Re-pin accepted basis to the successor SCA-004 revision |
| 64 `_CONTEXT.md` provenance blocks | SCOPE_CHANGE for exact DEL-01-06 fields; PROJECT_SETUP/pointer owner for the other 63 | `1 DIRECT / 63 STALE_REPIN_REQUIRED` | Keep all semantic fields unchanged except DEL-01-06; update accepted-basis provenance under approved propagation |
| DEL-01-06 dependency anchor package | dependency-extract / PROJECT_SETUP | `STALE_ANCHOR_REFRESH_REQUIRED` | Add the SOW-077 requirement anchor, then rerun strict register validation and dependency closure; do not add an execution edge |
| README, STATUS, `_COORDINATION.md`, standing PEC workplan | HELP_HUMAN / owning loop-maintenance workflow | `STALE_POINTER_OR_MAP_NOTE` | Update only current-basis/current-open-decision statements under ordinary authority; do not rewrite historical entries |
| Historical run/review/reconciliation packages | their immutable evidence owners | `CURRENT_HISTORY` | No regeneration; later consumers cite them as pre-SCA-004 history |

All four affected deliverables are currently `INITIALIZED`. Their status files
were read together with sibling memory files when present; no sibling
`_MEMORY.md` or `MEMORY.md` exists for these four folders. No lifecycle effect
follows from derivative staleness.

## Orphan, invariant and telemetry risk

| Risk | Pre-change evidence | Post-change exposure | Required control |
|---|---|---|---|
| Package/deliverable orphan | 11/11 packages and 64/64 deliverables found; no reverse-only folder | `0` expected | Preserve PKG-01 and DEL-01-06 identity/path |
| Unassigned IN scope item | `0` | Would become 1 if A001 landed without its assignments | Apply SOW-077 status, package, deliverable and objective cells atomically |
| Non-reciprocal scope mapping | Strict register validator clean | Would become 1 if A003 omitted SOW-077 | Pair A001 with DEL-01-06 CoversScopeItems update |
| Missing requirement anchor | DEL-01-06 currently traces only SOW-094 | One derivative anchor gap after SOW-077 becomes IN | Record as open downstream work; add one non-execution anchor under owning workflow |
| Dependency cycle | 119 edges / 0 SCCs / 0 bidirectional pairs | None; no execution edge changes | Re-run closure after anchor refresh and confirm same graph |
| Analyzer zero-edge-node metric | DEL-00-03 and DEL-01-05 | Unchanged; neither is a structural orphan created here | Preserve as known non-blocking graph state |
| Package isolation | DEL-01-06 remains PKG-01 registry configuration/port/adapter slice | None | Preserve name/type/artifacts and the inward core port |
| Objective mapping | OBJ-004 has active support | Scope-side support increases by one; deliverable population unchanged | Update objective summary consistently |
| Telemetry drift | 71/14/9; 11 open/2 resolved | Exact deltas are 72/14/8 and 10 open/3 resolved | Recompute telemetry and verify all other counts byte/semantic parity |
| Supersession ambiguity | PRD §16.3 is an unanswered question | D-PEC-78 supplies detail without contradicting a prior fact | No Supersession_Delta expected; cite PRD + D-PEC-78 together |
| Professional reliance / cross-loop authority | None granted | None | Preserve D-PEC-78 non-effects and graceful absence |

## Estimate and schedule staleness

No estimate or schedule rerun is required by the amendment itself. DEL-01-06
retains its `S` Context Envelope, `LOW` QA risk, `P1` phase, package, type,
name, artifacts and three existing consumer edges. D-PEC-78 states that no
source change is required. The added SOW-077 mapping records the long-term
authority of the already-produced shape rather than a new implementation
slice.

If a later contract-currency review discovers new production work beyond the
ruled existing paths/port/schema, that is a new scope fact and must return
through SCOPE_CHANGE or an exact D-PEC source packet; it is not inferred here.

## Active snapshot and handoff impact

- `_Decomposition/_LATEST.md` remains revision 1.3 and
  `_ScopeChange/_LATEST.md` remains SCA-003 throughout Gates 2–4.
- `SCA-004_2026-08-02_2325/` is interim Gate 2 evidence, not accepted
  decomposition truth and not an active snapshot.
- A Gate 5 execution, if separately authorized, must produce the complete
  SCA-004 artifact set, post-change audit, successor hashes, derivative-state
  table and explicit closure verdict before either pointer moves.
- A scope-change-only close may leave downstream packages stale only if the
  final handoff records each exact owner and rerun obligation. It may not imply
  contract, SPEC, source, lifecycle, release or professional-reliance closure.

## Recommended downstream sequence after a later accepted Gate 5

1. Run final `AUDIT_DECOMP` against the exact successor and compare it with
   this pre-change baseline.
2. Re-pin all 64 `_REFERENCES.md` and all 64 `_CONTEXT.md` provenance blocks,
   with only DEL-01-06 receiving semantic context-field changes.
3. Refresh DEL-01-06's non-gating SOW-077 requirement anchor; rerun strict
   register validation and dependency closure.
4. Route the four exact ScopeOfWork contracts through WORKING_ITEMS contract
   currency and their ordinary review/fitness gates.
5. Route the accepted DEL-00-03 SPEC through its owning artifact-amendment and
   exact-byte acceptance gates.
6. Refresh current PEC orientation/map pointers under HELP_HUMAN; retain all
   historical receipts, decisions and snapshots unchanged.

No downstream rerun is authorized by Gate 2. This table records impact and
future ownership only.

## Gate 2 recommendation and owner question

**Recommendation:** accept this impact assessment as the bounded consequence
of the confirmed SCA-004 intake. The amendment remains MODIFY-only and should
advance next only to an exact Gate 3 diff preview; derivative repairs remain
frozen and separately owner-gated.

**Do you accept this impact assessment and authorize SCOPE_CHANGE to prepare
the exact SCA-004 Gate 3 amendment preview only?**

