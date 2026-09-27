# XRG-004 allows supporting deliverables in another Package

Notice only; no action is requested of this loop. PEC is being redeveloped and the owner is deferring action on findings until that settles.

Owner-directed Root tranche `ROOT-XRG004-SUPPORTING-DELIVERABLES-20260926` (manifest `docs/governance_harness/tranche_manifests/ROOT-XRG004-SUPPORTING-DELIVERABLES-20260926.yaml`) changes `tools/validation/validate_decomposition_registers.py`:
- **`XRG-004` is now a WARNING and fires only when an item's home Package holds none of its linked deliverables.** It was an ERROR for every linked deliverable outside the item's `PackageID`. Under D-GOV-48 and management manual v7, a linked deliverable in another Package is a supporting contribution, not a finding.
- **New option `--registers-dir DIR`** reads the companion registers from a folder other than `<EXECUTION_ROOT>/_Decomposition/`. The default is unchanged.

The owner's ruling, 2026-09-26: "Warn only if home holds none (Recommended)".

PEC-specific: `validate_decomposition_registers.py projects/pec/execution --families XRG` reports the same result before and after this change: 26 `XRG-013` warnings, no errors, exit 0. This tranche does not edit PEC's registers.
