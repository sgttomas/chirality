# BLOCK

- **Audit:** governance/package/erratum recheck
- **Role:** fresh bounded read-only Agent 2 generalist
- **Basis:** `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- **Subject disposition:** substantive 22-row derivative and owner slate are
  internally coherent and decision-ready as proposals, but remain unaccepted
- **Terminal verdict:** `BLOCK`
- **Blocking finding:** `GPE-001`
- **Waivers:** none

## GPE-001 — duplicate status member loses machine-visible path provenance

**Severity:** material blocking control-record non-conformance.

The raw R1-REPAIR2 `STATUS.json` is bound exactly to SHA-256
`a48d9a634f279726f9c3cc4b23fb8e558b58f34502cd03ae6c87c5f6f4537a44`.
It contains two top-level members named `control_label_erratum`, in this raw
order:

1. Lines 56–62: an object containing classification
   `NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED` and exact
   `correct_paths` values
   `projects/chirality-app-dev/frontend/src/app/globals.css` and
   `projects/chirality-app-dev/frontend/src/lib/shell/ansi.ts`.
2. Line 103: the string
   `NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED`.

The occurrence count is exactly two. The classification text agrees, but the
values are not structurally equivalent: only the first occurrence carries the
two corrected paths.

### Parser behavior and impact

| Check | Reproduced result | Consequence |
|---|---|---|
| Node `JSON.parse` | accepts, last member wins | `control_label_erratum` is a string; both `correct_paths` values are absent from the parsed record |
| `jq` | accepts, last member wins | same string result and same corrected-path loss |
| Python duplicate-detecting `object_pairs_hook` | rejects | the entire status record is unavailable to a fail-closed duplicate detector |
| Raw ordered-pair decode | preserves both | confirms object first, string second, and no hidden third occurrence |

Repository managed-delegation status reads use ordinary `JSON.parse`, so the
observed repository parser follows the last-wins branch. No current in-scope
consumer was found that reads this ad hoc erratum member, so the terminal
`status`, `accepted`, and release fields are not presently changed. A consumer
of `control_label_erratum.correct_paths`, however, receives `undefined` (or a
type error under a structured validator), while a duplicate-rejecting status
validator rejects the entire record. This is actual parser-visible path and
provenance loss and a plausible automation/schema failure, not merely a
cosmetic duplication.

RFC 8259 §4 says object member names should be unique and warns that
non-unique behavior is unpredictable across implementations. The repository
does not expose a formal JSON Schema for these ad hoc status extensions, but
the first member itself declares a structured shape that the later string
destroys under the repository's ordinary parser. The runtime contract also
treats `STATUS.json` as a materialized coordination summary, not an
unstructured archival byte stream.

The provisional
`NONCONSEQUENTIAL_DUPLICATE_JSON_MEMBER_ERRATUM` disposition is therefore
**refuted under the sealed brief's explicit fail-closed criterion**. The
independent package surfaces prevent this defect from concealing a source,
ownership, authority, acceptance, or release change, but they do not restore
the missing paths to an ordinary parse of this status record. This finding
affects no substantive manifest row or proposal group; it blocks acceptance
of the R1-REPAIR2 terminal package as a conforming machine-readable input.

## Substantive row and classification audit

The frozen manifest reproduces as 22 rows, 22 unique paths, 22 existing files,
and ordered path-list SHA-256
`2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`.
All 22 worktree SHA-256 values and all 22 basis Git blobs match the ledger.
The five live Remaining containers reproduce as `14+1+1+4+2=22`; each is
`IN_PROGRESS`, each says the affinity is deferred without ownership or
mapping, and each is unchanged from the basis.

D-APP-60 fast reject was reperformed for every row. Every proposed mapping or
physical/shared-boundary choice would create the ownership or scope meaning
that the applicable Remaining record expressly withholds. D-APP-64 permits
reasoned candidate selection but cannot cross that scope/ownership boundary.
Accordingly all 22 `OWNER_CLASS` classifications are sustained; no row is
eligible for disposition-class execution, and no `BLOCKED_INPUT`,
`STALE_INPUT`, or `NO_REPAIR` row was found.

All rows have the same evaluation disposition:
`SUBSTANTIVE_PASS_UNACCEPTED_OWNER_CLASS_PROPOSAL`. No row, mapping, group, or
slate is accepted by this return.

## Nine proposal groups

| Group | Exact members | Count | Disposition |
|---:|---|---:|---|
| 1 | `globals.css`, `page.tsx`, `chat-markdown.tsx`, `ansi.ts`, `navigation-intent.ts` | 5 | substantive pass; owner choice required |
| 2 | `document-view.tsx`, `file-picker.tsx`, `document-view-state.ts`, `chirality-window.d.ts` | 4 | substantive pass; owner choice required |
| 3 | `session-list-view.tsx`, `subagent-stream-view.tsx`, `tool-stream-view.tsx`, `harness-events-provider.tsx`, `harness-event-buffer.ts`, `harness-event-views.ts` | 6 | substantive pass; owner choice required |
| 4 | working-root deliverable-content `route.ts` | 1 | substantive pass; physical route-owner ruling required |
| 5 | `generate-tool-catalog.mjs` | 1 | substantive pass; owner choice required |
| 6 | `preload.ts` | 1 | substantive pass; integration-owner ruling required |
| 7 | `scripted-agent-sdk-proof.ts` | 1 | substantive pass; owner choice required |
| 8 | `assert-harness-contract-deps.mjs` | 1 | substantive pass; owner choice required |
| 9 | `pec-scratch-server.mjs`, `run-pec-bridge-rehearsal.ts` | 2 | substantive pass; owner choice required |
| **Total** | exact frozen manifest, with no duplicate membership | **22** | proposal-only |

The slate presents complete proposal choices, material alternatives,
consumer/semantic/security boundaries, and rejection rationale. It does not
attribute any selection to the owner. It preserves D-APP-69's subject-write
fence, all lifecycle/release/publication/professional hard fences, continued
owner routing and W1 blocks, and the absence of owner acceptance. No smuggled
mapping, scope, repair, lifecycle, release, Git, or professional authority was
found.

## Sealed child and 14-row fidelity matrix

The sealed child brief and return match SHA-256 values
`7ee27d1f464460bc8e9fb39c87aebdc044e1440eddb8ddd735c3bb0667b5b3fa`
and
`b9bfb2923ec3853c4373923a61bca7e340963251e40fab94f3dbf5bdc56480c0`.
The child return has 14 unique rows in exact DEL-02-01 filtered-manifest
order, every required field, exact basis, and exact live/basis blob and
SHA-256 bindings. Its terminal containment records one child-return write,
zero subject/authority/Git writes, no tests, and no delegation.

`DEL02_01_CHILD_PACKAGE_FIDELITY.csv` reproduces exactly 14 rows and 19
columns, exact filtered-manifest order, exact source bindings, valid group and
integrated-location accounting, and these independently checked dispositions:

- `EXACT` (5): `chat-markdown.tsx`, `document-view.tsx`,
  `session-list-view.tsx`, `ansi.ts`, `document-view-state.ts`.
- `FAITHFUL_COMPRESSION` (5): `page.tsx`, `subagent-stream-view.tsx`,
  `tool-stream-view.tsx`, `harness-event-buffer.ts`,
  `navigation-intent.ts`.
- `REPAIRED_MATERIAL_LOSS` (4): `globals.css`, `file-picker.tsx`,
  `harness-events-provider.tsx`, `harness-event-views.ts`.
- `EXPLICITLY_REASONED_REJECTION` (0); unexplained differences (0).

The five compressions omit only rejected directory/host/analogy alternatives
whose rejection and rationale remain explicit in the matrix. The four prior
material losses are faithfully restored across the integrated package:

1. FilePicker retains DEL-02-03 primary, DEL-02-04 attachment UI state, and
   DEL-09-06/server enforceable attachment security; DEL-06-04 write/edit
   enforcement is expressly rejected as a substitute.
2. `globals.css` retains DEL-02-01 integration lead without semantic
   transfer, the complete capability-boundary inventory, and the materially
   distinct ownerless/shared-file and capability-split choices.
3. HarnessEventsProvider retains DEL-05-04 nearest, DEL-05-02 persistence,
   DEL-02-01 composition, cross-application consumers, and shared application
   infrastructure as an explicit owner alternative.
4. Harness event views retain DEL-05-04 nearest, all semantic owners, and
   explicit split-file and ownerless/shared projection-utility alternatives.

## CSV, package, and hash integrity

- `CQF1_PATH_LEDGER.csv`: exact 13-column schema, 22 rows, unique paths,
  manifest order, 22 `OWNER_CLASS` values, exact source bindings.
- `PROPOSED_MAPPING.csv`: exact 7-column schema, 22 rows, unique paths,
  manifest order, 22 `OWNER_CLASS` values.
- Fidelity CSV: exact 19-column schema and accounting stated above.
- Activated derivative: exactly 14 files. All 14 match the launch-bound
  SHA-256 manifest:
  - analysis `1e825d797ddf5c4a9757bb1984ae63be0bf6b053736fe1bd5a8f932d415d4035`;
  - slate `f6e630e9294c4779f87a0f7734667f565113127769cdaed3ab20b32cd099ce93`;
  - ledger `b56f87731920765279639d528393bae212403fe49ffb5de6c27065ddd4095288`;
  - classification `4f7d8d41b344daafd7f4533dcaaec5dc4859fa44561133181ce744006ed285fd`;
  - fidelity matrix `100445dd4e2054440776a60e1be36e53d7cdb0bf6cbe94b9e21555f420f1706c`;
  - handoff `9af95a170fa77149fac4cbe5bae7320e5abe357b39434a5c083a200ba80dbc75`;
  - DEL-02-01 note `0045d350a15c5fae07d0a0958096477c8fc057aedb8227cc433947feb3e6dafa`;
  - DEL-03-03 note `1ae7d3e728093a853e79240da5eaa91ce6407dc0c67a3b4c10a3cd3c656f6935`;
  - DEL-06-02 note `cd0b5b206c3ede37fb1eb3130b5a12cfece15ed1a1b498159ece87aed619f299`;
  - DEL-09-04 note `946d03791ae296397b39c8322dd6c48d6daf21bd65489ba07f24558045cb8a48`;
  - DEL-10-04 note `9a5e5291e30d3deb9a04992080c406c1499489b1696ee6fd361c4d27385fb59e`;
  - mapping `a01651fb49883d2f15971cbc8a85c5cff4c5039eeffb2500be6a78fd62378e86`;
  - QA `8cf4c42184a1ccd73577e11180562e2b9a576a9063728f4fd3c410227e92dbfd`;
  - run basis `f752abe6d078ec3f485621a9b1f15476db0667642bfb591ed20420d97c2e537d`.
- Every package file ends in exactly one LF and has no horizontal trailing
  whitespace. All 14 per-file no-index whitespace checks are clean.
- Changed/output accounting reproduces nine modified package files plus the
  new fidelity matrix (ten package paths), the R1-REPAIR2 return, and its
  terminal status. The four non-DEL-02-01 package notes remain byte-identical
  to R1-REPAIR. No R1-REPAIR2 child path exists.

## Earlier wrong-label erratum

The v8 wrong-label erratum remains correctly classified
`NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED`:

- wrong and nonexistent: `frontend/src/styles/globals.css`;
  current exact path: `projects/chirality-app-dev/frontend/src/app/globals.css`;
- wrong and nonexistent: `frontend/src/lib/ansi.ts`;
  current exact path:
  `projects/chirality-app-dev/frontend/src/lib/shell/ansi.ts`.

The full corrected paths occur in the R1-REPAIR2 return, frozen manifest,
sealed child, both 22-row CSVs, and fidelity matrix. The analysis, DEL-02-01
note, and slate bind the same basename rows and corrected semantics; QA binds
them to the exact manifest paths; handoff sustains V1R-003. The wrong labels
occur only in immutable historical control records or later erratum
discussions. They do not occur as a manifest, child, ledger, mapping, or
matrix row. No execution, evidence, write, authority, or acceptance target
used either wrong path.

## Preservation and containment

- R1-REPAIR2 terminal return hash matches
  `bb520447e5923a36fca6533379ff49458dbb0fbbfcefe6edbfaf7ae4f2f4a12a`;
  the raw duplicate-bearing status hash remains exactly preserved.
- All ten v9 V1-RECHECK bindings match, including return/status, protocol,
  report, findings, handoff, and both child launch/return pairs.
- V1-RETRY return/status and both child returns match the preserved v7 hashes.
  The original evaluation protocol/report/findings/handoff match the v8
  bindings. All five R1-RETRY child returns match the hashes recorded in QA.
- The orchestration plan and work graph remain bound to SHA-256
  `72d0860beb7fe4f80f4d66485982dc43f1f3199191289150688831e3bc9fd9c2`
  and `fce24371d3980b5169464bacc7f3cc40b21bde5a39dac42467d1dfca408a7008`.
- A basis diff over all 22 subject paths and five Remaining `_STATUS.md`
  paths is empty. `HEAD` and `origin/main` both equal the frozen basis. The
  Git index is clean. No ref, PR, lifecycle, authority, decision, receipt,
  plan/graph, subject, or historical package write was made by this audit.
- This audit's sole write is this `RETURN.md`; no test or service was run.

## Unknowns, repair, and rerun

No formal repository JSON Schema for the ad hoc `control_label_erratum` status
extension was found. That absence does not cure the demonstrated last-wins
path loss or strict-parser rejection.

Repair owner is the coordination workflow that owns the R1 instance status,
under a HELP_HUMAN versioned amendment. Do not rewrite the immutable raw
R1-REPAIR2 record. Emit a new additive control attempt/record with exactly one
structured `control_label_erratum` member containing both classification and
corrected paths, validate duplicate rejection and ordinary parse equivalence,
and bind the unchanged 14-file derivative and predecessors. No source,
Remaining, mapping, slate, authority, lifecycle, or Git repair is indicated.

After that control repair, rerun a fresh V1 check from the earliest stale
control node. Owner-slate routing and W1 remain blocked. Additional rerun
triggers remain source/Remaining/authority drift, any package or child hash
mismatch, unexplained fidelity loss, or a new material refutation.
