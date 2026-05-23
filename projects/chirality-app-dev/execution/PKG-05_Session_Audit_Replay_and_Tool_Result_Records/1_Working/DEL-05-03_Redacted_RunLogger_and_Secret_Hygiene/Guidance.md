# Guidance: DEL-05-03 Redacted RunLogger and Secret Hygiene

## Purpose

DEL-05-03 exists to prevent API keys and configured secrets from becoming runtime audit content. The runtime audit mirror is intentionally rich enough for replay and diagnosis, so this deliverable supplies the redaction control that lets Chirality keep durable event, provider, SDK, tool, and run-log records without converting key material into project truth or persistent runtime leakage.

Primary evidence:

- `docs/CONTRACT.md` K-EVENT-6: runtime events, run logs, tool artifacts, and provider errors must redact secrets and avoid storing API keys.
- `docs/CONTRACT.md` K-KEY-1: API keys are non-project convenience state and must not be written to project files, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts.
- `docs/PRD.md` FR-075: runtime logging redacts API keys and configured secret variants from SDK errors, tool outputs where policy requires, and event records.

## Principles

1. Redact before persistence.
   Any provider, SDK, tool, or run-log payload that may be written to JSONL, artifacts, logs, error details, or diagnostics should pass through redaction before it crosses the persistence boundary.

2. Keep the audit useful.
   Redaction should remove secret values while preserving non-secret diagnostic structure such as error class, status, source, policy category, event type, byte counts, truncation flags, and artifact references.

3. Treat API keys as non-project convenience state.
   API keys can be resolved from UI safeStorage or environment variables for active turns, but they must not become project files, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts.

4. Keep SDK artifacts secondary.
   SDK transcripts and metadata are resume/debug artifacts. The Chirality audit mirror remains the product-owned record, and SDK-shaped values should be retained only as adapter metadata where source contracts permit it.

5. Prefer shared redaction over isolated patches.
   Current code contains provider-local redaction behavior. ASSUMPTION: the deliverable should consolidate product-wide redaction behavior into a shared helper used by provider error handling, run logging, event emission, and tool artifact handling.

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| Provider errors | Preserve typed `SDK_FAILURE` classification while redacting key material and configured secret variants. | `docs/PRD.md` FR-034 |
| Event records | `HarnessEvent.data` may be rich but must not contain secrets. | `docs/SPEC.md` Section 9 |
| SDK stderr/debug logs | Treat as potentially sensitive and route through the run logger redaction layer. | `docs/PLAN.md` Section 6.3; `docs/PRD.md` runtime notes |
| Tool results | Do not rely on truncation alone for sensitive values. Apply redaction or withhold sensitive raw values before inline event payloads or artifact storage. | `docs/PRD.md` Section 10.5 |
| Secret variants | The PRD names API keys and configured secret variants but does not define the configuration schema. Keep schema-specific claims as TBD until implementation is decided. | `docs/PRD.md` FR-075 |
| PRD source state | `docs/PRD.md` has a HASH_MISMATCH in `_REFERENCES.md`; use it as accessible source context with warning, not as an unchecked sole authority. | `_REFERENCES.md`; human runtime instruction |

## Trade-offs

| Trade-off | Direction |
|---|---|
| Strict redaction vs diagnostic detail | Prefer strict redaction of values while retaining typed, non-secret metadata for debugging. |
| Inline tool result convenience vs leakage risk | Prefer preview/metadata/artifact references and redaction over raw inline content when sensitivity is possible. |
| Product-owned audit vs SDK transcript completeness | Keep Chirality JSONL canonical; use SDK transcript linkage as secondary metadata, not as a replacement. |
| Provider-local helper vs shared helper | Prefer a shared helper once this deliverable is implemented; keep provider-specific handling only where source payload shapes require it. |

## Examples

TBD: final examples should be generated from accepted fixtures after implementation. Candidate examples:

- Provider auth error containing a configured API key is stored as typed `SDK_FAILURE` details with the key replaced by the accepted redaction token.
- SDK stderr line containing an encoded key variant is logged with the encoded variant redacted.
- Tool result containing a secret-like configured value is not persisted as raw inline `HarnessEvent.data`; the event stores redacted preview and metadata or withholds the payload according to policy.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| None | No direct source conflict found. Source-state warning remains for `docs/PRD.md` HASH_MISMATCH. | `_REFERENCES.md` | Human runtime instruction | All documents using PRD evidence | Use PRD as accessible source with warning; do not derive unsupported details from it alone. | TBD |
