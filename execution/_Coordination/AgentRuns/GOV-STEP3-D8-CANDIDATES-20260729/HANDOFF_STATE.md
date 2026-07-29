# Handoff — GOV-STEP3-D8-CANDIDATES-20260729

Status: `READY_FOR_OWNER_SELECTION`

## State

- `ClosureVerdict`: `CANDIDATES_AUTHORED_AWAITING_SELECTION`
- `DerivativePackage`: `NO` (proposal package; non-authoritative)
- `AuthoritativeEffect`: `NONE` (K-AUTH-1; live D-8 fully in force)
- `GlobalBlocker`: `NONE`

## Candidate identity

- Frozen candidate basis:
  `main@4f7808acb2802443370d045efa198152934c1674`
- Candidate branch: `gov/step3-d8-candidates`
- Package:
  `docs/governance_harness/_PROPOSALS/D-GOV-31_2026-07-29_merge_gate_policy_succession/`
- Candidate A (ROOT-ONLY) subject SHA-256:
  `d21a2d8d4bc2deb2a32dbe4936f1e4647efabac24158adeae4f45fa4a18d8d35`
  (`CANDIDATE_A_ROOT_ONLY/PRD_ROOT_REV7_CANDIDATE.md`)
- Candidate B (SHARED-CHANGE-POLICY) subject SHA-256:
  `15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748`
  (`CANDIDATE_B_SHARED_CHANGE/PRD_ROOT_REV7_CANDIDATE.md`)
- Decision record: none — created at adoption per the D-GOV-28
  precedent, together with the `_REGISTER.md` row.

## Closure posture

Authoring is complete and candidate-only. Both candidates carry the full
mandatory policy content (default unchanged; bounded recorded owner
grant; the execution-authority-is-not-semantic-approval key sentence;
four closeout identities; owner token grammar; express exclusions;
K-MERGE-1 unchanged with strengthened pre-merge evidencing) and differ in
exactly seven scope-bearing lines. No selection, adoption, PRD edit,
register row, receipt, grant, or notice routing is contained. This
package binds nothing and is not a substitute for decomposition truth or
live governed state.

## Pipeline position and remaining blockers

Per the approved program plan (prepare both → commit/hash both
candidate-only → owner selects one without adoption → HZN-GOV-01 rerun
against the selected committed candidate → resolve findings → owner
adopts → publish through human merge):

1. Owner session: `SELECT` one committed candidate against the packet's
   pre-fixed identities. Selection is not adoption.
2. HZN-GOV-01 rerun against the selected committed candidate, per
   `execution/_Evaluation/CHIRALITY_PROGRAM_POST_REMEDIATION_HORIZON_2026-07-28_85EA0628/HANDOFF.md`
   §Rerun; resolve findings.
3. Owner adoption: create the D-GOV-31 decision record bound to the
   exact candidate SHA, with the `_REGISTER.md` row; fill the manifest
   authorization with the owner's verbatim ruling if the owner supplies
   one; apply the adopted bytes through the required M2/CHANGE closeout.
4. Publication: human-gated PR merge under the still-current D-8; the
   successor never consumes its own not-yet-effective merge exception.
5. Step-4 propagation by the owners enumerated in the selected
   candidate's `POLICY_DELTA.md` §4 (7 obligations for A; 9 for B,
   including shared CHANGE surfaces and routed M6 notices). SHA-pinned
   historical mirrors and receipts are expressly not rewritten.
6. M6 notice disposition (`pending`) at Agent 0 fan-in.

## Owner selection (2026-07-29, in-session)

The owner returned, verbatim:

> SELECT CANDIDATE-B — Ryan Tufts 2026-07-29

Effect: Candidate B (shared-CHANGE scope; subject SHA-256
`15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748`, committed
candidate-only at `3ad43c27b`) is selected for the HZN-GOV-01 governance rerun
per PACKET §6. Selection is not adoption: no PRD amendment, no D-GOV-31
record, no register row, no publication occurs by this act. Candidate A
remains immutable candidate history. Adoption remains a separate future owner
act after horizon findings are resolved.

## HZN-GOV-01 rerun (2026-07-29)

Verdict: **ADOPTION_CLEAR_WITH_NOTES** — no blocking finding. The rerun
ran against the exact committed Candidate B (subject SHA-256
`15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748` at
candidate commit `3ad43c27b`), pre-adoption, per PACKET §6 and the
horizon package's §Rerun procedure. The full return lives in the Agent 0
session record.

Summary: prior findings HZN-GOV-001, HZN-GOV-003, HZN-GOV-004,
HZN-GOV-005, HZN-GOV-006, and HZN-GOV-007 are RESOLVED; HZN-GOV-002 is
partially resolved with a nonblocking residual (RB-1). New notes
RB-1..RB-8 are all nonblocking, with recorded dispositions: RB-1's
definitional residual is cured in the D-GOV-31 record (same-actor grants
permitted; "self-merge" working definition) and its census gap
(`DEL-04-06/_CONTEXT.md` lines 11, 21) becomes a Step-4 row-2 surface
addition; RB-2 and RB-5 become Step-4 drafting preferences (grants
strictly before exercise, owner-authored when PR-carried; "local merge
discipline remains controlling" wording); RB-3 and RB-6 become Step-4
obligations (tranche-manifest grant-reference field as the pre-merge
pin's registered home; full deterministic-check suite restated in the
rows-4–6 tools tranche); RB-4 is cured by the adoption token carrying
the subject SHA8; RB-7 confirmed no retroactive-legitimization pathway;
RB-8 (§3 intent-quote verbatim status) resolved by owner
confirmation-by-non-objection at adoption, recorded in the D-GOV-31
decision record.

## Owner adoption (2026-07-29, in-session)

The owner returned, verbatim:

<!-- BEGIN OWNER RULING VERBATIM -->
APPROVE D-GOV-31 15fba9c3 — Ryan Tufts 2026-07-29
<!-- END OWNER RULING VERBATIM -->

Effect: Candidate B is adopted. The D-GOV-31 decision record
(`docs/governance_harness/_DECISIONS/D-GOV-31_merge_gate_policy_succession.md`)
is created, bound to the exact candidate SHA, with the `_REGISTER.md`
row; the adopted bytes are applied to `docs/PRD_ROOT.md` (Rev 7);
publication rides this PR under the still-current D-8 — the successor
never consumes its own not-yet-effective merge exception.

Remaining: owner approval of the final branch HEAD, then the
owner-executed merge; `CandidateMergeSHA`, `PublicationSHA`, and
`EffectiveSHA` are backfilled after, per the D-GOV-18/19/21/22
convention.
