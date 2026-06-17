# R6 — Extensibility & MCP Boundary Maturity Plan

**Date:** 2026-06-17
**Status:** ACCEPTED / ACTIVE / GOVERNING (active development queue)
**Acceptance ruling:** `execution/_Coordination/_DECISIONS/D-APP-14_RULING_2026-06-17.md` (human project authority in chat)
**Product:** Chirality desktop harness and bundled agent operating system
**Working root:** `projects/chirality-app-dev/`
**Prepared by:** `WORKING_ITEMS`
**Follows:** `plans/PLAN_2026-06-16_runtime_stabilization.md` (completed, closed)
**Roadmap anchor:** `docs/PLAN.md` §R6 "Extensibility and MCP Boundaries"

This plan proposes the next bounded app-dev program after the Runtime Stabilization
program completed. It matures the local/in-process tool extension boundary — catalog,
naming, collision prevention, and contributor documentation — now that the runtime tool
surface (read built-ins, read MCP tools, Write/Edit/Bash, and the STAB-04 mutating
Chirality MCP tools) is landed and proven. It does **not** open any new capability:
remote MCP, plugins, remote execution, broad tool search, domain tools, and non-Anthropic
providers all remain out of scope and human-gated. Project truth remains in governed docs,
decomposition and deliverable artifacts, source, tests, evidence records, decision
records, and git history. Humans decide all gates.

This plan was accepted by the human project authority (`D-APP-14`) and is the active
development queue; the coordination surfaces are re-pointed to it. Acceptance of the
program does not pre-approve crossing any §7 fence — those remain human-gated.

## 1. Purpose

R6 is sequenced explicitly *after* local/in-process SDK governance is reliable
(`docs/PLAN.md:260-262`). Stabilization made the tool surface real and proven; R6 makes
that surface **legible, collision-safe, and extensible-by-contributors** without weakening
the permission/hook/path/redaction/event invariants. The binding form of the goal is
`docs/CONTRACT.md:88` **K-MCP-1**: "MCP is a transport, not a bypass. In-process Chirality
MCP tools pass through the same permission, hook, path, redaction, and event logging policy
as SDK built-ins."

## 2. Current Substrate (verified live)

Already landed — R6 builds on, not rebuilds, these:

- **Single source-of-truth descriptor registry.** `HARNESS_TOOL_DESCRIPTORS`, one frozen
  list of 18 descriptors (`frontend/src/lib/harness/tool-descriptor.ts:318-849`; version
  tag `harness-tools.v6.mutating-mcp` at `:13`). Rich `HarnessToolDescriptor` type
  (`:84-105`) carrying surface, permissions, pathScope, idempotence, concurrency,
  resultBudget, provenance, humanGate, `adapter.claudeAgentSdk.toolName`, schemas, and
  runtime-exposure discriminant.
- **Naming convention + chirality-MCP collision helper.** `mcp__chirality__*` builders and
  `isChiralityMcpAllowedToolName` allow-set (`frontend/src/lib/harness/mcp/tool-names.ts:19-45`),
  with typed read (`:3-8`) and mutating (`:10-13`) unions.
- **Registration path.** `buildSdkOptions` → `resolveHarnessToolPool`,
  `filterChiralityMcpAllowedToolNames`, `createChiralityMcpServers`
  (`frontend/src/lib/harness/sdk-options-builder.ts:85,101,127`); each in-process MCP
  `tool()` is gated on its allow-name, and the server attaches only when ≥1 tool is allowed
  (`frontend/src/lib/harness/mcp/read-tools.ts:634-763`).
- **MCP-as-transport enforcement.** The SDK behavior probe (STAB-04) showed raw in-process
  `mcp_message` calls do **not** auto-invoke `canUseTool` or hook callbacks, so each
  mutating MCP handler runs its own fail-closed permission/evidence wrapper
  (`frontend/docs/harness/runtime_engine_contract.md:136-139`). This is the concrete
  mechanism R6's "same overlay" acceptance must certify for any *new* tool.
- **Unknown-tool rejection** already structural before streaming
  (`runtime_engine_contract.md:232`; `docs/SPEC.md:730-736`).
- **Tests.** Descriptor ordering/permissions/runtime/mode invariants
  (`__tests__/lib/tool-descriptor.test.ts`), unknown-tool rejection, server-attach-only,
  mutating-tool gating (`__tests__/lib/chirality-mutating-mcp.test.ts`).

## 3. Gaps R6 Closes

