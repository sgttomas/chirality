# Tandem Review — Common Sealed Brief (Pass 1, Independent)

Status: sealed common brief, identical for Reviewer A and Reviewer B.
Prepared: 2026-07-26 by the EVALUATION-role supervising manager.
This brief is non-governing review procedure. It creates no product authority.

## 1. Review identity and frozen basis

- Review: Chirality Program architecture review under the Tandem Review Charter.
- Stage: Pass 1 — independent review. No reciprocal challenge occurs in this stage.
- Review freeze commit (governs all product bytes):
  `da31c19b5656dd74615e308c4215688971d33dc9`
- Product-basis commit: `aeadf5304435e1a4d8b4a26306da9ad4d4519eb6`
  (verified: only the charter file changed between product-basis and freeze).
- Working copy: `/Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76`
  — its HEAD is exactly the freeze commit and its tracked tree is clean, so you may
  read product files directly with file tools. The only untracked additions are the
  review workspace under `plans/reviews/tandem_2026-07-26/`. If you ever doubt a
  file's currency, resolve it through
  `git show da31c19b5656dd74615e308c4215688971d33dc9:<path>` — the frozen commit governs.
- Frozen corpus manifest (374 hashed files):
  `plans/reviews/tandem_2026-07-26/REVIEW_MANIFEST.json`
  SHA-256 `8ac8abb86f064a2a1ef5c51c4eacbbf7b90497d78d1f7a92b55406a44a27096c`
- Charter (non-governing reviewer guidance / challenge material only):
  `plans/chirality_program_architecture_and_tandem_review_2026-07-25.html`
  SHA-256 `1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f`

## 2. Boundaries (hard rules)

1. Read-only over the repository. You must not modify the primary checkout at
   `/Users/ryan/dev/chirality`, any product file, or any governed surface. The ONLY
   file you may write is your own report file named in your reviewer-specific brief.
2. Independence. You must not read, list, or search:
   - `plans/reviews/tandem_2026-07-26/reports/` (except writing your own report),
   - the other reviewer's brief file.
   You have no knowledge of the other reviewer's reasoning and must not attempt to obtain any.
3. Orientation order (charter §05): FIRST orient from the governed records themselves
   and form your own account; ONLY THEN read the charter and use it as a challenge set.
   Record your orientation account in the report before charter-derived material.
4. The charter is never evidence. Where the charter and governed records differ, the
   governed record controls and the difference is itself review evidence.
5. A review may expose a candidate requirement; it cannot create one. Never propose
   introducing new commitments through decomposition or SOW prose.
6. You may run read-only commands (git show/log/grep, shasum, python for parsing CSVs).
   Never run anything that writes to the repository outside your report file.

## 3. Scope

Both reviewers assess ALL of: Chirality Root, Chirality App, and PEC, on BOTH axes:

- **Depth**: intent → PRD → decomposition → registers → deliverable → ScopeOfWork
  traceability; authority and acceptance provenance; fitness of each layer.
- **Breadth**: boundaries, ownership, integration, optionality, runtime composition,
  coordination, downstream effects, and program coherence.

Your assigned lens (in your reviewer-specific brief) determines emphasis, not
exclusive jurisdiction.

## 4. Common frozen-basis description

The following is the shared statement of the review corpus, its identity, disclosed
conditions, and exclusions. Treat it as the common basis description; verify against
the repository wherever you rely on it.

### Status and identity

- Corpus frozen at `da31c19b5656dd74615e308c4215688971d33dc9`; product inventory
  established at `aeadf5304435e1a4d8b4a26306da9ad4d4519eb6`; product files unchanged
  between them.
- Mutable pointers are navigation aids, not independent authority.
- Candidate documents, proposals, historical snapshots, run evidence, and plans are
  not accepted basis unless a governing instrument expressly gives them that status.
- The charter is non-governing reviewer guidance. Its architectural propositions are
  questions to test, not facts to presume.

### Cross-product control surfaces

- Tier-0 decision register: `_DomainEngines/_DECISIONS/_REGISTER.md` (23 D-T0 decisions).
- Particularly relevant: D-T0-01 (framework-root contract precedence), D-T0-07
  (Tier-0 ownership of contract versioning), D-T0-09 (flow-a.contract.v0.1.0),
  D-T0-15 (PEC fences F-PEC-1..F-PEC-4), D-T0-19 (PEC/App bridge lane and cross-loop
  D-APP minting grant), D-T0-23 (shared-runtime convergence; App and PEC as distinct clients).

