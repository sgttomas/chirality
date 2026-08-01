# Evidence Record: Six Program Investigations (2026-08-01)

Status: evidence record per `plans/evidence/README.md`. Non-normative.
Not agent runtime context.

Engagement: six read-only investigation briefs dispatched in parallel
from the Agent 0 posture (one orchestrating model instance + six
subordinate read-only agent instances), each with a frozen scope,
citation requirements, and a falsifiable headline question. No repo
writes occurred during investigation; this record is the only artifact.
Full agent returns exist in the session transcript only; the durable
facts are consolidated here.

## 1. Session facts by investigation

### 1.1 Shared runtime daemon

- Delegation is, in code, a single-child pilot: at most one child per
  Agent 1 run, local Pi/oMLX engine only, exactly one pre-declared
  `read_file` tool (`runtime/packages/core/src/agent1-run-coordinator.ts`
  ~L220-233), narrower than the general delegation language in
  `AGENTS.md` (D-GOV-20 section 9 scopes this as the initial slice).
- Write-scope enforcement for the Claude engine does not exist inside
  `runtime/`: `engine-claude` is a host-injected shim
  (`runtime/packages/engine-claude/src/index.ts` ~L10-14); session
  records carry `allowedWriteTargets` that nothing in core consumes
  (`runtime/packages/core/src/session-store.ts` ~L52-56). The Pi
  adapter self-enforces its pilot bounds
  (`runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts` ~L56-90).
- Delegated-return evidence is hash-only in the durable run record
  (`returnHash`, `rationaleHash`); chat deltas are not persisted, only
  harness events (`runtime/packages/core/src/turn-coordinator.ts`
  ~L181-216); persistence of return text depends on engine emissions.
- Run records (`chirality.agent-run/v1`) are persisted before execution
  and rewritten per state change under
  `<projectRoot>/<defaultExecutionRoot>/_Coordination/AgentRuns/runtime/`,
  fsync-then-rename, 0600/0700; they carry parentage, brief/return
  hashes, scopes, residency epoch, actual engine selections.
- Authority mechanics: per-project tokens exclude `projects:write`,
  `models:write`, `credentials:*`; unix socket 0600; manifest realpath
  containment; post-approval manifest drift bricks the project;
  the public API cannot create an agent2 session
  (`runtime/packages/core/src/runtime-service.ts` ~L157-163).
- Operational gaps: turn locks are in-memory (daemon crash strands
  sessions at "running"); interruption is cooperative-only; bind-time
  vs exec-time realpath TOCTOU in the `read_file` closure.

### 1.2 Pipe-stress claims boundary

- `USER_RULE_PASSED` is intentionally absent from the status enum
  (`projects/chirality-piping/schemas/analysis_status.schema.yaml`
  ~L109); a clean check is `USER_RULE_CHECKED` +
  `checked_no_failures_reported`. Every result envelope must contain
  `HUMAN_REVIEW_REQUIRED` (`schemas/results.schema.yaml` ~L769-770).
- `professional_boundary` claim booleans are `const: false` in schema;
  a document asserting a claim is schema-invalid, and the Rust report
  generator independently blocks on any true flag
  (`core/reporting/report_generator/src/lib.rs` ~L342-349, ~L610-626).
- `HUMAN_APPROVED_FOR_PROJECT` exists only inside
  `HumanAcceptanceRecord` (actor_type const "human", bound_hashes
  minItems 1); external-prover metadata types incoming authority
  assertions only as `RejectedAuthorityClaim`
  (`schemas/external_prover_metadata.schema.json` ~L666-697).
- Residual exposure is free text: the protected-content linter's
  claim-phrase list has 4 entries
  (`core/reporting/protected_content_linter/src/lib.rs` ~L636-642);
  rendered section bodies, adapter prose, and UI labels
  (`apps/desktop/src/features/results/resultInterpretation.ts`) are
  substring-screened or unscreened; the adapter scanner misses
  case/underscore variants ("code compliant" vs `CODE_COMPLIANT`).
- Acceptance-record hash-staleness is policy without code (PB-TBD-002,
  `projects/chirality-piping/docs/PROFESSIONAL_BOUNDARY.md` section 7).

### 1.3 Domain corpus and retrieval

