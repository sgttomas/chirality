# QA Report

- Decomposition SHA-256: `69b3110c26cb0b435ced4144845282bf6905cde4c0474b21282b9a1806984946`.
- Gate-3 concordance artifact SHA-256: `5cad671098a637aff150004a79a3e32a162d0df5a5dd26ef26796e8b788830c2`.
- Gate-3 concordance rerun: `PASS: 31 SOW; 5 PKG; 17 DEL; 5 OBJ; 25 contexts; U1-U5 preserved`.
- Packages: 10/10 declared folders resolved.
- Deliverables: 51/51 declared folders resolved.
- Contexts: 51/51 present and identity/type/envelope aligned. Two context files carry an accepted named human ResponsibleParty while the decomposition retains `TBD`; the protocol treats this as matching because one side is `TBD`.
- SOW contracts: 51/51 product deliverables contain `chirality-deliverable-sow/v1` with matching package and deliverable IDs.
- Scope Ledger: 78 rows; 73 `IN`, 4 `OUT`, 1 `TBD`; all 73 `IN` rows reference existing packages, deliverables, and objectives.
- Objectives: 10/10 have at least one declared, existing supporting deliverable; no product deliverable lacks objective mapping.
- Lifecycle: all 51 declared product deliverables are `IN_PROGRESS`.
- Whitespace validation: `git diff --check` passes for the changed decomposition and context surfaces.

## Limits and observations

- Check 6 uses the established folder-local anticipated-artifact filename method. SOW_V1 contracts validate, but named implementation artifacts are not matched to deliverable-folder filenames; this yields one warning per declared product deliverable.
- PKG-00 and DEL-00-01/02 are documented control-plane surfaces outside the product decomposition. The protocol still reports them as reverse-only warnings.
- `DEL-03-06` under the historical `PKG-03_Harness_Runtime_Core` root is not declared in the current decomposition and remains a reverse-only warning.
- The active `_ScopeChange/_LATEST.md` correctly remains on complete SCA-APP-004 until SCA-APP-005 closure artifacts, including this audit, are finalized by the managing SCOPE_CHANGE instance.
