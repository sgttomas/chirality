# D-PEC-15 - PROPOSAL: post-disposition weekly re-import behavior (convention or source change)

**Status:** PROPOSAL / RULED — indefinitely postponed (owner, 2026-07-07; verbatim in Human ruling).
**Date prepared:** 2026-07-06
**Decision ID:** D-PEC-15
**Prepared by:** PEC work loop agent under the standing PEC loop. The ruling act is the owner's (K-AUTH-1; D-GOV-04). No live pre-ruling covers this row: the owner's 2026-07-06 session authorization (`_DomainEngines/pec/LOOP_RECEIPTS.md` Receipt 32 item 4) named "previously opened NOT_PREPARED rows such as D-PEC-13/14/15" as pre-rulable, but it expired by its own terms ("this session only; expires at session end or 24 hours after this direction, whichever comes first") and this packet is prepared in a later session — so it stops at the gate for the owner's read.

Structure precedent: D-PEC-17 for the O-C form (a source-tranche authorization
packet whose ruling opens an in-packet enumerated fence, with rollback plan
and STOP clause); D-PEC-09 for the narrow-repair shape and its
owner-escalation history (stated honestly in O-C); the D-PEC-10
verified-facts / obligations packet form; residual-row convention per
`_REGISTER.md`.

## Why (the observation, and why it is acute now)

The D-PEC-10 rehearsal recorded as fact (MANIFEST step 6, observation dry-run
IPR-0006, withdrawn after capture): a full RAIL re-import after triage would
re-land every RAIL row whose intake item had been dispositioned as a NEW intake
item, while un-dispositioned rows update in place. Numbers from the artifact
(`_DomainEngines/pec/PEC_2026-07-05_DPEC10-rehearsal-01/artifacts/20-observation-rail-reimport-dryrun.json`):
`updated: 3` (the anchored work item + the 2 un-dispositioned intake items),
`intakeCreated: 4` (the 4 dispositioned rows re-land), `conflicts: 0`. The
register row opened from that observation is this row.

**Urgency basis.** The 272-item mass triage run (D-PEC-10 mechanism) was
initiated this session under the lawfulness clarification recorded in
`_DomainEngines/pec/LOOP_RECEIPTS.md` Receipt 32's gate outcome ("the 272-item
run on pilot-scratch is owner-clarified lawful (scratch/demo mutation basis)");
its evidence dir is to land as `PEC_2026-07-06_DPEC10-triage-01/` (concurrent,
this session — no results asserted here). The lane is carried in Receipt 32's
parked lanes ("272-item triage run on pilot-scratch (lawful, behind bridge
priority); D-PEC-13/14/15 preparation (item-4-eligible, behind bridge
priority)") and again in Receipt 35's ("272-item run on pilot-scratch (lawful,
owner-clarified); D-PEC-13/14/15 preparation (item-4-eligible)"). Once that
run completes, every RAIL row it dispositions — bounded by the full 272; the
actual scale depends on the run's disposition rate — would re-land as a new
intake item on the next full weekly re-import. The owner's weekly workflow
(D-PEC-10 intent of record: weekly updates, agent as primary update means)
hits this boundary on its first post-triage week.

**Interim rule this packet supersedes or ratifies.**
`../IMPORT_TEMPLATES/FILE_DROP_RUNBOOK.md` v1.2 step 5: "until D-PEC-15 rules
a convention, drop dispositioned `item_id`s from the weekly export or expect
and triage the re-landed rows." That step is the un-ruled union of options O-A
and O-B below.

## The mechanism (verified facts — why dispositioned rows re-land)

All citations are to the live tree (`main` at `c0a3214cf`, read-only).

