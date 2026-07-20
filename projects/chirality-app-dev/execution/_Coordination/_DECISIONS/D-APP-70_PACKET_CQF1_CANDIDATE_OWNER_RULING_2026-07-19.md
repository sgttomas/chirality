# D-APP-70 — CQ-F1 Candidate Owner Ruling

**Status:** PROPOSAL / `AWAITING_RULING`
**Decision ID:** D-APP-70
**Prepared:** 2026-07-19
**Authority posture:** owner decision required; this packet is not a ruling
**Basis:** `57652ba1cd0905e8f47131e4c4ebf518272f7c16`

## 1. Decision requested

Choose the candidate physical/integration ownership treatment for all 22 CQ-F1
paths, organized into the nine non-overlapping groups below. Every row remains
an unaccepted `OWNER_CLASS` proposal until the owner rules and a separate
ruling record is added.

V1-RECHECK3 validates that this slate is ready for an owner decision. It does
not validate, create, transfer, or accept ownership. Code, call graphs, and
tests are evidence for candidate selection, not authority.

## 2. Accepted evidence and immutable bindings

- Accepted V1-RECHECK3 return:
  `28fd98d46a160016d6fd875ea0281c07ee85971054b4e7de45fbe9af83b62936`.
- Accepted V1-RECHECK3 status:
  `9f71e6d7604439f69d94c78cea66bbe0f1feb2924b06adfcc37e0b25e3274460`.
- Fresh control/parser child return:
  `072d816045939e345a10ad837905b49153e6321d660bc72d153e5c2ca2f0d4fb`.
- Fresh substantive/preservation child return:
  `fa2572ce449004e846bf6684328db54a18affe23eef16c100df0aa7a041d93b3`.
- Ordered 22-path manifest SHA-256:
  `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`.

The unchanged activated derivative has 14 files:

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

The two proposal CSVs remain 22×13 and 22×7 in exact manifest order, all 22
rows are `OWNER_CLASS`, and every mapping status is proposal-only. The nine
groups have population `5+4+6+1+1+1+1+1+2=22`. The 14×19 fidelity matrix
remains 5 exact, 5 faithful compressions, 4 repaired material losses, 0
reasoned rejections, and 0 unexplained losses.

## 3. Group decisions

### 1. Shell integration and shared presentation — 5 paths

**Affected paths**

1. `projects/chirality-app-dev/frontend/src/app/globals.css`
2. `projects/chirality-app-dev/frontend/src/app/page.tsx`
3. `projects/chirality-app-dev/frontend/src/components/shell/chat-markdown.tsx`
4. `projects/chirality-app-dev/frontend/src/lib/shell/ansi.ts`
5. `projects/chirality-app-dev/frontend/src/lib/workspace/navigation-intent.ts`

**Recommendation 1:** adopt the exact proposed mapping: DEL-02-01 for
`page.tsx` and `navigation-intent.ts`; DEL-02-01 primary for
`chat-markdown.tsx` and its sole-imported `ansi.ts` helper; and DEL-02-01 as
the `globals.css` physical integration lead without semantic transfer.

Retain DEL-02-03 as the current production consumer of ChatMarkdown/ANSI and
DEL-08-02 as the persona/guard boundary for navigation intent. For
`globals.css`, retain DEL-02-02 Pipeline/Workbench, DEL-02-03 Working Root,
DEL-02-04 pane/toolkit, DEL-02-05 API-key/runtime feedback, DEL-05-04
projection, DEL-06-01 mode/permission, DEL-08-02 persona routing, DEL-08-05
child-run, DEL-09-06 renderer-security, and the recorded DEL-02-02/DEL-08-03
Pipeline-selector boundary. The integration lead owns physical coordination,
not those semantics.

**Alternatives:** designate `globals.css` as an ownerless/shared physical file;
split it by capability before assigning path leads; select DEL-02-04 as the
stylesheet's UI-state physical lead while preserving all named boundaries;
treat ChatMarkdown/ANSI as ownerless shared presentation utilities; or defer
the entire group unchanged.

### 2. Working-root document UX — 4 paths

**Affected paths**

