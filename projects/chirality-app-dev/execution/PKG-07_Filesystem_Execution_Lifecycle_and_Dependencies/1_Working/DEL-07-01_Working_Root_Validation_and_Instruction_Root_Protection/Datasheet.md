# Datasheet: DEL-07-01 Working Root Validation and Instruction Root Protection

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-07-01 |
| DeliverableName | Working Root Validation and Instruction Root Protection |
| PackageID | PKG-07 |
| PackageName | Filesystem Execution, Lifecycle, and Dependencies |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | M |
| CoversScopeItems | SOW-002, SOW-027 |
| SupportsObjectives | OBJ-006, OBJ-008 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary control subject | Working-root validity, root separation, path containment, and instruction-root write protection. | `_CONTEXT.md` `Deliverable Scope`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `PKG-07` table |
| Working root meaning | User-selected local filesystem location for project execution state, sessions, artifacts, and git history. | `docs/TYPES.md` Section 1.6 |
| Instruction root meaning | Release-managed app resource tree containing governance documents, agent instructions, and framework materials. | `docs/TYPES.md` Section 1.5; `docs/SPEC.md` Section 1.1 |
| Ordinary project truth write location | Working root is the ordinary location where agents and tools write project truth. | `docs/SPEC.md` Section 1.2; `docs/CONTRACT.md` K-ROOT-3 |
| Validation endpoint | `/api/working-root/validate` validates and normalizes a working root. | `docs/SPEC.md` API endpoints table; `docs/PRD.md` Section 7.1 |
| Runtime enforcement surfaces | Path helpers, PreToolUse hooks, MCP tools, and Chirality hooks. | `docs/CONTRACT.md` K-PATH-2; `docs/CONTRACT.md` K-ROOT-2 |
| Anticipated artifacts | Root validation tests; path policy helpers; instruction-root protection fixtures. | `_CONTEXT.md` `Anticipated Artifacts`; decomposition `DEL-07-01` row |

## Conditions

| Condition | Required Behavior | Source |
|---|---|---|
| Working-root path form | Working root must be an absolute existing directory. | `docs/SPEC.md` Section 1.2; `docs/PRD.md` Section 7.1 |
| Working-root access | Working root must be readable and writable by the app. | `docs/SPEC.md` Section 1.2; `docs/PRD.md` Section 7.1 |
| Root separation | Working root must not be inside the instruction root. | `docs/SPEC.md` Section 1.2; `docs/CONTRACT.md` K-ROOT-1 |
| Instruction-root mutation | Ordinary project execution must not mutate the instruction root; writes under instruction root must be denied. | `docs/SPEC.md` Section 1.1; `docs/CONTRACT.md` K-ROOT-2 |
| Path containment | Runtime tools must enforce working-root containment and reject writes outside the active project root. | `docs/CONTRACT.md` K-PATH-2; `docs/PRD.md` FR-050 |
| Symlink writes | Symlink writes are rejected in the initial policy. | `docs/CONTRACT.md` K-PATH-3; `docs/SPEC.md` Section 15.2 |
| Permission override | Deny decisions from policy, hooks, path containment, governance, SDK deny rules, or human gates override allows. | `docs/PRD.md` Section 3; `docs/CONTRACT.md` K-PERM-1 |
| Source-state warning | `docs/PRD.md` is usable for this draft but has a HASH_MISMATCH in `_REFERENCES.md`; content depending on it should remain review-aware. | `_REFERENCES.md` REF-006 |

## Construction

| Component | Construction Notes | Source |
|---|---|---|
| Root validator | Validate absolute path, existence, directory type, readability, writability, and instruction-root containment before use. | `docs/PRD.md` Section 7.1; `docs/PRD.md` FR-003 |
| Path policy helper | Resolve project-relative and absolute tool paths and reject paths outside the active project root. | `docs/PRD.md` FR-050; `docs/CONTRACT.md` K-PATH-2 |
| Instruction-root resolver/protection | Identify the active instruction root, including development override behavior, and deny ordinary writes beneath it. | `docs/SPEC.md` Section 1.1; `docs/PRD.md` Section 10.1 |
| Hook integration | Apply containment, instruction-root protection, symlink rejection, and provenance policy through required hooks before governed writes. | `docs/SPEC.md` Section 15.2; `docs/PRD.md` FR-095 |
| Test fixtures | Include invalid root cases, instruction-root-contained roots, outside-project paths, instruction-root write attempts, and symlink write attempts. | `docs/PRD.md` FR-003, FR-050, FR-051, FR-095, FR-097 |
| Code locations | TBD - implementation files are not identified by the authoritative source slices read for this Phase 2.2 draft. | Source-grounding gap |

## References

| RefID | SourcePath | SectionRef | Notes |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Sections 2.6-2.9 | Project truth, root separation, reliance boundaries. |
| REF-002 | `docs/CONTRACT.md` | Sections 1.3, 1.7; K-PATH/K-HOOK rows | Root separation, path containment, hooks, lifecycle invariants. |
| REF-003 | `docs/SPEC.md` | Sections 1.1, 1.2, 15.2; API endpoints table | Instruction-root and working-root contracts, hooks, API surfaces. |
| REF-004 | `docs/TYPES.md` | Sections 1.5, 1.6, 8.2 | Vocabulary and permission-mode terms. |
| REF-005 | `docs/PLAN.md` | Implementation sequencing references to hooks and path containment | Context only; not used as primary authority for requirements. |
| REF-006 | `docs/PRD.md` | Sections 7.1, 8.9, 8.15, 10.1, 10.2; FR-003, FR-050, FR-051, FR-095, FR-097 | Product requirements. HASH_MISMATCH warning recorded in `_REFERENCES.md`. |
| REF-007 | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | PKG-07 and DEL-07-01 rows; SOW mapping rows | Scope routing and deliverable identity. |