| # | Fact | Source |
|---|---|---|
| M-1 | A RAIL row first takes the update path only if its `item_id` matches an existing work-item/hold/interface **ref**: `SELECT id, version FROM ${table} WHERE project_id = ? AND ref = ?` bound to `row.item_id`. | `projects/pec/server/src/import/index.ts:194-197` |
| M-2 | Failing M-1 and any `deliverable_ref` anchor, the row is matched against **un-dispositioned** intake items only, by its verbatim `[item_id] ` statement prefix: `... FROM intake_item WHERE project_id = ? AND state != 'dispositioned' AND substr(statement_verbatim, 1, ?) = ?`. A match updates in place (WF-6 idempotency, evidenced 2026-07-05). | `projects/pec/server/src/import/index.ts:220-243` |
| M-3 | Failing M-2, the row falls through and **creates a new intake item** (`report.intakeCreated++`). | `projects/pec/server/src/import/index.ts:244-257` |
| M-4 | Triage disposition sets the intake item's `state` to `'dispositioned'` — which removes it from the M-2 lookup by construction. The record itself still carries the `[item_id] ` prefix; the matcher just no longer looks at it. | `projects/pec/server/src/services/intake.ts:138-141` |
| M-5 | A `converted` disposition creates its records with **fresh PEC refs** (`sx.repo.nextRef(...)` — e.g. `WI-0001`), never the source `item_id`, so the converted record cannot satisfy M-1 either. The linkage survives as `intake_link` back-links on every conversion target, plus `sourceType`/`sourceId` on converted **work items only** (`intake.ts:110`); other conversion targets carry only the `intake_link`. | `projects/pec/server/src/services/work.ts:70`; `projects/pec/server/src/services/intake.ts:110-135` |
| M-6 | The app's own RAIL export already excludes dispositioned intake items (`if (t.state === 'dispositioned') continue`) — an export/re-import round trip of the app's register would not re-land them. The owner's weekly RAIL is the team's external source document, not an app export, so it keeps carrying the rows. | `projects/pec/server/src/import/index.ts:554-560` |
| M-7 | Dry-run and apply run the same `importContract` code path (dry-run in a rolled-back savepoint), so any matcher change has dry-run/apply report parity by construction; proposal lifecycle, hash-bound acceptance, and the staleness watermark live in the proposals layer and are untouched by matcher behavior. | `projects/pec/server/src/services/proposals.ts:75-84,141-161,178-200` |

**The cause in one sentence:** disposition severs both keys a re-imported RAIL
row can match on — the intake prefix lookup is state-filtered to exclude
dispositioned items (M-2, M-4), and conversion mints new refs rather than
adopting the source `item_id` (M-5) — so the row falls through to
create-new-intake (M-3), every full re-import, forever.

Two secondary consequences worth the owner's eye: (a) re-landed duplicates are
themselves un-dispositioned, so the *next* re-import updates them in place —
each dispositioned row yields one live shadow duplicate rather than compounding
weekly, **unless** the shadow is itself triaged, which re-severs the key and
re-lands it again the following week; (b) after conversion, external edits to
that source row no longer reach the converted record through any import path —
the update channel is severed independently of the duplication symptom.

## Decision to rule

What the weekly cycle does with RAIL rows whose intake items are already
dispositioned: an owner-side export convention (O-A), an agent-side triage
convention (O-B), a narrow source change to the intake matcher under a fenced
tranche (O-C), or defer (O-D).

## Scope boundary

This packet authorizes no source change, no test change, no import behavior
change, and no mutation of PEC data **unless the owner rules O-C**, in which
case the ruling itself is the source-tranche authorization for exactly the
fence named in O-C below (single-gate structure — see O-C). Options O-A/O-B
are coordination-surface conventions only (runbook edit; lawful under the
F-PEC-1 `execution/_Coordination/**` carve-out).

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Owner-side export convention: dispositioned `item_id`s are dropped from the weekly RAIL file before drop. | No code change; weekly manual pruning burden on the owner; fragile (see below). |
| O-B | Agent-side triage convention: expect the re-landed rows and triage them as `duplicate` each week (or hold them as standing shadows). | No code change; unbounded weekly re-triage burden after the 272-item run; queue and history noise. |
| O-C | Narrow source change under this ruling's named tranche: the RAIL matcher recognizes dispositioned intake items by their `[item_id] ` prefix and reports the row as already-dispositioned instead of creating a new intake item. | One fenced tranche opens `server` source scope; the weekly cycle becomes clean by construction. |
| O-D | Defer. | Runbook v1.2 step 5 interim rule stands; the first post-triage weekly re-import inherits the problem at up-to-272-row scale. |

