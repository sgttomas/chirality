# T3 — Confirm Addendum 10 candidates (absence is not evidence of absence)

Read `_COMMON.md` first. Also read CONVENTIONS §2.6 ("Absence is not evidence of absence") and
RUN_BASIS Addenda 10 and 11, and the owner's words in
`<APP_WORK>/execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/OWNER_DIRECTION.md`
section `r2_absence_not_evidence` (read that file from the working repository; it is run
evidence, not a deliverable).

**Input.** `<RUN>/R3/_work/CAND_ADD10.csv` (column `Why` gives the screen reason): candidates from
a keyword screen, PKG-09 PACKAGE_SUMMARY §8 (30 rows), and the EXT release-document rows
(`R2/EXT/EXT_SUMMARY.md` §5 `RELEASE_PROCESS_NOT_RUN`). The screen is broad on purpose; many
candidates will not qualify.

**Rule.** A claim may be about whether an action or event happened outside the code:
notarization, signing, publication, a release or CI job run, an attestation, a manual or human
step, or a credentialed operation. If the row's conclusion that the event did *not* happen (or
was not done for this version) rests **only** on no record existing within the evidence roots,
the Disposition is `UNKNOWN` with `OWNER_CHECK: <one-line question>`. Positive evidence either
way counts as usual (for example a failed job log, a script that hard-fails at a block step, an
AgentRuns record that the event did happen, or a dependency boundary that makes a proof
impossible to pass). Code-presence findings are unaffected: whether code exists and is reached
is judged from the code.

**For each candidate decide one verdict:**
- `REMAP_UNKNOWN`: the Disposition rests only on an absent record of an off-code event. It becomes
  `UNKNOWN` and the row gets an OWNER_CHECK question.
- `NOTE_ONLY`: the Disposition stands on code or positive evidence, but part of the row's
  reasoning (or RemainingWork) asserts an off-code event did not happen from absence alone. The
  Disposition stays; the row gets an OWNER_CHECK note for that part.
- `NO_CHANGE`: not an off-code event claim, or positive evidence decides it.
- `UNDECIDED`: give both readings.
Check the cited records in the frozen tree where the row's reasoning depends on them (for
example `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_*` release records,
`.github/workflows/*.yml` under the App project if cited, `frontend/package.json`).

**Output 1.** `<RUN>/R3/_work/T3_ADD10_VERDICTS.csv`:
`ClaimKey,SealedDisposition,Verdict,EventGroup,Version,OwnerCheck,Evidence`
- `EventGroup`: `RELEASE_ACT|SIGNING|NOTARIZATION|PUBLICATION|CI_AND_RELEASE_JOBS|ATTESTATION|MANUAL_STEPS|PACKAGED_PROOFS|OTHER`.
- `Version`: `3.0.0`, `3.0.1`, `BOTH`, `ANY` or `NA`.
- `OwnerCheck`: for REMAP_UNKNOWN and NOTE_ONLY, one line the owner can answer yes / no / don't
  know, phrased as a question about what the owner did or saw happen (for example "Did you run
  the packaged network-policy proof on the v3.0.0 DMG before publishing it?"). Never word the
  event as settled either way. Reuse the exact same wording for rows that ask the same thing, so
  questions group. Empty for NO_CHANGE.
- `Evidence`: what was found (positive records with repo-relative paths) or "no record in
  <where searched>". One or two sentences.

**Output 2.** `<RUN>/R3/_work/T3_NOTES.md` (≤ 60 lines): counts by verdict and EventGroup; the
distinct OwnerCheck questions with their row counts; any positive evidence you found that bears
on several rows (for example records showing 3.0.0 signed, notarized and published); and the
owner-reported fact "v3.0.1 was notarized, as v3.0.0 was" listed as a statement to confirm (not
applied).
