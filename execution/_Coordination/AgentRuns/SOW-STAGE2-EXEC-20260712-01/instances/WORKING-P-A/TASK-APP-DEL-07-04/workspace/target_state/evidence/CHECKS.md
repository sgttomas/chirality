# DEL-07-04 Replacement Verification Checks

Verdict: `PASS`

Basis: `main@0d260eb024d8b8dada0df477b70ac880a6906ffa`; Stage-1 App evidence commit `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`; P3 `B1/G3 PASS`; `PILOT-VALIDATION-001`.

## Identity and format

- All four live production sources and `_STATUS.md` match the exact P3 hashes, the `main@0d260e...` blobs, and isolated `legacy_source` seed copies.
- Extracted candidate, target seed, accepted hash, and Stage-1 commit blob all equal `d456e9d29262c0cb9d0fc3350ab52b1b5a36b9c3bfab1378476c2e3ae55a9342`.
- Current live state validates `LEGACY_FOUR_DOC`, has no `ScopeOfWork.md`, remains `IN_PROGRESS`, and has zero issues.
- Target root has `ScopeOfWork.md` and `_STATUS.md`, has no legacy production file at root, validates `SOW_V1`, and has zero issues.
- Candidate retains only the historical `D-GOV-15@58aa81d62f4a32e3c2d687e4356a1e4be8141674` pilot provenance marker. It has no `D-GOV-16` migration-authority marker; no converter, isolated-dual validation, overlay, or marker insertion was invoked.
- Stage-1's historical `PILOT_DUAL` envelope was not replayed. `PILOT-VALIDATION-001` requires and this run applies two separate validations: current live legacy-only and isolated target-only.

## Mapping, parity, and review checklist

- Claim map: 34 rows, 34 unique resolved `CLM-*` targets, all `PRESERVED`; SHA-256 `680effcf80a77c0f59bc424898c8e54f375b4d52c6e86bea19c6379fed1d4e65`.
- Parity: PASS, 34/34 checks, 383/383 source lines, zero issues. Fresh report is semantically identical to Stage-1 after excluding its run-local `scope_of_work` path.
- Candidate markers: 34 begin and 34 end; every marker binds the current source hash and a defined target. There are no `MERGED` or `SPLIT` dispositions requiring multi-source reference checks.
- Evaluation identity: one `OUT-001`, one `AC-001`, and one `VER-001`; the matrix links all three with `SOW-028 OBJ-006`.
- Checklist runs are byte-identical at SHA-256 `9d19904d714c572bc2549d6b49b1d4ca56d016ca24882b32431cb8dd1df1629d`. `DEL-07-04-AC-001` appears exactly once with exact text, source order/identity, candidate hash, output, and `VER-001` linkage.
- Fresh and Stage-1 checklist `items` are byte-semantically identical after canonical JSON rendering (digest `bd5e145df31456f08328718b77a66f4fee3d233456b5de9dc1f0a2c03710b4be`). The envelope format differs lawfully from historical `PILOT_DUAL` to current `SOW_V1` under `PILOT-VALIDATION-001`.
- Negative checklist derivation against the live legacy-only input failed with exit 1 before output; no invalid checklist artifact exists.

## Rendering, grounding, and preservation

- Two renders are byte-identical at SHA-256 `15ea2b827219b9f33be903959a7186ba58e1a81cf336a5e4102c749d97493eff`, exactly matching both Stage-1 renders.
- HTML binds schema `chirality-deliverable-sow/v1`, candidate hash, and renderer `chirality-sow-renderer/v1`. It contains no script, form, iframe, object, embed, external URL/resource, `src=`, `href=`, or CSS `url(`.
- Current accepted decomposition assigns `DEL-07-04` to `SOW-028` and `OBJ-006`; `_CONTEXT.md`, candidate frontmatter, and the output matrix agree. Decomposition bytes at candidate revision `2770fda4c63c98ee9f18cffbafd14c9aa59f497f` equal current/base bytes.
- Stage-1 inventory agrees on candidate/source/status hashes, 34 mappings, 383 mapped lines, lifecycle, objective refs, and PASS results. Fresh map is byte-identical, parity is semantically identical, render hash is identical, and AC/VER identity is unchanged under the corrected `SOW_V1` state.
- HEAD, `main`, and `origin/main` equal `0d260eb024d8b8dada0df477b70ac880a6906ffa`. Live project tracked content, candidate, sources, status, lifecycle, controls, history, and Git state were not modified.

## Future atomic replacement evidence

- `REPLACEMENT_MANIFEST.tsv` has exactly five data rows: one `ADD ScopeOfWork.md` and four `DELETE` legacy production rows at exact hashes.
- `_STATUS.md` and every control/lifecycle path are absent from the action set and remain byte-identical. The manifest is evidence only and was not applied.

## Result classes

- Schema/project-content: `PASS`.
- Source/status preservation and replacement containment: `PASS`.
- Execution substrate/write containment: `PASS`.
- Conflicts, blockers, waivers, repairs, and rerun requirements: none at the recorded hashes.
