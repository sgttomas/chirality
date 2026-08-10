# Owner direction — Root evidence-pin class closure

Date: 2026-08-09

Status: `ACCOUNTABLE-HUMAN DIRECTION AND CONDITIONAL RULING — VERBATIM TRANSCRIPTION`

The fenced block below preserves the owner's direction exactly. Text outside
the block is custodial metadata and does not extend the ruling.

<!-- VERBATIM_OWNER_DIRECTION_BEGIN -->
```text
Owner direction, 2026-08-09 — owner-sourced finding and ruling, arriving
after the accepted Step 2 harvest. Slot this per your pass protocol (as a
bounded addition to this pass's tranche or an immediately following bounded
invocation — your instruments choose), but do not retroactively amend the
accepted harvest report; this finding is owner-sourced, not a harvest
product.

FINDING (verify independently before acting; fail closed on any mismatch):
Archived rows TM-ROOT-109 and TM-ROOT-121 pin EvidenceSha
66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06 on the
same EvidenceRef as TM-ROOT-105:
execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/OWNER_RULING_TRANSCRIPT_2026-08-03.md.
All three rows were closed 2026-08-03 in the same batch (Receipt 92) citing
that transcript. Commit 2b6d53027 (the candidate-whitespace normalization)
drifted the file to
9b6d0a17ac73c4494541f1fb323760c03148d8978802b593c4f7d4b09ad0874a.
The 2026-08-09 Option-A ruling re-pinned only TM-ROOT-105; rows 109 and 121
still carry the stale pin.

RULING, conditional on your independent reproduction of the above:
Apply the identical Option-A mechanical repair to TM-ROOT-109 and
TM-ROOT-121 — retain each row's EvidenceRef, Disposition, Closed date, and
EvidenceQuote; change only EvidenceSha to 9b6d0a17…874a; append to each
row's Notes the same both-hash and commit provenance (closure-time
66b96700…bb06 at ba4678ca; post-closure normalization 2b6d53027; current
9b6d0a17…874a), citing the 2026-08-09 Option-A precedent
(OWNER_RULING_2026-08-09_ROOT_GOVERNANCE_CURRENTNESS.md) and this
direction. No closure meaning changes; this is not a re-close.

CLASS CLOSURE, same tranche: run the class-complete check the instance
repairs skipped — for every live and archived Root row with a
64-hex EvidenceSha and a path-resolvable EvidenceRef, verify the pin
against current committed bytes. Report the sweep result in the tranche
evidence. (Owner's own sweep predicts exactly two mismatches — 109 and
121 — with composite "path row X" refs and living-register pins excluded
as unpinnable by this method; if your sweep finds more, stop and return
the delta to me before repairing anything beyond 109/121.)

CANDIDATE, for preparation only: the register validator passed both
registers with these stale pins present — evidence-pin currency is
unvalidated. Prepare an owner-sourced candidate recording this gap, with
its disposition options (new row, or fold into the TM-ROOT-113/115
validator-quality genus at the owner gate). Present it with your next
slate; do not promote or dispose without my ruling.

Constraints: no other register bytes change; validators before and after;
receipt and handoff updates per your pass discipline; everything lands by
PR at my merge gate.
```
<!-- VERBATIM_OWNER_DIRECTION_END -->
