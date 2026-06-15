# Monorepo Root: Path-Anchoring Convention and Root Governance Restoration

Date: 2026-06-15

Repository root: `/Users/ryan/ai-env/projects/chirality`

Package role: planning artifact / decision record. Advisory; does not supersede governed authority documents, accepted snapshots, or handoff states. Authored from a maintainer discussion plus a `RESEARCH`-agent discovery pass over the accepted Chirality self-domain decomposition (`domains/chirality/_Decomposition/`, Gate 6 accepted) and the live instruction surface.

## Problem

Two coupled, repo-wide maintainer issues surfaced while setting up per-project/per-domain isolation:

1. **Worktree isolation breaks.** Agent instructions and handoff files hard-code machine-absolute paths anchored at the *main* checkout, so an agent launched in a git worktree writes back to main instead of the worktree. Switching to bare CWD-relative paths trades that for ambiguity, because many artifact names recur across scopes (`NEXT_INSTANCE_PROMPT.md`, `_COORDINATION.md`, `AGENTS.md`, `init-prompt.md`, `README.md`).

2. **The monorepo-root governance layer is hollowed out.** The canonical documents the README orientation path and the shared agents reference — `docs/DIRECTIVE.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/CONTRACT.md`, `docs/PLAN.md` — **do not exist at root**. They live only under `projects/*/docs/` and `.archive/`. An accepted `AUDIT_GOVERNANCE` atom still verifies agent `WRITE_SCOPE` against `SPEC.md §1.2` (the tool-root registry), which is absent at root.

## Findings (evidence)

- **The `{*_ROOT}` token convention already dominates the instruction surface** — ~30 distinct tokens, led by `{EXECUTION_ROOT}`, `{COORDINATION_ROOT}`, `{REPO_ROOT}`, `{WORKING_ROOT}`. Agent bodies already prohibit embedded absolutes (`agents/AGENT_RESEARCH.md:40`; accepted atom `HBA-AG001-00015` for AGGREGATION). This is not a convention to invent; it is the de-facto standard, lacking only a worktree-correct anchor.
- **Git worktrees already exist as a documented model.** `agents/AGENT_CHANGE.md:60` — "Disjoint write scopes are the default concurrency control … Do not introduce separate worktrees merely because work is concurrent." `:61` — "Worktrees are explicit isolation lanes" for "overlapping write scopes, **concurrent root governance edits**, risky refactors." Lane machinery at `:100` (`WORKTREE_ROOT` = sibling of repo root), `:278-290` (`git worktree add ../chirality-domain-kty -b codex/domain-kty main`). `AGENT_ORCHESTRATOR.md` validators already assume worktree isolation. The maintainer's "procedural worktree via convention" *is* the documented default.
- **Breakage mechanism = the ScopePath contract + launcher seam.** `agents/AGENT_TASK.md`: `ScopePath` must resolve to an existing local path (`:151`), run records always write to `{ScopePath}/_run_records/` (`:232`), `ScopePath` is stored as a normalized absolute path (`:371`), and nothing checks it is under the current checkout. The launcher (`init/init-prompt.md`) and per-scope `NEXT_INSTANCE_PROMPT.md` / `_COORDINATION.md` hard-code the main absolute path. `AGENT_CHANGE.md`'s lane plan (`:278-285`) records a `WORKTREE_PATH` and repo-relative `SCOPE_PATHS` but never re-anchors the worker's `ScopePath` into the lane.
- **Root governance docs absent.** `docs/{SPEC,DIRECTIVE,CONTRACT,TYPES,PLAN}.md` are absent at root (root `docs/` holds only `CYCLE_DRIVEN_RESOLUTION.md` + `rubrics/`, `templates/`, `thesis/`). The canonical copies live at `projects/chirality-app-dev/docs/`, `projects/chirality-piping/docs/`, and `.archive/`. `README.md:37-41,107,121,219` still reference the root `docs/*` paths → stale links.
- **The monorepo was assembled by merging four sibling repos** (`.archive/migration/path_map.yaml`); a prior path-rewrite pass already ran (`.archive/migration/rewrite_paths.py`, 18,010-row audit). Residual `/Users/ryan` paths are concentrated in generated provenance (`domains/*/_Sources/*_pdf2md_work/`, `_Decomposition/source_*`) and run records — not the `AGENT_*.md` bodies.

