# WORKING_ITEMS launch brief — DEL-01-05 contract currency

RequestedBy: HELP_HUMAN
RunID: PEC-DPEC77-78-20260802
InstanceID: working-items-del0105
PackageID: PKG-01
PackagePath: `projects/pec/execution/PKG-01_Service_Core_Store/`
SelectedDeliverables: `DEL-01-05`

## Objective

Execute only D-PEC-77 O-A phase 1: repair the exact DEL-01-05
`ScopeOfWork.md` currency statements within packet §3.1, validate unchanged
SOW_V1 structure and AC-001 through AC-011, and return evidence for the next
owner REVIEW gate.

## Authority

Owner ruling `D-PEC-77: O-A; CON-002: G-A`; packet SHA-256
`f848d55557d4b59d4c425e3924b850d634011a4a7db6c6fbd2eee9fc46cc5c31`.

## Declared reads

D-PEC-77 packet and decision record; accepted PRD v2.2 and decomposition
revision 1.3; DEL-00-01 accepted ADRs; DEL-01-05 context/status/references;
live PEC v2 core and project workflow profile; D-PEC-75 handoff.

## Allowed write targets

- `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/ScopeOfWork.md`
- this instance's `RETURN.md` and `STATUS.json`

No other file may change. In particular, no source, test, workflow profile,
status, review, register, decomposition, decision record, receipt, or Task
Management write is authorized.

## Return contract

Return exact pre/post SHA-256, line-level change summary mapped to packet
§3.1 items 1–7, SOW validator result, deterministic checklist identity and
count, requirement/AC/VER preservation, changed-path containment, open gates,
and any blocker. Source production remains dormant.
