# RUN — NM-4 import: mandatory-gate bypass via command chaining

**Date:** 2026-07-17 · **Operator:** app-dev loop agent (Claude Fable 5)
**Instrument:** D-APP-60 — disposition-class exercise; this record is the
rationale artifact (cross-cutting → AgentRuns) and the durable home of the
imported near-miss entry. That home is a forced composition of ruled
premises, not a verbatim rule — block item 5 (near-miss-form records live
in rationale artifacts) + item 6 (supersede-never-edit) + S1.2 (NM-1..3
fixed as the adopted baseline in a now-immutable ruled packet) + S3
(rationale artifacts in existing homes only; cross-cutting → AgentRuns) +
F-APP-5 (no new standing surface): every alternative home violates one of
these, so post-adoption entries live in rationale artifacts.

## NM-4 — Mandatory-gate bypass via command chaining (imported)

**Provenance (verified against the live source before import):** piping
loop ruling-execution tranche, disclosed in the PR #265 conversation comment
(github.com/sgttomas/chirality/pull/265#issuecomment-5008976186), offered
for cross-import by the piping operator via the owner 2026-07-17. (The
citation is a PR conversation comment on the merged PR #265.)

**The incident:** a commit briefly landed on the piping branch with a
structurally INVALID receipt — and a `;` in the executing command chain
let commit+push proceed past the failed receipt-validator gate. Caught
immediately from the validator output in the same sequence; repaired and
force-pushed; nothing merged in the interval.

**The lesson (mechanism-level, applies to this loop's validators
identically):** gates must be sequenced so a failure halts the chain — a
mandatory validator followed by `;` is not a gate, it is a log line. Use
`&&` (or separate sequenced commands with checked exit codes) between any
mandatory check and the state-changing command it guards; never `;`. The
family is the same as NM-3 (anticipatory recording): the method defeated
by execution convenience, not intent.

## Class test (run adversarially)

- **Limits screen:** no limit touched — recording a verified lesson with
  provenance; no ruled-record edit (the D-APP-60 packet's baseline corpus
  is untouched; this artifact is the entry's home), no scope, authority,
  accountability, spend, or merge act. Survives.
- **(a) Applies authority, creates none:** the corpus conventions and
  rationale-artifact homes are ruled (D-APP-60 S1/S3); the incident is
  recorded fact on a merged PR's review surface. PASS.
- **(b) Deterministic:** import-with-provenance of a verified,
  sibling-offered entry has one coherent shape; declining it would
  discard a mechanism-level lesson both adopters agreed to share. PASS.
- **(c) Reversible and bounded:** one documentation artifact plus a
  receipt, in-fence. PASS.
- **Attempted failure mode (recorded):** "importing a sibling incident
  makes piping history app-dev truth." Refuted: the entry is recorded as
  an import with verified provenance and a mechanism-level lesson; the
  incident's facts remain piping's record, cited not restated as local
  history.

## Rejections considered this tranche

None beyond the recorded attempted failure mode; the empty referral
slate is stated.
