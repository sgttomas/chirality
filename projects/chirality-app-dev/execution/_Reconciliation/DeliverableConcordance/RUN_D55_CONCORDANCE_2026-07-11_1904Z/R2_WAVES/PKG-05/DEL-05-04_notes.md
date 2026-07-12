# DEL-05-04 Runtime Replay and Transcript View — R2 concordance notes

Source state: `main` = `fac46e33f` (frontend byte-identical to `4c8ed8907` / `61d70bdb0`,
git diff empty). Behavioral binding: `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0;
Vitest 667 passed / 4 skipped) plus named test files/cases per row (MR-3).

## Census

- Total rows: 18
- By ClaimType: REQUIREMENT 13, EXCLUSION 4, REMAINING_WORK 1
- By Disposition: ALIGNED 17, STALE_SPECIFICATION 1
- REGISTER_DEFECT rows: 0 (see register cross-check below)
- IMPLEMENTED_UNMAPPED rows: 0 (see unmapped scan below)

The R1 REQUIREMENT_INDEX 13-ID checklist (REQ-001..013) was fully re-derived from
Specification.md and all 13 are covered as REQUIREMENT rows; the four Specification
"Out of scope" bullets are covered as EXC-001..004; the single `## Remaining` item is
REM-001. Datasheet attributes and the Standards table restate the REQ set (MR-4: folded
into the REQ rows; no datasheet-distinct ACCEPTANCE condition found — the kit already
declares all references `MATCH`, so there is no HASH_MISMATCH acceptance row of the kind
seen in PKG-02/PKG-04 waves).

## Key finding — transcript model relocated out of the recorded path (REQ-013, STALE_SPECIFICATION)

The single non-ALIGNED row. The kit's mandated handoff-path list (Spec REQ-013),
Datasheet "Exact parser API" row, Procedure Records, Guidance line 23, the ADQ-09
evidence file (lines 21-22), and Assessment REQ004/REQ007 all record the transcript
reconstruction model at `frontend/src/lib/harness/transcript-replay.ts` (and the session
types at `frontend/src/lib/harness/types.ts`). At `fac46e33f` those files do not exist at
those paths: the transcript model is `frontend/packages/harness-contract/src/transcript-replay.ts`
(`deriveTranscriptView` / `TranscriptView`) and types are `.../harness-contract/src/types.ts`,
imported everywhere as `@chirality/harness-contract/*`. `git ls-files` confirms the old
paths are untracked. This is the 2026-07-04 **D-APP-48** SHA-pinned harness-contract
extraction (its pull contract pins package path
`projects/chirality-app-dev/frontend/packages/harness-contract`), which post-dates the
2026-06-21 INSP-03 assessment (SHA 18511e933). MR-8 tie-break: the kit flatly asserts a
now-false file location → STALE_SPECIFICATION (repair-shaped), with `D-APP-48 (context)`.
The three other recorded paths (session-events.ts, events route.ts, transcript-stream-view.tsx)
remain accurate.

The behavior itself is unchanged by the move: every behavioral requirement that depends on
the transcript model (REQ-004/005/006/007/011) is ALIGNED with tests that import the
relocated module and pass in the W1 gate. Assessment tokens on REQ-004/REQ-007 note the
cited `types.ts` path moved but mark the behavior STILL CURRENT.

## Least-confident rows (self-flagged for fan-in recheck) with flip conditions

