# Shared instruction and runtime findings

Status: candidate decision support. Parent investigator: HELPS_HUMANS. Basis: `781b478176db46ca66ebd38991607612e0ce9338`; this is the inspected checkout, not a declaration of fetched-main currency or product deployment status.

## 1. Current structural conformance

`python3 tools/validation/validate_agent_instructions.py --json` returned 34 files checked, zero errors, zero warnings. The observation concerns the current structural contract. The proposed instruction audit asks a different question: how clearly each package evokes its role and supplies what its work requires.

The shared four-section markers and six Agent Type table fields are explicitly required by `docs/WORKFLOW_COMPONENT_STANDARD.md:339` and `docs/SPEC.md:679`. The root validator's `REQUIRED_MARKERS` and `REQUIRED_FIELDS` (`tools/validation/validate_agent_instructions.py:25–49`) encode those expectations. Its file checks (`:115–220`) also use class, blocking posture, scope and specialist approval references. A proposal to change those representations has a concrete shared-contract dependency.

## 2. Distinguish machine metadata from model-visible instruction

The inspected App implementation reads the instruction body as well as frontmatter:

- `projects/chirality-app-dev/frontend/src/lib/harness/agent-instruction.ts:47–73`: six required table fields, four section names and recognized frontmatter keys.
- The same file `:251–280`: type/class parsed from body headers or table rows; `:367–431`: conformance checks on table presence, class, scope and section markers.
- `projects/chirality-app-dev/frontend/src/lib/harness/options.ts:49–54`: frontmatter supplies tool and turn defaults; `:89–111`: effective session options resolve those defaults with explicit runtime options.
- `projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts:261–330`: parent/child type, child eligibility and dedicated approval records are consumed by delegation policy; `:194–198` and `:590` connect instruction tool declarations to child policy.
- `projects/chirality-runtime/packages/core/src/runtime-service.ts:409–441`: the Runtime project's agent discovery reads type/class from the instruction and filters direct-chat selection using type.

The App prompt composer injects the complete role content alongside governance, working-root, mode and tool context (`projects/chirality-app-dev/frontend/src/lib/harness/persona-manager.ts:210–263`). That creates a concrete design opportunity: the discovery/policy representation and the model-visible role could be made separate projections. A sidecar or other representation is a design candidate, not an existing contract established by this audit. Prompt assembly, hash/provenance semantics, fixtures and consumers would need coordinated amendment.

These observations establish source-code consumers. They do not demonstrate that every configured harness or deployed version enforces identical behavior, or that semantic responsibilities can be discharged by a parser.

## 3. Three useful proposal scopes

1. **Instruction editing:** consolidate repetitions, remove superseded narrative, strengthen role-specific language and refer to already available contracts. Retain the currently required machine-facing representation until its replacement is accepted.
2. **Shared representation change:** separate runtime configuration and policy evidence from model-facing instructions, with corresponding standard, parser, composer, validator and attribution changes. The role can still use PROTOCOL/SPEC/STRUCTURE/RATIONALE.
3. **Role disposition:** move a recurring method into a skill or a deterministic operation into a tool; identify the retained caller, interaction, recovery and output contracts and the exact replacement before live retirement.

These scopes separate the destination design from what can be faithfully applied under current contracts. Each can be proposed for user judgment now.

## 4. Existing migration authority and evidence

`docs/governance_harness/_DECISIONS/D-GOV-10_workflow_component_architecture_normalization.md` explicitly permits component requalification and slimming; changes to its ruled directions require superseding owner decisions. D-GOV-11 establishes the current roles and runtime positions. D-GOV-13 `:32–44` permits future dedicated-specialist replacement with a skill/tool after method, callers, compatibility, historical-reference posture, validators and tests land together. D-GOV-17 locates model capability direction in session steering and puts owner judgment above defective instruction-surface validators. D-GOV-18 contains previous role slimming and method-extraction decisions.

This audit offers recommendations against that history. The recommendations are not accepted new classifications.

## 5. Project and publication dependencies

The App authority-corpus reconciler explicitly includes `AGENT_SOFTWARE_DECOMP.md` and `AGENT_DOMAIN_ENGINE.md` (`projects/chirality-app-dev/execution/_Reconciliation/References/reconcile_authority_corpus.py:44–58`); its corpus is `AUTHORITY_CORPUS.json` in that directory. This is a concrete downstream adoption/currency dependency.

Current parser, roster, managed-delegation and Runtime discovery consumers above are additional affected project surfaces. Existing notices in App, Piping and PEC coordination directories show instruction updates have been routed there. `domains/chirality` is absent in this checkout; historical references alone establish neither its present location nor a current receiving route.

The public exporter includes the complete `agents`, `skills`, `tools`, `docs` and `init` directories (`exports/chirality-app/export_public.py:21–39`). A selected instruction or method migration therefore also has an export-regeneration disposition.

The exact affected project/mirror/export census must be refreshed for the selected implementation diff. The present audit has no live instruction changes to route. A future tranche follows the shared change-notice rule, D-GOV-21 M2/G4/M6 and the receiving loop's own adoption instruments. The source-code inventory is a starting point, not an exhaustive project-coupling census.

## 6. Behavioral evidence to collect after candidate selection

Use matched current/candidate runs on the same role-relevant scenarios, with the same supplied context, harness and model settings. Record those actual settings per run. Judge role distinctness, task completion, human interaction, handling of uncertainty and fidelity to interfaces. Include ordinary use, an ambiguous situation and a recovery case. The per-agent cards propose specific probes. Report improvements, regressions and inconclusive outcomes separately. Word count is a descriptive measure; semantic sufficiency and behavioral improvement require their own evidence.

## Limitations

Read-only source inspection and one existing structural validator run; no shortened-agent trials, production workflows, deployed-runtime verification, or exhaustive foreign-project adoption survey were performed. Some working-tree governance documents carry prospective migration banners; the cited historical ruled instruments and live contracts establish this audit's limited conclusions. The proposal itself changes no authority or live role.
