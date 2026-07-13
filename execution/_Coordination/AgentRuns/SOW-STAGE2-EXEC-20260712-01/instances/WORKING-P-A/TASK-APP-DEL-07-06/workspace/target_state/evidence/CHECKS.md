# DEL-07-06 Replacement Verification Checks

Verdict: `PASS`

Basis: `main@0d260eb024d8b8dada0df477b70ac880a6906ffa`; Stage-1 App evidence commit `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`; P3 `B1/G3 PASS`; `PILOT-VALIDATION-001`.

## Identity and format

- All four live production sources and `_STATUS.md` match the exact P3 hashes, the `main@0d260e...` blobs, and isolated `legacy_source` seed copies.
- Extracted candidate, target seed, accepted hash, and Stage-1 commit blob all equal `6de59e2a9d6806fb620c673b1da4822337b4c531a41de3186c9f0fde8e10b93e`.
- Current live state validates `LEGACY_FOUR_DOC`, has no `ScopeOfWork.md`, remains `IN_PROGRESS`, and has zero issues.
- Target root has `ScopeOfWork.md` and `_STATUS.md`, has no legacy production file at root, validates `SOW_V1`, and has zero issues.
- Candidate retains only the historical `D-GOV-15@58aa81d62f4a32e3c2d687e4356a1e4be8141674` pilot provenance marker. It has no `D-GOV-16` migration-authority marker; no converter, isolated-dual validation, overlay, or marker insertion was invoked.
- Stage-1's historical `PILOT_DUAL` envelope was not replayed. `PILOT-VALIDATION-001` requires and this run applies two separate validations: current live legacy-only and isolated target-only.

## Mapping, parity, and review checklist

- Claim map: 29 rows, 29 unique resolved `CLM-*` targets, all `PRESERVED`; SHA-256 `e84f0bb9bba1837aff902ed45f6e00280387a1396071cf384320570b6f1f23ca`.
- Parity: PASS, 29/29 checks, 309/309 source lines, zero issues. Fresh report is semantically identical to Stage-1 after excluding its run-local `scope_of_work` path; canonical digest is `db4622a037dc6f15b70cdef23f93fd58e352629455218c05aab30ef8d8e013a3`.
- Candidate markers: 29 begin and 29 end; every marker binds the current source hash and a defined target. There are no `MERGED` or `SPLIT` dispositions requiring multi-source reference checks.
- Evaluation identity: one `OUT-001`, one `AC-001`, and one `VER-001`; the matrix links all three with `SOW-032 SOW-033 SOW-034 OBJ-006 OBJ-009`.
- Checklist runs are byte-identical at SHA-256 `61c55a8bb9e4d3cb8507a2629f70b0a9f83ea8b5527437ab895251fd9360212b`. `DEL-07-06-AC-001` appears exactly once with exact text, source order/identity, candidate hash, output, and `VER-001` linkage.
- Fresh and Stage-1 checklist `items` are semantically identical after canonical JSON rendering (digest `6bbed9985bf6502a52c4667b06df30d3869512391bfb5d1800742019f867ee35`). The envelope format differs lawfully from historical `PILOT_DUAL` to current `SOW_V1` under `PILOT-VALIDATION-001`.
- Negative checklist derivation against the live legacy-only input failed with exit 1 before output; no invalid checklist artifact exists.

## Rendering, grounding, and preservation

- Two renders are byte-identical at SHA-256 `8bae3dad755538742f999215e7d990f2afff647816abf0ec04fd6848c98308d2`, exactly matching both Stage-1 renders.
- HTML binds schema `chirality-deliverable-sow/v1`, candidate hash, and renderer `chirality-sow-renderer/v1`. It contains no script, form, iframe, object, embed, external URL/resource, `src=`, `href=`, `action=`, or CSS `url(`.
- Current accepted decomposition assigns `DEL-07-06` to `SOW-032`, `SOW-033`, `SOW-034`, `OBJ-006`, and `OBJ-009`; `_CONTEXT.md`, candidate frontmatter, and output matrix agree. Decomposition bytes at candidate revision `2770fda4c63c98ee9f18cffbafd14c9aa59f497f` equal current/base bytes at SHA-256 `a907cda33835ebf06187331c1c5937a9ae9949923c5465b17519cbd8fcaba6d4`.
- Stage-1 inventory agrees on candidate/source/status hashes, 29 mappings, 309 mapped lines, lifecycle, objective refs, and PASS results. Fresh map is byte-identical, parity is semantically identical, render hash is identical, and AC/VER identity is unchanged under the corrected `SOW_V1` state.
- HEAD, `main`, and `origin/main` equal `0d260eb024d8b8dada0df477b70ac880a6906ffa`. Live project tracked content, candidate, sources, status, lifecycle, controls, history, and Git state were not modified.

## Future atomic replacement evidence

- `REPLACEMENT_MANIFEST.tsv` has exactly five data rows: one `ADD ScopeOfWork.md` and four `DELETE` legacy production rows at exact hashes.
- `_STATUS.md` and every control/lifecycle path are absent from the action set and remain byte-identical. The manifest is evidence only and was not applied.

## Result classes

- Schema/project-content: `PASS`.
- Source/status preservation and replacement containment: `PASS`.
- Execution substrate/write containment: `PASS`.
- Conflicts, blockers, waivers, repairs, and rerun requirements: none at the recorded hashes.