1. `projects/chirality-app-dev/frontend/src/components/shell/document-view.tsx`
2. `projects/chirality-app-dev/frontend/src/components/shell/file-picker.tsx`
3. `projects/chirality-app-dev/frontend/src/lib/shell/document-view-state.ts`
4. `projects/chirality-app-dev/frontend/src/types/chirality-window.d.ts`

**Recommendation 2:** select DEL-02-03 as primary for all four paths. Retain
DEL-02-01 as the shell host for DocumentView and document-view state,
DEL-03-03 as DocumentView's route dependency, and DEL-09-04 as the
`chirality-window.d.ts` verification consumer. For FilePicker, retain
DEL-02-04 attachment UI state, DEL-09-06 and server routes as the enforceable
attachment-security boundary, and DEL-02-01 as shell host. DEL-06-04
write/edit enforcement is not a substitute and has no separately evidenced
current FilePicker boundary.

**Alternatives:** carve FilePicker out to an explicitly named physical owner
while retaining DEL-02-03 Working Root behavior, DEL-02-04 UI state, and
DEL-09-06/server enforceable security; split another named path only with its
consumer boundaries intact; or defer the group unchanged.

### 3. Replay and projection — 6 paths

**Affected paths**

1. `projects/chirality-app-dev/frontend/src/components/shell/session-list-view.tsx`
2. `projects/chirality-app-dev/frontend/src/components/shell/subagent-stream-view.tsx`
3. `projects/chirality-app-dev/frontend/src/components/shell/tool-stream-view.tsx`
4. `projects/chirality-app-dev/frontend/src/components/workspace/harness-events-provider.tsx`
5. `projects/chirality-app-dev/frontend/src/lib/shell/harness-event-buffer.ts`
6. `projects/chirality-app-dev/frontend/src/lib/shell/harness-event-views.ts`

**Recommendation 3:** select DEL-05-04 primary for all six live/replay view
and projection paths. Retain DEL-05-01 storage and DEL-02-01 hosting for
SessionListView; DEL-08-05 child-run semantics for SubagentStreamView;
DEL-05-05 artifact semantics and PKG-06 execution policy for ToolStreamView;
DEL-05-02 schema/persistence and DEL-02-01 composition for
HarnessEventsProvider; DEL-05-02 persistence for the event buffer; and
DEL-05-02 event vocabulary/persistence, DEL-05-05 tool-result/artifact,
DEL-06-01 permission, and DEL-08-05 child-run semantics for harness event
views.

**Alternatives:** designate HarnessEventsProvider to a shared application-
infrastructure owner; split `harness-event-views.ts` by capability owner;
treat it as an ownerless/shared projection utility; make another explicitly
named integration owner primary for a named physical path while preserving
all semantic boundaries; or defer the group unchanged.

### 4. Working-root content route — 1 path

**Affected path:**
`projects/chirality-app-dev/frontend/src/app/api/working-root/deliverable/content/route.ts`.

**Recommendation 4:** select DEL-07-03 as the nearest existing physical
route-contract owner while retaining DEL-07-01 containment and DEL-02-03
consumption boundaries. This route is not reassigned to its prior DEL-03-03
Remaining container merely because that container held the CQ-F1 item.

**Alternatives:** explicitly name another physical route-contract integration
owner while preserving both boundaries, or defer unchanged.

### 5. Catalog generation — 1 path

**Affected path:**
`projects/chirality-app-dev/frontend/scripts/generate-tool-catalog.mjs`.

**Recommendation 5:** select DEL-06-02 only for the deterministic generator
and check mechanism. Generated-catalog semantics remain distributed among
their ruled capability owners.

**Alternatives:** name an explicit shared tooling/integration owner for the
mechanism, or defer unchanged. Semantic centralization under DEL-06-02 or any
other single deliverable is not an option in this packet.

### 6. Electron preload — 1 path

**Affected path:**
`projects/chirality-app-dev/frontend/electron/preload.ts`.

**Recommendation 6:** establish an explicit shared implementation boundary
across DEL-02-03 `selectDirectory`, DEL-02-05 `apiKey`, and DEL-09-06
`safeStorage`/security. Require a named physical integration lead before any
repair or path-level ownership application.

