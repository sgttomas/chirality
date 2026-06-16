# Source Pack: SRC-DEL-DEL-05-05-TOOLRESULTSTORE-AND-SESSION-ARTIFACTS

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-05_ToolResultStore_and_Session_Artifacts/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-05_ToolResultStore_and_Session_Artifacts/Datasheet.md

### Datasheet: DEL-05-05 ToolResultStore and Session Artifacts

#### Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-05-05 |
| DeliverableName | ToolResultStore and Session Artifacts |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |
| ResponsibleParty | TBD |

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary purpose | Store and preview medium/large tool outputs under session artifacts without flooding chat or model context. | `_CONTEXT.md` Deliverable Scope; decomposition `DEL-05-05` row |
| Session artifact location | `.chirality/sessions/<sessionId>/artifacts/` for raw large tool results. | `docs/SPEC.md` Sections 8.2, 9.2; `docs/PRD.md` Sections 10.3, 10.5 (HASH_MISMATCH warning) |
| Canonical audit mirror | `.chirality/sessions/<sessionId>/events.jsonl`; SDK transcripts remain secondary unless imported into `HarnessEvent` form. | `docs/SPEC.md` Section 8.4; `docs/DIRECTIVE.md` Section 2.3 |
| Event linkage | Tool result artifacts must be referenced by path from persisted runtime event metadata. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` Section 10.4 (HASH_MISMATCH warning) |
| Artifact metadata fields | Tool name, turn ID, byte count, truncation flag, and relative artifact path. | `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning) |
| Redaction boundary | Runtime events, run logs, tool artifacts, and provider errors must redact secrets and avoid API keys. | `docs/CONTRACT.md` K-EVENT-6, K-KEY-1; `docs/PRD.md` NFR-002 (HASH_MISMATCH warning) |
| Output budget classes | Small results inline, medium results preview plus metadata, large results raw artifact plus metadata. | `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning) |
| Output budget thresholds | TBD. Source corpus defines classes but not byte thresholds. | `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning) |

#### Conditions

| Condition | Value | Source |
|---|---|---|
| Working-root locality | Project execution state, sessions, and tool artifacts live under the selected working root or configured Chirality-controlled session path. | `docs/DIRECTIVE.md` Sections 2.3, 2.8; `docs/SPEC.md` Section 10.2 |
| Replay requirement | JSONL replay must tolerate malformed trailing lines while preserving valid prior events. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
| Ordering requirement | JSONL writes must append newline-delimited events in write sequence. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` Section 10.4 (HASH_MISMATCH warning) |
| Concurrent tool activity | Deterministic replay must survive SDK tool concurrency. | Decomposition SOW-053; `docs/SPEC.md` Section 9.2 |
| Model/chat budget | Large outputs must not flood chat or model context. | `docs/PRD.md` NFR-017 and R4 acceptance (HASH_MISMATCH warning) |
| Sensitive payload storage | Sensitive values must not be stored unless a redaction pass has approved the payload. | `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning); `docs/CONTRACT.md` K-EVENT-6 |

#### Construction

| Component | Expected construction | Status |
|---|---|---|
| `ToolResultStore` | Product-owned artifact and preview policy for tool outputs. | Required; interface/module location TBD |
| Session artifact writer | Writes large raw results beneath `.chirality/sessions/<sessionId>/artifacts/` and returns relative artifact references. | Required; implementation path TBD |
| Preview builder | Produces inline small results and medium previews without unbounded chat/model expansion. | Required; thresholds and preview format TBD |
| Metadata fixture set | Covers tool name, turn ID, byte count, truncation flag, relative artifact path, and redaction status where applicable. | Required |
| Output budget tests | Verify inline/preview/artifact behavior and no chat/context flooding. | Required |
| Replay fixtures | Verify artifact links remain reconstructible through `events.jsonl` replay, including malformed-tail tolerance. | Required |

#### Current Discovery State

