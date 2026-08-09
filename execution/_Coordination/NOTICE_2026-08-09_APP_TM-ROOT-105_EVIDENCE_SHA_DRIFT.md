# App → Root: TM-ROOT-105 closure-evidence SHA drift routed for Root consideration

**To:** Root coordination / Root `TASK_MANAGEMENT`
**From:** chirality-app-dev `TASK_MANAGEMENT`, 2026-08-09
**Status:** ROUTED DELIVERY COPY — COORDINATION ONLY — NOT AUTHORITY

This file is the routed delivery copy, placed on Root's coordination surface,
of the App-authored notice
`projects/chirality-app-dev/execution/_Coordination/_TaskManagement/DRAFT_NOTICE_ROOT_TM-ROOT-105_EVIDENCE_SHA_DRIFT_2026-08-09.md`,
SHA-256
`3d9061b60f85903fdf3a8dca8dfa28870d20a5db35e093f888f28845162f3ada`.
That App-side file is the authoritative original; this copy exists so Root's
discovery sweeps find the notice on Root's own surface.

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
