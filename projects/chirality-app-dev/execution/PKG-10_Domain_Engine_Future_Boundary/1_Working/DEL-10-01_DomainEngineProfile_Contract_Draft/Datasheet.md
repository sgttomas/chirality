# Datasheet: DEL-10-01 DomainEngineProfile Contract Draft

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-10-01 |
| DeliverableName | DomainEngineProfile Contract Draft |
| PackageID | PKG-10 |
| PackageName | Domain Engine Future Boundary |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | API_CONTRACT |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| Current posture | Future-boundary contract, not current implementation |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Contract subject | Future `DomainEngineProfile` profile contract | `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-10; `docs/TYPES.md` §11.1 |
| Required profile identity fields | `profileId`, `engineName`, optional `engineVersion` | `docs/TYPES.md` §11.1 |
| Required boundary/path fields | `protectedPaths`, `proposalPaths` | `docs/TYPES.md` §11.1; `docs/PRD.md` §8.17 FR-108, FR-110, FR-111 |
| Required artifact and operation fields | `artifactTypes`, `operations` | `docs/TYPES.md` §11.1; `docs/PRD.md` §8.17 FR-108 |
| Required manifest and notice fields | `manifestRules`, `boundaryNotice` | `docs/TYPES.md` §11.1; `docs/PRD.md` §8.17 FR-108, FR-115 |
| Operation descriptor schema | TBD. `DomainEngineOperationDescriptor[]` is referenced, but no descriptor interface is defined in accessible sources. | `docs/TYPES.md` §11.1 |
| Manifest rule schema | TBD. `manifestRules` is typed as `unknown` in the accessible vocabulary source. | `docs/TYPES.md` §11.1 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Release scope | Domain-engine endpoints and tools are provisional future platform interfaces and must not be implemented as current-release scope. | `docs/SPEC.md` §18 |
| Sequencing | Domain Engine Profiles and operation-proposal workflows are introduced after core harness stability. | `docs/PLAN.md` §R7; `docs/PRD.md` §8.17 |
| Engine-specific integration | A generic `DomainEngineProfile` contract precedes any engine-specific integration. | `docs/PRD.md` §8.17 FR-107 |
| Protected path posture | Protected domain paths are write-quarantined; agents write proposals, summaries, and review aids, not protected model truth. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110, FR-111 |
| Human gate posture | Applying a domain operation requires explicit human acceptance. | `docs/SPEC.md` §18; `docs/PRD.md` §8.17 FR-113 |
| Professional boundary | Domain-engine outputs must not be represented as professional approval, code compliance, external validation, or solver truth owned by Chirality. | `docs/CONTRACT.md` §1.10 K-DOMAIN-4; `docs/PRD.md` §8.17 FR-115 |
| PRD source status | Source warning: `_REFERENCES.md` records a PRD hash mismatch. This draft treats PRD content as available source with warning, per dispatch instruction. | `_REFERENCES.md`; dispatch instruction |

## Construction

### Draft TypeScript Shape

```ts
interface DomainEngineProfile {
  profileId: string;
  engineName: string;
  engineVersion?: string;
  protectedPaths: string[];
  proposalPaths: string[];
  artifactTypes: string[];
  operations: DomainEngineOperationDescriptor[];
  manifestRules: unknown;
  boundaryNotice: string;
}
```

Source: `docs/TYPES.md` §11.1.

### Validation Notes

| Check | Draft rule | Source |
|---|---|---|
| Required fields present | A future validator should reject profiles missing identity, path, artifact, operation, manifest, or boundary-notice fields. | `docs/PRD.md` §8.17 FR-108, FR-109 |
| Deterministic validation | Profile validation must be deterministic before runtime exposure. | `docs/PRD.md` §8.17 FR-109 |
| Future-only exposure | Candidate domain endpoints/tools must remain provisional until governed future amendment. | `docs/SPEC.md` §18 |
| Solver separation | Profile contract must preserve that domain engines own authoritative domain truth. | `docs/CONTRACT.md` §1.10 K-DOMAIN-1 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-10, SOW-066, SOW-067, DEC-006
- `docs/CONTRACT.md` §1.10
- `docs/SPEC.md` §18
- `docs/TYPES.md` §11
- `docs/PLAN.md` §R7
- `docs/PRD.md` §8.17, §10.10, §R7, KG-016 through KG-020; source warning: hash mismatch recorded in `_REFERENCES.md`
