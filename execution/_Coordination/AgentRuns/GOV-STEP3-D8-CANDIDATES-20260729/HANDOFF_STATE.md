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
