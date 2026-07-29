# SCA-002 Handoff State

Status: `OPEN_CANDIDATE_AWAITING_OWNER_GATES`

| Field | Value |
|---|---|
| AmendmentID | `SCA-002` |
| DecompositionTruthState | `INCOMPLETE` — **no live decomposition surface was modified**; the amendment exists only as candidate bytes inside this snapshot |
| DerivativePackageState | `INCOMPLETE` — POLICY_DELTA §4 rows 2–9 are enumerated, unstarted, and owned by others |
| ContentRemediationState | `NOT_REQUIRED` |
| DownstreamRerunState | `FROZEN` — nothing reruns until owner acceptance and application |
| MetadataAlignmentState | `NOT_REQUIRED` |
| AuditState | `NOT_RUN` — AUDIT_DECOMP pre/post pair is an application-phase obligation; deterministic drafting checks pass (37/37) |
| ReadyForNextPhase | `NO` |
| ClosureVerdict | `OPEN_PENDING_OWNER_DECISION` — not closed; not applied |

## What this run did and did not do

**Did:** drafted the SCA-002 candidate (three exact surfaces under
`Gate_3_Candidate/` + `Gate_3_Exact_Amendment.diff`), the Gate 1–4 decision
artifacts, deterministic validation (`Gate_3_Validation.json`, 37/37 PASS),
the pre-change register baseline, the header-only cumulative supersession
map, and this handoff. Repointed `execution/_ScopeChange/_LATEST.md` to this
snapshot as the active working snapshot.

**Did not:** modify any file under `execution/_Decomposition/`, the live
SOFTWARE_DECOMP working surface, DEL-04-06's working folder, `LOOP_INIT.md`,
any validator, any agent instruction surface, any frozen package or receipt,
or any project-loop surface. Issued no grant. Claimed no owner acceptance.
Pushed nothing; merged nothing.

## Exact next step (owner)

The owner reviews this package and rules on Gates 1–4 (intake, impact, exact
amendment, propagation plan). **Only after those confirmations** does a later
gated act apply the exact approved candidate bytes to the three authoritative
paths (copy discipline in `Propagation_Plan.md` §2), run the post-change
validations and AUDIT_DECOMP, obtain the Gate 5 confirmation, and hand off to
CHANGE for human-gated Git closeout. Application before acceptance is
prohibited by this package's own terms.

## `_LATEST.md` disposition

`_LATEST.md` is a stateful pointer, not a plain one-line pointer. It was
repointed to this snapshot because the SCA-001 precedent (Decision_Log
manager determination 8) shows the pointer names the active working snapshot
even while incomplete, and because AGENT_SCOPE_CHANGE requires it to point at
exactly one active snapshot. The rewritten pointer states explicitly that
revision 1.1 remains the accepted decomposition basis, that SCA-002 is
pending owner decision, and that SCA-001 remains the last closed amendment —
so the pending posture cannot be misread as acceptance.

## Flagged owner decisions carried out of drafting

1. SOW-042 `SourceRef` bracket: candidate retains `[TRANSCRIBED]` per the
   drafting brief; the live D-8 row is PROPOSED (Rev 7). Owner may keep or
   amend the bracket at acceptance (`Impact_Assessment.md`, flagged item 1).
2. AUDIT_DECOMP pre/post pair deferred to the application phase (this bounded
   drafting run has no delegation).

## Blockers

None for the owner decision itself. Application is blocked on: (1) owner
rulings on Gates 1–4; (2) basis-integrity re-verification at application
time; (3) the post-change validation and audit suite; (4) Gate 5
confirmation; (5) CHANGE human-gated Git closeout under the successor
policy's standing default (no grant exists).

## Next owning workflows

Owner (gates) → SCOPE_CHANGE application act (post-acceptance) → CHANGE (Git
closeout) → WORKING_ITEMS route (POLICY_DELTA §4 row 2) and HELPS_HUMANS /
Agent 0 (rows 3–9), each under its own instruments.

---

## Application append — 2026-07-29 (run GOV-STEP4-APPLICATION-20260729)

Status: `APPLIED_AWAITING_GIT_CLOSEOUT`

Everything above this line is the frozen drafting-time handoff and is
unedited. The owner accepted SCA-002 on 2026-07-29
(`ACCEPT SCA-002 271d456a`, verbatim with byte/hash identity in
`Decision_Log.md`'s application append) and ruled the SOW-042 `SourceRef`
bracket delta (`BRACKET AS RECOMMENDED …`, same append). This tranche applied
the amendment.

| Field | Value |
|---|---|
| DecompositionTruthState | `ACCEPTED_AND_APPLIED` — revision 1.2 applied to the three authoritative paths at basis `main@204321467b567ede862636a36dd67bcac1ff326a`; working surface and deliverable register byte-identical to the accepted candidate; ledger carries exactly the one owner-ruled bracket delta (`Applied_File_Hashes.json`) |
| DerivativePackageState | `CURRENT_FOR_ROW_1` — POLICY_DELTA §4 rows 2–9 were performed by the sibling tranche merged as PR #418 (`204321467…`); the public export under `exports/chirality-app/` remains a stale derivative deferred to the next export release (unchanged posture) |
| ContentRemediationState | `NOT_REQUIRED` |
| DownstreamRerunState | `NONE_PENDING` — no dependency, estimate, schedule, or scaffold rerun attaches to this restatement |
| AuditState | `DISPOSITIONED_DETERMINISTIC` — the AUDIT_DECOMP pre/post pair obligation is dispositioned: the deterministic application validation (`Gate_5_Validation.json`, 33/33 PASS) plus `Pre_Change_Register_Baseline.json` stand in for it; any full AUDIT_DECOMP run is deferred to the next regular audit cycle |
| ReadyForNextPhase | `YES_AFTER_GIT_CLOSEOUT` |
| ClosureVerdict | `CLOSED_FOR_SCOPE_CHANGE_ONLY_PENDING_GIT_CLOSEOUT` — scope-change work is complete; publication of the applied bytes is a human-gated PR whose merge authorization is a separate owner act on the exact final branch HEAD |

### Remaining obligations

- **Row 1 (this amendment):** none beyond (a) the human-gated Git closeout of
  this tranche and (b) a one-line `execution/_ScopeChange/_LATEST.md` pointer
  refresh to the applied state — the pointer still reads
  `OPEN_CANDIDATE_AWAITING_OWNER_GATES` and sits outside this run's sealed
  write scope; the next SCOPE_CHANGE-owned act (or the closeout tranche that
  owns the pointer) updates it. Nothing in the stale pointer overrides this
  append or the applied surfaces.
- **Rows 2–9:** done — performed by the sibling tranche merged as PR #418
  (effective merge `204321467b567ede862636a36dd67bcac1ff326a`), including the
  DEL-04-06 contract-surface reconciliation whose acceptance dependency on
  SCA-002 is now satisfied by the owner acceptance recorded here.
- **Audit pair:** dispositioned as recorded in `AuditState` above.

### Next owning workflows

CHANGE-equivalent human-gated Git closeout of this tranche (merge
authorization = a separate owner act on the exact final branch HEAD) →
next SCOPE_CHANGE-owned act refreshes `_LATEST.md`.
