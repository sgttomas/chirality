# EVQ-006 resolves EvidenceFile in each allowed form

Notice only; no action is requested of this loop. PEC is being redeveloped and the owner is deferring action on findings until that settles.

Owner-directed Root tranche `ROOT-EVIDENCEFILE-RESOLUTION-20260927` (manifest `docs/governance_harness/tranche_manifests/ROOT-EVIDENCEFILE-RESOLUTION-20260927.yaml`) changes `tools/validation/validate_decomposition_registers.py`:
- **`EVQ-006` now tries three bases and fires only when none names a regular file:** the deliverable folder (the bare-filename form of Root SPEC §6.5), the working root (`--evidence-root`), then the instruction root (new `--instruction-root`, default: the checkout holding the tool), per SPEC §0.2.4. Absolute paths, paths that leave both roots, directories and files that exist in no form are still findings.
- **Unchanged.** Every other check, its severity and the exit codes.

The owner's direction, 2026-09-27: "You can take care of those remaining items now.  Include the items with the "other owners".  You can make changes as necessary."

PEC-specific: `validate_decomposition_registers.py --strict projects/pec/execution` gives the same findings before and after this change: 26 `XRG-013` warnings and no errors, so it exits 1 under `--strict` and 0 without it, as before. All 285 `EvidenceFile` cells resolve working-root-relative, as before. This tranche does not edit PEC's registers.
