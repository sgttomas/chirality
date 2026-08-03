# Architecture Alternatives — No Selection

The two-target and domain-first requirements are fixed. This comparison tests
implementation form only. Each variant preserves Woven Dialogue, governed
work/agent projections, existing compatibility routes, App affected-client
status, and Root ownership of generic runtime semantics.

## Variant A — One lightly skinned codebase

One Next/Electron application and one shell composition remain load-bearing.
A ruled product profile selects copy, visual resources, initial navigation,
domain-typed agent presentation, structured-information views, workflows, and
decision-gate affordances. Packaging may run the same build with target
configuration to emit distinct artifacts, but target conditionals live in the
same application graph.

Strengths:

- closest to the current single-workspace/single-entry topology;
- smallest initial extraction cost and shortest domain-first path;
- shared accessibility, compatibility, and Woven regressions stay directly
  exercised in one composition.

Risks/tradeoffs:

- target conditionals can spread beyond an explicit skin boundary;
- domain-only workflows can accidentally appear in standalone mode;
- distinct bundle identity/resources still require target-specific build
  controls even if source remains one graph;
- every common change must exercise both configuration permutations;
- a later second domain may turn “light skin” into implicit plugin
  architecture without a governed contract.

Evidence needed before selection: a complete product-profile field inventory,
conditional-import census, two-target route/resource proof, and a demonstration
that domain-specific workflow/decision surfaces remain bounded to named slots.

## Variant B — Shared core with target-specific shells

Shared components, client adapters, contracts, and presentation primitives
move behind internal packages. Separate standalone and per-domain shell entry
points own navigation composition, target identity/resources, and packaging
manifests.

Strengths:

- explicit isolation of identity, resources, entry routes, and domain-specific
  workflow composition;
- target leakage is easier to detect through dependency boundaries;
- multiple future domain applications can evolve shells without making the
  standalone shell conditional-heavy.

Risks/tradeoffs:

- largest near-term package/build reorganization;
- common Woven/Workbench/Pipeline behavior can drift or be duplicated by shell
  composition;
- shared-core boundaries become a new internal API requiring version and
  compatibility discipline;
- two Electron/Next application graphs multiply build, package, and smoke
  evidence;
- may be disproportionate before a concrete first-domain UI delta is frozen.

Evidence needed before selection: a shared-core extraction map, duplicate-risk
analysis, shell dependency graph, build-time cost estimate, and proof that
compatibility routes/accessibility stay equivalent in both shells.

## Variant C — Build-time product profiles over a shared shell

A versioned declarative product manifest is consumed at build time to emit
separate standalone and domain artifacts from one shared Woven shell. Target
adapters fill named composition slots and resource/identity fields; runtime
dynamic skin switching is excluded. This differs from A by making the target
an immutable build input with separately validated outputs, and from B by not
creating independently composed full shell applications.

Strengths:

- explicit, auditable target identity/config/resource boundary;
- separate artifacts without a full shell fork;
- compile-time target selection reduces accidental runtime cross-target bleed;
- matches domain-first delivery while retaining one shared interaction shell.

Risks/tradeoffs:

- the manifest and slot schema become a product-level compatibility contract;
- build tooling can hide architectural coupling if target adapters import
  unrestricted App internals;
- sufficiently large target adapters recreate separate shells indirectly;
- a single shared shell may still constrain mature domain workflows;
- packaging/test matrix is still two-dimensional.

Evidence needed before selection: a minimal manifest/schema proposal, strict
slot/import rules, generated-artifact identity proof, and a size/complexity
threshold that triggers reconsideration of Variant B.

## Comparative summary

| Criterion | A: light skin | B: shared core + shells | C: build-time profiles |
|---|---|---|---|
| Fit to current topology | strongest | weakest initially | strong |
| Target isolation | lowest unless disciplined | strongest | medium/strong |
| First domain lead time | shortest | longest | medium |
| Multi-domain scaling | conditional-sprawl risk | strongest explicit model | bounded by manifest/slots |
| Packaging identity | separate build parameters required | explicit per shell | explicit per target build |
| Shared UI parity | inherent but permutation-tested | package contract required | inherent but output-tested |
| Reversibility | easy initially; harder after conditionals spread | costly initial move | moderate; can graduate to B |
| Scope-change pressure | likely text/config amendments | likely substantial structural amendment | likely text/config/build amendment |

No variant is selected by this document. Current evidence establishes
plausibility, not fitness. In particular, the first domain's exact typed-agent,
structured-information, workflow, and decision-gate surface has not yet been
frozen into App-owned product requirements.
