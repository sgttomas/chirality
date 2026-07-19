# Orchestration Plan — Concordance Rulings and Governed Repairs

- **RunID:** `APPDEV_LOOP_2026-07-19_CONCORDANCE_RULINGS`
- **Plan version:** 1 — FROZEN BEFORE PACKAGE DISPATCH; active execution
  amendment v2 is non-consequential and recorded under `amendments/v2.md`
- **Parent:** HELP_HUMAN (Agent 0)
- **Selection authority:** HUMAN
- **Posture:** MIXED
- **Branch:** `codex/app-dev-concordance-rulings-20260719`
- **Accepted basis:** `96563e8e09b89908e13e6b2f1f1139aca3283855`
- **Parent handoff:** Receipt-74
- **Date:** 2026-07-19
- **Current status:** C0 complete. Original R1 was interrupted after an
  extended read phase, made no repository changes outside this run root, and
  produced no accepted output. Amendment v2 replaces its execution node with
  concurrent R1A and R1B; every package dispatch remains held until both
  returns are accepted.

## Objective

Transcribe the owner's eight approved recommendations into one governed ruling
record, derive an exact repair manifest, execute only the resulting
package-local documentary repairs through disjoint WORKING_ITEMS managers,
independently verify the fan-in, and then perform serialized loop closeout and
CHANGE publication. This run implements already-rendered owner decisions; it
does not make new decisions.

Frontend runtime source, lifecycle transitions, release-prep, domain-engine
apply/accept work, and every hard-fenced surface are excluded.

## Authoritative owner ruling

The authoritative chat ruling on 2026-07-19 is:

> “I approve recommendations 1–8.”

The numbering is bound to the chronology in which the recommendations were
actually presented, not to the earlier derivative slate's numbering.

## Approved chronology and operative interpretation

1. **Legacy CLM blocks are live normative content.** Contradictions inside
   migrated `ScopeOfWork.md` CLM blocks are repaired; they are not excused as
   inert historical quotations.
2. **No redundant standalone D-APP pointer for D-GOV-16.** D-GOV-16 already
   authorizes the migration. Annotate live dangling migration citations where
   they remain operative; immutable prior concordance ledgers remain unchanged.
3. **Managed-orchestration ownership.** Record one consolidated mapping of the
   managed-orchestration surface across the nearest existing DEL-05, DEL-06,
   and DEL-08 owners. Do not create a new deliverable or duplicate ownership.
4. **DEL-08-04 refresh.** Refresh the live deliverable content to cite ruled
   D-GOV-14 item 7 and `delegate_agent` as the active managed delegation path.
5. **Child-output thresholds are a no-op confirmation.** D-APP-56 R4-P32
   already made 16 KiB / 512 KiB normative under DEL-08-05; DEL-05-05
   explicitly does not own those thresholds. Do not create a new threshold
   ruling or transfer ownership.
6. **Bash timeout ratification.** Record 120000 ms default and 600000 ms
   maximum under DEL-06-05.
7. **PEC hygiene ownership.** Assign the PEC credential/cookie envelope
   hygiene surface to DEL-05-03, citing D-APP-52 and D-APP-67 and preserving
   the limits of those rulings.
8. **Version-pinned adoption verdict.** DEL-04-01 is
   `ADOPT_WITH_RESIDUAL_RISK`. The decision record must name and assess the
   twelve existing residual categories: SDK API drift, settings leakage,
   allowed-tools misconception, transcript location, Electron packaging, SDK
   security boundary, subagent inherited permissions, session-mirror
   reliability, product-identity drift, platform dependency,
   reliance-boundary ambiguity, and engine-adapter lock-in. The verdict is
   demonstrator-scoped and is not release approval, issuance, certification,
   or professional acceptance.

### Refuted derivative item

The earlier derivative-slate suggestion that the Pipeline scaffold lacked an
owner is refuted/no-op. D-APP-56 R4-P28 already assigns that surface to
DEL-02-02. No PKG-02 dispatch, mapping change, or source edit is authorized by
this run for that item.

## Work graph

The machine-readable graph is `WORK_GRAPH.json`.

| Node | Owner | Function | Depends on | State at v1 freeze |
|---|---|---|---|---|
| C0 | CHANGE | Create/switch branch at exact clean basis | none | COMPLETE |
| R1 | RECONCILIATION | Original combined ruling/manifest node | C0 | INTERRUPTED / NOT ACCEPTED |
| R1A | RECONCILIATION | Shared D-APP-68 packet + register row | C0 | READY |
| R1B | RECONCILIATION | Derivative exact repair/mapping manifest | C0 | READY |
| P01 | WI-PKG00-01 | PKG-00/01 repairs from manifest | accepted R1A + R1B | HELD |
| P04 | WI-PKG04 | DEL-04-01 adoption-verdict record/repairs | accepted R1A + R1B | HELD |
| P05 | WI-PKG05 | PKG-05 ownership/hygiene repairs | accepted R1A + R1B | HELD |
| P06 | WI-PKG06 | PKG-06 ownership/timeout repairs | accepted R1A + R1B | HELD |
| P08 | WI-PKG08 | PKG-08 ownership/delegation/no-op annotations | accepted R1A + R1B | HELD |
| V1 | EVALUATION | Independent read-only verification of all governed surfaces | all five accepted package returns | HELD |
| C1 | ORCHESTRATOR | Accepted fan-in, Receipt-75, completion-log and handoff closeout | accepted V1 | HELD |
| G1 | CHANGE-PUBLISH | Coherent commit, push, and PR | accepted C1 | HELD |
| H1 | OWNER | Review and merge | G1 | TERMINAL OWNER ACT |

