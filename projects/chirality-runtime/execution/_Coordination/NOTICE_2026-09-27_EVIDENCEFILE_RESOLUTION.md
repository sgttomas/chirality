# EVQ-006 resolves EvidenceFile in each allowed form

Owner-directed Root tranche `ROOT-EVIDENCEFILE-RESOLUTION-20260927` (manifest `docs/governance_harness/tranche_manifests/ROOT-EVIDENCEFILE-RESOLUTION-20260927.yaml`) changes `tools/validation/validate_decomposition_registers.py`, which every loop that checks decomposition registers runs:
- **`EVQ-006` now tries three bases and fires only when none names a regular file.** The validator used to resolve `EvidenceFile` only from the project root (the parent of the execution root). Root SPEC §6.5 calls the cell "the source document filename", and `dependency-extract` writes `EvidenceFile=_DEPENDENCIES.md`, so a bare filename relative to the deliverable folder is a valid form. SPEC §0.2.4 adds working-root references and instruction-root references. The validator now tries the deliverable folder, then the working root (`--evidence-root`), then the instruction root (new `--instruction-root`, default: the checkout holding the tool).
- **Still findings.** Absolute paths, paths that leave both roots, directories and files that exist in no form. The JSON report gains `instruction_root` and `evidence_file_resolution_forms`.
- **Unchanged.** Every other check, its severity and the exit codes. No register was edited.

The owner's direction, 2026-09-27: "You can take care of those remaining items now.  Include the items with the "other owners".  You can make changes as necessary."

Runtime-specific: `EVQ-006` falls from 54 to 0. All 54 cells resolve instruction-root-relative: 42 checkout-relative `projects/chirality-runtime/...` paths and 12 cells citing Root's `execution/_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN/DEPENDENCY_DISTRIBUTION.csv`. The other findings are unchanged: 54 `DRB-001`, 54 `DRB-006` and 42 `EVQ-003`, so the exit code is still 1. The XRG family still skips this loop. This loop decides its own adoption; this source tranche grants no release.
