# Guidance: DEL-10-01 DomainEngineProfile Contract Draft

## Purpose

This guidance explains how to read and maintain the `DomainEngineProfile` contract draft as a future-boundary artifact. The profile contract exists to preserve future compatibility for domain-engine integrations without moving domain execution into the current runtime slice.

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-10; `docs/PRD.md` §8.17; `docs/PLAN.md` §R7.

## Principles

| Principle | Guidance | Source |
|---|---|---|
| Generic first | Keep the profile contract generic before any engine-specific integration. OpenPipeStress may become a fixture later, but it must not shape Chirality core runtime assumptions. | `docs/PRD.md` §8.17 FR-107, FR-114 |
| Future gated | Treat endpoints, tools, validators, adapters, and path hooks as future platform interfaces until a governed amendment accepts them. | `docs/SPEC.md` §18; `docs/PLAN.md` §R7 |
| Truth separation | Domain engines own authoritative domain truth; Chirality governs interaction, proposals, records, and human gates. | `docs/CONTRACT.md` §1.10 K-DOMAIN-1 |
| Path quarantine | Protected paths and proposal paths must remain distinct. Agents may draft proposals and summaries, not overwrite protected model truth. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110, FR-111 |
| Human acceptance | Domain operations are not applied merely because a tool can produce an output; application requires explicit human acceptance. | `docs/SPEC.md` §18; `docs/PRD.md` §8.17 FR-113 |
| Professional boundary | Boundary notices must prevent solver outputs from being presented as professional approval, code compliance, external validation, or solver truth owned by Chirality. | `docs/CONTRACT.md` §1.10 K-DOMAIN-4; `docs/PRD.md` §8.17 FR-115 |

## Considerations

- Use `docs/TYPES.md` §11.1 as the current field baseline for `DomainEngineProfile`.
- Treat `DomainEngineOperationDescriptor` as unresolved because the accessible sources reference the type but do not define its fields.
- Treat `manifestRules` as unresolved because the accessible source currently types it as `unknown`.
- Keep OpenPipeStress references fixture-level only. The profile contract should permit an OpenPipeStress fixture later without embedding OpenPipeStress assumptions in the generic contract.
- Any future validator should be deterministic and reject invalid or incomplete profiles before runtime exposure.
- The PRD is available but carries a recorded hash mismatch in `_REFERENCES.md`; this run treats that as a source warning only under the dispatch instruction.

## Trade-offs

| Topic | Conservative position | Risk if loosened |
|---|---|---|
| Descriptor schema | Leave operation descriptor fields as TBD until authoritative definition exists. | Invented fields could become false contract surface. |
| Manifest schema | Preserve `manifestRules: unknown` until a governed schema is accepted. | Over-specific rules could conflict with future adapter design. |
| Endpoint references | Mention candidate endpoint families only as provisional future interfaces. | Current-release scope creep or accidental implementation pressure. |
| Boundary notice copy | Require boundary notices but avoid final copy until future UI, documentation, event-record, and concrete profile-instance context is approved. Disposition: X-001 incorporated as acceptance-context guidance. Source reread: `docs/CONTRACT.md` §1.10 K-DOMAIN-4; `docs/PRD.md` §8.17 FR-115 and §R7. | Copy may imply professional reliance or solver-truth ownership. |

## Examples

### Example Generic Skeleton

```ts
const exampleProfile: DomainEngineProfile = {
  profileId: "TBD",
  engineName: "TBD",
  engineVersion: "TBD",
  protectedPaths: ["TBD"],
  proposalPaths: ["TBD"],
  artifactTypes: ["TBD"],
  operations: [], // DomainEngineOperationDescriptor shape TBD.
  manifestRules: "TBD",
  boundaryNotice: "TBD"
};
```

This example is illustrative only. It is not an accepted runtime fixture and must not be treated as implementation-ready.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-1 | `DomainEngineOperationDescriptor` is referenced but not defined in accessible sources. | `docs/TYPES.md` §11.1 references `DomainEngineOperationDescriptor[]`. | No accessible source slice defines `DomainEngineOperationDescriptor`. | `Datasheet.md` Attributes; `Specification.md` Requirements; future validator design | Keep descriptor shape TBD until governed type definition is accepted. Disposition: D-001 already covered and retained as unresolved conflict. Source reread: `docs/TYPES.md` §11.1; `docs/PRD.md` §8.17 FR-108. | TBD |
| CONFLICT-2 | `manifestRules` is required but typed as `unknown`. | `docs/TYPES.md` §11.1 includes `manifestRules: unknown`. | `docs/PRD.md` §8.17 FR-108 requires manifest rules but does not define schema in accessible slice. | `Datasheet.md` Attributes; `Specification.md` Requirements; future validator design | Keep manifest schema TBD until accepted manifest-rule schema exists. Disposition: D-002 already covered and retained as unresolved conflict. Source reread: `docs/TYPES.md` §11.1; `docs/PRD.md` §8.17 FR-108. | TBD |

## Pass 3 Disposition Notes

| ItemID | Disposition | Evidence |
|---|---|---|
| A-001 | Converted to human ruling gate. | `Specification.md` Verification now requires PRD hash refresh or explicit acceptance before downstream reliance. |
| B-001 | Incorporated. | `Specification.md` Verification now includes a PRD source refresh gate for PRD-dependent assertions. |
| C-001 | Incorporated as status-policy normalization. | `Procedure.md` distinguishes P1/P2 status transition from Phase 2.5 P3_ONLY NO_STATUS_TOUCH execution. |
| F-001 | Incorporated as dependency gate. | `Procedure.md` now blocks closeout when accepted upstream dependency status remains unresolved unless human acceptance of proceeding is recorded. |
| D-001 | Already covered and retained. | CONFLICT-1 keeps `DomainEngineOperationDescriptor` unresolved until an accepted type definition exists. |
| D-002 | Already covered and retained. | CONFLICT-2 keeps `manifestRules` unresolved until an accepted manifest-rule schema exists. |
| X-001 | Incorporated. | `Guidance.md` Trade-offs now names future UI, documentation, event-record, and profile-instance context for boundary notice acceptance. |
| E-001 | Incorporated. | `Specification.md` Verification now requires future instance-level review data for concrete profile fixtures. |

## References

- `docs/CONTRACT.md` §1.10
- `docs/SPEC.md` §18
- `docs/TYPES.md` §11
- `docs/PLAN.md` §R7
- `docs/PRD.md` §8.17, §10.10, KG-016 through KG-020
