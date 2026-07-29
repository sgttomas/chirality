# Validation — GOV-STEP2-ROOT-20260728

Status: `PRE-COMMIT PASS (bounded warnings documented)`

## Basis and preimages

- Worktree branch `gov/step2-root-disclosure` resolves to
  `85ea0628fa4e57dd6aae53b06139b2b8734a9612` (frozen basis; clean before
  authoring).
- All eight pinned do-not-touch surfaces in `RUN_MANIFEST.md` match their
  recorded SHA-256 preimages; none appears in the working diff.
- `docs/governance_harness/_DECISIONS/_REGISTER.md` preimage SHA-256
  `4bc26afed30dfb665df4d137722640f1e16d551c60be809863af8e74b08ec147`;
  the only change is one appended `D-GOV-30` row.
- `execution/_Coordination/LOOP_RECEIPTS.md` is untouched; Receipt 59 is
  the verified cursor and **60** is the verified next-free receipt number
  used by the packet's RECEIPT_DRAFT.

## Candidate results

- Packet CandidateSubjectSHA256:
  `32b4afbfb402d65fecc14558bca79f5b83fc5690bd0b4f56cc9a656ced6c35e3`,
  computed over the final packet bytes and recorded in the decision
  record and register row. The packet was not edited after hashing.
- Every ruling slot (four in the packet, four in the decision record, one
  in the RECEIPT_DRAFT) holds exactly the fenced literal
  `<<RULING PLACEHOLDER — OWNER RETURN VERBATIM: D-GOV-30>>` between
  `<!-- BEGIN OWNER RULING VERBATIM -->` and
  `<!-- END OWNER RULING VERBATIM -->`. No ruling text exists anywhere.
- OD7-G1 R-4 enumeration re-verified at this basis: `shasum -a 256 -c`
  reproduces all 15 member hashes (10 + 5, 15/15 OK); both manifest-file
  SHA-256s match the values recorded in the packet.
- The OD7-G1 packet's `D-GOV-29` observation is byte-untouched; the
  numbering rationale is recorded in packet §3.
- No retroactive-cure, first-transcription, or compliance claim appears;
  the owner direction is cited by reference to the closeout record with
  its SHA-256.

## Deterministic checks

1. G4 manifest validator (`validate_instruction_tranche_manifest.py`, CI
   mode): **PASS**, 12 manifests schema-valid including
   `ROOT-GOV30-DISCLOSURE-20260728`; one INFO for the lawful
   `m6_notice.disposition: pending`. The validator accepts the
   `m2_gate.authorization` pending-quote convention (non-empty factual
   string carrying the marker
   `<<AUTHORIZATION QUOTE PENDING OWNER SESSION>>`); no rejection, so no
   fallback rewording was needed beyond embedding the marker in a factual
   sentence, with the convention noted in `scope_limits`.
2. Candidate whitespace (`validate_candidate_whitespace.py`): **PASS**.
3. Practitioner harness `self-check`: exit 0, no BLOCK. Four **expected
   WARN** `UNRESOLVED_SOURCE_REF` findings are introduced by this
   candidate: the two `execution/_Evaluation/*_2026-07-28_85EA0628/`
   evidence paths cited in the packet and decision record do not exist at
   this basis because the frozen evidence lands via the separate evidence
   PR (branch `gov/step1-evidence-landing`, commit `02b1f091a`). The
   citations are content-addressed (manifest SHA-256s
   `53844bfd…` and `a592b509…`) and resolve once that PR merges. All
   other findings match the pre-existing baseline.
4. `git status --porcelain`: exactly the seven declared write-scope
   paths (one modified, six added); nothing else.

## Required completion-time reruns (after the owner session)

1. Transcribe the owner's verbatim per-item returns into the decision
   record's four ruling slots; record any decline per item.
2. Replace the manifest `m2_gate.authorization` pending marker with the
   owner's verbatim Step-2 authorization quote.
