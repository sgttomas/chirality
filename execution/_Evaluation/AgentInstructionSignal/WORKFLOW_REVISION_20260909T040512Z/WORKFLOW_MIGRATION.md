# Existing workflow package migration

The inventory contains **45 packages and 183 files** under the current `skills/` root. This revision inventories their entrypoints, metadata, and supporting files; it does not claim a new full semantic audit of all package bodies. The human’s accepted concept supplies their target classification as workflow instructions.

Initially retain package names and relocate each entrypoint as mapped below. Each package’s actual inputs, outputs, stage guidance, tools, and references must be reconciled during its rewrite. Preserve existing status and caller eligibility. Two entrypoints explicitly carry a LEGACY marker; other packages may also have contextual restrictions documented by their callers or bodies. Absence of that marker is not an active-status certification.

| Existing entrypoint | Proposed entrypoint | Observed legacy marker |
|---|---|---|
| [content-digest](/Users/ryan/.codex/worktrees/45d2/chirality/skills/content-digest/SKILL.md) | `workflows/content-digest/WORKFLOW.md` | Unmarked |
| [dbm-concordance-seed](/Users/ryan/.codex/worktrees/45d2/chirality/skills/dbm-concordance-seed/SKILL.md) | `workflows/dbm-concordance-seed/WORKFLOW.md` | LEGACY |
| [dbm-concordance-verify](/Users/ryan/.codex/worktrees/45d2/chirality/skills/dbm-concordance-verify/SKILL.md) | `workflows/dbm-concordance-verify/WORKFLOW.md` | Unmarked |
| [dbm-draft-review](/Users/ryan/.codex/worktrees/45d2/chirality/skills/dbm-draft-review/SKILL.md) | `workflows/dbm-draft-review/WORKFLOW.md` | Unmarked |
| [dbm-postauthor-concordance](/Users/ryan/.codex/worktrees/45d2/chirality/skills/dbm-postauthor-concordance/SKILL.md) | `workflows/dbm-postauthor-concordance/WORKFLOW.md` | Unmarked |
| [dbm-publish](/Users/ryan/.codex/worktrees/45d2/chirality/skills/dbm-publish/SKILL.md) | `workflows/dbm-publish/WORKFLOW.md` | Unmarked |
| [dbm-section-publish](/Users/ryan/.codex/worktrees/45d2/chirality/skills/dbm-section-publish/SKILL.md) | `workflows/dbm-section-publish/WORKFLOW.md` | Unmarked |
| [decomposition-package-review](/Users/ryan/.codex/worktrees/45d2/chirality/skills/decomposition-package-review/SKILL.md) | `workflows/decomposition-package-review/WORKFLOW.md` | Unmarked |
| [deliverable-consistency](/Users/ryan/.codex/worktrees/45d2/chirality/skills/deliverable-consistency/SKILL.md) | `workflows/deliverable-consistency/WORKFLOW.md` | Unmarked |
| [dependency-extract](/Users/ryan/.codex/worktrees/45d2/chirality/skills/dependency-extract/SKILL.md) | `workflows/dependency-extract/WORKFLOW.md` | Unmarked |
| [domain-documents](/Users/ryan/.codex/worktrees/45d2/chirality/skills/domain-documents/SKILL.md) | `workflows/domain-documents/WORKFLOW.md` | Unmarked |
| [domain-prose-validate](/Users/ryan/.codex/worktrees/45d2/chirality/skills/domain-prose-validate/SKILL.md) | `workflows/domain-prose-validate/WORKFLOW.md` | Unmarked |
| [domain-source-atomize](/Users/ryan/.codex/worktrees/45d2/chirality/skills/domain-source-atomize/SKILL.md) | `workflows/domain-source-atomize/WORKFLOW.md` | Unmarked |
| [drawing-extract-page](/Users/ryan/.codex/worktrees/45d2/chirality/skills/drawing-extract-page/SKILL.md) | `workflows/drawing-extract-page/WORKFLOW.md` | Unmarked |
| [drawing-titleblock-page](/Users/ryan/.codex/worktrees/45d2/chirality/skills/drawing-titleblock-page/SKILL.md) | `workflows/drawing-titleblock-page/WORKFLOW.md` | Unmarked |
| [equation-bbox-detect](/Users/ryan/.codex/worktrees/45d2/chirality/skills/equation-bbox-detect/SKILL.md) | `workflows/equation-bbox-detect/WORKFLOW.md` | Unmarked |
| [equation-flag-interpret](/Users/ryan/.codex/worktrees/45d2/chirality/skills/equation-flag-interpret/SKILL.md) | `workflows/equation-flag-interpret/WORKFLOW.md` | Unmarked |
| [equipment-costing-extract](/Users/ryan/.codex/worktrees/45d2/chirality/skills/equipment-costing-extract/SKILL.md) | `workflows/equipment-costing-extract/WORKFLOW.md` | Unmarked |
| [equipment-extract](/Users/ryan/.codex/worktrees/45d2/chirality/skills/equipment-extract/SKILL.md) | `workflows/equipment-extract/WORKFLOW.md` | Unmarked |
| [estimate-prep](/Users/ryan/.codex/worktrees/45d2/chirality/skills/estimate-prep/SKILL.md) | `workflows/estimate-prep/WORKFLOW.md` | Unmarked |
| [estimate-snapshot](/Users/ryan/.codex/worktrees/45d2/chirality/skills/estimate-snapshot/SKILL.md) | `workflows/estimate-snapshot/WORKFLOW.md` | Unmarked |
| [evaluation-protocol](/Users/ryan/.codex/worktrees/45d2/chirality/skills/evaluation-protocol/SKILL.md) | `workflows/evaluation-protocol/WORKFLOW.md` | Unmarked |
| [four-documents](/Users/ryan/.codex/worktrees/45d2/chirality/skills/four-documents/SKILL.md) | `workflows/four-documents/WORKFLOW.md` | Unmarked |
| [kty-content-remediate](/Users/ryan/.codex/worktrees/45d2/chirality/skills/kty-content-remediate/SKILL.md) | `workflows/kty-content-remediate/WORKFLOW.md` | Unmarked |
| [kty-metadata-align](/Users/ryan/.codex/worktrees/45d2/chirality/skills/kty-metadata-align/SKILL.md) | `workflows/kty-metadata-align/WORKFLOW.md` | Unmarked |
| [lens-register](/Users/ryan/.codex/worktrees/45d2/chirality/skills/lens-register/SKILL.md) | `workflows/lens-register/WORKFLOW.md` | Unmarked |
| [pandid-valve-symbol-instance](/Users/ryan/.codex/worktrees/45d2/chirality/skills/pandid-valve-symbol-instance/SKILL.md) | `workflows/pandid-valve-symbol-instance/WORKFLOW.md` | Unmarked |
| [pandid-valve-tile](/Users/ryan/.codex/worktrees/45d2/chirality/skills/pandid-valve-tile/SKILL.md) | `workflows/pandid-valve-tile/WORKFLOW.md` | LEGACY |
| [pdf2md](/Users/ryan/.codex/worktrees/45d2/chirality/skills/pdf2md/SKILL.md) | `workflows/pdf2md/WORKFLOW.md` | Unmarked |
| [pdf2md-folio-extract](/Users/ryan/.codex/worktrees/45d2/chirality/skills/pdf2md-folio-extract/SKILL.md) | `workflows/pdf2md-folio-extract/WORKFLOW.md` | Unmarked |
| [pdf2md-page](/Users/ryan/.codex/worktrees/45d2/chirality/skills/pdf2md-page/SKILL.md) | `workflows/pdf2md-page/WORKFLOW.md` | Unmarked |
| [pdf2md-page-assets](/Users/ryan/.codex/worktrees/45d2/chirality/skills/pdf2md-page-assets/SKILL.md) | `workflows/pdf2md-page-assets/WORKFLOW.md` | Unmarked |
| [pdf2md-page-full](/Users/ryan/.codex/worktrees/45d2/chirality/skills/pdf2md-page-full/SKILL.md) | `workflows/pdf2md-page-full/WORKFLOW.md` | Unmarked |
| [proposal-format](/Users/ryan/.codex/worktrees/45d2/chirality/skills/proposal-format/SKILL.md) | `workflows/proposal-format/WORKFLOW.md` | Unmarked |
| [research-orchestration](/Users/ryan/.codex/worktrees/45d2/chirality/skills/research-orchestration/SKILL.md) | `workflows/research-orchestration/WORKFLOW.md` | Unmarked |
| [scc-resolution-case](/Users/ryan/.codex/worktrees/45d2/chirality/skills/scc-resolution-case/SKILL.md) | `workflows/scc-resolution-case/WORKFLOW.md` | Unmarked |
| [scope-change-packet](/Users/ryan/.codex/worktrees/45d2/chirality/skills/scope-change-packet/SKILL.md) | `workflows/scope-change-packet/WORKFLOW.md` | Unmarked |
| [scope-of-work](/Users/ryan/.codex/worktrees/45d2/chirality/skills/scope-of-work/SKILL.md) | `workflows/scope-of-work/WORKFLOW.md` | Unmarked |
| [semantic-lensing](/Users/ryan/.codex/worktrees/45d2/chirality/skills/semantic-lensing/SKILL.md) | `workflows/semantic-lensing/WORKFLOW.md` | Unmarked |
| [semantic-matrix-build](/Users/ryan/.codex/worktrees/45d2/chirality/skills/semantic-matrix-build/SKILL.md) | `workflows/semantic-matrix-build/WORKFLOW.md` | Unmarked |
| [software-bounded-implementation](/Users/ryan/.codex/worktrees/45d2/chirality/skills/software-bounded-implementation/SKILL.md) | `workflows/software-bounded-implementation/WORKFLOW.md` | Unmarked |
| [software-code-review](/Users/ryan/.codex/worktrees/45d2/chirality/skills/software-code-review/SKILL.md) | `workflows/software-code-review/WORKFLOW.md` | Unmarked |
| [software-defect-diagnosis](/Users/ryan/.codex/worktrees/45d2/chirality/skills/software-defect-diagnosis/SKILL.md) | `workflows/software-defect-diagnosis/WORKFLOW.md` | Unmarked |
| [software-repository-reconnaissance](/Users/ryan/.codex/worktrees/45d2/chirality/skills/software-repository-reconnaissance/SKILL.md) | `workflows/software-repository-reconnaissance/WORKFLOW.md` | Unmarked |
| [software-test-planning](/Users/ryan/.codex/worktrees/45d2/chirality/skills/software-test-planning/SKILL.md) | `workflows/software-test-planning/WORKFLOW.md` | Unmarked |