### O-A — drop dispositioned `item_id`s from the weekly export (owner-side, procedural)

**Exactly how.** Before each weekly drop, the set of dispositioned `item_id`s
is obtained from the app — either the intake export (`GET` register export
`intake`, which carries `state` and `disposition`; `import/index.ts:604-611`),
filtering `state = dispositioned` and reading the `[item_id]` prefix from the
statement column, or equivalently by diffing against the app's RAIL export,
which already omits them (M-6). The owner (or the agent, presenting the filter
list at propose time for the owner to apply to the source file) removes those
rows from the weekly RAIL CSV before it is dropped. The agent additionally
cross-checks at propose time: a dry-run `intakeCreated` count above the
expected new-row count flags un-pruned residue before any accept.

**Fragility (stated honestly).**
- The prune list grows monotonically (every triaged week adds to it) and must
  be re-derived and re-applied every single week against the team's live
  source document; after the 272-item run the list starts at the scale of
  that run's actual dispositions (bounded by 272).
- A missed row re-lands silently as a duplicate (the failure mode is the
  status quo, per row).
- A wrongly pruned row is worse: the team's later updates to it never enter
  the app at all, with no report line anywhere — a silent drop performed
  upstream of the §16 never-silently-drop posture, where the contract cannot
  see it.
- It edits the team's working document to fit the tool. The RAIL source file
  is the team's record; deleting rows from the copy that gets dropped means
  the dropped file and the team file permanently diverge, or the team file
  itself gets distorted.

### O-B — expect-and-triage the re-landed rows (agent-side, procedural)

