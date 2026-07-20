# Evaluation Report — CQ-F1 R1-REPAIR V1-RECHECK

## Verdict

`BLOCK`.

R1-REPAIR sustains the repairs for V1-001 through V1-004, exact source and
package bindings, all 22 `OWNER_CLASS` classifications, and the nine-group
population. The v8 wrong-path-label correction is genuinely a
nonconsequential control-label erratum.

The repaired derivative is nevertheless not decision-ready. Fresh-child
fan-in materially alters the attachment-security boundary for
`file-picker.tsx`, and it drops physical-ownership alternatives for
`globals.css`, `harness-events-provider.tsx`, and `harness-event-views.ts`.
These losses affect owner-slate groups 1, 2, and 3. No mapping or slate is
accepted. W1 remains blocked.

## Basis, method, and validated bindings

- Basis: `57652ba1cd0905e8f47131e4c4ebf518272f7c16`.
- Subject: repaired activated derivative `ACTIVATED_57652BA1/`.
- Manifest: 22 rows, 22 unique paths, 22 existing paths, exact order; ordered
  newline-terminated path-list SHA-256
  `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`.
- Source: 22/22 Git blobs and SHA-256 values independently recompute at the
  basis and match current bytes. The subject diff is empty for all 22 paths.
- Package: all 13 declared file hashes match the R1-REPAIR return. Both CSVs
  parse with their 13- and 7-column schemas and contain the exact 22 rows in
  manifest order. JSON evidence parses.
- Fresh child: exact 14/14 DEL-02-01 rows in filtered manifest order; all
  required fields, blobs, SHA-256 values, classifications, and read-only
  containment claims reproduce.
- Remaining populations remain DEL-02-01 14, DEL-03-03 1, DEL-06-02 1,
  DEL-09-04 4, and DEL-10-04 2. Their statuses remain `IN_PROGRESS` and
  unchanged from basis.
- Method: two fresh bounded read-only audits plus manager fan-in over source,
  caller/import, tests, scopes, authority, classification, package schemas,
  hashes, alternatives, EOF hygiene, predecessor preservation, and
  containment. No runtime test or service was run.

Fresh audit returns:

- technical recheck:
  `0ecdef2e1859c623616d3220a022e6606d99471e056ee8f10705a0b39d1eea94`;
- governance/package recheck:
  `5b5ae9218be706964847f94183a13d10070c0d5ff7fe9358a4faabe35f47cdbe`.

## Prior V1 findings

### V1-001 — `REPAIRED_SUSTAINED`

The exact stylesheet at `frontend/src/app/globals.css` retains explicit
Pipeline/Workbench, API-key, shell, session/projection, persona, child/tool,
mode/permission, attachment, and renderer boundaries. DEL-02-01 is proposed
only as integration lead. The stale `DEL-02-06` source heading remains
evidence, not authority.

### V1-002 — `REPAIRED_SUSTAINED`

The complete production consumer graph for ChatMarkdown is exactly ChatPanel
and DocumentView. The repaired package removes the unsupported DEL-05-04
consumer and retains DEL-02-03 as the material consumer edge.

### V1-003 — `REPAIRED_SUSTAINED`

`ansi.ts` has exactly one direct importer, ChatMarkdown, and no replay or
transcript caller. The repaired package proposes DEL-02-01 with DEL-02-03
consumption, retains a shared-utility alternative, and rejects DEL-05-04.

### V1-004 — `REPAIRED_SUSTAINED`

All 13 package files end in exactly one LF and contain no horizontal trailing
whitespace. The exact ten files named by original V1 were normalized without
reopening the immutable original finding record.

### V1-005 — `OBSERVATION_PRESERVED_NONBLOCKING`

The `pec-scratch-server.mjs` comment still names only two callers while a
third live-LLM-demo caller exists. The derivative itself names all three and
does not repeat the stale count. Source repair remains outside this run.

## Blocking findings

### V1R-001 — FilePicker boundary altered during fan-in

