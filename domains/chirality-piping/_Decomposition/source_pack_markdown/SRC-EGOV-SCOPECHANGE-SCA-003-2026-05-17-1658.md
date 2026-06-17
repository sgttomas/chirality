# Source Pack: SRC-EGOV-SCOPECHANGE-SCA-003-2026-05-17-1658

Grouping: `GROUPED_FOLDER`  RepoGlob: `execution/_ScopeChange/SCA-003_2026-05-17_1658/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/_ScopeChange/SCA-003_2026-05-17_1658/Impact_Assessment.md

---
amendment_id: SCA-003
doc_kind: scope_change.impact_assessment
package_role: snapshot / handoff artifact
created: 2026-05-17
status: executed
---

### Impact Assessment

#### Impact Summary

|Action|Affected Sections / Files|Impact|
|---|---|---|
|Modify decomposition revision and intake|`execution/_Decomposition/SOFTWARE_DECOMP.md` frontmatter and intake summary|Revision changes from 0.5 to 0.6 and records SCA-003.|
|Modify architecture basis|`AB-00-04`, resolved architecture baseline, decision log|Physical storage profile is no longer TBD for MVP.|
|Modify scope notes|`SOW-050`, `SOW-059`, `OI-011`|Persistence storage profile is selected; migration framework/tooling remains TBD.|
|Modify companion registers|`docs/_Registers/ScopeLedger.csv`, `Deliverables.csv`, `ContextBudgetQA.csv`|Register notes mirror the accepted SCA-003 basis.|
|Modify dispatch contexts|Affected `_CONTEXT.md` files for persistence, plugin/API boundary, adapter boundary, packaging, and local-first storage|Future TASK briefs receive SCA-003 constraints without reading the full snapshot.|
|Create SCA snapshot/latest state|`execution/_ScopeChange/SCA-003_2026-05-17_1658/*`, latest pointers, docs-side authority|SCA-003 becomes current accepted scope-change state.|

#### Direct Write Surfaces

|Surface|Package Role|Write Basis|
|---|---|---|
|`execution/_Decomposition/SOFTWARE_DECOMP.md`|working surface|Canonical decomposition amendment.|
|`docs/_Registers/ScopeLedger.csv`|authoritative companion register|Scope notes mirror decomposition truth.|
|`docs/_Registers/Deliverables.csv`|authoritative companion register|Deliverable notes mirror decomposition truth.|
|`docs/_Registers/ContextBudgetQA.csv`|authoritative companion register|Context-budget notes mirror decomposition truth.|
|Affected deliverable `_CONTEXT.md` files|downstream dispatch context|Allowed PROJECT/SOFTWARE propagation write surface.|
|`execution/_ScopeChange/SCA-003_2026-05-17_1658/*`|snapshot / handoff artifact|Immutable SCA evidence and handoff.|
|`execution/_ScopeChange/_LATEST.md` and `docs/_ScopeChange/_LATEST.md`|snapshot / handoff pointer|Current accepted SCA state.|
|`docs/_ScopeChange/SCA-003_2026-05-17_1658/Authority.md`|snapshot / handoff artifact|Docs-side authority pointer.|
|`execution/_Decomposition/_LATEST.md`|snapshot / handoff pointer|Current accepted decomposition revision.|

#### Explicit Non-Writes

- No schema edits to `schemas/project_persistence.schema.yaml`.
- No source edits to `core/project_persistence`, desktop services, Tauri configuration, or dependencies.
- No updates to `docs/architecture/persistence_contract.md` or `docs/security/local_first_storage_policy.md` in this SCOPE_CHANGE run.
- No test implementation or fixture update.
- No downstream deliverable production-document rewrite.
- No lifecycle state promotion or `_STATUS.md` mutation.
- No package/deliverable ID additions, removals, merges, splits, or reclassification.

#### Downstream Stale Surfaces

|Owner|Surface / Area|Required Follow-Up|
|---|---|---|
|TASK / domain-schema|`schemas/project_persistence.schema.yaml`|Add concrete physical-container profile and external artifact reference fields.|
|TASK / persistence service|`core/project_persistence` and tests|Implement local SQLite storage profile while preserving canonical JSON/JCS round-trip checks.|
|TASK / security-privacy|`docs/security/local_first_storage_policy.md` and related tests|Refresh policy text from TBD to SCA-003 local SQLite profile without adding cloud/network assumptions.|
|TASK / architecture docs|`docs/architecture/persistence_contract.md`|Update physical-container language when a sealed DEL-02-05 or DEL-00-04 brief authorizes it.|
|TASK / interop-build|Desktop packaging and API/plugin boundary|Bundle SQLite/FTS5 capability and prohibit direct plugin/adapter SQL access.|
|TASK / gui-workflow|Desktop save/open UX|Implement local create/open/save behavior behind application services.|
|TASK / report-audit and PKG-14/15/16|Run history, states, handoff, operation audit trail|Persist state/run/audit metadata through the SCA-003 storage profile without making DB tables public contracts.|

#### Invariant Risk

|Invariant|Risk|Disposition|
|---|---|---|
|Canonical JSON/JCS truth|SQLite tables could become treated as domain truth.|Explicitly prohibited; SQLite is substrate/projection only.|
|No-bypass plugin/adapter boundary|Direct SQL access could skip validation/private-data checks.|Explicitly prohibited in AB-00-04 and affected contexts.|
|Local-first privacy|DB files, sidecars, logs, backups, or exports could leak private data.|Downstream security TASK must update policy/tests.|
|Round-trip reproducibility|Indexes/caches could affect canonical hashes.|Sidecars are rebuildable and non-authoritative.|
|Large-file handling|Path-only refs could break portability or silently miss changed files.|Downstream schema/service work must record hash/metadata diagnostics and explicit export-copy workflow.|

#### Coverage Summary

Counts are intentionally unchanged. SCA-003 changes architecture decisions and notes, not package/deliverable/objective cardinality.

## Component: execution/_ScopeChange/SCA-003_2026-05-17_1658/Propagation_Plan.md

---
amendment_id: SCA-003
doc_kind: scope_change.propagation_plan
package_role: snapshot / handoff artifact
created: 2026-05-17
status: executed
---

### Propagation Plan

#### Direct SCA Writes

|Surface|Action|
|---|---|
|`execution/_Decomposition/SOFTWARE_DECOMP.md`|Update revision to 0.6, add SCA-003 intake/vocabulary/architecture/decision/open-issue changes.|
|`docs/_Registers/ScopeLedger.csv`|Update SOW-050 and SOW-059 decision refs and notes.|
|`docs/_Registers/Deliverables.csv`|Update DEL-00-04, DEL-02-05, and DEL-12-01 storage notes.|
|`docs/_Registers/ContextBudgetQA.csv`|Update DEL-00-04, DEL-02-05, and DEL-12-01 context notes.|
|Affected `_CONTEXT.md` files|Inject SCA-003 constraints into persistence, plugin/API, adapter, packaging, and local-first storage contexts.|
|`execution/_ScopeChange/SCA-003_2026-05-17_1658/*`|Create immutable SCA-003 snapshot.|
|`docs/_ScopeChange/SCA-003_2026-05-17_1658/Authority.md`|Record docs-side authority pointer.|
|Latest pointers|Update execution/docs latest SCA pointers and decomposition latest pointer.|

#### Context Injection Map

|Deliverable|Reason|
|---|---|
|DEL-00-04|Owns persistence/schema versioning architecture.|
|DEL-02-05|Owns project persistence and round-trip serialization.|
|DEL-02-04|Owns plugin/extension domain contracts and no-bypass rules.|
|DEL-10-01|Owns public API/plugin boundary.|
|DEL-10-02|Owns import/export adapter framework.|
|DEL-10-04|Owns packaging implications for bundled SQLite/FTS5 capability.|
|DEL-12-01|Owns local-first storage and private data path posture.|

#### Deferred Downstream Work

|Owner|Work|
|---|---|
|ORCHESTRATOR|Plan bounded TASK refreshes for schema/docs/code/storage implementation.|
|TASK / domain-schema|Update persistence schema physical-container and external artifact reference contract.|
|TASK / persistence|Implement local SQLite storage profile and tests.|
|TASK / security-privacy|Update local-first storage policy/tests for SCA-003.|
|TASK / interop-build|Ensure app packaging can bundle SQLite/FTS5 without hosted service/network dependency.|
|TASK / GUI workflow|Implement save/open UX behind application services.|
|REVIEW / RECONCILIATION|Check downstream docs/schema/code for stale `physical container remains TBD` wording before storage implementation closes.|
|CHANGE|Handle git staging/commit if requested.|

#### Explicit Non-Writes

SCA-003 does not directly update schemas, runtime dependencies, code, tests, persistence service behavior, desktop UX, local-first policy docs, persistence architecture docs, DAGs, lifecycle registers, or implementation evidence. Those surfaces remain downstream-owned.
