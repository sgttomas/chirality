# RECONCILE_CONTEXT_TEMPLATE_VS_SKILL_NAMING (Tooling Tracker)

**Date:** 2026-05-02 (Session 4)
**Status:** OPEN_TRACKER — operational status `RESOLVED-IN-PRACTICE` (no runtime risk); documentation/tooling housekeeping only.
**Owner:** tooling/skill maintainers (not the piping-design domain workspace).
**Filed by:** ORCHESTRATOR while executing `.Archive/PIPING_DESIGN_ITEMS_7_8_FOLLOWUP_PLAN.md` Item D (archived/completed Session 4 driver).

## Problem statement

Two artifacts in the piping-design workspace describe two different KA filename conventions:

- **`_CONTEXT.md` "Anticipated Artifacts" sections** in some KTY folders list filenames in the `KA-SUB-NN-NN-NN_{Slug}.md` form (e.g., `KTY-01-02/_CONTEXT.md` lines 13-15 list `KA-SUB-01-02-01_Codes-and-Standards.md` and `KA-SUB-01-02-02_Client-and-Project-Data.md`).
- **The `domain-documents` SKILL default** is `PREFIXED_TYPED_SLUG → KA-01_{Type}__{Slug}.md` (`skills/domain-documents/SKILL.md` line 78; `skills/domain-documents/BRIEF_SCHEMA.md` line 119).

The on-disk reality is mixed:

- **39 of 42 KTYs** carry `KA-NN_{Type}__{Slug}.md` files (e.g., `KTY-01-02/KA-01_Reference__Codes-and-Standards.md`) — the SKILL default.
- **3 of 42 KTYs** (KTY-01-03, KTY-08-03, KTY-10-02) carry `KA-SUB-NN-NN-NN_{Slug}.md` files — each with a documented Decision_Log entry per `_Coordination/_COORDINATION.md` § AOP-03 (line 90).

The `_CONTEXT.md` "Anticipated Artifacts" entries appear to have been authored against an earlier assumption (KA-SUB- form) and were never refreshed when `domain-documents` produced the actual files in either form. Note that the `_CONTEXT.md` schema in `agents/AGENT_PREPARATION.md` (lines 364, 388) does **not** hard-code either form — it renders `## Anticipated Artifacts` as `- [List from decomposition; may be empty]`. The KA-SUB- filenames in some `_CONTEXT.md` files therefore reflect authoring choices, not template-generator output.

## Operational status (from Item 8 audit, 2026-05-02)

**`RESOLVED-IN-PRACTICE`** — see `_Coordination/ITEM8_KA_FORM_AUDIT_2026-05-02.md` for full evidence.

The `dependency-extract` skill discovers source documents in a form-agnostic way:

- `SOURCE_DOCS: AUTO` (default) scans the deliverable folder for candidate source documents (`skills/dependency-extract/SKILL.md` line 46) — no naming-pattern filter.
- `DOC_ROLE_MAP: DEFAULT` does keyword-substring filename matching (datasheet, scope, spec, procedure, method, plan, workflow, guidance, runbook — `SKILL.md` lines 50-51) — no `KA-` prefix opinion.
- A search for `KA-`, `KA_`, `KA-SUB`, or `KA-NN` substrings across `skills/dependency-extract/{SKILL.md, BRIEF_SCHEMA.md, QA_CHECKS.md, TOOL_POLICY.md}` returns zero matches.

On-disk evidence in two production `Dependencies.csv` files (one from each naming camp) confirms the runtime correctly cites the actual filenames present — `KTY-01-02/Dependencies.csv` cites `KA-01_Reference__Codes-and-Standards.md` (the on-disk form, not the `KA-SUB-` form claimed by its `_CONTEXT.md`); `KTY-08-03/Dependencies.csv` cites `KA-SUB-08-03-01_Structural-Vibration.md`.

**AOP-03's runtime requirement** ("every consuming skill must accept both forms via `KA-*.md`") is therefore satisfied operationally for `dependency-extract`. Other consuming skills (`semantic-matrix-build`, `equipment-extract`, `equipment-costing-extract`, `kty-metadata-align`, `dbm-section-publish`, `domain-documents`) explicitly reference the `KA-*.md` glob in their specs (verified by grep), so they too satisfy AOP-03.

**Affected KTYs (KA-SUB camp):** KTY-01-03, KTY-08-03, KTY-10-02 (per `_COORDINATION.md` line 90).

## Three resolution paths (verbatim from predecessor plan, Item 8)