### Consulted-only context

- Domain packs are consulted-only context (not additional reviewed products), but
  their pins, notices, and drift may reveal effects of Root/App/PEC architecture:
  `domains/chirality`, `domains/chirality-app-dev`, `domains/chirality-piping`,
  `domains/piping-design`.
- Chirality Piping is a situated-product exemplar and a test of notice and
  inheritance coverage — not a fourth reviewed product.
- SOLVER Engine may illuminate historical lineage but is not governing evidence.
- Resource governance is candidate program architecture described only by the
  charter. It is optional, as PEC is optional. It may consume accepted system
  information to provide estimates, sequencing, locks or freezes, budgets, usage,
  cost, and forecast monitoring. It is NOT accepted Root/App/PEC scope, a source of
  authority, a system of record, or a correctness dependency.
- App UI/API semantic-parity work is owner-directed future work not yet established
  through a repository instrument. It is not accepted basis.

### 4.1 Chirality Root

Accepted PRD:
- `docs/PRD_ROOT.md`, Revision 5, SHA-256 prefix `82f7ea2944e7`, adopted by D-GOV-22
  on 2026-07-25. Exact adopted candidate bytes preserved at
  `execution/_Coordination/PRD_CANDIDATE_2026-07-25_root_product.md`;
  `docs/PRD_ROOT.md` is a pointer block plus the adopted candidate.
- D-GOV-26 and D-GOV-27 supersede PRD §5.2 O-1's six-member instruction-surface
  enumeration. Authoritative enumeration: `docs/SPEC.md` §0.2.1, eight members
  including CLAUDE.md and `.github/workflows/`. The PRD body alone therefore contains
  deliberately superseded wording; follow the pointer and governing instruments.

Root authority chain:
- `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`.
- Relevant invariants: K-AUTH-1, K-AUTH-2, K-WRITE-2, K-AGENTS-1, K-DOMAIN-1..K-DOMAIN-4.
- DIRECTIVE §1's earlier genus statement was superseded through D-GOV-23.

Accepted decomposition:
- `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`, v1.0, SHA-256
  prefix `14067a7d97c9`, accepted by D-GOV-25.
- Headline counts: 6 packages, 45 deliverables, 103 scope items, 7 objectives.
- Registers: `chirality_root_scope_ledger_v1_0.csv`,
  `chirality_root_deliverable_register_v1_0.csv`,
  `chirality_root_objective_register_v1_0.csv`,
  `chirality_root_prd_coverage_forward_v1_0.csv`,
  `chirality_root_trace_reverse_v1_0.csv` (same directory).
- The accepted candidate was augmented by accepted D-GOV-25 dispositions and D-GOV-27
  objective/responsibility propagation without changing package/deliverable/scope-item/
  objective counts.
- SHA roles: `ec62af070…` = AcceptedCandidateSHA; `ea0ad7a56…` = CandidateMergeSHA;
  `653fabc9b…` = D-GOV-25 EffectiveSHA and the SOW basis; `31b8dc94a…` = D-GOV-26
  EffectiveSHA and work-graph accepted basis. The decomposition header itself calls
  `ea0ad7a56…` "EffectiveSHA," conflicting with the accepting decision's more precise
  role assignment.

Root scopes of work:
- 45 live `ScopeOfWork.md` files under `execution/PKG-01_*` … `execution/PKG-06_*`;
  all INITIALIZED; all pin decomposition basis `653fabc9b3e8…`; contracts accepted
  through the owner's merge of PR #354.
- AC-*/VER-* statements remain CANDIDATE within all 45 contracts, expressed through
  varied prose rather than one deterministic metadata field.
- Governing standard: `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`.

Root decisions and current state:
- Register: `docs/governance_harness/_DECISIONS/_REGISTER.md`; highest decision D-GOV-27.
- Particularly relevant: D-GOV-09 (authority chain ratification), D-GOV-14 (standards),
  D-GOV-16 (ScopeOfWork standard), D-GOV-20 (Root-owned shared runtime and per-user
  daemon), D-GOV-21 (working-root exception), D-GOV-22 (PRD adoption), D-GOV-23/24
  (genus supersession/propagation), D-GOV-25 (decomposition acceptance), D-GOV-26
  (owner-gated closeout), D-GOV-27 (initialization and closing rulings).