| Topic | Current state | Disposition |
|---|---|---|
| B-001 source-state warning | `_REFERENCES.md` marks REF-006 `docs/PRD.md` as `HASH_MISMATCH`; PRD-derived artifact-budget and metadata claims remain warning-qualified until human source reconciliation accepts the snapshot. | Surfaced as a source-state caveat; not treated as a substitute for human ruling. |
| C-001 implementation and fixture paths | Repository discovery did not find an accepted `ToolResultStore` module, output-budget test files, metadata fixture files, replay fixture files, or redaction fixture files. | Keep paths `TBD` until implementation work lands and is accepted. |
| F-001 unresolved policy fields | Byte thresholds, preview length, artifact naming, checksum policy, and retention/deletion behavior are not specified by the matched source corpus. | Keep as governed design deferrals; do not encode hidden policy. |

#### References

| RefID | Source | Notes |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | MATCH. Runtime events explain work and the Chirality audit mirror is canonical. |
| REF-002 | `docs/CONTRACT.md` | MATCH. K-EVENT and K-KEY invariants bind redaction, artifacts, and replay. |
| REF-003 | `docs/SPEC.md` | MATCH. Defines session layout, `HarnessEvent`, append/replay rules, and artifact path references. |
| REF-004 | `docs/TYPES.md` | MATCH. Defines `ToolResultStore`, session terms, `events.jsonl`, and `artifacts/`. |
| REF-005 | `docs/PLAN.md` | MATCH. Places tool-result budgeting in R4 and preserves Chirality ownership of artifact/preview policy. |
| REF-006 | `docs/PRD.md` | HASH_MISMATCH. Used as accessible vNext direction per task instruction; unsupported details remain `TBD`. |
| REF-007 | `AGENT_SOFTWARE_DECOMP.md` | MATCH. Used for decomposition method context only. |

## Component: execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-05_ToolResultStore_and_Session_Artifacts/Guidance.md

### Guidance: DEL-05-05 ToolResultStore and Session Artifacts

#### Purpose

This deliverable exists to keep tool-heavy runtime work auditable and readable. Tool results must be available for replay and diagnosis, but large payloads must not be pushed unbounded into chat, browser events, or model context. Chirality owns the artifact/preview policy even when the SDK supplies the tool loop.

Sources: `_CONTEXT.md`; decomposition `DEL-05-05`; `docs/DIRECTIVE.md` Sections 2.3 and 2.8; `docs/PLAN.md` R4; `docs/PRD.md` Sections 9.4 and 10.5 (HASH_MISMATCH warning).

#### Principles

- Keep `events.jsonl` canonical. Runtime artifact metadata should point from Chirality events to stored outputs; artifact storage must not make SDK transcripts or chat history the authority. Source: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-EVENT-4.
- Budget output by representation. Small text can be inline, medium output needs preview plus metadata, and large output needs artifact storage plus a compact reference. Source: `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning).
- Preserve replay before convenience. A user reviewing a session later should be able to reconstruct tool summaries, terminal outcomes, and artifact links from Chirality JSONL plus session metadata. Source: `docs/PRD.md` FR-076 and NFR-017 (HASH_MISMATCH warning); `docs/SPEC.md` Section 9.2.
- Redact before storing sensitive content. Secrets must not land in runtime events, run logs, provider errors, or tool artifacts. Source: `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1.
- Keep provider details out of product contracts. `ToolResultStore` should operate on Chirality event/session concepts, not SDK-native transcript shapes. Source: `docs/PRD.md` Section 9.4 (HASH_MISMATCH warning); `docs/CONTRACT.md` K-ENGINE-4.
- Make missing policy explicit. Thresholds, preview lengths, naming, checksum, and retention are currently source gaps and should remain `TBD` until accepted design work fills them.

#### Considerations

##### Source-state warning

`docs/PRD.md` is listed with `HASH_MISMATCH` in `_REFERENCES.md`. The task instruction says to treat this as a source-state warning. This draft uses PRD content as accessible vNext direction but does not invent unsupported values from it.

##### Budget thresholds

The corpus defines small, medium, and large output classes but does not define byte thresholds. Use `TBD` in implementation tickets and tests until thresholds are selected and accepted. A test can still assert class behavior once thresholds are parameterized.

F-001 and X-001 should remain linked: threshold and preview-limit acceptance is the policy decision, and threshold-boundary verification is the proof that the accepted policy behaves as intended. Until that decision exists, boundary tests should be recorded as pending rather than filled with arbitrary values.

##### Event and artifact separation

Avoid embedding raw large payloads in `HarnessEvent.data`. Store the payload under session artifacts and persist metadata sufficient for replay. This keeps UI events compact and prevents model-context flooding while preserving audit evidence.

