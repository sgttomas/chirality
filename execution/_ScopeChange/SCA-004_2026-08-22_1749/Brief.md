---
amendment_id: SCA-004
doc_kind: scope_change.brief
decomp_variant: SOFTWARE
gate: 1
created: 2026-08-22
status: AWAITING_OWNER_ACCEPTANCE
accepted_basis: main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776
requested_by: Ryan Tufts through HELP_HUMAN
allow_renumbering: false
---

# SCA-004 — v3 release-pathway Root carrier intake

## Posture

This immutable Gate-1 assessment parses the owner-directed Root half of the
Chirality App v3 release pathway. It is an assessment package only. It does
not amend decomposition truth, any companion register, the Root four-doc
contract set, a deliverable lifecycle, `DEL-02-06`, runtime code, a project
loop, Task Management, or `execution/_ScopeChange/_LATEST.md`.

Status is `AWAITING_OWNER_ACCEPTANCE`. Gates 2–5 are not open. Every one of
the ten accepted DEL-02-06 `HELD_UNAVAILABLE` bindings remains held.

## Exact human-initiated request

The owner directed SCOPE_CHANGE to assess and carry a refreshed
objective-relative release-pathway graph for the Root-side changes described
in:

1. `plans/steers/chirality_app_v3_phase0_steer_root_2026-08-22.md`;
2. `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`, SHA-256
   `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b`;
3. Revision 3.1,
   `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`,
   SHA-256
   `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`,
   as non-governing planning input only.

The G0 record controls where it is marked `AMENDS PLAN`. In particular:

- A3 always offers Codex Agent 0/1/2 role entry and labels explicit Agent
  2/TASK evidence `instruction-asserted` when non-delegation is not
  mechanically enforced;
- A4 replaces fresh-thread-only recovery with terminalization followed by
  `thread/resume` under canonical-root, account-identity, and policy-digest
  continuity, otherwise a fresh thread, with no in-flight re-attach claim;
- A7 replaces managed-network denial with three consented per-root command
  network postures and routed `networkApprovalContext` prompts carrying the
  destination-grouping caveat;
- B2 routes the physical-bundling question to G-HELPER;
- B4 keeps Pi and Electron pin drift outside SCA-004 as G1 blockers.

## Resolved runtime variables

| Field | Resolved value |
|---|---|
| `DECOMP_VARIANT` | `SOFTWARE` |
| `CONTEXT_ROOT` | `execution/` |
| `DECOMPOSITION_PATH` | `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` |
| `SCOPE_CHANGE_ROOT` | `execution/_ScopeChange/` |
| `AMENDMENT_ID` | `SCA-004` — owner-assigned; SCA-003 is a closed zero-action intake and `_LATEST.md` identifies applied SCA-002 |
| `ALLOW_RENUMBERING` | `false` |
| Allowed writes at this gate | this SCA-004 snapshot plus the one Root-to-App coordination notice |

## Accepted upstream state

| Surface | State / identity | Package role |
|---|---|---|
| Root SOFTWARE decomposition | revision 1.2 accepted current basis; SHA-256 `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` | working surface |
| Deliverable register | SHA-256 `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395` | authoritative companion register |
| Scope ledger | SHA-256 `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2` | authoritative companion register |
| Latest applied SCA | SCA-002 through `_LATEST.md` SHA-256 `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` | snapshot / pointer state |
| SCA-003 | `CLOSED_ZERO_ACTION_NO_DECOMPOSITION_CHANGE`; not the latest applied amendment | historical snapshot |
| DEL-02-06 Scope of Work | SHA-256 `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146` | deliverable-local accepted contract |
| DEL-02-06 compatibility bytes | `root-runtime-1`, epoch `1`, candidate SHA-256 `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`; ten bindings held | accepted derivative compatibility package |

## Semantic section binding

Resolved by heading text, not section number:

| Semantic section | Bound heading / authoritative surface |
|---|---|
| Change Register | `Decision Log / Change Log` |
| Unit Ledger | `Scope Ledger`; `chirality_root_scope_ledger_v1_0.csv` |
| Objectives | `Objectives`; `chirality_root_objective_register_v1_0.csv` |
| Primary Partitions | `Packages` |
| Secondary Entities | `Deliverables`; `chirality_root_deliverable_register_v1_0.csv` |
| Coverage Basis | `Coverage and Telemetry` plus forward/reverse registers |

## Gate-1 action parse

The request fits existing accepted Root scope. `SOW-104` already owns
consequential generic-runtime stewardship and the standing integration
carrier; `SOW-041` and `SOW-053` already own loop-receipt and snapshot/receipt
discipline. No PRD amendment or new scope item is inferred.

The smallest decomposition-level candidate is:

1. keep `DEL-02-06` as the standing semantic integration and release-assurance
   carrier, but modify its decomposition allocation so implementation breadth
   is split before activation;
2. add six bounded PKG-02 deliverables for process supervisor/control,
   supply/protocol, account/consent, adapter/event/API-v2, terminal
   reconciliation, and conformance;
3. add one bounded PKG-04 test-suite deliverable for a deterministic Root loop
   receipt validator, preserving `DEL-04-05` as the loop/receipt doctrine
   carrier and `DEL-05-02` as its evidence-discipline crosscheck.

Candidate IDs `DEL-02-07` through `DEL-02-12` and `DEL-04-11` are
collision-free at this basis. They are reserved only as Gate-1 proposals;
owner acceptance does not create folders, SOWs, mappings, or implementation
authority. Exact names, rows, and Context Envelopes must be previewed at later
gates before any decomposition edit.

See `Parsed_Actions.csv` and `Gate_1_Validation.md`.

## Pre-change SOFTWARE coverage baseline

The mandatory fresh Gate-1 `AUDIT_DECOMP` baseline is recorded at
`Evidence/AUDIT_DECOMP/coverage_summary.json`, SHA-256
`2210e77f989f29c11e005d7fe89944e2e0f0fe265e0a514f53042aaa89de9e45`.
It is scoped to the affected live carriers `DEL-02-06`, `DEL-04-05`, and
`DEL-05-02`; proposed additions are not yet live decomposition entities.

| Baseline metric | Result |
|---|---:|
| Scoped packages found | 3/3 (100.0%) |
| Scoped deliverables found | 3/3 (100.0%) |
| Reverse folder coverage | 3/3 (100.0%) |
| Context fidelity | 3/3 (100.0%) |
| Relevant objectives with scoped live support | 5/5 (100.0%) |
| Scoped IN-ledger rows without objective mapping | 0/5 |
| Lifecycle distribution | `INITIALIZED`: 3 |
| Anticipated production artifacts present | 0/11 (0.0%) |
| Findings | 0 BLOCKER; 0 WARNING; 11 INFO |
| Audit result | `OK`; closure readiness `PASS` for decomposition/filesystem coverage only |

The eleven informational findings are expected pre-production telemetry: the
three valid `SOW_V1` carriers remain `INITIALIZED`, so their anticipated
production outputs are not yet materialized. The audit changes no truth,
interprets no owner decision, and grants no Gate-2 authority.

## Gate-1 question

Does the owner accept this intake and impact boundary: preserve DEL-02-06 as
the standing integration carrier; open Gate 2 on six bounded PKG-02 carrier
additions plus one bounded PKG-04 Root receipt-validator carrier; keep all ten
bindings held; and treat App coordination only as reciprocal notices under
SCA-APP-008?

Until that answer is recorded against this exact package, Gate 2 is closed.
