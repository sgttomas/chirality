# Deterministic Owner-Question and Ruling Transform

Status: `BOUND_APPROVAL_EFFECT`

The approval-effect manifest binds this transform, both templates, and the
renderer implementation. The proposal-artifact manifest excludes itself and
the two rendered outputs because each output cites that manifest's own digest.
Those three exact exclusions break the digest cycle; the renderer verifies the
excluded outputs deterministically from the two bound templates and the two
manifest digests.

## Root

Compute lowercase SHA-256 over the exact bytes of
`APPROVAL_EFFECT_MANIFEST.sha256`. Call the 64-character result `ROOT`.

Compute lowercase SHA-256 over the exact bytes of
`ARTIFACT_HASHES.sha256`. Call the 64-character result `ARTIFACT`.

## Owner question

Read `OWNER_QUESTION_TEMPLATE.md` as UTF-8 with LF line endings. Require
exactly one occurrence of `{{APPROVAL_EFFECT_MANIFEST_SHA256}}` and no ruling
status or owner-answer token. Also require exactly one occurrence of
`{{ARTIFACT_HASHES_SHA256}}`. Replace the root token with `ROOT` and the
artifact token with `ARTIFACT`. Change no other byte. The output is
`OWNER_QUESTION.md`.

Both digests are visible immediately above the question. The owner is asked
the rendered blockquote together with those cited digests.

## Conditional ruling

Read `RULING_TEMPLATE.md` as UTF-8 with LF line endings. Require exactly two
root-token occurrences, exactly two artifact-token occurrences, one
`{{RULING_STATUS}}`, and one `{{OWNER_ANSWER}}`. Only the exact owner answer
`Yes` to the current two-digest owner question is valid for operational use.
Preparation and independent review may run this exact render solely to verify
the conditional postimage bytes; such a render is not evidence that the owner
answered and creates no authority. Replace:

- both root tokens with `ROOT`;
- both artifact tokens with `ARTIFACT`;
- `{{RULING_STATUS}}` with `RULED — GIT CLOSEOUT PENDING`; and
- `{{OWNER_ANSWER}}` with `Yes`.

Change no other byte. The output is
`postimages/projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-104_RULING_APP_HOLD_DEL_09_07_BOOTSTRAP_2026-09-04.md`, and later the
identical live ruling path.

The proposal output remains a non-authoritative conditional postimage. It may
be treated as a ruling and copied to the live path only after the exact current
question is presented and the owner supplies a new exact `Yes`.

## Enforcement

Run `PYTHONDONTWRITEBYTECODE=1 python3 tools/render_approval.py verify` from
this proposal directory.
It fails if any approval leaf, rendered output, proposal file-set row,
live-surface row, artifact-manifest leaf, or acyclic exclusion disagrees.
`render-question` and `render-ruling --owner-answer Yes` reproduce the outputs
without free-form editing. Any template, transform, renderer, live-effect
manifest, integration contract, or application-instruction change alters
`ROOT`; any included proposal artifact change alters `ARTIFACT`. Either change
requires a new owner question. A prior answer is never carried to a replacement
digest pair.
