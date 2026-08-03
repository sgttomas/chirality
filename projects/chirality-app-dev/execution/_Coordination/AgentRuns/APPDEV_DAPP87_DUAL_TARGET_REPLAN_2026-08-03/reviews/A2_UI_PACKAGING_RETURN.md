# A2 UI and Packaging Review Return

RunID: `APPDEV_DAPP87_DUAL_TARGET_REPLAN_2026-08-03`

Role: ephemeral Agent 2 generalist; no delegation

Status: `COMPLETE — DERIVATIVE REVIEW — NO ARCHITECTURE SELECTED`

## 1. Executive finding

The frozen basis is sufficient to prepare an owner proposal that compares
implementation forms and authorizes a later bounded design/prototype tranche.
It is not sufficient to select or eliminate an architecture, amend the PRD or
decomposition, assign final package identities, or claim either target is
validated.

The adopted facts are preserved:

1. there are two product targets: standalone Chirality Desktop and a
   per-domain control plane; and
2. delivery is domain-first because domain applications are the primary
   vehicle for agents.

Three viable forms remain open:

- **A — lightly skinned one codebase:** one application composition and shell,
  parameterized by a governed target/domain descriptor;
- **B — shared core with target-specific shells:** shared semantic/runtime UI
  packages with separate Desktop and domain composition roots; and
- **C — build-time target compositions:** one source workspace and common
  component graph, but deterministic build-time entry generation and immutable
  target resource manifests produce target-specific outputs without creating
  durable shell packages.

Variant C is evidence-grounded by the existing single Next/Electron workspace,
internal `packages/*` capability, route-based Woven composition, closed
code-defined domain-profile registry, and electron-builder resource manifest.
It remains a hypothesis; no current script, manifest, or accepted package proves
that form.

## 2. Evidence and authority boundary

| Class | Material used | Effect in this review |
|---|---|---|
| Adopted authority for this run | D-APP-87 ruling and selected packet | Fixes two targets and domain-first emphasis; requires comparison and leaves architecture unselected. |
| Accepted product/decomposition basis | `docs/PRD.md`; active v3.2 decomposition; active SCA pointer and SCA-APP-004/005/007 handoffs; validation, quality-gate, and build/release documents; D-APP-36 ruling | Defines current requirements, topology, semantic ownership, evidence bar, and protected boundaries. It is not amended here. |
| Live working state | `frontend/package.json`, `next.config.mjs`, Woven Dialogue shell, domain-profile registry, Electron main entry | Shows one current application/packaging identity and the actual coupling seams. Live state is not product authority. |
| Derivative evidence | D-APP-89 migration return/handoff; D-APP-88 R2 return/handoff | D-APP-89 supports the current direct Root-contract consumer posture. D-APP-88 proves only that a distinct Electron helper can be structurally packaged; its product bytes were rolled back and the required graceful-stop proof failed. |
| Coordination only | Root response notice and graceful-stop investigation notice | Names open/deferred Root gates and an unproven shutdown hypothesis. Neither notice defines product or runtime truth. |

No D-APP-88 helper artifact is treated as accepted target packaging. No generic
runtime, sandbox, identity, version, resume, or Bash semantic is selected here;
those lanes remain `BLOCKED_BY_ROOT`.

## 3. Current-state findings

1. `frontend/` currently has one npm workspace, one Next application, one
   Electron entry, one builder configuration, `appId=com.chirality.app`, and
   `productName=Chirality`. It has no target descriptor schema, target build
   matrix, second shell package, or second accepted packaging manifest.
2. The Woven Dialogue shell already centralizes shared composition: primary
   dialogue, Work/Agents coordination, recorded-session replay, Navigator,
   Workbench, Pipeline, Activity Shelf, persona selection, and local layout
   state. This is a favorable seam for all three variants but does not prove
   that all surfaces should appear in both targets.
3. Existing UI state is project-scoped and stored locally, but it is not
   target-namespaced. Two targets using one user-data location could therefore
   couple layout, active-surface, replay-selection, and other convenience state
   unless a target namespace or separate product identity is ruled.
