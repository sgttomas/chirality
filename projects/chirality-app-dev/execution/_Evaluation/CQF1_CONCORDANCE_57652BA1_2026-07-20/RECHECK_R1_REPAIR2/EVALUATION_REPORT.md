# Evaluation Report — CQ-F1 R1-REPAIR2 V1-RECHECK2

## Verdict

`BLOCK`.

R1-REPAIR2 substantively passes. All four prior material fan-in losses are
repaired; the 14-row fidelity matrix, all 22 proposal rows, 22 `OWNER_CLASS`
classifications, nine groups, source/package bindings, schemas, EOF hygiene,
preservation, containment, and the earlier wrong-label erratum all sustain.

The sole blocker is the duplicate `control_label_erratum` member in the bound
R1-REPAIR2 `STATUS.json`. Ordinary parsers erase the structured corrected-path
provenance by keeping the later string; a duplicate-rejecting parser rejects
the entire status. This is the path/provenance/schema/automation loss that the
sealed launch brief explicitly requires to return `BLOCK`.

No row, mapping, group, or owner slate is accepted. Owner routing and W1
remain blocked.

## Basis, method, and validated returns

- Basis: `57652ba1cd0905e8f47131e4c4ebf518272f7c16`.
- Manifest: 22 rows, 22 unique paths, 22 existing paths, exact order; ordered
  newline-terminated path-list SHA-256
  `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`.
- Remaining populations: DEL-02-01 14, DEL-03-03 1, DEL-06-02 1, DEL-09-04
  4, DEL-10-04 2; every status remains `IN_PROGRESS` and unchanged.
- R1-REPAIR2 return/raw status bindings:
  `bb520447e5923a36fca6533379ff49458dbb0fbbfcefe6edbfaf7ae4f2f4a12a`
  and
  `a48d9a634f279726f9c3cc4b23fb8e558b58f34502cd03ae6c87c5f6f4537a44`.
- Sealed child brief/return:
  `7ee27d1f464460bc8e9fb39c87aebdc044e1440eddb8ddd735c3bb0667b5b3fa`
  and
  `b9bfb2923ec3853c4373923a61bca7e340963251e40fab94f3dbf5bdc56480c0`.
- Source bindings: 22/22 Git blobs and SHA-256 values independently matched
  the basis and current bytes. Subject diff: zero.
- Method: two fresh bounded read-only Agent-2 audits plus manager hash,
  source/caller/test, SOW/status/dependency/authority, CSV/JSON, raw duplicate,
  schema, EOF, no-index, predecessor, and containment checks. No runtime test
  or service was run.

Validated fresh returns:

- technical/fidelity `ACCEPT`, SHA-256
  `32474f641ac1de6ba55ad521466bad375ff3280c0951bc1d4e636927c655682d`;
- governance/package/erratum `BLOCK`, SHA-256
  `f67c7707e7e705717339374d36c4469fce7aae2f37e8845d6f24088dae2aedb3`.

The manager independently reproduces both returns and sustains the governance
child's sole blocker.

## Blocking finding V1R2-001 — duplicate status member

The raw R1-REPAIR2 status contains exactly two top-level members named
`control_label_erratum`, in this order:

1. a structured object with classification
   `NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED` and corrected paths
   `projects/chirality-app-dev/frontend/src/app/globals.css` and
   `projects/chirality-app-dev/frontend/src/lib/shell/ansi.ts`;
2. the same classification as a string.

The classification texts agree, but the values are not structurally
equivalent. Reproduced parser behavior is:

| Parser posture | Result | Loss |
|---|---|---|
| Python, Node `JSON.parse`, and `jq` ordinary parsing | later string wins | structured object and both `correct_paths` disappear |
| duplicate-detecting ordered-pair parser | rejects | entire status record unavailable |
| raw ordered-pair inspection | preserves both | proves exact count, order, values, and raw hash |

Repository status readers use ordinary JSON parsing. No current in-scope
consumer reads this ad hoc member, so terminal state and downstream gates did
not change. Nevertheless, a structured consumer receives no corrected paths,
and a fail-closed consumer receives no status record. Independent provenance
elsewhere prevents source or ownership concealment but does not restore the
lost paths to an ordinary parse of this bound control record. The provisional
`NONCONSEQUENTIAL_DUPLICATE_JSON_MEMBER_ERRATUM` disposition is therefore
refuted under the launch brief's explicit fail rule.

This blocker affects the R1-REPAIR2 terminal control binding, not any manifest
row or owner group.

## Complete 14-row fidelity disposition

All 19 columns were checked against the sealed child and the ledger, mapping,
analysis, DEL-02-01 note, slate, QA, handoff, run basis, and matrix locations.

