# TM109-A identity/provenance envelope design acceptance

Status: `RECORDED — CONTRACT-DESIGN SEMANTICS ONLY`

RunID: `ROOT_TM109_DESIGN_ACCEPTANCE_2026-08-03`

Recorder: `HELPS_HUMANS`, managed by `HELP_HUMAN`

Accountable human: `Ryan Tufts`

Decision date: `2026-08-03`

## Authority source

The ruling of record is carried verbatim in:

`execution/_Coordination/AgentRuns/ROOT_SEMANTIC_RETURNS_2026-08-03/OWNER_RETURN_TRANSCRIPT_2026-08-03.txt`

Authority-transcript SHA-256:
`6396dd26c3fb8b6ed922c1cb7da584f67a08188d5b27525d650bf3ca1560c566`.

The exact signed TM109-A return is:

> ACCEPT TM109-A IDENTITY-PROVENANCE ENVELOPE DESIGN 2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489 — EXACT CANDIDATE BYTES AND EACH RECORDED CANDIDATE CHOICE ACCEPTED AS CONTRACT-DESIGN SEMANTICS ONLY; RECORDED NON-SELECTIONS REMAIN BLOCKERS; THE ENVELOPE RECORDS IDENTITY AND PROVENANCE AND DOES NOT PERFORM OR AUTHORIZE EQUALITY, MAPPING, NORMALIZATION, TOLERANCE EVALUATION, SEMANTIC COMPARISON, CONFORMANCE, OR COMPATIBILITY; UNIT-SYSTEM AND TOLERANCE-PROFILE REFERENCES REMAIN OPAQUE; ALL CONSUMER-LOCAL SOLVER/RULE, ENGINEERING, PRIVACY, PROFESSIONAL, AND HUMAN-REVIEW MEANINGS REMAIN LOCAL; NO IMPLEMENTATION, AFFECTED-CLIENT ACCEPTANCE, LIFECYCLE, RELEASE, PUBLICATION, OR RELIANCE AUTHORIZED — Ryan Tufts 2026-08-03

## Recorded effect

The accountable human accepted the exact six-member semantic package bound by
`POST_REFUTATION_MANIFEST.csv` at SHA-256
`2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489`.
The accepted bytes and their Git object identities are frozen in
`ACCEPTED_PACKAGE_BINDING.csv`.

Acceptance selects each `Candidate choice in prepared bytes` for OD109-01
through OD109-16 exactly. A candidate choice that deliberately selects no
algorithm, canonicalization method, payload-scope value, validator/format
profile, trust resolver, or evolution rule remains a blocker. Acceptance does
not fill, normalize, or infer any such non-selection.

## Exact-byte calibration after the whitespace repair

The owner required PR #510's candidate-whitespace failure to be repaired and
re-pushed before these returns were recorded. Repair commit
`2b6d53027ea10374dd515a4a5a203f8ed4cf2f04` is present at both branch `HEAD`
and its `origin/` remote-tracking ref. The recorded hosted rerun passed at run
`30877532946`, job `91891904563`.

The manifest file itself remains byte-identical and still hashes to the signed
package digest after that repair. Four manifest members had only one surplus
terminal blank line removed by the repair, however. Therefore the exact bytes
accepted by the signed digest are the manifest and member blobs at immutable
pre-repair commit `ba4678ca00c0cf9fb862ba36d1410d11ce1ff6ac`, not silent
substitutions from the normalized descendant checkout. Git preserves all
accepted blobs. This carrier binds them without mutating the original
candidate carrier or regenerating its packet.

## Express exclusions and holds

This acceptance does not perform or authorize equality, mapping,
normalization, tolerance evaluation, semantic comparison, conformance, or
compatibility. Unit-system and tolerance-profile references remain opaque.
Consumer-local solver/rule, engineering, privacy, professional, and
human-review meanings remain local.

No implementation, affected-client acceptance, lifecycle move, release,
publication, reliance, source/test change, validator selection, migration, or
compatibility claim is authorized. Any such action requires a later sealed,
human-gated tranche that resolves the applicable non-selections and names its
exact surfaces, clients, checks, rollback, and evidence.
