# SEALED CHALLENGE BRIEF — Reviewer B challenges Reviewer A's frozen report

Charter protocol step 5 (reciprocal challenge). Your own pass-1 report is
frozen (`REVIEWER_B_REPORT.md`, sha256 `5c20315e9ad7…`) and MUST NOT be
edited, appended to, or rewritten — challenge marks live in a new file only.

## Input

- The other reviewer's frozen report:
  `/Users/ryan/dev/chirality-tandem-review-2026-07-26/REVIEWER_A_REPORT.md`
  Verify sha256 = `ee39da9fc11d9e56d9c7db8ab5bd458252519a1acd66e8504ec9c52fe650ee3e`
  before relying on it; if it does not match, stop and report.
- Evidence basis: the same frozen corpus,
  `/Users/ryan/dev/chirality-review-frozen-da31c19` @ `da31c19b5…` — the only
  admissible evidence source. Never read `/Users/ryan/dev/chirality`.
- Reviewer A's report contains findings RA-001…RA-018 (1 BLOCK, 7 REVIEW,
  7 WARN, 3 INFO), matrices, and a fan-in summary.

## Task

For **every** BLOCK and REVIEW finding in A's report (RA-001…RA-008 by
severity ordering — identify them from the report itself, do not trust this
brief's arithmetic), and for a **recorded sample of at least three** of the
WARN/INFO findings (state which you sampled and why), mark exactly one
verdict:

- **CONFIRM** — the assertion is correct and the evidence supports it; you
  independently re-verified the load-bearing evidence at the frozen corpus.
- **REFUTE** — the assertion is wrong, or the evidence does not establish
  it; give the disproving evidence.
- **NARROW** — partially correct; state precisely which part survives and
  which does not, with evidence for the boundary.
- **ADD-MISSING-EVIDENCE** — the assertion stands but needs evidence the
  report lacks (or is materially strengthened/complicated by evidence it
  missed); supply that evidence.

Rules:
1. Re-verify at the corpus; do not accept A's citations on faith and do not
   rely on your own pass-1 memory without re-checking the file.
2. Judge A's severity and class too: if a verdict is CONFIRM but you judge
   the severity wrong, say so under the verdict (this is challenge
   commentary, not a new finding).
3. You may not mint new findings in this stage. Genuinely new material goes
   in a final short section "Out-of-scope observations for fan-in" (no IDs,
   no severities — the manager dispositions them).
4. Where A's finding overlaps ground your own report covered, still verify
   A's specific assertion as written — the claim under test is A's, not
   yours.
5. Assertion-status discipline and the manifest's 20 disclosed conditions
   continue to apply.

## Output — write EXACTLY ONE file

`/Users/ryan/dev/chirality-tandem-review-2026-07-26/CHALLENGE_B_ON_A.md`

Structure: header (challenger id B, input-report hash you verified, corpus
commit, date); one block per challenged finding — FindingID, verdict,
evidence, severity/class commentary if any, confidence; the WARN/INFO
sample record; the out-of-scope observations section (may be empty).

Do not read `CHALLENGE_A_ON_B.md` or `CHALLENGE_BRIEF_A.md` (they may
exist). Do not modify any other file anywhere. No git-state changes; no
repo scripts that write.

Return (final message): `DONE — challenge written`, the file path, its
sha256, and your verdict tally (CONFIRM/REFUTE/NARROW/ADD-MISSING-EVIDENCE
counts).
