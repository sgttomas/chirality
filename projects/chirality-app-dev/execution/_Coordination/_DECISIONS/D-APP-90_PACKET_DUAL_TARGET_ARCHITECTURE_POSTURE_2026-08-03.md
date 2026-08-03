# D-APP-90 — Dual-Target Architecture Posture and Next Gate

**Status:** `PROPOSAL — AWAITING_RULING — NO OPTION SELECTED`

**Prepared:** 2026-08-03 by `HELPS_HUMANS`, managed by App `HELP_HUMAN`

**Predecessor:** D-APP-87 Option B ruling SHA-256
`d13543f7164a688cd6ee5472455564e76eeba5f30acc1c157beb87017a82f0fe`

## 1. Decision requested

Given the adopted two-target requirement and domain-first delivery emphasis,
which architecture posture should govern the next App product-basis work?

This gate may select a planning baseline or authorize a bounded comparative
proof. It does not implement a target, amend the PRD/decomposition, or select
generic runtime semantics.

## 2. Fixed requirements and open hypothesis

D-APP-87 fixed all of the following:

- standalone Chirality Desktop remains a target;
- a per-domain control-plane application is a second target; and
- domain applications are the primary delivery vehicle for agents.

It deliberately did **not** decide whether these targets should use one
lightly skinned codebase, a shared core with target-specific shells, or another
form. This packet preserves that distinction.

## 3. Re-plan evidence

The derivative re-plan is frozen at:

`execution/_Coordination/AgentRuns/APPDEV_DAPP87_DUAL_TARGET_REPLAN_2026-08-03/`

It inventories the current PRD, accepted decomposition/SCOPE_CHANGE state,
live Remaining items, one Next/Electron workspace and one current packaging
identity, Woven Dialogue topology, D-APP-36 UI evidence bar, D-APP-89 direct
Root-contract migration evidence, D-APP-88 R2 blocked/rollback evidence, and
the current Root response.

Key findings:

1. The current source is structurally closest to one shared application, but
   it has no ruled product-skin schema, target-specific shell packages, or
   two-artifact packaging identity.
2. The closed domain-profile registry is a domain-runtime boundary, not a
   product-skin/configuration system.
3. Woven Dialogue and its authority/projection/accessibility invariants should
   be common unless a later App product requirement expressly varies them.
4. The exact first-domain typed-agent, structured-information, workflow, and
   decision-gate mapping is not yet an App-owned product requirement.
5. D-APP-88 proves a separate Electron target can be constructed, but the
   helper candidate was rolled back and remains blocked; it is not domain
   packaging authority.
6. D-APP-89's validated migration is compatible with each option but neither
   chooses architecture nor settles facade retirement.

## 4. Options and tradeoffs

### Option A — One lightly skinned application graph

Use one Next/Electron application and shared Woven shell. A ruled product
profile selects target copy, resources, initial navigation, typed-agent views,
structured-information views, workflows, and decision-gate presentation.
Target-specific package outputs are build configurations over the same graph.

Tradeoff: shortest domain-first path and closest current-topology fit, but the
highest risk of conditional spread, target leakage, and a future implicit
plugin architecture.

Effect of ruling: selects A as the planning baseline and authorizes preparation
of the exact first-domain requirements, PRD, SCOPE_CHANGE, and packaging-
identity packets. It authorizes no source or live product change.

### Option B — Shared core with target-specific shells

Plan internal shared UI/client packages with separately composed standalone
and domain shell entry points and packaging manifests.

Tradeoff: strongest target isolation and multi-domain scaling, but highest
up-front extraction, duplicate-composition, build-matrix, and scope-amendment
cost before the first-domain delta is frozen.

Effect of ruling: selects B as the planning baseline and authorizes preparation
of the same later owner packets, including explicit package/shell topology
impact. It authorizes no extraction or source change.

### Option C — Build-time product profiles over a shared shell

Plan a versioned declarative product manifest and bounded target adapters/slots
that emit distinct immutable standalone and domain artifacts from one shared
Woven shell. No runtime skin switching; no independently composed full shell.

Tradeoff: explicit target identity/config/resource boundaries without a full
shell fork, but the manifest/slot schema becomes a product contract and can
hide shell divergence if adapter imports are not strictly bounded.

Effect of ruling: selects C as the planning baseline and authorizes preparation
of the same later owner packets, including manifest/slot and graduation-to-B
criteria. It authorizes no manifest implementation or build change.

### Option D — Authorize a bounded comparative architecture proof before selection (recommended)

