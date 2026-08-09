# Draft Coordination Notice to Root — TM-ROOT-105 Evidence SHA Drift

Status: `DRAFT — AUTHORIZED TO SHIP ONLY IN APP TASK-MANAGEMENT CLOSEOUT`

Date: `2026-08-09`

From: chirality-app-dev `TASK_MANAGEMENT`

To: Root coordination / Root `TASK_MANAGEMENT`

Authority: owner ruling recorded in
`OWNER_RULING_2026-08-09_GEN_PASS_DEFERRAL.md`, SHA-256
`a02f95da6307579629c0ffe7c964acfe7bfed3bdaaf062aca830e73b39a255b7`.

Detecting instrument:
`DEFERRAL_CLASSIFICATION_REPORT_2026-08-09_GEN_PASS.md`, SHA-256
`5eabd3b3c93364b521370f26b09e454c9590663601eb453f5f88e1952106bccd`.

## Observation

Root archive row `TM-ROOT-105` in
`execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv` cites:

- `EvidenceRef`:
  `execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/OWNER_RULING_TRANSCRIPT_2026-08-03.md`
- pinned `EvidenceSha`:
  `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`
- disposition: `RESOLVED_BY_DECISION`
- closed: `2026-08-03`

The current committed bytes at that exact `EvidenceRef` hash to:
`9b6d0a17ac73c4494541f1fb323760c03148d8978802b593c4f7d4b09ad0874a`.

The App deferral review detected this mismatch while evaluating
`TM-APP-027` and `TM-APP-028`. It did not use the changed bytes to infer a
trigger, closure, or disposition. Both App rows remain `DEFERRED` under
owner-ruled prospective triggers.

## Requested Root-side consideration

Please evaluate the closure-evidence mismatch under Root's own instruments
and cadence. This notice is coordination only: it directs no Root register
write, supplies no replacement evidence identity, and grants no authority to
alter, re-close, or reinterpret `TM-ROOT-105`.

## Reciprocal citation contract

If Root later records or routes a response, cite this notice by its final
closeout SHA-256 and name `TM-ROOT-105`. The App closeout record will bind the
final notice SHA and the owner-ruling SHA above. No receiving-row creation is
requested or implied.