##### Redaction posture

The safest implementation shape is a redaction decision before artifact persistence. If source uncertainty remains about whether a payload contains secrets, prefer redacted preview and blocked raw storage over saving unreviewed sensitive output.

##### Concurrent tool activity

The decomposition explicitly includes deterministic replay under tool concurrency. Store enough sequence or parent-event linkage to preserve replay order under interleaved completions. The source corpus does not specify exact fields beyond the `HarnessEvent` shape, so sequence metadata details are TBD.

D-001 is best handled as an assertion-design requirement: replay tests should prove ordering from JSONL write sequence or accepted event-ordering metadata, not from incidental SDK completion order.

#### Trade-offs

| Trade-off | Guidance |
|---|---|
| Inline content vs artifact link | Inline improves immediate readability for small text. Artifact links preserve performance and context for large output. Use the budget class, not ad hoc UI convenience, to decide. |
| Preview richness vs leakage risk | Rich previews help review, but sensitive data must be redacted. Prefer safe summaries when redaction status is uncertain. |
| SDK transcript detail vs Chirality canonicality | SDK transcripts may contain useful details, but Chirality event metadata and artifact references are the replay authority unless transcript content is imported into `HarnessEvent` form. |
| Early hardcoded thresholds vs configurable policy | Hardcoded thresholds would unblock tests but risk becoming undocumented product policy. Keep threshold values TBD until design acceptance. |
| Retention/checksum certainty vs premature policy | E-001 remains a rationale gap until retention/deletion and checksum policy are selected. The interim balance is to preserve auditable artifact references and redaction posture while labeling retention, deletion, checksum, naming, and redaction-status metadata as explicit TBDs. |

#### Examples

| Scenario | Expected behavior |
|---|---|
| Small text result | Store result inline in the tool completion event data when it is within the accepted small-output threshold and contains no unredacted secrets. Threshold TBD. |
| Medium text result | Store a preview and required metadata; avoid placing the full raw result in chat/model context. Preview length TBD. |
| Large result | Store raw payload under `.chirality/sessions/<sessionId>/artifacts/`; persist relative artifact path, tool name, turn ID, byte count, and truncation flag in event metadata. |
| Sensitive tool output | Apply redaction before event/artifact persistence; if redaction cannot approve the payload, do not store raw sensitive values. |
| Malformed trailing JSONL line | Replay should ignore the malformed tail and preserve valid prior events and artifact links. |

#### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| TBD | No direct source-content conflict identified. `docs/PRD.md` has a hash mismatch warning, but the task instructed use as a source-state warning. | `_REFERENCES.md` REF-006 | User task instruction | All sections citing PRD | Treat PRD as accessible direction while preserving unsupported details as `TBD`. | TBD |
| B-001 | PRD-derived tool-result budgeting and metadata claims are useful direction, but REF-006 remains `HASH_MISMATCH` in `_REFERENCES.md`. | `_REFERENCES.md` REF-006 | `docs/PRD.md` Sections 10.4-10.5 and NFR-017 | Datasheet Attributes; Specification Requirements; Procedure Steps | Keep PRD-derived claims warning-qualified until source reconciliation is accepted. | TBD |

## Component: execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-05_ToolResultStore_and_Session_Artifacts/Procedure.md

### Procedure: DEL-05-05 ToolResultStore and Session Artifacts

#### Purpose

Define the production and verification procedure for implementing `ToolResultStore` and session artifact behavior for DEL-05-05. The procedure focuses on producing the deliverable artifacts named in `_CONTEXT.md`: artifact store, output budget tests, and metadata fixtures.

#### Prerequisites

- Confirm the active source corpus listed in `_REFERENCES.md` is available.
- Review `docs/SPEC.md` Sections 8-9 for session layout and `HarnessEvent` append/replay rules.
- Review `docs/CONTRACT.md` K-EVENT-4 through K-EVENT-7 and K-KEY-1 for canonical audit, replay, redaction, and artifact constraints.
- Review `docs/PRD.md` Sections 10.4-10.5 and NFR-017 as source-state-warning input because `_REFERENCES.md` marks PRD as `HASH_MISMATCH`.
- Confirm upstream dependencies once dependency extraction exists. Current `_DEPENDENCIES.md` lists upstream and downstream as TBD.
- Confirm implementation location for `ToolResultStore`. Current source corpus names the concept but does not specify a module path.
- Treat B-001 as unresolved until REF-006 source reconciliation is accepted; PRD-derived artifact-budget details remain warning-qualified.

