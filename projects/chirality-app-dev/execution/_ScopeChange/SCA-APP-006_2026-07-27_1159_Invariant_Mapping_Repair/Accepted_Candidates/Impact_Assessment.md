# SCA-APP-006 Impact Assessment

**Gate:** 2

**Status:** `PREPARED_NOT_ACCEPTED`

**Date:** 2026-07-27

**Basis:** `4214915d9fcfecdc2952626421bf50b0e5f7845b`

## Decision requested

Gate 1 is confirmed. Gate 2 asks the owner to accept or amend the impact
envelope below. Acceptance would authorize preparation of the exact Gate-3
amendment only; it would not approve amendment text, companion-register rows,
propagation, application, contracts, repinning, APP-HOLD-1, implementation, or
Git closeout.

## Summary

SCA-APP-006 is a traceability and decomposition-package repair, including one
bounded decomposition-contract clarification. It adds one authoritative
companion register and reconciles seven supported relations between the
Deliverables view and Scope Ledger. It does not add, remove, rename,
reclassify, merge, split, or retire any package, deliverable, scope item, or
objective.

Expected topology after an accepted amendment remains:

- 78 scope items;
- 10 packages;
- 51 deliverables;
- 10 objectives; and
- all existing stable IDs, package membership, context envelopes, and
  lifecycle states preserved.

The new register will map App obligations and evidence to CONTRACT invariant
identity. It cannot transfer or reinterpret Root, Tier-0, PEC, project, or
other external semantic ownership.

## Action impact

| Action | Direct decomposition effect | Metadata effect if later approved | Downstream effect |
|---|---|---|---|
| A001 | Add the authorized invariant register as authoritative companion truth. | None outside `_Decomposition/`. | App ScopeOfWork population needs later concordance and repin against the accepted basis. |
| A002 | Clarify field-level precedence, package roles, and the planned-to-live register transition. | Candidate context rows may cite the accepted topology only; no external-owner semantics move. | Persistent validator/CI work, if wanted, routes separately to HELPS_HUMANS. |
| A003 | Add `DEL-02-03` to the `SOW-002` ledger assignment. | `DEL-02-03` context is already consistent; no direct context write is presently indicated. | Corresponding contract trace surfaces become stale until OD6 repair. |
| A004 | Expand `DEL-02-05` description, artifacts, and scope trace to truthfully carry `SOW-023`; retain `DEL-09-06`. | `DEL-02-05/_CONTEXT.md` requires exact parity if Gate 4 approves it. | Held/contract work remains separately governed. |
| A005–A006 | Add `SOW-064` to `DEL-06-02` and `DEL-06-03` with a non-overlapping obligation partition. | Both deliverable contexts require exact parity if Gate 4 approves them. | Contract traces become stale; remote MCP/marketplace scope remains excluded. |
| A007–A010 | Add supported reverse-view relations for `SOW-075` through `SOW-078`; OUT rows remain OUT. | Four deliverable contexts require exact parity if Gate 4 approves them. | Contract traces become stale; no scope activation occurs. |
| A011 | Replace stale `REF-006` hash with the accepted App PRD SHA-256. | None. | Any PRD identity change before Gate 3 blocks rather than being silently absorbed. |
| A012 | Add `DEC-022` and the SCA change-log entry after exact approval. | None. | Establishes the later accepted decision provenance; historical rows remain unchanged. |

## Package-role classification

| Surface | Package role | Gate-2 classification | Authority and treatment |
|---|---|---|---|
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | working surface | `DIRECT_EDIT_CANDIDATE` | App decomposition truth; exact Gate-3 diff required. |
| `execution/_Decomposition/contract_invariant_coverage_register.csv` | authoritative companion register | `DIRECT_ADD_CANDIDATE` | Explicitly authorized write surface; all 81 rows and enums require Gate-3 approval. |
| Seven named deliverable `_CONTEXT.md` files | variant-local metadata | `DIRECT_EDIT_CANDIDATE_AT_GATE_4` | Enumerated maximum propagation set; exact files and bytes require Gate-4 approval. `DEL-02-05` also carries four pre-existing stale PKG-02 package-description fields inside this candidate path. |
| This SCA snapshot and `_ScopeChange/_LATEST.md` | snapshot / handoff artifact | `DIRECT_EDIT_BY_SCA` | Records gate state; does not substitute for decomposition truth. |
| Pre/post AUDIT_DECOMP snapshots | derived evaluation package | `RECOMPUTE` | AUDIT_DECOMP owns immutable audit evidence and its pointer. |
| 53 App ScopeOfWork contracts and basis pins | downstream accepted contracts | `NO_DIRECT_EDIT_STALE_AFTER_ACCEPTANCE` | OD6 serialized population repair owns later concordance/repin. |
| Six APP-HOLD-1 targets and D-APP-75 surfaces | protective control | `NO_CHANGE` | Hold remains binding; this SCA neither releases nor overrides it. |
| `Dependencies.csv`, estimates, schedules | downstream project state | `NO_DIRECT_EDIT_REVIEW_AFTER_ACCEPTANCE` | No topology/lifecycle change; downstream owners determine whether their derived facts require refresh. |
| App PRD and CONTRACT | accepted upstream authority | `NO_CHANGE` | Used as source authority only. |
| Product/runtime implementation | implementation surface | `NO_CHANGE` | No implementation authority. |
| Persistent tools/CI validators | Root instruction/tooling surface | `NO_CHANGE` | Any persistent validator is separately governed HELPS_HUMANS work. |

## Structural and invariant risk