## Content treatment

SKILL.md becomes the workflow definition through rewriting. BRIEF_SCHEMA.md supplies inputs: integrate short requirements into the entrypoint, and link substantial schemas where needed. QA_CHECKS.md supplies essential result checks or a stage-specific review reference; deterministic checks belong in tested tools. TOOL_POLICY.md supplies tool-choice/fallback guidance near the relevant operation, while effective permissions move through the adopted runtime policy migration. Preserve tool policy semantics during that transition.

The loader’s present all-companion requirement is replaced by explicit entrypoint/resource references. Resolve relative references from the workflow package and tool references from the declared tool root. Moving a file requires migrating its callers and links; selective loading depends on a clear route to essential guidance.

## Observed migration surfaces

The root reference inventory reports 163 candidate files, found by text search across AGENTS.md, agents, skills, tools, docs, init, and exports. It mixes executable consumers, documentation, tests, and historical evidence. Classify these for the actual implementation diff; historical accepted records preserve their original terminology.

- `AGENTS.md`, `docs/WORKFLOW_COMPONENT_STANDARD.md` §11, and `skills/README.md`: definitions, package membership, discovery, and companion requirements. Introduce the workflow definition and reconcile the current broader workflow-package vocabulary.
- `agents/AGENT_TASK.md`: TaskSkill selection, mandatory companion loading, frontmatter parsing, policy merge, and run records. Revise together with manager/worker workflow invocation.
- `tools/validation/validate_skill_metadata.py`: required files and custom allowed-tools format. Proposed replacement: `validate_workflow_metadata.py` with workflow entrypoint, binding, resource, and metadata checks. Keep a legacy adapter only for demonstrated current consumers.
- Brief builders under `tools/decomp/`, `tools/drawing_extract/`, `tools/equation_audit/`, `tools/pdf2md/`, and `tools/publication/`: migrate rendered TaskSkill fields, schema references, and their output consumers/tests.
- `tools/validation/validate_kty_remediation_manifest.py`: TaskSkill is a field and enum-dependent action contract. Version or adapt the schema and migrate producing and reading workflows together.
- `tools/validation/validate_instruction_tranche_manifest.py`, `validate_root_surface_ownership.py`, `validate_root_work_graph_dispatch.py`, and `tools/practitioner_harness/cmd_brief.py`: the current instruction surface includes skills paths. Add workflows consistently to the accepted ownership, scope, and manifest treatment.
- `exports/chirality-app/export_public.py`: migrate export inclusion and reference targets so a published workflow has its required tools and resources.
- Project runtime/prompt/discovery consumers and authority corpora: refresh the original shared-findings inventory against the selected revision. This root scan is not an exhaustive inspection of nested project implementations or external mirrors.

## Compatibility and retirement

Use a single authoritative workflow definition and an explicit mapping from an old TaskSkill token/path to the new target. Compatibility readers can resolve old briefs and accepted evidence; newly produced briefs use Workflow after their readers support it. Record both supplied and resolved identity where needed for replay and provenance. A resource move does not by itself establish equivalent recovery behavior.

Resolve aliases before permission checks and record lookup; reject conflicting current/legacy targets. Reconcile the existing custom command policy before removing its parser. Measure the context actually supplied through each supported runtime route. Retire old wrappers and loader branches after active callers have migrated and the accepted replay policy is satisfied.

Standard SKILL.md adapters are optional distribution outputs for a selected host. Their generation, installation, and broad discovery are outside the default repository migration. A requested adapter must declare its workflow/tool dependencies and reference a particular source revision.
