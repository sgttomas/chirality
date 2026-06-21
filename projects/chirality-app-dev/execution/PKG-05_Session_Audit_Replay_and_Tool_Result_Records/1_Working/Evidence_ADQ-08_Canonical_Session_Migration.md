# Evidence ADQ-08: Canonical Session Migration

## Scope

ADQ-08 implements D-APP-41 for DEL-05-01. The runtime now treats
`{sessionRoot}/{sessionId}/session.json` as the canonical session metadata file
and treats flat `{sessionRoot}/{sessionId}.json` records as migration inputs.

## Implementation

| Area | Evidence |
|---|---|
| Storage implementation | `frontend/src/lib/harness/session-manager.ts` |
| Focused migration tests | `frontend/src/__tests__/lib/session-manager.test.ts` |
| Event log compatibility | `frontend/src/lib/harness/session-events.ts` already writes `{sessionRoot}/{sessionId}/events.jsonl` |
| Session metadata type | `frontend/src/lib/harness/types.ts` keeps Chirality `sessionId` separate from `engineSessionId`, `claudeSessionId`, `sdkSessionId`, and SDK transcript metadata |

Implemented behavior:

- New sessions write only `{sessionRoot}/{sessionId}/session.json`.
- New sessions do not write legacy flat `{sessionId}.json` files.
- `getById`, `resume`, `save`, `list`, and `delete` all canonicalize legacy flat records before completing.
- Duplicate folder/flat records resolve by D-APP-41: defined canonical values take precedence, legacy-only fields are preserved, the merged canonical `session.json` is written, and the flat record is removed.
- Delete resolves the session first, then removes the canonical session folder and any stray flat duplicate.
- Legacy `claudeSessionId` remains readable as legacy adapter metadata and is not silently remapped to `sdkSessionId`.

## Source-State

D-APP-38 corpus v2 is current for this deliverable. DEL-05-01 `_REFERENCES.md`
reports MATCH for PRD, SPEC, TYPES, CONTRACT, and PLAN. ADQ-08 did not modify
`_STATUS.md` and does not claim lifecycle issuance, release readiness,
professional approval, certification, sealing, authentication, or code-compliance
acceptance.

## Validation

| Command | Result |
|---|---|
| `npm run test -- src/__tests__/lib/session-manager.test.ts --testTimeout=15000` | PASS: 1 file / 6 tests |
| `npm run test -- src/__tests__/api/harness/routes.test.ts src/__tests__/lib/session-events.test.ts src/__tests__/lib/turn-engine.test.ts --testTimeout=15000` | PASS: 3 files / 41 tests |
| `npm run typecheck` | PASS |
| `npm run harness:validate:section8` | PASS with local Next dev server at `http://127.0.0.1:3000`; 8 checks |
| `npm run harness:validate:section9` | PASS: 13 Section 9 checks |
| `npm run test -- --testTimeout=15000` | PASS: 77 files / 527 tests |
| `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` | PASS: corpus v2, no drift |
| `git diff --check` | PASS |

## Remaining Limits

- R1/OI-002 SDK transcript placement remains unresolved and is not closed by ADQ-08.
- `turns/` and `sdk/` directory materialization remains demand-driven/downstream unless a later replay/transcript tranche requires placeholder directories.