4. The domain registry is closed and source-defined for exactly
   `open_pipe_stress` and `pec`. It carries evidence/transport metadata, not
   product branding, navigation, agent catalogue, workflow, resource, or
   packaging configuration. It must not be silently promoted into a skin
   registry.
5. Electron currently derives its packaged instruction root from
   `process.resourcesPath`, serves the packaged Next tree from `app.asar`, and
   uses one application `userData` area for runtime paths. These are direct
   configuration/resource/identity coupling points.
6. The current package includes broad shared resources (`agents/`, project
   docs, root instruction files, runtime CLI) and one product icon/category.
   A domain artifact needs an explicit decision on whether it carries the full
   instruction root, a verified subset, or a shared external installation; the
   basis does not choose among them.
7. The current unsigned local evidence commands prove only the current
   standalone configuration. A successful `desktop:pack` or `desktop:dist`
   cannot prove a domain-target claim without target-bound artifact identity,
   configuration, resource, launch, and UI evidence.
8. D-APP-89 removes ordinary App reliance on the deprecated facade while
   retaining rollback identity. This reduces one source coupling but does not
   choose a target architecture.
9. D-APP-88 demonstrates that electron-builder can produce a separate bundle
   with distinct identity and embedded resources. Because its source was
   rolled back and its terminal graceful-stop evidence failed, it is diagnostic
   evidence only. Its shutdown issue is specifically relevant if an option
   introduces a separately activated helper/daemon bundle; it does not by
   itself eliminate a separate UI shell.

## 4. Shared and target-specific surface map

The table distinguishes semantic ownership from presentation. “Shared” means
the invariant should be implemented or consumed consistently; it does not
require identical visual density or navigation in both targets.

| Surface | Shared invariant/core | Standalone Desktop emphasis | Per-domain control-plane emphasis | Boundary |
|---|---|---|---|---|
| Woven Dialogue | One mounted primary dialogue; provenance-bearing artifacts; read-only selected-session replay; no second evidence store; live/replay distinction | Broad workspace navigation, working-root selection, Workbench, Pipeline, toolkit/settings, compatibility routes, multi-domain/operator context | Domain-scoped entry, reduced navigation, domain-context header, focused outcome path, explicit return/escalation to broader Desktop where ruled | Skin may change labels, order, density, and defaults. It may not change authority, replay isolation, accepted-record provenance, or primary-dialogue ownership. |
| Typed agents | Canonical agent/persona IDs, aliases, recorded hierarchy, session parentage, disabled/unavailable semantics, guarded selection | Full ruled persona/agent catalogue and compatibility matrix/aliases | Governed domain allowlist and defaults; domain-oriented descriptions and task starters; only recorded parentage shown | A target descriptor may filter/present an already-authorized catalogue. It may not mint agents, infer hierarchy, or grant tools/runtime capability. |
| Structured information | Source class/reference, authority class, status basis, currency, exact recorded relationships, stale/missing/conflict states | General deliverable artifacts, file tree, Work/Agents, Workbench and Pipeline records | Domain profile facts, protected/proposal path notices, domain evidence envelopes, operation proposals where separately authorized | Structured views remain projections over admitted sources; a skin/config file is not project or domain truth. |
| Workflow | Shared workflow-state vocabulary, route/query compatibility where applicable, explicit disabled states, recorded work only | General DECOMP/PREP/TASK/AUDIT navigation and broad working-root operations | Domain-specific guided sequence toward an outcome; domain stages can wrap or link to presentation-neutral dispatch semantics | Domain workflow labels/order may be target-specific. Dispatch meaning remains with DEL-08-03; current-release domain operation execution remains fenced. |
| Decision gates | Human authority; proposal/draft/evidence distinguished from accepted truth; no professional-approval claim | General approvals, lifecycle and permission interactions already in scope | Prominent domain operation/proposal gate, deterministic-check evidence, protected-path and solver-truth notice | UI may expose or focus a gate already authorized. It may not create approval, apply protected-domain changes, or redefine generic runtime permission semantics. |
| Runtime/client feedback | Typed App-facing state, errors, connectivity, retry, key/credential status; one generic semantic owner remains Root | Broad operator diagnostics and settings | Minimal domain-relevant status and recovery; enough evidence to avoid hiding blocked/unavailable states | Target presentation/configuration is App scope. Generic identity, sandbox, resume, version, Bash, daemon, and credential semantics remain Root-owned or blocked. |

