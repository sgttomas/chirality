# D-APP-86 — App UI/API Parity Evidence Instrument

**Status:** `PROPOSAL — AWAITING_RULING — NO OPTION SELECTED`

**Prepared:** 2026-08-02 by `HELPS_HUMANS`, managed by App `HELP_HUMAN`

**Task Management link:** `TM-APP-002`

## 1. Decision requested

Select whether and how the App loop should activate the bounded parity
instrument already presented as Option 1 in the App Next-Work Slate. The
instrument covers exactly three live evidence residuals:

1. DEL-02-02 packaged Desktop smoke for the re-hosted Workbench and Pipeline;
2. DEL-08-02 packaged Desktop smoke for guarded navigator selection; and
3. DEL-05-04 transcript-item rendering against a real daemon-owned session.

Packet preparation is not selection. No proof work is dispatched until the
owner rules.

## 2. Accepted basis and current facts

| Evidence | SHA-256 | Current fact used |
|---|---|---|
| `execution/_Coordination/NOTICE_2026-08-02_TM-APP-002_PARITY_NEXT_PLANNING.md` | `f397bcffb0f99ba8b478e3a2c7ce2a7551e0d2b7b4c2e4aca0e771a3eba8df62` | Routes packet preparation only; selection remains the owner's. |
| `execution/_Coordination/_TaskManagement/DRAFT_HANDOFF_TM-APP-002_PARITY_INSTRUMENT_2026-08-02.md` | `2d18198ac097fe54d0f8092e79c7f520da4646fdf012366a52f1695f1392c8c7` | Seals the three evidence surfaces above. |
| `execution/_Coordination/APP_NEXT_WORK_SLATE_2026-07-29.md` | `e2316732063fc631b54e7fff0a22dc34476514499c287f9fa10bfa21b8490128` | Option 1 names the three-surface instrument; the slate selects nothing. |
| DEL-02-02 `_STATUS.md` | current tree | Re-hosted Workbench/Pipeline are implemented; packaged smoke remains. |
| DEL-08-02 `_STATUS.md` | current tree | Guarded navigator selection is implemented and has live component proof; packaged smoke remains. |
| DEL-05-04 `_STATUS.md` | current tree | The replay lens exists, but its transcript list has not rendered items from a real daemon session. |

The packaged daemon is now capable of producing a real daemon-owned session,
so daemon unavailability is not a present blocker. This packet does not reuse
the deleted temporary drill session as evidence.

## 3. Options

### Option A — Integrated three-surface activation (recommended)

Authorize one bounded evidence tranche that builds one unsigned local package,
starts an isolated packaged daemon/app posture, and records all three surfaces
against the same source revision and evidence manifest.

Required observations:

- Workbench opens, preserves its governed content/interaction boundary, and
  returns without route or state corruption;
- Pipeline opens, preserves its governed dispatch boundary, and returns
  without route or state corruption;
- guarded navigator selection changes the selected recorded session without
  mutating a turn in flight or crossing the read-only replay boundary; and
- a real daemon-owned session containing transcript events renders at least
  one transcript item with session/event provenance and preserved
  manager/child attribution where such attribution exists in the fixture run.

This is the strongest parity evidence because UI and API-facing observations
share one packaged build, daemon identity, session corpus, and manifest.

### Option B — Two-phase activation, all three surfaces retained

Authorize the same evidence contract in two serial phases:

1. packaged Workbench/Pipeline and guarded-navigator smoke; then
2. real-daemon transcript-item rendering.

Phase 2 must use the same committed source revision as Phase 1 or explicitly
restart the whole instrument. Phase 1 alone does not close `TM-APP-002` and
does not establish UI/API parity. This alternative reduces drill complexity
but creates a handoff boundary and a greater risk of basis drift.

### Option C — Defer

Keep `TM-APP-002` deferred and select no proof work. State the later trigger
(for example, the next packaged UI reliance tranche). Existing unit,
component, and daemon-service evidence remains valid only for the narrower
claims it already supports.

### Option D — Decline the combined instrument

Decline this three-surface instrument. The three deliverable-local evidence
residuals remain open unless separately dispositioned through their owning
instruments. Decline does not convert existing partial evidence into parity
evidence.

## 4. Exact output contract if A or B is selected

The executing manager must freeze a run ID and write a derivative evidence
package under:

`execution/_Coordination/AgentRuns/APPDEV_PARITY_INSTRUMENT_<RUN_DATE>/`

Minimum contents:

| Output | Required content |
|---|---|
| `RUN_MANIFEST.md` | exact commit/tree, clean/dirty state, runtime versions, package identity, isolated user-data/runtime roots, commands, actor/parentage, and selected option |
| `EVIDENCE_INDEX.csv` | one row per required observation with deliverable, surface, artifact path, artifact SHA-256, result, and limitation |
| `PACKAGED_UI_SMOKE.md` | Workbench, Pipeline, and guarded-navigator steps/results plus screenshots or equivalent captured state |
| `REAL_DAEMON_REPLAY.md` | session ID, daemon/session evidence, event count, rendered transcript-item count, attribution observations, and cleanup disposition without secrets |
| `VALIDATION.md` | exact commands, exits, generated-summary paths/hashes, skips, and reasons |
| `HANDOFF.md` | closure verdict per surface, rerun triggers, unresolved blockers, derivative status, and next lawful owner |

On successful fan-in, each affected deliverable receives one `_run_records/`
pointer to the accepted evidence. `_STATUS.md` Remaining text changes only to
the extent proven by accepted evidence; lifecycle state and Checking Approval
SHA do not change.

## 5. Validation contract

Run from `projects/chirality-app-dev/frontend/` unless a command says
otherwise:

1. applicable focused Vitest component/runtime tests for the three surfaces;
2. `npm run typecheck`;
3. `npm run build`;
4. `npm run desktop:pack`;
5. `npm run harness:validate:premerge` against the isolated reachable app;
6. `npm run validate:release-quality`, with no provider-backed check silently
   skipped; and
7. repo-wide practitioner harness/self-check and App receipt/corpus checks at
   closeout as required by the standing loop plan.

The executor must stop any unrelated local dev server before build, pack, or
premerge commands. Captured evidence must not contain tokens, credentials, or
private session content.

## 6. Dependencies, risks, and non-effects

- A/B depend on an unsigned local packaged app and an isolated real daemon
  session; they do not depend on Root's unresolved generic runtime contract.
- This instrument tests the current accepted surfaces. It does not add Agent-2
  Bash, Pi capability, provider/network scope, or a new runtime contract.
- A passing instrument is software evidence only. It is not release,
  distribution, issuance, lifecycle advancement, professional reliance, or a
  blanket parity claim beyond the enumerated observations.
- F-APP-2 remains in force: no signing, notarization, publication, or external
  distribution.
- The six D-APP-81 `HISTORICAL_RELATION_UNKNOWN` relations are untouched.

## 7. Non-binding recommendation

Select **Option A**. The three residuals are already implemented and their
runtime prerequisite exists; one integrated build/session basis gives the
cleanest evidence and avoids a phase-boundary drift problem. Option B is the
bounded fallback if the owner prefers operational separation.

## 8. Owner return tokens

- `APPROVE D-APP-86 OPTION A`
- `APPROVE D-APP-86 OPTION B`
- `APPROVE D-APP-86 OPTION C — TRIGGER: <trigger>`
- `APPROVE D-APP-86 OPTION D`
- or amend the evidence contract explicitly.
