# D-APP-107 — DEL-09-07 Scope of Work initialization repair

Status: RULED (bounded repair authorized; integration pending)

Owner: Ryan Tufts

Date: 2026-09-04

## Conversation provenance

The owner directed PROJECT_SETUP with:

> Proceed accordingly.

HELP_HUMAN then reported the expired structural-bootstrap preflight and asked:

> This exposes an initialization gap we missed at closeout. May I route a narrowly scoped repair through HELPS_HUMANS so PROJECT_SETUP can create DEL-09-07’s Scope of Work?

The owner answered:

> yes.

These quotations are from the current conversation supplied to this run.
The answer authorizes this bounded repair and continuation of the previously
directed initialization. It is not represented as approval of exact, unseen
implementation bytes or acceptance of a future ScopeOfWork.

## Applied design within that direction

Retire the expired D-APP-104 live register row and add the separate typed
`SOW_INITIALIZATION` admission for `DEL-09-07`, `PKG-09`, exact folder
`execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-07_Two-Job_Runtime-Control_Installer_Migration_and_Rollback`.
Preserve D-APP-104 and its proposal as immutable history.

Permit only `dispatch` with declared token `PROJECT_SETUP:SCOPE_OF_WORK:INIT`
while ScopeOfWork is absent. Bind decomposition SHA-256
`e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97`,
companion SHA-256
`e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70`,
post-SCA-009 pointer SHA-256
`f235ced4526aac51c4e7f5307ac619f3500e824c3549960b106bb80b67a6e17c`,
and the five exact scaffold input hashes in `execution/_Scripts/app_hold.py`
(`INIT_SCAFFOLD_HASHES`, sourced from merge `95b5687a7c9a4c6fe6e655f628495dec08ce04d8`).
Allow regular run evidence only beneath `_run_records/`; reject symlinks,
traversal, missing/changed input files, special files, and other root entries.

Contract appearance consumes this initialization admission. The ordinary
scan then governs the exact package/path/target; malformed or HELD contracts
and register mismatch remain blocking. CLEAR is a structural basis result,
not owner acceptance. PROJECT_SETUP retains its skill, brief, review, and
lifecycle obligations. No product, repinning, lifecycle, reliance, acceptance,
release, signing, or distribution act is authorized by this admission.

## Integration and next owner

HELPS_HUMANS prepares the tested App-local guard/register/instruction repair;
HELP_HUMAN handles publication and owner integration. PROJECT_SETUP may then
resume Phase 2.2 under the existing owner direction, use the documented exact
preflight, and dispatch `TASK + scope-of-work`, `MODE=INIT`. This repair creates
no ScopeOfWork itself.