- D-GOV-27 still contains an unbackfilled EffectiveSHA placeholder; Receipt 52 records
  this debt.
- Navigation: `execution/_Coordination/LOOP_INIT.md` → `CURRENT_WORKPLAN.md` →
  `WORKPLAN_2026-07-25_root_initialization.md` → `LOOP_RECEIPTS.md`. Receipt 52 acts
  as the current initialization handoff. The named current workplan is marked ACTIVE
  even though its goal is complete and no successor has opened.
- Root guard state under `execution/_harness/`: G1–G4 passing; all work-graph nodes pending.

Root integration and drift surfaces:
- Runtime doctrine and agent index: `AGENTS.md`; generic runtime charter `runtime/README.md`.
- Standards: `docs/WORKFLOW_COMPONENT_STANDARD.md`, `docs/DECOMPOSITION_STANDARD.md`,
  `docs/SOFTWARE_WORKFLOW_PROFILE.md`.
- `domains/chirality/_Sources/Source_Manifest.csv` pins Root AGENTS.md, governance
  documents, agent contracts, and skill contracts. Recomputed at product-basis:
  126 CLEAN, 93 DRIFT, 6 MISSING. The six missing ACTIVE-pinned agent files:
  `agents/AGENT_CONTEXT_TRANSPOSE.md`, `agents/AGENT_DECOMP_BASE.md`,
  `agents/AGENT_ORCHESTRATOR.md`, `agents/AGENT_SCHEDULING.md`,
  `agents/AGENT_SKILLMAKER.md`, `agents/AGENT_TOOLMAKER.md`.
- Routed Root-doctrine notice coverage is uneven: App holds several notices;
  `domains/chirality` lacks D-GOV-26; Piping received no D-GOV doctrine notices;
  PEC received no D-GOV doctrine notices. This is a live test of the agent-index
  change-notice and downstream-detection architecture.

Do not mistake for current Root basis:
- `docs/governance_harness/_PROPOSALS/**`; PRD candidate revisions 1–4; ruled proposal
  packets whose authority resides in decision records; the not-adopted D-GOV-17
  model-capability proposal; `execution/_Coordination/HANDOFF_STATE.md` as the current
  initialization handoff (it belongs to the superseded Stage-2 arc, though it still
  records a parked Root compatibility-retirement lane); historical workplans and
  PLAN_INDEX; deliberately retained stale fixtures already dispositioned by an owner
  ruling; ScopeOfWork copies inside AgentRuns and Evaluation snapshots; `plans/**` as
  product authority.

Root conditions to assess, not silently normalize:
1. D-GOV-27 EffectiveSHA remains unbound.
2. Decomposition SHA-role terminology conflicts across surfaces.
3. Accepted post-candidate decomposition amendments lack one supplied verifying diff.
4. OI-011 appears stale after its resolution condition was met.
5. Receipt 52 acts as handoff without a dedicated initialization HANDOFF_STATE file.
6. CURRENT_WORKPLAN points to a completed but still ACTIVE workplan.
7. Root AGENTS.md predates the Root decomposition and does not identify its six
   packages or 45 deliverables.
8. Candidate AC/VER status is machine-opaque.
9. Root initialization recorded unresolved instrument conflicts involving AGENT_TASK
   absolute-path fields, validate_id_format.sh, the SOW validator's prefix set, and
   tools/REGISTRY.md.
10. PRD §5.2 O-1 remains superseded only through the pointer/instrument mechanism.

### 4.2 Chirality App

Product identity:
- Root: `projects/chirality-app-dev/`; registered through
  `projects/chirality-app-dev/chirality.project.json`. A registered project loop, not
  a domain engine.

Accepted PRD basis:
- `projects/chirality-app-dev/docs/PRD.md`, SHA-256 prefix `ef638f43ccae`. No stated
  version number; identity of record is its exact pin in AUTHORITY_CORPUS.json v17.
- Not adopted through one PRD ruling; reflects accumulated D-APP rulings including
  D-APP-72, D-APP-73, D-APP-74.
- Synchronized six-document corpus: DIRECTIVE.md, CONTRACT.md, SPEC.md, TYPES.md,
  PLAN.md, PRD.md. `docs/MANIFEST.json` is stale — use the v17 authority-corpus pin
  for identity, not that manifest.

Accepted decomposition:
- `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`,
  v3.2, SHA-256 prefix `952d3cbf81b0`.
