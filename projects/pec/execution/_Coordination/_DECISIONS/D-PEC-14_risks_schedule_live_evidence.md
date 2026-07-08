# D-PEC-14 - PROPOSAL: Risk Log + Schedule proposal-path live evidence (D-PEC-10 obligations WF-3/WF-4)

**Status:** PROPOSAL / RULED — indefinitely postponed (owner, 2026-07-07; verbatim in Human ruling).
**Date prepared:** 2026-07-06
**Decision ID:** D-PEC-14
**Prepared by:** PEC work loop agent. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

Structure precedent: the verified-facts + options + on-ruling-mechanism shape of
`D-PEC-10_agent_intake_triage.md` and the design-gate option slate of
`D-PEC-16_builtin_agent_ui.md`. No pre-ruling covers this row: the 2026-07-06
session-scoped conditional standing pre-ruling (Receipt 32 item 4) named
D-PEC-13/14/15 as eligible but expired by its own terms at that session's end,
and this packet is a later session's work — so it stops at this gate for the
owner's read.

**Register note (write fence):** this packet was authored under a one-file
write fence; the register row flip NOT_PREPARED → AWAITING_RULING rides the
PR that carries this packet, not a separate edit in this tranche.

## Why this row exists

Register row D-PEC-14 (opened on the D-PEC-10 ruling, per its WF-3/WF-4
discharge paths), verbatim:

> Risk Log + Schedule proposal-path live evidence (D-PEC-10 obligations
> WF-3/WF-4): a live-API scratch-basis exercise captured as evidence, or a
> per-contract test under a ruled source tranche — undischarged by the
> RAIL+MDL rehearsal per direction item 3.

The workflow these obligations serve is the owner workflow intent of record
(2026-07-05, in-session, Ryan Tufts, verbatim — this quote governs; no text
may paraphrase it in place of quoting it):

> So for now I'm planning to use it myself, on my local machine. I will be using the RAIL,
> Master Deliverables List, Risk Log, Schedule, and Package Tracker, to update the status by
> having the agent intake and triage the information therein to the correct database
> assignments. The interface will also allow the human to make targeted changes within the
> current screen and what it shows. But the agent is the primary means of making updates. As
> for how I get the information into those documents, it occurs from weekly updates and work
> I do within my team. That's the intended workflow, which was more than how I probably
> initially described it.

Why rehearsal-01 did not discharge these rows — the owner's preparation
direction item 3 (2026-07-05, verbatim and in full from the D-PEC-10 packet):

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

And direction item 4 (verbatim and in full):

> 4. Standing constraints unchanged: D-T0-14 CLOSED residency (rehearsal data is synthetic;
> real use is owner-provided by construction); no pilot DB — scratch/demo basis only;
> accept, apply, and force remain human acts per shipped RBAC; the D-PEC-12 ruling and
> amendment govern semantics. Prepare to AWAITING_RULING and stop at the gate.

Two sentences in those directions bear directly against option O-A below, and
this packet does not soften them: "The agent intakes and triages; accept/apply
stays with me at the screen" (item 3) and "accept, apply, and force remain
human acts per shipped RBAC" (item 4, carried forward as a ruled D-PEC-10
rider). O-A can proceed only if the owner **knowingly varies that rider for
this discharge run** — the variance is stated in the option itself and argued
openly in the Recommendation.

Rehearsal-01 exercised RAIL and MDL exactly as directed and marked WF-3/WF-4
`PARKED → register row D-PEC-14` in its manifest
(`_DomainEngines/pec/PEC_2026-07-05_DPEC10-rehearsal-01/MANIFEST.md`).

On the risk data specifically, the owner's standing direction (2026-07-05,
in-session, Ryan Tufts, verbatim excerpt — Receipt 25):

> I will upload risks but at a later time. Deferred.

## Verified facts (live tree, 2026-07-06 — the live tree wins over any stale claim)