| # | Gap | Evidence | Class |
|---:|---|---|---|
| G1 | **No registry-wide collision/uniqueness invariant.** `createDescriptorLookup` (`tool-descriptor.ts:855-868`) does `Map.set` with no duplicate guard — a colliding name/alias/`adapter.toolName` **silently overwrites**. No test asserts global uniqueness. | `tool-descriptor.ts:855-868`; grep `duplicate\|collision\|unique` over registry+tests = 0 hits | CODE (load-bearing) |
| G2 | **Built-in vs `mcp__chirality__*` disjointness only de-facto**, not enforced; nothing blocks a future built-in named `status_read` or an MCP alias shadowing `Read`. | tool-names.ts; tool-descriptor.ts | CODE |
| G3 | **Descriptor/handler drift.** Nothing asserts the live MCP `tool()` registration set equals the chirality-MCP descriptor set; `inputSchema` (JSON) and Zod schemas are duplicated and uncross-checked. | descriptors `:382-538` vs handlers `read-tools.ts:642-734` | CODE |
| G4 | **No tool-catalog doc.** Only the descriptor array and hard-coded test `.toEqual` lists enumerate tools; no human-readable catalog of descriptions/modes/write-scopes/hook-requirements. | confirmed absent in `frontend/docs`, `docs` | DOC |
| G5 | **No "how to add a governed tool" contributor doc.** A new tool silently touches ≥3 source files + 3 test lists; the K-MCP-1 wrapper requirement is undocumented for contributors. | read-tools.ts, tool-names.ts, tool-descriptor.ts | DOC |
| G6 | **Organization smell.** `read-tools.ts` (22KB) holds both read and mutating tools; no `write-tools.ts`; back-compat alias `createChiralityReadMcpServers` misnames its contents (`read-tools.ts:765-770`). | read-tools.ts | REFACTOR (light) |
| G7 | **`Agent` exposure is special-cased** outside the descriptor pool (`sdk-options-builder.ts:94-100` re-adds `Agent` when a bridge exists), so the descriptor runtime flag is not its sole gate. The catalog must document this exception. | sdk-options-builder.ts:94-100 | DOC |

## 4. Tranche Spine

| Tranche | Purpose | Primary scope | Minimum validation |
|---|---|---|---|
| `R6-01` Collision-Prevention Invariant | Make "tool collisions are prevented" a real, tested invariant (G1, G2, G3). | Add a fail-closed duplicate guard to `createDescriptorLookup` (throw on duplicate name/alias/`adapter.toolName`); add a module-load/test invariant asserting global uniqueness, built-in↔MCP-name disjointness, and that the live MCP `tool()` set equals the chirality-MCP descriptor set. | `npm run test` (new uniqueness/disjointness/parity tests), `npm run typecheck`. |
| `R6-02` Generated Tool Catalog | Author the tool catalog (G4) as a **regenerable** artifact so it cannot drift. | A small script that emits a catalog table (name, adapter name, surface, permissions, pathScope, idempotence, humanGate, hook requirements, exposed?) from `HARNESS_TOOL_DESCRIPTORS`; commit the generated `frontend/docs/harness/tool_catalog.md`; a test asserting the committed catalog matches the registry. Document the `mcp__chirality__*` naming convention + reserved `mcp__chirality__domain_*` future namespace. | `npm run test` (catalog-matches-registry test), `npm run typecheck`, governance gate for the doc. |
| `R6-03` Contributor Guide ("Adding a Governed Tool") | Document the safe path to add an in-process tool (G5, G7). | A doc (`frontend/docs/harness/adding_a_tool.md`) covering: the multi-file sequence; the built-in path (permission overlay + Pre/PostToolUse hooks) vs the in-process MCP path (per-handler fail-closed wrapper, since `canUseTool`/hooks don't auto-fire); the K-MCP-1 requirement; the `Agent` special case; how the collision invariant and catalog test gate a PR. | Governance gate (diff hygiene, path/link checks, no-runtime-change). |
| `R6-04` MCP Module Organization *(optional)* | Resolve the organization smell (G6). | Behavior-preserving split of `mcp/read-tools.ts` into read + mutating modules (e.g., `mcp/read-tools.ts` + `mcp/mutating-tools.ts`) and rename the misleading back-compat alias; no exposure or behavior change; tests unchanged green. | `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge` (confirm no exposure change). |
| `R6-05` Contract & Boundary Refresh + Closeout | Fold R6 outcomes into governance and close the program. | Add a "Tool Catalog, Naming, Collision Prevention, and Adding Tools" section to `runtime_engine_contract.md` (linking the catalog + contributor doc); re-affirm the out-of-scope fences (§7); advance affected `_STATUS.md`/decomposition notes; refresh coordination and close R6. | Governance gate; runtime commands skipped unless executable behavior changed. |

## 5. Tranche Detail

### R6-01 — Collision-Prevention Invariant (G1, G2, G3)

This is the one load-bearing **code** tranche; everything else is docs/organization. PLAN.md
R6 acceptance "tool collisions are prevented" is currently only half-met (unknown-tool
rejection exists; duplicate-descriptor collision does not).

- Harden `createDescriptorLookup` (`tool-descriptor.ts:855-868`) to **throw** on the first
  duplicate `name`, `alias`, or `adapter.claudeAgentSdk.toolName` instead of silently
  overwriting. Because the lookup is built at module load over a frozen registry, a
  collision becomes a deterministic startup/import failure (fail-closed).
- Add tests asserting: (a) every descriptor `name`/`alias`/`adapter.toolName` is globally
  unique; (b) the set of built-in adapter names and the set of `mcp__chirality__*` names
  are disjoint; (c) the live in-process MCP `tool()` registration set
  (`buildChiralityMcpTools`) equals the set of `chirality-mcp` descriptors — closing the
  descriptor/handler drift (G3).
- Optionally add a parity check that each chirality-MCP descriptor's `inputSchema` and the
  handler's Zod schema agree on required fields (lighter: assert field-name parity, not
  full schema equality). If full cross-validation is too costly, record it as deferred.

