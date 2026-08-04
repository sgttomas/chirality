# Hash-binding and application procedure

Status: `BLUEPRINT — PROCEDURE NOT EXECUTED`

## Stage 0 — prerequisites

Do not instantiate a candidate until all are true:

1. The exact S2 reconciliation candidate was separately presented and owner-
   accepted.
2. S2 was applied and validated under its Gate 5.
3. The applied PRD and decomposition current-facing acceptance/status text is
   internally consistent with the accepted records.
4. S2 supplies exact values for every allowed `{{S2_*}}` placeholder.
5. The candidate staging path and integration owner are declared, empty, and
   outside the live `accepted_inputs/` directory.

## Stage 1 — instantiate immutable content files

1. Copy the five non-manifest templates to their exact final basenames in a
   new staging directory under this run root.
2. Substitute only the verified S2 values enumerated by
   `PROVENANCE_CONTRACT.md`.
3. Confirm zero `{{...}}` token remains.
4. Run candidate whitespace and `validate_candidate_packet.py --content-only`.
5. Freeze the five content files. Any later edit restarts Stage 1.

## Stage 2 — manifest and candidate-set identity

1. Compute SHA-256 for the five content files from exact bytes.
2. Write exactly five sorted manifest lines using lowercase hex, two spaces,
   and basename. Do not include the manifest itself.
3. Run `validate_candidate_packet.py` and require PASS.
4. Compute SHA-256 of `CANDIDATE_SET_MANIFEST.sha256`. This digest is
   `CandidateSetManifestSHA256`.
5. Recompute all five file hashes and manifest identity a second time. Require
   byte-identical results.
6. Record the candidate directory, six file hashes, manifest identity,
   validator hash/results, S2 applied identities, and Git observation in a
   presentation record outside the six-file packet.

The manifest cannot contain its own hash. The owner acceptance record is also
outside the packet, so neither operation changes the candidate bytes.

## Stage 3 — owner presentation and acceptance

Present all six exact files, the manifest identity, validation results,
non-reconstruction statement, S2 bindings, and no-effect boundary. The exact
acceptance line begins `ACCEPT DEL-02-06 INPUT PACKET`, followed by one space,
the exact lowercase 64-hex candidate-manifest SHA-256, ` — Ryan Tufts `, and
the ruling date in ISO `YYYY-MM-DD` form.

The owner may accept, return, or defer. Only the exact returned token is
recorded verbatim in the external acceptance record. The acceptance record
also stores token byte length and SHA-256. An acceptance with another manifest
identity does not apply. Any content edit invalidates the presentation and
requires a new manifest plus new owner act.

## Stage 4 — copy exact accepted bytes to the live input root

Only after valid owner acceptance:

1. Verify the candidate directory again without mutation.
2. Create the previously absent live directory at
   `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-RUNTIME-SPEC-001/accepted_inputs/`.
3. Copy exactly the six accepted files; add no acceptance record to that
   directory.
4. Compare each copied file byte-for-byte with the accepted candidate.
5. Recompute the content hashes and manifest identity twice.
6. Write an application evidence record outside `accepted_inputs/` binding the
   acceptance record, candidate manifest identity, live copy identities, S2
   applied basis, and zero foreign/runtime/lifecycle effects.

## Stage 5 — fresh N0

Only after Stages 0–4 pass, dispatch a fresh N0 using
`N0_RERUN_BRIEF.md`. N0 independently verifies the live packet, external owner
acceptance, applied S2 basis, lifecycle, profile absence, dependencies, and
write containment. It does not rely on the preparation manager's validation.

No stage authorizes runtime implementation, semantic adoption, client work,
lifecycle transition, release, or Task Management closure.