| Fact | Source |
|---|---|
| Both contracts are wired through the full IPR lifecycle in code. `CONTRACTS = ['mdl', 'rail', 'decisions', 'risks', 'schedule']` gates `createProposal`; the propose/list/get/refresh/accept/reject/apply routes are contract-generic (`?contract=` dispatch); dry-run and apply both call the one `importContract` switch, which dispatches `risks` → `importRisks` and `schedule` → `importSchedule`. Nothing code-side blocks a risks or schedule proposal today. | `server/src/services/proposals.ts:22,76-84,186`; `server/src/api.ts:342-367`; `server/src/import/index.ts:493-500` |
| No proposal-path evidence or test exists for either contract. Live IPR evidence covers `mdl` (L3-evidence-01), `rail`+`mdl` (rehearsal-01, IPR-0001..0006), and `mdl` only again in both 2026-07-06 packs (`PEC_2026-07-06_DPEC17-evidence-01`, `PEC_2026-07-06_BRIDGE-evidence-01` — manifests checked: every proposal in each is `contract=mdl`). The proposal test file pins `contract=mdl` only. The direct (legacy) import endpoints for risks and schedule DO have tests — but that is the pre-IPR seam, not the proposal path these obligations name. | `server/test/import-proposal.test.ts:33-168`; the four evidence manifests; direct-seam tests `server/test/integration.test.ts:209`, `server/test/p2-plan.test.ts:269-274` |
| **The owner's risk log is template-empty (live fact, re-verified read-only 2026-07-06).** `pilot-scratch/input/risk.xlsx` (owner-dropped 2026-07-05, unchanged since) holds only scaffold content (Risk Log grid + Risk Chart legend sheets): **100 pre-numbered rows `RISK-1..RISK-100`** with zero populated titles/descriptions; every shared string in the workbook is legend/header text. The derived extract agrees: `pilot-scratch/derived/risks-verbatim.csv` is 155 lines — a 10-line scaffold preamble + header, then 145 lines of which the 100 pre-numbered `RISK-N` rows are the only ID-bearing ones (the other 45 are entirely blank) — and **zero** lines anywhere carry a risk title or description. This matches the owner's Receipt 25 deferral and the `IMPORT_MAPPING.md` "placeholder/scaffold only" note, which carries an unratified placeholder crosswalk for when real risks arrive. | `pilot-scratch/input/risk.xlsx`; `pilot-scratch/derived/risks-verbatim.csv`; `IMPORT_TEMPLATES/IMPORT_MAPPING.md` §risks |
| The schedule input is real, mapped, and proven — but only through the legacy seam. Owner-dropped `pilot-scratch/input/schedule.csv` (127 extractor rows) was mapped to the §16 shape (`activity_id ← SCH-{id}`) as `pilot-scratch/import-ready/schedule.csv` and imported 127/127 accepted in pilot-evidence-04 — via the direct `/import/schedule` endpoint, before the IPR seam existed. The proposal path has never carried a schedule CSV. | `_DomainEngines/pec/PEC_2026-07-05_DPEC01-pilot-evidence-04/MANIFEST.md`; `IMPORT_TEMPLATES/IMPORT_MAPPING.md` §schedule |
| Contract behaviors the evidence should pin: `risks` has the full conflict surface — `ref = risk_id` idempotency, in-app-edit-since-import conflict refusal (`use force=true` reported, never auto-applied), row-level rejects (missing risk_id/title/status, unknown status, unmatched owner, probability/impact outside 1-5). `schedule` rows are import-owned (no in-app edit path): re-import always refreshes in place and the contract ignores `force` by construction (`_force`) — it has NO conflict path, which the evidence records as fact rather than papering over. | `server/src/import/index.ts:378-434` (risks), `435-491` (schedule) |
| **The accept/apply basis for O-A, stated honestly — it is NOT settled standing precedent.** The owner's verbatim D-PEC-12 ruling says only: "The agent should have full agency, don't try to use semantics as a replacement for proper governance harnesses (more than just semantics) so focus on making a useful agent for now." The demo/scratch accept-apply clause is the packet's **agent-authored recorded interpretation** of that ruling, and by its own terms defers to the ruling text on any disagreement. The two demo-cast executions — Receipts 34/35, a **prior session** (2026-07-06) — ran while Receipt 32 item 4 was live: that owner text expressly permitted demo-cast accept/apply on scratch for rehearsal evidence and **expired by its own terms at that session's end**. Force posture there: `force` never sent (Receipt 34; absent is treated as false — the apply route binds `b.force === true`) / `force: false` pinned on both applies (Receipt 35). Demo-cast accept/apply for THIS run would therefore be a **fresh owner choice made by this ruling**, informed by that interpretation and by the now-expired Receipt-32 characterization — disclosed as such, not claimed as inherited authority. | `D-PEC-12_l3_import_proposal_semantics.md` (Human ruling + recorded interpretation); `_DomainEngines/pec/LOOP_RECEIPTS.md` Receipts 32/34/35; `server/src/api.ts:363-367` |

## Decision to rule