- Warrant/discovery split: retrieval hits are R1 evidence ("useful
  lead, not membership proof"); load-bearing claims require an accepted
  ledger row plus source read (`agents/AGENT_RESEARCH.md` ~L90, L150,
  L215, L290, L310-318); every evidence row records its
  VerificationSource.
- Retrieval enters authority in exactly one place: decomposition gate
  scope ratification, where cosine-vs-threshold verdicts act as a
  conservative alarm, frozen into companion registers and
  human-confirmed (`agents/AGENT_DOMAIN_DECOMP.md` ~L408-448).
- Machinery is deterministic around the one stochastic surface: exact
  numpy dot-product cosine, no ANN
  (`tools/retrieval/query_source_index.py` ~L407-440); immutable
  snapshots; "no silent refresh"; tool-emitted query logs. All four
  `domains/*/_LocalIndexes` are empty in git — indexes are disposable
  local derivatives; ledgers are the truth (~53k atom rows).
- Freshness gaps: embedding-model drift is silent (only the model name
  is recorded, `tools/retrieval/build_source_index.py` ~L140);
  never-indexed new files are out of the freshness checker's scope
  (`tools/source_catalog/check_snapshot_freshness.py` ~L27-28); no
  post-build re-verification of `input_chunks_sha256`.

### 1.4 Cycle-driven resolution

- The doctrine has run live to closure: chirality-app-dev PKG-00
  (`projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DAG_CLOSURE_CONTROL.md`)
  records SCC-002 resolved by a recorded retire/preserve pair and
  SCC-001 closed across three tranches, with ruling
  D-APP-06 (2026-06-15, "Human project authority in chat") holding
  executable work until the residual six-node SCC was addressed; a
  decompose-only tranche (cut/merge explicitly prohibited by the owner)
  reached `StrictSCCCount: 0`, accepted by snapshot 2026-07-11.
- Tooling: Tarjan in `tools/coordination/audit_dag.py` ~L213-249 and
  `tools/coordination/analyze_dep_closure.py` ~L154-192; `--strict`
  gates exist but are not wired into CI;
  `tools/validation/validate_dependencies_schema.py` has no graph
  logic.
- Bypass observed: piping's two candidate SCCs (DAG-006) were never
  resolved by a recorded move — the 2026-06-16 register re-derivation
  (DAG-007) produced an empty candidate worklist; the edges' fate is
  unrecorded. They were CANDIDATE (non-gating), so no ordering was
  silently imposed, but re-derivation bypassed the move-record
  discipline.
- `docs/DECOMPOSITION_STANDARD.md` contains no cycle/SCC language; the
  doctrine binds via `AGENTS.md` only. The section-3.7 SCC edge-lister
  was never implemented; the safe-moves run hand-built its edge CSV.

### 1.5 PEC act vocabulary

- The vocabulary of record is `BoundActs`
  (`projects/pec/agent-sidecar/src/engine/port.ts` ~L85-118): reads,
  dry-run proposals, refresh/withdraw-own, bounded triage
  (parked/duplicate/rejected only, grounds required). No
  accept/apply/reject-of-others/force/approval-outcome shape exists;
  `converted` and `merged` dispositions are refused.
- Enforcement is seven-layered but not uniform: for `converted`,
  server RBAC provides no protection (conversion runs under
  `skipPermission`, `projects/pec/server/src/services/intake.ts`
  ~L106-131); the GOV MAJOR-1 payload guard (type omission + deep key
  scan + acts-layer refusal) is the primary gate there. `import.accept`
  is admin-only 403 for the agent person elsewhere
  (`projects/pec/core/src/permissions.ts` ~L229-231).
- Fatal misprovisioning probe: if a `can/import.accept` probe
  succeeds, the agent refuses to operate at all
  (`projects/pec/agent-sidecar/src/pec-client.ts` ~L266-273) — the
  agent verifies its own powerlessness as a startup precondition.
- Refusals surface verbatim to the owner panel with deep links to the
  human screen act; capability boundaries are disclosed in refusals,
  never silently trimmed. Rulings shaping the vocabulary: D-PEC-10
  (riders; approval-record ban), GOV MAJOR-1 (payload guard),
  D-PEC-20/D-T0-21 (read widening with re-pinned denials),
  D-PEC-36/37 (report reads without professional opinions), D-PEC-44
  (draft-only docx to gitignored scratch).

### 1.6 Program self-measurement

- Numeric, accreting, git-tracked telemetry exists in exactly one
  place: piping evidence sweeps
  (`projects/chirality-piping/validation/evidence/sweeps/`), JSON keyed
  by timestamp + commit with durations and per-surface outcomes,
  accreting since 2026-06-12.
- The richest per-command numeric stream — harness evidence records —
  is gitignored (`_harness_generated/`) and does not accrete.
- D-GOV-20 engine/provider/model-per-run attribution is implemented
  (`runtime/packages/contracts/src/events.ts` ~L26-33) but lives
  off-repo in daemon user-data state. Tokens and cost are recorded
  nowhere; two run records state this explicitly (piping
  DEL0904-EXEC-R3 RUN_RECORD; app-dev
  SOW-APP-RUNTIME-ANALYSIS-20260713-01 HANDOFF_STATE).
- Gap grading: rulings-per-period derivable today (dated decision
  registers); activation width and verification-inversion rate and
  rot-discovery rate capturable with small schema changes (timestamps
  in STATUS.json; structured claim-disposition and defect-origin
  fields); cost-per-accepted-change structurally absent (no upstream
  token emission).
- A one-shot runtime-analysis derivative exists
  (`tools/analysis/analyze_agentic_runtime.py`; used once,
  SOW-APP-RUNTIME-ANALYSIS-20260713-01).

## 2. Claim dispositions (orchestrator impressions vs findings)

| Prior impression | Disposition |
|---|---|
| Doctrine-to-code ratio risks ceremony | INVERTED: doctrine leads code; the risk is present-tense reading of future-tense capability (delegation generality, write scopes) |
| Cycle doctrine likely never exercised live | INVERTED: ran to full closure in app-dev PKG-00 under ruling D-APP-06 |
| Claims discipline enforcement depth unknown | REFINED: structural for machine-readable surfaces; substring-thin for free text |
| Retrieval either suggestion-only or load-bearing | REFINED: third state — bounded authority as human-ratified conservative alarm |
| PEC layers presumed uniform defense-in-depth | REFINED: per-gap primaries; RBAC absent for `converted` |
| Rot lives on unexecuted paths | CONFIRMED: flagship instance is the gitignored harness evidence stream |

## 3. Enforcement frontier (policy-without-code, enumerated)

1. Runtime write-scope enforcement for host-injected engines.
2. Acceptance-record hash-staleness invalidation (PB-TBD-002).
3. SCC edge-lister (cycle doctrine section 3.7) — unimplemented.
4. Cycle checks as CI/mechanical gate (currently workflow convention).
5. Cycle/SCC language absent from the ratified decomposition standard.
6. Token/cost telemetry emission from runtime engines (the only
   structurally absent self-measurement input).

Recurrent weak-surface class across subsystems: content that can be
rephrased or regenerated escapes the type disciplines — free-text
report/adapter/UI language, register re-derivation, embedding weights
behind a recorded name, hash-only return evidence.

## 4. Derived observations (dated induction — see supersession note)

Derived 2026-08-01 by the orchestrating model from Section 1-3 facts.
Supersession: re-derive from the facts with a current model; that
derivation supersedes this list.

1. The program has one signature move applied independently in every
   subsystem: closed vocabulary + human-gated escalation + dated
   durable record; the strongest instances make powerlessness
   self-verifying (PEC misprovisioning probe, pinned canary defects).
2. The universal residual weakness is whatever escapes grammar:
   free text and re-derivation. Closing it requires either more
   determinism (content hashes) or semantic review; substring lists
   cannot close it.
3. Doctrine written ahead of code is a deliberate authoring strategy
   here, but it creates a legibility hazard: readers (including agent
   instances) cannot distinguish implemented guarantees from
   specified intentions without code-level verification.
4. The piping sweep artifact pattern (git-tracked, machine-written,
   schema-versioned, timestamp+commit-keyed JSON) is the natural
   template for a root throughput ledger; `plans/evidence/` records
   remain the narrative/judgment layer, not the machine-row layer.
