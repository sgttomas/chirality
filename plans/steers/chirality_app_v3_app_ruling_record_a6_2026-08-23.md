# APP RULING RECORD A6 — post-ratification concordance resolutions — owner rulings of 2026-08-23

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: resolutions that follow the ratification of Root's K-CONTROL-1 design amendment (PR #657, main `a252502af5180290a0a50a128b414d5a3bd27bb5`, ratified Root contract SHA-256 `ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83`). Target workspace: App-dev loop. Supersedes nothing; the loop's instruments govern. Companion instruments: records A4 (SHA-256 `14db687762b9af099debbfe9cfcaab0879e7082922f6eda9897b3f4d61ff330d`) and A5 (SHA-256 `1896d89200c4cd390b4606aed0229fe03bf7c5070f454e1dca5d6c6acde2bb9b`); the App Phase-2 return (Receipt 197, merged as PR #656, main `699b3eae0829c8306dee9bcd2035ecb6dcf11260`).

Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session minder chat on
2026-08-23. "[click]" marks the option the owner selected.

Concordance context for both rulings: HELP_HUMAN's post-ratification check
found the approved Gate-3 C-01 (K-CONTROL-1) candidate concordant with the
ratified Root row on topology (two purpose-limited sockets, supervisor
socket never renderer- or CLI-callable, `0700`/`0600`, no third socket, no
TCP, stale recovery) and divergent on two points: the candidate asserts
present-tense two-socket operation ("uses exactly two", "two-listener
inventory") where ratified Root truth states the supervisor socket is
accepted design not yet implemented with exactly one control socket live
today; and the candidate places the sockets beneath "app-owned" runtime
directories where Root K-RUNTIME-1 makes the Root daemon the exclusive
runtime owner.

A6-A — C-01 resolution: [click] "Authorize Phase 2b".
  The owner authorizes a bounded App Phase 2b under a separate
  owner-carried steer, per step 6 of the approved concordance workplan:
  regenerate the exact K-CONTROL-1 contract-row candidate aligned to the
  ratified Root row — design-honest tense (one control socket live today;
  the supervisor socket activates only through the separately gated
  DEL-02-07/WP-03 implementation pathway), Root-consistent ownership
  wording, design-gated supervisor-socket and two-listener verification —
  while preserving the candidate's App-side enforcement strengthenings;
  recompute the resolved full-contract candidate; rebuild the companion
  invariant-coverage register candidate; and return everything under fresh
  independent review, closing `AWAITING_OWNER_APPROVAL`. It applies
  nothing.

A6-B — K-EVENT-4 Root-binding staleness: [click] "Re-pin in Phase 2b".
  The Phase-2 K-EVENT-4 candidate binds the Root contract at its
  pre-amendment identity `ed87eaff4e936bb76f94e1bf3018f708c54c23167e6b4884a7f17193c9dcf679`,
  which the ratification moved to `ad0a4e6a…` above. HELP_HUMAN verified
  the two files differ at exactly line 162 (the K-CONTROL-1 row); the
  K-RUNTIME-1 (line 161) and K-STORE-2 (line 164) rows the A4-A selection
  cites are byte-identical. The owner directs that Phase 2b re-pin the
  K-EVENT-4 candidate's Root-contract binding to the ratified identity as
  a re-grounding only: the resolved K-EVENT-4 row post-image bytes must
  remain byte-identical to the Phase-2 resolved row (SHA-256
  `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93`).
  No carry-forward caveat remains once the re-pin lands.

Not ruled here: the exact regenerated candidate bytes (returned for their
own owner approval); C-03 notice routing; Gate 5 and any pointer move;
Root schedule-basis transcription; TM-ROOT-106/122 and every held binding;
C1; any implementation, activation, release, publication, or reliance act.