| Child row | Path | Disposition | Recheck result |
|---:|---|---|---|
| 1 | `frontend/src/app/globals.css` | `REPAIRED_MATERIAL_LOSS` | pass — shared/ownerless and capability-split choices restored |
| 2 | `frontend/src/app/page.tsx` | `FAITHFUL_COMPRESSION` | pass — weak host/ownerless choices reasonedly rejected |
| 3 | `frontend/src/components/shell/chat-markdown.tsx` | `EXACT` | pass |
| 4 | `frontend/src/components/shell/document-view.tsx` | `EXACT` | pass |
| 5 | `frontend/src/components/shell/file-picker.tsx` | `REPAIRED_MATERIAL_LOSS` | pass — DEL-02-04 and DEL-09-06 restored; DEL-06-04 substitution rejected |
| 6 | `frontend/src/components/shell/session-list-view.tsx` | `EXACT` | pass |
| 7 | `frontend/src/components/shell/subagent-stream-view.tsx` | `FAITHFUL_COMPRESSION` | pass |
| 8 | `frontend/src/components/shell/tool-stream-view.tsx` | `FAITHFUL_COMPRESSION` | pass |
| 9 | `frontend/src/components/workspace/harness-events-provider.tsx` | `REPAIRED_MATERIAL_LOSS` | pass — shared-infrastructure choice restored |
| 10 | `frontend/src/lib/shell/ansi.ts` | `EXACT` | pass |
| 11 | `frontend/src/lib/shell/document-view-state.ts` | `EXACT` | pass |
| 12 | `frontend/src/lib/shell/harness-event-buffer.ts` | `FAITHFUL_COMPRESSION` | pass |
| 13 | `frontend/src/lib/shell/harness-event-views.ts` | `REPAIRED_MATERIAL_LOSS` | pass — split/shared choices restored |
| 14 | `frontend/src/lib/workspace/navigation-intent.ts` | `FAITHFUL_COMPRESSION` | pass |

Totals reproduce exactly: 5 `EXACT`, 5 `FAITHFUL_COMPRESSION`, 4
`REPAIRED_MATERIAL_LOSS`, 0 `EXPLICITLY_REASONED_REJECTION`, and 0 unexplained
differences. Every material alternative, boundary, rejection, blocker,
classification, mapping posture, group, source binding, and integrated
location is complete.

## Complete 22-row disposition

Every row substantively passes as an unaccepted `OWNER_CLASS` proposal. The
control blocker does not change an individual row disposition.

| # | Path | Disposition |
|---:|---|---|
| 1 | `frontend/src/app/globals.css` | substantive pass; full shared/split choice set |
| 2 | `frontend/src/app/page.tsx` | substantive pass |
| 3 | `frontend/src/app/api/working-root/deliverable/content/route.ts` | substantive pass; physical owner remains unresolved |
| 4 | `frontend/src/components/shell/chat-markdown.tsx` | substantive pass |
| 5 | `frontend/src/components/shell/document-view.tsx` | substantive pass |
| 6 | `frontend/src/components/shell/file-picker.tsx` | substantive pass; UI/security boundary repaired |
| 7 | `frontend/src/components/shell/session-list-view.tsx` | substantive pass |
| 8 | `frontend/src/components/shell/subagent-stream-view.tsx` | substantive pass |
| 9 | `frontend/src/components/shell/tool-stream-view.tsx` | substantive pass |
| 10 | `frontend/src/components/workspace/harness-events-provider.tsx` | substantive pass; shared-infrastructure choice restored |
| 11 | `frontend/src/lib/shell/ansi.ts` | substantive pass |
| 12 | `frontend/src/lib/shell/document-view-state.ts` | substantive pass |
| 13 | `frontend/src/lib/shell/harness-event-buffer.ts` | substantive pass |
| 14 | `frontend/src/lib/shell/harness-event-views.ts` | substantive pass; split/shared choices restored |
| 15 | `frontend/src/lib/workspace/navigation-intent.ts` | substantive pass |
| 16 | `frontend/src/types/chirality-window.d.ts` | substantive pass; omitted `apiKey` remains observation only |
| 17 | `frontend/electron/preload.ts` | substantive pass; integration owner remains unresolved |
| 18 | `frontend/src/lib/harness/scripted-agent-sdk-proof.ts` | substantive pass; not packaged proof |
| 19 | `frontend/scripts/assert-harness-contract-deps.mjs` | substantive pass |
| 20 | `frontend/scripts/generate-tool-catalog.mjs` | substantive pass; mechanism only |
| 21 | `frontend/scripts/pec-scratch-server.mjs` | substantive pass; stale caller-count comment remains nonblocking |
| 22 | `frontend/scripts/run-pec-bridge-rehearsal.ts` | substantive pass; F-APP-3 retained |

D-APP-60/D-APP-64 screening was reperformed. Accepting any proposed mapping
or physical/shared boundary would create currently withheld ownership/scope
meaning. All 22 therefore remain `OWNER_CLASS`; none qualifies as
`DISPOSITION_CLASS`, `NO_REPAIR`, `BLOCKED_INPUT`, or `STALE_INPUT`.

## Nine-group disposition

The population is exactly `5+4+6+1+1+1+1+1+2=22`, with no omission or
duplicate. Each group is substantively decision-ready as a proposal but
unaccepted and unrouted because the terminal control input is blocked.

