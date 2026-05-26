# Procedure — DEL-050-05 Vendor Document Turnover Package

This procedure describes the operational steps the Package Vendor follows to **produce** the vendor document turnover package for PKG-050 (Stabilizer Overheads Compressors), and the steps the EPC Integrator follows to **consume** it for review. EPC-side acceptance itself is governed by `DEL-050-06`.

## Prerequisites

- Package scope and SOW items `SOW-0173`–`SOW-0176` are defined and current.
- `DEL-050-02_package-datasheet` exists at sufficient maturity to drive vendor documentation expectations.
- `DEL-050-04_vendor-engineered-equipment-package` engineering work is underway or complete.
- Project document control standard (numbering, transmittal, revision, retention) is identified. **TBD — not located in accessible source slices.**
- Vendor has access to applicable codes and standards (compressor-specific). **TBD.**

Declared upstream dependencies in `_DEPENDENCIES.md`: **none declared during PREPARATION.**

## Steps

1. **Initialize the vendor document register.**
   1.1 Create the register with required columns: document number, title, class, revision, submittal type, submittal date, transmittal ID, review status, acceptance state, certified/as-built revision. (Column set: ASSUMPTION pending project document control standard.)
   1.2 Pre-populate one row per anticipated document, mapped to the originating SOW item or requirement.

2. **Enumerate document classes in scope** for PKG-050 Stabilizer Overheads Compressors.
   2.1 Include drawings, calculations, certifications, manuals, ITPs, MTRs, test/inspection records, spares lists, training materials, and any other class the package scope requires. (Class list: ASSUMPTION.)

3. **Issue submittals through controlled transmittals.**
   3.1 For each submittal cycle (for-review → for-approval → certified → as-built), bundle the documents, prepare a transmittal record, and update the register.
   3.2 Capture EPC review responses; advance register state only when response permits.

4. **Maintain source-required documentation traceability.**
   4.1 For every SOW item (`SOW-0173`–`SOW-0176`), confirm at least one register entry exists and is traceable. (Mapping content: TBD pending SOW row text access.)

5. **Compile turnover records.**
   5.1 Confirm each register entry has reached its required final state (typically certified or as-built).
   5.2 Produce the turnover index/binder (electronic and/or physical per project document control standard — TBD).
   5.3 Include test/inspection evidence, certifications, MTRs, and final operations and maintenance materials.

6. **Transmit turnover package to EPC Integrator.**
   6.1 Issue final transmittal with the turnover index, supporting register, and a closure statement confirming all required documentation is included.

7. **Support EPC review.**
   7.1 Respond to EPC Integrator comments raised through `DEL-050-06_epc-vendor-package-review-and-acceptance`.
   7.2 Re-issue any document required for closure; update register and transmittal log accordingly.

## Verification

| Step | Verification |
|---|---|
| 1 | Register exists with required columns and one row per anticipated document. |
| 2 | Document-class coverage check against PKG-050 equipment scope. |
| 3 | Each register-state change has a corresponding transmittal record and EPC response (where applicable). |
| 4 | SOW-to-register traceability matrix complete for `SOW-0173`–`SOW-0176`. |
| 5 | Turnover index complete; sample documents inspected for finality (certified or as-built). |
| 6 | Final transmittal logged; closure statement included. |
| 7 | All `DEL-050-06` review comments dispositioned and closed in the register. |

## Records

- Vendor Document Register (current and revision history).
- Submittal transmittal log.
- Source-required vendor documentation per `SOW-0173`–`SOW-0176`.
- Turnover index / binder.
- Final transmittal and closure statement.
- Review comment disposition log (joint with `DEL-050-06`).
