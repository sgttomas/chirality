# HELPS-CHECKLIST Launch Brief — v1

Role: `HELPS_HUMANS` (Agent 1)
Objective: implement the owner-directed governance correction for deterministic
candidate checklist derivation and REVIEW consumption.
Basis: owner direction in `amendments/RUN/v3.md`; D-GOV-15; frozen candidate
implementation at `main@2770fda4c...`; completed pilot commits.
Writes on `codex/sow-stage1-execution`: registered deterministic checklist
tool and tests under `tools/scope_of_work/`; applicable tool registries and
scope-of-work skill QA/policy; candidate standard; `AGENT_REVIEW.md`; an
append-only D-GOV-15 addendum and register summary. Root run evidence may also
be updated. No project/pilot path is writable.
Required behavior: take a validated `ScopeOfWork.md`, emit a stable structured
checklist directly from defined `AC-*` in source order with candidate/source
hash, AC text/source identity, and linked `VER-*` or explicit human-review
method; identical input yields byte-identical output; invalid/ambiguous input
fails closed unless the exact D-GOV-15 variance is supplied. REVIEW consumes
this artifact and does not mint, paraphrase, reorder, or silently omit `AC-*`.
Semantic additions remain human-gated review work.
Checks: unit positive/negative/determinism tests, ten-pilot reproduction,
applicable agent/skill/registry/root suites. Return hashes, results, blockers,
and reruns.
Denied: `docs/TYPES.md`, `docs/SPEC.md`, project loops/content, candidates,
statuses, lifecycle, Stage 2, corpus conversion, push/PR/merge.
