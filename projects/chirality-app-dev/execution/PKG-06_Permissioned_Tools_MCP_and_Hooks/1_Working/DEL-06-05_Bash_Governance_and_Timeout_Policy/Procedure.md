# Procedure: DEL-06-05 Bash Governance and Timeout Policy

## Purpose

This procedure describes how to produce and verify the DEL-06-05 Bash governance implementation and timeout/capture policy evidence. It is written for the deliverable artifact, not as an end-user shell runbook.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Accepted DEL-06-05 scope and source references | Available in `_CONTEXT.md` and `_REFERENCES.md` |
| Binding Bash invariant | Available in `docs/CONTRACT.md` Section 1.6 K-BASH-1 |
| Permission/mode vocabulary | Available in `docs/TYPES.md` Section 8 and `docs/SPEC.md` Section 15.1 |
| Tool-surface rules | Available in `docs/SPEC.md` Section 14.3 |
| R4 sequencing and acceptance criteria | Available in `docs/PLAN.md`; `docs/PRD.md` is warning-qualified due to HASH_MISMATCH |
| Declared upstream dependencies | TBD - `_DEPENDENCIES.md` lists no accepted upstream edges yet |
| Exact implementation file paths | TBD |
| Exact test fixture paths | TBD |
| Bash-specific numeric timeout default and maximum | TBD - required by policy but not specified in accessible sources |

## Steps

1. Establish the default-deny posture.
   - Ensure SDK `Bash` is not exposed by default.
   - Add explicit denial for Bash in `readOnly` and `dontAsk`.
   - Verify denial is enforced by runtime policy, not prompt text.

2. Resolve Bash tool exposure through the permission overlay.
   - Treat SDK `Bash` as a governed tool candidate, not as automatically available.
   - Apply `disallowedTools`, permission mode, Chirality policy, hooks, and `canUseTool` mediation as applicable.
   - Do not rely on `allowedTools` as a restriction mechanism.

3. Implement Bash preflight.
   - Require explicit mode or session capability that permits Bash.
   - Require a timeout policy before execution.
   - Require stdout/stderr capture plan.
   - Require result storage or preview policy for medium/large outputs.
   - Require audit metadata sufficient to record permission, start, terminal outcome, and artifact references.
   - ASSUMPTION: command metadata and network posture checks are part of Bash preflight because PRD R4 says the Bash `PreToolUse` hook enforces them; this is PRD HASH_MISMATCH warning-qualified.

4. Enforce denied-never-spawns.
   - Place denial checks before process creation.
   - Instrument tests or runner seams so a denied Bash request proves no child process was started.

5. Execute governed Bash only after preflight passes.
   - Start the process with the resolved timeout.
   - Capture stdout and stderr separately.
   - Track exit code, timeout, interruption, cancellation, and failure classifications where available.
   - Redact secrets from logs, tool outputs, and event records where policy requires.

6. Store and summarize output.
   - Inline only small safe outputs.
   - Preview medium/large outputs.
   - Store raw large outputs under session artifacts and persist safe metadata such as artifact path, byte counts, truncation status, and channel labels where the accepted schema permits.
   - Exact metadata schema: TBD.

7. Persist audit evidence.
   - Persist permission evidence before allowing execution.
   - Persist tool started/completed/failed events and terminal success/failure/interruption/cancellation outcomes.
   - Keep SDK transcript linkage secondary to Chirality-owned event records.

8. Add tests and traceability.
   - Add default deny, `readOnly` deny, `dontAsk` deny, denied-never-spawns, timeout-required, stdout/stderr separation, output artifact metadata, and interruption tests.
   - Tag or name tests with DEL-06-05 or SOW-062 where local test conventions allow.
   - Record the PRD HASH_MISMATCH warning in implementation or review notes.

## Verification

| Check | Expected result |
|---|---|
| Default posture | Bash is denied or omitted with no explicit enablement. |
| `readOnly` behavior | Bash cannot execute. |
| `dontAsk` behavior | Bash denies without prompting. |
| `allowedTools` misconception | Tests show `allowedTools` cannot enable or restrict Bash by itself and cannot bypass deny policy. |
| Denied-never-spawns | Denied Bash request creates no child process. |
| Timeout preflight | Allowed Bash cannot start without a resolved timeout policy. |
| Capture channels | stdout and stderr are captured separately. |
| Output budget | Large output is stored as an artifact and represented by preview/metadata. |
| Interrupt behavior | Active Bash can be interrupted when supported, and terminal outcome is persisted. |
| Audit records | Permission, start, completion/failure/interruption, and artifact metadata are persisted in Chirality-owned event shape. |
| Hook fail-closed | Hook failure blocks shell execution. |
| PRD warning | PRD-derived details remain traceable to `_REFERENCES.md` HASH_MISMATCH until reconciled. |

## Records

- Bash governance policy or options-builder slice: TBD.
- Bash preflight hook or equivalent enforcement point: TBD.
- Timeout default and override policy: TBD.
- stdout/stderr capture evidence: TBD.
- Tool output artifact metadata fixture: TBD.
- Denied-never-spawns test evidence: TBD.
- Interruption/timeout terminal outcome test evidence: TBD.
- Review note for PRD HASH_MISMATCH: required until REF-006 source state is reconciled.
