# SCA-APP-011 group-3 candidate validation

Accepted group-2 commit `e7f6daee1`; integrated candidate revision `3f75abfab`. Read-only; the tree is not modified.

1. Candidate hashes: 16/16 files match their expected group-3 candidate hash (14 group-2 hash, 1 basis refresh, 1 correction); basis refreshes re-derived from their basis commit with the accepted edits: 1/1.
2. Non-conditional edits present: 126/126; acceptance-conditional edits withheld: E47; files carrying a `{APPLICATION_DATE}` literal: 0.
3. Write containment (`e7f6daee1..3f75abfab`): 74 paths changed; scope-text paths 16 (outside the accepted boundary: 0; boundary files not written: 0); code-change and SCA-folder paths 58; protected paths changed: 0; paths in no permitted category: 0.
4. `validate_scope_of_work.py` on each written Scope of Work:

| Deliverable folder | Exit |
|---|---|
| `DEL-07-04_Status_Transition_API_and_MCP_Tool` | 0 |
| `DEL-07-05_Dependencies_csv_v3_1_Reader_Writer_and_Linter` | 0 |
| `DEL-09-03_Unit_and_Integration_Test_Expansion` | 0 |
| `DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch` | 0 |
| `DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI` | 0 |
| `DEL-02-02_Workbench_and_Pipeline_Selection_UX` | 0 |
| `DEL-07-02_Execution_Root_Scaffolding_from_Decomposition` | 0 |
| `DEL-03-03_Harness_API_and_SSE_Compatibility_Adapter` | 0 |
| `DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection` | 0 |

5. Deliverable contracts and contexts swept: 108; uncovered lines naming a retired route or scaffold-route obligation: 0.
6. Table rows written by edits checked for column count: 24.

Result: PASS
