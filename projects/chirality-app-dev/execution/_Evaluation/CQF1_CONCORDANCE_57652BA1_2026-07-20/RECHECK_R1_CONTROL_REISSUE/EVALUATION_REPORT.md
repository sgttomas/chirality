# Evaluation Report — CQ-F1 R1-CONTROL-REISSUE V1-RECHECK3

## Verdict

`ACCEPT`.

The additive R1 control reissue repairs V1R2-001 without rewriting the
immutable defective predecessor. Its status contains one unique structured
`control_label_erratum` member, and strict Python, ordinary Python, Node
`JSON.parse`, and jq expose the exact same classification and corrected-path
array.

The substantive derivative remains unchanged and passes: 14 exact package
hashes, the complete 14×19 fidelity matrix, all four repaired fan-in losses,
22 evidence-supported `OWNER_CLASS` proposal rows, nine groups, schemas, EOF
hygiene, authority, preservation, and containment.

This verdict accepts only evaluation readiness. It does not accept or route a
row, group, mapping, or owner slate. W1 and owner routing remain blocked until
HELP_HUMAN separately accepts this return and performs the applicable gate.

## Basis, method, and validated returns

- Basis: `57652ba1cd0905e8f47131e4c4ebf518272f7c16`.
- Manifest: 22 rows, 22 unique paths, 22 existing paths, exact order; ordered
  path-list SHA-256
  `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`.
- Corrected control status/return:
  `0a6e4d600d26d1c71c1cb1c7f442c767f00f6ff4be854ce519fdb374800f17c0`
  and
  `f94081cf3848b387deb6e9edf74f6c104c706f014697ff14b67f2f440c6d76b6`.
- Immutable R1-REPAIR2 return/raw status:
  `bb520447e5923a36fca6533379ff49458dbb0fbbfcefe6edbfaf7ae4f2f4a12a`
  and
  `a48d9a634f279726f9c3cc4b23fb8e558b58f34502cd03ae6c87c5f6f4537a44`.
- Sealed child brief/return:
  `7ee27d1f464460bc8e9fb39c87aebdc044e1440eddb8ddd735c3bb0667b5b3fa`
  and
  `b9bfb2923ec3853c4373923a61bca7e340963251e40fab94f3dbf5bdc56480c0`.
- Source: 22/22 Git blobs and SHA-256 values match the basis and current bytes;
  five Remaining statuses remain `IN_PROGRESS` and basis-identical.
- Method: deterministic manager checks plus two fresh bounded read-only
  Agent-2 confirmations. No runtime test or service was run.

Validated fresh returns:

- control/parser/provenance `ACCEPT`, SHA-256
  `072d816045939e345a10ad837905b49153e6321d660bc72d153e5c2ca2f0d4fb`;
- substantive/package/preservation `ACCEPT`, SHA-256
  `fa2572ce449004e846bf6684328db54a18affe23eef16c100df0aa7a041d93b3`.

No child disagreement, blocker, unknown affecting acceptance, or waiver
remains.

## Corrected-control confirmation

The corrected raw status contains exactly one top-level
`control_label_erratum` and no repeated member at any object depth. Its exact
value is:

```json
{
  "classification": "NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED",
  "correct_paths": [
    "projects/chirality-app-dev/frontend/src/app/globals.css",
    "projects/chirality-app-dev/frontend/src/lib/shell/ansi.ts"
  ]
}
```

| Check | Result |
|---|---|
| Raw top-level occurrence count | exactly 1 |
| Duplicate-rejecting Python parser at every object depth | pass |
| Ordinary Python `json.load` | exact structured value and path order |
| Node `JSON.parse` | exact structured value and path order |
| jq | exact structured value and path order |

The immutable predecessor still reproduces exactly two unequal object/string
members, ordinary last-member path loss, and strict duplicate rejection at its
bound raw hash. The reissue therefore supersedes the defect additively rather
than erasing it. V1R2-001 is `REPAIRED_SUSTAINED`.

The earlier wrong labels `frontend/src/styles/globals.css` and
`frontend/src/lib/ansi.ts` remain nonexistent historical control evidence.
Current manifest, child, ledger, mapping, matrix, and package evidence use
only the corrected paths. The earlier erratum remains
`NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED`.

## Complete 14-row fidelity confirmation

All 19 columns, source bindings, child/integrated candidates, boundaries,
alternatives, rejections, action classes, mapping statuses, blockers, groups,
and integrated locations remain exact.

| Child row | Path | Fidelity | Result |
|---:|---|---|---|
| 1 | `frontend/src/app/globals.css` | `REPAIRED_MATERIAL_LOSS` | pass — shared/ownerless and capability-split choices retained |
| 2 | `frontend/src/app/page.tsx` | `FAITHFUL_COMPRESSION` | pass |
| 3 | `frontend/src/components/shell/chat-markdown.tsx` | `EXACT` | pass |
| 4 | `frontend/src/components/shell/document-view.tsx` | `EXACT` | pass |
| 5 | `frontend/src/components/shell/file-picker.tsx` | `REPAIRED_MATERIAL_LOSS` | pass — DEL-02-04 and DEL-09-06 retained; DEL-06-04 substitution rejected |
| 6 | `frontend/src/components/shell/session-list-view.tsx` | `EXACT` | pass |
| 7 | `frontend/src/components/shell/subagent-stream-view.tsx` | `FAITHFUL_COMPRESSION` | pass |
| 8 | `frontend/src/components/shell/tool-stream-view.tsx` | `FAITHFUL_COMPRESSION` | pass |
| 9 | `frontend/src/components/workspace/harness-events-provider.tsx` | `REPAIRED_MATERIAL_LOSS` | pass — shared-infrastructure choice retained |
| 10 | `frontend/src/lib/shell/ansi.ts` | `EXACT` | pass |
| 11 | `frontend/src/lib/shell/document-view-state.ts` | `EXACT` | pass |
| 12 | `frontend/src/lib/shell/harness-event-buffer.ts` | `FAITHFUL_COMPRESSION` | pass |
| 13 | `frontend/src/lib/shell/harness-event-views.ts` | `REPAIRED_MATERIAL_LOSS` | pass — split/shared choices retained |
| 14 | `frontend/src/lib/workspace/navigation-intent.ts` | `FAITHFUL_COMPRESSION` | pass |

