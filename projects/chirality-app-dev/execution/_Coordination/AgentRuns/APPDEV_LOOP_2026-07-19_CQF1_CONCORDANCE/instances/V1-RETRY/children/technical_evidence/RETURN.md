# Technical-Evidence Audit Return

- **Verdict:** `BLOCK`
- **Basis:** `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- **Scope:** exact 22 paths in `CQF1_SCOPE.csv`
- **Role:** bounded read-only Agent 2 auditor
- **Delegation:** none
- **Tests/services:** none run; inspection was limited to read-only source,
  caller/import, test, citation, hash, and Git-object evidence

## Coverage and source binding

- Manifest: 22 rows, 22 unique paths, 22 existing paths, in sealed order.
- Ordered newline-terminated path-list SHA-256:
  `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`.
- Source binding: 22/22 ledger Git blobs and 22/22 ledger SHA-256 values
  independently recomputed at the exact basis and matched. The current copies
  of all 22 paths also matched those basis bytes during this audit.
- Five child-return union: 14 + 1 + 1 + 4 + 2 = 22 unique paths, with no
  duplicate or omitted path. The five child-return SHA-256 values match the
  values recorded in R1 `QA.md`.
- All 22 source files, their direct callers/imports/consumers, the cited test
  surfaces, the technical fields of all five child returns, the integrated
  ledger/mapping, five package notes, affinity analysis, QA, handoff, and
  nine-group candidate slate were inspected.

No source-state staleness was found. The BLOCK is caused by materially false
or incomplete technical evidence and candidate boundaries in three rows and
two grouped recommendations.

## Blocking findings

### TE-001 — `globals.css` omits two material capability families

**Severity:** material / decision-slate blocking.

The DEL-02-01 child describes `globals.css` and proposes explicit capability
edges, but omits two large, plainly implemented regions:

1. Pipeline and Workbench styling occupies `globals.css:1055-1425`, including
   `.pipeline-*` and `.workbench-*`; DEL-02-02's live scope expressly covers
   Workbench and Pipeline UX at its `ScopeOfWork.md:116-122`.
2. API-key settings/status/error styling occupies `globals.css:1631-1724`;
   DEL-02-05's live scope expressly covers API-key settings/status and
   secure-storage feedback at its `ScopeOfWork.md:119-127`. The source comment
   at `globals.css:1631` calls this `DEL-02-06`, which is itself stale.

The child implementation summary and citations at
`children/del_02_01/RETURN.json:16-23` skip both regions; its candidate edge
list at line 44 omits DEL-02-02 and DEL-02-05. The lossy omission propagates
to `CQF1_PATH_LEDGER.csv:2`, `PROPOSED_MAPPING.csv:2`,
`AFFINITY_AND_MAPPING_ANALYSIS.md:16`, and Candidate Owner Slate group 1 at
`CANDIDATE_OWNER_SLATE.md:9-12`.

An owner asked to designate a stylesheet integration lead would therefore
not be shown two material retained semantic boundaries. This is not cured by
the generic statement that styled capability semantics do not transfer,
because the package says the listed edges are explicit and decision-ready.

**Required repair:** rerun/reissue the DEL-02-01 technical slice and R1 fan-in
so the stylesheet row fully inventories its capability regions, cites the
omitted source sections, includes DEL-02-02 and DEL-02-05 as retained evidence
edges or expressly analyzes/rejects them, corrects or records the stale
`DEL-02-06` source comment, and propagates the complete boundary to the
ledger, proposed mapping, affinity analysis, package note, and owner slate.
No source-code repair is authorized by this finding.

### TE-002 — `chat-markdown.tsx` has no replay consumer

**Severity:** material false call-graph claim / decision-slate blocking.

The child correctly identifies the actual production consumers in its own
implementation citations: `chat-panel.tsx:25,497-506` and
`document-view.tsx:6,198-204`. Repository-wide import/use inspection found no
third production consumer. The accepted transcript view instead derives
`TranscriptItem`s and renders text directly at
`transcript-stream-view.tsx:46-61,103-106`; it neither imports nor calls
`ChatMarkdown`.

Nevertheless, the child marks DEL-05-04 as a consumer/evidence edge at
`children/del_02_01/RETURN.json:153-172`; the integrated ledger says the
renderer is used by "chat, documents, and replay" at
`CQF1_PATH_LEDGER.csv:5`; `PROPOSED_MAPPING.csv:5` calls DEL-05-04 a consumer;
and Candidate Owner Slate group 1 repeats the DEL-05-04 consumer edge at
`CANDIDATE_OWNER_SLATE.md:9-12`.

The current call graph supports DEL-02-01 and DEL-02-03 consumer evidence. It
does not support a DEL-05-04 replay-consumer assertion.

**Required repair:** rerun/reissue this row and R1 fan-in to remove the false
replay/current-consumer claim and DEL-05-04 consumer edge unless new direct
evidence is produced. Reassess the primary/shared-boundary rationale and
propagate the corrected call graph through the ledger, mapping, affinity
analysis, package note, and owner slate.

### TE-003 — `ansi.ts` is assigned to DEL-05-04 without a replay/transcript caller

**Severity:** material unsupported candidate affinity / group-boundary
blocking.

`ansi.ts:1-14` is imported only by `chat-markdown.tsx:6`, which calls it at
lines 30-50. As established in TE-002, ChatMarkdown's production consumers are
live chat and Working Root document display, not the DEL-05-04 transcript
view. No replay parser, replay model, transcript view, session replay route,
or DEL-05-04 implementation path imports the ANSI helper.

The child concedes that its only direct production consumer is the
DEL-02-01-side ChatMarkdown (`children/del_02_01/RETURN.json:553-568` and
disagreement at line 805), yet proposes DEL-05-04 based only on a semantic
"transcript/output" label. The integrated artifacts then upgrade that weak
analogy to "ANSI-to-HTML transcript presentation helper" and DEL-05-04 owner
at `CQF1_PATH_LEDGER.csv:12`, `PROPOSED_MAPPING.csv:12`, and
`AFFINITY_AND_MAPPING_ANALYSIS.md:15`; Candidate Owner Slate group 3 includes
ANSI among seven DEL-05-04 paths at `CANDIDATE_OWNER_SLATE.md:16-19`.

That is insufficient implementation affinity for a decision-ready mapping:
"output" is broader than the actual DEL-05-04 replay/transcript feature, and
the concrete current call graph points to DEL-02-01 plus DEL-02-03 consumption.

**Required repair:** rerun/reissue the ANSI row and the replay/projection
group. Re-evaluate DEL-02-01, DEL-02-03/shared shell presentation, and
deliberately shared utility as the technically evidenced alternatives. Keep
DEL-05-04 only if a real current interface/evidence relationship is shown;
do not describe it as a current replay/transcript consumer on the frozen
basis. Propagate the result through the child return, ledger, mapping,
affinity analysis, package note, and owner slate.

## Row-by-row technical disposition

| # | Path | Technical disposition |
|---:|---|---|
| 1 | `frontend/src/app/globals.css` | `BLOCK` — TE-001 |
| 2 | `frontend/src/app/page.tsx` | `ACCEPT` — direct `PortalLoopShell` root composition and test limit accurately stated |
| 3 | `frontend/src/app/api/working-root/deliverable/content/route.ts` | `ACCEPT` — helper, consumer, containment tests, and unresolved backend/UI boundary accurately represented |
| 4 | `frontend/src/components/shell/chat-markdown.tsx` | `BLOCK` — TE-002 |
| 5 | `frontend/src/components/shell/document-view.tsx` | `ACCEPT` — roster/content behavior and DEL-02-03/route/host boundary supported |
| 6 | `frontend/src/components/shell/file-picker.tsx` | `ACCEPT` — client behavior, API use, attachment boundary, and direct-test limit accurately stated |
| 7 | `frontend/src/components/shell/session-list-view.tsx` | `ACCEPT` — list/replay/hydrate behavior and storage/view/host split supported |
| 8 | `frontend/src/components/shell/subagent-stream-view.tsx` | `ACCEPT` — read-only projection and DEL-08-05 semantic boundary supported |
| 9 | `frontend/src/components/shell/tool-stream-view.tsx` | `ACCEPT` — read-only projection and result/execution boundaries supported |
| 10 | `frontend/src/components/workspace/harness-events-provider.tsx` | `ACCEPT` — live/hydrated bounded state, consumers, and lack of direct provider test accurately disclosed |
| 11 | `frontend/src/lib/shell/ansi.ts` | `BLOCK` — TE-003 |
| 12 | `frontend/src/lib/shell/document-view-state.ts` | `ACCEPT` — sole consumer and focused branch tests supported |
| 13 | `frontend/src/lib/shell/harness-event-buffer.ts` | `ACCEPT` — live/hydrate parity and non-persistence boundary supported |
| 14 | `frontend/src/lib/shell/harness-event-views.ts` | `ACCEPT` — tool, permission, and child projection behavior plus retained semantic boundaries supported |
| 15 | `frontend/src/lib/workspace/navigation-intent.ts` | `ACCEPT` — sole AgentMatrix consumer, scheduling behavior, tests, and persona/guard boundary supported |
| 16 | `frontend/src/types/chirality-window.d.ts` | `ACCEPT` — selector typing and omitted `apiKey` observation accurate |
| 17 | `frontend/electron/preload.ts` | `ACCEPT` — two feature families and unresolved physical-file integration boundary accurately preserved |
| 18 | `frontend/src/lib/harness/scripted-agent-sdk-proof.ts` | `ACCEPT` — development/test gate, network-proof caller, test limits, and DEL-09-06/DEL-04-01 evidence split supported |
| 19 | `frontend/scripts/assert-harness-contract-deps.mjs` | `ACCEPT` — lint behavior, invocations, no-focused-test limit, and DEL-03-01/DEL-09-05 boundary supported |
| 20 | `frontend/scripts/generate-tool-catalog.mjs` | `ACCEPT` — generator/check mechanism and distributed descriptor semantics supported |
| 21 | `frontend/scripts/pec-scratch-server.mjs` | `ACCEPT` — all three current callers, scratch-only behavior, and DEL-10-03 consumer boundary captured; source comment's two-caller statement is stale but the R1 row does not repeat it |
| 22 | `frontend/scripts/run-pec-bridge-rehearsal.ts` | `ACCEPT` — direct-handler evidence behavior, demo-cast acts, historical evidence limits, and DEL-10-03/DEL-10-04 overlap accurately represented |

## Test and evidence limits

- Existing focused tests materially support the route, Markdown/ANSI behavior,
  document state, event derivations/buffer, navigation scheduler, scripted SDK
  gate, and catalog drift claims cited by R1.
- The package accurately discloses that no tests or services were run and that
  there is no direct test for DocumentView fetch/render integration,
  FilePicker navigation, the provider context lifecycle, ambient window
  typing, the preload bridge contract, or the contract-lint parser.
- Those limits do not independently block proposal discovery. They do prevent
  treating the package as fresh runtime/release verification, which R1 does
  not claim.

## Stale observations and triggers

- All 22 source blobs are fresh at the frozen basis.
- R1 correctly preserves the stale pre-package paths in
  `frontend/docs/harness/adding_a_tool.md` and the stale historical
  `DELIVERABLE_ROOT` in `run-network-policy-proof.mjs` as observations.
- `pec-scratch-server.mjs:6-8` says the helper has only two callers, while the
  current call graph also includes `run-dapp52-live-llm-demo.ts:30-38`; the
  technical child correctly includes that third caller. This is a non-blocking
  source-comment observation because the mapped evidence itself is accurate.
- Rerun the technical evidence node if any scoped source blob, direct caller,
  cited focused test, relevant deliverable scope, or governing mapping basis
  changes. After the three findings are repaired in a new controlled R1
  attempt/package, rerun this technical audit against the new immutable
  bindings.

## Handoff

The technical evidence package is not decision-ready. R1/RECONCILIATION must
repair TE-001 through TE-003 and re-fan-in the affected shell slice and owner
groups before V1 can accept the derivative for owner routing. The unaffected
19 rows need not be rediscovered unless their frozen inputs change, but the
new package must reproduce the exact 22-row union and preserve their accepted
evidence.

No mapping or slate is accepted by this return. W1 must remain blocked. No
subject, R1 package, evaluation package, control file other than this
`RETURN.md`, lifecycle, authority, Git, index, ref, or PR state was modified.