R1A and R1B may run concurrently because their writes are disjoint: R1A alone
owns the shared decision packet/register stage, while R1B writes only a new
derivative manifest and its run-local evidence. The five package managers may
run concurrently only after both returns are accepted and R1B has frozen
exact, non-overlapping write targets. Their package writes remain disjoint.
C1 owns the later serialized shared closeout. V1 is read-only on governed/
project surfaces and writes verification evidence only inside this run
directory. No sibling direct messaging is required; notices and returns route
through the parent hierarchy.

## R1 interruption and amendment-v2 split

Original R1 was interrupted after an extended read phase. It made no
repository changes outside this run root, and no R1 output was accepted. Its
objective, owner ruling, interpretation, scope, package topology, validation
criteria, and stop conditions remain unchanged. Amendment v2 only decomposes
the work into two disjoint coordination nodes:

R1A must:

1. Transcribe the exact owner quote and the eight chronology-bound meanings
   into `execution/_Coordination/_DECISIONS/D-APP-68_PACKET_CONCORDANCE_RULINGS_2026-07-19.md`.
2. Append exactly one governed D-APP-68 row to
   `execution/_Coordination/_DECISIONS/_REGISTER.md`; do not alter prior ruled
   rows.

R1B must:

1. Write `REPAIR_MANIFEST.md` in this run root with every proposed package
   write named as an exact path, assigned to exactly one package manager, and
   traced to one or more of rulings 1–8.
2. Mark no-op/refuted items explicitly and assign them no repair write.
3. Return blockers rather than inventing a target or broadening authority.

No package brief becomes executable until HELP_HUMAN accepts both R1A and R1B
and amends each package placeholder with its exact R1B manifest slice. This
plan freezes the ownership graph; R1A freezes the ruling record; R1B freezes
the path-level graph.

## Package ownership and boundaries

- **WI-PKG00-01:** only manifest-listed live PKG-00/01 `ScopeOfWork.md` or
  deliverable-local evidence/history annotations for rulings 1–2.
- **WI-PKG04:** only manifest-listed DEL-04-01 decision/evidence and
  deliverable-local truth surfaces for ruling 8.
- **WI-PKG05:** only manifest-listed PKG-05 deliverable-local surfaces for the
  DEL-05 side of ruling 3 and PEC ownership ruling 7; threshold ownership must
  remain outside DEL-05-05.
- **WI-PKG06:** only manifest-listed PKG-06 deliverable-local surfaces for the
  DEL-06 side of ruling 3 and DEL-06-05 timeout ruling 6.
- **WI-PKG08:** only manifest-listed PKG-08 deliverable-local surfaces for the
  DEL-08 side of ruling 3, DEL-08-04 ruling 4, and ruling-5 no-op confirmation.

Every package remains read-only outside its accepted manifest slice. No
manager may edit another package, shared decision/register state, frontend
runtime source, loop receipts, completion log, decomposition truth, prior
concordance ledgers, or this plan.

## Validation and fan-in gates

Each package return must provide exact changed paths, claim-to-ruling mapping,
before/after contradiction disposition, checks, exclusions, lifecycle proof,
and blockers. Manager validation must include appropriate document/schema,
reference, dependency, authority-corpus, receipt-contract, scope, and diff
checks selected from the live profile. No frontend runtime suite is required
unless a package unexpectedly proposes frontend source; such a proposal is a
scope blocker, not permission to run or edit it.

V1 independently verifies:

- owner quote and chronology are transcribed without semantic drift;
- every edit is authorized by one of the eight rulings and the accepted R1B
  manifest;
- live CLM contradictions in scope are repaired;
- prior immutable ledgers are unchanged;
- the consolidated DEL-05/06/08 mapping is coherent and non-duplicative;
- DEL-08-04 points to D-GOV-14 item 7 and `delegate_agent`;
- the Pipeline and threshold items remain correctly no-op;
- timeout, PEC ownership, and adoption-verdict content match the ruling;
- no lifecycle state/Approval SHA, frontend runtime source, or hard-fence
  surface changed.

Only an accepted V1 return releases C1. C1 writes the minimal Receipt-75 and
landed-work entry in `plans/PLAN_COMPLETION_LOG.md`, updates run-local handoff
evidence, reruns the receipt validator, and then releases CHANGE-PUBLISH.

## Escalation and stop conditions

Stop the affected path and return to HELP_HUMAN for: a missing exact target,
overlapping package writes, semantic ambiguity outside the approved
chronology, a request to modify an immutable prior ledger, frontend runtime
need, lifecycle mutation, dependency-authority conflict, hard-fence contact,
or failed validation that cannot be repaired within the same exact manifest
slice. Consequential scope expansion requires a new human act.

## Handoff

After accepted C1, CHANGE-PUBLISH may create one coherent commit, push the
branch, and open a PR. The owner merge remains terminal. Neither this plan nor
any manager return constitutes merge, lifecycle acceptance, or release
approval.