#### Steps

1. Identify the session artifact root.
   - Use canonical `.chirality/sessions/<sessionId>/artifacts/` from `docs/SPEC.md` Section 8.2 unless the runtime is explicitly configured with a Chirality-controlled session root.
   - Keep artifact paths relative in event metadata where required by `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning).

2. Define the tool-result budget policy.
   - Represent small, medium, and large result classes.
   - Keep concrete byte thresholds and preview length as `TBD` until accepted design work supplies values.
   - Ensure the policy can produce inline small data, medium preview plus metadata, and large artifact references.

3. Define the artifact metadata shape.
   - Include tool name, turn ID, byte count, truncation flag, and relative artifact path.
   - ASSUMPTION: Include redaction status or redaction decision reference if the implementation needs audit evidence for sensitive payload handling. Source support exists for redaction before storage, but the exact metadata field is TBD.

4. Implement artifact persistence.
   - Store raw large results under the session artifact folder.
   - Persist compact metadata in Chirality runtime events rather than embedding raw large payloads in `HarnessEvent.data`.
   - Preserve ordered append/write sequence semantics for replay.

5. Implement preview handling.
   - Inline small text results only when within the accepted threshold and after redaction policy permits storage.
   - Generate medium previews that are sufficient for UI scan/replay without full raw output in chat/model context.
   - For large results, show artifact metadata/link plus a bounded preview if permitted by redaction policy.

6. Apply redaction before persistence.
   - Redact API keys and configured secret variants from event data, logs, provider errors, and tool artifacts.
   - Do not store sensitive values unless a redaction pass has approved the payload.

7. Add output budget tests.
   - Cover small inline, medium preview plus metadata, and large raw artifact storage.
   - Include threshold-boundary fixtures once threshold values are accepted.
   - Verify large outputs do not flood chat or model context.
   - For X-001, record exact threshold-boundary tests as pending until byte thresholds and preview limits are accepted.

8. Add metadata and replay fixtures.
   - Assert required metadata fields.
   - Verify relative artifact paths resolve under the session artifact root.
   - Verify valid artifact links remain available when replay ignores a malformed trailing JSONL line.
   - Include interleaved tool-result fixtures for deterministic replay under concurrency.
   - For D-001, assert replay order from JSONL write sequence or accepted event-ordering metadata; do not rely on incidental SDK completion order.

9. Run relevant validation.
   - Run unit and integration tests for the artifact store, event append/replay, redaction, and session metadata.
   - Add or update Section 9 validation coverage when the runtime validation IDs land.

10. Record residual TBDs.
    - If thresholds, naming, checksum, retention, or redaction metadata remain unspecified, leave explicit `TBD` notes in implementation documentation and test TODOs rather than encoding hidden policy.
    - For E-001, explain any accepted retention/deletion, checksum, and redaction-status metadata policy as a balance between audit reconstructability and leakage minimization.

#### Verification

| Check | Expected result |
|---|---|
| Session path check | Large artifact payloads are written beneath `.chirality/sessions/<sessionId>/artifacts/` or an approved Chirality-controlled session artifact root. |
| Metadata check | Tool name, turn ID, byte count, truncation flag, and relative artifact path are persisted with the result reference. |
| Budget check | Small, medium, and large outputs take distinct inline/preview/artifact paths. Threshold values remain TBD until accepted. |
| Redaction check | API keys and configured secrets do not appear in event data, logs, provider errors, or stored artifacts. |
| Replay check | Valid prior artifact links survive malformed trailing JSONL during replay. |
| Concurrency check | Interleaved tool completions replay deterministically by write sequence or accepted event ordering metadata. |
| Provider-neutral check | Public contracts and canonical events are Chirality-owned and do not expose SDK-shaped internals except as adapter metadata. |

#### Records

- Artifact store implementation path: TBD.
- Output budget test files: TBD.
- Metadata fixture files: TBD.
- Replay fixture files: TBD.
- Redaction fixture files: TBD.
- Residual design decisions: thresholds, preview length, artifact naming, checksum policy, retention/deletion behavior, and optional redaction-status metadata.
- C-001 path disposition: current code discovery found no accepted implementation or fixture paths for this deliverable; all listed paths remain `TBD`.
- F-001 policy disposition: output thresholds, preview length, artifact naming, checksum policy, and retention/deletion behavior remain governed deferrals.
- D-001 verification disposition: concurrent replay checks must bind to write sequence or accepted event-ordering metadata.
- X-001 verification disposition: threshold-boundary checks remain pending until threshold and preview-limit values are accepted.
- E-001 rationale disposition: retention/deletion, checksum, and redaction-status rationale remains pending until the corresponding policies are chosen.

## Component: execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-05_ToolResultStore_and_Session_Artifacts/Specification.md

### Specification: DEL-05-05 ToolResultStore and Session Artifacts

#### Scope

DEL-05-05 covers the backend feature slice that stores, previews, and references medium/large tool outputs as session artifacts so chat and model context are not flooded. The slice belongs to PKG-05, whose package scope is canonical session layout, `HarnessEvent`, JSONL append/replay, redaction, and tool result artifacts.

In scope:

- Product-owned `ToolResultStore` policy and implementation surface for tool output budgeting.
- Session-local artifact storage under `.chirality/sessions/<sessionId>/artifacts/`.
- Metadata records linking stored artifacts to tool name, turn ID, byte count, truncation flag, and relative artifact path.
- Preview behavior for medium results and inline behavior for small results.
- Output budget tests, replay/metadata fixtures, and redaction-sensitive artifact behavior.

Out of scope:

- Tool permission semantics and deny-first policy, except where stored tool output must respect redaction and audit constraints.
- SDK transcript canonicality decisions outside artifact linkage.
- Bash enablement policy, except that allowed bash output must eventually use the same result budgeting behavior.

Sources: `_CONTEXT.md`; decomposition `DEL-05-05`; `docs/SPEC.md` Sections 8-9; `docs/PRD.md` Sections 10.4-10.5 (HASH_MISMATCH warning).

#### Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-05-05-REQ-001 | The implementation MUST preserve `.chirality/sessions/<sessionId>/events.jsonl` as the product-owned Chirality audit mirror; artifact storage MUST NOT make SDK transcripts canonical. | `docs/SPEC.md` Section 8.4; `docs/DIRECTIVE.md` Section 2.3; `docs/CONTRACT.md` K-EVENT-4 |
| DEL-05-05-REQ-002 | Large tool result payloads MUST be stored as artifacts and referenced by path from runtime event metadata. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` Section 10.4 (HASH_MISMATCH warning) |
| DEL-05-05-REQ-003 | Raw large tool results MUST be stored beneath `.chirality/sessions/<sessionId>/artifacts/` or an explicitly configured Chirality-controlled session artifact path. | `docs/SPEC.md` Section 8.2; `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning) |
| DEL-05-05-REQ-004 | Small text tool results MAY be carried inline in `tool.completed` data; medium results MUST include preview and metadata; large results MUST include artifact metadata rather than unbounded inline content. | `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning) |
| DEL-05-05-REQ-005 | Artifact metadata MUST include tool name, turn ID, byte count, truncation flag, and relative artifact path. | `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning) |
| DEL-05-05-REQ-006 | Runtime events, run logs, tool artifacts, and provider errors MUST redact secrets and avoid storing API keys. | `docs/CONTRACT.md` K-EVENT-6, K-KEY-1; `docs/PRD.md` NFR-002 (HASH_MISMATCH warning) |
| DEL-05-05-REQ-007 | Sensitive values MUST NOT be stored in tool artifacts unless a redaction pass has approved the payload. | `docs/PRD.md` Section 10.5 (HASH_MISMATCH warning); `docs/CONTRACT.md` K-EVENT-6 |
| DEL-05-05-REQ-008 | Artifact links and summaries MUST remain replayable from Chirality JSONL plus session metadata even when a malformed trailing JSONL line exists. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
| DEL-05-05-REQ-009 | Tool result storage MUST preserve deterministic replay under concurrent SDK tool activity by relying on ordered append/write sequence metadata rather than arrival ambiguity. | Decomposition SOW-053; `docs/SPEC.md` Section 9.2 |
| DEL-05-05-REQ-010 | Output budget tests MUST verify that large outputs do not flood chat or model context and that medium/large outputs surface usable previews or artifact links. | `docs/PRD.md` NFR-017 and R4 acceptance (HASH_MISMATCH warning); decomposition anticipated artifacts |
| DEL-05-05-REQ-011 | ASSUMPTION: The implementation should expose `ToolResultStore` through a product-owned interface/module that is not SDK-shaped, because TYPES and PRD identify it as Chirality-owned policy. | `docs/TYPES.md` Section 7/8 glossary; `docs/PRD.md` Section 9.4 (HASH_MISMATCH warning) |
| DEL-05-05-REQ-012 | Output class byte thresholds, preview length, artifact naming scheme, checksum policy, and retention/deletion behavior are TBD until specified by implementation design or a governed source update. | Source gap in `docs/SPEC.md` Sections 8-9 and `docs/PRD.md` Section 10.5 |
| DEL-05-05-REQ-013 | The deterministic replay test for concurrent or interleaved tool-result completions MUST assert the accepted ordering signal: JSONL append/write sequence, `parentEventId` linkage where applicable, or another explicitly accepted event-ordering metadata field. | D-001; `docs/SPEC.md` Section 9.1-9.2; decomposition SOW-053 |
| DEL-05-05-REQ-014 | Threshold-boundary verification MUST be added when byte thresholds and preview limits are accepted; until then, tests may verify class behavior only through parameterized or fixture-specific policy inputs. | X-001; `docs/PRD.md` NFR-017 and R4 acceptance (HASH_MISMATCH warning); F-001 deferral |

#### Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Chirality `HarnessEvent` schema | Persisted runtime event metadata must use stable product-owned event shape. | `docs/SPEC.md` Section 9.1; `docs/PRD.md` Section 10.4 (HASH_MISMATCH warning) |
| Append-only JSONL event store | Artifact references must be compatible with ordered append/replay semantics. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
| Session layout contract | Artifact storage must fit canonical session folder layout. | `docs/SPEC.md` Section 8.2 |
| K-EVENT invariants | Binding audit, replay, redaction, and artifact-budget constraints. | `docs/CONTRACT.md` Section 1.5 |
| Working-root/project-truth boundary | Tool artifacts are runtime audit state, not accepted project truth or human approval records. | `docs/DIRECTIVE.md` Sections 2.3, 2.8 |

#### Verification

| Requirement IDs | Verification approach |
|---|---|
| REQ-001, REQ-002, REQ-003 | Unit tests for session path resolution, relative artifact references, and event metadata persistence under `.chirality/sessions/<sessionId>/`. |
| REQ-004, REQ-010 | Output budget tests covering small inline, medium preview plus metadata, and large artifact-only raw storage. Threshold values are TBD. |
| REQ-005 | Metadata fixture tests asserting tool name, turn ID, byte count, truncation flag, and relative artifact path. |
| REQ-006, REQ-007 | Redaction tests using provider errors, run logs, event data, and tool-result payload fixtures with secret-like values. |
| REQ-008 | Replay tests using valid JSONL followed by a malformed trailing line; valid prior artifact links must remain available. |
| REQ-009, REQ-013 | Deterministic ordering tests using concurrent or interleaved tool-result completion fixtures; assertions must bind replay order to write sequence or accepted event-ordering metadata rather than completion-arrival ambiguity. |
| REQ-011 | Conformance/type tests ensuring public event/API contracts remain provider-neutral and not SDK-shaped. |
| REQ-012 | Human/design review before finalizing thresholds, preview limits, naming, checksums, and retention policy. |
| REQ-014 | Threshold-boundary tests added after threshold and preview-limit acceptance; current validation remains `TBD` for exact boundary values. |

#### Documentation

Required implementation artifacts for this deliverable:

- Artifact store implementation or module path: TBD.
- Output budget tests for inline/preview/artifact behavior.
- Metadata fixtures covering required artifact metadata fields.
- Replay fixtures with artifact references and malformed-tail JSONL tolerance.
- Redaction fixtures for sensitive tool output handling.
- Developer notes identifying threshold values and any residual risks once chosen.
- P3 disposition record for B-001, C-001, F-001, D-001, X-001, and E-001 showing which items were incorporated, deferred as `TBD`, or surfaced for human ruling.
