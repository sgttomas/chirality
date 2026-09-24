# Brief A1 — sister-loop file-truth survey (TASK, read-only)

Purpose: give SCA-005 a hash-bound, source-cited account of the CURRENT shapes of every surface PEC's accepted basis says it ingests or depends on, across the App, Piping, Runtime, Root and PEC loops, and of the change events that produced them. Accepted basis: D-PEC-86 §3 I-1. Role: TASK (agents/AGENT_TASK.md). No delegation.

Write boundary (only): `projects/pec/execution/_Coordination/SCA-005_PREP_2026-09-23/SURVEY_SISTER_LOOP_FILE_TRUTH.md` and `SURVEY_MANIFEST.json`. Everything else read-only. Content-minimal: cite paths, headings, keys, counts and SHA-256; never copy transcript or prose bodies from other loops beyond a heading or key name.

Required content:
1. Ingest-surface matrix. Rows = the surface classes named in PEC PRD row PEC-RCN-002, §8, PEC-PRS-001, PEC-STR-003 (`_STATUS.md`, decision registers/packets, receipts ledgers, `WORK_GRAPH.json`/`STATUS.json`/`RUNTIME_SUMMARY.json`, dependency registers, workplans/LOOP_INIT, `_harness/adapter.yaml`, MEMORY, Task Management registers, presence/session sources). Columns = loop (chirality-app-dev, chirality-piping, pec, root, chirality-runtime). Cells = current path pattern(s); current grammar/shape (frontmatter, headings, table columns, CSV header); status CURRENT / HISTORICAL-FROZEN / ABSENT; the change event (commit SHA, PR number, notice path, amendment record) with SHA-256 of the record; whether older shapes still exist on disk (e.g. `WORK_GRAPH.json` in older AgentRuns).
2. Development-loop method facts: `workflows/construct-local-work-graph`, `bounded-reconciliation`, `task-management`; root `docs/SPEC.md` §9.8; `docs/templates/MEMORY_TEMPLATE.md`; `docs/governance_harness/_DECISIONS/AMENDMENT_2026-09-22_DEVELOPMENT_LOOP_MEMORY_GRAPH.md`; the 2026-09-23 tranche manifests for App/Piping receipts and evergreen loops. Record what each fixes as a required location or shape.
3. Runtime topology facts for PEC presence/streams: D-GOV-43 and A2 supplement records, `projects/chirality-runtime/README.md`, `docs/APPLICATION_CONSUMER_GUIDE.md`, `docs/APPLICATION_TOOLS.md` if present. State what a PEC client would need (own instance, config schema, socket, tokens, SSE routes) and what no longer exists (per-user daemon, global event feed).
4. Loop registry facts: every loop with a `LOOP_INIT.md` or equivalent; its receipt arrangement; graph location; TM register; decision register; adapter.yaml presence. Compare with `projects/pec/v2/config/loops.json` (registers only `pec`) and PRD §12 "five loops".
5. Fixture candidates: App `execution/_Coordination/WorkGraphs/replay-session-boundary-2026-09-23/`, Piping `WorkGraphs/PIPING_LINTER_SCOPE_20260923/` and `WorkGraphs/dec025-clean-base-repair-2026-09-23/`, their `AgentRuns/<RunID>/` receipts and evidence, affected MEMORY files. List files with SHA-256 and the content-minimal fields a PEC record could carry (path, state, counts, PR numbers, commit SHAs). Do not propose scope.
6. Drift findings table `DR-01..`: PEC-basis locator (PRD row, decomposition row, SOW claim) vs observed current truth, with severity for PEC ingestion (BLOCKING-FOR-PARSER / STALE-PREMISE / INFORMATIONAL). Do not decide dispositions.
7. Open questions for the manager.

`SURVEY_MANIFEST.json`: `{examined_through: <HEAD sha>, files: [{path, sha256, loop, role, status}]}` for every file you relied on.

Acceptance: every claim has a path and, where a file is cited as authority, its SHA-256; no writes outside the boundary; return a short summary listing DR ids and open questions.
