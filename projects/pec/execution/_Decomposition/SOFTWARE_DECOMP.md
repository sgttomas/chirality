---
doc_id: PEC-SOFTWARE-DECOMP
doc_kind: decomposition.software
package_role: working_surface
status: draft_gate1
revision: "0.1"
date: 2026-07-24
agent_persona: SOFTWARE_DECOMP
method_reference: agents/AGENT_SOFTWARE_DECOMP.md (conforms to docs/DECOMPOSITION_STANDARD.md)
session_authorization: D-PEC-60
source_corpus: projects/pec/docs/PRD.md (v2.0, adopted 2026-07-24, D-PEC-58)
---

# PEC v2 Coordination Plane — Software Development Decomposition

> **Package role: working surface.** This is the main decomposition document
> and the authoritative amendment surface for this package. Heavy
> machine-truth lives in the companion registers listed in §Companion
> Inventory once they exist (Phases 4–6). Any single-file render assembled
> from this package is a derived publication artifact.

## Gate Log

| Gate | Phase | State | Owner confirmation (verbatim) | Date |
|---|---|---|---|---|
| 1 | Intake | **PRESENTED** | — | 2026-07-24 |
| 2 | SSOW | not reached | — | — |
| 3 | Objectives | not reached | — | — |
| 4 | Packages | not reached | — | — |
| 5 | Deliverables | not reached | — | — |
| 6 | Coverage + Context Budget | not reached | — | — |
| 7 | Final acceptance | not reached | — | — |

---

## 1. Intake (Phase 1)

### 1.1 Project title

**PEC v2 — Chirality Coordination Plane** (greenfield build).

### 1.2 Intake summary

The work is a greenfield software build of the product defined by PRD v2.0:
a deterministic, rebuildable projection of governed file truth (**record
tier**) plus an ephemeral presence layer (**presence tier**), embodying loop
Step 0 (Discover) and the deterministic parts of Step 1 (gate review,
decision-slate presentation). It is consumed by harnesses on behalf of
agents and by the human owner through dashboards, and it must remain "the
coordination plane that doesn't need to exist": deletable at any moment
without blocking any governed act.

The scope to decompose comprises, per the PRD:

- **Reconciliation** (PEC-RCN-001..006): a one-command-rebuildable record
  tier ingesting `_STATUS.md`, decision registers/packets, receipts ledgers
  (per-loop grammar), `WORK_GRAPH.json`/`STATUS.json`/`RUNTIME_SUMMARY.json`,
  dependency registers, workplans/LOOP_INIT, and `_harness/adapter.yaml`
  manifests; incremental on Git delta; drift-classifying; never writing
  sources; permanently parity-diffable against the practitioner harness.
- **Orientation** (PEC-ORI-001..006): per-loop orientation serves and deltas
  since a caller SHA, scope-parameterized per the modes ladder, every claim
  cited, every response SHA-stamped, measurement limits stated explicitly.
- **Gate evaluation and decision slate** (PEC-GAT-001..004): deterministic,
  advisory, Explain-shaped evaluation of file/Git-reducible gate
  preconditions; a cross-loop decision slate that links to authored files
  and provides no ruling write path.
- **Presence** (PEC-PRS-001..007): harness-reported sessions, Git/worktree
  scanning (names and counts, never content), session×worktree×scope
  correlation, live parent→child hierarchy edges, TTL'd heartbeat-aged
  records, advisory-only overlap surfacing.
- **Streams and ingest** (PEC-STR-001..005): idempotent append-only event
  ingest; versioned event contracts (home is an open §16 placement
  decision); daemon SSE, hooks CLI, and optional cmux bridges; stream loss
  always recovered by reconciliation.
- **API** (PEC-API-001..005): local-only Unix-socket service, token-scoped;
  ≤100 ms p95 orientation reads; versioned additive schema; compact
  citation-bearing responses; SSE delta/presence subscription.
