# SCA-APP-001 Propagation Plan

**Package Role:** snapshot / handoff artifact
**Gate:** 4 - Propagation Plan Approval
**Status:** PREVIEW_PENDING_HUMAN_APPROVAL

This plan is limited to governance, decomposition, coordination, planning, and runtime-contract documentation. It excludes runtime source, package manifests, dependencies, lockfiles, coding-language migrations, desktop wrapper changes, Pi imports, Pi adapter work, and concrete non-Anthropic provider implementation.

## Approved-After-Human-Acceptance Write Scope

| Surface | Gate 5 action |
|---|---|
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Apply approved semantic amendments; preserve IDs and topology. |
| `execution/_ScopeChange/SCA-APP-001_2026-06-13_1819_Provider-General_Runtime_Pi_Pattern-Corpus_v2/` | Update RUN_SUMMARY/Handoff/Post_Change_Coverage after Gate 5. |
| `execution/_Coordination/_DECISIONS/_REGISTER.md` | Set D-APP-01/02/03 to RULED and point to ruling records. |
| `execution/_Coordination/_DECISIONS/D-APP-*_RULING_2026-06-13.md` | Create ruling records from the human rulings and SCA approval. |
| `docs/PRD.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md` | Apply provider-general, Pi pattern-corpus, and capability-policy amendments. |
| `execution/_Coordination/_COORDINATION.md`, `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` | Align active agentic-development loop to approved strategy. |
| `plans/PLAN_2026-06-13_runtime_completion.md` | Update active queue and decision mirror. |
| `plans/PLAN_COMPLETION_LOG.md` | Add closeout entry only after Gate 5 lands. |
| `frontend/docs/harness/runtime_engine_contract.md` | Align runtime adapter contract docs. |
| `plans/pi-agent-harness-assessment.md`, `plans/pi-assessment/*.md`, `plans/claude-agent-sdk-implementation-followups.md` | Mark Pi as pattern corpus only and Claude SDK work as first-adapter work. |
| Affected `execution/PKG-*/1_Working/DEL-*/_CONTEXT.md` files listed in `Execution_Deliverable_Impact.csv` | Align deliverable-local context with the accepted amendment, or record row-level blockers in `Handoff_State.md`. |

## Explicit No-Write Scope

| Surface | Reason |
|---|---|
| `frontend/src/**` | Runtime implementation is out of scope. |
| `package.json`, package manifests, lockfiles | No dependency/runtime-floor/wrapper migration authorized. |
| desktop wrapper files | No application wrapper migration authorized. |
| Pi package import paths | D-APP-01 and D-APP-02 prohibit import/fork/adapter/spike work. |
| concrete non-Anthropic provider code | D-APP-03 approves strategy only; implementation requires future bounded tranche. |
| broad rewrites of deliverable-local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md` | These may be stale after Gate 5, but should be refreshed through bounded package-local follow-up tranches unless exact edits are separately approved. |

## Gate 5 Steps

1. Apply decomposition text amendments exactly as approved in `Amendment_Preview.md`.
2. Create D-APP ruling records and update `_DECISIONS/_REGISTER.md`.
3. Update `docs/PRD.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, and `docs/PLAN.md`.
4. Update active coordination and completion-plan surfaces.
5. Update runtime contract docs and Pi/SDK reference plans.
6. Update affected execution deliverable `_CONTEXT.md` files listed in `Execution_Deliverable_Impact.csv`, or record explicit blockers for deferred rows.
7. Update this SCA snapshot:
   - `Post_Change_Coverage.json`
   - `Decision_Log.md`
   - `Handoff_State.md`
   - `RUN_SUMMARY.md`
8. Run static validation.
9. Stage, commit, and push the validated Gate 5 tranche.

## Downstream Rerun Advisory

| Downstream owner | Required after Gate 5? | Notes |
|---|---|---|
| Dependency extraction / SCC graph | Advisory | Topology does not change, but provider-general semantics may alter future tranche selection. No immediate dependency CSV rewrite is required by this SCA. |
| REVIEW / governance audit | Advisory | Recommended after docs/decomposition alignment if release claims are later considered. |
| Package-local deliverable refresh | Required follow-up | Review affected deliverable `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md` after Gate 5 context alignment. Do not treat these local files as current if the SCA handoff marks them stale. |
| Runtime tests | Not required by this SCA | No source code changes are authorized. |
| Frontend test suite | Not required by this SCA | No frontend behavior changes are authorized. |
| Build/release checks | Not required by this SCA | No build/package changes are authorized. |

## Validation Plan

Run after Gate 5 edits:

```bash
git diff --check -- docs plans execution frontend/docs/harness
node -e "JSON.parse(require('fs').readFileSync('docs/MANIFEST.json','utf8'))"
rg "possible later.*Pi|Pi adapter|pi-ai|pi-agent-core|Node 22 sidecar|runtime floor.*Pi" docs plans execution frontend/docs/harness
rg "deny-first" docs plans execution frontend/docs/harness
rg "Claude Agent SDK is the preferred|Anthropic-only|possible later constrained backend-adapter spike" execution/PKG-01_* execution/PKG-04_* execution/PKG-06_* execution/PKG-09_* execution/PKG-10_*
git diff --name-only -- frontend/src package.json package-lock.json pnpm-lock.yaml yarn.lock desktop electron
```

Expected results:

- `git diff --check` passes.
- `docs/MANIFEST.json` parses if changed.
- Pi adapter/import/spike language is absent from active instruction/planning docs, except historical references explicitly marked superseded or prohibited.
- Any remaining `deny-first` wording is either historical or explicitly means hard-deny precedence, not blanket tool suppression.
- Affected execution deliverable context either reflects the accepted amendment or is explicitly listed as a blocker/deferred stale surface.
- No source/package/runtime-wrapper files are modified.

## Closure Criteria

Gate 5 can close only when:

- the decomposition document contains the SCA decision entry;
- D-APP-01/02/03 ruling records exist and the register rows are RULED;
- active coordination and completion plan no longer select Pi adapter/spike work;
- active strategy says provider-adapter generality is approved, while concrete new providers remain future bounded implementation items;
- affected execution deliverable `_CONTEXT.md` files are aligned or explicitly blocked/deferred in the SCA handoff;
- deliverable-local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, dependency, and reference artifacts are either confirmed current or listed as `STALE_LOCAL_REVIEW_REQUIRED`;
- the SCA handoff state records changed surfaces, stale/deferred surfaces, validation, and next recommended runtime tranche;
- no runtime source, package manifests, dependencies, lockfiles, or desktop wrapper files are modified.