### Accessibility invariants

Both targets require independently demonstrated:

- named landmarks and unambiguous region labels;
- keyboard traversal, collapse, resize, focus entry, and focus return for every
  region present in that target;
- focus preservation when the target descriptor hides, reorders, or replaces a
  navigation surface;
- accessible names and state for target/domain selectors, typed-agent choices,
  structured records, disabled actions, gates, and error/retry controls;
- contrast, zoom/reflow, reduced-motion, truncation, long-label, empty/stale,
  conflict, and narrow-window behavior for target-specific copy/resources; and
- no inaccessible fallback path when a domain resource/configuration is absent,
  invalid, or mismatched.

The current Woven shell's keyboard-operable separator controls are useful live
evidence, not proof for a target configuration that changes the regions.

### D-APP-36 consequences

D-APP-36 applies per target and per materially different configuration:

- component/render tests are required for user-facing target switches,
  navigation, agent choices, structured-information states, workflow states,
  gates, disabled/active controls, missing configuration, and target-specific
  copy/resources;
- browser screenshots or browser-level checks are additionally required for
  high-risk layout, viewport, overlap, focus, or interaction differences;
- a shared component test may prove invariant behavior once, but it cannot
  prove that both target compositions include and configure it correctly; and
- Desktop evidence cannot stand in for a domain target, nor can one domain
  profile stand in for all materially distinct domain configurations.

## 5. Candidate skin, configuration, and resource boundaries

### 5.1 Candidate target descriptor

A comparison/prototype may test a validated, immutable descriptor with fields
such as:

- descriptor/schema version;
- `targetKind` (`desktop` or `domain-control-plane`);
- stable target key and, for domain targets, ruled `domainProfileId`;
- presentation-only route allowlist/default route and navigation ordering;
- allowed/default canonical persona or agent IDs;
- presentation-only workflow and structured-view registrations;
- product display name, boundary copy key, icon/theme resource keys;
- resource-manifest hash and build/source revision; and
- local-state namespace/migration version.

`ASSUMPTION:` those are candidate comparison fields, not adopted contract
fields. Capability, tool, sandbox, provider, credential, identity, domain-write,
and human-approval grants must not be inferred from the descriptor. Unknown or
unruled values must fail closed rather than fall back to filesystem discovery.

### 5.2 Shared code/config boundary

Candidate shared code includes:

- Woven Dialogue semantic composition and authority/provenance components;
- typed-agent canonical identity and guarded selection;
- Work/Agents and replay projection contracts;
- presentation-neutral Pipeline dispatch semantics;
- accessibility primitives and common design tokens;
- App-side runtime-client/event/error adapters; and
- configuration parsing, schema validation, and mismatch reporting.

Candidate target-specific configuration includes route visibility/defaults,
navigation density, domain profile binding, view registrations, copy keys,
branding resource keys, local-state namespace, and build artifact metadata.
Changing any of those into a capability grant or semantic owner would cross the
configuration boundary and require a separate authority review.

### 5.3 Resource boundary

| Resource class | Candidate shared posture | Candidate target-specific posture | Required guard |
|---|---|---|---|
| Instruction root and agent instructions | Versioned, integrity-checked governed source | Either the same verified set or an explicitly ruled/verifiable subset | No silent omission, ambient discovery, mutable post-build substitution, or target-specific authority fork. |
| Next/Electron application bytes | Reusable components, runtime-client adapters, common shell primitives | Entry composition and/or generated bootstrap depending on variant | Output must bind to source revision, target descriptor hash, and manifest. |
| Domain profile/evidence resources | Closed schema and validation machinery | Exact ruled profile and domain assets required by the target | Profile identity/hash must match the artifact; no registration-by-presence. |
| Brand/copy/theme/icon | Shared Chirality identity and professional-boundary vocabulary | Domain display name, icon/theme/copy only after owner ruling | Target copy must preserve Chirality identity, human authority, and solver-truth separation. |
| Local operator state | Shared schema and migration tooling | Target/domain namespace or separate user-data root | No state bleed, authority transfer, replay mounting, or destructive migration. |
| Build evidence | Common evidence schema and command semantics | Separate summaries, paths, checksums, identity/resource extracts, launch and UI results | Evidence artifact is derivative and target-bound; it is not release or product truth. |

