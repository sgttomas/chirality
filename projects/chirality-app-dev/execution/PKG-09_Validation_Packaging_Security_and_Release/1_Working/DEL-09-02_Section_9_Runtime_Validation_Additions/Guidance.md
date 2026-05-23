# Guidance: DEL-09-02 Section 9 Runtime Validation Additions

## Purpose

This deliverable turns the vNext runtime-governance requirements into Section 9 validation coverage. Its purpose is to make release readiness visible as SDK-backed runtime phases land, without treating SDK behavior as product truth unless Chirality contracts, event records, and tests verify the boundary.

## Principles

- Validate product-owned contracts, not SDK implementation details. SDK names, sessions, transcripts, hooks, and messages may appear as adapter metadata, but Chirality `UIEvent`, `HarnessEvent`, permission, session, and governance contracts remain authoritative. Source: `docs/SPEC.md` Sections 9-10; `docs/CONTRACT.md` K-ENGINE-4.
- Keep Section 8 stable while Section 9 expands. Section 9 additions should not regress server reachability, session CRUD, boot taxonomy, stream ordering, persistence/resume, permissions markers, interrupts, or SDK-native stream handling. Source: `docs/PRD.md` Sections 12.3-12.4.
- Prefer explicit pending states over false pass/fail results for runtime phases that have not landed. Source: PRD Section 12.4 states IDs are added "as runtime phases land"; domain-profile validation is conditional on governed amendment.
- Treat PRD as source with a recorded hash warning. Do not erase the mismatch; use corroborating SPEC/CONTRACT/TYPES slices where possible.
- Keep `ResponsibleParty` as `TBD` until a human assigns ownership. Source: `_CONTEXT.md` Source Authority.

## Considerations

Section 9 spans several packages and runtime concepts. The runner and summary schema should therefore make each validation ID independently reportable, with clear statuses such as pass, fail, pending, skipped, or blocked. The exact status enum is TBD because no local source defines it.

The validation set should distinguish:

- Contract presence checks: engine contract, mapper boundary, event schema, reliance register.
- Runtime behavior checks: event append/replay, settings isolation, permission denial, MCP wrapper behavior, hooks, result budgets, compaction, subagent governance.
- Conditional checks: `section9.domain_profile_validation`, which should remain pending or gated until a governed domain-profile amendment enters scope.

Where implementation files are not yet known, avoid binding tests to guessed paths. Use Section 9 IDs and source-defined contract names as the stable interface until the owning implementation deliverables establish file locations.

## Trade-offs

| Topic | Guidance |
|---|---|
| ID completeness vs implementation readiness | Register all source-defined Section 9 IDs, but permit pending/gated status for IDs whose runtime phase is not implemented yet. |
| SDK conformance vs product conformance | Product conformance wins. Tests should assert Chirality-owned contracts and use SDK details only as observed inputs or adapter metadata. |
| Summary detail vs release readability | Store enough detail for diagnosis while preserving a stable summary artifact for premerge/release review. Exact schema remains TBD. |
| Broad Section 9 scope vs local deliverable bounds | Keep this deliverable focused on validation additions; defer implementation of runtime features to their owning deliverables. |

## Examples

Example validation record shape, ASSUMPTION based on anticipated "summary schema":

```json
{
  "id": "section9.permission_overlay_deny_first",
  "status": "TBD",
  "evidence": [],
  "source": "docs/PRD.md Section 12.4; docs/CONTRACT.md K-PERM-1"
}
```

Example gating note for conditional domain validation:

```json
{
  "id": "section9.domain_profile_validation",
  "status": "pending_governed_amendment",
  "reason": "PRD Section 12.4 scopes this after a governed domain-profile amendment enters scope."
}
```

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-001 | PRD hash mismatch recorded in `_REFERENCES.md`, but assignment instructs treating it as source warning only. | `_REFERENCES.md` REF-006 | Assignment runtime override | All PRD-cited sections | Proceed with PRD as accessible source while preserving the warning and corroborating with SPEC/CONTRACT/TYPES where possible. | TBD |
| CONFLICT-002 | Section 9 includes `section9.domain_profile_validation`, but source states it applies only after governed domain-profile amendment enters scope. | `docs/SPEC.md` Section 19.3 | `docs/PRD.md` Section 12.4 | Datasheet Attributes; Specification Requirements; Procedure Steps | Include the ID in the registry but mark it pending/gated until amendment is accepted. | TBD |

