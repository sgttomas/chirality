# Research Note - PKG-05 Session Audit / Replay / Tool Result Records gap assessment

Status: DERIVATIVE_RESEARCH_PACKET

## Question
For each PKG-05 deliverable (DEL-05-01..05), judge implementationReality against the LIVE tree, and state the gap to IN_PROGRESS -> CHECKING -> ISSUED.

## Accepted Basis
Live execution tree + git HEAD of projects/chirality-app-dev. Deliverable docs under execution/PKG-05_*/1_Working/DEL-*/. Retrieval snapshot SRCIDX_20260616T043733Z is STALE (CONTENT_DRIFT, 49/660 artifacts changed) - used for discovery only.

## Short Answer
The R1 audit/event-log substrate is substantially implemented and test-proven in the live tree: HarnessEvent schema, append-only JSONL writer + malformed-tail-tolerant replay, accepted-turn-before-execution + terminal-event durability, cross-surface API-key redaction, typed provider-error classification, and a budgeted redacted ToolResultStore are all present and wired into the runtime, with green vitest suites. The dominant gaps are: (1) DEL-05-01's canonical <sessionId>/session.json FOLDER layout + legacy-migration helper are NOT realized (the session manager still writes flat {sessionId}.json) and have no migration/legacy tests; (2) DEL-05-04 has a backend replay summarizer but NO transcript VIEW/parser module; (3) all five deliverables are still IN_PROGRESS with zero consolidated Evidence_*.md files, so none can advance to the human-gated CHECKING/ISSUED transition yet.

## Evidence
See Evidence_Map.csv (16 rows, all VerificationSource=LIVE_TREE; behavior claims carry :RUN from executed vitest). 110 PKG-05-relevant tests executed green (11 core + 99 supporting).

## Interpretation
implementationReality: DEL-05-02 SUBSTANTIAL/COMPLETE; DEL-05-03 SUBSTANTIAL; DEL-05-05 SUBSTANTIAL; DEL-05-01 PARTIAL; DEL-05-04 PARTIAL (backend done, view absent).

## Caveats
- Retrieval index STALE; live tree is authority. Index surfaced only decomposition docs, no source modules.
- No Evidence_*.md or Dependencies-satisfied records inside any DEL-05-* working folder; _STATUS/MEMORY carry no file-level implementation evidence.
- anthropic-agent-sdk-manager (typed provider errors) is opt-in per D-APP-12 Option B hold; default path is claude-agent-sdk-manager which also redacts.

## Open Questions
See Open_Questions.csv / Amendment_Candidates.csv (4 candidates routed SCOPE_CHANGE/DOMAIN_DECOMP).

## Handoff / Next Action
Consolidate per-deliverable Evidence_*.md citing the live modules+tests; close the DEL-05-01 canonical-folder/migration and DEL-05-04 transcript-view scope questions (amend or implement); then human-gated CHECKING -> ISSUED.