No new tool is exposed; no permission/path/network behavior changes. Acceptance: a
deliberately-duplicated descriptor fixture fails fast; all real tools remain green.

### R6-02 — Generated Tool Catalog (G4)

PLAN.md R6 target: "Tool catalog with descriptions, modes, write scopes, and hook
requirements" (`docs/PLAN.md:266`).

- Write a generator (script or test-fixture) that renders a catalog table from
  `HARNESS_TOOL_DESCRIPTORS`: columns name | adapter name | surface | permissions |
  pathScope | idempotence | concurrency | humanGate | hook requirements | exposed-to-model.
- Commit the generated `frontend/docs/harness/tool_catalog.md`; add a test that regenerates
  in-memory and asserts equality with the committed file (so the catalog cannot silently
  drift from the registry — the same anti-drift discipline as Section 9).
- In the catalog (or alongside), document the `mcp__chirality__*` naming convention and
  reserve `mcp__chirality__domain_*` for future governed domain-profile tools
  (`docs/TYPES.md:413`) — names only, no implementation.

Acceptance: the catalog enumerates all 18 descriptors with correct modes/scopes/hook
requirements and is regenerable; the parity test gates drift.

### R6-03 — Contributor Guide: "Adding a Governed Tool" (G5, G7)

PLAN.md R6 target: "Documentation for adding in-process tools without bypassing permissions
or hooks" (`docs/PLAN.md:269`).

`frontend/docs/harness/adding_a_tool.md` covering:

- The exact multi-file sequence (descriptor in `HARNESS_TOOL_DESCRIPTORS`; `tool-names.ts`
  union if MCP; handler in the MCP server builder; catalog regeneration; test `.toEqual`
  list updates).
- **Built-in tools** flow through descriptor → permission overlay (hard-deny precedence) →
  Pre/PostToolUse hooks → evidence.
- **In-process MCP tools** do NOT auto-invoke `canUseTool`/hooks, so each handler MUST use
  the fail-closed permission/evidence wrapper (cite the STAB-04 probe and K-MCP-1). A new
  MCP tool that skips the wrapper is a bypass and must be rejected in review.
- The `Agent` special case (`sdk-options-builder.ts:94-100`): exposure is gated by the
  subagent bridge, not the descriptor runtime flag alone.
- How the R6-01 collision invariant and the R6-02 catalog test enforce these rules in CI.

Acceptance: a contributor can add a governed read or mutating tool by following the doc;
the doc states the bypass-prevention rule explicitly.

### R6-04 — MCP Module Organization *(optional, behavior-preserving)* (G6)

Split `mcp/read-tools.ts` into read and mutating modules and rename the misleading
back-compat alias (`createChiralityReadMcpServers` → keep a thin deprecated re-export only
if other call sites need it). No exposure, schema, or behavior change. Run
`harness:validate:premerge` to confirm the tool surface is byte-for-byte unchanged. This
tranche is optional and may be deferred if churn outweighs the readability gain.

### R6-05 — Contract & Boundary Refresh + Closeout

- Add a "Tool Catalog, Naming, Collision Prevention, and Adding Tools" section to
  `frontend/docs/harness/runtime_engine_contract.md` linking the catalog and contributor
  guide, and stating the collision invariant.
- Re-affirm the §7 out-of-scope fences in the contract/governance docs (no new capability).
- Advance the relevant `_STATUS.md` / decomposition notes for DEL-06-02/06-03 where R6
  evidence supports it (forward-only, actor-authorized — no bulk edits).
- Refresh `_COORDINATION.md` / `NEXT_INSTANCE_PROMPT.md` / `_LATEST.md`; record R6 complete
  in `PLAN_COMPLETION_LOG.md`; stop and report that the next program is unselected.

## 6. Sequencing