How the D-PEC-10 obligations WF-3 (Risk Log proposal-shaped agent path) and
WF-4 (Schedule likewise) get discharged **at evidence level** — the register
row's two named routes (live-API scratch-basis exercise captured as evidence,
or per-contract test under a ruled source tranche), the data basis for each
contract, and who performs accept/apply.

One framing reading the options turn on — **this packet's reading, not
established fact; the ruling may reject it**: WF-3/WF-4 are obligations about
the **path** — that each contract works end-to-end through the proposal seam
under the agent's actor basis — not about the owner's real data landing. On
that reading, synthetic risk rows discharge the path evidence exactly as
synthetic RAIL/MDL rows did in rehearsal-01 (direction item 3: "synthetic, so
no residency question"), and the owner's real risks upload stays an owner-side
act on its own clock (Receipt 25) regardless of which option rules here.

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | **Live-API scratch-basis evidence run, demo-cast accept/apply.** The rehearsal-01 mechanism end to end: fresh guarded-seed scratch DB; the agent under its own provisioned person (`is_admin=0`, coordinator) files and refreshes risks + schedule proposals through the live HTTP API; accept and apply are performed by the seeded demo-cast admin on the scratch basis, disclosed per act, `force` never true. Data: **synthetic, agent-fabricated, for BOTH contracts by default** (risk.xlsx is template-empty — verified above — and synthetic data carries no residency question); re-use of the real evidence-04 schedule CSV is a **separate explicit opt-in line in the ruling** (basis in Constraints). **Ruling O-A expressly authorizes, for this discharge run only, a variance of the ruled D-PEC-10 rider "Accept, apply, and `force` remain human acts per shipped RBAC" — the demo-cast admin, not the owner at the screen, performs accept/apply.** | WF-3 and WF-4 discharge without a scheduled owner session; evidence `PEC_<date>_DPEC14-evidence-01/`; the accept/apply acts are demo-cast-on-scratch, disclosed per act — not a rehearsal of the owner's own screen workflow (stated in the manifest); the rider variance and the schedule-data choice are both recorded in this row's ruling. |
| O-B | **Owner-at-the-screen accept/apply (the rehearsal-01 exact pattern), scheduled.** Same run design as O-A, but every accept and apply is the owner's act at the screen, as in rehearsal-01. The D-PEC-10 rider holds unvaried. | The human-gate half is exercised by the actual human gate; requires a scheduled owner session; WF-3/WF-4 remain open until it happens. |
| O-C | **Per-contract tests under a ruled source tranche.** Extend `server/test/import-proposal.test.ts` (or a sibling) to drive `contract=risks` and `contract=schedule` through propose → refresh → accept → apply, pinning the risks conflict/reject shapes and the schedule no-conflict/force-ignored behavior. F-PEC-1 is an absolute write-path fence: this needs its own ruled tranche packet (exact file fence, tests, rollback) — it is not assumed by this row. | Durable regression coverage; opens source scope; discharge is by code artifact rather than a rehearsed instance — the register row's second-named route. Compatible as a follow-on to O-A/O-B rather than a substitute. |
| O-D | **Defer risks until the owner uploads; discharge schedule now** (O-A or O-B shape for the schedule half only), per the surface reading of "I will upload risks but at a later time." | WF-4 discharges; WF-3 remains open, pinned to the owner's upload clock and carried by a **new successor register row** per the residual-row convention (mechanism below) — this row still flips RULED. |

Combinations are rulable (e.g., O-A now + O-C later as a tranche row; O-B for
schedule + O-A for risks). If the owner amends, the amended text governs and
is recorded verbatim.

## The evidence run (shared design, O-A/O-B)

- **Basis:** fresh scratch DB via the D-PEC-06-guarded seed, server on
  loopback, DB deleted after capture (rehearsal-01 pattern). The existing
  D-PEC-01 surfaces (`pec-scratch-import.db`, backups) untouched.
- **Actors:** agent under its own provisioned person (`is_admin=0`,
  `coordinator` — proposes, refreshes, withdraws); accept/apply per the ruled
  option (owner at the screen under O-B, or demo-cast admin disclosed per act
  under O-A's rider variance). `force` is never set to true by anyone; the
  schedule contract's force-ignored behavior is recorded as fact.
- **Risks sequence:** synthetic v1 (rows shaped to force accepts + each
  reject class: missing required field, unknown status, unmatched owner,
  out-of-range probability) → propose → dry-run → accept → apply; edited v2
  re-import proves `ref = risk_id` update-in-place. A v3 proposal then
  exercises both guards in the code-consistent order: **propose v3 → dry-run
  → accept → one in-app risk edit (history-evented; moves the watermark) →
  apply refused 409 `STALE_PROPOSAL` → refresh (voids the acceptance and
  re-baselines; the refreshed dry-run now reports the in-app-edited row as a
  conflict) → re-accept → apply with `force=false` → the conflicted row is
  reported and left untouched while the remaining rows apply.**
- **Schedule sequence:** synthetic activities v1 (default) → propose →
  dry-run → accept → apply; edited v2 proves refresh-in-place. If the owner
  opts into the real CSV (explicit ruling line), the mapped evidence-04
  `import-ready/schedule.csv` — same file, same SHA-256 — is used instead.
  Either way the no-conflict/import-owned boundary is stated in the manifest,
  not discovered later.
- **Capture:** immutable `PEC_<date>_DPEC14-evidence-01/` per the L3-evidence
  convention — manifest (actors, DB path, git SHA, SHA-256s), committed
  synthetic inputs (+ the schedule CSV reference if opted in), proposal/report
  JSONs, history extracts showing the actor split, export round-trips.

## What the run would and would not claim (F-PEC-2)

Facts only. It would claim: the `risks` and `schedule` §16 contracts work end
to end through the live proposal seam under the agent actor basis, with the
stated conflict/reject/idempotency behaviors observed. It would NOT claim:
pilot readiness, go-live, correctness of the `IMPORT_MAPPING.md` risks
placeholder crosswalk (unratifiable until real risk rows exist), anything
about the owner's real risk data (none exists in the tree), or — under O-A —
that the owner's screen workflow was rehearsed (demo-cast accept/apply is
disclosed as such, per act). Mutation basis: scratch only, deleted after
capture. Discharge of a D-PEC-10 obligation is recorded by evidence +
receipt, never by code landing (owner direction item 3).

## On ruling (mechanism)

Common to O-A/O-B/O-D: execute branch-first; capture
`PEC_<date>_DPEC14-evidence-01/`; the manifest carries a WF-3/WF-4 status
table (EXERCISED / boundary observations); append the receipt (workflow
intent quoted verbatim); flip this register row to RULED with the ruling
verbatim; STOP at owner merge.

**Where the WF-3/WF-4 discharge is recorded — precisely:** the D-PEC-10
packet is RULED and is **never amended** (the register's residual-work
convention: a ruling's residue gets its own row; a ruled packet is not
reopened or annotated). The discharge record is the triple: (1) the
`DPEC14-evidence-01` manifest's obligation table, (2) the receipt entry, and
(3) this row's ruling record in the register. Anyone auditing WF-3/WF-4
follows D-PEC-10's discharge-path cell → this row → the evidence dir. No
edit to `D-PEC-10_agent_intake_triage.md` occurs under any option.

Per option:

- **O-A:** run in the next work-loop session with demo-cast accept/apply
  disclosed per act and `force` never true; the ruling records the D-PEC-10
  rider variance verbatim and the schedule-data choice (synthetic default /
  real-CSV opt-in); both WF-3 and WF-4 marked EXERCISED in the manifest.
- **O-B:** same capture, scheduled with the owner at the screen for every
  accept/apply; the row stays AWAITING-execution until the session happens.
- **O-C:** this row's ruling authorizes preparation of a tranche packet
  (exact test-file fence under `projects/pec/server/test/**`), which itself
  goes to its own gate; WF-3/WF-4 flip only when the ruled tests land and the
  receipt records them — noting the register row's own text treats test-based
  discharge as requiring the ruled tranche, and discharge is still recorded
  in this row's chain, not in D-PEC-10.
- **O-D:** the schedule half proceeds per the ruled shape and **this row
  flips RULED** with the WF-4 discharge recorded in its chain. The risks half
  is residue, and residue never stays open on a ruled row (the register's
  residual-row convention): a **new successor row** is minted next-free at
  execution (deconfliction against the live register honored), opened
  NOT_PREPARED, carrying WF-3 with the owner's risks upload as its named
  unblock.

## Constraints (bind any ruled option)

- **Write fences:** no pec source change under this row (F-PEC-1 absolute;
  O-C's tests require their own ruled tranche). Evidence writes go only to
  `_DomainEngines/pec/PEC_<date>_DPEC14-evidence-01/` + receipt + register
  row + this packet's ruling section.
- **Residency and capture (kept distinct):** synthetic data — the default
  for both contracts — carries no residency question (direction item 3;
  rehearsal-01 precedent). *Visibility:* reading the owner-dropped
  `input/risk.xlsx` to establish the template-empty fact is lawful under the
  D-T0-20 O-B enumerated OPEN surface (item (iv), owner-dropped weekly files);
  D-T0-20 governs visibility only and expressly leaves capture limits to the
  D-PEC-01/RV-11 conventions. *Capture (real-CSV opt-in only):* committing
  the mapped schedule CSV into the evidence dir is re-use of content already
  captured under the 2026-07-05 basis — the mapped file itself lives on the
  gitignored pilot-scratch surface, SHA-pinned in the committed evidence-04
  manifest (live file verified byte-identical to that pin), and the same
  instance content is already committed unredacted via evidence-04's export
  round-trip — not materially new capture under the Receipt-22 S-2 RV-11
  convention, so the D-PEC-01 2026-07-05 basis carries it; and this
  ruling's named data basis doubles as the owner's capture confirmation for
  this run. Agent person provisioned `is_admin=0`.
- **Mutation basis:** scratch only; fresh DB, deleted after capture; no
  pilot DB; the D-PEC-01 scratch instance and its backups untouched.
- **No force:** `force=true` is never sent by anyone; the schedule
  contract's structural force-ignore is disclosed, not exploited.
- **Accept/apply are human acts** per shipped RBAC (`import.accept`
  admin-only) and per the ruled D-PEC-10 rider — **unless** the ruled option
  is O-A, in which case **this ruling itself** authorizes the demo-cast
  variance afresh (recorded verbatim in the ruling; not carried by standing
  authority), with per-act disclosure in the evidence and `force` never true
  (the Receipts 34/35 disclosure pattern: never sent / `force: false`
  pinned).
- No pilot-readiness, go-live, or issuance claim (F-PEC-2); gaps found in
  the run become register rows, never in-run fixes (D-PEC-12 recorded
  interpretation).

## Recommendation (non-binding)

**O-A (synthetic data for both contracts), with O-C available later as its
own tranche row if the owner wants regression pinning.** Reasoning:

1. Both contracts are already wired through the IPR lifecycle — the only
   thing missing is the exercised instance, which is exactly what a scratch
   evidence run produces.
2. The owner's risk log is verifiably template-empty, so synthetic risk data
   is not a compromise but the only lawful content available, and direction
   item 3 already ruled synthetic data residency-clean. Synthetic schedule
   data keeps the run uniform; the real-CSV opt-in costs one ruling sentence
   if the owner prefers evidence-04 continuity, and its capture basis is
   already carried (Constraints).
3. **The accept/apply question, argued openly rather than assumed.** The
   owner's own words cut against O-A twice: "accept/apply stays with me at
   the screen" (item 3) and the ruled rider "accept, apply, and `force`
   remain human acts per shipped RBAC" (item 4). This packet does not
   reinterpret those away — they were written as the D-PEC-10 rehearsal's
   shape and they still bind. O-A asks the owner to **vary the rider
   knowingly, for this narrower run only**, on this ground: rehearsal-01
   already exercised the human gate itself — the owner at the screen, on this
   exact seam, including the staleness refusal and its recovery. What
   WF-3/WF-4 still lack is per-contract path evidence, not human-gate
   evidence. The demo-cast shape has run cleanly twice before (Receipts
   34/35) — but under a session-scoped owner permission that has since
   expired, in a prior session — so it is offered here as a fresh choice the
   owner makes with that history in view, not as precedent that decides
   anything. If the owner declines the variance, O-B is the identical run
   with the rider intact, and costs only the scheduling dependency.
4. Against O-D: on this packet's path-not-data reading, deferring risks
   leaves a ruled obligation open on a data-arrival clock it does not depend
   on, and spawns a successor row for no protective gain — the real upload
   gets its own import run (and, if the owner wants it, its own capture)
   whenever it happens, under any option ruled here.

## Human ruling

**RULED: indefinitely postponed** (owner in-session 2026-07-07, Ryan Tufts,
verbatim — the direction addressed D-PEC-14/15/19 together, after receiving
plain-language explanations of all three packets in the same exchange):

> I don't quite understand what's being proposed by D-PEC-14 and D-PEC-15 or
> even D-PEC-19 for that matter.  What I would say is that future refinement
> of the interface and importing should be indefinitely postponed.  My
> intention now is to simplify workflows and reinforce only reporting on what
> is factual and has a clear basis.

Effect on this row: none of O-A/O-B/O-C/O-D is selected; the WF-3/WF-4
discharge question is postponed indefinitely as import refinement. The
D-PEC-10 obligations remain undischarged and this row remains their register
home; the slate returns only if the owner reopens it. No evidence run, no
tranche, no successor row.