- **Dashboards** (PEC-DSH-001..007): overview per loop, lifecycle census,
  read-only link-only register views, the aggregated "waiting on you"
  slate, presence board, universal drill-down to cited sources,
  documented Explain-shaped pressure rules.
- **Service posture** (PEC-SVC-001..006): zero third-party runtime
  dependencies in the core; local single-owner, no egress; bounded rebuild;
  the standing kill test; gitignored store with ingest-enforced content
  minimalism; self-observable reconcile/ingest logging.
- **Validation obligations carried by the PRD** (§11–§12): the pre-P1
  Step-0 cost baseline measurement, the permanent harness parity diff, the
  standing kill test, and the P1–P4 exit tests. (P0 governance is complete
  and is not scope for this decomposition.)

**Anticipated build shape (for sizing, not yet a package proposal):** the
PRD's release strategy sequences P1 (one-loop reconciler + orientation
store + read-only API) → P2 (dashboards, five loops) → P3 (harness
integration: hooks CLI + daemon polling, presence registry, Git/worktree
scanner) → P4 (streams: SSE bridge, hooks push, live hierarchy, optional
cmux adapter). Per the method's anti-pattern rule, **phases will not become
packages**; packages will be work domains, and phase membership will be
carried as deliverable metadata/sequencing hints.

### 1.3 Hard constraints (identified at intake)

| # | Constraint | Source |
|---|---|---|
| C1 | Graceful absence: no governed act may require PEC; kill test is a standing release gate | PEC-K-01, PEC-SVC-004 |
| C2 | Files govern: record tier rebuildable by one command; store gitignored, safe to delete; output never citable as authority; rulings file-native | PEC-K-02, D-GOV-01, K-AUTH-1 |
| C3 | Harness-owned consumption; agents never call PEC by instruction | PEC-K-03 |
| C4 | Two trust tiers never blurred; presence facts never in record-tier citations | PEC-K-05, PEC-PRS-007 |
| C5 | Observation not participation: no dispatch, leases, arbitration, merge opinions; read-only over Git | PEC-K-06, D-GOV-20 |
| C6 | Content-minimal: paths, counts, SHAs, states, hashes — never file or diff content; enforced at ingest | PEC-K-10, PEC-SVC-005, D-T0-14/20 |
| C7 | Zero third-party runtime dependencies in the service core (workspace-internal contracts packages permitted) | PEC-SVC-001 (carries ADR-002) |
| C8 | Local-only, Unix socket default, token-scoped, no external egress; any loopback TCP listener is an open owner decision | PEC-API-001, PEC-SVC-002, §16.9 |
| C9 | Orientation reads ≤100 ms p95; full rebuild within a bound confirmed at P1; incremental reconcile within seconds | PEC-API-002, PEC-SVC-003 |
| C10 | Permanent parity-diff against the practitioner harness; PEC neither directs the harness nor opens its cache half | PEC-RCN-005, PRD §15 |
| C11 | Frozen reference corpus: old PEC read/cite only; machinery carries as cited patterns, never as code | PRD §7.3/§13, D-PEC-58 |
| C12 | The nine §16 open owner decisions are not resolved by this decomposition; where one materially affects architecture the affected work is fenced or flagged, never guessed | PRD §16, standing plan |
| C13 | No second execution loop; daemon owns sessions, delegation, turn locks | D-GOV-20, D-PEC-56 (surviving behaviors 4/7) |
| C14 | Every implementation tranche needs its own owner-ruled packet; this decomposition authorizes no implementation write | standing plan step 3, D-PEC-60 |

### 1.4 Intake postures (for Gate 1 confirmation)

1. **Requirement source = PRD v2.0 alone.** The 46 PEC-\*-NNN requirements,
   11 PEC-K invariants, §3 outcomes, §11 metrics/falsification clause, §5
   modes ladder, and §12 exit tests are the scope-item source. Governance
   instruments (workplan, fences, D-GOV/D-T0 rulings) enter as constraints,
   not scope; the frozen corpus enters as reference, not scope.
