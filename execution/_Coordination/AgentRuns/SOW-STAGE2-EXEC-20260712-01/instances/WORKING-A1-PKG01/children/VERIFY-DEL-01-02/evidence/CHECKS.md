# VERIFY-DEL-01-02 Independent Verification Checks

Verdict: `PASS`

## Frozen identity and format

- Exact seeded candidate and accepted candidate target are byte-identical at SHA-256 `a6c04d568d83dee81af68815fe5b2adaa13cbe771b3788b6a73d5571e0722b64`.
- All 9/9 seeded inputs equal the live files and exact accepted A1 manifest hashes before and after verification.
- Live state resolves as valid `LEGACY_FOUR_DOC`; no live `ScopeOfWork.md` exists; `_STATUS.md` remains `IN_PROGRESS`.
- The isolated candidate resolves as valid authorized `MIGRATION_DUAL` with `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176` and zero validator issues.

## Independent deterministic reproduction

| Check | Result |
|---|---|
| Validator | PASS — exact schema/frontmatter/headings/IDs/matrix and authorized isolated dual state |
| Claim map | PASS — 60 data rows; SHA-256 `3f9e560d510716797e0aeee052bc26c7686f416f26902d142e755dad2b08da4c` |
| Parity | PASS — 60/60 checks, zero issues, zero failed checks, all dispositions `PRESERVED` |
| Source distribution | PASS — Datasheet 13; Specification 10; Procedure 15; Guidance 22 |
| Markers | PASS — 60 begin and 60 end markers; every marker binds the current source hash and one defined `CLM-*` target |
| Checklist repeatability | PASS — 1/1 candidate `AC-001`, exact text/order/qualified identity/source binding, matrix-linked `OUT-001` and `VER-001`; both SHA-256 `1b6e541f5f8a6750a125a635141b057d71ed5cf9e7153c3cc7d52e153f781ac0` |
| Render repeatability | PASS — both SHA-256 `bbad6595b1c4f6372c9f85bf4bc9b261a7b1ed5dda4e048dff1500d77c19e37a`; canonical candidate hash embedded; no script, external URL, `src=`, `href=`, or CSS `url(` reference |
| Author-result comparison | PASS — independently reproduced claim map, checklist, and render hashes equal the author artifacts |

## Semantic-addition review

All transformed text outside byte-exact source blocks was inspected. It is limited to converter-owned headings/`CLM-*` identities, frozen frontmatter and traceability, the migration-authority marker, one output/acceptance/verification triplet, and its matrix row.

- `OUT-001` conservatively names the legacy-source Reliance Boundary Register, enforcement matrix, and test index; those exact artifacts are repeatedly required in Datasheet, Specification, Guidance, and Procedure.
- `AC-001` limits acceptance to preservation and traceability against the exact frozen A1 scope/objective refs.
- `VER-001` names only the sealed brief's deterministic checks plus later human review.
- Seed identity is exactly `OUT-001`, `AC-001`, and `VER-001`; no additional `OUT-*`, `AC-*`, or `VER-*` identity exists.
- No new scope, reliance claim, lifecycle meaning, implementation obligation, issuance claim, conflict resolution, or human-gate action was introduced.

## Four verdict classes

| Class | Verdict | Evidence |
|---|---|---|
| Schema | PASS | Valid authorized `MIGRATION_DUAL`; exact identities, required sections, linkages, and matrix closure. |
| Project-content authority | PASS | All seed meaning is a conservative traceable restatement of accepted row identity/refs, exact legacy content, and sealed verification method. |
| Preservation | PASS | Nine inputs byte-identical; 60/60 source blocks exact and `PRESERVED`; status/control unchanged. |
| Execution substrate | PASS | Registered local tools only; deterministic repeats stable; negative fixtures fail closed; output containment and portability pass. |

## Fail-closed fixtures

- Partial legacy fixture (missing `Procedure.md`): validator exit `1`, format `INVALID`, explicit missing-file issue.
- Unauthorized dual fixture: validator exit `1`, format `AMBIGUOUS`, explicit exact-authority/isolation issue.
- Checklist derivation against unauthorized dual: exit `1`; the requested output artifact was not created.
- Fixtures used only child-local links to read-only seeded inputs and were removed after the checks.

## Replacement and containment

- `REPLACEMENT_MANIFEST.tsv` contains exactly five data rows: add only `ScopeOfWork.md`; delete only the four legacy documents. `_STATUS.md` and every control/dependency path are excluded.
- Project path, accepted candidate, author instance, package manager, siblings, Git, lifecycle, H1/H2, ISSUED, release, and retirement state were not written.
- Generated verifier metadata/evidence contains zero checkout-prefix, temp-prefix, or `file://` occurrence after portability normalization.
- `PRESERVED_SOURCE_LITERAL` exceptions are exactly two accepted input occurrences: one in `_DEPENDENCIES.md` and one in `Dependencies.csv`; both retain their frozen hashes. Candidate and renders contain zero such occurrence.

## Findings

- Schema findings: none.
- Project-content findings: none.
- Preservation findings: none.
- Execution-substrate findings: none.
- Conflicts: none.
- Blockers: none.
- Rerun requirements: none for verifier completion.
