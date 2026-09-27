# SCA-APP-012 group-2 postimage validation

Dry run with `{APPLICATION_DATE}` = `2099-01-01` (placeholder). Nothing in the tree is modified.

1. Edits applied in sequence: 80 in 12 files; `old` passages not found exactly once: 0.
   Table rows checked on edited passages: 17; pipe-count mismatches: 0.
2. `validate_scope_of_work.py` on each edited Scope of Work (exit code before → after):

| Deliverable folder | Before | After |
|---|---|---|
| `DEL-02-01_Desktop_Shell_and_Matrix_Navigation` | 0 | 0 |
| `DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI` | 0 | 0 |
| `DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts` | 0 | 0 |
| `DEL-08-02_Persona_Alias_and_Agent_Matrix_Routing_Contract` | 0 | 0 |
| `DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch` | 0 | 0 |
| `DEL-07-02_Execution_Root_Scaffolding_from_Decomposition` | 0 | 0 |
| `DEL-06-03_Initial_Chirality_MCP_Read_Tools` | 0 | 0 |
| `DEL-02-02_Workbench_and_Pipeline_Selection_UX` | 0 | 0 |

3. Edited paragraphs naming a retired item or loop-first obligation without an SCA-APP-012 marker: 0.
4. Retired items named with an SCA-APP-012 marker: 19/19; retired routes left in the PRD §9.2 or SPEC §17.2 table: 0.
5. Register rows: 24; rows with their own edits: 23; rows carried by other rows' edits: [24]; rows with neither: []; edits naming an unknown row: [].
6. Files swept: 114 (every deliverable `ScopeOfWork.md` and `_CONTEXT.md`, the decomposition, PRD, SPEC, PLAN, DIRECTIVE and TYPES). Lines naming a retired item or keeping a retired obligation without an SCA-APP-012 marker: 0 uncovered; 0 in files whose SCA-APP-012 controlling section governs them; 3 listed historical passages. The same sweep over the current bytes (before the amendment) finds 39 such units, which the edits address.

   Historical passages, unchanged:

   - `DEL-02-02_Workbench_and_Pipeline_Selection_UX` L172: DEL-02-02 CLM-003 Workbench and Pipeline content, retired as history by its SCA-APP-011 controlling section
   - `DEL-07-02_Execution_Root_Scaffolding_from_Decomposition` L477: Closed Task Management record APP-R058 (closed by SCA-APP-011); history, unchanged (Impact Assessment §9)
   - `_Decomposition` L675: SCA-APP-004 §13 note kept as history; the new SCA-APP-012 §13 note (E23) says it ends that compatibility period

Result: PASS
