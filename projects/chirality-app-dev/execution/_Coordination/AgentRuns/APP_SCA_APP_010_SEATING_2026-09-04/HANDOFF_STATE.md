# Handoff State — APP_SCA_APP_010_SEATING_2026-09-04

**Candidate:** branch `claude/sca-app-010-seating`, one unmerged PR against `main` (number recorded in the PR body and the receipt).
**Basis:** `787a551e70d9fb33f6f9a9fe228443d890a8d02d` (PR #712 merge).
**Authorization basis:** D-APP-108 (`execution/_Coordination/_DECISIONS/D-APP-108_RULING_SCA_APP_010_SEATING_AND_SHELL_QUESTIONS_2026-09-04.md`): owner adoption of the seating list as presented, seating of the outside items in the same pass, WORKING_ITEMS alignment in the same PR, eleven question rulings, and the Q8 routing authorization; on top of SCA-APP-010 G1-CONFIRM to G5-POINTER.
**Accepted upstream truth:** applied decomposition SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (PR #708 merge `7795b0972…`); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; `execution/_ScopeChange/_LATEST.md` SHA-256 `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` naming SCA-APP-010 (PR #711 merge `311a2f0b8…`); authority corpus v20, no drift.
**Closure verdict:** `CANDIDATE_PREPARED_AWAITING_OWNER_BYTE_REVIEW`. **ReadyForNextPhase:** `NO` until owner merge.

## Four-state form

| State | Value | Meaning |
|---|---|---|
| `ApplicationState` | `COMPLETE_ON_CANDIDATE_BRANCH` | Twenty Remaining items and two record-only history lines seated across seventeen carriers; Scope of Work re-pin with a SCA-APP-010 Gate-5 Current Contract section, `_CONTEXT.md`, `_REFERENCES.md`, history, and memory alignment for the thirteen carriers (WI-001 to WI-065); D-APP-108 ruling record and register row; Root notice routed (N-001); TM-001 vacuous (no register row carries the label). Built deterministically by `build_seating.py` from frozen pre-images with post-image parity. |
| `AuthorityState` | `SEATING_ONLY_NO_ACT_INFERRED` | D-APP-108 authorizes seating and alignment. Merge confers selectability only. No implementation, lifecycle, Checking Approval SHA, dependency-extraction, dependency-acceptance, product, host-mutation, signing, release, publication, reliance, or Root-acceptance act is inferred or performed. |
| `DerivativeState` | `CARRIER_SURFACES_CURRENT_DEPENDENCY_REGISTERS_STALE` | The thirteen carriers' working surfaces are current with the applied decomposition. Their `Dependencies.csv` and `_DEPENDENCIES.md` still predate the SOW-081 to SOW-084 and revised SOW-001/002/004/006/007/008/010 relations (DEP-001 to DEP-026 not run). SCA-APP-010's own derivative closure (`Handoff_State.md` `DerivativePackageState INCOMPLETE`) stays open; SCA-APP-009's stays open under its snapshot. |
| `NextGateState` | `OWNER_BYTE_REVIEW_THEN_MERGE` | The owner reviews and merges or rejects. After merge, `loop/LOOP_INIT.md` Step 1 may select DEL-02-02-V3-03, DEL-07-01-V3-01, and DEL-07-03-V3-01; every other seated item stays parked on its named gate. |

## Review

`REVIEW.md`: first pass PASS (BLOCKER 0, MAJOR 2, MINOR 4; all applied and
rebuilt from the same pre-images); second pass by a fresh reviewer instance
over the re-frozen zero-context diff (SHA-256
`66c0163c5b2f531674d130d5b9a2c4390d41046411e3f4679e06302f88e887b2`) PASS
(BLOCKER 0, MAJOR 0, MINOR 1 on run-packet wording, applied). All seventeen
carriers, the ruling record, the register row, the Root notice, and the run
packet PASS.

## Open owner gates and blockers (none lifted here)

- Owner byte review and merge of this candidate.
- Owner acceptance of the alignment (`OWNER_ACTION_MATRIX.csv` step 18 accepted), which triggers, in order: `TASK + dependency-extract` report-only preview over the thirteen carriers, then the reviewed write (DEP-001 to DEP-026; retire, never delete; any SCC edge or Root path proposed stops for a ruling); `AUDIT_DEP_CLOSURE — SCA-APP-010-GATE5-POST-APPLICATION`; RECONCILIATION no-drift and claim-level concordance; AUDIT_DECOMP fresh full audit with pre/post comparison; then the SCA-APP-010 `Handoff_State.md` derivative fields may be updated toward closure on the owner's disposition.
- Root returns that unpark App items, each as a routed `NOTICE_*` on the App coordination surface: DEL-02-09 shared-login contract (DEL-02-05-V3-03); DEL-02-10 acceptance of the additive `proposal.*` types (DEL-05-02-V3-02); DEL-02-11 stored delegation-policy field (persistence behind DEL-03-02-V3-01 and DEL-08-04-V3-02).
- Gate tightening, if the owner wants it, for the three items whose presented gate is looser than plan §7 (`MAPPING.md` §C); the technical dependency on DEL-02-03-V3-01 is recorded in their `Depends` lines.
- Owner write-scope grant for `agents/**` and `skills/**` at DEL-08-01-V3-01 selection.
- Standing: SCA-APP-009 derivative-closure disposition; D-APP-97 / F-APP-2 through preparation; the A1 re-stage rule for any `frontend/` mutation by a later selectable item.

## Rerun requirements

- Any later change to a carrier `ScopeOfWork.md` requires the SOW validator and, where dependency evidence changes, the registered dependency extraction plus the closure audit.
- Any authority-document edit requires the D-APP-38 `status → bump → apply → audit` workflow (not triggered here; no corpus member changed).
- If the owner amends any gate, item text, or ruling by reply, the change is a new dated history line in the carrier and a residual row citing D-APP-108, never an edit to this run's frozen evidence.

## Attribution

Prepared by Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) acting as HELP_HUMAN (Agent 0) in an untyped Claude Code session and, for the carrier writes, as WORKING_ITEMS' applicator under the owner's authorization; two bounded read-only Claude Code subagents acted as independent reviewers (one per pass). Role not mechanically enforced.