- **Severity:** material / owner-slate blocking
- **Affected row:** 6, `frontend/src/components/shell/file-picker.tsx`
- **Affected group:** 2, Working-root document UX

The immutable fresh child proposes DEL-02-03 for Working Root browsing,
retains DEL-02-04 for attachment UI state, and retains DEL-09-06/server routes
for enforceable attachment security. Source and scope evidence support this:
FilePicker is a read-only browser that applies client navigation and extension
filters and emits non-authoritative attachment metadata, while DEL-09-06 owns
server-side attachment path, type, symlink, readability, size, failure, and
retry validation.

The integrated ledger, proposed mapping, and group 2 instead preserve
DEL-02-04 and substitute DEL-06-04 path enforcement for DEL-09-06. DEL-06-04
principally governs write/edit mutation gates. The package records no
reasoned disagreement for the substitution and `QA.md` reports fan-in as
passing. This is a material boundary alteration, not harmless compression.

### V1R-002 — material physical-owner alternatives omitted

- **Severity:** material / owner-slate blocking
- **Affected rows:** 1, 10, and 14
- **Affected groups:** 1 and 3

Three fresh-child alternative sets were narrowed during integration:

1. `globals.css`: ownerless/shared physical-file treatment and a
   capability-level split were dropped. Styled semantic owners are not
   substitutes for these physical ownership choices.
2. `harness-events-provider.tsx`: an explicit shared-application-
   infrastructure owner was dropped despite root mounting and consumers
   spanning shell, navigation, replay, transcript, tool, subagent, and
   permission surfaces.
3. `harness-event-views.ts`: split-file and ownerless/shared projection-
   utility treatments were dropped and replaced by semantic capability
   owners, which answer a different question.

The nearest proposed candidates remain technically supportable, but the
owner choices are incomplete. Five other fresh-child omissions are weak or
generic alternatives and are harmless compression; five rows are faithful.
The complete 14-row fidelity result is therefore 5 faithful, 5 harmlessly
compressed, 3 materially lossy, and 1 boundary-altered.

## Exact row disposition

All 22 classifications remain `OWNER_CLASS`. The following four rows block
because of fan-in fidelity; the other 18 rows substantively pass on the frozen
basis. No row mapping is accepted.

| # | Path | Disposition |
|---:|---|---|
| 1 | `frontend/src/app/globals.css` | `BLOCK_FANIN_ALTERNATIVES` — V1-001 repaired; V1R-002 remains |
| 2 | `frontend/src/app/page.tsx` | substantive pass |
| 3 | `frontend/src/app/api/working-root/deliverable/content/route.ts` | substantive pass; physical owner remains an explicit choice |
| 4 | `frontend/src/components/shell/chat-markdown.tsx` | substantive pass; V1-002 repaired |
| 5 | `frontend/src/components/shell/document-view.tsx` | substantive pass |
| 6 | `frontend/src/components/shell/file-picker.tsx` | `BLOCK_ALTERED_BOUNDARY` — V1R-001 |
| 7 | `frontend/src/components/shell/session-list-view.tsx` | substantive pass |
| 8 | `frontend/src/components/shell/subagent-stream-view.tsx` | substantive pass |
| 9 | `frontend/src/components/shell/tool-stream-view.tsx` | substantive pass |
| 10 | `frontend/src/components/workspace/harness-events-provider.tsx` | `BLOCK_FANIN_ALTERNATIVES` — V1R-002 |
| 11 | `frontend/src/lib/shell/ansi.ts` | substantive pass; V1-003 repaired |
| 12 | `frontend/src/lib/shell/document-view-state.ts` | substantive pass |
| 13 | `frontend/src/lib/shell/harness-event-buffer.ts` | substantive pass |
| 14 | `frontend/src/lib/shell/harness-event-views.ts` | `BLOCK_FANIN_ALTERNATIVES` — V1R-002 |
| 15 | `frontend/src/lib/workspace/navigation-intent.ts` | substantive pass |
| 16 | `frontend/src/types/chirality-window.d.ts` | substantive pass |
| 17 | `frontend/electron/preload.ts` | substantive pass; integration owner remains an explicit choice |
| 18 | `frontend/src/lib/harness/scripted-agent-sdk-proof.ts` | substantive pass; not packaged proof |
| 19 | `frontend/scripts/assert-harness-contract-deps.mjs` | substantive pass |
| 20 | `frontend/scripts/generate-tool-catalog.mjs` | substantive pass; mechanism only |
| 21 | `frontend/scripts/pec-scratch-server.mjs` | substantive pass; V1-005 remains nonblocking |
| 22 | `frontend/scripts/run-pec-bridge-rehearsal.ts` | substantive pass; F-APP-3 retained |