## 6. Variant comparison

| Dimension | A — lightly skinned one codebase | B — shared core + target-specific shells | C — build-time target compositions |
|---|---|---|---|
| Composition | One durable application shell reads a governed target/domain descriptor. | Shared semantic/component packages are consumed by separately owned Desktop and domain shell entrypoints. | A deterministic generator/build step emits target entry/config/resource manifests from one source graph; generated compositions are not maintained as shell packages. |
| Shared/target boundary | Maximum runtime sharing; target differences concentrated in descriptor, resources, and conditionals/registries. | Explicit compile-time boundary between common core and each shell; target behavior can diverge without pervasive conditionals. | Shared sources plus build profiles; differences are explicit in generated manifest/entry output but less structurally isolated than separate packages. |
| Artifact identity | Could be one generic app artifact plus external/embedded domain descriptors, or separately built identities from the same manifest. Owner must choose. | Naturally supports separate bundle IDs, product/executable names, icons, resources, update channels, and user-data roots. | Naturally supports separate output manifests and possibly separate bundle IDs while retaining one common Electron main and dependency graph. |
| Configuration | Highest dependence on runtime/config validation and fail-closed feature gating. | Shell code fixes more decisions at build time; smaller runtime target config. | Build-time config is frozen into output; runtime switching can be prohibited or narrowly limited. |
| Resource isolation | Weakest by default; must prove domain artifacts do not accidentally ship unrelated resources or expose irrelevant routes. | Strongest structural resource boundary, at cost of duplication and shell drift. | Intermediate: resource allowlists can be generated per target, but generator correctness becomes load-bearing. |
| UI coupling | Risk of target conditionals spreading through Woven, navigation, tests, and local state. | Risk of duplicated composition/accessibility behavior and semantic drift between shells. | Risk of opaque generated differences, build-profile combinatorics, and source-to-output traceability gaps. |
| Packaging coupling | Smallest initial manifest change if one binary is reused; identity/user-data semantics become ambiguous. | Largest packaging surface: multiple configs, entrypoints, manifests, icons, output paths, and lifecycle tests. | Moderate packaging surface: target matrix/generator plus target-specific builder overrides/outputs. |
| Domain-first fit to test | Fast addition of a ruled descriptor may favor early domain slice; must prove domain experience is not merely hidden Desktop UI. | Domain shell can lead sequencing without forcing Desktop presentation decisions; shared-core extraction can delay first vertical slice. | Domain build profile can lead with a thin vertical slice; generator/manifest tooling may become premature infrastructure. |
| Reversibility | High while descriptor fields remain presentation-only; decreases if conditionals enter semantics or persisted state. | High at target boundary, lower if shared-core extraction causes broad refactors or shells fork. | High if generated artifacts are reproducible and disposable; low if generated source is hand-edited or becomes authority. |
| Current supporting evidence | One shell, one route graph, shared components, closed registry. | Existing internal workspaces and D-APP-88 structural proof that a separate Electron artifact can be built. | Existing single source graph, builder manifest, internal workspaces, and deterministic closed registry are compatible with profile-driven generation. |
| Current disconfirming evidence/gap | No target descriptor, state namespace, resource partition, or multi-target evidence. | No accepted second shell/config; D-APP-88 bytes rolled back and helper graceful-stop proof failed. | No generator, source/output concordance, target manifest schema, or accepted generated composition. |

None of these observations selects a variant.

## 7. Packaging topology and unsigned local evidence

