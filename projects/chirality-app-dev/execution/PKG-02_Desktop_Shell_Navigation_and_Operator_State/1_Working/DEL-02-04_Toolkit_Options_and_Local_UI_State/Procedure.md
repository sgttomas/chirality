# Procedure: DEL-02-04 Toolkit Options and Local UI State

## Purpose

Define the operational steps to produce and verify the Toolkit Options and Local UI State UX/UI slice while preserving the non-authoritative status of local UI convenience state.

## Prerequisites

- Accepted source basis available locally:
  - `docs/DIRECTIVE.md`
  - `docs/CONTRACT.md`
  - `docs/SPEC.md`
  - `docs/TYPES.md`
  - `docs/PLAN.md`
  - `docs/PRD.md` with hash mismatch warning from `_REFERENCES.md`
  - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- Declared upstream dependencies: `_DEPENDENCIES.md` reports no accepted human-declared upstream dependency edges outside the extracted register. The extracted register is present and lists active source prerequisites plus `DEP-DEL-02-04-014` for TBD adjacent runtime option contracts and permission policy integration points.
- Runtime option contracts and permission policy integration points available from adjacent deliverables: TBD per `DEP-DEL-02-04-014`.
- ResponsibleParty: TBD.

## Steps

1. Confirm scope boundaries.
   - Include Toolkit controls, pane resize/collapse state, local draft/preset guards, and UI handling of runtime option fallback.
   - Exclude runtime engine internals and DEL-02-05 API key/error-feedback UI.
   - Sources: `_CONTEXT.md`; `docs/PRD.md` Sections 8.1, 8.4, 8.7.

2. Implement or review pane resize/collapse behavior.
   - Provide File Tree, Toolkit, and Chat pane resize/collapse affordances.
   - Support drag behavior and keyboard behavior, including Home collapse and End expand.
   - Persist widths locally.
   - Sources: `docs/PRD.md` Section 8.1 FR-005; Section 11.4 NFR-019.

3. Implement or review Toolkit per-turn option controls.
   - Expose model, tools, max turns, mode, persona, and governance metadata only as supported by runtime.
   - Treat exact component structure and labels as TBD until implementation files are selected.
   - Record the runtime-supported option inventory used by the UI, or explicitly mark unavailable controls as TBD/disabled.
   - Source: `docs/PRD.md` Section 8.7 FR-041.

4. Align Toolkit option handoff with deterministic runtime behavior.
   - Confirm model, tools, and max-turn fallback chains remain deterministic.
   - Confirm unknown option keys warn and are ignored.
   - Preserve test evidence that unknown keys do not silently mutate runtime behavior.
   - Sources: `docs/PRD.md` Section 8.4 FR-023 and FR-024; `docs/SPEC.md` Section 13.1.

5. Guard local presets and Toolkit settings.
   - Persist settings locally only as non-authoritative convenience state.
   - Confirm local presets cannot override governance enforcement or project truth.
   - Sources: `docs/PRD.md` Section 8.7 FR-042; `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3.

6. Guard drafts and attachment selections.
   - Persist chat drafts and attachment selections locally per root/persona/mode.
   - Drop malformed records.
   - Warn on storage failures without breaking chat.
   - Source: `docs/PRD.md` Section 8.7 FR-043.

7. Prepare permission-mode integration without overclaiming.
   - Map Toolkit mode controls to permission policy modes once the policy engine exists.
   - Mark enforcement as TBD until the policy engine and accepted enums/contracts are available.
   - Source: `docs/PRD.md` Section 8.7 FR-044.

8. Check professional and project-truth boundaries.
   - Confirm UI copy, tests, and implementation do not imply local state, presets, drafts, or agent outputs are approved project truth.
   - Sources: `docs/DIRECTIVE.md` Sections 2.3, 2.4, 2.6; `docs/PRD.md` Section 15 KG-015.

## Verification

| Check | Expected Result |
|---|---|
| Pane drag resize | File Tree, Toolkit, and Chat panes resize without layout breakage. |
| Pane keyboard resize/collapse | Resize handles are focusable; keyboard resize works where implemented; Home collapses; End expands. |
| Pane state persistence | Width/collapse state persists locally and remains non-authoritative. |
| Toolkit option controls | UI exposes only supported per-turn options or marks unsupported items as unavailable/TBD. |
| Deterministic option handoff | Runtime receives supported options; fallback behavior remains deterministic; unknown keys warn and are ignored. |
| Local preset authority | Presets do not write project truth and cannot override governance enforcement. |
| Draft/attachment local persistence | Records are keyed per root/persona/mode; malformed records are dropped; storage failures warn without breaking chat. |
| Permission-mode controls | If policy engine exists, controls map to enforced modes; if not, enforcement remains clearly TBD. |

## Records

- Toolkit controls implementation or review notes: TBD.
- Pane resize/collapse implementation or review notes: TBD.
- Draft/preset storage guard tests: TBD.
- Runtime option handoff tests, including unknown-key warning/ignore evidence: TBD.
- Accessibility checks for keyboard resize/collapse: TBD.
- Local-state non-authority tests for presets, drafts, attachment selections, fallback behavior, accessibility, and storage guards: TBD.
- Policy-mode mapping evidence after the permission policy engine exists: TBD.
- Human ruling on PRD hash mismatch reconciliation: TBD.