- **(a)** Update `_CONTEXT.md` template generator (and update the existing 3 KTY `_CONTEXT.md` files in the KA-SUB camp + any of the 39 PREFIXED_TYPED_SLUG-camp KTYs whose `_CONTEXT.md` was authored against the wrong assumption) to match the SKILL default `KA-NN_{Type}__{Slug}.md`.
- **(b)** Update the `domain-documents` SKILL default to match the `_CONTEXT.md` template's KA-SUB form (`KA-SUB-NN-NN-NN_*.md`). This is the most disruptive option because it would break 39 of 42 already-accepted Pass-3 deliverables.
- **(c)** Accept both forms permanently and codify the choice explicitly in both places (the `_CONTEXT.md` schema in `agents/AGENT_PREPARATION.md` and the `domain-documents` `ARTIFACT_NAMING` enum). This matches the AOP-03 runtime stance already in effect; lowest disruption.

## Recommendation

**Path (c) — codify "both forms accepted" in both the `_CONTEXT.md` schema and the `domain-documents` `ARTIFACT_NAMING` enum.** Rationale:

1. AOP-03 already accepts both forms operationally; codifying it removes the divergence without churning content.
2. Every consuming skill (`dependency-extract`, `semantic-matrix-build`, `equipment-extract`, `equipment-costing-extract`, `kty-metadata-align`, `dbm-section-publish`, `domain-documents`) already accepts `KA-*.md` glob, so no consuming-skill changes are needed.
3. Avoids touching 39 already-accepted Pass-3 deliverables (path (b)) and avoids a per-KTY refresh wave on `_CONTEXT.md` files (path (a)).
4. The 3 KTY-SUB-form KTYs already have documented Decision_Log entries justifying their override — this is captured intent, not drift.
5. A small follow-up under path (c): the template `_CONTEXT.md` "Anticipated Artifacts" entries that currently mismatch on-disk reality (e.g., `KTY-01-02/_CONTEXT.md` claiming `KA-SUB-` filenames that don't exist) can be refreshed lazily in a separate housekeeping pass — they are stale authoring artifacts, not template-generator bugs.

If path (c) is rejected, path (a) is the next-best option (smaller blast radius than (b) — only `_CONTEXT.md` files and the template-generator, no Pass-3 churn). Path (b) should be rejected unless there is a specific authoring or downstream reason to prefer the KA-SUB- form globally.

## Out-of-workspace boundary note

This tracker remains in the piping-design workspace's `plans/` directory **for discoverability**. Its predecessor plan is archived/completed at `.Archive/PIPING_DESIGN_CROSS_CUTTING_REMEDIATION_PLAN.md`; this tracker is **owned by tooling/skill maintainers**. Resolution actions belong to:

- **`agents/AGENT_PREPARATION.md`** — `_CONTEXT.md` schema (lines 364, 388 + the surrounding KTY-variant block).
- **`skills/domain-documents/SKILL.md`** — `ARTIFACT_NAMING` enum and the `PREFIXED_TYPED_SLUG` value definition.
- **`skills/domain-documents/BRIEF_SCHEMA.md`** — corresponding `RuntimeOverrides.ARTIFACT_NAMING` row.

**Resolution must NOT touch** the piping-design `_Decomposition/`, `_Sources/`, or any per-KTY content under `CAT-*/1_Working/<KTY>/`. The 42 KTY `Dependencies.csv` files, `_DEPENDENCIES.md` files, `Scoping.md` files, and `KA-*.md` files remain at the lifecycle states recorded in `_Coordination/NEXT_INSTANCE_STATE.md`.

## Cross-references

- **Authority overlay:** `_Coordination/_COORDINATION.md` § AOP-03 (lines 87-97) — references this tracker by name (`RECONCILE_CONTEXT_TEMPLATE_VS_SKILL_NAMING`).
- **Operational audit:** `_Coordination/ITEM8_KA_FORM_AUDIT_2026-05-02.md` — RESOLVED-IN-PRACTICE conclusion + cited evidence.
- **Plan that filed this tracker:** `.Archive/PIPING_DESIGN_ITEMS_7_8_FOLLOWUP_PLAN.md` (archived/completed; Item D).
- **Predecessor plan that flagged the divergence:** `.Archive/PIPING_DESIGN_CROSS_CUTTING_REMEDIATION_PLAN.md` (archived/completed; Item 8 filed this still-open tooling tracker).
- **Trigger watch that depends on this tracker's status:** `_Coordination/NEXT_INSTANCE_STATE.md` § Item 7 — Trigger Watch (Active) — embeds the `RESOLVED-IN-PRACTICE` outcome, so Item 7 (c) may proceed without halting on Item 8.