### 7.1 Artifact identity/configuration/resource questions

The owner proposal should preserve these as explicit later gates:

1. Is the domain target one generic “Chirality Domain” artifact that consumes a
   governed descriptor, or one artifact per domain? The basis does not answer.
2. Does each target have a distinct bundle ID/product/executable name and
   `userData` root, or does a shared identity select a target at launch? This is
   unruled and coupled to generic identity/runtime questions that may require
   Root coordination.
3. Does a domain artifact embed the full instruction root, a ruled subset, or
   reference an installed shared resource? Any choice must retain integrity and
   version evidence.
4. Are domain resources compiled/embedded, selected from an allowlisted bundle,
   or supplied externally? Ambient profile discovery is inconsistent with the
   current closed-registry posture.
5. Are standalone and domain artifacts independently versioned, upgraded, and
   rolled back? Release channels/signing/publication remain outside this run.

### 7.2 Candidate target-bound evidence matrix

| Evidence item | Standalone Desktop | Each domain target/configuration |
|---|---|---|
| Source/config identity | Commit or dirty-state declaration; Desktop descriptor/manifest hash | Same source identity plus exact domain descriptor/profile/resource-manifest hashes |
| Static/config checks | Schema pass; route/agent/resource references resolve; no domain-only leakage assertions | Schema pass; ruled profile match; allowlists resolve; unknown/extra resources and agents fail closed |
| Component/render | Shared invariant tests plus full Desktop navigation, compatibility, Workbench/Pipeline, replay, settings and error states | Shared invariant tests plus typed-agent, structured-information, workflow, gate, missing/stale/conflict, unavailable and boundary-copy states |
| Browser/manual risk | Desktop viewports, resize/collapse/focus, route/query/deep-link compatibility | Domain viewports, long domain labels, focus after filtered/reordered regions, gate interaction, cross-domain leakage checks |
| Build | `npm run build` or target-specific equivalent bound to Desktop output | Target-specific build bound to exact descriptor and generated/selected entry |
| Package layout | `desktop:pack`; dependency boundary; instruction-root integrity | Domain pack equivalent; dependency boundary; target resource/instruction-root integrity; absence of unallowed domain resources |
| Artifact identity | Extract bundle ID, product/executable name, version, icon, category, output path, checksum | Extract the same fields and prove uniqueness/equality according to the later ruling; prove descriptor/profile identity inside artifact |
| Local state isolation | Desktop user-data/runtime/state path and migration evidence | Domain target/domain namespace or separate path; no layout/draft/replay/config bleed across Desktop or domains |
| Launch/smoke | Unsigned local launch, packaged Woven/Workbench/Pipeline/guarded-selection smoke, packaged replay/runtime feedback | Unsigned local launch directly into correct domain context; typed-agent → structured info → workflow → decision-gate smoke; invalid/missing descriptor graceful failure |
| Runtime client | App affected-client behavior only; current daemon/client contract references | Same affected-client behaviors with target attribution; no new generic semantic claim |
| Evidence interpretation | Unsigned/unnotarized local derivative evidence only | Unsigned/unnotarized local derivative evidence only; one domain result does not prove another materially different domain |

The current `desktop:pack`/`desktop:dist` scripts and output directory are
single-target. A later implementation must use distinct output paths and
stable target-labelled summaries so concurrent builds cannot overwrite or be
mistaken for one another.

## 8. Candidate deliverable mapping

“Amend” below means a candidate for a later ruled PRD/decomposition or
deliverable-record amendment. This review performs no amendment. “Evidence
only” means the semantic description may remain but target-specific acceptance
and Remaining text likely change.