- Header records Gates 1–7 PASSED and acceptance through "implicit human approval per
  user instruction." No separate gate-acceptance ruling file exists.
- Amended in place through SCA-APP-003/D-APP-73 and SCA-APP-004/D-APP-74, topology preserved.
- Headline counts: 78 scope items, 10 packages, 51 decomposition deliverables, 10 objectives.
- The required-or-deferred `contract_invariant_coverage_register.csv` is absent, and
  no deferral ruling was found.
- The latest decomposition coverage package closes with WARNINGS and states
  READY_FOR_IMPLEMENTATION_HANDOFF.

App scopes of work:
- 53 live ScopeOfWork.md + 53 _STATUS.md files: 51 decomposition deliverables + 2
  PKG-00 control deliverables. All 53 IN_PROGRESS following D-APP-54; none ISSUED.
- Open work expressed through each contract's "Remaining" section; the queue
  convention was retired. F-APP-4 fences CHECKING to ISSUED.

App decisions and current state:
- Register: `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md`
  (describes itself as non-governing tracking; 74 RULED rows through D-APP-74).
- Particularly relevant: D-APP-38 (authority-corpus model), D-APP-48..50 (contract
  pull, mirrors, headless transport), D-APP-53/54 (queue retirement, lifecycle
  rebaseline), D-APP-56/57/60/61/64 (governance and delegation changes), D-APP-65
  (PKG-09 and piping transport parked), D-APP-70/71 (ownership slate), D-APP-72
  (Pi/oMLX second engine), D-APP-73 (shared-runtime extraction), D-APP-74 (Woven
  Dialogue information architecture).
- Navigation: `loop/LOOP_INIT.md` → `loop/WORKPLAN_2026-07-18b_app_dev_loop.md` →
  `loop/LOOP_RECEIPTS.md`. Receipt 91 records the daemon-as-service tranche as
  executed and the owner merge of PR #333 as terminal; the associated run handoff
  still says PENDING_PR_AND_OWNER_MERGE.
- SCA-APP-004 is the latest scope-change pointer, marked
  GOVERNANCE_PROPAGATED_IMPLEMENTATION_PENDING.

App integration and drift surfaces:
- Authority corpus:
  `projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json`
  v17 pins the six App documents plus Root SOFTWARE_DECOMP and DOMAIN_ENGINE agent
  instructions; v17 pins were clean at the freeze.
- D-APP-48's 12-file SHA-pinned harness-contract pull is 12/12 stale after the
  shared-runtime tranche rewrote those files to deprecation shims without repinning.
- `domains/chirality-app-dev/_Sources/Source_Manifest.csv` recomputed: 119 CLEAN,
  129 DRIFT, 219 MISSING.
- Runtime/client seams: `frontend/src/lib/runtime-client/daemon-harness-port.ts`,
  `frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts`,
  `frontend/electron/runtime-host.ts`, `frontend/docs/harness/runtime_engine_contract.md`,
  `docs/harness/reliance_boundary_register.md` (all under the App project root).
- The App project AGENTS.md carries frontmatter status "draft" while operating as an
  active overlay.

Do not mistake for current App basis:
- The charter's proposed semantic-parity SCA; `_LATEST.md` or `_REGISTER.md` as
  independent authority; retired NEXT_INSTANCE, dispatch, workspace-manifest, and
  source-audit surfaces; completed or retired plans; unselected design-option
  packages; historical SCA snapshots; the orphan PKG-03_Harness_Runtime_Core evidence
  tree as a registered package; evaluation and reconciliation snapshots as
  decomposition truth; undispositioned notices as adopted authority; build outputs,
  staging trees, session stores, or the separate public App repository.

App conditions to assess, not silently normalize:
1. No repository instrument presently establishes the proposed App UI/API
   semantic-parity work.
2. The PRD has no internal version and contains duplicate §17 numbering.
3. Decomposition acceptance rests on "implicit human approval" rather than a separate ruling.
4. `contract_invariant_coverage_register.csv` is neither present nor explicitly deferred.
5. The D-APP-48 contract mirror is 12/12 stale.
6. D-APP-49 mirror obligations may no longer describe the rehomed architecture.
7. An orphan PKG-03/DEL-03-06 evidence tree exists outside the decomposition.
8. The decomposition count of 51 and filesystem count of 53 require the PKG-00 explanation.
9. Receipt 91 lacks the terminal PR merge SHA.
10. Root-doctrine notices remain undispositioned, including one notice that
    misidentifies its stale target.