2. **Phases are not packages.** P1–P4 membership is deliverable metadata.
3. **§16 open decisions** enter the SSOW as `TBD` items with open issues
   attached, so their eventual rulings amend the decomposition through the
   scope-change machinery instead of being silently pre-decided.
4. **Validation work is in scope** (kill test, parity diff, Step-0 cost
   baseline, seeded-conflict tests) because the PRD binds releases to it.
5. **Vocabulary collision handled at Gate 2:** decomposition IDs (`PKG-XX`,
   `DEL-XX-YY`) will coexist in this repo with the retired product's own
   `*-PKG-*` tokens (`26020-PKG-001` demo data, `PEC-PKG-009` v1
   requirement IDs). The Vocabulary Map will disambiguate; prose in this
   package will say "work-domain package" where ambiguity is possible.

### 1.5 References

| Ref | Path | Role |
|---|---|---|
| R1 | `projects/pec/docs/PRD.md` (v2.0, adopted 2026-07-24, `D-PEC-58`) | Source corpus |
| R2 | `docs/DECOMPOSITION_STANDARD.md` | Ratified 7-gate protocol |
| R3 | `agents/AGENT_SOFTWARE_DECOMP.md` | Conforming method (software variant) |
| R4 | `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md` | Standing plan; D1 authorization context |
| R5 | `projects/pec/AGENTS.md` | Project agent posture, fences, write scopes |
| R6 | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-57..60` | Pivot, adoption, follow-ons, session packets |
| R7 | `tools/practitioner_harness/README.md` | Permanent parity peer |
| R8 | `projects/pec/{core,server,web,agent-sidecar,tools}` | Frozen reference corpus (cite-only) |
| R9 | Root `AGENTS.md`; `docs/SOFTWARE_WORKFLOW_PROFILE.md` | Runtime doctrine; downstream execution profile |

---

## 2. SSOW (Phase 2) — not started

## 3. Objectives (Phase 3) — not started

## 4. Packages (Phase 4) — not started

## 5. Deliverables (Phase 5) — not started

## 6. Scope Ledger — not started (will be authoritative in `ScopeLedger.csv`)

## 7. Coverage & Telemetry (Phase 6) — not started

## 8. Context Budget QA — not started (will be authoritative in `ContextBudgetQA.csv`)

## 9. Vocabulary Map — not started (seeded at Phase 2)

## 10. Open Issues — none yet

## 11. Decision Log

| # | Date | Decision | Rationale |
|---|---|---|---|
| DL-1 | 2026-07-24 | Package layout: main surface + co-located CSV companion registers + `Companion_Inventory.csv` + `_LATEST.md`, all inside `execution/_Decomposition/` | Matches `docs/DECOMPOSITION_STANDARD.md` package architecture and the review skill's read boundary; avoids the piping split (`docs/_Registers/`) and the app-dev monolith |
| DL-2 | 2026-07-24 | Main doc filename is bare `SOFTWARE_DECOMP.md`; revision lives in front matter | The app-dev versioned filename caused ~40 downstream path references to a mutable name |
| DL-3 | 2026-07-24 | Release phases P1–P4 are recorded as deliverable metadata, never as packages | `AGENT_SOFTWARE_DECOMP.md` anti-pattern: packages are work domains, not phases |

## Companion Inventory

| Filename | PackageRole | Status | Description |
|---|---|---|---|
| `SOFTWARE_DECOMP.md` | working surface | live (this file) | Main decomposition document; amendment surface |
| `_LATEST.md` | snapshot / handoff artifact | live | Revision pointer; kept current on every revision bump |
| `ScopeLedger.csv` | authoritative companion register | planned (Phase 4) | SOW→PKG→DEL→OBJ row-level ledger |
| `Deliverables.csv` | authoritative companion register | planned (Phase 5) | Deliverable register incl. Context Envelope |
| `ContextBudgetQA.csv` | authoritative companion register | planned (Phase 6) | Per-deliverable envelope/risk/action QA |
| `Companion_Inventory.csv` | authoritative companion register | planned (Phase 7) | Machine-readable mirror of this table at publication |
