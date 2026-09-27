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

Runtime-specific: `EVQ-006` stays at 54. All 54 cells are nonconforming checkout-relative paths, and each names a file that exists:
- **42 cells cite `projects/chirality-runtime/...`.** SPEC §0.2.4 says project material resolves relative to the project root, so these paths should drop the `projects/chirality-runtime/` prefix.
- **12 cells cite Root's `execution/_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN/DEPENDENCY_DISTRIBUTION.csv`.** That file lies outside this project's root and outside the instruction surface, so the validator cannot resolve it in any allowed form. This loop needs to decide how to cite it: a copy or pointer in its own records, or a waiver-style note.

These are left for this loop to refresh at its next `dependency-extract` run. The other findings are unchanged: 54 `DRB-001`, 54 `DRB-006` and 42 `EVQ-003`, so the exit code is still 1. The XRG family still skips this loop. This loop decides its own adoption; this source tranche grants no release.
