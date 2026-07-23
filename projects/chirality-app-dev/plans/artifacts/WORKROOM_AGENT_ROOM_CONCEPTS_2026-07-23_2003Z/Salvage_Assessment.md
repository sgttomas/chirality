# Component Salvage Assessment

> **NON_AUTHORITATIVE — CONCEPT EVIDENCE**

**Evidence basis:** monorepo
`3c9ff297a4037d509bc930d1f607daf56769804d`; published application evidence
inspected separately and treated as non-authoritative.

## Current monorepo

| Surface | Disposition | Reason |
|---|---|---|
| Root provider composition | `REUSE` | Workspace, deliverable, toolkit, and harness-event providers are IA-neutral and must remain singleton owners above shell switching. |
| `app-shell.tsx` | `REWORK_MECHANICS` | Pointer and keyboard resizing, collapse behavior, and persisted geometry are valuable; current pane semantics and ordering are not the target architecture. |
| `layout-state.ts` | `REWORK_WITH_V2_MIGRATION` | Safe parsing/clamping is useful. Introduce a v2 workspace schema; retain v1 for forward migration and rollback. |
| `portal-loop-shell.tsx`, `loop-shell.tsx`, `loop-tertiary-shell.tsx` | `COMPATIBILITY_ONLY` | Preserve current routes and deep links during migration; they embody the chat-primary IA being replaced. |
| `shell-frame.tsx` | `REWORK` | Retain global project/settings affordances, but replace fixed surface taxonomy with workspace breadcrumbs/search/commands. |
| `workspace-sidebar.tsx` | `SPLIT_AND_REHOST` | Its child views are useful; the single overloaded tab strip is not. Separate Navigator, Agent Room, activity shelf, and inspectors. |
| `file-tree-panel.tsx` | `REWORK` | Keep bounded API and refresh safety; make selection open artifacts, centralize polling, and add keyboard tree semantics. |
| `document-view.tsx` | `REWORK` | Reuse deliverable/content APIs and Markdown renderer; move selection to Navigator and content to a persistent canvas. |
| `session-list-view.tsx` | `REWORK` | Keep list/replay clients and mid-turn guard; rename replay action honestly and project sessions in Agent Room. |
| Transcript/tool/subagent views | `REHOST_AS_DETAIL` | Preserve derived views as expandable evidence and activity-shelf detail, not primary navigation. |
| Pipeline/Workbench surfaces | `REHOST` | Preserve functional controls and query semantics; present them as contextual inspectors/action sheets. |
| Chat panel | `REHOST_AS_SUPPORT` | Keep streaming, drafts, interruption, permissions, and settings; make it summonable or contextual rather than the default canvas. |
| `globals.css` | `REUSE_TOKEN_FOUNDATION` | The restrained light-first system is materially closer to the desired professional calm than the published command-centre skin. |

## Published application evidence

| Surface | Disposition | Reason |
|---|---|---|
| `ResizableLayout.tsx` | `REDERIVE_CONCEPT` | Three-region composition, rails, and compact-mode thinking are useful; styling, chat anchoring, and missing width persistence are not. |
| `FilePreview.tsx` | `SALVAGE_ALGORITHM` | Unified-diff parsing, line numbering, context collapsing, and Markdown preview are strong candidates for adaptation with tests and accessible table semantics. |
| `FileTree.tsx` | `REDERIVE_SELECTIVELY` | Git overlays and lazy navigation are useful, but must be bound to current containment and working-root APIs. |
| `DashboardList.tsx` | `REDERIVE_INFORMATION_MODEL` | Deliverable roster/status as a navigable collection belongs in the Workroom; discard uppercase command-centre styling. |
| `HexGrid.tsx` | `REJECT_AS_PRIMARY_IA` | Hard-coded cell-to-agent navigation conflates model/persona taxonomy with the user's object of work. |
| Published polish plan | `HISTORICAL_EVIDENCE` | Its density findings remain helpful; its prohibition on IA change explains why it could not solve the current problem. |

## Shared design rules

- Reuse behavior and tested boundaries before markup or styling.
- Do not copy old absolute-path assumptions, provider logic, or credential UI.
- Do not create a second event or session store.
- Do not multiply working-root polling across regions.
- Retain accessible resizing, tab, tree, focus, and interruption behavior.
- Preserve physical integration ownership without transferring semantic
  responsibility across deliverables.