| Group | Paths | Substantive result |
|---|---:|---|
| 1. Shell integration/shared presentation | 5 | pass; stylesheet physical-owner choices complete |
| 2. Working-root document UX | 4 | pass; FilePicker UI/security boundaries complete |
| 3. Replay/projection | 6 | pass; provider and event-view choices complete |
| 4. Working-root content route | 1 | pass; owner choice retained |
| 5. Catalog generation | 1 | pass |
| 6. Electron preload | 1 | pass; integration-owner choice retained |
| 7. Network-policy fixture | 1 | pass |
| 8. Contract dependency lint | 1 | pass |
| 9. PEC evidence | 2 | pass with DEL-10-03 interest and F-APP-3 retained |

## Package, hashes, and preservation

The activated derivative contains exactly 14 files, all ending in exactly one
LF with no horizontal trailing whitespace. Per-file no-index and tracked diff
hygiene pass.

| File | SHA-256 |
|---|---|
| `AFFINITY_AND_MAPPING_ANALYSIS.md` | `1e825d797ddf5c4a9757bb1984ae63be0bf6b053736fe1bd5a8f932d415d4035` |
| `CANDIDATE_OWNER_SLATE.md` | `f6e630e9294c4779f87a0f7734667f565113127769cdaed3ab20b32cd099ce93` |
| `CQF1_PATH_LEDGER.csv` | `b56f87731920765279639d528393bae212403fe49ffb5de6c27065ddd4095288` |
| `DECISION_CLASSIFICATION.md` | `4f7d8d41b344daafd7f4533dcaaec5dc4859fa44561133181ce744006ed285fd` |
| `DEL02_01_CHILD_PACKAGE_FIDELITY.csv` | `100445dd4e2054440776a60e1be36e53d7cdb0bf6cbe94b9e21555f420f1706c` |
| `HANDOFF.md` | `9af95a170fa77149fac4cbe5bae7320e5abe357b39434a5c083a200ba80dbc75` |
| `PACKAGE_NOTES/DEL-02-01.md` | `0045d350a15c5fae07d0a0958096477c8fc057aedb8227cc433947feb3e6dafa` |
| `PACKAGE_NOTES/DEL-03-03.md` | `1ae7d3e728093a853e79240da5eaa91ce6407dc0c67a3b4c10a3cd3c656f6935` |
| `PACKAGE_NOTES/DEL-06-02.md` | `cd0b5b206c3ede37fb1eb3130b5a12cfece15ed1a1b498159ece87aed619f299` |
| `PACKAGE_NOTES/DEL-09-04.md` | `946d03791ae296397b39c8322dd6c48d6daf21bd65489ba07f24558045cb8a48` |
| `PACKAGE_NOTES/DEL-10-04.md` | `9a5e5291e30d3deb9a04992080c406c1499489b1696ee6fd361c4d27385fb59e` |
| `PROPOSED_MAPPING.csv` | `a01651fb49883d2f15971cbc8a85c5cff4c5039eeffb2500be6a78fd62378e86` |
| `QA.md` | `8cf4c42184a1ccd73577e11180562e2b9a576a9063728f4fd3c410227e92dbfd` |
| `RUN_BASIS.md` | `f752abe6d078ec3f485621a9b1f15476db0667642bfb591ed20420d97c2e537d` |

Ledger, mapping, and fidelity schemas reproduce as 22×13, 22×7, and 14×19.
All v9 V1-RECHECK bindings, original V1/V1-RETRY evidence, R1/R1-RETRY child
returns, plan, work graph, decisions, receipts, authority, lifecycle, and
subject/Remaining state remain immutable. Evaluation writes are confined to
the two authorized additive roots. Waivers: none.

## Earlier erratum and observations

The earlier wrong-label erratum remains
`NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED`. Wrong/nonexistent labels
`frontend/src/styles/globals.css` and `frontend/src/lib/ansi.ts` occur only in
preserved error history. Current manifest, child, CSVs, matrix, and package
evidence use only the exact corrected paths.

V1-001 through V1-004 and V1R-001/V1R-002 are repaired and sustained. V1-005
remains the nonblocking stale two-caller source-comment observation. No source
repair occurred.

## Required control-only repair and rerun

The coordination workflow that owns the R1 instance status, under a
HELP_HUMAN versioned amendment, must preserve R1-REPAIR2 immutably and emit a
new additive control attempt/record with exactly one structured
`control_label_erratum` member containing the sustained classification and
both corrected paths. It must:

1. validate unique top-level member names with a duplicate-rejecting parser;
2. prove ordinary parsing returns the same structured value;
3. bind the unchanged 14-file derivative, sealed child, predecessors, basis,
   22 rows, classifications, and groups;
4. preserve owner/W1/downstream blocks and all authority fences; and
5. issue refreshed immutable terminal return/status hashes.

No source, Remaining, SOW/dependency, mapping, slate, package, authority,
lifecycle, decision, receipt, plan/graph, or Git repair is indicated.

After the control record is reissued, EVALUATION must rerun a fresh V1 check
from the earliest stale control node. The substantive audits may be reused
only while their exact inputs and bindings remain unchanged.
