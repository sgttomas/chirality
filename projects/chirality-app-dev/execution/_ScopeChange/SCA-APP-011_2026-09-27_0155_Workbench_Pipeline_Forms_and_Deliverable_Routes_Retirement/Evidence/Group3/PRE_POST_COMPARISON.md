# SCA-APP-011 pre/post coverage comparison (group-3 candidate)

Pre: `Pre_Change_Coverage.json` (accepted group-1 baseline, basis `5843c0b8c`). Post: `Post_Change_Coverage.json` (candidate, basis `3f75abfab`).

| Field | Equal | Pre | Post |
|---|---|---|---|
| repository_topology | yes | `{"deliverables": 52, "ledger_rows": 84, "objectives": 10, "packages": 10, "retired_deliverables": ["DEL-09-07"], "scope_items": 84}` | `{"deliverables": 52, "ledger_rows": 84, "objectives": 10, "packages": 10, "retired_deliverables": ["DEL-09-07"], "scope_items": 84}` |
| ledger_distribution | yes | `{"IN": 78, "OUT": 5, "TBD": 1}` | `{"IN": 78, "OUT": 5, "TBD": 1}` |
| context_envelopes | yes | `{"L": 2, "M": 41, "S": 9}` | `{"L": 2, "M": 41, "S": 9}` |
| forward_coverage | yes | `{"declared": 52, "found": 52, "missing_folders": []}` | `{"declared": 52, "found": 52, "missing_folders": []}` |
| reverse_coverage | yes | `{"folders": 54, "undeclared_folders": ["DEL-00-01", "DEL-00-02"]}` | `{"folders": 54, "undeclared_folders": ["DEL-00-01", "DEL-00-02"]}` |
| scope_items_without_deliverable | yes | `[]` | `[]` |
| objectives_without_deliverable | yes | `[]` | `[]` |
| lifecycle_distribution | yes | `{"IN_PROGRESS": 53, "OPEN": 1}` | `{"IN_PROGRESS": 53, "OPEN": 1}` |
| issued_deliverables | yes | `[]` | `[]` |
| affected_lifecycle | **no** | `{"DEL-02-01": "IN_PROGRESS", "DEL-02-02": "IN_PROGRESS", "DEL-02-03": "IN_PROGRESS", "DEL-03-03": "IN_PROGRESS", "DEL-05-01": "IN_PROGRESS", "DEL-07-02": "IN...` | `{"DEL-02-01": "IN_PROGRESS", "DEL-02-02": "IN_PROGRESS", "DEL-02-03": "IN_PROGRESS", "DEL-03-03": "IN_PROGRESS", "DEL-05-01": "IN_PROGRESS", "DEL-07-01": "IN...` |
| audit_structure.run_status | yes | `"COMPLETE"` | `"COMPLETE"` |
| audit_structure.subject_status | yes | `"FAIL"` | `"FAIL"` |
| audit_structure.summary | yes | `{"fail": 0, "lifecycle_states": {"IN_PROGRESS": 53, "OPEN": 1}, "partitions": 11, "pass": 54, "production_formats": {"SOW_V1": 54}, "units": 54}` | `{"fail": 0, "lifecycle_states": {"IN_PROGRESS": 53, "OPEN": 1}, "partitions": 11, "pass": 54, "production_formats": {"SOW_V1": 54}, "units": 54}` |
| audit_structure.issue_count | yes | `2` | `2` |
| audit_structure.target_unit | yes | `{"current_state": "IN_PROGRESS", "production_format": "SOW_V1", "valid": true}` | `{"current_state": "IN_PROGRESS", "production_format": "SOW_V1", "valid": true}` |
| analyze_dep_closure | yes | `{"accepted_dag": null, "anchor_rows": 275, "bidirectional_pair_count": 0, "cycles_truncated": false, "declared_disagreement_count": 0, "declared_only_rows": ...` | `{"accepted_dag": null, "anchor_rows": 275, "bidirectional_pair_count": 0, "cycles_truncated": false, "declared_disagreement_count": 0, "declared_only_rows": ...` |
| validate_decomposition_registers.findings_by_code | yes | `{"EVQ-006": 592}` | `{"EVQ-006": 592}` |
| validate_decomposition_registers.error_count | yes | `592` | `592` |
| validate_decomposition_registers.exit | yes | `1` | `1` |
| decomposition_sha256 | **no** | `"9261ce30f933a0b72364a5af09c8aeed9208372774959864ff24a805126ea8a6"` | `"dc1314638af4b60608a200ccbbe2fb33c53a45c509b7083338db043c9bc04459"` |
| companion_register_sha256 | yes | `"918e475a48899d18755139027e61db200d23a531e48ed9f969c526dd842fa944"` | `"918e475a48899d18755139027e61db200d23a531e48ed9f969c526dd842fa944"` |
| scope_change_pointer_sha256 | yes | `"6fdba0c96f6d1d6c2dc60c35219fb51f8a9fd9bbee9e390c5653398a742c04e3"` | `"6fdba0c96f6d1d6c2dc60c35219fb51f8a9fd9bbee9e390c5653398a742c04e3"` |