11. The project AGENTS.md overlay remains marked draft.
12. The latest run handoff and terminal receipt disagree about whether the PR merge
    is pending.

### 4.3 PEC

Product identity:
- Root: `projects/pec/`. PEC is the optional Chirality coordination plane: a
  deterministic, rebuildable projection plus ephemeral presence. No governed act may
  require PEC.

Accepted PRD:
- `projects/pec/docs/PRD.md`, v2.1, SHA-256 prefix `de0a969cad15`. v2.0 adopted by
  D-PEC-58; directed-bootstrap clarification to v2.1 adopted by D-PEC-61.
- Product invariants PEC-K-01..PEC-K-11. The PRD does not make every described
  capability an immediate implementation mandate.

Accepted decomposition:
- `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`, revision 1.2, SHA-256
  prefix `3e5be4e453ed`. Rev 1.0 accepted by D-PEC-60; SCA-001/D-PEC-61 established
  directed FULL_GRAPH self-bootstrap; SCA-002/D-PEC-64 completed objective mapping
  (rev 1.2).
- Registers: `Deliverables.csv`, `ScopeLedger.csv`, `Companion_Inventory.csv`,
  `ContextBudgetQA.csv`.
- Headline counts: 11 packages (PKG-00..PKG-10), 64 deliverables, 94 scope-ledger rows.
- Read `execution/_Decomposition/_LATEST.md` as the handoff pointer, not as
  decomposition truth independent of the accepted files.

PEC scopes of work and dependency state:
- 32 of 64 deliverables have validated ScopeOfWork.md contracts at INITIALIZED. The
  remaining 32 P2–P4 deliverables remain OPEN without SOWs by deliberate sequencing;
  their absence is not, by itself, a coverage gap.
- All 64 deliverables have local Dependencies.csv files; no central dependency
  register by owner decision.
- Current calibrated dependency state: 254 rows; 135 ANCHOR; 119 EXECUTION; 62 graph
  nodes; 119 edges; 2 orphans; 0 SCCs; 0 waiver sidecars; strict validation clean.
- Advisory blocker state: 24 BLOCKED, 40 UNBLOCKED. Blocker state is visibility, not
  work authority.

PEC decisions and current state:
- Register: `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`.
- Particularly relevant: D-PEC-57 (coordination-plane pivot), D-PEC-58 (PRD v2),
  D-PEC-59 (instruction/profile changes), D-PEC-60 (decomposition acceptance),
  D-PEC-61 (PRD v2.1 and FULL_GRAPH), D-PEC-62 (scaffold and local dependency
  registers), D-PEC-63 (SOW initialization wave), D-PEC-64 (SCA-002 and rev 1.2),
  D-PEC-65 (register-evidence repair), D-PEC-66 (edge decline, DEL-10-10 repair, QA
  dispositions).
- F-PEC-1..F-PEC-4 remain in force. F-PEC-1 fences source work; each build tranche
  requires its own owner-ruled packet.
- Phase 1.3 established INITIALIZED as the activation threshold, deliverable-local
  dependency storage, and the DAG exhibit as frozen gate provenance.
- Current status: `projects/pec/docs/STATUS.md`. Current coordination:
  `projects/pec/execution/_Coordination/_COORDINATION.md` — current calibrated
  numbers are in coordination item 9, superseding item 8.
- Latest domain-engine receipt: `_DomainEngines/pec/LOOP_RECEIPTS.md`, Receipt 112.
- Next owner gates concern P1 build-slice packets followed by WORKING_ITEMS ownership.

PEC integration surfaces:
- Project overlay: `projects/pec/AGENTS.md`. Domain-engine profile:
  `_DomainEngines/profiles/pec.yaml` (records that full supersession remains pending
  the v2 implementation shape).
- Root shared-runtime doctrine: D-GOV-20 and D-T0-23; PEC is a distinct client of the
  Root runtime. PEC PKG-07 and PKG-08 contain the principal shared-runtime and
  API-facing seams.

Do not mistake for current PEC basis:
- The frozen v0.4 prototype under `core/`, `server/`, `web/`, `agent-sidecar/`,
  `tools/`, `fixtures/`; archived PRD v1 material; PRD v2 candidate placement; the
  frozen DAG exhibit as the live dependency register; executed setup plans,
  seed/wave/repair working files, AgentRuns, or historical scope-change evidence;
  advisory blocker output as authority; historical status lines rather than each
  _STATUS.md file's Current State field.

