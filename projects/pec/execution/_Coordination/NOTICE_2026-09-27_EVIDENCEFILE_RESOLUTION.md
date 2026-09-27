# EVQ-006 resolves EvidenceFile in each allowed form

Notice only; no action is requested of this loop. PEC is being redeveloped and the owner is deferring action on findings until that settles.

Owner-directed Root tranche `ROOT-EVIDENCEFILE-RESOLUTION-20260927` (manifest `docs/governance_harness/tranche_manifests/ROOT-EVIDENCEFILE-RESOLUTION-20260927.yaml`) changes `tools/validation/validate_decomposition_registers.py`:
- **`EVQ-006` now tries three forms and fires only when none names a regular file.** The validator used to resolve `EvidenceFile` only from the project root (the parent of the execution root). The forms now tried are:
  1. relative to the deliverable folder. Root SPEC §6.5 calls the cell "the source document filename", and `dependency-extract` writes `EvidenceFile=_DEPENDENCIES.md`;
  2. relative to the project root (`--evidence-root`), per SPEC §0.2.4;
  3. relative to the instruction root, but only for the instruction surface SPEC §0.2.4 names: `agents/`, `workflows/`, `tools/`, root `docs/` and `AGENTS.md`. The instruction root is `--instruction-root`, else `CHIRALITY_INSTRUCTION_ROOT`, else the checkout holding the tool.
- **Still findings.** Checkout-relative paths to project material (`projects/<name>/...`), paths that leave the project root, absolute paths, directories and files that exist in no form.
- **Order matters.** Forms are tried in the order above. A bare name missing from the deliverable folder can resolve to a same-named file at the project root. The JSON report gains `instruction_root`, `instruction_root_source`, `evidence_file_resolution_forms` and `evidence_file_multi_form`.
- **Unchanged.** Every other check, its severity and the exit codes.

The owner's direction, 2026-09-27: "You can take care of those remaining items now.  Include the items with the "other owners".  You can make changes as necessary."

PEC-specific: `validate_decomposition_registers.py --strict projects/pec/execution` gives the same findings before and after this change: 26 `XRG-013` warnings and no errors, so it exits 1 under `--strict` and 0 without it, as before. All 285 `EvidenceFile` cells resolve relative to the project root, as before. This tranche does not edit PEC's registers.