| Existing deliverable(s) | Candidate disposition | Reason |
|---|---|---|
| `DEL-01-03` | Direct amendment | Product identity, target/domain display names, package copy, human-only authority, and domain solver-truth notices require two-target wording and evidence. |
| `DEL-02-01` | Direct amendment | The Woven shell and compatibility navigation need an explicit shared invariant and target-specific composition/visibility contract. |
| `DEL-02-02` | Direct amendment | Work/Agents, Workbench, Pipeline, structured information, and domain workflow/gate presentation must be mapped per target without moving semantic ownership. |
| `DEL-02-03` | Direct amendment | Working-root selection, file-tree/scope presentation, and domain-context binding need per-target requirements and evidence. |
| `DEL-02-04` | Direct amendment | Descriptor-driven layout/defaults and target/domain state namespaces require migration, rollback, and no-state-bleed criteria. |
| `DEL-02-05` | Direct amendment | Key/runtime/error/attachment presentation must remain available or intentionally re-presented in each target without creating a second credential owner. |
| `DEL-05-04` | Evidence/acceptance amendment | Replay/projection semantics remain shared and unchanged, but real-daemon rendering and same-session Desktop/CLI evidence must be target-attributed; a domain target must not mount replay as live dialogue. |
| `DEL-08-02` | Direct amendment | Target/domain route defaults, agent/persona allowlists, aliases, guarded session selection, and compatibility behavior require an explicit target-neutral semantic contract. |
| `DEL-08-03` | Direct amendment | Domain workflow presentation must reference, not redefine, presentation-neutral category/task-scope dispatch and disabled-option rules. |
| `DEL-08-05` | Cross-reference / no semantic change | Parent-child records and accepted artifact paths remain checkout evidence. Targets consume the same records; only target attribution in UI/evidence may be referenced. |
| `DEL-09-01` | Direct evidence amendment | Section 8/premerge evidence must identify target and prevent a Desktop-only pass from proving a domain claim. |
| `DEL-09-02` | App affected-client evidence amendment | Target attribution may extend App validation IDs/summaries; no generic runtime semantics may be added. |
| `DEL-09-03` | Direct evidence amendment | Component, integration, configuration-failure, route, accessibility, and cross-target isolation coverage becomes a two-target matrix. |
| `DEL-09-04` | Direct amendment | Owns builder configurations, artifact identities, resources, instruction-root integrity, target output isolation, unsigned package layout, and target-specific packaged smoke. D-APP-88 remains diagnostic/blocked evidence, not completion. |
| `DEL-09-05` | Direct amendment | Local/CI artifact names, matrices, checksums, summaries, and manual verification must be target-labelled; signing/publication remains unselected. |
| `DEL-09-06` | Direct evidence amendment | Renderer allowlist, key/storage, attachment, resource/config injection, and cross-target leakage checks must cover both targets without expanding provider/network policy. |
| `DEL-10-01` | Direct boundary amendment | The future domain profile contract needs an explicit relationship to product target descriptors while keeping engine identity separate from skin/package identity. |
| `DEL-10-02` | Cross-reference unless protected/proposal paths enter the target UI | Existing protected/proposal path policy remains sufficient for a presentation-only target. Amend only if packaging/configuration or UI introduces a new path boundary. |
| `DEL-10-03` | Cross-reference unless operation-proposal gates are activated for presentation | Existing human-gate semantics remain; a focused UI may reference them but cannot activate apply or acceptance. |
| `DEL-10-04` | Cross-reference, then evidence amendment when another domain configuration is ruled | Current fixture/profile validation remains future-boundary work. A per-domain product target does not itself activate engine execution. |
| `DEL-10-05` | Direct amendment | Domain-target copy and package/UI notices must preserve solver truth, Chirality identity, and no-professional-approval claims. |

### Runtime/client families to cross-reference, not redefine in this lane

| Existing deliverable(s) | Disposition in UI/packaging proposal |
|---|---|
| `DEL-03-01`, `DEL-03-02`, `DEL-03-03`, `DEL-03-04` | Cross-reference affected-client interfaces and target evidence only. Preserve Root ownership and the D-APP-89 facade-retirement residual. |
| `DEL-04-01`, `DEL-04-02`, `DEL-04-05` | Cross-reference version/options/credential/network participation. No provider, settings, identity, or generic configuration semantic is selected. |
| `DEL-05-01`, `DEL-05-02`, `DEL-05-03`, `DEL-05-05` | Cross-reference canonical session/event/redaction/result ownership; target UI/resource changes do not create duplicate stores. |
| `DEL-06-01`, `DEL-06-02` | Cross-reference policy/catalog and disabled-state presentation; target configuration cannot grant tools or permissions. |
| `DEL-08-04` | Cross-reference checkout authority and daemon delegation boundary; domain-first presentation does not authorize new subagent capability. |