PEC conditions to assess, not silently normalize:
1. The PEC domain-engine profile still awaits full v2 supersession.
2. Only 32 deliverables are initialized; the other 32 are intentionally deferred.
3. Recorded REVIEW residuals remain: DEL-08-02 CLM-002/AX-006 provenance text;
   DEL-08-01 AC-005's second clause reachable only through AC-007's HUMAN_REVIEW row;
   DEL-00-03 CLM-001 unreferenced in its matrix.
4. These residuals are already recorded; assess them in context, do not present them
   as newly discovered.
5. The frozen DAG exhibit's older 120-edge/255-row figures are superseded by the live
   119-edge/254-row local-register state.

### 4.4 Shared method and runtime layers

Shared ScopeOfWork method layer:
- `skills/scope-of-work/`, `tools/scope_of_work/`,
  `tools/validation/validate_decomposition_registers.py`,
  `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`.

Version-skew condition:
- The shared SOW method changed through amendments v1–v6.1. PEC's 32 SOWs were
  repaired and validated under the current method. Root's 45 SOWs passed before the
  v6/v6.1 QA-item-20 harmonization. A current-tool rerun over Root may produce
  tool-drift findings rather than proving the accepted historical validation false.
- Whenever you rely on a validator PASS, identify the tool basis.

Shared runtime:
- Root owns the generic runtime under `runtime/`. App and PEC are distinct clients
  under D-GOV-20 and D-T0-23. Runtime transport does not confer project authority.
  Project adapters retain their own gates, permissions, data boundaries, and evidence.
- Test whether ownership and integration seams are sufficiently explicit to prevent
  Root, App, PEC, and future domain applications from silently absorbing one
  another's responsibilities.

### 4.5 Basis-wide disclosed conditions

Treat the following as disclosed conditions whose consequences must be assessed.
Disclosure does not exempt them from criticism, but distinguish validation from
redundant rediscovery:

1. D-GOV-27's EffectiveSHA is unbound.
2. Root decomposition SHA-role language conflicts across surfaces.
3. Root's live decomposition includes accepted amendments over its accepted candidate
   without one supplied verifying diff.
4. Root's initialization handoff is Receipt 52 rather than a dedicated current
   HANDOFF_STATE file.
5. Root's current workplan is complete but still marked ACTIVE.
6. Root AC/VER candidate status is not deterministically represented.
7. App PRD identity depends on corpus v17 rather than an internal version.
8. App decomposition acceptance provenance is weaker than Root or PEC.
9. App lacks its required-or-deferred invariant-coverage register.
10. App's D-APP-48 pinned mirror is entirely stale.
11. App's domain source manifest is heavily drifted.
12. Root's Chirality domain source manifest contains extensive drift and six missing
    ACTIVE pins.
13. Root-doctrine change notices have not reached or been dispositioned consistently
    by downstream loops.
14. PEC's 32 absent P2–P4 SOWs are deliberate sequencing, not an accidental gap.
15. Root and PEC have different SOW validation-era identities.
16. Domain packs are consulted-only context but contain evidence about downstream
    drift and notice effectiveness.
17. Piping is consulted-only as a situated-product and notice-coverage exemplar.
18. The proposed App semantic-parity change is not yet an accepted instrument.
19. Resource governance is optional candidate architecture, not accepted scope.
20. The charter's program model is reviewer guidance to challenge, not evidence to
    cite as proof.

## 5. Evidence rules

1. Every finding must carry exact evidence anchors: file path plus section, heading,
   row, ID, or line; include SHAs when identity matters. Anchors must resolve at the
   freeze commit.
2. Distinguish accepted basis, candidate/proposed material, superseded material, and
   navigation pointers. Never cite a "do not mistake" surface as accepted basis.
3. Apply the charter's assertion-status discipline:
   - Accepted basis → missing/contradicted/uncovered intent is a conformance finding.
   - Clarified framing → at most a concordance question, ambiguity, risk, or
     recommendation; never fail a product for not instantiating it.
   - Candidate architecture → at most an evidence-linked proposal or owner-decision
     request; never count absence as a scope gap.
   - Open design question → preserve alternatives and decision criteria; do not close
     it by preference.
4. Findings that assess a disclosed condition (§4.5 or product condition lists) must
   say so and add consequence analysis beyond restating the disclosure.