3. Rescan the receipt cursor; append Receipt 60 (packet RECEIPT_DRAFT)
   to `LOOP_RECEIPTS.md` only if 60 is still free, filling its ruling
   slot from the owner return.
4. Backfill AcceptedCandidateSHA, CandidateMergeSHA, PublicationSHA, and
   EffectiveSHA per the D-GOV-18/19/21/22 convention.
5. Confirm the evidence PR has merged so the four expected WARN
   references resolve; re-run G4 (CI and diff mode), whitespace, and
   self-check.
6. Route or close the pending M6 notice disposition at Agent 0 fan-in.
7. The PR is human-gated; no self-merge.

Validation is evidence, not acceptance.

## Completion pass — 2026-07-28 (owner ruling received)

The owner ruled in-session on 2026-07-28 with a single composite return
covering R-1..R-4. This run record is evidence, not an authority surface,
so it carries no ruling fence of its own: the operative verbatim ruling is
recorded in the D-GOV-30 decision record's four slots and in Receipt 60.

Completion edits applied in the completion commit on
`gov/step2-root-disclosure`:

1. The four ruling slots in
   `docs/governance_harness/_DECISIONS/D-GOV-30_program_disclosure_and_ratification.md`
   hold that line byte-exact; the field block records
   `Status: RULED`, the `HumanRuling` one-line summary, and
   `AcceptedCandidateSHA: 9f6a4c637f38959b5d89df6d92846335fd20d60c` (the
   candidate commit). `CandidateMergeSHA`, `PublicationSHA`, and
   `EffectiveSHA` remain PENDING for backfill after the human-gated PR
   merge, per the D-GOV-18/19/21/22 convention. No item was declined.
2. The `D-GOV-30` register row state flipped from `AWAITING_RULING` to
   `RULED`; no other row or cell was touched.
3. The tranche manifest `m2_gate.authorization` now carries the owner's
   verbatim line in place of the pending marker, preserving the K-AUTH-1
   disclaimer sentence. `self_merge` remains `false` and `merge_gate`
   remains `human-gated-pr`.
4. Receipt 60 was appended to `execution/_Coordination/LOOP_RECEIPTS.md`
   after an execution-time cursor rescan (59 was still the cursor; 60 was
   still free). The appended text is the packet RECEIPT_DRAFT with only
   its ruling fence filled; no earlier receipt was touched.

Deterministic reruns at completion:

- G4 manifest validator (`validate_instruction_tranche_manifest.py`, CI
  mode): **PASS**.
- Candidate whitespace (`validate_candidate_whitespace.py`): **PASS**.

Intentional survivals — not unfilled slots:

- The four ruling slots in the candidate packet
  (`_PROPOSALS/D-GOV-30_2026-07-28_program_disclosure_ratification/PACKET.md`)
  still hold the fenced placeholder by design. The packet is the hashed
  immutable candidate (CandidateSubjectSHA256 `32b4afbf…`) and is never
  edited after hashing; its §7 states that the slots are marked ruling
  slots and that the operative rulings live in the decision record.
  Editing it would break the subject hash the ruling is bound to.
- Three descriptive prose mentions of the literal placeholder token
  survive, in the tranche manifest `scope_limits`, in `RUN_MANIFEST.md`,
  and in this file's pre-completion sections above. They describe the
  candidate tranche as authored and are historical statements about that
  state, not live ruling slots.
- The `<<AUTHORIZATION QUOTE PENDING OWNER SESSION>>` mention in this
  file's "Deterministic checks" section is likewise a historical
  description of the pre-completion manifest; the marker itself no longer
  appears in the manifest.

Still open after this pass: the four expected `UNRESOLVED_SOURCE_REF`
WARNs until the evidence PR merges; the SHA backfills in item 1; the M6
notice disposition at Agent 0 fan-in; and the human-gated PR merge — no
self-merge.
