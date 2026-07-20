# Technical Recheck Return

- **Verdict:** `BLOCK`
- **Basis:** `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- **Scope:** exact 22 paths in `CQF1_SCOPE.csv`
- **Role:** bounded read-only Agent 2 auditor
- **Delegation:** none
- **Tests/services:** none run; source, caller/import, test, scope, authority,
  Git-object, and derivative evidence was inspected read-only

## Outcome

V1-001 through V1-003 are repaired, and the v8 control-label erratum is
nonconsequential: execution targeted the two exact manifest paths and their
sealed source objects. The other 19 previously supportable row conclusions
also remain technically supportable at the frozen source state.

The repaired derivative nevertheless fails fresh-child fidelity on
`frontend/src/components/shell/file-picker.tsx`. The accepted fresh child
retains DEL-02-04 attachment UI state and DEL-09-06/server-side attachment
security as boundaries, but the integrated ledger, mapping, and owner slate
replace DEL-09-06 with DEL-06-04 path enforcement. That substitution is not
supported by the fresh child or the governing scopes and makes row 6 and
owner group 2 materially misleading. Three additional fresh-child rows lose
material physical-ownership alternatives during compression into the
integrated package: the shared/split stylesheet treatments, an explicit shared
infrastructure owner for the event provider, and split/shared treatments for
the multi-capability event-view projections. Those losses do not falsify the
proposed nearest candidates, but they make the owner choices incomplete. They
require reconciliation repair and a fresh V1 recheck; no source-code repair is
authorized.

## Basis, population, and source bindings

- `HEAD` equals the frozen basis.
- Manifest: 22 rows, 22 unique paths, 22 existing paths, exact frozen order.
- Ordered newline-terminated path-list SHA-256:
  `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`.
- Ledger population and order match the manifest 22/22.
- Every ledger source binding was independently recomputed: 22/22 Git blobs
  and 22/22 SHA-256 values match the basis and current bytes.
- Subject diff against the basis: empty for all 22 paths.
- Repaired package bindings inspected by this audit match the declared
  ledger, mapping, slate, analysis, notes, QA, and handoff hashes.

## V1-001 through V1-003

### V1-001 — `globals.css`: `ACCEPT`

`frontend/src/app/layout.tsx:1-24` imports the exact
`frontend/src/app/globals.css` file. Direct inspection confirms material
Pipeline/Workbench rules at `globals.css:1215-1425`, API-key settings/status/
error rules at `globals.css:1631-1724`, and the other shell, Working Root,
pane/toolkit, session/projection, persona, child/tool, mode/permission, and
attachment/renderer-related regions listed by the fresh child. The repaired
row and group 1 expressly retain DEL-02-02 and DEL-02-05 along with the other
material capability boundaries and propose DEL-02-01 only as integration
lead, without semantic transfer. The stale source heading `DEL-02-06` at line
1631 is correctly treated as evidence, not authority.

### V1-002 — `chat-markdown.tsx`: `ACCEPT`

The complete production-import graph is exactly:

1. `chat-panel.tsx:25,497-506`; and
2. `document-view.tsx:6,179-205`.

Repository-wide production import/use inspection found no third consumer.
`transcript-stream-view.tsx` renders derived event text directly and does not
import ChatMarkdown. The repaired child, ledger, mapping, analysis, notes, and
group 1 consistently propose DEL-02-01 primary plus a DEL-02-03 consumer edge
and reject a DEL-05-04 current-consumer edge.

### V1-003 — `ansi.ts`: `ACCEPT`

The complete production-import graph is one direct importer:
`chat-markdown.tsx:6,30-50`. Its transitive production consumers are therefore
ChatPanel and DocumentView only. No replay parser, session replay surface, or
transcript projection imports either ANSI or ChatMarkdown on this basis. The
repaired artifacts consistently propose DEL-02-01 primary with a DEL-02-03
consumer edge, retain deliberately shared presentation utility as an
alternative, and reject DEL-05-04 absent a real call/interface edge.

## Blocking finding

### TR-001 — FilePicker fresh-child boundary was replaced during fan-in

- **Severity:** material / decision-slate blocking
- **Affected row:** 6, `frontend/src/components/shell/file-picker.tsx`
- **Affected group:** 2, Working-root document UX

The fresh R1-REPAIR child states:

> DEL-02-03 primary for Working Root file browsing; DEL-02-04 retains
> attachment UI state and DEL-09-06/server routes retain enforceable security
> boundaries.

It also lists DEL-09-06 attachment security as a competing candidate and says
client prefix checks are not the enforceable security owner. That conclusion
is supported by the source: FilePicker is a read-only UI browser over
`/api/working-root/tree` (`file-picker.tsx:73-117`), applies only client-side
navigation checks (`:30-49,194-205,247-260`), filters attachment extensions
and emits client metadata (`:143-173,234-292`), and is imported only by
ChatPanel (`chat-panel.tsx:26,533-581,635-645`). DEL-09-06 explicitly covers
server-side attachment path/type/symlink/readability/size validation and
states that client attachment metadata is non-authoritative
(`DEL-09-06 ScopeOfWork.md:71,84,144-158`). DEL-02-03 owns the bounded
file-tree UI/API consumption, while DEL-02-04 retains local attachment state.

The integrated artifacts instead say:

- ledger: `DEL-02-04 attachment persistence; DEL-06-04 path enforcement`;
- proposed mapping: the same DEL-02-04/DEL-06-04 boundary; and
- candidate slate group 2: retain DEL-02-04 attachment persistence and
  DEL-06-04 path enforcement.

DEL-06-04 governs write/edit mutation gates and path hooks, not this read-only
attachment picker or the server-side attachment-validation boundary
(`DEL-06-04 ScopeOfWork.md:120,149-164`). The substitution is both a direct
fresh-child disagreement and a material semantic-boundary change. `QA.md`
nevertheless reports the fresh child as accepted and the fan-in as passing.

**Required repair:** RECONCILIATION must re-fan-in FilePicker from the accepted
fresh child; restore DEL-09-06/server-side attachment security and DEL-02-04
UI-state boundaries, remove DEL-06-04 unless new direct evidence justifies a
separate relationship, and update the ledger, proposed mapping, candidate
slate group 2, analysis, DEL-02-01 package note, QA, handoff, and all hashes.
The repaired derivative then needs a fresh independent V1 recheck.

### TR-002 — Three material physical-ownership alternatives were dropped

- **Severity:** material / decision-slate blocking
- **Affected rows:** 1, 10, and 14
- **Affected groups:** 1 and 3

The fresh child identifies technically viable physical-ownership treatments
that are not equivalent to the semantic-capability boundaries substituted
into the integrated ledger's `CompetingCandidates` field:

1. `globals.css`: ownerless/shared physical file and capability-level split
   are alternatives to DEL-02-01 integration leadership. The integrated row
   lists styled semantic owners instead, and group 1 only directs designation
   of DEL-02-01. The semantic boundaries are preserved, but the physical-file
   ownership choices are not.
2. `harness-events-provider.tsx`: an explicit shared-application-
   infrastructure owner is a viable alternative because RootLayout mounts the
   provider and eight production consumers span shell, navigation, replay,
   transcript, tool, subagent, and permission surfaces. The integrated row
   retains only DEL-05-02 and DEL-02-01 as competitors.
3. `harness-event-views.ts`: splitting the tool/permission/subagent exports or
   treating the module as an ownerless shared projection utility are viable
   alternatives to DEL-05-04 integration ownership. The integrated row
   instead lists the semantic capability owners that the child expressly
   distinguishes from physical-file ownership; group 3 does not present the
   split/shared choices.

These are not mere wording changes: each changes who, if anyone, owns the
physical integration path while retaining the same semantic capability
owners. Their omission is material to the owner question even though the
DEL-02-01 and DEL-05-04 nearest proposals remain supportable.

**Required repair:** carry these physical-owner alternatives into the ledger,
mapping/slate decision context, analysis, affected package note, QA, and
handoff, or explicitly reject each with evidence. Recompute hashes and rerun
V1. No source split or ownership act is authorized.

## Fresh-child-to-package fidelity matrix

| Fresh-child row | Integrated fidelity | Disposition |
|---:|---|---|
| 1 `globals.css` | Candidate and semantic boundaries retained; ownerless/shared and capability-split physical treatments dropped | `MATERIAL_LOSS` — TR-002 |
| 2 `page.tsx` | Weak DEL-02-03/ownerless alternatives compressed to `none material` after direct root-shell evidence | `HARMLESS_COMPRESSION` |
| 3 `chat-markdown.tsx` | Primary, DEL-02-03 consumer, shared alternative, and DEL-05-04 rejection retained | `FAITHFUL` |
| 4 `document-view.tsx` | DEL-02-03 candidate plus content-route and shell-host boundaries retained | `FAITHFUL` |
| 5 `file-picker.tsx` | DEL-09-06/server-security boundary replaced by DEL-06-04 write/edit enforcement | `ALTERED_BOUNDARY` — TR-001 |
| 6 `session-list-view.tsx` | DEL-05-04 candidate and DEL-05-01/DEL-02-01 boundaries retained | `FAITHFUL` |
| 7 `subagent-stream-view.tsx` | DEL-08-05 boundary retained; generic shell-host alternative omitted | `HARMLESS_COMPRESSION` |
| 8 `tool-stream-view.tsx` | DEL-05-05 and DEL-06 boundaries retained; generic shell-host alternative omitted | `HARMLESS_COMPRESSION` |
| 9 `harness-events-provider.tsx` | Candidate and semantic boundaries retained; explicit shared-infrastructure owner dropped | `MATERIAL_LOSS` — TR-002 |
| 10 `ansi.ts` | Caller graph, candidate, shared alternative, and DEL-05-04 rejection retained | `FAITHFUL` |
| 11 `document-view-state.ts` | Candidate and sole-consumer basis retained | `FAITHFUL` |
| 12 `harness-event-buffer.ts` | DEL-05-02 boundary retained; generic shell-host alternative omitted | `HARMLESS_COMPRESSION` |
| 13 `harness-event-views.ts` | Semantic owners retained, but split-file and ownerless/shared physical treatments dropped | `MATERIAL_LOSS` — TR-002 |
| 14 `navigation-intent.ts` | DEL-08-02 boundary retained; generic ownerless-utility alternative omitted under a sole concrete caller | `HARMLESS_COMPRESSION` |

Thus five rows are faithful, five contain harmless compression, three lose
material alternatives, and one alters a material boundary. No other fresh-
child disagreement or stale source binding was found.

## Exact 22-row technical disposition and consumer evidence

| # | Path | Direct production consumer/import/invocation evidence | Disposition |
|---:|---|---|---|
| 1 | `frontend/src/app/globals.css` | imported once by `src/app/layout.tsx` | `BLOCK_FANIN_ALTERNATIVES` — V1-001 boundaries repaired, TR-002 remains |
| 2 | `frontend/src/app/page.tsx` | Next root route; directly renders `PortalLoopShell` | `ACCEPT` |
| 3 | `frontend/src/app/api/working-root/deliverable/content/route.ts` | fetched by `DocumentView`; delegates to `readDeliverableContent` | `ACCEPT` — DEL-07-03 nearest with DEL-07-01/DEL-02-03 boundaries and unresolved route owner is honest |
| 4 | `frontend/src/components/shell/chat-markdown.tsx` | exactly ChatPanel and DocumentView | `ACCEPT` — V1-002 repaired |
| 5 | `frontend/src/components/shell/document-view.tsx` | imported only by WorkspaceSidebar; fetches roster/content routes | `ACCEPT` — DEL-02-03 dominant behavior supported |
| 6 | `frontend/src/components/shell/file-picker.tsx` | imported only by ChatPanel; consumes tree API and attachment helpers | `BLOCK` — TR-001 lossy fan-in |
| 7 | `frontend/src/components/shell/session-list-view.tsx` | imported by WorkspaceSidebar; calls session list/replay and provider hydrate actions | `ACCEPT` — DEL-05-04 view/replay with DEL-05-01 storage boundary supported |
| 8 | `frontend/src/components/shell/subagent-stream-view.tsx` | imported by WorkspaceSidebar; consumes provider plus `deriveSubagentActivity` | `ACCEPT` — projection/DEL-08-05 semantic split supported |
| 9 | `frontend/src/components/shell/tool-stream-view.tsx` | imported by WorkspaceSidebar; consumes provider plus `deriveToolActivity` | `ACCEPT` — projection/result-policy split supported |
| 10 | `frontend/src/components/workspace/harness-events-provider.tsx` | mounted by RootLayout; hooks consumed by ChatPanel, AgentMatrix, PortalLoopShell, SessionList, Transcript, Tool, Subagent, and PermissionRequests | `BLOCK_FANIN_ALTERNATIVES` — nearest mapping supported, TR-002 remains |
| 11 | `frontend/src/lib/shell/ansi.ts` | exactly ChatMarkdown | `ACCEPT` — V1-003 repaired |
| 12 | `frontend/src/lib/shell/document-view-state.ts` | exactly DocumentView | `ACCEPT` — DEL-02-03 supported |
| 13 | `frontend/src/lib/shell/harness-event-buffer.ts` | exactly HarnessEventsProvider | `ACCEPT` — DEL-05-04 buffer / DEL-05-02 persistence split supported |
| 14 | `frontend/src/lib/shell/harness-event-views.ts` | ToolStreamView, SubagentStreamView, and PermissionRequests | `BLOCK_FANIN_ALTERNATIVES` — nearest mapping supported, TR-002 remains |
| 15 | `frontend/src/lib/workspace/navigation-intent.ts` | exactly AgentMatrix | `ACCEPT` — DEL-02-01 navigation / DEL-08-02 persona-guard split supported |
| 16 | `frontend/src/types/chirality-window.d.ts` | ambient selector type consumed by WorkspaceProvider; API-key surface omitted | `ACCEPT` — DEL-02-03 and DEL-09-04 verification-consumer boundary supported |
| 17 | `frontend/electron/preload.ts` | context bridge exposes directory selection plus API-key IPC; main process supplies handlers | `ACCEPT` — unresolved DEL-02-03/DEL-02-05/DEL-09-06 physical integration owner accurately preserved |
| 18 | `frontend/src/lib/harness/scripted-agent-sdk-proof.ts` | imported by `sdk-options-builder`; activated only by explicit dev/test env, which network-policy proof sets | `ACCEPT` — DEL-09-06 primary / DEL-04-01 evidence interest supported |
| 19 | `frontend/scripts/assert-harness-contract-deps.mjs` | npm `harness:validate:contract-deps`; first step of `validate:release-quality` | `ACCEPT` — D-APP-46/DEL-03-01 rule with DEL-09-05 orchestration consumer supported |
| 20 | `frontend/scripts/generate-tool-catalog.mjs` | npm generation entry; imports contract renderer and checks/writes catalog | `ACCEPT` — DEL-06-02 mechanism-only mapping supported |
| 21 | `frontend/scripts/pec-scratch-server.mjs` | imported by PEC integration test, bridge rehearsal, and D-APP-52 live-LLM demo | `ACCEPT` — DEL-10-04 primary with DEL-10-03 verification interest supported |
| 22 | `frontend/scripts/run-pec-bridge-rehearsal.ts` | direct opt-in evidence driver over PEC scratch helper and proposal handlers | `ACCEPT` — DEL-10-04 primary / DEL-10-03 near-peer boundary supported |

Coverage is 22/22: 18 technically acceptable integrated rows, three rows with
supportable nearest mappings but blocking alternative loss, and one row with
a blocking altered boundary. This return does not accept any ownership
mapping.

## Test evidence and limits

Existing focused tests materially support the content route, Markdown/ANSI,
document-view state, session/tool/subagent views, event buffer/derivations,
navigation scheduler, SDK proof gate, tool catalog, PEC bridge, and API-key IPC
claims. The package correctly says no tests were run and discloses the absence
of direct focused tests for FilePicker navigation, DocumentView fetch/render,
the provider context lifecycle, the preload bridge contract, and the contract
lint parser. Those limits are acceptable for discovery, but they do not cure
TR-001 or establish runtime/release verification.

## Fresh-child validation and fan-in

- Fresh child SHA-256:
  `b9bfb2923ec3853c4373923a61bca7e340963251e40fab94f3dbf5bdc56480c0`.
- Population/order: exact 14/14 DEL-02-01 manifest paths, unique and ordered.
- Schema: all required top-level and per-row fields present and populated.
- Source binding: 14/14 child blobs and SHA-256 values independently matched.
- Classification: 14/14 `OWNER_CLASS`; proposal-only posture preserved.
- Focus findings: globals, ChatMarkdown, and ANSI all internally coherent and
  supported by the reopened source/caller graph.
- Containment: current subject bytes match the basis; no subject or authority
  write is visible.
- Fan-in: 5/14 faithful, 5/14 harmlessly compressed, 3/14 materially lossy,
  and 1/14 boundary-altered, per the fidelity matrix and TR-001/TR-002.

## Control-label erratum

Disposition: `NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM` is sustained.

- Neither erroneous path exists:
  `frontend/src/styles/globals.css` and `frontend/src/lib/ansi.ts` are absent.
- The exact manifest, fresh child launch and return, ledger, proposed mapping,
  analysis, slate, notes, QA, and package bindings use
  `frontend/src/app/globals.css` and `frontend/src/lib/shell/ansi.ts`.
- The fresh child launch seals Git blobs `6eb6d932...` and `53500f33...`; the
  child and ledger SHA-256 values match those actual files.
- Repository search finds the wrong labels only in preserved/error-recording
  control surfaces, not in the manifest, child population, ledger, mapping,
  package execution targets, or writes.

No scope, source, authority, write-ownership, objective, risk, or acceptance
change resulted from the labels.

## Uncertainties, triggers, containment, and handoff

- The content-route and Electron-preload integration owners remain genuinely
  unresolved; the package preserves rather than flattens those ambiguities.
- `chirality-window.d.ts` still omits the runtime preload `apiKey` surface;
  this is an implementation observation, not repair authority.
- Rerun from the earliest stale node if any scoped source blob, relevant
  caller/import, cited test, deliverable scope/status, governing authority, or
  accepted child return changes.
- After TR-001/TR-002 repair, rerun independent technical and package fan-in checks
  against new immutable hashes.
- Waivers: none.
- Candidate slate and W1 must remain blocked.
- No mapping, repair, lifecycle, release, publication, professional, Git,
  index, ref, or PR authority is exercised by this return.
- Sole write by this child:
  `instances/V1-RECHECK/children/technical_recheck/RETURN.md`.
- Subject writes: zero. Authority writes: zero. Git-state changes: zero.
