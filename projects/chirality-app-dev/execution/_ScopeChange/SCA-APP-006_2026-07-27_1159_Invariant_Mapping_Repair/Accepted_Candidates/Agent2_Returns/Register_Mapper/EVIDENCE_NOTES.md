# SCA-APP-006 invariant-register mapper — evidence notes

## Return posture

This is a read-only Agent 2 candidate return. It is not authoritative
decomposition truth and does not approve Gate 3. The candidate is derived
from Git object c487b7dd57a378e2f74417118e78e7f61a161629; no repository or SCA snapshot file was edited.

## Exact source basis

- CONTRACT: `projects/chirality-app-dev/docs/CONTRACT.md`
  - SHA-256: `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7`
- App decomposition: `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
  - SHA-256: `69b3110c26cb0b435ced4144845282bf6905cde4c0474b21282b9a1806984946`
- Accepted runtime boundary: D-GOV-20, D-GOV-28 / Root PRD O-11, and
  SCA-APP-005's accepted Root-owner/App-client classification.
- D-T0-23 is cited only as a coordinating counterpart. It is not used as Root
  authority.

## Mapping method

1. Parse every exact `K-*` row directly from the CONTRACT catalog, retaining
   its exact source line and enforcement cell.
2. Resolve App package and deliverable IDs from the accepted decomposition.
3. Start from decomposition §10A.1 family coverage, then narrow each exact
   invariant to the smallest source-supported deliverable set using Sections
   7–9, SOW statements, deliverable descriptions, and open issues.
4. Apply SCA-APP-005's accepted partition: Root owns generic runtime semantics
   and operations; App retains client integration, project authority,
   presentation, compatibility, conformance, and acceptance evidence.
5. Set `SemanticOwnerProduct=UNKNOWN` when an exact invariant crosses a seam
   SCA-APP-005 explicitly left unresolved. This is deliberate non-invention,
   not a claim that App has no mapped obligation.
6. Preserve the domain family as a future composite boundary because current
   sources distinguish Root minimum invariants, App specializations, and
   external domain truth rather than assigning one singular product owner.

## Closed vocabularies proposed

- `SemanticOwnerProduct`: APP, ROOT, UNKNOWN
- `OwnerAuthorityBasis`: APP_CONTRACT_AND_DECOMPOSITION, ROOT_RULED_CONTINUING_STEWARDSHIP, UNRESOLVED_COMPOSITE, FUTURE_BOUNDARY_COMPOSITE
- `AppObligationClass`: APP_GOVERNANCE_AND_AUTHORITY, APP_PRODUCT_OR_PROJECT_IMPLEMENTATION, APP_CLIENT_CONFORMANCE, APP_RELEASE_AND_VALIDATION, FUTURE_BOUNDARY_DEFINITION, UNRESOLVED_COMPOSITE
- `CoverageStatus`: MAPPED, MAPPED_WITH_OPEN_ISSUE, FUTURE_BOUNDARY, UNRESOLVED_SEMANTIC_OWNER
- `ProvenanceStatus`: DIRECT_APP_AUTHORITY, EXTERNAL_ROOT_AUTHORITY, COMPOSITE_AUTHORITY_UNRESOLVED, FUTURE_BOUNDARY_COMPOSITE

## Candidate result

- 81 exact invariant rows; 81 unique IDs; 48 families.
- Semantic-owner counts: {"APP":45,"ROOT":22,"UNKNOWN":14}.
- Coverage counts: {"MAPPED":33,"MAPPED_WITH_OPEN_ISSUE":34,"FUTURE_BOUNDARY":4,"UNRESOLVED_SEMANTIC_OWNER":10}.
- Every App package and deliverable reference resolves in the accepted
  decomposition.
- Every open-issue reference resolves either in decomposition §11 or the
  D-GOV-28 open-item register.
- All `UNKNOWN` semantic-owner rows are repeated in
  `UNRESOLVED_MAPPINGS.csv` with the source-backed reason and required
  disposition.

## Interpretation cautions

- The exact CONTRACT enforcement cell is carried in `EnforcementSurfaces`.
  It is descriptive enforcement evidence, not a claim that every named
  implementation already exists or passes.
- `ValidationSurfaces` names accepted App deliverables that own or carry the
  relevant verification work. It does not report runtime test results.
- `MAPPED_WITH_OPEN_ISSUE` means topology is source-backed while an admitted
  issue still conditions lifecycle or reliance claims.
- `FUTURE_BOUNDARY` does not activate implementation.
- A final Gate-3 register should remain blocked if an owner insists on a
  non-UNKNOWN singular owner for a composite seam without a new ruled source.
