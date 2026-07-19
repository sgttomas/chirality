# RETURN — N8 Packet Author (T4, D-APP-66 + D-APP-67)

- **RunID:** D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18
- **Brief:** `LAUNCH_BRIEF_PACKETS_T4.md` (this folder)
- **Date:** 2026-07-18
- **Files written (exactly the four in scope):**
  1. `execution/_Coordination/_DECISIONS/D-APP-66_PACKET_CONTENT_SHA_REVALIDATION_2026-07-18.md` (new, AWAITING_RULING)
  2. `execution/_Coordination/_DECISIONS/D-APP-67_PACKET_SECRET_REGISTRY_REDACTION_TAXONOMY_2026-07-18.md` (new, AWAITING_RULING)
  3. `execution/_Coordination/_DECISIONS/_REGISTER.md` (exactly two rows appended after D-APP-65; State AWAITING_RULING; Ruling record `— (awaiting owner ruling)`)
  4. This return.

No ruling recorded anywhere; no code written.

## D-APP-66 — Content-change SHA revalidation (DEL-07-04)

### Options (owner-presentable summaries)

- **Option A (draft-recommended) — transition-time revalidation via a recorded content-hash binding.** When a human-gated transition to CHECKING supplies an approval SHA, the runtime also computes a deterministic SHA-256 digest of the deliverable's governed documents (sorted paths + contents, excluding `_STATUS.md`, `_run_records/`, `MEMORY.md`) and persists it as `Approved Content SHA-256` next to `Checking Approval SHA`. At the ISSUED transition the digest is recomputed and compared before anything is written; a mismatch — or a missing binding — throws a new typed `APPROVAL_SHA_STALE` and blocks the write. Honest limit stated in the packet: the git-commit SHA itself stays format-validated evidence only (the runtime is git-free and cannot check the commit exists or contains the approved content); what becomes deterministic is the actual voiding condition — that content at the gated write is byte-identical to content at approval. Tests in `lifecycle-status.test.ts` cover match, stale, and malformed/missing-binding cases. Fail-closed on a missing binding strands nothing: all 53 deliverables are IN_PROGRESS, so every future ISSUED is preceded by a binding-minting CHECKING.
- **Option B — consumption-time warning only.** No transition blocking; the status read surfaces recompute the digest and annotate the snapshot with a staleness flag when it mismatches. Smaller surface, but human-gated writes still succeed on stale approvals — REQ-014 stays PARTIAL with better instrumentation.
- **Option C — status quo.** Keep content-change voiding as a governance checklist (the INSP-03 recommendation as written); discharge the deferred item by recording that the check is intentionally procedural; the gap survives to issuance time, where F-APP-4 puts the owner at every gate anyway.

### Draft recommendation

**Option A** — the only option closing the REQ-014 gap deterministically at the gated write, honest about git-free-runtime limits, consistent with the snapshot rule, and single-choke-point cheap (D-APP-65 accepted basis graded it a "cheap determinism win").

### Key pinned design facts (from code reading)

- Approval-SHA validation today is presence + format only: `/^[0-9a-f]{7,64}$/i` at `frontend/src/lib/lifecycle/transition.ts:65`, enforcement `transition.ts:92-118`, error union (`APPROVAL_SHA_REQUIRED`, `INVALID_APPROVAL_SHA`) at `transition.ts:32-38`.
- Persistence is metadata-only: `checkingApprovalSha`/`approvalSha` merged at `transition.ts:120-135`, written by `updateStatusDocument` at `frontend/src/lib/lifecycle/status-writer.ts:125-160` (the assessment anchor) with no verification step.
- `applyLifecycleTransition` is pure content-in/content-out (`transition.ts:137-195`); the single filesystem-aware choke point is `transitionStatusFile` (`transition.ts:197-212`) reached by both API route and MCP tool through `transitionDeliverableStatus` (`frontend/src/lib/workspace/deliverable-contracts.ts:364-386`), which already holds the deliverable folder path (`:374`) — so digest wiring has exactly one insertion point and both surfaces inherit it.
- What the SHA references: in recorded practice a git commit SHA of the approved state (owner-approved `8c6d55d3e…` in DEL-07-04 `_STATUS.md:5-7`); kit docs require only a hex SHA-like token (`docs/PRD.md:572` FR-054, `docs/SPEC.md:222`, `docs/CONTRACT.md:100` K-STATUS-2). No lifecycle module shells out to git — full commit verification is not deterministically possible in-runtime, hence the bounded content-hash-binding design.
- Existing approval-SHA tests to preserve unchanged: `frontend/src/__tests__/lib/lifecycle-status.test.ts:205-252, 254-278`.

## D-APP-67 — Arbitrary-secret-registry redaction taxonomy (DEL-05-03)