Keep A/B/C open and authorize a run-local, non-product proof that returns:

- exact first-domain UI delta inventory from reciprocally cited Piping inputs;
- A/B/C source/package dependency maps over the current tree;
- candidate product-profile/slot schemas for A and C and a shared-core/shell
  extraction map for B;
- target leakage, duplicate composition, build-matrix, and migration-cost
  measurements;
- two-artifact identity/resource/data-coexistence design examples; and
- elimination criteria plus a new owner packet selecting A, B, or C.

The proof may use frozen manifests, mock dependency graphs, and scratch/run-
local prototypes only. It cannot edit product source, PRD, decomposition,
deliverables, Root/Piping/PEC surfaces, or define generic runtime semantics.

Tradeoff: adds one owner gate and some planning latency, but converts the most
important unknowns into comparable evidence without prematurely freezing a
package architecture.

### Option E — Defer

Keep D-APP-87's adopted requirements but open no next work until the owner
names a trigger.

Tradeoff: preserves latitude but leaves domain-first delivery without an App
architecture path.

## 5. Six-lane re-plan summary

| Lane | Proposed handling after this gate |
|---|---|
| UI | Preserve Woven/authority/accessibility invariants; freeze the first-domain typed-agent/info/workflow/gate map; then bind target slots/shell composition. |
| Packaging | Produce two distinguishable unsigned local artifacts with explicit identity/config/resource/data boundaries; no signing/publication commitment. |
| Runtime client | Specify only App client needs and target-indexed conformance; generic contract, sandbox, identity, version, resume, and Bash remain `BLOCKED_BY_ROOT`. |
| Deliverables | Candidate direct review: `DEL-01-01`, `DEL-01-03`, `DEL-02-01`, `DEL-02-02`, `DEL-02-04`, `DEL-08-02`, `DEL-08-03`, `DEL-09-04`, `DEL-09-05`; conditional review for runtime/client/validation/domain-boundary siblings; no topology addition adopted. |
| Validation | Common checks plus separate standalone/domain source, component, visual, accessibility, build, package, runtime-client, and data/session evidence. One target cannot prove the other. |
| Later decisions | first-domain UI contract, PRD, SCOPE_CHANGE, packaging identity, Root generic contract, App adoption, vertical slice, retirement/helper residuals, release, and cross-loop adoption remain separate gates. |

## 6. Root block and separate residuals

Generic runtime, sandbox, identity, version, resume, and Bash remain
`BLOCKED_BY_ROOT` while Root `TM-ROOT-105`, `TM-ROOT-107`, and `TM-ROOT-109`
and their Piping-response prerequisites remain unresolved. No option grants
Agent-2 Bash or chooses a generic contract.

D-APP-88 helper identity/graceful stop and D-APP-89 facade retirement remain
separate gates. Selecting architecture neither closes nor bypasses either.

## 7. Validation and non-effects

The re-plan requires an independent adversarial authority/boundary review,
source/path/hash checks, next-ID uniqueness, reference integrity,
`git diff --check`, applicable receipt/corpus/self-check evidence, and
preservation checks for existing planning/D-APP-88 route artifacts and the six
D-APP-81 `HISTORICAL_RELATION_UNKNOWN` relations.

No option in this packet directly edits PRD, decomposition, SCOPE_CHANGE,
deliverables/status, source/frontend/runtime, Task Management, receipt, corpus,
completion log, Root/Piping/PEC, or Git. No option creates release,
publication, distribution, lifecycle, provider/network, solver-truth,
professional-reliance, or generic-runtime authority.

## 8. Non-binding recommendation

Select **Option D**. Current evidence distinguishes the tradeoffs but does not
yet contain the exact first-domain UI delta or enough package/build measures to
justify choosing A, B, or C. Option D preserves domain-first momentum and
returns a selection-ready packet without preselecting architecture.

## 9. Owner return tokens

- `APPROVE D-APP-90 OPTION A — ONE LIGHTLY SKINNED APPLICATION GRAPH`
- `APPROVE D-APP-90 OPTION B — SHARED CORE WITH TARGET-SPECIFIC SHELLS`
- `APPROVE D-APP-90 OPTION C — BUILD-TIME PRODUCT PROFILES OVER A SHARED SHELL`
- `APPROVE D-APP-90 OPTION D — BOUNDED COMPARATIVE ARCHITECTURE PROOF`
- `APPROVE D-APP-90 OPTION E — DEFER; TRIGGER: <exact trigger>`