The mapping retains the accepted 10-package / 51-deliverable / 78-SOW-row /
10-objective topology. Any direct amendment remains a later SCOPE_CHANGE and
owner act; no new deliverable is proposed here.

## 9. Coupling, reversibility, and risks

| Risk/coupling | Options most exposed | Reversible control | Elimination signal |
|---|---|---|---|
| Target conditionals leak into semantic owners or capability decisions | A, C | Presentation-only descriptor schema; dependency rules; fail-closed unknowns; semantic contract tests | Eliminate if a representative domain slice requires branching canonical routing, replay, permission, or runtime semantics throughout shared code. |
| Shell drift duplicates Woven/replay/accessibility behavior | B | Shared semantic packages; contract/render suites run against both shells; minimal composition roots | Eliminate if keeping one change conformant in both shells requires repeated target-specific semantic fixes or unacceptable duplicate ownership. |
| Generated build output becomes opaque or hand-maintained | C | Disposable generation; source-to-output manifest; clean regeneration/diff check; generated artifacts never authoritative | Eliminate if byte-reproducible generation and source/config traceability cannot be achieved without checked-in divergent source. |
| Product identity/user-data/runtime identity collision | All; greatest for A with one identity and B with a helper-like artifact | Explicit owner gate; isolated local evidence; target/domain state namespace; Root coordination where generic identity is implicated | Eliminate a concrete topology if it cannot prevent state/LaunchServices/runtime ownership collision under the ruled identity boundary. |
| Unrelated domain resources or agents leak into a domain artifact | A, C | Resource allowlist, closed registry, negative package inspection, visible unavailable states | Eliminate if target-bound package inspection cannot prove resource/catalog isolation. |
| Domain target becomes a hidden Desktop rather than focused outcome path | A | Representative domain journey and usability evidence; limit target-only conditionals to governed view registrations | Eliminate if typed-agent → structured info → workflow → gate cannot be expressed without exposing the full Desktop operator surface. |
| Shared-core extraction delays domain-first delivery | B | Thin vertical extraction, preserve current shell, migration manifest, no big-bang move | Eliminate for the first tranche if the smallest coherent extraction cannot deliver a domain vertical slice before broad Desktop refactoring. |
| Build/profile matrix grows combinatorially | C, B | Canonical representative profiles; equivalence classes; stable matrix rules | Eliminate if every domain requires bespoke code/config/evidence rather than schema-conformant composition. |
| Accessibility regressions from filtering/reordering | All | Shared primitives plus per-composition D-APP-36 and browser evidence | Eliminate an implementation if target configuration cannot preserve focus order, return, labels, and disabled-state discoverability. |
| D-APP-88 graceful-stop blocker is overgeneralized | B if it introduces a separate helper/daemon; otherwise limited | Distinguish UI shell bundle from runtime helper; reuse Root investigation evidence; do not inherit failed proof as acceptance | Eliminate a helper-coupled package form only if the required shutdown/identity contract remains unsatisfied after Root disposition. |
| Domain UI implies current domain-operation authority | All | Boundary copy, disabled states, proposal-only semantics, protected-path tests | Eliminate any design that cannot present domain value without implying apply, professional approval, or protected-model write authority. |

## 10. Evidence needed to eliminate an option

Before architectural selection, a bounded comparison should produce the same
representative vertical slice in A, B, and C, preferably against one already
ruled domain profile, with no operation-apply authority. Minimum comparison
evidence:

1. source/path manifest identifying shared and target-specific files;
2. exact target descriptor/configuration and resource manifest;
3. typed-agent → structured information → workflow → human decision-gate
   render path, including missing/stale/conflict/disabled conditions;
