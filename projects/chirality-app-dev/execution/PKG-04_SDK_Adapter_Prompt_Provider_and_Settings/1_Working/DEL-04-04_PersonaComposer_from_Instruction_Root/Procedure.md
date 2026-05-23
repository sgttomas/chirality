# Procedure: DEL-04-04 PersonaComposer from Instruction Root

## Purpose

Provide an operational path for implementing and verifying the PersonaComposer slice so it replaces stub prompt behavior with deterministic, source-grounded prompt composition from instruction-root governance, active persona, working-root policy, mode, and permitted tool-surface inputs.

## Prerequisites

| Item | Requirement / Status | Source |
|---|---|---|
| Instruction root | Must be readable and contain required governance and agent resources. | `docs/SPEC.md` Section 1.1 |
| Working root | Must remain separate from the instruction root and provide contextual project-root information only. | `docs/SPEC.md` Section 1.2; `docs/DIRECTIVE.md` Section 2.7 |
| Persona alias vocabulary | Use or delegate the accepted alias mappings. | `docs/TYPES.md` Section 3.4 |
| Runtime mode/tool policy | Use resolved mode and permitted tool-surface inputs supplied by the runtime/options layer. | `docs/SPEC.md` Sections 13-15 |
| Upstream dependencies | TBD - no accepted upstream dependency edges have been extracted. | `_DEPENDENCIES.md` |
| Source-state warning | Treat `docs/PRD.md` hash mismatch as a warning; do not rely on PRD-only details without confirmation. | `_REFERENCES.md` REF-006 |

## Steps

1. Confirm target boundaries.
   Verify the implementation remains in the prompt/persona composition slice and does not absorb SDK option building, SDK message mapping, provider key/network handling, or instruction-root packaging conformance.

2. Define PersonaComposer inputs.
   Include at minimum selected persona, normalized project root or working-root summary, mode, permitted tool surface, governance preface source, persona instruction content source, and available fingerprint-policy inputs. Mark unresolved fields `TBD` rather than inventing interfaces.

3. Resolve persona identity.
   Normalize aliases according to accepted vocabulary or delegate to the accepted alias resolver. Resolve the canonical persona to `agents/AGENT_<persona>.md`. Missing persona behavior should produce a typed failure; exact token `PERSONA_NOT_FOUND` is PRD-derived and requires confirmation against an accepted PRD snapshot.

4. Read instruction-root content.
   Read required governance preface material and selected agent instruction content from the instruction root. Do not write to the instruction root. Preserve instruction-root path protection as runtime policy, not prompt convention.

5. Compose prompt material deterministically.
   Build a stable ordered prompt from governance preface, selected persona instruction, working-root boundary/summary, mode policy, permitted tool surface, and professional-boundary reminders. Omit unavailable optional sections in a documented stable way or mark them `TBD` in tests/fixtures.

6. Preserve policy boundaries.
   Ensure prompt text describes mode/tool posture but does not claim to enforce permissions. Runtime enforcement must remain with SDK options, denied tools, `canUseTool`, hooks, path containment, and Chirality overlays.

7. Produce boot fingerprint inputs.
   Normalize and hash supported inputs such as persona content, governance preface, mode, visible SDK tool names/versions, permission-policy version, settings-source posture, MCP server versions, and subagent policy version. Where an input is not yet available from adjacent slices, record it as `TBD` or an explicit optional field.

8. Integrate with the runtime boundary.
   Pass composed prompt material and fingerprint metadata to the product-owned runtime boundary without making public APIs, `UIEvent`, `HarnessEvent`, or session storage SDK-shaped.

9. Add tests.
   Add persona content hash tests, fingerprint sensitivity tests, missing persona tests, alias tests or resolver-delegation tests, prompt section inclusion tests, and checks that API keys/transcripts/local presets do not become prompt authority.

10. Record unresolved dependencies.
   If implementation depends on DEL-04-02 tool-surface shape, DEL-08-01 instruction-root integrity, or DEL-08-02 alias routing, record the dependency explicitly for extraction rather than encoding a silent local assumption.

## Verification

| Check | Expected Result |
|---|---|
| Four-document consistency | Datasheet, Specification, Guidance, and Procedure use the same deliverable identity and source-state warning. |
| Persona resolution | Canonical personas resolve to instruction-root `AGENT_*.md`; missing personas fail in a typed way. |
| Prompt contents | Prompt includes governance preface, selected persona instruction, working-root boundaries, mode policy, permitted tool surface, and professional-boundary reminders. |
| Policy separation | Tests or review confirm prompt text is not used as the sole permission/path/tool enforcement boundary. |
| Fingerprint sensitivity | Fingerprint changes when supported prompt/policy inputs change. |
| Source-state handling | PRD-only claims remain warned, `TBD`, or `ASSUMPTION` until an accepted PRD snapshot is available. |

## Records

- Implementation artifact: `persona-composer.ts` or accepted equivalent.
- Tests: persona content hash tests, boot fingerprint tests, alias/missing-persona tests, prompt-content tests.
- Integration evidence: boot/session fingerprint metadata update.
- Open items: accepted dependency edges, exact runtime input interface, and accepted PRD snapshot confirmation.
