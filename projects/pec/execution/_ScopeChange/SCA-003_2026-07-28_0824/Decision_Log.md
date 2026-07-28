---
amendment_id: SCA-003
doc_kind: scope_change.decision_log
decomp_variant: SOFTWARE
gate: 5
created: 2026-07-28
status: owner_ruled
---

# SCA-003 — Decision Log

## Standing owner ruling

> "Finish out your plan now (attaining your goal) with self merge of PRs and
> auto approve for owners rulings, which should still be recorded in the usual
> manner with your recommendation standing as what I approved."

| Decision | Gate | Agent 0 / SCOPE_CHANGE recommendation | Owner-approved disposition |
|---|---:|---|---|
| SCA003-G1 | 1 | Open a narrow `MODIFY`-only amendment on PRD v2.2; preserve topology and all exclusions | `APPROVED` under standing ruling |
| SCA003-G2 | 2 | Accept the bounded impact assessment; derivative consumers remain frozen | `APPROVED` under standing ruling |
| SCA003-G3 | 3 | Approve the exact revision-1.3 semantic postimage and DEL-10-12 label/path preservation | `APPROVED` under standing ruling |
| SCA003-G4 | 4 | Apply only decomposition truth, three exact contexts, SCA/audit evidence and pointers | `APPROVED` under standing ruling |
| SCA003-G5 | 5 | Accept revision 1.3 as `current_basis`; close `CLOSED_FOR_SCOPE_CHANGE_ONLY / REGEN_ONLY` | `APPROVED` under standing ruling |

## Gate 5 recommendation and owner-approved selection

**Recommendation:** accept revision 1.3 as the current decomposition basis,
record `NON_BLOCKING_PASS`, preserve the active reliance hold and all
excluded surfaces, and close SCA-003
`CLOSED_FOR_SCOPE_CHANGE_ONLY / REGEN_ONLY`.

**Owner-approved selection under the standing direction:** approve the
recommendation exactly.

Git publication is handled through CHANGE. The authorized workflow stops
before merge after opening the PR and observing green required checks.
