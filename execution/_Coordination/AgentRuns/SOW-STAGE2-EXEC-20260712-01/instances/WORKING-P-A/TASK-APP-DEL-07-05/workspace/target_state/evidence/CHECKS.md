# DEL-07-05 Replacement Verification Checks

Verdict: `PASS`

Basis: `main@0d260eb024d8b8dada0df477b70ac880a6906ffa`; Stage-1 App evidence commit `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`; exact P3 `B1/G3 PASS` row; `PILOT-VALIDATION-001`.

## Identity and format

- All four live production sources and `_STATUS.md` match the exact P3 hashes, the `main@0d260e...` blobs, and isolated `legacy_source` seed copies.
- Extracted candidate, target seed, accepted hash, and Stage-1 commit blob all equal `f38b0e741949abd9a892e8fea1a93c91be7da95bda668b3c80c2fd4dac7f450e`.
- Current live state validates `LEGACY_FOUR_DOC`, has no `ScopeOfWork.md`, remains `IN_PROGRESS`, and has zero issues.
- Target root has `ScopeOfWork.md` and `_STATUS.md`, has no legacy production file at root, validates `SOW_V1`, and has zero issues.
- Candidate retains only the historical `D-GOV-15@58aa81d62f4a32e3c2d687e4356a1e4be8141674` pilot provenance marker. It has no `D-GOV-16` or migration-authority marker; no converter, isolated-dual validation, overlay, or marker insertion was invoked.
- Stage-1's historical `PILOT_DUAL` envelope was not replayed. `PILOT-VALIDATION-001` requires and this run applies two separate validations: current live legacy-only and isolated target-only.

## Mapping, parity, and review checklist

- Claim map: 35 rows, 35 unique resolved `CLM-*` targets, all `PRESERVED`; SHA-256 `a1e27777b54c94f31b9365bf87b2ed909a13bcf188eca11f3cf040b5965127ae`.
- Parity: PASS, 35/35 checks, 419/419 source lines, zero issues. Fresh report is semantically identical to Stage-1 after excluding its run-local `scope_of_work` path.
- Candidate markers: 35 begin and 35 end; every marker binds the current source hash and a defined target. There are no `MERGED` or `SPLIT` dispositions requiring multi-source reference checks.
- Evaluation identity: one `OUT-001`, one `AC-001`, and one `VER-001`; the matrix links all three with `SOW-029 OBJ-006`.
- Checklist runs are byte-identical at SHA-256 `127982a2ff0c11da13b1fb0742e453763961e4bb18922358bf3dfe8c70719af5`. `DEL-07-05-AC-001` appears exactly once with exact text, source order/identity, candidate hash, output, and `VER-001` linkage.
- The fresh checklist reproduces the Stage-1 recorded `AC-001` criterion exactly. The envelope differs lawfully from historical Stage-1 posture to current `SOW_V1` under `PILOT-VALIDATION-001`.
- Negative checklist derivation against the live legacy-only input failed with exit 1 before output; no invalid checklist artifact exists.

## Rendering, grounding, and preservation

- Two renders are byte-identical at SHA-256 `6c974e08c102c493d8de38cad67875af3c659da5791fb847bffd184ca35508a7`, exactly matching both Stage-1 renders.
- HTML binds schema `chirality-deliverable-sow/v1`, candidate hash, and renderer `chirality-sow-renderer/v1`. It contains no script, form, iframe, object, embed, external URL/resource, `src=`, `href=`, or CSS `url(`.
- Current accepted decomposition assigns `DEL-07-05` to `SOW-029` and `OBJ-006`; `_CONTEXT.md`, candidate frontmatter, PRD Section 8.9, and the output matrix agree. Decomposition bytes at candidate revision `2770fda4c63c98ee9f18cffbafd14c9aa59f497f` equal current/base bytes.
- Stage-1 inventory agrees on candidate/source/status hashes, 35 mappings, 419 mapped lines, lifecycle, objective refs, and PASS results. Fresh map is byte-identical, parity is semantically identical, render hash is identical, and AC/VER identity is preserved under the corrected `SOW_V1` state.
- The candidate preserves the live source's dated PRD-warning/history language byte-for-byte; current-state notes and `_REFERENCES.md` identify REF-006 as `MATCH`. No verifier repair or silent semantic rewrite occurred.
- HEAD, `main`, and `origin/main` equal `0d260eb024d8b8dada0df477b70ac880a6906ffa`. Live project tracked content, candidate, sources, status, lifecycle, controls, history, and Git state were not modified.

## Future atomic replacement evidence

- `REPLACEMENT_MANIFEST.tsv` has exactly five data rows: one `ADD ScopeOfWork.md` and four `DELETE` legacy production rows at exact hashes.
- `_STATUS.md` and every control/lifecycle path are absent from the action set and remain byte-identical. The manifest is evidence only and was not applied.

## Result classes

- Schema/project-content: `PASS`.
- Source/status preservation and replacement containment: `PASS`.
- Execution substrate/write containment: `PASS`.
- Conflicts, blockers, waivers, repairs, and rerun requirements: none at the recorded hashes.
