---
amendment_id: SCA-002
doc_kind: scope_change.propagation_plan
decomp_variant: SOFTWARE
gate: 4
created: 2026-07-29
status: awaiting_gate_4_approval
accepted_gate_3_candidate: Gate_3_Candidate/ (three exact surfaces; owner approval pending)
requested_by: Ryan Tufts (through the D-GOV-31 adoption ruling)
---

# SCA-002 Gate 4 — Propagation Plan

Gate 4 owner approval is **PENDING**.

## 1. Propagation boundary

SCA-002 restates two existing rows and records the amendment; it adds and
removes nothing. There is no child-remap closure set, no scaffold work, no
guard-baseline change, and no dependency, estimate, or schedule impact.
SCOPE_CHANGE's entire write claim is:

| Surface | Classification | Action |
|---|---|---|
| `execution/_ScopeChange/SCA-002_2026-07-29_0800/**` | snapshot / handoff artifact | Written by this drafting run |
| `execution/_ScopeChange/_LATEST.md` | snapshot pointer | Repointed to the active pending snapshot; accepted basis stated unchanged |
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | working surface | **Application-phase only**, after owner acceptance, by copying the exact approved candidate bytes |
| `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv` | authoritative companion register | **Application-phase only**, same discipline |
| `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv` | authoritative companion register | **Application-phase only**, same discipline |

**Nothing else.** In particular, this run and the later application act write
none of the POLICY_DELTA §4 rows 2–9 surfaces.

## 2. Application-phase copy discipline (after owner acceptance)

1. Verify the three authoritative surfaces still carry the basis SHA-256
   identities in `Pre_Change_Register_Baseline.json` (no unapproved
   intervening change).
2. Re-run `validate_gate3_candidate.py`; require PASS with the exact
   candidate hashes in `Gate_3_Validation.json`.
3. Copy the exact approved candidate bytes to the three authoritative paths;
   regenerate nothing.
4. Record per-file before/after SHA-256 in an `Applied_File_Hashes.json`.
5. Run the post-change deterministic register suite and an `AUDIT_DECOMP`
   post-change snapshot; present the applied state to the owner for the
   Gate 5 confirmation; hand off to CHANGE for human-gated Git closeout under
   the successor policy's standing default.

## 3. Downstream obligations owned by others — POLICY_DELTA §4 rows 2–9

Enumerated for coordination; **SCOPE_CHANGE claims none of these writes**.
Verbatim anchors were re-verified at the frozen basis.

| Row | Surface | Verified anchor(s) | Obligation | Owner |
|---|---|---|---|---|
| 2 | DEL-04-06 scope of work + context | `execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/DEL-04-06_Change_Management_and_Human_Gated_Closeout/ScopeOfWork.md` — REQ-001 at lines 62–66 plus occurrences at lines 20, 22, 38, 44, 56–58 (CLM-002), 77, 100; **and `_CONTEXT.md` lines 11 and 21** (added per the D-GOV-31 RB-1 disposition) | Reconcile requirement, output, and evidence definitions to the four-identity discipline and bounded-grant policy after the SCA-002 register text is accepted | Downstream contract owner (DEL-04-06 via WORKING_ITEMS) |
| 3 | Loop protocol closeout rule | `execution/_Coordination/LOOP_INIT.md` §7, line 126 ("use CHANGE for Git closeout; never self-merge.") | Amend to the successor default-plus-grant formulation, preferring the "local merge discipline remains controlling" wording (RB-5) | HELPS_HUMANS via a human-gated M2 tranche |
| 4 | Deterministic G4 check | `tools/validation/validate_instruction_tranche_manifest.py` self_merge must-be-false check, lines 304–308 | Extend semantics so a recorded bounded grant is representable without weakening the default; never silently delete the check; the tranche carries the mandatory pre-merge pin's registered home (a tranche-manifest grant-reference field) and restates the full deterministic-check suite (RB-3, RB-6) | HELPS_HUMANS via a human-gated tools tranche |
| 5 | G4 check test | `tools/validation/test_validate_instruction_tranche_manifest.py::test_block_on_self_merge`, lines 228–234 | Update in the same tranche as row 4, preserving a failing test for undeclared self-merge | Same tranche as row 4 |
| 6 | Tranche-manifest schema semantics | `instruction-tranche-manifest/v1`, `m2_gate.self_merge` | Define bounded-grant declaration (grant-reference field naming the durable grant record); `self_merge: false` remains the default; grants recorded strictly before exercise preferred, owner-authored when PR-carried (RB-2) | HELPS_HUMANS |
| 7 | Practitioner harness invariant map | `tools/practitioner_harness/harness_common.py` line 78 (`"K-MERGE-1": "RATIFIED"`) | Verify the mapping remains accurate under strengthened evidencing; no change expected absent a `docs/CONTRACT.md` §1.8 amendment | HELPS_HUMANS |
| 8 | Shared CHANGE instruction surface | `agents/AGENT_CHANGE.md` merge-execution and verification passages (lines 46, 73, 87, 100, 115, 134 at the D-GOV-31 basis) | Reconcile to the bounded-grant policy under the AGENTS.md agent-index change-notice rule, in a human-gated tranche | HELPS_HUMANS |
| 9 | M6 routed coordination notices | Each registered loop's coordination surface (at this basis: App, PEC, Piping) | One notice per loop in the same tranche that changes the shared surfaces; notices are coordination, never authority; stricter local discipline remains controlling until loop adoption | Agent 0 / HELPS_HUMANS (M6 disposition at fan-in) |

**Express non-obligations** (POLICY_DELTA §4, preserved by D-GOV-31 Effect 4):
SHA-pinned historical mirrors, frozen proposal and evidence packages,
`LOOP_RECEIPTS.md` receipts, and OD transcription records are not rewritten.
Historical statements of the old rule remain historical statements. Other
repository occurrences of the old phrase found by the drafting census
(workplans, decision packets, evaluation snapshots, project-loop surfaces,
`docs/governance_harness/**` records, `plans/**`, `_DomainEngines/**`,
`projects/**`) fall under these rows or the non-obligation and are touched by
no SCA act.

## 4. Downstream rerun advisory

| Rerun | Owner | When |
|---|---|---|
| Post-change `AUDIT_DECOMP` snapshot | EVALUATION / AUDIT_DECOMP via the applying workflow | Application phase, after copy |
| Deterministic register suite re-run | Applying workflow | Application phase |
| DEL-04-06 contract reconciliation (row 2) | WORKING_ITEMS route | After accepted application |
| CHANGE Git closeout | CHANGE (human-gated PR; standing default; no grant exists) | After Gate 5 confirmation |

## 5. Rollback

Before owner acceptance there is nothing to roll back: live decomposition
surfaces are untouched. If the owner declines, this snapshot remains
immutable declined-candidate evidence and `_LATEST.md` is repointed by the
declining act. After an accepted application, any reversal is a new
human-initiated SCOPE_CHANGE.

## 6. Gate 4 question (for the owner, at review)

Do you approve this propagation plan?