| Risk | Current assessment | Gate-3/5 control |
|---|---|---|
| Stable-ID collision | None found; `SCA-APP-006` and App-local `DEC-022` are available. | Rescan immediately before exact amendment and application. |
| Parent/child orphaning | None: no package or lineage action. | Prove 10/10 packages and 51/51 deliverables remain matched. |
| Unsupported relation deletion | Prohibited by the owner-selected M1-A route. | Deterministic before/after relation comparator must show zero deleted supported relations. |
| OUT-scope activation | Possible if `SOW-076`–`078` are described as executable scope rather than exclusions. | Exact rows must retain `OUT` and state boundary-only trace semantics. |
| `SOW-023` false trace | Current `DEL-02-05` prose is too narrow despite its ledger relation. | Exact description/artifacts/context must make the UI slice truthful; preserve `DEL-09-06` security responsibility. |
| `SOW-064` overlap | Both deliverables are ledgered but neither reverse-view row carries the relation. | Gate 3 must partition catalog/validation/collision work from in-process wrapper/extension-boundary work. |
| External-owner reassignment | High if register rows infer semantic ownership from App topology. | Closed owner/enforcement enums, explicit `UNKNOWN`, source anchors, and validator rejection of invented/unresolved owners. |
| Register incompleteness | Current main document covers only 41 of 48 invariant families narratively. | Register must contain exactly 81 unique IDs in all 48 families; missing/extra/duplicate IDs block. |
| Basis drift | `REF-006` is stale today. | Gate 3 freezes current PRD/CONTRACT/decomposition identities; any intervening change returns as a variance. |
| Context-envelope drift | `DEL-02-05` remains a focused UI slice only if exact attachment UI artifacts stay cohesive. | Gate 3 must demonstrate the expanded slice remains coherent at the existing envelope or return a variance; no silent envelope change. |
| Carried context drift | `DEL-02-05/_CONTEXT.md` has four stale PKG-02 package-description fields while its deliverable-level fields remain aligned. | If Gate 4 approves metadata parity, repair those four fields in the existing path together with A004; otherwise record them as an explicit downstream blocker. |

## Mapping reconciliation envelope

| Scope item | Required terminal relation |
|---|---|
| `SOW-002` | `DEL-02-03;DEL-07-01` |
| `SOW-023` | `DEL-02-05;DEL-09-06` |
| `SOW-064` | `DEL-06-02;DEL-06-03` |
| `SOW-075` | `DEL-01-01;DEL-07-01` |
| `SOW-076` | `DEL-01-04;DEL-04-02` while status remains `OUT` |
| `SOW-077` | `DEL-01-04;DEL-07-06` while status remains `OUT` |
| `SOW-078` | `DEL-01-04;DEL-09-04` while status remains `OUT` |

The terminal comparator must report zero unexplained differences between the
Deliverables reverse view and Scope Ledger for the accepted population.

## Downstream and derivative-package state

| Package/surface | Owner | Expected state after Gate-5 application | Required action |
|---|---|---|---|
| App decomposition working surface | SCOPE_CHANGE | `CURRENT` after owner-confirmed Gate 5 | Apply only exact Gate-3 text. |
| Invariant companion register | SCOPE_CHANGE | `CURRENT` after owner-confirmed Gate 5 | Create exactly approved rows and run SCA-local validator. |
| App deliverable contexts | SCOPE_CHANGE under Gate 4 | `CURRENT` only if exact parity edits are approved/applied | Update only accepted maximum set. |
| AUDIT_DECOMP evidence | AUDIT_DECOMP | `PRECHANGE_CURRENT`; post-change pending | Run full post-change audit and compare. |
| App ScopeOfWork contracts | OD6 App repair owner | `STALE_REPAIR_REQUIRED` after accepted SCA | Perform all-53 concordance and later one-time population repin under separate authority. |
| APP-HOLD-1 | App loop / D-APP-75 | `UNCHANGED_HELD` | No action in this SCA. |
| Dependencies/estimates/schedules | PROJECT_SETUP and downstream skills | `REVIEW_REQUIRED` | Confirm no refresh is needed or rerun after accepted topology/mapping state. |
| Persistent validation tooling | HELPS_HUMANS | `NOT_CREATED` | Propose separately only if SCA-local validation proves recurring need. |

## Estimate and schedule posture

The requested change does not alter package membership, deliverable count,
context envelope, lifecycle state, dependencies, estimates, or schedule
authority. The accepted mapping and artifact-description changes may affect
later contract and acceptance evidence, so downstream owners must explicitly
confirm current derived state or rerun it; SCOPE_CHANGE does not write those
surfaces.

## Audit and current limitations

The fresh all-scope pre-change AUDIT_DECOMP is immutable at
`execution/_Evaluation/DecompCoverage/COV_SCA_APP_006_PRECHANGE_2026-07-27_1201/`.
It reports `WARNINGS` with 0 blockers, 55 warnings, and 2 information
findings. It proves 10/10 package and 51/51 deliverable coverage, 51/51
contexts, 51/51 valid SOW contracts, 78 ledger rows, and 10/10 objective
coverage.

The independent deterministic rescan reproduced the 81-ID/48-family census,
zero duplicate topology identifiers, exactly seven mapping differences, every
candidate context path, and every A001–A012 target. It found only the carried
four-field `DEL-02-05` package-description drift described above. That drift
does not expand the path or topology envelope, but its exact disposition must
be included in Gate 4.

## Gate-2 boundary

If accepted, Gate 2 authorizes drafting the complete exact Gate-3 candidate:
the decomposition diff, all 81 register rows and closed enums, a runnable
SCA-local validator, the exact `DEL-02-05` and `SOW-064` obligation wording,
the full traceability comparator, `REF-006`, and `DEC-022`.

It does not approve any of those bytes. Gate 3 remains a separate explicit
owner gate.
