# Root governance state interface v1

Implementation interface under approved Gate4 plan; no new authority class. All paths repository-relative; hashes SHA256; commit refs full40hex. YAMLs retain their existing v1 schema IDs and add `mode: governance-only`, `governance_state: {path: ..., sha256: ...}`. Omitted mode remains legacy only for existing legacy schema; any other mode is rejected.

State JSON fields:

```json
{
  "schema": "root-governance-state/v1",
  "stage": "prepared",
  "selected_subject": {"path":"execution/_ScopeChange/SCA-005_2026-09-05_2344/FINAL_INTEGRATION_V3/COMBINED_ARTIFACTS.sha256", "sha256":"547d1f3369e71aa96d1b61561f6b1603b978016c7335fca39f86df97ddd73fc3"},
  "propagation_plan": {"path":"execution/_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN/FINAL_ARTIFACTS.sha256", "sha256":"917656f3a828d7e05e2feaf22e14394f1f6dc9fbb26bb99760b633e0ceb17efd"},
  "gate3": {"path":"plans/steers/root_runtime_migration_gate3_approval_2026-09-05.md", "sha256":"ACTUAL", "commit":"PUBLISHED_COMMIT", "subject_sha256":"547d1f3369e71aa96d1b61561f6b1603b978016c7335fca39f86df97ddd73fc3"},
  "gate4": {"path":"plans/steers/root_runtime_migration_gate4_approval_2026-09-05.md", "sha256":"ACTUAL", "commit":"PUBLISHED_COMMIT", "subject_sha256":"917656f3a828d7e05e2feaf22e14394f1f6dc9fbb26bb99760b633e0ceb17efd"},
  "gate5": null,
  "successor_bindings": [{"source_id":"SOURCE_FULL_ID", "target":"GOV-XX-YY or chirality-runtime::DEL_FULL_ID", "path":"GOV_FILE or RUNTIME_SCOPEOFWORK_FILE", "sha256":"ACTUAL", "authority":{"path":"ACTUAL_ACCEPTANCE_WRAPPER", "sha256":"ACTUAL"}, "write_targets":["EXACT_SCOPE_OR_TERMINAL_/**"]}],
  "transaction": null
}
```

Stage values: prepared, applied_pending_confirmation, effective. Prepared contains pre-retirement source statuses. Applied pending confirmation contains exact approved RETIRED postimages but supplies no effective transfer or production eligibility. Effective additionally requires actual published Gate5 owner record (same ref shape) and `effect_subject_sha256` binding the exact confirmed application subject. No guessed acceptance fields. Each binding target is identity; path is the actual record. Exactly46 GOV files and7 runtime ScopeOfWork paths correspond to approved53 map. Authority wrapper is actual acceptance/application reference, never a substitute for selected Gate3 bytes. All bindings must resolve at application; prepared scaffolding may be constructed after successors exist and before retirement.

Module `tools/validation/root_governance_state.py` exports `GovernanceError`, `safe_path(root, relative, allow_missing=False)`, `verify_owner_act(root, ref, expected_subject_sha)`, `load_governance_state(root, config, require_effective=False, verify_statuses='postimage')`. Status choices preimage, postimage, either; no status check may be silently skipped. Load returns state plus `source_statuses` list of path/source_id/source_package/preimage_sha256/postimage_sha256/postimage_path/successor, `source_ids`, `governance_ids`, `runtime_ids` and `successors` (normalized binding list). Approved map/source/postimage facts are derived from hash-pinned Gate4 plan and selected Gate3 V3, not caller-provided counts.

GOV binding write targets must be confined to approved migration governance targets (Gate4 WRITE_TARGETS + GUARDS WRITE_PATH_INVENTORY) or that control's own record/evidence subtree; they cannot cover a project, retired source carrier or repository wholesale. Runtime bindings are observational project ownership and confined to that carrier's runtime project directory, never a Root product grant. Any later operational feature scope remains a separate accepted project instrument.

Transaction reference may name an actual immutable completed journal or null. Pending/blocked transaction journal refuses production dispatch; structural checks may inspect it. Avoid cycles: prepared subject and completed journal and applied state are distinct objects, so a completed journal may pin prepared subject while applied state pins completed journal. No file embeds its own hash.

Owner validation requires ref bytes match current declared path and Git at declared commit, commit reachable from origin/main, and exact expected subject present in the actual owner record. Tests may mock this boundary for other unit cases but no production fixture bypass exists. Readonly scratch prospective validation may use read-only Git metadata pointing to the real published repository.

## Reviewed implementation refinements

Applied pending state requires a transaction reference; a prospective dry-run may precede creation of that journal. Mutable pending journal uses sha256 null; actual effective state requires hash-pinned journal schema root-retirement-journal/v1, state APPLIED, all53 exact entries and no blockers. G3 independently refuses any active dispatch during an absent/pending/blocked transaction.

Effective Gate5 uses a distinct published plans/steers/root_runtime_migration_gate5_confirmation_DATE.md, binds the exact completed journal digest and application subject. effect_subject is the path/hash reference to that root-retirement-application/v1 subject and effect_subject_sha256 equals its digest and the journal subject. Its prepared governance state fixes all successor/authority bindings and selected intent. The only permitted state transition differences are actual stage/Gate5/transaction/effect evidence. effect_configuration is four {target,path,sha256} references to tested original YAML snapshot bytes: current configs may change only governance_state references, not tested ownership/guard/adapter/graph intent. Tested implementation remains hash-bound. No Gate5 record exists during this execution; effective dispatch must fail closed.

Core also verifies exact accepted live runtime PRD and four decomposition registers, derives nine held IDs from the approved hold map, and permits no runtime feature capabilities in Root migration dispatch (unknown aliases/nonstring values also refused). Distinct execution_class governance-migration follows actual published Gate4 for bounded preparation/application; governance-operation requires actual effective confirmation. This removes the circular migration precondition without granting product activation.
