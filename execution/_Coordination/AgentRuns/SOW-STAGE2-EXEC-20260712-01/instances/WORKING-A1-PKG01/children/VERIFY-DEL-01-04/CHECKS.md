# VERIFY-DEL-01-04 Independent Verification Checks

Verdict: `PASS`

## Frozen identity and format

- Exact seeded candidate and manager-accepted candidate are byte-identical at SHA-256 `13a2a49d1cb74fc83b9c64dc39c25f8ae98107b5b666b5b7352a95b4e626a068`.
- All 9/9 seeded inputs equal live files and exact A1 hashes; `_STATUS.md` remains `IN_PROGRESS`; live is exact `LEGACY_FOUR_DOC` with no live Scope of Work.
- Isolated candidate is valid authorized `MIGRATION_DUAL`, canonical `PKG-01`, exact D-GOV-16 authority, zero schema issue.

## Independent reproduction

| Check | Result |
|---|---|
| Validator | PASS — exact frontmatter, headings, IDs, refs, linkage, matrix, and authorized dual state |
| Claim map/parity | PASS — 28 rows; claim-map SHA-256 `5ab369a8f5640fcb1f86cf4fd1af05b7ce1b4370bdcd05ad7223c2b7ae38d1c0`; 28/28 parity; zero issue |
| Coverage/markers | PASS — 333/333 lines; 28 begin and 28 end markers; all dispositions `PRESERVED` |
| Checklist | PASS — exact one-item `AC-001`, exact source identity/text/order, matrix-linked `OUT-001`/`VER-001`; repeat SHA-256 `bd3f80c3d8e3904c64e6053128649e86b2f2f0c674a7fad9c1ecb44ae312fb49` |
| Render | PASS — repeat SHA-256 `a737b479a22884df5a35cc32920be503456e7cd70017dae114e22e5da130e956`; canonical hash bound; zero script/form/external/src/href reference |
| Author comparison | PASS — independently reproduced claim map, checklist, and render bytes equal author artifacts |

## Semantic and verdict review

- Exact transformed source text is marker-bound. Outside source blocks, only converter structure, frozen traceability, `OUT-001`, `AC-001`, `VER-001`, matrix linkage, and authority marker occur.
- Seed meaning is conservative and authorized; no scope, reliance claim, lifecycle meaning, obligation, issuance, conflict resolution, or human-gate act was introduced.
- The preserved source-local `CHECKING` statement is not current lifecycle truth and was not silently resolved.
- Schema PASS; project-content authority PASS; preservation PASS; execution substrate PASS.

## Fail closed, replacement, portability, containment

- Partial legacy validator: exit 1, `INVALID`, explicit missing-file issue.
- Unauthorized dual validator: exit 1, `AMBIGUOUS`, explicit isolation/authority issue.
- Unauthorized dual checklist: exit 1; requested output artifact absent.
- `evidence/REPLACEMENT_MANIFEST.tsv` has exactly five data rows: add Scope of Work; delete only four legacy documents; all status/control/dependency paths excluded.
- `PRESERVED_SOURCE_LITERAL` inventory binds `Datasheet.md` hash/line 80 and `_REFERENCES.md` hash/line 13, candidate `CLM-007` marker/line 132, and render line 97 echoes. Other generated metadata/run evidence has zero checkout/temp/file-URI prefix.
- Writes are verifier-instance-only. Candidate, project, author, sibling, manager, Git, lifecycle, H1/H2, issuance, release, and retirement state remain read-only/unmodified.

Findings: none. Conflicts requiring verifier action: none. Blockers: none. Rerun requirements: none for verifier completion.
