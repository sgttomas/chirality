# Document workflow conversion return

Status: COMPLETE
Role: TASK (Type 2)
Parent: WORKING_ITEMS, `/root/working_items`
Mechanism: delegated-harness-native; role and write scope instruction-asserted

## Completed scope

Converted all 21 assigned existing packages and four retired agent packages into 25 workflow entrypoints. The old assigned `skills/` directories and four agent files are removed after conversion. All writes are within the assigned package paths and this evidence directory. No delegation, staging, commit, branch, push, or product-code changes were performed.

The four orchestration entrypoints are `dbm-publisher`, `drawing-extract`, `equation-audit`, and `pdf2md-orchestration`, compatible with WORKING_ITEMS. Their detailed procedures, artifact contracts, and acceptance checks are selected resources. Drawing workflow extension guidance is a separate `EXTENDING.md`. The 21 bounded workflows can be applied by TASK, WORKING_ITEMS, or HELPS_HUMANS within their role and brief; whole-workflow manager delegation is not granted to TASK.

Each existing package's brief schema, QA checks, and tool-use responsibilities are consolidated into `CONTRACT.md`. Metadata tables and profile boilerplate are removed. Optional execution companions carry independent command restrictions. Explicitly reasoning-only methods deny shell commands. The P&ID symbol-instance workflow inherits its bounded brief's tool policy for any authorized crop operation. Existing command-expression allowlists are preserved for the bounded PDF and publication/review methods.

## Substantive changes

- DBM publication retains all seven human decisions, source-admission requirements, input classes, manifest/schema/map/rules fields, full engineering body standards, section-context/open-item contracts, section and package outputs, and post-authoring review. Durable model allocation is removed, including from the legacy concordance method. Review eligibility is based on consolidation evidence rather than model tier.
- New PDF conversion dispatches use `pdf2md-page-full`; Markdown and asset JSON are paired outputs in every mode. `pdf2md-page` and `pdf2md-page-assets` are explicitly LEGACY resume methods; `pdf2md-folio-extract` remains optional and active. Folio uncertainty remains null and physical pages retain identity.
- PDF materialization canonically rewrites inline references into regenerated working anchored Markdown. The contradictory append-only rationale is removed. Invalid or partial output pairs are requeued; missing source hashes cannot establish safe reuse merely through matching paths and DPI. The bounded PDF workflow now checks source identity before rasterization and validates reused output rather than trusting file existence.
- PDF page failure instructions return unavailable output paths explicitly instead of requiring impossible writes into invalid targets. Task-data read limits distinguish page input from supplied role/workflow/brief context.
- Equation audit uses a single complete `SOURCE_AUDIT_ROOT`, ending at `audit/equations/`. Writable page Markdown and assembled source are explicit brief targets, including when the work directory is a sibling of the source tree. Ambiguous flags return for human clarification before the schema gate; `ALLOW_UNREVIEWED` changes coverage only and cannot waive flags, backcheck, or overlaps. Snapshot artifacts are assembled before closure and existing snapshots are never reused or overwritten.
- Drawing extraction has one target-dispatch registry for five implemented combinations, with ISOMETRIC/GA remaining fail-fast stubs. Coverage, crop/tile, resume, duplicate and merge methods remain. Current P&ID outputs require page-global pixel geometry; MINI_GRID is an optional aid. Run folders are working surfaces until closure and freeze afterward.
- Caller examples use WORKING_ITEMS and an explicit workflow, with TASK for bounded stages. Instructions describe selected-resource loading and actual recorded evidence; prose no longer claims automatic hydration or host enforcement.
- No NEXT_INSTANCE_PROMPT, NEXT_INSTANCE_STATE, or next-instance handoff contract occurs in any assigned workflow or resource.

## Evidence and verification

`COVERAGE.json` records all 25 source-to-destination dispositions, original source hashes, legacy status, selected resources, and all 84 original package-file dispositions. `ARTIFACT_MANIFEST.json` fingerprints the 84 resulting package files. `VALIDATION.json` records 253 passing checks.

Executed `python3 .../document_workflows/verify.py`: PASS, 253/253. Verification covers the complete assigned source set, original fingerprints, minimal frontmatter, old-path retirement, selected resource loading through the Root resolver, manager/TASK compatibility, matching legacy selectors, command restrictions, tool/reference existence, omitted next-instance content, absence of durable model allocation, the specific repaired cross-resource contracts, and selected tool resolution from `/tmp`.

Historical field values such as `Origin = AGENT_CHECK` and `EvidenceSource = AGENT_REVIEW:<description>` remain unchanged because they are output-schema vocabulary. Prior accepted source snapshots are untouched.

## Integration handoff

Root tool and brief consumers are owned by the runtime worker. Parent-routed requirements are: replace companion-file expectations with selected `CONTRACT.md` context; emit `Workflow`, `RequestedBy: WORKING_ITEMS`, and the caller workflow where needed; use the merged PDF page worker for new orchestration; keep the single equation-audit root convention. Publication local parameter labels now use `*_WORKFLOW` instead of `*_SKILL`.

No unresolved implementation item remains in this write scope. The parent must run the full tranche checks and refresh package fingerprints if integration changes these files. Public adoption and host enforcement remain governed by the Root adoption hold.
