## 10. Reading (hand-written by the PKG-01 manager; agent measurement, not a ruling)

- **Rule stage.** A and B received the same brief (`BRIEFS/WORKER_BRIEF.md`, carrying the Addendum 5 and
  Addendum 6 texts verbatim) in the same dispatch round. Their pass-2 messages were identical except for the
  folder and seal values, and both received the same 10 capability files (the union of both ledgers' areas).
  Neither worker received HELP_HUMAN's `OTHER:V3_ROLE_ADOPTION` note or the Addendum 6 rule-3 clarification
  before sealing: both had already sealed, so the stage was identical.
- **Disposition agreement 25/31 (81%)** on indexed base keys, against DEL-06-02's 19/35 (54%; before the
  Addendum 5 tie-break) and DEL-05-02's 24/33 (73%).
  - **No split falls between STALE_SPECIFICATION and REMAINING_STATE_MISMATCH.** Both workers agree on all 9
    keys where either used SS or RSM. The Addendum 5 tie-break appears to have closed the DEL-06-02 variance
    source for this deliverable.
  - **All 6 Disposition disagreements are about how much of the claim is met.**
    - A reads 4 as PARTIALLY_IMPLEMENTED or DOCUMENTED_UNIMPLEMENTED where B reads ALIGNED: CLM-004, CLM-017
      (no boundary review record for the shipped v3.0.x release), CLM-022, and the CLM-009 sub-rows.
    - On CLM-026 and CLM-029, A reads a CONTEXT_CLAIM (NOT_AUDITABLE) where B reads a REQUIREMENT (ALIGNED).
  - **CLM-009 sub-rows (REQ-01..10).** Both workers split them identically, but agree on the Disposition of
    only 2 of 10 sub-rows. A found missing live copy for REQ-01 (governed-work posture), REQ-04 (draft notice)
    and REQ-06 (runtime records are not approvals); B judged these ALIGNED.
- **A factual disagreement for R3 (reach, not interpretation).**
  - A's erratum on CLM-009.2 says the "Anthropic API Key" settings panel is reachable live, because the 404
    page (`not-found.tsx`) renders the legacy ShellFrame.
  - B's erratum on the same row says the panel is never rendered.
  - V-DEL-01-03_A CONFIRMED A's erratum, and B's ledger is not verified. The capability file
    (CAP-SETTINGS-009, STATE=DISABLED) misses the 404 path, according to A.
- **HumanDecisionNeeded 29/31.** R4 tokens agree on 0 of the 2 keys where either worker cited one.
  - On CLM-009, B adds R4-Q5 for the live "Codex" notification tab.
  - On CLM-024, A cites R4-Q1 and B cites plain R4. Both mark the row AUTHORITY_CONFLICT against the
    unamended DIRECTIVE §2.8.
  - On the run-local rows, both workers independently raised AUTHORITY_CONFLICT on `_CONTEXT.md` "Claude
    Agent SDK / Anthropic remains the current path" (A STATE-1, B STATE-2).
- **Metadata columns.** CauseTag 20/31 (65%). The main split is CARRIER_PROPAGATION (A) against PRE_V3_DRIFT
  (B) on the stale dependency and TBD text (CLM-008, 011, 012, 016, 019). That matches the R0 finding that cause precedence is
  weakly reproducible. ClaimType 24/31: B reads SoW state prose as STATE_ASSERTION where A reads it as
  REQUIREMENT.
- **Reverse Response agreement 438/452 (97%).** Where both workers answered PARTIAL, they named the same base
  key 9/9 times.