1. **DEL-05-04-REQ-012 (ALIGNED, MEDIUM).** I read REQ-012 as an
   assignment-and-recording obligation ("paths are assigned by ADQ-09 and must remain
   recorded in evidence") that is met — the paths were assigned and are recorded — and
   routed the *path-accuracy* staleness to REQ-013 to avoid double-counting one defect.
   Alternative reading that flips it: if "must remain recorded in evidence" is read as
   requiring the recorded values to stay *accurate*, then the stale transcript-model/types
   paths make REQ-012 itself STALE_SPECIFICATION (a second stale-path row). I chose the
   narrower reading; the fan-in may prefer to split the defect across both rows.

2. **DEL-05-04-REQ-013 (STALE_SPECIFICATION, HIGH — the operative finding).** Flagged
   though HIGH-confidence on the facts because the disposition choice is a judgment.
   Alternative reading: since D-APP-48 is a ruled, accepted structural relocation, one
   could read the divergence as `ACCEPTED_DIVERGENCE` (ruling-acknowledged bounded
   difference) rather than STALE_SPECIFICATION. I applied MR-8: D-APP-48 rules the package
   *mechanism* but does not acknowledge or bless the DEL-05-04 kit's specific path text, so
   the kit wording is a flatly now-false state → STALE_SPECIFICATION (repair-shaped). If
   the verifier holds that D-APP-48 implicitly accepts all downstream path drift, this
   flips to ACCEPTED_DIVERGENCE (no repair implied).

3. **DEL-05-04-REQ-010 (ALIGNED, HIGH — corrected at fan-in).** My original note here
   claimed the Section 9 runner sat outside the executed Vitest gate with only
   source-inspection coverage. That was wrong: `frontend/src/__tests__/scripts/validate-harness-section9.test.ts`
   exists inside the Vitest suite (independently re-verified this run) and gate-binds the
   Section 9 governance surface — lines 13-57 assert the governed manifest pins the exact
   16-ID inventory, including `section9.session_event_replay` (line 17) and
   `section9.sdk_session_link_resume` (line 20), with every check required to carry
   testFiles/evidenceFiles; lines 59-72 assert runner/wrapper content. The claim row's
   VerificationEvidence now cites this test; Confidence raised MEDIUM→HIGH and
   RemainingWork → NONE_OBSERVED. Retained precision: the gate binds the manifest
   inventory and runner *content*; it does not execute the `.mjs` runner itself (MR-3 —
   nothing was executed this run). Disposition unchanged: ALIGNED.

4. **DEL-05-04-EXC-001 (ALIGNED, MEDIUM).** `appendHarnessEvent` co-locates in
   DEL-05-04's `session-events.ts`, while the exclusion places the "append-only writer"
   with DEL-05-02. I read the exclusion's "primarily DEL-05-02" as bounded, so the thin
   append helper is not a breach. Alternative reading: if the append helper is deemed the
   writer surface, this is IMPLEMENTED_DIFFERENTLY / a scope-ownership question for
   DEL-05-02 vs DEL-05-04.

## D-APP-36 (context) — UI render bar

Per the wave dispatch, I checked render coverage for the transcript-view surface.
`frontend/src/__tests__/components/harness-stream-views.test.ts` lines 84-125 render
`TranscriptStreamList` (empty state + assistant messages/tool artifacts/terminal status),
so the D-APP-36 component render-test bar IS satisfied for the presentational list. Noted
on REQ-006 as `D-APP-36 (context)`: the live provider-wired container `TranscriptStreamView`
(transcript-stream-view.tsx lines 103-107, consuming `useHarnessEvents`) has no *direct*
render test — only the presentational list it delegates to is covered. This is a
render-coverage nuance, not a gap that changes the ALIGNED disposition; recorded as
optional RemainingWork.

## Register cross-check (Dependencies.csv / _DEPENDENCIES.md / _REFERENCES.md) — no defect

- **Dependencies.csv**: 9 rows, all ACTIVE / SATISFIED. `_DEPENDENCIES.md` summary tables
  (9 ACTIVE, 9 SATISFIED, 4 ANCHOR + 5 EXECUTION) agree with the CSV. Declared
  Upstream/Downstream narrative matches the extracted register (no TBD-vs-populated lag of
  the kind found on DEL-04-01/03/04). Rows DEP-05-04-005 (DEL-05-01), -007 (DEL-04-01),
  -009 (DEL-05-05) re-verified live against the tree — the referenced surfaces exist and
  the SATISFIED states hold at `fac46e33f`.
- **_REFERENCES.md**: 7 refs, all `MATCH`; hashes present and internally consistent. No
  falsified cell.
- **Metadata-lag observation (not a defect):** the registers were last updated 2026-06-21
  and predate the 2026-07-04 D-APP-48 relocation, and the ADQ-09 evidence quote in
  Dependencies.csv DEP-05-04-006 cites `frontend/src/lib/harness/session-events.ts` — which
  did *not* move, so that cell is still accurate. No register cell cites the relocated
  `transcript-replay.ts` / `types.ts` paths, so there is no internal register inconsistency
  to raise as a REGISTER_DEFECT (MR-5). The stale-path issue lives entirely in the kit
  documents and ADQ-09 evidence and is captured by REQ-013.
- **Cosmetic lag (noted, no row):** Spec/Datasheet/Guidance/Assessment refer to
  "D-APP-38 authority corpus **v2**" while the run's current corpus snapshot is **v6**
  (AUTHORITY_MAP). Both v2 and v6 report all DEL-05-04 references `MATCH`, so no now-false
  state is asserted; this is a version-label lag only, below the threshold for a claim row.

## Unmapped-implementation scan — none material

Walked the four DEL-05-04 surfaces. All material live behavior maps to a requirement:
events route (`route.ts`) → REQ-001/005; parser (`session-events.ts`) → REQ-001/002/003/008;
transcript model (`transcript-replay.ts`) → REQ-004..007/011; UI (`transcript-stream-view.tsx`)
→ REQ-006 and the Documentation section's named Transcript sidebar tab. The
`runtime.mirror.error` → diagnostic transcript item (transcript-replay.ts lines 335-347) is
covered by the Guidance/Datasheet "diagnostics" language under REQ-003/REQ-006 and is not
broken out as UNMAPPED.

## Method deviations

None. 19-column §6 header copied verbatim from the R0 exemplar; MR-1 (one Assessment
token per row), MR-2 (SelectableUnderCurrentLoop=YES only on REM-001), MR-3/MR-10
verification vocabulary, and MR-8 tie-break applied as recorded above. No tests executed;
no lifecycle transitions; write scope limited to these two files.
