# Scaffold Contract

## Operation map

| Operation | Required accepted input | Result |
|---|---|---|
| Package hierarchy | package ID and name | package lifecycle directories |
| Package references | package identity and available references | files or `_REFERENCE_INDEX.md` |
| Deliverable fileset | deliverable and package fields plus decomposition reference | five control files |
| Aggregation prerequisites | execution root | `_Aggregation` root and neutral templates |
| Category hierarchy | category ID and name | category lifecycle directories |
| Knowledge-type fileset | knowledge-type and category fields plus decomposition reference | five control files |
| Domain tool roots | execution root | hypergraph and closure structural roots |

## Tool operations

Resolve commands against the tool root.

- Package or category hierarchy: `tools/scaffolding/scaffold_package.sh`.
- Deliverable or knowledge-type folder: `tools/scaffolding/scaffold_deliverable.sh <package-or-category>/1_Working <ID> <Label>`. It creates `{ID}_{Label}` under the parent's `1_Working/` with empty control-file stubs. Add `--memory` only when `MEMORY.md` is selected and authorized; the tool refuses when a legacy `_MEMORY.md` exists, so report that instead of working around it.
- Aggregation prerequisites: `tools/scaffolding/scaffold_tool_root.sh {EXECUTION_ROOT} _Aggregation`, then create any missing `_Aggregation/_Templates/AGGREGATION_BRIEF_TEMPLATE.md` (neutral headings only) and `_Aggregation/_Templates/TARGET_SCHEMA_TEMPLATE.csv` (header row only).
- Domain tool roots: `tools/scaffolding/scaffold_tool_root.sh {EXECUTION_ROOT}/_Aggregation Hypergraph` and `tools/scaffolding/scaffold_tool_root.sh {EXECUTION_ROOT}/_Evaluation HypergraphClosure`.

Package and category lifecycle hierarchies contain `0_References/`, `0_References/_Archive/`, `1_Working/`, `1_Working/_Archive/`, `2_Checking/`, `2_Checking/From/`, `2_Checking/To/`, `3_Issued/`, and `3_Issued/_Archive/`.

## Context files

A deliverable `_CONTEXT.md` records its ID and canonical name, package ID and canonical name, discipline, type, responsible party, exact accepted description, anticipated artifacts, decomposition path, and deliverable ID.

A knowledge-type `_CONTEXT.md` records its ID and canonical name, category ID and canonical name, discipline, type, responsible party, exact accepted description, anticipated artifacts, decomposition path, knowledge-type ID, and category ID.

Do not normalize or embellish accepted field values. Use `TBD` only when the accepted source itself is unresolved, and report that condition.

## Dependency file

`_DEPENDENCIES.md` is a durable container with:

- a human-owned coordination mode: `NOT_TRACKED`, `DECLARED`, or `FULL_GRAPH`;
- human-declared upstream and downstream entries, including reason, required maturity, and location when supplied;
- an extracted dependency-register section initialized to `NOT_RUN_YET`;
- run-history, lifecycle-summary, and consumer-handoff placeholders.

Do not infer dependency edges. For `NOT_TRACKED`, state that humans coordinate dependencies externally.

## Remaining control files

- `_STATUS.md`: when the file is newly created, including an empty stub from
  the scaffolder, write exactly this form, naming the actual actor:

  ```markdown
  # Status: <ID> <Name>

  **Current State:** OPEN
  **Last Updated:** <YYYY-MM-DD>

  ## History
  - <YYYY-MM-DD> — State set to OPEN (<actor>)
  ```

  `tools/scaffolding/write_status.sh` parses the `**Current State:**` line for
  later transitions and cannot initialize an empty stub.
- `_REFERENCES.md`: list supplied reference names or IDs, locations, and relevance; otherwise state that references are not yet identified.
- `_SEMANTIC.md`: create a `PLACEHOLDER` lens with no engineering assertions. A later semantic workflow may replace it.
- `MEMORY.md`: optional and outside the minimum fileset. Create it only when explicitly selected and authorized, filling it from `docs/templates/MEMORY_TEMPLATE.md` (the terse `## Runs` index). Do not create a future-work list.

Aggregation templates, when requested, are structural only. The target-schema CSV begins with `RecordID,SourceID,SourcePath,SectionRef,EntityType,Key,Value,Notes,Confidence,Tags` and no data rows.