`R6-01` (collision invariant — de-risks the whole surface) → `R6-02` (catalog, depends on a
stable registry) ∥ `R6-03` (contributor guide, depends on the invariant + wrapper rule
being defined) → `R6-04` (optional organization) → `R6-05` (refresh + closeout, last).
R6-01 and R6-02 may run back-to-back; R6-03 consumes both.

## 7. Boundaries — Explicit Out of Scope (human-gated)

R6 does **not** authorize, and these remain out of scope until a governed future amendment
(`docs/PLAN.md:444-457`; `docs/CONTRACT.md:88,123`; `docs/DIRECTIVE.md:225`;
`docs/SPEC.md:809`; `docs/TYPES.md:413`):

- remote MCP servers; plugin marketplace; remote execution;
- **broad tool search** (fenced "before local tool governance is mature" — maturing that
  governance is R6's purpose, but *lifting* the fence is a separate future ruling, not part
  of R6);
- `mcp__chirality__domain_*` domain tools (gated on the R7 domain-profile amendment);
- shipped `bypassPermissions` ordinary workflow; concrete non-Anthropic providers;
- any change to the professional/reliance boundary (`CONTRACT.md` K-AUTH-1, K-PROF-1).

## 8. Required Human Rulings

R6's catalog, collision-invariant, contributor-doc, and organization work formalize
**already-approved** local/in-process governance and need **no new ruling** beyond program
acceptance. The only governance decision is minor and bounded:

- **R6 deliverable binding (recommended: no amendment).** No numbered deliverable currently
  binds the R6 *documentation* targets; SOW-064 and DEL-06-02/06-03 cover the substrate.
  Recommendation: track R6-01 (collision invariant) under **DEL-06-02** (tool validation)
  and treat the catalog/contributor docs as governance artifacts under PLAN.md §R6 +
  SOW-064, **without** a decomposition amendment. Alternative (if you want it formally
  tracked): bind a new `DEL-06-07` "Tool Catalog and Extension-Boundary Documentation" via
  a minor decomposition amendment. This is a `WORKING_ITEMS`/human call at acceptance, not a
  blocker.

A new ruling is required only if a tranche proposes crossing a §7 fence — which R6 does not.

## 9. Validation Policy

From `frontend/`:

```bash
npm run test        # R6-01 uniqueness/disjointness/parity; R6-02 catalog-matches-registry
npm run typecheck
```

Add for tranches that touch the MCP server build or could affect exposure (R6-04):

```bash
npm run harness:validate:premerge   # confirm the tool surface is unchanged
```

Governance/doc-only tranches (R6-03, R6-05) use static checks (diff hygiene, path/link
existence, explicit no-runtime-change confirmation) and record skipped runtime checks.
`proof:network-policy` and packaging are **not** in scope for R6.

## 10. Acceptance Criteria (from `docs/PLAN.md` §R6)

R6 is complete when:

- new MCP tools pass through the same permission and hook overlay as SDK built-ins
  (K-MCP-1), documented and enforced by the contributor guide + the R6-01 invariant;
- tool collisions are prevented (fail-closed duplicate guard + tests; unknown-tool
  rejection preserved);
- a regenerable tool catalog documents descriptions, modes, write scopes, and hook
  requirements;
- the `mcp__chirality__*` naming convention is documented and `mcp__chirality__domain_*`
  reserved for the future amendment;
- remote MCP and plugin marketplace remain out of scope;
- the cross-cutting "MCP tool contracts" validation category holds (`docs/PLAN.md:341`).

## 11. Evidence Basis

Scoped from a focused read-only research pass (two parallel analysts over the live tree +
retrieval DB, 2026-06-17). Load-bearing facts: the descriptor registry is a single frozen
array with rich metadata but **no duplicate guard**; the `mcp__chirality__*` convention and
allow-set helper exist but no registry-wide collision test; no tool-catalog or
"adding-a-tool" doc exists; in-process MCP calls do not auto-invoke `canUseTool`/hooks
(per the STAB-04 probe), making the per-handler fail-closed wrapper the K-MCP-1 enforcement
point. No source changes were made while scoping this plan.

## 12. Finalization Rule

This plan is the active development queue as of its acceptance ruling (`D-APP-14`);
`_COORDINATION.md`, `NEXT_INSTANCE_PROMPT.md`, and `_LATEST.md` are re-pointed to it. Per
§8, R6-01 is tracked under DEL-06-02 and the docs as governance artifacts (no decomposition
amendment). When all tranches land (or the human selects a replacement program), update the
coordination surfaces to the next active queue, move landed narrative to
`plans/PLAN_COMPLETION_LOG.md`, and mark this plan closed/non-governing. Human acceptance
remains required for every gate inside it, and every §7 fence stays human-gated.
