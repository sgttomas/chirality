---
amendment_id: SCA-002
doc_kind: scope_change.brief
decomp_variant: SOFTWARE
gate: 1
created: 2026-07-29
status: CANDIDATE_DRAFTED_ALL_OWNER_GATES_PENDING
accepted_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md revision 1.1
frozen_git_basis: main@ea3db3607fbcbb7ce5f65bab31268a7eca431adb
requested_by: Ryan Tufts (through the D-GOV-31 adoption ruling)
upstream_authority: D-GOV-31; Root PRD Revision 7 (D-8 successor row + annex §5.3.1)
drafting_run: GOV-STEP4-SCA-20260729 (bounded Agent 2 AUTHOR under HELP_HUMAN, SCOPE_CHANGE lane)
---

# SCA-002 — SOW-042 / DEL-04-06 Restatement to the D-GOV-31 Successor Merge-Gate Policy

## Posture

**This is a candidate-only package.** No live file under
`execution/_Decomposition/` and no live SOFTWARE_DECOMP working surface is
modified by this run. The amendment exists only as candidate copies under
`Gate_3_Candidate/` plus `Gate_3_Exact_Amendment.diff`. Application is a
later, separately gated act that occurs only after owner acceptance. The
owner has NOT accepted this amendment; all five SCOPE_CHANGE owner gates are
pending.

## Human-initiated request (authority chain)

The owner adopted D-GOV-31 Candidate B in session on 2026-07-29. The ruling,
recorded verbatim in
`docs/governance_harness/_DECISIONS/D-GOV-31_merge_gate_policy_succession.md`:

> APPROVE D-GOV-31 15fba9c3 — Ryan Tufts 2026-07-29

The adopted subject is PRD Revision 7 (SHA-256
`15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748`),
published and effective at merge `ea3db3607fbcbb7ce5f65bab31268a7eca431adb`.
Its Effects §4 enumerates the nine POLICY_DELTA §4 Step-4 propagation
obligations; row 1 obligates SCOPE_CHANGE to restate the root scope-ledger
row SOW-042 from "never self-merge" to the successor policy, preserving the
stable ID and D-8 traceability. This SCA drafts that amendment (and the
directly paired DEL-04-06 register-row reconciliation) as a candidate for
owner decision. Adoption of D-GOV-31 authorized the drafting; it did not
pre-approve any SCOPE_CHANGE gate.

## Resolved current basis

| Field | Resolved value |
|---|---|
| Accepted decomposition | `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` |
| Decomposition revision | v1.1 (SCA-001 successor; owner-confirmed 2026-07-26; Git effect PR #366 merge `2db2c7128c32d32d197ae47660eb34ab2cef9660`) |
| Frozen working-tree basis | `ea3db3607fbcbb7ce5f65bab31268a7eca431adb` (the D-GOV-31 effective merge) |
| Current adopted PRD | `docs/PRD_ROOT.md` Revision 7 |
| Current PRD SHA-256 | `15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748` |
| Policy authority | D-GOV-31 record + PRD D-8 row (line 462) + annex §5.3.1 |
| Scope-change root | `execution/_ScopeChange/` |
| Next available amendment ID | `SCA-002` |
| Allow renumbering | `false` |

Basis integrity is evidenced in `Pre_Change_Register_Baseline.json`: the
three touched surfaces carry exactly the SCA-001 applied v1.1 SHA-256
identities; no unapproved intervening change exists.

## Semantic section binding

Identical to SCA-001, resolved by heading text:

| Semantic section | Bound heading / surface |
|---|---|
| Change Register | `## 13. Decision Log / Change Log` in the working surface |
| Unit Ledger | `## 10. Scope Ledger`; rows in `chirality_root_scope_ledger_v1_0.csv` |
| Objectives | `## 7. Objectives`; `chirality_root_objective_register_v1_0.csv` |
| Primary Partitions | `## 8. Packages` |
| Secondary Entities | `## 9. Deliverables`; rows in `chirality_root_deliverable_register_v1_0.csv` |
| Coverage Basis | `## 11. Coverage and Telemetry` + forward/reverse registers |

## Old-text census (drafting evidence)

`grep -rn "self-merge" execution/_Decomposition/` at the frozen basis returns
exactly two hits, both in scope for this SCA:

| Location | Text | Disposition |
|---|---|---|
| `chirality_root_scope_ledger_v1_0.csv` line 43 (SOW-042) | "…human-gated pull requests and never self-merge." | **IN SCOPE** — restated by this candidate |
| `chirality_root_deliverable_register_v1_0.csv` line 27 (DEL-04-06) | "…human-gated pull requests and no self-merge." + "no-self-merge evidence" | **IN SCOPE** — reconciled by this candidate |

Variants "self merge" / "selfmerge" return zero hits in
`execution/_Decomposition/`. The decomposition working-surface files covered
by SCA-001's Gate_3_Candidate set (`Chirality_Root_SOFTWARE_DECOMP_v1_0.md`,
`chirality_root_objective_register_v1_0.csv`,
`chirality_root_prd_coverage_forward_v1_0.csv`,
`chirality_root_trace_reverse_v1_0.csv`,
`chirality_root_coverage_telemetry_v1_0.md`) reference SOW-042 / DEL-04-06 /
D-8 by stable ID only and never restate the obligation text; they need no
old-text edit. The working surface is nonetheless touched for
change-register, revision-metadata, and source-pin traceability required by
the SCOPE_CHANGE protocol (Gate 3 change-register rule) — see
`Amendment_Preview.md`.

Old-text occurrences outside `execution/_Decomposition/` (DEL-04-06
`ScopeOfWork.md` and `_CONTEXT.md`, `execution/_Coordination/LOOP_INIT.md`,
validator/tooling surfaces, agent instruction surfaces, and frozen historical
records) are **other-owner work or express non-obligations** enumerated in
`Propagation_Plan.md`. This SCA touches none of them.

## Parsed actions

See `Parsed_Actions.csv`. All actions are `MODIFY`; no entity is added,
removed, retired, reclassified, merged, or split; no parent-closure set is
triggered; every stable ID is preserved.
