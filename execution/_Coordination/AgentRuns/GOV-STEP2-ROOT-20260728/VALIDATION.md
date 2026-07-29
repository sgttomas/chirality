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
