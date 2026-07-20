# Governance and Package Recheck Return

- **Verdict:** `BLOCK`
- **Auditor:** bounded read-only V1-RECHECK governance/package child
- **Basis:** `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- **Subject posture:** read-only
- **Sole write:** this `RETURN.md`
- **Subject writes:** 0
- **Waivers:** none

## Executive disposition

The repaired derivative reproduces the exact basis, 22-row manifest, 13-file
package, 22 `OWNER_CLASS` classifications, and nine-group population. The
V1-004 ten-file EOF normalization passes, original V1 evidence remains bound
and unchanged, and the v8 control-label erratum is nonconsequential: execution
used the two exact manifest paths and never targeted either erroneous label.

The package nevertheless remains `BLOCK` because fresh-child fan-in is lossy
for `file-picker.tsx`. The required fresh 14-row child replaces the predecessor
DEL-06-04 framing with a material DEL-09-06/server attachment-security
boundary. The integrated ledger, mapping, and group 2 silently retain
DEL-06-04 and omit DEL-09-06. That variance is not disclosed or reasoned, and
the live DEL-09-06 scope expressly covers attachment validation, server
revalidation, unsafe-file rejection, and retry/failure behavior. The affected
row and group are therefore not decision-ready under the sealed fan-in and
material-alternative criteria.

No mapping or slate is accepted by this return. W1 remains blocked.

## Basis, bindings, and package schema

- `HEAD` is the exact frozen basis.
- `CQF1_SCOPE.csv` has 22 rows, 22 unique paths, and 22 existing paths in
  frozen order. SHA-256 over the newline-terminated ordered path list is
  `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`.
- The five Remaining populations reproduce as DEL-02-01 14, DEL-03-03 1,
  DEL-06-02 1, DEL-09-04 4, and DEL-10-04 2. Each `_STATUS.md` remains
  `IN_PROGRESS`, retains its no-ownership/no-mapping statement, and has no
  basis diff.
- The seven sealed R1-REPAIR bindings all match: terminal return
  `d9cd30ad...157e`, status `ad5087ac...ebb`, fresh-child brief
  `7ee27d1f...3fa`, fresh-child return `b9bfb292...0c0`, ledger
  `c4425242...054`, mapping `447b129e...0a3`, and slate
  `7545cb34...812`.
- The fresh child parses as JSON; its required top-level schema is present.
  It contains the exact 14 DEL-02-01 manifest rows in filtered manifest order,
  14 unique source blobs and SHA-256 values matching the basis, every required
  row field, 14 `OWNER_CLASS` results, and a read-only containment return.
- `CQF1_PATH_LEDGER.csv` and `PROPOSED_MAPPING.csv` parse with their declared
  13- and 7-column schemas. Both have 22 unique, fully populated rows in exact
  manifest order. Every integrated source Git blob and SHA-256 recomputes.

All 13 package-file hashes match the R1-REPAIR terminal manifest:

| File | SHA-256 |
|---|---|
| `AFFINITY_AND_MAPPING_ANALYSIS.md` | `4da75d8ca90d7fbe205f794007042f35279a4f67ea5a7f249a542535ebd81783` |
| `CANDIDATE_OWNER_SLATE.md` | `7545cb34f7a34b9a8743e52ff1f3885f6acc6ca21550eca507965d0da739f812` |
| `CQF1_PATH_LEDGER.csv` | `c4425242ca66736a793a611ad936219c8e700c0cf8e2c1011b4ff60fe9c62054` |
| `DECISION_CLASSIFICATION.md` | `e2a689667b74aa75749ee3380904321aa5530f827c6a8a975e9f3b1da4d57bb5` |
| `HANDOFF.md` | `0baed092aab4f1959f4a63cdd749d524ea7ed30e55269fa6e0c5ba900b660910` |
| `PACKAGE_NOTES/DEL-02-01.md` | `c9acf1480ce84ddcb9a4f1ac0852dd55511bfe423304cea77a1d14b530fd07f1` |
| `PACKAGE_NOTES/DEL-03-03.md` | `1ae7d3e728093a853e79240da5eaa91ce6407dc0c67a3b4c10a3cd3c656f6935` |
| `PACKAGE_NOTES/DEL-06-02.md` | `cd0b5b206c3ede37fb1eb3130b5a12cfece15ed1a1b498159ece87aed619f299` |
| `PACKAGE_NOTES/DEL-09-04.md` | `946d03791ae296397b39c8322dd6c48d6daf21bd65489ba07f24558045cb8a48` |
| `PACKAGE_NOTES/DEL-10-04.md` | `9a5e5291e30d3deb9a04992080c406c1499489b1696ee6fd361c4d27385fb59e` |
| `PROPOSED_MAPPING.csv` | `447b129e3aa21289d5681b9df208b83a20f1ad1cbcc64e85c398f05f266300a3` |
| `QA.md` | `cb639d202f45853e6c5928c31f3a8e9e0bdf66d652ab704eb7e4ad5aaeaa20dd` |
| `RUN_BASIS.md` | `63d62fb30a28781135ba141498958ece700571c1bff1137ff7ceae8314e4056d` |

## Blocking finding GOV-RECHECK-001 — lossy FilePicker fan-in

The fresh child records for
`projects/chirality-app-dev/frontend/src/components/shell/file-picker.tsx`:

- candidate: DEL-02-03 primary for Working Root browsing;
- retained state boundary: DEL-02-04 attachment UI state;
- retained security boundary: DEL-09-06/server routes;
- normative sources: DEL-02-03, DEL-02-04, and DEL-09-06 ScopeOfWork;
- competing candidates: DEL-02-04, DEL-09-06, and DEL-02-01.

The integrated package instead records DEL-02-03 primary with DEL-02-04
persistence and DEL-06-04 path enforcement in both CSVs and group 2. It omits
DEL-09-06 and cites DEL-06-04 rather than the fresh child's DEL-09-06 source.
No package disagreement or selection rationale explains that substitution.

The omitted boundary is material, not label-level:

- `file-picker.tsx` filters supported attachment extensions and emits
  `UiAttachment` records while relying on server routes for enforceable checks;
- DEL-09-06 `ScopeOfWork.md:58-59,71-72,84-85,151-156` expressly covers
  attachment extension/type/path/symlink/readability/budget validation,
  server revalidation of non-authoritative client metadata, and attachment
  failure/retry behavior;
- DEL-06-04 is principally the write/edit and mutation-hook path-policy slice.
  Its attachment/write-relevant applicability does not erase DEL-09-06's
  explicit security/evidence boundary.

This fails the launch brief's requirement to compare every fresh-child row,
preserve disagreements, avoid lossy fan-in, and present every material
boundary to the owner. It affects manifest row 6 and owner group 2.

The exact owning repair is RECONCILIATION. It must re-fan-in the FilePicker row
from the immutable fresh child; preserve DEL-02-03 as the proposal-only
primary and DEL-02-04 as the local-state boundary; add the material DEL-09-06
server/attachment-security boundary; and explicitly determine, from current
evidence, whether DEL-06-04 remains a distinct material boundary or should be
rejected. The result must propagate through the ledger, mapping, analysis,
DEL-02-01 note, group 2 slate, QA/handoff/bindings, and terminal accounting.
Then package hashes and V1 must rerun. This return performs none of that
repair.

## D-APP-60 / D-APP-64 classification

All 22 `OWNER_CLASS` classifications are sustained. Every current Remaining
entry says the recorded affinity asserts no ownership or mapping. Accepting
any proposed path mapping or shared physical/integration boundary would create
the missing normative ownership/scope meaning. That hits the D-APP-60 limits
and D-APP-64 section 5.1 scope/boundary, new-normative-content, and
claim-warrant fast rejects before reasoned selection can authorize effect.
D-APP-69 expressly authorizes discovery only and withholds mapping acceptance.

None of the rows is:

- `DISPOSITION_CLASS`, because the missing ownership premise is not already
  accepted and the proposed act would create normative content;
- `NO_REPAIR`, because the question is an unresolved mapping/boundary act,
  not whether implementation exists;
- `BLOCKED_INPUT` or `STALE_INPUT`, because the exact basis, source bindings,
  Remaining state, and governing authority are available and current.

Reasoned selection lawfully narrows candidates and alternatives but cannot
override the fast-reject result. The package remains derivative proposal
evidence, not authority or decomposition truth.

## Exact 22-row and nine-group disposition

Rows 1-5 and 7-22 pass this governance/package recheck subject to the separate
technical audit. Row 6 is `BLOCK` under GOV-RECHECK-001. All classifications
remain `OWNER_CLASS`:

| Rows | Governance/package disposition | Classification |
|---|---|---|
| 1 `globals.css`; 2 `page.tsx`; 3 content `route.ts`; 4 `chat-markdown.tsx`; 5 `document-view.tsx` | package/fan-in pass | `OWNER_CLASS` |
| 6 `file-picker.tsx` | `BLOCK` — lossy fresh-child boundary fan-in | `OWNER_CLASS` |
| 7 `session-list-view.tsx`; 8 `subagent-stream-view.tsx`; 9 `tool-stream-view.tsx`; 10 `harness-events-provider.tsx`; 11 `ansi.ts` | package/fan-in pass | `OWNER_CLASS` |
| 12 `document-view-state.ts`; 13 `harness-event-buffer.ts`; 14 `harness-event-views.ts`; 15 `navigation-intent.ts`; 16 `chirality-window.d.ts` | package/fan-in pass | `OWNER_CLASS` |
| 17 `preload.ts`; 18 `scripted-agent-sdk-proof.ts`; 19 contract-dependency lint; 20 catalog generator; 21 PEC scratch server; 22 PEC rehearsal | package/fan-in pass | `OWNER_CLASS` |

The nine group populations are exactly `5+4+6+1+1+1+1+1+2=22`, with 22
unique memberships and no omission or duplication:

| Group | Paths | Disposition |
|---|---:|---|
| 1. Shell integration and shared presentation | 5 | package decision-ready |
| 2. Working-root document UX | 4 | `BLOCK` — FilePicker omits fresh DEL-09-06 boundary |
| 3. Replay and projection | 6 | package decision-ready; DEL-05-02/05-05/06-01/08-05 boundaries retained |
| 4. Working-root content route | 1 | decision-ready owner/integration choice |
| 5. Catalog generation | 1 | decision-ready mechanism-only choice |
| 6. Electron preload | 1 | decision-ready unresolved integration-owner choice |
| 7. Network-policy fixture | 1 | decision-ready evidence-boundary choice |
| 8. Contract dependency lint | 1 | decision-ready owner/consumer choice |
| 9. PEC evidence | 2 | decision-ready with DEL-10-03 interest and F-APP-3 retained |

All nine are truthfully proposal-only and state that acceptance does not
authorize implementation, lifecycle, release, publication, or Remaining
closure. Rejection leaves the current affinity-only/no-mapping state. Group 2
cannot be routed until its evidence and retained boundaries match the fresh
child or a reasoned disagreement is made explicit.

## V1-004 EOF repair and V1-005 preservation

`V1-004` passes. The immutable original V1 record identified exactly ten
files with two terminal LF bytes. Direct current byte inspection finds exactly
one terminal LF in those same ten files:

1. `CANDIDATE_OWNER_SLATE.md`
2. `DECISION_CLASSIFICATION.md`
3. `HANDOFF.md`
4. `PACKAGE_NOTES/DEL-02-01.md`
5. `PACKAGE_NOTES/DEL-03-03.md`
6. `PACKAGE_NOTES/DEL-06-02.md`
7. `PACKAGE_NOTES/DEL-09-04.md`
8. `PACKAGE_NOTES/DEL-10-04.md`
9. `QA.md`
10. `RUN_BASIS.md`

The other three package files also end in exactly one LF. All 13 have no
horizontal trailing whitespace, and per-file no-index diff hygiene plus
tracked `git diff --check` produces no finding. The immutable V1 defect
record, exact repair amendment, R1 changed-path accounting, current bytes, and
recomputed 13-file manifest provide a coherent exact-normalization chain.

`V1-005` remains nonblocking and unrepaired. The source comment in
`pec-scratch-server.mjs` still omits the third live-LLM-demo caller; the third
import remains present. R1-REPAIR status/return/handoff continue to identify
V1-005 as preserved outside repair scope, and no source repair or authority
conversion occurred.

## Original V1 and predecessor preservation

All eight sealed original-V1 bindings match exactly:

- V1-RETRY return `d0952cbe...d8b` and status `d22f1431...aaf`;
- original evaluation protocol `bc18cd34...52a`, report
  `2157d8ad...2b0`, findings `ea9d9266...10c`, and handoff
  `a82b2b27...ea9`;
- original technical child `a17d4aeb...706` and governance child
  `aa3b8a69...041`.

The original R1 launch/return/status also retain
`c8810c00...0c7`, `b682a43a...265`, and `197a83a7...a06`. The five
R1-RETRY child-return hashes remain exactly
`6ba2cecb...45b`, `83387f67...3b1`, `2d708240...50e`,
`4b5bd686...aa2`, and `70e4aa4a...ba2`. Earlier children are visibly
predecessor evidence and are not represented as the fresh R1-REPAIR child.

## Control-label erratum disposition

The v8 disposition `NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM` is sustained.
The incorrect labels are control metadata in preserved v7/R1-REPAIR launch
and status surfaces:

- `frontend/src/styles/globals.css`; and
- `frontend/src/lib/ansi.ts`.

Neither path exists. Neither appears in `CQF1_SCOPE.csv`, the fresh child
brief/return, either integrated CSV, package analysis/slate/notes/QA, or the
terminal package manifest. Those execution/evidence surfaces instead use:

- `projects/chirality-app-dev/frontend/src/app/globals.css`, Git blob
  `6eb6d932410368d2163208fa40ec08061a4c9bb8`; and
- `projects/chirality-app-dev/frontend/src/lib/shell/ansi.ts`, Git blob
  `53500f33e066567f39f03978fd7f59f6b8ade9e0`.

The correction was recorded additively in v8 without rewriting history. The
error changed no manifest member, inspected or written path, source binding,
objective, authority, risk, write ownership, classification, acceptance
criterion, or downstream gate. It therefore does not conceal a consequential
amendment and is not an additional blocker.

## Containment, mutation, unknowns, and rerun

- Current tracked diff from the basis contains only the parent-owned
  `HANDOFF_STATE.md` append carrying live updates v5-v8. All 22 subject paths,
  five `_STATUS.md` files, plans, `WORK_GRAPH.json`, decisions, registers,
  receipts, authority, lifecycle, historical blocked derivative, and other
  tracked governance surfaces have no basis diff.
- R1-REPAIR writes are confined to the activated derivative and its instance
  root. Original R1/R1-RETRY/V1/V1-RETRY evidence is hash-preserved.
- This child made no subject, package, control-integration, evaluation-package,
  lifecycle, authority, Git/index/ref/PR, or external-state write. Its sole
  write is this return.
- No tests or services were run. The question is static derivative governance,
  schema, provenance, and decision readiness.
- No waiver resolves the FilePicker fan-in mismatch. Unknowns that remain
  proposal-visible include the content-route and Electron-preload physical
  integration owner. They do not cure or enlarge GOV-RECHECK-001.

Required rerun: RECONCILIATION repairs only the FilePicker fan-in and every
affected derivative reference under fresh parent authority, recomputes the
13-file manifest and control bindings, and returns terminally. A fresh V1
recheck then reruns from the repaired package binding. Any source, Remaining,
authority, fresh-child, or other package-byte drift reruns from its earliest
stale node. Until a terminal V1 `ACCEPT` is accepted by HELP_HUMAN, the slate
and W1 remain blocked and no ownership, repair, lifecycle, or release effect
exists.
