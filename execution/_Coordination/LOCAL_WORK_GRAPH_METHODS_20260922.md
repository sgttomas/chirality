# Local work graph methods — implementation and review

Basis: `379df923927d157be3ebb51d8a1dcf783d970112`. Owner: Ryan Tufts. Integration: HELP_HUMAN `/root`.

## Authorization and scope

Owner direction in this task, 2026-09-22, transcribed verbatim:

> You may open the PR and merge when the CI goes green.  Select the appropriate level of CI for this.

This follows the owner's review and revision of the two workflow drafts,
App/Piping LOOP_INIT replacements and companion instruction changes. Earlier
clarification selected "Infer and clarify material gaps". Source integration
is authorized; no product work, run activation, lifecycle acceptance or release
is initiated by this tranche.

The methods are registered in Root's bundled library as
`chirality-root:bundled:workflow:construct-local-work-graph` and
`chirality-root:bundled:workflow:bounded-reconciliation`. They use specialist
navigation categories Plan & organize and Review & check, leaving central/Core
membership unchanged. The authoring basis is the bundled create-workflow method.
The reviewed draft bytes remain local to the original task; maintained packages
are committed at `workflows/` and do not depend on those drafts or ZIPs.

## Integration with current main

The draft basis was `00115c719`; current main contains the separately activated
App/Piping September 21 whole-corpus reconciliation graphs. Both entry pointers
now locate those graphs instead of App `none` / the older Piping UI graph.
Existing phase cursors, pinned methods and owner gates remain operative.
The newly merged D-GOV-44 claim-granularity rule is reflected in the bounded
method: requirements and stable scope remain distinct from mechanism detail.
No in-flight run is silently re-pinned or switched to the new method.

The companion changes relocate substantive checks/fences into the owning
project AGENTS files, preserve historical evidence citations and receipt
validation, and distinguish pointer maintenance from behavioral instruction
amendments. Notices route to App, Piping, Runtime and PEC.

## Verification and independent review

Validation is recorded against the actual candidate in the PR. Required local
coverage comprises workflow metadata/catalog/discovery, instruction entrypoints,
agent contracts, routed practitioner-harness/validation/workflow-runtime tests,
self-check, App hold-register integrity and G0–G4. Product source and build
configuration are untouched, so product-profile build and native witnesses are
not newly required locally. Existing hosted path-selection policies still
apply; no bypass label, check waiver or CI policy change is part of this work.

Local validation on source commit `aa6ff06c71143fdb882f7e2d0645b27bd6f5c62c`:

- Routed practitioner-harness, validation and workflow-runtime suites: **918
  passed, 48 subtests passed**. The initial run found only obsolete catalog
  counts (59 specialists before these two additions); counts and explicit new
  group assertions were updated. The focused 21-test catalog suite also passes.
- Workflow metadata: **74 valid packages, zero invalid**; generated index:
  **82 methods**, current; both source-qualified methods resolve through the
  Root resolver in HELP_HUMAN/TASK roles respectively.
- Agent contracts and instruction entrypoints: PASS. Self-check: exit 0,
  **no BLOCK** (14 INFO, 1 NOT_APPLICABLE, 4 REVIEW, 113 WARN).
- G0/G1/G2/G3 and actual-range G4: PASS. Conflict-marker and diff checks: PASS.
- App hold integrity: 54 contracts scanned, zero held, register match, PASS.

Local verification used an isolated Python environment with PyYAML, pytest,
pytest-xdist and numpy; no repository dependency files changed. Hosted CI uses
its own declared environment. On this complete diff, the existing Piping
selector chooses **full** coverage for shared paths rather than not-applicable.
App pre-merge and PEC tests also trigger. All selected hosted checks must pass
on the actual PR candidate; no artifact-proof label or selector override is used.

Independent review: fresh read-only TASK `/root/adoption_review`, configured
`gpt-5.6-terra` / high, via native `collaboration.spawn_agent`, parent `/root`.
The reviewer did not implement the changes and cannot delegate. Write scope was
empty; that limit was instruction-asserted in the shared filesystem, not a
sandbox claim. Exact launch and return are retained in the task conversation;
its final verdict and checked revision are recorded in the PR before merge.
A separate read-only Terra/high TASK inspected CI selection and notice routes;
parent corrected its initial not-applicable prediction by running the actual
Piping selector on the complete candidate.

Supplied instruction origins are repository-relative. Parent initially read
Root/project instructions at the base revision above; candidate review uses
updated instructions. Role and method bodies are unchanged from that base.
The following hashes bind the final candidate instruction/method bytes:

| Source | SHA-256 |
|---|---|
| `AGENTS.md` | `1bb670ca339a990b153cf033dac2d8e29ca71bdea0accee4200e6dd1feed3d57` |
| `agents/AGENT_HELP_HUMAN.md` | `0c2fe7a3097ad26c93c0267e4da6aaf90c9264489df8dc368fad657bcac69183` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `.agents/skills/chirality-change/SKILL.md` | `2b490e172436417896c1cd25dbcd543c676e3473aa58b7663985d75785ff7dba` |
| `.agents/skills/software-code-review/SKILL.md` | `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a` |
| `workflows/create-workflow/WORKFLOW.md` | `7d4443b63c474a8727a1391dca2e4c20b3a81a04d344d575d862be8f8536cf10` |
| `projects/chirality-app-dev/AGENTS.md` | `abb4ff48987b427015ef412874aef8651e028fbc62c49fc3e53a3a9b755b015f` |
| `projects/chirality-piping/AGENTS.md` | `d8a1f4380962efcd258571c6fb563722be9e2e89d4fa5898b7f6d24dc61ab879` |