### Options (owner-presentable summaries)

- **Option A (draft-recommended) — adopt the configured-secret registry taxonomy (runtime + committed-file + tests).** (i) Runtime: broaden the run-logger helper from three hardwired API-key sources to registered named secrets fed only from explicit configuration — a new env var `CHIRALITY_REDACTION_SECRET_ENV_NAMES` listing `ENV_NAME[:class]` entries (class `api-key` | `secret`), with built-ins: the three existing API-key sources plus `CHIRALITY_PEC_AGENT_PASSWORD` (class `secret`); same variant expansion (raw, double URL-encoding, lowercase-percent, `+`-encoding) and one longest-first pool; replacement tokens `[REDACTED_API_KEY]` (key-class, backward compatible) and `[REDACTED_SECRET]` (other classes); ≥8-char floor; no pattern-guessing of values, ever. (ii) Committed-file surface: ratify the scanner's fixture-marker convention as governed taxonomy — a secret-shaped string is allowed in committed/generated text only if fixture-marked (12-marker list or test path); exact environment values stay blocked regardless of markers ("markers sanctify shapes, never values"); verifier returns quote secret-shaped tokens only in fixture-marked form. (iii) Tests extending `run-logger.test.ts` (class tokens, cross-class longest-first, floor, unset-var skip) and `redaction-path-matrix.test.ts` (registered non-key secret through persistence/replay/browser paths).
- **Option B — ratify the taxonomy document only.** Adopt the committed-file rules and verifier-quoting rule as governed taxonomy without touching the runtime helper (stays API-key-specific, no `[REDACTED_SECRET]`). Resolves the operational friction — the four verifier trips were all committed-text/quoting boundary cases — at zero runtime risk, but leaves the R12 runtime-registry question open (live class `CHIRALITY_PEC_AGENT_PASSWORD` protected only by envelope construction, not by the registry).
- **Option C — defer again.** The gate stays; the boundary that tripped four verifier returns remains unwritten convention re-derived per verifier; the assessment TBD stands.

### Draft recommendation

**Option A** — the taxonomy and registry questions are one decision surface: the scanner already enforces a de-facto taxonomy (UNMAPPED-2, implemented but unowned), a live non-key secret class already circulates (`CHIRALITY_PEC_AGENT_PASSWORD`), and the session paid a four-trip cost for the taxonomy being unratified. Small code+test surface; explicit-configuration-only keeps it deterministic; existing `[REDACTED_API_KEY]` behavior preserved for all consumers.

### Key pinned design facts (from code reading)

- Exactly three configured sources today: `getUiApiKey()` (process-global `__CHIRALITY_UI_API_KEY__`, `frontend/src/lib/harness/api-key-store.ts:12,24-27`), `ANTHROPIC_API_KEY`, `CHIRALITY_ANTHROPIC_API_KEY` — `frontend/src/lib/harness/run-logger.ts:64-77`.
- Variant discipline to replicate: two encoding rounds with lowercase-percent and `+`-for-`%20` (`run-logger.ts:19-62`), longest-first sort (`run-logger.ts:76`), single token `[REDACTED_API_KEY]` (`run-logger.ts:90`), structural recursion `redactJsonLike` (`run-logger.ts:93-109`).
- Live unregistered secret class: `CHIRALITY_PEC_AGENT_PASSWORD`/`EMAIL` read at `frontend/src/lib/harness/mcp/pec-bridge-client.ts:184,296`; kept out of envelopes by construction (D-55 row DEL-05-03 UNMAPPED-1) but invisible to the redaction registry.
- Scanner prior art (`frontend/scripts/scan-secret-evidence.mjs`, D-55 row UNMAPPED-2): exact env values + variants with ≥8-char floor (`:180-204`), `sk-ant-` shape (`:50`), URL-credential shape (`:51`), 12 fixture markers (`:52-65`), marker-or-test-path fixture test (`:141-148`), exact env values blocked unconditionally — markers never sanctify real values (`:296-317`), hash-only findings (`:166-178`).
- ORN-11 exclusion pinned: "An arbitrary configured-secret registry remains outside ORN-11" / "not inferred or added by ORN-11" (`Evidence_ORN-11_Runtime_Redaction_Path_Matrix.md:11,30`).
- Operational evidence home: four consecutive verifier-return trips over the fixture-marker/real-credential boundary, recorded in the D-APP-65 accepted basis (`D-APP-65_PACKET_ACCEPTED_RECOMMENDATIONS_2026-07-18.md` §2 recommendation 4).

## Deviations

None. Both packets follow the D-APP-63 compact shape, land AWAITING_RULING with placeholder ruling sections, name concrete test additions, state explicitly that no code lands without an owner ruling (declined/deferred leaves the gate intact), and the register received exactly two rows.
