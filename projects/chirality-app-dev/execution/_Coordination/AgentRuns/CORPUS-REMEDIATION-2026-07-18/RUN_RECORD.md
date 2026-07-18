# Corpus remediation tranche — rationale record

**RunID:** `CORPUS-REMEDIATION-2026-07-18`
**Authority:** owner-directed architecture-evaluation remediation program
(2026-07-18, in-session plan approval); D-APP-60 instrument for the
disposition-class exercises below.
**Branch:** `claude/app-dev-corpus-remediation`

## Exercised judgments (disposition-class under the D-APP-60 instrument)

### E1 — F2 identifier-qualification correction notes (6 assessment files)

Appended one dated correction note to each `Assessment_INSP-03_*` file for
DEL-08-01..05 and DEL-07-01, mapping the reversed `REQ-XX-YY-NNN` form to the
canonical `DEL-XX-YY-REQ-NNN` form of the Scope-of-Work Standard §4. No
recorded row edited; the note governs interpretation only.

Class test (fast-reject ordering): limits screen — touches no recorded limit
(no lifecycle, ruling, issuance, fence, or accountability content). (a)
applies authority, creates none: the canonical form is already ruled
(D-GOV-16 standard §4); the note adds no requirement content. (b)
deterministic: one defensible mapping (same NNN, standard token order); no
competing outcome survives. (c) reversible and bounded: an appended dated
note inside `projects/chirality-app-dev/**`, revertible by supersession.
Attempted failure mode (adversarial): "the note silently corrects recorded
evidence" — refuted: rows are byte-unchanged and the note is dated,
appended, and interpretation-only; the alternative (editing rows in place)
was rejected as record-editing.

### E2 — F7b `_STATUS.md` Last-Updated synchronization (53 files)

Deterministic script set each `**Last Updated:**` line to the newest
YYYY-MM-DD date present in the same file: 52 files 2026-07-11 → 2026-07-12,
and DEL-10-04 2026-07-11 → 2026-07-17 (its history carries 2026-07-15/16/17
entries from the D-APP-58/D-APP-59 closures). Diff audited: exactly 53
one-line changes; lifecycle states, history entries, approval SHAs, and all
other bytes untouched.

Class test: limits screen — `_STATUS.md` files are governed artifacts
(D-APP-60 S1.2), which triggers the calibrated verifier, not owner-class
referral; no lifecycle or authorization content is touched. (a) applies
authority, creates none: the newest in-file date is already recorded; the
sync asserts nothing new. (b) deterministic: the newest-date rule admits one
outcome per file. (c) reversible and bounded: 53 one-line edits, revertible.
Attempted failure mode: "a file's newest date might postdate its true last
edit (e.g. a future-dated entry)" — checked: 52 in-file maxima are
2026-07-12 (the D-APP-56 R5/R6 wave) and DEL-10-04's is 2026-07-17 (the
D-APP-58/D-APP-59 closure entries); no date in any file postdates
2026-07-18. An earlier draft of this section wrongly claimed all maxima were
2026-07-12; the pre-commit verifier's first return (BLOCK, preserved below)
caught it, and this corrected text supersedes that claim.

## Referred to the owner (pre-triaged)

- **F5 → D-APP-62** (packet staged `AWAITING_RULING`): interpreting the
  scope of the recorded `_SEMANTIC.md` invalidity assertion fails class-test
  gate (a) — construing a recorded ruling creates interpretive normative
  content, which is owner-class. Pre-triage names the gate; options O-A/O-B/
  O-C staged in the packet. The 10 addenda execute only on an O-A ruling.

No other referral candidates arose; the slate is otherwise empty.

## Model attribution

Orchestrator (planning, drafting, class tests, deterministic edits):
claude-fable-5. Independent adversarial pre-commit verifier:
claude-fable-5, fresh context, sealed refutation-only brief, no shared
authorship of the checked artifacts.

## Verification

<!-- Verdicts are recorded only after they exist. -->

- Pre-commit adversarial verifier (staging scope: E1, E2, D-APP-62 staging):
  verdict recorded below after return.
- Post-ruling verifier (addenda + ruling transcription), if O-A: recorded
  below after return.

### Verifier returns

**Return 1 — BLOCK (2026-07-18, recorded after return).** Claim 4/E2
refuted: the run record asserted "all 53 files: 2026-07-11 → 2026-07-12" and
"all in-file maxima are 2026-07-12"; the live tree shows DEL-10-04 synced
2026-07-11 → 2026-07-17 (history entries 2026-07-15/16/17 from the
D-APP-58/D-APP-59 closures). The sync itself was correct under the
newest-in-file-date rule; the recorded audit claim was false. Non-blocking
caveat: D-APP-62 register row inserted above D-APP-61, breaking numeric
order. Disposition: accepted; E2 text corrected (supersession noted in
place), register row reordered; fresh return requested on unchanged sealed
claims.

**Return 2 — COMMIT-SAFE (2026-07-18, recorded after return).** All five
sealed claims re-verified against the full diff, including independent
recomputation of the transition distribution (52 → 2026-07-12; DEL-10-04 →
2026-07-17) and a fairness check on the Return-1 summary above. The
staging-scope pre-commit gate is satisfied; the D-APP-62 addenda remain
gated on the owner ruling.