## Recommendation — path anchoring

Do not choose absolute-vs-relative, and do not choose git-vs-procedural. Both halves are already partly built. Keep the procedural-worktree (disjoint write scopes) default; make it deterministic and worktree-safe with a derived root plus one containment guard.

1. **Derive the anchor, never bake it.** Resolve `REPO_ROOT = git rev-parse --show-toplevel` at the launcher (returns the *worktree's* root in a worktree). All roots (`WORKING_ROOT`, `EXECUTION_ROOT`, `COORDINATION_ROOT`, `ScopePath`) derive from it.
2. **ScopePath-containment guard (highest-leverage change).** In `AGENT_TASK.md` normalization: the resolved `ScopePath` MUST be under `git rev-parse --show-toplevel`; otherwise STOP `SCOPE_OUTSIDE_WORKTREE`. No-op in shared-monorepo mode; in worktree mode it is the deterministic backstop that would have caught the original bug. Converts the convention into an enforced invariant without requiring worktrees.
3. **Fix the launcher seams** to `${REPO_ROOT}/<subpath>` (derived), never `/Users/...`: `init/init-prompt.md` and the per-scope coordination/handoff files.
4. **Close the CHANGE lane gap:** the Worktree Lane Plan should state the worker `ScopePath` as `{WORKTREE_PATH}/{SCOPE_SUBPATH}`.
5. **Two-anchor path rule for the instruction surface:** `{REPO_ROOT}`-relative for the shared instruction surface (`agents/`, `skills/`, `tools/`, `AGENTS.md`); `{WORKING_ROOT}`-relative for per-project governance/scope (`docs/`, `_Coordination/`, `execution/`). Absolute paths are permitted only in run records / evidence (provenance), never re-executed.
6. **Enforcement:** a deterministic validator (pre-commit / `harness-premerge.yml`) that fails on literal home-dir absolutes in the instruction/coordination/plan surface — generalizing the existing publish-time export sanitizer.

## Recommendation — root governance restoration

The path rule has no canonical home today because root `docs/` is hollowed out. Restore the monorepo-root canonical governance layer at the appropriate altitude: **root = the shared instruction surface / framework governance; projects and domains = working-roots that specialize it.** Author using `.archive/` (the prior root canon) and `projects/*/docs/` (working-root specializations) as guides, written for the root's role.

Canonical root doc set to author (the README orientation set, currently missing at root):

| Doc | Root-level role | Adds from this plan |
|---|---|---|
| `docs/DIRECTIVE.md` | Founding intent, four pillars, human authority, instruction-root vs working-root split (§2.6) | Make the instruction/working-root split explicit and root-canonical |
| `docs/SPEC.md` | Physical filesystem structures, package/deliverable layouts, tool roots (§1.2 registry), agent-instruction structure | The path-anchoring convention (`REPO_ROOT`/`WORKING_ROOT` split + `ScopePath` containment) |
| `docs/TYPES.md` | Canonical vocabulary, stable IDs, enums, agent roles, lifecycle states | A `{*_ROOT}` token registry |
| `docs/CONTRACT.md` | The K-* invariants | A path-anchoring / `ScopePath`-containment invariant |
| `docs/PLAN.md` | Root roadmap (maintainer-owned) | Skeleton only; human fills priorities |

Design-basis docs (`DBM_Agent_Instruction_Architecture.md`, `SE_Design_Analysis.md`) are referenced by `AGENTS.md`; equivalent depth already lives in `docs/thesis/`. Out of scope for the first authoring pass — flagged.

After authoring: reconcile README orientation/prose references (`README.md:37-41,107,121,219`) to the restored root docs — this also completes the earlier incomplete README drift fix.

## Open issues / caveats

- These are binding governance documents. Per `CONTRACT` invariant I1 (human-validated), author them as **drafts pending human ratification**, not accepted truth.
- Confirm whether the root-`docs/` hollowing was intentional (governance deliberately per-project) or merge drift. This plan assumes restoration at root is wanted, per maintainer direction.
- Cross-check the exact prior wording of `DIRECTIVE.md §2.6` and `SPEC.md §1.2` against the archived and per-project versions during authoring; do not invent invariants or tool roots.
