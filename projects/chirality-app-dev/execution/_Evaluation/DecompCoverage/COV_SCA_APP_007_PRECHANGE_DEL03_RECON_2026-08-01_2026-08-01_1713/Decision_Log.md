# Decision Log

| Topic | Decision |
|---|---|
| Scope binding | Audit only PKG-03 and PKG-09 declarations, plus reverse-only folders carrying those stable-ID prefixes. |
| Stable-ID matching | Match folder names by `PKG-XX` and `DEL-XX-YY`; descriptive suffixes are physical labels, not separate identities. |
| Duplicate PKG-03 roots | Treat `PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle` as the current matching root and `PKG-03_Harness_Runtime_Core` as a duplicate historical physical root because both resolve to stable ID PKG-03. |
| DEL-03-01..04 | Treat as current declared deliverables; all four folders are present under the current PKG-03 physical root. |
| DEL-03-05 | Record historical provenance but no current coverage issue because neither the accepted current decomposition nor filesystem declares/carries it. |
| DEL-03-06 | Record a reverse-coverage warning because the current decomposition has no DEL-03-06 row while the historical physical root contains a tracked evidence-only folder. |
| DEL-09-06 | Treat as the accepted current security-validation owner named by the decomposition; do not infer that all historical DEL-03-06 evidence can be moved without SCOPE_CHANGE review. |
| Artifact matching | Preserve the prior audit method: the SOW_V1 contract validates, while named implementation artifacts without folder-local filename matches are warnings because all scoped deliverables are IN_PROGRESS. |
| Active snapshot | Use `_ScopeChange/_LATEST.md` exactly as found; it resolves to closed SCA-APP-006 and truthfully records its scope-change-only closure. |
| Human overrides | None. |
