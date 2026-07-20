# Affinity and Mapping Analysis

## Result

The D-APP-56 R4-P48 affinity containers were useful search partitions but did
not survive as a uniform ownership answer. They remain prior agent evidence,
never authority. Current source structure, direct call sites, tests, accepted
deliverable scopes, and D-APP-68 boundaries support the following proposal
families.

| Proposal family | Paths | Nearest mapping or boundary |
|---|---:|---|
| Shell, navigation, and shared presentation | 4 | DEL-02-01 for `page.tsx` and `navigation-intent.ts`; DEL-02-01 primary with DEL-02-03 consumer for `chat-markdown.tsx` and its sole-imported `ansi.ts` helper |
| Working-root document UX | 4 | DEL-02-03 for `document-view.tsx`, `file-picker.tsx`, `document-view-state.ts`, and renderer selector typing; FilePicker retains DEL-02-04 attachment UI state and DEL-09-06/server enforceable attachment security |
| Runtime replay/projection | 6 | DEL-05-04 nearest for session, tool, subagent, event-provider, buffer, and view-model behavior; the provider retains a shared-application-infrastructure owner alternative, while the view-model module retains split-file and ownerless/shared utility alternatives |
| Shared shell stylesheet | 1 | DEL-02-01 integration lead only, with ownerless/shared physical-file and capability-level-split alternatives plus explicit DEL-02-02, DEL-02-03, DEL-02-04, DEL-02-05, DEL-05-04, DEL-06-01, DEL-08-02, DEL-08-05, and DEL-09-06 capability boundaries and the DEL-02-02/DEL-08-03 Pipeline-selector boundary retained |
| Working-root content API | 1 | unresolved shared boundary, nearest DEL-07-03 with DEL-07-01 containment and DEL-02-03 consumption |
| Tool-catalog generator | 1 | DEL-06-02 mechanism only; generated semantics stay with their ruled owners |
| Electron bridge integration | 1 | `preload.ts` requires a physical-file integration-owner ruling across DEL-02-03, DEL-02-05, and DEL-09-06; its separate renderer typing path is counted in Working-root document UX |
| SDK/network proof | 1 | DEL-09-06 primary, DEL-04-01 evidence interest |
| Harness-contract dependency lint | 1 | DEL-03-01 semantic owner, DEL-09-05 validation consumer |
| PEC evidence tools | 2 | DEL-10-04 primary, DEL-10-03 proposal-tool verification interest |

The family counts total 22. Exact accounting remains the 22-row ledger and
proposed mapping CSV.

## Material alternatives and rejection rationale

- Directory or affinity-container ownership was rejected wherever the file's
  dominant behavior aligned more closely with another accepted deliverable.
- DEL-02-01 remains shell host but is not proposed as semantic owner of
  working-root document discovery or runtime replay projections.
- The fresh production graph has exactly ChatPanel and DocumentView consuming
  ChatMarkdown, and exactly ChatMarkdown importing `ansi.ts`. DEL-05-04 was
  therefore rejected for both paths; transcript/output analogy is not a
  caller or interface edge.
- DEL-02-01's proposed `globals.css` integration lead does not absorb the
  material Pipeline/Workbench, API-key, or other enumerated capability
  regions. The source's `DEL-02-06` API-key heading is stale; DEL-02-05 is the
  current capability boundary. Ownerless/shared physical-file treatment and
  a capability-level split before assigning a path lead remain materially
  distinct owner choices and are not adjudicated here.
- FilePicker remains DEL-02-03-primary read-only browsing. DEL-02-04 retains
  attachment UI state and DEL-09-06/server routes retain enforceable
  attachment security. DEL-06-04 write/edit enforcement is rejected as a
  substitute; no separate current FilePicker relationship was evidenced.
- DEL-05-02 remains event-schema/persistence owner; it does not absorb
  in-memory replay and presentation mechanics assigned in the proposal to
  DEL-05-04.
- `harness-events-provider.tsx` retains a shared application infrastructure
  owner as an explicit alternative to DEL-05-04 because its root mount and
  consumers cross shell, navigation, replay, transcript, tool, subagent, and
  permission surfaces.
- `harness-event-views.ts` retains both splitting the file by capability owner
  and ownerless/shared projection-utility treatment as physical-owner
  alternatives. Its semantic capability boundaries do not answer that
  physical-file choice.
- DEL-08-05 remains child-run lifecycle/artifact owner; it is not proposed as
  owner of the read-only subagent stream projection.
- DEL-05-05 remains ToolResultStore and ordinary result-budget owner; the
  tool-stream projection does not transfer those semantics.
- DEL-09-04 consumes packaging evidence but does not thereby own Electron
  feature contracts, a development-only network fixture, or a contract lint.
- DEL-10-03 owns proposal-tool implementation; PEC fixture/rehearsal evidence
  is nearer DEL-10-04 without transferring the generic handler.

## Preserved ambiguities and observations

1. `preload.ts` genuinely combines multiple feature boundaries; no single
   accepted physical-file integration owner was found.
2. The working-root content route is robust and containment-safe, but the
   route contract itself is not explicitly located in current scope truth.
3. `chirality-window.d.ts` declares `selectDirectory` but omits the preload
   `apiKey` surface. This is an implementation observation, not authorized
   repair scope.
4. `frontend/docs/harness/adding_a_tool.md` cites pre-package-move paths while
   the catalog contract now lives under `frontend/packages/harness-contract/`.
5. `run-network-policy-proof.mjs` retains stale historical deliverable-root
   metadata. It was not repaired.
6. V1-001 through V1-003 were repaired by a fresh 14-row DEL-02-01 read. The
   resulting mappings remain owner-class proposals pending fresh V1 recheck.
7. V1R-001 and V1R-002 were repaired through exact sealed-child fan-in. The
   complete comparison and the 5 exact / 5 faithful-compression / 4 repaired-
   material-loss accounting are in `DEL02_01_CHILD_PACKAGE_FIDELITY.csv`.
8. The v8 control-label erratum remains
   `NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED`; current execution uses
   only the exact manifest paths.

These findings remain evidence for V1 and an owner; they do not expand the
22-path scope.