4. D-APP-36 component/render results and one high-risk browser/a11y review;
5. state-isolation and rollback/migration proof across Desktop and two domain
   configurations;
6. unsigned local package outputs with extracted identity, resource,
   instruction-root, dependency, profile, checksum, and launch evidence;
7. source-to-package traceability and target-labelled evidence summaries;
8. change-footprint, duplicated-code, conditional-density, package-size,
   build-time, test-matrix, and maintenance-drift measurements;
9. proof that target configuration cannot grant agents, tools, permissions,
   provider/network scope, or domain operations; and
10. explicit Root response or a bounded no-dependency statement for any
    topology whose identity, daemon, user-data, sandbox, resume, or shutdown
    behavior depends on generic Root semantics.

An option should be eliminated only against predeclared thresholds or a
demonstrated invariant violation. Relative code size or aesthetic preference
alone is not sufficient.

## 11. Assumptions and gaps

### Assumptions

- `ASSUMPTION:` “per-domain control plane” permits either one generic domain
  artifact configured for a ruled profile or one artifact per domain; the
  ruling does not disambiguate.
- `ASSUMPTION:` a representative domain vertical slice may be UI/read/proposal
  focused and need not activate current-release domain operation execution.
- `ASSUMPTION:` target-specific labels, routes, resources, and defaults are App
  presentation/packaging concerns when they do not grant generic runtime or
  domain capability.
- `ASSUMPTION:` Desktop compatibility routes remain required until a later
  owner retirement decision; a domain target may omit them only if Desktop
  compatibility remains intact and domain deep-link behavior is separately
  specified.

### Gaps requiring owner proposal or later evidence

1. Exact domain-target artifact granularity and naming are unspecified.
2. Bundle ID, executable/product name, icon, URL protocol, user-data root,
   update channel, install coexistence, and version/rollback policy are unruled.
3. No target/skin descriptor schema, configuration owner, or invalid-config
   behavior is accepted.
4. The exact typed-agent catalogue, structured-information views, workflow
   stages, decision gates, and representative domain journey are unspecified.
5. Full versus subset instruction-root/resource packaging is undecided.
6. No target-specific build, pack, dist, launch, accessibility, D-APP-36, or
   evidence-summary command exists.
7. No measurement defines acceptable duplication, conditional density, package
   size, build time, matrix size, or shell drift.
8. Generic identity/sandbox/version/resume/Bash semantics remain
   `BLOCKED_BY_ROOT`; graceful-stop causality remains unproven.
9. Signing, notarization, publication, external distribution, hosted CI, and
   non-macOS targets remain outside this comparison.
10. A future amendment must reconcile D-APP-87 into PRD/decomposition and the
    exact deliverable records; this derivative review cannot do so.

## 12. Verdict for manager fan-in

`SUFFICIENT_WITH_GAPS_FOR_OWNER_PROPOSAL`

The manager can prepare an owner proposal that:

- preserves the two-target/domain-first rulings;
- compares A, B, and C without recommendation by implication;
- asks for the missing artifact-granularity and bounded comparison/prototype
  decisions;
- carries the candidate deliverable mapping and target-bound evidence matrix;
- names all later PRD, decomposition/SCOPE_CHANGE, packaging identity,
  resource, release, and Root coordination gates; and
- expressly creates no product/source/authority effect.

The basis is **not** sufficient for an architectural ruling unless the owner
chooses to rule under acknowledged uncertainty. No option has current
target-specific package, accessibility, D-APP-36, state-isolation, or
maintenance evidence adequate to eliminate the others.

## 13. Return contract

- Findings: complete.
- Variant comparison: A, B, and evidence-grounded C compared; no selection.
- Candidate deliverable mapping: direct amendment, evidence-only amendment,
  and cross-reference/no-change rows identified.
- Risks/coupling/reversibility: identified with elimination signals.
- Gaps/assumptions: explicit.
- Owner-proposal sufficiency verdict: `SUFFICIENT_WITH_GAPS_FOR_OWNER_PROPOSAL`.
- Product/source/authority decision: none.
- Writes outside this return: none.
