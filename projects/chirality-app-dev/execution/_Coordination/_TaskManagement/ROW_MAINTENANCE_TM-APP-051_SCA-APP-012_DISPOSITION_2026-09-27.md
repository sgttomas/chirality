# TM-APP-051 row maintenance — SCA-APP-012 disposition note

Date: `2026-09-27`

Mode: `row maintenance`

Status: `OWNER-DIRECTED APPLICATION — APP REGISTER ONLY`

This record applies the owner's choice of option 1 in
`execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/TM_APP_051_PROPOSAL.md`.
It records Task Management attention state only. It has no effect on any of
the following: a deliverable, lifecycle, scope, priority, Trigger, other
register row, Runtime or release.

## Mandatory federation preflight

Before the row was maintained, the deterministic helper
`tools/taskmgmt/taskmgmt.py federation --register projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv`
returned:
- **Coverage:** `COMPLETE` over four canonical tracked registers (Root, App,
  Piping, PEC) with `register_writes: 0`.
- **Findings:** 55 typed-field findings, of which 30 were presented for this
  non-Root invocation:
  - `FOREIGN_LINK_TO_LOCAL=1`;
  - `LOCAL_LINK_TO_FOREIGN=26`;
  - `REMOTE_CLOSED_LOCAL_OPEN=1`;
  - `LOCAL_CLOSED_REMOTE_OPEN=22`;
  - `MISSING_NOTICE=5`.
- **TM-APP-051:** none of the findings names the row.

The same helper, rerun after the write, returned the same coverage and counts,
again with no finding on TM-APP-051. The generated
`.candidates/federation.json` projection is gitignored, rebuildable and
derivative evidence only. `COMPLETE` is a coverage verdict, not a
semantic-closure or global-absence claim. `taskmgmt validate` passes the
21-row App `REGISTER.csv` before and after the write.

## Owner act and accepted upstream evidence

The owner's words, typed in chat on 2026-09-27 (verbatim):

> I Confirm the SCA-APP-012 incremental plan under FULL_GRAPH; DEP-02-03-008: retire; TM-APP-051: option 1.

The clause "TM-APP-051: option 1" is the authority for this record.

| Artifact | SHA-256 | Use |
|---|---|---|
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/CHAT_TRANSCRIPTION.md` | `8100d2e111fbb9e3fd0d46802373222d52689c4be98564b66da4e1422ed190e4` | Verbatim transcription of the owner act (evidence, not ruling). |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/TM_APP_051_PROPOSAL.md` | `d6790d6b106af16c11e54e4b5e7b89285deb649ef8ea422bddf84e5a93b02534` | The option the owner chose, with the exact row delta. |
| `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/Propagation_Plan.md` | `d5a14d2bfbecf2cc2cc9d96223b780e21893d0751065b2f9979f378d789fea18` | §8 item 5: the proposed disposition note for the row's owner. |
| `projects/chirality-app-dev/execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-3_2026-09-27/DECISION.md` | `612e4cbe6d7e160f7e7d030b822f37d5d2c8272e6abf6d0f4c6d201af110c267` | SCA-APP-012 checkpoint group 3 acceptance. |
| DEL-02-03 `ScopeOfWork.md` | `ac34b8dccb03f02db626fde1bdfeaa4af80933a9cb203c6f7d0b26afdf54cc91` | Lines 22-24 (SCA-APP-012 controlling section): scope scan is `/api/project/deliverables`; DEL-02-03-REQ-009 retired; DEL-02-03-REQ-010 restated. |

## Exact row delta

Only `TM-APP-051` changed in `REGISTER.csv`:

- `Status`: retained `DEFERRED`;
- `ScaRef`: `NONE` → `SCA-APP-012`;
- `LastReviewed`: `2026-09-23` → `2026-09-27`;
- `Notes`: appended, after the register's ` | ` separator, the §8 item 5 note
  as `TM_APP_051_PROPOSAL.md` words it, and a pointer to the owner act and
  this record:
  "SCA-APP-012 (accepted 2026-09-27, checkpoint group 3; landed in PR #1020,
  `bc1ea504d`) disposes three of the four consumers: route retired with
  DEL-02-03-REQ-009 (R-b); scope scan is `/api/project/deliverables`,
  `/api/working-root/scope` retired; status restated read-only by
  DEL-02-03-REQ-010 from `/api/project/deliverables`. The summary widget is
  still unimplemented and stays with DEL-02-03; the row stays open for it
  only.";
- every other field unchanged, including `Concern`, `Trigger`, `SourceRef`,
  `SourceSha`, `CandidateRef`, `AssociatedWith`, `EvidenceRef`, `EvidenceSha`
  and `EvidenceQuote`.

Prior App `REGISTER.csv` SHA-256:
`5ca17f4a25e72b90f8650779297d883a777623d895de6c6d2761891f499addad`.
Resulting App `REGISTER.csv` SHA-256:
`a57b80c887b41951b8dfad6828e72669474133916c4336996b6c689909ece31a`.

## Disposition recorded

| Consumer | After SCA-APP-012 |
|---|---|
| Route | Retired with DEL-02-03-REQ-009 (R-b) |
| Scope scan | `/api/project/deliverables`; `/api/working-root/scope` retired |
| Status | Restated read-only by DEL-02-03-REQ-010 from `/api/project/deliverables` |
| Summary widget | Still unimplemented; stays with DEL-02-03 |

The row stays `DEFERRED`, open only for the summary/status widget. SCA-APP-012
does not close it, and this record does not fire its Trigger.

## Not changed

- **Concern and Trigger.** Variant 1b of the proposal (narrowing them to the
  summary/status widget) was not chosen; they stay byte-for-byte.
- **Evidence fields.** `EvidenceSha` (`4aba6a5c…33e1`) no longer matches the
  current DEL-02-03 `ScopeOfWork.md` (`ac34b8dc…cc91`, after SCA-APP-011 and
  SCA-APP-012). As the TM-APP-032 precedent did, this maintenance leaves the
  evidence fields as they are; refreshing them is a separate row-maintenance
  choice for the owner.

## Precedent and fit

This follows `ROW_MAINTENANCE_TM-APP-032_RESCOPE_2026-08-21.md`, which
maintained a live `REGISTER.csv` row: preflight, owner act and evidence hashes,
exact row delta, then disposition. No Task Management index or registry lists
row-maintenance records, so no index update is required.

## Derivative and handoff state

This record is a derivative Task Management record. Its accepted upstream
evidence is the owner transcription and the SCA-APP-012 records named above;
it does not replace any of them. The authoritative App register remains
`REGISTER.csv`. The SCA-APP-012 `Handoff_State.md` names this note as the
row owner's pending item; the post-setup `audit-scope-closure` checks it.
