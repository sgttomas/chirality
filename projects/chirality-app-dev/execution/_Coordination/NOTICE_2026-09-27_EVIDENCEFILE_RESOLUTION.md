# EVQ-006 resolves EvidenceFile in each allowed form

Owner-directed Root tranche `ROOT-EVIDENCEFILE-RESOLUTION-20260927` (manifest `docs/governance_harness/tranche_manifests/ROOT-EVIDENCEFILE-RESOLUTION-20260927.yaml`) changes `tools/validation/validate_decomposition_registers.py`, which every loop that checks decomposition registers runs:
- **`EVQ-006` now tries three forms and fires only when none names a regular file.** The validator used to resolve `EvidenceFile` only from the project root (the parent of the execution root). The forms now tried are:
  1. relative to the deliverable folder. Root SPEC §6.5 calls the cell "the source document filename", and `dependency-extract` writes `EvidenceFile=_DEPENDENCIES.md`;
  2. relative to the project root (`--evidence-root`), per SPEC §0.2.4;
  3. relative to the instruction root, but only for the instruction surface SPEC §0.2.4 names: `agents/`, `workflows/`, `tools/`, root `docs/` and `AGENTS.md`. The instruction root is `--instruction-root`, else `CHIRALITY_INSTRUCTION_ROOT`, else the checkout holding the tool.
- **Still findings.** Checkout-relative paths to project material (`projects/<name>/...`), paths that leave the project root, absolute paths, directories and files that exist in no form.
- **Order matters.** Forms are tried in the order above. A bare name missing from the deliverable folder can resolve to a same-named file at the project root. The JSON report gains `instruction_root`, `instruction_root_source`, `evidence_file_resolution_forms` and `evidence_file_multi_form`.
- **Unchanged.** Every other check, its severity and the exit codes. No register was edited.

The owner's direction, 2026-09-27: "You can take care of those remaining items now.  Include the items with the "other owners".  You can make changes as necessary."

App-specific: `EVQ-006` falls from 644 to 84. Of the resolved cells, 559 are relative to the deliverable folder, 13 to the project root and 1 to the instruction root (`workflows/dependency-extract/...`). The 84 that remain:
- **61 cells (59 `ACTIVE`, 2 `RETIRED`) are nonconforming checkout-relative paths** (`projects/chirality-app-dev/...`). Each names a file that exists, but SPEC §0.2.4 says project material resolves relative to the project root, so the path should drop the `projects/chirality-app-dev/` prefix. They are left for this loop to refresh at its next `dependency-extract` run.
- **23 `RETIRED` rows name a four-document-kit file** (`Procedure.md`, `Specification.md`, `Datasheet.md` or `Guidance.md`) that is no longer in the deliverable folder. These files really are missing.

The exit code is still 1. This loop decides its own adoption; this source tranche grants no release.
