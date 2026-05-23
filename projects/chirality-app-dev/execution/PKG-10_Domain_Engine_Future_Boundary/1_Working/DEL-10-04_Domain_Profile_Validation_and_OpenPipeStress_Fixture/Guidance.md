# Guidance: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

## Purpose

DEL-10-04 exists to keep future Domain Engine Profile validation and an OpenPipeStress fixture representable without turning Chirality into a domain-specific solver or moving domain operations into current-release scope. The accepted decomposition describes this as a TEST_SUITE deliverable for validating generic domain profiles and modeling OpenPipeStress as a future fixture without hardcoding solver assumptions into core.

## Principles

1. Treat PKG-10 as future-boundary work. `docs/PLAN.md` R7 and `docs/SPEC.md` Section 18 place domain profiles, operations, and endpoints in future amendment scope.
2. Keep the profile generic before fixture-specific details. `docs/PRD.md` Section 8.17 FR-107 requires a generic `DomainEngineProfile` contract before engine-specific integration.
3. Validate deterministically. `docs/PRD.md` Section 8.17 FR-109 requires invalid or incomplete profiles to fail before runtime exposure.
4. Separate protected truth from proposals. `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 and `docs/PRD.md` Section 8.17 FR-110/FR-111 require agents to write proposals and summaries, not protected domain-engine model truth.
5. Preserve human gates. `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 and `docs/PRD.md` Section 8.17 FR-113 require explicit human acceptance before applying domain operations.
6. Keep professional boundaries visible. `docs/CONTRACT.md` Section 1.1 K-AUTH-1 and Section 1.10 K-DOMAIN-4 prohibit representing agent, runtime, or domain adapter output as professional approval, code compliance, external validation, or Chirality-owned solver truth.

## Considerations

- The future fixture should test the generic shape first: identity, protected paths, proposal paths, artifact types, operations, manifest rules, and boundary notices.
- OpenPipeStress can be a concrete profile fixture only after the generic profile boundary is accepted by amendment. Until then, OpenPipeStress-specific values, solver assumptions, file formats, and execution semantics remain TBD.
- A useful future validation suite should include negative cases. Examples include missing boundary notice, protected path listed as proposal path, missing deterministic adapter manifest rule, incomplete operation descriptor, or fixture wording that implies Chirality owns solver truth.
- ASSUMPTION: Future test locations will be selected by the package implementation plan after PKG-10 amendment; no current source assigns concrete test paths for DEL-10-04.
- ASSUMPTION: The adapter assumptions note should distinguish profile-level assumptions, adapter-manifest assumptions, operation-proposal assumptions, and explicit non-assumptions about Chirality core runtime.
- Future adapter assumptions should separate at least four classes: profile-level fixture facts, adapter-level manifest and execution assumptions, operation-proposal-level human-gated change assumptions, and explicit core-runtime non-assumptions. This preserves `docs/PRD.md` Section 8.17 FR-114 without making OpenPipeStress behavior part of the harness core.
- The REF-006 PRD hash mismatch is a visible source-status warning, not a new design fact. Continued PRD citation is accepted for this assignment only because the task brief explicitly directed P3 enrichment to proceed; closure reliance still needs human acceptance or refreshed source metadata.

## Trade-offs

| Trade-off | Guidance | Source |
|---|---|---|
| Concrete OpenPipeStress examples vs. core neutrality | Use OpenPipeStress only as fixture data; do not put OpenPipeStress concepts in public core runtime contracts. | `docs/PRD.md` Section 8.17 FR-114 |
| Agent convenience vs. protected domain truth | Prefer proposal paths and review aids; reject direct protected model writes. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 |
| Prompt instruction vs. runtime enforcement | Do not rely on prompt-only controls for writes, tool exposure, or domain operations. | `docs/CONTRACT.md` Section 1.6 K-PERM-2 |
| Early domain integration vs. runtime spine stability | Keep profile validation future-scoped until core harness stability. | `docs/PLAN.md` R7; `docs/PRD.md` R7 |
| Early fixture detail vs. evidence quality | Prefer TBDs and deterministic expected-failure slots over unsupported OpenPipeStress values, solver assumptions, or file formats. | `docs/PRD.md` Section 8.17 FR-109/FR-114 |

## Examples

### Candidate Positive Fixture Shape

TBD - no accepted fixture file exists. A future positive fixture should be a generic `DomainEngineProfile` instance for `openpipestress` with required fields present, protected/proposal path separation, operation descriptors, manifest rules, and boundary notice.

### Candidate Negative Cases

- Missing `boundaryNotice`.
- `protectedPaths` and `proposalPaths` overlap.
- Operation descriptor lacks deterministic checks.
- Fixture text states or implies Chirality approves engineering work.
- OpenPipeStress behavior is asserted as core harness runtime behavior.

These are candidate examples only; they require future amendment and test-path assignment before implementation.

### Future Evidence Checklist

TBD until amendment assigns files and owner:

- Concrete positive fixture path.
- Negative fixture paths and deterministic expected failures.
- Adapter manifest location and rule semantics.
- Operation proposal fixture records with required human gate.
- Boundary notice wording fixture.
- Stable validation result record format.
- No-current-release-activation evidence.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-001 | No source-content conflict identified during P1/P2. PRD hash mismatch is recorded as a source warning only per dispatch. | `_REFERENCES.md` REF-006 | Assignment override | All documents citing PRD | Treat PRD mismatch as warning during P3, but require human acceptance or refreshed source metadata before closure reliance | TBD |
