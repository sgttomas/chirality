# Evidence: ADQ-10 Tool Result Artifact Metadata, Checksum, and Retention

## Scope

ADQ-10 covers the DEL-05-05 residuals selected by the autonomous development queue:

- complete tool-result artifact metadata for replay and transcript projection;
- D-APP-42 SHA-256 checksum and retention policy;
- deterministic replay coverage for interleaved tool artifact events.

This evidence does not claim release readiness, issuance, distribution readiness, TTL/quota cleanup, retention daemon behavior, or any lifecycle transition beyond the current working-state evidence.

## Governing Ruling

D-APP-42 selected minimal audit policy with SHA-256 and session-lifetime retention:

- persisted tool-result artifacts include `sha256` for exact stored artifact bytes after redaction/truncation;
- returned metadata includes `toolName` and optional `turnId` where available;
- metadata keeps relative path, byte counts, redaction/truncation flags, and retention policy;
- retention is session-lifetime only;
- no TTL, quota, daemon, release-quality retention, or broader custody claim is authorized;
- thresholds, preview length, and artifact naming remain unchanged.

## Implementation

| Area | Evidence |
|---|---|
| Artifact metadata contract | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 8-19 defines `sha256`, optional `toolName`, optional `turnId`, and `retentionPolicy: 'session-lifetime'`. |
| Exact stored-byte checksum | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 34-35 and 105-118 compute SHA-256 over the exact UTF-8 artifact content written after redaction/truncation. |
| Tool name and optional turn ID | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 51-63 and 107-115 write/return tool name and optional turn ID when supplied. |
| SDK artifact mapping | `frontend/src/lib/harness/sdk-message-mapper.ts` lines 455-495 passes `parentTurnId` where available and emits artifact metadata in `tool.completed` / `tool.failed` evidence. |
| Transcript projection | `frontend/src/lib/harness/transcript-replay.ts` lines 18-28 and 136-152 projects SHA-256, tool name, turn ID, retention, redaction, truncation, and byte length into transcript artifact links. |
| Transcript display | `frontend/src/components/shell/transcript-stream-view.tsx` lines 28-43 displays SHA-256 and retention metadata when present. |

## Test Evidence

| Test | Evidence |
|---|---|
| Artifact metadata and checksum | `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 44-99 asserts tool name, turn ID, retention policy, SHA-256 shape, exact SHA-256 match against stored bytes, redaction, and truncation. |
| SDK artifact evidence | `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 451-479 asserts mapper-emitted artifact metadata contains SHA-256, tool name, session-lifetime retention, redaction, and no raw secret. |
| Interleaved replay order | `frontend/src/__tests__/lib/session-events.test.ts` lines 234-325 asserts interleaved `tool.started` / `tool.completed` events replay in JSONL append order and preserve checksum/retention metadata. |
| Transcript artifact projection | `frontend/src/__tests__/lib/transcript-replay.test.ts` lines 26-89 asserts transcript artifact links carry SHA-256, tool name, turn ID, session-lifetime retention, redaction, truncation, and byte length. |

## Validation

| Check | Result |
|---|---|
| Focused ADQ-10 suite | PASS: `npm run test -- src/__tests__/lib/tool-result-artifacts.test.ts src/__tests__/lib/tool-evidence.test.ts src/__tests__/lib/session-events.test.ts src/__tests__/lib/sdk-message-mapper.test.ts src/__tests__/lib/chirality-hooks.test.ts src/__tests__/lib/chirality-read-mcp.test.ts src/__tests__/lib/transcript-replay.test.ts --testTimeout=30000` from `frontend/`; 7 files, 38 tests passed. |
| TypeScript | PASS: `npm run typecheck` from `frontend/`; app and Electron TypeScript configs passed. |
| Section 9 harness validator | PASS: `npm run harness:validate:section9` from `frontend/`; `HARNESS_SECTION9_STATUS=pass`, 14 checks. |
| Full Vitest suite | PASS: `npm run test -- --testTimeout=30000` from `frontend/`; 78 files, 534 tests passed. |
| Section 8 harness validator | PASS: `npm run harness:validate:section8` against local Next dev server on `http://localhost:3000`; `HARNESS_VALIDATION_STATUS=pass`; dev server stopped after validation. |
| Authority corpus status | PASS: `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status`; corpus `v2`, all authority refs `MATCH`, no drift. |
| Whitespace/check diff | PASS: `git diff --check -- projects/chirality-app-dev`. |

## Dependency And Document Updates

- DEL-05-05 `Specification.md`, `Procedure.md`, `Guidance.md`, and `Datasheet.md` now record D-APP-42 checksum/retention policy and accepted implementation/test paths.
- DEL-05-05 `Assessment_INSP-03_DEL-05-05.md` now marks the ADQ-10 metadata, checksum/retention, and interleaved replay findings as closed.
- DEL-05-05 `Dependencies.csv` rows DEP-05-05-008 through DEP-05-05-010 are satisfied for REF-006 source state, implementation path, and D-APP-42 checksum/retention policy.
- DEL-05-05 `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, and `MEMORY.md` carry ADQ-10 overlays while preserving generated history.