**Alternatives:** name DEL-02-03, DEL-02-05, or DEL-09-06 as physical
integration lead while retaining all three semantic interests, or defer
unchanged. No lead choice transfers the other two semantics.

### 7. Network-policy fixture — 1 path

**Affected path:**
`projects/chirality-app-dev/frontend/src/lib/harness/scripted-agent-sdk-proof.ts`.

**Recommendation 7:** select DEL-09-06 primary, retain the DEL-04-01 evidence
edge, and record that this dev/test fixture is not packaged proof.

**Alternatives:** select DEL-04-01 primary with DEL-09-06 retaining the
network-policy boundary; designate an explicit shared fixture; or defer
unchanged.

### 8. Contract dependency lint — 1 path

**Affected path:**
`projects/chirality-app-dev/frontend/scripts/assert-harness-contract-deps.mjs`.

**Recommendation 8:** select DEL-03-01 for the semantic dependency lint and
retain DEL-09-05 as the release-quality consumer.

**Alternatives:** establish an explicit shared lint-utility boundary while
preserving DEL-03-01 semantics and DEL-09-05 consumption, or defer unchanged.

### 9. PEC evidence — 2 paths

**Affected paths**

1. `projects/chirality-app-dev/frontend/scripts/pec-scratch-server.mjs`
2. `projects/chirality-app-dev/frontend/scripts/run-pec-bridge-rehearsal.ts`

**Recommendation 9:** select DEL-10-04 primary for both evidence-driver paths
while retaining DEL-10-03's proposal-tool verification interest and F-APP-3.
The selection does not authorize an apply surface or hard-fence crossing.

**Alternatives:** explicitly split physical ownership by evidence-driver and
proposal-tool function while preserving DEL-10-04, DEL-10-03, and F-APP-3
boundaries, or defer unchanged.

## 4. Owner response surface

- **Option A (recommended):** approve recommendations 1–9 exactly as stated.
  Exact response: `APPROVE: D-APP-70 Option A`.
- **Option B:** approve only named recommendations and explicitly name every
  group-level alternative or substitution being selected. Exact response
  form: `APPROVE: D-APP-70 Option B — G1=RECOMMENDATION; G2=DEFER; ...`.
  The owner may list only the groups being ruled; every omitted group remains
  `AWAITING_RULING` unchanged. Silence never selects its recommendation.
- **Option C:** defer all nine groups unchanged. Exact response:
  `APPROVE: D-APP-70 Option C`.

For Option B, wording applies only to explicitly named groups. A substitution
must identify the group and chosen alternative or new physical/integration
owner; ambiguous or silent wording does not select a recommendation.

## 5. Risks and validation implications

- A physical/integration lead can be mistaken for semantic ownership. Every
  retained boundary above must survive any ruling transcription, mapping
  application, repair brief, and backcheck.
- Shared physical files can create overlapping-write and integration risks.
  Any later implementation stage must serialize the integration owner or
  partition disjoint writes under a separately authorized W1 brief.
- Deferral preserves all 22 rows as owner-class proposals and leaves their
  five Remaining containers unchanged.
- A future ruling must be recorded in a separate D-APP-70 ruling record and
  update the register before it has effect. Partial rulings leave unmentioned
  groups `AWAITING_RULING`.
- Before any mapping application or repair, revalidate the exact source,
  Remaining, authority, package, and ruling bindings. Material drift reruns
  from the earliest stale concordance or evaluation node.
- Any authorized application requires exact 22-row/group accounting and a
  fresh post-change backcheck. Existing V1 accepts decision readiness only.

Even a future owner mapping ruling does not authorize subject or derivative-
package repair, W1, lifecycle transition, release, issuance, publication,
hard-fence crossing, or Git action. Each requires its own governing gate.

## 6. Governed record effects of this packet

This proposal preparation creates only this packet, one append-only
`AWAITING_RULING` register row, Receipt-78, and the R2 instance handoff and
terminal records. No ruling record exists. No mapping, owner selection,
acceptance, source change, Remaining change, or downstream release is made.
