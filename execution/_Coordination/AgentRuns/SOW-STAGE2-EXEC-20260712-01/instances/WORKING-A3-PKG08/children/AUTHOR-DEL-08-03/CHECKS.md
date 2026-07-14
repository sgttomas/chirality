# AUTHOR-DEL-08-03 Checks

## Frozen basis

- PASS — current checkout is synchronized `main@193663b1d93299c18d64f59b543b36a0dd5f0ee1`.
- PASS — the exact `A3_MANIFEST.tsv` row identifies APP / PKG-08 / DEL-08-03, 10 dependency rows, `SOW-007, SOW-026`, `OBJ-001, OBJ-007`, and the frozen decomposition basis.
- PASS — all four source, status, context, reference, and dependency hashes equal the frozen row.
- PASS — live production format is `LEGACY_FOUR_DOC`: all four legacy files exist and no live `ScopeOfWork.md` exists.
- PASS — `_STATUS.md` is `IN_PROGRESS`; manifest fields `pilot=false`, `issued=false` prove the ordinary non-issued path.

## Conversion and bindings

- PASS — isolated workspace resolves as valid `MIGRATION_DUAL` only with exact `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176` authority.
- PASS — candidate frontmatter binds DEL-08-03, PKG-08, the frozen decomposition basis, SOW-007/SOW-026, and OBJ-001/OBJ-007.
- PASS — `OUT-001`, `AC-001`, and `VER-001` conservatively restate accepted row/identity/legacy literals and add no lifecycle, reliance, or semantic obligation.
- PASS — 37 `PRESERVED` markers cover all 372 source lines without gaps or overlaps; every map row binds source file, source line range, frozen source hash, unique `CLM-*` target, candidate hash, and disposition.
- PASS — matrix binds `OUT-001 -> CLM-011 -> AC-001 -> VER-001` and all declared evaluation IDs are consumed.

## Deterministic QA

- PASS — validator runs are byte-identical and report `valid=true`, `format=MIGRATION_DUAL`, zero issues.
- PASS — claim-map runs are byte-identical at 37 data rows.
- PASS — parity runs are byte-identical and all 37 checks pass with no silent drop or text mismatch.
- PASS — checklist runs are byte-identical, contain AC-001 exactly once in source order with exact text, candidate identity/hash, OUT-001 linkage, and exact VER-001 text.
- PASS — render runs are byte-identical, bind the candidate hash/schema, and contain no script, form, external URL, external `src`/`href`, or JavaScript reference.
- PASS — partial legacy fixture resolves `INVALID` and fails; unauthorized dual fixture resolves `AMBIGUOUS` and fails.
- PASS — unauthorized checklist and render invocations fail nonzero and emit no output artifact.

## Containment

- PASS — the nine copied input/control files remain byte-identical to live sources.
- PASS — the live project deliverable has no scoped Git modification and still has no live SOW.
- PASS — the candidate tree contains only `DEL-08-03/ScopeOfWork.md`, byte-identical to workspace candidate.
- PASS — all author writes are inside the sealed child instance tree or exact candidate tree.
- PASS — Git, lifecycle, H1/H2, ISSUED, release, integration, sibling, and package surfaces were not modified.
