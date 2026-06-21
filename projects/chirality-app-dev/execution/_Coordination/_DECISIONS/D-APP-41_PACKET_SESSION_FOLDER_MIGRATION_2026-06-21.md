# D-APP-41 Packet - Session Folder Migration Duplicate-Shape Semantics

**Status:** PROPOSAL / AWAITING_RULING
**Date:** 2026-06-21
**Decision ID:** D-APP-41
**Prepared by:** WORKING_ITEMS

## Context / Problem

ADQ-08 selected the G3 implementation item: canonical `.chirality/sessions/<sessionId>/session.json`
folders plus legacy flat `{sessionId}.json` compatibility. Current source still writes primary
session records as flat JSON in `frontend/src/lib/harness/session-manager.ts`, while adjacent
event/artifact writers already use folder-backed paths:

- `frontend/src/lib/harness/session-events.ts` writes `<sessionId>/events.jsonl`.
- `frontend/src/lib/harness/tool-result-artifacts.ts` writes `<sessionId>/artifacts/tools/...`.

DEL-05-01 source material authorizes canonical folder creation and legacy flat read/list/resume/delete
compatibility, but it explicitly leaves duplicate folder-versus-flat behavior unresolved:

- `Procedure.md` says listing should avoid duplicate records for the same stable `sessionId`, but
  duplicate-resolution policy is `TBD`.
- `Procedure.md` says delete should work for both folder and flat legacy records, but if both shapes
  exist for the same `sessionId`, delete semantics are `TBD` and require human or design ruling before
  destructive behavior.
- `Guidance.md` says duplicate folder-versus-flat behavior should not implement destructive delete or
  overwrite behavior until duplicate precedence and deletion semantics are ruled.

WORKING_ITEMS cannot self-rule this storage contract. Implementing canonical folders without deciding
duplicate precedence/delete semantics would create hidden behavior at the exact migration boundary
DEL-05-01 calls out.

## Decision Needed

Choose the duplicate-shape policy for session records during migration:

- Which record wins for read/resume/list/save when both `<sessionId>/session.json` and
  `<sessionId>.json` exist?
- What should `DELETE /api/harness/session/<sessionId>` do when both shapes exist?
- Whether flat-only legacy records are lazily migrated, preserved as flat records, or eagerly
  converted.

## Option A - Canonical Preferred, Legacy Preserved, Duplicate Delete Refused

Adopt a conservative compatibility rule:

- New sessions are written as canonical folders with `session.json` and prepared `turns/`,
  `artifacts/`, and `sdk/` directories.
- Flat-only legacy records remain readable, listable, resumable, saveable, and deletable.
- If both folder and flat records exist for the same `sessionId`, read/resume/list/save prefer the
  canonical `session.json` record and list the session once.
- If both shapes exist, delete refuses with a typed conflict response and does not remove either
  shape. A later explicit migration/cleanup action can remove or archive the legacy duplicate after
  human acceptance.

Expected follow-up: implement canonical folder creation, dual-shape read/list/save, flat-only legacy
delete, canonical-only delete, duplicate read/list precedence, and duplicate-delete refusal tests.

## Option B - Canonical Preferred, Delete Both Duplicate Shapes

Adopt canonical precedence for read/resume/list/save, but treat both shapes as one logical session for
delete:

- New sessions are canonical folders.
- Flat-only legacy records remain compatible.
- Duplicate read/list/save prefer `session.json`.
- `DELETE` removes both `<sessionId>/` and `<sessionId>.json` when both exist.

Expected follow-up: implement the same migration helpers plus a duplicate-delete-both fixture. This
has simpler user-facing delete semantics, but it is destructive toward the legacy flat record.

## Option C - Flat Legacy Preferred Until Explicit Migration

Keep legacy flat records as the winner whenever both shapes exist:

- New sessions are canonical folders.
- Flat-only legacy records remain compatible.
- If both shapes exist, read/resume/list/save prefer the flat record until an explicit migration is
  performed.
- Delete follows the winning flat shape unless an accepted migration command removes the folder.

Expected follow-up: implement canonical creation but keep legacy precedence in duplicate fixtures.
This minimizes behavior change for old records, but it weakens the canonical-folder transition and can
make existing event/artifact folders look detached from the primary session record.

## Option D - Eager Legacy Conversion

Convert flat legacy records to canonical folders on first read/list/resume/save and remove or archive
the flat JSON record.

Expected follow-up: add conversion code and migration evidence. This simplifies future readers but has
the highest field-loss and destructive-migration risk.

## Recommendation

WORKING_ITEMS recommends **Option A**. It satisfies the canonical-folder requirement for new sessions,
keeps flat legacy sessions usable, gives deterministic duplicate read/list precedence, and avoids
destructive duplicate delete behavior until a later human-accepted cleanup path exists. This is a
recommendation only; no ADQ-08 implementation should proceed until the ruling is recorded.

## Blocks

- ADQ-08 completion.
- ADQ-09 transcript view work if it depends on final session storage compatibility behavior.
- Any DEL-05-01 issue-readiness claim that treats canonical folder migration, duplicate-shape
  behavior, or legacy delete semantics as closed.

## Non-Goals / Fences

This decision does not authorize provider/network expansion, SDK transcript placement finalization,
remote MCP/plugins/tool search, release/distribution posture, signing, notarization, publication,
release-readiness claims, lifecycle issuance, professional approval, certification, sealing,
authentication, code-compliance acceptance, or R7 domain-engine implementation.

## Validation Implications

- For Option A: run focused session-manager/API tests for canonical create/get/list/save/delete,
  flat-only legacy get/list/save/delete, duplicate read/list/save canonical precedence, duplicate delete
  refusal, session-root override behavior, `npm run typecheck`, and broader harness route tests.
- For Option B or D: add destructive-migration fixtures and run broader regression tests because
  delete/conversion can remove legacy records.
- For any option: record DEL-05-01 evidence, update the ADQ queue/completion log, and run D-APP-38
  corpus status if authority documents are edited.

## Affected Files After Ruling

Likely implementation files:

- `frontend/src/lib/harness/session-manager.ts`
- `frontend/src/__tests__/api/harness/routes.test.ts`
- Possible focused `frontend/src/__tests__/lib/session-manager.test.ts`
- DEL-05-01 evidence and local assessment/memory records under `execution/PKG-05_.../DEL-05-01_...`
- `plans/PLAN_2026-06-20_autonomous_development_queue.md`
- `plans/PLAN_COMPLETION_LOG.md`
