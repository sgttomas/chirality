# QA Report

- Decomposition SHA-256: `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`.
- Invariant-register SHA-256: `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`.
- Gate-5 deterministic state validator: `PASS`; accepted Gate-3/Gate-4 manifests reproduce, 12 action rows resolve, and no unexpected changed path exists.
- Packages: 10/10 declared folders resolved.
- Deliverables: 51/51 declared folders resolved.
- Contexts: 51/51 present and identity/type/envelope aligned. Two context files carry an accepted named human ResponsibleParty while the decomposition retains `TBD`; the protocol treats this as matching because one side is `TBD`.
- SOW contracts: 51/51 product deliverables contain `chirality-deliverable-sow/v1` with matching package and deliverable IDs.
- Scope Ledger: 78 rows; 73 `IN`, 4 `OUT`, 1 `TBD`; all 73 `IN` rows reference existing packages, deliverables, and objectives.
- Objectives: 10/10 have at least one declared, existing supporting deliverable; no product deliverable lacks objective mapping.
- Lifecycle: all 51 declared product deliverables are `IN_PROGRESS`.
- Companion register: 81 data rows, 81 unique invariant IDs, 48 invariant families; the main document labels it as the authoritative companion and states field-level precedence.
- Whitespace validation: `git diff --check` passes for the changed decomposition and context surfaces.

## Limits and observations

- Check 6 uses the established folder-local anticipated-artifact filename method. SOW_V1 contracts validate, but named implementation artifacts are not matched to deliverable-folder filenames; this yields one warning per declared product deliverable.
- PKG-00 and DEL-00-01/02 are documented control-plane surfaces outside the product decomposition. The protocol still reports them as reverse-only warnings.
- `DEL-03-06` under the historical `PKG-03_Harness_Runtime_Core` root is not declared in the current decomposition and remains a reverse-only warning.
- The active `_ScopeChange/_LATEST.md` points exactly to SCA-APP-006. Its `RUN_SUMMARY.md` and `Handoff_State.md` accurately report complete decomposition truth, incomplete derivative closure, `AuditState=NOT_RUN`, and `ReadyForNextPhase=NO`; no later phase is claimed.
