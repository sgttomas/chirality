# Substantive Package/Preservation Confirmation Return

- **Role:** fresh bounded read-only Agent 2
- **Parent:** EVALUATION / V1-RECHECK3
- **Basis:** `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- **Verdict:** `ACCEPT`
- **Subject writes:** zero
- **Waivers:** none

## Terminal conclusion

Independent refutation did not find a substantive or preservation defect. The
unchanged 14-file derivative reproduces the exact 22-path basis, all 22 source
bindings, the two proposal schemas, all 22 unaccepted `OWNER_CLASS` rows, all
nine proposal groups, and the complete 14-row sealed-child fidelity inventory.
The four earlier substantive repairs remain present without semantic
substitution or lost physical-owner alternative. Nothing in the package
accepts a mapping, assigns ownership, closes Remaining, authorizes repair, or
releases a downstream node.

`ACCEPT` here is evidence for the V1-RECHECK3 manager only. It does not accept
the candidate owner slate or any row or group.

## Exact basis and predecessor bindings

- `HEAD` and `origin/main` both equal the basis; the branch is `+0/-0` against
  `origin/main`, the index is empty, and no Git ref or commit changed.
- Corrected R1-CONTROL-REISSUE `STATUS.json` and `RETURN.md` reproduce
  `0a6e4d600d26d1c71c1cb1c7f442c767f00f6ff4be854ce519fdb374800f17c0`
  and
  `f94081cf3848b387deb6e9edf74f6c104c706f014697ff14b67f2f440c6d76b6`.
  This slice relied on that immutable binding but did not duplicate the
  separately dispatched parser audit.
- Immutable R1-REPAIR2 return and raw status reproduce
  `bb520447e5923a36fca6533379ff49458dbb0fbbfcefe6edbfaf7ae4f2f4a12a`
  and
  `a48d9a634f279726f9c3cc4b23fb8e558b58f34502cd03ae6c87c5f6f4537a44`.
- The sealed fresh-evidence child brief and return reproduce
  `7ee27d1f464460bc8e9fb39c87aebdc044e1440eddb8ddd735c3bb0667b5b3fa`
  and
  `b9bfb2923ec3853c4373923a61bca7e340963251e40fab94f3dbf5bdc56480c0`.
- V1-RECHECK2 return/status/protocol/report/findings/handoff and both child
  launch/return pairs reproduce all corrected-control bindings. In
  particular, return/status/report/findings reproduce
  `cfb858139539f038629d06279f2c259c6948dff7ede772dad48ea1b12515820e`,
  `af250ce853165152321c993fe3065f2df2b36ab774c1f67e8057e493875c0fe4`,
  `81cf1298e32e7a263fd6f01136fe29857102ac5a21d26fb25efa622a0855a0ea`,
  and
  `43ba5e391b2a867cda1d2cea098859b757c140ff125762ef4210dd4932025f05`.

## Scope, source, and Remaining reproduction

- `CQF1_SCOPE.csv` has 22 rows, 22 unique paths, and 22 existing paths in
  exact frozen order. The ordered path-list SHA-256 is
  `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`.
- The five populations reproduce as DEL-02-01 14, DEL-03-03 1, DEL-06-02 1,
  DEL-09-04 4, and DEL-10-04 2. All five owning `_STATUS.md` files remain
  basis-identical, `IN_PROGRESS`, and explicit that CQ-F1 ownership/mapping is
  not asserted.
- For every row, the live bytes' Git hash-object and SHA-256 equal both the
  ledger binding and `git rev-parse 57652ba1:<path>`. There are 22/22 exact
  blob matches and 22/22 exact content-hash matches.
- The two current paths are exactly
  `projects/chirality-app-dev/frontend/src/app/globals.css` and
  `projects/chirality-app-dev/frontend/src/lib/shell/ansi.ts`. The former
  wrong labels do not exist and occur nowhere in the current 14-file package.

## Four repaired rows

| Finding/row | Independent evidence and retained package choice | Disposition |
|---|---|---|
| V1-001 — `globals.css` | The live stylesheet contains Pipeline/Workbench, API-key/runtime-feedback, replay, permission, persona, child, Working Root, and pane/toolkit regions. Ledger, mapping, matrix, note, analysis, and slate retain DEL-02-02 and DEL-02-05 plus every other named semantic boundary. DEL-02-01 is only an integration-lead proposal. | `REPAIRED_SUSTAINED` |
| V1-002 — `chat-markdown.tsx` | Production search finds exactly ChatPanel and DocumentView importing/rendering ChatMarkdown. No replay/transcript implementation imports it. The package rejects DEL-05-04 and retains DEL-02-01 primary, DEL-02-03 consumer, and shared-utility alternatives. | `REPAIRED_SUSTAINED` |
| V1-003 — `ansi.ts` | The sole production importer is ChatMarkdown; the same two transitive consumers and absence of a DEL-05-04 caller reproduce. The package records DEL-02-01 primary, DEL-02-03 consumer, and ownerless/shared utility. | `REPAIRED_SUSTAINED` |
| V1-004 — package EOF | Every one of the 14 package files ends in exactly one LF, has no horizontal trailing whitespace, and passes per-file `git diff --no-index --check`. | `REPAIRED_SUSTAINED` |
| V1R-001 — FilePicker | The source is a bounded Working Root tree browser with local selection state and client filtering that emits non-authoritative `UiAttachment` metadata. Every integration surface retains DEL-02-03 primary, DEL-02-04 attachment UI state, and DEL-09-06/server enforceable attachment security. DEL-06-04 write/edit enforcement is expressly rejected as a substitute. | `REPAIRED_SUSTAINED` |
| V1R-002 — physical-owner alternatives | `globals.css` retains ownerless/shared, capability-split, and DEL-02-04-lead alternatives; HarnessEventsProvider retains shared-application-infrastructure; harness-event views retains split-by-capability and ownerless/shared projection-utility. All semantic interfaces remain explicit. | `REPAIRED_SUSTAINED` |

The earlier wrong-path-label observation V1R-003/V1R2-002 remains a sustained
nonconsequential control erratum. V1-005 also remains truthful and
nonblocking: the `pec-scratch-server.mjs` comment still names only the opt-in
integration test and rehearsal driver, while live search finds the additional
`run-dapp52-live-llm-demo.ts` importer. No source repair was made or implied.

## Fourteen-file package disposition

| File | SHA-256 | Disposition |
|---|---|---|
| `AFFINITY_AND_MAPPING_ANALYSIS.md` | `1e825d797ddf5c4a9757bb1984ae63be0bf6b053736fe1bd5a8f932d415d4035` | `PASS_UNCHANGED` |
| `CANDIDATE_OWNER_SLATE.md` | `f6e630e9294c4779f87a0f7734667f565113127769cdaed3ab20b32cd099ce93` | `PASS_UNCHANGED` |
| `CQF1_PATH_LEDGER.csv` | `b56f87731920765279639d528393bae212403fe49ffb5de6c27065ddd4095288` | `PASS_UNCHANGED_22x13` |
| `DECISION_CLASSIFICATION.md` | `4f7d8d41b344daafd7f4533dcaaec5dc4859fa44561133181ce744006ed285fd` | `PASS_UNCHANGED` |
| `DEL02_01_CHILD_PACKAGE_FIDELITY.csv` | `100445dd4e2054440776a60e1be36e53d7cdb0bf6cbe94b9e21555f420f1706c` | `PASS_UNCHANGED_14x19` |
| `HANDOFF.md` | `9af95a170fa77149fac4cbe5bae7320e5abe357b39434a5c083a200ba80dbc75` | `PASS_UNCHANGED` |
| `PACKAGE_NOTES/DEL-02-01.md` | `0045d350a15c5fae07d0a0958096477c8fc057aedb8227cc433947feb3e6dafa` | `PASS_UNCHANGED` |
| `PACKAGE_NOTES/DEL-03-03.md` | `1ae7d3e728093a853e79240da5eaa91ce6407dc0c67a3b4c10a3cd3c656f6935` | `PASS_UNCHANGED` |
| `PACKAGE_NOTES/DEL-06-02.md` | `cd0b5b206c3ede37fb1eb3130b5a12cfece15ed1a1b498159ece87aed619f299` | `PASS_UNCHANGED` |
| `PACKAGE_NOTES/DEL-09-04.md` | `946d03791ae296397b39c8322dd6c48d6daf21bd65489ba07f24558045cb8a48` | `PASS_UNCHANGED` |
| `PACKAGE_NOTES/DEL-10-04.md` | `9a5e5291e30d3deb9a04992080c406c1499489b1696ee6fd361c4d27385fb59e` | `PASS_UNCHANGED` |
| `PROPOSED_MAPPING.csv` | `a01651fb49883d2f15971cbc8a85c5cff4c5039eeffb2500be6a78fd62378e86` | `PASS_UNCHANGED_22x7` |
| `QA.md` | `8cf4c42184a1ccd73577e11180562e2b9a576a9063728f4fd3c410227e92dbfd` | `PASS_UNCHANGED` |
| `RUN_BASIS.md` | `f752abe6d078ec3f485621a9b1f15476db0667642bfb591ed20420d97c2e537d` | `PASS_UNCHANGED` |

Package population is exactly 14. Both 22-row CSVs have their declared
schemas, exact manifest order, no duplicate path, and 22 `OWNER_CLASS` rows.
The fidelity CSV has exactly 19 columns and exact DEL-02-01 filtered-manifest
order. Its dispositions reproduce 5 `EXACT`, 5 `FAITHFUL_COMPRESSION`, 4
`REPAIRED_MATERIAL_LOSS`, 0 `EXPLICITLY_REASONED_REJECTION`, and 0 unexplained.

## Twenty-two-row disposition

| # | Path | Current proposal/boundary | Disposition |
|---:|---|---|---|
| 1 | `frontend/src/app/globals.css` | DEL-02-01 integration lead only; shared/split/UI-state alternatives and all semantic boundaries retained | `PASS_OWNER_CLASS_PROPOSAL` |
| 2 | `frontend/src/app/page.tsx` | DEL-02-01 direct root-shell render | `PASS_OWNER_CLASS_PROPOSAL` |
| 3 | `frontend/src/app/api/working-root/deliverable/content/route.ts` | DEL-07-03 nearest; DEL-07-01 containment and DEL-02-03 consumer; physical route owner unresolved | `PASS_OWNER_CLASS_PROPOSAL` |
| 4 | `frontend/src/components/shell/chat-markdown.tsx` | DEL-02-01 primary; DEL-02-03 consumer; no DEL-05-04 caller | `PASS_OWNER_CLASS_PROPOSAL` |
| 5 | `frontend/src/components/shell/document-view.tsx` | DEL-02-03 with content-route and shell-host interfaces | `PASS_OWNER_CLASS_PROPOSAL` |
| 6 | `frontend/src/components/shell/file-picker.tsx` | DEL-02-03 primary; DEL-02-04 UI state; DEL-09-06/server security | `PASS_OWNER_CLASS_PROPOSAL` |
| 7 | `frontend/src/components/shell/session-list-view.tsx` | DEL-05-04 replay/hydration; DEL-05-01 storage and DEL-02-01 host retained | `PASS_OWNER_CLASS_PROPOSAL` |
| 8 | `frontend/src/components/shell/subagent-stream-view.tsx` | DEL-05-04 projection; DEL-08-05 child lifecycle/artifact semantics retained | `PASS_OWNER_CLASS_PROPOSAL` |
| 9 | `frontend/src/components/shell/tool-stream-view.tsx` | DEL-05-04 projection; DEL-05-05 artifact and PKG-06 execution policy retained | `PASS_OWNER_CLASS_PROPOSAL` |
| 10 | `frontend/src/components/workspace/harness-events-provider.tsx` | DEL-05-04 nearest view buffer; DEL-05-02, DEL-02-01, and shared-infrastructure alternatives retained | `PASS_OWNER_CLASS_PROPOSAL` |
| 11 | `frontend/src/lib/shell/ansi.ts` | DEL-02-01 primary; DEL-02-03 consumer; shared utility retained | `PASS_OWNER_CLASS_PROPOSAL` |
| 12 | `frontend/src/lib/shell/document-view-state.ts` | DEL-02-03 sole-consumer document-state helper | `PASS_OWNER_CLASS_PROPOSAL` |
| 13 | `frontend/src/lib/shell/harness-event-buffer.ts` | DEL-05-04 live/replay view buffer; DEL-05-02 persistence retained | `PASS_OWNER_CLASS_PROPOSAL` |
| 14 | `frontend/src/lib/shell/harness-event-views.ts` | DEL-05-04 shared projection; semantic, split-file, and shared-utility alternatives retained | `PASS_OWNER_CLASS_PROPOSAL` |
| 15 | `frontend/src/lib/workspace/navigation-intent.ts` | DEL-02-01 route mechanics; DEL-08-02 persona/guard boundary retained | `PASS_OWNER_CLASS_PROPOSAL` |
| 16 | `frontend/src/types/chirality-window.d.ts` | DEL-02-03 renderer selector typing; DEL-09-04 packaging consumer | `PASS_OWNER_CLASS_PROPOSAL` |
| 17 | `frontend/electron/preload.ts` | unresolved integration owner across DEL-02-03, DEL-02-05, DEL-09-06 | `PASS_OWNER_CLASS_PROPOSAL` |
| 18 | `frontend/src/lib/harness/scripted-agent-sdk-proof.ts` | DEL-09-06 primary; DEL-04-01 evidence interest | `PASS_OWNER_CLASS_PROPOSAL` |
| 19 | `frontend/scripts/assert-harness-contract-deps.mjs` | DEL-03-01 contract lint; DEL-09-05 validation consumer | `PASS_OWNER_CLASS_PROPOSAL` |
| 20 | `frontend/scripts/generate-tool-catalog.mjs` | DEL-06-02 deterministic mechanism only; semantic owners retained | `PASS_OWNER_CLASS_PROPOSAL` |
| 21 | `frontend/scripts/pec-scratch-server.mjs` | DEL-10-04 bounded PEC evidence helper; DEL-10-03 verification interest; V1-005 retained | `PASS_OWNER_CLASS_PROPOSAL_WITH_NONBLOCKING_OBSERVATION` |
| 22 | `frontend/scripts/run-pec-bridge-rehearsal.ts` | DEL-10-04 PEC fixture evidence; DEL-10-03 proposal-tool interest retained | `PASS_OWNER_CLASS_PROPOSAL` |

The live implementation supports each evidence description: direct imports and
callers reproduce the shell/document/projection rows; the Electron bridge
combines selector and API-key channels; the SDK proof is development/test
gated; the lint and generator are thin deterministic scripts; and the two PEC
paths are bounded evidence drivers. Accepted SOW boundaries support the named
semantic owner/consumer distinctions. D-APP-60/D-APP-64 fast-reject screening
was independently reopened: accepting any of these path mappings would create
ownership or accepted scope meaning, so all 22 correctly remain `OWNER_CLASS`.

## Nine-group disposition

| Group | Exact members/population | Disposition |
|---:|---|---|
| 1 | `globals.css`, `page.tsx`, `chat-markdown.tsx`, `ansi.ts`, `navigation-intent.ts` — 5 | `PASS_PROPOSAL_ONLY` |
| 2 | `document-view.tsx`, `file-picker.tsx`, `document-view-state.ts`, `chirality-window.d.ts` — 4 | `PASS_PROPOSAL_ONLY` |
| 3 | session, subagent, tool, provider, buffer, and event-view paths — 6 | `PASS_PROPOSAL_ONLY` |
| 4 | Working Root content route — 1 | `PASS_PROPOSAL_ONLY` |
| 5 | tool-catalog generator — 1 | `PASS_PROPOSAL_ONLY` |
| 6 | Electron preload — 1 | `PASS_PROPOSAL_ONLY` |
| 7 | scripted network-policy fixture — 1 | `PASS_PROPOSAL_ONLY` |
| 8 | harness-contract dependency lint — 1 | `PASS_PROPOSAL_ONLY` |
| 9 | PEC scratch server and bridge rehearsal — 2 | `PASS_PROPOSAL_ONLY` |

The population is exactly `5+4+6+1+1+1+1+1+2=22`, with no overlap or
omission. Each group is phrased as a ruling question, retains its material
boundaries, and states that owner action remains required.

## Preservation, authority, and containment

- All 22 frontend/source paths are byte-identical to basis; there are zero
  subject writes. The five Remaining/status files are byte-identical to basis.
- `ORCHESTRATION_PLAN.md`, `WORK_GRAPH.json`, and `CQF1_SCOPE.csv` are
  byte-identical to basis. The immutable D-APP authority/decision surfaces,
  receipt/lifecycle/decomposition surfaces, and relied-on SOW/dependency
  corpus show no tracked drift from basis.
- Prior R1/V1 instances, children, evaluation packages, and their recorded
  hashes remain immutable. The historical blocked derivative is unchanged.
- The only tracked app-dev delta against basis is the parent-owned cumulative
  coordination `HANDOFF_STATE.md`; it is not a subject, authority, Remaining,
  plan, graph, predecessor, or derivative-package mutation. Expected additive
  run amendments/instances/evaluation/activated-package paths remain untracked
  work products. The index is empty and Git identity/ref state is unchanged.
- The package repeatedly states derivative/proposal-only posture. It records
  22 owner gates, `accepted=false`, no Remaining closure, no W1 release, and no
  implementation/lifecycle/release/publication/Git authority. No ownership or
  downstream effect is smuggled through QA, classification, or handoff text.
- This child used only read-only file, Git, search, hash, CSV, and JSON
  inspection. It did not delegate. Its sole write is this `RETURN.md`.

## Findings, unknowns, waivers, and rerun

- **Blocking findings:** none.
- **Nonblocking observations:** V1-005 remains unrepaired and correctly
  bounded; the earlier wrong-path-label erratum remains historical and
  nonconsequential. The content-route and Electron-preload physical owner
  questions, the missing renderer `apiKey` typing, stale catalog-document
  pointers, and stale network-proof metadata remain visible unknowns rather
  than inferred answers.
- **Waivers:** none requested or used.
- **Tests:** no runtime/frontend/service test was run; this was a read-only
  source, caller, SOW, authority, hash, schema, and preservation audit.
- **Rerun requirement:** rerun from the earliest stale node if the basis,
  any scoped source/blob/caller, any of the five Remaining entries, governing
  authority, sealed child, predecessor binding, package hash/schema/fidelity,
  final-LF state, proposal-only posture, or write containment changes, or if
  the parent/control-parser slice reports a contradictory material finding.
- **Next gate:** V1-RECHECK3 manager fan-in. Owner-slate routing and W1 remain
  blocked until HELP_HUMAN separately accepts the manager's terminal result
  and performs the applicable human-routing gate.