**Exactly how.** The weekly cycle proceeds unmodified; after each full RAIL
re-import, the agent's triage pass (D-PEC-10 mechanism) treats every re-landed
row — recognizable by its `[item_id] ` prefix matching a dispositioned intake
item — as `duplicate`, with the prior item named in the disposition note
(the rehearsal's INTK-0003 pattern).

**Cost, quantified with the 272 context.** Because triaging the shadow
re-severs the key (M-4), the same rows re-land again the following week: this
is a perpetual weekly obligation, not a one-time cleanup. At the post-run
scale that is on the order of up to ~272 re-landed items per week (bounded by
272; the actual scale depends on the run's disposition rate) — each needing
`open_triage` + `disposition` (two RBAC'd acts, two history entries, one
raiser notification each; `intake.ts:55-67,138-154`) — roughly 500+ API acts
and 500+ history/notification rows of pure noise weekly, growing with every
newly triaged item, indefinitely. The intake queue and the unanchored section
of the RAIL export (M-6 inverse: un-dispositioned shadows DO export) are
polluted between import and triage every week.

**Variant B2 (disclosed, not recommended):** leave the shadows permanently
un-dispositioned. They then update in place on subsequent re-imports (M-2) and
become a de-facto mirror of the external RAIL — no weekly re-triage, but the
intake queue permanently carries a shadow copy of every previously triaged row,
defeating the queue's meaning (queue = awaiting triage) and burying real new
items among hundreds of shadows.

### O-C — narrow source change: matcher recognizes dispositioned intake items (D-PEC-09-narrow repair, D-PEC-17-form tranche)

**Authorization structure — stated plainly:** ruling O-C **authorizes the
source change** under the named tranche below in the same act (single gate).
The structure precedent for the single gate is **D-PEC-17**: a source-tranche
authorization packet whose ruling opens an in-packet enumerated fence, with
rollback plan and STOP clause. **D-PEC-09 is precedent for the repair's
narrowness, not for the single gate** — it was opened design-only ("it
authorizes no source change") and it was the OWNER who collapsed the two
steps in the ruling act ("I authorize the source change for D-PEC-09." —
Receipt 23, verbatim). A packet may not pre-collapse the steps on its own
authority; this packet therefore presents the single-gate form as O-C's
defined structure *for the owner to rule*, and the two-step alternative
stands equally rulable: ruling "O-C design-only" keeps this packet as design
and opens a successor source-tranche row per the residual-row convention.

**Ruled design.** In `importRail`, when a row fails the ref lookup (M-1), a
dispositioned-prefix lookup (the M-2 query with its state filter inverted:
`state = 'dispositioned'`) runs **hoisted ahead of the anchor branch**, so it
covers every create path — the no-anchor intake branch (M-3) and the anchored
create paths (`index.ts:261-311`) alike. It fires only when no live
(un-dispositioned) prefix match exists (point 3):

1. On match: **no record is created or mutated.** The row is reported under a
   new additive `ImportReport` category (e.g.
   `alreadyDispositioned: Array<{ row, key, intakeRef, disposition }>`),
   naming the matched intake item, its disposition, and — **always** — its
   converted target records resolved via `intake_link` (e.g.
   `converted -> WI-0001`); no discretionary omission. §16
   never-silently-drop is honored by the report line, not by creating a
   duplicate.
2. If the incoming statement differs from the stored verbatim, the report line
   says so as information. Nothing is applied and nothing is rewritten, so no
   OM-3 conflict is raised and the verbatim trigger-freeze is untouched.
3. Precedence unchanged: a live (un-dispositioned) prefix match still wins and
   takes today's update path — the WF-6 update-in-place semantics evidenced
   2026-07-05 are preserved bit-for-bit. (To be precise: only the
   **dispositioned** lookup is hoisted ahead of the anchor branch; the live
   M-2 update path stays where it is today, inside the no-anchor branch — in
   the anchored branch a live prefix match does not divert the row, and the
   pre-existing anchored-create behavior there is unchanged and out of scope.)
   The dispositioned lookup fires only when no live match exists
   (interim-created shadows therefore keep receiving updates). Multiple
   dispositioned matches: newest named.
4. `force` has **no effect** on this path — force overwrites in-app edits on
   live records; it must never resurrect or mutate a dispositioned item.
5. Dry-run/apply parity is by construction (M-7). The proposal history
   summary lines (`proposals.ts:124-126,190`) gain the new count so it is
   never silently omitted from what the owner reads at accept time.

**Disclosed edge case (folded into the ruled design via the hoist):** a
previously dispositioned RAIL row whose `deliverable_ref` newly RESOLVES in a
later week would — with a lookup placed only in the no-anchor branch — take
the anchored-create path (`index.ts:261-311`) and create a one-time duplicate
anchored record with `ref = item_id` (thereafter caught by M-1). The hoisted
placement above covers that branch too: the row reports `alreadyDispositioned`
there as well, and anchoring a previously-triaged row becomes, like every
other post-disposition change, a report-visible human/agent screen act — never
an import-side duplicate create.

**Tranche fence (this ruling opens exactly these files, nothing else):**

| File | Permitted change |
|---|---|
| `projects/pec/server/src/import/index.ts` | The RAIL import section (hoisted dispositioned-prefix lookup per the ruled design) + the additive `ImportReport` field (the type is server-local at lines 24-31 — no `core/**` change). |
| `projects/pec/server/src/services/proposals.ts` | The two report-summary history strings (lines ~124-126 and ~190) **and** the `applyProposal` audit record's `newValue.report` literal (lines ~194-197, today `{accepted, updated, conflicts, rejected, intakeCreated}`) — all three count enumerations gain `alreadyDispositioned` so the append-only audit record never silently omits it (design point 5 made whole). |
| `projects/pec/server/test/import-proposal.test.ts` | Extend the existing RAIL re-import/OM-3 block (lines ~178-207) with tests pinning design points 1-5 and the edge case: dispositioned no-op + report line, changed-statement information line, live-shadow precedence, `force` inertness, newly-resolving-anchor coverage. |
| `projects/pec/web/src/pages/Admin.tsx` | Display-only: the local `ImportReport` interface (lines ~193-199), the proposal summary string (~147), and `ImportReportView` (~297-302) gain the new field/count. |
| `projects/pec/web/src/agent/AgentPanel.tsx` | Display-only: the local report shapes (lines ~36 and ~239) and the report line (~253) gain the new count. |

No RBAC, lifecycle, watermark, or proposal-state change. Branch-first; checks
on the final SHA: the workplan step-4 set (profile validator where touched;
repo self-check; pec belt-and-braces `npm run typecheck && npm test && npm run
build && npm run drill`; adversarial review of citations + git-diff scope
containment) plus `coord-check` on the committed range per the receipts'
standard check set; owner merge per the standing gate.

**Rollback plan (the D-PEC-08/D-PEC-17 tranche bar):** the tranche is
branch-first (`codex/pec-dpec15-reimport-matcher`); pre-merge abandonment is
closing the PR and deleting the branch — no trace on `main`. Post-merge
rollback is a single `git revert` of the tranche's merge commit: the change is
behavioral plus one additive report field. **There is no DB migration or
schema change to roll back**: `dry_run_report`/`apply_report` are
serialized-JSON TEXT columns (`server/src/repo.ts:54`, `server/src/db.ts:588`),
so the additive field needs no migration, pre-change proposal records remain
readable unchanged, and post-change records remain readable by pre-change code
(the extra field is ignored). No data backfill. No DB — scratch or otherwise
— is touched by the tranche itself: tests run on ephemeral DBs, and any
evidence re-run of the IPR-0006 shape is a separate scratch-basis act under
the standing rules.

**STOP clause (the D-PEC-17 rider-8 pattern):** if execution discovers a need
for a DB/schema change, a file outside the fence table above, or any behavior
beyond design points 1-5 and the disclosed edge case, execution STOPS and
returns to the owner — no in-run fence widening.

**Expressly out of scope (carried per the residual-row convention):** routing
the changed fields of a re-imported row through `intake_link` to update the
converted record. That would let an import mutate triaged controlled records
and is a different authority question entirely. Under O-C the severed update
channel (secondary consequence (b) above) remains — the report line makes it
visible; acting on it stays a human/agent screen act. On an O-C ruling this
residue is OPENED as its own named successor register row (next-free D-PEC
ID) per the residual-row convention — see On ruling — unless the owner's
ruling text explicitly declines the row, in which case that choice is
recorded verbatim.

### O-D — defer

The runbook v1.2 step 5 interim rule stands as written. The first post-triage
full re-import is handled ad hoc under it, at up-to-272-row scale (the actual
scale depends on the concurrent run's disposition rate).

## Constraints (bind any ruled option)

- **F-PEC-1** (workplan fence): source change only under a ruled tranche; the
  O-C fence above is that tranche if O-C is ruled; O-A/O-B touch only the
  runbook (the `execution/_Coordination/**` carve-out).
- **F-PEC-2** (no record-state invention): no option invents or file-mutates
  record state. O-C in particular creates no state and mutates no
  dispositioned record — it only reclassifies what the import *reports*.
  O-B's triage acts go through the RBAC'd API as D-PEC-10 ruled.
- **D-PEC-12 compatibility (checked, no contradiction found):** D-PEC-12
  ruled the proposal-seam semantics — single in-app record of authority,
  hash+version-bound acceptance, dry-run rollback, transaction-atomic apply,
  scope = the five §16 contracts "and nothing else. Any other operation family
  needs its own row" (packet section 2). No option here touches that
  lifecycle, adds an operation family, or changes a permission; O-C modifies
  behavior *inside* the existing `rail` contract. The recorded interpretation
  of the owner's amendment says gaps found in practice "come back as register
  rows, not as prose restrictions invented mid-run" — this row is that
  convention operating as designed. The update-in-place idempotency evidenced
  under D-PEC-10 WF-6 (un-dispositioned rows) is preserved unchanged by every
  option; O-C extends idempotency to the dispositioned boundary rather than
  contradicting it.
- **D-PEC-10 riders unchanged:** accept, apply, and `force` remain human
  screen acts; the agent-act boundary stands; scratch/demo mutation basis
  only until a pilot-DB row rules otherwise.
- **Immutable evidence:** the rehearsal snapshot
  (`PEC_2026-07-05_DPEC10-rehearsal-01/`) records the pre-change behavior as
  fact and is not revised by any option (D-T0-13 convention).

## Recommendation (non-binding)

**O-C.** The honest trade-off is weekly-cycle integrity versus source-change
surface, and it tips decisively after the 272-item run:

- O-A and O-B are both *perpetual* weekly taxes that grow with every triaged
  item; O-A additionally moves the failure mode upstream where the contract's
  never-silently-drop posture cannot see it, and O-B manufactures hundreds of
  audit-trail entries per week that document nothing.
- O-C is a small, mechanically checkable change at exactly the seam the
  matcher already owns (one additional lookup, one additive report field), it
  makes the weekly cycle clean by construction, and it *strengthens* the §16
  posture: the already-dispositioned rows become a named report category the
  owner sees at accept time, instead of either silent upstream pruning (O-A)
  or duplicate noise (O-B).
- The cost is real and should be weighed as such: it opens `server/src`
  scope on the import path — the core weekly seam — for the first time since
  D-PEC-17, and the report-shape addition ripples (minimally, additively)
  into the proposal history summaries, the append-only audit record's count
  literal, and the two web display sites — every ripple site is enumerated
  in the fence table. (One further report consumer exists outside the fence
  and needs no change: `tools/pilot-drill.ts:77-80` prints report counts, but
  the drill re-imports only MDL and never re-imports RAIL after triage, so
  the new category never fires there and no drill assertion is affected.)

If the owner prefers zero source surface right now, O-A is the workable
fallback and is compatible with ruling O-C later; in that case the agent
should own generating the weekly prune list at propose time so the fragility
is at least machine-checked.

## On ruling (mechanism)

- **O-A:** record the ruling verbatim here; flip the register row RULED.
  Author runbook **v1.3** — the append-a-new-version pattern with dated
  provenance, as v1.2 superseded v1.1's full-RAIL rule — recording the O-A
  procedure (prune-list derivation from the intake export, agent propose-time
  residue check) and superseding v1.2 step 5. Coordination-surface work only;
  receipt appended.
- **O-B:** same surface; author runbook **v1.3** (same append-a-new-version
  pattern, dated provenance) recording the expect-and-triage convention and
  naming the ruled sub-mode (weekly `duplicate` triage vs B2 standing
  shadows), superseding v1.2 step 5. Receipt appended.
- **O-C:** record the ruling verbatim; flip the row RULED. Execute the tranche
  branch-first under the fence table above (suggested branch
  `codex/pec-dpec15-reimport-matcher`), tests per the fence table's test row,
  the check set named in the fence (workplan step-4 set plus `coord-check`
  per the receipts' standard check set), owner merge per the standing gate.
  On merge, author runbook **v1.3** (append-a-new-version pattern, dated
  provenance) recording the ruled behavior and superseding v1.2 step 5. OPEN
  the severed-update-channel successor register row (next-free D-PEC ID) per
  the residual-row convention, unless the owner's ruling text explicitly
  declines it — the choice recorded verbatim either way. Optionally re-run
  the IPR-0006 shape on a scratch basis as evidence that the four rows now
  report `alreadyDispositioned` instead of `intakeCreated`. Receipt appended.
- **O-D:** the row records the deferral; the interim rule stands; the slate
  returns when the owner reopens it.

## Human ruling

**RULED: indefinitely postponed** (owner in-session 2026-07-07, Ryan Tufts,
verbatim — the direction addressed D-PEC-14/15/19 together, after receiving
plain-language explanations of all three packets in the same exchange):

> I don't quite understand what's being proposed by D-PEC-14 and D-PEC-15 or
> even D-PEC-19 for that matter.  What I would say is that future refinement
> of the interface and importing should be indefinitely postponed.  My
> intention now is to simplify workflows and reinforce only reporting on what
> is factual and has a clear basis.

Effect on this row: the postponement's practical shape matches O-D (defer) —
the owner did not name an option, so nothing beyond deferral is read into it.
`FILE_DROP_RUNBOOK.md` v1.2 step 5's interim rule stands as written; no
source change, no runbook v1.3, no successor row. The slate returns only if
the owner reopens it.
