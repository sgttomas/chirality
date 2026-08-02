# Decision Log

| Topic | Decision |
|---|---|
| Scope binding | Audit only PKG-03 and PKG-09 declarations, plus any reverse-only folders carrying those stable-ID prefixes. |
| Stable-ID matching | Match physical labels by stable `PKG-XX` and `DEL-XX-YY` prefixes. |
| DEL-03-01..04 | Treat as the four current declared PKG-03 deliverables; all four are present under the sole current PKG-03 physical root. |
| DEL-03-05 | No current issue: it remains absent from both accepted decomposition and current filesystem. Historical provenance was established in the pre-change audit. |
| DEL-03-06 | Treat the absence of the retired physical folder as the intended post-change state. Its historical evidence under DEL-09-06 is evidence content, not a reverse-only deliverable folder. |
| DEL-09-06 | Treat as the accepted current owner. Validate migration integrity from `PROVENANCE.md` and the 38-row manifest without reinterpreting preserved historical bundle names. |
| Artifact matching | Preserve the pre-change method: SOW_V1 contracts validate; named anticipated implementation artifacts without folder-local filename matches remain warnings because all scoped deliverables are IN_PROGRESS. |
| Active SCOPE_CHANGE snapshot | Use `_ScopeChange/_LATEST.md` exactly as found. It continues to resolve to closed SCA-APP-006 and remains internally consistent for that snapshot. |
| Human override | Do not update `_Evaluation/DecompCoverage/_LATEST.md`. This overrides Step 13.6 and is recorded verbatim in `Brief.md`. |
| Snapshot role | This run is derivative Gate-5 evidence and does not replace the accepted decomposition or SCA-APP-007 owner ruling. |
