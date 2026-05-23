# Guidance: DEL-02-04 Toolkit Options and Local UI State

## Purpose

DEL-02-04 exists to make runtime options and local operator conveniences visible and usable without turning those conveniences into project truth. The slice supports OBJ-001 by preserving clear desktop-shell operator behavior and supports OBJ-004 where Toolkit options touch deterministic runtime option handling.

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-02-04, OBJ-001, OBJ-004; `docs/PRD.md` Sections 8.1, 8.4, 8.7.

## Principles

1. Treat local state as convenience, not authority.
   UI drafts, local presets, pane widths, SDK transcripts, API keys, runtime logs, and caches are non-authoritative unless governed project files import relevant content. Sources: `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3.

2. Keep governance stronger than UI choice.
   Toolkit settings and visible options may help the operator express intent, but they cannot override governance enforcement, permission policy, or project truth. Sources: `docs/PRD.md` Section 8.7 FR-042; `docs/SPEC.md` Section 7.4.

3. Prefer explicit warnings over silent behavior changes.
   Unknown option keys should warn and be ignored instead of mutating behavior. Storage failures should warn without breaking chat. Sources: `docs/PRD.md` Section 8.4 FR-024; Section 8.7 FR-043.

4. Preserve drafts for operator continuity, not approval.
   Draft and attachment-selection persistence improves recovery and retry behavior, but it does not approve work or create project truth. Sources: `docs/DIRECTIVE.md` Sections 2.3, 2.4, 2.6; `docs/PRD.md` Section 8.7 FR-043.

5. Make pane controls accessible.
   Resize/collapse affordances should be usable by keyboard users through focusable separators and keyboard behavior. Sources: `docs/PRD.md` Section 8.1 FR-005; Section 11.4 NFR-019.

## Considerations

- Runtime option controls should distinguish "operator selected," "runtime defaulted," and "governance enforced" states where the source model supports that distinction. Exact UI copy and state model are TBD.
- Local storage should degrade gracefully. A blocked quota, private-window limitation, or parse error should not make chat unusable; malformed records should be dropped and failures should warn. Source: `docs/PRD.md` Section 8.7 FR-043.
- The Toolkit should not imply that SDK or permission modes are prompt hints only. PRD FR-044 requires runtime enforcement once the permission policy engine exists.
- The PRD source is accessible but hash-mismatched against `_REFERENCES.md`; use it as directed by this task with warning, and avoid over-claiming details not present in the accessible text.
- PRD FR-006 points to `docs/ui/UI_POLISH_EXECUTION_PLAN.md` for polish acceptance, but that file was not accessible in the source tree during this P3 run. Treat dense, professional interface review as required with checklist location TBD rather than substituting an invented rubric.

## Trade-offs

| Trade-off | Guidance | Source |
|---|---|---|
| Convenience persistence vs. project truth | Persist pane widths, drafts, and presets locally, but never write them as authoritative deliverable state unless a governed import occurs. | `docs/DIRECTIVE.md` Section 2.6; `docs/SPEC.md` Section 1.3 |
| Rich Toolkit controls vs. runtime authority | Surface options that improve operator control, but let runtime fallback, validation, and permission policy remain authoritative. | `docs/PRD.md` Section 8.4 FR-023 and FR-024; Section 8.7 FR-042 and FR-044 |
| Strict local parsing vs. operator continuity | Drop malformed local records and warn on storage failures, but avoid breaking chat when local persistence fails. | `docs/PRD.md` Section 8.7 FR-043 |
| Keyboard support vs. compact shell layout | Keep resize/collapse controls accessible even in a dense desktop shell. | `docs/PRD.md` Section 11.4 NFR-019 |

## Examples

- Supported example: a user adjusts Toolkit max turns for one turn. The UI may submit that option, but runtime fallback and policy decide final behavior. Source: `docs/PRD.md` Section 8.4 FR-023; Section 8.7 FR-041.
- Supported example: a malformed local draft record is encountered. The UI drops the malformed record and continues with a warning if needed. Source: `docs/PRD.md` Section 8.7 FR-043.
- Supported example: pane widths persist locally after keyboard resize. Source: `docs/PRD.md` Section 8.1 FR-005; Section 11.4 NFR-019.
- Unsupported as project truth: a local Toolkit preset that attempts to bypass governance or override permission policy. Source: `docs/PRD.md` Section 8.7 FR-042; `docs/SPEC.md` Section 7.4.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-001 | `_REFERENCES.md` records a PRD SHA mismatch while the task instructs that the mismatch is a warning, not a blocker. | `_REFERENCES.md` REF-006 | Dispatch instruction for this TASK run | All sections citing `docs/PRD.md` | Use accessible PRD text with warning for this run; require later source-hash reconciliation before closure. Closure artifact and accountable resolver are TBD. | TBD |

## Rulings Needed

- Human ruling needed on PRD hash reconciliation before final package closure, because `_REFERENCES.md` expected and actual PRD hashes differ.
- Human ruling needed to name the accountable resolver and closure artifact for the PRD hash mismatch, such as an accepted reference refresh, source-snapshot ruling, or decomposition/package closure note.
- Human ruling needed if local presets should have a specific retention duration, storage namespace, or migration policy; no accessible source defines those details.
- Human ruling or downstream source needed for the missing UI polish checklist path referenced by PRD FR-006.
