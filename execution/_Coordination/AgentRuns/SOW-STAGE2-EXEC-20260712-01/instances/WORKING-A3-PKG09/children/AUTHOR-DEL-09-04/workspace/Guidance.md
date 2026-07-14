# Guidance: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

This deliverable makes release packaging explicit and repeatable for the current macOS-only target. Its job is not just to produce a DMG, but to prove that packaged Chirality preserves the instruction-root resource boundary and can execute the SDK subprocess/binary from the packaged layout.

## Principles

- Treat `desktop:dist` as release-significant. `docs/CONTRACT.md` K-VALIDATE-1 includes `desktop:dist` among checks required before release-significant changes are accepted.
- Keep the release target narrow. `docs/PRD.md` KG-014 and decomposition SOW-078 make Windows/Linux packaging out of scope without amendment.
- Treat instruction-root resources as package blockers. `docs/SPEC.md` Section 1.1 says missing required instruction-root assets are a P0 packaging and runtime-readiness blocker.
- Preserve Chirality-owned boundaries in packaged form. Packaged validation should still exercise instruction-root integrity, working-root availability, current shipped Anthropic network guardrails, and SDK package execution.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

## Considerations

- The instruction-root required asset set includes `AGENTS.md`, `README.md`, `agents/`, `docs/`, core docs, and root-level assets where packaging/integrity policy requires them. If the code-level integrity manifest differs from this list, record the difference as a conflict or source-completeness blocker rather than silently passing packaging readiness.
- SDK subprocess packaging is an empirical check. `docs/PRD.md` KG-025 flags potential needs such as `asarUnpack`, signing, environment, or path adjustments; the accepted result must come from a probe or build evidence, not from configuration review alone.
- The integrity summary path is part of expected packaging evidence: `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`.
- The unsigned/adhoc local-builder DMG posture is acceptable only because `docs/CONTRACT.md` K-RELEASE-1 and `docs/PRD.md` Section 6.2 define that as the current release target. A notarized distribution target would require scope amendment rather than silent tightening of this deliverable.
- Release evidence should be reviewable without rerunning the build: command transcript, artifact listing or checksum, integrity summary, first-adapter probe output, and blocker list need stable paths or attachment identifiers.
- `ASSUMPTION: PACKAGE_HEURISTIC` associates OBJ-008 because the decomposition maps this deliverable through PKG-09 and SOW-072/SOW-073, but no human has assigned a hard objective-specific owner.

## Trade-offs

| Trade-off | Guidance |
|---|---|
| Strict asset completeness vs. build progress | Prefer failing readiness with a documented blocker when required instruction-root assets are absent. Do not weaken integrity requirements without a governed amendment. |
| `app.asar` packing convenience vs. SDK executable access | Prefer package layout that allows the SDK subprocess/binary to be found and executed. If `asar` trapping prevents execution, record the packaging probe failure and adjust packaging under this deliverable. |
| Local unsigned DMG vs. notarized distribution | Keep unsigned/adhoc posture for current scope. Notarization is outside this deliverable unless scope changes. |
| General release checklist vs. DEL-09-04 scope | Keep CI artifact upload and broader release workflow details in DEL-09-05 unless directly needed to prove the DMG/instruction-root/SDK packaging result. |

## Examples

TBD: No source-backed example transcript or accepted packaging probe output is available in the local reference corpus for this deliverable.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| DEL-09-04-CONF-001 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006 | Assignment override | All PRD-backed requirements | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | TBD — reconciled under D-APP-38 |
| DEL-09-04-CONF-002 | Required instruction-root assets may be incomplete in current source or package state. | `docs/SPEC.md` Section 1.1; `docs/PRD.md` Section 10.1 | Decomposition OI-004 | Specification requirements, Procedure verification | Treat missing assets as P0 readiness blocker until completed or amended. | TBD |
| DEL-09-04-CONF-003 | The accepted authority for the required instruction-root packaged asset set must be explicit when code-level integrity manifests differ from policy-level required assets. | `docs/SPEC.md` Section 1.1; `docs/PRD.md` FR-058 | Code-level integrity manifest, location TBD | Specification requirements, Procedure verification | Treat policy-level required assets as readiness blockers unless a governed amendment narrows the manifest. | TBD |
| DEL-09-04-CONF-004 | Whether SDK-backed turn start after R1 is a DEL-09-04 closure blocker or deferred packaged-app validation needs human/source ruling. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 | `_CONTEXT.md` deliverable scope | Procedure packaged runtime guardrail check | Keep SDK subprocess/package-layout proof in scope; mark full packaged SDK-backed turn start as `TBD` until owner ruling. | TBD |
