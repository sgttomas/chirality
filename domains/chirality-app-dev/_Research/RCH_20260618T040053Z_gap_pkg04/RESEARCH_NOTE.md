# Research Note - PKG-04 SDK Adapter, Prompt, Provider and Settings gap assessment

Status: DERIVATIVE_RESEARCH_PACKET

## Question

Assess PKG-04 (R0 probe + R1 adapter/prompt/settings): for each of DEL-04-01..05, judge
implementationReality against the LIVE tree, state the gap to IN_PROGRESS->CHECKING->ISSUED,
and list blockers.

## Accepted Basis

Live execution tree + git HEAD aaf9348 of projects/chirality-app-dev. Decision register
_REGISTER.md. Retrieval snapshot SRCIDX_20260616T043733Z (STALE, discovery only).

## Short Answer

PKG-04 has substantial-to-complete runtime code, all proven by green tests: SdkOptionsBuilder
(DEL-04-02), SdkMessageMapper (DEL-04-03), PersonaComposer in persona-manager.ts (DEL-04-04),
and the Anthropic provider key/baseURL/network/redaction bridge in anthropic-agent-sdk-manager.ts
(DEL-04-05) are all implemented and green (130 tests run green across the relevant suites). The
DEL-04-01 probe is SUBSTANTIAL: version pin is satisfied and the previously BLOCKED_TBD packaging
and subprocess paths are now exercised by a RULED live packaged agentSdk read-tool proof
(D-APP-15/16). The dominant gap is governance, not code: every deliverable is Current State
IN_PROGRESS with no consolidated Evidence_*.md (except a partial DEL-04-01 probe record), REF-006
PRD HASH_MISMATCH remains a closure blocker, and the IN_PROGRESS->CHECKING->ISSUED transition is
human-gated. The default provider remains stub (agentSdk opt-in); default-provider cutover is
blocked by D-APP-18 (AWAITING_RULING) but that fence does not block CHECKING/ISSUED of the opt-in
adapter slices.

## Evidence

See Evidence_Map.csv (EV-01..EV-11) and Query_Log.csv. Key live anchors:
- frontend/src/lib/harness/sdk-options-builder.ts:136 (settingSources []), L109-114 (maxTurns/allowed/disallowed/permissionMode/canUseTool).
- frontend/src/lib/harness/anthropic-agent-sdk-manager.ts:255 (key precedence), L204-246 (baseURL validation).
- frontend/src/lib/harness/persona-manager.ts (PersonaComposer compose + fingerprint).
- frontend/src/lib/harness/sdk-message-mapper.ts (1189 LOC provider-neutral mapper).
- Test run green: sdk-options-builder(11), sdk-message-mapper(11), persona-manager(4),
  claude-agent-sdk-manager(3), harness-anthropic-agent-sdk-manager(80), api-key-storage(5),
  api-key-ipc(6), build-network-policy(4), verify-packaged-agent-sdk-runtime(2),
  agent-sdk-mcp-behavior-probe(1), harness-instruction-root(3) = 130 tests.

## Interpretation

The code/test reality is well ahead of the recorded lifecycle and the dispatch brief's decision
posture. The deliverables are stuck at IN_PROGRESS for governance reasons (no Evidence consolidation,
human gate), not for missing implementation.

## Caveats

Retrieval index STALE; REF-006 HASH_MISMATCH; adoption verdict human-gated; not every REQ row was
mapped to an individual assertion (representative load-bearing criteria verified + full suites run).

## Open Questions

See Open_Questions.csv. Chiefly: who is the DEL-04-01 ResponsibleParty/approver, and is the RULED
live packaged proof sufficient to close the DEL-04-01 packaging/subprocess BLOCKED_TBD rows.

## Handoff / Next Action

Route AM-01..AM-04 (Amendment_Candidates.csv). Author per-deliverable Evidence_*.md, refresh the
DEL-04-01 probe record with the RULED proof, resolve REF-006, then human-gated CHECKING/ISSUED.
