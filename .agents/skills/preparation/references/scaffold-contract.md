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

- Package or category hierarchy: `tools/scaffolding/scaffold_package.sh <EXECUTION_ROOT> <ID> <Label>`.
- Identifier check: `tools/validation/validate_id_format.sh <PKG|DEL|CAT|KTY> <ID>`.
- Deliverable or knowledge-type folder: `tools/scaffolding/scaffold_deliverable.sh <package-or-category>/1_Working <ID> <Label>`. It creates `{ID}_{Label}` under the parent's `1_Working/` with empty control-file stubs. Add `--memory` as the fourth argument only when `MEMORY.md` is selected and authorized; the tool refuses when a legacy `_MEMORY.md` exists, so report that instead of working around it.
- Aggregation prerequisites: `tools/scaffolding/scaffold_tool_root.sh {EXECUTION_ROOT} _Aggregation`, then create any missing `_Aggregation/_Templates/AGGREGATION_BRIEF_TEMPLATE.md` (neutral headings only) and `_Aggregation/_Templates/TARGET_SCHEMA_TEMPLATE.csv` (header row only).
- Domain tool roots: `tools/scaffolding/scaffold_tool_root.sh {EXECUTION_ROOT}/_Aggregation Hypergraph` and `tools/scaffolding/scaffold_tool_root.sh {EXECUTION_ROOT}/_Evaluation HypergraphClosure`.

Package and category lifecycle hierarchies contain `0_References/`, `0_References/_Archive/`, `1_Working/`, `1_Working/_Archive/`, `2_Checking/`, `2_Checking/From/`, `2_Checking/To/`, `3_Issued/`, and `3_Issued/_Archive/`.

## Context files

A deliverable `_CONTEXT.md` records its ID and canonical name, package ID and canonical name, discipline, type, responsible party, exact accepted description, anticipated artifacts, decomposition path, and deliverable ID.

A knowledge-type `_CONTEXT.md` records its ID and canonical name, category ID and canonical name, discipline, type, responsible party, exact accepted description, anticipated artifacts, decomposition path, knowledge-type ID, and category ID.

Do not normalize or embellish accepted field values. Use `TBD` only when the accepted source itself is unresolved, and report that condition.

## Dependency file

`_DEPENDENCIES.md` is a durable container whose single heading schema is `docs/SPEC.md` §5.2 (D-GOV-46). Humans or the coordinating workflow own the three declared sections; `dependency-extract` later fills the extracted sections, keeps the declared sections and their headings unchanged, and adds any missing section under its §5.2 heading. When the file is newly created, including an empty stub from the scaffolder, write exactly this skeleton, using `KTY`/category labels for a knowledge type. Take the mode from the coordination record (`NOT_TRACKED`, `DECLARED` or `FULL_GRAPH`; SPEC §5.3). Do not infer dependency edges. Do not rewrite an existing file to this skeleton.

```markdown
# Dependencies: [DEL-ID] [Deliverable Name]

## Dependency Tracking Mode
- **Mode:** [NOT_TRACKED | DECLARED | FULL_GRAPH]
- **Register:** the declared sections of this file together with Dependencies.csv (schema v3.1) when present (docs/SPEC.md §5.3)
- **Notes:** [pointer to coordination record or external system, or "TBD"]

---

## Declared Upstream (I need these before I can proceed)
- (If Mode = NOT_TRACKED: write “Dependencies coordinated externally by humans.”)
- [DEL-ID] [Name] — Reason: [from WORKING_ITEMS (workflow: project-setup) declarations]
  - Required maturity: [OPEN | INITIALIZED | SEMANTIC_READY | IN_PROGRESS | CHECKING | ISSUED]
  - Location: [path if known, else TBD]

## Declared Downstream (These need me)
- (If Mode = NOT_TRACKED: write “Dependencies coordinated externally by humans.”)
- [DEL-ID] [Name] — Reason: [from WORKING_ITEMS (workflow: project-setup) declarations]
  - Required maturity: [state they need from me]
  - Location: [path if known, else TBD]

---

## Extracted Dependency Register
- **Status:** NOT_RUN_YET

---

## Lifecycle Summary
- (placeholder)

---

## Run Notes
- (placeholder)

## Run History
- (placeholder)
```

Do not add `## Downstream Handoff Notes`; `dependency-extract` adds it only for a run whose `CONSUMER_CONTEXT` is not `NONE`.

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
