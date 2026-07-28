# Authority and source reliability map

| Source class | Surface | Reliability / use |
|---|---|---|
| Product authority | `projects/pec/docs/PRD.md` v2.2 | Normative product scope; exact PEC-K-03/-11 and surrounding concordance |
| Decomposition truth | `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.3 and companion registers | Authoritative downstream deliverable/scope meaning |
| Owner decisions | D-PEC-67, D-PEC-68, D-PEC-69 | Accepted boundaries, activation and fences |
| Scope-change snapshot | `execution/_ScopeChange/SCA-003_2026-07-28_0824/` | Accepted decomposition amendment evidence and handoff |
| Active production contracts | complete `ScopeOfWork.md` files | Target declared state; may contain stale claims being repaired |
| Lifecycle | deliverable-local `_STATUS.md` | Sole lifecycle and Remaining authority; read-only in this run |
| Dependencies | deliverable-local `Dependencies.csv` / `_DEPENDENCIES.md` | Current dependency truth/derivative; excluded from changes |
| Reliance control | `ACTIVE_RELIANCE_HOLDS.csv` and preflight output | Active hard control; no release |
| Frozen implementation | `projects/pec/{core,server,web,agent-sidecar,tools,fixtures}` | Historical/reference evidence only; never scope authority |
| Deterministic tools | registered SOW/register/hold validators | Structural evidence; never human acceptance |
| Prior run artifacts | D-PEC-63/-66 and SCA-003 evidence | Provenance baseline; revalidated against current state before use |

On disagreement, current accepted PRD/decomposition/decision authority
governs. A disagreement among live authority sources is
`AUTHORITY_CONFLICT`; no agent resolves it by precedence invention.
