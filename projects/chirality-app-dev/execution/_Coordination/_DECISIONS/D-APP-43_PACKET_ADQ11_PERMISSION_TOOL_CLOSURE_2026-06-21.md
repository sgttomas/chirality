# D-APP-43 Packet - ADQ-11 Permission/Tool Closure Semantics

**Status:** RULED
**Date:** 2026-06-21
**Decision ID:** D-APP-43
**Prepared by:** WORKING_ITEMS

## Context / Problem

ADQ-11 selected PKG-06 permission/tool residuals: boot/version fingerprint, missing dependency-register
fallback, exact-edit preconditions, controlled-write atomicity, Bash interruption proof, and
PreCompact/Stop semantics.

Earlier ADQ-11 work implemented the first four residuals, but left Bash interruption and
PreCompact/Stop closure blocked/deferred. D-APP-40 later ruled a dedicated `turn.interrupted` terminal
taxonomy, and D-APP-42 ruled SHA-256/session-lifetime tool-result artifact metadata. The remaining
ADQ-11 question is how to close the tool/interruption and lifecycle evidence without inventing SDK
features or keeping ambiguous legacy behavior.

## Decision Needed

Choose the accepted ADQ-11 closure semantics for:

- interrupted SDK Bash/tool results;
- PreCompact and Stop/finalization evidence when the SDK exposes adapter messages/status/results but
  not dedicated hook callbacks;
- strict versus compatibility-oriented workspace/tool cleanup for missing dependency registers,
  exact-edit checks, and controlled writes.

## Option 1A - Metadata-Only Interrupted Tool Results

Treat `interrupted: true` as successful tool completion with metadata only.

## Option 1B - Interrupted Tool Results Are Non-Success Outcomes

Treat `interrupted: true` as a non-successful interrupted tool outcome in evidence and replay.

## Option 1C - Require Live Provider Process-Cancellation Proof

Require a live end-to-end Anthropic Bash cancellation fixture before closing the residual.

## Option 2A - Invent Synthetic PreCompact/Stop Hook Callbacks

Create Chirality synthetic hook callbacks for PreCompact and Stop even when the SDK does not expose
those callbacks directly.

## Option 2B - Accept Adapter Lifecycle Mapping

Accept provider-status/result mapping as the canonical lifecycle surface for this slice:
`context.compaction.started`, `context.compacted`, `context.compaction.failed`, `turn.completed`,
`turn.failed`, and `turn.interrupted`.

## Option 2C - Leave Residual Open Until SDK Adds Hooks

Keep the residual blocked until explicit SDK PreCompact/Stop hooks exist.

## Option 3A - Preserve Permissive Legacy Behavior

Keep permissive legacy behavior where possible.

## Option 3B - Enforce Strict Canonical Tool/Workspace Behavior

Use explicit missing-register evidence, exact-edit precondition denial, and same-directory atomic
controlled writes as the canonical behavior.

## Option 3C - Infer Compatibility Registers From Prose

Broaden compatibility by parsing or generating replacement dependency registers from markdown
summaries.

## Recommendation

WORKING_ITEMS recommends **1B, 2B, and 3B** for the most stable long-term outcome:

- an interrupted tool did not complete successfully;
- Chirality should normalize real adapter signals instead of fabricating provider hooks;
- strict filesystem/tool behavior avoids silent state invention, stale edits, and partial controlled
  writes.

## Non-Goals / Fences

This decision does not authorize provider/network expansion, remote MCP/plugins/tool search,
release/distribution posture, signing, notarization, publication, release-readiness claims, lifecycle
issuance, professional approval, certification, sealing, authentication, code-compliance acceptance, or
R7 domain-engine implementation.
