# D-PEC-10 - PROPOSAL: agent-performed intake and triage (workflow intent, obligations, rehearsal gate)

**Status:** RULED (O-A, 2026-07-05).
**Date prepared:** 2026-07-05
**Decision ID:** D-PEC-10
**Prepared by:** PEC work loop agent. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

Structure precedent: the D-PEC-07 named-obligation pattern (RV-13..21), the
D-PEC-12 adopt/amend/defer slate, and the residual-row convention in
`_REGISTER.md`.

## Why (owner workflow intent of record)

Owner direction opening this row (2026-07-05, in-session, Ryan Tufts, verbatim
excerpt — Receipt 25): "I'm going to delegate the intake of those items. I want
the agent to do it once it has the capability."

Owner workflow intent of record (2026-07-05, in-session, Ryan Tufts, verbatim —
this quote governs; every obligation below cites it and no text may paraphrase
it in place of quoting it):

> So for now I'm planning to use it myself, on my local machine. I will be using the RAIL,
> Master Deliverables List, Risk Log, Schedule, and Package Tracker, to update the status by
> having the agent intake and triage the information therein to the correct database
> assignments. The interface will also allow the human to make targeted changes within the
> current screen and what it shows. But the agent is the primary means of making updates. As
> for how I get the information into those documents, it occurs from weekly updates and work
> I do within my team. That's the intended workflow, which was more than how I probably
> initially described it.

## Preparation direction of record (2026-07-05, in-session, Ryan Tufts, verbatim)

The owner's steer governing this packet's preparation, quoted in full:

> Steer (owner, D-PEC-10): I confirm the preparation direction and add the following, which
> governs the packet.
>
> 1. Record this as the owner workflow intent of record — quote it VERBATIM in the packet's
> "Why" section and in your receipt; do not paraphrase it anywhere; downstream text cites it:
>
> > So for now I'm planning to use it myself, on my local machine. I will be using the RAIL,
> > Master Deliverables List, Risk Log, Schedule, and Package Tracker, to update the status by
> > having the agent intake and triage the information therein to the correct database
> > assignments. The interface will also allow the human to make targeted changes within the
> > current screen and what it shows. But the agent is the primary means of making updates. As
> > for how I get the information into those documents, it occurs from weekly updates and work
> > I do within my team. That's the intended workflow, which was more than how I probably
> > initially described it.
>
> 2. Decompose that intent into numbered, individually checkable obligations in the packet
> (the D-PEC-07 → RV-13..21 pattern). Each is discharged explicitly or parked as its own new
> register row — no silent scope trims. At minimum the list must cover: (a) each of the five
> named source documents has a proposal-shaped agent path — note the Package Tracker has NO
> §16 import contract today, so it gets its own register row rather than an awkward MDL
> mapping; (b) weekly re-import of updated documents is idempotent (update-in-place, never
> duplicate); (c) human targeted screen edits and agent proposals interleave safely — the
> watermark/staleness guard is EXERCISED in evidence, not merely present; (d) the agent
> operates under its own provisioned actor identity so append-only history separates agent
> acts from mine; (e) every triage disposition (new record / update / intake disposition /
> conflict-for-owner) is auditable to its source row; (f) the decisions contract has no named
> source document in my workflow — resolve where decisions arrive from as a triage question,
> not an import assumption.
>
> 3. Verification is rehearsal, not merge: two documents suffice — RAIL and MDL, on test
> data the agent fabricates itself (synthetic, so no residency question), scratch/demo
> basis. Shape the rehearsal to exercise the obligations, not just the happy path: import
> each document twice (v1, then an edited v2) to prove idempotent update-in-place; include
> row shapes that force each triage disposition (new / update / intake disposition /
> conflict-for-owner); and interleave one human screen edit between a proposal's creation
> and its apply to force and recover from the staleness refusal. The agent intakes and
> triages; accept/apply stays with me at the screen — captured as an evidence snapshot per
> the L3-evidence convention. The full five-document weekly cycle is the intent, not the
> verification bar; item-2 obligations not exercised by this rehearsal (remaining
> contracts' live paths, etc.) are discharged by test or parked as their own register rows.
> Code landing alone does not discharge the intent; the rehearsed instance does.
>
> 4. Standing constraints unchanged: D-T0-14 CLOSED residency (rehearsal data is synthetic;
> real use is owner-provided by construction); no pilot DB — scratch/demo basis only;
> accept, apply, and force remain human acts per shipped RBAC; the D-PEC-12 ruling and
> amendment govern semantics. Prepare to AWAITING_RULING and stop at the gate.

## Decision to rule

Whether to adopt, as the D-PEC-10 mechanism: the obligations WF-1..WF-11 below
(the intent decomposed per direction item 2), the rehearsal gate (direction
item 3) as the verification bar, and the WF-10 decisions-source resolution —
under the standing constraints of direction item 4. The mechanism in one line:
the agent intakes and triages source-document information through the shipped
proposal seam and the shipped RBAC'd triage acts, under its own provisioned
actor identity; accept, apply, and `force` remain human acts at the screen.

## The shipped mechanical harness (verified facts; the harness governs per the D-PEC-12 recorded interpretation)

| Fact | Source |
|---|---|
| The proposal seam is live: propose / list / get / refresh / accept / reject / apply routes; dry-run rolls back; acceptance is hash+version-bound; apply is transaction-atomic. | `server/src/api.ts:341-366`; `server/src/services/proposals.ts`; D-PEC-08 tranche (PR #82), Receipt 24 |
| The staleness guard is a watermark: accept/apply compare the proposal's `basisHistoryId` to the current history watermark and refuse with 409 `STALE_PROPOSAL`; a refreshed dry-run voids any prior acceptance (RV-13). The watermark moves on history-evented record edits (deliverables, risks, interfaces, work items, intake, plan items) — but project-config and capacity edits are audit-only and do NOT move it. | `server/src/services/proposals.ts:53-54,61-66,121,151,183`; audit-only carve-outs `server/src/api.ts:375-403`, `server/src/services/plan.ts:440-445` |
| Exactly five §16 import contracts exist: `mdl`, `rail`, `decisions`, `risks`, `schedule`. There is NO Package Tracker contract. | `server/src/import/index.ts:79,156,319,381,438,493` |
| The proposal path is contract-generic (`?contract=` dispatch into the same `importContract` layer), but its test file pins the `mdl` contract only — per-contract live proposal evidence exists for `mdl` alone (L3-evidence-01). | `server/src/api.ts:341-345`; `server/test/import-proposal.test.ts`; `_DomainEngines/pec/PEC_2026-07-05_L3-evidence-01/MANIFEST.md` |
| Unanchored RAIL rows land as intake items with the source row bound in: `statementVerbatim` carries the verbatim `[item_id]` prefix and the import history line names the RAIL row. Re-import matches that prefix and updates in place (idempotency repair, PR #82). | `server/src/import/index.ts:217-257` |
| Intake lifecycle: `raised → in_triage → dispositioned`; the only legal transitions are `open_triage` and `disposition`, both gated by `intake.triage` (coordinator/pm/admin). | `core/src/lifecycles.ts:39-49`; `core/src/permissions.ts:93-95`; `core/src/types.ts:182-187` |
| Dispositions are `converted`, `merged`, `duplicate`, `rejected`, `parked`; `converted` atomically creates ≥1 record (work items, holds, risks, decisions, approval records, interfaces) with `intake_link` back-links; every act is version-bound and history-evented append-only; disposition notifies the raiser (open-triage does not). Conversion runs under the triage authority alone — per-type create permissions are skipped, including for approval records. | `server/src/services/intake.ts:87-156` (skipPermission at 110-127); `server/src/api.ts:290-293` |
| Roles are a fixed 14-token list with no agent role: an agent actor is a person record plus a role grant, and sessions are person-bound (DB-backed), so append-only history attributes every act to its person. The instance-admin flag is break-glass for everything except personal judgments — an agent person must be provisioned `is_admin=0` for role bounds to hold. | `core/src/types.ts:30-35`; `server/src/auth.ts`; `core/src/permissions.ts:78-79` |
| `import.propose`: admin/pm/coordinator/document_controller. `import.accept` (accept/apply): admin only. A `coordinator` grant covers `import.propose` + `intake.triage` and cannot accept or apply — but it also carries direct record create/update permissions (work items, risks, decisions, interfaces, holds, conditions); the agent-act rider below bounds what the agent exercises under this ruling. | `core/src/permissions.ts:224-231`; `core/src/permissions.ts:93-95`; roles/creators `core/src/permissions.ts:48`; act-families `core/src/permissions.ts:97-116`, `core/src/permissions.ts:154-163`, `core/src/permissions.ts:173-185`, `core/src/permissions.ts:205-213` |

## Obligations (WF-1..WF-11 — direction item 2; each discharged explicitly or parked as its own register row; no silent scope trims)

| ID | Obligation (intent clause served) | Discharge path |
|---|---|---|
| WF-1 | RAIL has a proposal-shaped agent path, exercised live ("I will be using the RAIL … to update the status"). | Rehearsal (v1 + edited v2). |
| WF-2 | The Master Deliverables List likewise. | Rehearsal (v1 + edited v2). |
| WF-3 | The Risk Log has a proposal-shaped agent path (the shipped `risks` contract through the generic seam). | Not rehearsed here: discharged by a later live-API scratch-basis exercise captured as evidence (no source change), or parked as its own register row on ruling — owner's choice per direction item 3. A per-contract test in `server/test/**` would itself need a ruled source tranche (F-PEC-1) and is not assumed. |
| WF-4 | The Schedule likewise (the shipped `schedule` contract, CSV/XER-derived per D-04). | Same as WF-3. |
| WF-5 | The Package Tracker has a proposal-shaped agent path. NO §16 contract exists today (verified above); per direction item 2(a) this parks as its own register row — a contract + path design, never an awkward MDL mapping. | PARKED by construction → new register row opened on ruling (contract design; carries its own L3-scope question — the ruled scope is imports per D-T0-18 O-A, and D-PEC-12 §2 states it as "The five §16 import contracts … and nothing else. Any other operation family needs its own row."). |
| WF-6 | Weekly re-import of updated documents is idempotent: update-in-place, never duplicate ("it occurs from weekly updates"). | Rehearsal: v1 then edited v2 for both RAIL and MDL, re-imported BEFORE any triage (the unanchored-intake prefix match covers un-dispositioned items only — dispositioned items no longer match); a post-triage re-import observation step captures the dispositioned-item behavior as fact, and any duplication gap found becomes its own register row. |
| WF-7 | Human targeted screen edits and agent proposals interleave safely ("The interface will also allow the human to make targeted changes within the current screen"); the watermark/staleness guard is EXERCISED in evidence, not merely present. | Rehearsal: one human screen edit — pinned to a history-evented record type (a deliverable field edit) — interleaved between a proposal's acceptance and its apply forces 409 `STALE_PROPOSAL`; recovery is captured (refresh → re-review → re-accept → apply). Boundary noted in evidence: project-config and capacity edits are audit-only and do not move the watermark. |
| WF-8 | The agent operates under its own provisioned actor identity so append-only history separates agent acts from the owner's. | Rehearsal: dedicated agent person, `is_admin=0`, with the `coordinator` role (covers `import.propose` + `intake.triage`, cannot accept/apply); history extract in evidence shows the actor split. |
| WF-9 | Every triage disposition — new record / update / intake disposition / conflict-for-owner — is auditable to its source row. | Rehearsal: synthetic rows shaped to force each of the four; evidence maps each outcome to its source row (import history refs, verbatim `[item_id]` intake prefixes, conflict report entries). |
| WF-10 | The decisions contract has no named source document in the owner's workflow; where decisions arrive from is resolved as a triage question, not an import assumption. Proposed resolution: decisions enter (i) by triage conversion of intake items (`converted` → decision record) and (ii) by the owner's targeted screen entry; the shipped `decisions` import contract stays dormant unless the owner later names a decisions source document. | Rehearsal exercises (i) with one synthetic intake row triaged `converted` → decision. The ruling affirms or amends the resolution; if amended, the amended text governs. |
| WF-11 | "But the agent is the primary means of making updates": the full five-document weekly cycle is the standing intent (not this rehearsal's bar); the cycle must be repeatable — weekly drop → agent proposals + triage → owner accept/apply at the screen. | EXERCISED at the two-document scope by the rehearsal itself (the rehearsed instance is the discharge); the standing five-document cycle rides the WF-3/4/5 rows. The runbook update (FILE_DROP_RUNBOOK v1.1 extension or successor) is a deliverable of execution, not itself a discharge. |

## Rehearsal gate (direction item 3 — verification is rehearsal, not merge)

- **Basis:** scratch/demo only (F-PEC-1; no pilot DB — direction item 4). A
  fresh scratch `PEC_DB`, seeded minimal cast, server on loopback. DB deleted
  after capture.
- **Data:** synthetic RAIL and MDL documents the agent fabricates itself (v1 +
  edited v2 each) — synthetic, so no residency question; D-T0-14 CLOSED
  untouched. Row shapes force each WF-9 disposition: new rows (create), edited
  rows (update-in-place), unanchorable rows (intake), and one RAIL v2 row whose
  verbatim statement is changed for an existing un-dispositioned intake item —
  the OM-3 conflict shape, reported as conflict-for-owner, never silently
  applied.
- **Actors:** the agent under its own provisioned person (`is_admin=0`,
  `coordinator` role — WF-8); the owner at the screen performs every accept and
  apply (`import.accept` is admin-only). `force` is never set by anyone in this
  run.
- **Sequence:** (1) agent files MDL v1 → dry-run → owner accepts + applies;
  (2) agent files RAIL v1 → owner accepts + applies → unanchored rows land as
  intake; (3) agent files edited v2 serially — MDL v2 propose → accept → apply,
  then RAIL v2 propose → accept → apply (an apply moves the watermark, so
  proposals are never left pending in parallel) → updated-in-place counts prove
  WF-6 and the conflict row surfaces in the report for the owner (WF-9); the
  owner's resolution of the conflict entry is captured; (4) agent triages each
  remaining intake item — open-triage + disposition, including one `converted`
  → decision (WF-10), one `parked`, one `duplicate`/`merged`; items the agent
  cannot ground in a source row are left un-dispositioned for the owner, never
  buried in a terminal disposition; (5) staleness exercise: agent files one
  further proposal; owner accepts; owner then makes one targeted screen edit (a
  deliverable field edit — history-evented); the apply attempt hits 409
  `STALE_PROPOSAL`; agent refreshes (voiding the acceptance); owner re-accepts;
  apply succeeds (WF-7); (6) post-triage observation: one further RAIL
  re-import captures, as fact, how rows whose intake items are now dispositioned
  behave (WF-6 boundary); any duplication gap found becomes its own register
  row; (7) capture.
- **Evidence:** immutable `PEC_<date>_DPEC10-rehearsal-01/` per the
  L3-evidence convention — manifest (actors, DB path, git SHA, SHA-256s),
  committed synthetic inputs, proposal/report JSONs, history extracts showing
  the agent/owner actor split, the per-disposition source-row audit map, and
  an export round-trip. The manifest carries the WF table with each obligation
  marked EXERCISED / DISCHARGED-BY-TEST / PARKED(row) — code landing alone
  discharges nothing; the rehearsed instance does.

## Scope notes

- **No pec source change is required or authorized by this packet.** The seam
  is shipped (PR #82); F-PEC-1 stays closed (per its RV-5 corrigendum reading:
  an absolute write-path fence — only an explicitly ruled tranche opens source
  scope). Any gap the rehearsal finds becomes its own register row (the
  D-PEC-12 recorded interpretation: "governance-harness gaps found in practice
  come back as register rows, not as prose restrictions invented mid-run") —
  never an in-run source change.
- **L3 scope is not extended — and this ruling grants one new authority.**
  RAIL/MDL (and risks/schedule/decisions) proposals sit inside the ruled
  D-T0-18/D-PEC-12 scope. The Package Tracker row (WF-5) carries the
  sixth-contract scope question when prepared. Agent triage acts
  (open-triage/disposition) are direct RBAC'd acts, not proposal-family acts:
  no `integration_level` change is claimed. Their authority does not exist
  today (D-T0-18: "no other write operation family is opened"; the D-PEC-12
  recorded interpretation's full-agency sentence is expressly scoped to the
  proposal pathway) — it is granted by THIS ruling naming the actor and
  policy, this packet being the "own row" D-PEC-12 §2 demands for a new
  family, on the same operating-human-basis pattern ("the operating human
  basis determines what the agent may lawfully drive end-to-end"). Accept,
  apply, and `force` remain human acts per shipped RBAC (direction item 4).
- **The register row's original wording** ("an agent pathway needs its own
  proposal-shaped design + authorization", opened at Receipt 25, before the
  D-T0-18/D-PEC-12 full-agency amendment) resolves as follows: the import path
  IS proposal-shaped as the row demanded; for the triage half, the
  proposal-shape expectation was superseded by the later full-agency amendment
  (Receipt 28), and this ruling itself is the authorization the row called
  for.
- **The 272 imported intake items** (this row's named block) are real RAIL
  content imported under the D-PEC-01 basis. Triaging them under the ruled
  mechanism proceeds only after the owner confirms the actor/visibility basis
  for that specific run (the D-PEC-01 rider-2 pattern — the owner may
  re-affirm the 2026-07-05 D-PEC-01 basis, which granted raw-view over exactly
  these rows, or supply a new one), on their existing scratch basis; those
  dispositions remain scratch-basis evidence — no real-record durability until
  a pilot DB exists (owner: "Another time", Receipt 26).

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Adopt WF-1..11, the rehearsal gate, and the WF-10 resolution as written. | Rehearsal executes branch-first with the owner at the screen; the WF-5 register row (and WF-3/4 rows if parked rather than tested) opens on execution; evidence snapshot + receipt; STOP at owner merge. |
| O-B | Adopt with owner amendments (state them in the ruling). | Amended text is recorded verbatim; execution follows the amended text. |
| O-C | Defer. | Row stays open; the 272 items keep awaiting triage; no rehearsal. |

## Recommendation (non-binding)

O-A. The mechanism adds no new mechanical gate — every gate is already shipped
and exercised (RBAC, watermark staleness, version binding, append-only
history) — and it grants exactly one new authority: an RBAC-bounded,
rider-bounded actor basis for the intake-triage family, granted by this ruling
alone (the "own row" D-PEC-12 §2 demands). The rehearsal exercises the
obligations rather than trusting code landing, and the places the intent
outruns today's shipped surface (Package Tracker, un-rehearsed contract live
paths) are carried as named rows instead of silent trims.

## On ruling (mechanism)

- **O-A:** record the ruling verbatim here; flip the register row to RULED.
  Execute the rehearsal branch-first (`codex/pec-dpec10-rehearsal`) with the
  owner at the screen for every accept/apply — in-session if the owner is
  present, else scheduled; capture `PEC_<date>_DPEC10-rehearsal-01/`; open the
  WF-5 Package Tracker row (and WF-3/4 rows if the owner parks rather than
  tests them); author the WF-11 runbook update; append the receipt (workflow
  intent quoted verbatim per direction item 1); workplan step-4 checks; STOP
  at owner merge. The 272-item triage run then proceeds under the ruled
  mechanism on its existing scratch basis only after the owner confirms the
  actor/visibility basis for that run (Scope note 4).
- **O-B:** same, per the amended text.
- **O-C:** the row records the deferral; no execution; the decision slate
  returns whenever the owner reopens it.

## Human ruling

**Ruling:** O-A affirmed by owner (Ryan Tufts), 2026-07-05.

Owner ruling of record (verbatim, in-session):

> 1. I rule `O-A`
> 2. merge PR #86

PR #86 was merged as directed (merge commit `9dd310cc3`); execution proceeds
per the On-ruling O-A mechanism in the PR carrying this note.

**Ruling SHA:** `9dd310cc3` (PR #86 merge commit — the packet the owner ruled on).

**Status change:** AWAITING_RULING → RULED.

## Riders (bind any ruled option)

- Accept, apply, and `force` remain human acts per shipped RBAC; no agent run
  ever sets `force=true` (direction item 4).
- **Agent-act boundary:** under this ruling the agent exercises only import
  propose/refresh/withdraw and intake open-triage/disposition (including the
  conversion records a disposition names — never approval records, which
  conversion could otherwise create under `skipPermission`). The other
  act-families a `coordinator` grant carries (direct record create/update,
  hold resolution, condition satisfaction) are NOT exercised by the agent
  absent their own register row. The agent person is provisioned
  `is_admin=0`. Items the agent cannot ground in a source row are left
  un-dispositioned for the owner.
- Scratch/demo basis only; no pilot DB; no non-scratch DB mutation (F-PEC-1).
- Rehearsal data is synthetic; real use is owner-provided by construction;
  D-T0-14 CLOSED unchanged; no instance-content visibility beyond an
  owner-enumerated basis (the D-PEC-01 pattern), and the RV-12 rider stands —
  no LLM call exists in the app and none is added.
- No record-state invention: every state change through the RBAC'd API only
  (F-PEC-2); no pilot-readiness, go-live, or issuance claim.
- Code landing alone does not discharge the intent; the rehearsed instance
  does (direction item 3).
