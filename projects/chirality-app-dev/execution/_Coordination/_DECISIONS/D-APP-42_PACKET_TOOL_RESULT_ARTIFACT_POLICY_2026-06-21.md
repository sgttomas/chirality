# D-APP-42 Packet - Tool Result Artifact Metadata, Checksum, and Retention Policy

**Status:** PROPOSAL / AWAITING_RULING
**Date:** 2026-06-21
**Decision ID:** D-APP-42
**Prepared by:** WORKING_ITEMS

## Context / Problem

ADQ-10 selected the DEL-05-05 residual item: tool-result artifact metadata, checksum/retention, and
concurrent replay tests. Current implementation already stores oversized tool results under
`.chirality/sessions/<sessionId>/artifacts/tools/` and persists redacted artifact metadata:

- `frontend/src/lib/harness/tool-result-artifacts.ts` writes redacted/truncated artifact files and
  returns `artifactPath`, `artifactRelativePath`, byte counts, redaction, and truncation flags.
- `frontend/src/lib/harness/tool-evidence.ts` classifies inline/artifact budget state without storing
  raw output.
- `frontend/src/lib/harness/session-events.ts` replays event JSONL and tolerates malformed trailing
  lines.

DEL-05-05 source material leaves several artifact policy values explicit `TBD`:

- `Specification.md` REQ-012 says output class byte thresholds, preview length, artifact naming,
  checksum policy, and retention/deletion behavior are `TBD` until implementation design or governed
  source update.
- `Guidance.md` says thresholds, preview lengths, naming, checksum, and retention should remain `TBD`
  until accepted design work fills them.
- `Procedure.md` records residual design decisions for thresholds, preview length, artifact naming,
  checksum policy, retention/deletion behavior, and optional redaction-status metadata.

WORKING_ITEMS can add replay fixtures that rely on JSONL write order, but it cannot self-rule checksum
and retention/deletion policy while the selected queue item asks to close those residuals.

## Decision Needed

Choose the accepted artifact policy for the next DEL-05-05 implementation slice:

- Whether persisted tool artifacts require a checksum in returned metadata and event metadata.
- Which checksum algorithm, if any, is canonical.
- What retention/deletion behavior applies to tool-result artifacts.
- Whether `turnId`, `toolName`, redaction status, and checksum must be duplicated in returned artifact
  metadata or only present inside artifact content / event context.
- Whether threshold/preview/naming policy remains deferred or is included in the same slice.

## Option A - Minimal Audit Policy: SHA-256 + Session-Lifetime Retention

Adopt a conservative metadata policy without adding a retention daemon:

- Add `sha256` for the exact stored artifact bytes after redaction/truncation.
- Add `toolName` and optional `turnId` to returned artifact metadata where inputs are available.
- Keep `redacted: true`, `truncated`, `originalByteLength`, `artifactByteLength`, and relative path.
- Treat retention as session-lifetime retention: artifacts remain with the session folder and are
  deleted only when the session/artifact folder is explicitly deleted by existing session lifecycle or
  future ruled cleanup.
- Do not add independent TTL, quota purge, release-quality retention claims, or background cleanup.
- Keep output thresholds, preview length, and artifact naming scheme unchanged until a later dedicated
  policy change.

Expected follow-up: implement checksum/metadata fields, add focused artifact metadata tests, add
concurrent/interleaved replay fixture using JSONL append order, and record retention as session-scoped
without claiming release-grade retention management.

## Option B - Metadata Fixture Only, Keep Checksum And Retention Deferred

Only add the concurrency replay fixture and optional `toolName`/`turnId` metadata where already
available; leave checksum and retention/deletion policy `TBD`.

Expected follow-up: smaller code change, but ADQ-10 would remain partially blocked because the queue
explicitly names checksum/retention residuals.

## Option C - Full Artifact Policy: Checksum + Retention Manifest

Add a richer policy surface:

- `sha256` checksum for artifact bytes.
- Artifact manifest/index under each session.
- Explicit retention class / deletion state fields.
- Tool-result cleanup behavior independent of session deletion.

Expected follow-up: broader implementation and tests for manifest consistency, deletion, replay after
cleanup, and failure recovery. This likely touches session/artifact contracts beyond the current
residual item.

## Option D - No Checksum, Rely On Append-Only Event Metadata

Do not add checksums. Keep artifact byte counts and append-only JSONL references as sufficient audit
metadata for now; retention remains implicit session-lifetime behavior.

Expected follow-up: least code churn, but leaves the inspection finding around checksum/retention
mostly unresolved.

## Recommendation

WORKING_ITEMS recommends **Option A**. It closes the useful checksum and metadata gap with low
runtime risk, avoids inventing quota/TTL cleanup policy, keeps artifacts bound to session lifetime,
and leaves threshold/preview/naming policy unchanged. This is a recommendation only; no ADQ-10
implementation should proceed until the ruling is recorded.

## Blocks

- ADQ-10 completion.
- DEL-05-05 issue-readiness claims that treat checksum, retention/deletion, or complete artifact
  metadata policy as closed.
- Downstream replay/transcript work that assumes a final artifact retention policy.

## Non-Goals / Fences

This decision does not authorize provider/network expansion, SDK transcript canonicality changes,
remote MCP/plugins/tool search, release/distribution posture, signing, notarization, publication,
release-readiness claims, lifecycle issuance, professional approval, certification, sealing,
authentication, code-compliance acceptance, or R7 domain-engine implementation.

## Validation Implications

- For Option A: run focused `tool-result-artifacts`, `tool-evidence`, `session-events`, and harness
  route tests; run `npm run typecheck`; add deterministic interleaved replay coverage.
- For Option C: add broader artifact manifest/deletion tests and replay-after-cleanup tests.
- For any option: record DEL-05-05 evidence, update the ADQ queue/completion log, and run D-APP-38
  corpus status if authority documents are edited.

## Affected Files After Ruling

Likely implementation files:

- `frontend/src/lib/harness/tool-result-artifacts.ts`
- `frontend/src/lib/harness/tool-evidence.ts`
- `frontend/src/__tests__/lib/tool-result-artifacts.test.ts`
- `frontend/src/__tests__/lib/session-events.test.ts`
- Possibly `frontend/src/__tests__/api/harness/routes.test.ts`
- DEL-05-05 evidence and local assessment/memory records under `execution/PKG-05_.../DEL-05-05_...`
- `plans/PLAN_2026-06-20_autonomous_development_queue.md`
- `plans/PLAN_COMPLETION_LOG.md`