5. When relying on any validator or tool output, state the tool, its basis/era, and
   whether the PASS predates a method change (§4.4 version skew).
6. Confidence must be evidence-grounded; use UNKNOWN visibly where the frozen basis
   cannot decide the question.

## 6. Required report structure and schema

Write your report as one Markdown file at the exact path given in your
reviewer-specific brief. Structure:

```
---
reviewer: A|B
lens: vertical-authority-trace | horizontal-boundary-adversarial
review_freeze_commit: da31c19b5656dd74615e308c4215688971d33dc9
manifest_sha256: 8ac8abb86f064a2a1ef5c51c4eacbbf7b90497d78d1f7a92b55406a44a27096c
charter_sha256: 1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f
date: 2026-07-26
finding_count: <n>
---

# Section 1 — Independent orientation account
(what you established from governed records alone, before consulting the charter;
per product: identity, accepted basis, acceptance provenance, current state)

# Section 2 — Findings
(one subsection per finding)

### <FindingID> — <short title>
```yaml finding
FindingID: <A|B>-F-###        # stable, never reused
Product: ROOT | APP | PEC | CROSS_PRODUCT
Surface: <specific file/SOW/deliverable/register or "program">
Assertion: <one checkable claim, not an impression>
EvidenceRefs:
  - <path>#<section/row/id> [sha256-prefix if identity matters]
Class: authority_conflict | trace_gap | ownership_gap | semantic_conflict | omission | overreach | observation
Severity: BLOCK | REVIEW | WARN | INFO
DisclosedCondition: none | <which disclosed condition this assesses>
Consequence: <why it matters for reliance, implementation, compatibility, closure, or future change>
SmallestAction: <least expansive lawful correction>
Owner: <owning instrument or workflow>
Confidence: HIGH | MEDIUM | LOW | UNKNOWN
```

# Section 3 — Coverage matrix
Markdown table, one row per (product × layer) for products ROOT, APP, PEC and layers:
PRD | AuthorityChain/Corpus | Decomposition+Registers | ScopesOfWork | Decisions |
Coordination/CurrentState | Integration/Drift.
Columns: Layer | Examined (FULL or SAMPLE n/of) | Depth verdict | Breadth verdict |
FindingRefs | Residual unknowns.
Every row must be present even when the verdict is "no finding".

# Section 4 — Boundary matrix
Markdown table, one row per shared function (at minimum: shared runtime; work-surface
/human-agent mediation; coordination projection (PEC); resource governance
(candidate); SOW method layer; decision/register mechanism; notice routing;
domain truth; evidence-and-acceptance flow).
Columns: Function | Semantic owner per accepted basis | Producers | Consumers |
Fallback/degraded | Routed change path | Verdict | FindingRefs.

# Section 5 — Charter challenge outcomes
For each of the 13 charter review questions (list in REVIEW_MANIFEST.json
review_question_set): your basis-grounded answer, and where your independent account
and the charter's framing diverge.

# Section 6 — Disclosed-conditions assessment
For each of the 20 basis-wide conditions: consequence assessment (validation or
escalation), cross-referenced to findings; explicitly avoid rediscovery framing.

# Section 7 — Standing questions and UNKNOWNs
Questions the frozen basis cannot decide, stated as owner-decision requests or
information requests, never as new requirements.
```

Findings must be complete over what you examined — full coverage, not selected
anecdotes — but do not pad: one finding per distinct defect, cross-referenced from
both matrices.

## 7. Reading strategy (guidance, not a limit)

The corpus is large (374 hashed files). Read FULLY: all three PRDs; the three
decomposition main documents; all three decision registers; the coordination/current-
state files named in §4; AGENTS.md overlays; `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`;
AUTHORITY_CORPUS.json; the Tier-0 register. Parse the register CSVs
programmatically where counting matters. For ScopeOfWork files, examine at minimum
2 per package per product (and every SOW any finding relies on), recording exact
sample sizes in the coverage matrix. Use grep/git for targeted verification. Budget
your context: prefer targeted reads of large files over full dumps where a section
suffices, but never base a finding on an unread passage.

## 8. Completion

Finish by writing the complete report file, then return (as your final agent text)
only: your reviewer ID, the report path, finding count by severity, and a one-line
statement of any hard blocker you hit (or "none"). Do not summarize findings in your
return text — the report file is the deliverable.
