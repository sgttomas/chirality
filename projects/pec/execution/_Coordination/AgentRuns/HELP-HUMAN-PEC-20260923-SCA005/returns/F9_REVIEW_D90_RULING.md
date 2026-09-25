# Return F9 — independent review of the D-PEC-90 ruling record (PR #899)

Reviewer: fresh read-only TASK (`pec-reviewer`, `model: opus`; host-reported `claude-opus-5-5`), dispatched by HELP_HUMAN. HELP_HUMAN transcription, condensed.

## Review of head `6db0520e99f8731fdf182a205b183862ff37aef7` (base `088fb7868d3246361e7209dd9276c6b0f8fc75d9`)

**Verdict: PASS, no blocking findings.** Verified: proposal SHA-256 `b04a8aa2…a5e147`; both owner lines quoted exactly everywhere; grants limited to the NOTE, two non-binding notices and later preparation; direct query recorded as later §8 direction with no access-class change; the ruling-on-summary disclosed (the draft-bytes-at-ruling claim rests on HELP_HUMAN's statement); all proposal loci and basis hashes match their sources; the L-A1 distinction is correct; no PRD, `AGENTS.md`, SOW, SPEC, `v2/**`, decomposition or `_STATUS.md` byte changed; Decision_Log additive and its hash matches Handoff_State; notice paths follow owner-ruled precedent (D-PEC-67 `d9225bbda`, D-PEC-73) and are covered by R-A; Receipt 187 VALID and append-only; `git diff --check` and decomposition `--strict` exit 0.

| # | Finding | Disposition |
|---|---|---|
| N1 | Proposal cites "§16 item 6" for access classes; access classes are §8, item 6 is auth reuse | Clarification added to the ruling record (proposal bytes unchanged) |
| N2 | "P1 has the store and guard only" understates `v2/` contents | Clarification added to the ruling record |
| N3 | Root notice did not raise Root PRD N-1's "does not exist for purposes of reliance" clause | Root notice now asks Root to confirm the N-1 reading too |
| N4 | Notices said PEC "will" amend; the amendment needs its own owner act | Reworded to "plans to" / "is planned to … needs its own owner act" |
| N5 | NOTE row should say checkpoint 2 still quotes in-force v2.2 | NOTE row clarified; `Decision_Log.md` hash updated in Handoff_State |
| N6 | F9 transcription must exist before merge | This file |
| N7 | STATUS/README omit "reliance begins at a release, not now" | Added to both |

## Final-head confirmation of `44a879bd9d0f260461dd551191ef93dea0b24ec8`

Same reviewer, re-reviewing the repair commit `6db0520e9..44a879bd9`. **Verdict: PASS, no blocking findings.** N1–N7 repairs match their findings and sources; proposal bytes unchanged (`b04a8aa2…`); `Decision_Log.md` SHA-256 `d8aced8d7cf196401525dd2ed5db0ad315ca042e0772d716bf453f949d1b8a11` matches both Handoff_State occurrences and the old value appears nowhere; the clarifications correct citations only and leave Grant and Limits byte-unchanged; this transcription is fair; validators pass. Non-blocking: the N5 sentence in row SCA005-D90-NOTE ("Checkpoint 2 still quotes the in-force PRD v2.2 … not diverge from the in-force text.") is HELP_HUMAN's clarification from F9 N5, not owner wording, although the row's status is `DIRECTED BY OWNER`. HELP_HUMAN records that provenance here rather than editing `Decision_Log.md` again. This section is added append-only after that head; no other byte changes.