## Nine-group disposition

The group populations reproduce exactly as `5+4+6+1+1+1+1+1+2=22`, with
no omission or duplicate. Groups 1, 2, and 3 block on the findings above;
the other six substantively pass but are not accepted or routed.

| Group | Paths | Disposition |
|---|---:|---|
| 1. Shell integration and shared presentation | 5 | `BLOCK` — globals physical-owner alternatives omitted |
| 2. Working-root document UX | 4 | `BLOCK` — FilePicker DEL-09-06 boundary altered |
| 3. Replay and projection | 6 | `BLOCK` — provider/view physical-owner alternatives omitted |
| 4. Working-root content route | 1 | substantive pass |
| 5. Catalog generation | 1 | substantive pass |
| 6. Electron preload | 1 | substantive pass |
| 7. Network-policy fixture | 1 | substantive pass |
| 8. Contract dependency lint | 1 | substantive pass |
| 9. PEC evidence | 2 | substantive pass with F-APP-3 retained |

## V8 wrong-label erratum audit

Disposition:
`NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED`.

The wrong v7 labels were:

- `frontend/src/styles/globals.css`; and
- `frontend/src/lib/ansi.ts`.

The corrected exact paths are:

- `projects/chirality-app-dev/frontend/src/app/globals.css`; and
- `projects/chirality-app-dev/frontend/src/lib/shell/ansi.ts`.

Neither wrong path exists. They occur only in preserved control/error records.
The frozen manifest, fresh child brief and return, ledger, mapping, source
bindings, package prose, slate, QA, and terminal records all use the corrected
paths and exact source objects. The erratum changed no inspected or written
path, objective, authority, risk, write ownership, source binding,
classification, acceptance criterion, or downstream gate. It therefore did
not conceal a consequential amendment.

## Preservation and containment

- All sealed original V1 return, status, protocol, report, findings, handoff,
  and child-return hashes remain exact.
- Original R1/R1-RETRY evidence and all five predecessor child-return hashes
  remain exact. Earlier children remain visibly predecessor evidence and are
  not represented as the fresh R1-REPAIR child.
- Evaluation wrote only its additive evaluation root and the V1-RECHECK
  instance root. It changed no subject, source, package, authority, lifecycle,
  status, decision, plan, graph, Git index, ref, branch, or PR state.
- Waivers: none.

## Required repair and rerun

RECONCILIATION requires a versioned parent amendment and a new controlled
attempt. It must:

1. restore the FilePicker DEL-02-04 UI-state and DEL-09-06/server
   attachment-security boundaries, and retain DEL-06-04 only if separately
   justified rather than substituted;
2. carry or explicitly reject with evidence the shared/ownerless/split
   physical-owner alternatives for `globals.css`,
   `harness-events-provider.tsx`, and `harness-event-views.ts`;
3. propagate the results through both CSVs, affected analysis/package notes,
   groups 1–3, QA, handoff, run basis, terminal accounting, and hashes;
4. revalidate every fresh-child row against the integrated package, exact
   22-row/nine-group coverage, schemas, source/child bindings, and EOF hygiene;
   and
5. refresh the V1 binding and trigger a fresh independent V1 recheck.

No source-code repair is authorized by this verdict. The existing fresh child
may be reused only if all of its sealed inputs and exact bindings remain
unchanged.
