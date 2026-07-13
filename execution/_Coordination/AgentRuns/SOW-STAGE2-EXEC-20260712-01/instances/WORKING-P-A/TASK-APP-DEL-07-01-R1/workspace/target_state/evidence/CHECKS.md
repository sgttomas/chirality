# DEL-07-01 Replacement Verification Checks

Verdict: `PASS`

Basis: `main@0d260eb024d8b8dada0df477b70ac880a6906ffa`; Stage-1 App evidence commit `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`; P3 `B1/G3 PASS`; `PILOT-VALIDATION-001`.

## Identity and format

- All four live production sources and `_STATUS.md` match the P3 hashes, the accepted current-base blobs, and the isolated `legacy_source` seed copies.
- Extracted candidate, target seed, accepted expected hash, and Stage-1 commit blob all equal `9b75621a465553baf47b08b665bbbee8dc39f3d60a1d64b6610b9949c9226744`.
- Current live state validates `LEGACY_FOUR_DOC`, has no `ScopeOfWork.md`, remains `IN_PROGRESS`, and has zero issues.
- Target root contains `ScopeOfWork.md` and `_STATUS.md`, contains no legacy production file at root, validates `SOW_V1`, and has zero issues.
- The candidate retains only the historical `D-GOV-15` pilot provenance marker. It has no `D-GOV-16` migration-authority marker; no converter or isolated-dual mode was invoked.

## Mapping, parity, and review checklist

- Claim map: 31 rows, 31 unique resolved `CLM-*` targets, all `PRESERVED`; SHA-256 `bfef3a1fa07da23c07f9413a1860f0c06e79ae2e95ca13fafbe88282edaab819`.
- Parity: PASS, 31/31 mapping checks, 370/370 source lines, zero issues. The fresh report is semantically identical to Stage-1 after excluding the run-local path field.
- Candidate markers: 31 begin and 31 end markers. Source hashes in markers bind the current sources.
- Candidate evaluation identity: one `OUT-001`, one `AC-001`, one `VER-001`; the matrix links all three and carries `SOW-002 SOW-027 OBJ-006 OBJ-008`.
- Checklist runs are byte-identical at SHA-256 `6f4a6dc3a2e64a5e2a3051067a8f579f864596645775943de38f7350cae3f8ef`. It contains `DEL-07-01-AC-001` exactly once in source order, binds the candidate hash, and links `VER-001` with exact source identity/text.
- Negative checklist derivation against legacy-only input failed before output as required; no invalid checklist artifact exists.

## Rendering, grounding, and preservation

- Two renders are byte-identical at SHA-256 `521b86d762ace99ce53e023eb8bb63ba2a5ef74d2402b5e11c67fad1b107844d`, matching Stage-1 evidence.
- HTML binds schema `chirality-deliverable-sow/v1`, candidate hash, and renderer `chirality-sow-renderer/v1`. Scan found no script, form, iframe, object, embed, external URL/resource, `src=`, `href=`, or CSS `url(`.
- Current accepted decomposition still assigns `DEL-07-01` to `SOW-002, SOW-027` and `OBJ-006, OBJ-008`; `_CONTEXT.md` agrees. Candidate and matrix carry those exact references.
- Stage-1 inventory agrees on candidate/source/status hashes, 31 mappings, 370 mapped lines, lifecycle `IN_PROGRESS`, objective references, and PASS results. Fresh map is byte-identical; parity is semantically identical; render hash is identical; checklist AC/VER identity is unchanged under the amendment's current `SOW_V1` state.
- Project status fingerprint was empty before and after verification; `HEAD` and `main` both equal the accepted current base. Candidate, source, status, lifecycle, control, history, Git, and live project bytes were not modified.

## Future atomic replacement evidence

- `REPLACEMENT_MANIFEST.tsv` has exactly five data rows: one `ADD ScopeOfWork.md` at the candidate hash and four `DELETE` rows at the P3 source hashes.
- `_STATUS.md` and every control/lifecycle path are absent from the action set and remain byte-identical. This manifest is evidence only and was not applied.

## Result classes

- Schema/project-content: `PASS`.
- Source/status preservation and replacement containment: `PASS`.
- Execution substrate/write containment: `PASS`.
- Conflicts, blockers, waivers, repairs, and rerun requirements: none at the recorded hashes.
