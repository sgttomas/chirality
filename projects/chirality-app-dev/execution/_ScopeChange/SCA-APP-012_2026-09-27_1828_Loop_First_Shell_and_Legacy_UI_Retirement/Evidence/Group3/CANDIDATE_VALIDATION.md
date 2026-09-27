# SCA-APP-012 group-3 candidate validation

Accepted group-2 commit `dad463311`; candidate revision `c47b74fd5` (integrated scope text and code). Git ran with every `GIT_*` variable removed. The script modifies no scope file and writes only this report.

1. Candidate hashes: 12/12 files match `PREIMAGE_POSTIMAGE.csv`.
2. Non-conditional edits present: 79/79; acceptance-conditional edits withheld: E26; files carrying a `{APPLICATION_DATE}` literal: 0.
3. Write containment (`dad463311..c47b74fd5`): 84 paths changed; scope-text paths 12 (outside the accepted boundary: 0; boundary files not written: 0); code-change paths 55; SCA-folder paths 17; protected paths changed: 0; paths in no permitted category: 0.
4. `validate_scope_of_work.py` on each written Scope of Work:

| Deliverable folder | Exit |
|---|---|
| `DEL-02-01_Desktop_Shell_and_Matrix_Navigation` | 0 |
| `DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI` | 0 |
| `DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts` | 0 |
| `DEL-08-02_Persona_Alias_and_Agent_Matrix_Routing_Contract` | 0 |
| `DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch` | 0 |
| `DEL-07-02_Execution_Root_Scaffolding_from_Decomposition` | 0 |
| `DEL-06-03_Initial_Chirality_MCP_Read_Tools` | 0 |
| `DEL-02-02_Workbench_and_Pipeline_Selection_UX` | 0 |

5. Retired-item sweep: 114 files; uncovered units: 0; listed historical passages: 3.
6. Table rows written by edits checked for column count: 17.
7. Code alignment: cited live files present 19/19; new cited test present 1/1; section-4 deletions still present 0/20; frozen `renderer-window-policy.ts` at its pinned hash: yes.

Result: PASS