Totals are exactly 5 `EXACT`, 5 `FAITHFUL_COMPRESSION`, 4
`REPAIRED_MATERIAL_LOSS`, 0 `EXPLICITLY_REASONED_REJECTION`, and 0 unexplained.

## Complete 22-row disposition

Every row passes as an evidence-supported, unaccepted `OWNER_CLASS` proposal.
D-APP-60/D-APP-64 screening confirms that accepting a path mapping or physical/
shared boundary would create ownership or accepted scope meaning that the
current Remaining records withhold.

| # | Path | Disposition |
|---:|---|---|
| 1 | `frontend/src/app/globals.css` | pass; full semantic and shared/split alternatives retained |
| 2 | `frontend/src/app/page.tsx` | pass |
| 3 | `frontend/src/app/api/working-root/deliverable/content/route.ts` | pass; physical owner remains unresolved |
| 4 | `frontend/src/components/shell/chat-markdown.tsx` | pass; exact two-consumer graph |
| 5 | `frontend/src/components/shell/document-view.tsx` | pass |
| 6 | `frontend/src/components/shell/file-picker.tsx` | pass; UI/security boundaries repaired |
| 7 | `frontend/src/components/shell/session-list-view.tsx` | pass |
| 8 | `frontend/src/components/shell/subagent-stream-view.tsx` | pass |
| 9 | `frontend/src/components/shell/tool-stream-view.tsx` | pass |
| 10 | `frontend/src/components/workspace/harness-events-provider.tsx` | pass; shared-infrastructure choice retained |
| 11 | `frontend/src/lib/shell/ansi.ts` | pass; sole importer graph sustained |
| 12 | `frontend/src/lib/shell/document-view-state.ts` | pass |
| 13 | `frontend/src/lib/shell/harness-event-buffer.ts` | pass |
| 14 | `frontend/src/lib/shell/harness-event-views.ts` | pass; split/shared choices retained |
| 15 | `frontend/src/lib/workspace/navigation-intent.ts` | pass |
| 16 | `frontend/src/types/chirality-window.d.ts` | pass; omitted `apiKey` remains observation only |
| 17 | `frontend/electron/preload.ts` | pass; integration owner remains unresolved |
| 18 | `frontend/src/lib/harness/scripted-agent-sdk-proof.ts` | pass; not packaged proof |
| 19 | `frontend/scripts/assert-harness-contract-deps.mjs` | pass |
| 20 | `frontend/scripts/generate-tool-catalog.mjs` | pass; mechanism only |
| 21 | `frontend/scripts/pec-scratch-server.mjs` | pass; V1-005 remains nonblocking |
| 22 | `frontend/scripts/run-pec-bridge-rehearsal.ts` | pass; F-APP-3 retained |

All classifications remain `OWNER_CLASS`; no `DISPOSITION_CLASS`,
`NO_REPAIR`, `BLOCKED_INPUT`, or `STALE_INPUT` row exists.

## Nine-group confirmation

The exact population is `5+4+6+1+1+1+1+1+2=22`, with no overlap or omission.
Each group is decision-ready as a proposal and retains all material choices,
boundaries, proposal attribution, and authority fences.

| Group | Paths | Result |
|---|---:|---|
| 1. Shell integration/shared presentation | 5 | pass |
| 2. Working-root document UX | 4 | pass |
| 3. Replay/projection | 6 | pass |
| 4. Working-root content route | 1 | pass |
| 5. Catalog generation | 1 | pass |
| 6. Electron preload | 1 | pass |
| 7. Network-policy fixture | 1 | pass |
| 8. Contract dependency lint | 1 | pass |
| 9. PEC evidence | 2 | pass |

## Package, findings, and preservation

All 14 package hashes remain exactly those bound in the corrected status:

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

Schemas remain 22×13, 22×7, and 14×19. All files end in exactly one LF,
contain no horizontal trailing whitespace, and pass no-index hygiene.

Finding state:

- V1-001 through V1-004: repaired and sustained;
- V1R-001 and V1R-002: repaired and sustained;
- V1R2-001: repaired and sustained by additive control reissue;
- earlier wrong-label erratum: sustained nonblocking;
- V1-005: nonblocking and unrepaired.

All prior R1/V1 packages, children, evaluation outputs, plan, graph,
decisions, receipts, authority, lifecycle, subject, Remaining, Git index, ref,
branch, and PR state remain unchanged. Evaluation writes are confined to its
two authorized roots. No ownership, mapping, Remaining closure, source repair,
lifecycle transition, release, publication, or Git authority is smuggled into
the derivative.

## Unknowns, waivers, and next gate

No blocking unknown or conflict remains. Existing proposal-visible unknowns
include the content-route and Electron-preload physical owners, renderer
`apiKey` typing, stale catalog-document pointers, and stale network-proof
metadata. They do not invalidate the discovery package or authorize repair.

Waivers: none.

HELP_HUMAN is the next gate. It may accept this evaluation return and consider
owner-slate routing. This EVALUATION does not itself accept or route the slate
or release W1. Rerun from the earliest stale node on any basis, parser,
source, Remaining, authority, child, package, schema, fidelity, containment,
or downstream-state change.
