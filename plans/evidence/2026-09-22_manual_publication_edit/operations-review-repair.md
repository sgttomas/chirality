# Independent-review repair — Task Management wording

Date: 2026-09-22
Reviewer: `/root/operational_review`, independent from the author.
Repair authorization: parent `/root` follow-up assigned the narrow documentation repair and publisher coordination.

- Reviewed preimage SHA-256: `fac5bfec4fa227864e850123d5ad568b4b00eff94223ae63b1b566b57af7de71`.
- Repaired User Manual v2 SHA-256: `8e0782a12c9cd845d46b912c2c0dd34d90ea331b2cebd922add27fa356de86da`.

## Findings and exact repair

1. **Projection storage.** K-TM-2 and the mandatory federation preflight require a derived, rebuildable, gitignored output. The old arbitrary `--out` template omitted the last requirement; the utility does not enforce Git ignoring for an arbitrary output. The example now omits `--out`, using the implemented `<register-home>/.candidates/federation.json` default, and explicitly requires verifying the exact destination is authorized and gitignored. Its directory name is not evidence of that property; explicit override paths need the same checks.
2. **Mode selection.** A six-item numbered account could suggest every mode runs on every invocation. Added the qualifier to run only requested modes and authorized follow-up after the required federation preflight, and stated the actual no-mode default: open-row state, staleness and closure-echo presentation, then await direction.

## Rechecked basis

- `workflows/task-management/resources/contract.md`: K-TM-2, invocation-local federation, mandatory preflight and projection standing.
- `workflows/task-management/resources/method.md`: optional inputs and no-mode default.
- `tools/taskmgmt/taskmgmt.py`: `federation()` default output expression and explicit-output treatment.

Exact hashes remain in `operations-sources.json`. Prior help-interface witnesses remain applicable because no interface changed. `operations-validation.json` contains current link/anchor/source-hash checks and focused repair checks. No policy, register or tool was changed and no Task Management operation ran. The independent reviewer receives the new candidate for backcheck; the HTML publisher receives notice to rerender.
